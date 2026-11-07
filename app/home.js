/* =========================================================
   Course home: Lessons (eras, checkpoints, daily review), dynasty Timeline,
   Family (succession), and Profile (stats, activity, weak lessons).
   Reads content/manifest.json, content/catalog.json and the chosen course (index.html?course=<id>).
   Without ?course it shows a subject's courses (index.html?subject=<id>) or, with neither, the app home.
   ========================================================= */
(() => {
"use strict";
const { B, T, N, asNum, G, ICON } = window.AXOM;
const $ = (s) => document.querySelector(s);
const params = new URLSearchParams(location.search);
// reviewer mode: ?review=1 turns it on (remembered on this device), ?review=0 turns it off; ?all works for one page
if (params.has("review")) { try { params.get("review") === "0" ? localStorage.removeItem("axom.review") : localStorage.setItem("axom.review", "1"); } catch { /* storage blocked */ } }
const UNLOCK_ALL = params.has("all") || (() => { try { return localStorage.getItem("axom.review") === "1"; } catch { return false; } })();
const UI = Object.assign({ tab: "lessons", open: {} }, AXOM.store.get("axom:ui", {}));
if (params.get("tab") === "overview") UI.open = {};
if (params.get("tab") === "skills") UI.tab = "skills";
const saveUI = () => AXOM.store.set("axom:ui", UI);
const ROOF = '<svg class="roof" viewBox="0 0 320 26" preserveAspectRatio="none"><path d="M0 4c22 2 30 10 52 13 44 6 172 6 216 0 22-3 30-11 52-13" fill="none" stroke="#fff" stroke-width="2"/><path d="M60 17v7M100 19v6M140 20v5M180 20v5M220 19v6M260 17v7" stroke="#fff" stroke-width="1.6"/></svg>';
const STAR = { A: "★★★", B: "★★", C: "★" };
const ALL_TABS = { lessons: B("Lessons", "পাঠ"), timeline: B("Timeline", "সময়ৰেখা"), family: B("Family", "বংশ"), profile: B("Profile", "প্ৰফাইল"), skills: B("My map", "মোৰ মানচিত্ৰ") };
const CID = (params.get("course") || "").replace(/[^a-z0-9-]/g, "");   // empty = show the hub
const VIEW = ["practice", "profile", "community"].includes(params.get("view")) ? params.get("view") : "";   // bottom-bar pages

document.body.insertAdjacentHTML("afterbegin", `
<input type="checkbox" id="as" aria-label="Show in Assamese">
<div class="stage"><div class="device home-page">
  <div class="view on" id="v-home">
    <div class="p-top">
      <a class="brand" href="index.html">Axomrank</a>
      <button class="chip-top hidden" id="install">${ICON.download}${T(B("Install", "ইনষ্টল"))}</button>
      <span class="spacer"></span>
      <span class="fire" id="fire"></span>
      <span class="gem" id="gem"></span>
      <button class="icon-btn hidden" id="account" aria-label="Account"></button>
      ${AXOM.LANG}
    </div>
    <div class="p-scroll" id="scroll"><div id="course"></div></div>
    <a class="continue-bar hidden" id="continue"></a>
    ${AXOM.nav(VIEW || (CID || (params.get("subject") || "") ? "learn" : "home"))}
  </div>
  <div class="toast" id="toast"></div>
  <div id="sheet-root"></div>
</div></div>`);
AXOM.initLang();

function toast(html) { const t = $("#toast"); t.innerHTML = html; t.classList.add("show"); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove("show"), 2200); }
function stats() {
  const s = AXOM.streakNow();
  $("#fire").innerHTML = ICON.fire + N(s); $("#fire").classList.toggle("on", s > 0);
  $("#gem").innerHTML = ICON.gem + N(G.xp);
}
const esc = (x) => String(x == null ? "" : x).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
const safeImg = (u) => (/^https:\/\//.test(u || "") ? esc(u) : "");
/* ---------- the one thing to do now (AXOM.nextAction decides; the learner only taps) ---------- */
function actionText(a) {
  if (a.kind === "review") return { small: B("Today's warm-up", "আজিৰ আৰম্ভণি"), big: B("Daily memory mission", "দৈনিক স্মৃতি অভিযান"), sub: B(`${a.round} clues · about 3 minutes`, `${asNum(a.round)}টা সংকেত · প্ৰায় ৩ মিনিট`) };
  if (a.kind === "done") return { small: B("All caught up", "সকলো শেষ"), big: B("Practise your mistakes", "ভুলবোৰ অনুশীলন কৰা"), sub: B("Every lesson so far is complete", "এতিয়ালৈকে সকলো পাঠ সম্পূৰ্ণ") };
  const unit = a.unit ? (a.unitNo === a.units ? B("Lesson test", "পাঠৰ পৰীক্ষা") : B(`Unit ${a.unitNo} of ${a.units - 1}: ${a.unit.en}`, `অধ্যায় ${asNum(a.unitNo)}/${asNum(a.units - 1)}: ${a.unit.as}`)) : B("", "");
  return { small: !G.xp ? B("Start here", "ইয়াৰ পৰা আৰম্ভ কৰা") : a.kind === "resume" ? B("Pick up where you left off", "য'ত ৰৈছিলা তাৰ পৰা") : a.kind === "new-course" ? B("Next course", "পিছৰ পাঠ্যক্ৰম") : B("Up next", "পিছৰটো"), big: a.title, sub: unit };
}
function todayCard(a) {
  const lv = AXOM.levelOf(), goal = G.game.goal || 30, today = AXOM.todayXP(), gp = Math.min(100, Math.round((today / goal) * 100));
  const streak = AXOM.streakNow(), studied = today > 0, x = actionText(a), late = new Date().getHours() >= 18;
  const risk = streak > 0 && !studied ? `<div class="streak-risk">${ICON.fire}<span>${T(late ? B(`Your ${streak}-day streak ends at midnight. One unit keeps it alive.`, `তোমাৰ ${asNum(streak)} দিনৰ ধাৰা মাজনিশা শেষ হ'ব। এটা অধ্যায়েই ইয়াক ৰাখিব।`) : B(`Keep your ${streak}-day streak going today.`, `আজিও তোমাৰ ${asNum(streak)} দিনৰ ধাৰা অব্যাহত ৰাখা।`))}</span></div>` : "";
  return `<section class="today">
    <div class="today-top">
      <div class="ring" style="--p:${gp}"><span><b>${N(Math.min(today, goal))}</b><small>/${N(goal)} XP</small></span></div>
      <div class="today-stats">
        <div class="t-row"><span class="t-fire ${streak ? "on" : ""}">${ICON.fire}${N(streak)}</span><span class="t-lbl">${T(B("day streak", "দিনৰ ধাৰা"))}</span>${G.game.freeze ? `<span class="t-freeze" title="Streak freeze">🧊×${N(G.game.freeze)}</span>` : ""}</div>
        <div class="t-row"><span class="lvl-chip">${T(B(`Lv ${lv.n}`, `স্তৰ ${asNum(lv.n)}`))}</span><span class="t-lbl">${T(lv.rank)}</span></div>
        <span class="lvl-bar"><i style="width:${lv.pct}%"></i></span>
        <small class="t-next">${T(B(`${lv.to - G.xp} XP to level ${lv.n + 1}`, `স্তৰ ${asNum(lv.n + 1)}লৈ ${asNum(lv.to - G.xp)} XP`))}</small>
      </div>
    </div>
    ${risk}
    <a class="go-now" href="${a.href}"><span class="g-txt"><small>${T(x.small)}</small><b>${T(x.big)}</b>${x.sub.en ? `<span>${T(x.sub)}</span>` : ""}</span><span class="g-btn">${T(gp >= 100 ? B("Keep going", "আগবাঢ়া") : studied ? B("Continue", "আগবাঢ়া") : B("Start", "আৰম্ভ"))} ›</span></a>
    ${gp >= 100 ? `<p class="goal-done">${T(B("🎯 Daily goal met. Extra lessons now are a bonus.", "🎯 আজিৰ লক্ষ্য পূৰণ হ'ল। এতিয়া যি পঢ়া সেয়া বোনাছ।"))}</p>` : ""}
  </section>`;
}
const years = (reign) => { const m = String(reign).match(/\d{3,4}/g) || []; return [+m[0], +(m[1] || m[0])]; };

let course, info, SKILLS = null;
/* ---------- shared data for the home and subject pages ---------- */
const SID = (params.get("subject") || "").replace(/[^a-z0-9-]/g, "");
const SUBJECT_ICON = {
  temple: '<path d="M3 21h18M5 21V11M19 21V11M9 21v-6h6v6M2.5 11 12 4l9.5 7z"/>',
  pillar: '<path d="M3 21h18M4 18h16M6 18V9M10 18V9M14 18V9M18 18V9M3 9l9-5 9 5z"/>',
  globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.6 3.8 5.6 3.8 9s-1.2 6.4-3.8 9c-2.6-2.6-3.8-5.6-3.8-9S9.4 5.6 12 3z"/>',
  puzzle: '<path d="M4 8h3.5a2 2 0 1 1 4 0H15v3.5a2 2 0 1 1 0 4V19H4z"/><path d="M15 8h5v11h-5"/>',
  scroll: '<path d="M7 4h11a2 2 0 0 1 2 2v1h-4M7 4a2 2 0 0 0-2 2v12a2 2 0 0 1-2 2h11a2 2 0 0 0 2-2V7M7 4a2 2 0 0 1 2 2v0M9 10h4M9 14h4"/>',
  coin: '<circle cx="12" cy="12" r="9"/><path d="M9 8h6M9 11h6M13 8c2 0 2 6-1 6h-3l5 4"/>',
  chart: '<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>',
  flask: '<path d="M9 3h6M10 3v6L4.5 18.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3M7.5 15h9"/>',
  news: '<path d="M4 5h13v14H6a2 2 0 0 1-2-2zM17 9h3v8a2 2 0 0 1-2 2M7 9h7M7 13h7M7 16h4"/>',
  sigma: '<path d="M18 5H6l6.5 7L6 19h12"/>',
  child: '<circle cx="12" cy="5" r="2.5"/><path d="M12 8v7M7 10.5l5 1.5 5-1.5M9 21l3-6 3 6"/>',
};
const sIcon = (k) => `<svg viewBox="0 0 24 24">${SUBJECT_ICON[k] || SUBJECT_ICON.scroll}</svg>`;
let DATA = null;
async function load() {
  if (DATA) return DATA;
  const [m, cat] = await Promise.all([AXOM.getJSON("content/manifest.json"), AXOM.getJSON("content/catalog.json")]);
  const list = await Promise.all(m.courses.map((c) => AXOM.getJSON(c.file)));
  return (DATA = { m, cat, courses: Object.fromEntries(list.map((c) => [c.id, c])) });
}
// a course's published lessons, how many are finished, and the next one to do
function progress(c, m) {
  const items = c.kings.filter((k) => k.lesson && m.lessons[k.lesson]);
  const done = items.filter((k) => AXOM.getLesson(k.lesson).done.test).length;
  return { total: items.length, done, next: items.find((k) => !AXOM.getLesson(k.lesson).done.test), started: items.some((k) => Object.keys(AXOM.getLesson(k.lesson).done).length) };
}
const subjectOf = (cat, cid) => cat.subjects.find((S) => S.courses.some((e) => e.course === cid));
const subjectSum = (S, D) => S.courses.filter((e) => D.courses[e.course] && !e.optional).map((e) => progress(D.courses[e.course], D.m)).reduce((a, p) => ({ total: a.total + p.total, done: a.done + p.done }), { total: 0, done: 0 });
const pct = (p) => (p.total ? Math.round((p.done / p.total) * 100) : 0);
const FOOT = `<div class="p-foot">${T(B("Bilingual · English / অসমীয়া · Sources accompany each lesson. Illustrations are artistic reconstructions.", "দ্বিভাষিক · English / অসমীয়া · প্ৰতিটো পাঠৰ লগত উৎস দিয়া আছে। চিত্ৰবোৰ শিল্পীৰ কল্পনা।"))}</div>`;
function reviewCard() {
  const due = AXOM.reviewQueue().length;
  const round = Math.min(due, AXOM.REVIEW_ROUND_SIZE);
  return due ? `<a class="review-card" href="lesson.html?review=1"><span class="ic">${ICON.repeat}</span><span><b>${T(B("Daily memory mission", "দৈনিক স্মৃতি অভিযান"))}</b><span class="s">${T(B(`${round} clues this round · ${due} waiting`, `এই পৰ্যায়ত ${asNum(round)}টা সংকেত · মুঠ ${asNum(due)}টা বাকী`))}</span></span><span class="go">›</span></a>` : "";
}

/* ---------- home: exam choice, continue, subjects ---------- */
async function homePage() {
  const D = await load(), { cat, m } = D;
  const exam = cat.exams.some((x) => x.id === UI.exam) ? UI.exam : "";
  const chips = [["", B("All exams", "সকলো পৰীক্ষা")], ...cat.exams.map((x) => [x.id, x.t])]
    .map(([id, t]) => `<button class="exam-chip ${exam === id ? "on" : ""}" data-exam="${id}">${T(t)}</button>`).join("");
  // continue: the course last opened, else the first one with progress, else the first live course
  const action = await AXOM.nextAction().catch(() => null);
  const live = cat.subjects.flatMap((S) => S.courses.filter((e) => D.courses[e.course]).map((e) => D.courses[e.course]));
  const last = D.courses[UI.lastCourse];
  const cur = (last && !last.archived && !last.draft && last) || live.find((c) => progress(c, m).started) || live[0];
  let cont = "";
  if (cur) {
    const p = progress(cur, m), S = subjectOf(cat, cur.id);
    const k = p.next;
    cont = `<a class="resume" href="${k ? `lesson.html?id=${k.lesson}` : `index.html?course=${cur.id}`}">
      <span class="face">${k ? `<img src="${AXOM.media(k.face)}" alt="" loading="lazy">` : sIcon(S.icon)}</span>
      <span class="t"><small>${p.started ? T(B("Continue", "আগবাঢ়া")) : T(B("Start here", "ইয়াৰ পৰা আৰম্ভ কৰা"))} · ${T(S.title)}</small>
        <b>${k ? T(k.name) : cur.kings.some((x) => !x.lesson) ? T(B("All lessons so far done", "এতিয়ালৈকে থকা সকলো পাঠ সম্পূৰ্ণ")) : T(B("Course complete", "পাঠ্যক্ৰম সম্পূৰ্ণ"))}</b><span>${T(cur.title)} · ${T(B(`${p.done}/${p.total} lessons`, `${asNum(p.total)}টাৰ ${asNum(p.done)}টা পাঠ`))}</span>
        <span class="meter"><i style="--p:${pct(p)}%;width:${pct(p)}%"></i></span></span><span class="go">›</span></a>`;
  }
  const subjects = cat.subjects.filter((S) => !exam || S.exams.includes(exam)).map((S) => {
    const n = S.courses.filter((e) => D.courses[e.course]).length;
    if (!n) return `<button class="subj soon" data-soon style="--c:var(--${S.color})"><span class="ic">${sIcon(S.icon)}</span><b>${T(S.title)}</b><span class="s">${T(S.blurb)}</span><span class="pill">${T(B("Coming soon", "সোনকালে"))}</span></button>`;
    const p = subjectSum(S, D);
    return `<a class="subj" href="${S.id === "assam-history" ? "index.html?course=assam-history" : `index.html?subject=${S.id}`}" style="--c:var(--${S.color})"><span class="ic">${sIcon(S.icon)}</span><b>${T(S.title)}</b><span class="s">${T(S.blurb)}</span>
      <span class="pill">${T(B(`${n} course${n > 1 ? "s" : ""} · ${p.total} lessons`, `${asNum(n)}টা পাঠ্যক্ৰম · ${asNum(p.total)}টা পাঠ`))}</span><span class="meter"><i style="--p:${pct(p)}%;width:${pct(p)}%"></i></span></a>`;
  }).join("");
  const examName = exam ? T(cat.exams.find((x) => x.id === exam).t) : "ADRE · Assam TET · APSC · Assam Police SI";
  $("#course").innerHTML = `${action ? todayCard(action) : ""}<section class="home-hero">${ROOF}<div class="eyebrow">${T(B("Assam exam preparation", "অসম পৰীক্ষাৰ প্ৰস্তুতি"))}</div><h1>Axomrank</h1>
      <p>${T(B("Short bilingual lessons, daily revision and exam-style tests for", "চুটি দ্বিভাষিক পাঠ, দৈনিক পুনৰীক্ষণ আৰু পৰীক্ষাৰ ধৰণৰ প্ৰশ্ন:"))} <b>${examName}</b></p>
      <div class="exam-chips" role="group" aria-label="My exam">${chips}</div></section>
    ${action ? "" : cont + reviewCard()}
    <h2 class="sec-title">${T(B("Or choose a subject", "নাইবা এটা বিষয় বাছা"))}</h2><div class="subj-grid">${subjects}</div>
    <h2 class="sec-title">${T(B("Exam tools", "পৰীক্ষাৰ সঁজুলি"))}</h2>
    <div class="tools"><div class="tool"><span class="ic">📝</span><b>${T(B("Mock tests", "মক টেষ্ট"))}</b><span class="s">${T(B("OMR-style, timed, negative marking", "OMR ধৰণৰ, সময় বান্ধি, ঋণাত্মক নম্বৰ"))}</span><span class="pill">${T(B("Coming soon", "সোনকালে"))}</span></div>
      <div class="tool"><span class="ic">📚</span><b>${T(B("Previous-year papers", "পূৰ্বৰ বছৰৰ প্ৰশ্নকাকত"))}</b><span class="s">${T(B("With verified answer keys", "পৰীক্ষিত উত্তৰৰ সৈতে"))}</span><span class="pill">${T(B("Coming soon", "সোনকালে"))}</span></div></div>
    ${FOOT}`;
  $("#continue").classList.add("hidden");
}

/* ---------- subject: its courses in order ---------- */
async function subjectPage() {
  const D = await load(), S = D.cat.subjects.find((x) => x.id === SID);
  if (!S || !S.courses.some((e) => D.courses[e.course])) { location.replace("index.html"); return; }
  if (S.id === "assam-history") { location.replace("index.html?course=assam-history" + (UNLOCK_ALL ? "&all" : "")); return; }
  const p = subjectSum(S, D);
  const rows = S.courses.map((e, i) => {
    const c = D.courses[e.course];
    if (!c) return `<div class="course-row soon"><span class="no">${N(i + 1)}</span><span class="t"><b>${T(e.title)}</b><span>${T(e.subtitle)}</span></span><span class="pill">${T(B("Soon", "সোনকালে"))}</span></div>`;
    const q = progress(c, D.m), face = (c.kings.find((k) => k.tier === "A") || c.kings[0]).face;
    return `<a class="course-row ${q.done === q.total ? "done" : ""}" href="index.html?course=${c.id}"><span class="no">${N(i + 1)}</span><span class="cover"><img src="${AXOM.media(face)}" alt="" loading="lazy"></span>
      <span class="t"><b>${T(c.title)}</b><span>${T(c.subtitle)}</span><span class="meter"><i style="--p:${pct(q)}%;width:${pct(q)}%"></i></span><small>${T(B(`${q.done}/${q.total} lessons done`, `${asNum(q.total)}টাৰ ${asNum(q.done)}টা পাঠ সম্পূৰ্ণ`))}</small></span>${e.optional ? `<span class="pill">${T(B("Optional", "ঐচ্ছিক"))}</span>` : ""}<span class="go">›</span></a>`;
  }).join("");
  $("#course").innerHTML = `<section class="c-hero" style="--c:var(--${S.color})">${ROOF}<a class="back-hub" href="index.html">‹ ${T(B("Home", "মূল পৃষ্ঠা"))}</a><div class="eyebrow">${T(B("Subject", "বিষয়"))}</div><h1>${T(S.title)}</h1><p>${T(S.blurb)}</p>
      <span class="meter"><i style="--p:${pct(p)}%;width:${pct(p)}%"></i></span><span class="count">${T(B(`${p.done} of ${p.total} lessons done`, `${asNum(p.total)}টাৰ ${asNum(p.done)}টা পাঠ সম্পূৰ্ণ`))}</span></section>
    ${reviewCard()}${S.intro ? `<p class="tab-intro">${T(S.intro)}</p>` : ""}<div class="course-list">${rows}</div>${FOOT}`;
  $("#continue").classList.add("hidden");
}
/* ---------- Practice: what is due, what was missed, and the skill maps ---------- */
async function practicePage() {
  const D = await load(), { m } = D;
  const missed = Object.entries(G.mistakes).filter(([id, list]) => list.length && m.lessons[id]).sort((a, b) => b[1].length - a[1].length);
  const maps = Object.values(D.courses).filter((c) => c.skills && !c.archived && !c.draft);
  const rows = missed.slice(0, 8).map(([id, list]) => `<a class="acc-row" href="lesson.html?id=${id}"><span>${T(m.lessons[id].title)}</span><span class="note">${T(B(`${list.length} to revise`, `${asNum(list.length)}টা ভুল`))}</span><b>›</b></a>`).join("");
  $("#course").innerHTML = `<section class="home-hero"><h1>${T(B("Practice", "অনুশীলন"))}</h1><p>${T(B("Bring back what you learned, in short rounds.", "যি শিকিলা, চমু পৰ্যায়ত আকৌ মনত পেলোৱা।"))}</p></section>
    ${reviewCard() || `<div class="card"><h3>${T(B("Daily memory mission", "দৈনিক স্মৃতি অভিযান"))}</h3><p class="note">${T(B("Nothing is due today. Finish a unit and its questions come back here.", "আজি একো বাকী নাই। এটা অধ্যায় শেষ কৰিলে তাৰ প্ৰশ্নবোৰ ইয়াত উভতি আহিব।"))}</p></div>`}
    ${rows ? `<div class="card"><h3>${T(B("Your mistakes", "তোমাৰ ভুলবোৰ"))}</h3>${rows}</div>` : ""}
    ${maps.length ? `<div class="card"><h3>${T(B("Skill maps", "দক্ষতাৰ মানচিত্ৰ"))}</h3>${maps.map((c) => `<a class="acc-row" href="index.html?course=${c.id}&tab=skills"><span>${T(c.title)}</span><b>›</b></a>`).join("")}</div>` : ""}${FOOT}`;
  $("#continue").classList.add("hidden");
}

/* ---------- Profile: totals across every course, activity, account and settings ---------- */
const activity = () => [...Array(35).keys()].reverse().map((i) => AXOM.iso(-i)).map((d) => { const xp = G.days[d] || 0; return `<i class="${xp ? (xp >= 60 ? "l3" : xp >= 30 ? "l2" : "l1") : ""}" title="${d}: ${xp} XP"></i>`; }).join("");
const accountNote = () => { const user = AXOM.auth.user; return user ? T(B(`Signed in as ${user.name || "you"}. Progress syncs across devices.`, `${user.name || "তুমি"} হিচাপে চাইন ইন। অগ্ৰগতি সকলো ডিভাইচত মিলে।`)) : T(B("Not signed in. Progress is saved on this device only.", "চাইন ইন কৰা নাই। অগ্ৰগতি কেৱল এই ডিভাইচত সাঁচি থোৱা হয়।")); };
async function profilePage() {
  const D = await load(), { m } = D;
  const tot = Object.values(G.stats).reduce((a, s) => ({ a: a.a + s.a, o: a.o + s.o }), { a: 0, o: 0 });
  const finished = Object.keys(m.lessons).filter((id) => AXOM.getLesson(id).done.test).length;
  AXOM.checkBadges();
  const lv = AXOM.levelOf(), got = AXOM.BADGES.filter((b) => G.game.badges[b.id]).length;
  const badges = AXOM.BADGES.map((b) => `<div class="bdg ${G.game.badges[b.id] ? "on" : ""}" title="${esc(b.d.en)}"><span class="b-ic">${b.icon}</span><b>${T(b.t)}</b><small>${T(b.d)}</small></div>`).join("");
  const seg = (key, opts) => `<div class="seg">${opts.map(([v, l]) => `<button data-game="${key}" data-val="${v}" class="${String(G.game[key]) === String(v) ? "on" : ""}">${l}</button>`).join("")}</div>`;
  $("#course").innerHTML = `<section class="home-hero"><h1>${T(B("Profile", "প্ৰফাইল"))}</h1><p>${T(B("Your level, badges and progress.", "তোমাৰ স্তৰ, বেজ আৰু অগ্ৰগতি।"))}</p></section>
    ${accountCard()}
    <div class="card lvl-card"><div class="lvl-big"><span class="lvl-num-big">${N(lv.n)}</span><span><small>${T(B("Level", "স্তৰ"))}</small><b>${T(lv.rank)}</b></span></div>
      <span class="lvl-bar"><i style="width:${lv.pct}%"></i></span><p class="note">${T(B(`${G.xp - lv.from} / ${lv.to - lv.from} XP · ${lv.to - G.xp} XP to level ${lv.n + 1}`, `${asNum(G.xp - lv.from)} / ${asNum(lv.to - lv.from)} XP · স্তৰ ${asNum(lv.n + 1)}লৈ ${asNum(lv.to - G.xp)} XP`))}</p></div>
    <div class="pf-stats">
      <div class="stat" style="--c:var(--gold)"><div class="h">XP</div><div class="v">${N(G.xp)}</div></div>
      <div class="stat" style="--c:var(--terra)"><div class="h">${T(B("Streak", "ধাৰা"))}</div><div class="v">${N(AXOM.streakNow())}</div></div>
      <div class="stat" style="--c:var(--good)"><div class="h">${T(B("Accuracy", "শুদ্ধতা"))}</div><div class="v">${tot.a ? N(Math.round((tot.o / tot.a) * 100)) + "%" : "–"}</div></div>
    </div>
    <div class="card"><h3>${T(B(`Badges · ${got} of ${AXOM.BADGES.length}`, `বেজ · ${asNum(AXOM.BADGES.length)}টাৰ ${asNum(got)}টা`))}</h3><div class="bdg-grid">${badges}</div></div>
    <div class="card"><h3>${T(B("Streak", "ধাৰা"))}</h3><p class="note">${T(B(`Longest: ${G.game.best} days · Streak freezes: ${G.game.freeze} of 2. You earn a freeze every 7 days in a row; it covers one missed day.`, `আটাইতকৈ দীঘল: ${asNum(G.game.best)} দিন · ধাৰা ৰক্ষাকৱচ: ২টাৰ ${asNum(G.game.freeze)}টা। একেৰাহে ৭ দিন পঢ়িলে এটা পাবা; ই এদিন বাদ পৰাটো ঢাকি দিয়ে।`))}</p></div>
    <div class="card"><h3>${T(B("Lessons finished", "সম্পূৰ্ণ পাঠ"))}</h3><p class="big-num">${N(finished)} <span>/ ${N(Object.keys(m.lessons).length)}</span></p></div>
    <div class="card"><h3>${T(B("Last 5 weeks", "শেহতীয়া ৫ সপ্তাহ"))}</h3><div class="cal">${activity()}</div></div>
    <div class="card"><h3>${T(B("Study plan", "পঢ়াৰ পৰিকল্পনা"))}</h3>
      <div class="setting"><span>${T(B("Daily goal", "দৈনিক লক্ষ্য"))}</span>${seg("goal", [[10, "10"], [30, "30"], [50, "50"], [100, "100"]])}</div>
      <div class="setting"><span>${T(B("Open where I left off", "য'ত ৰৈছিলোঁ তাতে খোলা"))}</span>${seg("auto", [[true, T(B("On", "অন"))], [false, T(B("Off", "অফ"))]])}</div></div>
    <button class="btn" id="settings">${ICON.gear}${T(B("Settings", "ছেটিং"))}</button>${FOOT}`;
  $("#continue").classList.add("hidden");
}
/* ---------- account card with a clear reason when sign-in fails ---------- */
const IN_APP = /FBAN|FBAV|Instagram|Line\/|; wv\)|Snapchat|MicroMessenger/i.test(navigator.userAgent);
function signInError(e) {
  const c = (e && e.code) || "";
  if (IN_APP || c === "auth/operation-not-supported-in-this-environment") return B("Google sign-in does not work inside this app's built-in browser. Open axomrank.pages.dev in Chrome or Safari and sign in there.", "এই এপৰ ভিতৰৰ ব্ৰাউজাৰত Google চাইন ইন নচলে। Chrome বা Safari ত axomrank.pages.dev খুলি তাত চাইন ইন কৰা।");
  if (c === "auth/unauthorized-domain") return B(`Sign-in is not yet enabled for ${location.hostname}. The site owner must add this domain in Firebase (scripts/authorize_domain.sh).`, `${location.hostname} ৰ বাবে চাইন ইন এতিয়াও সক্ৰিয় কৰা হোৱা নাই। চাইটৰ গৰাকীয়ে Firebase ত এই ডমেইন যোগ কৰিব লাগিব।`);
  if (c === "auth/popup-closed-by-user" || c === "auth/cancelled-popup-request") return B("The sign-in window was closed before it finished. Tap Sign in again.", "চাইন ইন শেষ হোৱাৰ আগতে উইণ্ড' বন্ধ হ'ল। আকৌ চাইন ইন টিপা।");
  if (c === "auth/network-request-failed") return B("No internet connection. Connect and try again.", "ইণ্টাৰনেট সংযোগ নাই। সংযোগ কৰি আকৌ চেষ্টা কৰা।");
  if (c === "auth/popup-blocked") return B("Your browser blocked the sign-in window. Allow pop-ups for this site and try again.", "ব্ৰাউজাৰে চাইন ইন উইণ্ড' বন্ধ কৰিলে। এই চাইটৰ বাবে পপ-আপ অনুমতি দি আকৌ চেষ্টা কৰা।");
  return B(`Sign-in did not finish (${c || "unknown error"}). Try again.`, `চাইন ইন সম্পূৰ্ণ নহ'ল (${c || "অজ্ঞাত"})। আকৌ চেষ্টা কৰা।`);
}
let signInMsg = null;
function accountCard() {
  if (!(window.AXOM_CONFIG || {}).firebase) return "";
  const u = AXOM.auth.user;
  if (u) return `<div class="card acct"><span class="acct-face">${safeImg(u.photo) ? `<img src="${safeImg(u.photo)}" alt="">` : ICON.user}</span><span class="acct-t"><b>${esc(u.name || "")}</b><small>${T(B("Progress syncs across your devices", "অগ্ৰগতি সকলো ডিভাইচত মিলে"))}</small></span><button class="link" id="signout-p">${T(B("Sign out", "চাইন আউট"))}</button></div>`;
  return `<div class="card acct-in"><h3>${T(B("Save your progress", "তোমাৰ অগ্ৰগতি সাঁচি ৰাখা"))}</h3><p class="note">${T(B("Sign in to keep your XP, streak and badges on every device, and to join the Community.", "সকলো ডিভাইচত XP, ধাৰা আৰু বেজ ৰাখিবলৈ আৰু সম্প্ৰদায়ত যোগ দিবলৈ চাইন ইন কৰা।"))}</p>
    <button class="btn google" data-signin><svg viewBox="0 0 24 24"><path fill="#4285F4" stroke="none" d="M22.5 12.3c0-.8-.1-1.500-.2-2.200H12v4.200h5.900a5 5 0 0 1-2.200 3.300v2.700h3.500c2.100-1.900 3.300-4.700 3.300-8z"/><path fill="#34A853" stroke="none" d="M12 23c3 0 5.500-1 7.300-2.700l-3.500-2.700c-1 .7-2.300 1.100-3.800 1.100-2.900 0-5.400-2-6.300-4.600H2.100v2.800A11 11 0 0 0 12 23z"/><path fill="#FBBC05" stroke="none" d="M5.700 14.100a6.600 6.600 0 0 1 0-4.200V7.100H2.100a11 11 0 0 0 0 9.800z"/><path fill="#EA4335" stroke="none" d="M12 5.400c1.600 0 3.100.6 4.200 1.700l3.100-3.100A11 11 0 0 0 2.100 7.100l3.600 2.800C6.600 7.300 9.100 5.400 12 5.400z"/></svg>${T(B("Sign in with Google", "Google ৰে চাইন ইন"))}</button>
    ${signInMsg ? `<p class="signin-err">${T(signInMsg)}</p>` : IN_APP ? `<p class="signin-err">${T(signInError(null))}</p>` : ""}</div>`;
}
async function doSignIn() {
  const auth = AXOM.auth;
  if (!auth.signIn) return toast(T(B("Connecting…", "সংযোগ হৈ আছে…")));
  signInMsg = null;
  try { await auth.signIn(); toast(T(B("Signed in. Progress will sync.", "চাইন ইন হ'ল। অগ্ৰগতি মিলাই থোৱা হ'ব।"))); }
  catch (err) { console.warn(err); signInMsg = signInError(err); toast(T(B("Sign-in did not finish", "চাইন ইন সম্পূৰ্ণ নহ'ল"))); render(); }
}

/* ---------- Community: people, group rooms and direct messages ---------- */
const ROOMS = [["general", B("Common room", "সাধাৰণ কোঠা")], ["adre", B("ADRE", "ADRE")], ["tet", B("Assam TET", "অসম TET")], ["apsc", B("APSC", "APSC")], ["si", B("Police SI", "আৰক্ষী SI")]];
const CV = Object.assign({ tab: "people", room: "general" }, AXOM.store.get("axom:community", {}));
let unsub = [], DM = null, PEOPLE = [], INBOX = [];
const stopAll = () => { unsub.forEach((f) => { try { f(); } catch { /* already stopped */ } }); unsub = []; };
const ago = (t) => { const s = (Date.now() - t) / 1000; return s < 60 ? B("now", "এতিয়া") : s < 3600 ? B(`${Math.floor(s / 60)}m`, `${asNum(Math.floor(s / 60))} মি`) : s < 86400 ? B(`${Math.floor(s / 3600)}h`, `${asNum(Math.floor(s / 3600))} ঘ`) : B(`${Math.floor(s / 86400)}d`, `${asNum(Math.floor(s / 86400))} দি`); };
const face = (photo, name) => safeImg(photo) ? `<img src="${safeImg(photo)}" alt="" loading="lazy" referrerpolicy="no-referrer">` : `<span class="initial">${esc((name || "?")[0].toUpperCase())}</span>`;
const blocked = (uid) => !!(G.game.block || {})[uid];
function communityPage() {
  stopAll();
  const auth = AXOM.auth;
  const hero = `<section class="home-hero"><h1>${T(B("Community", "সম্প্ৰদায়"))}</h1><p>${T(B("Study together: see who is learning, climb the weekly board and talk.", "একেলগে পঢ়া: কোনে পঢ়ি আছে চোৱা, সাপ্তাহিক তালিকাত উঠা আৰু কথা পাতা।"))}</p></section>`;
  $("#continue").classList.add("hidden");
  if (!(window.AXOM_CONFIG || {}).firebase) { $("#course").innerHTML = hero + `<div class="card"><p class="note">${T(B("Community needs an internet connection and an account.", "সম্প্ৰদায়ৰ বাবে ইণ্টাৰনেট আৰু একাউণ্ট লাগে।"))}</p></div>`; return; }
  if (!auth.ready) { $("#course").innerHTML = hero + `<div class="card"><p class="note">${T(B("Connecting…", "সংযোগ হৈ আছে…"))}</p></div>`; return; }
  if (!auth.user) { $("#course").innerHTML = hero + accountCard(); return; }
  const S = auth.social;
  if (DM) return dmView();
  const tabs = [["people", B("People", "মানুহ")], ["rooms", B("Rooms", "কোঠা")], ["inbox", B("Messages", "বাৰ্তা")]];
  $("#course").innerHTML = hero + `<div class="tabs home-tabs cm-tabs" role="tablist">${tabs.map(([k, t]) => `<button class="tab ${CV.tab === k ? "on" : ""}" data-ctab="${k}">${T(t)}${k === "inbox" ? '<i class="dot hidden" id="inbox-dot"></i>' : ""}</button>`).join("")}</div><div id="cm-body"><p class="note cm-load">${T(B("Loading…", "ল'ড হৈ আছে…"))}</p></div>`;
  const body = $("#cm-body");
  unsub.push(S.inbox((list) => { INBOX = (list || []).filter((d) => !blocked(d.users.find((u) => u !== auth.user.uid))); const seen = AXOM.store.get("axom:dmseen", {}); const n = INBOX.filter((d) => d.from !== auth.user.uid && d.t > (seen[d.id] || 0)).length; const dot = $("#inbox-dot"); if (dot) dot.classList.toggle("hidden", !n); if (CV.tab === "inbox") inboxView(body); }));
  if (CV.tab === "people") unsub.push(S.people((list, err) => { if (err) return showErr(body, err); PEOPLE = list.filter((p) => !blocked(p.id)); peopleView(body); }));
  if (CV.tab === "rooms") roomView(body);
}
function showErr(el, err) { console.warn(err); el.innerHTML = `<div class="card"><p class="note">${T(B("Community could not load. Check your connection and try again.", "সম্প্ৰদায় খুলিব পৰা নগ'ল। সংযোগ পৰীক্ষা কৰি আকৌ চেষ্টা কৰা।"))}</p></div>`; }
function peopleView(el) {
  const me = AXOM.auth.user.uid, now = Date.now(), week = (PEOPLE.find((p) => p.id === me) || {}).week;
  const online = PEOPLE.filter((p) => now - p.t < 5 * 60e3);
  const board = PEOPLE.filter((p) => p.week === week && p.weekXp > 0).sort((a, b) => b.weekXp - a.weekXp).slice(0, 20);
  const myRank = board.findIndex((p) => p.id === me);
  const row = (p, extra = "") => `<button class="person ${p.id === me ? "me" : ""}" data-person="${esc(p.id)}"><span class="p-face">${face(p.photo, p.name)}${now - p.t < 5 * 60e3 ? '<i class="online"></i>' : ""}</span><span class="p-t"><b>${esc(p.name)}${p.id === me ? ` · ${T(B("you", "তুমি"))}` : ""}</b><small>${T(B(`Lv ${p.level} · 🔥${p.streak} · 🏅${p.badges}`, `স্তৰ ${asNum(p.level)} · 🔥${asNum(p.streak)} · 🏅${asNum(p.badges)}`))}</small></span>${extra}</button>`;
  el.innerHTML = `<div class="card"><h3>${T(B(`Online now · ${online.length}`, `এতিয়া অনলাইন · ${asNum(online.length)}`))}</h3>${online.length ? `<div class="online-strip">${online.map((p) => `<button class="o-face" data-person="${esc(p.id)}">${face(p.photo, p.name)}<small>${esc(p.name)}</small></button>`).join("")}</div>` : `<p class="note">${T(B("Nobody else right now. Start a lesson; others will see you here.", "এতিয়া আন কোনো নাই। এটা পাঠ আৰম্ভ কৰা; আনে তোমাক ইয়াত দেখিব।"))}</p>`}</div>
    <div class="card"><h3>${T(B("This week's leaderboard", "এই সপ্তাহৰ শীৰ্ষ তালিকা"))}</h3>${myRank >= 0 ? `<p class="note">${T(B(`You are #${myRank + 1} this week.`, `এই সপ্তাহত তুমি #${asNum(myRank + 1)}।`))}</p>` : `<p class="note">${T(B("Earn XP this week to join the board.", "তালিকাত উঠিবলৈ এই সপ্তাহত XP অৰ্জন কৰা।"))}</p>`}
      ${board.map((p, i) => row(p, `<span class="rank r${i + 1}">${i < 3 ? ["🥇", "🥈", "🥉"][i] : N(i + 1)}</span><span class="wxp">${N(p.weekXp)} XP</span>`)).join("") || ""}</div>
    <div class="card"><h3>${T(B("Learners", "শিক্ষাৰ্থী"))}</h3>${PEOPLE.slice(0, 60).map((p) => row(p, `<span class="when">${T(ago(p.t))}</span>`)).join("")}</div>
    <p class="note cm-rule">${T(B("Be kind. Never share your phone number, address or passwords. Long-press or tap ⋯ on a message to report it.", "সদয় হোৱা। ফোন নম্বৰ, ঠিকনা বা পাছৱৰ্ড কেতিয়াও নিদিবা। কোনো বাৰ্তা ৰিপ'ৰ্ট কৰিবলৈ ⋯ টিপা।"))}</p>`;
}
function msgHTML(msg, where, canDelete) {
  const me = AXOM.auth.user.uid, mine = msg.uid === me;
  return `<div class="msg ${mine ? "mine" : ""}">${mine ? "" : `<button class="m-face" data-person="${esc(msg.uid)}">${face(msg.photo, msg.name)}</button>`}<div class="cm-bubble">${mine || !msg.name ? "" : `<b>${esc(msg.name)}${msg.lv ? ` <small>Lv ${esc(msg.lv)}</small>` : ""}</b>`}<p>${esc(msg.text)}</p><small class="m-when">${T(ago(msg.t))}</small></div>
    <button class="m-more" data-msg="${esc(msg.id)}" data-where="${esc(where)}" data-mine="${mine && canDelete ? 1 : 0}" aria-label="More">⋯</button></div>`;
}
let MSGS = {};
function composer(id) { return `<form class="composer" data-send="${id}"><input maxlength="500" autocomplete="off" placeholder="${esc(G.as ? "বাৰ্তা লিখা…" : "Write a message…")}" aria-label="Message"><button class="btn send" aria-label="Send">${ICON.arrow}</button></form>`; }
function roomView(el) {
  el.innerHTML = `<div class="room-chips">${ROOMS.map(([id, t]) => `<button class="exam-chip ${CV.room === id ? "on" : ""}" data-room="${id}">${T(t)}</button>`).join("")}</div><div class="chat" id="chat"></div>${composer("room")}`;
  unsub.push(AXOM.auth.social.room(CV.room, (list, err) => {
    if (err) return showErr($("#chat"), err);
    MSGS = Object.fromEntries(list.map((x) => [x.id, x]));
    const box = $("#chat"); if (!box) return;
    box.innerHTML = list.filter((x) => !blocked(x.uid)).map((x) => msgHTML(x, `rooms/${CV.room}/msgs`, true)).join("") || `<p class="note">${T(B("No messages yet. Say hello!", "এতিয়ালৈকে কোনো বাৰ্তা নাই। নমস্কাৰ কোৱা!"))}</p>`;
    box.scrollTop = box.scrollHeight; $("#scroll").scrollTop = $("#scroll").scrollHeight;
  }));
}
function inboxView(el) {
  const me = AXOM.auth.user.uid, seen = AXOM.store.get("axom:dmseen", {});
  el.innerHTML = INBOX.length ? `<div class="card">${INBOX.map((d) => { const o = d.users.find((u) => u !== me), unread = d.from !== me && d.t > (seen[d.id] || 0); return `<button class="person ${unread ? "unread" : ""}" data-dm="${esc(o)}" data-name="${esc((d.names || {})[o])}" data-photo="${esc((d.photos || {})[o])}"><span class="p-face">${face((d.photos || {})[o], (d.names || {})[o])}</span><span class="p-t"><b>${esc((d.names || {})[o] || "")}</b><small>${d.from === me ? T(B("You: ", "তুমি: ")) : ""}${esc(d.last)}</small></span><span class="when">${T(ago(d.t))}</span></button>`; }).join("")}</div>`
    : `<div class="card"><p class="note">${T(B("No messages yet. Tap a learner in People to start a chat.", "এতিয়ালৈকে কোনো বাৰ্তা নাই। কথা পাতিবলৈ মানুহ টেবত কোনো শিক্ষাৰ্থীক টিপা।"))}</p></div>`;
}
function dmView() {
  const S = AXOM.auth.social, pair = S.pairOf(AXOM.auth.user.uid, DM.uid);
  $("#course").innerHTML = `<div class="dm-head"><button class="icon-btn" data-dm-back aria-label="Back">${ICON.arrowBack}</button><span class="p-face">${face(DM.photo, DM.name)}</span><b>${esc(DM.name)}</b></div><div class="chat dm" id="chat"></div>${composer("dm")}`;
  unsub.push(S.dm(DM.uid, (list, err) => {
    if (err) return showErr($("#chat"), err);
    MSGS = Object.fromEntries(list.map((x) => [x.id, x]));
    const seen = AXOM.store.get("axom:dmseen", {}); seen[pair] = Date.now(); AXOM.store.set("axom:dmseen", seen);
    const box = $("#chat"); if (!box) return;
    box.innerHTML = list.map((x) => msgHTML({ ...x, name: "", photo: DM.photo }, `dms/${pair}/msgs`, true)).join("") || `<p class="note">${T(B(`Say hello to ${DM.name}.`, `${DM.name}ক নমস্কাৰ জনোৱা।`))}</p>`;
    $("#scroll").scrollTop = $("#scroll").scrollHeight;
  }));
}
function personSheet(uid) {
  const p = PEOPLE.find((x) => x.id === uid) || { id: uid, name: (Object.values(MSGS).find((x) => x.uid === uid) || {}).name || "", photo: (Object.values(MSGS).find((x) => x.uid === uid) || {}).photo || "", level: "?", streak: 0, badges: 0, xp: 0, t: 0 };
  const me = uid === AXOM.auth.user.uid;
  $("#sheet-root").innerHTML = `<div class="backdrop" data-close></div><div class="sheet left person-sheet"><div class="grab"></div>
    <div class="ps-face">${face(p.photo, p.name)}</div><h2>${esc(p.name)}</h2>
    <div class="pf-stats"><div class="stat" style="--c:var(--indigo)"><div class="h">${T(B("Level", "স্তৰ"))}</div><div class="v">${esc(p.level)}</div></div><div class="stat" style="--c:var(--terra)"><div class="h">${T(B("Streak", "ধাৰা"))}</div><div class="v">${N(p.streak || 0)}</div></div><div class="stat" style="--c:var(--gold)"><div class="h">XP</div><div class="v">${N(p.xp || 0)}</div></div></div>
    ${me ? `<label class="nick"><span>${T(B("Your name in Community", "সম্প্ৰদায়ত তোমাৰ নাম"))}</span><input id="nick" maxlength="30" value="${esc(G.game.nick || p.name)}"></label><button class="btn" id="nick-save">${T(B("Save", "সাঁচি ৰাখা"))}</button>
      <div class="setting"><span>${T(B("Show me in Community", "সম্প্ৰদায়ত মোক দেখুওৱা"))}</span><div class="seg"><button data-game="hidden" data-val="false" class="${G.game.hidden ? "" : "on"}">${T(B("Yes", "হয়"))}</button><button data-game="hidden" data-val="true" class="${G.game.hidden ? "on" : ""}">${T(B("No", "নহয়"))}</button></div></div>`
      : `<button class="btn" data-dm="${esc(p.id)}" data-name="${esc(p.name)}" data-photo="${esc(p.photo)}">${T(B("Send a message", "বাৰ্তা পঠিওৱা"))}</button><button class="link danger" data-block="${esc(p.id)}">${T(blocked(p.id) ? B("Unblock", "অৱৰোধ আঁতৰোৱা") : B("Block", "অৱৰোধ কৰা"))}</button>`}
    <button class="link" data-close>${T(B("Close", "বন্ধ কৰা"))}</button></div>`;
}
document.addEventListener("submit", async (e) => {
  const f = e.target.closest("[data-send]"); if (!f) return;
  e.preventDefault();
  const input = f.querySelector("input"), text = input.value.trim(); if (!text) return;
  input.value = ""; input.focus();
  try { f.dataset.send === "dm" ? await AXOM.auth.social.tell(DM.uid, DM.name, DM.photo, text) : await AXOM.auth.social.say(CV.room, text); AXOM.checkBadges(); AXOM.saveGlobal(); }
  catch (err) { console.warn(err); input.value = text; toast(T(B("Message not sent. Try again.", "বাৰ্তা পঠোৱা নহ'ল। আকৌ চেষ্টা কৰা।"))); }
});
document.addEventListener("click", async (e) => {
  let b;
  if (e.target.closest("[data-signin]")) return doSignIn();
  if (e.target.closest("#signout-p")) { await AXOM.auth.signOut(); toast(T(B("Signed out", "চাইন আউট হ'ল"))); return; }
  if ((b = e.target.closest("[data-game]"))) {
    const k = b.dataset.game, raw = b.dataset.val; G.game[k] = raw === "true" ? true : raw === "false" ? false : +raw; AXOM.saveGlobal();
    b.parentElement.querySelectorAll("button").forEach((x) => x.classList.toggle("on", x === b));
    if (k === "hidden" && AXOM.auth.social) AXOM.auth.social.publish().catch(() => {});
    return;
  }
  if ((b = e.target.closest("[data-ctab]"))) { CV.tab = b.dataset.ctab; AXOM.store.set("axom:community", CV); return communityPage(); }
  if ((b = e.target.closest("[data-room]"))) { CV.room = b.dataset.room; AXOM.store.set("axom:community", CV); return communityPage(); }
  if ((b = e.target.closest("[data-dm]"))) { $("#sheet-root").innerHTML = ""; DM = { uid: b.dataset.dm, name: b.dataset.name, photo: b.dataset.photo }; return communityPage(); }
  if (e.target.closest("[data-dm-back]")) { DM = null; CV.tab = "inbox"; return communityPage(); }
  if ((b = e.target.closest("[data-person]"))) return personSheet(b.dataset.person);
  if ((b = e.target.closest("[data-block]"))) { const id = b.dataset.block; G.game.block = { ...(G.game.block || {}) }; if (G.game.block[id]) delete G.game.block[id]; else G.game.block[id] = true; AXOM.saveGlobal(); $("#sheet-root").innerHTML = ""; return communityPage(); }
  if (e.target.closest("#nick-save")) { G.game.nick = $("#nick").value.replace(/[<>]/g, "").trim().slice(0, 30); AXOM.saveGlobal(); await AXOM.auth.social.publish().catch(() => {}); $("#sheet-root").innerHTML = ""; toast(T(B("Saved", "সাঁচি ৰখা হ'ল"))); return communityPage(); }
  if ((b = e.target.closest("[data-msg]"))) {
    const msg = MSGS[b.dataset.msg]; if (!msg) return;
    $("#sheet-root").innerHTML = `<div class="backdrop" data-close></div><div class="sheet left"><div class="grab"></div><p class="note">“${esc(msg.text)}”</p>
      ${b.dataset.mine === "1" ? `<button class="btn" data-del="${esc(b.dataset.where)}/${esc(msg.id)}">${T(B("Delete my message", "মোৰ বাৰ্তা মচা"))}</button>` : `<button class="btn" data-report="${esc(msg.id)}" data-where="${esc(b.dataset.where)}">${T(B("Report to moderators", "পৰিচালকক জনোৱা"))}</button><button class="link danger" data-block="${esc(msg.uid)}">${T(B("Block this person", "এই মানুহজনক অৱৰোধ কৰা"))}</button>`}
      <button class="link" data-close>${T(B("Close", "বন্ধ কৰা"))}</button></div>`;
    return;
  }
  if ((b = e.target.closest("[data-del]"))) { await AXOM.auth.social.remove(b.dataset.del.split("/")).catch((err) => console.warn(err)); $("#sheet-root").innerHTML = ""; return; }
  if ((b = e.target.closest("[data-report]"))) { const msg = MSGS[b.dataset.report]; await AXOM.auth.social.report(msg, b.dataset.where).then(() => toast(T(B("Reported. Thank you.", "জনোৱা হ'ল। ধন্যবাদ।")))).catch(() => toast(T(B("Could not report. Try again.", "জনাব পৰা নগ'ল।")))); $("#sheet-root").innerHTML = ""; }
});
/* ---------- first visit: four short screens, then straight into the first lesson ----------
   1 language · 2 exam · 3 daily goal · 4 how it works + Start. Shown once (G.game.onboarded); Skip is always there. */
const ONB = { step: 0 };
const GOALS = [[10, B("Casual", "সহজ"), B("about 3 min a day", "দিনে প্ৰায় ৩ মিনিট")], [30, B("Regular", "নিয়মীয়া"), B("about 10 min a day", "দিনে প্ৰায় ১০ মিনিট")], [50, B("Serious", "গুৰুত্বসহকাৰে"), B("about 15 min a day", "দিনে প্ৰায় ১৫ মিনিট")], [100, B("Intense", "তীব্ৰ"), B("about 30 min a day", "দিনে প্ৰায় ৩০ মিনিট")]];
async function onboarding() {
  const s = ONB.step, cat = s === 1 ? (await load()).cat : null;   // only the exam step needs the catalogue
  const dots = `<div class="onb-dots">${[0, 1, 2, 3].map((k) => `<i class="${k === s ? "on" : k < s ? "done" : ""}"></i>`).join("")}</div>`;
  const top = `<div class="onb-top">${s ? `<button class="icon-btn" data-onb-back aria-label="Back">${ICON.arrowBack}</button>` : "<span></span>"}${dots}<button class="onb-skip" data-onb-skip>${T(B("Skip", "এৰি যোৱা"))}</button></div>`;
  let body = "";
  if (s === 0) body = `<div class="onb-hero">${ROOF}<div class="onb-logo">অ</div><h1>Axomrank</h1><p>${T(B("Prepare for Assam government exams in short, game-like lessons. Free, in English and Assamese.", "চুটি, খেলৰ দৰে পাঠেৰে অসম চৰকাৰী পৰীক্ষাৰ প্ৰস্তুতি। বিনামূলীয়া, ইংৰাজী আৰু অসমীয়াত।"))}</p></div>
    <h2 class="onb-q">${T(B("Which language do you prefer?", "কোন ভাষা ভাল পোৱা?"))}</h2>
    <div class="onb-opts"><button class="onb-opt ${G.as ? "" : "on"}" data-onb-lang="en"><span class="o-ic">Aa</span><b>English</b></button><button class="onb-opt ${G.as ? "on" : ""}" data-onb-lang="as"><span class="o-ic">অ</span><b>অসমীয়া</b></button></div>
    <p class="onb-hint">${T(B("You can switch any time with EN / অসমীয়া at the top.", "ওপৰৰ EN / অসমীয়া টিপি যিকোনো সময়তে সলনি কৰিব পাৰা।"))}</p>`;
  if (s === 1) body = `<h2 class="onb-q big">${T(B("Which exam are you preparing for?", "কোন পৰীক্ষাৰ বাবে প্ৰস্তুতি কৰিছা?"))}</h2><p class="onb-sub">${T(B("We'll put the subjects for your exam first.", "তোমাৰ পৰীক্ষাৰ বিষয়বোৰ আগত দেখুওৱা হ'ব।"))}</p>
    <div class="onb-opts col">${[...cat.exams.map((x) => [x.id, x.t]), ["", B("Not decided yet", "এতিয়াও ঠিক কৰা নাই")]].map(([id, t]) => `<button class="onb-opt row ${(UI.exam || "") === id && ONB.exam ? "on" : ""}" data-onb-exam="${id}"><span class="o-ic">${id ? "🎯" : "🤔"}</span><b>${T(t)}</b><span class="o-go">›</span></button>`).join("")}</div>`;
  if (s === 2) body = `<h2 class="onb-q big">${T(B("How much time can you give each day?", "দিনে কিমান সময় দিব পাৰিবা?"))}</h2><p class="onb-sub">${T(B("Small and daily beats long and rare. You can change this later in Profile.", "সৰু কিন্তু প্ৰতিদিনে পঢ়াটো দীঘল কিন্তু কেতিয়াবা পঢ়াতকৈ ভাল। পিছত প্ৰফাইলত সলনি কৰিব পাৰিবা।"))}</p>
    <div class="onb-opts col">${GOALS.map(([v, t, d]) => `<button class="onb-opt row ${G.game.goal === v && ONB.goal ? "on" : ""}" data-onb-goal="${v}"><span class="o-ic">${{ 10: "🌱", 30: "📘", 50: "🔥", 100: "🚀" }[v]}</span><span class="o-t"><b>${T(t)}</b><small>${T(d)} · ${N(v)} XP</small></span><span class="o-go">›</span></button>`).join("")}</div>`;
  if (s === 3) {
    const a = await AXOM.nextAction().catch(() => null);
    const step = (ic, t, d) => `<div class="how"><span class="h-ic">${ic}</span><span><b>${T(t)}</b><small>${T(d)}</small></span></div>`;
    body = `<h2 class="onb-q big">${T(B("Here's how it works", "এনেদৰে চলে"))}</h2>
      <div class="how-list">
        ${step("👆", B("Just tap Start", "কেৱল Start টিপা"), B("Every time you open the app, it takes you to exactly what to study next. No planning needed.", "এপ খুলিলেই পিছত কি পঢ়িব লাগে তাতে লৈ যায়। একো ভাবিব নালাগে।"))}
        ${step("⏱️", B("Short units", "চুটি অধ্যায়"), B("A short story, then 5–7 quick questions. Each answer explains why.", "এটা চুটি কাহিনী, তাৰ পিছত ৫–৭টা প্ৰশ্ন। প্ৰতিটো উত্তৰৰ কাৰণ দিয়া থাকে।"))}
        ${step("🧠", B("Daily memory mission", "দৈনিক স্মৃতি অভিযান"), B("What you learned comes back after 1, 3 and 7 days, so you don't forget it.", "যি শিকিলা সেয়া ১, ৩ আৰু ৭ দিনৰ পিছত উভতি আহে, যাতে নাপাহৰা।"))}
        ${step("🔥", B("XP, levels and streaks", "XP, স্তৰ আৰু ধাৰা"), B("Earn XP, level up, collect badges and keep your daily streak alive.", "XP অৰ্জন কৰা, স্তৰ বঢ়োৱা, বেজ গোটোৱা আৰু দৈনিক ধাৰা ৰাখা।"))}
      </div>
      ${a && a.title ? `<div class="onb-first"><small>${T(B("Your first lesson", "তোমাৰ প্ৰথম পাঠ"))}</small><b>${T(a.title)}</b></div>` : ""}`;
  }
  const foot = s === 0 ? `<button class="btn" data-onb-next>${T(B("Continue", "আগবাঢ়া"))}</button>`
    : s === 3 ? `<button class="btn onb-start" data-onb-start>${T(B("Start my first lesson", "মোৰ প্ৰথম পাঠ আৰম্ভ কৰা"))}${ICON.arrow}</button>${(window.AXOM_CONFIG || {}).firebase && !AXOM.auth.user ? `<button class="btn-ghost" data-signin>${T(B("I have an account · Sign in with Google", "মোৰ একাউণ্ট আছে · Google ৰে চাইন ইন"))}</button>` : ""}` : "";
  let el = $("#onb");
  if (!el) { el = document.createElement("div"); el.id = "onb"; el.className = "onb"; $(".device").append(el); }
  el.innerHTML = `${top}<div class="onb-body" key="${s}">${body}</div><div class="onb-foot">${foot}</div>`;
}
function onbDone(go) {
  G.game.onboarded = true; AXOM.saveGlobal();
  const el = $("#onb"); if (el) el.remove();
  if (go) AXOM.nextAction().then((a) => { location.href = a && a.kind !== "done" ? a.href : "index.html"; }).catch(() => render());
  else render();
}
document.addEventListener("click", (e) => {
  if (!$("#onb")) return;
  let b;
  if ((b = e.target.closest("[data-onb-lang]"))) { const as = b.dataset.onbLang === "as", box = $("#as"); box.checked = as; box.dispatchEvent(new Event("change")); ONB.step = 1; return onboarding(); }
  if ((b = e.target.closest("[data-onb-exam]"))) { UI.exam = b.dataset.onbExam; saveUI(); ONB.exam = true; ONB.step = 2; return onboarding(); }
  if ((b = e.target.closest("[data-onb-goal]"))) { G.game.goal = +b.dataset.onbGoal; AXOM.saveGlobal(); ONB.goal = true; ONB.step = 3; return onboarding(); }
  if (e.target.closest("[data-onb-next]")) { ONB.step = Math.min(3, ONB.step + 1); return onboarding(); }
  if (e.target.closest("[data-onb-back]")) { ONB.step = Math.max(0, ONB.step - 1); return onboarding(); }
  if (e.target.closest("[data-onb-skip]")) return onbDone(false);
  if (e.target.closest("[data-onb-start]")) return onbDone(true);
});

async function render() {
  // a learner with progress from before onboarding existed never sees it
  if (!G.game.onboarded && (G.xp > 0 || AXOM.lessonsFinished())) { G.game.onboarded = true; AXOM.saveGlobal(); }
  if (!G.game.onboarded && !VIEW && !CID && !SID) { onboarding(); load().catch(() => {}); return homePage(); }   // welcome shows at once; Home loads behind it
  if (VIEW) return VIEW === "practice" ? practicePage() : VIEW === "community" ? communityPage() : profilePage();
  // Opening the app lands straight in what to do next (once per visit; Home stays reachable from the bar).
  if (!CID && !SID && !location.search && G.game.auto !== false && G.xp > 0 && !sessionStorage.getItem("axom:landed")) {
    sessionStorage.setItem("axom:landed", "1");
    const a = await AXOM.nextAction().catch(() => null);
    if (a && a.kind !== "done") { location.replace(a.href); return; }
  }
  try { sessionStorage.setItem("axom:landed", "1"); } catch { /* storage blocked */ }
  if (!CID) return SID ? subjectPage() : homePage();
  if (!course) { const D = await load(); course = D.courses[CID]; info = D.m.lessons; const redirect = D.cat.course_redirects?.[CID]; if (redirect) { location.replace(`index.html?course=${redirect}${UNLOCK_ALL ? "&all" : ""}`); return; } if (!course) { location.replace("index.html"); return; } }
  if (CID === "assam-history" && params.get("tab") !== "overview") {
    const entries = course.kings.filter(k => k.lesson && info[k.lesson]);
    const saved = AXOM.store.get("axom:journey:assam-history", {});
    const next = entries.find(k => !AXOM.getLesson(k.lesson).done.test) || entries[0];
    const id = entries.some(k => k.lesson === saved.lesson) ? saved.lesson : next?.lesson;
    if (id) { location.replace(`lesson.html?id=${id}${UNLOCK_ALL ? "&all" : ""}`); return; }
  }
  if (CID === "assam-history") UI.tab = "overview";
  if (UI.lastCourse !== CID) { UI.lastCourse = CID; saveUI(); }
  if (course.skills && !SKILLS) SKILLS = await AXOM.getJSON(course.skills);
  document.documentElement.classList.toggle("maths", AXOM.notebook(CID));
  const S = subjectOf(DATA.cat, CID);
  const TABS = (CID === "assam-history" ? ["lessons", "overview"] : course.tabs || ["lessons", "timeline", "family", "profile"]).map((k) => [k, k === "family" && course.familyTitle ? course.familyTitle : (k === "overview" ? B("Overview", "অৱলোকন") : ALL_TABS[k])]);
  if (!TABS.some(([k]) => k === UI.tab)) UI.tab = "lessons";
  const byNo = Object.fromEntries(course.kings.filter((k) => k.lesson && info[k.lesson]).map((k) => [k.n, k.lesson]));
  const doneTest = (id) => !!AXOM.getLesson(id).done.test;
  const status = (k) => {
    const id = byNo[k.n];
    if (!id) return { s: "soon" };
    const done = Object.keys(AXOM.getLesson(id).done).length, steps = info[id].steps;
    if (doneTest(id)) return { s: "done", id, done, steps };
    const prevIds = Object.keys(byNo).map(Number).filter((n) => n < k.n);
    const prev = prevIds.length ? byNo[Math.max(...prevIds)] : null;
    return { s: UNLOCK_ALL || !prev || doneTest(prev) ? "open" : "locked", id, done, steps };
  };
  const tabs = `<div class="tabs home-tabs" role="tablist">${TABS.map(([k, t]) => `<button class="tab ${UI.tab === k ? "on" : ""}" data-tab="${k}">${T(t)}</button>`).join("")}</div>`;
  const worksheet = {
    "assam-geography": "assam-geography-atlas.html",
    "geography-foundations": "geography-foundations-atlas.html",
  }[course.id];
  const hero = `<section class="c-hero">${ROOF}<a class="back-hub" href="${S && S.id !== "assam-history" ? `index.html?subject=${S.id}` : "index.html"}">‹ ${S && S.id !== "assam-history" ? T(S.title) : T(B("Home", "মূল পৃষ্ঠা"))}</a><div class="eyebrow">${T(course.eyebrow)}</div><h1>${T(course.title)}</h1><p>${T(course.subtitle)}</p>${worksheet ? `<a class="back-hub" href="content/${worksheet}">${T(B("Opening and final atlas worksheet", "আৰম্ভণি আৰু শেষৰ মানচিত্ৰ অনুশীলন"))}</a>` : ""}</section>`;
  const body = { lessons: lessonsTab, timeline: timelineTab, family: familyTab, profile: profileTab, overview: lessonsTab, skills: skillsTab }[UI.tab](status, byNo);
  $("#course").innerHTML = hero + tabs + (CID === "assam-history" ? `<a class="offline-btn reference-link" href="history.html">${T(B("Timeline,people and places", "সময়ৰেখা,মানুহ আৰু ঠাই"))} ›</a>` : "") + body + `<div class="p-foot">${T(B("Bilingual · English / অসমীয়া · Sources accompany each lesson. Illustrations are artistic reconstructions.", "দ্বিভাষিক · English / অসমীয়া · প্ৰতিটো পাঠৰ লগত উৎস দিয়া আছে। চিত্ৰবোৰ শিল্পীৰ কল্পনা।"))}</div>`;
  // sticky Continue: the next open lesson that is not finished
  const next = course.kings.map((k) => ({ k, st: status(k) })).find((x) => x.st.s === "open");
  const c = $("#continue");
  if (next && UI.tab === "lessons") { c.href = `lesson.html?id=${next.st.id}`; c.innerHTML = `<span>${T(B("Continue", "আগবাঢ়া"))}</span><b>${T(B(`Lesson ${next.k.n} · ${next.k.name.en.split(" (")[0]}`, `পাঠ ${asNum(next.k.n)} · ${next.k.name.as}`))}</b>`; c.classList.remove("hidden"); }
  else c.classList.add("hidden");
}

/* ---------- Lessons tab ---------- */
function lessonsTab(status) {
  const curEra = (course.eras.find((e) => course.kings.some((k) => k.n >= e.from && k.n <= e.to && status(k).s === "open")) || course.eras[0]).id;
  return reviewCard() + course.eras.map((e) => {
    const kings = course.kings.filter((k) => k.n >= e.from && k.n <= e.to);
    const sts = kings.map(status), avail = sts.filter((x) => x.s !== "soon"), done = sts.filter((x) => x.s === "done").length;
    const open = UI.open[e.id] ?? (CID === "assam-history" ? false : e.id === curEra);
    const word = course.eraWord || B("era", "যুগ"), cpDone = !!G.checkpoints[e.id], cpOpen = avail.length && avail.every((x) => x.s === "done");
    const checkpoint = avail.length ? `<div class="cp-card ${cpDone ? "done" : cpOpen ? "open" : ""}">
        <span class="ic">${cpDone ? ICON.check : "🏁"}</span>
        <span><b>${T(B(`${word.en[0].toUpperCase()}${word.en.slice(1)} checkpoint`, `${word.as}ৰ পৰীক্ষা`))}</b><span class="s">${cpDone ? T(B("Passed", "উত্তীৰ্ণ")) : cpOpen ? T(B("15 exam-style questions · pass mark 80%", "পৰীক্ষাৰ ধৰণৰ ১৫টা প্ৰশ্ন · উত্তীৰ্ণ নম্বৰ ৮০%")) : T(B(`Opens when this ${word.en}'s lessons are done`, `এই ${word.as}ৰ পাঠবোৰ শেষ হ'লে খোল খাব`))}</span></span>
        ${cpOpen || cpDone ? `<a class="cp-go" href="lesson.html?checkpoint=${e.id}&course=${CID}">${cpDone ? T(B("Retake", "আকৌ")) : T(B("Start", "আৰম্ভ"))}</a>` : `<a class="cp-skip" href="lesson.html?checkpoint=${e.id}&course=${CID}&testout=1">${T(B("Test out", "পৰীক্ষা দি আগবাঢ়া"))}</a>`}
      </div>` : "";
    return `<section class="era-sec ${open ? "open" : ""}">
      <button class="era-head" data-era="${e.id}"><span class="t">${T(e.title)}</span><span class="p">${T(B(`${done}/${kings.length} lessons`, `${asNum(kings.length)}টাৰ ${asNum(done)}টা পাঠ`))}</span><span class="chev">${ICON.chevron}</span>
        <span class="era-bar"><i style="--p:${(done / kings.length) * 100}%;width:${(done / kings.length) * 100}%"></i></span></button>
      <div class="kings">${open ? kings.map((k, i) => card(k, sts[i])).join("") + checkpoint : ""}</div>
    </section>`;
  }).join("");
}
const LABEL = { done: B("Review", "পুনৰীক্ষণ"), open: B("Start", "আৰম্ভ"), locked: B("Jump here", "ইয়ালৈ জঁপিওৱা"), soon: B("Soon", "সোনকালে") };
function card(k, st) {
  const started = st.s === "open" && st.done > 0, miss = st.id ? (G.mistakes[st.id] || []).length : 0;
  // a locked lesson opens its page, which offers the jump test (passing it unlocks the lesson)
  const href = st.s === "open" || st.s === "done" ? `lesson.html?id=${st.id}` : st.s === "locked" ? `lesson.html?id=${st.id}` : "", tag = href ? "a" : "div";
  return `<${tag} class="king ${st.s} tier-${k.tier}" ${href ? `href="${href}"` : `data-why="${st.s}"`}>
    <span class="face"><img src="${AXOM.media(k.face)}" alt="" loading="lazy"></span><span class="n">${N(k.n)}</span>
    <span class="who"><b>${T(k.name)}</b><span class="sub2">${N(k.reign)} · <span class="stars" title="Exam importance">${STAR[k.tier]}</span></span>
      ${started ? `<span class="bar2"><i style="--p:${(st.done / st.steps) * 100}%;width:${(st.done / st.steps) * 100}%"></i></span>` : ""}</span>
    <span class="state">${started ? T(B("Continue", "আগবাঢ়া")) : T(LABEL[st.s])}</span>
    ${miss ? `<span class="badge">${T(B(`${miss} to revise`, `${asNum(miss)}টা ভুল`))}</span>` : ""}
  </${tag}>`;
}

/* ---------- Timeline tab: every reign as a bar ---------- */
function timelineTab(status) {
  const spans = course.kings.map((k) => [k, ...years(k.reign)]);
  const longest = Math.max(...spans.map(([, a, b]) => b - a || 1));
  let prevEnd = null, html = "";
  course.eras.forEach((e) => {
    html += `<div class="era">${T(e.title)}</div><div class="tl-list">`;
    spans.filter(([k]) => k.n >= e.from && k.n <= e.to).forEach(([k, a, b]) => {
      if (prevEnd && a > prevEnd) html += `<div class="tl-gap">${T(B(`${prevEnd}–${a} · no king (interregnum)`, `${asNum(prevEnd)}–${asNum(a)} · ৰজা নাছিল`))}</div>`;
      prevEnd = Math.max(prevEnd || 0, b);
      const st = status(k), link = st.s === "open" || st.s === "done", tag = link ? "a" : "div";
      html += `<${tag} class="tl-row tier-${k.tier}" ${link ? `href="lesson.html?id=${st.id}"` : ""}><span class="y">${N(a)}</span><span class="nm">${T(k.name)}</span>
        <span class="tl-bar"><i style="--p:${Math.max(3, ((b - a || 1) / longest) * 100)}%;width:${Math.max(3, ((b - a || 1) / longest) * 100)}%"></i></span><span class="len">${N(b - a || 1)}${T(B("y", "ব"))}</span></${tag}>`;
    });
    html += `</div>`;
  });
  return `<p class="tab-intro">${T(B("Bar length shows how long each king ruled. Gaps mark periods with no king.", "দণ্ডৰ দৈৰ্ঘ্যই ৰাজত্বকালৰ দৈৰ্ঘ্য দেখুৱায়। খালী ঠাইবোৰ ৰজা নথকা সময়।"))}</p>` + html;
}

/* ---------- Family tab: succession and relations ---------- */
function familyTab() {
  const people = course.rulers || course.kings;
  let prev = null;
  const rows = people.map((k) => {
    const r = k.rel || {}, linked = prev && r.of === prev.id && (r.type === "son" || r.type === "brother");
    const line = !prev ? "" : linked ? (r.type === "son" ? "son" : "brother") : "break";
    prev = k;
    return `<div class="fam-row ${line}"><span class="fam-face"><img src="${AXOM.media(k.face)}" alt="" loading="lazy"></span>
      <span class="fam-txt"><b>${N(k.n)}. ${T(k.name)}</b><span class="rel rel-${r.type || "other"}">${T(r.t || B("", ""))}</span></span></div>`;
  }).join("");
  return `<p class="tab-intro">${T(course.familyIntro || B("A solid line: son of the king above. A dashed line: brother. A gap: the throne passed outside the direct line.", "সৰল ৰেখা: ওপৰৰ ৰজাৰ পুত্ৰ। ডেচ ৰেখা: ভাই। খালী: সিংহাসন পোনপটীয়া বংশৰ বাহিৰলৈ গ'ল।"))}</p><div class="fam">${rows}</div>
    <p class="tab-intro small">${T(course.familyNote || B("Relations follow the AHOM project catalogue; some early details differ between chronicles.", "সম্পৰ্কবোৰ AHOM প্ৰকল্পৰ তালিকা অনুসৰি; আগৰ কিছুমান তথ্য বুৰঞ্জী অনুসৰি বেলেগ।"))}</p>`;
}

/* ---------- My map: every skill in the syllabus, what is weak and what to do next ---------- */
const SK_STATE = { new: B("Not tested", "পৰীক্ষা হোৱা নাই"), weak: B("Weak", "দুৰ্বল"), learning: B("Learning", "শিকি আছে"), ready: B("Ready", "সাজু"), strong: B("Strong", "দৃঢ়"), rusty: B("Rusty", "পাহৰিছে") };
function skillsTab() {
  const map = Object.fromEntries(SKILLS.skills.map((x) => [x.id, x]));
  const canDrill = (x) => x.steps.length > 0, state = (x) => AXOM.skillState(x.id);
  const weak = SKILLS.skills.filter((x) => ["weak", "rusty"].includes(state(x))).sort((a, b) => G.skills[a.id].p - G.skills[b.id].p);
  const drill = (id) => `lesson.html?drill=${id}&course=${CID}`;
  const start = !G.checkpoints.diagnostic ? `<a class="review-card" href="lesson.html?diagnostic=${CID}"><span class="ic">🎯</span><span><b>${T(B("Find your starting point", "তোমাৰ আৰম্ভণি বিচাৰা"))}</b><span class="s">${T(B(`A short placement round across the whole syllabus · ${SKILLS.probes.length} questions at most`, `সমগ্ৰ পাঠ্যক্ৰমৰ চমু পৰ্যায় · সৰ্বাধিক ${asNum(SKILLS.probes.length)}টা প্ৰশ্ন`))}</span></span><span class="go">›</span></a>` : "";
  const next = weak.length ? (() => {
    const x = weak[0], root = AXOM.rootCause(x.id, map), fix = root ? map[root] : x;
    return `<div class="card focus"><h3>${T(B("Fix this next", "পিছত এইটো ঠিক কৰা"))}</h3><p class="big-skill">${T(fix.t)}</p>
      ${root ? `<p class="note">${T(B(`${x.t.en} depends on it.`, `${x.t.as} ইয়াৰ ওপৰত নিৰ্ভৰশীল।`))}</p>` : ""}
      ${canDrill(fix) ? `<a class="btn" href="${drill(fix.id)}">${T(B("Practise now", "এতিয়াই অনুশীলন কৰা"))}</a>` : `<p class="note">${T(B("The lesson for this skill is being written.", "এই দক্ষতাৰ পাঠটো লিখি থকা হৈছে।"))}</p>`}</div>`;
  })() : "";
  const patterns = Object.entries(G.miscon).filter(([tag]) => SKILLS.misconceptions[tag]).sort((a, b) => b[1].n - a[1].n).slice(0, 4);
  const slips = patterns.length ? `<div class="card"><h3>${T(B("Your repeated slips", "তোমাৰ বাৰে বাৰে হোৱা ভুল"))}</h3>${patterns.map(([tag, m]) => { const c = SKILLS.misconceptions[tag], x = map[c.skill]; return `<a class="acc-row" href="${x && canDrill(x) ? drill(c.skill) : "#"}"><span>${T(c.t)}</span><span class="note">×${N(m.n)}</span><b>›</b></a>`; }).join("")}</div>` : "";
  const legend = ["weak", "learning", "ready", "strong"].map((k) => `<span class="sk-chip ${k}">${T(SK_STATE[k])}</span>`).join("");
  const topics = SKILLS.topics.map((t) => {
    const list = SKILLS.skills.filter((x) => x.topic === t.id);
    return `<section class="sk-topic"><h3>${T(t.t)}${list.some(canDrill) ? "" : `<small>${T(B("Soon", "সোনকালে"))}</small>`}</h3><div class="sk-chips">${list.map((x) => { const st = state(x), r = G.skills[x.id], label = `<span class="sk-chip ${st}" title="${SK_STATE[st].en}">${T(x.t)}${r && r.a ? `<small>${N(Math.round(r.p * 100))}%</small>` : ""}</span>`; return canDrill(x) ? `<a href="${drill(x.id)}">${label}</a>` : label; }).join("")}</div></section>`;
  }).join("");
  return `${start}${next}${slips}<p class="tab-intro">${T(B("A skill turns strong only after you answer it correctly at least three days later. Hints and retries never count.", "কমেও তিনি দিনৰ পিছত শুদ্ধকৈ উত্তৰ দিলেহে দক্ষতা দৃঢ় হয়। ইংগিত আৰু পুনৰ চেষ্টা গণনা নহয়।"))}</p><div class="sk-chips sk-legend">${legend}</div>${topics}`;
}

/* ---------- Profile tab ---------- */
function profileTab(status, byNo) {
  const lessonIds = Object.values(byNo);
  const finished = lessonIds.filter((id) => AXOM.getLesson(id).done.test).length;
  const tot = Object.values(G.stats).reduce((a, s) => ({ a: a.a + s.a, o: a.o + s.o }), { a: 0, o: 0 });
  const acc = tot.a ? Math.round((tot.o / tot.a) * 100) : 0;
  const nameOf = (id) => (course.kings.find((k) => k.lesson === id) || { name: B(id, id) }).name;
  const perLesson = Object.entries(G.stats).filter(([id]) => info[id]).map(([id, s]) => ({ id, pct: Math.round((s.o / s.a) * 100), a: s.a })).sort((x, y) => x.pct - y.pct);
  const weak = perLesson.filter((x) => x.a >= 5 && x.pct < 80).slice(0, 3);
  return `<div class="pf-stats">
      <div class="stat" style="--c:var(--gold)"><div class="h">XP</div><div class="v">${N(G.xp)}</div></div>
      <div class="stat" style="--c:var(--terra)"><div class="h">${T(B("Streak", "ধাৰা"))}</div><div class="v">${N(AXOM.streakNow())}</div></div>
      <div class="stat" style="--c:var(--good)"><div class="h">${T(B("Accuracy", "শুদ্ধতা"))}</div><div class="v">${tot.a ? N(acc) + "%" : "–"}</div></div>
    </div>
    <div class="card"><h3>${T(B("Lessons finished", "সম্পূৰ্ণ পাঠ"))}</h3><p class="big-num">${N(finished)} <span>/ ${N(course.kings.length)}</span></p></div>
    <div class="card"><h3>${T(B("Last 5 weeks", "শেহতীয়া ৫ সপ্তাহ"))}</h3><div class="cal">${activity()}</div></div>
    ${perLesson.length ? `<div class="card"><h3>${T(B("Accuracy by lesson", "পাঠ অনুসৰি শুদ্ধতা"))}</h3>${perLesson.map((x) => `<a class="acc-row" href="lesson.html?id=${x.id}"><span>${T(nameOf(x.id))}</span><span class="acc-bar"><i style="--p:${x.pct}%;width:${x.pct}%" class="${x.pct < 60 ? "low" : x.pct < 80 ? "mid" : ""}"></i></span><b>${N(x.pct)}%</b></a>`).join("")}</div>` : ""}
    ${weak.length ? `<div class="card"><h3>${T(B("Revise next", "পিছত পুনৰ চোৱা"))}</h3>${weak.map((x) => `<a class="acc-row" href="lesson.html?id=${x.id}"><span>${T(nameOf(x.id))}</span><span class="note">${N(x.pct)}%</span><b>›</b></a>`).join("")}</div>` : ""}
    <div class="card"><h3>${T(B("Account", "একাউণ্ট"))}</h3><p class="note">${accountNote()}</p></div>`;
}

/* ---------- events ---------- */
document.addEventListener("click", (e) => {
  let b;
  if ((b = e.target.closest("[data-exam]"))) { UI.exam = b.dataset.exam; saveUI(); render(); return; }
  if (e.target.closest("[data-soon]")) return toast(T(B("This subject is being written. Coming soon!", "এই বিষয়টো লিখি থকা হৈছে। সোনকালে আহিব!")));
  if ((b = e.target.closest("[data-tab]"))) { if (CID === "assam-history" && b.dataset.tab === "lessons") { location.href = "index.html?course=assam-history"; return; } UI.tab = b.dataset.tab; saveUI(); render(); $("#scroll").scrollTop = 0; return; }
  if ((b = e.target.closest("[data-era]"))) { const id = b.dataset.era, sec = b.closest(".era-sec"); UI.open[id] = !sec.classList.contains("open"); saveUI(); render(); return; }
  if (e.target.closest("#settings")) return AXOM.openSettings(settingsExtra());
  if (e.target.closest("[data-why]")) toast(T(B("This lesson is being written", "এই পাঠটো লিখি থকা হৈছে")));
  if (e.target.closest("[data-close]")) $("#sheet-root").innerHTML = "";
  if (e.target.closest("#reset")) {
    if (!confirm("Reset all progress on this device?")) return;
    Object.keys(localStorage).filter((k) => k.startsWith("axom:")).forEach((k) => localStorage.removeItem(k));
    location.reload();
  }
});
function settingsExtra() {
  return `<div class="setting"><span>${T(B("Progress", "অগ্ৰগতি"))}</span><button class="link danger" id="reset">${T(B("Reset on this device", "এই ডিভাইচত মচা"))}</button></div>`;
}
$("#as").addEventListener("change", () => render());
AXOM.onSave(() => stats());

/* ---------- install the web app (Android/desktop Chrome, Edge) ---------- */
let installEvent = null;
window.addEventListener("beforeinstallprompt", (e) => { e.preventDefault(); installEvent = e; $("#install").classList.remove("hidden"); });
$("#install").addEventListener("click", async () => { if (!installEvent) return; installEvent.prompt(); await installEvent.userChoice; installEvent = null; $("#install").classList.add("hidden"); });

/* ---------- account (only when Firebase is configured in app/config.js) ---------- */
const auth = AXOM.auth;
function accountButton(user) {
  const b = $("#account");
  b.classList.remove("hidden");
  b.innerHTML = user && user.photo ? `<img class="avatar" src="${user.photo}" alt="">` : ICON.user;
  b.classList.toggle("signed-in", !!user);
}
if ((window.AXOM_CONFIG || {}).firebase) {
  accountButton(null);
  auth.onChange.push((user) => { accountButton(user); stats(); if (!DM || !user) { DM = null; render(); } });
  auth.onError.push((err) => { signInMsg = signInError(err); render(); });
  $("#account").addEventListener("click", async () => {
    if (!auth.signIn) return toast(T(B("Connecting…", "সংযোগ হৈ আছে…")));
    if (auth.user) {
      $("#sheet-root").innerHTML = `<div class="backdrop" data-close></div><div class="sheet left"><div class="grab"></div><h2>${auth.user.name || T(B("Signed in", "চাইন ইন কৰা হৈছে"))}</h2>
        <p class="note">${T(B("Your progress, XP, streak, reviews and mistakes are saved to your account and sync across devices.", "তোমাৰ অগ্ৰগতি, XP, ধাৰা, পুনৰীক্ষণ আৰু ভুলবোৰ একাউণ্টত সাঁচি থোৱা হয় আৰু সকলো ডিভাইচত মিলে।"))}</p>
        <button class="btn" id="signout">${T(B("Sign out", "চাইন আউট"))}</button><button class="link" data-close>${T(B("Close", "বন্ধ কৰা"))}</button></div>`;
      $("#signout").onclick = async () => { await auth.signOut(); $("#sheet-root").innerHTML = ""; toast(T(B("Signed out", "চাইন আউট হ'ল"))); };
    } else {
      if (VIEW !== "profile") { location.href = "index.html?view=profile"; return; }
      doSignIn();
    }
  });
}

/* When a new app version takes over, reload the course home once so it shows the update.
   (Lesson pages never reload by themselves, so a unit in progress is never lost.) */
if ("serviceWorker" in navigator && navigator.serviceWorker.controller) {
  let reloaded = false;
  navigator.serviceWorker.addEventListener("controllerchange", () => { if (!reloaded) { reloaded = true; location.reload(); } });
}

stats();
render().catch((e) => { $("#course").innerHTML = `<div class="load-error"><h2>${T(B("Could not load the course", "পাঠ্যক্ৰম খুলিব পৰা নগ'ল"))}</h2><p>${T(B("Check your internet connection and try again.", "ইণ্টাৰনেট সংযোগ পৰীক্ষা কৰি আকৌ চেষ্টা কৰা।"))}</p></div>`; console.warn(e); });
})();
