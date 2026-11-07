#!/usr/bin/env python3
"""Check the Constitution course without a browser.

Plays each exercise's answer key against the rules in app/engine.js, and checks
what a player run would reveal: answers that cannot be chosen, spot tokens out of
range, duplicate options, mismatched languages, unit budgets, and any article
number that is not in the register. It cannot judge law or Assamese.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
read = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))
course = read("content/courses/indian-constitution.json")
register = {a["no"] for a in read("docs/research/constitution-article-register.json")["articles"]}
entities = read("content/entities.json")
budget = {int(n): int(u) for n, _, u in re.findall(r"^\| (\d+) \| .+? \| ([ABC]) \| (\d+) \|", (ROOT / "docs/CONSTITUTION-COURSE.md").read_text(encoding="utf-8"), re.M)}
errors = []
ids = set()
ASSAMESE = re.compile(r"[ঀ-৿]")
ARTICLE = re.compile(r"\bArticles? ((?:\d+[A-Z]{0,2}(?:-[IO])?(?:\(\w+\))*(?:,? (?:and |to |or )?|–)?)+)")


def text_of(v):
    if isinstance(v, dict):
        return " ".join(text_of(x) for k, x in v.items() if k not in ("id", "type"))
    if isinstance(v, list):
        return " ".join(text_of(x) for x in v)
    return str(v)


def check_text(v, where):
    if isinstance(v, dict) and set(v) >= {"en", "as"}:
        en, as_ = v["en"], v["as"]
        if isinstance(en, str) and isinstance(as_, str):
            if re.search(r"[A-Za-z]{4,}", re.sub(r"\[\[[^\]]*\]\]|<[^>]+>", "", as_)) and not re.search(r"APSC|UPSC|ADRE|DME|NCERT|GST|CAG|PIL|NITI|PDF|NJAC|TET|PAC|OBC|OCI|NOTA|TEARS|EVM|VVPAT|NHRC|CIC", as_):
                errors.append(f"{where}: English word in Assamese text: {as_[:50]}")
            if not ASSAMESE.search(as_.replace("।", "")) and not re.fullmatch(r"[\s\d()ivx,.\-–→+=/%A-Z।”“]*", as_):
                errors.append(f"{where}: no Assamese script: {as_[:50]}")
            for m in re.finditer(r"\[\[([a-z0-9-]+)", en + as_):
                if m[1] not in entities:
                    errors.append(f"{where}: unknown entity {m[1]}")
            for lang in (en, as_):
                if lang.count("<mark>") != lang.count("</mark>") or lang.count("[[") != lang.count("]]"):
                    errors.append(f"{where}: unbalanced markup: {lang[:50]}")
            en_plain = re.sub(r"\b(List|Appendix|Appendices) (I{1,3})\b( and (I{1,3})\b)?", lambda m: f"{m[1]} {len(m[2])}" + (f" and {len(m[4])}" if m[4] else ""), en)
            en_nums = sorted(re.findall(r"\d+", re.sub(r"\[\[[^\]]*\]\]", "", en_plain)))
            as_nums = sorted(re.findall(r"\d+", re.sub(r"\[\[[^\]]*\]\]", "", as_.translate(str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")))))
            if en_nums and as_nums and en_nums != as_nums:
                errors.append(f"{where}: numbers differ between languages: {en_nums} / {as_nums}")
        return
    if isinstance(v, dict):
        for k, x in v.items():
            check_text(x, where)
    elif isinstance(v, list):
        for x in v:
            check_text(x, where)


def check_step(s, where):
    if s["id"] in ids:
        errors.append(f"{where}: duplicate id")
    ids.add(s["id"])
    kind = s["type"]
    if "options" in s and kind != "picture":
        names = [o["en"].strip().lower() for o in s["options"]]
        if len(set(names)) != len(names) or len({o["as"].strip() for o in s["options"]}) != len(names):
            errors.append(f"{where}: duplicate options")
        if not 0 <= s["answer"] < len(names):
            errors.append(f"{where}: answer out of range")
    if kind == "spot":
        for lang in ("en", "as"):
            if not 0 <= s["wrong"][lang] < len(s["tokens"][lang]):
                errors.append(f"{where}: spot index out of range")
            if len(set(s["tokens"][lang])) != len(s["tokens"][lang]) and s["tokens"][lang].count(s["tokens"][lang][s["wrong"][lang]]) > 1:
                errors.append(f"{where}: wrong word appears twice")
    if kind == "timeline":
        ys = [int(a["y"]) for a in s["anchors"]]
        if ys != sorted(ys):
            errors.append(f"{where}: anchors out of order")
        for x in s["items"]:
            if not 0 <= x["slot"] <= len(s["anchors"]):
                errors.append(f"{where}: timeline slot out of range")
    if kind == "match":
        if len(s["pairs"]) < 3:
            errors.append(f"{where}: match needs three pairs")
        for side in (0, 1):
            if len({p[side]["en"] for p in s["pairs"]}) != len(s["pairs"]):
                errors.append(f"{where}: duplicate match text")
    if kind == "order" and len(s["items"]) < 3:
        errors.append(f"{where}: order needs three items")
    if kind == "unscramble" and len(s["word"]["as"]) < 2:
        errors.append(f"{where}: unscramble needs two tiles")
    if kind == "story":
        if s.get("map") is None and "figure" not in s and s.get("art") not in ("scroll", "calendar", "rooster", "embassy", "door", "court", "houses", "seal"):
            errors.append(f"{where}: unknown art {s.get('art')}")
    check_text(s, where)
    for m in ARTICLE.finditer(text_of({k: v.get("en") if isinstance(v, dict) else v for k, v in s.items() if isinstance(v, dict) and "en" in v})):
        for no in re.findall(r"\d+[A-Z]{0,2}(?:-[IO])?", re.sub(r"\([^)]*\)", "", m[1])):
            if no not in register:
                errors.append(f"{where}: Article {no} not in the register")


done = 0
for k in course["kings"]:
    if not k.get("lesson"):
        continue
    done += 1
    L = read(f"content/lessons/{k['lesson']}.json")
    if len(L["units"]) != budget[k["n"]]:
        errors.append(f"{k['lesson']}: {len(L['units'])} units, budget {budget[k['n']]}")
    if L["no"] != k["n"]:
        errors.append(f"{k['lesson']}: number differs from the course")
    check_text(L["mission"], k["lesson"])
    for u in L["units"]:
        check_text(u["learned"], f"{k['lesson']}/{u['id']}")
        check_text(u["mission"], f"{k['lesson']}/{u['id']}")
        check_text(u["title"], f"{k['lesson']}/{u['id']}")
        if len({p["en"] for p in u["learned"]}) != 4:
            errors.append(f"{k['lesson']}/{u['id']}: repeated learned point")
    for u in L["units"] + [L["test"]]:
        for s in u["steps"]:
            check_step(s, f"{k['lesson']}/{s['id']}")
    if sum(s["type"] == "mcq" for s in L["test"]["steps"]) > 1:
        errors.append(f"{k['lesson']}: more than one plain mcq in the test")

for e in errors:
    print(e)
print(f"Constitution check: {done} of {len(course['kings'])} lessons, {len(ids)} steps, {len(errors)} problem(s)")
sys.exit(1 if errors else 0)
