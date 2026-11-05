#!/usr/bin/env python3
"""Short forms for writing Indian History lessons. Text is "English|Assamese".

Ids follow unit and step order: ih-NN.uU.SS. Once a lesson is published, add new
steps only at the end of a unit.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from constitution_kit import IN, MA, MC, OD, OR, S, SC, SP, TEST, TF, U, WH, YR, many, src, t  # noqa: E402,F401
from constitution_pilot import B, ROOT  # noqa: E402,F401

REVIEW = ("AI-assisted bilingual educational content, checked against the sources listed. "
          "Fluent Assamese educator review and historian review remain pending.")
FULL = {"base": "india", "box": [64, 6, 96, 37]}


def MP(q, target, choices, why):
    return {"type": "map", "q": t(q), "target": target, "choices": choices, "why": t(why)}


def LINK(step, lesson_id, lesson, unit_no, unit_title, note):
    step["link"] = {"lessonId": lesson_id, "lesson": lesson, "unitNo": unit_no, "unitTitle": t(unit_title), "note": t(note)}
    return step


def PLACES(new):
    """Add entities that are missing; give existing places a position if they lack one."""
    path = ROOT / "content/entities.json"
    e = json.loads(path.read_text(encoding="utf-8"))
    for k, v in new.items():
        if k not in e:
            e[k] = {"type": v[0], "name": t(v[1]), "meaning": t(v[2]), "lessons": [], **({"geo": v[3]} if len(v) > 3 else {})}
        elif len(v) > 3 and not e[k].get("geo"):
            e[k]["geo"] = v[3]
    path.write_text(json.dumps(e, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def LESSON(no, king, reign, section, label, title, hook, sources, units, test, show, timeline=None, box=None):
    short = f"ih-{no:02d}"
    course_file = ROOT / "content/courses/indian-history.json"
    course = json.loads(course_file.read_text(encoding="utf-8"))
    entry = next(k for k in course["kings"] if k["n"] == no)
    lid = entry["id"]
    for u in units + [test]:
        for k, s in enumerate(u["steps"], 1):
            s["id"] = f"{short}.{u['id']}.{k:02d}"
    sec = t(section)
    lesson = {"id": lid, "course": "indian-history", "no": no, "version": 1,
              "eyebrow": B("Indian History · " + sec["en"], "ভাৰতৰ ইতিহাস · " + sec["as"]), "king": t(king), "reign": t(reign),
              "portrait": "indian-history/era-tile.webp", "mission": {"label": t(label), "title": t(title), "hook": t(hook)},
              "sources": sources, "review_notes": REVIEW, "map": {**FULL, **({"box": box} if box else {}), "show": show},
              "guide": {"timeline": [{"y": str(y), "t": t(x), "unit": u} for y, x, u in (timeline or [])]}, "units": units, "test": test}
    (ROOT / f"content/lessons/{lid}.json").write_text(json.dumps(lesson, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    entry["lesson"] = lid
    course_file.write_text(json.dumps(course, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{lid}: {len(units)} units, {sum(len(u['steps']) for u in units)} steps, {len(test['steps'])} test steps")
