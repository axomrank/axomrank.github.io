/* =========================================================
   AxomRank lesson engine
   lesson.html?id=<lesson>           one lesson: path of units + lesson test
   lesson.html?review=1              daily review across all lessons (spaced repetition + mistakes)
   lesson.html?checkpoint=<era>      era checkpoint (&testout=1 to skip the era's lessons)
   lesson.html?jump=<lesson>         test on the unfinished lessons before <lesson>; pass to skip to it
   Shared data: content/entities.json (names, places, terms), content/maps/assam.json (base map),
   content/questions/ahom.json (exam question bank).
   ========================================================= */
(() => {
"use strict";
const { B, N, asNum, G, SFX, media } = window.AXOM;
const MATH = window.AXOM_MATH;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const shuffle = (a) => { const b = a.slice(); for (let i = b.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [b[i], b[j]] = [b[j], b[i]]; } return b; };
const shuffledIdx = (n) => { let s; do { s = shuffle([...Array(n).keys()]); } while (n > 1 && s.every((v, k) => v === k)); return s; };
const params = new URLSearchParams(location.search);
// reviewer mode: ?review=1 turns it on (remembered on this device), ?review=0 turns it off; ?all works for one page
if (params.has("review")) { try { params.get("review") === "0" ? localStorage.removeItem("axom.review") : localStorage.setItem("axom.review", "1"); } catch { /* storage blocked */ } }
const UNLOCK_ALL = params.has("all") || (() => { try { return localStorage.getItem("axom.review") === "1"; } catch { return false; } })();

/* ---------- shared names list: [[id]] or [[id|text]] inside lesson text ---------- */
let ENT = {}, REFERENCE_LESSONS = {};
const MARK = /\[\[([a-z0-9-]+)(?:\|([^\]]+))?\]\]/g;
const entText = (lang, id, text) => text || (ENT[id] ? ENT[id].name[lang] : id);
const plain = (str, lang) => String(str).replace(MARK, (m, id, text) => entText(lang, id, text));
const rich = (str, lang) => String(str).replace(MARK, (m, id, text) => `<button class="ent" data-ent="${id}">${entText(lang, id, text)}</button>`);
// T: bilingual text with names as plain words. TR: names become tappable.
const T = (o) => (o == null ? "" : typeof o === "string" ? o : `<span class="en">${plain(o.en, "en")}</span><span class="as">${plain(o.as, "as")}</span>`);
const TR = (o) => (o == null ? "" : typeof o === "string" ? o : `<span class="en">${rich(o.en, "en")}</span><span class="as">${rich(o.as, "as")}</span>`);

/* ---------- loading ---------- */
async function load() {
  try {
    const [entities, basemap, manifest, india] = await Promise.all([AXOM.getJSON("content/entities.json"), AXOM.getJSON("content/maps/assam.json"), AXOM.getJSON("content/manifest.json"), AXOM.getJSON("content/maps/india.json").catch(() => null)]);
    REFERENCE_LESSONS = manifest.lessons;
    ENT = entities; BASES = { assam: basemap, india: india || basemap };
    if (params.has("review")) return boot(await buildReview(), "review");
    if (params.get("diagnostic")) { CID = params.get("diagnostic").replace(/[^a-z0-9-]/g, ""); return boot(await buildDiagnostic(), "diagnostic"); }
    if (params.get("drill")) { CID = (params.get("course") || "mathematics").replace(/[^a-z0-9-]/g, ""); return boot(await buildDrill(params.get("drill").replace(/[^a-z0-9-]/g, "")), "drill"); }
    if (params.get("checkpoint")) { CID = (params.get("course") || "ahom-kings").replace(/[^a-z0-9-]/g, ""); if (!manifest.courses.some(c=>c.id===CID)) CID = manifest.courseRedirects?.[CID] || CID; return boot(await buildCheckpoint(params.get("checkpoint").replace(/[^a-z-]/g, "")), "checkpoint"); }
    if (params.get("jump")) { const t = params.get("jump").replace(/[^a-z0-9-]/g, ""); CID = ((await AXOM.getJSON("content/manifest.json")).lessons[t] || {}).course || "ahom-kings"; return boot(await buildJump(t), "jump"); }
    const id = (params.get("id") || "sukaphaa").replace(/[^a-z0-9-]/g, "");
    const L = await AXOM.getJSON(`content/lessons/${id}.json`);
    // Old downloaded lesson JSON keeps working after consolidation.
    const current = manifest.lessons[L.id];
    CID = current?.course || L.course || "ahom-kings";
    if (current) { L.course = CID; L.no = current.no; }
    NEXT = await nextLesson(L.no).catch(() => null);
    GATE = UNLOCK_ALL ? null : await lessonGate(L).catch(() => null);
    COURSE = await coursePath().catch(() => []);
    boot(L, "lesson");
  } catch (e) {
    document.body.insertAdjacentHTML("afterbegin", `<div class="stage"><div class="device"><div class="load-error"><h2>${T(B("This lesson could not be opened", "পাঠটো খুলিব পৰা নগ'ল"))}</h2><p>${T(B("Check your internet connection, or download the lesson for offline use when you are online.", "ইণ্টাৰনেট সংযোগ পৰীক্ষা কৰা, বা অনলাইন থকাৰ সময়ত পাঠটো অফলাইনৰ বাবে ডাউনলোড কৰি ৰাখা।"))}</p><a class="btn" href="index.html">${T(B("All lessons", "সকলো পাঠ"))}</a></div></div></div>`);
    console.warn(e);
  }
}
// A step taken from another lesson keeps that lesson's id (for images, maps, progress)
const tagStep = (s, Lsrc) => ({ ...s, _lesson: Lsrc.id, _map: Lsrc.map });
async function lessonsById(ids) {
  const out = {};
  await Promise.all([...new Set(ids)].map(async (id) => { try { out[id] = await AXOM.getJSON(`content/lessons/${id}.json`); } catch { /* not available offline */ } }));
  return out;
}
async function buildReview() {
  const queue = AXOM.dailyReviewQueue();
  const lessons = await lessonsById(queue.map((q) => q.l));
  const steps = [];
  for (const q of queue) {
    const Ls = lessons[q.l]; if (!Ls) continue;
    const s = [...Ls.units, Ls.test].flatMap((u) => u.steps).find((x) => x.id === q.id);
    if (s && s.type !== "story") steps.push(tagStep(s, Ls));
  }
  return { id: "review", virtual: true, king: B("Daily memory mission", "দৈনিক স্মৃতি অভিযান"), reign: B(`${steps.length} clues this round`, `এই পৰ্যায়ত ${asNum(steps.length)}টা সংকেত`), units: [],
    test: { id: "review", title: B("Daily memory mission", "দৈনিক স্মৃতি অভিযান"), learned: [], steps } };
}
// the course in order, keeping only kings whose lesson is published
let CID = "ahom-kings";   // the course this page belongs to
const courseUrl = () => `content/courses/${CID}.json`;
async function publishedKings() {
  const [course, manifest] = await Promise.all([AXOM.getJSON(courseUrl()), AXOM.getJSON("content/manifest.json")]);
  return course.kings.filter((k) => k.lesson && manifest.lessons[k.lesson]);
}
let NEXT = null;   // the lesson after this one: { id, n, name }
let pendingUpdate = false;   // a new app version took over while a unit was being played; reload on the way back to the path
let GATE = null;
let COURSE_TITLE = null;
let COURSE = [];   // every published lesson in course order, with unit summaries from the manifest: the whole path
async function coursePath() {
  const [course, manifest] = await Promise.all([AXOM.getJSON(courseUrl()), AXOM.getJSON("content/manifest.json")]);
  COURSE_TITLE = course.title;
  return course.kings.filter((k) => k.lesson && manifest.lessons[k.lesson] && manifest.lessons[k.lesson].units)
    .map((k) => ({ n: k.n, id: k.lesson, name: k.name, face: k.face, reign: k.reign, units: manifest.lessons[k.lesson].units }));
}   // the earlier lesson that must be finished before this one opens: { id, n, name }, or null
async function lessonGate(L) {
  if (UNLOCK_ALL || AXOM.getLesson(L.id).done.test) return null;
  const prev = (await publishedKings()).filter((k) => k.n < L.no).pop();
  return prev && !AXOM.getLesson(prev.lesson).done.test ? { id: prev.lesson, n: prev.n, name: prev.name } : null;
}
async function nextLesson(no) {
  const k = (await publishedKings()).find((x) => x.n > no);
  return k ? { id: k.lesson, n: k.n, name: k.name } : null;
}
// Jump ahead: questions from the tests of every unfinished lesson before the target; pass to mark them complete
async function buildJump(target) {
  const kings = await publishedKings(), t = kings.find((k) => k.lesson === target);
  const skip = kings.filter((k) => k.n < t.n && !AXOM.getLesson(k.lesson).done.test).map((k) => k.lesson);
  const lessons = await lessonsById(skip);
  const per = Math.max(2, Math.ceil(15 / Math.max(1, skip.length)));
  const steps = shuffle(skip.flatMap((id) => (lessons[id] ? shuffle(lessons[id].test.steps.filter((s) => s.type !== "story")).slice(0, per).map((s) => tagStep(s, lessons[id])) : [])))
    .slice(0, Math.min(24, Math.max(15, skip.length * 2)));
  const eraUnits = Object.fromEntries(Object.entries(lessons).map(([id, Ls]) => [id, [...Ls.units.map((u) => u.id), "test"]]));
  return { id: `jump-${target}`, virtual: true, eraUnits, target: { id: target, n: t.n, name: t.name }, king: B("Jump ahead", "আগলৈ জঁপিওৱা"),
    reign: B(`To lesson ${t.n} · ${t.name.en}`, `পাঠ ${asNum(t.n)} · ${t.name.as}লৈ`), units: [],
    test: { id: "jump", title: B(`Jump to lesson ${t.n} · ${t.name.en}`, `পাঠ ${asNum(t.n)} · ${t.name.as}লৈ জঁপিওৱা`), learned: [], steps } };
}
/* ---------- skill courses: a course may name a skills file (content/skills/<course>.json) ---------- */
async function skillData() {
  const course = await AXOM.getJSON(courseUrl()), data = await AXOM.getJSON(course.skills);
  return { ...data, map: Object.fromEntries(data.skills.map((x) => [x.id, x])) };
}
// Placement: one or two probes per skill, foundations first. A miss removes probes that depend on that skill.
async function buildDiagnostic() {
  const data = await skillData(), order = new Map(data.skills.map((x, k) => [x.id, k]));
  const steps = data.probes.slice().sort((a, b) => order.get(a.skill) - order.get(b.skill)).map((s) => ({ ...s, _bank: true }));
  return { id: "diagnostic", virtual: true, skillMap: data.map, skillList: data.skills, king: B("Find your starting point", "তোমাৰ আৰম্ভণি বিচাৰা"), reign: B("Placement round", "স্থান নিৰ্ণয় পৰ্যায়"), units: [],
    test: { id: "diagnostic", title: B("Find your starting point", "তোমাৰ আৰম্ভণি বিচাৰা"), learned: [], steps } };
}
// Repair round for one skill. If a prerequisite is the real gap, that comes first.
async function buildDrill(skillId) {
  const data = await skillData(), skill = data.map[skillId];
  if (!skill) return { id: "drill", virtual: true, king: B("Practice", "অনুশীলন"), reign: B("", ""), units: [], test: { id: "drill", title: B("Practice", "অনুশীলন"), learned: [], steps: [] } };
  const root = AXOM.rootCause(skillId, data.map);
  const refs = [...(root ? shuffle(data.map[root].steps).slice(0, 3) : []), ...shuffle(skill.steps).slice(0, root ? 4 : 7)];
  const lessons = await lessonsById(refs.map((r) => r.l));
  const steps = refs.flatMap((r) => { const Ls = lessons[r.l]; const st = Ls && [...Ls.units, Ls.test].flatMap((u) => u.steps).find((x) => x.id === r.id); return st ? [tagStep(st, Ls)] : []; });
  return { id: `drill-${skillId}`, virtual: true, king: skill.t, reign: root ? B(`Starting with ${data.map[root].t.en}`, `${data.map[root].t.as}ৰ পৰা আৰম্ভ`) : B("Focused practice", "নিৰ্দিষ্ট অনুশীলন"), units: [],
    test: { id: "drill", title: skill.t, learned: [], steps } };
}
async function buildCheckpoint(eraId) {
  const course = await AXOM.getJSON(courseUrl());
  const [manifest, bank] = await Promise.all([AXOM.getJSON("content/manifest.json"), AXOM.getJSON(course.bank || "content/questions/ahom.json")]);
  const era = course.eras.find((e) => e.id === eraId);
  const ids = course.kings.filter((k) => k.n >= era.from && k.n <= era.to && k.lesson && manifest.lessons[k.lesson]).map((k) => k.lesson);
  const lessons = await lessonsById(ids);
  const per = Math.max(3, Math.ceil(6 / Math.max(1, ids.length)));
  const fromTests = ids.flatMap((id) => (lessons[id] ? shuffle(lessons[id].test.steps.filter((s) => s.type !== "story")).slice(0, per).map((s) => tagStep(s, lessons[id])) : []));
  const asked = new Set(fromTests.map((s) => s.id));
  const fromBank = bank.questions.filter((q) => q.era === eraId && lessons[q.lesson] && !asked.has(q.source_step)).map((q) => ({ ...tagStep(q, lessons[q.lesson]), _bank: true }));
  const steps = shuffle([...shuffle(fromBank).slice(0, 10), ...fromTests]).slice(0, 15);
  const eraUnits = Object.fromEntries(Object.entries(lessons).map(([id, Ls]) => [id, [...Ls.units.map((u) => u.id), "test"]]));
  const word = course.eraWord || B("era", "যুগ");
  return { id: `checkpoint-${eraId}`, virtual: true, era, word, eraUnits, king: B(`${word.en[0].toUpperCase()}${word.en.slice(1)} checkpoint`, `${word.as}ৰ পৰীক্ষা`), reign: era.title, units: [],
    test: { id: "checkpoint", title: era.title, learned: [], steps } };
}

/* ---------- base map (real district + river shapes from the KMZ) ---------- */
let BASES = { assam: { districts: {}, rivers: {}, ridges: {} } };
function smoothPath(pts) {
  if (pts.length < 3) return `M${pts.map((p) => p.join(" ")).join(" L")}`;
  let d = `M${pts[0][0].toFixed(1)} ${pts[0][1].toFixed(1)}`;
  for (let i = 1; i < pts.length - 1; i++) {
    const mx = (pts[i][0] + pts[i + 1][0]) / 2, my = (pts[i][1] + pts[i + 1][1]) / 2;
    d += ` Q${pts[i][0].toFixed(1)} ${pts[i][1].toFixed(1)} ${mx.toFixed(1)} ${my.toFixed(1)}`;
  }
  const l = pts[pts.length - 1];
  return d + ` L${l[0].toFixed(1)} ${l[1].toFixed(1)}`;
}
// spec: { base: "assam" or "india" (default assam), box: [lonMin, latMin, lonMax, latMax], show: [ids], routes: [[id or [lat,lon], ...]], texts: [{ t, at }], labels: { id: { pos, at, t } } }
function mapSVG(spec, { story = false, route = false, choices = [] } = {}) {
  const BASE = BASES[spec.base] || BASES.assam;
  const [lonMin, latMin, lonMax, latMax] = spec.box;
  const c = Math.cos(((latMin + latMax) / 2) * Math.PI / 180), k = 340 / ((lonMax - lonMin) * c);
  const W = 340, H = Math.round((latMax - latMin) * k);
  const P = ([lat, lon]) => [(lon - lonMin) * c * k, (latMax - lat) * k];
  const clamp = ([x, y]) => [Math.min(W - 14, Math.max(14, x)), Math.min(H - 14, Math.max(14, y))];
  const name = (id) => (ENT[id] ? ENT[id].name : { en: (BASE.rivers[id] || {}).name || id, as: (BASE.rivers[id] || {}).name || id });
  const OFF = { e: [10, 4, "start"], w: [-10, 4, "end"], n: [0, -11, "middle"], s: [0, 17, "middle"], ne: [8, -8, "start"], nw: [-8, -8, "end"], se: [8, 14, "start"], sw: [-8, 14, "end"] };
  const label = (id, [x, y], fallback, cls = "place") => {
    const o = (spec.labels || {})[id] || {}, [dx, dy, anchor] = OFF[o.pos || fallback], t = o.t || name(id);
    return `<text class="lbl ${cls}" x="${(x + dx).toFixed(1)}" y="${(y + dy).toFixed(1)}" text-anchor="${anchor}"><tspan class="en">${t.en}</tspan></text><text class="lbl ${cls} as" x="${(x + dx).toFixed(1)}" y="${(y + dy).toFixed(1)}" text-anchor="${anchor}">${t.as}</text>`;
  };
  const show = new Set(spec.show || []), isChoice = (id) => choices.includes(id);
  // label anchor: labels[id].at = [lat, lon] on the map, or a fraction (0–1) along the line
  // a fraction counts along the part of the line that is inside the frame, so a long river is named where you can see it
  const labelAt = (id, pts, def) => {
    const at = ((spec.labels || {})[id] || {}).at; if (Array.isArray(at)) return P(at);
    const vis = pts.filter(([x, y]) => x >= 20 && x <= W - 20 && y >= 20 && y <= H - 20), use = vis.length ? vis : pts;
    return clamp(use[Math.round((use.length - 1) * (at ?? def))]);
  };
  let out = `<svg class="map" viewBox="0 0 ${W} ${H}" role="img" aria-label="Map"><defs><marker id="arrowhead" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--terra)"/></marker><clipPath id="mapclip"><rect width="${W}" height="${H}" rx="18"/></clipPath></defs><g clip-path="url(#mapclip)"><rect class="sea" width="${W}" height="${H}"/>`;
  // present-day districts: always drawn faintly; a lesson can name some (spec.districts) to help place the story today
  const ringPath = (r, cls) => `<path class="${cls}" d="M${r.map((p) => P(p).map((v) => v.toFixed(1)).join(" ")).join(" L")} Z"/>`;
  // neighbours first, so India's own outline is what shows along its border
  (BASE.land || []).forEach((r) => (out += ringPath(r, "neighbour")));
  (BASE.outline || []).forEach((r) => (out += ringPath(r, "outline")));
  const named = new Set(spec.districts || []);
  Object.entries(BASE.districts).forEach(([id, d]) => d.rings.forEach((r) => (out += `<path class="district${named.has(id) ? " named" : ""}" d="M${r.map((p) => P(p).map((v) => v.toFixed(1)).join(" ")).join(" L")} Z"/>`)));
  const dlabels = [...named].filter((id) => BASE.districts[id]).map((id) => {
    const ring = BASE.districts[id].rings.reduce((a, r) => (r.length > a.length ? r : a), []);
    const c = ring.reduce((a, p) => [a[0] + p[0] / ring.length, a[1] + p[1] / ring.length], [0, 0]), [x, y] = P(c);
    const nm = BASE.districts[id].name, as = BASE.districts[id].as || nm;
    return `<text class="lbl dlbl" x="${x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="middle"><tspan class="en">${nm}</tspan></text><text class="lbl dlbl as" x="${x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="middle">${as}</text>`;
  }).join("");
  if (story) (spec.texts || []).forEach((t) => { const [x, y] = P(t.at); out += `<text class="lbl big" x="${x.toFixed(1)}" y="${y.toFixed(1)}"><tspan class="en">${t.t.en}</tspan></text><text class="lbl big as" x="${x.toFixed(1)}" y="${y.toFixed(1)}">${t.t.as}</text>`; });
  Object.entries(BASE.rivers).forEach(([id, r]) => {
    const main = id === "brahmaputra", pts = r.pts.map(P);
    out += `<path class="river${main ? " main" : show.has(id) ? "" : " faint"}" d="${smoothPath(pts)}"/>`;
    if (!show.has(id)) return;
    if (isChoice(id) && !story) out += `<g class="hit" data-place="${id}"><path class="zone" d="${smoothPath(pts)}"/></g>`;
    out += label(id, labelAt(id, pts, 0.5), "e", "river-lbl");   // map questions name every choice too
  });
  Object.entries(BASE.ridges).forEach(([id, line]) => {
    if (!show.has(id)) return;
    const pts = line.map(P); let peaks = "";
    for (let i = 0; i < pts.length - 1; i++) { const [x1, y1] = pts[i], [x2, y2] = pts[i + 1], n = Math.max(1, Math.round(Math.hypot(x2 - x1, y2 - y1) / 22)); for (let j = 0; j < n; j++) { const x = x1 + ((x2 - x1) * j) / n, y = y1 + ((y2 - y1) * j) / n; peaks += `<path d="M${(x - 12).toFixed(1)} ${(y + 8).toFixed(1)} L${x.toFixed(1)} ${(y - 11).toFixed(1)} L${(x + 12).toFixed(1)} ${(y + 8).toFixed(1)} Z"/>`; } }
    out += `<g class="hills">${peaks}</g>`;
    if (isChoice(id) && !story) out += `<g class="hit" data-place="${id}"><path class="zone" d="M${pts.map((p) => p.join(" ")).join(" L")}"/></g>`;
    out += label(id, labelAt(id, pts, 0.5), "w");
  });
  if (story && route) (spec.routes || []).forEach((r) => { const pts = r.map((ref) => (Array.isArray(ref) ? P(ref) : clamp(P(ENT[ref].geo)))); out += `<path class="route" d="${smoothPath(pts)}" marker-end="url(#arrowhead)"/>`; });
  out += dlabels;
  [...show].filter((id) => ENT[id] && ENT[id].geo).forEach((id) => {
    const e = ENT[id], [x, y] = clamp(P(e.geo)), pass = e.type === "pass";
    if (!story && !isChoice(id) && !pass) return;
    if (isChoice(id) && !story) { out += `<g class="hit${pass ? " pass-hit" : ""}" data-place="${id}"><circle class="ring" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="17"/><circle class="${pass ? "pass" : "dot"}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${pass ? 8 : 7}"/></g>`; return; }
    out += pass ? `<circle class="pass-glow" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="13"/><circle class="pass" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="8"/><path class="pass-mark" d="M${(x - 4).toFixed(1)} ${(y + 3).toFixed(1)} L${x.toFixed(1)} ${(y - 3).toFixed(1)} L${(x + 4).toFixed(1)} ${(y + 3).toFixed(1)}"/>`
      : `<circle class="dot" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="6"/>`;
    if (story || isChoice(id) || (pass && !choices.length)) out += label(id, [x, y], "e", pass ? "place passlbl" : "place");
  });
  const note = BASE.outline ? B("Today's India, not historical borders; places approximate. Map data:", "আজিৰ ভাৰত, ঐতিহাসিক সীমা নহয়; ঠাইবোৰ আনুমানিক। মানচিত্ৰৰ তথ্য:") : B("Districts and rivers of today's Assam; places approximate", "আজিৰ অসমৰ জিলা আৰু নদী; ঠাইবোৰ আনুমানিক");
  const mapCredits = BASE.outline ? ` <a href="https://github.com/datameet/maps/tree/master/Country">DataMeet</a> · <a href="https://creativecommons.org/licenses/by-sa/2.5/">CC BY-SA 2.5</a> · <a href="https://www.naturalearthdata.com/about/terms-of-use/">Natural Earth</a>` : "";
  return out + `</g></svg><div class="map-note">${T(note)}${mapCredits}</div>`;
}

/* ========================================================= */
function boot(L, mode) {
const VIRTUAL = mode !== "lesson";
if (AXOM.notebook(L.course) || (["diagnostic", "drill"].includes(mode) && AXOM.notebook(CID))) document.documentElement.classList.add("maths");
const P = VIRTUAL ? { done: {} } : AXOM.getLesson(L.id);
const saveAll = () => (VIRTUAL ? AXOM.saveGlobal() : AXOM.saveLesson(L.id, P));
const bankOf = (lid) => (G.mistakes[lid] = G.mistakes[lid] || []);
const lessonOf = (s) => s._lesson || L.id;

/* ---------- icons and art ---------- */
const ICONS = {
  walk: '<svg viewBox="0 0 24 24"><circle cx="13" cy="4" r="2"/><path d="M10 22l2-6-3-3 1-5 4 3h3M9 8l-3 3"/></svg>',
  home: '<svg viewBox="0 0 24 24"><path d="M3 11l9-7 9 7M5 10v10h14V10"/><path d="M10 20v-5h4v5"/></svg>',
  hands: '<svg viewBox="0 0 24 24"><path d="M8 13l3 3a2 2 0 0 0 3 0l5-5M2 12l4-4 4 2 3-2 4 2 5 2"/><path d="M6 8l-4 4 6 6"/></svg>',
  crown: '<svg viewBox="0 0 24 24"><path d="M3 8l4 4 5-7 5 7 4-4-2 11H5z"/></svg>',
  hill: '<svg viewBox="0 0 24 24"><path d="M2 20l7-11 4 6 3-4 6 9z"/><circle cx="17" cy="5" r="2"/></svg>',
  star: '<svg viewBox="0 0 24 24"><path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/></svg>',
  river: '<svg viewBox="0 0 24 24"><path d="M3 6c3 0 3 3 6 3s3-3 6-3 3 3 6 3M3 12c3 0 3 3 6 3s3-3 6-3 3 3 6 3M3 18c3 0 3 3 6 3"/></svg>',
  moon: '<svg viewBox="0 0 24 24"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></svg>',
  flag: '<svg viewBox="0 0 24 24"><path d="M5 21V4M5 4h11l-2 4 2 4H5"/></svg>',
  trophy: '<svg viewBox="0 0 24 24"><path d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H4a3 3 0 0 0 4 4M16 6h4a3 3 0 0 1-4 4M12 13v4M8 21h8M9 17h6"/></svg>',
  lock: '<svg viewBox="0 0 24 24"><rect x="5" y="11" width="14" height="10" rx="2.5"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
  done: '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" stroke-width="3.4"/></svg>',
};
const ART = {
  door: `<svg viewBox="0 0 200 150"><rect x="62" y="16" width="76" height="120" rx="4" fill="var(--surface)" stroke="var(--indigo)" stroke-width="3"/><path d="M70 24l42 12v96l-42-4z" fill="var(--terra)"/><circle cx="104" cy="84" r="4" fill="var(--gold)"/><path d="M120 136h48M32 136h30" stroke="var(--line-2)" stroke-width="3" stroke-linecap="round"/><path d="M126 76l34-22M126 84h40M126 92l34 22" stroke="var(--gold)" stroke-width="3" stroke-linecap="round"/></svg>`,
  court: `<svg viewBox="0 0 200 150"><path d="M100 18l70 34H30z" fill="var(--terra)"/><rect x="36" y="56" width="128" height="8" fill="var(--indigo)"/>${[50, 78, 106, 134].map((x) => `<rect x="${x}" y="68" width="16" height="48" rx="2" fill="var(--surface)" stroke="var(--line-2)" stroke-width="2"/>`).join("")}<rect x="28" y="118" width="144" height="8" fill="var(--indigo)"/><rect x="18" y="128" width="164" height="8" rx="2" fill="var(--gold)"/></svg>`,
  houses: `<svg viewBox="0 0 200 150"><path d="M20 100a38 38 0 0 1 76 0z" fill="var(--terra)"/><path d="M104 100a38 38 0 0 1 76 0z" fill="var(--indigo)"/><path d="M58 62v-14M142 62v-14" stroke="var(--gold)" stroke-width="4" stroke-linecap="round"/><path d="M20 108h76M104 108h76" stroke="var(--line-2)" stroke-width="4"/><path d="M78 126h44" stroke="var(--gold)" stroke-width="4" stroke-linecap="round"/><path d="M78 126l10-7M78 126l10 7M122 126l-10-7M122 126l-10 7" stroke="var(--gold)" stroke-width="4" stroke-linecap="round"/></svg>`,
  seal: `<svg viewBox="0 0 200 150"><rect x="48" y="16" width="104" height="118" rx="6" fill="var(--surface)" stroke="var(--line-2)" stroke-width="3"/>${[34, 48, 62, 76].map((y, i) => `<path d="M64 ${y}h${i % 2 ? 60 : 72}" stroke="var(--indigo)" stroke-width="4" stroke-linecap="round" opacity=".7"/>`).join("")}<circle cx="124" cy="106" r="18" fill="var(--terra)"/><path d="M115 106l7 7 12-14" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>`,
  scroll: `<svg viewBox="0 0 200 150"><rect x="44" y="32" width="112" height="86" rx="6" fill="var(--surface)" stroke="var(--terra)" stroke-width="3"/><rect x="30" y="26" width="18" height="98" rx="9" fill="var(--terra)"/><rect x="152" y="26" width="18" height="98" rx="9" fill="var(--terra)"/>${[50, 62, 74, 86, 98].map((y, i) => `<path d="M60 ${y}h${i % 2 ? 66 : 80}" stroke="var(--indigo)" stroke-width="4" stroke-linecap="round" opacity="${0.85 - i * 0.1}"/>`).join("")}<circle cx="132" cy="104" r="8" fill="var(--gold)"/></svg>`,
  calendar: `<svg viewBox="0 0 200 150"><rect x="50" y="22" width="100" height="112" rx="14" fill="var(--surface)" stroke="var(--line-2)" stroke-width="3"/><path d="M50 36a14 14 0 0 1 14-14h72a14 14 0 0 1 14 14v18H50z" fill="var(--terra)"/><rect x="72" y="12" width="8" height="22" rx="4" fill="var(--indigo)"/><rect x="120" y="12" width="8" height="22" rx="4" fill="var(--indigo)"/><text class="en" x="100" y="48" text-anchor="middle" font-family="Noto Sans, sans-serif" font-weight="900" font-size="14" fill="#fff" letter-spacing="2">DEC</text><text class="as" x="100" y="48" text-anchor="middle" font-family="Noto Sans Bengali, sans-serif" font-weight="800" font-size="14" fill="#fff">ডিচেম্বৰ</text><text class="en" x="100" y="114" text-anchor="middle" font-family="Noto Sans, sans-serif" font-weight="900" font-size="58" fill="var(--indigo)">2</text><text class="as" x="100" y="114" text-anchor="middle" font-family="Noto Sans Bengali, sans-serif" font-weight="800" font-size="58" fill="var(--indigo)">২</text></svg>`,
  rooster: `<svg viewBox="0 0 200 150" preserveAspectRatio="xMidYMid slice"><rect width="200" height="150" fill="#2E3170"/><circle cx="160" cy="34" r="22" fill="#F6E7C4" opacity=".18"/><circle cx="160" cy="34" r="15" fill="#F6E7C4"/>${[[30, 20], [70, 40], [120, 18], [40, 60], [180, 70], [95, 70]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="1.6" fill="#F6E7C4"/>`).join("")}<path d="M0 128c40-10 80-10 120-4s60 6 80 2v24H0z" fill="#1D1F4D"/><g transform="translate(62 54)"><path d="M30 70c-22 0-34-16-30-34 3-12 14-20 26-20 6-10 18-14 26-8l-4 6c8 0 12 6 10 12l-10-2c4 8 4 20-2 30" fill="var(--terra)"/><path d="M50 8c2-6 8-8 10-4-4 0-6 2-6 6z" fill="#D2483E"/><path d="M62 18l10 3-10 3z" fill="var(--gold)"/><circle cx="55" cy="16" r="2" fill="#1D1F4D"/><path d="M6 44c-10-6-16-20-8-30 2 10 8 16 14 18" fill="var(--gold)"/><path d="M24 70v12M36 68v14M18 82h10M30 82h12" stroke="var(--gold)" stroke-width="3" stroke-linecap="round"/></g><path d="M140 70q8-6 16 0M146 60q10-8 20 0" stroke="#F6E7C4" stroke-width="2" fill="none" stroke-linecap="round" opacity=".7"/></svg>`,
  embassy: `<svg viewBox="0 0 200 150"><path d="M20 120 C 60 60, 140 60, 180 120" fill="none" stroke="var(--terra)" stroke-width="4" stroke-dasharray="8 7" stroke-linecap="round"/><circle cx="20" cy="120" r="12" fill="var(--indigo)"/><circle cx="180" cy="120" r="12" fill="var(--gold)"/><rect x="82" y="44" width="36" height="26" rx="4" fill="var(--surface)" stroke="var(--terra)" stroke-width="3"/><path d="M82 46l18 14 18-14" fill="none" stroke="var(--terra)" stroke-width="3"/></svg>`,
};
const KICK = {
  mcq: B("Choose the correct answer", "শুদ্ধ উত্তৰটো বাছি লোৱা"), tf: B("True or false?", "শুদ্ধ নে অশুদ্ধ?"),
  map: B("Tap on the map", "মানচিত্ৰত টিপা"), unscramble: B("Unscramble", "সজাই লিখা"), inline: B("Complete the sentence", "বাক্যটো সম্পূৰ্ণ কৰা"),
  order: B("Put it in order", "ক্ৰম অনুসৰি সজোৱা"), match: B("Match the following", "মিলোৱা"), fill: B("Fill in the blank", "খালী ঠাই পূৰ কৰা"),
  odd: B("Odd one out", "অমিলটো বিচাৰা"), picture: B("Picture", "ছবি চিনাক্ত কৰা"), whoami: B("Who am I?", "মই কোন?"),
  spot: B("Spot the error", "ভুলটো বিচাৰা"), timeline: B("Timeline", "সময়ৰেখা"), story: B("Story", "কাহিনী"), articles: B("Article line", "অনুচ্ছেদৰ ৰেখা"),
  solve: B("Work it out", "হিচাপ কৰা"), explore: B("Try it", "নিজে চোৱা"), stepwise: B("Step by step", "খোজে খোজে"),
};
const PRAISE = [B("Correct!", "শুদ্ধ!"), B("Excellent!", "বঢ়িয়া!"), B("Well done!", "বহুত ভাল!"), B("Great!", "চমৎকাৰ!")];

/* ---------- page skeleton ---------- */
document.body.insertAdjacentHTML("afterbegin", `
<input type="checkbox" id="as" aria-label="Show in Assamese">
<div class="stage"><div class="device lesson-page${VIRTUAL ? " virtual" : ""}${L.mission && !VIRTUAL ? " has-mission" : ""}" id="device">
  <div class="confetti" id="confetti" aria-hidden="true"></div>
  <div class="view" id="v-path">
    <div class="p-top">
      <a class="icon-btn" href="index.html?course=${CID}" aria-label="All lessons">${AXOM.ICON.arrowBack}</a>
      <span class="top-title">${T(COURSE_TITLE || L.eyebrow || B("Lessons", "পাঠ"))}</span>
      <span class="spacer"></span>
      ${AXOM.LANG}
    </div>
    <div class="p-scroll">
      <section class="hero">
        <div class="txt">
          <h1>${T(L.king)}</h1>
          <div class="reign">${L.no ? T(B(`Lesson ${L.no}`, `পাঠ ${asNum(L.no)}`)) + " · " : ""}${T(L.reign)}</div>
          ${L.buildsOn ? `<a class="builds-on" href="lesson.html?id=${L.buildsOn.id}">${T(B(`Builds on Lesson ${L.buildsOn.no}: ${L.buildsOn.title.en}`, `পাঠ ${asNum(L.buildsOn.no)}ৰ ভেটিত: ${L.buildsOn.title.as}`))}</a>` : ""}
          <div class="hero-btns"><button class="offline-btn" id="guide">${AXOM.ICON.book}${T(B("Guidebook", "নিৰ্দেশিকা"))}</button><button class="offline-btn" id="offline"></button>${L.course === "assam-history" ? `<a class="offline-btn" href="index.html?course=assam-history&tab=overview">${T(B("Overview", "অৱলোকন"))}</a>` : ""}</div>
        </div>
        <div class="ring"><i id="meter"></i><div class="ring-t"><b id="count"></b><small>${T(B("Units complete", "অধ্যায় সম্পূৰ্ণ"))}</small></div></div>
      </section>
      <div id="mission-slot"></div>
      <div id="mistake-slot"></div>
      <div class="path" id="path"></div>
      ${AXOM.notebook(L.course) ? "" : `<div class="p-foot">${T(B("Paintings are artistic reconstructions.", "ছবিবোৰ শিল্পীৰ কল্পনা।"))}</div>`}
    </div>
    ${AXOM.nav("learn")}
  </div>
  <div class="view" id="v-empty"><div class="empty-pane">${AXOM.ICON.book}<p>${T(B("Choose a unit on the left to start.", "আৰম্ভ কৰিবলৈ বাওঁফালৰ পৰা এটা অধ্যায় বাছি লোৱা।"))}</p></div></div>
  <div class="view" id="v-play">
    <div class="top">
      <button class="close" id="exit" aria-label="Leave">${AXOM.ICON.close}</button>
      <div class="bar" id="bar"><i id="progress"></i></div>
      <span class="step-count" id="step-count"></span>
      <label class="lang mini" for="as"><span class="en">অ</span><span class="as">EN</span></label>
    </div>
    <div class="screen" id="screen"></div>
    <div class="foot" id="foot">
      <div class="fb" role="status" aria-live="polite">
        <div class="fb-head"><span class="fb-badge" id="fb-badge"></span><span id="fb-title"></span><span class="fb-xp" id="fb-xp"></span></div>
        <div class="fb-ans" id="fb-ans"></div>
        <div class="fb-why" id="fb-why"></div>
      </div>
      <button class="btn" id="action"></button>
    </div>
  </div>
  <div class="view" id="v-done">
    <div class="top done-top"><button class="close" id="done-x" aria-label="Back to lesson">${AXOM.ICON.close}</button><span class="spacer"></span>${AXOM.LANG}</div>
    <div class="done-wrap" id="done"></div>
    <div class="foot"><button class="btn" id="done-btn">${T(B("Continue", "আগবাঢ়া"))}</button><button class="btn-ghost hidden" id="done-back">${T(VIRTUAL ? B("Back to course", "পাঠ্যক্ৰমলৈ উভতি যোৱা") : B("Back to lesson", "পাঠলৈ উভতি যোৱা"))}</button></div>
  </div>
  <div id="sheet-root"></div>
</div></div>`);
AXOM.initLang();
const langBox = $("#as");
const isAS = () => langBox.checked;
document.title = L.no ? `${L.king.en} · Lesson ${L.no}` : `${L.king.en} · Axomrank`;

/* ---------- lesson path ---------- */
const ALL = [...L.units, L.test];
const unlocked = (k) => !GATE && (UNLOCK_ALL || k === 0 || !!P.done[ALL[k - 1].id]);
function showView(id) {
  if (pendingUpdate && id === "v-path") return location.reload();
  $$(".view").forEach((v) => v.classList.toggle("on", v.id === id));
  if (id === "v-path") $("#v-empty").classList.add("on");   // wide screens show an empty right pane beside the path
}
let pop = null;                // the unit card opened by a tap; otherwise the next unit to do is open
let HERE = null;               // this lesson's header and cards, moved into its place on the course path
let scrolled = false;
const BY_ID = new Map(ALL.flatMap((u) => u.steps.map((s) => [s.id, s])));
if (!VIRTUAL) (() => {   // migrate mistakes saved by position before steps had ids
  const b = bankOf(L.id), conv = b.map((ref) => { const m = /^(\w+):(\d+)$/.exec(ref); if (!m) return ref; const u = ALL.find((x) => x.id === m[1]); return u && u.steps[+m[2]] ? u.steps[+m[2]].id : null; }).filter(Boolean);
  if (conv.join() !== b.join()) { G.mistakes[L.id] = [...new Set(conv)]; saveAll(); }
})();
function resolveStep(ref) { const s = BY_ID.get(ref); return s ? { s, ref } : null; }
const journeyKey = `axom:journey:${L.course || "ahom-kings"}`;
const previousJourney = AXOM.store.get(journeyKey, {});
AXOM.store.set(journeyKey, { lesson: L.id, scroll: previousJourney.lesson === L.id ? previousJourney.scroll || 0 : 0 });
addEventListener("pagehide", () => {
  const scroll = $("#v-path .p-scroll")?.scrollTop || 0;
  AXOM.store.set(journeyKey, { lesson: L.id, scroll });
});
if (!VIRTUAL) { const ui = AXOM.store.get("axom:ui", {}); if (ui.lastCourse !== L.course) AXOM.store.set("axom:ui", { ...ui, lastCourse: L.course }); }
function renderPath() {
  const doneCount = ALL.filter((u) => P.done[u.id]).length;
  $("#meter").style.width = `${(doneCount / ALL.length) * 100}%`; $("#meter").style.setProperty("--p", $("#meter").style.width);
  $("#count").innerHTML = `${N(doneCount)}/${N(ALL.length)}`;
  // Mission explanations are presented inside the unit player.
  $("#mission-slot").replaceChildren();
  const m = bankOf(L.id).map(resolveStep).filter(Boolean);
  const gate = GATE ? `<div class="gate-card"><span class="ic">${ICONS.lock}</span><div><b>${T(B("This lesson is locked", "এই পাঠটো বন্ধ"))}</b>
      <span class="s">${T(B(`Finish Lesson ${GATE.n} · ${GATE.name.en.split(" (")[0]} first, or tap Jump here at the end of this lesson to pass a test on the lessons before it.`, `প্ৰথমে পাঠ ${asNum(GATE.n)} · ${GATE.name.as.split(" (")[0]} শেষ কৰা, নহ'লে এই পাঠৰ শেষৰ 'ইয়ালৈ জঁপিওৱা' টিপি আগৰ পাঠবোৰৰ পৰীক্ষা দিয়া।`))}</span>
      <div class="gate-btns"><a class="cp-go" href="lesson.html?id=${GATE.id}">${T(B(`Go to Lesson ${GATE.n}`, `পাঠ ${asNum(GATE.n)}লৈ যোৱা`))}</a></div></div></div>` : "";
  $("#mistake-slot").innerHTML = gate;
  $("#practise")?.remove();
  if (m.length) $(".hero .hero-btns").insertAdjacentHTML("beforeend", `<button class="offline-btn mistake-pill" id="practise">${AXOM.ICON.repeat}<span>${T(B("Mistakes", "ভুল"))} · ${N(m.length)}</span></button>`);
  const cur = ALL.findIndex((u, k) => unlocked(k) && !P.done[u.id]);
  const offs = [0, 24, 0, 8, 34, 44, 12];
  const unitNote = (u, isTest, ex) => isTest ? B(`${ex} questions · 80% to pass`, `${asNum(ex)}টা প্ৰশ্ন · উত্তীৰ্ণ হ'বলৈ ৮০%`) : (u.learned && u.learned[0]) || B(`${ex} exercises`, `${asNum(ex)}টা অনুশীলন`);
  const ARROW = AXOM.ICON.arrow;
  // this lesson's units: a row each, and one open card (the tapped unit, otherwise the next to do)
  const mine = () => ALL.map((u, k) => {
    const isTest = u === L.test, isDone = !!P.done[u.id], jump = isTest && !isDone && !!GATE, testout = isTest && !isDone && !unlocked(k) && !GATE, open = unlocked(k) || testout || jump;
    const cls = `${isTest ? "test " : ""}${isDone ? "done" : open ? "open" : "locked"}${k === cur ? " cur" : ""}`;
    const ex = u.steps.filter((s) => s.type !== "story").length;
    const glyph = isDone ? ICONS.done : isTest ? ICONS.trophy : `<span class="num">${N(k + 1)}</span>`;
    const expanded = pop === k || (pop == null && k === cur);
    const tag = isTest ? T(B("Lesson test", "পাঠৰ পৰীক্ষা")) : `${T(B(`Unit ${k + 1}`, `অধ্যায় ${asNum(k + 1)}`))} · ${T(B("4 min", "৪ মিনিট"))}`;
    const line = jump ? B("Pass a test on the lessons before this one. If you get 80%, they are marked complete and this lesson opens.", "আগৰ পাঠবোৰৰ পৰীক্ষা দিয়া। ৮০% পালে সেইবোৰ সম্পূৰ্ণ হ'ব আৰু এই পাঠ খোল খাব।")
      : testout ? B(`Know this lesson already? Get 80% on the ${ex} questions to complete the lesson and unlock the next one.`, `এই পাঠটো আগৰে পৰা জানা নেকি? ${asNum(ex)}টা প্ৰশ্নত ৮০% পালে পাঠটো সম্পূৰ্ণ হ'ব আৰু পিছৰটো খোল খাব।`)
      : open ? unitNote(u, isTest, ex)
      : GATE ? B(`This lesson opens when you finish Lesson ${GATE.n}.`, `পাঠ ${asNum(GATE.n)} শেষ কৰিলে এই পাঠ খোল খাব।`)
      : B("Complete the step above to unlock this.", "ওপৰৰ স্তৰটো শেষ কৰিলে এইটো খোল খাব।");
    const action = jump ? `<a class="btn" href="lesson.html?jump=${L.id}">${T(B("Jump here", "ইয়ালৈ জঁপিওৱা"))}${ARROW}</a>`
      : open ? `<button class="btn" data-start="${k}" ${testout ? "data-testout" : ""}>${isDone ? T(B("Practise again", "আকৌ অনুশীলন")) : testout ? T(B("Take the test", "পৰীক্ষা দিয়া")) : T(B("Start unit", "অধ্যায় আৰম্ভ কৰা"))}${ARROW}</button>` : "";
    const card = `<div class="pop ${isDone ? "done" : isTest ? "test" : open ? "" : "locked"}"><small>${tag}</small><h3>${T(u.title)}</h3><p>${T(line)}</p>
        ${open && unitLinks(u).length ? `<p class="builds">${CHAIN}${T(B("Builds on", "ভেটি"))}: ${unitLinks(u).map((l) => T(linkLabel(l))).join(", ")}</p>` : ""}${action}</div>`;
    const row = `<button class="node-text ${open ? "" : "locked"}" data-node="${k}"><b>${T(u.title)}</b><small>${T(unitNote(u, isTest, ex))}</small></button>`;
    return `<div class="node-wrap${expanded ? " expanded" : ""}" style="--x:${offs[k % offs.length]}px"><button class="node ${cls}${testout || jump ? " testout" : ""}" data-node="${k}" aria-label="${u.title.en}">${glyph}</button>${expanded ? card : row}</div>`;
  }).join("");
  // every other lesson is one banner on the course path; its units open on that lesson's own page
  const lessonDone = (id) => !!(id === L.id ? P : AXOM.getLesson(id)).done.test;
  const other = (c, i) => {
    const lessonOpen = UNLOCK_ALL || i === 0 || lessonDone(COURSE[i - 1].id) || lessonDone(c.id), done = lessonDone(c.id);
    return `<div class="sec"><a class="sec-banner ${done ? "done" : lessonOpen ? "open" : "locked"}" href="lesson.html?id=${c.id}">
        <span class="face"><img src="${media(c.face)}" alt="" loading="lazy"></span>
        <span class="t"><small>${T(B(`Lesson ${c.n}`, `পাঠ ${asNum(c.n)}`))}</small><b>${T(B(c.name.en.split(" (")[0], c.name.as.split(" (")[0]))}</b><span>${N(c.reign)}</span></span>
        <span class="st">${done ? ICONS.done : lessonOpen ? "›" : ICONS.lock}</span></a></div>`;
  };
  const here = COURSE.findIndex((c) => c.id === L.id);
  $("#path").innerHTML = here < 0 ? mine() : COURSE.map((c, i) => (c.id === L.id ? `<div class="sec here" id="sec-here"></div>${mine()}` : other(c, i))).join("");
  if (here >= 0) $("#sec-here").append(...HERE);
  drawTrail();
  if (!scrolled) {
    scrolled = true;
    requestAnimationFrame(() => {
      if (previousJourney.lesson === L.id && previousJourney.scroll > 0) $("#v-path .p-scroll").scrollTop = previousJourney.scroll;
      else if (here > 0) $("#sec-here").scrollIntoView({ block: "start" });
    });
  }
}
// one soft curve through the unit circles of this lesson
function drawTrail() {
  const path = $("#path"); path.querySelector(".trail")?.remove();
  const box = path.getBoundingClientRect();
  const pts = $$(".node", path).map((n) => { const r = n.getBoundingClientRect(); return [r.left + r.width / 2 - box.left, r.top + r.height / 2 - box.top]; });
  if (pts.length < 2) return;
  const d = pts.reduce((a, [x, y], i) => { if (!i) return `M${x} ${y}`; const [px, py] = pts[i - 1], m = (py + y) / 2; return `${a} C${px} ${m} ${x} ${m} ${x} ${y}`; }, "");
  path.insertAdjacentHTML("afterbegin", `<svg class="trail" aria-hidden="true" width="${box.width}" height="${box.height}"><path d="${d}"/></svg>`);
}
// labels change height with the language and once fonts load, so redraw the curve then too
const redrawTrail = () => { if ($("#v-path").classList.contains("on")) drawTrail(); };
addEventListener("resize", redrawTrail);
document.addEventListener("change", (e) => { if (e.target.id === "as") setTimeout(redrawTrail, 30); });
if (document.fonts) document.fonts.addEventListener("loadingdone", redrawTrail);

/* ---------- connections between units / lessons ---------- */
function linkLabel(link) {
  if (link.lesson) return B(`Lesson ${link.lesson} · ${link.unitTitle.en}`, `পাঠ ${asNum(link.lesson)} · ${link.unitTitle.as}`);
  const k = ALL.findIndex((u) => u.id === link.unit);
  return k < 0 ? B("", "") : B(`Unit ${k + 1} · ${ALL[k].title.en}`, `অধ্যায় ${asNum(k + 1)} · ${ALL[k].title.as}`);
}
const CHAIN = '<svg viewBox="0 0 24 24"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></svg>';
function linkCallout(link) {
  return `<button class="linkback" data-link><span class="ic">${CHAIN}</span><span><small>${T(B("Connects to", "সংযোগ"))} · ${T(linkLabel(link))}</small>${T(link.note)}</span></button>`;
}
function sheet(inner) { $("#sheet-root").innerHTML = `<div class="backdrop" data-keep></div><div class="sheet left"><div class="grab"></div>${inner}<button class="link" data-keep>${T(B("Close", "বন্ধ কৰা"))}</button></div>`; }
function openLinkSheet(link) {
  let body = `<p class="note">${T(link.note)}</p>`;
  if (link.lesson) body += `<a class="btn" href="lesson.html?id=${link.lessonId}" target="_blank" rel="noopener">${T(B(`Open Lesson ${link.lesson} in a new tab`, `পাঠ ${asNum(link.lesson)} নতুন টেবত খোলা`))}</a>`;
  else { const u = ALL.find((x) => x.id === link.unit); if (u && u.learned) body += `<ul class="recap">${u.learned.map((l) => `<li>${T(l)}</li>`).join("")}</ul>`; }
  sheet(`<h2>${T(linkLabel(link))}</h2>${body}`);
}
const unitLinks = (u) => {
  const seen = new Map();
  u.steps.forEach((s) => { if (s.link) { const key = s.link.lesson ? `L${s.link.lesson}:${s.link.unitNo}` : s.link.unit; if (!seen.has(key)) seen.set(key, s.link); } });
  return [...seen.values()];
};
const TYPE = { place: B("Place", "ঠাই"), article: B("Article", "অনুচ্ছেদ"), river: B("River", "নদী"), ridge: B("Hills", "পাহাৰ"), pass: B("Mountain pass", "গিৰিপথ"), people: B("People", "জনগোষ্ঠী"), person: B("Person", "ব্যক্তি"), office: B("Office", "পদ"), term: B("Term", "শব্দ") };
function openEntity(id) {
  const e = ENT[id]; if (!e) return;
  const links = (e.lessons || []).filter((l) => l !== L.id);
  sheet(`<div class="ent-type">${T(TYPE[e.type] || B("", ""))}</div><h2>${T(e.name)}</h2><p class="note">${T(e.meaning)}</p>
    ${links.length ? `<p class="also">${T(B("Also in", "আৰু আছে"))}: ${links.map((l) => `<a href="lesson.html?id=${l}" target="_blank" rel="noopener">${REFERENCE_LESSONS[l] ? T(REFERENCE_LESSONS[l].title) : ENT[l] ? T(ENT[l].name) : l}</a>`).join(", ")}</p>` : ""}`);
}

function openSources() {
  sheet(`<h2>${T(B("Sources", "উৎস"))}</h2><ul class="src-list">${(L.sources || []).map((x) => `<li>${x.url ? `<a href="${escapeHTML(x.url)}" target="_blank" rel="noopener">${escapeHTML(x.title)}</a>` : `<b>${escapeHTML(x.title)}</b>`}${x.used_for ? `<span>${escapeHTML(x.used_for)}</span>` : ""}</li>`).join("")}</ul>`);
}

/* ---------- guidebook: one-screen revision note built from the lesson ---------- */
function openGuide() {
  const facts = L.units.flatMap((u) => u.learned || []);
  const traps = ALL.flatMap((u) => u.steps).filter((s) => (s.type === "tf" && s.answer === false) || s.type === "spot");
  const names = new Set();
  JSON.stringify(L.units).replace(MARK, (m, id) => names.add(id));
  const tl = (L.guide && L.guide.timeline) || [];
  const extra = (L.guide && L.guide.extra_stories) || [];
  sheet(`<h2>${T(B("Guidebook", "নিৰ্দেশিকা"))} · ${T(L.king)}</h2>
    <h4>${T(B("Key facts", "মূল তথ্য"))}</h4><ul class="recap">${facts.map((f) => `<li>${T(f)}</li>`).join("")}</ul>
    ${tl.length ? `<h4>${T(B("Timeline", "সময়ৰেখা"))}</h4><div class="g-tl">${tl.map((x) => `<div><b>${x.y ? N(x.y) : "·"}</b><span>${T(x.t)}</span></div>`).join("")}</div>` : ""}
    ${traps.length ? `<h4>${T(B("Exam traps", "পৰীক্ষাৰ ফান্দ"))}</h4>${traps.map((s) => `<div class="trap"><div class="w">✕ ${T(s.type === "tf" ? s.s : B(s.tokens.en.join(" "), s.tokens.as.join(" ")))}</div><div class="r">✓ ${T(s.why)}</div></div>`).join("")}` : ""}
    ${extra.length ? `<details class="guide-more"><summary>${T(B("More context", "অধিক প্ৰসংগ"))}</summary>${extra.map(s=>`<h4>${T(s.title)}</h4>${s.text.map(p=>`<p class="note">${TR(p)}</p>`).join("")}`).join("")}</details>` : ""}
    ${names.size ? `<h4>${T(B("Names to know", "জানিবলগীয়া নাম"))}</h4><div class="g-names">${[...names].filter((id) => ENT[id]).map((id) => `<button class="ent" data-ent="${id}">${T(ENT[id].name)}</button>`).join("")}</div>` : ""}`);
}

/* ---------- unit play ---------- */
let U = null;
function startUnit(k, testout = false) {
  const unit = ALL[k];
  U = { unit, practice: false, testout, queue: unit.steps.map((s) => ({ s, ref: s.id })), pos: 0, done: 0, total: unit.steps.length, xp: 0, ok: 0, asked: 0, mistakes: [], start: Date.now(), phase: "answer", st: {} };
  pop = null; showView("v-play"); renderStep(true);
}
function startPractice() {
  const items = shuffle(bankOf(L.id).map(resolveStep).filter(Boolean)).slice(0, 10);
  if (!items.length) return;
  const unit = { id: "practice", title: B("Practise your mistakes", "ভুলৰ অনুশীলন"), learned: [], steps: items.map((x) => x.s) };
  U = { unit, practice: true, queue: items, pos: 0, done: 0, total: items.length, xp: 0, ok: 0, asked: 0, mistakes: [], start: Date.now(), phase: "answer", st: {} };
  pop = null; showView("v-play"); renderStep(true);
}
const step = () => U.queue[U.pos];

const escapeHTML = (value) => String(value).replace(/[&<>"]/g, (c) => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;",
}[c]));
function renderStep(animate) {
  const it = step(); it.s = MATH.vary(it.s);   // a step with variants shows new numbers each time
  const s = it.s;
  U.phase = "answer"; U.st = {};
  paintProgress();
  $("#foot").className = "foot";
  const scr = $("#screen");
  scr.classList.remove("enter"); void scr.offsetWidth; if (animate) scr.classList.add("enter");
  const from = s._lesson && s._lesson !== L.id ? `<span class="from">${T(B(s._lesson[0].toUpperCase() + s._lesson.slice(1), s._lesson[0].toUpperCase() + s._lesson.slice(1)))}</span>` : "";
  const unitNo = mode === "lesson" && !U.practice ? L.units.indexOf(U.unit) + 1 : 0;
  const kick = s.type === "story" ? `<div class="kicker story">${T(s.tasks ? B("Find out", "বিচাৰি উলিওৱা") : unitNo ? B(`Unit ${unitNo} · Story`, `অধ্যায় ${asNum(unitNo)} · কাহিনী`) : KICK.story)}${s.text.length > 1 ? `<span class="dots">${s.text.map((_, k) => `<i class="${k ? "" : "on"}"></i>`).join("")}</span>` : ""}</div>`
    : it.retry ? `<div class="kicker retry">${T(B("Previous mistake", "আগৰ ভুল"))}</div>`
    : s.guess ? `<div class="kicker guess">${T(s.decide ? B("You decide", "তুমিয়েই সিদ্ধান্ত লোৱা") : B("Make a guess", "অনুমান কৰা"))}</div>`
    : `<div class="kicker">${T(KICK[s.scale || s.type])}${from}${s.link && !VIRTUAL ? `<button class="linkchip" data-link>${CHAIN}${T(linkLabel(s.link))}</button>` : ""}${s.type === "whoami" ? `<span class="xp" id="who-xp"></span>` : ""}</div>`;
  const mission = L.mission && U.unit.mission && !U.practice && !U.testout && mode === "lesson"
    ? `<div class="mission-ribbon"><small>${T(L.mission.label)} · ${T(U.unit === L.test ? B("Final challenge", "শেষ প্ৰত্যাহ্বান") : B(`Finding ${L.units.indexOf(U.unit) + 1} of ${L.units.length}`, `${asNum(L.units.length)}টাৰ ${asNum(L.units.indexOf(U.unit) + 1)} নম্বৰ প্ৰমাণ`))}</small><strong>${T(U.unit.mission.objective)}</strong></div>` : "";
  const evidence = s.type !== "story" && s.img && s.imageCaption
    ? `<figure class="story-visual"><div class="frame library">${picture(s.img, lessonOf(s))}</div><figcaption>${T(s.imageCaption)}
      ${s.imageAlt ? `<details><summary>${T(B("Read the map as text", "মানচিত্ৰৰ বৰ্ণনা পঢ়া"))}</summary>${T(s.imageAlt)}</details>` : ""}</figcaption></figure>`
    : "";
  const passage = s.passage
    ? `<details class="reading-passage" open><summary>${escapeHTML(s.passage.title)}</summary><p>${escapeHTML(s.passage.text)}</p></details>`
    : "";
  scr.classList.toggle("story-screen", s.type === "story");
  scr.innerHTML = s.type === "story" ? RENDER.story(s, mission + kick) : mission + kick + `<h1 class="q-title">${T(U.unit.title)}</h1>` + evidence + passage + RENDER[s.type](s);
  scr.scrollTop = 0;
  if (SETUP[s.type]) SETUP[s.type](s, scr);
  refresh();
}
// a bare file name is in the lesson's own folder; "folder/file" is relative to content/media (shared/…, or another lesson's pictures)
const img = (f, size, lid = L.id) => media(f.includes("/") ? f : `${lid}/${f}`, size);
const picture = (f, lid) => `<img src="${img(f, 0, lid)}" srcset="${img(f, 480, lid)} 480w, ${img(f, 0, lid)} 1080w" sizes="(max-width: 440px) 92vw, 360px" alt="">`;
// a story card may carry its own map ({box, show, routes, texts, labels, districts}); otherwise it uses the lesson map
const mapOf = (s) => s._map || (s.map && s.map.box ? s.map : L.map);
// years in story text get their own style; only text between tags is touched
const years = (html) => html.split(/(<[^>]+>|\$[^$]+\$)/).map((x) => (x.startsWith("<") || x.startsWith("$") ? x : x.replace(/(^|[^\w\u0980-\u09FF])(1[0-9]{3}|১[০-৯]{3})(?![\w০-৯])/g, '$1<span class="yr">$2</span>'))).join("");
// a story card shows its first beat; each tap (or Continue) reveals the next before moving on
function storyBeat() {
  const held = $("#screen").querySelector(".beat.hold"); if (!held) return false;
  held.classList.remove("hold"); held.classList.add("on");
  const dots = $("#screen").querySelectorAll(".kicker.story .dots i"), n = $("#screen").querySelectorAll(".beat.on").length;
  dots.forEach((d, k) => d.classList.toggle("on", k < n));
  if (!$("#screen").querySelector(".beat.hold")) $("#screen").querySelector(".story .more")?.remove();
  held.scrollIntoView({ behavior: "smooth", block: "nearest" });
  return true;
}
function storyDiagram({ layout, items }) {
  const flow = layout === "flow";
  const list = flow ? "ol" : "ul";
  return `<figure class="story-diagram">
    <${list} class="story-diagram-items ${flow ? "is-flow" : ""}">${items.map((item, index) =>
      `<li>${flow ? `<span class="story-diagram-number" aria-hidden="true">${T(B(String(index + 1), asNum(String(index + 1))))}</span>` : ""}${T(item)}</li>`
    ).join("")}</${list}>
  </figure>`;
}
const IMAGE_CREDITS = {
  map: B("Locator map", "অৱস্থান মানচিত্ৰ"),
  diagram: B("Schematic diagram", "আঁচনিগত চিত্ৰ"),
  photo: B("Photograph", "আলোকচিত্ৰ"),
  document: B("Document scan", "নথিৰ স্কেন"),
};
const RENDER = {
  story: (s, head = "") => {
    // Story card standard: a painting across the top, then one glass card with kicker + beat dots, title, lede and one beat per tap (see README "Story cards")
    const yr = (s.text.map((p) => p.en).join(" ").match(/\b(1[0-9]{3})\b/) || [])[1];
    const stamp = yr && s.img && !s.imageCaption ? `<span class="stamp">${T(B(yr, asNum(yr)))}</span>` : "";
    const memo = /^Remember\b/.test(s.title.en), last = s.text.length - 1;
    const asks = (p) => /\?\s*$/.test(String(p.en).replace(/<[^>]+>/g, ""));
    const bleed = (s.img && !s.imageCaption) || (!s.img && !s.map && !s.diagram && !s.figure && !s.widget);
    const picturePart = s.img ? s.imageCaption ? `<figure class="story-visual"><div class="frame library ${s.imageLayout === "contain" ? "contain" : ""}">${picture(s.img, lessonOf(s))}${stamp}<span class="credit">${T(IMAGE_CREDITS[s.imageKind] || B("Artistic reconstruction", "শিল্পীৰ কল্পনা"))}</span></div><figcaption>${T(s.imageCaption)}</figcaption></figure>` : `<figure class="frame ${s.top ? "top" : ""}">${picture(s.img, lessonOf(s))}${stamp}<span class="credit">${T(B("Artistic reconstruction", "শিল্পীৰ কল্পনা"))}</span></figure>`
      : s.map ? `<figure class="frame mapframe">${mapSVG(mapOf(s), { story: true, route: s.map.route })}</figure>`
      : s.figure ? GEOFIG.story(s.figure, T)
      : s.diagram ? storyDiagram(s.diagram)
      : s.widget ? `<div class="wx story-wx"></div>`
      : `<figure class="frame art${s.art === "rooster" ? " full" : ""}">${ART[s.art]}</figure>`;
    const beats = `<div class="story${memo ? " memo" : ""}">${s.text.map((p, k) => k && k === last && asks(p)
        ? `<div class="beat think hold"><span class="think-ic">${AXOM.ICON.bulb}</span><div><b>${T(B("Think about it", "ভাবি চোৱা"))}</b><p>${years(TR(p))}</p></div></div>`
        : `<p class="beat${k ? " later" : " lede"}${k ? " hold" : " on"}">${years(TR(p))}</p>`).join("")}
    ${s.text.length > 1 ? `<div class="more" aria-hidden="true">${T(B("Tap to read on", "পঢ়ি যাবলৈ টিপা"))}</div>` : ""}</div>`;
    const extras = (s.link ? linkCallout(s.link) : "") + (L.sources && L.sources.length ? `<button class="src-link" data-sources>${T(B("View sources", "উৎস চোৱা"))}${AXOM.ICON.external}</button>` : "");
    const title = `<h1 class="t">${T(s.title)}</h1>`;
    return bleed ? `${picturePart}<div class="story-card">${head}${title}${beats}${extras}</div>` : `<div class="story-card plain">${head}${title}${picturePart}${beats}${extras}</div>`;
  },
  mcq: (s) => `<p class="prompt" ${s.small ? 'style="font-size:18px"' : ""}>${T(s.q)}</p>
    <div class="opts">${s.options.map((o, k) => `<button class="tile opt" data-opt="${k}"><span class="k">${"ABCD"[k]}</span><span>${T(o)}</span></button>`).join("")}</div>`,
  figtap: (s) => `<p class="prompt">${T(s.q)}</p>${GEOFIG.quiz(s.kind)}`,
  odd: (s) => `<p class="prompt">${T(s.q)}</p><div class="opts grid2">${s.options.map((o, k) => `<button class="tile opt" data-opt="${k}"><span>${T(o)}</span></button>`).join("")}</div>`,
  inline: (s) => `<p class="sentence">${T(s.before)} <span class="blank" data-fillchip>&nbsp;</span> ${T(s.after)}</p>
    <div class="opts grid2 ${s.big ? "big" : ""}">${s.options.map((o, k) => `<button class="tile opt" data-opt="${k}"><span>${T(o)}</span></button>`).join("")}</div>`,
  tf: (s) => `<div class="statement">${T(s.s)}</div><div class="tf">
    <button class="tile t" data-tf="1"><span class="sym">✓</span>${T(B("True", "শুদ্ধ"))}</button>
    <button class="tile f" data-tf="0"><span class="sym">✕</span>${T(B("False", "অশুদ্ধ"))}</button></div>`,
  fill: (s) => `<div class="en"><p class="sentence">${plain(s.before.en, "en")} <span class="blank"><span class="given">${s.answer[0]}</span><input type="text" maxlength="${s.answer.length - 1}" style="--n:${s.answer.length - 1}" placeholder="${"_".repeat(s.answer.length - 1)}" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Type the rest of the word"></span>${plain(s.after.en, "en")}</p>
      <p class="help">The first letter is given. Type the rest.</p></div>
    <div class="as"><p class="sentence">${plain(s.before.as, "as")} <span class="blank" data-fillchip>&nbsp;</span> ${plain(s.after.as, "as")}</p>
      <div class="chips">${s.asOptions.map((o, k) => `<button class="tile" data-chip="${k}">${o}</button>`).join("")}</div></div>`,
  map: (s) => `<p class="prompt">${T(s.q)}</p>${mapSVG(mapOf(s), { choices: s.choices })}`,
  picture: (s) => `<p class="prompt">${T(s.q)}</p><div class="pics">${s.options.map((src, k) => `<button class="tile pic" data-opt="${k}"><img src="${img(src, 480, lessonOf(s))}" alt=""></button>`).join("")}</div>`,
  whoami: (s) => `<div class="clues" id="clues"></div><div class="more"><button class="chip-btn" id="more">${T(B("Show another clue", "আৰু এটা সূত্ৰ"))}</button></div>
    <div class="opts grid2">${s.options.map((o, k) => `<button class="tile opt" data-opt="${k}"><span>${T(o)}</span></button>`).join("")}</div>`,
  unscramble: (s) => `<p class="prompt">${T(s.q)}</p>
    <div class="en"><div class="word-slots" data-lang="en">${s.word.en.map(() => `<span class="wslot"></span>`).join("")}</div><div class="letters" data-lang="en"></div></div>
    <div class="as"><div class="word-slots" data-lang="as">${s.word.as.map(() => `<span class="wslot"></span>`).join("")}</div><div class="letters" data-lang="as"></div></div>`,
  spot: (s) => `<p class="prompt" style="font-size:18px">${T(s.q)}</p>
    <div class="spot en">${s.tokens.en.map((w, k) => `<button class="tok" data-tok="${k}" data-lang="en">${w}</button>`).join(" ")}</div>
    <div class="spot as">${s.tokens.as.map((w, k) => `<button class="tok" data-tok="${k}" data-lang="as">${w}</button>`).join(" ")}</div>`,
  order: (s) => `<p class="prompt">${T(s.q)}</p><div class="slots">${s.items.map((_, k) => `<div class="oslot"><span class="n">${N(k + 1)}</span></div>`).join("")}</div><div class="bank"></div>`,
  match: (s) => `<p class="prompt">${T(s.q)}</p><div class="match"><div class="col" data-side="left"></div><div class="col" data-side="right"></div></div>`,
  timeline: (s) => {
    const hint = s.scale === "articles" ? B("Tap a provision, then tap here", "উপবন্ধ এটা টিপি ইয়াত টিপা") : B("Tap an event, then tap here", "ঘটনা এটা টিপি ইয়াত টিপা");
    const slot = (k) => `<div class="tslot" data-slot="${k}">${T(hint)}</div>`;
    return `<p class="prompt">${T(s.q)}</p><div class="tline">${slot(0)}${s.anchors.map((a, k) => `<div class="anchor"><span class="y">${N(a.y)}</span><span class="l">${T(a.l)}</span></div>${slot(k + 1)}`).join("")}</div>
      <div class="tbank">${s.items.map((x, k) => `<button class="tile" data-item="${k}">${T(x.t)}</button>`).join("")}</div>`;
  },
};
const SETUP = {
  order: (s, scr) => { const bk = $(".bank", scr); shuffledIdx(s.items.length).forEach((k) => bk.insertAdjacentHTML("beforeend", `<button class="tile" data-step="${k}">${T(s.items[k])}</button>`)); U.st.placed = []; },
  match: (s, scr) => {
    shuffledIdx(s.pairs.length).forEach((k) => $('[data-side="left"]', scr).insertAdjacentHTML("beforeend", `<button class="tile" data-pair="${k}">${T(s.pairs[k][0])}</button>`));
    shuffledIdx(s.pairs.length).forEach((k) => $('[data-side="right"]', scr).insertAdjacentHTML("beforeend", `<button class="tile" data-pair="${k}">${T(s.pairs[k][1])}</button>`));
    U.st = { left: null, right: null, matched: 0, misses: 0 };
  },
  unscramble: (s, scr) => {
    ["en", "as"].forEach((lg) => { const box = $(`.letters[data-lang="${lg}"]`, scr); shuffledIdx(s.word[lg].length).forEach((k) => box.insertAdjacentHTML("beforeend", `<button class="tile" data-letter="${k}" data-lang="${lg}">${s.word[lg][k]}</button>`)); });
    U.st = { en: [], as: [] };
  },
  whoami: (s) => { U.st.clues = 0; revealClue(s); },
  timeline: () => { U.st = { armed: null, placed: {} }; },
};
const MX = MATH.bind({ U: () => U, refresh: () => refresh(), check: () => check(), hintsAllowed: () => mode === "drill" || (mode === "lesson" && !U.testout && U.unit !== L.test) });
Object.assign(RENDER, MX.RENDER); Object.assign(SETUP, MX.SETUP);
function revealClue(s) {
  const n = U.st.clues++;
  $("#clues").insertAdjacentHTML("beforeend", `<div class="clue"><span class="n">${N(n + 1)}</span><span>${T(s.clues[n])}</span></div>`);
  if (U.st.clues >= s.clues.length) $("#more").disabled = true;
  const el = $("#who-xp"); if (el) el.innerHTML = T(B(`Worth ${whoXP()} XP`, `${asNum(whoXP())} XP`));
}
const whoXP = () => [30, 20, 10][Math.min(U.st.clues, 3) - 1];

function ready() {
  const s = step().s, st = U.st, scr = $("#screen");
  switch (s.type) {
    case "story": return true;
    case "mcq": case "odd": case "figtap": case "inline": case "picture": case "whoami": return st.sel != null;
    case "fill": return isAS() ? st.chip != null : $(".en input", scr).value.trim().length === s.answer.length - 1;
    case "map": return st.place != null;
    case "unscramble": { const lg = isAS() ? "as" : "en"; return st[lg].length === s.word[lg].length; }
    case "spot": return st.tok != null;
    case "order": return st.placed.length === s.items.length;
    case "timeline": return Object.keys(st.placed).length === s.items.length;
    case "solve": case "explore": case "stepwise": return MX.ready(s, st);
  }
  return false;   // tf and match check themselves
}
function refresh() {
  if (!step()) return;   // a scene animation can finish just after the unit ends
  const s = step().s, btn = $("#action"), last = U.pos === U.queue.length - 1;
  if (U.phase === "feedback" || s.type === "story") { btn.innerHTML = last ? T(B("Finish", "শেষ কৰা")) : T(B("Continue", "আগবাঢ়া")); btn.disabled = s.type === "story" && !!s.tasks && U.phase !== "feedback" && !U.st.tasksDone; return; }
  btn.innerHTML = T(B("Check", "পৰীক্ষা কৰা"));
  btn.disabled = !ready();
}
function check() {
  const s = step().s, st = U.st, scr = $("#screen");
  let right = false;
  const markOpts = (ci) => { $$("[data-opt]", scr).forEach((o) => { o.disabled = true; if (+o.dataset.opt === ci) o.classList.add("right"); }); if (st.sel !== ci) $(`[data-opt="${st.sel}"]`, scr).classList.add("wrong"); };
  switch (s.type) {
    case "mcq": case "odd": case "figtap": case "picture": case "whoami": right = st.sel === s.answer; markOpts(s.answer); if (s.type === "whoami") $("#more").disabled = true; break;
    case "inline": { right = st.sel === s.answer; markOpts(s.answer); const c = $("[data-fillchip]", scr); c.innerHTML = T(s.options[s.answer]); c.classList.add("right"); break; }
    case "tf": right = st.sel === s.answer; $$("[data-tf]", scr).forEach((b) => { b.disabled = true; const v = b.dataset.tf === "1"; if (v === s.answer) b.classList.add("right"); else if (v === st.sel) b.classList.add("wrong"); }); break;
    case "fill":
      if (isAS()) {
        right = st.chip === s.asAnswer;
        $$("[data-chip]", scr).forEach((c) => { c.disabled = true; if (+c.dataset.chip === s.asAnswer) c.classList.add("right"); else if (+c.dataset.chip === st.chip) c.classList.add("wrong"); });
        const c = $(".as [data-fillchip]", scr); c.textContent = s.asOptions[s.asAnswer]; c.classList.add("right");
      } else {
        const inp = $(".en input", scr); right = inp.value.trim().toLowerCase() === s.answer.slice(1).toLowerCase();
        inp.disabled = true; if (!right) inp.value = s.answer.slice(1);
        $(".en .blank", scr).classList.add(right ? "right" : "wrong");
      }
      break;
    case "map": right = st.place === s.target; $$(".hit", scr).forEach((h) => { h.classList.remove("sel"); if (h.dataset.place === s.target) h.classList.add("right"); else if (h.dataset.place === st.place) h.classList.add("wrong"); }); break;
    case "unscramble": { const lg = isAS() ? "as" : "en"; right = st[lg].every((k, i) => s.word[lg][k] === s.word[lg][i]); $(`.word-slots[data-lang="${lg}"]`, scr).classList.add(right ? "right" : "wrong"); $$(".tile", scr).forEach((t) => (t.disabled = true)); break; }
    case "spot": {
      const lg = isAS() ? "as" : "en", w = s.wrong[lg]; right = st.tok === w;
      $$(`.tok[data-lang="${lg}"]`, scr).forEach((t) => { t.disabled = true; t.classList.remove("sel"); if (+t.dataset.tok === w) t.classList.add("wrong"); else if (+t.dataset.tok === st.tok) t.classList.add("sel"); });
      $(`.tok[data-lang="${lg}"][data-tok="${w}"]`, scr).insertAdjacentHTML("afterend", ` <span class="fix">${s.fix[lg]}</span>`);
      break;
    }
    case "order": right = st.placed.every((k, i) => k === i); $$(".oslot", scr).forEach((o, i) => o.classList.add(st.placed[i] === i ? "right" : "wrong")); $$(".tile", scr).forEach((t) => (t.disabled = true)); break;
    case "timeline":
      right = s.items.every((x, k) => st.placed[k] === x.slot);
      $$(".tslot", scr).forEach((sl) => { const k = +sl.dataset.slot; const items = Object.entries(st.placed).filter(([, v]) => v === k).map(([i]) => +i); if (items.length) sl.classList.add(items.every((i) => s.items[i].slot === k) ? "right" : "wrong"); });
      $$(".tile", scr).forEach((t) => (t.disabled = true));
      break;
    case "match": right = st.misses === 0; break;
    case "solve": case "explore": case "stepwise": right = MX.check(s, st); break;
  }
  feedback(right);
}
function answerHTML(s) {
  if (s.answerText) return T(s.answerText);
  switch (s.type) {
    case "solve": return MX.answerHTML(s);
    case "mcq": case "odd": case "whoami": case "inline": return T(s.options[s.answer]);
    case "figtap": return T(s.answerText);
    case "tf": return T(s.answer ? B("True", "শুদ্ধ") : B("False", "অশুদ্ধ"));
    case "order": return s.items.map((x, i) => `${N(i + 1)}. ${T(x)}`).join("<br>");
    case "timeline": return T(B("See the explanation below", "তলৰ ব্যাখ্যা চোৱা"));
  }
  return "";
}
// a guess step ({guess: true}) asks the learner to predict before the story reveals it: any answer is welcome,
// it earns a little XP, is never recorded as a mistake and never comes back
function guessFeedback(right) {
  const s = step().s; U.xp += 5; SFX.good();
  U.done = Math.min(U.total, U.done + 1);
  $("#fb-badge").textContent = right ? "✓" : "?";
  $("#fb-title").innerHTML = right ? T(B("You called it!", "ঠিকেই অনুমান কৰিলা!")) : T(B("Good guess. Here is what happened", "ভাল অনুমান। আচলতে যি হৈছিল"));
  $("#fb-xp").innerHTML = `+${N(5)} XP`;
  $("#fb-ans").innerHTML = right ? "" : `<small>${T(B("What really happened", "আচলতে যি হৈছিল"))}</small>${answerHTML(s)}`;
  $("#fb-why").innerHTML = TR(s.why);
  $("#foot").className = "foot fb-good fb-guess";
  U.phase = "feedback"; paintProgress(); saveAll(); refresh();
  $("#action").focus({ preventScroll: true });
}
// Surprise rewards: now and then a correct answer opens a small gift, so a lesson never feels fully predictable.
// At most one per unit, never in the first two answers, never on retries, tests-out, jump tests or checkpoints.
// Gifts: a "Did you know?" card about a name from this lesson (each shown once per device), or bonus XP.
const SEEN_KEY = "axom.facts";
const lessonNames = (() => { const ids = new Set(); JSON.stringify(L).replace(/\[\[([a-z0-9-]+)/g, (m, id) => { if (ENT[id] && ENT[id].meaning) ids.add(id); return m; }); return [...ids]; })();
function surprise(it) {
  if (mode !== "lesson" || it.retry || U.testout || U.surprised || U.asked < 3 || Math.random() > 0.2) return "";
  U.surprised = true;
  let seen = []; try { seen = JSON.parse(localStorage.getItem(SEEN_KEY) || "[]"); } catch { /* storage blocked */ }
  const fresh = lessonNames.filter((id) => !seen.includes(id));
  if (fresh.length && Math.random() < 0.7) {
    const id = fresh[Math.floor(Math.random() * fresh.length)], e = ENT[id];
    try { localStorage.setItem(SEEN_KEY, JSON.stringify([...seen, id].slice(-400))); } catch { /* storage blocked */ }
    U.xp += 5; SFX.gift();
    return `<div class="gift"><span class="gift-ic">🎁</span><div><b>${T(B("Did you know?", "জানানে?"))} <span class="gift-xp">+${N(5)} XP</span></b><span class="gift-t"><strong>${T(e.name)}</strong>: ${T(e.meaning)}</span></div></div>`;
  }
  U.xp += 15; SFX.gift();
  return `<div class="gift"><span class="gift-ic">🎁</span><div><b>${T(B("Surprise bonus!", "আচৰিত বোনাচ!"))} <span class="gift-xp">+${N(15)} XP</span></b><span class="gift-t">${T(B("A little gift for a sharp answer.", "চোকা উত্তৰৰ বাবে সৰু উপহাৰ।"))}</span></div></div>`;
}
function feedback(right) {
  if (step().s.guess) return guessFeedback(right);
  const it = step(), s = it.s, slips = s.type === "match" && !right, lid = lessonOf(s);
  let gain = 0;
  if (!it.retry) { U.asked++; AXOM.record(lid, right); }
  // Skill evidence: first attempts only, so a retry can never raise mastery.
  let coaching = "";
  if (s.skill) {
    const results = MX.outcomes(s, U.st, right);
    if (!it.retry) results.forEach((r) => { AXOM.skillAnswer(r.skill, r.right, r); if (r.tag) AXOM.misconception(r.tag); });
    const t = results.find((r) => r.trap);
    if (t) coaching = MX.coach(t.trap);
    if (mode === "diagnostic" && !right) MATH.prune(U, s.skill, L.skillMap);
  }
  if (right) { if (!it.retry) U.ok++; gain = U.st.hinted ? 5 : it.retry ? 5 : s.type === "whoami" ? whoXP() : ["order", "timeline"].includes(s.type) ? 20 : 10; SFX.good(); }
  else { if (slips) gain = 5; SFX.bad(); }
  U.xp += gain;
  // spaced repetition: learned steps come back after 1, 3, 7, 15, 30 days; review answers move them along
  if (!it.retry && !s._bank && !s.id.startsWith("bank.")) { if (mode === "review") AXOM.srsAnswer(s.id, lid, right); else if (right) AXOM.srsLearn(s.id, lid); }
  // mistakes bank: kept for "Practise your mistakes" and daily review; a later correct answer clears them
  const b = bankOf(lid);
  if (right && b.includes(it.ref) && (U.practice || VIRTUAL || !it.retry)) b.splice(b.indexOf(it.ref), 1);
  if (!right && !b.includes(it.ref) && !s._bank && !s.id.startsWith("bank.")) b.push(it.ref);
  // A missed question comes back once at the end of a unit or lesson test (not matching; not in exams).
  if (!right && !it.retry) { U.mistakes.push({ s }); if (!slips && mode !== "checkpoint" && mode !== "jump" && mode !== "diagnostic" && !U.testout) {
    // Maths repairs on the spot: in a teaching unit the same idea returns at once, with new numbers.
    if (s.skill && mode === "lesson" && U.unit !== L.test) U.queue.splice(U.pos + 1, 0, { s, ref: it.ref, retry: true });
    else U.queue.push({ s, ref: it.ref, retry: true });
  } }
  if (!it.retry) U.done = Math.min(U.total, U.done + 1);
  $("#fb-badge").textContent = right || slips ? "✓" : "✕";
  $("#fb-title").innerHTML = right ? T(PRAISE[Math.floor(Math.random() * PRAISE.length)])
    : slips ? T(B(`All matched, ${U.st.misses} slip${U.st.misses > 1 ? "s" : ""}`, `সকলো মিলিল, ${asNum(U.st.misses)}টা ভুল`)) : T(B("Not quite", "হোৱা নাই"));
  $("#fb-xp").innerHTML = gain ? `+${N(gain)} XP` : "";
  $("#fb-ans").innerHTML = right || slips ? "" : `<small>${T(B("Correct answer", "শুদ্ধ উত্তৰ"))}</small>${answerHTML(s)}`;
  $("#fb-why").innerHTML = coaching + TR(s.why) + (right ? surprise(it) : "");
  $("#foot").className = `foot ${right ? "fb-good" : "fb-bad"}`;
  U.phase = "feedback";
  paintProgress();
  saveAll(); refresh();
  $("#action").focus({ preventScroll: true });
}
// segmented bar and "2 / 8": the step being answered counts, so the first step shows 1
function paintProgress() {
  const cur = Math.min(U.total, U.done + (U.phase === "answer" ? 1 : 0)), bar = $("#progress");
  bar.style.width = `${(cur / U.total) * 100}%`;
  $("#bar").style.setProperty("--n", U.total);
  $("#step-count").innerHTML = `${N(cur)} / ${N(U.total)}`;
}
function next() {
  if (step().s.type === "story") U.done = Math.min(U.total, U.done + 1);
  U.pos++;
  if (U.pos >= U.queue.length) return finishUnit();
  renderStep(true);
}

/* ---------- unit complete ---------- */
let AFTER = null;   // what the main button on the complete screen does: { start: unit } or { href }, with its label
function finishUnit() {
  const u = U.unit, wasDone = !!P.done[u.id];
  // A completed teaching unit opens the next unit. A lesson test opens the
  // next lesson only after the first-attempt pass check below.
  if (!U.practice && !VIRTUAL && !U.testout && u !== L.test) P.done[u.id] = true;
  G.xp += U.xp; AXOM.addDayXP(U.xp); AXOM.bumpStreak();
  let note = "";
  if (mode === "checkpoint") {
    const pass = U.asked && U.ok / U.asked >= 0.8;
    if (pass) {
      G.checkpoints[L.era.id] = true;
      Object.entries(L.eraUnits).forEach(([id, units]) => { const Pl = AXOM.getLesson(id); units.forEach((u) => (Pl.done[u] = true)); AXOM.store.set(`axom:lesson:${id}`, Pl); });
    }
    note = pass ? T(B(params.has("testout") ? `Passed! The lessons of this ${L.word.en} are marked complete.` : `Passed! ${L.word.en[0].toUpperCase()}${L.word.en.slice(1)} checkpoint complete.`, params.has("testout") ? `উত্তীৰ্ণ! এই ${L.word.as}ৰ পাঠবোৰ সম্পূৰ্ণ বুলি চিহ্নিত কৰা হ'ল।` : `উত্তীৰ্ণ! ${L.word.as}ৰ পৰীক্ষা সম্পূৰ্ণ।`))
      : T(B("You need 80% to pass. Review the lessons and try again.", "উত্তীৰ্ণ হ'বলৈ ৮০% লাগে। পাঠবোৰ আকৌ চাই পুনৰ চেষ্টা কৰা।"));
  }
  if (mode === "diagnostic") G.checkpoints.diagnostic = true;
  let pass = null;
  if (mode === "jump" || U.testout) {
    pass = !!U.asked && U.ok / U.asked >= 0.8;
    if (pass && mode === "jump") Object.entries(L.eraUnits).forEach(([id, units]) => { const Pl = AXOM.getLesson(id); units.forEach((x) => (Pl.done[x] = true)); AXOM.store.set(`axom:lesson:${id}`, Pl); });
    if (pass && U.testout) ALL.forEach((x) => (P.done[x.id] = true));
    note = pass ? T(mode === "jump" ? B("Passed! The lessons before it are marked complete.", "উত্তীৰ্ণ! আগৰ পাঠবোৰ সম্পূৰ্ণ বুলি চিহ্নিত কৰা হ'ল।") : B("Passed! This lesson is marked complete.", "উত্তীৰ্ণ! এই পাঠটো সম্পূৰ্ণ বুলি চিহ্নিত কৰা হ'ল।"))
      : T(B("You need 80% to pass. Do the units first, or try again later.", "উত্তীৰ্ণ হ'বলৈ ৮০% লাগে। আগতে অধ্যায়বোৰ কৰা, বা পিছত আকৌ চেষ্টা কৰা।"));
  }
  // Passing a lesson test, however it was taken (after the units, as a test-out, or as practice), completes the lesson,
  // so the first unit of the next lesson opens.
  if (!VIRTUAL && u === L.test && !U.testout) {
    pass = !!U.asked && U.ok / U.asked >= 0.8;
    if (pass) P.done.test = true;
    else note = T(B("You need 80% to pass. Review the lesson and try again.", "উত্তীৰ্ণ হ'বলৈ ৮০% লাগে। পাঠটো আকৌ চাই পুনৰ চেষ্টা কৰা।"));
  }
  saveAll();
  SFX.done();
  const secs = Math.round((Date.now() - U.start) / 1000), time = `${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`;
  const allDone = !VIRTUAL && ALL.every((x) => P.done[x.id]);
  const go = mode === "jump" && pass ? { id: L.target.id, start: true, label: B(`Start lesson ${L.target.n} · ${L.target.name.en}`, `পাঠ ${asNum(L.target.n)} আৰম্ভ কৰা · ${L.target.name.as}`) }
    : !VIRTUAL && u === L.test && P.done.test && NEXT ? { id: NEXT.id, start: true, label: B(`Next: Lesson ${NEXT.n} · ${NEXT.name.en.split(" (")[0]}, Unit 1`, `পৰৱৰ্তী: পাঠ ${asNum(NEXT.n)} · ${NEXT.name.as.split(" (")[0]}, অধ্যায় ১`) } : null;
  const promptOf = (s) => s.q || s.s || (s.before ? B(`${s.before.en} ___ ${s.after.en}`, `${s.before.as} ___ ${s.after.as}`) : s.clues ? s.clues[0] : B("", ""));
  const title = mode === "diagnostic" ? B("Your starting map", "তোমাৰ আৰম্ভণিৰ মানচিত্ৰ") : mode === "drill" ? B("Practice complete!", "অনুশীলন সম্পূৰ্ণ!") : mode === "review" ? B("Memory mission complete!", "স্মৃতি অভিযান সম্পূৰ্ণ!") : mode === "checkpoint" ? B("Checkpoint finished", `${L.word.as}ৰ পৰীক্ষা শেষ`) : pass === false ? B("Not this time", "এইবাৰ নহ'ল") : mode === "jump" ? B("Jumped ahead!", "আগলৈ জঁপিয়ালা!") : U.practice ? B("Practice complete!", "অনুশীলন সম্পূৰ্ণ!") : u === L.test && allDone ? B("Lesson complete!", "পাঠ সম্পূৰ্ণ!") : B("Another step forward.", "আৰু এখোজ আগবাঢ়িলা।");
  const unitNo = mode === "lesson" && !U.practice && u !== L.test ? L.units.indexOf(u) + 1 : 0;
  const sub = unitNo ? B(`Unit ${unitNo} complete`, `অধ্যায় ${asNum(unitNo)} সম্পূৰ্ণ`) : u.title;
  const nextUnit = mode === "lesson" && !U.practice && !U.testout && u !== L.test ? ALL.findIndex((x) => !P.done[x.id]) : -1;
  AFTER = go ? { href: `lesson.html?id=${go.id}&start=0`, label: go.label } : mode === "review" && AXOM.reviewQueue().length ? { href: "lesson.html?review=1", label: B(`Continue reviewing · ${AXOM.reviewQueue().length} waiting`, `আৰু অনুশীলন কৰা · ${asNum(AXOM.reviewQueue().length)}টা বাকী`) }
    : nextUnit >= 0 ? { start: nextUnit, label: nextUnit === ALL.length - 1 ? B("Take the lesson test", "পাঠৰ পৰীক্ষা দিয়া") : B("Next unit", "পিছৰ অধ্যায়") } : null;
  const doneCount = ALL.filter((x) => P.done[x.id]).length;
  const missionResult = L.mission && u.mission && !U.practice && pass !== false ? `<div class="mission-result"><small>${T(L.mission.label)} · ${T(u === L.test ? B("File sealed", "নথি সম্পূৰ্ণ") : B("Finding recorded", "প্ৰমাণ লিখা হ'ল"))}</small><p>${T(u.mission.result)}</p></div>` : "";
  $("#done").innerHTML = `
    ${DONE_ART(pass !== false)}
    <h1>${T(title)}</h1>
    <p class="sub">${T(sub)}${wasDone && !U.practice && !VIRTUAL ? " · " + T(B("practice", "অনুশীলন")) : ""}</p>
    ${note ? `<p class="cp-note">${note}</p>` : ""}
    ${mode === "diagnostic" ? MATH.report(L.skillList) : ""}
    ${missionResult}
    <div class="stats">
      <div class="stat xp"><span class="stat-ic">${DONE_ICONS.star}</span><div><div class="v">+${N(U.xp)} XP</div><div class="h">${T(pass === false ? B("Keep practising", "অনুশীলন কৰি থাকা") : B("Well done!", "বহুত ভাল!"))}</div></div></div>
      <div class="stat streak"><span class="stat-ic">${DONE_ICONS.flame}</span><div><div class="v">${T(B(`${G.streak.n} day streak`, `${asNum(G.streak.n)} দিনৰ ধাৰা`))}</div><div class="h">${T(B("Keep going!", "আগবাঢ়ি থাকা!"))}</div></div></div>
    </div>
    ${u.learned && u.learned.length ? `<div class="card learned"><h3>${T(B("What you learned", "তুমি কি শিকিলা"))}</h3><ul>${u.learned.map((l) => `<li>${T(l)}</li>`).join("")}</ul></div>` : ""}
    ${U.mistakes.length ? `<div class="card mistakes"><h3>${T(B("Revise these", "এইবোৰ আকৌ চোৱা"))}</h3><ul>${U.mistakes.map((m) => `<li><span class="q">${T(promptOf(m.s))}</span>${answerHTML(m.s)}</li>`).join("")}</ul></div>` : ""}
    ${mode === "lesson" ? `<div class="card prog"><div class="prog-h"><b>${T(B("Lesson progress", "পাঠৰ অগ্ৰগতি"))}</b><span>${T(B(`${doneCount} of ${ALL.length} units complete`, `${asNum(ALL.length)}টাৰ ${asNum(doneCount)}টা অধ্যায় সম্পূৰ্ণ`))}</span></div><div class="prog-dots">${ALL.map((x) => `<i class="${P.done[x.id] ? "on" : ""}"></i>`).join("")}</div></div>` : ""}
    <p class="done-meta">${T(B(`${U.ok} of ${U.asked} right first time · ${time}`, `প্ৰথম চেষ্টাত ${asNum(U.asked)}টাৰ ${asNum(U.ok)}টা শুদ্ধ · ${asNum(time)}`))}</p>`;
  $("#done-btn").innerHTML = AFTER ? `${T(AFTER.label)}<svg viewBox="0 0 24 24"><path d="M4 12h15M13 6l6 6-6 6"/></svg>` : T(B("Continue", "আগবাঢ়া"));
  $("#done-back").classList[AFTER ? "remove" : "add"]("hidden");
  showView("v-done");
  const c = $("#confetti");
  c.innerHTML = Array.from({ length: 18 }, (_, k) => `<i style="left:${(k * 37) % 100}%;animation-delay:${(k % 9) * 0.12}s"></i>`).join("");
  c.classList.add("on"); setTimeout(() => c.classList.remove("on"), 3200);
}

// the "complete" seal: a japi-like disc inside a ring of woven ticks, with sprigs and falling leaves
const DONE_ICONS = {
  star: '<svg viewBox="0 0 24 24"><path fill="#F5A623" stroke="#E08A0B" stroke-width="1" stroke-linejoin="round" d="M12 2.6l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.5l-5.9 3.1 1.2-6.5L2.5 9.5l6.6-.9z"/></svg>',
  flame: '<svg viewBox="0 0 24 24"><path fill="#EF4A23" d="M12.6 1.8c.4 3.100-1.200 4.800-2.700 6.500C8.300 10 6.700 11.800 6.700 14.700c0 3.700 2.700 6.700 5.800 6.700s5.800-2.800 5.800-6.400c0-2.600-1.200-4.700-2.700-6.200-.3 1.500-.9 2.400-1.900 3 .3-2.700-.3-6.200-1.100-10z"/><path fill="#FFC531" d="M12.500 21.400c-1.800 0-3.200-1.500-3.200-3.300 0-1.600.9-2.600 1.800-3.600.7-.8 1.200-1.600 1.300-2.700 1.500 1.600 3.300 3.500 3.300 6 0 2-1.400 3.600-3.200 3.600z"/></svg>',
};
function DONE_ART(ok) {
  const C = 120, turn = (n) => Array.from({ length: n }, (_, k) => (k * 360) / n);
  const ticks = turn(60).map((a) => `<rect x="${C - 1.5}" y="24" width="3" height="${a % 18 ? 7 : 11}" rx="1.5" fill="#D8202B" opacity="${a % 18 ? .55 : .95}" transform="rotate(${a} ${C} ${C})"/>`).join("");
  const star = turn(8).map((a, k) => `<path d="M${C} 50l13 40h-26z" fill="${k % 2 ? "#D8202B" : "#20354A"}" transform="rotate(${a} ${C} ${C})"/>`).join("");
  const diamonds = turn(16).map((a) => `<path d="M${C} 42l3.500 5-3.500 5-3.500-5z" fill="#D8202B" transform="rotate(${a + 11.250} ${C} ${C})"/>`).join("");
  const leaf = (x, y, r, f, s = 1) => `<path d="M0 0c6-7 16-7 22 0-6 7-16 7-22 0z" fill="${f}" transform="translate(${x} ${y}) rotate(${r}) scale(${s})"/>`;
  const sprig = [[34, 176, -68], [28, 158, -96], [33, 139, -112], [46, 192, -44], [62, 205, -26]].map(([x, y, r], k) => leaf(x, y, r, k % 2 ? "#3C9A4E" : "#2B7D3F", .86));
  const falling = [[20, 30, 30, "#2B7D3F"], [58, 8, 110, "#E8A21E"], [176, 6, 60, "#D8202B"], [216, 34, 150, "#3C9A4E"], [10, 88, 200, "#D8202B"], [228, 96, 20, "#2B7D3F"], [120, 0, 80, "#2B7D3F"]].map(([x, y, r, f]) => leaf(x, y, r, f, .46)).join("");
  return `<svg class="done-art${ok ? "" : " miss"}" viewBox="0 0 240 228" aria-hidden="true">
    ${falling}<g>${sprig.join("")}</g><g transform="matrix(-1 0 0 1 240 0)">${sprig.join("")}</g>
    ${ticks}
    <circle cx="${C}" cy="${C}" r="78" fill="#D8202B"/><circle cx="${C}" cy="${C}" r="71" fill="#F4E2BE"/><circle cx="${C}" cy="${C}" r="71" fill="none" stroke="#B9851E" stroke-width="1.500" stroke-dasharray="3 4" opacity=".6"/>
    ${diamonds}${star}
    <circle cx="${C}" cy="${C}" r="31" fill="#fff"/><circle cx="${C}" cy="${C}" r="27" fill="#D8202B"/>
    ${ok ? `<path d="M${C - 13} ${C + 1}l9 9 17-20" fill="none" stroke="#fff" stroke-width="6.500" stroke-linecap="round" stroke-linejoin="round"/>` : `<path d="M${C - 11} ${C}h22" fill="none" stroke="#fff" stroke-width="6.500" stroke-linecap="round"/>`}
  </svg>`;
}

/* ---------- events ---------- */
function refreshSlotsHint() {
  $$("#screen .tslot").forEach((sl) => { const has = !!sl.querySelector(".tile"); sl.childNodes.forEach((n) => { if (n.nodeType === 1 && !n.classList.contains("tile")) n.style.display = has ? "none" : ""; }); });
}
document.addEventListener("click", (e) => {
  const g = (sel) => e.target.closest(sel);
  let b;
  if ((b = g("[data-ent]"))) { e.preventDefault(); return openEntity(b.dataset.ent); }
  if (g("[data-sources]")) return openSources();
  if (g("#guide")) return openGuide();
  if (g("#practise")) return startPractice();
  if ((b = g("[data-node]"))) { const k = +b.dataset.node; pop = pop === k ? null : k; SFX.tap(); return renderPath(); }
  if ((b = g("[data-start]"))) return startUnit(+b.dataset.start, b.hasAttribute("data-testout"));
  if ($("#v-path").classList.contains("on") && pop != null && !g(".pop")) { pop = null; return renderPath(); }
  if (g("#done-btn") && AFTER) { const a = AFTER; AFTER = null; if (a.href) { location.href = a.href; return; } return startUnit(a.start); }
  if (g("#done-btn") || g("#done-back") || g("#done-x")) { AFTER = null; if (VIRTUAL) { location.href = `index.html?course=${CID}${mode === "diagnostic" || mode === "drill" ? "&tab=skills" : ""}`; return; } showView("v-path"); renderPath(); return; }
  if (g("#exit")) return openLeave();
  if (g("[data-link]") && U) { const s0 = step().s; if (s0.link) return openLinkSheet(s0.link); }
  if (g("[data-keep]")) return closeSheet();
  if (g("[data-leave]")) { closeSheet(); if (VIRTUAL) { location.href = `index.html?course=${CID}`; return; } showView("v-path"); renderPath(); return; }
  if (!$("#v-play").classList.contains("on") || !U || U.phase !== "answer") return;

  const s = step().s, st = U.st, scr = $("#screen");
  if (g("#more")) { revealClue(s); SFX.tap(); return refresh(); }
  if ((b = g("[data-opt]")) && !b.disabled) {
    st.sel = +b.dataset.opt; $$("[data-opt]", scr).forEach((o) => o.classList.toggle("sel", o === b)); SFX.tap();
    if (s.type === "inline") $("[data-fillchip]", scr).innerHTML = T(s.options[st.sel]);
    return refresh();
  }
  if ((b = g("[data-tf]")) && !b.disabled) { st.sel = b.dataset.tf === "1"; return check(); }
  if ((b = g("[data-chip]")) && !b.disabled) { st.chip = +b.dataset.chip; $$("[data-chip]", scr).forEach((c) => c.classList.toggle("sel", c === b)); $(".as [data-fillchip]", scr).textContent = s.asOptions[st.chip]; SFX.tap(); return refresh(); }
  if ((b = g(".hit"))) { st.place = b.dataset.place; $$(".hit", scr).forEach((h) => h.classList.toggle("sel", h === b)); SFX.tap(); return refresh(); }
  if ((b = g("[data-letter]")) && !b.disabled) {
    const lg = b.dataset.lang, box = b.closest(".word-slots");
    if (box) { const slots = $$(".wslot", box), k = slots.indexOf(b.closest(".wslot")); st[lg].splice(k).forEach((li) => $(`.letters [data-letter="${li}"][data-lang="${lg}"]`, scr).classList.remove("used")); slots.slice(k).forEach((sl) => (sl.innerHTML = "")); }
    else { const slot = $$(`.word-slots[data-lang="${lg}"] .wslot`, scr)[st[lg].length]; if (!slot) return; slot.innerHTML = `<button class="tile" data-letter="${b.dataset.letter}" data-lang="${lg}">${b.textContent}</button>`; b.classList.add("used"); st[lg].push(+b.dataset.letter); }
    SFX.tap(); return refresh();
  }
  if ((b = g("[data-tok]")) && !b.disabled) { st.tok = +b.dataset.tok; $$(".tok", scr).forEach((t) => t.classList.toggle("sel", t === b)); SFX.tap(); return refresh(); }
  if ((b = g("[data-step]")) && !b.disabled) {
    if (b.closest(".bank")) { const slot = $$(".oslot", scr)[st.placed.length]; if (!slot) return; slot.insertAdjacentHTML("beforeend", `<button class="tile" data-step="${b.dataset.step}">${b.innerHTML}</button>`); b.classList.add("used"); st.placed.push(+b.dataset.step); }
    else { const slots = $$(".oslot", scr), k = slots.indexOf(b.closest(".oslot")); st.placed.splice(k).forEach((i) => $(`.bank [data-step="${i}"]`, scr).classList.remove("used")); slots.slice(k).forEach((o) => { const x = o.querySelector(".tile"); if (x) x.remove(); }); }
    SFX.tap(); return refresh();
  }
  if ((b = g("[data-pair]")) && !b.disabled) {
    const side = b.closest(".col").dataset.side;
    $$(`.col[data-side="${side}"] .tile`, scr).forEach((x) => x.classList.toggle("sel", x === b));
    st[side] = b;
    if (st.left && st.right) {
      const Lt = st.left, Rt = st.right; st.left = st.right = null; Lt.classList.remove("sel"); Rt.classList.remove("sel");
      if (Lt.dataset.pair === Rt.dataset.pair) { Lt.classList.add("done"); Rt.classList.add("done"); Lt.disabled = Rt.disabled = true; SFX.pair(); if (++st.matched === s.pairs.length) return check(); }
      else { st.misses++; SFX.bad(); [Lt, Rt].forEach((x) => { x.classList.remove("no"); void x.offsetWidth; x.classList.add("no"); setTimeout(() => x.classList.remove("no"), 450); }); }
    } else SFX.tap();
    return refresh();
  }
  if ((b = g("[data-item]")) && !b.disabled) {
    if (b.closest(".tslot")) { const k = b.dataset.item; delete st.placed[+k]; b.remove(); $(`.tbank [data-item="${k}"]`, scr).classList.remove("used"); refreshSlotsHint(); return refresh(); }
    st.armed = +b.dataset.item; $$(".tbank .tile", scr).forEach((x) => x.classList.toggle("sel", x === b)); $$(".tslot", scr).forEach((sl) => sl.classList.add("armed")); SFX.tap(); return refresh();
  }
  if ((b = g(".tslot")) && st.armed != null) {
    const k = st.armed, src = $(`.tbank [data-item="${k}"]`, scr);
    st.placed[k] = +b.dataset.slot; st.armed = null;
    b.insertAdjacentHTML("beforeend", `<button class="tile" data-item="${k}">${src.innerHTML}</button>`);
    src.classList.remove("sel"); src.classList.add("used"); $$(".tslot", scr).forEach((sl) => sl.classList.remove("armed"));
    refreshSlotsHint(); SFX.tap(); return refresh();
  }
});
$("#action").addEventListener("click", () => { if (step().s.type === "story" && U.phase !== "feedback" && storyBeat()) return; if (U.phase === "feedback" || step().s.type === "story") return next(); if (ready()) check(); });
$("#screen").addEventListener("click", (e) => { if (step() && step().s.type === "story" && !e.target.closest("button, a, input, .ent, .wx, .gfig")) storyBeat(); });
// Names and dates can contain spaces, digits and punctuation. The field is
// plain text and its value is compared with the authored answer, never HTML.
document.addEventListener("input", (e) => { if (!$("#v-play").classList.contains("on") || step().s.type !== "fill") return; refresh(); });
document.addEventListener("keydown", (e) => { if (e.key === "Enter" && $("#v-play").classList.contains("on") && !$("#action").disabled && !$("#sheet-root").innerHTML) { e.preventDefault(); $("#action").click(); } });
langBox.addEventListener("change", () => {
  if ($("#v-play").classList.contains("on") && U.phase === "answer" && ["fill", "unscramble", "spot"].includes(step().s.type)) renderStep(false);
  else if ($("#v-play").classList.contains("on")) refresh();
});
function openLeave() {
  $("#sheet-root").innerHTML = `<div class="backdrop" data-keep></div><div class="sheet"><h2>${T(B("Leave now?", "এতিয়া এৰি যাবা নে?"))}</h2><p>${T(B("Your progress in this round will be lost.", "এই পৰ্যায়ৰ অগ্ৰগতি হেৰাব।"))}</p>
    <button class="btn" data-keep>${T(B("Keep learning", "শিকি থাকোঁ"))}</button><button class="link" data-leave>${T(B("Leave", "এৰি যাওঁ"))}</button></div>`;
}
function closeSheet() { $("#sheet-root").innerHTML = ""; }

if (/[?&]debug\b/.test(location.search)) window.__L = { LESSON: L, run: () => U, render: renderStep, refresh, G, P, audioState: AXOM._audioState };   // test hook only

/* ---------- download this lesson for offline use ---------- */
function lessonFiles() {
  const files = new Set([L.portrait]);
  ALL.forEach((u) => u.steps.forEach((s) => { if (s.img) files.add(s.img); if (s.type === "picture") s.options.forEach((o) => files.add(o)); }));
  const urls = [`content/lessons/${L.id}.json`, "content/entities.json", "content/maps/assam.json", "content/maps/india.json"];
  files.forEach((f) => { urls.push(img(f), img(f, 480)); });
  return urls.map((u) => new URL(u, location.href).href);
}
async function setupOffline() {
  const btn = $("#offline");
  if (!("caches" in window)) { btn.remove(); return; }
  const urls = lessonFiles();
  const show = (state, a, b) => {
    btn.disabled = state !== "idle";
    btn.innerHTML = state === "saved" ? `${AXOM.ICON.check}${T(B("Offline", "অফলাইন"))}`
      : state === "busy" ? `${AXOM.ICON.download}${T(B(`${a}/${b}`, `${asNum(a)}/${asNum(b)}`))}`
      : `${AXOM.ICON.download}${T(B("Download", "ডাউনলোড"))}`;
  };
  show((await AXOM.isOffline(urls)) ? "saved" : "idle");
  btn.addEventListener("click", async () => {
    try { show("busy", 0, urls.length); await AXOM.saveOffline(urls, (a, b) => show("busy", a, b)); show("saved"); }
    catch (e) { show("idle"); console.warn(e); }
  });
}

if (VIRTUAL) {
  if (!L.test.steps.length) {
    showView("v-done");
    $("#done").innerHTML = `<svg class="done-art" viewBox="0 0 180 150" aria-hidden="true"><circle cx="90" cy="80" r="40" fill="var(--good)"/><path d="M70 80l14 14 26-28" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <h1>${T(mode === "review" ? B("All caught up!", "সকলো শেষ!") : B("Nothing to test yet", "পৰীক্ষা কৰিবলৈ এতিয়াও একো নাই"))}</h1>
      <p class="sub">${T(mode === "review" ? B("No questions are due today. Come back tomorrow.", "আজি কোনো প্ৰশ্ন বাকী নাই। কাইলৈ আহিবা।") : B("Finish some lessons of this era first.", "প্ৰথমে এই যুগৰ কিছু পাঠ শেষ কৰা।"))}</p>`;
  } else startUnit(ALL.length - 1);
} else {
  HERE = [$(".hero"), $("#mission-slot"), $("#mistake-slot")];
  showView("v-path"); renderPath(); setupOffline();
  const k = params.has("start") ? +params.get("start") : -1, testout = params.has("testout");
  history.replaceState(null, "", `lesson.html?id=${L.id}${UNLOCK_ALL ? "&all" : ""}${params.has("debug") ? "&debug" : ""}`);
  if (k >= 0 && k < ALL.length && (unlocked(k) || (testout && ALL[k] === L.test && !GATE))) startUnit(k, testout && !unlocked(k));
}
}   // end boot

load();
// When a new app version takes over: reload now if the learner is on the unit path, or as soon as they return to it.
// A unit being played is never interrupted.
if ("serviceWorker" in navigator && navigator.serviceWorker.controller) {
  navigator.serviceWorker.addEventListener("controllerchange", () => {
    const playing = document.querySelector("#v-play.on, #v-done.on");
    if (playing) pendingUpdate = true; else location.reload();
  });
}
})();
