#!/usr/bin/env python3
"""Check the Reasoning course beyond what build.py can see.

Every version of every step: distinct options, traps that are really wrong, known skills and
mistake tags, and scenes that do not start on their answer. Puzzle answers are worked out again
here from the question's own words, using none of the generator's code.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
errors = []
skills_file = json.loads((ROOT / "content/skills/reasoning.json").read_text(encoding="utf-8"))
SKILLS = {s["id"]: s for s in skills_file["skills"]}
TAGS = skills_file["misconceptions"]
GOALS = {"shift": {"k"}, "walk": {"x", "y", "f"}, "venn": {"sel"}, "alpha": {"pick"}, "gaps": {"opened", "next"}}
FACES = ["north", "east", "south", "west"]
rechecked = 0


def move(word, k):
    return "".join(chr((ord(c) - 65 + k) % 26 + 65) for c in word)


def follow(q):
    """Walk the instructions in a question's English text. Returns x, y, facing."""
    x = y = 0
    f = FACES.index(re.search(r"Face (\w+)", q).group(1))
    for verb, arg in re.findall(r"(Turn|Walk) (left|right|\d+)", q):
        if verb == "Turn":
            f = (f + (1 if arg == "right" else 3)) % 4
        else:
            x += [0, 1, 0, -1][f] * int(arg)
            y += [1, 0, -1, 0][f] * int(arg)
    return x, y, f


def recheck(s, where):
    """True if this version's answer was recomputed from its own text."""
    q = s.get("q", {}).get("en", "") if isinstance(s.get("q"), dict) else ""
    t = s["type"]
    w = s.get("widget") or {}
    def expect(got, want):
        if str(got) != str(want):
            errors.append(f"{where}: answer {got}, but the question gives {want}")
        return True
    if t == "explore" and w.get("kind") == "shift":
        return expect(move(w["word"], s["target"]), w["code"])
    if t == "explore" and w.get("kind") == "walk" and w.get("ask") == "place":
        x, y, _ = follow(q)
        return expect(s["target"], (x + 50) * 100 + y + 50)
    if t == "explore" and w.get("kind") == "walk" and "Which way do you face" in q:
        return expect(s["target"], follow(q)[2])
    m = re.match(r"Face (\w+), then turn (.+)\. Turn the walker", q)
    if m:
        f = FACES.index(m.group(1))
        for turn in m.group(2).split(" then "):
            f = (f + (1 if turn == "right" else 3)) % 4
        return expect(s["target"], f)
    if t == "explore" and w.get("kind") == "venn" and q.startswith("Shade everyone in exactly two"):
        return expect(s["target"], (1 << 3) | (1 << 5) | (1 << 6))
    if t == "explore" and w.get("kind") == "venn" and q.startswith("Shade everyone who likes exactly one"):
        return expect(s["target"], (1 << 1) | (1 << 2))
    if t != "solve":
        return False
    a = s["answer"]
    m = re.match(r"Every letter moves (\d+) places forward\. Write the code for (\w+)", q)
    if m:
        return expect(a, move(m.group(2), int(m.group(1))))
    m = re.match(r"Which letter comes (\d+) places after (\w)", q)
    if m:
        return expect(a, move(m.group(2), int(m.group(1))))
    m = re.match(r"The rule was \+(\d+)\. The code reads (\w+)", q)
    if m:
        return expect(a, move(m.group(2), -int(m.group(1))))
    m = re.match(r"Use the ring: .* Move every letter of (\w+) forward (\d+)", q)
    if m:
        return expect(a, move(m.group(1), int(m.group(2))))
    m = re.match(r"Letters take turns: \+?(−?\d+), then \+?(−?\d+)", q)
    if m:
        gaps = [int(g.replace("−", "-")) for g in m.groups()]
        word = re.search(r"code for (\w+)", q).group(1)
        return expect(a, "".join(move(c, gaps[i % 2]) for i, c in enumerate(word)))
    m = re.match(r"With A = 1, B = 2 and so on, what is the sum of the letters in (\w+)", q)
    if m:
        return expect(a, sum(ord(c) - 64 for c in m.group(1)))
    m = re.match(r"Now Z = 1, Y = 2 and so on\. What number is (\w)", q)
    if m:
        return expect(a, 91 - ord(m.group(1)))
    m = re.match(r"(\d+) students play football, (\d+) play cricket and (\d+) play both", q)
    if m:
        p, r, b = map(int, m.groups())
        return expect(a, p + r - b)
    m = re.match(r"In a class of (\d+), (\d+) read Assamese, (\d+) read English and (\d+) read both", q)
    if m:
        n, p, r, b = map(int, m.groups())
        return expect(a, n - p - r + b)
    m = re.match(r"Walk (\d+) km north, then (\d+) km east", q)
    if m:
        p, r = map(int, m.groups())
        return expect(int(a) ** 2, p * p + r * r)
    return False


def check_version(s, where):
    global rechecked
    text = json.dumps({k: v for k, v in s.items() if k != "variants"}, ensure_ascii=False)
    if re.search(r"\bNone\b|\bnan\b|\{[a-z_]+\}|\ufffd", text):
        errors.append(f"{where}: leftover template text")
    t = s["type"]
    if t == "inline":
        names = [o["en"] for o in s["options"]]
        if len(set(names)) != len(names) or not 0 <= s["answer"] < len(names):
            errors.append(f"{where}: bad inline options {names}")
    if t in ("mcq", "odd"):
        names = [o["en"] for o in s["options"]]
        if len(set(names)) != len(names) or len(names) != 4:
            errors.append(f"{where}: needs four different options {names}")
        if any(x["opt"] == s["answer"] for x in s.get("traps", [])):
            errors.append(f"{where}: the right option is marked as a trap")
    if t == "solve":
        if any(x["ans"] == s["answer"] for x in s.get("traps", [])):
            errors.append(f"{where}: a trap equals the answer")
        if s.get("input") == "letters" and not re.fullmatch(r"[A-Z]+", s["answer"]):
            errors.append(f"{where}: a letter answer must use A to Z")
        if s.get("input") != "letters" and not re.fullmatch(r"-?\d+", s["answer"]):
            errors.append(f"{where}: {s['answer']} needs a letter input")
    if t == "explore":
        w = s["widget"]
        if w["kind"] == "walk" and w.get("ask") != "place" and s["target"] == w.get("f", 0):
            errors.append(f"{where}: the walker starts on the answer")
        if w["kind"] == "walk" and w.get("ask") == "place" and s["target"] == 5050:
            errors.append(f"{where}: the route ends at the start")
        if w["kind"] == "setpick" and not 0 <= s["target"] < len(w["options"]):
            errors.append(f"{where}: no such diagram")
        if any(x["val"] == s["target"] for x in s.get("traps", [])):
            errors.append(f"{where}: a trap equals the answer")
    if t == "match":
        right = [str(p[1]["en"]).strip() for p in s["pairs"]]
        if len(set(right)) != len(right):
            errors.append(f"{where}: match has repeated answers {right}")
    if t == "unscramble" and not all(isinstance(s["word"][lang], list) for lang in ("en", "as")):
        errors.append(f"{where}: an unscramble word must be a list of tiles")
    if t == "stepwise":
        for p in s["parts"]:
            names = [o["en"] for o in p["options"]]
            if len(set(names)) != len(names):
                errors.append(f"{where}: repeated part option {names}")
            if p.get("tag") and p["tag"] not in TAGS:
                errors.append(f"{where}: unknown tag {p['tag']}")
    for x in s.get("traps", []):
        if x["tag"] not in TAGS:
            errors.append(f"{where}: unknown tag {x['tag']}")
    rechecked += recheck(s, where)


def check_step(s, where):
    if s["type"] == "story":
        kind = (s.get("widget") or {}).get("kind")
        for t in s.get("tasks", []):
            if kind not in GOALS or not set(t["goal"]) <= GOALS[kind]:
                errors.append(f"{where}: {kind} cannot reach goal {t['goal']}")
        return
    if s.get("skill") not in SKILLS:
        errors.append(f"{where}: unknown skill {s.get('skill')}")
    versions = s.get("variants", [])
    if s["type"] in ("solve", "explore", "stepwise", "mcq", "inline") and len(versions) < 2:
        errors.append(f"{where}: a generated step needs at least two variants")
    for k, v in enumerate(versions):
        check_version({**s, **v}, f"{where}#{k}")
    if not versions:
        check_version(s, where)


seen, count = set(), 0
for path in sorted((ROOT / "content/lessons").glob("rs-*.json")):
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
for tag, m in TAGS.items():
    if m["skill"] not in SKILLS:
        errors.append(f"misconception {tag}: unknown skill {m['skill']}")
taken = set(re.findall(r'g\("\[(data-[a-z-]+)\]', (ROOT / "app/engine.js").read_text(encoding="utf-8")))
for attr in set(re.findall(r'closest\("\[(data-[a-z-]+)\]', (ROOT / "app/reasonstage.js").read_text(encoding="utf-8"))) & taken:
    errors.append(f"reasonstage.js: {attr} is already used by app/engine.js")

stage = (ROOT / "app/reasonstage.js").read_text(encoding="utf-8")
if re.search(r'aria-label="[^"]*\$\{T\(|<text[^`]*?>\$\{T\(', stage):
    errors.append("reasonstage.js: T() writes HTML, so it cannot go in an attribute or SVG text; use ST() or plain text")

if errors:
    print(f"reasoning check: {len(errors)} problem(s)")
    print("\n".join(f"  - {e}" for e in errors[:60]))
    sys.exit(1)
print(f"Reasoning check passed: {count} step versions, {rechecked} answers recomputed from the question text, {len(SKILLS)} skills, {len(TAGS)} mistake patterns")
