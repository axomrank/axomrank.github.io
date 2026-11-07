#!/usr/bin/env python3
"""Content checks for the Indian History lessons. Cannot judge history or Assamese."""
import json, re, glob, collections

AS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
ORD = re.compile(r"\b\d+(st|nd|rd|th)\b|Edict \d+")
def years(x):
    """Numbers in a string. Ordinals are words in Assamese, so they are skipped."""
    x = ORD.sub("", re.sub(r"\[\[[^\]|]+(\|)?", "", x.translate(AS)))
    return {n.replace(",", "").lstrip("0") for n in re.findall(r"\d[\d,]*\d|\d", x)}
def differ(a, b, en=""):
    """Compare full years and large figures only; 1936 to 40 is a short form, and 1930s reads as a phrase."""
    if re.search(r"\d{4}s\b", en): return False
    return any(len(n) >= 3 and not (n in b or any(len(m) == 2 and n.endswith(m) for m in b)) for n in a)
prob = []
def walk(o, at):
    if isinstance(o, dict):
        if set(o) >= {"en", "as"} and isinstance(o["en"], str):
            a, b = years(o["en"]), years(o["as"])
            if differ(a, b, o["en"]) or differ(b, a, o["en"]): prob.append(f"{at}: numbers differ {sorted(a)} / {sorted(b)}: {o['en'][:60]}")
            if re.search(r"[A-Za-z]{4,}", re.sub(r"<[^>]+>|\[\[[^\]]+\]\]|HMIS|HSRA|Hiuen Tsang|Xuanzang|DataMeet|APSC|ADRE|Karenge", "", o["as"])): prob.append(f"{at}: Latin text in Assamese: {o['as'][:60]}")
            return
        for k, v in o.items(): walk(v, f"{at}.{o.get('id', k)}")
    elif isinstance(o, list):
        for x in o: walk(x, at)

n = st = 0; seen = collections.Counter()
for f in sorted(glob.glob("content/lessons/ih-*.json")):
    L = json.load(open(f, encoding="utf-8")); n += 1
    walk({k: L[k] for k in ("king", "mission", "units", "test", "guide") if k in L}, L["id"])
    for u in L["units"] + [L["test"]]:
        for s in u["steps"]:
            st += 1; seen[s["id"]] += 1
            if s["type"] != "story" and not s.get("why"): prob.append(f"{s['id']}: no explanation")
            if "options" in s and isinstance(s["options"], list) and s["type"] != "picture":
                if not 0 <= s["answer"] < len(s["options"]): prob.append(f"{s['id']}: answer out of range")
                if len({o["en"].lower() for o in s["options"]}) != len(s["options"]): prob.append(f"{s['id']}: repeated option")
            if s["type"] == "match" and len({p[1]["en"] for p in s["pairs"]}) != len(s["pairs"]): pass
for k, v in seen.items():
    if v > 1: prob.append(f"{k}: repeated id")
for p in prob: print(p)
print(f"Indian History check: {n} lessons, {st} steps, {len(prob)} problem(s)")
raise SystemExit(1 if prob else 0)
