/* =========================================================
   AxomRank maths stage, part seven: figures.
   scaleup: area and volume scale, shear: triangle area, sticks: triangle rule, kite: rhombus,
   roll: circumference, sectors: circle area, exterior: outer angle, tangent: tangent and radius,
   fence: fixed perimeter, stack: volume, net: surface, pour: cone.
   Same contract as app/mathstage.js. The reasons are in docs/MATHEMATICS-VISUALS.md.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#1B272C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F";
const short = (v) => +v.toFixed(2);
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
// A scene with one slider: redraw on change, freeze on check, jump for Show me.
function slider(el, html, start, draw, on, keys) {
  el.innerHTML = html;
  const input = $("input", el); let v = start, touched = false, locked = false;
  input.addEventListener("input", () => { if (locked) return; v = +input.value; touched = true; SFX.tap(); draw(v); on(); });
  draw(v);
  const set = (x) => { v = x; input.value = x; touched = true; draw(v); on(); };
  return { value: () => v, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: set, state: () => ({ [keys]: v }), demo(g) { set(g[keys]); } };
}
function isoCube(x, y, z, s, top, left, right) {
  const X = (a, b) => 170 + (a - b) * s * 0.87, Y = (a, b, c) => 150 + (a + b) * s * 0.5 - c * s;
  const p = (a, b, c) => `${X(a, b).toFixed(1)},${Y(a, b, c).toFixed(1)}`;
  return `<polygon points="${p(x, y, z + 1)} ${p(x + 1, y, z + 1)} ${p(x + 1, y + 1, z + 1)} ${p(x, y + 1, z + 1)}" fill="${top}" stroke="#fff"/><polygon points="${p(x, y + 1, z + 1)} ${p(x + 1, y + 1, z + 1)} ${p(x + 1, y + 1, z)} ${p(x, y + 1, z)}" fill="${left}" stroke="#fff"/><polygon points="${p(x + 1, y, z + 1)} ${p(x + 1, y + 1, z + 1)} ${p(x + 1, y + 1, z)} ${p(x + 1, y, z)}" fill="${right}" stroke="#fff"/>`;
}
const blocks = (l, b, h, s, c = ["#7FA9E6", BLUE, "#174A97"]) => { let o = ""; for (let z = 0; z < h; z++) for (let y = 0; y < b; y++) for (let x = 0; x < l; x++) o += isoCube(x - l / 2, y - b / 2, z, s, ...c); return o; };

/* ---------- scale-up: k times the side is k² times the area and k³ times the volume ---------- */
W.scaleup = (el, w, on) => {
  const three = w.dim === 3, top = w.max || 4;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 200" role="img" aria-label="A shape scaled up"><g id="sg"></g></svg><input class="wx-range" type="range" min="1" max="${top}" value="${w.k || 1}" aria-label="Scale"><div class="wx-read fg-read"></div>`, w.k || 1, (k) => {
    const g = $("#sg", el);
    if (three) { const s = 92 / top * 1.15; g.innerHTML = blocks(k, k, k, s); }
    else { const c = 180 / top, x0 = 170 - (k * c) / 2, y0 = 190 - k * c; let o = ""; for (let i = 0; i < k; i++) for (let j = 0; j < k; j++) o += `<rect x="${x0 + i * c + 1}" y="${y0 + j * c + 1}" width="${c - 2}" height="${c - 2}" fill="${i === 0 && j === k - 1 ? GOLD : BLUE}"/>`; g.innerHTML = o; }
    $(".fg-read", el).innerHTML = three ? `${T(B("Side", "বাহু"))} $\\times ${k}$ ${T(B("gives volume", "ত আয়তন"))} <b>$\\times ${k ** 3}$</b>` : `${T(B("Side", "বাহু"))} $\\times ${k}$ ${T(B("gives area", "ত কালি"))} <b>$\\times ${k * k}$</b>`;
  }, on, "k");
};

/* ---------- shear: a triangle is half its box, wherever the apex sits ---------- */
W.shear = (el, w, on) => {
  const b = w.b, h = w.h, k = Math.min(300 / b, 150 / h), X0 = 20, BASE = 176;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 196" role="img" aria-label="A triangle in its box"><g id="sg"></g></svg><input class="wx-range" type="range" min="0" max="${b}" value="${w.x ?? b / 2}" aria-label="Top corner"><div class="wx-read fg-read"></div>`, w.x ?? b / 2, (x) => {
    const ax = X0 + x * k, top = BASE - h * k;
    $("#sg", el).innerHTML = `<rect x="${X0}" y="${top}" width="${b * k}" height="${h * k}" fill="#E2ECFA" stroke="${INK}" stroke-dasharray="5 4"/><path d="M${X0} ${BASE}H${X0 + b * k}L${ax} ${top}Z" fill="${BLUE}"/><path d="M${ax} ${top}V${BASE}" stroke="#fff" stroke-width="2" stroke-dasharray="4 3"/><text x="${X0 + (b * k) / 2}" y="${BASE + 16}" text-anchor="middle" font-size="13" font-weight="900" fill="${INK}">${b}</text><text x="${X0 - 6}" y="${(BASE + top) / 2}" text-anchor="end" font-size="13" font-weight="900" fill="${INK}">${h}</text>`;
    $(".fg-read", el).innerHTML = `$\\frac{1}{2} \\times ${b} \\times ${h} = ${short((b * h) / 2)}$`;
  }, on, "x");
};

/* ---------- sticks: two sides must reach further than the third ---------- */
W.sticks = (el, w, on) => {
  const a = w.a, b = w.b, top = a + b + 3;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 170" role="img" aria-label="Three sticks"><g id="sg"></g></svg><input class="wx-range" type="range" min="1" max="${top}" value="${w.c || Math.abs(a - b) + 1}" aria-label="Third side"><div class="wx-read fg-read"></div>`, w.c || Math.abs(a - b) + 1, (c) => {
    const s = Math.min(300 / Math.max(c, a + b), 18), x0 = 170 - (c * s) / 2, y0 = 150, x1 = x0 + c * s, ok = c < a + b && c > Math.abs(a - b);
    let o = `<path d="M${x0} ${y0}H${x1}" stroke="${ok ? GREEN : RED}" stroke-width="6" stroke-linecap="round"/>`;
    if (ok) { const px = (c * c + a * a - b * b) / (2 * c), py = Math.sqrt(Math.max(0, a * a - px * px)), X = x0 + px * s, Y = y0 - py * s; o += `<path d="M${x0} ${y0}L${X} ${Y}L${x1} ${y0}" fill="rgba(15,138,95,.12)" stroke="${BLUE}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>`; }
    else { o += `<path d="M${x0} ${y0}l${a * s * 0.94} ${-a * s * 0.34}" stroke="${BLUE}" stroke-width="6" stroke-linecap="round"/><path d="M${x1} ${y0}l${-b * s * 0.94} ${-b * s * 0.34}" stroke="${GOLD}" stroke-width="6" stroke-linecap="round"/>`; }
    $("#sg", el).innerHTML = o;
    $(".fg-read", el).innerHTML = `$${a}, ${b}, ${c}$: <b class="${ok ? "yes" : "no"}">${ok ? T(B("makes a triangle", "ত্ৰিভুজ হয়")) : c >= a + b ? T(B("the two sticks cannot reach", "দুডাল লাঠি নাপায়")) : T(B("the long stick sticks out", "দীঘল লাঠি ওলাই থাকে"))}</b>`;
  }, on, "c");
};

/* ---------- kite: a rhombus is half the box around its diagonals ---------- */
W.kite = (el, w, on) => {
  const a = w.d1, b = w.d2, k = Math.min(300 / a, 170 / b), cx = 170, cy = 92, A = (a * k) / 2, Bb = (b * k) / 2;
  el.innerHTML = `<svg class="fgv" viewBox="0 0 340 186" role="img" aria-label="A rhombus in a box"><rect id="bx" x="${cx - A}" y="${cy - Bb}" width="${a * k}" height="${b * k}" fill="#FCEFD2" stroke="${INK}" stroke-dasharray="5 4"/><path d="M${cx - A} ${cy}L${cx} ${cy - Bb}L${cx + A} ${cy}L${cx} ${cy + Bb}Z" fill="${BLUE}"/><path d="M${cx - A} ${cy}H${cx + A}M${cx} ${cy - Bb}V${cy + Bb}" stroke="#fff" stroke-width="2"/></svg><button class="tile gr-go" data-fold>${T(B("Fold the corners in", "চুকবোৰ ভিতৰলৈ ভাঁজ কৰা"))}</button><div class="wx-read fg-read"></div>`;
  let folded = false, locked = false, touched = false;
  const draw = () => { $("#bx", el).setAttribute("fill", folded ? "none" : "#FCEFD2"); $(".fg-read", el).innerHTML = folded ? `<b class="yes">$\\frac{${a} \\times ${b}}{2} = ${short((a * b) / 2)}$</b>` : `$${a} \\times ${b} = ${a * b}$`; };
  el.addEventListener("click", (e) => { if (e.target.closest("[data-fold]") && !locked) { folded = !folded; touched = true; SFX.pair(); draw(); on(); } });
  draw();
  return { value: () => (a * b) / 2, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ folded: folded ? 1 : 0 }), demo() { folded = true; touched = true; draw(); on(); } };
};

/* ---------- rolling wheel: one turn lays the circumference along the ground ---------- */
W.roll = (el, w, on) => {
  const r = w.r, c = (2 * 22 * r) / 7, top = w.max || 4, k = 300 / (c * top + 2 * r), s = Math.max(k * r, 10), X0 = 12 + s, BASE = 122;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 150" role="img" aria-label="A wheel rolling"><g id="sg"></g></svg><input class="wx-range" type="range" min="0" max="${top}" value="0" aria-label="Turns"><div class="wx-read fg-read"></div>`, 0, (n) => {
    const d = n * c, x = X0 + d * k, ang = n * 360; let marks = "";
    for (let i = 1; i <= n; i++) marks += `<path d="M${X0 + i * c * k} ${BASE - 7}V${BASE + 7}" stroke="${RED}" stroke-width="3"/>`;
    $("#sg", el).innerHTML = `<path d="M0 ${BASE}H340" stroke="${INK}" stroke-width="2"/><path d="M${X0} ${BASE}H${x}" stroke="${GREEN}" stroke-width="6"/>${marks}<g transform="translate(${x} ${BASE - s}) rotate(${ang})"><circle r="${s}" fill="#fff" stroke="${BLUE}" stroke-width="5"/><path d="M0 0V${s}" stroke="${RED}" stroke-width="3"/><circle r="4" fill="${INK}"/></g>`;
    $(".fg-read", el).innerHTML = `$${n} \\times 2 \\times \\frac{22}{7} \\times ${r} = ${short(d)}$`;
  }, on, "turns");
};

/* ---------- sectors: cut a circle finely and it rearranges into πr × r ---------- */
W.sectors = (el, w, on) => {
  const R = 74, base = 150;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 170" role="img" aria-label="A circle cut into slices"><g id="sg"></g></svg><input class="wx-range" type="range" min="4" max="40" step="2" value="${w.n || 6}" aria-label="Slices"><div class="wx-read fg-read"></div>`, w.n || 6, (n) => {
    const a = (2 * Math.PI) / n, step = (Math.PI * R) / n, chord = 2 * R * Math.sin(a / 2), h = R * Math.cos(a / 2), x0 = 170 - (Math.PI * R) / 2, top = base - R;
    let o = "";
    for (let i = 0; i < n; i++) {   // odd slices point up and even slices down, so they lock together
      const xc = x0 + (i + 0.5) * step, up = i % 2 === 0, tip = up ? top : base, edge = up ? top + h : base - h;
      o += `<path d="M${xc} ${tip}L${xc - chord / 2} ${edge}A${R} ${R} 0 0 ${up ? 0 : 1} ${xc + chord / 2} ${edge}Z" fill="${up ? BLUE : GOLD}" stroke="#fff" stroke-width=".8"/>`;
    }
    $("#sg", el).innerHTML = o;
    $(".fg-read", el).innerHTML = `${T(B(`${n} slices`, `${n}টা টুকুৰা`))}: ${n >= 24 ? `<b class="yes">$\\pi r \\times r = \\pi r^2$</b>` : T(B("cut finer", "আৰু সৰু কৰা"))}`;
  }, on, "n");
};

/* ---------- exterior angle: the outside angle equals the two far inside angles ---------- */
W.exterior = (el, w, on) => {
  let a = w.a ?? 50, b = w.b ?? 60, touched = false, locked = false;
  el.innerHTML = `<svg class="fgv" viewBox="0 0 340 170" role="img" aria-label="A triangle with one side extended"><g id="sg"></g></svg><label class="sl"><span>A <b id="la"></b></span><input class="wx-range" id="ia" type="range" min="10" max="120" step="5" value="${a}"></label><label class="sl"><span>B <b id="lb"></b></span><input class="wx-range" id="ib" type="range" min="10" max="120" step="5" value="${b}"></label><div class="wx-read fg-read"></div>`;
  const RAD = Math.PI / 180;
  const draw = () => {
    const c = 180 - a - b, L = 190, x0 = 30, y0 = 146, ok = c > 0, Bx = x0 + L, h = ok ? (L * Math.sin(a * RAD) * Math.sin(b * RAD)) / Math.sin((a + b) * RAD) : 0, Ax = ok ? x0 + h / Math.tan(a * RAD) : x0, top = Math.max(y0 - h, 8), kind = !ok ? null : Math.max(a, b, c) > 90 ? B("Obtuse", "স্থূলকোণী") : Math.max(a, b, c) === 90 ? B("Right", "সমকোণী") : B("Acute", "সূক্ষ্মকোণী"), sides = !ok ? null : a === b && b === c ? B("equilateral", "সমবাহু") : a === b || b === c || a === c ? B("isosceles", "সমদ্বিবাহু") : B("scalene", "বিষমবাহু");
    $("#sg", el).innerHTML = ok ? `<path d="M${x0} ${y0}L${Bx} ${y0}L${Ax} ${top}Z" fill="#E2ECFA" stroke="${BLUE}" stroke-width="3"/><path d="M${Bx} ${y0}H334" stroke="${GOLD}" stroke-width="4"/><text x="${x0 + 26}" y="${y0 - 6}" font-size="13" font-weight="900" fill="${BLUE}">${a}°</text><text x="${Bx - 44}" y="${y0 - 6}" font-size="13" font-weight="900" fill="${BLUE}">${b}°</text><text x="${Ax - 12}" y="${top + 26}" font-size="13" font-weight="900" fill="${INK}">${c}°</text><text x="${Bx + 26}" y="${y0 - 8}" font-size="15" font-weight="900" fill="${GOLD}">${a + b}°</text>` : `<text x="170" y="90" text-anchor="middle" font-size="15" font-weight="900" fill="${RED}">${a + b}° &gt; 180°</text>`;
    $("#la", el).textContent = `${a}°`; $("#lb", el).textContent = `${b}°`;
    $(".fg-read", el).innerHTML = ok ? `$${a} + ${b} = ${a + b}^\\circ$ ${T(B("outside", "বাহিৰত"))} <b class="yes">${T(kind)}, ${T(sides)}</b>` : `<b class="no">${T(B("No triangle", "ত্ৰিভুজ নহয়"))}</b>`;
  };
  const change = () => { if (locked) return; a = +$("#ia", el).value; b = +$("#ib", el).value; touched = true; SFX.tap(); draw(); on(); };
  $("#ia", el).addEventListener("input", change); $("#ib", el).addEventListener("input", change); draw();
  const set = (x, y) => { a = x; b = y; $("#ia", el).value = a; $("#ib", el).value = b; touched = true; draw(); on(); };
  return { value: () => 180 - a - b, touched: () => touched, freeze() { locked = true; $("#ia", el).disabled = $("#ib", el).disabled = true; }, show(v) { const sum = 180 - v, x = Math.round(sum / 10) * 5; set(x, sum - x); }, state: () => ({ a, b }), demo(g) { set(g.a ?? a, g.b ?? b); } };
};

/* ---------- tangent: it meets the radius at a right angle, so Pythagoras applies ---------- */
W.tangent = (el, w, on) => {
  const r = w.r, top = w.max || 24;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 190" role="img" aria-label="A circle with a tangent"><g id="sg"></g></svg><input class="wx-range" type="range" min="1" max="${top}" value="${w.pq ?? 3}" aria-label="Tangent length"><div class="wx-read fg-read"></div>`, w.pq ?? 3, (pq) => {
    const k = Math.min(70 / r, 240 / top), R = r * k, Ox = 84, Oy = 100, Px = Ox, Py = Oy - R, Qx = Px + pq * k, oq = Math.sqrt(r * r + pq * pq), whole = Number.isInteger(+oq.toFixed(6));
    $("#sg", el).innerHTML = `<circle cx="${Ox}" cy="${Oy}" r="${R}" fill="#E2ECFA" stroke="${BLUE}" stroke-width="3"/><path d="M4 ${Py}H336" stroke="${GOLD}" stroke-width="3"/><path d="M${Ox} ${Oy}V${Py}" stroke="${INK}" stroke-width="3"/><path d="M${Ox} ${Oy}L${Qx} ${Py}" stroke="${RED}" stroke-width="3"/><path d="M${Px + 12} ${Py}v12h-12" fill="none" stroke="${INK}" stroke-width="1.5"/><circle cx="${Qx}" cy="${Py}" r="6" fill="${RED}"/><text x="${Ox - 10}" y="${(Oy + Py) / 2 + 4}" text-anchor="end" font-size="13" font-weight="900" fill="${INK}">${r}</text><text x="${(Px + Qx) / 2}" y="${Py - 7}" text-anchor="middle" font-size="13" font-weight="900" fill="${GOLD}">${pq}</text>`;
    $(".fg-read", el).innerHTML = `$${r}^2 + ${pq}^2 = ${r * r + pq * pq}$ <b class="${whole ? "yes" : ""}">$OQ = ${whole ? +oq.toFixed(6) : `\\sqrt{${r * r + pq * pq}}`}$</b>`;
  }, on, "pq");
};

/* ---------- fence: one perimeter, many rectangles; the square holds the most ---------- */
W.fence = (el, w, on) => {
  const half = w.p / 2, lo = Math.ceil(w.p / 4), hi = half - 1;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 170" role="img" aria-label="A rectangle with a fixed perimeter"><g id="sg"></g></svg><input class="wx-range" type="range" min="${lo}" max="${hi}" value="${w.l ?? lo}" aria-label="Length"><div class="wx-read fg-read"></div>`, w.l ?? lo, (l) => {
    const b = half - l, k = Math.min(300 / hi, 130 / lo), x0 = 170 - (l * k) / 2, y0 = 80 - (b * k) / 2, d2 = l * l + b * b, d = Math.sqrt(d2), whole = Number.isInteger(+d.toFixed(6));
    $("#sg", el).innerHTML = `<rect x="${x0}" y="${y0}" width="${l * k}" height="${b * k}" fill="#E2ECFA" stroke="${BLUE}" stroke-width="3"/><path d="M${x0} ${y0 + b * k}L${x0 + l * k} ${y0}" stroke="${GOLD}" stroke-width="2" stroke-dasharray="6 4"/><text x="170" y="${y0 + b * k + 18}" text-anchor="middle" font-size="14" font-weight="900" fill="${INK}">${l}</text><text x="${x0 - 8}" y="${y0 + (b * k) / 2 + 5}" text-anchor="end" font-size="14" font-weight="900" fill="${INK}">${b}</text>`;
    $(".fg-read", el).innerHTML = `$${l} \\times ${b} = ${l * b}$ <b class="yes">${T(B("diagonal", "কৰ্ণ"))} $${whole ? +d.toFixed(6) : `\\sqrt{${d2}}`}$</b>`;
  }, on, "l");
};

/* ---------- stack: volume is base area × the number of layers ---------- */
W.stack = (el, w, on) => {
  const l = w.l, b = w.b, top = w.max || 6;
  return slider(el, `<svg class="fgv" viewBox="0 0 340 210" role="img" aria-label="Stacked cubes"><g id="sg"></g></svg><input class="wx-range" type="range" min="1" max="${top}" value="${w.h || 1}" aria-label="Layers"><div class="wx-read fg-read"></div>`, w.h || 1, (h) => {
    const s = Math.min(216 / (l + b + top), 26); $("#sg", el).innerHTML = `<g transform="translate(0 ${30 + top * s * 0.2})">${blocks(l, b, h, s)}</g>`;
    $(".fg-read", el).innerHTML = `$${l} \\times ${b} \\times ${h} = ${l * b * h}$`;
  }, on, "h");
};

/* ---------- net: unfold a cube and its surface is six squares ---------- */
W.net = (el, w, on) => {
  const a = w.a; let open = false, locked = false, touched = false;
  el.innerHTML = `<svg class="fgv" viewBox="0 0 340 200" role="img" aria-label="A cube"><g id="sg"></g></svg><button class="tile gr-go" data-unfold>${T(B("Unfold it", "খুলি দিয়া"))}</button><div class="wx-read fg-read"></div>`;
  const draw = () => {
    if (open) { const c = 48, pos = [[1, 0], [0, 1], [1, 1], [2, 1], [3, 1], [1, 2]], x0 = 170 - 2 * c, y0 = 26; $("#sg", el).innerHTML = pos.map(([x, y], k) => `<rect x="${x0 + x * c}" y="${y0 + y * c}" width="${c - 2}" height="${c - 2}" fill="${k % 2 ? BLUE : "#7FA9E6"}"/><text x="${x0 + x * c + c / 2}" y="${y0 + y * c + c / 2 + 5}" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">${a * a}</text>`).join(""); }
    else $("#sg", el).innerHTML = `<g transform="translate(0 -14)">${isoCube(-0.5, -0.5, 0, 84, "#7FA9E6", BLUE, "#174A97")}</g>`;
    $(".fg-read", el).innerHTML = open ? `<b class="yes">$6 \\times ${a}^2 = ${6 * a * a}$</b>` : `${T(B("Side", "বাহু"))} $${a}$`;
  };
  el.addEventListener("click", (e) => { if (e.target.closest("[data-unfold]") && !locked) { open = !open; touched = true; SFX.pair(); draw(); on(); } });
  draw();
  return { value: () => 6 * a * a, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ open: open ? 1 : 0 }), demo() { open = true; touched = true; draw(); on(); } };
};

/* ---------- pour: three cones fill the cylinder of the same base and height ---------- */
W.pour = (el, w, on) => {
  let n = 0, locked = false, touched = false;
  el.innerHTML = `<svg class="fgv" viewBox="0 0 340 190" role="img" aria-label="A cone and a cylinder"><path d="M40 170L80 40L120 170Z" fill="${GOLD}"/><ellipse cx="80" cy="170" rx="40" ry="9" fill="${GOLD}"/><rect id="lv" x="192" width="96" fill="${BLUE}" opacity=".8"/><path d="M192 40V170M288 40V170" stroke="${INK}" stroke-width="3"/><ellipse cx="240" cy="40" rx="48" ry="9" fill="none" stroke="${INK}" stroke-width="3"/><ellipse cx="240" cy="170" rx="48" ry="9" fill="none" stroke="${INK}" stroke-width="3"/></svg><button class="tile gr-go" data-pour>${T(B("Pour one cone", "এটা শংকু ঢালা"))}</button><div class="wx-read fg-read"></div>`;
  const draw = () => { const h = (n / 3) * 130; $("#lv", el).setAttribute("y", 170 - h); $("#lv", el).setAttribute("height", h); $(".fg-read", el).innerHTML = n === 3 ? `<b class="yes">$3 \\times \\text{cone} = \\pi r^2 h$</b>` : `$${n}/3$`; $("[data-pour]", el).disabled = n === 3; };
  el.addEventListener("click", (e) => { if (e.target.closest("[data-pour]") && !locked && n < 3) { n++; touched = true; SFX.pair(); draw(); on(); } });
  draw();
  return { value: () => n, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ n }), demo() { n = 3; touched = true; draw(); on(); } };
};
})();
