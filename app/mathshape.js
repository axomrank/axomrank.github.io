/* =========================================================
   AxomRank maths stage, part six: sequences and triangles.
   stairs: AP and GP, triangle: trig ratios, quarter: the value table, tower: height and distance.
   Same contract as app/mathstage.js. The reasons are in docs/MATHEMATICS-VISUALS.md.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#16305C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F";
const short = (v) => +v.toFixed(3);
const gcd = (a, b) => (b ? gcd(b, a % b) : a);
const RAD = Math.PI / 180;

/* ---------- stairs: an AP counts n − 1 steps; two copies make a rectangle; a GP multiplies ---------- */
W.stairs = (el, w, on) => {
  const gp = w.mode === "gp", a = w.a, d = w.d ?? 0, r = w.r ?? 2, top = w.max || 12;
  let n = w.n || 3, paired = false, touched = false, locked = false;
  const term = (k) => (gp ? a * r ** (k - 1) : a + (k - 1) * d);
  el.innerHTML = `<svg class="stv" viewBox="0 0 340 170" role="img" aria-label="Bars growing"><g id="sb"></g></svg><label class="sl"><span>${T(B("Term", "পদ"))} <b id="sn"></b></span><input class="wx-range" type="range" min="1" max="${top}" value="${n}"></label>${w.sum ? `<button class="tile gr-go" data-flip>${T(B("Add a flipped copy", "ওলোটা প্ৰতিলিপি যোগ কৰা"))}</button>` : ""}<div class="wx-read st-read"></div>`;
  const input = $("input", el), read = $(".st-read", el), BASE = 158;
  const draw = () => {
    const last = term(n), peak = paired ? a + last : Math.max(term(top), 1), k = 146 / peak, cw = 330 / (paired ? n : top), bw = Math.min(cw - 2, 44);
    let out = "";
    for (let i = 1; i <= n; i++) {
      const v = term(i), x = 5 + (i - 1) * cw, h = v * k;
      out += `<rect x="${x}" y="${BASE - (gp ? h : a * k)}" width="${bw}" height="${gp ? h : a * k}" fill="${BLUE}"/>`;
      if (!gp) out += `<rect x="${x}" y="${BASE - h}" width="${bw}" height="${h - a * k}" fill="${GOLD}"/>`;
      if (paired) { const mirror = term(n + 1 - i); out += `<rect x="${x}" y="${BASE - h - mirror * k}" width="${bw}" height="${mirror * k}" fill="#A9C4E8"/>`; }
      if (bw > 15 && n <= 14) out += `<text x="${x + bw / 2}" y="${BASE - h + (h > 18 ? 14 : -3)}" text-anchor="middle" font-size="11" font-weight="900" fill="${h > 18 ? "#fff" : INK}">${v}</text>`;
    }
    $("#sb", el).innerHTML = `${out}<path d="M0 ${BASE}H340" stroke="${INK}" stroke-width="2"/>`;
    $("#sn", el).textContent = n;
    const sum = (n * (a + last)) / 2;
    read.innerHTML = paired ? `<b class="yes">$\\frac{${n} \\times (${a} + ${last})}{2} = ${sum}$</b>` : gp ? `$${a} \\times ${r}^{${n - 1}} = ${last}$` : `$${a} + ${n - 1} \\times ${d} = ${last}$`;
  };
  input.addEventListener("input", () => { if (locked) return; n = +input.value; touched = true; SFX.tap(); draw(); on(); });
  el.addEventListener("click", (e) => { if (e.target.closest("[data-flip]") && !locked) { paired = !paired; touched = true; SFX.pair(); draw(); on(); } });
  draw();
  return { value: () => n, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show(v) { n = v; input.value = v; touched = true; draw(); on(); }, state: () => ({ n, paired: paired ? 1 : 0 }),
    demo(g) { if (g.n) { n = g.n; input.value = n; } if (g.paired) paired = true; touched = true; draw(); on(); } };
};

/* ---------- triangle: resize freely and the ratios stay; tap a side to name it ---------- */
W.triangle = (el, w, on) => {
  const [o, ad, h] = w.triple || [3, 4, 5], pick = !!w.pick; let k = w.k || 1, sel = null, touched = false, locked = false;
  const topAngle = w.from === "top", MAX = w.max || 4;
  el.innerHTML = `<svg class="trv" viewBox="0 0 340 200" role="img" aria-label="A right triangle"><g id="tg"></g></svg>${pick ? "" : `<input class="wx-range" type="range" min="1" max="${MAX}" value="${k}" aria-label="Size"><div class="wx-read tr-read"></div>`}`;
  const input = $("input", el), read = $(".tr-read", el);
  const draw = () => {
    const s = (pick ? 34 : 34 * (0.55 + 0.45 * (k / MAX) * 1.4)) * (5 / h) * (h > 6 ? 1 : 1), bw = ad * s, bh = o * s, Ax = 40, Ay = 182, Bx = Ax + bw, Cy = Ay - bh;
    // in question mode every side is the same ink, so colour cannot give the answer away; the wide invisible stroke is the finger target
    const mark = (id, d, tx, ty, label, c) => `<path d="${d}" stroke="${sel === id ? GOLD : pick ? INK : c}" stroke-width="${pick ? 7 : 4}" stroke-linecap="round" fill="none"/>${pick ? `<path d="${d}" stroke="transparent" stroke-width="30" fill="none" data-side="${id}" style="cursor:pointer"/>` : `<text x="${tx}" y="${ty}" text-anchor="middle" font-size="15" font-weight="900" fill="${c}">${label}</text>`}`;
    const theta = topAngle ? `<path d="M${Bx} ${Cy + 28}A28 28 0 0 1 ${Bx - 22} ${Cy + 18}" fill="none" stroke="${RED}" stroke-width="3"/><text x="${Bx - 14}" y="${Cy + 48}" font-size="15" font-weight="900" fill="${RED}">θ</text>` : `<path d="M${Ax + 34} ${Ay}A34 34 0 0 0 ${Ax + 34 * (ad / h)} ${Ay - 34 * (o / h)}" fill="none" stroke="${RED}" stroke-width="3"/><text x="${Ax + 42}" y="${Ay - 8}" font-size="15" font-weight="900" fill="${RED}">θ</text>`;
    $("#tg", el).innerHTML = `<path d="M${Ax} ${Ay}L${Bx} ${Ay}L${Bx} ${Cy}Z" fill="#E2ECFA"/><path d="M${Bx - 14} ${Ay}v-14h14" fill="none" stroke="${INK}" stroke-width="1.5"/>${mark("b", `M${Ax} ${Ay}L${Bx} ${Ay}`, (Ax + Bx) / 2, Ay + 16, ad * k, topAngle ? BLUE : GREEN)}${mark("v", `M${Bx} ${Ay}L${Bx} ${Cy}`, Bx + 18, (Ay + Cy) / 2, o * k, topAngle ? GREEN : BLUE)}${mark("h", `M${Ax} ${Ay}L${Bx} ${Cy}`, (Ax + Bx) / 2 - 12, (Ay + Cy) / 2 - 8, h * k, INK)}${theta}`;
    if (read) { const g = (a, b) => { const c = gcd(a, b); return `\\frac{${a / c}}{${b / c}}`; }; read.innerHTML = `$\\sin\\theta = \\frac{${o * k}}{${h * k}} = ${g(o, h)}$<br>$\\cos\\theta = \\frac{${ad * k}}{${h * k}} = ${g(ad, h)}$`; }
  };
  if (input) input.addEventListener("input", () => { if (locked) return; k = +input.value; touched = true; SFX.tap(); draw(); on(); });
  el.addEventListener("click", (e) => { const b = e.target.closest("[data-side]"); if (b && !locked) { sel = b.dataset.side; touched = true; SFX.tap(); draw(); on(); } });
  draw();
  const code = { v: 1, b: 2, h: 3 };
  return { value: () => (pick ? code[sel] || 0 : k), touched: () => touched, freeze() { locked = true; }, show(v) { if (pick) sel = Object.keys(code).find((c) => code[c] === v) || null; else { k = v; input.value = v; } touched = true; draw(); on(); },
    state: () => ({ k }), demo(g) { k = g.k; input.value = k; touched = true; draw(); on(); } };
};

/* ---------- quarter circle: the whole value table is one point moving on a radius of 1 ---------- */
W.quarter = (el, w, on) => {
  const NAMES = { 0: [["0"], ["1"], "0"], 30: ["\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "\\frac{1}{\\sqrt{3}}"], 45: ["\\frac{1}{\\sqrt{2}}", "\\frac{1}{\\sqrt{2}}", "1"], 60: ["\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}", "\\sqrt{3}"], 90: ["1", "0", "\\text{—}"] };
  let deg = w.deg ?? 0, touched = false, locked = false;
  el.innerHTML = `<svg class="qv" viewBox="-14 -196 214 214" role="img" aria-label="A quarter circle"><path d="M180 0A180 180 0 0 1 0 -180" fill="none" stroke="#CFDDE8" stroke-width="3"/><path d="M0 0H190M0 0V-190" stroke="${INK}" stroke-width="2"/><g id="qg"></g></svg><input class="wx-range" type="range" min="0" max="90" step="${w.step || 15}" value="${deg}" aria-label="Angle"><div class="wx-read q-read"></div>`;
  const input = $("input", el), read = $(".q-read", el), R = 180;
  const draw = () => {
    const c = Math.cos(deg * RAD), s = Math.sin(deg * RAD), x = R * c, y = -R * s;
    $("#qg", el).innerHTML = `<path d="M0 0L${x} ${y}" stroke="${INK}" stroke-width="3"/><path d="M${x} 0V${y}" stroke="${BLUE}" stroke-width="7"/><path d="M0 0H${x}" stroke="${GREEN}" stroke-width="7"/><circle cx="${x}" cy="${y}" r="8" fill="${RED}"/><text x="26" y="-8" font-size="14" font-weight="900" fill="${RED}">${deg}°</text>`;
    const n = NAMES[deg];
    read.innerHTML = n ? `<span class="s">$\\sin ${deg}^\\circ = ${n[0]}$</span> <span class="c">$\\cos ${deg}^\\circ = ${n[1]}$</span>` : `<span class="s">$\\sin = ${short(s)}$</span> <span class="c">$\\cos = ${short(c)}$</span>`;
  };
  input.addEventListener("input", () => { if (locked) return; deg = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const set = (v) => { deg = v; input.value = v; touched = true; draw(); on(); };
  return { value: () => deg, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: set, state: () => ({ deg }), demo(g) { set(g.deg); } };
};

/* ---------- tower: raise it until the sight line reaches the top at the given angle ---------- */
W.tower = (el, w, on) => {
  const d = w.d, ang = w.ang, surd = !!w.surd, top = w.max || 40, unit = surd ? Math.sqrt(3) : 1, want = d * Math.tan(ang * RAD);
  let k = w.k ?? 5, touched = false, locked = false;
  el.innerHTML = `<svg class="twv" viewBox="0 0 340 200" role="img" aria-label="A tower and an observer"><g id="tw"></g></svg><input class="wx-range" type="range" min="1" max="${top}" value="${k}" aria-label="Height"><div class="wx-read tw-read"></div>`;
  const input = $("input", el), read = $(".tw-read", el);
  const draw = () => {
    const h = k * unit, scale = Math.min(250 / d, 170 / Math.max(want, h)), X0 = 40, BASE = 186, Tx = X0 + d * scale, Hy = BASE - h * scale, ray = BASE - want * scale, hit = Math.abs(h - want) < 1e-6;
    $("#tw", el).innerHTML = `<path d="M0 ${BASE}H340" stroke="${INK}" stroke-width="2"/><rect x="${Tx}" y="${Hy}" width="22" height="${BASE - Hy}" fill="${BLUE}"/><path d="M${X0} ${BASE}L${Tx} ${ray}" stroke="${hit ? GREEN : RED}" stroke-width="3" stroke-dasharray="${hit ? "0" : "6 4"}"/><circle cx="${X0}" cy="${BASE - 6}" r="6" fill="${INK}"/><path d="M${X0 + 30} ${BASE}A30 30 0 0 0 ${X0 + 30 * Math.cos(ang * RAD)} ${BASE - 30 * Math.sin(ang * RAD)}" fill="none" stroke="${RED}" stroke-width="2.5"/><text x="${X0 + 36}" y="${BASE - 8}" font-size="13" font-weight="900" fill="${RED}">${ang}°</text><text x="${(X0 + Tx) / 2}" y="${BASE + 12}" text-anchor="middle" font-size="12" font-weight="900" fill="${INK}">${w.dText || d}</text><text x="${Tx + 28}" y="${(BASE + Hy) / 2}" font-size="13" font-weight="900" fill="${BLUE}">${surd ? `${k}√3` : k}</text>`;
    read.innerHTML = `<b class="${hit ? "yes" : "no"}">$\\tan ${ang}^\\circ = \\frac{${surd ? `${k}\\sqrt{3}` : k}}{${w.dText ? w.dTex : d}}$</b> ${hit ? "✓" : ""}`;
  };
  input.addEventListener("input", () => { if (locked) return; k = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const exact = Math.round(want / unit), set = (v) => { k = v; input.value = v; touched = true; draw(); on(); };
  return { value: () => k, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: set, state: () => ({ hit: Math.abs(k * unit - want) < 1e-6 ? 1 : 0 }), demo() { set(exact); } };
};
})();
