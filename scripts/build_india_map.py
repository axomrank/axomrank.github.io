#!/usr/bin/env python3
"""Build content/maps/india.json, the base map for lessons with "base": "india".

India's outline comes only from the DataMeet Survey of India-derived file. Natural
Earth supplies other countries and is drawn underneath, so its de facto lines can
never show inside India's outline. Modern reference geography, not historical borders.
"""
import json, os

LIB = "/home/angsuman/extra_spac/Assam History/data/maps"
BOX = (55, -12, 112, 45)   # lon min, lat min, lon max, lat max
SKIP = {"India", "Antarctica"}
ROUND = 3

def perp(p, a, b):
    (y, x), (y1, x1), (y2, x2) = p, a, b
    dx, dy = x2 - x1, y2 - y1
    if dx == dy == 0: return ((x - x1) ** 2 + (y - y1) ** 2) ** .5
    t = max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)))
    return ((x - x1 - t * dx) ** 2 + (y - y1 - t * dy) ** 2) ** .5

def simplify(ring, tol):
    """Douglas-Peucker on a closed ring; small islands are kept whole."""
    if len(ring) < 8: return ring
    open_ring = ring[:-1] if ring[0] == ring[-1] else ring
    far = max(range(len(open_ring)), key=lambda i: perp(open_ring[i], open_ring[0], open_ring[0]))
    keep = {0, far, len(open_ring) - 1}
    stack = [(0, far), (far, len(open_ring) - 1)]
    while stack:
        a, b = stack.pop()
        if b <= a + 1: continue
        i = max(range(a + 1, b), key=lambda j: perp(open_ring[j], open_ring[a], open_ring[b]))
        if perp(open_ring[i], open_ring[a], open_ring[b]) > tol:
            keep.add(i); stack += [(a, i), (i, b)]
    return [open_ring[i] for i in sorted(keep)]

def clip(ring):
    """Sutherland-Hodgman against BOX. Points are [lat, lon]."""
    tests = [
        (lambda p: p[1] >= BOX[0], lambda a, b: cross(a, b, 1, BOX[0])),
        (lambda p: p[1] <= BOX[2], lambda a, b: cross(a, b, 1, BOX[2])),
        (lambda p: p[0] >= BOX[1], lambda a, b: cross(a, b, 0, BOX[1])),
        (lambda p: p[0] <= BOX[3], lambda a, b: cross(a, b, 0, BOX[3])),
    ]
    for inside, at in tests:
        out = []
        for i, p in enumerate(ring):
            q = ring[i - 1]
            if inside(p):
                if not inside(q): out.append(at(q, p))
                out.append(p)
            elif inside(q): out.append(at(q, p))
        ring = out
        if not ring: break
    return ring

def cross(a, b, axis, value):
    t = (value - a[axis]) / (b[axis] - a[axis])
    p = [a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])]
    p[axis] = value
    return p

def tidy(ring): return [[round(p[0], ROUND), round(p[1], ROUND)] for p in ring]

bounds = json.load(open(f"{LIB}/boundaries.json", encoding="utf-8"))["india"]
world = json.load(open(f"{LIB}/world.json", encoding="utf-8"))
outline = [tidy(simplify(r, .02)) for r in bounds["rings"]]
land, used = [], []
for c in world["countries"]:
    if c["name"] in SKIP: continue
    rings = [tidy(r) for r in (simplify(clip(x), .07) for x in c["rings"]) if len(r) >= 3]
    rings = [r for r in rings if len({tuple(p) for p in r}) >= 3]
    if rings: land += rings; used.append(c["name"])
out = {
    "note": "Modern reference geography, not historical borders. Built by scripts/build_india_map.py. Places on it are approximate.",
    "sources": {
        "outline": {"source": bounds["source"], "url": bounds["url"], "license": bounds["license"], "sha256": bounds["sha256"], "change": "Simplified at 0.02 degrees for display."},
        "land": {"source": world["source"], "url": world["url"], "license": world["license"], "sha256": world["sha256"], "change": "Countries other than India, clipped and simplified at 0.07 degrees."},
    },
    "box": list(BOX), "outline": outline, "land": land, "districts": {}, "rivers": {}, "ridges": {},
}
os.makedirs("content/maps", exist_ok=True)
json.dump(out, open("content/maps/india.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("outline rings", len(outline), "points", sum(map(len, outline)), "| land rings", len(land), "points", sum(map(len, land)), "| KB", os.path.getsize("content/maps/india.json") // 1024)
print(len(used), "neighbours; disputed-looking:", [n for n in used if any(w in n for w in ("Kashmir", "Siachen", "Aksai", "Arunachal", "Line", "disputed"))])
