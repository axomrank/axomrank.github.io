/* =========================================================
   AxomRank maths layer, loaded before app/engine.js.
   - KaTeX typesetting: any $...$ in rendered text becomes formatted maths.
   - Steps: solve (typed answer on a keypad, with traps and hints),
     explore (reach a target on an interactive widget),
     stepwise (a worked problem, one decision at a time).
   - Widgets are shared by explore steps and playable story cards:
     fracbar, grid100, numline, peel, hops, blocks.
   - A step may carry `variants`: complete alternative versions with new numbers,
     generated and checked by scripts/build_math_course.py. A retry or a review shows a
     different variant under the same permanent step id. Nothing is computed from
     authored expressions in the browser.
   ========================================================= */
(() => {
"use strict";
const { B, T, N, asNum, SFX } = window.AXOM;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

/* ---------- typesetting ---------- */
function typesetText(node) {
  const parts = node.nodeValue.split(/(\$[^$\n]+\$)/);
  if (parts.length < 2) return;
  const out = document.createDocumentFragment();
  parts.forEach((p) => {
    if (p.length > 2 && p.startsWith("$") && p.endsWith("$")) {
      const box = document.createElement("span");
      box.className = "mx";
      window.katex.render(p.slice(1, -1), box, { throwOnError: false, output: "htmlAndMathml" });
      out.append(box);
    } else if (p) out.append(p);
  });
  node.replaceWith(out);
}
function typeset(root) {
  if (!window.katex) return;
  if (root.nodeType === 3) { if (root.nodeValue.includes("$") && root.parentElement && !root.parentElement.closest(".katex, script, style")) typesetText(root); return; }
  if (root.nodeType !== 1 || root.closest(".katex")) return;
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT), found = [];
  while (walker.nextNode()) if (walker.currentNode.nodeValue.includes("$") && !walker.currentNode.parentElement.closest(".katex, script, style")) found.push(walker.currentNode);
  found.forEach(typesetText);
}
new MutationObserver((list) => list.forEach((m) => m.addedNodes.forEach(typeset))).observe(document.body, { childList: true, subtree: true });

/* ---------- answers ---------- */
function toNumber(x) {
  const v = String(x).trim().replace(/−/g, "-").replace(/,/g, "");
  const frac = /^(-?\d*\.?\d+)\/(\d*\.?\d+)$/.exec(v);
  if (frac) return +frac[2] ? +frac[1] / +frac[2] : NaN;
  return /^-?\d*\.?\d+$/.test(v) ? +v : NaN;
}
const same = (a, b) => Math.abs(toNumber(a) - toNumber(b)) < 1e-9;
const compact = (x) => String(x).replace(/\s/g, "").replace(/−/g, "-");
const prettyAnswer = (x) => { const m = /^(-?\d+)\/(\d+)$/.exec(compact(x)); return m ? `$\\frac{${m[1]}}{${m[2]}}$` : `$${x}$`; };

/* ---------- widgets: mount(el, spec, onChange) returns { value, touched, freeze, show } ---------- */
const frac = (a, b) => `\\frac{${a}}{${b}}`;
const readout = (html) => `<div class="wx-read">${html}</div>`;
const round = (v) => +v.toFixed(4);
const WIDGETS = {
  // A bar cut into equal parts. Tap parts to shade; with split, change the number of parts.
  fracbar(el, w, on) {
    let n = w.n || 4, shaded = new Set(Array.from({ length: w.shade || 0 }, (_, k) => k)), locked = false, touched = false;
    const cells = (count, fill, cls = "") => `<div class="fbar ${cls}" style="--n:${count}">${Array.from({ length: count }, (_, k) => `<span class="${fill(k) ? "on" : ""}" ${cls ? "" : `data-cell="${k}"`}></span>`).join("")}</div>`;
    const draw = () => {
      el.innerHTML = `${w.ref ? cells(w.ref[1], (k) => k < w.ref[0], "ref") : ""}${cells(n, (k) => shaded.has(k))}
        ${w.split ? `<div class="wx-step"><button class="tile" data-less aria-label="Fewer parts">−</button><span>${T(B(`${n} equal parts`, `${asNum(n)}টা সমান ভাগ`))}</span><button class="tile" data-more aria-label="More parts">+</button></div>` : ""}
        ${readout(`$${frac(shaded.size, n)}${w.pct ? ` = ${round((shaded.size / n) * 100)}\\%` : ""}$`)}`;
    };
    el.addEventListener("click", (e) => {
      if (locked) return;
      const c = e.target.closest("[data-cell]");
      if (c) { const k = +c.dataset.cell; shaded.has(k) ? shaded.delete(k) : shaded.add(k); }
      else if (e.target.closest("[data-more]")) { if (n >= (w.max || 12)) return; n++; shaded = new Set([...shaded].filter((k) => k < n)); }
      else if (e.target.closest("[data-less]")) { if (n <= (w.min || 2)) return; n--; shaded = new Set([...shaded].filter((k) => k < n)); }
      else return;
      touched = true; SFX.tap(); draw(); on();
    });
    draw();
    return { value: () => shaded.size / n, parts: () => [shaded.size, n], touched: () => touched, freeze: () => { locked = true; }, show(v) { n = w.n || n; shaded = new Set(Array.from({ length: Math.round(v * n) }, (_, k) => k)); touched = true; draw(); } };
  },
  // Ten rows of ten. Tap or drag: everything up to that square is shaded.
  grid100(el, w, on) {
    let count = w.shade || 0, locked = false, touched = false;
    el.innerHTML = `<div class="g100">${Array.from({ length: 100 }, (_, k) => `<i data-k="${k + 1}"></i>`).join("")}</div><div class="wx-out"></div>`;
    const grid = $(".g100", el), out = $(".wx-out", el), squares = $$("i", grid);
    const draw = () => {
      squares.forEach((sq, k) => sq.classList.toggle("on", k < count));
      out.innerHTML = readout(`$${count}\\% = ${frac(count, 100)} = ${round(count / 100)}${w.of ? `\\quad\\Rightarrow\\quad ${count}\\%\\ \\text{of}\\ ${w.of} = ${round((count * w.of) / 100)}` : ""}$`);
    };
    const pick = (e) => {
      const hit = document.elementFromPoint(e.clientX, e.clientY);
      if (locked || !hit || !hit.dataset || !hit.dataset.k || hit.parentElement !== grid) return;
      if (count !== +hit.dataset.k) { count = +hit.dataset.k; touched = true; draw(); on(); }
    };
    grid.addEventListener("pointerdown", (e) => { grid.setPointerCapture(e.pointerId); pick(e); SFX.tap(); });
    grid.addEventListener("pointermove", (e) => { if (e.buttons || e.pressure) pick(e); });
    draw();
    return { value: () => count, touched: () => touched, freeze: () => { locked = true; }, show(v) { count = v; touched = true; draw(); } };
  },
  // A number line. den > 1 makes each notch 1/den and shows fractions.
  numline(el, w, on) {
    const den = w.den || 1, min = (w.min || 0) * den, max = w.max * den, marks = Math.min(max - min, 24);
    let k = w.start != null ? Math.round(w.start * den) : min, locked = false, touched = false;
    const label = (v) => (den > 1 && v % den ? frac(v, den) : String(v / den));
    el.innerHTML = `<div class="nline"><div class="nticks">${Array.from({ length: marks + 1 }, () => "<i></i>").join("")}</div>
      <input type="range" min="${min}" max="${max}" step="1" value="${k}" aria-label="Number line"><div class="nends"><span>$${w.min || 0}$</span><span>$${w.max}$</span></div></div><div class="wx-out"></div>`;
    const input = $("input", el), out = $(".wx-out", el);
    const draw = () => { out.innerHTML = readout(`$${label(k)}${den > 1 ? ` = ${round(k / den)}` : ""}$`); };
    input.addEventListener("input", () => { if (locked) return; k = +input.value; touched = true; draw(); on(); });
    draw();
    return { value: () => k / den, touched: () => touched, freeze: () => { locked = true; input.disabled = true; }, show(v) { k = Math.round(v * den); input.value = k; touched = true; draw(); } };
  },
  // Peel a number into primes: each good tap divides it, a tap that does not divide shakes.
  peel(el, w, on) {
    let left = w.n, stack = [], slips = 0, locked = false, touched = false;
    const draw = () => {
      el.innerHTML = `<div class="peel-num">${left === 1 ? "✓" : `$${left}$`}</div>
        <div class="wx-keys">${(w.primes || [2, 3, 5, 7]).map((p) => `<button class="tile" data-prime="${p}" ${left === 1 ? "disabled" : ""}>$${p}$</button>`).join("")}</div>
        ${readout(`$${w.n} = ${stack.length ? stack.join("\\times") : "?"}${left > 1 && stack.length ? `\\times ${left}` : ""}$`)}`;
    };
    el.addEventListener("click", (e) => {
      const b = e.target.closest("[data-prime]");
      if (!b || locked || left === 1) return;
      const p = +b.dataset.prime; touched = true;
      if (left % p === 0) { left /= p; stack.push(p); SFX.pair(); draw(); on(); }
      else { slips++; SFX.bad(); b.classList.remove("no"); void b.offsetWidth; b.classList.add("no"); }
    });
    draw();
    return { value: () => (left === 1 ? w.n : 0), ready: () => left === 1, slips: () => slips, touched: () => touched, freeze: () => { locked = true; }, show() { let v = w.n; stack = []; for (const p of w.primes || [2, 3, 5, 7]) while (v % p === 0) { stack.push(p); v /= p; } left = 1; touched = true; draw(); } };
  },
  // Numbers on a strip. Multiples (or factors) of a and b are marked; tap the one the question asks for.
  hops(el, w, on) {
    let pick = null, locked = false;
    const factors = w.mode === "factors", top = w.max || (factors ? Math.min(w.a, w.b) : 60);
    const has = (n, x) => (factors ? x % n === 0 : n % x === 0);
    // only: for questions. Mark one number's list and let the learner test it against the other,
    // because marking both would colour the answer before anyone has thought.
    const markA = !w.only || factors, markB = !w.only || !factors;
    const draw = () => {
      el.innerHTML = `<div class="hops">${Array.from({ length: top }, (_, i) => { const n = i + 1, a = markA && has(n, w.a), b = markB && has(n, w.b); return `<button class="hop ${a ? "a" : ""} ${b ? "b" : ""} ${pick === n ? "sel" : ""}" data-hop="${n}">${n}</button>`; }).join("")}</div>
        <div class="hop-key">${markA ? `<span class="a">$${w.a}$</span>` : ""}${markB ? `<span class="b">$${w.b}$</span>` : ""}${markA && markB ? `<span class="ab">${T(B("both", "দুয়োটা"))}</span>` : ""}</div>`;
    };
    el.addEventListener("click", (e) => { const b = e.target.closest("[data-hop]"); if (!b || locked) return; pick = +b.dataset.hop; SFX.tap(); draw(); on(); });
    draw();
    return { value: () => pick, touched: () => pick != null, freeze: () => { locked = true; }, show(v) { pick = v; draw(); } };
  },
  // Rows of equal blocks. Slide the worth of one block until the total fits.
  blocks(el, w, on) {
    const parts = w.parts, sum = parts.reduce((a, b) => a + b, 0);
    let u = w.min || 1, locked = false, touched = false;
    const rows = () => parts.map((p, r) => `<div class="brow"><small>${w.labels ? T(w.labels[r]) : ""}</small><span class="bset r${r}">${Array.from({ length: p }, (_, k) => `<i class="${w.take != null && k >= w.take ? "off" : ""}">${u}</i>`).join("")}</span></div>`).join("");
    el.innerHTML = `<div class="blocks"></div><input class="wx-range" type="range" min="${w.min || 1}" max="${w.max}" step="${w.step || 1}" value="${u}" aria-label="Worth of one block"><div class="wx-out"></div>`;
    const input = $("input", el), box = $(".blocks", el), out = $(".wx-out", el);
    const draw = () => {
      box.innerHTML = rows();
      out.innerHTML = readout(`$${sum}\\times ${u} = ${round(sum * u)}${w.total != null ? `\\;/\\;${w.total}` : ""}$`);
    };
    input.addEventListener("input", () => { if (locked) return; u = +input.value; touched = true; draw(); on(); });
    draw();
    return { value: () => u, touched: () => touched, freeze: () => { locked = true; input.disabled = true; }, show(v) { u = v; input.value = v; touched = true; draw(); } };
  },
};
function mount(el, spec, on = () => {}) {
  const make = WIDGETS[spec.kind];
  if (!make) { console.warn("Unknown widget", spec.kind); return null; }
  el.classList.add(`wx-${spec.kind}`);
  return make(el, spec, on);
}

/* ---------- the engine plugs in here ---------- */
function bind(ctx) {   // ctx: { U(), refresh(), check(), hintsAllowed() }
  const hintBar = (s) => (s.hints && s.hints.length && ctx.hintsAllowed() ? `<div class="hints" id="hints"></div><button class="chip-btn hint-btn" id="hint">${T(B("Need a hint?", "ইংগিত লাগে নেকি?"))}</button>` : "");
  const keypad = () => `<div class="kp">${["7", "8", "9", "⌫", "4", "5", "6", "/", "1", "2", "3", ".", "−", "0"].map((k) => `<button class="tile" data-key="${k}" aria-label="${k === "⌫" ? "Delete" : k}">${k}</button>`).join("")}</div>`;
  const RENDER = {
    solve: (s) => `<p class="prompt mprompt">${T(s.q)}</p>${hintBar(s)}
      <div class="ans-box" id="ans-box">${s.prefix ? `<span>${T(s.prefix)}</span>` : ""}<output id="ans" aria-live="polite"></output>${s.suffix ? `<span>${T(s.suffix)}</span>` : ""}</div>${keypad()}`,
    explore: (s) => `<p class="prompt mprompt">${T(s.q)}</p>${hintBar(s)}<div class="wx" id="wx"></div>`,
    stepwise: (s) => `<p class="prompt mprompt">${T(s.q)}</p><div class="parts" id="parts"></div>`,
  };
  function drawPart(s) {
    const st = ctx.U().st, box = $("#parts"), p = s.parts[st.part];
    box.innerHTML = s.parts.slice(0, st.part).map((x, k) => `<div class="pline ${st.slips.includes(k) ? "no" : "ok"}"><small>${T(x.ask)}</small><b>${T(x.options[x.answer])}</b>${st.slips.includes(k) ? `<span>${T(x.note)}</span>` : ""}</div>`).join("")
      + (p ? `<div class="pask"><small>${T(B(`Step ${st.part + 1} of ${s.parts.length}`, `${asNum(s.parts.length)}টাৰ ${asNum(st.part + 1)} নম্বৰ খোজ`))}</small><b>${T(p.ask)}</b></div><div class="opts">${p.options.map((o, k) => `<button class="tile opt" data-part="${k}"><span>${T(o)}</span></button>`).join("")}</div>` : "");
  }
  const SETUP = {
    solve: (s) => { ctx.U().st.typed = ""; },
    explore: (s) => { const st = ctx.U().st; st.w = mount($("#wx"), s.widget, () => ctx.refresh()); },
    stepwise: (s) => { const st = ctx.U().st; st.part = 0; st.slips = []; drawPart(s); },
    story: (s) => {
      const el = $("#screen .story-wx"); if (!el) return;
      const st = ctx.U().st;
      if (!s.tasks) { mount(el, s.widget); return; }
      st.task = 0; st.tasksDone = false;
      $("#screen").insertAdjacentHTML("beforeend", `<div class="tasks" id="tasks"></div>`);
      const drawTask = () => {
        const box = $("#tasks"), t = s.tasks[st.task];
        const pips = `<div class="pips">${s.tasks.map((_, k) => `<i class="${k < st.task ? "on" : ""}"></i>`).join("")}</div>`;
        box.querySelector(".task")?.remove(); box.querySelector(".pips")?.remove();
        box.insertAdjacentHTML("afterbegin", pips);
        if (t) box.querySelector(".pips").insertAdjacentHTML("afterend", `<div class="task"><span>${T(t.do)}</span><button data-showme>${T(B("Show me", "দেখুওৱা"))}</button></div>`);
        box.querySelector(".task")?.scrollIntoView({ block: "nearest" });
      };
      const check = () => {
        const t = s.tasks[st.task];
        if (!t || !goalMet(t.goal, st.w.state ? st.w.state() : { value: st.w.value() })) return;
        box_found(t); st.task++;
        if (st.task >= s.tasks.length) { st.tasksDone = true; SFX.good(); } else SFX.pair();
        drawTask(); ctx.refresh();
      };
      const box_found = (t) => { if (t.then) $("#tasks").insertAdjacentHTML("beforeend", `<div class="found">${T(t.then)}</div>`); };
      st.w = mount(el, s.widget, () => setTimeout(check, 0));
      st.showMe = () => { const t = s.tasks[st.task]; if (t) { if (st.w.demo) st.w.demo(t.goal); else st.w.show(t.goal.value); setTimeout(check, 750); } };
      drawTask();
    },
  };
  const ready = (s, st) => {
    if (s.type === "solve") return !!st.typed && !Number.isNaN(toNumber(st.typed));
    if (s.type === "explore") return st.w ? (st.w.ready ? st.w.ready() : st.w.touched()) : false;
    return false;   // a stepwise problem checks itself after its last step
  };
  function check(s, st) {
    if (s.type === "solve") {
      const right = s.exact ? compact(st.typed) === compact(s.answer) : same(st.typed, s.answer);
      $("#ans-box").classList.add(right ? "right" : "wrong");
      $$("[data-key]").forEach((k) => (k.disabled = true));
      return right;
    }
    if (s.type === "explore") {
      const v = st.w.value(), right = (st.w.slips ? st.w.slips() === 0 : true) && Math.abs(v - s.target) < 1e-9;
      st.w.freeze();
      if (!right && !st.w.slips) st.w.show(s.target);
      return right;
    }
    return st.slips.length === 0;
  }
  const answerHTML = (s) => (s.type === "solve" ? prettyAnswer(s.answer) : "");
  // The pattern behind a wrong answer, when the author predicted it.
  function trap(s, st) {
    if (s.slipTrap && st.w && st.w.slips && st.w.slips() > 0) return s.slipTrap;   // the wrong step, not the final value, shows the mistake
    if (!s.traps) return null;
    if (s.type === "solve") return s.traps.find((x) => compact(x.ans) === compact(st.typed)) || s.traps.find((x) => same(x.ans, st.typed)) || null;
    if (s.type === "explore") { const v = st.w.value(); return s.traps.find((x) => Math.abs(x.val - v) < 1e-9) || null; }
    return s.traps.find((x) => x.opt === st.sel) || null;
  }
  // Every piece of evidence one answer gives: a stepwise problem reports each of its steps.
  function outcomes(s, st, right) {
    const typed = s.type === "solve", hinted = !!st.hinted;
    if (s.type === "stepwise") return s.parts.map((p, k) => ({ skill: p.skill || s.skill, right: !st.slips.includes(k), hinted, typed: false, tag: st.slips.includes(k) ? p.tag : null }));
    const t = right ? null : trap(s, st);
    return [{ skill: s.skill, right, hinted, typed, tag: t ? t.tag : null, trap: t }];
  }
  const coach = (t) => `<div class="coach"><b>${T(B("What happened", "কি হ'ল"))}</b><span>${T(t.why)}</span></div>`;
  document.addEventListener("click", (e) => {
    const U = ctx.U();
    if (!U || U.phase !== "answer" || !$("#v-play").classList.contains("on")) return;
    const s = U.queue[U.pos].s, st = U.st;
    if (e.target.closest("[data-showme]")) { if (st.showMe) st.showMe(); return; }
    if (e.target.closest("#hint")) {
      const n = st.hintsShown || 0; st.hintsShown = n + 1; st.hinted = true;
      $("#hints").insertAdjacentHTML("beforeend", `<div class="hint"><span class="n">${N(n + 1)}</span><span>${T(s.hints[n])}</span></div>`);
      if (st.hintsShown >= s.hints.length) e.target.closest("#hint").remove();
      SFX.tap(); return;
    }
    const key = e.target.closest("[data-key]");
    if (key && s.type === "solve") return press(key.dataset.key);
    const part = e.target.closest("[data-part]");
    if (part && s.type === "stepwise") {
      const p = s.parts[st.part], k = +part.dataset.part;
      if (k !== p.answer) { st.slips.push(st.part); SFX.bad(); } else SFX.pair();
      st.part++; drawPart(s);
      if (st.part === s.parts.length) ctx.check();
    }
  });
  function press(k) {
    const st = ctx.U().st;
    if (k === "⌫" || k === "Backspace") st.typed = st.typed.slice(0, -1);
    else if (k === "−" || k === "-") { if (!st.typed) st.typed = "−"; else return; }
    else if (st.typed.length >= 12) return;
    else st.typed += k;
    $("#ans").textContent = st.typed; SFX.tap(); ctx.refresh();
  }
  document.addEventListener("keydown", (e) => {
    const U = ctx.U();
    if (!U || U.phase !== "answer" || !$("#v-play").classList.contains("on") || U.queue[U.pos].s.type !== "solve" || $("#sheet-root").innerHTML) return;
    if (/^[0-9./-]$/.test(e.key) || e.key === "Backspace") { e.preventDefault(); press(e.key); }
  });
  return { RENDER, SETUP, ready, check, answerHTML, outcomes, coach };
}

// A goal like { value: -3 } or { span: { lt: 0.1 } } is met by a scene's state().
function goalMet(goal, state) {
  return Object.entries(goal).every(([k, want]) => {
    const v = state[k];
    if (typeof want === "number") return Math.abs(v - want) < 1e-6;
    return (want.lt == null || v < want.lt) && (want.gt == null || v > want.gt) && (want.near == null || Math.abs(v - want.near) < (want.tol ?? 1e-6));
  });
}
// Test hook: complete a do-to-discover card.
function finishTasks(st) { st.tasksDone = true; }
/* A new version of the same step: fresh numbers on every showing, never the one just seen. */
function vary(s) {
  if (!s.variants || !s.variants.length) return s;
  const options = s.variants.map((_, k) => k).filter((k) => k !== s._v), k = options[Math.floor(Math.random() * options.length)];
  return { ...s, ...s.variants[k], _v: k };
}
// After a missed probe, drop later probes that depend on the failed skill: they would only measure the same gap.
function prune(U, failed, map) {
  const dependsOn = (id, seen = new Set()) => !!map[id] && !seen.has(id) && (seen.add(id), (map[id].pre || []).some((p) => p === failed || dependsOn(p, seen)));
  const keep = U.queue.filter((it, k) => k <= U.pos || !dependsOn(it.s.skill));
  U.total -= U.queue.length - keep.length;
  U.queue = keep;
}
const STATE = { new: B("Not tested", "পৰীক্ষা হোৱা নাই"), weak: B("Weak", "দুৰ্বল"), learning: B("Learning", "শিকি আছে"), ready: B("Ready", "সাজু"), strong: B("Strong", "দৃঢ়"), rusty: B("Rusty", "পাহৰিছে") };
function report(skills) {
  const rows = skills.map((x) => ({ x, st: AXOM.skillState(x.id) }));
  const weak = rows.filter((r) => r.st === "weak"), good = rows.filter((r) => ["ready", "strong", "learning"].includes(r.st)), open = rows.filter((r) => r.st === "new");
  const chips = (list) => list.map((r) => `<span class="sk-chip ${r.st}">${T(r.x.t)}</span>`).join("");
  return `${weak.length ? `<div class="card"><h3>${T(B("Build these first", "প্ৰথমে এইবোৰ গঢ়া"))}</h3><div class="sk-chips">${chips(weak)}</div></div>` : ""}
    ${good.length ? `<div class="card"><h3>${T(B("Looking good", "ভাল হৈছে"))}</h3><div class="sk-chips">${chips(good)}</div></div>` : ""}
    ${open.length ? `<div class="card"><h3>${T(B("Not tested yet", "এতিয়াও পৰীক্ষা হোৱা নাই"))}</h3><div class="sk-chips">${chips(open)}</div></div>` : ""}
    <p class="sub" style="font-size:13px">${T(B("One round is a first estimate, not a verdict. Your map updates with every question.", "এটা পৰ্যায় কেৱল প্ৰথম অনুমান, চূড়ান্ত ৰায় নহয়। প্ৰতিটো প্ৰশ্নৰ লগে লগে মানচিত্ৰ সলনি হয়।"))}</p>`;
}
// Test hook for scripts/autoplay.js: answer a widget without gestures.
const autoSet = (s, st, wrong) => { st.w.show(wrong ? (s.traps && s.traps[0] ? s.traps[0].val : s.target + 1) : s.target); };

window.AXOM_MATH = { bind, vary, prune, report, mount, typeset, STATE, toNumber, same, autoSet, widgets: WIDGETS, finishTasks };
})();
