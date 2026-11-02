#!/usr/bin/env python3
"""Check the pedagogical shape of explicitly selected new lesson files.

Use alongside build.py, which checks the app's structural/media contract.
This check cannot certify source accuracy, translation, or editorial quality.
"""
import argparse
import json
from pathlib import Path


def audit(path):
    lesson = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    for u in lesson["units"]:
        at = f"{path}:{u['id']}"
        stories = [s for s in u["steps"] if s["type"] == "story"]
        exercises = [s for s in u["steps"] if s["type"] != "story"]
        if len(u.get("learned", [])) != 4:
            errors.append(f"{at}: needs four learned points")
        if not 2 <= len(stories) <= 3:
            errors.append(f"{at}: needs two or three story cards")
        if not 5 <= len(exercises) <= 7:
            errors.append(f"{at}: needs five to seven exercises")
        if len({s["type"] for s in exercises}) < 4:
            errors.append(f"{at}: needs at least four exercise types")
        if not u["steps"] or u["steps"][0]["type"] != "story":
            errors.append(f"{at}: introduce the story before testing")
        if sum(s["type"] == "mcq" and not s.get("guess") for s in exercises):
            errors.append(f"{at}: use an interaction suited to the fact instead of plain MCQ")
        for point in u.get("learned", []):
            if not all(point.get(lang, "").strip() for lang in ("en", "as")):
                errors.append(f"{at}: learned point needs both languages")
    if len(lesson["test"]["steps"]) < 5:
        errors.append(f"{path}: needs at least five lesson-test exercises")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lessons", nargs="+", type=Path)
    args = parser.parse_args()
    problems = [error for path in args.lessons for error in audit(path)]
    for error in problems:
        print(error)
    if problems:
        raise SystemExit(1)
    print(f"Lesson design audit passed: {len(args.lessons)} lesson(s)")
