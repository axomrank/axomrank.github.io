/* =========================================================
   AxomRank reasoning stage: scenes where the action is the reasoning.
   docs/REASONING-COURSE.md lists them. Same contract as app/mathstage.js:
   { value(), state(), touched(), freeze(), show(v), demo(goal) }
   shift: a code wheel. walk: a walker whose left and right turn with them.
   venn: tap regions. setpick: choose the diagram that fits.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#1B272C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F", FAINT = "#7E93AE";
const AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const encode = (word, k) => [...word].map((c) => (AZ.includes(c) ? AZ[(AZ.indexOf(c) + k + 2600) % 26] : c)).join("");
let uid = 0;
// T() writes HTML spans, which SVG text cannot show. Language switching works the same way on tspans.
const ST = (o) => `<tspan class="en">${o.en}</tspan><tspan class="as">${o.as}</tspan>`;

/* ---------- shift: outer ring is the plain letter, inner ring the code letter ---------- */
W.shift = (el, w, on) => {
  const min = w.min ?? -12, max = w.max ?? 13, step = 360 / 26, cx = 160, cy = 160;
  let k = w.start || 0, touched = false, locked = false;
  const ring = (r, cls, make) => [...AZ].map((c, i) => { const a = (i * step - 90) * Math.PI / 180; return `<text class="${cls}" data-c="${c}" x="${(cx + r * Math.cos(a)).toFixed(1)}" y="${(cy + r * Math.sin(a) + 5).toFixed(1)}" text-anchor="middle" transform="rotate(${(i * step).toFixed(1)} ${(cx + r * Math.cos(a)).toFixed(1)} ${(cy + r * Math.sin(a)).toFixed(1)})">${make(i)}</text>`; }).join("");
  el.innerHTML = `<svg class="whl" viewBox="0 0 320 320" role="img" aria-label="Code wheel">
      <circle cx="${cx}" cy="${cy}" r="152" fill="#fff" stroke="${INK}" stroke-width="2"/><circle cx="${cx}" cy="${cy}" r="124" fill="#EEF4FB" stroke="${FAINT}"/>
      <g>${ring(138, "pl", (i) => AZ[i])}</g><g id="inner">${ring(106, "cd", (i) => AZ[i])}</g>
      <text x="${cx}" y="${cy - 8}" text-anchor="middle" class="whk" id="whk"></text>
      <text x="${cx}" y="${cy + 18}" text-anchor="middle" class="whs">${ST(B("outer → inner", "বাহিৰ → ভিতৰ"))}</text></svg>
    <input class="wx-range" type="range" min="${min}" max="${max}" step="1" value="${k}" aria-label="Shift">
    <div class="wx-out"></div>`;
  const input = $("input", el), inner = $("#inner", el), out = $(".wx-out", el);
  const draw = () => {
    inner.setAttribute("transform", `rotate(${(-k * step).toFixed(2)} ${cx} ${cy})`);
    $("#whk", el).textContent = `${k > 0 ? "+" : k < 0 ? "−" : ""}${Math.abs(k)}`;
    el.querySelectorAll("text.pl").forEach((t) => t.classList.toggle("hit", !!w.word && w.word.includes(t.dataset.c)));
    out.innerHTML = w.word ? `<div class="wx-read"><b>${w.word}</b> → <b class="${w.code === encode(w.word, k) ? "yes" : ""}">${encode(w.word, k)}</b>${w.code ? `<span class="whg">${T(B("target", "লক্ষ্য"))}: ${w.code}</span>` : ""}</div>` : "";
  };
  const set = (v) => { k = v; input.value = v; touched = true; draw(); on(); };
  input.addEventListener("input", () => { if (locked) return; k = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  return { value: () => k, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: set, state: () => ({ k }), demo(g) { set(g.k); } };
};

/* ---------- walk: facing is 0 N, 1 E, 2 S, 3 W ---------- */
const DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]];
W.walk = (el, w, on) => {
  const c = 34, mid = 160, R = 4, sx = (x) => mid + x * c, sy = (y) => mid - y * c;
  const start = { x: w.x || 0, y: w.y || 0, f: w.f || 0 };
  let x = start.x, y = start.y, f = start.f, trail = [[x, y]], touched = false, locked = false;
  const grid = Array.from({ length: 2 * R + 1 }, (_, i) => { const p = mid + (i - R) * c, a = mid - R * c, b = mid + R * c; return `<path d="M${p} ${a}V${b}M${a} ${p}H${b}" stroke="#D5E1EF"/>`; }).join("");
  const mark = (t, px, py) => `<text x="${px}" y="${py}" text-anchor="middle" class="wlc">${t}</text>`;
  el.innerHTML = `<svg class="wlk" viewBox="0 0 320 320" role="img" aria-label="Walking map">${grid}
      ${mark(ST(B("N", "উ")), 160, 14)}${mark(ST(B("E", "পূ")), 310, 165)}${mark(ST(B("S", "দ")), 160, 316)}${mark(ST(B("W", "প")), 10, 165)}
      <circle cx="${sx(start.x)}" cy="${sy(start.y)}" r="5" fill="${FAINT}"/><polyline id="tr" fill="none" stroke="${BLUE}" stroke-width="3" stroke-linejoin="round"/><g id="me"></g></svg>
    <div class="wlk-keys"><button class="tile" data-wl>↺ ${T(B("Left", "বাওঁ"))}</button>${w.turnOnly ? "" : `<button class="tile" data-ws>↑ ${T(B("Step", "খোজ"))}</button>`}<button class="tile" data-wr>${T(B("Right", "সোঁ"))} ↻</button></div>
    <button class="chip-btn wlk-reset" data-w0>${T(B("Start again", "পুনৰ আৰম্ভ"))}</button>`;
  const value = () => (w.ask === "place" ? (x + 50) * 100 + y + 50 : f);
  const draw = () => {
    $("#tr", el).setAttribute("points", trail.map(([a, b]) => `${sx(a)},${sy(b)}`).join(" "));
    const px = sx(x), py = sy(y), [dx, dy] = DIRS[f];
    const leftX = px - dy * 27, leftY = py - dx * 27, rightX = px + dy * 27, rightY = py + dx * 27;
    $("#me", el).innerHTML = `<g transform="translate(${px} ${py}) rotate(${f * 90})"><path d="M0 -14L10 11L0 6L-10 11Z" fill="${RED}" stroke="#fff" stroke-width="1.5"/></g>
      <text class="wls" x="${leftX}" y="${leftY + 4}" text-anchor="middle">${ST(B("L", "বাওঁ"))}</text><text class="wls" x="${rightX}" y="${rightY + 4}" text-anchor="middle">${ST(B("R", "সোঁ"))}</text>`;
  };
  const act = () => { touched = true; SFX.tap(); draw(); on(); };
  el.addEventListener("click", (e) => {
    if (locked) return;
    if (e.target.closest("[data-wl]")) { f = (f + 3) % 4; act(); }
    else if (e.target.closest("[data-wr]")) { f = (f + 1) % 4; act(); }
    else if (e.target.closest("[data-ws]")) { const nx = x + DIRS[f][0], ny = y + DIRS[f][1]; if (Math.abs(nx) > R || Math.abs(ny) > R) return; x = nx; y = ny; trail.push([x, y]); act(); }
    else if (e.target.closest("[data-w0]")) { x = start.x; y = start.y; f = start.f; trail = [[x, y]]; act(); }
  });
  draw();
  const go = (g) => { if (g.x != null) x = g.x; if (g.y != null) y = g.y; if (g.f != null) f = g.f; trail.push([x, y]); touched = true; draw(); on(); };
  return { value, touched: () => touched, freeze() { locked = true; el.querySelectorAll("button").forEach((b) => (b.disabled = true)); },
    show(v) { go(w.ask === "place" ? { x: Math.floor(v / 100) - 50, y: (v % 100) - 50 } : { f: ((v % 4) + 4) % 4 }); }, state: () => ({ x, y, f }), demo: go };
};

/* ---------- venn: a region is the set of circles a point sits in, as bits. Value: one bit per shaded region ---------- */
const VENN = {
  2: { c: [[120, 120, 82], [200, 120, 82]], at: { 1: [80, 125], 2: [240, 125], 3: [160, 125] }, labels: [[62, 26], [258, 26]], h: 220 },
  3: { c: [[120, 98, 72], [200, 98, 72], [160, 168, 72]], at: { 1: [84, 76], 2: [236, 76], 3: [160, 62], 4: [160, 208], 5: [106, 146], 6: [214, 146], 7: [160, 118] }, labels: [[50, 14], [270, 14], [282, 226]], h: 248 },
};
W.venn = (el, w, on) => {
  const n = w.n || 2, G = VENN[n], id = `vn${++uid}`, COL = [BLUE, RED, GREEN];
  let sel = 0, touched = false, locked = false;
  const defs = G.c.map(([x, y, r], i) => `<clipPath id="${id}c${i}"><circle cx="${x}" cy="${y}" r="${r}"/></clipPath><mask id="${id}m${i}"><rect width="320" height="${G.h}" fill="#fff"/><circle cx="${x}" cy="${y}" r="${r}" fill="#000"/></mask>`).join("");
  const region = (m) => G.c.reduce((inner, _, i) => `<g ${(m >> i) & 1 ? `clip-path="url(#${id}c${i})"` : `mask="url(#${id}m${i})"`}>${inner}</g>`, `<rect width="320" height="${G.h}" fill="${GOLD}" opacity=".62"/>`);
  const names = (w.sets || []).map((s, i) => `<text class="vnl" x="${G.labels[i][0]}" y="${G.labels[i][1]}" text-anchor="middle" fill="${COL[i]}">${ST(s)}</text>`).join("");
  const count = (m) => (w.counts && w.counts[m] != null ? `<text class="vnn" x="${m ? G.at[m][0] : 296}" y="${m ? G.at[m][1] : G.h - 10}" text-anchor="middle">${w.counts[m]}</text>` : "");
  el.innerHTML = `<svg class="vn" viewBox="0 0 320 ${G.h}" role="img" aria-label="Venn diagram"><defs>${defs}</defs><rect x="1" y="1" width="318" height="${G.h - 2}" rx="8" fill="#fff" stroke="${FAINT}"/><g id="sh"></g>
      ${G.c.map(([x, y, r], i) => `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="${COL[i]}" stroke-width="2.5"/>`).join("")}${names}${Array.from({ length: 2 ** n }, (_, m) => count(m)).join("")}</svg><div class="wx-out"></div>`;
  const svg = $("svg", el);
  const draw = () => {
    $("#sh", el).innerHTML = Array.from({ length: 2 ** n }, (_, m) => m).filter((m) => (sel >> m) & 1).map(region).join("");
    const total = w.counts ? Object.entries(w.counts).reduce((a, [m, v]) => a + ((sel >> +m) & 1 ? v : 0), 0) : null;
    $(".wx-out", el).innerHTML = w.counts && w.showTotal ? `<div class="wx-read">${T(B("Shaded", "ছাঁ দিয়া"))}: <b>${total}</b></div>` : "";
  };
  svg.addEventListener("click", (e) => {
    if (locked) return;
    const b = svg.getBoundingClientRect(), px = ((e.clientX - b.left) / b.width) * 320, py = ((e.clientY - b.top) / b.height) * G.h;
    const m = G.c.reduce((a, [x, y, r], i) => a + (Math.hypot(px - x, py - y) <= r ? 1 << i : 0), 0);
    sel ^= 1 << m; touched = true; SFX.tap(); draw(); on();
  });
  draw();
  const set = (v) => { sel = v; touched = true; draw(); on(); };
  return { value: () => sel, touched: () => touched, freeze() { locked = true; }, show: set, state: () => ({ sel }), demo(g) { set(g.sel); } };
};

/* ---------- setpick: tap the diagram. Each option is a list of [x, y, r] in a 100-unit box ---------- */
W.setpick = (el, w, on) => {
  let pick = null, locked = false;
  const COL = [BLUE, RED, GREEN];
  const face = (circles) => `<svg viewBox="0 0 100 100" aria-hidden="true">${circles.map(([x, y, r, t], i) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${COL[i]}" fill-opacity=".1" stroke="${COL[i]}" stroke-width="2"/>`).join("")}</svg>`;
  const draw = () => { el.innerHTML = `<div class="spk">${w.options.map((o, k) => `<button class="tile spk-o ${pick === k ? "sel" : ""}" data-sp="${k}" aria-label="Diagram ${k + 1}">${face(o)}</button>`).join("")}</div>`; };
  el.addEventListener("click", (e) => { const b = e.target.closest("[data-sp]"); if (!b || locked) return; pick = +b.dataset.sp; SFX.tap(); draw(); on(); });
  draw();
  return { value: () => pick, touched: () => pick != null, freeze() { locked = true; }, show(v) { pick = v; draw(); on(); }, state: () => ({ pick }) };
};

/* ---------- alpha: the alphabet as two rows. fold pairs each letter with its opposite ---------- */
W.alpha = (el, w, on) => {
  let pick = null, locked = false;
  const top = [..."ABCDEFGHIJKLM"], low = w.fold ? [..."ZYXWVUTSRQPON"] : [..."NOPQRSTUVWXYZ"];
  const cell = (c) => { const p = AZ.indexOf(c) + 1, mate = AZ[26 - p]; return `<button class="tile alc ${pick === p ? "sel" : ""} ${w.fold && pick && AZ[pick - 1] === mate ? "mate" : ""}" data-al="${p}">${c}${w.nums ? `<small>${p}</small>` : ""}</button>`; };
  const draw = () => { el.innerHTML = `<div class="alr">${top.map(cell).join("")}</div><div class="alr">${low.map(cell).join("")}</div>`; };
  el.addEventListener("click", (e) => { const b = e.target.closest("[data-al]"); if (!b || locked) return; pick = +b.dataset.al; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { pick = v; draw(); on(); };
  return { value: () => pick, touched: () => pick != null, freeze() { locked = true; }, show: set, state: () => ({ pick }), demo(g) { set(g.pick); } };
};

/* ---------- gaps: tap to open each level of differences, then set the next term ---------- */
W.gaps = (el, w, on) => {
  const t = w.terms, name = (v) => (w.letters ? AZ[((v - 1) % 26 + 26) % 26] : v);
  const levels = [t]; while (levels.length < 3) { const l = levels[levels.length - 1]; levels.push(l.slice(1).map((v, i) => v - l[i])); }
  let opened = 0, next = t[t.length - 1], touched = false, locked = false;
  const row = (l, i) => `<div class="gpr l${i}">${l.map((v) => `<span>${i === 0 ? name(v) : (v > 0 ? "+" : "") + String(v).replace("-", "−")}</span>`).join("")}</div>`;
  const draw = () => { el.innerHTML = `<div class="gpb">${levels.slice(0, opened + 1).map(row).join("")}</div>
      ${opened < 2 ? `<button class="chip-btn gpo" data-gp>${T(opened ? B("Open the gaps of the gaps", "ব্যৱধানৰ ব্যৱধান খোলা") : B("Open the gaps", "ব্যৱধান খোলা"))}</button>` : ""}
      <div class="wx-step"><button class="tile" data-gless aria-label="Less">−</button><span>${T(B("Next term", "পিছৰ পদ"))}: <b>${name(next)}</b></span><button class="tile" data-gmore aria-label="More">+</button></div>`; };
  el.addEventListener("click", (e) => {
    if (locked) return;
    if (e.target.closest("[data-gp]")) opened++;
    else if (e.target.closest("[data-gmore]")) next++;
    else if (e.target.closest("[data-gless]")) next--;
    else return;
    touched = true; SFX.tap(); draw(); on();
  });
  draw();
  const set = (v) => { next = v; touched = true; draw(); on(); };
  return { value: () => next, touched: () => touched, freeze() { locked = true; el.querySelectorAll("button").forEach((b) => (b.disabled = true)); }, show: set, state: () => ({ opened, next }), demo(g) { if (g.opened != null) opened = g.opened; if (g.next != null) next = g.next; touched = true; draw(); on(); } };
};

/* ---------- tree: climb generations. value: generations above (+) or below (−) the start ---------- */
W.tree = (el, w, on) => {
  let gen = 0, touched = false, locked = false;
  const rows = [2, 1, 0, -1, -2], word = { 2: B("Grandparents", "আজোককাসকল"), 1: B("Parents", "পিতৃ-মাতৃ"), 0: B("My generation", "মোৰ প্ৰজন্ম"), "-1": B("Children", "সন্তান"), "-2": B("Grandchildren", "নাতি-নাতিনী") };
  const draw = () => { el.innerHTML = `<div class="trb">${rows.map((r) => `<div class="trr ${r === gen ? "on" : ""}"><span>${T(word[r])}</span><b>${r === gen ? "●" : ""}</b></div>`).join("")}</div>
      <div class="wlk-keys"><button class="tile" data-tu>↑ ${T(B("Parent", "পিতৃ/মাতৃ"))}</button><button class="tile" data-td>↓ ${T(B("Child", "সন্তান"))}</button></div>`; };
  el.addEventListener("click", (e) => { if (locked) return; if (e.target.closest("[data-tu]")) gen = Math.min(2, gen + 1); else if (e.target.closest("[data-td]")) gen = Math.max(-2, gen - 1); else return; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { gen = v; touched = true; draw(); on(); };
  return { value: () => gen, touched: () => touched, freeze() { locked = true; el.querySelectorAll("button").forEach((b) => (b.disabled = true)); }, show: set, state: () => ({ gen }), demo(g) { set(g.gen); } };
};

/* ---------- queue: slide one person along a line; both ranks change together ---------- */
W.queue = (el, w, on) => {
  const n = w.n; let pos = w.start || 1, touched = false, locked = false;
  el.innerHTML = `<div class="qur"></div><input class="wx-range" type="range" min="1" max="${n}" step="1" value="${pos}" aria-label="Place"><div class="wx-out"></div>`;
  const input = $("input", el);
  const draw = () => {
    $(".qur", el).innerHTML = Array.from({ length: n }, (_, k) => `<i class="${k + 1 === pos ? "on" : ""}"></i>`).join("");
    $(".wx-out", el).innerHTML = `<div class="wx-read">${T(B("From left", "বাওঁৰ পৰা"))}: <b>${pos}</b> · ${T(B("From right", "সোঁৰ পৰা"))}: <b>${w.hideRight ? "?" : n - pos + 1}</b></div>`;
  };
  input.addEventListener("input", () => { if (locked) return; pos = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { pos = v; input.value = v; touched = true; draw(); on(); };
  return { value: () => pos, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: set, state: () => ({ pos }), demo(g) { set(g.pos); } };
};

/* ---------- seats: tap a name, then a seat. value: seat order as one number (1-based names, base 10) ---------- */
W.seats = (el, w, on) => {
  const n = w.names.length, seat = Array(n).fill(0), cx = 150, cy = 120, R = 86; let hold = 0, touched = false, locked = false;
  const code = () => seat.reduce((a, s) => a * 10 + s, 0);
  const at = (k) => { const a = (k / n) * 2 * Math.PI - Math.PI / 2; return [cx + R * Math.cos(a), cy + R * Math.sin(a)]; };
  const draw = () => {
    const spots = w.round ? `<div class="sts rd"><svg viewBox="0 0 300 240" aria-hidden="true"><circle cx="${cx}" cy="${cy}" r="${R - 26}" fill="#EEF4FB" stroke="#7E93AE"/></svg>${seat.map((s, k) => { const [x, y] = at(k); return `<button class="tile stc" style="left:${(x / 300) * 100}%;top:${(y / 240) * 100}%" data-st="${k}">${s ? w.names[s - 1] : k + 1}</button>`; }).join("")}</div>`
      : `<div class="sts">${seat.map((s, k) => `<button class="tile stl" data-st="${k}">${s ? w.names[s - 1] : k + 1}</button>`).join("")}</div>`;
    el.innerHTML = `${spots}<div class="wx-keys">${w.names.map((m, k) => `<button class="tile ${hold === k + 1 ? "sel" : ""}" data-nm="${k + 1}" ${seat.includes(k + 1) ? "disabled" : ""}>${m}</button>`).join("")}</div><button class="chip-btn wlk-reset" data-st0>${T(B("Clear", "মচা"))}</button>`;
  };
  el.addEventListener("click", (e) => {
    if (locked) return;
    const a = e.target.closest("[data-nm]"), b = e.target.closest("[data-st]");
    if (a) hold = +a.dataset.nm;
    else if (b && hold) { seat[+b.dataset.st] = hold; hold = 0; touched = true; }
    else if (e.target.closest("[data-st0]")) { seat.fill(0); hold = 0; }
    else return;
    SFX.tap(); draw(); on();
  });
  draw();
  const set = (v) => { String(v).padStart(n, "0").split("").forEach((d, k) => (seat[k] = +d)); touched = true; draw(); on(); };
  return { value: code, ready: () => seat.every(Boolean), touched: () => touched, freeze() { locked = true; }, show: set, state: () => ({ code: code() }), demo(g) { set(g.code); } };
};

/* ---------- oddday: a seven-day wheel. value: day index, 0 Sunday ---------- */
const DAYS = [B("Sun", "দেও"), B("Mon", "সোম"), B("Tue", "মঙ্গল"), B("Wed", "বুধ"), B("Thu", "বৃহস্পতি"), B("Fri", "শুক্ৰ"), B("Sat", "শনি")];
W.oddday = (el, w, on) => {
  const start = w.start || 0; let day = start, touched = false, locked = false;
  const draw = () => { el.innerHTML = `<div class="ody">${DAYS.map((d, k) => `<span class="${k === day ? "on" : ""}">${T(d)}</span>`).join("")}</div>
      <div class="wlk-keys">${[1, 2, 3].map((k) => `<button class="tile" data-od="${k}">+${k}</button>`).join("")}<button class="tile" data-od="-1">−1</button></div>`; };
  el.addEventListener("click", (e) => { const b = e.target.closest("[data-od]"); if (!b || locked) return; day = (day + +b.dataset.od + 7) % 7; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { day = ((v % 7) + 7) % 7; touched = true; draw(); on(); };
  return { value: () => day, touched: () => touched, freeze() { locked = true; el.querySelectorAll("button").forEach((b) => (b.disabled = true)); }, show: set, state: () => ({ day }), demo(g) { set(g.day); } };
};

/* ---------- hands: run a clock. value: minutes past the starting hour ---------- */
W.hands = (el, w, on) => {
  const h0 = w.hour ?? 3; let min = w.start || 0, touched = false, locked = false;
  const ticks = Array.from({ length: 12 }, (_, k) => { const a = (k / 6) * Math.PI; return `<line x1="${100 + 80 * Math.sin(a)}" y1="${100 - 80 * Math.cos(a)}" x2="${100 + 88 * Math.sin(a)}" y2="${100 - 88 * Math.cos(a)}" stroke="${INK}" stroke-width="2"/>`; }).join("");
  el.innerHTML = `<svg class="hnd" viewBox="0 0 200 200" role="img" aria-label="Clock"><circle cx="100" cy="100" r="92" fill="#fff" stroke="${INK}" stroke-width="3"/>${ticks}<line id="hh" x1="100" y1="100" stroke="${RED}" stroke-width="6" stroke-linecap="round"/><line id="mh" x1="100" y1="100" stroke="${BLUE}" stroke-width="4" stroke-linecap="round"/></svg>
    <input class="wx-range" type="range" min="0" max="${w.max || 60}" step="1" value="${min}" aria-label="Minutes"><div class="wx-out"></div>`;
  const input = $("input", el);
  const draw = () => {
    const ma = min * 6, ha = h0 * 30 + min * 0.5, gap = Math.abs(((ma - ha) % 360 + 360) % 360), sep = Math.min(gap, 360 - gap), hand = (id, deg, r) => { const a = (deg * Math.PI) / 180, l = $(id, el); l.setAttribute("x2", 100 + r * Math.sin(a)); l.setAttribute("y2", 100 - r * Math.cos(a)); };
    hand("#hh", ha, 50); hand("#mh", ma, 76);
    $(".wx-out", el).innerHTML = `<div class="wx-read">${h0}:${String(min).padStart(2, "0")}${w.angle ? ` · ${T(B("Angle", "কোণ"))}: <b>${sep}°</b>` : ""}</div>`;
  };
  input.addEventListener("input", () => { if (locked) return; min = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { min = v; input.value = v; touched = true; draw(); on(); };
  return { value: () => min, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: set, state: () => ({ min }), demo(g) { set(g.min); } };
};

/* ---------- figures drawn from data: ["c",x,y,r,fill] ["r",x,y,w,h,fill] ["p",points,fill] ["l",x1,y1,x2,y2] ["t",x,y,text] in a 100-unit box ---------- */
const shape = (s) => {
  const stroke = `stroke="${INK}" stroke-width="2.5"`, fill = (f) => `fill="${f || "none"}"`;
  if (s[0] === "c") return `<circle cx="${s[1]}" cy="${s[2]}" r="${s[3]}" ${fill(s[4])} ${stroke}/>`;
  if (s[0] === "r") return `<rect x="${s[1]}" y="${s[2]}" width="${s[3]}" height="${s[4]}" ${fill(s[5])} ${stroke}/>`;
  if (s[0] === "p") return `<polygon points="${s[1].map((q) => q.join(",")).join(" ")}" ${fill(s[2])} ${stroke}/>`;
  if (s[0] === "l") return `<line x1="${s[1]}" y1="${s[2]}" x2="${s[3]}" y2="${s[4]}" ${stroke}/>`;
  return `<text x="${s[1]}" y="${s[2]}" text-anchor="middle" font-size="${s[4] || 22}" font-weight="900" fill="${INK}">${s[3]}</text>`;
};
const figure = (f) => `<svg viewBox="0 0 100 100" aria-hidden="true">${f.map(shape).join("")}</svg>`;
W.figpick = (el, w, on) => {
  let pick = null, locked = false;
  const stem = w.stem ? `<div class="fgs">${w.stem.map((f) => (f ? `<span>${figure(f)}</span>` : `<span class="q">?</span>`)).join("")}</div>` : "";
  const draw = () => { el.innerHTML = `${stem}<div class="spk">${w.options.map((o, k) => `<button class="tile spk-o ${pick === k ? "sel" : ""}" data-fp="${k}" aria-label="Figure ${k + 1}">${figure(o)}</button>`).join("")}</div>`; };
  el.addEventListener("click", (e) => { const b = e.target.closest("[data-fp]"); if (!b || locked) return; pick = +b.dataset.fp; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { pick = v; draw(); on(); };
  return { value: () => pick, touched: () => pick != null, freeze() { locked = true; }, show: set, state: () => ({ pick }), demo(g) { set(g.pick); } };
};

/* ---------- dicenet: a cross-shaped net. Tap the face that lands opposite the marked one ---------- */
W.dicenet = (el, w, on) => {
  let pick = null, locked = false;
  const draw = () => { el.innerHTML = `<div class="dnt">${w.net.map((r) => `<div>${r.map((v) => (v === null ? "<i></i>" : `<button class="tile ${v === w.mark ? "mk" : ""} ${pick === v ? "sel" : ""}" data-dn="${v}">${v}</button>`)).join("")}</div>`).join("")}</div>`; };
  el.addEventListener("click", (e) => { const b = e.target.closest("[data-dn]"); if (!b || locked) return; pick = +b.dataset.dn; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { pick = v; draw(); on(); };
  return { value: () => pick, touched: () => pick != null, freeze() { locked = true; }, show: set, state: () => ({ pick }), demo(g) { set(g.pick); } };
};

/* ---------- numgrid: rows of numbers with one hidden cell; step it to the value ---------- */
W.numgrid = (el, w, on) => {
  let val = w.start ?? 0, touched = false, locked = false;
  const draw = () => { el.innerHTML = `<div class="ngd" style="--c:${w.rows[0].length}">${w.rows.map((r) => r.map((v) => `<span class="${v === null ? "q" : ""}">${v === null ? (touched ? val : "?") : v}</span>`).join("")).join("")}</div>
      <div class="wx-step"><button class="tile" data-ngl aria-label="Less">−</button><span><b>${val}</b></span><button class="tile" data-ngm aria-label="More">+</button></div>`; };
  el.addEventListener("click", (e) => { if (locked) return; if (e.target.closest("[data-ngm]")) val++; else if (e.target.closest("[data-ngl]")) val--; else return; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { val = v; touched = true; draw(); on(); };
  return { value: () => val, touched: () => touched, freeze() { locked = true; el.querySelectorAll("button").forEach((b) => (b.disabled = true)); }, show: set, state: () => ({ val }), demo(g) { set(g.val); } };
};

/* ---------- bars: a chart you read by tapping a bar ---------- */
W.bars = (el, w, on) => {
  let pick = null, locked = false; const top = Math.max(...w.vals);
  const draw = () => { el.innerHTML = `<div class="brs">${w.vals.map((v, k) => `<button class="brc ${pick === k ? "sel" : ""}" data-br="${k}" aria-label="${w.labels[k]}"><b>${w.hide ? "" : v}</b><i style="height:${Math.round((v / top) * 130)}px"></i><span>${w.labels[k]}</span></button>`).join("")}</div>`; };
  el.addEventListener("click", (e) => { const b = e.target.closest("[data-br]"); if (!b || locked) return; pick = +b.dataset.br; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { pick = v; draw(); on(); };
  return { value: () => pick, touched: () => pick != null, freeze() { locked = true; }, show: set, state: () => ({ pick }), demo(g) { set(g.pick); } };
};
})();
