/* =========================================================
   Geography figures: drawn teaching scenes with numbered pins.
   A story step's `figure: {kind, spots}` explores one; a `figtap`
   step asks the learner to tap the right pin. Every scene is a
   schematic, never a measured map. spots[k] belongs to pins[k].
   ========================================================= */
(() => {
const B = (en, as) => ({ en, as });
// Shared paint: gradients, shadows and texture, injected once per page and reused by every figure.
const DEFS = `<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<linearGradient id="gf-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe7f3"/><stop offset="1" stop-color="#f6fbfd"/></linearGradient>
<linearGradient id="gf-night" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f2233"/><stop offset="1" stop-color="#26445e"/></linearGradient>
<linearGradient id="gf-sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6fb9d6"/><stop offset="1" stop-color="#22698f"/></linearGradient>
<radialGradient id="gf-ocean" cx=".45" cy=".4" r=".8"><stop offset="0" stop-color="#8fcde3"/><stop offset="1" stop-color="#3a86ad"/></radialGradient>
<linearGradient id="gf-land" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eee3bd"/><stop offset="1" stop-color="#cdbb8b"/></linearGradient>
<linearGradient id="gf-grass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9d78c"/><stop offset="1" stop-color="#76a65d"/></linearGradient>
<linearGradient id="gf-rock" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#b79c7c"/><stop offset="1" stop-color="#7c6550"/></linearGradient>
<linearGradient id="gf-rock2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d2bf9f"/><stop offset="1" stop-color="#9c8566"/></linearGradient>
<linearGradient id="gf-sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7e3a8"/><stop offset="1" stop-color="#ddb86c"/></linearGradient>
<linearGradient id="gf-snow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d9ecf5"/></linearGradient>
<linearGradient id="gf-alluv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe39a"/><stop offset="1" stop-color="#95bb5e"/></linearGradient>
<linearGradient id="gf-paper" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fffaf0"/><stop offset="1" stop-color="#f3ead6"/></linearGradient>
<radialGradient id="gf-sun" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#fff3b0"/><stop offset=".55" stop-color="#ffc23d"/><stop offset="1" stop-color="#f08a24"/></radialGradient>
<radialGradient id="gf-glow"><stop offset="0" stop-color="#ffd76a" stop-opacity=".75"/><stop offset="1" stop-color="#ffd76a" stop-opacity="0"/></radialGradient>
<radialGradient id="gf-core" cx=".45" cy=".4"><stop offset="0" stop-color="#fff0a0"/><stop offset="1" stop-color="#f29a2e"/></radialGradient>
<linearGradient id="gf-mantle" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e9874a"/><stop offset="1" stop-color="#b8441f"/></linearGradient>
<filter id="gf-shadow" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="2" stdDeviation="2.2" flood-color="#17313b" flood-opacity=".22"/></filter>
<filter id="gf-soft"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="gf-grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .3  0 0 0 0 .25  0 0 0 0 .2  0 0 0 .06 0"/></filter>
</defs></svg>`;
const inject = () => { if (!document.getElementById("gf-sky") && document.body) document.body.insertAdjacentHTML("afterbegin", DEFS); };
if (document.body) inject(); else document.addEventListener("DOMContentLoaded", inject);

const INDIA = "M179.9 177.0 173.9 184.3 156.5 196.5 156.6 201.1 147.0 202.9 144.1 208.7 139.2 207.8 135.7 210.7 137.7 232.4 132.2 247.2 133.2 261.2 127.7 261.5 123.8 269.0 126.6 270.9 117.2 273.1 115.8 279.6 108.6 282.0 101.3 274.6 94.3 252.8 84.7 236.8 80.9 219.6 77.7 217.9 79.2 217.2 76.0 215.2 76.2 211.8 71.6 205.9 63.8 169.4 66.1 162.5 63.4 152.8 65.6 152.0 62.8 152.0 62.4 149.0 66.4 146.1 61.1 145.2 58.7 156.5 46.3 161.4 28.4 146.5 29.4 144.2 31.0 146.3 40.0 143.5 43.1 138.5 35.6 141.8 25.5 137.7 23.8 133.9 26.5 126.8 38.6 128.0 49.1 125.8 44.7 113.2 39.4 111.0 40.1 105.1 33.7 103.2 34.4 99.1 42.0 91.1 46.9 94.0 56.6 91.6 61.3 83.8 66.7 81.3 71.0 72.6 76.5 70.2 76.2 67.3 83.5 61.7 81.8 61.1 82.7 53.9 90.0 50.5 83.4 48.2 83.5 44.8 73.2 42.3 71.0 30.0 78.1 22.9 68.2 15.6 62.7 15.2 63.3 11.9 68.0 7.7 75.7 7.7 73.8 5.6 89.6 4.3 103.8 15.9 109.0 17.1 109.3 19.4 115.0 19.6 126.9 14.6 134.4 16.0 137.5 19.5 135.1 26.7 129.7 29.0 128.9 33.4 123.9 33.8 125.8 37.3 124.0 37.1 124.4 39.5 129.1 40.7 128.0 43.1 130.8 45.7 127.9 47.1 124.7 49.6 122.6 46.1 119.0 47.8 122.8 52.8 122.8 58.6 126.2 58.2 128.9 62.1 144.3 69.6 138.0 74.4 135.1 83.2 152.6 92.6 160.5 93.8 160.7 96.0 178.8 97.6 179.0 100.3 184.4 103.1 188.5 102.0 190.6 104.9 211.4 107.0 212.6 91.6 217.2 89.9 219.8 92.6 218.5 99.4 222.1 102.6 250.2 102.3 250.8 98.0 246.3 96.2 245.3 92.6 255.0 92.9 262.5 85.1 268.1 84.8 274.9 78.3 282.7 81.3 288.9 77.2 291.8 79.2 289.6 82.5 293.1 80.9 293.9 83.8 290.6 87.3 301.4 89.4 301.3 92.3 296.6 94.9 299.0 99.9 294.8 97.2 290.2 98.1 279.9 104.5 280.2 109.7 275.0 116.2 275.7 120.6 270.3 131.1 262.5 128.6 263.0 137.9 260.5 138.8 261.2 146.3 258.3 149.3 256.5 147.4 255.5 149.0 252.3 132.3 249.2 132.2 246.0 139.7 241.6 133.4 243.7 128.6 248.7 128.3 251.3 125.5 253.8 119.7 228.8 117.2 227.5 108.3 224.2 110.3 221.7 106.6 217.7 107.9 215.1 104.4 216.3 107.0 212.3 112.4 220.9 117.4 215.5 118.0 211.3 123.2 218.3 127.0 216.6 133.0 218.9 134.4 218.2 136.8 220.8 137.1 220.4 142.9 217.7 143.5 220.4 146.6 217.6 145.5 217.0 149.6 213.8 151.4 210.1 144.6 213.0 147.8 201.1 155.0 201.4 160.4 199.6 160.8 202.1 161.1 199.5 164.9 180.0 177.1Z";
const lx = (lon) => +((lon - 66) * 9.6).toFixed(1), ly = (lat) => +((37.5 - lat) * 9.6).toFixed(1);
const G = (k, s) => `<g data-part="${k}">${s}</g>`;
const P = (d, c = "") => `<path class="${c}" d="${d}"/>`;
const C = (x, y, r, c = "") => `<circle class="${c}" cx="${x}" cy="${y}" r="${r}"/>`;
const R = (x, y, w, h, c = "", rx = 0) => `<rect class="${c}" x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}"/>`;
const TX = (x, y, en, as, c = "", anchor = "middle") => `<text class="gf-t ${c}" x="${x}" y="${y}" text-anchor="${anchor}"><tspan class="en">${en}</tspan><tspan class="as">${as}</tspan></text>`;
const AR = (x1, y1, x2, y2, c = "") => {   // an arrow with a head drawn in place
  const a = Math.atan2(y2 - y1, x2 - x1), h = 8, f = (d) => `${(x2 - h * Math.cos(a + d)).toFixed(1)} ${(y2 - h * Math.sin(a + d)).toFixed(1)}`;
  return `<path class="gf-ar ${c}" d="M${x1} ${y1} L${x2} ${y2}"/><path class="gf-ah ${c}" d="M${x2} ${y2} L${f(0.45)} L${f(-0.45)}Z"/>`;
};
const CURVE = (d, c = "") => `<path class="gf-ar flow ${c}" d="${d}"/>`;
const SKY = R(0, 0, 320, 190, "sky");
const SEA = (y) => R(0, y, 320, 190 - y, "water");
const DROPS = (xs, y0, y1) => xs.map((x, k) => `<path class="drop" style="animation-delay:${(k * 0.23).toFixed(2)}s" d="M${x} ${y0} v${y1 - y0}"/>`).join("");
const SUN = (x, y, r = 16) => `<g class="sun">${C(x, y, r, "sunc")}</g>`;
const ind = (lon, lat) => [lx(lon), ly(lat)];
const IN = (s) => INX(s);
const line = (pts, c) => P("M" + pts.map(([lon, lat]) => `${lx(lon)} ${ly(lat)}`).join(" L"), c);
const blob = (pts, c) => P("M" + pts.map(([lon, lat]) => `${lx(lon)} ${ly(lat)}`).join(" L") + "Z", c);
const IPIN = (...ll) => ll.map(([lon, lat]) => ind(lon, lat));
const TEETH = (pts) => pts.map(([lon, lat]) => { const [x, y] = ind(lon, lat); return `<path class="peak" d="M${x - 7} ${y + 5} L${x} ${y - 7} L${x + 7} ${y + 5}Z"/>`; }).join("");
const BAR = (x, base, w, h, c) => R(x, base - h, w, h, `grow ${c}`, 3);

// ---------- Scene kit: richer illustration pieces shared by the redrawn figures ----------
const r1 = (n) => +n.toFixed(1);
const CLOUD = (x, y, s = 1, o = 1) => `<g class="cloud" opacity="${o}" transform="translate(${x} ${y}) scale(${s})"><path fill="#fff" d="M-26 8 a12 12 0 0 1 4-20 a16 16 0 0 1 29-6 a13 13 0 0 1 21 9 a10 10 0 0 1 -2 17Z"/></g>`;
const HAZE = (y, c = "#9fc3d3", o = .55) => `<path fill="${c}" opacity="${o}" d="M0 ${y} Q40 ${y - 22} 80 ${y - 8} T160 ${y - 14} T240 ${y - 6} T320 ${y - 18} V190 H0Z"/>`;
const MTN = (peaks, base = 190, snow = true) => peaks.map(([x, h, w]) => { const t = base - h; return `<path fill="url(#gf-rock2)" d="M${x - w} ${base} L${x} ${t} L${x + w} ${base}Z"/><path fill="#7c6550" opacity=".55" d="M${x} ${t} L${x + w} ${base} L${r1(x + w * .15)} ${base}Z"/>` + (snow && h > 70 ? `<path fill="url(#gf-snow)" d="M${x} ${t} L${r1(x + w * .28)} ${r1(t + h * .28)} L${r1(x + w * .1)} ${r1(t + h * .22)} L${r1(x - w * .05)} ${r1(t + h * .3)} L${r1(x - w * .28)} ${r1(t + h * .28)}Z"/>` : ""); }).join("");
const TREE = (x, y, s = 1, c = "#3f8c55") => `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-1.5" y="-4" width="3" height="8" fill="#6b4f35"/><circle cy="-9" r="7" fill="${c}"/><circle cx="-3" cy="-11" r="3" fill="#fff" opacity=".18"/></g>`;
const PINE = (x, y, s = 1) => `<g transform="translate(${x} ${y}) scale(${s})"><path fill="#2f6e48" d="M0 -18 L7 -4 H-7Z M0 -12 L8 2 H-8Z"/><rect x="-1.2" y="2" width="2.4" height="4" fill="#5d4330"/></g>`;
const FOREST = (x0, x1, y, n, s = 1, pine) => Array.from({ length: n }, (_, k) => { const x = x0 + ((x1 - x0) * (k + .5)) / n, yy = y + ((k * 37) % 7) - 3; return pine ? PINE(r1(x), yy, s) : TREE(r1(x), yy, s * (.8 + ((k * 13) % 5) / 10), k % 3 ? "#3f8c55" : "#5aa267"); }).join("");
const HOUSE = (x, y, s = 1, roof = "#c8553d") => `<g transform="translate(${x} ${y}) scale(${s})" filter="url(#gf-shadow)"><rect x="-7" y="-9" width="14" height="10" fill="#fffaf0" stroke="#17313b" stroke-width=".6"/><path fill="${roof}" d="M-9 -8 L0 -16 L9 -8Z"/><rect x="-2" y="-5" width="4" height="6" fill="#17313b" opacity=".7"/></g>`;
const FOAM = (y, x0 = 0, x1 = 320, a = 4) => { let d = `M${x0} ${y}`; for (let x = x0; x < x1; x += 20) d += ` q5 ${-a} 10 0 t10 0`; return `<path d="${d}" stroke="#fff" stroke-width="1.6" fill="none" opacity=".75"/>`; };
const SEAFILL = (y) => `<rect x="0" y="${y}" width="320" height="${190 - y}" fill="url(#gf-sea)"/>` + FOAM(y + 8, 0, 320, 2) + FOAM(y + 22, 10, 320, 2);
const STRATA = (x, y, w, h, cols) => cols.map((c, k) => `<rect x="${x}" y="${r1(y + (h / cols.length) * k)}" width="${w}" height="${r1(h / cols.length + .5)}" fill="${c}"/>`).join("");
const LBL = (x, y, en, as, anchor = "middle", cls = "") => TX(x, y, en, as, cls, anchor);
const RAYS = (x, y, r = 20) => `<g stroke="#f5b73c" stroke-width="2" stroke-linecap="round" opacity=".8">${Array.from({ length: 10 }, (_, k) => { const a = (k * Math.PI) / 5; return `<path d="M${r1(x + Math.cos(a) * (r + 4))} ${r1(y + Math.sin(a) * (r + 4))} L${r1(x + Math.cos(a) * (r + 10))} ${r1(y + Math.sin(a) * (r + 10))}"/>`; }).join("")}</g>`;
const SUNR = (x, y, r = 16) => `<circle cx="${x}" cy="${y}" r="${r * 2.4}" fill="url(#gf-glow)"/>${RAYS(x, y, r)}<circle cx="${x}" cy="${y}" r="${r}" fill="url(#gf-sun)"/>`;
const BIRDS = (x, y) => `<path d="M${x} ${y} q4 -4 8 0 q4 -4 8 0 M${x + 22} ${y - 8} q3 -3 6 0 q3 -3 6 0" stroke="#17313b" stroke-width="1.2" fill="none" opacity=".55"/>`;
const SKYBG = (h = 190) => `<rect width="320" height="${h}" fill="url(#gf-sky)"/>`;
const GROUND = (d, fill = "url(#gf-grass)") => `<path fill="${fill}" filter="url(#gf-shadow)" d="${d}"/>`;
// India base with graticule, sea names and a soft coast glow
const INX = (s) => `<rect width="320" height="300" fill="url(#gf-ocean)"/>` + [10, 20, 30].map((la) => `<path d="M0 ${ly(la)} H320" stroke="#fff" stroke-opacity=".22" stroke-dasharray="3 5"/>`).join("") + [70, 80, 90].map((lo) => `<path d="M${lx(lo)} 0 V300" stroke="#fff" stroke-opacity=".22" stroke-dasharray="3 5"/>`).join("")
  + `<path d="${INDIA}" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="6" filter="url(#gf-soft)"/><path class="land" d="${INDIA}"/>`
  + `<text class="gf-sea" x="${lx(68.6)}" y="${ly(15)}">ARABIAN SEA</text><text class="gf-sea" x="${lx(88.6)}" y="${ly(15.5)}">BAY OF BENGAL</text>` + s;

const F = {
  // Mission 1: map skills
  compass: { pins: [[66, 48], [232, 150]], art: R(0, 0, 320, 190, "paper") + G(0, C(66, 95, 38, "ring") + `<path class="needle spin-slow" d="M66 62 L74 95 L58 95Z"/><path class="needle2" d="M66 128 L74 95 L58 95Z"/>` + TX(66, 54, "N", "উ", "bold")) + G(1, R(150, 40, 150, 122, "card", 8) + C(170, 66, 6, "water") + TX(186, 70, "Lake", "হ্ৰদ", "", "start") + P("M162 96 h20", "road") + TX(190, 100, "Road", "পথ", "", "start") + `<path class="peak" d="M163 132 l8 -12 l8 12Z"/>` + TX(186, 130, "Hill", "পাহাৰ", "", "start")) },
  graticule: { pins: [[300, 95], [160, 20]], art: C(160, 95, 86, "water") + `<g class="grid"><ellipse cx="160" cy="95" rx="86" ry="30"/><ellipse cx="160" cy="95" rx="86" ry="60"/><ellipse cx="160" cy="95" rx="30" ry="86"/><ellipse cx="160" cy="95" rx="60" ry="86"/></g>` + G(0, P("M40 95 H300", "hi")) + G(1, P("M160 9 V181", "hi2")) + TX(50, 88, "0°", "০°", "bold") + TX(172, 176, "0°", "০°", "bold") },
  scalebar: { pins: [[86, 150], [190, 150]], art: R(0, 0, 320, 190, "paper") + P("M30 70 C90 20 150 110 210 56 S290 60 300 40", "road") + C(30, 70, 6, "accent") + C(300, 40, 6, "accent") + G(0, TX(70, 134, "km", "কি.মি.", "bold")) + G(1, R(50, 158, 60, 10, "ink") + R(110, 158, 60, 10, "paper2") + R(170, 158, 60, 10, "ink") + R(230, 158, 60, 10, "paper2")) + ["0", "5", "10", "15", "20"].map((v, k) => `<text class="gf-t" x="${50 + k * 60}" y="152" text-anchor="middle">${v}</text>`).join("") },
  contour: { pins: [[92, 66], [236, 66]], art: R(0, 0, 320, 190, "paper") + `<g class="ctr"><ellipse cx="108" cy="72" rx="86" ry="52"/><ellipse cx="102" cy="72" rx="58" ry="40"/></g>` + G(0, `<g class="ctr hic">${[0, 1, 2, 3, 4].map((k) => `<ellipse cx="${74 - k * 0}" cy="72" rx="${28 - k * 3}" ry="${28 - k * 4}"/>`).join("")}</g>`) + G(1, P("M196 26 C226 60 240 90 250 120", "hi2")) + P("M16 182 L46 150 L72 136 L100 132 L180 172 L304 182Z", "rock") + P("M16 138 H304", "dash") },

  // Mission 2: moving Earth
  daynight: { pins: [[220, 95], [108, 95]], art: R(0, 0, 320, 190, "night") + SUN(296, 95, 20) + DROPS([], 0, 0) + [40, 60, 80].map((y) => AR(270, y + 35, 240, y + 35, "sunray")).join("") + G(0, `<path class="dayc" d="M164 25 A70 70 0 0 1 164 165Z"/>`) + G(1, `<path class="nightc" d="M164 25 A70 70 0 0 0 164 165Z"/>`) + CURVE("M100 180 C130 192 200 192 230 180", "spin-note") },
  sunangle: { pins: [[226, 52], [100, 50]], art: R(0, 0, 320, 190, "night") + SUN(30, 95, 22) + `<g transform="rotate(23.5 214 95)">` + C(214, 95, 66, "water") + P("M214 16 V174", "dash") + G(0, P("M214 95 m-62 -22 a66 66 0 0 1 124 0Z", "hotcap")) + P("M214 95 m-62 22 a66 66 0 0 0 124 0Z", "coolcap") + `</g>` + G(1, AR(56, 66, 150, 72, "sunray")) + AR(56, 124, 150, 116, "sunray") },
  earthlayers: { pins: [[160, 20], [160, 56], [160, 112]], art: R(0, 0, 320, 190, "paper") + G(0, C(160, 200, 186, "crust")) + G(1, C(160, 200, 176, "mantle")) + G(2, C(160, 200, 96, "core")) + `<g class="heat">${[100, 160, 220].map((x, k) => CURVE(`M${x} 96 C${x - 16} 70 ${x + 16} 50 ${x} 34`, "warm d" + k)).join("")}</g>` },
  boundaries: { pins: [[54, 92], [160, 76], [266, 92]], art: SKY + P("M0 112 H320 V190 H0Z", "mantle") + G(0, P("M6 112 H48 V132 H6Z M60 112 H104 V132 H60Z", "crust") + AR(38, 150, 8, 150, "warm") + AR(68, 150, 98, 150, "warm") + P("M54 112 L46 132 H62Z", "melt")) + G(1, P("M112 112 L156 112 L170 86 L184 112 L208 112 V132 H112Z", "crust") + AR(116, 150, 146, 150, "warm") + AR(204, 150, 174, 150, "warm")) + G(2, P("M216 112 H314 V132 H216Z", "crust") + P("M265 104 V140", "fault") + AR(248, 98, 222, 98, "warm") + AR(282, 146, 308, 146, "warm")) },

  // Mission 3: landforms
  rockcycle: { pins: [[62, 120], [160, 56], [262, 120]], art: R(0, 0, 320, 190, "paper") + G(0, C(62, 124, 44, "melt") + `<g class="dots">${[[46, 112], [66, 136], [82, 112], [54, 138]].map(([x, y]) => C(x, y, 3.5, "ink")).join("")}</g>`) + G(1, `${[34, 48, 62, 76].map((y, k) => R(114, y, 92, 12, k % 2 ? "sand" : "rock2", 2)).join("")}`) + G(2, `${[0, 1, 2].map((k) => P(`M222 ${106 + k * 15} q20 -14 40 0 t40 0`, "fold")).join("")}`) + CURVE("M92 88 C100 66 104 60 112 56") + CURVE("M210 60 C230 62 246 76 256 92") + CURVE("M226 160 C190 186 130 186 96 160") },
  grainpath: { pins: [[58, 54], [170, 100], [288, 148]], art: SKY + `<path class="rock" d="M0 190 V50 L60 30 L120 96 L200 128 L320 150 V190Z"/>` + P("M34 62 C70 70 90 104 130 112 S240 140 320 160", "river") + G(0, C(58, 58, 8, "crack") + P("M50 50 l8 6 l-3 8 l9 6", "fault")) + G(1, C(170, 118, 4, "sandd grain")) + G(2, P("M232 172 Q280 148 320 160 V190 H232Z", "sand")) },
  meander: { pins: [[240, 50], [104, 66]], art: R(0, 0, 320, 190, "grass") + `<path class="riverw" d="M-4 30 C110 -20 250 10 260 66 S160 110 126 92 S40 96 70 160 S240 200 330 150"/>` + `<path class="river-flow" d="M-4 30 C110 -20 250 10 260 66 S160 110 126 92 S40 96 70 160 S240 200 330 150"/>` + G(0, P("M250 28 q22 30 4 62", "hi")) + G(1, P("M104 42 q90 -6 112 22 q-40 -2 -112 -22Z", "sand")) },
  threeprofiles: { pins: [[54, 50], [160, 66], [270, 50]], art: SKY + G(0, `<path class="ice" d="M4 40 C26 136 86 136 108 40Z"/><path class="rock" d="M4 40 C26 136 86 136 108 40 L108 190 H4Z"/>`) + G(1, R(114, 138, 92, 52, "sand") + P("M114 138 C136 138 140 86 164 86 C172 86 192 134 206 138Z", "sand") + AR(118, 76, 150, 76, "wind")) + G(2, P("M214 190 V46 H266 L272 150 H316 V190Z", "rock") + R(272, 150, 48, 40, "water") + `<path class="wave" d="M316 142 q-10 -8 -20 0 t-20 0"/>`) },

  // Mission 4: air and water
  climategraph: { pins: [[150, 104], [224, 40]], art: R(0, 0, 320, 190, "paper") + P("M34 18 V160 H304", "axis") + G(0, P("M36 112 C100 90 200 92 302 108", "hi2")) + G(1, P("M36 126 L70 106 L100 120 L134 98 L180 112 L214 112 L226 34 L240 112 L272 96 L302 120", "spark")) + TX(170, 180, "Time →", "সময় →") },
  seabreeze: { pins: [[92, 92], [248, 138]], art: SKY + SUN(280, 28) + SEA(150).replace('x="0"', 'x="170"').replace('width="320"', 'width="150"') + P("M0 190 V146 L170 150 V190Z", "land") + G(0, [62, 92, 122].map((x, k) => CURVE(`M${x} 138 C${x - 14} 110 ${x + 14} 90 ${x} 58`, "warm d" + k)).join("")) + G(1, AR(248, 138, 150, 138, "cool") + AR(150, 56, 240, 56, "cool2") + CURVE("M248 62 C256 90 256 110 252 130", "cool")) },
  pressure: { pins: [[80, 96], [244, 96]], art: R(0, 0, 320, 190, "paper") + G(0, [66, 46, 26].map((r) => C(80, 96, r, "iso")).join("") + TX(80, 101, "H", "H", "big")) + G(1, [66, 46, 26].map((r) => C(244, 96, r, "iso")).join("") + TX(244, 101, "L", "L", "big")) + AR(112, 76, 200, 76, "cool") + AR(112, 96, 208, 96, "cool") + AR(112, 116, 200, 116, "cool") },
  infiltrate: { pins: [[120, 142], [224, 64]], art: SKY + P("M0 60 Q160 20 320 104 V190 H0Z", "soil") + P("M0 60 Q160 20 320 104", "turf") + DROPS([40, 90, 140, 190, 240], 2, 28) + G(0, [66, 104, 148].map((x, k) => `<path class="soak d${k}" d="M${x} 56 V150"/>`).join("") ) + G(1, CURVE("M170 46 C214 54 260 74 304 100", "cool")) + R(0, 160, 320, 30, "water") },
  ridge: { pins: [[92, 96], [232, 110]], art: SKY + P("M0 190 V164 L90 150 L160 52 L230 156 L320 168 V190Z", "rock") + `<ellipse class="cloud" cx="108" cy="56" rx="50" ry="17"/>` + G(0, CURVE("M6 136 C60 126 100 104 140 66", "cool") + DROPS([86, 104, 122], 74, 120)) + G(1, CURVE("M182 62 C210 86 240 118 300 130", "warm")) + C(286, 28, 14, "sunc") },

  // Mission 5: ocean and hazards
  shelf: { pins: [[260, 170], [146, 122], [62, 92]], art: SKY + R(0, 50, 320, 140, "water") + P("M0 58 L100 74 L196 150 L320 170 V190 H0Z".replace("M0 58", "M0 56"), "land") + G(2, P("M0 56 L100 74 V60 H0Z", "hotcap")) + G(1, P("M100 74 L196 150", "hi")) + G(0, P("M196 150 L320 170", "hi2")) },
  wave: { pins: [[160, 58], [58, 140], [262, 100]], art: SKY + R(0, 110, 320, 80, "water") + G(0, `<path class="wave wgo" d="M-80 96 q20 -24 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0"/>`) + G(1, R(30, 78, 16, 90, "paper2", 3) + AR(38, 90, 38, 150, "warm") + AR(26, 150, 26, 96, "warm")) + G(2, AR(214, 164, 300, 164, "cool") + AR(214, 144, 300, 144, "cool")) },
  tide: { pins: [[84, 76], [84, 136], [40, 30]], art: SKY + `<g class="tideg">${R(0, 104, 320, 90, "water")}</g>` + G(0, P("M0 76 H320", "hi2")) + G(1, P("M0 136 H320", "hi")) + P("M150 190 C200 150 240 96 270 60 L322 44 V190Z", "land") + G(2, C(40, 30, 16, "moon")) },
  exposure: { pins: [[60, 120], [226, 130]], art: SKY + `<path class="land" d="M0 190 V150 H320 V190Z"/>` + G(0, `<path class="wave wgo" d="M-40 138 q20 -14 40 0 t40 0 t40 0 t40 0 t40 0"/>` + R(0, 144, 130, 12, "water")) + G(1, [176, 208, 240, 272].map((x) => `<path class="house" d="M${x} 150 v-22 l13 -12 l13 12 v22Z"/>`).join("") + P("M150 158 H320", "road")) },
  cyclone: { pins: [[160, 95], [78, 150], [264, 150]], art: R(0, 0, 320, 190, "water2") + G(0, `<g class="spin">${[0, 120, 240].map((a) => `<path class="swirl" transform="rotate(${a} 160 95)" d="M160 95 C150 50 208 30 244 66"/>`).join("")}</g>` + C(160, 95, 7, "eye")) + G(1, P("M24 186 Q78 118 132 186Z", "wavebig")) + G(2, P("M214 186 Q264 148 316 186Z", "water") + AR(264, 176, 264, 138, "warm")) },
  surge: { pins: [[86, 62], [240, 124], [240, 170]], art: SKY + G(0, `<g class="spin">${[0, 120, 240].map((a) => `<path class="swirl" transform="rotate(${a} 70 58)" d="M70 58 C64 34 92 22 112 42"/>`).join("")}</g>` + AR(120, 92, 158, 92, "wind")) + R(0, 112, 320, 78, "water") + G(1, `<path class="wave" d="M130 112 Q200 70 268 112"/>`) + G(2, P("M180 190 L208 158 L224 168 L250 150 L300 190Z", "rock") + AR(236, 148, 236, 122, "warm")) },

  // Mission 6: locating India
  neighbours: { pins: IPIN([69, 30], [84, 29.4], [91, 28.6], [96.5, 21.5]), size: 300, art: IN("") },
  seas: { pins: IPIN([70, 16], [90, 15]), size: 300, art: IN(G(0, blob([[67, 8], [76, 8], [73, 19], [69, 21], [67, 19]], "seahi")) + G(1, blob([[81, 8], [94, 8], [94, 21], [87, 21], [81, 15]], "seahi"))) },
  anchors: { pins: IPIN([77.2, 28.6], [94.1, 25.7], [91.7, 26.1]), size: 300, art: IN(G(0, C(...ind(77.2, 28.6), 6, "accent")) + G(1, C(...ind(94.1, 25.7), 6, "accent")) + G(2, C(...ind(91.7, 26.1), 6, "accent"))) },
  tropic: { pins: IPIN([70, 23.5], [82.5, 14]), size: 300, art: IN(G(0, line([[66, 23.5], [98, 23.5]], "hi")) + G(1, line([[82.5, 36], [82.5, 7]], "hi2"))) },
  sunrise: { pins: [[286, 58], [34, 58]], art: R(0, 0, 320, 190, "dawn") + P("M0 100 Q160 74 320 100 V190 H0Z", "land") + SUN(286, 72, 24) + G(0, C(286, 124, 7, "accent")) + G(1, C(34, 124, 7, "ink")) + AR(262, 124, 56, 124, "warm") + TX(160, 150, "1° = 4 min", "১° = ৪ মিনিট", "bold") + TX(160, 172, "Sun moves east → west", "সূৰ্য পূবৰ পৰা পশ্চিমলৈ", "") },
  islands: { pins: IPIN([92.8, 11.5], [72.8, 11]), size: 300, art: IN(G(0, [[92.8, 13.2], [92.7, 12], [92.7, 10.8], [93.6, 8.2], [93.8, 7.2]].map(([a, b]) => C(...ind(a, b), 4, "accent")).join("")) + G(1, [[72.7, 12], [73, 10.8], [72.2, 10], [73, 8.5]].map(([a, b]) => C(...ind(a, b), 3.4, "accent")).join(""))) },

  // Mission 7: relief
  himabelts: { pins: [[256, 150], [158, 96], [62, 40]], art: SKY + `<path class="ice" d="M30 72 L66 22 L104 74Z"/>` + G(2, P("M0 190 V96 L34 64 L66 22 L100 74 L124 110 V190Z", "rock")) + G(1, P("M118 190 V116 L150 78 L170 92 L190 128 V190Z", "rock2")) + G(0, P("M186 190 V138 L222 118 L250 136 L276 150 V190Z", "grass2")) + R(276, 150, 44, 40, "sand") + TX(60, 180, "N", "উ", "bold") + TX(300, 180, "S", "দ", "bold") },
  plainsthar: { pins: IPIN([84, 26.2], [71, 27]), size: 300, art: IN(G(0, blob([[74, 31], [79, 29.5], [86, 26.5], [93, 26], [95, 27.5], [90, 25], [84, 24.8], [77, 26.5], [74, 29]], "alluv")) + G(1, blob([[69, 29], [74, 29], [73.5, 25], [70, 24.5]], "sandy"))) },
  alluvium: { pins: [[92, 110], [240, 64]], art: SKY + G(0, P("M0 190 V132 Q60 120 150 126 V190Z", "alluv") + P("M0 124 Q70 112 150 118", "riverthin")) + G(1, P("M172 190 V130 Q192 88 216 124 Q242 76 276 124 Q294 110 320 130 V190Z", "sand")) + SUN(258, 32) },
  ghats: { pins: IPIN([74, 16], [82, 17], [91.5, 25.5]), size: 300, art: IN(G(0, TEETH([[73.4, 19], [74, 15.5], [75.3, 12], [76.8, 9.6]])) + G(1, TEETH([[79, 13.5], [81.5, 16.6], [84, 19.5]])) + G(2, blob([[89.8, 26], [92.8, 26.1], [93.5, 25.3], [90, 25.2]], "alluv"))) },
  gap: { pins: [[256, 72], [176, 112], [86, 88]], art: SKY + G(2, P("M0 190 V96 L46 70 L96 88 L136 108 V190Z", "rock")) + G(1, P("M136 190 V126 H216 V190Z", "alluv") + P("M136 126 H216", "riverthin")) + G(0, P("M216 190 V108 L254 62 L290 72 L320 96 V190Z", "rock2")) },
  coasts: { pins: IPIN([73.2, 17], [80.6, 15.2]), size: 300, art: IN(G(0, line([[72.6, 21], [73, 17], [74.6, 13], [76.3, 9.2]], "hi")) + G(1, line([[77.6, 8.6], [80.2, 13.4], [81, 16], [86, 20], [88, 22]], "hi2"))) },
  coastcut: { pins: [[62, 150], [248, 150]], art: SKY + R(0, 150, 60, 40, "water") + R(260, 150, 60, 40, "water") + P("M42 190 L60 146 L84 60 L128 74 L160 90 L196 134 L262 148 L276 190Z", "rock") + G(0, P("M46 190 L60 146 L84 146 V190Z", "grass2")) + G(1, P("M196 190 V134 L262 148 L276 190Z", "alluv")) },

  // Mission 8: rivers
  watershed: { pins: [[160, 28], [160, 128]], art: R(0, 0, 320, 190, "grass") + G(0, P("M0 30 Q80 14 160 32 T320 26", "hi")) + G(1, C(160, 128, 8, "accent")) + `<g class="rivs">${["M60 40 C80 90 120 110 160 128", "M260 40 C230 90 200 110 160 128", "M160 44 C160 80 158 104 160 128", "M160 128 C160 150 170 170 160 190"].map((d) => P(d, "river-flow")).join("")}</g>` },
  northrivers: { pins: IPIN([74.5, 33], [84, 26.5], [93, 26.8]), size: 300, art: IN(G(0, line([[81, 31], [75, 34.5], [73, 31], [71, 27.5], [68, 24]], "riverline")) + G(1, line([[79, 31], [79, 27.5], [83, 25.5], [87.9, 24.5], [89.5, 22]], "riverline")) + G(2, line([[85, 30.5], [91, 29.5], [95.2, 29], [95, 27.8], [91, 26.2], [89.7, 25.3], [90, 23.5]], "riverline"))) },
  penrivers: { pins: IPIN([74, 21.7], [80, 17]), size: 300, art: IN(G(0, line([[81.7, 22.6], [78, 22.5], [72.8, 21.7]], "riverline") + line([[78, 21.7], [74, 21.2], [72.7, 21.1]], "riverline")) + G(1, line([[73.6, 20], [78, 19], [81.8, 16.6]], "riverline") + line([[73.7, 18], [78, 16.5], [81, 15.8]], "riverline") + line([[75.7, 12.4], [78.5, 11], [79.9, 10.8]], "riverline"))) },
  mouths: { pins: [[86, 96], [244, 96]], art: R(0, 0, 320, 120, "grass") + R(0, 120, 320, 70, "water") + G(0, P("M86 0 V70", "riverthick") + P("M86 70 L38 134 M86 70 L66 140 M86 70 L106 140 M86 70 L134 134", "riverthin") + P("M30 120 Q86 158 142 120 L86 60Z", "sand")) + G(1, P("M236 0 L250 0 L300 190 L190 190Z", "water") ) },

  // Mission 9: monsoon
  rainseason: { pins: [[166, 90], [262, 60]], art: R(0, 0, 320, 190, "paper") + G(0, R(106, 40, 96, 100, "seahi", 6)) + ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"].map((m, k) => `<text class="gf-t" x="${27 + k * 24}" y="160" text-anchor="middle">${m}</text>`).join("") + [6, 6, 10, 18, 30, 70, 92, 84, 62, 30, 12, 6].map((h, k) => BAR(18 + k * 24, 140, 18, h, k > 4 && k < 9 ? "bwater" : "bmute")).join("") + G(1, P("M234 40 v100", "dash")) },
  onsetdates: { pins: [[160, 62], [70, 136]], art: R(0, 0, 320, 190, "paper") + P("M20 110 H300", "axis") + G(0, P("M160 42 V110", "hi2") + TX(160, 34, "Normal date", "স্বাভাৱিক তাৰিখ", "bold")) + G(1, [90, 128, 150, 196, 234].map((x, k) => C(x, 126 + (k % 2) * 14, 7, "accent")).join("")) + TX(160, 178, "Each dot: one year (illustrative)", "প্ৰতিটো বিন্দু: এটা বছৰ (উদাহৰণ)") },
  monsoonpaths: { pins: IPIN([70, 13], [89, 16]), size: 300, art: IN(G(0, AR(...ind(68, 8), ...ind(73, 13), "cool") + AR(...ind(71, 11), ...ind(75, 20), "cool") + AR(...ind(70, 14), ...ind(74, 21), "cool")) + G(1, AR(...ind(85, 9), ...ind(90, 19), "cool") + AR(...ind(89, 15), ...ind(92, 24), "cool") + CURVE(`M${lx(90)} ${ly(23)} C${lx(86)} ${ly(26)} ${lx(80)} ${ly(27)} ${lx(75)} ${ly(29)}`, "cool"))) },
  stationbars: { pins: [[96, 28], [230, 28]], art: R(0, 0, 320, 190, "paper") + G(0, [8, 12, 26, 48, 70, 78, 84, 68, 52, 28, 10, 6].map((h, k) => BAR(26 + k * 11, 150, 9, h, k === 6 ? "bwater" : "bmute")).join("") + TX(92, 172, "Guwahati", "গুৱাহাটী", "bold")) + G(1, [8, 4, 4, 6, 10, 14, 26, 30, 32, 84, 76, 28].map((h, k) => BAR(170 + k * 11, 150, 9, h, k === 9 ? "bwater" : "bmute")).join("") + TX(236, 172, "Chennai", "চেন্নাই", "bold")) + TX(160, 186, "Shape only; bars not to scale", "কেৱল আকৃতি; মাপ অনুসৰি নহয়") },
  withdrawal: { pins: IPIN([72, 28], [80, 12]), size: 300, art: IN(G(0, C(...ind(72, 28), 7, "accent") + AR(...ind(74, 27), ...ind(84, 22), "warm") + AR(...ind(84, 22), ...ind(79, 14), "warm")) + G(1, line([[77.6, 8.6], [80.2, 13.4], [81, 16]], "hi"))) },
  nemonsoon: { pins: IPIN([79.6, 12], [87, 14.4]), size: 300, art: IN(blob([[81, 8], [90, 8], [90, 20], [84, 19]], "seahi") + G(1, AR(...ind(90, 20), ...ind(82, 13), "cool") + AR(...ind(88, 15), ...ind(81, 10.5), "cool")) + G(0, line([[77.6, 8.6], [80.2, 13.4], [81, 16]], "hi")) + "") },

  // Mission 10: land and livelihoods
  soils: { pins: IPIN([84, 26], [76, 20]), size: 300, art: IN(G(0, blob([[75, 31], [86, 26.8], [94, 26], [88, 24.5], [78, 26]], "alluv")) + G(1, blob([[73.5, 22.5], [78, 22.5], [79, 17], [75, 15.5]], "black"))) },
  soilcut: { pins: [[86, 60], [236, 60]], art: SKY + G(0, R(26, 44, 120, 136, "alluv", 6) + `<g class="dots">${[[50, 80], [90, 72], [120, 110], [60, 130], [104, 150]].map(([x, y]) => C(x, y, 3, "ink")).join("")}</g>`) + G(1, R(174, 44, 120, 136, "black", 6) + P("M204 44 l10 44 l-6 26 M254 44 l-8 54 l10 40", "cracks")) },
  raingradient: { pins: [[56, 74], [262, 74], [160, 150]], art: SKY + `<path class="land" d="M0 190 V120 H320 V190Z"/>` + DROPS([20, 44, 68, 92], 8, 40) + SUN(280, 30) + G(0, [24, 52, 80].map((x) => C(x, 86, 24, "tree") + R(x - 3, 100, 6, 24, "trunk")).join("")) + G(1, [232, 262, 292].map((x) => P(`M${x} 122 V96 M${x} 106 l-10 -8 M${x} 104 l10 -10`, "thorn")).join("")) + G(2, R(100, 120, 120, 70, "water") + [130, 160, 190].map((x) => P(`M${x} 152 v-24 M${x} 152 l-10 16 M${x} 152 l10 16`, "thorn") + C(x, 124, 11, "tree")).join("")) },
  vegmap: { pins: IPIN([75.5, 11], [72, 25], [89, 21.8]), size: 300, art: IN(G(0, blob([[73.2, 19], [75, 14], [77, 9], [75.6, 10.2], [73.5, 15]], "treez")) + G(1, blob([[69.5, 28.5], [75, 29], [75, 24], [70, 23.5]], "sandy")) + G(2, blob([[87.8, 22.4], [90, 22.4], [90, 21.4], [87.8, 21.4]], "treez"))) },
  cropbars: { pins: [[108, 30], [212, 30]], art: R(0, 0, 320, 190, "paper") + P("M40 160 H284", "axis") + G(0, BAR(72, 160, 72, 118, "bwater") + TX(108, 178, "Kharif", "খৰিফ", "bold")) + G(1, BAR(176, 160, 72, 118, "bgold") + TX(212, 178, "Rabi", "ৰবি", "bold")) },
  cropcalendar: { pins: [[96, 80], [224, 80]], art: R(0, 0, 320, 190, "paper") + G(0, `<path class="seahi" d="M160 95 L160 19 A76 76 0 0 1 160 171Z" transform="rotate(180 160 95) rotate(60 160 95)"/>`) + G(1, `<path class="sandy" d="M160 95 L160 19 A76 76 0 0 1 160 171Z" transform="rotate(60 160 95)"/>`) + C(160, 95, 42, "paperc") + TX(160, 92, "One", "এটা") + TX(160, 108, "year", "বছৰ") },
  density: { pins: [[86, 30], [236, 30]], art: R(0, 0, 320, 190, "paper") + G(0, R(26, 42, 120, 120, "card", 6) + Array.from({ length: 30 }, (_, k) => C(40 + (k % 6) * 19, 58 + Math.floor(k / 6) * 22, 5, "accent")).join("")) + G(1, R(174, 42, 120, 120, "card", 6) + [[196, 70], [262, 66], [226, 120], [274, 140], [192, 142]].map(([x, y]) => C(x, y, 5, "accent")).join("")) + TX(160, 182, "Same area, different people ÷ area", "একে কালি, বেলেগ মানুহ ÷ কালি") },
  settlement: { pins: [[172, 112], [64, 48]], art: R(0, 0, 320, 190, "grass") + `<path class="peak2" d="M0 72 L34 22 L66 64 L104 18 L140 70Z"/>` + P("M0 150 C100 110 200 130 320 80", "riverw2") + G(0, [150, 170, 192, 160, 184].map((x, k) => `<path class="house" transform="translate(${x - 150} ${k > 2 ? 18 : 0}) scale(.6) translate(100 30)" d="M150 120 v-20 l13 -12 l13 12 v20Z"/>`).join("")) + G(1, P("M0 96 L130 110 L320 134", "road")) },
  // Shared idea diagrams for non-map lessons
  stairs4: { pins: [[52, 142], [124, 106], [196, 70], [268, 34]], art: R(0, 0, 320, 190, "paper") + [0, 1, 2, 3].map((k) => G(k, R(20 + k * 72, 150 - k * 36, 66, 40 + k * 36, ["bmute", "bgold", "bwater", "grass2"][k], 4))).join("") },
  pillars3: { pins: [[62, 56], [160, 56], [258, 56]], art: R(0, 0, 320, 190, "paper") + P("M16 34 H304 L160 8Z", "rock2") + [0, 1, 2].map((k) => G(k, R(34 + k * 98, 36, 56, 124, ["bwater", "bgold", "grass2"][k], 4))).join("") + R(16, 160, 288, 14, "rock", 3) },
  hub3: { pins: [[58, 40], [262, 40], [160, 164]], art: R(0, 0, 320, 190, "paper") + C(160, 92, 30, "core") + [[58, 40], [262, 40], [160, 164]].map(([x, y], k) => G(k, CURVE(`M160 92 L${x} ${y}`, "cool") + C(x, y, 24, "seahi"))).join("") },
  line4: { pins: [[46, 92], [122, 92], [198, 92], [274, 92]], art: R(0, 0, 320, 190, "paper") + AR(14, 92, 310, 92, "cool") + [46, 122, 198, 274].map((x, k) => G(k, P(`M${x} 60 V124`, "dash"))).join("") },
  scales2: { pins: [[70, 118], [250, 90]], art: R(0, 0, 320, 190, "paper") + P("M160 30 V170 M116 170 H204", "axis") + P("M70 74 L250 46", "axis") + G(0, P("M70 74 L34 122 H106Z", "seahi")) + G(1, P("M250 46 L214 94 H286Z", "sandy")) },
  fcpie: { pins: [[218, 118], [100, 150], [56, 96], [84, 52], [130, 28], [190, 34]], art: R(0, 0, 320, 190, "paper") + (() => { let a = -Math.PI / 2; return [42.5, 17.5, 10, 10, 10, 10].map((v, k) => { const b = a + (v / 100) * 2 * Math.PI, pt = (t) => `${(160 + 82 * Math.cos(t)).toFixed(1)} ${(95 + 82 * Math.sin(t)).toFixed(1)}`, d = `M160 95 L${pt(a)} A82 82 0 ${v > 50 ? 1 : 0} 1 ${pt(b)}Z`; a = b; return G(k, P(d, ["bwater", "bgold", "grass2", "rock2", "alluv", "sandy"][k] + " slice")); }).join(""); })() },
  patterns4: { pins: [[80, 24], [240, 24], [80, 118], [240, 118]], art: R(0, 0, 320, 190, "grass") + G(0, P("M80 88 V40 M80 74 L52 50 M80 74 L108 50 M80 60 L62 34 M80 60 L98 34 M52 50 L40 58 M108 50 L120 58", "riverthin")) + G(1, [0, 1, 2, 3, 4, 5, 6, 7].map((k) => { const t = k * Math.PI / 4; return AR(+(240 + 12 * Math.cos(t)).toFixed(1), +(52 + 12 * Math.sin(t)).toFixed(1), +(240 + 36 * Math.cos(t)).toFixed(1), +(52 + 36 * Math.sin(t)).toFixed(1), "cool"); }).join("")) + G(2, P("M80 180 V130 M80 170 H52 M80 170 H108 M80 152 H52 M80 152 H108 M80 136 H58 M80 136 H102", "riverthin")) + G(3, [0, 1, 2, 3, 4, 5, 6, 7].map((k) => { const t = k * Math.PI / 4; return AR(+(240 + 38 * Math.cos(t)).toFixed(1), +(150 + 34 * Math.sin(t)).toFixed(1), +(240 + 14 * Math.cos(t)).toFixed(1), +(150 + 13 * Math.sin(t)).toFixed(1), "cool"); }).join("") + C(240, 150, 10, "water")) },
  prayag5: { pins: [[92, 32], [116, 62], [140, 92], [164, 122], [204, 152]], art: R(0, 0, 320, 190, "grass") + P("M56 6 L92 32 L116 62 L140 92 L164 122 L204 152 L316 176", "riverthick") + P("M136 10 L92 32 M172 26 L116 62 M214 46 L140 92 M254 72 L164 122 M300 96 L204 152", "riverthin") },
  plainbelts4: { pins: [[66, 102], [142, 114], [214, 124], [282, 136]], art: SKY + P("M0 190 V62 L30 40 L50 74 L104 130 L320 150 V190Z", "rock2") + G(0, P("M20 190 L46 76 L104 130 V190Z", "rock")) + G(1, P("M104 190 V130 L176 138 V190Z", "grass2")) + G(2, P("M176 190 V138 L250 144 V190Z", "alluv")) + G(3, P("M250 190 V144 L320 150 V190Z", "water")) },
  extremes4: { pins: IPIN([75.8, 34.4], [75, 28.3], [70.9, 26.9], [91.6, 25.3]), size: 300, art: IN("") },
  peaks3: { pins: [[60, 66], [158, 106], [260, 118]], art: SKY + G(0, P("M0 190 L60 84 L122 190Z", "rock")) + G(1, P("M100 190 L158 124 L214 190Z", "rock2")) + G(2, P("M196 190 L260 136 L320 190Z", "grass2")) },
  forces2: { pins: [[90, 150], [238, 46]], art: SKY + DROPS([206, 232, 258], 8, 34) + P("M0 190 V116 L56 52 L120 120 L200 104 L320 138 V190Z", "rock") + G(0, AR(56, 186, 56, 96, "warm") + AR(112, 186, 112, 140, "warm")) + G(1, CURVE("M196 106 C236 112 270 120 316 138", "cool")) },
  reserves5: { pins: [[74, 62], [160, 28], [246, 62], [214, 150], [106, 150]], art: R(0, 0, 320, 190, "paper") + [[74, 62], [160, 28], [246, 62], [214, 150], [106, 150]].map(([x, y], k) => G(k, C(x, y, 26, "seahi"))).join("") },
  kzcorridors: { pins: [[50, 104], [110, 104], [170, 104], [230, 104], [282, 104]], art: R(0, 0, 320, 70, "grass2") + TX(160, 38, "Kaziranga", "কাজিৰঙা", "bold") + P("M0 84 H320", "road") + P("M0 190 V132 L60 118 L140 132 L220 116 L320 132 V190Z", "rock") + TX(160, 172, "Karbi Anglong hills", "কাৰ্বি আংলং পাহাৰ", "bold") + [50, 110, 170, 230, 282].map((x, k) => G(k, AR(x, 66, x, 124, "cool"))).join("") + TX(160, 186, "Order not to scale", "ক্ৰম মাপ অনুসৰি নহয়") },
  kzranges: { pins: [[40, 112], [100, 112], [168, 112], [244, 112], [170, 36]], art: R(0, 0, 320, 190, "grass") + P("M0 74 Q160 50 320 66", "riverw2") + P("M0 96 H320", "road") + [[12, 64], [72, 68], [132, 72], [204, 72]].map(([x, w], k) => G(k, R(x, 86, [58, 58, 70, 86][k], 54, ["rock2", "alluv", "grass2", "sandy"][k], 6))).join("") + G(4, R(120, 18, 100, 34, "seahi", 6)) + TX(160, 170, "Brahmaputra north, highway south · schematic", "উত্তৰে ব্ৰহ্মপুত্ৰ, দক্ষিণে ঘাইপথ") },
};

// ---------- Redrawn Geography Foundations scenes (same pins and meanings as before) ----------
Object.assign(F, {
  compass: { pins: [[70, 40], [214, 160]], art: R(0, 0, 320, 190, "paper")
    + `<g filter="url(#gf-shadow)"><path fill="url(#gf-grass)" d="M150 20 h150 a10 10 0 0 1 10 10 v130 a10 10 0 0 1 -10 10 h-150 a10 10 0 0 1 -10 -10 v-130 a10 10 0 0 1 10 -10Z"/></g>`
    + `<path d="M150 120 C190 108 220 132 300 112" stroke="url(#gf-sea)" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M146 66 H306" class="road"/>` + MTN([[262, 42, 18], [284, 30, 14]], 66, false) + FOREST(162, 220, 96, 6, .8) + HOUSE(190, 64, .8)
    + G(0, `<circle cx="70" cy="95" r="52" fill="#fff" filter="url(#gf-shadow)"/><circle cx="70" cy="95" r="44" fill="none" stroke="#d9ccb0" stroke-width="1.5"/>` + `<g class="spin-slow"><path fill="#e0563b" d="M70 52 L80 95 H60Z"/><path fill="#9aa7ab" d="M70 138 L80 95 H60Z"/></g><circle cx="70" cy="95" r="5" fill="#17313b"/>` + LBL(70, 36, "N", "উ", "middle", "bold") + LBL(124, 99, "E", "পূ", "middle", "bold") + LBL(16, 99, "W", "প", "middle", "bold") + LBL(70, 160, "S", "দ", "middle", "bold"))
    + G(1, `<rect x="164" y="138" width="138" height="44" rx="9" fill="#fff" filter="url(#gf-shadow)"/><path d="M174 152 h16" stroke="#4f9fc4" stroke-width="4"/>` + LBL(196, 156, "River", "নদী", "start") + `<path d="M236 152 h16" class="road"/>` + LBL(258, 156, "Road", "পথ", "start") + `<circle cx="182" cy="170" r="4" fill="#3f8c55"/>` + LBL(196, 174, "Forest", "অৰণ্য", "start") + `<path d="M238 175 l6 -9 l6 9Z" fill="url(#gf-rock)"/>` + LBL(258, 174, "Hill", "পাহাৰ", "start")) },
  graticule: { pins: [[300, 95], [160, 18]], art: `<rect width="320" height="190" fill="url(#gf-night)"/>` + Array.from({ length: 26 }, (_, k) => `<circle cx="${(k * 97) % 320}" cy="${(k * 53) % 190}" r="${k % 3 ? .7 : 1.2}" fill="#fff" opacity=".7"/>`).join("")
    + `<circle cx="160" cy="95" r="94" fill="url(#gf-glow)" opacity=".35"/><circle cx="160" cy="95" r="82" fill="url(#gf-ocean)"/>`
    + `<path fill="url(#gf-grass)" opacity=".9" d="M120 40 q30 -12 52 4 q14 18 -6 30 q-20 4 -18 26 q4 22 -14 30 q-16 -14 -20 -40 q-10 -26 6 -50Z M190 96 q22 -6 34 10 q4 22 -16 30 q-18 -6 -18 -40Z"/>`
    + `<g fill="none" stroke="#fff" stroke-opacity=".45"><ellipse cx="160" cy="95" rx="82" ry="28"/><ellipse cx="160" cy="95" rx="82" ry="58"/><ellipse cx="160" cy="95" rx="28" ry="82"/><ellipse cx="160" cy="95" rx="58" ry="82"/></g>`
    + `<circle cx="160" cy="95" r="82" fill="none" stroke="#fff" stroke-opacity=".6" stroke-width="2"/>`
    + G(0, `<path d="M62 95 H300" stroke="#ff8a5c" stroke-width="4" stroke-linecap="round"/>` + LBL(60, 88, "0° latitude", "০° অক্ষাংশ", "end", "bold")) + G(1, `<path d="M160 10 V180" stroke="#7fd6ff" stroke-width="4" stroke-linecap="round"/>` + LBL(168, 186, "0° longitude", "০° দ্ৰাঘিমা", "start", "bold")) },
  scalebar: { pins: [[60, 150], [178, 150]], art: R(0, 0, 320, 190, "paper") + `<path fill="url(#gf-grass)" opacity=".55" d="M0 0 H320 V120 C240 132 120 110 0 128Z"/>` + FOREST(220, 310, 40, 6, .8) + `<path d="M30 92 C90 30 150 110 210 60 S290 64 300 40" stroke="#5d5148" stroke-width="5" fill="none" stroke-dasharray="10 6" stroke-linecap="round"/>`
    + HOUSE(30, 92, 1.1) + HOUSE(300, 40, 1.1, "#1d6f96")
    + G(0, `<rect x="16" y="136" width="70" height="26" rx="8" fill="#fff" filter="url(#gf-shadow)"/>` + LBL(51, 154, "1 cm : 5 km", "১ ছেমি : ৫ কিমি", "middle", "bold"))
    + G(1, `<g filter="url(#gf-shadow)">${[0, 1, 2, 3].map((k) => `<rect x="${110 + k * 48}" y="160" width="48" height="10" fill="${k % 2 ? "#fff" : "#17313b"}" stroke="#17313b"/>`).join("")}</g>` + ["0", "5", "10", "15", "20 km"].map((v, k) => `<text class="gf-t" x="${110 + k * 48}" y="183" text-anchor="middle">${v}</text>`).join("")) },
  contour: { pins: [[94, 70], [246, 70]], art: R(0, 0, 320, 190, "paper")
    + `<g filter="url(#gf-shadow)"><rect x="12" y="12" width="140" height="110" rx="10" fill="#f6efd9"/><rect x="168" y="12" width="140" height="110" rx="10" fill="#f6efd9"/></g>`
    + G(0, [44, 36, 28, 20, 12].map((r, k) => `<ellipse cx="82" cy="70" rx="${r + 10}" ry="${r}" fill="${["#e9e1b8", "#ddd09c", "#cfbf86", "#bfa874", "#a99062"][k]}" stroke="#7c6550" stroke-width=".8"/>`).join("") + LBL(82, 30, "close lines", "ঘন ৰেখা", "middle", "bold"))
    + G(1, [44, 30, 16].map((r, k) => `<ellipse cx="238" cy="70" rx="${r + 18}" ry="${r}" fill="${["#e9e1b8", "#d7c993", "#c4b07a"][k]}" stroke="#7c6550" stroke-width=".8"/>`).join("") + LBL(238, 30, "spread lines", "বহল ৰেখা", "middle", "bold"))
    + `<path fill="url(#gf-rock)" d="M14 184 L52 140 L82 132 L112 140 L150 184Z"/><path fill="url(#gf-rock2)" d="M170 184 L210 160 L238 154 L270 160 L306 184Z"/>` + LBL(160, 150, "same rise", "একে উচ্চতা") },
  daynight: { pins: [[214, 95], [116, 95]], art: `<rect width="320" height="190" fill="url(#gf-night)"/>` + Array.from({ length: 18 }, (_, k) => `<circle cx="${(k * 41) % 150}" cy="${(k * 67) % 190}" r=".9" fill="#fff" opacity=".7"/>`).join("") + SUNR(296, 95, 18)
    + [70, 95, 120].map((y) => AR(270, y, 244, y, "sunray")).join("")
    + `<circle cx="164" cy="95" r="74" fill="url(#gf-glow)" opacity=".3"/>` + G(0, `<path fill="url(#gf-ocean)" d="M164 23 A72 72 0 0 1 164 167Z"/><path fill="url(#gf-grass)" opacity=".85" d="M176 50 q24 -2 30 20 q-4 18 -20 14 q-14 10 -10 30 q-12 -6 -10 -30 q-6 -20 10 -34Z"/>`)
    + G(1, `<path fill="#1b3149" d="M164 23 A72 72 0 0 0 164 167Z"/><path fill="#2c4a39" opacity=".8" d="M120 60 q20 -10 30 6 q-6 22 -22 22 q-12 -12 -8 -28Z"/>` + [[130, 120], [142, 108], [118, 98]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="1.6" fill="#ffd76a"/>`).join(""))
    + `<path d="M164 23 V167" stroke="#fff" stroke-opacity=".35"/>` + CURVE("M96 178 C130 190 200 190 232 178", "cool2") },
  sunangle: { pins: [[226, 52], [100, 52]], art: `<rect width="320" height="190" fill="url(#gf-night)"/>` + SUNR(34, 95, 22)
    + `<g transform="rotate(23.5 214 95)"><circle cx="214" cy="95" r="68" fill="url(#gf-ocean)"/>` + G(0, `<path fill="#ffcf7a" opacity=".85" d="M146 70 A68 68 0 0 1 282 70Z"/>`) + `<path fill="#2c5b83" opacity=".75" d="M146 120 A68 68 0 0 0 282 120Z"/><path d="M214 14 V176" stroke="#fff" stroke-width="2" stroke-dasharray="5 4"/>` + LBL(214, 10, "N", "উ", "middle", "bold") + `</g>`
    + G(1, AR(60, 66, 150, 70, "sunray") + AR(60, 74, 150, 80, "sunray")) + AR(60, 120, 150, 112, "sunray") + LBL(214, 186, "June: north leans in", "জুন: উত্তৰ সূৰ্যমুখী", "middle", "bold") },
  earthlayers: { pins: [[160, 22], [160, 60], [160, 128]], art: `<rect width="320" height="190" fill="url(#gf-night)"/>` + SUNR(290, 26, 8)
    + G(0, `<circle cx="160" cy="214" r="196" fill="#8a6a48"/><path d="M-30 214 A190 190 0 0 1 350 214" stroke="url(#gf-grass)" stroke-width="5" fill="none"/>`)
    + G(1, `<circle cx="160" cy="214" r="184" fill="url(#gf-mantle)"/>` + [92, 160, 228].map((x, k) => CURVE(`M${x} 128 C${x - 18} 104 ${x + 18} 84 ${x} 62`, "warm d" + k)).join(""))
    + G(2, `<circle cx="160" cy="214" r="102" fill="url(#gf-core)"/><circle cx="160" cy="214" r="54" fill="#fff3b0" opacity=".7"/>`) + LBL(160, 180, "thin crust · thick mantle · hot core", "পাতল ভূত্বক · ডাঠ মেণ্টল · উত্তপ্ত কেন্দ্ৰ", "middle", "bold") },
  boundaries: { pins: [[54, 86], [160, 70], [266, 86]], art: SKYBG() + `<rect y="132" width="320" height="58" fill="url(#gf-mantle)"/>` + [40, 160, 280].map((x) => CURVE(`M${x - 20} 182 C${x - 20} 150 ${x + 20} 150 ${x + 20} 182`, "warm")).join("")
    + G(0, `<path fill="url(#gf-rock)" d="M4 112 H46 L50 132 H4Z M58 112 H104 V132 H62Z"/><path fill="#e0562c" d="M50 132 L54 100 L58 132Z" filter="drop-shadow(0 0 4px #f08a24)"/>` + AR(34, 148, 8, 148, "cool") + AR(74, 148, 100, 148, "cool"))
    + G(1, `<path fill="url(#gf-rock)" d="M112 132 V112 H146 L160 66 L174 112 H208 V132Z"/><path fill="url(#gf-snow)" d="M160 66 L166 86 L154 86Z"/>` + AR(116, 148, 146, 148, "cool") + AR(204, 148, 174, 148, "cool"))
    + G(2, `<path fill="url(#gf-rock)" d="M216 112 H314 V132 H216Z"/><path d="M265 104 V140" class="fault"/>` + AR(250, 100, 222, 100, "cool") + AR(280, 146, 310, 146, "cool"))
    + LBL(54, 182, "apart", "আঁতৰ", "middle", "bold") + LBL(160, 182, "together", "ওচৰ", "middle", "bold") + LBL(266, 182, "slide", "পিছল", "middle", "bold") },
  rockcycle: { pins: [[62, 118], [160, 52], [262, 118]], art: R(0, 0, 320, 190, "paper")
    + G(0, `<circle cx="62" cy="122" r="44" fill="#4a3d38" filter="url(#gf-shadow)"/>${Array.from({ length: 14 }, (_, k) => `<path fill="${["#e8e2d6", "#c9b9a6", "#2f2724"][k % 3]}" d="M${36 + (k * 17) % 50} ${100 + (k * 23) % 44} l5 -3 l4 4 l-4 4Z"/>`).join("")}` + LBL(62, 178, "igneous", "আগ্নেয়", "middle", "bold"))
    + G(1, `<g filter="url(#gf-shadow)">${STRATA(110, 28, 100, 52, ["#e8cf96", "#c9a66c", "#efdcae", "#b58c58", "#e1c487"])}</g>` + LBL(160, 98, "sedimentary", "পাললিক", "middle", "bold"))
    + G(2, `<g filter="url(#gf-shadow)"><rect x="216" y="92" width="94" height="58" rx="6" fill="#7d8a86"/>${[0, 1, 2, 3].map((k) => `<path d="M216 ${102 + k * 13} q24 -10 47 0 t47 0" stroke="${k % 2 ? "#cfd8d4" : "#4f5c58"}" stroke-width="5" fill="none"/>`).join("")}</g>` + LBL(262, 172, "metamorphic", "ৰূপান্তৰিত", "middle", "bold"))
    + CURVE("M92 86 C100 66 104 58 110 52") + CURVE("M210 58 C232 62 248 76 258 90") + CURVE("M226 160 C190 186 130 186 96 162") },
  grainpath: { pins: [[54, 58], [172, 104], [282, 152]], art: SKYBG() + CLOUD(250, 40, .9) + MTN([[40, 150, 56]], 190, true) + `<path fill="url(#gf-rock)" d="M0 190 V70 L54 40 L120 100 L210 128 L320 150 V190Z"/>` + FOREST(120, 200, 112, 5, .8)
    + `<path d="M40 70 C70 78 92 104 132 114 S240 140 320 162" stroke="url(#gf-sea)" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M40 70 C70 78 92 104 132 114 S240 140 320 162" class="river-flow" fill="none"/>`
    + G(0, `<path fill="url(#gf-rock2)" stroke="#17313b" stroke-width=".8" d="M44 48 h20 l4 16 h-28Z"/><path d="M54 48 l-3 8 l5 4 l-3 6" stroke="#17313b" stroke-width="1.4" fill="none"/>`)
    + G(1, [0, 1, 2, 3].map((k) => `<circle class="grain" style="animation-delay:${k * .3}s" cx="${156 + k * 10}" cy="${116 + k * 2}" r="2.6" fill="#c99a3c"/>`).join(""))
    + G(2, `<path fill="url(#gf-sand)" d="M226 190 Q270 150 320 162 V190Z"/>` + STRATA(250, 172, 70, 18, ["#e8cf96", "#d3b276", "#e8cf96"])) },
  meander: { pins: [[246, 50], [100, 64]], art: `<rect width="320" height="190" fill="url(#gf-grass)"/>` + FOREST(10, 90, 30, 4, .9) + FOREST(200, 310, 178, 5, .9)
    + `<path d="M-4 30 C110 -20 250 10 260 66 S160 110 126 92 S40 96 70 160 S240 200 330 150" stroke="#6a5a3d" stroke-opacity=".25" stroke-width="36" fill="none"/>`
    + `<path d="M-4 30 C110 -20 250 10 260 66 S160 110 126 92 S40 96 70 160 S240 200 330 150" stroke="url(#gf-sea)" stroke-width="26" fill="none"/>` + `<path class="river-flow" fill="none" d="M-4 30 C110 -20 250 10 260 66 S160 110 126 92 S40 96 70 160 S240 200 330 150"/>`
    + G(0, `<path d="M252 24 q26 34 4 70" stroke="#c8553d" stroke-width="5" fill="none" stroke-linecap="round" stroke-dasharray="2 6"/>` + LBL(292, 40, "cut bank", "খহনীয়া পাৰ", "middle", "bold"))
    + G(1, `<path fill="url(#gf-sand)" d="M96 40 q100 -8 120 22 q-46 -2 -120 -22Z"/>` + LBL(120, 30, "sand bar", "বালিচৰ", "middle", "bold")) },
  threeprofiles: { pins: [[54, 48], [160, 64], [270, 48]], art: SKYBG() + CLOUD(160, 26, .8)
    + G(0, `<path fill="url(#gf-snow)" d="M2 40 C24 140 84 140 106 40Z"/><path fill="url(#gf-rock)" d="M2 40 C24 140 84 140 106 40 L106 190 H2Z"/><path d="M28 132 Q54 146 80 132" stroke="#4f9fc4" stroke-width="4" fill="none"/>` + LBL(54, 182, "U valley · ice", "U উপত্যকা · বৰফ", "middle", "bold"))
    + G(1, `<rect x="112" y="140" width="96" height="50" fill="url(#gf-sand)"/><path fill="url(#gf-sand)" d="M112 140 C134 140 140 82 166 82 C176 82 194 134 208 140Z"/><path d="M128 120 q20 -10 40 -24" stroke="#c99a3c" stroke-width="1.2" fill="none"/>` + AR(116, 70, 152, 72, "wind") + LBL(160, 182, "dune · wind", "বালিয়াড়ি · বতাহ", "middle", "bold"))
    + G(2, `<path fill="url(#gf-rock)" d="M214 190 V44 H262 L268 150 H320 V190Z"/>` + FOREST(220, 258, 46, 3, .8) + `<rect x="268" y="150" width="52" height="40" fill="url(#gf-sea)"/>` + FOAM(156, 268, 320) + LBL(270, 182, "cliff · waves", "শিলাপাৰ · ঢৌ", "middle", "bold")) },
  climategraph: { pins: [[150, 100], [226, 34]], art: R(0, 0, 320, 190, "paper") + `<rect x="34" y="16" width="270" height="144" rx="8" fill="#fff" filter="url(#gf-shadow)"/>` + [50, 82, 114, 146].map((y) => `<path d="M40 ${y} H298" stroke="#e8dfca"/>`).join("")
    + G(0, `<path d="M40 112 C100 92 200 94 298 108" stroke="#1d6f96" stroke-width="5" fill="none" stroke-linecap="round" opacity=".85"/>` + LBL(66, 132, "30-year mean", "৩০ বছৰৰ গড়", "start", "bold"))
    + G(1, `<path class="spark" fill="none" d="M40 126 L70 106 L100 120 L134 98 L180 112 L212 112 L226 32 L240 112 L272 96 L298 120"/>` + `<g transform="translate(226 20)"><path fill="#fff" stroke="#17313b" stroke-width=".8" d="M-12 4 a8 8 0 0 1 4 -12 a10 10 0 0 1 18 2 a6 6 0 0 1 2 10Z"/><path d="M-2 6 l-3 7 h4 l-3 7" stroke="#f2b43b" stroke-width="2" fill="none"/></g>`)
    + LBL(170, 180, "time →", "সময় →") },
  seabreeze: { pins: [[90, 92], [246, 140]], art: SKYBG() + SUNR(276, 30, 14) + `<rect x="166" y="150" width="154" height="40" fill="url(#gf-sea)"/>` + FOAM(158, 166, 320)
    + GROUND("M0 190 V146 Q80 140 170 150 V190Z", "url(#gf-sand)") + HOUSE(40, 146) + TREE(120, 146, 1.2) + `<path d="M150 150 v-30 l14 8 l-14 8" stroke="#17313b" fill="#e0563b" stroke-width="1"/>`
    + G(0, [62, 92, 122].map((x, k) => CURVE(`M${x} 138 C${x - 14} 110 ${x + 14} 90 ${x} 58`, "warm d" + k)).join("") + LBL(92, 48, "warm air rises", "গৰম বায়ু উঠে", "middle", "bold"))
    + G(1, AR(250, 136, 152, 136, "cool") + AR(150, 54, 240, 54, "cool2") + CURVE("M248 60 C256 90 256 110 252 130", "cool") + LBL(250, 120, "sea breeze", "সাগৰৰ বতাহ", "middle", "bold")) },
  pressure: { pins: [[80, 96], [244, 96]], art: R(0, 0, 320, 190, "paper")
    + G(0, `<circle cx="80" cy="96" r="70" fill="#1d6f96" opacity=".12"/>` + [66, 46, 26].map((r) => C(80, 96, r, "iso")).join("") + LBL(80, 104, "H", "H", "middle", "big") + LBL(80, 182, "cool, heavy air", "শীতল গধুৰ বায়ু", "middle", "bold"))
    + G(1, `<circle cx="244" cy="96" r="70" fill="#e0702f" opacity=".12"/>` + [66, 46, 26].map((r) => C(244, 96, r, "iso")).join("") + LBL(244, 104, "L", "L", "middle", "big") + LBL(244, 182, "warm, rising air", "উষ্ণ উঠা বায়ু", "middle", "bold"))
    + [78, 96, 114].map((y) => CURVE(`M116 ${y} C150 ${y - 6} 176 ${y + 6} 204 ${y}`, "cool")).join("") + [78, 96, 114].map((y) => AR(196, y, 208, y, "cool")).join("") },
  infiltrate: { pins: [[120, 142], [240, 70]], art: SKYBG() + CLOUD(80, 22, 1.1) + CLOUD(150, 18, .9) + DROPS([50, 80, 110, 140, 170], 30, 52)
    + `<path fill="#8d6748" d="M0 62 Q160 20 320 104 V190 H0Z"/>` + STRATA(0, 150, 320, 40, ["#a7835f", "#7a5a40"]).replace(/<rect /g, '<rect opacity=".7" ') + `<path d="M0 62 Q160 20 320 104" stroke="url(#gf-grass)" stroke-width="8" fill="none"/>` + FOREST(20, 140, 60, 5, .8)
    + G(0, [66, 104, 148].map((x, k) => `<path class="soak d${k}" d="M${x} 58 V148"/>`).join("") + `<rect x="0" y="160" width="320" height="30" fill="#4f9fc4" opacity=".5"/>` + LBL(70, 180, "groundwater", "ভূগৰ্ভৰ পানী", "start", "bold"))
    + G(1, CURVE("M170 46 C214 54 262 76 306 102", "cool") + `<path d="M296 104 q10 4 24 4" stroke="url(#gf-sea)" stroke-width="10"/>`) },
  ridge: { pins: [[92, 96], [236, 112]], art: SKYBG() + HAZE(120) + MTN([[160, 140, 74], [120, 90, 50], [204, 96, 54]], 170, true) + GROUND("M0 190 V164 L320 170 V190Z")
    + G(0, `<rect x="0" y="164" width="140" height="26" fill="url(#gf-grass)"/>` + FOREST(10, 120, 168, 7, 1) + CLOUD(104, 56, 1.4) + CLOUD(70, 70, 1) + CURVE("M4 140 C56 128 96 108 132 74", "cool") + DROPS([84, 100, 116, 132], 76, 124) + LBL(56, 186, "windward · wet", "বায়ুমুখী · সেমেকা", "middle", "bold"))
    + G(1, `<rect x="210" y="166" width="110" height="24" fill="url(#gf-sand)"/>` + CURVE("M186 66 C214 90 244 120 302 134", "warm") + LBL(262, 186, "rain shadow · dry", "বৃষ্টিছায়া · শুকান", "middle", "bold")) + SUNR(292, 26, 10) },
  shelf: { pins: [[262, 168], [150, 120], [60, 84]], art: SKYBG(56) + `<rect y="50" width="320" height="140" fill="url(#gf-sea)"/>` + FOAM(56) + `<path fill="url(#gf-land)" d="M0 30 L60 36 L84 50 H0Z"/>` + HOUSE(24, 36, .8) + TREE(46, 36, .8)
    + `<path fill="url(#gf-sand)" filter="url(#gf-shadow)" d="M0 50 L100 70 L196 150 L320 172 V190 H0Z"/>` + `<g opacity=".35" fill="#fff">${[[40, 80], [140, 120], [250, 176]].map(([x, y]) => `<path d="M${x} ${y} q4 -10 8 0 q4 -10 8 0"/>`).join("")}</g>`
    + G(2, `<path d="M0 50 L100 70" stroke="#e0563b" stroke-width="5" stroke-linecap="round"/>`) + G(1, `<path d="M100 70 L196 150" stroke="#e0563b" stroke-width="5" stroke-linecap="round"/>`) + G(0, `<path d="M196 150 L320 172" stroke="#e0563b" stroke-width="5" stroke-linecap="round"/>`) },
  wave: { pins: [[150, 56], [44, 140], [262, 100]], art: SKYBG(110) + CLOUD(260, 30, 1) + BIRDS(70, 30) + `<rect y="104" width="320" height="86" fill="url(#gf-sea)"/>`
    + G(0, `<path class="wgo" d="M-80 96 q20 -26 40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 t40 0 V200 H-80Z"/>` + FOAM(90, -10, 320, 3))
    + G(1, `<rect x="30" y="64" width="14" height="110" rx="3" fill="#fff" stroke="#17313b"/>` + [80, 100, 120, 140, 160].map((y) => `<path d="M30 ${y} h6" stroke="#17313b"/>`).join("") + AR(54, 90, 54, 150, "warm") + AR(64, 150, 64, 96, "warm"))
    + G(2, AR(214, 168, 304, 168, "cool") + AR(224, 150, 300, 150, "cool")) },
  tide: { pins: [[84, 76], [84, 136], [40, 30]], art: SKYBG() + `<g class="tideg"><rect y="104" width="320" height="100" fill="url(#gf-sea)"/>${FOAM(110, 0, 200)}</g>`
    + G(0, `<path d="M0 76 H230" stroke="#1d6f96" stroke-width="3" stroke-dasharray="8 5"/>` + LBL(150, 70, "high tide", "জোৱাৰ", "middle", "bold")) + G(1, `<path d="M0 136 H210" stroke="#e0563b" stroke-width="3" stroke-dasharray="8 5"/>` + LBL(150, 130, "low tide", "ভাটা", "middle", "bold"))
    + `<path fill="url(#gf-sand)" filter="url(#gf-shadow)" d="M150 190 C200 150 240 96 270 60 L322 44 V190Z"/>` + FOREST(272, 316, 52, 3, .9) + HOUSE(252, 86, .9) + G(2, `<circle cx="40" cy="30" r="26" fill="url(#gf-glow)"/><circle cx="40" cy="30" r="15" class="moon"/>`) },
  exposure: { pins: [[60, 120], [228, 128]], art: SKYBG() + CLOUD(70, 30, 1) + `<path fill="url(#gf-grass)" d="M0 190 V150 H320 V190Z"/>`
    + G(0, `<path class="wgo" d="M-40 138 q20 -16 40 0 t40 0 t40 0 t40 0 t40 0 V200 H-40Z"/><rect y="146" width="134" height="44" fill="#4f9fc4" opacity=".55"/>` + LBL(60, 182, "flood can reach", "বান পাব পাৰে", "middle", "bold"))
    + G(1, [176, 206, 236, 266].map((x) => HOUSE(x, 150, 1.4)).join("") + `<path d="M140 166 H320" class="road"/>` + LBL(232, 186, "homes and road", "ঘৰ আৰু পথ", "middle", "bold")) },
  cyclone: { pins: [[160, 92], [74, 150], [266, 150]], art: `<rect width="320" height="190" fill="url(#gf-sea)"/>` + FOAM(170, 0, 320, 3)
    + G(0, `<circle cx="160" cy="92" r="70" fill="#fff" opacity=".08"/><g class="spin">${[0, 72, 144, 216, 288].map((a) => `<path class="swirl" transform="rotate(${a} 160 92)" d="M160 92 C150 50 210 34 238 70"/>`).join("")}</g>` + `<circle cx="160" cy="92" r="8" fill="#17313b"/>`)
    + G(1, `<path fill="#1d6f96" d="M20 190 Q74 116 128 190Z"/>` + FOAM(130, 50, 100, 3))
    + G(2, `<path fill="url(#gf-rock)" d="M214 190 L240 172 L290 168 L316 190Z"/>` + AR(264, 166, 264, 130, "warm")) },
  surge: { pins: [[80, 52], [240, 112], [240, 168]], art: SKYBG(112) + G(0, `<g class="spin">${[0, 120, 240].map((a) => `<path class="swirl" style="stroke:#9fb6c3" transform="rotate(${a} 70 54)" d="M70 54 C64 30 92 18 112 38"/>`).join("")}</g>` + AR(120, 88, 160, 92, "wind") + AR(120, 100, 160, 104, "wind"))
    + `<rect y="112" width="320" height="78" fill="url(#gf-sea)"/>` + G(1, `<path fill="#1d6f96" d="M120 112 Q200 66 280 112Z"/>` + FOAM(84, 170, 240, 3))
    + G(2, `<path fill="url(#gf-rock)" d="M170 190 L200 164 L224 172 L252 152 L306 190Z"/>` + AR(236, 150, 236, 124, "warm")) + `<path fill="url(#gf-sand)" d="M280 112 L320 96 V112Z"/>` + HOUSE(306, 100, .8) },
  sunrise: { pins: [[284, 120], [36, 120]], art: `<rect width="320" height="190" fill="#18304a"/><rect width="320" height="190" fill="url(#gf-sky)" opacity=".0"/><path d="M160 0 H320 V190 H160Z" fill="#f6c58b" opacity=".85"/><path d="M200 0 H320 V190 H200Z" fill="#ffd9a3"/>`
    + SUNR(288, 70, 22) + `<path fill="#2b3d52" d="M0 190 V120 Q160 92 320 120 V190Z"/><path fill="url(#gf-land)" d="M160 190 V108 Q240 98 320 120 V190Z"/>`
    + G(0, HOUSE(284, 120, 1.4)) + G(1, HOUSE(36, 120, 1.4, "#3d4e63")) + AR(250, 150, 70, 150, "warm") + LBL(160, 170, "1° = 4 minutes", "১° = ৪ মিনিট", "middle", "bold") + LBL(70, 40, "still dark", "এতিয়াও আন্ধাৰ", "middle", "bold").replace("gf-t", "gf-t night-t") },
  himabelts: { pins: [[252, 140], [156, 92], [62, 34]], art: SKYBG() + CLOUD(250, 30, 1) + HAZE(100, "#bcd3dd", .6)
    + G(2, MTN([[66, 170, 64], [26, 130, 40], [104, 140, 46]], 190, true)) + G(1, MTN([[156, 106, 44], [184, 90, 36]], 190, false) + FOREST(128, 196, 166, 5, .9, true))
    + G(0, `<path fill="url(#gf-grass)" d="M206 190 V148 Q236 126 266 144 Q280 138 294 150 V190Z"/>` + FOREST(210, 290, 164, 5, .8))
    + `<rect x="290" y="150" width="30" height="40" fill="url(#gf-alluv)"/>` + LBL(20, 184, "N", "উ", "middle", "bold") + LBL(306, 184, "S", "দ", "middle", "bold") },
  alluvium: { pins: [[90, 104], [244, 70]], art: SKYBG() + SUNR(272, 28, 12)
    + G(0, `<path fill="url(#gf-alluv)" d="M0 190 V130 Q70 118 156 126 V190Z"/>` + STRATA(0, 150, 156, 40, ["#b3cc80", "#9ab665", "#c0d68f"]).replace(/<rect /g, '<rect opacity=".8" ') + `<path d="M0 124 Q70 112 156 118" stroke="url(#gf-sea)" stroke-width="6" fill="none"/>` + `<g>${[20, 50, 80, 110, 140].map((x) => `<path d="M${x} 130 v-8 m-3 4 l3 -4 l3 4" stroke="#5f8a3a" stroke-width="1.4" fill="none"/>`).join("")}</g>` + LBL(78, 182, "river-built", "নদীয়ে গঢ়া", "middle", "bold"))
    + G(1, `<path fill="url(#gf-sand)" d="M164 190 V132 Q188 86 214 124 Q242 72 278 124 Q298 108 320 130 V190Z"/><path d="M176 120 q30 -20 60 -10" stroke="#c99a3c" stroke-width="1.2" fill="none"/>` + `<g transform="translate(296 128)"><rect x="-2" y="-14" width="4" height="16" fill="#6b8f3a"/><rect x="-7" y="-10" width="3" height="8" fill="#6b8f3a"/></g>` + LBL(240, 182, "wind-built", "বতাহে গঢ়া", "middle", "bold")) },
  gap: { pins: [[256, 70], [176, 108], [88, 84]], art: SKYBG() + HAZE(110, "#c2d6de")
    + G(2, MTN([[56, 110, 56], [100, 84, 44]], 190, false) + FOREST(20, 130, 186, 6, .8) + LBL(60, 182, "Chota Nagpur", "ছোটনাগপুৰ", "middle", "bold"))
    + G(1, `<path fill="url(#gf-alluv)" d="M136 190 V126 H216 V190Z"/><path d="M136 132 Q176 122 216 132" stroke="url(#gf-sea)" stroke-width="6" fill="none"/>` + LBL(176, 182, "gap", "ফাঁক", "middle", "bold"))
    + G(0, MTN([[256, 120, 52], [296, 96, 40]], 190, false) + FOREST(222, 316, 186, 6, .8, true) + CLOUD(266, 40, .9) + LBL(266, 182, "Meghalaya", "মেঘালয়", "middle", "bold")) },
  coastcut: { pins: [[66, 140], [246, 140]], art: SKYBG() + `<rect y="150" width="60" height="40" fill="url(#gf-sea)"/><rect x="262" y="150" width="58" height="40" fill="url(#gf-sea)"/>` + FOAM(158, 0, 60) + FOAM(158, 262, 320)
    + MTN([[92, 126, 40], [126, 104, 40]], 190, false) + `<path fill="url(#gf-rock)" d="M84 190 L160 92 L262 150 L276 190Z" opacity=".75"/>` + FOREST(90, 140, 120, 4, .8)
    + G(0, `<path fill="url(#gf-grass)" d="M46 190 L60 146 L84 146 V190Z"/>` + LBL(60, 184, "narrow west", "ঠেক পশ্চিম", "middle", "bold"))
    + G(1, `<path fill="url(#gf-alluv)" d="M180 190 V138 L262 148 L276 190Z"/>` + `<path d="M190 160 Q230 150 270 162" stroke="url(#gf-sea)" stroke-width="4" fill="none"/>` + LBL(230, 184, "broad east", "বহল পূব", "middle", "bold")) },
  watershed: { pins: [[160, 26], [160, 126]], art: `<rect width="320" height="190" fill="url(#gf-grass)"/>` + MTN([[40, 46, 46], [110, 52, 50], [210, 50, 50], [284, 44, 44]], 46, false) + FOREST(20, 300, 64, 12, .7, true) + FOREST(30, 120, 160, 5, .8)
    + G(0, `<path d="M0 30 Q80 12 160 30 T320 24" stroke="#c8553d" stroke-width="4" fill="none" stroke-dasharray="2 6" stroke-linecap="round"/>` + LBL(260, 16, "divide", "জলবিভাজিকা", "middle", "bold"))
    + ["M60 44 C80 92 120 112 160 128", "M262 44 C232 92 200 112 160 128", "M160 46 C160 82 158 106 160 128", "M160 128 C160 152 172 172 162 192"].map((d) => `<path d="${d}" stroke="url(#gf-sea)" stroke-width="6" fill="none" stroke-linecap="round"/><path d="${d}" class="river-flow" fill="none"/>`).join("")
    + G(1, `<circle cx="160" cy="128" r="10" fill="#fff" opacity=".6"/>`) },
  mouths: { pins: [[86, 92], [246, 92]], art: `<rect width="320" height="120" fill="url(#gf-grass)"/><rect y="118" width="320" height="72" fill="url(#gf-sea)"/>` + FOAM(130) + FOREST(150, 200, 40, 3, .8) + `<path d="M160 0 V190" stroke="#fff" stroke-width="3"/>`
    + G(0, `<path fill="url(#gf-alluv)" d="M24 118 Q86 170 148 118 L86 64Z"/><path d="M86 0 V70" stroke="url(#gf-sea)" stroke-width="10"/><path d="M86 70 L38 132 M86 70 L66 142 M86 70 L106 142 M86 70 L134 132" stroke="#4f9fc4" stroke-width="4" fill="none" stroke-linecap="round"/>` + LBL(86, 184, "fan · delta", "পাখি · বদ্বীপ", "middle", "bold"))
    + G(1, `<path fill="url(#gf-sea)" d="M236 0 L252 0 L306 190 L186 190Z"/>` + FOAM(130, 200, 300) + LBL(246, 184, "funnel · estuary", "চুঙা · মোহনা", "middle", "bold")) },
  rainseason: { pins: [[164, 34], [252, 56]], art: R(0, 0, 320, 190, "paper") + `<rect x="10" y="10" width="300" height="168" rx="12" fill="#fff" filter="url(#gf-shadow)"/>`
    + G(0, `<rect x="134" y="20" width="94" height="128" rx="10" fill="#1d6f96" opacity=".12"/>` + CLOUD(182, 34, .8)) + ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"].map((m, k) => `<text class="gf-t" x="${33 + k * 23.5}" y="168" text-anchor="middle">${m}</text>`).join("")
    + [6, 6, 10, 18, 30, 70, 92, 84, 62, 30, 12, 6].map((h, k) => BAR(24 + k * 23.5, 150, 18, h, k > 4 && k < 9 ? "bwater" : "bmute")).join("") + G(1, `<path d="M244 24 v124" stroke="#e0563b" stroke-width="2" stroke-dasharray="4 4"/>`) },
  onsetdates: { pins: [[160, 56], [96, 132]], art: R(0, 0, 320, 190, "paper") + `<rect x="10" y="20" width="300" height="134" rx="12" fill="#fff" filter="url(#gf-shadow)"/><path d="M24 116 H296" stroke="#9aa7ab" stroke-width="2"/>` + ["May 25", "Jun 1", "Jun 8"].map((d, k) => `<text class="gf-t" x="${60 + k * 100}" y="146" text-anchor="middle">${d}</text>`).join("")
    + G(0, `<path d="M160 40 V116" stroke="#1d6f96" stroke-width="3"/>` + `<rect x="114" y="28" width="92" height="22" rx="11" fill="#1d6f96"/><text x="160" y="43" text-anchor="middle" fill="#fff" font-weight="800" font-size="11">normal date</text>`)
    + G(1, [[82, 0], [126, 1], [150, 0], [196, 1], [234, 0], [110, 2]].map(([x, r], k) => `<circle cx="${x}" cy="${100 - r * 12}" r="7" fill="#e0563b" stroke="#fff" stroke-width="2" filter="url(#gf-shadow)"/>`).join("")) + LBL(160, 176, "each dot = one year's onset (illustrative)", "প্ৰতিটো বিন্দু = এবছৰৰ আগমন (উদাহৰণ)") },
  stationbars: { pins: [[94, 26], [234, 26]], art: R(0, 0, 320, 190, "paper") + `<rect x="10" y="12" width="148" height="166" rx="12" fill="#fff" filter="url(#gf-shadow)"/><rect x="162" y="12" width="148" height="166" rx="12" fill="#fff" filter="url(#gf-shadow)"/>`
    + G(0, [8, 12, 26, 48, 70, 78, 84, 68, 52, 28, 10, 6].map((h, k) => BAR(22 + k * 11, 150, 9, h, k === 6 ? "bwater" : "bmute")).join("") + LBL(84, 170, "Guwahati · July", "গুৱাহাটী · জুলাই", "middle", "bold"))
    + G(1, [8, 4, 4, 6, 10, 14, 26, 30, 32, 84, 76, 28].map((h, k) => BAR(174 + k * 11, 150, 9, h, k === 9 ? "bwater" : "bmute")).join("") + LBL(236, 170, "Chennai · October", "চেন্নাই · অক্টোবৰ", "middle", "bold")) },
  soilcut: { pins: [[86, 56], [234, 56]], art: SKYBG(46) + `<rect y="40" width="320" height="8" fill="url(#gf-grass)"/>` + FOREST(10, 300, 44, 10, .7)
    + G(0, `<g filter="url(#gf-shadow)">${STRATA(26, 48, 120, 132, ["#c8b07a", "#b39a64", "#c9b585", "#a68b57"])}</g>` + `<g fill="#6b5a3a" opacity=".7">${Array.from({ length: 22 }, (_, k) => `<circle cx="${32 + (k * 37) % 108}" cy="${58 + (k * 29) % 116}" r="${1 + k % 3}"/>`).join("")}</g>` + LBL(86, 186, "alluvial · layered silt", "পলসুৱা · স্তৰীভূত পলস", "middle", "bold"))
    + G(1, `<rect x="174" y="48" width="120" height="132" fill="#36302c" filter="url(#gf-shadow)"/><path d="M204 48 l10 44 l-6 26 l8 30 M254 48 l-8 54 l10 40" stroke="#8d847a" stroke-width="1.8" fill="none"/>` + LBL(234, 186, "black · cracks when dry", "ক'লা · শুকালে ফাটে", "middle", "bold")) },
  raingradient: { pins: [[54, 70], [262, 70], [160, 146]], art: SKYBG() + SUNR(286, 26, 12) + CLOUD(50, 22, 1.1) + DROPS([20, 40, 60, 80], 28, 52) + `<path fill="url(#gf-grass)" d="M0 190 V120 H120 V190Z"/><path fill="url(#gf-sand)" d="M200 190 V120 H320 V190Z"/>`
    + G(0, FOREST(6, 112, 120, 6, 1.6)) + G(1, [222, 252, 284, 306].map((x) => `<path d="M${x} 122 V96 M${x} 108 l-9 -8 M${x} 104 l9 -10" stroke="#6b7f3a" stroke-width="3" stroke-linecap="round"/>`).join(""))
    + G(2, `<rect x="110" y="122" width="100" height="68" fill="url(#gf-sea)"/>` + [134, 160, 186].map((x) => `<path d="M${x} 154 v-22 M${x} 154 l-9 14 M${x} 154 l9 14" stroke="#4f3b2a" stroke-width="2.4"/>` + `<circle cx="${x}" cy="128" r="11" fill="#2f7a4d"/>`).join("")) },
  cropbars: { pins: [[108, 30], [212, 30]], art: R(0, 0, 320, 190, "paper") + `<rect x="30" y="14" width="260" height="168" rx="12" fill="#fff" filter="url(#gf-shadow)"/><path d="M44 160 H276" stroke="#9aa7ab" stroke-width="2"/>`
    + G(0, BAR(72, 160, 72, 118, "bwater") + `<g>${[86, 100, 114, 128].map((x) => `<path d="M${x} 40 v10 m-3 -6 l3 -4 l3 4" stroke="#fff" stroke-width="1.4" fill="none"/>`).join("")}</g>` + LBL(108, 176, "Kharif 169.46", "খৰিফ ১৬৯.৪৬", "middle", "bold"))
    + G(1, BAR(176, 160, 72, 118, "bgold") + LBL(212, 176, "Rabi 169.17", "ৰবি ১৬৯.১৭", "middle", "bold")) },
  cropcalendar: { pins: [[98, 70], [222, 120]], art: R(0, 0, 320, 190, "paper") + `<circle cx="160" cy="95" r="82" fill="#fff" filter="url(#gf-shadow)"/>`
    + G(0, `<path fill="url(#gf-sea)" opacity=".85" d="M160 95 L${r1(160 + 76 * Math.sin(Math.PI * 5 / 6))} ${r1(95 - 76 * Math.cos(Math.PI * 5 / 6))} A76 76 0 0 1 ${r1(160 + 76 * Math.sin(Math.PI * 1.75))} ${r1(95 - 76 * Math.cos(Math.PI * 1.75))}Z"/>`.replace(/A76 76 0 0 1/, "A76 76 0 0 0"))
    + G(1, `<path fill="url(#gf-sand)" d="M160 95 L${r1(160 + 76 * Math.sin(Math.PI * 1.75))} ${r1(95 - 76 * Math.cos(Math.PI * 1.75))} A76 76 0 0 0 ${r1(160 + 76 * Math.sin(Math.PI / 3))} ${r1(95 - 76 * Math.cos(Math.PI / 3))}Z"/>`)
    + ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"].map((m, k) => { const a = (k + .5) * Math.PI / 6; return `<text class="gf-t" x="${r1(160 + 90 * Math.sin(a))}" y="${r1(99 - 90 * Math.cos(a))}" text-anchor="middle">${m}</text>`; }).join("")
    + `<circle cx="160" cy="95" r="34" fill="#fffaf0"/>` + LBL(160, 99, "one year", "এবছৰ", "middle", "bold") },
  density: { pins: [[86, 30], [236, 30]], art: R(0, 0, 320, 190, "paper")
    + G(0, `<rect x="26" y="40" width="120" height="120" rx="10" fill="url(#gf-grass)" filter="url(#gf-shadow)"/>` + Array.from({ length: 16 }, (_, k) => HOUSE(42 + (k % 4) * 29, 66 + Math.floor(k / 4) * 28, .9)).join(""))
    + G(1, `<rect x="174" y="40" width="120" height="120" rx="10" fill="url(#gf-grass)" filter="url(#gf-shadow)"/>` + [[196, 74], [262, 70], [226, 120], [276, 146], [194, 146]].map(([x, y]) => HOUSE(x, y, .9)).join("") + FOREST(200, 290, 100, 4, .7))
    + LBL(160, 182, "people ÷ area", "মানুহ ÷ কালি", "middle", "bold") },
  settlement: { pins: [[176, 110], [60, 52]], art: `<rect width="320" height="190" fill="url(#gf-grass)"/>` + MTN([[30, 60, 40], [86, 70, 44], [130, 50, 34]], 74, false) + FOREST(150, 310, 40, 8, .8)
    + `<path d="M0 154 C100 112 200 132 320 82" stroke="url(#gf-sea)" stroke-width="14" fill="none"/><path class="river-flow" fill="none" d="M0 154 C100 112 200 132 320 82"/>`
    + G(0, [[150, 112], [168, 106], [190, 108], [160, 128], [184, 126], [206, 120]].map(([x, y]) => HOUSE(x, y, 1)).join(""))
    + G(1, `<path d="M0 96 L130 110 L320 136" stroke="#5d5148" stroke-width="5" fill="none" stroke-dasharray="10 6" stroke-linecap="round"/>`) },
  forces2: { pins: [[84, 150], [244, 52]], art: SKYBG() + CLOUD(230, 22, 1.1) + DROPS([208, 230, 252], 30, 52) + `<path fill="url(#gf-mantle)" d="M0 190 V170 H320 V190Z"/>`
    + MTN([[60, 140, 70], [120, 96, 50]], 170, true) + `<path fill="url(#gf-rock)" d="M150 170 L200 104 L320 138 V170Z"/>` + FOREST(200, 310, 140, 6, .8)
    + G(0, AR(50, 188, 50, 100, "warm") + AR(110, 188, 110, 132, "warm") + LBL(84, 186, "push up · inside", "ভিতৰৰ ঠেলা", "middle", "bold").replace('y="186"', 'y="182"'))
    + G(1, CURVE("M196 104 C236 110 272 120 316 136", "cool") + LBL(256, 98, "wear down · outside", "বাহিৰৰ ক্ষয়", "middle", "bold")) },
  plainbelts4: { pins: [[70, 100], [140, 116], [212, 124], [282, 134]], art: SKYBG() + MTN([[30, 140, 50], [70, 110, 40]], 140, true)
    + G(0, `<path fill="url(#gf-rock2)" d="M30 190 L50 120 L104 130 V190Z"/>${Array.from({ length: 14 }, (_, k) => `<circle cx="${52 + (k * 13) % 48}" cy="${140 + (k * 17) % 44}" r="2.6" fill="#8a7a66"/>`).join("")}`)
    + G(1, `<path fill="#6fa25f" d="M104 190 V130 L176 138 V190Z"/>` + FOREST(108, 172, 140, 5, .9) + `<path d="M120 170 q20 -6 40 0" stroke="#4f9fc4" stroke-width="3" fill="none"/>`)
    + G(2, `<path fill="url(#gf-alluv)" d="M176 190 V138 L250 144 V190Z"/>` + `<path d="M176 138 L250 144" stroke="#7f9d45" stroke-width="2"/>`)
    + G(3, `<path fill="#d7e9a8" d="M250 190 V144 L300 148 V190Z"/><rect x="300" y="148" width="20" height="42" fill="url(#gf-sea)"/>`) },
  peaks3: { pins: [[62, 60], [160, 100], [262, 114]], art: SKYBG() + CLOUD(120, 30, .9) + CLOUD(270, 50, .7)
    + G(0, MTN([[62, 128, 64]], 190, true) + FOREST(10, 110, 186, 5, .7, true) + LBL(62, 182, "Saramati 3,826 m", "চাৰামাটি ৩,৮২৬ মি.", "middle", "bold"))
    + G(1, MTN([[160, 88, 54]], 190, false) + FOREST(120, 200, 186, 4, .8, true) + LBL(160, 182, "Phawngpui 2,157 m", "ফৱংপুই ২,১৫৭ মি.", "middle", "bold"))
    + G(2, `<path fill="url(#gf-grass)" d="M206 190 L262 128 L318 190Z"/>` + FOREST(220, 300, 184, 5, .7, true) + LBL(262, 182, "Shillong Peak 1,965 m", "শ্বিলং শিখৰ ১,৯৬৫ মি.", "middle", "bold")) },
  patterns4: { pins: [[80, 22], [240, 22], [80, 118], [240, 118]], art: R(0, 0, 320, 190, "paper") + [[6, 6], [166, 6], [6, 100], [166, 100]].map(([x, y]) => `<rect x="${x}" y="${y}" width="148" height="86" rx="10" fill="url(#gf-grass)" filter="url(#gf-shadow)"/>`).join("")
    + G(0, `<path d="M80 86 V40 M80 74 L52 50 M80 74 L108 50 M80 60 L62 34 M80 60 L98 34 M52 50 L40 58 M108 50 L120 58 M62 34 L54 26 M98 34 L106 26" stroke="#3b8dbb" stroke-width="3" fill="none" stroke-linecap="round"/>`)
    + G(1, MTN([[240, 30, 22]], 62, false) + [0, 1, 2, 3, 4, 5, 6, 7].map((k) => { const t = k * Math.PI / 4; return AR(r1(240 + 18 * Math.cos(t)), r1(52 + 16 * Math.sin(t)), r1(240 + 46 * Math.cos(t)), r1(52 + 34 * Math.sin(t)), "cool"); }).join(""))
    + G(2, [0, 1, 2].map((k) => `<path d="M${30 + k * 38} 108 V184" stroke="#a48a6e" stroke-width="10" opacity=".55"/>`).join("") + `<path d="M80 186 V110 M80 170 H52 M80 170 H108 M80 150 H52 M80 150 H108 M80 130 H58 M80 130 H102" stroke="#3b8dbb" stroke-width="3" fill="none" stroke-linecap="round"/>`)
    + G(3, `<ellipse cx="240" cy="146" rx="22" ry="14" fill="url(#gf-sea)"/>` + [0, 1, 2, 3, 4, 5, 6, 7].map((k) => { const t = k * Math.PI / 4; return AR(r1(240 + 66 * Math.cos(t) * .9), r1(146 + 36 * Math.sin(t)), r1(240 + 30 * Math.cos(t)), r1(146 + 18 * Math.sin(t)), "cool"); }).join("")) },
  prayag5: { pins: [[92, 36], [118, 66], [142, 96], [166, 126], [206, 156]], art: `<rect width="320" height="190" fill="url(#gf-grass)"/>` + MTN([[30, 50, 40], [80, 40, 30], [260, 56, 50], [300, 40, 30]], 60, true) + FOREST(180, 310, 110, 8, .8, true)
    + `<path d="M56 4 L92 36 L118 66 L142 96 L166 126 L206 156 L320 180" stroke="url(#gf-sea)" stroke-width="11" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path class="river-flow" fill="none" d="M56 4 L92 36 L118 66 L142 96 L166 126 L206 156 L320 180"/>`
    + `<path d="M136 12 L92 36 M174 30 L118 66 M216 50 L142 96 M256 78 L166 126 M300 104 L206 156" stroke="#5aa9cd" stroke-width="5" fill="none" stroke-linecap="round"/>`
    + `<rect x="190" y="166" width="96" height="20" rx="10" fill="#17313b"/><text x="238" y="180" text-anchor="middle" fill="#fff" font-size="11" font-weight="800">Ganga →</text>` },
  extremes4: { pins: IPIN([75.8, 34.4], [75, 28.3], [70.9, 26.9], [91.6, 25.3]), size: 300, art: IN(`<circle cx="${lx(75.8)}" cy="${ly(34.4)}" r="16" fill="#9fd3f5" opacity=".6"/><circle cx="${lx(75)}" cy="${ly(28.3)}" r="16" fill="#f08a24" opacity=".55"/><circle cx="${lx(70.9)}" cy="${ly(26.9)}" r="16" fill="#f2d48a" opacity=".7"/><circle cx="${lx(91.6)}" cy="${ly(25.3)}" r="16" fill="#1d6f96" opacity=".55"/>`) },
});

const pinsSVG = (kind, pick) => F[kind].pins.map(([x, y], k) => `<g class="gf-pin" ${pick ? `data-opt="${k}"` : `data-pin="${k}"`} role="button" tabindex="0" aria-label="${k + 1}"><circle class="tap" cx="${x}" cy="${y}" r="20"/><circle class="dot" cx="${x}" cy="${y}" r="12"/><text x="${x}" y="${y + 4.5}" text-anchor="middle">${k + 1}</text></g>`).join("");
const svg = (kind, pick) => { const f = F[kind], h = f.size || 190; return `<svg class="gf-svg gf-${kind}" viewBox="0 0 320 ${h}" role="img">${f.art}<rect class="gf-tex" width="320" height="${h}" filter="url(#gf-grain)"/>${pinsSVG(kind, pick)}</svg>`; };
const NOTE = B("Tap a number", "সংখ্যা এটা টিপা");
const PLAY = '<svg viewBox="0 0 16 16"><path d="M4 2.5v11l9-5.5z"/></svg>';
window.GEOFIG = {
  kinds: F,
  defs: DEFS, india: INDIA, lx, ly,
  kit: { R, C, P, G, TX, AR, CURVE, DROPS, BAR, CLOUD, HAZE, MTN, TREE, PINE, FOREST, HOUSE, FOAM, STRATA, LBL, SUNR, BIRDS, SKYBG, GROUND, INX, r1 },
  story: ({ kind, spots }, T) => { inject(); return `<figure class="gfig" data-gfig data-kind="${kind}"><div class="gf-stage">${svg(kind)}<div class="gf-call" aria-live="polite"></div></div>
    <div class="gf-note"><button type="button" class="gf-tour" data-tour>${PLAY}${T(B("Tour", "ভ্ৰমণ"))}</button><span>${T(NOTE)}</span><span class="gf-sch">${T(B("Schematic", "আঁচনিগত"))}</span></div>
    <div class="gf-spots">${spots.map((o, k) => `<button type="button" class="gf-spot" data-pin="${k}"><b>${k + 1}</b><span>${T(o)}</span></button>`).join("")}</div></figure>`; },
  quiz: (kind) => { inject(); return `<figure class="gfig quiz"><div class="gf-stage">${svg(kind, true)}</div></figure>`; },
};
const select = (root, k, keep) => {
  const same = !keep && root.dataset.on === String(k);
  if (same) delete root.dataset.on; else root.dataset.on = k;
  root.querySelectorAll("[data-part]").forEach((p) => { p.classList.toggle("dim", !same && p.dataset.part !== String(k)); p.classList.toggle("lit", !same && p.dataset.part === String(k)); });
  root.querySelectorAll("[data-pin]").forEach((p) => { const on = !same && p.dataset.pin === String(k); p.classList.toggle("on", on); if (on && p.classList.contains("gf-spot")) p.classList.add("seen"); });
  const call = root.querySelector(".gf-call"), spot = root.querySelector(`.gf-spot[data-pin="${k}"] span`), pin = F[root.dataset.kind]?.pins[k];
  if (!call) return;
  if (same || !spot || !pin) { call.classList.remove("show"); return; }
  const vb = root.querySelector("svg").viewBox.baseVal, x = (pin[0] / vb.width) * 100, y = (pin[1] / vb.height) * 100;
  call.innerHTML = spot.innerHTML; call.style.left = `${Math.min(80, Math.max(20, x))}%`; call.style.top = `${y}%`;
  call.classList.toggle("below", y < 34); call.classList.add("show");
};
const tours = new WeakMap();
const stopTour = (root) => { clearInterval(tours.get(root)); tours.delete(root); root.querySelector("[data-tour]")?.classList.remove("playing"); };
document.addEventListener("click", (e) => {
  const t = e.target.closest?.("[data-gfig] [data-tour]");
  if (t) {
    const root = t.closest("[data-gfig]"); if (tours.has(root)) return stopTour(root);
    const n = root.querySelectorAll(".gf-spot").length; let k = 0; t.classList.add("playing"); select(root, 0, true);
    tours.set(root, setInterval(() => { k++; if (k >= n || !root.isConnected) return stopTour(root); select(root, k, true); }, 2200));
    return;
  }
  const pin = e.target.closest?.("[data-gfig] [data-pin]");
  if (pin) { const root = pin.closest("[data-gfig]"); stopTour(root); select(root, pin.dataset.pin); }
});
})();
