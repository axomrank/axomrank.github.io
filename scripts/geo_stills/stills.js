/* Still images for Physical and Indian Geography Foundations, drawn with the same kit as
   app/geofigure.js. Each entry keeps the letters, numbers and data the lessons refer to.
   Render: scripts/geo_stills/render.sh (writes content/media/gf-NN-…/name.webp). */
(() => {
const { R, C, P, TX, AR, CURVE, DROPS, BAR, CLOUD, HAZE, MTN, FOREST, HOUSE, FOAM, STRATA, LBL, SUNR, BIRDS, GROUND, INX, r1, PINE, TREE } = GEOFIG.kit;
const { lx, ly } = GEOFIG;
const W = 320, H = 180;
const SKY = `<rect width="${W}" height="${H}" fill="url(#gf-sky)"/>`;
const PAPER = `<rect width="${W}" height="${H}" fill="url(#gf-paper)"/>`;
const NIGHT = `<rect width="${W}" height="${H}" fill="url(#gf-night)"/>` + Array.from({ length: 30 }, (_, k) => `<circle cx="${(k * 97) % W}" cy="${(k * 53) % H}" r="${k % 3 ? .6 : 1}" fill="#fff" opacity=".7"/>`).join("");
// a letter badge the lessons refer to
const L = (x, y, t, dark, r = 9) => `<g filter="url(#gf-shadow)"><circle cx="${x}" cy="${y}" r="${r}" fill="${dark ? "#17313b" : "#fff"}" stroke="${dark ? "#fff" : "#17313b"}" stroke-width="1.6"/><text x="${x}" y="${y + 4}" text-anchor="middle" font-weight="800" font-size="11" fill="${dark ? "#fff" : "#17313b"}">${t}</text></g>`;
const T = (x, y, s, o = {}) => `<text x="${x}" y="${y}" text-anchor="${o.a || "middle"}" font-size="${o.s || 8}" font-weight="${o.w || 700}" fill="${o.c || "#17313b"}" paint-order="stroke" stroke="${o.h === false ? "none" : "rgba(255,255,255,.85)"}" stroke-width="2.4" stroke-linejoin="round" ${o.i ? 'font-style="italic"' : ""}>${s}</text>`;
const NORTH = (x, y, c = "#17313b") => `<g transform="translate(${x} ${y})" filter="url(#gf-shadow)"><circle r="11" fill="#fff"/><path d="M0 -8 L4 4 L0 1 L-4 4Z" fill="#e0563b"/>${T(0, -14, "N", { s: 8, w: 800 })}</g>`;
const CARD = (x, y, w, h, fill = "#fff") => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="8" fill="${fill}" filter="url(#gf-shadow)"/>`;
// India in a 16:9 frame
const IND = (inner, dx = 64, s = .6, dy = 0) => `<g transform="translate(${dx} ${dy}) scale(${s})">${INX(inner).replace('<rect width="320" height="300" fill="url(#gf-ocean)"/>', '<rect x="-260" y="-200" width="840" height="700" fill="url(#gf-ocean)"/>').replace(/M0 (\d)/g, "M-260 $1").replace(/ H320"/g, ' H580"')}</g>`;
const at = (lon, lat, dx = 64, s = .6, dy = 0) => [r1(dx + lx(lon) * s), r1(dy + ly(lat) * s)];
const riv = (pts, c = "#1d6f96") => `<path d="M${pts.map(([a, b]) => `${lx(a)} ${ly(b)}`).join(" L")}" stroke="${c}" stroke-width="4.5" fill="none" stroke-linejoin="round" stroke-linecap="round"/>` + (() => { const [a, b] = pts[pts.length - 2], [c2, d] = pts[pts.length - 1]; const x1 = lx(a), y1 = ly(b), x2 = lx(c2), y2 = ly(d), an = Math.atan2(y2 - y1, x2 - x1), f = (q) => `${r1(x2 - 10 * Math.cos(an + q))} ${r1(y2 - 10 * Math.sin(an + q))}`; return `<path d="M${x2} ${y2} L${f(.5)} L${f(-.5)}Z" fill="${c}"/>`; })();
const BARS = (vals, labels, x0, base, gap, max, fill) => vals.map((v, k) => { const h = (v / max) * 118, x = x0 + k * gap; return `<rect x="${x}" y="${r1(base - h)}" width="${gap * .55}" height="${r1(h)}" rx="3" fill="${fill(k)}" filter="url(#gf-shadow)"/>` + T(x + gap * .275, r1(base - h - 5), v, { s: 7.5 }) + T(x + gap * .275, base + 12, labels[k], { s: 8, w: 800 }); }).join("");
const AXIS = (x, base, max, step, w) => Array.from({ length: max / step + 1 }, (_, k) => { const y = r1(base - (k * step / max) * 118); return `<path d="M${x} ${y} H${x + w}" stroke="#e5dcc8" stroke-width=".8"/>` + T(x - 4, y + 3, k * step, { a: "end", s: 6.5, w: 600, c: "#6a7c83" }); }).join("") + T(x - 4, base - 128, "mm", { a: "end", s: 6.5, c: "#6a7c83" });

window.STILLS = {
  "gf-01-map-skills/symbols": () => `<rect width="${W}" height="${H}" fill="url(#gf-grass)"/>` + FOREST(20, 120, 40, 6, .9) + MTN([[250, 40, 22], [280, 30, 18]], 52, false)
    + `<path d="M0 132 C60 118 110 150 170 136 S270 120 320 140" stroke="#5aa9cd" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M0 132 C60 118 110 150 170 136 S270 120 320 140" class="river-flow" stroke="#e9f7ff" stroke-width="2" stroke-dasharray="8 14" fill="none"/>`
    + `<path d="M40 86 H280" stroke="#4d8a3a" stroke-width="5" stroke-linecap="round"/>` + HOUSE(150, 80, 1) + HOUSE(170, 80, .9, "#1d6f96") + L(60, 86, "A") + L(260, 86, "B") + NORTH(296, 26)
    + CARD(8, 150, 140, 24) + `<path d="M16 162 q5 -4 10 0 t10 0" stroke="#5aa9cd" stroke-width="3" fill="none"/>` + T(40, 165, "≈ river", { a: "start", s: 7.5 }) + `<path d="M84 162 h16" stroke="#4d8a3a" stroke-width="3"/>` + T(104, 165, "— road", { a: "start", s: 7.5 }),
  "gf-01-map-skills/grid": () => PAPER + CARD(40, 14, 240, 150, "#f6efd9") + `<path fill="url(#gf-grass)" opacity=".55" d="M70 40 q60 -20 120 10 q50 30 60 80 q-60 20 -110 0 q-60 -10 -70 -90Z"/>`
    + [30, 20, 10].map((v, k) => `<path d="M70 ${34 + k * 52} H260" stroke="#7c8f96" stroke-width="1" stroke-dasharray="3 3"/>` + T(64, 37 + k * 52, `${v}°N`, { a: "end", s: 8 })).join("")
    + [70, 80, 90].map((v, k) => `<path d="M${90 + k * 75} 26 V150" stroke="#7c8f96" stroke-width="1" stroke-dasharray="3 3"/>` + T(90 + k * 75, 160, `${v}°E`, { s: 8 })).join("")
    + `<circle cx="165" cy="34" r="4" fill="#e0563b"/>` + L(178, 26, "A") + `<circle cx="240" cy="86" r="4" fill="#e0563b"/>` + L(253, 78, "B") + `<circle cx="90" cy="138" r="4" fill="#e0563b"/>` + L(103, 130, "C"),
  "gf-01-map-skills/scale": () => `<rect width="${W}" height="${H}" fill="url(#gf-grass)"/>` + FOREST(10, 90, 150, 5, .8) + FOREST(230, 310, 40, 5, .8) + NORTH(296, 150)
    + `<path d="M40 76 H280" stroke="#5d5148" stroke-width="4" stroke-dasharray="9 5" stroke-linecap="round"/>` + HOUSE(40, 72, 1) + HOUSE(220, 72, 1, "#1d6f96") + HOUSE(280, 72, 1, "#7a5c9a")
    + L(40, 96, "A") + L(220, 96, "B") + L(280, 96, "C")
    + CARD(40, 126, 150, 40) + `<rect x="54" y="138" width="60" height="7" fill="#17313b"/><rect x="114" y="138" width="60" height="7" fill="#fff" stroke="#17313b"/>` + T(54, 157, "0", { s: 8 }) + T(114, 157, "2", { s: 8 }) + T(174, 157, "4 km", { s: 8 }),
  "gf-01-map-skills/contours": () => PAPER + CARD(14, 12, 140, 156, "#f6efd9") + CARD(166, 12, 140, 156, "#f6efd9")
    + [0, 1, 2].map((k) => `<path d="M${52 + k * 10} 30 l10 22 l-10 22 l10 22 l-10 22 l10 22" stroke="#7c6550" stroke-width="1.6" fill="none"/>` + T(57 + k * 10, 18 + k * 7, [100, 120, 140][k], { s: 6 })).join("")
    + [0, 1, 2].map((k) => `<path d="M${196 + k * 36} 30 l10 22 l-10 22 l10 22 l-10 22 l10 22" stroke="#7c6550" stroke-width="1.6" fill="none"/>` + T(200 + k * 36, 26, [100, 120, 140][k], { s: 6.5 })).join("")
    + `<path fill="url(#gf-rock)" d="M30 166 L60 166 L80 140 L100 140Z" opacity=".0"/>` + L(84, 150, "A", true) + L(236, 150, "B", true) + T(160, 176, "Same scale · numbers are metres", { s: 7, c: "#6a7c83" }),
  "gf-02-moving-earth/rotation": () => NIGHT + SUNR(24, 90, 18) + [60, 90, 120].map((y) => AR(52, y, 92, y, "sunray")).join("")
    + `<circle cx="170" cy="90" r="62" fill="url(#gf-glow)" opacity=".3"/><circle cx="170" cy="90" r="56" fill="url(#gf-ocean)"/><path fill="url(#gf-grass)" opacity=".85" d="M140 54 q22 -8 34 8 q-2 18 -18 18 q-12 12 -8 28 q-14 -8 -14 -30 q-4 -14 6 -24Z M190 92 q16 -4 22 10 q-4 16 -16 14 q-10 -6 -6 -24Z"/>`
    + `<path fill="#0b1826" opacity=".72" d="M170 34 A56 56 0 0 1 170 146Z"/>` + [[196, 100], [204, 70], [190, 120]].map(([x, y]) => `<circle cx="${x}" cy="${y}" r="1.4" fill="#ffd76a"/>`).join("") + `<path d="M170 34 V146" stroke="#fff" stroke-opacity=".3"/>`
    + `<circle cx="146" cy="90" r="3" fill="#e0563b"/>` + L(146, 76, "A") + `<circle cx="196" cy="90" r="3" fill="#e0563b"/>` + L(196, 76, "B") + `<path d="M120 164 Q170 178 222 164" stroke="#fff" stroke-width="2" fill="none" stroke-opacity=".8"/>` + `<path d="M222 164 l-8 -4 l1 7Z" fill="#fff"/>`,
  "gf-02-moving-earth/seasons": () => NIGHT + `<ellipse cx="160" cy="92" rx="132" ry="48" fill="none" stroke="#fff" stroke-opacity=".25" stroke-dasharray="4 5"/>` + SUNR(160, 92, 20)
    + [[56, "A"], [264, "B"]].map(([x, l]) => `<g><circle cx="${x}" cy="92" r="30" fill="url(#gf-ocean)"/><g transform="rotate(23.5 ${x} 92)"><path fill="#0b1826" opacity=".6" d="M${x} 62 A30 30 0 0 ${x < 160 ? 0 : 1} ${x} 122Z"/><path d="M${x} 54 V130" stroke="#fff" stroke-width="2"/>${T(x, 50, "N", { s: 8, w: 800, c: "#fff", h: false })}</g></g>` + L(x, 146, l)).join("")
    + AR(130, 92, 92, 92, "sunray") + AR(190, 92, 228, 92, "sunray"),
  "gf-02-moving-earth/interior": () => NIGHT + `<circle cx="140" cy="92" r="80" fill="#8a6a48"/><circle cx="140" cy="92" r="70" fill="url(#gf-mantle)"/><circle cx="140" cy="92" r="34" fill="url(#gf-core)"/><path fill="url(#gf-ocean)" d="M140 12 A80 80 0 0 1 220 92 H140Z" opacity="0"/>`
    + `<path d="M140 92 L140 12 A80 80 0 0 1 220 92Z" fill="#1d3550" opacity=".0"/>`
    + [[212, 40, 252, 36, "A"], [196, 76, 252, 84, "B"], [150, 100, 252, 132, "C"]].map(([x1, y1, x2, y2, l]) => `<path d="M${x1} ${y1} L${x2 - 10} ${y2}" stroke="#fff" stroke-width="1.4"/><circle cx="${x1}" cy="${y1}" r="2.5" fill="#fff"/>` + L(x2, y2, l)).join(""),
  "gf-02-moving-earth/plates": () => SKY + [0, 1, 2].map((k) => { const y = 14 + k * 54; return `<rect x="70" y="${y}" width="200" height="40" rx="8" fill="url(#gf-rock2)" filter="url(#gf-shadow)"/><path d="M170 ${y} V${y + 40}" stroke="#17313b" stroke-width="2" stroke-dasharray="4 3"/>` + L(48, y + 20, "ABC"[k]); }).join("")
    + AR(150, 34, 96, 34, "warm") + AR(190, 34, 244, 34, "warm") + `<path fill="#e0562c" d="M166 18 h8 v32 h-8Z" opacity=".7"/>`
    + AR(96, 88, 150, 88, "warm") + AR(244, 88, 190, 88, "warm")
    + AR(150, 160, 150, 128, "warm") + AR(190, 128, 190, 160, "warm"),
  "gf-03-landforms/rock-families": () => PAPER + [[60, "A"], [160, "B"], [260, "C"]].map(([x, l]) => L(x, 22, l)).join("")
    + `<g filter="url(#gf-shadow)"><path fill="#4a3d38" d="M22 150 L30 60 L70 46 L98 70 L96 150Z"/>${Array.from({ length: 18 }, (_, k) => `<path fill="${["#e8e2d6", "#c9b9a6", "#d98c6a"][k % 3]}" d="M${34 + (k * 17) % 56} ${66 + (k * 23) % 78} l5 -3 l4 4 l-4 4Z"/>`).join("")}</g>`
    + `<g filter="url(#gf-shadow)"><path fill="#e1c487" d="M122 150 L126 58 L196 52 L198 150Z"/>${[0, 1, 2, 3, 4, 5].map((k) => `<path d="M122 ${70 + k * 14} Q160 ${66 + k * 14} 198 ${70 + k * 14}" stroke="${k % 2 ? "#b58c58" : "#f0dcae"}" stroke-width="7" fill="none"/>`).join("")}</g>`
    + `<g filter="url(#gf-shadow)"><path fill="#7d8a86" d="M222 150 L228 56 L296 60 L298 150Z"/>${[0, 1, 2, 3, 4].map((k) => `<path d="M224 ${72 + k * 16} q18 -10 37 0 t37 0" stroke="${k % 2 ? "#cfd8d4" : "#4f5c58"}" stroke-width="5" fill="none"/>`).join("")}</g>`
    + T(60, 168, "crystals", { s: 8 }) + T(160, 168, "layers", { s: 8 }) + T(260, 168, "bands", { s: 8 }),
  "gf-03-landforms/sediment-journey": () => SKY + CLOUD(250, 30, 1) + MTN([[50, 120, 50]], 150, true) + `<path fill="url(#gf-grass)" d="M0 180 V150 H320 V180Z"/>`
    + `<path d="M70 150 C130 140 200 156 320 150" stroke="url(#gf-sea)" stroke-width="10" fill="none"/>`
    + `<path fill="url(#gf-rock2)" stroke="#17313b" stroke-width=".8" d="M30 104 h30 l6 26 h-42Z"/><path d="M45 104 l-4 10 l6 6 l-4 10" stroke="#17313b" stroke-width="1.6" fill="none"/>` + L(46, 92, "A")
    + [0, 1, 2, 3].map((k) => `<circle cx="${140 + k * 12}" cy="${144 + (k % 2) * 3}" r="3" fill="#c99a3c"/>`).join("") + AR(130, 128, 190, 128, "cool") + L(162, 114, "B")
    + `<g filter="url(#gf-shadow)">${STRATA(240, 152, 70, 24, ["#e8cf96", "#c9a66c", "#e8cf96", "#b58c58"])}</g>` + L(260, 138, "C"),
  "gf-03-landforms/meander": () => `<rect width="${W}" height="${H}" fill="url(#gf-grass)"/>` + FOREST(10, 110, 26, 5, .9) + FOREST(200, 310, 170, 5, .9)
    + `<path d="M-6 150 C80 150 120 120 150 92 C190 54 240 48 250 70 C262 98 210 110 190 96 C160 76 140 40 180 20 S300 10 330 20" stroke="url(#gf-sea)" stroke-width="22" fill="none"/>`
    + `<path d="M248 46 q26 28 4 54" stroke="#c8553d" stroke-width="4" stroke-dasharray="2 5" fill="none"/>` + L(276, 70, "A") + `<path fill="url(#gf-sand)" d="M200 84 q24 2 30 -12 q-18 6 -30 12Z"/>` + L(212, 112, "B")
    + AR(70, 132, 112, 112, "") + NORTH(24, 26),
  "gf-03-landforms/landform-profiles": () => SKY + [[56, "A"], [160, "B"], [266, "C"]].map(([x, l]) => L(x, 18, l)).join("")
    + `<path fill="url(#gf-snow)" d="M4 40 C24 150 88 150 108 40Z"/><path fill="url(#gf-rock)" d="M4 40 C24 150 88 150 108 40 L108 180 H4Z"/>`
    + `<rect x="114" y="140" width="94" height="40" fill="url(#gf-sand)"/><path fill="url(#gf-sand)" d="M114 140 C134 140 140 80 164 80 C176 80 194 134 208 140Z"/>`
    + `<path fill="url(#gf-rock)" d="M214 180 V40 H262 L268 140 H320 V180Z"/>` + FOREST(218, 258, 42, 3, .8) + `<rect x="268" y="140" width="52" height="40" fill="url(#gf-sea)"/>` + FOAM(146, 268, 320),
  "gf-04-air-and-water/weather-record": () => PAPER + CARD(26, 10, 280, 160) + AXIS(66, 146, 300, 100, 222) + BARS([11.5, 283.4, 117.9], ["01", "07", "10"], 92, 146, 72, 300, (k) => k === 1 ? "url(#gf-sea)" : "#7fb6cf") + T(176, 22, "Guwahati · mean monthly rainfall", { s: 7.5, c: "#6a7c83" }),
  "gf-04-air-and-water/water-paths": () => SKY + SUNR(30, 26, 12) + `<rect y="132" width="120" height="48" fill="url(#gf-sea)"/>` + FOAM(138, 0, 120)
    + `<path fill="url(#gf-grass)" d="M110 180 V134 L180 92 L240 80 L320 104 V180Z"/>` + `<path fill="#8d6748" d="M120 180 V150 L180 116 L240 106 L320 126 V180Z"/>` + FOREST(190, 300, 92, 6, .8)
    + CLOUD(150, 34, 1.2) + CLOUD(190, 40, 1)
    + AR(70, 126, 110, 50, "cool") + L(78, 92, "A") + DROPS([196, 206, 216], 50, 80) + AR(206, 54, 206, 84, "cool") + L(224, 66, "B")
    + AR(170, 112, 128, 138, "cool") + L(150, 112, "C") + AR(250, 104, 250, 150, "cool") + L(266, 134, "D"),
  "gf-04-air-and-water/rain-shadow": () => SKY + HAZE(120) + MTN([[160, 130, 76]], 160, true) + `<rect y="158" width="320" height="22" fill="url(#gf-grass)"/>` + FOREST(10, 120, 162, 7, 1) + `<rect x="210" y="158" width="110" height="22" fill="url(#gf-sand)"/>`
    + CLOUD(110, 50, 1.4) + CURVE("M4 138 C56 126 96 100 132 64", "cool") + DROPS([98, 112, 126], 64, 110) + CURVE("M190 60 C220 86 250 118 306 128", "warm") + AR(4, 150, 50, 150, "wind")
    + L(84, 124, "A") + L(236, 124, "B"),
  "gf-05-ocean-and-hazards/shelf": () => SKY.replace(H, 50) + `<rect y="46" width="${W}" height="134" fill="url(#gf-sea)"/>` + FOAM(52) + `<path fill="url(#gf-land)" d="M0 26 L60 32 L84 46 H0Z"/>` + HOUSE(24, 32, .8)
    + `<path fill="url(#gf-sand)" filter="url(#gf-shadow)" d="M0 46 L100 64 L196 142 L320 162 V180 H0Z"/>` + L(56, 72, "A") + L(158, 102, "B") + L(246, 136, "C"),
  "gf-05-ocean-and-hazards/coastal-exposure": () => `<rect width="${W}" height="${H}" fill="url(#gf-grass)"/>` + `<rect width="90" height="${H}" fill="url(#gf-sea)"/>` + `<path d="M88 0 C96 40 84 90 96 180" stroke="#fff" stroke-width="2" fill="none" opacity=".7"/>`
    + `<path fill="#bfe3f0" opacity=".85" d="M88 0 H150 C156 40 146 110 160 180 H96 C84 90 96 40 88 0Z"/>` + T(124, 14, "inundation zone", { s: 7, c: "#1d6f96", i: 1 }) + FOREST(200, 310, 40, 5, .9)
    + `<path d="M126 92 L190 110 L250 108 L284 140" stroke="#17313b" stroke-width="4" fill="none" stroke-linecap="round"/>` + HOUSE(126, 86, 1.1) + L(126, 108, "A") + HOUSE(284, 136, 1.1, "#1d6f96") + L(262, 146, "B") + NORTH(300, 22),
  "gf-06-india-location/island-locators": () => `<rect width="${W}" height="${H}" fill="url(#gf-ocean)"/>` + IND([[72.7, 12], [73, 10.8], [72.2, 10], [73, 8.5]].map(([a, b]) => `<circle cx="${lx(a)}" cy="${ly(b)}" r="4.5" fill="#e0563b" stroke="#fff" stroke-width="1.6"/>`).join("") + [[92.8, 13.2], [92.7, 12], [92.7, 10.8], [93.6, 8.2], [93.8, 7.2]].map(([a, b]) => `<circle cx="${lx(a)}" cy="${ly(b)}" r="4.5" fill="#e0563b" stroke="#fff" stroke-width="1.6"/>`).join(""), 2, 1, -150)
    + L(...at(70.4, 10.4, 2, 1, -150), "A") + L(...at(95.6, 10.8, 2, 1, -150), "B"),
  "gf-07-india-relief/himalayan-transect": () => SKY + CLOUD(250, 28, 1) + HAZE(92, "#bcd3dd", .6) + MTN([[60, 156, 60], [22, 120, 36], [100, 128, 42]], 180, true) + MTN([[154, 98, 40], [182, 82, 32]], 180, false) + FOREST(130, 196, 172, 5, .9, true)
    + `<path fill="url(#gf-grass)" d="M204 180 V140 Q234 120 264 138 Q276 134 288 142 V180Z"/>` + `<rect x="286" y="146" width="34" height="34" fill="url(#gf-alluv)"/>`
    + L(60, 40, "A") + L(160, 88, "B") + L(240, 120, "C") + L(298, 118, "D") + AR(110, 172, 180, 172, "") + T(98, 175, "N", { s: 8, w: 800, a: "end" }) + T(190, 175, "S", { s: 8, w: 800, a: "start" }),
  "gf-08-indian-rivers/basin": () => `<rect width="${W}" height="${H}" fill="url(#gf-grass)"/>` + `<path fill="url(#gf-alluv)" opacity=".7" stroke="#8a6a48" stroke-width="4" d="M40 120 L90 30 L180 20 L260 40 L300 110 L240 168 L110 170Z"/>` + FOREST(100, 260, 36, 8, .7, true)
    + ["M110 50 C130 80 150 96 164 104", "M110 118 C130 112 150 108 164 104", "M164 104 C200 116 240 130 290 156"].map((d) => `<path d="${d}" stroke="url(#gf-sea)" stroke-width="6" fill="none" stroke-linecap="round"/>`).join("") + AR(270, 146, 296, 160, "cool")
    + L(110, 40, "A") + L(164, 88, "B") + L(282, 136, "C"),
  "gf-08-indian-rivers/northern": () => `<rect width="${W}" height="${H}" fill="url(#gf-ocean)"/>` + IND(riv([[81, 31], [75, 34.5], [73, 31], [71, 27.5], [68, 24]]) + riv([[79, 31], [79, 27.5], [83, 25.5], [87.9, 24.5], [89.5, 22]]) + riv([[85, 30.5], [91, 29.5], [95.2, 29], [95, 27.8], [91, 26.2], [89.7, 25.3], [90, 22.5]]))
    + L(...at(71, 31.5), "1", true) + L(...at(82, 27.5), "2", true) + L(...at(93.5, 29.5), "3", true),
  "gf-08-indian-rivers/peninsula": () => `<rect width="${W}" height="${H}" fill="url(#gf-ocean)"/>` + IND(riv([[81.7, 22.6], [78, 22.6], [72.8, 21.7]]) + riv([[78, 21.6], [75, 21.2], [72.7, 21.1]]) + riv([[82, 22], [84, 21], [86.7, 20.3]]) + riv([[73.6, 20], [78, 19], [81.8, 16.6]]) + riv([[73.7, 18], [78, 16.5], [81, 15.8]]) + riv([[75.7, 12.4], [78.5, 11], [79.9, 10.8]]), 12, 1.1, -132)
    + L(...at(78.4, 23.8, 12, 1.1, -132), "1", true, 9) + L(...at(74.6, 19.9, 12, 1.1, -132), "2", true, 9) + L(...at(87.6, 21.4, 12, 1.1, -132), "3", true, 9) + L(...at(83.4, 17.4, 12, 1.1, -132), "4", true, 9) + L(...at(82.4, 15, 12, 1.1, -132), "5", true, 9) + L(...at(81, 10.1, 12, 1.1, -132), "6", true, 9),
  "gf-08-indian-rivers/mouths": () => `<rect width="${W}" height="110" fill="url(#gf-grass)"/><rect y="108" width="${W}" height="72" fill="url(#gf-sea)"/>` + FOAM(120) + `<path d="M160 0 V180" stroke="#fff" stroke-width="3"/>`
    + `<path fill="url(#gf-alluv)" d="M24 108 Q86 160 148 108 L86 60Z"/><path d="M86 0 V64" stroke="url(#gf-sea)" stroke-width="9"/><path d="M86 64 L38 122 M86 64 L66 132 M86 64 L106 132 M86 64 L134 122" stroke="#4f9fc4" stroke-width="3.5" fill="none" stroke-linecap="round"/>`
    + `<path fill="url(#gf-sea)" d="M236 0 L252 0 L306 180 L186 180Z"/>` + FOREST(170, 220, 40, 3, .8) + FOREST(270, 316, 40, 3, .8) + L(86, 20, "A") + L(244, 20, "B"),
  "gf-09-india-monsoon/moisture-pathways": () => `<rect width="${W}" height="${H}" fill="url(#gf-ocean)"/>` + IND(`<g stroke-width="5">${CURVE(`M${lx(66)} ${ly(7)} C${lx(70)} ${ly(10)} ${lx(73)} ${ly(14)} ${lx(75)} ${ly(20)}`, "cool")}${CURVE(`M${lx(86)} ${ly(7)} C${lx(89)} ${ly(13)} ${lx(91)} ${ly(19)} ${lx(91)} ${ly(25)}`, "cool")}</g>` + AR(lx(74.6), ly(18.6), lx(75), ly(20.4), "cool") + AR(lx(91), ly(23.6), lx(91), ly(25.4), "cool") + `<g transform="translate(${lx(80)} ${ly(25)})">${CLOUD(0, 0, 1)}${CLOUD(30, 6, .8)}</g>`)
    + L(...at(68.4, 9.2), "1", true) + L(...at(87.6, 9.2), "2", true),
  "gf-09-india-monsoon/station-normals": () => PAPER + CARD(26, 10, 280, 160) + AXIS(66, 146, 300, 100, 222) + BARS([283.4, 117.9, 113.1, 278.3], ["G·07", "G·10", "C·07", "C·10"], 82, 146, 56, 300, (k) => k < 2 ? "url(#gf-sea)" : "#e7a64a") + T(176, 22, "Mean monthly rainfall, 1991–2020", { s: 7.5, c: "#6a7c83" }),
  // covers
  "gf-06-india-location/cover": () => `<rect width="${W}" height="${H}" fill="url(#gf-night)"/>` + Array.from({ length: 40 }, (_, k) => `<circle cx="${(k * 97) % W}" cy="${(k * 53) % H}" r="${k % 3 ? .6 : 1.1}" fill="#fff" opacity=".7"/>`).join("")
    + IND(`<path d="M0 ${ly(23.5)} H320" stroke="#ffb35c" stroke-width="2"/><path d="M${lx(82.5)} 0 V300" stroke="#7fd6ff" stroke-width="2"/><circle cx="${lx(82.5)}" cy="${ly(23.5)}" r="5" fill="#fff"/>`, 80, .62)
    + T(42, 30, "Put India", { s: 13, w: 800, c: "#fff", h: false, a: "start" }) + T(42, 46, "on the map", { s: 13, w: 800, c: "#ffd76a", h: false, a: "start" }),
  "gf-09-india-monsoon/cover": () => `<rect width="${W}" height="${H}" fill="#3e5f78"/><rect width="${W}" height="${H}" fill="url(#gf-sea)" opacity=".5"/>` + IND(CURVE(`M${lx(66)} ${ly(7)} C${lx(70)} ${ly(10)} ${lx(73)} ${ly(14)} ${lx(75)} ${ly(20)}`, "cool") + CURVE(`M${lx(86)} ${ly(7)} C${lx(89)} ${ly(13)} ${lx(91)} ${ly(19)} ${lx(91)} ${ly(25)}`, "cool"), 120, .6)
    + CLOUD(70, 44, 1.4) + CLOUD(150, 34, 1.1) + CLOUD(262, 42, 1.3) + DROPS([40, 62, 84, 106, 128, 236, 258, 280, 302], 62, 118) + T(40, 160, "Read India’s monsoon", { s: 13, w: 800, c: "#fff", h: false, a: "start" }),
  "gf-10-land-and-livelihoods/cover": () => SKY + SUNR(270, 34, 14) + BIRDS(120, 30) + HAZE(80, "#a9c7b2", .6) + MTN([[40, 70, 50], [90, 56, 40]], 90, false)
    + [0, 1, 2, 3].map((k) => `<path fill="${["#cfe39a", "#a9cf6e", "#e8cf96", "#8fbf5a"][k]}" d="M0 ${96 + k * 20} Q160 ${84 + k * 20} 320 ${100 + k * 20} V180 H0Z" filter="url(#gf-shadow)"/>`).join("")
    + [[60, 112], [86, 108], [240, 132], [270, 128]].map(([x, y]) => HOUSE(x, y, 1)).join("") + FOREST(150, 210, 106, 4, .9) + `<path d="M0 170 C100 150 220 172 320 156" stroke="url(#gf-sea)" stroke-width="8" fill="none"/>`
    + T(20, 26, "Connect land", { s: 13, w: 800, a: "start" }) + T(20, 42, "and livelihoods", { s: 13, w: 800, a: "start", c: "#2f6e48" }),
};
})();
