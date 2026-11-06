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
const INK = "#16305C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F", FAINT = "#7E93AE";
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
})();
