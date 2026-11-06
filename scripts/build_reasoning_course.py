#!/usr/bin/env python3
"""Generate the Reasoning course: lessons, course file, skill graph and placement probes.

Run: python3 scripts/build_reasoning_course.py && python3 scripts/check_reasoning.py && python3 scripts/build.py

The course is a draft: only the pilot lessons exist, and it is hidden from the catalog.
Past papers set the patterns only (docs/REASONING-COURSE.md). Every question is original,
and step ids are permanent. Edit this generator, not the JSON it writes.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "scripts" / "reasoning_course"), str(ROOT / "scripts" / "math_course")]
from math_kit import B, mcq  # noqa: E402
import importlib  # noqa: E402
from reason_kit import enc, face_as, face_en  # noqa: E402

COURSE = "reasoning"
SOURCE = {"title": "Axomrank original puzzles", "url": "", "used_for": "All questions and numbers are original. Patterns were studied from past papers; no question, word list or figure was copied."}
REVIEW = "Answers computed by scripts/build_reasoning_course.py and rechecked by scripts/check_reasoning.py. Independent Assamese editorial review pending."

PARTS = [("r-patterns", B("Patterns", "আৰ্হি"), 1, 8, "patterns"), ("r-position", B("Position", "অৱস্থান"), 9, 13, "position"), ("r-logic", B("Logic", "যুক্তি"), 14, 16, "logic"),
         ("r-figures", B("Figures", "চিত্ৰ"), 17, 20, "figures"), ("r-aptitude", B("APSC aptitude", "APSC যোগ্যতা"), 21, 23, "aptitude")]
TOPICS = [(1, "alphabet", B("Alphabet tools", "বৰ্ণমালাৰ কৌশল"), "A"), (2, "number-series", B("Number series", "সংখ্যা শৃংখল"), "A"), (3, "letter-series", B("Letter series", "আখৰ শৃংখল"), "A"),
          (4, "analogy", B("Analogy", "সাদৃশ্য"), "A"), (5, "odd-one-out", B("Odd one out", "বেলেগটো উলিওৱা"), "A"), (6, "coding", B("Coding and decoding", "সংকেত আৰু সংকেত ভঙা"), "A"),
          (7, "operators", B("Symbols and operators", "চিহ্ন আৰু প্ৰক্ৰিয়া"), "B"), (8, "number-puzzles", B("Number puzzles", "সংখ্যাৰ সাঁথৰ"), "A"), (9, "direction", B("Direction sense", "দিশ জ্ঞান"), "B"),
          (10, "blood-relations", B("Blood relations", "তেজৰ সম্পৰ্ক"), "B"), (11, "ranking", B("Ranking and order", "স্থান আৰু ক্ৰম"), "B"), (12, "arrangement", B("Arrangements", "সজ্জা"), "B"),
          (13, "calendar-clock", B("Calendar and clocks", "কেলেণ্ডাৰ আৰু ঘড়ী"), "B"), (14, "venn", B("Venn diagrams", "ভেন চিত্ৰ"), "B"), (15, "syllogism", B("Syllogisms", "ন্যায়"), "C"),
          (16, "statements", B("Statements and conclusions", "উক্তি আৰু সিদ্ধান্ত"), "B"), (17, "figure-patterns", B("Figure patterns", "চিত্ৰৰ আৰ্হি"), "B"), (18, "mirror-fold", B("Mirrors and folding", "দাপোণ আৰু ভাঁজ"), "B"),
          (19, "cube-count", B("Cubes and counting", "ঘনক আৰু গণনা"), "B"), (20, "number-figures", B("Numbers in figures", "চিত্ৰত সংখ্যা"), "B"), (21, "data", B("Tables and charts", "তালিকা আৰু লেখ"), "B"),
          (22, "communication", B("Communication", "যোগাযোগ"), "A"), (23, "decisions", B("Decision making", "সিদ্ধান্ত গ্ৰহণ"), "A")]
SKILLS = {
    "r-shift": ("coding", B("Move letters by a rule", "নিয়মেৰে আখৰ সৰোৱা"), []), "r-decode": ("coding", B("Undo a code", "সংকেত উভতোৱা"), ["r-shift"]), "r-pattern": ("coding", B("Find changing gaps", "সলনি হোৱা ব্যৱধান"), ["r-shift"]),
    "r-move": ("coding", B("Rearrange letters", "আখৰ পুনৰ সজোৱা"), []), "r-value": ("coding", B("Letters as numbers", "আখৰ সংখ্যা ৰূপে"), []), "r-compare": ("coding", B("Compare coded sentences", "সংকেতৰ বাক্য তুলনা"), []),
    "r-turn": ("direction", B("Left and right when turning", "ঘূৰোঁতে বাওঁ-সোঁ"), []), "r-route": ("direction", B("Follow a route", "পথ অনুসৰণ"), ["r-turn"]), "r-dist": ("direction", B("Straight distance", "পোন দূৰত্ব"), ["r-route"]), "r-shadow": ("direction", B("Sun and shadow", "সূৰ্য আৰু ছাঁ"), ["r-turn"]),
    "r-region": ("venn", B("Name a region", "অংশ চিনাক্তি"), []), "r-relate": ("venn", B("Choose the diagram", "চিত্ৰ বাছনি"), []), "r-count": ("venn", B("Count with overlaps", "সাধাৰণ অংশসহ গণনা"), ["r-region"]), "r-three": ("venn", B("Three sets", "তিনিটা সংহতি"), ["r-count"]),
}
MISCONCEPTIONS = {
    "r-m-shiftback": ("r-shift", B("Counting backwards on a + rule", "+ নিয়মত পিছলৈ গণা")), "r-m-encode": ("r-decode", B("Applying the rule again when decoding", "সংকেত ভাঙোঁতে নিয়ম আকৌ দিয়া")), "r-m-oneshift": ("r-pattern", B("Using one shift for every letter", "সকলো আখৰত একেটা স্থানান্তৰ")),
    "r-m-order": ("r-move", B("Reversing instead of the stated move", "কোৱা নিয়মৰ সলনি ওলোটোৱা")), "r-m-position": ("r-value", B("Counting from the wrong end", "ভুল মূৰৰ পৰা গণা")), "r-m-wordorder": ("r-compare", B("Trusting the word order", "শব্দৰ ক্ৰমক বিশ্বাস কৰা")),
    "r-m-leftwest": ("r-turn", B("Treating left as west", "বাওঁফালক পশ্চিম ধৰা")), "r-m-addlegs": ("r-dist", B("Adding walks instead of the straight line", "পোন দূৰত্বৰ সলনি খোজ যোগ কৰা")), "r-m-shadow": ("r-shadow", B("Putting the shadow on the sun's side", "ছাঁ সূৰ্যৰ ফালে ধৰা")),
    "r-m-only": ("r-region", B("Reading 'only' as the whole circle", "'কেৱল'ক গোটেই বৃত্ত বুলি পঢ়া")), "r-m-double": ("r-count", B("Counting the overlap twice", "সাধাৰণ অংশ দুবাৰ গণা")), "r-m-inside": ("r-relate", B("Choosing the wrong relation between sets", "সংহতিৰ ভুল সম্পৰ্ক বাছনি")),
}


# Lesson modules in course order. A later module may define SKILLS, TAGS and probes() of its own.
MODULES = [importlib.import_module(m) for m in ("lesson_alphabet", "lesson_coding", "lesson_direction", "lesson_venn")]
_series = importlib.import_module("lesson_series")
MODULES += [_series.NUMBERS, _series.LETTERS]
SKILLS.update(_series.SKILLS)
MISCONCEPTIONS.update(_series.TAGS)
for mod in MODULES:
    SKILLS.update(getattr(mod, "SKILLS", {}))
    MISCONCEPTIONS.update(getattr(mod, "TAGS", {}))


def probes():
    o = lambda sid, skill, fn, params: mcq(f"bank.rs.{sid}", skill, fn, params)
    extra = [p for mod in MODULES if hasattr(mod, "probes") for p in mod.probes()]
    return extra + [
        o("shift", "r-shift", lambda w, n: {"q": B(f"Move each letter of {w} forward {n}.", f"{w} ৰ প্ৰতিটো আখৰ {n} ঘৰ আগবঢ়োৱা।"), "right": enc(w, n), "wrong": [(enc(w, -n), "r-m-shiftback", B("That moved backwards.", "সেয়া পিছলৈ গ'ল।"))], "fill": [enc(w, n + 1), enc(w, n + 2)], "why": B(f"{w} → {enc(w, n)}.", f"{w} → {enc(w, n)}।")}, [("DUCK", 2), ("BELL", 3)]),
        o("decode", "r-decode", lambda w, n: {"q": B(f"The rule was +{n} and the code is {enc(w, n)}. What was the word?", f"নিয়ম +{n}, সংকেত {enc(w, n)}। শব্দটো কি আছিল?"), "right": w, "wrong": [(enc(w, 2 * n), "r-m-encode", B("That applied the rule again.", "সেয়া নিয়ম আকৌ দিয়া হ'ল।"))], "fill": [enc(w, 1), enc(w, n + 1), enc(w, -1)], "why": B(f"Count back {n}.", f"{n} ঘৰ পিছলৈ গণা।")}, [("NEST", 2), ("WOOD", 3)]),
        o("value", "r-value", lambda c: {"q": B(f"With Z = 1, Y = 2 and so on, what is {c}?", f"Z = 1, Y = 2 এনেদৰে ধৰিলে {c} কিমান?"), "right": 27 - (ord(c) - 64), "wrong": [(ord(c) - 64, "r-m-position", B("That counted from A.", "সেয়া A ৰ পৰা গণা হ'ল।"))], "fill": [26 - (ord(c) - 64), 28 - (ord(c) - 64), 25], "why": B("Use 27 minus its place.", "27 ৰ পৰা স্থান বিয়োগ কৰা।")}, [("F",), ("K",)]),
        o("turn", "r-turn", lambda f: {"q": B(f"You face {face_en(f)}. What is on your left?", f"তুমি {face_as(f)}লৈ মুখ কৰিছা। বাওঁফালে কি?"), "right": face_en(f + 3).capitalize(), "wrong": [("West" if f != 0 else "East", "r-m-leftwest", B("Left is west only when you face north.", "উত্তৰলৈ মুখ কৰিলেহে বাওঁফাল পশ্চিম।"))], "fill": [face_en(f).capitalize(), face_en(f + 1).capitalize(), face_en(f + 2).capitalize()], "why": B("Left is one step anticlockwise.", "বাওঁফাল ঘড়ীৰ ওলোটা দিশে এক খোজ।")}, [(1,), (2,)]),
        o("route", "r-route", lambda a, b: {"q": B(f"Walk {a} north, right, {b}, right, {a}. Where do you end?", f"উত্তৰলৈ {a}, সোঁফালে, {b}, সোঁফালে, {a}। ক'ত শেষ?"), "right": f"{b} east", "fill": [f"{b} west", f"{a} north", f"{a + b} east"], "wrong": [], "why": B(f"North and south cancel, leaving {b} east.", f"উত্তৰ-দক্ষিণ কাটে, পূবে {b}।")}, [(3, 2), (4, 5)]),
        o("dist", "r-dist", lambda a, b, c: {"q": B(f"Walk {a} north, then {b} east. What is the straight distance back?", f"উত্তৰলৈ {a}, তাৰ পিছত পূবলৈ {b}। পোন দূৰত্ব কিমান?"), "right": c, "wrong": [(a + b, "r-m-addlegs", B("That added the walks.", "সেয়া খোজ যোগ কৰা হ'ল।"))], "fill": [c + 1, c - 1, a * b], "why": B(f"{a}² + {b}² = {c}².", f"{a}² + {b}² = {c}²।")}, [(3, 4, 5), (6, 8, 10)]),
        o("region", "r-region", lambda a, b: {"q": B(f"{a} like A and {b} of them also like B. How many like A only?", f"{a} জনে A ভাল পায়, ইয়াৰে {b} জনে B ও। কেৱল A কিমান?"), "right": a - b, "wrong": [(a, "r-m-only", B("'Only' leaves out the overlap.", "'কেৱল' ত সাধাৰণ অংশ নপৰে।"))], "fill": [a + b, b, a - b + 1], "why": B(f"{a} − {b} = {a - b}.", f"{a} − {b} = {a - b}।")}, [(25, 10), (32, 14)]),
        o("count", "r-count", lambda a, b, c: {"q": B(f"{a} like A, {b} like B and {c} like both. How many like at least one?", f"{a} জনে A, {b} জনে B, {c} জনে দুয়োটা ভাল পায়। অন্ততঃ এটা কিমান?"), "right": a + b - c, "wrong": [(a + b, "r-m-double", B("That counted the overlap twice.", "সাধাৰণ অংশ দুবাৰ গণা হ'ল।"))], "fill": [a + b - 2 * c, a - c, c], "why": B(f"{a} + {b} − {c} = {a + b - c}.", f"{a} + {b} − {c} = {a + b - c}।")}, [(20, 16, 6), (30, 22, 9)]),
    ]


def tile(name, draw):
    """A plain course tile, made once. build.py makes its thumbnail."""
    path = ROOT / f"content/media/reasoning/{name}.webp"
    if path.exists():
        return
    from PIL import Image, ImageDraw
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (720, 720), "#F7FAFC")
    d = ImageDraw.Draw(img)
    for k in range(0, 720, 48):
        d.line([(k, 0), (k, 720)], fill="#DCE7F3", width=2)
        d.line([(0, k), (720, k)], fill="#DCE7F3", width=2)
    draw(d)
    img.save(path, "WEBP", quality=80)


def tiles():
    ink, blue, red, gold = "#16305C", "#1F5FBF", "#D3323F", "#D8930B"
    tile("patterns", lambda d: ([d.rounded_rectangle((120 + k * 170, 280, 260 + k * 170, 440), 24, outline=c, width=14) for k, c in enumerate((blue, gold, red))]))
    tile("position", lambda d: (d.ellipse((130, 130, 590, 590), outline=ink, width=14), d.polygon([(360, 170), (430, 360), (290, 360)], fill=red), d.polygon([(360, 550), (430, 360), (290, 360)], fill=blue)))
    tile("logic", lambda d: (d.ellipse((130, 200, 450, 520), outline=blue, width=16), d.ellipse((270, 200, 590, 520), outline=red, width=16)))
    tile("figures", lambda d: (d.polygon([(360, 130), (580, 250), (360, 370), (140, 250)], outline=ink, width=14), d.line([(140, 250), (140, 470), (360, 590), (360, 370)], fill=ink, width=14), d.line([(360, 590), (580, 470), (580, 250)], fill=ink, width=14)))
    tile("aptitude", lambda d: [d.rectangle((150 + k * 150, 540 - h, 260 + k * 150, 540), fill=c) for k, (h, c) in enumerate(((180, blue), (340, gold), (260, red)))])


def write(path, data):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def part_of(n):
    return next(p for p in PARTS if p[2] <= n <= p[3])


def main():
    tiles()
    lessons = sorted((mod.lesson() for mod in MODULES), key=lambda L: L["no"])
    by_no = {L["no"]: L for L in lessons}
    for L in lessons:
        write(f"content/lessons/{L['id']}.json", {
            "id": L["id"], "course": COURSE, "no": L["no"], "version": 1, "eyebrow": B("Reasoning", "যুক্তি"), "king": L["title"], "reign": L["reign"],
            "portrait": f"reasoning/{part_of(L['no'])[4]}.webp", "sources": [SOURCE], "review_notes": REVIEW, "map": {"box": [89.5, 24, 96.5, 28.2], "show": []},
            "units": L["units"], "test": L["test"],
        })
    kings = []
    for n, slug, title, tier in TOPICS:
        k = {"n": n, "id": f"reason-{slug}", "name": title, "reign": part_of(n)[1], "face": f"reasoning/{part_of(n)[4]}.webp", "tier": tier}
        if n in by_no:
            k["lesson"] = by_no[n]["id"]
        kings.append(k)
    write(f"content/courses/{COURSE}.json", {
        "id": COURSE, "order": 0, "draft": True, "title": B("Reasoning", "যুক্তি"), "eyebrow": B("See the rule", "নিয়মটো চিনা"),
        "subtitle": B("Stop memorising question types and learn the rule behind each puzzle", "প্ৰশ্নৰ ধৰণ মুখস্থ নকৰি প্ৰতিটো সাঁথৰৰ নিয়ম শিকা"),
        "tabs": ["lessons", "skills", "profile"], "bank": f"content/questions/{COURSE}.json", "skills": f"content/skills/{COURSE}.json",
        "kings": kings, "eras": [{"id": i, "title": t, "from": a, "to": b} for i, t, a, b, _ in PARTS], "eraWord": B("part", "ভাগ"),
    })
    write(f"content/questions/{COURSE}.json", {"questions": []})
    steps = {}
    for L in lessons:
        for u in L["units"] + [L["test"]]:
            for s in u["steps"]:
                if s.get("skill") in SKILLS:
                    steps.setdefault(s["skill"], []).append({"l": L["id"], "id": s["id"]})
    write(f"content/skills/{COURSE}.json", {
        "topics": [{"id": L["slug"], "t": L["title"]} for L in lessons],
        "skills": [{"id": i, "topic": v[0], "t": v[1], "pre": v[2], "steps": steps.get(i, [])} for i, v in SKILLS.items()],
        "misconceptions": {k: {"skill": v[0], "t": v[1]} for k, v in MISCONCEPTIONS.items()},
        "probes": probes(),
    })
    print(f"reasoning course: {len(lessons)} lessons, {sum(len(v) for v in steps.values())} skill-linked exercises, {len(probes())} probes")


if __name__ == "__main__":
    main()
