#!/usr/bin/env python3
"""Shared helpers for the Constitution pilot lessons.

Each docs/authoring/constitution_l*.py file describes one lesson and calls
write(). Ids come from the unit and step order, so once a lesson is published do
not insert or reorder steps: add new steps at the end of a unit.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVIEW = ("AI-assisted bilingual educational content, checked against the sources listed. "
          "Fluent Assamese educator review and legal review remain pending. "
          "Scenarios are hypothetical teaching examples, not real cases.")


def B(en, as_):
    return {"en": en, "as": as_}


def story(title, paras, art=None, map=None):
    s = {"type": "story", "title": title, "text": paras}
    if map:
        s["map"] = map
    else:
        s["art"] = art
    return s


def tf(s, answer, why):
    return {"type": "tf", "s": s, "answer": answer, "why": why}


def inline(before, after, options, answer, why):
    return {"type": "inline", "before": before, "after": after, "options": options, "answer": answer, "why": why}


def match(pairs, why):
    return {"type": "match", "pairs": [[a, b] for a, b in pairs], "why": why}


def order(q, items, why):
    return {"type": "order", "q": q, "items": items, "why": why}


def odd(q, options, answer, why):
    return {"type": "odd", "q": q, "options": options, "answer": answer, "why": why}


def spot(q, en, as_, wrong_en, wrong_as, fix, answer, why):
    return {"type": "spot", "q": q, "tokens": {"en": en.split(), "as": as_.split()}, "wrong": {"en": wrong_en, "as": wrong_as}, "fix": fix, "answerText": answer, "why": why}


def who(clues, options, answer, why):
    return {"type": "whoami", "clues": clues, "options": options, "answer": answer, "why": why}


def line(q, anchors, items, why):
    """Article line: anchors are (number, label); items are (text, slot)."""
    return {"type": "timeline", "scale": "articles", "q": q, "anchors": [{"y": str(y), "l": l} for y, l in anchors], "items": [{"t": t, "slot": n} for t, n in items], "why": why}


def years(q, anchors, items, why):
    return {"type": "timeline", "q": q, "anchors": [{"y": str(y), "l": l} for y, l in anchors], "items": [{"t": t, "slot": n} for t, n in items], "why": why}


def scramble(q, en, as_syllables, answer, why):
    return {"type": "unscramble", "q": q, "word": {"en": list(en), "as": as_syllables}, "answerText": answer, "why": why}


def mcq(q, options, answer, why):
    return {"type": "mcq", "q": q, "options": options, "answer": answer, "why": why}


def mapq(q, target, choices, why):
    return {"type": "map", "q": q, "target": target, "choices": choices, "why": why}


def unit(uid, icon, title, objective, result, learned, steps):
    return {"id": uid, "icon": icon, "title": title, "mission": {"objective": objective, "result": result}, "learned": learned, "steps": steps}


def write(no, lid, king, reign, eyebrow, mission, sources, units, test, lesson_map=None, timeline=None):
    short = f"con-{no:02d}"
    for u in units + [test]:
        for k, s in enumerate(u["steps"], 1):
            s["id"] = f"{short}.{u['id']}.{k:02d}"
    lesson = {"id": lid, "course": "indian-constitution", "no": no, "version": 1, "eyebrow": eyebrow, "king": king, "reign": reign,
              "portrait": "constitution/part-tile.webp", "mission": mission, "sources": sources, "review_notes": REVIEW,
              "map": lesson_map or {"box": [88.5, 23, 97, 29], "show": []}, "guide": {"timeline": timeline or []}, "units": units, "test": test}
    (ROOT / f"content/lessons/{lid}.json").write_text(json.dumps(lesson, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    course_file = ROOT / "content/courses/indian-constitution.json"
    course = json.loads(course_file.read_text(encoding="utf-8"))
    entry = next(k for k in course["kings"] if k["n"] == no)
    assert entry["id"] == lid, (entry["id"], lid)
    entry["lesson"] = lid
    course_file.write_text(json.dumps(course, ensure_ascii=False), encoding="utf-8")
    print(f"{lid}: {len(units)} units, {sum(len(u['steps']) for u in units)} steps, {len(test['steps'])} test steps")


def add_entities(new):
    path = ROOT / "content/entities.json"
    entities = json.loads(path.read_text(encoding="utf-8"))
    entities.update(new)
    path.write_text(json.dumps(entities, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
