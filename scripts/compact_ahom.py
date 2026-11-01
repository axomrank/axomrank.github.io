"""Build compact ahom-kingdom lessons by choosing steps from the reign-by-reign lessons.
Usage: python3 scripts/compact_ahom.py .   (writes content/lessons/ahom-NN-*.json; then run scripts/build.py)
The chosen steps for each lesson are in scripts/compact_ahom_spec.py."""
import json, re, sys, copy, os
from compact_ahom_spec import LESSONS, EYEBROW

ROOT = sys.argv[1]
os.chdir(ROOT)
src = {}
def S(lid):
    if lid not in src: src[lid] = json.load(open(f"content/lessons/{lid}.json", encoding="utf-8"))
    return src[lid]
# step id -> (lesson id, unit, step)
index = {}
for f in os.listdir("content/lessons"):
    lid = f[:-5]
    L = json.load(open(f"content/lessons/{f}", encoding="utf-8"))
    if L.get("course", "ahom-kings") != "ahom-kings": continue
    src[lid] = L
    for u in L["units"] + [L["test"]]:
        for s in u["steps"]: index[s["id"]] = (lid, u, s)

def path(lid, f): return f if "/" in f else f"{lid}/{f}"

for spec in LESSONS:
    n, used, out_units = spec["no"], [], []
    def take(sid):
        lid, u, s = index[sid]
        used.append(lid)
        s = copy.deepcopy(s)
        s["id"] = f"ak{n}.{sid}"
        s.pop("link", None)
        if s.get("img"): s["img"] = path(lid, s["img"])
        if s["type"] == "picture": s["options"] = [path(lid, o) for o in s["options"]]
        # a map question or map card without its own box keeps the map of the lesson it came from,
        # so it is framed as the author drew it (the merged lesson map can span the whole valley)
        if s["type"] == "map" or (s["type"] == "story" and isinstance(s.get("map"), dict) and not s["map"].get("box")):
            own = s.get("map") if isinstance(s.get("map"), dict) else {}
            s["map"] = {**copy.deepcopy(S(lid)["map"]), **{k: v for k, v in own.items() if k != "labels"}}
        return s, u
    for k, us in enumerate(spec["units"], 1):
        steps = [take(x) for x in us["steps"]]
        first_unit = steps[0][1]
        learned = []
        for ref in us["learned"]:
            lid, uid, i = ref.split("/")
            learned.append(next(u for u in S(lid)["units"] if u["id"] == uid)["learned"][int(i)])
        out_units.append({"id": f"u{k}", "icon": us.get("icon", first_unit.get("icon", "trophy")), "title": us["title"], "learned": learned, "steps": [s for s, _ in steps]})
    test = {"id": "test", "title": {"en": "Lesson test", "as": "পাঠৰ পৰীক্ষা"}, "learned": [], "steps": [take(x)[0] for x in spec["test"]]}
    order = list(dict.fromkeys(used))
    # map: the main source lesson's map, widened to show every place a map step asks for
    base = copy.deepcopy(S(spec["map_from"])["map"])
    box = base["box"]
    for lid in order:
        m = S(lid)["map"]
        for i in m["show"]:
            if i not in base["show"]: base["show"].append(i)
        for k2, v in m.get("labels", {}).items(): base.setdefault("labels", {}).setdefault(k2, v)
        if any(s["type"] == "map" for u in out_units + [test] for s in u["steps"] if s["id"].split(".", 1)[1] in {x["id"] for uu in S(lid)["units"] + [S(lid)["test"]] for x in uu["steps"]}):
            b = m["box"]; box = [min(box[0], b[0]), min(box[1], b[1]), max(box[2], b[2]), max(box[3], b[3])]
    base["box"] = box
    # guidebook timeline: entries from the source lessons whose year the new lesson actually mentions
    text = json.dumps([x["text"] for u in out_units for x in u["steps"] if x["type"] == "story"], ensure_ascii=False)
    tl, seen = [], set()
    for lid in order:
        for e in S(lid).get("guide", {}).get("timeline", []):
            key = (e.get("y"), e["t"]["en"])
            if key in seen or (e.get("y") and e["y"] not in text) or (len(order) > 1 and not e.get("y")): continue
            seen.add(key)
            if len(order) > 1:   # a merged lesson: say whose reign each entry belongs to
                nm = {k: re.sub(r"^(Swargadeo|Chaolung|স্বৰ্গদেউ|চাওলুং) ", "", S(lid)["king"][k]) for k in ("en", "as")}
                e = {**e, "t": {k: f"{nm[k]}: {e['t'][k]}" for k in ("en", "as")}}
            tl.append(e)
    tl.sort(key=lambda e: int(re.match(r"\d+", e.get("y") or "0").group()))
    sources, urls = [], set()
    for lid in order:
        for x in S(lid)["sources"]:
            if x["url"] not in urls: urls.add(x["url"]); sources.append(x)
    L = {"id": spec["id"], "course": "ahom-kingdom", "no": n, "version": 1, "eyebrow": EYEBROW, "king": spec["title"], "reign": spec["reign"],
         "portrait": spec["portrait"], "compiled_from": order, "sources": sources, "guide": {"timeline": tl}, "map": base,
         "units": out_units, "test": test}
    json.dump(L, open(f"content/lessons/{spec['id']}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    steps = sum(len(u["steps"]) for u in out_units) + len(test["steps"])
    print(f"{spec['id']}: {len(out_units)} units, {steps} steps, from {len(order)} lessons, timeline {len(tl)}")
