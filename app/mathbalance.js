/* =========================================================
   AxomRank maths stage, part two: scenes about balance and scale.
   ray: proportion, level: average, seesaw: weighted average, chain: linked ratios.
   Same contract as app/mathstage.js. The reasons are in docs/MATHEMATICS-VISUALS.md.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#16305C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F", GRID = "#CFDDE8", FAINT = "#7E93AE";
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const drag = (svg, move) => {
  let on = false;
  svg.addEventListener("pointerdown", (e) => { svg.setPointerCapture(e.pointerId); on = true; move(e); SFX.tap(); });
  svg.addEventListener("pointermove", (e) => { if (on) move(e); });
  ["pointerup", "pointercancel"].forEach((n) => svg.addEventListener(n, () => { on = false; }));
};
const point = (svg, e, width, height) => { const r = svg.getBoundingClientRect(); return [((e.clientX - r.left) / r.width) * width, ((e.clientY - r.top) / r.height) * height]; };

/* ---------- ratio ray: every equal ratio lies on one straight line through 0 ---------- */
W.ray = (el, w, on) => {
  const a = w.a, b = w.b, N = w.n || 12, unit = w.unit || 1, S = 22, L = 26, BOT = 8 + N * S, VW = L + N * S + 8, VH = BOT + 24;
  const px = (x) => L + x * S, py = (y) => BOT - y * S;
  let x = w.x ?? a, y = w.y ?? b, touched = false, locked = false;
  let grid = "";
  for (let k = 0; k <= N; k++) {
    grid += `<path d="M${px(k)} ${py(0)}V${py(N)}M${px(0)} ${py(k)}H${px(N)}" stroke="${GRID}" stroke-width="1"/>`;
    if (k % (N > 12 ? 4 : 2) === 0) grid += `<text x="${px(k)}" y="${BOT + 16}" text-anchor="middle" font-size="11" font-weight="800" fill="${BLUE}">${k * unit}</text><text x="${L - 6}" y="${py(k) + 4}" text-anchor="end" font-size="11" font-weight="800" fill="${GOLD}">${k * unit}</text>`;
  }
  const reach = Math.min(N / a, N / b);
  el.innerHTML = `<svg class="rayv" viewBox="0 0 ${VW} ${VH}" role="img" aria-label="Ratio grid">${grid}<path d="M${px(0)} ${py(0)}L${px(a * reach)} ${py(b * reach)}" stroke="${GREEN}" stroke-width="3.5" stroke-linecap="round"/>
    <path id="dr" fill="none" stroke="${INK}" stroke-width="1.5" stroke-dasharray="4 3"/><circle id="dt" r="10" stroke="#fff" stroke-width="3"/></svg><div class="wx-read ray-read"></div>`;
  const svg = $("svg", el), read = $(".ray-read", el), online = () => x * b === y * a && x > 0;
  const draw = () => {
    const ok = online();
    $("#dt", el).setAttribute("cx", px(x)); $("#dt", el).setAttribute("cy", py(y)); $("#dt", el).setAttribute("fill", ok ? GREEN : RED);
    $("#dr", el).setAttribute("d", `M${px(x)} ${py(0)}V${py(y)}H${px(0)}`);
    read.innerHTML = `<b class="${ok ? "yes" : "no"}">$${x * unit} : ${y * unit}$</b> ${ok ? T(B(`equals ${a * unit} : ${b * unit}`, `${a * unit} : ${b * unit}ৰ সমান`)) : T(B("is off the line", "ৰেখাত নাই"))}`;
  };
  drag(svg, (e) => {
    if (locked) return;
    const [mx, my] = point(svg, e, VW, VH), nx = w.fixX ? x : clamp(Math.round((mx - L) / S), 0, N), ny = clamp(Math.round((BOT - my) / S), 0, N);
    if (nx !== x || ny !== y) { x = nx; y = ny; touched = true; draw(); on(); }
  });
  draw();
  return { value: () => y * unit, touched: () => touched, freeze() { locked = true; }, show(v) { y = v / unit; touched = true; draw(); on(); },
    state: () => ({ x, y, on: online() ? 1 : 0 }), demo(g) { x = g.x ?? x; y = g.y ?? (x * b) / a; touched = true; draw(); on(); } };
};

/* ---------- level line: the average is where the surplus above equals the gap below ---------- */
W.level = (el, w, on) => {
  const vals = w.vals, n = vals.length, top = Math.max(...vals) * 1.12, VW = 340, VH = 190, BASE = 170, gap = 6, bw = (VW - 16 - gap * (n - 1)) / n, y = (v) => BASE - (v / top) * (BASE - 12);
  const sum = vals.reduce((p, v) => p + v, 0), mean = sum / n, step = w.step || 1;
  let lv = w.start ?? Math.round(Math.max(...vals) / step) * step, touched = false, locked = false;
  el.innerHTML = `<svg class="levelv" viewBox="0 0 ${VW} ${VH}" role="img" aria-label="Bars and a level line"><g id="bars"></g><path d="M0 ${BASE}H${VW}" stroke="${INK}" stroke-width="2"/><g id="ln"><path d="M0 0H${VW}" stroke="${INK}" stroke-width="3"/><circle cx="${VW - 12}" r="11" fill="${INK}"/><text id="lt" x="${VW - 12}" y="4" text-anchor="middle" font-size="11" font-weight="900" fill="#fff"></text></g></svg><div class="lv-sums"></div>`;
  const svg = $("svg", el), bars = $("#bars", el), sums = $(".lv-sums", el);
  const draw = () => {
    let up = 0, down = 0, out = "";
    vals.forEach((v, k) => {
      const X = 8 + k * (bw + gap), hi = Math.max(v, lv), lo = Math.min(v, lv);
      out += `<rect x="${X}" y="${y(lo)}" width="${bw}" height="${BASE - y(lo)}" fill="#A9C4E8"/>`;
      if (v > lv) { up += v - lv; out += `<rect x="${X}" y="${y(hi)}" width="${bw}" height="${y(lo) - y(hi)}" fill="${BLUE}"/><text x="${X + bw / 2}" y="${y(hi) - 3}" text-anchor="middle" font-size="12" font-weight="900" fill="${BLUE}">+${+(v - lv).toFixed(2)}</text>`; }
      if (v < lv) { down += lv - v; out += `<rect x="${X}" y="${y(hi)}" width="${bw}" height="${y(lo) - y(hi)}" fill="#FBE4E6" stroke="${RED}" stroke-dasharray="3 3"/><text x="${X + bw / 2}" y="${y(lo) - 3}" text-anchor="middle" font-size="12" font-weight="900" fill="${RED}">−${+(lv - v).toFixed(2)}</text>`; }
      out += `<text x="${X + bw / 2}" y="${BASE + 14}" text-anchor="middle" font-size="12" font-weight="800" fill="${INK}">${v}</text>`;
    });
    bars.innerHTML = out;
    $("#ln", el).setAttribute("transform", `translate(0 ${y(lv)})`); $("#lt", el).textContent = lv;
    const eq = Math.abs(up - down) < 1e-9;
    sums.innerHTML = `<span class="pos">${T(B("Above", "ওপৰত"))} <b>${+up.toFixed(2)}</b></span><span class="${eq ? "ok" : "ne"}">${eq ? "=" : "≠"}</span><span class="neg">${T(B("Gap", "খালী"))} <b>${+down.toFixed(2)}</b></span>`;
  };
  drag(svg, (e) => {
    if (locked) return;
    const my = point(svg, e, VW, VH)[1], v = clamp(Math.round((((BASE - my) / (BASE - 12)) * top) / step) * step, 0, top);
    if (v !== lv) { lv = +v.toFixed(4); touched = true; draw(); on(); }
  });
  draw();
  return { value: () => lv, touched: () => touched, freeze() { locked = true; }, show(v) { lv = v; touched = true; draw(); on(); },
    state: () => ({ level: lv, balanced: Math.abs(lv - mean) < 1e-9 ? 1 : 0 }), demo() { lv = mean; touched = true; draw(); on(); } };
};

/* ---------- see-saw: a group average is a balance point, nearer the bigger group ---------- */
W.seesaw = (el, w, on) => {
  const a = w.a, b = w.b, n1 = w.n1, n2 = w.n2, step = w.step || 1, L = 34, R = 306, VW = 340, VH = 160, PIV = 96, x = (v) => L + ((v - a) / (b - a)) * (R - L);
  const truth = (a * n1 + b * n2) / (n1 + n2);
  let p = w.start ?? (a + b) / 2, touched = false, locked = false;
  // dots show the size ratio; the true count is written beside them, so large groups still fit
  const hcf = (x, y) => (y ? hcf(y, x % y) : x), g = hcf(n1, n2);
  const stack = (cx, n, c) => `${Array.from({ length: Math.min(n / g, 12) }, (_, k) => `<circle cx="${cx + ((k % 4) - 1.5) * 15}" cy="${-14 - Math.floor(k / 4) * 15}" r="7" fill="${c}"/>`).join("")}<text x="${cx}" y="22" text-anchor="middle" font-size="13" font-weight="900" fill="${c}">×${n}</text>`;
  el.innerHTML = `<svg class="sawv" viewBox="0 0 ${VW} ${VH}" role="img" aria-label="See-saw"><g id="bm"><rect x="${L - 16}" y="-4" width="${R - L + 32}" height="8" rx="4" fill="${INK}"/>${stack(L, n1, BLUE)}${stack(R, n2, GOLD)}</g>
    <path id="pv" fill="${RED}"/><path d="M0 ${PIV + 42}H${VW}" stroke="${FAINT}" stroke-width="2"/><text x="${L}" y="${PIV + 60 - 2}" text-anchor="middle" font-size="13" font-weight="900" fill="${BLUE}">${a}</text><text x="${R}" y="${PIV + 58}" text-anchor="middle" font-size="13" font-weight="900" fill="${GOLD}">${b}</text><text id="pt" y="${PIV + 58}" text-anchor="middle" font-size="15" font-weight="900" fill="${RED}"></text></svg><div class="wx-read saw-read"></div>`;
  const svg = $("svg", el), read = $(".saw-read", el), left = () => n1 * (p - a), right = () => n2 * (b - p);
  const draw = () => {
    const X = x(p), diff = right() - left(), tilt = clamp((diff / (n1 + n2) / (b - a)) * 40, -13, 13);
    $("#bm", el).setAttribute("transform", `rotate(${tilt} ${X} ${PIV}) translate(0 ${PIV})`);
    $("#pv", el).setAttribute("d", `M${X} ${PIV + 4}L${X - 18} ${PIV + 42}H${X + 18}Z`);
    const t = $("#pt", el); t.setAttribute("x", clamp(X, 60, 280)); t.textContent = p;
    const eq = Math.abs(diff) < 1e-9;
    read.innerHTML = `$${n1} \\times ${+(p - a).toFixed(2)} = ${+left().toFixed(2)}$ <b class="${eq ? "yes" : "no"}">${eq ? "=" : "≠"}</b> $${n2} \\times ${+(b - p).toFixed(2)} = ${+right().toFixed(2)}$`;
  };
  drag(svg, (e) => {
    if (locked) return;
    const mx = point(svg, e, VW, VH)[0], v = clamp(Math.round((a + ((mx - L) / (R - L)) * (b - a)) / step) * step, a, b);
    if (v !== p) { p = +v.toFixed(4); touched = true; draw(); on(); }
  });
  draw();
  return { value: () => p, touched: () => touched, freeze() { locked = true; }, show(v) { p = v; touched = true; draw(); on(); },
    state: () => ({ p, balanced: Math.abs(p - truth) < 1e-9 ? 1 : 0 }), demo() { p = truth; touched = true; draw(); on(); } };
};

/* ---------- chain: A:B and B:C join only when B is the same size in both ---------- */
W.chain = (el, w, on) => {
  const [p, q] = w.ab, [r, s] = w.bc, MAX = w.max || 8;
  let m1 = 1, m2 = 1, touched = false, locked = false;
  el.innerHTML = `<svg class="chv" viewBox="0 0 340 96" role="img" aria-label="Two linked ratios"><g id="rows"></g></svg>
    <div class="ch-keys"><span><button class="tile" data-c="1-">−</button><b id="k1"></b><button class="tile" data-c="1+">+</button></span><span><button class="tile" data-c="2-">−</button><b id="k2"></b><button class="tile" data-c="2+">+</button></span></div><div class="wx-read ch-read"></div>`;
  const rows = $("#rows", el), read = $(".ch-read", el), good = () => q * m1 === r * m2;
  const block = (x, y, n, c, cell, t) => `<rect x="${x}" y="${y}" width="${n * cell - 2}" height="30" rx="4" fill="${c}"/><text x="${x + (n * cell) / 2}" y="${y + 20}" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">${t} ${n}</text>`;
  const draw = () => {
    const A = p * m1, B1 = q * m1, B2 = r * m2, C = s * m2, cell = Math.min(22, 334 / (A + Math.max(B1, B2) + C)), x0 = 3 + A * cell, ok = good();
    rows.innerHTML = block(3, 8, A, BLUE, cell, "A") + block(x0, 8, B1, ok ? GREEN : GOLD, cell, "B") + block(x0, 52, B2, ok ? GREEN : GOLD, cell, "B") + block(x0 + B2 * cell, 52, C, RED, cell, "C");
    $("#k1", el).textContent = `×${m1}`; $("#k2", el).textContent = `×${m2}`;
    read.innerHTML = ok ? `<b class="yes">$A : B : C = ${A} : ${B1} : ${C}$</b>` : T(B("The two B's are different sizes", "দুটা B বেলেগ আকাৰৰ"));
  };
  el.addEventListener("click", (e) => {
    const b = e.target.closest("[data-c]"); if (!b || locked) return;
    const code = b.dataset.c, d = code[1] === "+" ? 1 : -1;
    if (code[0] === "1") m1 = clamp(m1 + d, 1, MAX); else m2 = clamp(m2 + d, 1, MAX);
    touched = true; SFX.tap(); draw(); on();
  });
  const lcmFit = () => { for (let a = 1; a <= MAX; a++) for (let c = 1; c <= MAX; c++) if (q * a === r * c) return [a, c]; return [1, 1]; };
  draw();
  return { value: () => (good() ? q * m1 : 0), touched: () => touched, freeze() { locked = true; }, show() { [m1, m2] = lcmFit(); touched = true; draw(); on(); },
    state: () => ({ match: good() ? 1 : 0 }), demo() { [m1, m2] = lcmFit(); touched = true; draw(); on(); } };
};
})();
