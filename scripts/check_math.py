#!/usr/bin/env python3
"""Check the Mathematics course beyond what build.py can see.

Every version of every step: answers sit among distinct options, traps are wrong answers,
widget targets are reachable, skills and mistake tags exist, and no template text is left over.
"""
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
skills_file = json.loads((ROOT / "content/skills/mathematics.json").read_text(encoding="utf-8"))
SKILLS = {s["id"]: s for s in skills_file["skills"]}
TAGS = skills_file["misconceptions"]


def value(x):
    x = str(x).replace("−", "-")
    return F(x)


def reachable(s, where):
    w, t = s["widget"], s["target"]
    if w["kind"] == "fracbar" and not w.get("split") and F(t).limit_denominator(100) * w["n"] % 1:
        errors.append(f"{where}: target needs other than {w['n']} parts")
    if w["kind"] == "grid100" and not (0 <= t <= 100 and t == int(t)):
        errors.append(f"{where}: grid target")
    if w["kind"] == "numline" and F(t).limit_denominator(1000) * w.get("den", 1) % 1:
        errors.append(f"{where}: target is between notches")
    if w["kind"] == "hops" and not (1 <= t <= w.get("max", 60)):
        errors.append(f"{where}: target is off the strip")
    if w["kind"] == "blocks" and not (w.get("min", 1) <= t <= w["max"]):
        errors.append(f"{where}: target is off the slider")
    if w["kind"] == "peel":
        n = w["n"]
        for p in w.get("primes", [2, 3, 5, 7]):
            while n % p == 0:
                n //= p
        if n != 1:
            errors.append(f"{where}: {w['n']} cannot be peeled with these primes")


def check_version(s, where):
    text = json.dumps({k: v for k, v in s.items() if k != "variants"}, ensure_ascii=False)
    if re.search(r"(None|nan|\{[a-z_]+\})", re.sub(r"\\[a-z]+\{[^}]*\}|\^\{[^}]*\}|\\overline\{\d+\}|\\mathbf\{[^}]*\}", "", text)):
        errors.append(f"{where}: leftover template text")
    t = s["type"]
    if t in ("mcq", "odd"):
        opts = [o["en"] for o in s["options"]]
        if len(set(opts)) != len(opts):
            errors.append(f"{where}: repeated option {opts}")
        if len(opts) != 4:
            errors.append(f"{where}: needs four options")
        for x in s.get("traps", []):
            if x["opt"] == s["answer"]:
                errors.append(f"{where}: the right option is marked as a trap")
    if t == "solve":
        value(s["answer"])
        for x in s.get("traps", []):
            if not s.get("exact") and value(x["ans"]) == value(s["answer"]):
                errors.append(f"{where}: trap {x['ans']} equals the answer")
    if t == "explore":
        reachable(s, where)
    if t == "stepwise":
        for p in s["parts"]:
            names = [o["en"] for o in p["options"]]
            if len(set(names)) != len(names):
                errors.append(f"{where}: repeated part option {names}")
            if p.get("skill") and p["skill"] not in SKILLS:
                errors.append(f"{where}: unknown skill {p['skill']}")
            if p.get("tag") and p["tag"] not in TAGS:
                errors.append(f"{where}: unknown tag {p['tag']}")
    for x in s.get("traps", []):
        if x["tag"] not in TAGS:
            errors.append(f"{where}: unknown tag {x['tag']}")


# What each scene's state() reports. A goal on anything else could never be met.
GOALS = {"line": {"value", "span", "zoom"}, "numline": {"value", "span", "zoom"}, "array": {"c", "broke", "found"}, "gears": {"meet", "meets"}, "tiles": {"done"},
         "dial": {"closed"}, "cuts": {"common"}, "area": {"a", "b"}, "dual": {"pct"}, "scaleup": {"k"}, "shear": {"x"}, "sticks": {"c"}, "kite": {"folded"}, "roll": {"turns"}, "sectors": {"n"}, "stack": {"h"}, "net": {"open"}, "pour": {"n"}, "stairs": {"n", "paired"}, "triangle": {"k"}, "quarter": {"deg"}, "tower": {"hit"}, "track": {"exact", "done"}, "journey": {"balanced"}, "ages": {"y"}, "growth": {"years", "rate"}, "tank": {"full"}, "mandays": {"men"}, "order": {"done"}, "square": {"side"}, "diffsq": {"moved"}, "pairs": {"done"}, "ladder": {"m", "d"}, "twosale": {"a"}, "ray": {"x", "y", "on"}, "level": {"balanced"}, "seesaw": {"balanced"}, "chain": {"match"}, "fracbar": {"value"}, "grid100": {"value"}, "blocks": {"value"}}


def check_step(s, where):
    if s["type"] == "story":
        kind = (s.get("widget") or {}).get("kind")
        for t in s.get("tasks", []):
            if kind not in GOALS or not set(t["goal"]) <= GOALS[kind]:
                errors.append(f"{where}: {kind} cannot reach goal {t['goal']}")
            for lang in ("en", "as"):
                if not t["do"].get(lang) or not t["then"].get(lang):
                    errors.append(f"{where}: task needs both languages")
        return
    if s.get("skill") not in SKILLS:
        errors.append(f"{where}: unknown skill {s.get('skill')}")
    for k, v in enumerate(s.get("variants", [])):
        check_version({**s, **v}, f"{where}#{k}")
    if not s.get("variants"):
        check_version(s, where)


seen = set()
count = 0
for path in sorted((ROOT / "content/lessons").glob("math-*.json")):
    L = json.loads(path.read_text(encoding="utf-8"))
    for u in L["units"] + [L["test"]]:
        for s in u["steps"]:
            if s["id"] in seen:
                errors.append(f"{s['id']}: duplicate id")
            seen.add(s["id"])
            check_step(s, f"{L['id']}/{s['id']}")
            count += len(s.get("variants", [])) or 1
for s in skills_file["probes"]:
    if s["id"] in seen or not s["id"].startswith("bank."):
        errors.append(f"{s['id']}: probe id must be unique and start with bank.")
    seen.add(s["id"])
    check_step(s, s["id"])
    count += len(s.get("variants", [])) or 1
for s in skills_file["skills"]:
    for pre in s["pre"]:
        if pre not in SKILLS:
            errors.append(f"skill {s['id']}: unknown prerequisite {pre}")
    for ref in s["steps"]:
        if ref["id"] not in seen:
            errors.append(f"skill {s['id']}: unknown step {ref['id']}")
order = {s["id"]: k for k, s in enumerate(skills_file["skills"])}
for s in skills_file["skills"]:
    for pre in s["pre"]:
        if order.get(pre, -1) >= order[s["id"]]:
            errors.append(f"skill {s['id']}: prerequisite {pre} must come first")
for tag, m in TAGS.items():
    if m["skill"] not in SKILLS:
        errors.append(f"misconception {tag}: unknown skill {m['skill']}")

# A scene's click attribute must not be one the player itself listens for, or the player will grab the click.
engine = (ROOT / "app/engine.js").read_text(encoding="utf-8")
taken = set(re.findall(r'g\("\[(data-[a-z-]+)\]', engine))
for path in sorted((ROOT / "app").glob("math*.js")):
    for attr in set(re.findall(r'closest\("\[(data-[a-z-]+)\]', path.read_text(encoding="utf-8"))) & taken:
        errors.append(f"{path.name}: {attr} is already used by app/engine.js")

if errors:
    print(f"math check: {len(errors)} problem(s)")
    print("\n".join(f"  - {e}" for e in errors[:60]))
    sys.exit(1)
print(f"Math check passed: {count} step versions, {len(SKILLS)} skills, {len(TAGS)} mistake patterns, {len(skills_file['probes'])} probes")
