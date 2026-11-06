/* =========================================================
   AxomRank maths stage, part three: working and money.
   order: order of operations, square and diffsq: squares as area, pairs: perfect squares,
   ladder: cost, marked and selling price, twosale: two sales at one price.
   Same contract as app/mathstage.js. The reasons are in docs/MATHEMATICS-VISUALS.md.
   ========================================================= */
(() => {
"use strict";
const { B, T, SFX } = window.AXOM;
const W = window.AXOM_MATH.widgets;
const $ = (s, r = document) => r.querySelector(s);
const INK = "#1B272C", BLUE = "#1F5FBF", RED = "#D3323F", GOLD = "#D8930B", GREEN = "#0F8A5F", GRID = "#CFDDE8";
const OPEN = "([{", CLOSE = ")]}";
const sign = (v) => (v > 0 ? `+${v}` : v < 0 ? `−${-v}` : "0");
const short = (v) => +v.toFixed(2);

/* ---------- tap the next step: the expression collapses one operation at a time ---------- */
W.order = (el, w, on) => {
  let tok = w.expr.match(/\d+(?:\.\d+)?|[+\-−×÷()[\]{}]/g).map((t) => (/\d/.test(t) ? +t : t.replace("-", "−")));
  let slips = 0, touched = false, locked = false, lines = [];
  const isOp = (t) => typeof t === "string" && "+−×÷".includes(t);
  function next() {   // innermost bracket first, then × and ÷ from the left, then + and − from the left
    let lo = 0, hi = tok.length;
    const end = tok.findIndex((t) => typeof t === "string" && CLOSE.includes(t));
    if (end >= 0) { hi = end; for (let k = end; k >= 0; k--) if (typeof tok[k] === "string" && OPEN.includes(tok[k])) { lo = k + 1; break; } }
    for (let k = lo; k < hi; k++) if (tok[k] === "×" || tok[k] === "÷") return k;
    for (let k = lo; k < hi; k++) if (tok[k] === "+" || tok[k] === "−") return k;
    return -1;
  }
  const done = () => tok.length === 1;
  const show = () => tok.map((t, k) => (isOp(t) ? `<button class="op" data-op="${k}" aria-label="Do ${t} here">${t}</button>` : `<span class="${typeof t === "number" ? "nm" : "br"}">${t}</span>`)).join("");
  const draw = (note = "") => {
    el.innerHTML = `<div class="ord-log">${lines.map((l) => `<div>${l}</div>`).join("")}</div><div class="ord-now">${done() ? "" : "= "}${done() ? `<b>= ${tok[0]}</b>` : show()}</div><div class="ord-note">${note}</div>`;
  };
  function apply(k) {
    const a = tok[k - 1], b = tok[k + 1], o = tok[k], v = o === "+" ? a + b : o === "−" ? a - b : o === "×" ? a * b : a / b;
    lines.push(tok.join(" ").replace(/([([{]) /g, "$1").replace(/ ([)\]}])/g, "$1"));
    tok.splice(k - 1, 3, short(v));
    for (let i = 0; i + 2 < tok.length; i++) if (typeof tok[i] === "string" && OPEN.includes(tok[i]) && typeof tok[i + 2] === "string" && CLOSE.includes(tok[i + 2])) { tok.splice(i + 2, 1); tok.splice(i, 1); i = -1; }
    if (done()) SFX.done(); else SFX.pair();
    draw(); on();
  }
  el.addEventListener("click", (e) => {
    const b = e.target.closest("[data-op]"); if (!b || locked) return;
    const k = +b.dataset.op, want = next(); touched = true;
    if (k === want) return apply(k);
    slips++; SFX.bad(); b.classList.remove("no"); void b.offsetWidth; b.classList.add("no");
    const inside = tok.some((t) => typeof t === "string" && CLOSE.includes(t));
    $(".ord-note", el).innerHTML = T(inside ? B("Brackets finish first", "প্ৰথমে বন্ধনীৰ ভিতৰত") : B("× and ÷ come before + and −, reading from the left", "+ আৰু −ৰ আগতে × আৰু ÷, বাওঁৰ পৰা"));
    on();
  });
  draw();
  const finish = () => { while (!done()) apply(next()); };
  return { value: () => (done() ? tok[0] : NaN), ready: done, slips: () => slips, touched: () => touched, freeze() { locked = true; }, show: finish, state: () => ({ done: done() ? 1 : 0 }), demo: finish };
};

/* ---------- square: a root is the side of a square with that area ---------- */
W.square = (el, w, on) => {
  const top = w.max || 15, S = 210; let n = w.side || 1, touched = false, locked = false;
  el.innerHTML = `<svg class="sqv" viewBox="-1 -1 ${S + 2} ${S + 2}" role="img" aria-label="A square"><g id="sq"></g></svg><input class="wx-range" type="range" min="1" max="${top}" value="${n}" aria-label="Side"><div class="wx-read sq-read"></div>`;
  const g = $("#sq", el), read = $(".sq-read", el), input = $("input", el);
  const draw = () => {
    const c = S / top, a = n * n; let cells = "";
    for (let r = 0; r < n; r++) for (let q = 0; q < n; q++) { const edge = w.gnomon && (r === n - 1 || q === n - 1); cells += `<rect x="${q * c + 0.5}" y="${r * c + 0.5}" width="${c - 1}" height="${c - 1}" fill="${edge ? GOLD : "#A9C4E8"}"/>`; }
    g.innerHTML = cells;
    const hit = w.area != null && a === w.area;
    read.innerHTML = `<b class="${hit ? "yes" : ""}">$${n} \\times ${n} = ${a}$</b>${w.area != null ? ` ${hit ? "=" : "≠"} $${w.area}$` : ""}${w.gnomon && n > 1 ? `<small>$${(n - 1) * (n - 1)} + ${2 * n - 1}$</small>` : ""}`;
  };
  input.addEventListener("input", () => { if (locked) return; n = +input.value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  return { value: () => n, touched: () => touched, freeze() { locked = true; input.disabled = true; }, show(v) { n = v; input.value = v; touched = true; draw(); on(); }, state: () => ({ side: n }), demo(g2) { n = g2.side; input.value = n; touched = true; draw(); on(); } };
};

/* ---------- sliding strip: a² − b² really is the rectangle (a + b)(a − b) ---------- */
W.diffsq = (el, w, on) => {
  const a = w.a, b = w.b, k = 200 / (a + b), A = a * k, Bb = b * k, H = (a - b) * k; let moved = false, locked = false, touched = false;
  el.innerHTML = `<svg class="dfv" viewBox="-14 -14 ${A + Bb + 28} ${A + 28}" role="img" aria-label="Square with a corner removed"><rect x="0" y="0" width="${A}" height="${H}" fill="${BLUE}"/><rect id="strip" fill="${GOLD}"/><rect id="gone" x="${H}" y="${H}" width="${Bb}" height="${Bb}" fill="none" stroke="${RED}" stroke-width="2" stroke-dasharray="5 4"/><text x="${A / 2}" y="-3" text-anchor="middle" font-size="12" font-weight="900" fill="${INK}" id="top">${a}</text><text x="-5" y="${H / 2 + 4}" text-anchor="end" font-size="12" font-weight="900" fill="${INK}">${a - b}</text></svg><button class="tile gr-go" data-slide>${T(B("Slide the strip", "পট্টীডাল সৰোৱা"))}</button><div class="wx-read df-read"></div>`;
  const strip = $("#strip", el), read = $(".df-read", el), gone = $("#gone", el), top = $("#top", el);
  const draw = () => {
    if (moved) { strip.setAttribute("x", A); strip.setAttribute("y", 0); strip.setAttribute("width", Bb); strip.setAttribute("height", H); } else { strip.setAttribute("x", 0); strip.setAttribute("y", H); strip.setAttribute("width", H); strip.setAttribute("height", Bb); }
    gone.setAttribute("opacity", moved ? 0 : 1); top.textContent = moved ? a + b : a; top.setAttribute("x", (moved ? A + Bb : A) / 2);
    read.innerHTML = moved ? `<b class="yes">$(${a} + ${b})(${a} - ${b}) = ${a + b} \\times ${a - b} = ${(a + b) * (a - b)}$</b>` : `$${a}^2 - ${b}^2 = ${a * a} - ${b * b} = ${a * a - b * b}$`;
  };
  el.addEventListener("click", (e) => { if (e.target.closest("[data-slide]") && !locked) { moved = !moved; touched = true; SFX.pair(); draw(); on(); } });
  draw();
  return { value: () => (a + b) * (a - b), touched: () => touched, freeze() { locked = true; }, show() { moved = true; draw(); }, state: () => ({ moved: moved ? 1 : 0 }), demo() { moved = true; touched = true; draw(); on(); } };
};

/* ---------- prime pairs: a perfect square is one where every prime has a partner ---------- */
W.pairs = (el, w, on) => {
  const g = w.group || 2, word = g === 3 ? B("group of three", "তিনিটাৰ গোট") : B("partner", "সংগী"), primes = []; { let v = w.n; for (let p = 2; p <= v; p++) while (v % p === 0) { primes.push(p); v /= p; } }
  const used = primes.map(() => false); let picks = [], touched = false, locked = false, made = [];
  const left = () => primes.filter((_, k) => !used[k]), count = (p) => left().filter((q) => q === p).length, canGroup = () => left().some((p) => count(p) >= g);
  // what is still needed: each unfinished prime up to the next full group
  const missing = () => [...new Set(left())].reduce((a, p) => a * p ** ((g - (count(p) % g)) % g), 1);
  const draw = () => {
    el.innerHTML = `<div class="pr-head">$${w.n}$</div><div class="pr-chips">${primes.map((p, k) => (used[k] ? "" : `<button class="tile ${picks.includes(k) ? "sel" : ""}" data-pr="${k}">$${p}$</button>`)).join("")}</div><div class="pr-made">${made.map((p) => `<span>$${Array(g).fill(p).join(" \\times ")}$</span>`).join("")}</div>
      <div class="wx-read pr-read">${canGroup() ? "" : left().length ? `<b class="no">${T(B(`No ${word.en}: ${left().join(", ")}`, `${word.as} নাই: ${left().join(", ")}`))}</b>` : `<b class="yes">${T(B(`Every prime has a ${word.en}`, `প্ৰতিটো মৌলিকৰ ${word.as} আছে`))}</b>`}</div>`;
  };
  el.addEventListener("click", (e) => {
    const b = e.target.closest("[data-pr]"); if (!b || locked) return;
    const k = +b.dataset.pr; touched = true;
    if (picks.includes(k)) { picks = picks.filter((x) => x !== k); SFX.tap(); draw(); return; }
    if (picks.length && primes[picks[0]] !== primes[k]) { picks = [k]; SFX.bad(); draw(); return; }
    picks.push(k);
    if (picks.length === g) { picks.forEach((x) => (used[x] = true)); made.push(primes[k]); picks = []; SFX.pair(); draw(); on(); return; }
    SFX.tap(); draw();
  });
  draw();
  const finish = () => { for (;;) { const p = left().find((q) => count(q) >= g); if (p == null) break; let n = 0; primes.forEach((q, k) => { if (q === p && !used[k] && n < g) { used[k] = true; n++; } }); made.push(p); } touched = true; draw(); on(); };
  return { value: missing, ready: () => !canGroup(), touched: () => touched, freeze() { locked = true; }, show: finish, state: () => ({ done: canGroup() ? 0 : 1 }), demo: finish };
};

/* ---------- price ladder: profit is on cost, discount is on marked price ---------- */
W.ladder = (el, w, on) => {
  let m = w.m ?? 0, d = w.d ?? 0, touched = false, locked = false; const top = 165, px = 300 / top;
  el.innerHTML = `<svg class="ldv" viewBox="0 0 340 128" role="img" aria-label="Cost, marked and selling price"><g id="ld"></g></svg><label class="sl"><span>${T(B("Mark up on cost", "ক্ৰয় মূল্যৰ ওপৰত বৃদ্ধি"))} <b id="lm"></b></span><input class="wx-range" id="im" type="range" min="0" max="60" step="5" value="${m}"></label><label class="sl"><span>${T(B("Discount on marked price", "চিহ্নিত মূল্যৰ ওপৰত ৰেহাই"))} <b id="ld2"></b></span><input class="wx-range" id="id" type="range" min="0" max="50" step="5" value="${d}"></label><div class="wx-read ld-read"></div>`;
  const sp = () => ((100 + m) * (100 - d)) / 100;
  const draw = () => {
    const rows = [[T(B("Cost", "ক্ৰয়")), 100, INK], [T(B("Marked", "চিহ্নিত")), 100 + m, GOLD], [T(B("Selling", "বিক্ৰী")), sp(), sp() >= 100 ? GREEN : RED]];
    const line = 100 * px + 40;
    $("#ld", el).innerHTML = rows.map(([, v, c], k) => `<rect x="40" y="${8 + k * 40}" width="${v * px}" height="30" rx="3" fill="${c}"/><text x="${40 + v * px - 6}" y="${28 + k * 40}" text-anchor="end" font-size="14" font-weight="900" fill="#fff">${short(v)}</text>`).join("") + `<path d="M${line} 2V124" stroke="${RED}" stroke-width="2" stroke-dasharray="5 4"/>`;
    const labels = ["C", "M", "S"]; $("#ld", el).insertAdjacentHTML("beforeend", labels.map((t, k) => `<text x="14" y="${28 + k * 40}" font-size="15" font-weight="900" fill="${INK}">${t}</text>`).join(""));
    $("#lm", el).textContent = `+${m}%`; $("#ld2", el).textContent = `−${d}%`;
    const p = sp() - 100;
    $(".ld-read", el).innerHTML = `<b class="${p > 0 ? "yes" : p < 0 ? "no" : ""}">${p > 0 ? T(B(`Profit ${short(p)}%`, `লাভ ${short(p)}%`)) : p < 0 ? T(B(`Loss ${short(-p)}%`, `লোকচান ${short(-p)}%`)) : T(B("No profit, no loss", "লাভো নাই, লোকচানো নাই"))}</b>`;
  };
  const change = () => { if (locked) return; m = +$("#im", el).value; d = +$("#id", el).value; touched = true; draw(); on(); };
  $("#im", el).addEventListener("input", change); $("#id", el).addEventListener("input", change); draw();
  return { value: () => sp() - 100, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ m, d }), demo(g) { m = g.m ?? m; d = g.d ?? d; $("#im", el).value = m; $("#id", el).value = d; touched = true; draw(); on(); } };
};

/* ---------- two sales at one price: the loss item cost more, so the pair always loses ---------- */
W.twosale = (el, w, on) => {
  const S = w.s || 100; let a = w.a ?? 0, touched = false, locked = false;
  el.innerHTML = `<svg class="ldv" viewBox="0 0 340 94" role="img" aria-label="Costs against sales"><g id="ts"></g></svg><label class="sl"><span>${T(B("Profit on one, loss on the other", "এটাত লাভ, আনটোত লোকচান"))} <b id="la"></b></span><input class="wx-range" id="ia" type="range" min="0" max="50" step="10" value="${a}"></label><div class="wx-read ts-read"></div>`;
  const draw = () => {
    const c1 = S / (1 + a / 100), c2 = S / (1 - a / 100), k = 320 / (S * 2.8), Y = 34;
    $("#ts", el).innerHTML = `<rect x="4" y="8" width="${c1 * k}" height="${Y - 8}" fill="${GREEN}"/><rect x="${4 + c1 * k}" y="8" width="${c2 * k}" height="${Y - 8}" fill="${RED}"/><text x="8" y="${Y - 8}" font-size="12" font-weight="900" fill="#fff">${short(c1)}</text><text x="${8 + c1 * k}" y="${Y - 8}" font-size="12" font-weight="900" fill="#fff">${short(c2)}</text>
      <rect x="4" y="${Y + 12}" width="${S * k}" height="26" fill="${BLUE}"/><rect x="${4 + S * k}" y="${Y + 12}" width="${S * k}" height="26" fill="#5B8FDA"/><text x="8" y="${Y + 30}" font-size="12" font-weight="900" fill="#fff">${S}</text><text x="${8 + S * k}" y="${Y + 30}" font-size="12" font-weight="900" fill="#fff">${S}</text><path d="M${4 + 2 * S * k} 2V${Y + 44}" stroke="${INK}" stroke-width="2"/>`;
    $("#la", el).textContent = `${a}%`;
    const cost = c1 + c2, loss = ((cost - 2 * S) / cost) * 100;
    $(".ts-read", el).innerHTML = `<b class="${a ? "no" : ""}">${a ? T(B(`Loss ${short(loss)}%`, `লোকচান ${short(loss)}%`)) : T(B("No profit, no loss", "লাভো নাই, লোকচানো নাই"))}</b>`;
  };
  $("#ia", el).addEventListener("input", () => { if (locked) return; a = +$("#ia", el).value; touched = true; SFX.tap(); draw(); on(); });
  draw();
  return { value: () => a, touched: () => touched, freeze() { locked = true; }, show() {}, state: () => ({ a }), demo(g) { a = g.a; $("#ia", el).value = a; touched = true; draw(); on(); } };
};
})();
