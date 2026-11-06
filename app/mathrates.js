/* =========================================================
   AxomRank maths stage, part four: rates over time.
   growth: simple and compound interest, tank: work and pipes, mandays: inverse proportion.
   Same contract as app/mathstage.js. The reasons are in docs/MATHEMATICS-VISUALS.md.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#1B272C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F";
const gcd = (a, b) => (b ? gcd(b, a % b) : a), lcm = (a, b) => (a * b) / gcd(a, b);
const short = (v) => +v.toFixed(2);

/* ---------- growth bars: simple interest repeats one slice; compound interest earns on itself ---------- */
W.growth = (el, w, on) => {
  let years = w.years ?? 1, rate = w.rate ?? 10, touched = false, locked = false;
  const P = w.p ?? 100, MAXY = 6;
  el.innerHTML = `<svg class="grv" viewBox="0 0 340 170" role="img" aria-label="Interest growing year by year"><g id="gb"></g></svg>
    <label class="sl"><span>${T(B("Years", "বছৰ"))} <b id="gy"></b></span><input class="wx-range" id="iy" type="range" min="1" max="${MAXY}" value="${years}"></label>
    ${w.fixRate ? "" : `<label class="sl"><span>${T(B("Rate", "হাৰ"))} <b id="gr"></b></span><input class="wx-range" id="ir" type="range" min="5" max="30" step="5" value="${rate}"></label>`}<div class="wx-read gr-read"></div>`;
  const draw = () => {
    const r = rate / 100, top = P * (w.simple ? 1 + r * MAXY : (1 + r) ** MAXY), BASE = 148, h = (v) => (v / top) * 132, X0 = 8, cw = 330 / MAXY;
    let out = "";
    for (let t = 1; t <= years; t++) {
      const si = P * r * t, ci = P * (1 + r) ** t, x = X0 + (t - 1) * cw, bw = w.simple ? cw - 12 : (cw - 10) / 2;
      out += `<rect x="${x}" y="${BASE - h(P)}" width="${bw}" height="${h(P)}" fill="#A9C4E8"/><rect x="${x}" y="${BASE - h(P + si)}" width="${bw}" height="${h(si)}" fill="${BLUE}"/>`;
      if (!w.simple) {
        const x2 = x + bw + 2, flat = P + si;
        out += `<rect x="${x2}" y="${BASE - h(P)}" width="${bw}" height="${h(P)}" fill="#A9C4E8"/><rect x="${x2}" y="${BASE - h(flat)}" width="${bw}" height="${h(si)}" fill="${BLUE}"/><rect x="${x2}" y="${BASE - h(ci)}" width="${bw}" height="${h(ci - flat)}" fill="${GOLD}"/>`;
      }
      out += `<text x="${x + (cw - 10) / 2}" y="${BASE + 15}" text-anchor="middle" font-size="12" font-weight="800" fill="${INK}">${t}</text>`;
    }
    $("#gb", el).innerHTML = `${out}<path d="M0 ${BASE}H340" stroke="${INK}" stroke-width="2"/>`;
    const si = P * r * years, ci = P * ((1 + r) ** years - 1);
    $("#gy", el).textContent = years; if ($("#gr", el)) $("#gr", el).textContent = `${rate}%`;
    $(".gr-read", el).innerHTML = w.simple ? `$${P} \\times ${rate}\\% \\times ${years} = ${short(si)}$` : `<span class="si">${T(B("Simple", "সৰল"))} ${short(si)}</span> <span class="ci">${T(B("Compound", "চক্ৰবৃদ্ধি"))} ${short(ci)}</span> <span class="gap">${T(B("Gap", "পাৰ্থক্য"))} ${short(ci - si)}</span>`;
  };
  const change = () => { if (locked) return; years = +$("#iy", el).value; if ($("#ir", el)) rate = +$("#ir", el).value; touched = true; SFX.tap(); draw(); on(); };
  $("#iy", el).addEventListener("input", change); if ($("#ir", el)) $("#ir", el).addEventListener("input", change);
  draw();
  return { value: () => years, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ years, rate }),
    demo(g) { years = g.years ?? years; rate = g.rate ?? rate; $("#iy", el).value = years; if ($("#ir", el)) $("#ir", el).value = rate; touched = true; draw(); on(); } };
};

/* ---------- tank: a job of LCM units; rates add, and an outlet is a negative rate ---------- */
W.tank = (el, w, on) => {
  const taps = w.taps, total = taps.reduce((a, t) => lcm(a, t.t), 1), rate = (t) => (total / t.t) * (t.out ? -1 : 1);
  const live = taps.map((t) => t.on !== false);
  let level = w.level ?? 0, day = 0, touched = false, locked = false;
  const net = () => taps.reduce((a, t, k) => a + (live[k] ? rate(t) : 0), 0), full = () => level >= total - 1e-9;
  const unitWord = w.hours ? B("hour", "ঘণ্টা") : B("day", "দিন");
  el.innerHTML = `<div class="tk"><svg viewBox="0 0 136 190" role="img" aria-label="A tank"><rect x="10" y="6" width="100" height="176" rx="4" fill="#fff" stroke="${INK}" stroke-width="3"/><rect id="wt" x="12" width="96" fill="${BLUE}" opacity=".75"/><g id="tt"></g></svg>
    <div class="tk-side"><div class="tk-taps">${taps.map((t, k) => `<button class="tile tk-tap on" data-tap="${k}"><b>${t.n}</b><span class="${t.out ? "neg" : "pos"}">${t.out ? "−" : "+"}${Math.abs(rate(t))}</span></button>`).join("")}</div>
    <div class="tk-net"></div><button class="tile gr-go" data-next></button><button class="tk-reset" data-reset>${T(B("Start again", "আকৌ আৰম্ভ কৰা"))}</button></div></div>`;
  const wt = $("#wt", el), tt = $("#tt", el), net0 = $(".tk-net", el), go = $("[data-next]", el);
  const H = 172, Y0 = 9;
  let ticks = ""; const every = total > 30 ? 5 : total > 12 ? 2 : 1;
  for (let k = 0; k <= total; k += every) { const y = Y0 + H - (k / total) * H; ticks += `<path d="M10 ${y}h8" stroke="${INK}" stroke-width="1.5"/>${(k % (every * 2) === 0 || total <= 12) ? `<text x="114" y="${y + 4}" font-size="10" font-weight="800" fill="${INK}">${k}</text>` : ""}`; }
  tt.innerHTML = ticks;
  const draw = () => {
    const f = Math.max(0, Math.min(1, level / total));
    wt.setAttribute("y", Y0 + H - f * H); wt.setAttribute("height", f * H);
    net0.innerHTML = `$${short(level)} / ${total}$ ${T(B(`after ${day} ${unitWord.en}${day === 1 ? "" : "s"}`, `${day} ${unitWord.as}ৰ পিছত`))}<br><b class="${net() > 0 ? "yes" : "no"}">${net() > 0 ? "+" : ""}${net()} ${T(B(`per ${unitWord.en}`, `প্ৰতি ${unitWord.as}`))}</b>`;
    go.innerHTML = full() ? "✓" : T(B(`Next ${unitWord.en}`, `পিছৰ ${unitWord.as}`)); go.disabled = full();
    taps.forEach((_, k) => $(`[data-tap="${k}"]`, el).classList.toggle("on", live[k]));
  };
  const step = () => { if (full()) return; level = Math.max(0, Math.min(total, level + net())); day++; touched = true; SFX.pair(); if (full()) SFX.done(); draw(); on(); };
  el.addEventListener("click", (e) => {
    if (locked) return;
    if (e.target.closest("[data-next]")) return step();
    if (e.target.closest("[data-reset]")) { level = w.level ?? 0; day = 0; touched = true; SFX.tap(); draw(); on(); return; }
    const b = e.target.closest("[data-tap]");
    if (b && w.toggle) { const k = +b.dataset.tap; live[k] = !live[k]; touched = true; SFX.tap(); draw(); on(); }
  });
  draw();
  const finish = () => { let g = 0; while (!full() && net() > 0 && g++ < 400) step(); };
  return { value: () => day, ready: full, touched: () => touched, freeze() { locked = true; }, show: finish, state: () => ({ full: full() ? 1 : 0, day, net: net() }), demo: finish };
};

/* ---------- man-days: the job is a fixed area, so more people means fewer days ---------- */
W.mandays = (el, w, on) => {
  const total = w.men * w.days, top = w.max || 40;
  let men = w.men, touched = false, locked = false;
  el.innerHTML = `<svg class="mdv" viewBox="0 0 340 170" role="img" aria-label="A rectangle of people and days"><rect id="mr" x="30" fill="${BLUE}" opacity=".75"/><path id="mg" fill="none" stroke="#fff" stroke-width="1" opacity=".5"/><text id="mw" text-anchor="middle" font-size="14" font-weight="900" fill="${INK}"></text><text id="mh" text-anchor="end" font-size="14" font-weight="900" fill="${INK}"></text><text id="ma" text-anchor="middle" font-size="18" font-weight="900" fill="#fff"></text></svg><input class="wx-range" type="range" min="${w.min || 2}" max="${top}" value="${men}" aria-label="People"><div class="wx-read md-read"></div>`;
  const input = $("input", el), BASE = 158;
  const draw = () => {
    const days = total / men, kx = 300 / top, ky = 140 / (total / (w.min || 2)), Wd = men * kx, Hd = Math.max(4, days * ky), y = BASE - Hd;
    const r = $("#mr", el); r.setAttribute("y", y); r.setAttribute("width", Wd); r.setAttribute("height", Hd);
    let d = ""; const sx = men > 20 ? 5 : 1; for (let k = sx; k < men; k += sx) d += `M${30 + k * kx} ${y}V${BASE}`;
    $("#mg", el).setAttribute("d", d);
    const mw = $("#mw", el); mw.setAttribute("x", 30 + Wd / 2); mw.setAttribute("y", Math.max(14, y - 6)); mw.textContent = men;
    const mh = $("#mh", el); mh.setAttribute("x", 25); mh.setAttribute("y", BASE - Hd / 2 + 5); mh.textContent = short(days);
    const ma = $("#ma", el); ma.setAttribute("x", 30 + Wd / 2); ma.setAttribute("y", BASE - Hd / 2 + 6); ma.textContent = Wd > 50 && Hd > 24 ? total : "";
    $(".md-read", el).innerHTML = `$${men} \\times ${short(days)} = ${total}$`;
  };
  input.addEventListener("input", () => { if (locked) return; men = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  return { value: () => total / men, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show(v) { men = Math.round(total / v); input.value = men; touched = true; draw(); on(); },
    state: () => ({ men }), demo(g) { men = g.men; input.value = men; touched = true; draw(); on(); } };
};
})();
