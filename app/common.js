/* =========================================================
   AxomRank shared core, used by the course home and the lesson player:
   bilingual text helpers, saved progress, streak, sound, media URLs,
   offline downloads and the merge rule used by account sync.
   ========================================================= */
(() => {
"use strict";
const CFG = window.AXOM_CONFIG || {};
const B = (en, as) => ({ en, as });
const AS_DIGITS = "০১২৩৪৫৬৭৮৯";
const asNum = (s) => String(s).replace(/\d/g, (d) => AS_DIGITS[d]);
const T = (o) => (o == null ? "" : typeof o === "string" ? o : `<span class="en">${o.en}</span><span class="as">${o.as}</span>`);
const N = (n) => (n && n.en ? T(n) : T(B(String(n), asNum(n))));

/* ---------- saved progress (localStorage; synced to the account when signed in) ---------- */
const store = {
  get(k, d) { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* storage blocked */ } },
};
const G = Object.assign({ xp: 0, streak: { n: 0, last: null }, sound: true, as: false, fs: 1, motion: true,
  mistakes: {}, srs: {}, days: {}, stats: {}, checkpoints: {}, skills: {}, miscon: {}, updated: 0 }, store.get("axom:global", {}));
const lessonKey = (id) => `axom:lesson:${id}`;
const getLesson = (id) => Object.assign({ done: {} }, store.get(lessonKey(id), {}));
const listeners = [];
function saveGlobal() { G.updated = Date.now(); store.set("axom:global", G); listeners.forEach((f) => f()); }
function saveLesson(id, P) { store.set(lessonKey(id), P); saveGlobal(); }

const dayKey = (d) => `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()}`;
const iso = (offset = 0) => { const d = new Date(Date.now() + offset * 864e5); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };

/* ---------- spaced repetition (rule-based): a step returns after 1, 3, 7, 15, 30 days ---------- */
const INTERVALS = [1, 3, 7, 15, 30];
function srsLearn(stepId, lessonId) { if (!G.srs[stepId]) G.srs[stepId] = { l: lessonId, s: 0, d: iso(1) }; }
function srsAnswer(stepId, lessonId, right) {
  const cur = G.srs[stepId] || { l: lessonId, s: 0 };
  const s = right ? Math.min(cur.s + 1, INTERVALS.length - 1) : 0;
  G.srs[stepId] = { l: lessonId, s, d: iso(right ? INTERVALS[s] : 1) };
}
function reviewQueue() {   // due steps + saved mistakes, as [{ l, id }]
  const today = iso(), seen = new Set(), out = [];
  Object.entries(G.srs).filter(([, v]) => v.d <= today).sort((a, b) => (a[1].d < b[1].d ? -1 : 1)).forEach(([id, v]) => { seen.add(id); out.push({ l: v.l, id }); });
  Object.entries(G.mistakes).forEach(([l, ids]) => ids.forEach((id) => { if (!seen.has(id)) { seen.add(id); out.push({ l, id }); } }));
  return out;
}
// A short, varied round from the existing queue. The underlying due dates and
// mistake records stay intact, so stopping after one round never drops work.
const REVIEW_ROUND_SIZE = 8;
function dailyReviewQueue(limit = REVIEW_ROUND_SIZE) {
  const queue = reviewQueue(), size = Math.max(0, Math.floor(limit));
  const mistakes = queue.filter(({ l, id }) => (G.mistakes[l] || []).includes(id));
  const selectedMistakes = mistakes.slice(0, 3);
  const selectedKeys = new Set(selectedMistakes.map(({ l, id }) => `${l}:${id}`));
  const ordered = [...selectedMistakes, ...queue.filter(({ l, id }) => !selectedKeys.has(`${l}:${id}`))];
  const round = [], counts = {};
  // First pass draws from different lessons; second pass fills a sparse round.
  for (const perLesson of [2, Infinity]) {
    for (const item of ordered) {
      if (round.length >= size) break;
      if (round.includes(item) || (counts[item.l] || 0) >= perLesson) continue;
      round.push(item); counts[item.l] = (counts[item.l] || 0) + 1;
    }
  }
  return round;
}
/* ---------- skill mastery (Bayesian knowledge tracing), separate from XP and from spaced review ----------
   skills[id] = { p: chance the skill is known, a: first attempts, o: correct first attempts, t: time of last answer,
                  g: date of last independent success, dr: delayed recalls, u: hints or help used }
   Only first attempts reach this model. A retry or a hinted answer never raises p, and "strong" needs a success
   at least DELAY_DAYS after an earlier one, so same-session practice cannot produce a delayed-mastery claim. */
const BKT = { init: 0.2, learn: 0.1, slip: 0.1, guess: 0.25, guessTyped: 0.12 };
const DELAY_DAYS = 3, RUSTY_DAYS = 21, READY_P = 0.85, WEAK_P = 0.5, READY_WINS = 3;
const daysBetween = (a, b) => Math.round((Date.parse(b) - Date.parse(a)) / 864e5);
function skillAnswer(id, right, { hinted = false, typed = false } = {}) {
  const r = (G.skills[id] = G.skills[id] || { p: BKT.init, a: 0, o: 0, t: 0, g: null, dr: 0, u: 0 });
  const guess = typed ? BKT.guessTyped : BKT.guess, now = iso();   // a typed answer is much harder to guess than a tapped one
  r.a++; r.t = Date.now();
  if (hinted) { r.u++; if (right) return r; }            // help used: a success teaches, but is not evidence of mastery
  if (right) {
    r.o++;
    const known = (r.p * (1 - BKT.slip)) / (r.p * (1 - BKT.slip) + (1 - r.p) * guess);
    r.p = known + (1 - known) * BKT.learn;
    if (r.g && daysBetween(r.g, now) >= DELAY_DAYS) r.dr = (r.dr || 0) + 1;
    r.g = now;
  } else {
    r.p = (r.p * BKT.slip) / (r.p * BKT.slip + (1 - r.p) * (1 - guess));
    r.dr = Math.max(0, (r.dr || 0) - 1);
  }
  r.p = Math.min(0.995, Math.max(0.01, +r.p.toFixed(4)));
  return r;
}
function misconception(tag) { const m = (G.miscon[tag] = G.miscon[tag] || { n: 0, t: 0 }); m.n++; m.t = Date.now(); }
// new (no evidence) · weak · learning · ready (high now, not yet tested after a delay) · strong (survived a delay) · rusty (strong or ready, long unused)
function skillState(id) {
  const r = G.skills[id];
  if (!r || !r.a) return "new";
  if (r.p < WEAK_P) return "weak";
  if (r.p < READY_P || r.o < READY_WINS) return "learning";
  if ((Date.now() - r.t) / 864e5 > RUSTY_DAYS) return "rusty";
  return r.dr > 0 ? "strong" : "ready";
}
// The deepest unmastered prerequisite behind a skill, so practice repairs the cause first. map: { id: { pre: [...] } }
function rootCause(id, map, seen = new Set()) {
  if (seen.has(id) || !map[id]) return null;
  seen.add(id);
  for (const pre of map[id].pre || []) {
    const deeper = rootCause(pre, map, seen);
    if (deeper) return deeper;
    if (["weak", "rusty"].includes(skillState(pre))) return pre;
  }
  return null;
}
function record(lessonId, right) { const st = (G.stats[lessonId] = G.stats[lessonId] || { a: 0, o: 0 }); st.a++; if (right) st.o++; }
function addDayXP(xp) { const k = iso(); G.days[k] = (G.days[k] || 0) + xp; }
// A streak freeze (earned every 7 days of streak, at most 2 in reserve) covers one missed day.
const dayBefore = () => dayKey(new Date(Date.now() - 2 * 864e5));
const streakNow = () => { const t = dayKey(new Date()), y = dayKey(new Date(Date.now() - 864e5)); return G.streak.last === t || G.streak.last === y || (G.streak.last === dayBefore() && (G.game || {}).freeze > 0) ? G.streak.n : 0; };
function bumpStreak() {
  const t = dayKey(new Date()), y = dayKey(new Date(Date.now() - 864e5));
  if (G.streak.last === t) return;
  let n = 1;
  if (G.streak.last === y) n = G.streak.n + 1;
  else if (G.streak.last === dayBefore() && G.game.freeze > 0) { G.game.freeze--; G.game.frozeOn = iso(); n = G.streak.n + 1; }
  G.streak = { n, last: t };
  if (n % 7 === 0) G.game.freeze = Math.min(2, (G.game.freeze || 0) + 1);
  G.game.best = Math.max(G.game.best || 0, n);
}

/* ---------- game layer: levels, badges, daily goal, streak freezes ----------
   G.game = { badges: { id: date earned }, feats: { units, perfect, reviews, early, late, msgs }, goal: daily XP goal,
              freeze: streak freezes in reserve (max 2), best: longest streak, hidden: not listed in Community,
              nick: Community name, block: { uid: true }, auto: open where I left off (default on) }
   Rewards measure effort and habit. They never touch first-attempt accuracy, skill mastery or spaced review. */
const GAME0 = () => ({ badges: {}, feats: {}, goal: 30, freeze: 0, best: 0, hidden: false, nick: "", block: {}, auto: true });
G.game = Object.assign(GAME0(), G.game || {});
G.game.best = Math.max(G.game.best || 0, G.streak.n || 0);
const LEVEL_XP = (n) => 25 * n * (n - 1);   // total XP that reaches level n: 0, 50, 150, 300, 500 …
function levelOf(xp = G.xp) {
  let n = 1; while (xp >= LEVEL_XP(n + 1)) n++;
  const from = LEVEL_XP(n), to = LEVEL_XP(n + 1);
  const rank = [[30, B("Legend", "কিংবদন্তি")], [20, B("Master", "পণ্ডিত")], [15, B("Expert", "পাৰ্গত")], [10, B("Scholar", "অধ্যয়নকাৰী")], [5, B("Explorer", "অন্বেষক")], [1, B("Beginner", "নতুন শিক্ষাৰ্থী")]].find(([min]) => n >= min)[1];
  return { n, from, to, pct: Math.round(((xp - from) / (to - from)) * 100), rank };
}
const todayXP = () => G.days[iso()] || 0;
const goalDays = () => Object.values(G.days).filter((x) => x >= (G.game.goal || 30)).length;
const lessonsFinished = () => Object.keys(localStorage).filter((k) => k.startsWith("axom:lesson:") && (store.get(k, {}).done || {}).test).length;
const feat = (k) => G.game.feats[k] || 0;
const BADGES = [
  ["first-unit", "🌱", B("First steps", "প্ৰথম খোজ"), B("Finish your first unit", "প্ৰথম অধ্যায় শেষ কৰা"), () => feat("units") >= 1],
  ["first-lesson", "📜", B("First lesson", "প্ৰথম পাঠ"), B("Pass a lesson test", "এটা পাঠৰ পৰীক্ষাত উত্তীৰ্ণ হোৱা"), () => lessonsFinished() >= 1],
  ["lessons-5", "📚", B("Bookworm", "কিতাপৰ পোক"), B("Finish 5 lessons", "৫টা পাঠ শেষ কৰা"), () => lessonsFinished() >= 5],
  ["lessons-25", "🏛️", B("Library keeper", "পুথিভঁৰালৰ ৰখীয়া"), B("Finish 25 lessons", "২৫টা পাঠ শেষ কৰা"), () => lessonsFinished() >= 25],
  ["lessons-100", "👑", B("Hundred lessons", "এশটা পাঠ"), B("Finish 100 lessons", "১০০টা পাঠ শেষ কৰা"), () => lessonsFinished() >= 100],
  ["streak-3", "🔥", B("On fire", "জ্বলি উঠিছা"), B("Keep a 3-day streak", "৩ দিনৰ ধাৰা ৰাখা"), () => G.game.best >= 3],
  ["streak-7", "⚡", B("One full week", "গোটেই এসপ্তাহ"), B("Keep a 7-day streak", "৭ দিনৰ ধাৰা ৰাখা"), () => G.game.best >= 7],
  ["streak-30", "🌟", B("Month of focus", "এমাহৰ মনোযোগ"), B("Keep a 30-day streak", "৩০ দিনৰ ধাৰা ৰাখা"), () => G.game.best >= 30],
  ["streak-100", "🏆", B("Unstoppable", "অপ্ৰতিৰোধ্য"), B("Keep a 100-day streak", "১০০ দিনৰ ধাৰা ৰাখা"), () => G.game.best >= 100],
  ["xp-100", "💎", B("100 XP", "১০০ XP"), B("Earn 100 XP", "১০০ XP অৰ্জন কৰা"), () => G.xp >= 100],
  ["xp-1000", "💠", B("1,000 XP", "১০০০ XP"), B("Earn 1,000 XP", "১০০০ XP অৰ্জন কৰা"), () => G.xp >= 1000],
  ["xp-5000", "🔷", B("5,000 XP", "৫০০০ XP"), B("Earn 5,000 XP", "৫০০০ XP অৰ্জন কৰা"), () => G.xp >= 5000],
  ["level-10", "🎓", B("Scholar", "অধ্যয়নকাৰী"), B("Reach level 10", "স্তৰ ১০ পোৱা"), () => levelOf().n >= 10],
  ["perfect-1", "🎯", B("Bullseye", "লক্ষ্যভেদ"), B("Get every question right first time in a unit", "এটা অধ্যায়ৰ সকলো প্ৰশ্ন প্ৰথম চেষ্টাতে শুদ্ধ"), () => feat("perfect") >= 1],
  ["perfect-10", "🏹", B("Sharpshooter", "নিখুঁত লক্ষ্য"), B("10 perfect units", "১০টা নিখুঁত অধ্যায়"), () => feat("perfect") >= 10],
  ["review-1", "🧠", B("Memory keeper", "স্মৃতিৰ ৰখীয়া"), B("Finish a daily memory mission", "এটা দৈনিক স্মৃতি অভিযান শেষ কৰা"), () => feat("reviews") >= 1],
  ["review-10", "🧩", B("Never forget", "কেতিয়াও নাপাহৰো"), B("Finish 10 memory missions", "১০টা স্মৃতি অভিযান শেষ কৰা"), () => feat("reviews") >= 10],
  ["checkpoint", "🏁", B("Checkpoint cleared", "পৰীক্ষা পাৰ"), B("Pass an era checkpoint", "এটা যুগৰ পৰীক্ষাত উত্তীৰ্ণ হোৱা"), () => Object.keys(G.checkpoints).some((k) => k !== "diagnostic" && G.checkpoints[k])],
  ["goal-7", "📅", B("Goal getter", "লক্ষ্য পূৰণকাৰী"), B("Meet your daily goal on 7 days", "৭ দিন দৈনিক লক্ষ্য পূৰণ কৰা"), () => goalDays() >= 7],
  ["early", "🌅", B("Early bird", "ৰাতিপুৱাৰ চৰাই"), B("Study before 7 am", "ৰাতিপুৱা ৭ বজাৰ আগতে পঢ়া"), () => feat("early") >= 1],
  ["late", "🦉", B("Night owl", "নিশাচৰ"), B("Study after 10 pm", "নিশা ১০ বজাৰ পিছত পঢ়া"), () => feat("late") >= 1],
  ["social", "💬", B("Study buddy", "পঢ়াৰ লগৰীয়া"), B("Send a message in Community", "সম্প্ৰদায়ত এটা বাৰ্তা পঠিওৱা"), () => feat("msgs") >= 1],
].map(([id, icon, t, d, test]) => ({ id, icon, t, d, test }));
// Award every badge whose condition now holds; returns the new ones so the caller can celebrate them.
function checkBadges() {
  const fresh = BADGES.filter((b) => !G.game.badges[b.id] && b.test());
  fresh.forEach((b) => (G.game.badges[b.id] = iso()));
  return fresh;
}
// Called by the lesson player when a unit or round ends (after XP is added). Returns what to celebrate.
function gameAfterUnit({ xp = 0, ok = 0, asked = 0, review = false } = {}) {
  const f = G.game.feats, before = levelOf(G.xp - xp).n, h = new Date().getHours(), goal = G.game.goal || 30;
  f.units = (f.units || 0) + 1;
  if (asked >= 3 && ok === asked) f.perfect = (f.perfect || 0) + 1;
  if (review) { f.reviews = (f.reviews || 0) + 1; G.game.reviewDay = iso(); }
  if (h < 7 && h >= 4) f.early = (f.early || 0) + 1;
  if (h >= 22) f.late = (f.late || 0) + 1;
  const after = levelOf();
  return { levelUp: after.n > before ? after : null, goalHit: todayXP() >= goal && todayXP() - xp < goal, badges: checkBadges() };
}

/* ---------- what to study now: one answer, so the learner never has to choose ----------
   1. A lesson already started  → its next unit.   2. Questions due for memory review → the memory mission (once a day).
   3. The next lesson of the course in use.        4. The next course with lessons left, in the subject order for the chosen exam. */
async function nextAction() {
  const [m, cat] = await Promise.all([getJSON("content/manifest.json"), getJSON("content/catalog.json")]);
  const ui = store.get("axom:ui", {});
  const unitsOf = (id) => (m.lessons[id] || {}).units || [];
  const startAt = (id) => { const P = getLesson(id), i = unitsOf(id).findIndex((u) => !(u.id === "test" ? P.done.test : P.done[u.id])); return Math.max(0, i); };
  const go = (id, kind) => { const L = m.lessons[id], i = startAt(id), u = unitsOf(id)[i]; return { kind, lesson: id, course: L.course, href: `lesson.html?id=${id}&start=${i}`, title: L.title, unit: u ? u.t : null, no: L.no, unitNo: i + 1, units: unitsOf(id).length }; };
  const started = (id) => m.lessons[id] && !getLesson(id).done.test && Object.keys(getLesson(id).done).length > 0;
  if (ui.lastLesson && started(ui.lastLesson)) return go(ui.lastLesson, "resume");
  const due = reviewQueue().length;
  if (due >= 3 && G.game.reviewDay !== iso()) return { kind: "review", href: "lesson.html?review=1", due, round: Math.min(due, REVIEW_ROUND_SIZE) };
  const live = new Set(m.courses.map((c) => c.id));
  const exam = ui.exam || "";
  const order = cat.subjects.filter((S) => !exam || (S.exams || []).includes(exam)).flatMap((S) => S.courses.filter((e) => live.has(e.course) && !e.optional).map((e) => e.course));
  const courses = [...new Set([ui.lastCourse, ...order].filter((c) => c && live.has(c)))];
  for (const cid of courses) {
    const ids = Object.entries(m.lessons).filter(([, L]) => L.course === cid).sort((a, b) => a[1].no - b[1].no).map(([id]) => id);
    const id = ids.find((x) => !getLesson(x).done.test);
    if (id) return go(id, started(id) ? "resume" : cid === ui.lastCourse ? "next" : "new-course");
  }
  return due ? { kind: "review", href: "lesson.html?review=1", due, round: Math.min(due, REVIEW_ROUND_SIZE) } : { kind: "done", href: "index.html?view=practice" };
}

/* ---------- account sync: one document per user ---------- */
// Shape of users/{uid}: { xp, streak, lessons: { id: { done: [...] } }, mistakes, srs, days, stats, checkpoints, updated }
function snapshot() {
  const lessons = {};
  Object.keys(localStorage).filter((k) => k.startsWith("axom:lesson:")).forEach((k) => { lessons[k.slice(12)] = { done: Object.keys(store.get(k, {}).done || {}) }; });
  const out = { xp: G.xp, streak: G.streak, lessons, mistakes: G.mistakes, srs: G.srs, days: G.days, stats: G.stats, checkpoints: G.checkpoints, game: G.game, updated: G.updated };
  // Sent only once used: the account rules must allow these two fields before a release that writes them.
  if (Object.keys(G.skills).length) out.skills = G.skills;
  if (Object.keys(G.miscon).length) out.miscon = G.miscon;
  return out;
}
// Merge rule: never lose progress. XP = higher, finished units = union of both,
// streak and mistakes = whichever side was updated more recently.
function merge(a, b) {
  const newer = (b.updated || 0) > (a.updated || 0) ? b : a;
  const lessons = {};
  new Set([...Object.keys(a.lessons || {}), ...Object.keys(b.lessons || {})]).forEach((id) => {
    lessons[id] = { done: [...new Set([...((a.lessons || {})[id] || {}).done || [], ...((b.lessons || {})[id] || {}).done || []])] };
  });
  const days = { ...(a.days || {}) };
  Object.entries(b.days || {}).forEach(([k, v]) => (days[k] = Math.max(days[k] || 0, v)));
  // skill records merge one by one: each device keeps whichever record was answered last
  const latest = (x = {}, y = {}) => { const o = { ...x }; Object.entries(y).forEach(([k, v]) => { if (!o[k] || (v.t || 0) > (o[k].t || 0)) o[k] = v; }); return o; };
  const skills = latest(a.skills, b.skills), miscon = latest(a.miscon, b.miscon);
  // game: badges and feats are never lost; settings follow the newer side
  const ga = a.game || {}, gb = b.game || {}, gn = newer === b ? gb : ga, feats = { ...(ga.feats || {}) };
  Object.entries(gb.feats || {}).forEach(([k, v]) => (feats[k] = Math.max(feats[k] || 0, v)));
  const game = { ...ga, ...gb, ...gn, badges: { ...(gb.badges || {}), ...(ga.badges || {}) }, feats, best: Math.max(ga.best || 0, gb.best || 0) };
  return { game, ...(Object.keys(skills).length ? { skills } : {}), ...(Object.keys(miscon).length ? { miscon } : {}), xp: Math.max(a.xp || 0, b.xp || 0), streak: newer.streak || { n: 0, last: null }, lessons, mistakes: newer.mistakes || {},
    srs: newer.srs || {}, days, stats: newer.stats || {}, checkpoints: { ...(a.checkpoints || {}), ...(b.checkpoints || {}) }, updated: Math.max(a.updated || 0, b.updated || 0) };
}
function applySnapshot(s) {
  G.xp = s.xp; G.streak = s.streak; G.mistakes = s.mistakes; G.updated = s.updated;
  G.srs = s.srs || {}; G.days = s.days || {}; G.stats = s.stats || {}; G.checkpoints = s.checkpoints || {}; G.skills = s.skills || {}; G.miscon = s.miscon || {}; G.game = Object.assign(GAME0(), s.game || {});
  store.set("axom:global", G);
  Object.entries(s.lessons).forEach(([id, v]) => { const P = getLesson(id); v.done.forEach((u) => (P.done[u] = true)); store.set(lessonKey(id), P); });
}

/* ---------- sound (gentle, optional; unlocked on first tap for phones) ---------- */
let ac = null;
function audio() {
  if (!ac) { try { ac = new (window.AudioContext || window.webkitAudioContext)(); } catch { return null; } }
  if (ac.state !== "running") ac.resume().catch(() => {});
  return ac;
}
function unlockAudio() {
  const c = audio(); if (!c) return;
  try { const b = c.createBuffer(1, 1, 22050), src = c.createBufferSource(); src.buffer = b; src.connect(c.destination); src.start(0); } catch { /* ignore */ }
  if (c.state === "running") ["pointerdown", "touchend", "keydown"].forEach((ev) => document.removeEventListener(ev, unlockAudio, true));
}
["pointerdown", "touchend", "keydown"].forEach((ev) => document.addEventListener(ev, unlockAudio, true));
document.addEventListener("visibilitychange", () => { if (!document.hidden && ac) ac.resume().catch(() => {}); });
function tone(freqs, type = "sine", dur = 0.14, gap = 0.09, vol = 0.2) {
  if (!G.sound) return;
  const c = audio(); if (!c) return;
  const play = () => {
    try {
      freqs.forEach((f, i) => {
        const o = c.createOscillator(), g = c.createGain(), st = c.currentTime + 0.01 + i * gap;
        o.type = type; o.frequency.value = f; g.gain.setValueAtTime(0.0001, st); g.gain.linearRampToValueAtTime(vol, st + 0.015);
        g.gain.exponentialRampToValueAtTime(0.0001, st + dur); o.connect(g).connect(c.destination); o.start(st); o.stop(st + dur + 0.03);
      });
    } catch { /* no audio */ }
  };
  if (c.state === "running") play(); else c.resume().then(play).catch(() => {});
}
const buzz = (p) => { try { if (navigator.vibrate && (!navigator.userActivation || navigator.userActivation.hasBeenActive)) navigator.vibrate(p); } catch { /* no vibration */ } };
const SFX = {   // volumes set for phone speakers
  tap: () => tone([520], "sine", 0.06, 0, 0.08),
  pair: () => tone([740], "sine", 0.1, 0, 0.16),
  good: () => { tone([659, 880], "sine", 0.18, 0.09, 0.22); buzz(12); },
  bad: () => { tone([233, 196], "triangle", 0.22, 0.12, 0.2); buzz([30, 40, 30]); },
  done: () => tone([523, 659, 784, 1047], "sine", 0.24, 0.11, 0.2),
  gift: () => { tone([988, 1319, 1568], "sine", 0.16, 0.07, 0.2); buzz([15, 30, 15]); },
};

/* ---------- content + media ---------- */
const mediaBase = CFG.mediaBase || "content/media/";
const media = (path, size) => mediaBase + (size === 480 ? path.replace(/\.webp$/, "@480.webp") : path);   // path like "sukaphaa/x.webp", "shared/x.webp", "faces/x.webp"
// Every content file is fetched with the release number (?v=…) from content/manifest.json, so a new
// release is a new address that no browser or service-worker cache can answer with an old copy.
let release = null;
const releaseVersion = () => (release = release || fetch("content/manifest.json", { cache: "no-cache" }).then((r) => r.json()).then((m) => m.version).catch(() => ""));
async function getJSON(url) {
  const v = url.startsWith("content/") && url !== "content/manifest.json" ? await releaseVersion() : "";
  const r = await fetch(v ? `${url}?v=${v}` : url, { cache: "no-cache" });
  if (!r.ok) throw new Error(`${url}: ${r.status}`);
  return r.json();
}

/* ---------- offline downloads (Cache API, shared with the service worker) ---------- */
const OFFLINE_CACHE = "axom-offline";
async function isOffline(urls) {
  if (!("caches" in window)) return false;
  const c = await caches.open(OFFLINE_CACHE);
  const hits = await Promise.all(urls.map((u) => c.match(u)));
  return hits.every(Boolean);
}
async function saveOffline(urls, onProgress) {
  const c = await caches.open(OFFLINE_CACHE);
  let done = 0;
  for (const u of urls) { await c.add(new Request(u, { cache: "reload" })); onProgress && onProgress(++done, urls.length); }
}

/* ---------- shared icons ---------- */
const ICON = {
  fire: '<svg viewBox="0 0 24 24"><path fill="currentColor" stroke="none" d="M12.6 2.2c.3 2.8-1 4.4-2.4 6-1.4 1.6-2.9 3.3-2.9 6.1A5.2 5.2 0 0 0 12.5 20a5.6 5.6 0 0 0 5.7-5.6c0-2.3-1-3.9-2-5.2-.2 1.3-.8 2.3-1.9 2.8.4-3.3-.4-6.8-1.7-9.8z"/></svg>',
  gem: '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M7 3h10l4 5.5L12 21 3 8.5z"/><path fill="#fff" opacity=".35" d="M7 3l2.5 5.5H3zM12 21 9.5 8.5h5z"/></svg>',
  soundOn: '<svg viewBox="0 0 24 24"><path d="M4 9h4l5-4v14l-5-4H4z"/><path d="M16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12"/></svg>',
  soundOff: '<svg viewBox="0 0 24 24"><path d="M4 9h4l5-4v14l-5-4H4z"/><path d="M17 9l5 6M22 9l-5 6"/></svg>',
  back: '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
  user: '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
  download: '<svg viewBox="0 0 24 24"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>',
  check: '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
  gear: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></svg>',
  book: '<svg viewBox="0 0 24 24"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5zM4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/></svg>',
  repeat: '<svg viewBox="0 0 24 24"><path d="M17 2l3 3-3 3M4 11V9a4 4 0 0 1 4-4h12M7 22l-3-3 3-3M20 13v2a4 4 0 0 1-4 4H4"/></svg>',
  chevron: '<svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg>',
  arrow: '<svg viewBox="0 0 24 24"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
  arrowBack: '<svg viewBox="0 0 24 24"><path d="M20 12H5M11 6l-6 6 6 6"/></svg>',
  close: '<svg viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19"/></svg>',
  external: '<svg viewBox="0 0 24 24"><path d="M7 17L17 7M9 7h8v8"/></svg>',
  bulb: '<svg viewBox="0 0 24 24"><path d="M9 18h6M10 21h4M12 3a6.500 6.500 0 0 0-3.800 11.800c.5.400.8 1 .8 1.700V17h6v-.5c0-.7.300-1.300.8-1.700A6.500 6.500 0 0 0 12 3z"/></svg>',
  navHome: '<svg viewBox="0 0 24 24"><path fill="currentColor" stroke="none" d="M12 3 2.500 11.200l1.300 1.500L5 11.700V21h5.200v-6h3.600v6H19v-9.300l1.200 1 1.300-1.500z"/></svg>',
  navLearn: '<svg viewBox="0 0 24 24"><path d="M12 6.500C10 4.800 7 4.300 3.500 4.800v14c3.500-.5 6.500 0 8.500 1.700 2-1.700 5-2.200 8.500-1.700v-14C17 4.300 14 4.800 12 6.500zM12 6.500v14"/></svg>',
  navPeople: '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.2"/><path d="M2.500 20a6.500 6.500 0 0 1 13 0"/><circle cx="17" cy="9" r="2.600"/><path d="M16 14.200a5.200 5.200 0 0 1 6 5.300"/></svg>',
  navPractice: '<svg viewBox="0 0 24 24"><path d="M16 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h7M8 8h7M8 12h5M8 16h3M14 19l.700-3 6-6a1.600 1.600 0 0 1 2.300 2.300l-6 6z"/></svg>',
};
// language switch used in page headers: both names are always shown, the active one in red
const LANG = '<label class="lang" for="as"><span class="l-en">EN</span><i>/</i><span class="l-as">অসমীয়া</span></label>';
// the app's five destinations
function nav(on) {
  const course = store.get("axom:ui", {}).lastCourse || "assam-history";
  const items = [["home", "index.html", ICON.navHome, B("Home", "মূল পৃষ্ঠা")], ["learn", `index.html?course=${course}`, ICON.navLearn, B("Learn", "শিকা")], ["practice", "index.html?view=practice", ICON.navPractice, B("Practice", "অনুশীলন")], ["community", "index.html?view=community", ICON.navPeople, B("Community", "সম্প্ৰদায়")], ["profile", "index.html?view=profile", ICON.user, B("Profile", "প্ৰফাইল")]];
  return `<nav class="nav-bar">${items.map(([id, href, icon, t]) => `<a class="${id === on ? "on" : ""}" href="${href}"${id === on ? ' aria-current="page"' : ""}>${icon}${T(t)}</a>`).join("")}</nav>`;
}

/* ---------- reading settings ---------- */
function applySettings() {
  document.documentElement.style.setProperty("--zoom", G.fs || 1);
  document.documentElement.classList.toggle("no-motion", G.motion === false);
}
applySettings();
function openSettings(extra = "") {
  const root = document.getElementById("sheet-root");
  const seg = (key, opts) => `<div class="seg">${opts.map(([v, l]) => `<button data-set="${key}" data-val="${v}" class="${String(G[key]) === String(v) ? "on" : ""}">${l}</button>`).join("")}</div>`;
  root.innerHTML = `<div class="backdrop" data-close-settings></div><div class="sheet left"><div class="grab"></div><h2>${T(B("Settings", "ছেটিং"))}</h2>
    <div class="setting"><span>${T(B("Language", "ভাষা"))}</span>${seg("as", [[false, "English"], [true, "অসমীয়া"]])}</div>
    <div class="setting"><span>${T(B("Sound", "শব্দ"))}</span>${seg("sound", [[true, T(B("On", "অন"))], [false, T(B("Off", "অফ"))]])}</div>
    <div class="setting"><span>${T(B("Text size", "আখৰৰ আকাৰ"))}</span>${seg("fs", [[0.92, "A−"], [1, "A"], [1.12, "A+"]])}</div>
    <div class="setting"><span>${T(B("Animations", "এনিমেচন"))}</span>${seg("motion", [[true, T(B("On", "অন"))], [false, T(B("Off", "অফ"))]])}</div>
    ${extra}<div class="setting ver"><span>${T(B("App version", "এপৰ সংস্কৰণ"))}</span><span id="app-ver">…</span></div><button class="link" data-close-settings>${T(B("Close", "বন্ধ কৰা"))}</button></div>`;
  releaseVersion().then((v) => { const el = document.getElementById("app-ver"); if (el) el.textContent = v || "?"; });
}
document.addEventListener("click", (e) => {
  const b = e.target.closest("[data-set]");
  if (b) {
    const k = b.dataset.set, raw = b.dataset.val;
    G[k] = raw === "true" ? true : raw === "false" ? false : +raw;
    if (k === "as") { const box = document.getElementById("as"); if (box) { box.checked = G.as; box.dispatchEvent(new Event("change")); } }
    saveGlobal(); applySettings();
    b.parentElement.querySelectorAll("button").forEach((x) => x.classList.toggle("on", x === b));
    return;
  }
  if (e.target.closest("[data-close-settings]")) document.getElementById("sheet-root").innerHTML = "";
});

/* ---------- language switch (both languages are in the page; CSS shows one) ---------- */
function initLang() {
  const box = document.getElementById("as");
  if (!box) return;
  if (G.as) box.checked = true;
  box.addEventListener("change", () => { G.as = box.checked; saveGlobal(); });
}

/* ---------- service worker (offline + install) ---------- */
// Coming back with the browser's Back button can show a frozen copy of the page from before the
// learner finished something (back/forward cache). Reload it so locks and progress are current.
addEventListener("pageshow", (e) => { if (e.persisted) location.reload(); });
if ("serviceWorker" in navigator && location.protocol !== "file:") {
  window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}

/* ---------- account sync (only when Firebase is configured) ---------- */
const auth = { ready: false, user: null, signIn: null, signOut: null, social: null, onChange: [], onError: [], lastError: null };
if (CFG.firebase) {
  import("./sync.js").then((m) => m.start({ CFG, auth, snapshot, merge, applySnapshot, listeners, G, levelOf, iso })).catch((e) => console.warn("Sync unavailable:", e));
}

const notebook = (cid) => cid === "mathematics" || cid === "reasoning";   // courses built around interactive scenes (app/math.css)
window.AXOM = { notebook, B, T, N, asNum, store, G, getLesson, saveGlobal, saveLesson, streakNow, bumpStreak, SFX, tone, media, getJSON,
  isOffline, saveOffline, ICON, LANG, nav, initLang, auth, merge, snapshot, applySnapshot, onSave: (f) => listeners.push(f), _audioState: () => (ac ? ac.state : "none"),
  iso, levelOf, todayXP, BADGES, checkBadges, gameAfterUnit, nextAction, lessonsFinished, skillAnswer, misconception, skillState, rootCause, srsLearn, srsAnswer, reviewQueue, dailyReviewQueue, REVIEW_ROUND_SIZE, record, addDayXP, openSettings };
})();
