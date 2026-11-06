/* =========================================================
   AxomRank maths stage: scenes built from what each concept is.
   docs/MATHEMATICS-VISUALS.md explains the idea behind each one.
   Every scene: scene(el, spec, onChange) returns
     { value(), state(), touched(), freeze(), show(v), demo(goal) }
   state() feeds the goals of do-to-discover cards.
   Colour carries meaning everywhere: blue positive, red negative, gold zero, green fractions.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#16305C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F", FAINT = "#7E93AE";
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const smooth = (a, b, v) => { const t = clamp((v - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
const gcd = (a, b) => (b ? gcd(b, a % b) : Math.abs(a));
const lcm = (a, b) => (a * b) / gcd(a, b);
const clean = (v) => +v.toFixed(10);
const still = () => matchMedia("(prefers-reduced-motion: reduce)").matches || document.documentElement.classList.contains("no-motion");
const minus = (s) => String(s).replace("-", "−");
function fmt(v, dp) { const s = Math.abs(v) < 1e-12 ? "0" : v.toFixed(Math.max(0, dp)); return minus(s); }
function nameFraction(v) {   // the simplest fraction for a value, when there is a short one
  for (let q = 1; q <= 100; q++) { const p = Math.round(v * q); if (Math.abs(v - p / q) < 1e-9) return [p, q]; }
  return null;
}
const texFrac = ([p, q]) => (q === 1 ? minus(p) : `${p < 0 ? "-" : ""}\\frac{${Math.abs(p)}}{${q}}`);
function tween(from, to, ms, step, done) {
  if (still()) { step(to); if (done) done(); return () => {}; }
  const t0 = performance.now(); let raf = 0, live = true;
  const tick = (t) => { if (!live) return; const k = clamp((t - t0) / ms, 0, 1), e = 1 - (1 - k) ** 3; step(from + (to - from) * e); if (k < 1) raf = requestAnimationFrame(tick); else if (done) done(); };
  raf = requestAnimationFrame(tick);
  return () => { live = false; cancelAnimationFrame(raf); };
}

/* ---------- the number line: position, sign and zoom. Decimals above, fractions below. ---------- */
W.line = (el, w, on) => {
  const lo = w.min ?? -10, hi = w.max ?? 10, H = 216, AXIS = 132;
  el.innerHTML = `<canvas class="nl" aria-label="Number line. Drag to move, pinch or use the buttons to zoom."></canvas><div class="nl-read" aria-live="polite"></div>
    <div class="nl-tools"><button class="nl-b" data-z="out" aria-label="Zoom out">−</button><button class="nl-b wide" data-z="in">${T(B("Zoom in ×10", "×10 জুম কৰা"))}</button><button class="nl-b" data-z="home" aria-label="Back to the start">⟲</button></div>`;
  const cv = $("canvas", el), g = cv.getContext("2d"), read = $(".nl-read", el);
  let width = 320, scale = 30, center = (lo + hi) / 2, homeS = 30, value = w.value ?? null, touched = false, locked = false, dirty = true, stopView = null;
  const X = (v) => width / 2 + (v - center) * scale, V = (x) => center + (x - width / 2) / scale;
  const minorStep = () => 10 ** Math.ceil(Math.log10(11 / scale));
  const snap = (v) => {
    const step = w.den ? 1 / w.den : w.snap || minorStep();
    let best = Math.round(v / step) * step;
    if (w.fractions && !w.den) for (const q of FRACTIONS) {   // a nearby visible fraction wins, so 3/4 and 1/3 can be reached
      if (scale / q < 30) break;
      const f = Math.round(v * q) / q; if (Math.abs(f - v) * scale < 10) { best = f; break; }
    }
    return clamp(clean(best), Math.min(lo, -1e9), 1e9);
  };
  const FRACTIONS = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 100];
  function size() {
    const r = cv.getBoundingClientRect(), d = Math.min(devicePixelRatio || 1, 3);
    if (!r.width) return;
    const keep = homeS === scale;
    width = r.width; cv.width = width * d; cv.height = H * d; g.setTransform(d, 0, 0, d, 0, 0);
    homeS = (width - 36) / (hi - lo); if (keep || scale < homeS) scale = homeS;
    dirty = true;
  }
  function text(s, x, y, color, font = "800 13px Nunito, sans-serif", a = "center") { g.font = font; g.fillStyle = color; g.textAlign = a; g.fillText(s, x, y); }
  function fraction(p, q, x, y, color) {
    const neg = p < 0, n = String(Math.abs(p)), d = String(q);
    g.font = "800 12px Nunito, sans-serif"; const bar = Math.max(g.measureText(n).width, g.measureText(d).width) + 3;
    text(n, x, y, color, "800 12px Nunito, sans-serif"); text(d, x, y + 14, color, "800 12px Nunito, sans-serif");
    g.strokeStyle = color; g.lineWidth = 1.4; g.beginPath(); g.moveTo(x - bar / 2, y + 3); g.lineTo(x + bar / 2, y + 3); g.stroke();
    if (neg) text("−", x - bar / 2 - 6, y + 6, color, "800 12px Nunito, sans-serif");
  }
  const pinMark = (x, color, big) => { g.fillStyle = color; g.beginPath(); g.moveTo(x, AXIS - 3); g.lineTo(x - (big ? 9 : 6), AXIS - (big ? 19 : 14)); g.lineTo(x + (big ? 9 : 6), AXIS - (big ? 19 : 14)); g.closePath(); g.fill(); };
  function draw() {
    dirty = false;
    g.clearRect(0, 0, width, H);
    const zero = X(0), left = V(0), right = V(width), zoomed = scale > homeS * 1.4;
    // the zoom ladder: where this view sits inside the view ten times wider
    if (zoomed) {
      const span = width / scale, wide = 10 ** Math.ceil(Math.log10(span * 2.5)), a = Math.floor(center / wide) * wide, x0 = 16, x1 = width - 16, Y = 26;
      const px = (v) => x0 + ((v - a) / wide) * (x1 - x0), wa = clamp(px(left), x0, x1), wb = clamp(px(right), x0, x1);
      g.fillStyle = "rgba(31,95,191,.09)"; g.beginPath(); g.moveTo(wa, Y); g.lineTo(wb, Y); g.lineTo(width, AXIS - 62); g.lineTo(0, AXIS - 62); g.closePath(); g.fill();
      g.strokeStyle = FAINT; g.lineWidth = 2; g.beginPath(); g.moveTo(x0, Y); g.lineTo(x1, Y); g.stroke();
      for (let k = 0; k <= 10; k++) { const x = x0 + (k / 10) * (x1 - x0); g.lineWidth = 1; g.beginPath(); g.moveTo(x, Y - 4); g.lineTo(x, Y + 4); g.stroke(); }
      g.strokeStyle = BLUE; g.lineWidth = 5; g.beginPath(); g.moveTo(wa, Y); g.lineTo(wb, Y); g.stroke();
      const dp = Math.max(0, -Math.round(Math.log10(wide)));
      text(fmt(a, dp), x0, Y - 9, FAINT, "800 11px Nunito, sans-serif", "left"); text(fmt(a + wide, dp), x1, Y - 9, FAINT, "800 11px Nunito, sans-serif", "right");
    }
    // the two halves of the line
    g.lineCap = "round"; g.lineWidth = 5;
    if (zero > 0) { g.strokeStyle = RED; g.beginPath(); g.moveTo(0, AXIS); g.lineTo(Math.min(zero, width), AXIS); g.stroke(); }
    if (zero < width) { g.strokeStyle = BLUE; g.beginPath(); g.moveTo(Math.max(zero, 0), AXIS); g.lineTo(width, AXIS); g.stroke(); }
    // ticks: each power of ten fades in as there is room, so zooming reveals the next decimal place
    const step = minorStep(), px = step * scale, dpOf = (s) => Math.max(0, -Math.round(Math.log10(s)));
    const first = Math.floor(left / step) - 1, last = Math.ceil(right / step) + 1;
    for (let k = first; k <= last; k++) {
      const v = k * step, x = X(v), ten = k % 10 === 0, five = k % 5 === 0;
      if (k === 0) continue;
      const color = v < 0 ? RED : BLUE;
      g.strokeStyle = color; g.globalAlpha = ten ? 1 : five ? 0.8 : smooth(10, 26, px) * 0.75 + 0.2; g.lineWidth = ten ? 2.4 : 1.4;
      const h = ten ? 15 : five ? 10 : 6; g.beginPath(); g.moveTo(x, AXIS - h); g.lineTo(x, AXIS + h * 0.5); g.stroke();
      const a = ten ? 1 : five ? smooth(20, 34, px * 5) * 0.9 * smooth(5.5, 8, px) : smooth(33, 48, px);
      g.globalAlpha = Math.min(1, a);
      if (a > 0.02) text(fmt(clean(v), ten ? dpOf(step * 10) : dpOf(step)), x, AXIS - 23, color, ten ? "900 15px Nunito, sans-serif" : "800 12.5px Nunito, sans-serif");
      g.globalAlpha = 1;
    }
    // fractions wait until they have room: the same points, named by cutting
    if (w.fractions !== false) {
      const taken = [];
      for (const q of FRACTIONS) {
        const a = smooth(26, 44, scale / q); if (!a) continue;
        for (let p = Math.floor(left * q); p <= Math.ceil(right * q); p++) {
          if (p % q === 0 || gcd(p, q) !== 1) continue;
          const x = X(p / q); if (taken.some((t) => Math.abs(t - x) < 27)) continue;
          taken.push(x); g.globalAlpha = a;
          g.strokeStyle = GREEN; g.lineWidth = 1.6; g.beginPath(); g.moveTo(x, AXIS + 3); g.lineTo(x, AXIS + 18); g.stroke();
          fraction(p, q, x, AXIS + 33, GREEN); g.globalAlpha = 1;
        }
      }
      if (scale >= 18) for (let n = Math.ceil(left); n <= Math.floor(right); n++) if (n && scale > 150 && !taken.some((t) => Math.abs(t - X(n)) < 20)) text(minus(n), X(n), AXIS + 36, n < 0 ? RED : BLUE, "900 13px Nunito, sans-serif");
    }
    // zero, the mirror between the two halves
    if (zero > -20 && zero < width + 20) {
      g.strokeStyle = GOLD; g.lineWidth = 4; g.beginPath(); g.moveTo(zero, AXIS - 24); g.lineTo(zero, AXIS + 16); g.stroke();
      g.fillStyle = GOLD; g.beginPath(); g.arc(zero, AXIS - 34, 11, 0, 7); g.fill(); text("0", zero, AXIS - 29.5, "#fff", "900 14px Nunito, sans-serif");
    }
    if (w.pin) { const x = X(w.pin.v); pinMark(x, GREEN, true); if (w.pin.t) text(w.pin.t, clamp(x, 18, width - 18), AXIS - 46, GREEN, "900 13px Nunito, sans-serif"); }
    if (value != null) {
      const x = X(value), color = value < 0 ? RED : value > 0 ? BLUE : GOLD;
      if (w.mirror && value) {
        const m = X(-value), mid = (x + m) / 2, r = Math.abs(x - m) / 2;
        g.strokeStyle = "rgba(216,147,11,.75)"; g.lineWidth = 2; g.setLineDash([5, 5]); g.beginPath(); g.ellipse(mid, AXIS, r, Math.min(r, 52), 0, Math.PI, 0); g.stroke(); g.setLineDash([]);
        pinMark(m, value > 0 ? "rgba(211,50,63,.55)" : "rgba(31,95,191,.55)", false);
        text(fmt(-value, dpOf(step)), clamp(m, 16, width - 16), AXIS - 24, value > 0 ? RED : BLUE, "900 13px Nunito, sans-serif");
      }
      pinMark(x, color, true);
      g.fillStyle = color; g.beginPath(); g.arc(clamp(x, 8, width - 8), AXIS, 7, 0, 7); g.fill();
      g.strokeStyle = "#fff"; g.lineWidth = 2.5; g.stroke();
    }
  }
  function report() {
    if (value == null) { read.innerHTML = w.prompt ? T(w.prompt) : ""; return; }
    const dp = Math.max(0, -Math.round(Math.log10(w.den ? 0.001 : minorStep()))), f = nameFraction(value);
    const dec = fmt(value, f && f[1] === 1 ? 0 : Math.min(dp + 1, 8)).replace(/(\.\d*?)0+$/, "$1").replace(/\.$/, "");
    read.innerHTML = `<b class="${value < 0 ? "neg" : value > 0 ? "pos" : "zero"}">$${dec}$</b>${f && f[1] !== 1 ? `<span class="fr">$= ${texFrac(f)}$</span>` : ""}${w.percent ? `<span>$= ${clean(value * 100)}\\%$</span>` : ""}`;
  }
  function viewTo(s, c, done) {
    if (stopView) stopView();
    const s0 = Math.log(scale), s1 = Math.log(s), c0 = center;
    stopView = tween(0, 1, 620, (k) => { scale = Math.exp(s0 + (s1 - s0) * k); center = c0 + (c - c0) * k; dirty = true; on(); }, done);
  }
  const zoomAt = (factor, at) => { const v = V(at); scale = clamp(scale * factor, homeS * 0.5, 4e7); center = v - (at - width / 2) / scale; dirty = true; on(); };
  const setValue = (v) => { value = v; touched = true; report(); dirty = true; on(); };
  const pts = new Map(); let mode = null, moved = 0, last = 0, dist = 0;
  cv.addEventListener("pointerdown", (e) => {
    if (stopView) stopView();
    cv.setPointerCapture(e.pointerId); pts.set(e.pointerId, e); const r = cv.getBoundingClientRect(), x = e.clientX - r.left;
    moved = 0; last = x;
    if (pts.size === 2) { const [a, b] = [...pts.values()]; dist = Math.abs(a.clientX - b.clientX); mode = "pinch"; return; }
    mode = !locked && value != null && !w.readonly && Math.abs(X(value) - x) < 34 ? "marker" : "pan";
    if (mode === "marker") SFX.tap();
  });
  cv.addEventListener("pointermove", (e) => {
    if (!pts.has(e.pointerId)) return;
    pts.set(e.pointerId, e); const r = cv.getBoundingClientRect(), x = e.clientX - r.left;
    if (mode === "pinch" && pts.size === 2) {
      const [a, b] = [...pts.values()], d = Math.max(20, Math.abs(a.clientX - b.clientX)), mid = (a.clientX + b.clientX) / 2 - r.left;
      zoomAt(d / Math.max(20, dist), mid); dist = d; moved += 10; report(); return;
    }
    moved += Math.abs(x - last);
    if (mode === "marker") setValue(snap(V(x)));
    else if (mode === "pan") { center -= (x - last) / scale; dirty = true; on(); }
    last = x;
  });
  const up = (e) => {
    if (!pts.has(e.pointerId)) return;
    const wasTap = mode === "pan" && moved < 6 && pts.size === 1 && !w.readonly && !locked;
    pts.delete(e.pointerId); mode = pts.size ? "pan" : null;
    if (wasTap) { const r = cv.getBoundingClientRect(); setValue(snap(V(e.clientX - r.left))); SFX.tap(); }
  };
  cv.addEventListener("pointerup", up); cv.addEventListener("pointercancel", up);
  cv.addEventListener("wheel", (e) => { e.preventDefault(); const r = cv.getBoundingClientRect(); zoomAt(Math.exp(-e.deltaY * 0.0022), e.clientX - r.left); report(); }, { passive: false });
  el.addEventListener("click", (e) => {
    const b = e.target.closest("[data-z]"); if (!b) return;
    const focus = value ?? (w.pin ? w.pin.v : center);
    if (b.dataset.z === "in") viewTo(Math.min(scale * 10, 4e7), focus, report);
    else if (b.dataset.z === "out") viewTo(Math.max(scale / 10, homeS), scale / 10 <= homeS ? (lo + hi) / 2 : center, report);
    else viewTo(homeS, (lo + hi) / 2, report);
    SFX.tap();
  });
  new ResizeObserver(() => { size(); }).observe(cv);
  const loop = () => { if (!cv.isConnected) return; if (dirty) draw(); requestAnimationFrame(loop); };
  size(); report(); requestAnimationFrame(loop);
  if (document.fonts) document.fonts.ready.then(() => { dirty = true; });
  return {
    value: () => value, touched: () => touched, freeze() { locked = true; },
    state: () => ({ value: value ?? NaN, span: width / scale, zoom: scale / homeS, left: V(0), right: V(width) }),
    show(v) {   // reveal a value at a zoom where its last digit is visible
      value = v; touched = true;
      const digits = (String(clean(v)).split(".")[1] || "").length, need = w.den ? scale : Math.max(scale, 16 * 10 ** digits);
      viewTo(digits && !w.den ? need : scale, digits ? v : scale > homeS * 1.4 ? v : center, report); report(); dirty = true; on();
    },
    demo(goal) {
      if (goal.value != null) { const v = goal.value.near ?? goal.value; value = v; touched = true; report(); viewTo(scale, Math.abs(X(v) - width / 2) < width / 2 - 20 ? center : v, () => on()); }
      else if (goal.span) { const f = value ?? (w.pin ? w.pin.v : center); viewTo(width / (goal.span.lt * 0.8), f, () => { report(); on(); }); }
      else if (goal.zoom) { const f = value ?? (w.pin ? w.pin.v : center); viewTo(homeS * goal.zoom.gt * 1.3, f, () => { report(); on(); }); }
    },
  };
};
// Older specs and short fraction lines still work: a zero-to-max line that snaps to one cut size.
W.numline = (el, w, on) => W.line(el, { min: w.min || 0, max: w.max, den: w.den, value: w.start, fractions: true }, on);

/* ---------- arrays: a factor is a rectangle the dots can make ---------- */
W.array = (el, w, on) => {
  const n = w.n, top = w.max || Math.min(n, 12);
  let c = w.c || 2, touched = false, locked = false; const found = new Set();
  el.innerHTML = `<div class="ar-box">${Array.from({ length: n }, () => "<i></i>").join("")}</div><input class="wx-range" type="range" min="1" max="${top}" value="${c}" aria-label="Dots in each row"><div class="ar-read"></div><div class="ar-found"></div>`;
  const box = $(".ar-box", el), dots = [...box.children], input = $("input", el), read = $(".ar-read", el), chips = $(".ar-found", el);
  function draw() {
    const rows = Math.ceil(n / c), fits = n % c === 0, W0 = box.clientWidth || 300, cell = Math.min(W0 / c, 168 / rows, 26), left = n % c, x0 = (W0 - cell * c) / 2;
    box.style.height = `${rows * cell + 4}px`;
    dots.forEach((d, k) => { const r = Math.floor(k / c), col = k % c; d.style.cssText = `width:${cell - 4}px;height:${cell - 4}px;transform:translate(${x0 + col * cell}px,${r * cell}px)`; d.className = !fits && r === rows - 1 ? "odd" : fits ? "fit" : ""; });
    read.innerHTML = fits ? `<b class="pos">$${n} = ${c} \\times ${n / c}$</b>` : `<b class="neg">$${n} \\div ${c}$</b> ${T(B(`leaves ${left} over`, `${left} বাকী থাকে`))}`;
    if (fits) { found.add(c); found.add(n / c); }
    chips.innerHTML = [...found].sort((a, b) => a - b).map((f) => `<span>${f}</span>`).join("");
  }
  input.addEventListener("input", () => { if (locked) return; c = +input.value; touched = true; SFX.tap(); draw(); on(); });
  new ResizeObserver(draw).observe(box); draw();
  return { value: () => found.size, touched: () => touched, freeze() { locked = true; input.disabled = true; },
    state: () => ({ c, fits: n % c === 0 ? 1 : 0, found: found.size, broke: n % c ? 1 : 0 }), show() {},
    demo(goal) { const want = goal.c ?? (goal.broke ? [2, 3, 4, 5, 7].find((k) => n % k) : [...Array(top).keys()].map((k) => k + 1).find((k) => n % k === 0 && !found.has(k))) ?? 1; c = want; input.value = c; touched = true; draw(); on(); if (goal.found && found.size < goal.found.gt + 1 && goal.found.gt < 20) setTimeout(() => this.demo(goal), 350); } };
};

/* ---------- gears: LCM is when two rhythms come back together ---------- */
W.gears = (el, w, on) => {
  const a = w.a, b = w.b, L = lcm(a, b), top = L * 2, k = 122 / (a + b), r1 = a * k + 10, r2 = b * k + 10, cx1 = 16 + r1, cx2 = cx1 + r1 + r2 + 1, cy = 100;
  const gear = (t, r, fill) => { const wide = Math.min(((2 * Math.PI * r) / t) * 0.52, 16); let d = ""; for (let i = 0; i < t; i++) d += `<rect x="${r - 6}" y="${-wide / 2}" width="13" height="${wide}" rx="2.5" fill="${fill}" transform="rotate(${(i * 360) / t})"/>`; return `${d}<circle r="${r - 3}" fill="${fill}"/><circle r="${(r - 3) * 0.52}" fill="#fff"/>`; };
  const off = -180 / b, mark = (r, ang) => { const t = (ang * Math.PI) / 180; return `<circle class="mk" cx="${(r - 8) * Math.cos(t)}" cy="${(r - 8) * Math.sin(t)}" r="7" fill="#fff" stroke="${RED}" stroke-width="3.5"/>`; };
  el.innerHTML = `<svg class="gears" viewBox="0 0 340 200" role="img" aria-label="Two gears"><g id="g1">${gear(a, r1, BLUE)}${mark(r1, 0)}</g><g id="g2">${gear(b, r2, GOLD)}${mark(r2, off)}</g>
    <circle id="spark" cx="${cx1 + r1}" cy="${cy}" r="20" fill="none" stroke="${RED}" stroke-width="3" opacity="0"/>
    <text x="${cx1}" y="${cy + 7}" text-anchor="middle" font-weight="900" font-size="20" fill="${INK}">${a}</text><text x="${cx2}" y="${cy + 7}" text-anchor="middle" font-weight="900" font-size="20" fill="${INK}">${b}</text></svg>
    <div class="gr-row"><button class="tile gr-go" data-go>${T(B("Turn one tooth", "এটা দাঁত ঘূৰোৱা"))}</button><span class="gr-n"></span></div><div class="gr-strip"></div>`;
  const g1 = $("#g1", el), g2 = $("#g2", el), strip = $(".gr-strip", el), count = $(".gr-n", el);
  let n = 0, shown = 0, touched = false, locked = false, stop = null;
  function pose(v) {
    g1.setAttribute("transform", `translate(${cx1} ${cy}) rotate(${(v / a) * 360})`);
    g2.setAttribute("transform", `translate(${cx2} ${cy}) rotate(${180 + 180 / b - (v / b) * 360})`);
  }
  function list() {
    count.textContent = n; const meet = n > 0 && n % a === 0 && n % b === 0;
    strip.innerHTML = Array.from({ length: Math.min(top, 48) }, (_, i) => { const v = i + 1, A = v % a === 0, Bb = v % b === 0; return v <= n ? `<i class="${A && Bb ? "ab" : A ? "a" : Bb ? "b" : ""}">${A || Bb ? v : ""}</i>` : "<i></i>"; }).join("");
    el.classList.toggle("meet", meet); $("#spark", el).setAttribute("opacity", meet ? 1 : 0);
    if (meet) SFX.pair();
  }
  const turn = (to) => { n = to; touched = true; list(); if (stop) stop(); stop = tween(shown, n, 360, (v) => { shown = v; pose(v); }); on(); };
  el.addEventListener("click", (e) => { if (e.target.closest("[data-go]") && !locked && n < top) { SFX.tap(); turn(n + 1); } });
  pose(0); list();
  return { value: () => n, touched: () => touched, freeze() { locked = true; }, show(v) { turn(v); },
    state: () => ({ n, meet: n > 0 && n % a === 0 && n % b === 0 ? 1 : 0, meets: Math.floor(n / L) }), demo(goal) { turn(L * ((goal.meets ? goal.meets.gt : 0) + 1)); } };
};

/* ---------- square tiles: HCF is the largest square that fills a rectangle (Euclid) ---------- */
W.tiles = (el, w, on) => {
  const sw = Math.max(w.a, w.b), sh = Math.min(w.a, w.b), k = Math.min(300 / sw, 150 / sh), PAL = [BLUE, GOLD, GREEN, RED];
  el.innerHTML = `<svg class="tl" viewBox="-1 -1 ${sw * k + 2} ${sh * k + 2}" role="img" aria-label="${w.a} by ${w.b} rectangle"><rect width="${sw * k}" height="${sh * k}" fill="#fff" stroke="${INK}" stroke-width="2"/></svg><button class="tile gr-go" data-cut>${T(B("Cut the biggest square", "সৰ্ববৃহৎ বৰ্গটো কাটা"))}</button><div class="tl-log"></div>`;
  const svg = $("svg", el), log = $(".tl-log", el);
  let x = 0, y = 0, rw = sw, rh = sh, depth = 0, cuts = 0, locked = false, touched = false;
  function cut() {
    if (!rh || !rw) return;
    const s = Math.min(rw, rh), wide = rw >= rh;
    svg.insertAdjacentHTML("beforeend", `<rect class="tl-s" x="${x * k + 1}" y="${y * k + 1}" width="${s * k - 2}" height="${s * k - 2}" rx="2" fill="${PAL[depth % 4]}"/><text x="${(x + s / 2) * k}" y="${(y + s / 2) * k + 5}" text-anchor="middle" font-weight="900" font-size="${Math.max(10, Math.min(16, s * k / 3))}" fill="#fff">${s}</text>`);
    cuts++; touched = true;
    if (wide) { x += s; rw -= s; } else { y += s; rh -= s; }
    const a = rw, b = rh;
    if (!rw || !rh) { log.innerHTML = `<b class="pos">${T(B(`Fits exactly. The HCF is ${s}.`, `ঠিক মিলিল। গ.সা.গু. ${s}।`))}</b>`; $("[data-cut]", el).disabled = true; SFX.done(); }
    else { log.innerHTML = `$${a} \\times ${b}$ ${T(B("is left", "বাকী"))}`; SFX.pair(); if ((wide && rw < rh) || (!wide && rh < rw)) depth++; }
    on();
  }
  el.addEventListener("click", (e) => { if (e.target.closest("[data-cut]") && !locked) cut(); });
  log.innerHTML = `$${sw} \\times ${sh}$`;
  return { value: () => (rw && rh ? 0 : Math.max(rw, rh)), touched: () => touched, freeze() { locked = true; }, show() { while (rw && rh) cut(); },
    state: () => ({ cuts, done: rw && rh ? 0 : 1 }), demo() { const go = () => { if (rw && rh) { cut(); setTimeout(go, 420); } }; go(); } };
};

/* ---------- the digit dial: the last digit of powers walks round a closed path ---------- */
W.dial = (el, w, on) => {
  const b = w.b % 10, P = (d) => { const a = (d / 10) * 2 * Math.PI - Math.PI / 2; return [100 + 74 * Math.cos(a), 100 + 74 * Math.sin(a)]; };
  el.innerHTML = `<div class="dl"><svg viewBox="0 0 200 200" role="img" aria-label="Dial of the digits 0 to 9"><circle cx="100" cy="100" r="74" fill="none" stroke="#CFE0EA" stroke-width="2"/>${Array.from({ length: 10 }, (_, d) => { const [x, y] = P(d), a = (d / 10) * 2 * Math.PI - Math.PI / 2; return `<circle cx="${x}" cy="${y}" r="4" fill="${FAINT}" data-d="${d}"/><text x="${100 + 91 * Math.cos(a)}" y="${105 + 91 * Math.sin(a)}" text-anchor="middle" font-weight="900" font-size="14" fill="${INK}">${d}</text>`; }).join("")}<path id="trail" fill="rgba(31,95,191,.12)" stroke="${BLUE}" stroke-width="3" stroke-linejoin="round"/></svg>
    <div class="dl-side"><button class="tile gr-go" data-next>${T(B("Next power", "পিছৰ ঘাত"))}</button><div class="dl-list"></div></div></div>`;
  const trail = $("#trail", el), list = $(".dl-list", el), seq = [];
  let cur = 1, closed = false, locked = false, touched = false;
  function next() {
    cur = (cur * b) % 10; const again = seq.includes(cur); touched = true;
    if (again) closed = true; seq.push(cur);
    const pts = seq.map(P); trail.setAttribute("d", `M${pts.map((p) => p.map((v) => v.toFixed(1)).join(" ")).join("L")}${closed ? "Z" : ""}`);
    list.innerHTML = seq.map((d, k) => `<span class="${closed && k === seq.length - 1 ? "again" : ""}">$${w.b}^{${k + 1}}$ ${T(B("ends", "শেষত"))} <b>${d}</b></span>`).join("");
    if (closed) { $("[data-next]", el).disabled = true; SFX.done(); } else SFX.pair();
    on();
  }
  el.addEventListener("click", (e) => { if (e.target.closest("[data-next]") && !locked && !closed) next(); });
  return { value: () => seq.length, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ k: seq.length, closed: closed ? 1 : 0 }), demo() { const go = () => { if (!closed) { next(); setTimeout(go, 380); } }; go(); } };
};

/* ---------- common cuts: fractions add once both fit the same cuts ---------- */
W.cuts = (el, w, on) => {
  const [p, q] = w.a, [r, s] = w.b, top = w.max || 24;
  let d = w.d || Math.max(q, s), touched = false, locked = false;
  el.innerHTML = `<svg class="ct" viewBox="0 0 320 112" role="img" aria-label="Fraction bar"><rect x="1" y="30" width="318" height="52" rx="5" fill="#fff" stroke="${INK}" stroke-width="2"/><rect id="fa" x="2" y="31" height="50" fill="${BLUE}" opacity=".78"/><rect id="fb" y="31" height="50" fill="${GREEN}" opacity=".78"/><g id="lines"></g></svg>
    <div class="wx-step"><button class="tile" data-less aria-label="Fewer cuts">−</button><span class="ct-n"></span><button class="tile" data-more aria-label="More cuts">+</button></div><div class="wx-read ct-read"></div>`;
  const lines = $("#lines", el), read = $(".ct-read", el);
  $("#fa", el).setAttribute("width", (p / q) * 316); $("#fb", el).setAttribute("x", 2 + (p / q) * 316); $("#fb", el).setAttribute("width", (r / s) * 316);
  const draw = () => {
    let out = ""; const xOf = (t) => 1 + t * 318;
    for (let k = 1; k < q; k++) out += `<path d="M${xOf(k / q)} 6V30" stroke="${BLUE}" stroke-width="3"/>`;
    for (let k = 1; k < s; k++) out += `<path d="M${xOf(k / s)} 82V106" stroke="${GREEN}" stroke-width="3"/>`;
    for (let k = 1; k < d; k++) { const hit = (k * q) % d === 0 || (k * s) % d === 0; out += `<path d="M${xOf(k / d)} 30V82" stroke="${hit ? INK : FAINT}" stroke-width="${hit ? 2 : 1}"/>`; }
    lines.innerHTML = out; const ok = d % q === 0 && d % s === 0;
    $(".ct-n", el).innerHTML = T(B(`${d} equal cuts`, `${d}টা সমান কাট`));
    read.innerHTML = ok ? `<b class="pos">$\\frac{${(p * d) / q}}{${d}} + \\frac{${(r * d) / s}}{${d}} = \\frac{${(p * d) / q + (r * d) / s}}{${d}}$</b>` : T(B("Some marks miss the cuts", "কিছুমান চিন কাটত নপৰে"));
  };
  el.addEventListener("click", (e) => { if (locked) return; if (e.target.closest("[data-more]") && d < top) d++; else if (e.target.closest("[data-less]") && d > 2) d--; else return; touched = true; SFX.tap(); draw(); on(); });
  draw();
  return { value: () => d, touched: () => touched, freeze() { locked = true; }, show(v) { d = v; draw(); }, state: () => ({ d, common: d % q === 0 && d % s === 0 ? 1 : 0 }), demo() { d = lcm(q, s); touched = true; draw(); on(); } };
};

/* ---------- area: the ab/100 of successive percentages is a real corner ---------- */
W.area = (el, w, on) => {
  let a = w.a ?? 0, b = w.b ?? 0, touched = false, locked = false;
  const lo = w.min ?? -50, hi = w.max ?? 60, U = 92, X0 = 10, Y0 = 8;
  el.innerHTML = `<svg class="ar" viewBox="0 0 200 165" role="img" aria-label="A rectangle whose sides change by a percentage"><g id="pcs"></g></svg>
    <label class="sl"><span>${T(B("Width", "প্ৰস্থ"))} <b id="la"></b></span><input class="wx-range" id="ia" type="range" min="${lo}" max="${hi}" step="5" value="${a}"></label><label class="sl"><span>${T(B("Height", "উচ্চতা"))} <b id="lb"></b></span><input class="wx-range" id="ib" type="range" min="${lo}" max="${hi}" step="5" value="${b}"></label><div class="wx-read ar-read2"></div>`;
  const pcs = $("#pcs", el), read = $(".ar-read2", el), sign = (v) => (v > 0 ? "+" : v < 0 ? "−" : "") + Math.abs(v);
  const draw = () => {
    const W0 = U * (1 + a / 100), H0 = U * (1 + b / 100), bx = Math.min(U, W0), by = Math.min(U, H0), corner = a * b / 100, c = corner > 0 ? GOLD : corner < 0 ? RED : "none";
    pcs.innerHTML = `<rect x="${X0}" y="${Y0}" width="${W0}" height="${H0}" fill="rgba(31,95,191,.2)"/><rect x="${X0}" y="${Y0}" width="${bx}" height="${by}" fill="rgba(31,95,191,.5)"/>
      ${a && b ? `<rect x="${X0 + bx}" y="${Y0 + by}" width="${Math.abs(W0 - U)}" height="${Math.abs(H0 - U)}" fill="${c}"/>` : ""}
      <rect x="${X0}" y="${Y0}" width="${U}" height="${U}" fill="none" stroke="${INK}" stroke-width="1.6" stroke-dasharray="4 3"/>
      ${a && b && Math.abs(corner) >= 2 ? `<text x="${X0 + bx + Math.abs(W0 - U) / 2}" y="${Y0 + by + Math.abs(H0 - U) / 2 + 4}" text-anchor="middle" font-weight="900" font-size="11" fill="#fff">${+Math.abs(corner).toFixed(1)}</text>` : ""}`;
    $("#la", el).textContent = `${sign(a)}%`; $("#lb", el).textContent = `${sign(b)}%`;
    const t = a + b + a * b / 100;
    read.innerHTML = `$${a} ${b < 0 ? "-" : "+"} ${Math.abs(b)} ${corner < 0 ? "-" : "+"} ${+Math.abs(corner).toFixed(2)} = ${+t.toFixed(2)}\\%$`;
  };
  const change = () => { if (locked) return; a = +$("#ia", el).value; b = +$("#ib", el).value; touched = true; draw(); on(); };
  $("#ia", el).addEventListener("input", change); $("#ib", el).addEventListener("input", change); draw();
  return { value: () => a + b + a * b / 100, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ a, b, total: a + b + a * b / 100 }),
    demo(g) { a = g.a ?? a; b = g.b ?? b; $("#ia", el).value = a; $("#ib", el).value = b; touched = true; draw(); on(); } };
};

/* ---------- double ruler: a percentage and an amount are two scales on one length ---------- */
W.dual = (el, w, on) => {
  const base = w.base, top = w.max || 100, step = w.step || 5, L = 16, R = 324, x = (p) => L + (p / top) * (R - L);
  let pct = w.pct ?? 0, touched = false, locked = false, drag = false;
  let ticks = ""; for (let p = 0; p <= top; p += 10) ticks += `<path d="M${x(p)} 58V${p % 50 ? 66 : 72}M${x(p)} 104V${p % 50 ? 96 : 90}" stroke="${FAINT}" stroke-width="1.5"/><text x="${x(p)}" y="50" text-anchor="middle" font-size="${p % 50 ? 0 : 12}" font-weight="800" fill="${BLUE}">${p}%</text><text x="${x(p)}" y="122" text-anchor="middle" font-size="${p % 50 ? 0 : 12}" font-weight="800" fill="${GREEN}">${+(base * p / 100).toFixed(2)}</text>`;
  el.innerHTML = `<svg class="dualr" viewBox="0 0 340 132" role="img" aria-label="Percent ruler above an amount ruler"><rect x="${L}" y="70" width="${R - L}" height="22" rx="4" fill="#fff" stroke="${INK}" stroke-width="1.5"/><rect id="fl" x="${L}" y="70" height="22" rx="4" fill="${BLUE}" opacity=".35"/>${ticks}<path id="cr" stroke="${RED}" stroke-width="3"/><circle id="kn" r="11" cy="81" fill="${RED}" stroke="#fff" stroke-width="3"/><text id="tp" y="24" text-anchor="middle" font-weight="900" font-size="15" fill="${RED}"></text></svg><div class="wx-read du-read"></div>`;
  const svg = $("svg", el), read = $(".du-read", el);
  const draw = () => { const X1 = x(pct); $("#fl", el).setAttribute("width", Math.max(0, X1 - L)); $("#cr", el).setAttribute("d", `M${X1} 32V128`); $("#kn", el).setAttribute("cx", X1); const tp = $("#tp", el); tp.setAttribute("x", clamp(X1, 26, 314)); tp.textContent = `${pct}%`; read.innerHTML = `$${pct}\\%\\ \\text{of}\\ ${base} = ${+(base * pct / 100).toFixed(2)}$`; };
  const move = (e) => { if (locked) return; const r = svg.getBoundingClientRect(), px = ((e.clientX - r.left) / r.width) * 340; pct = clamp(Math.round((((px - L) / (R - L)) * top) / step) * step, 0, top); touched = true; draw(); on(); };
  svg.addEventListener("pointerdown", (e) => { svg.setPointerCapture(e.pointerId); drag = true; move(e); SFX.tap(); });
  svg.addEventListener("pointermove", (e) => { if (drag) move(e); }); svg.addEventListener("pointerup", () => { drag = false; }); svg.addEventListener("pointercancel", () => { drag = false; });
  draw();
  return { value: () => pct, touched: () => touched, freeze() { locked = true; }, show(v) { pct = v; touched = true; draw(); }, state: () => ({ pct, amount: base * pct / 100 }), demo(g) { pct = g.pct ?? pct; touched = true; draw(); on(); } };
};
})();
