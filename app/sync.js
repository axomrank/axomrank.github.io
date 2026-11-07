/* =========================================================
   Account sign-in, progress sync and Community (Firebase Auth + Firestore).
   Loaded only when AXOM_CONFIG.firebase is set. Without it the app
   works fully offline with progress saved on the device.
   Data (see firestore.rules):
     users/{uid}                 the learner's private progress (common.js snapshot())
     profiles/{uid}              the public Community card: name, photo, level, XP, streak, weekly XP
     rooms/{room}/msgs/{id}      group chat rooms
     dms/{a_b}, dms/{a_b}/msgs   direct messages between two learners (uids sorted, joined by "_")
     reports/{id}                messages reported to the moderators (write-only)
   ========================================================= */
const V = "10.12.2";
const { initializeApp } = await import(`https://www.gstatic.com/firebasejs/${V}/firebase-app.js`);
const { getAuth, onAuthStateChanged, GoogleAuthProvider, signInWithPopup, signInWithRedirect, getRedirectResult, signOut } = await import(`https://www.gstatic.com/firebasejs/${V}/firebase-auth.js`);
const { getFirestore, doc, getDoc, setDoc, deleteDoc, addDoc, collection, query, where, orderBy, limit, onSnapshot, serverTimestamp } = await import(`https://www.gstatic.com/firebasejs/${V}/firebase-firestore.js`);

export function start({ CFG, auth, snapshot, merge, applySnapshot, listeners, G, levelOf, iso }) {
  const app = initializeApp(CFG.firebase);
  const fbAuth = getAuth(app);
  const db = getFirestore(app);
  let timer = null, busy = false;

  /* ---------- the public Community card ---------- */
  const weekStart = () => { const d = new Date(); d.setDate(d.getDate() - ((d.getDay() + 6) % 7)); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };
  const weekXP = () => { const w = weekStart(); return Object.entries(G.days).filter(([k]) => k >= w).reduce((a, [, v]) => a + v, 0); };
  const nameOf = () => (G.game.nick || (auth.user && auth.user.name.split(" ")[0]) || "Learner").slice(0, 30);
  async function publishProfile() {
    if (!auth.user) return;
    const ref = doc(db, "profiles", auth.user.uid);
    if (G.game.hidden) { await deleteDoc(ref).catch(() => {}); return; }
    const ui = JSON.parse(localStorage.getItem("axom:ui") || "{}");
    await setDoc(ref, { name: nameOf(), photo: (auth.user.photo || "").slice(0, 500), xp: G.xp | 0, level: levelOf().n, streak: G.streak.n | 0,
      week: weekStart(), weekXp: weekXP() | 0, badges: Object.keys(G.game.badges).length, course: (ui.lastCourse || "").slice(0, 40), t: serverTimestamp() });
  }

  async function push() {
    if (!auth.user || busy) return;
    try { await setDoc(doc(db, "users", auth.user.uid), snapshot()); } catch (e) { console.warn("Sync push failed", e); }
    publishProfile().catch((e) => console.warn("Profile publish failed", e));
  }
  const pushSoon = () => { clearTimeout(timer); timer = setTimeout(push, 4000); };

  async function pull() {
    busy = true;
    try {
      const ref = doc(db, "users", auth.user.uid);
      const snap = await getDoc(ref);
      const merged = snap.exists() ? merge(snapshot(), snap.data()) : snapshot();
      applySnapshot(merged);
      await setDoc(ref, merged);
    } catch (e) { console.warn("Sync pull failed", e); }
    busy = false;
    publishProfile().catch((e) => console.warn("Profile publish failed", e));
  }

  /* ---------- Google sign-in ----------
     The popup is the reliable path: the redirect path loses its result in browsers that partition
     third-party storage, because authDomain (firebaseapp.com) differs from the site's own domain.
     So redirect is only a fallback when a popup cannot open at all. */
  auth.signIn = async () => {
    const provider = new GoogleAuthProvider();
    provider.setCustomParameters({ prompt: "select_account" });
    try { await signInWithPopup(fbAuth, provider); }
    catch (e) {
      if (e && ["auth/popup-blocked", "auth/operation-not-supported-in-this-environment"].includes(e.code)) return signInWithRedirect(fbAuth, provider);
      throw e;
    }
  };
  auth.signOut = () => signOut(fbAuth);
  getRedirectResult(fbAuth).catch((e) => { auth.lastError = e; auth.onError.forEach((f) => f(e)); });

  onAuthStateChanged(fbAuth, async (user) => {
    auth.user = user ? { uid: user.uid, name: user.displayName || "", photo: user.photoURL || "" } : null;
    if (user) await pull();
    auth.ready = true;
    auth.onChange.forEach((f) => f(auth.user));
  });

  listeners.push(pushSoon);
  document.addEventListener("visibilitychange", () => { if (document.hidden) push(); });

  /* ---------- Community ---------- */
  const me = () => auth.user && auth.user.uid;
  const pairOf = (a, b) => [a, b].sort().join("_");
  const clean = (text) => String(text || "").replace(/\s+/g, " ").trim().slice(0, 500);
  const rows = (snap) => snap.docs.map((d) => ({ id: d.id, ...d.data(), t: d.data().t ? d.data().t.toMillis() : Date.now() }));
  const noteMessage = () => { G.game.feats.msgs = (G.game.feats.msgs || 0) + 1; };
  auth.social = {
    publish: publishProfile,
    // learners active most recently first (the page sorts them into "online", leaderboards etc.)
    people(cb) { return onSnapshot(query(collection(db, "profiles"), orderBy("t", "desc"), limit(150)), (s) => cb(rows(s)), (e) => cb(null, e)); },
    room(id, cb) { return onSnapshot(query(collection(db, "rooms", id, "msgs"), orderBy("t", "desc"), limit(60)), (s) => cb(rows(s).reverse()), (e) => cb(null, e)); },
    async say(id, text) {
      text = clean(text); if (!text || !me()) return;
      await addDoc(collection(db, "rooms", id, "msgs"), { uid: me(), name: nameOf(), photo: (auth.user.photo || "").slice(0, 500), lv: levelOf().n, text, t: serverTimestamp() });
      noteMessage();
    },
    inbox(cb) { return onSnapshot(query(collection(db, "dms"), where("users", "array-contains", me())), (s) => cb(rows(s).sort((a, b) => b.t - a.t)), (e) => cb(null, e)); },
    dm(other, cb) { return onSnapshot(query(collection(db, "dms", pairOf(me(), other), "msgs"), orderBy("t", "desc"), limit(60)), (s) => cb(rows(s).reverse()), (e) => cb(null, e)); },
    async tell(other, otherName, otherPhoto, text) {
      text = clean(text); if (!text || !me() || other === me()) return;
      const pair = pairOf(me(), other);
      await addDoc(collection(db, "dms", pair, "msgs"), { uid: me(), text, t: serverTimestamp() });
      await setDoc(doc(db, "dms", pair), { users: pair.split("_"), names: { [me()]: nameOf(), [other]: String(otherName || "").slice(0, 30) },
        photos: { [me()]: (auth.user.photo || "").slice(0, 500), [other]: String(otherPhoto || "").slice(0, 500) }, last: text.slice(0, 120), from: me(), t: serverTimestamp() });
      noteMessage();
    },
    remove(path) { return deleteDoc(doc(db, ...path)); },
    report(msg, where_) { return addDoc(collection(db, "reports"), { by: me(), uid: String(msg.uid || ""), text: clean(msg.text), where: String(where_).slice(0, 80), t: serverTimestamp() }); },
    pairOf,
  };
}
