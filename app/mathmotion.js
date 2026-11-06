/* =========================================================
   AxomRank maths stage, part five: motion and time.
   track: distance, trains and relative speed, journey: average speed, ages: the fixed gap.
   Same contract as app/mathstage.js. The reasons are in docs/MATHEMATICS-VISUALS.md.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#16305C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F";
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const short = (v) => +v.toFixed(2);
const gcd = (a, b) => (b ? gcd(b, a % b) : a);

/* ---------- track: A runs at closing speed against B; a crossing ends when A's tail clears ---------- */
W.track = (el, w, on) => {
  const a = w.a, b = w.b || null, L = a.len || 0, gap = w.gap || 0, bLen = b ? b.len || 0 : 0, bv = b ? b.v || 0 : 0;
  const closing = a.v - bv, need = w.dist ?? (w.meet ? gap : gap + bLen + L), end = need / closing, top = w.max ?? Math.ceil(end * 1.4), step = w.step || 1;
  const T1 = top, ax = a.v * T1, x0 = Math.min(-L, gap + Math.min(0, bv * T1)) - 8, x1 = Math.max(ax, gap + bLen + Math.max(0, bv * T1), w.dist ?? 0) + 8, k = 332 / (x1 - x0), X = (v) => 4 + (v - x0) * k;
  let t = 0, touched = false, locked = false;
  el.innerHTML = `<svg class="trk" viewBox="0 0 340 112" role="img" aria-label="A moving train"><path d="M0 44H340" stroke="${INK}" stroke-width="2"/>${bv ? `<path d="M0 72H340" stroke="${INK}" stroke-width="2"/>` : ""}<g id="tb"></g><g id="ta"></g><rect x="4" y="84" width="332" height="10" rx="5" fill="#E9F0F5"/><rect id="tp" x="4" y="84" height="10" rx="5" fill="${GREEN}"/></svg><input class="wx-range" type="range" min="0" max="${top}" step="${step}" value="0" aria-label="Time"><div class="wx-read tk-read"></div>`;
  const input = $("input", el), read = $(".tk-read", el);
  const body = (fr, len, c, name, y0 = 24) => { const x = X(fr - Math.max(len, 8 / k)), w0 = Math.max(len, 8 / k) * k; return `<rect x="${x}" y="${y0}" width="${w0}" height="20" rx="3" fill="${c}"/>${w0 > 22 ? `<text x="${x + w0 / 2}" y="${y0 + 15}" text-anchor="middle" font-size="12" font-weight="900" fill="#fff">${name}</text>` : ""}`; };
  const draw = () => {
    const fa = a.v * t, covered = closing * t, doneNow = covered >= need - 1e-9;
    $("#ta", el).innerHTML = body(fa, L, BLUE, a.n || "A") + (L ? `<circle cx="${X(fa - L)}" cy="44" r="4" fill="${RED}"/>` : "");
    let scene = "";
    if (b) { const rear = gap + bv * t; scene = bv ? body(rear + bLen, bLen, GOLD, b.n || "B", 52) : bLen ? `<rect x="${X(gap)}" y="44" width="${bLen * k}" height="8" fill="${GOLD}"/>` : `<path d="M${X(gap)} 12V44" stroke="${GOLD}" stroke-width="4"/>`; }
    if (w.dist != null) scene = `<path d="M${X(w.dist)} 10V44" stroke="${GREEN}" stroke-width="3" stroke-dasharray="4 3"/>`;
    $("#tb", el).innerHTML = scene;
    $("#tp", el).setAttribute("width", clamp(covered / need, 0, 1) * 332);
    read.innerHTML = `$${closing} \\times ${t} = ${short(covered)}$ <b class="${doneNow ? "yes" : ""}">/ ${need} ${w.unit || "m"}</b>`;
  };
  input.addEventListener("input", () => { if (locked) return; t = +input.value; touched = true; draw(); on(); });
  draw();
  const setT = (v) => { t = v; input.value = v; touched = true; draw(); on(); };
  return { value: () => t, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: setT, state: () => ({ t, done: closing * t >= need - 1e-9 ? 1 : 0, exact: Math.abs(t - end) < 1e-9 ? 1 : 0 }), demo() { setT(end); } };
};

/* ---------- journey: width is time, height is speed, area is distance ---------- */
W.journey = (el, w, on) => {
  const legs = w.legs, times = legs.map((l) => l.d / l.v), T0 = times.reduce((p, v) => p + v, 0), D = legs.reduce((p, l) => p + l.d, 0), mean = D / T0, top = Math.max(...legs.map((l) => l.v)) * 1.15, VW = 340, VH = 170, BASE = 150, x = (s) => 8 + (s / T0) * 324, y = (v) => BASE - (v / top) * 136, step = w.step || 1;
  let lv = w.start ?? top * 0.8, touched = false, locked = false; lv = Math.round(lv / step) * step;
  el.innerHTML = `<svg class="levelv" viewBox="0 0 ${VW} ${VH}" role="img" aria-label="Speed against time"><g id="jb"></g><path d="M0 ${BASE}H${VW}" stroke="${INK}" stroke-width="2"/><g id="jl"><path d="M0 0H${VW}" stroke="${INK}" stroke-width="3"/><circle cx="${VW - 12}" r="11" fill="${INK}"/><text id="jt" x="${VW - 12}" y="4" text-anchor="middle" font-size="11" font-weight="900" fill="#fff"></text></g></svg><div class="lv-sums"></div>`;
  const svg = $("svg", el), sums = $(".lv-sums", el);
  const draw = () => {
    let s = 0, out = "", up = 0, down = 0;
    legs.forEach((l, k) => {
      const t = times[k], X = x(s), W0 = x(s + t) - X, hi = Math.max(l.v, lv), lo = Math.min(l.v, lv);
      out += `<rect x="${X}" y="${y(lo)}" width="${W0}" height="${BASE - y(lo)}" fill="#A9C4E8"/>`;
      if (l.v > lv) { up += (l.v - lv) * t; out += `<rect x="${X}" y="${y(hi)}" width="${W0}" height="${y(lo) - y(hi)}" fill="${BLUE}"/>`; }
      if (l.v < lv) { down += (lv - l.v) * t; out += `<rect x="${X}" y="${y(hi)}" width="${W0}" height="${y(lo) - y(hi)}" fill="#FBE4E6" stroke="${RED}" stroke-dasharray="3 3"/>`; }
      out += `<text x="${X + W0 / 2}" y="${BASE - 8}" text-anchor="middle" font-size="12" font-weight="900" fill="${INK}">${l.v}</text><text x="${X + W0 / 2}" y="${BASE + 15}" text-anchor="middle" font-size="11" font-weight="800" fill="${INK}">${short(t)} h</text>`;
      s += t;
    });
    $("#jb", el).innerHTML = out; $("#jl", el).setAttribute("transform", `translate(0 ${y(lv)})`); $("#jt", el).textContent = lv;
    const eq = Math.abs(up - down) < 1e-9;
    sums.innerHTML = `<span class="pos">${T(B("Above", "ওপৰত"))} <b>${short(up)}</b></span><span class="${eq ? "ok" : "ne"}">${eq ? "=" : "≠"}</span><span class="neg">${T(B("Gap", "খালী"))} <b>${short(down)}</b></span>`;
  };
  let hold = false;
  const move = (e) => { if (locked) return; const r = svg.getBoundingClientRect(), my = ((e.clientY - r.top) / r.height) * VH, v = clamp(Math.round((((BASE - my) / 136) * top) / step) * step, 0, top); if (v !== lv) { lv = +v.toFixed(4); touched = true; draw(); on(); } };
  svg.addEventListener("pointerdown", (e) => { svg.setPointerCapture(e.pointerId); hold = true; move(e); SFX.tap(); }); svg.addEventListener("pointermove", (e) => { if (hold) move(e); });
  ["pointerup", "pointercancel"].forEach((n) => svg.addEventListener(n, () => { hold = false; }));
  draw();
  return { value: () => lv, touched: () => touched, freeze() { locked = true; }, show(v) { lv = v; touched = true; draw(); on(); }, state: () => ({ balanced: Math.abs(lv - mean) < 1e-9 ? 1 : 0 }), demo() { lv = mean; touched = true; draw(); on(); } };
};

/* ---------- age bars: every year moves both, so the gap between them never changes ---------- */
W.ages = (el, w, on) => {
  const a = w.a, b = w.b, back = w.back ?? Math.min(a, b) - 1, fwd = w.fwd ?? 30, top = Math.max(a, b) + fwd;
  let y = 0, touched = false, locked = false;
  el.innerHTML = `<svg class="agv" viewBox="0 0 340 92" role="img" aria-label="Two ages"><g id="ag"></g></svg><label class="sl"><span id="yl"></span><input class="wx-range" type="range" min="${-back}" max="${fwd}" value="0"></label><div class="wx-read ag-read"></div>`;
  const input = $("input", el), read = $(".ag-read", el), k = 300 / top;
  const draw = () => {
    const A = a + y, Bb = b + y, lo = Math.min(A, Bb), hi = Math.max(A, Bb);
    $("#ag", el).innerHTML = `<text x="14" y="26" text-anchor="middle" font-size="15" font-weight="900" fill="${INK}">${w.na || "A"}</text><rect x="28" y="8" width="${A * k}" height="28" rx="3" fill="${BLUE}"/><text x="${28 + A * k - 6}" y="27" text-anchor="end" font-size="14" font-weight="900" fill="#fff">${A}</text>
      <text x="14" y="70" text-anchor="middle" font-size="15" font-weight="900" fill="${INK}">${w.nb || "B"}</text><rect x="28" y="52" width="${Bb * k}" height="28" rx="3" fill="${GOLD}"/><text x="${28 + Bb * k - 6}" y="71" text-anchor="end" font-size="14" font-weight="900" fill="#fff">${Bb}</text>
      <rect x="${28 + lo * k}" y="${A < Bb ? 8 : 52}" width="${(hi - lo) * k}" height="28" fill="#FBE4E6" stroke="${RED}" stroke-dasharray="4 3"/><text x="${28 + ((lo + hi) / 2) * k}" y="${(A < Bb ? 8 : 52) + 19}" text-anchor="middle" font-size="13" font-weight="900" fill="${RED}">${hi - lo}</text>`;
    const g = gcd(A, Bb) || 1, hit = w.ratio && A * w.ratio[1] === Bb * w.ratio[0];
    $("#yl", el).innerHTML = y === 0 ? T(B("Today", "আজি")) : y > 0 ? T(B(`${y} years from now`, `${y} বছৰৰ পিছত`)) : T(B(`${-y} years ago`, `${-y} বছৰ আগতে`));
    read.innerHTML = `<b class="${hit ? "yes" : ""}">$${A} : ${Bb}$</b> $= ${A / g} : ${Bb / g}$`;
  };
  input.addEventListener("input", () => { if (locked) return; y = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  const setY = (v) => { y = v; input.value = v; touched = true; draw(); on(); };
  return { value: () => y, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show: setY, state: () => ({ y }), demo(g) { setY(g.y); } };
};
})();
