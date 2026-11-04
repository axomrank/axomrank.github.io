#!/usr/bin/env python3
"""Build the Constitution checkpoint bank from the lessons' choice steps.

Every question keeps its source_step. Ids are derived from step ids, so they
stay stable when the bank is rebuilt. Exam tags follow the polity subject in
content/catalog.json; a TET tag waits for a decision on the course's scope.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TYPES = {"inline", "odd", "mcq"}


def blank(before, after):
    tail = after.strip()
    gap = "" if not tail or tail[0] in ".-।,:" else " "
    return f"{before} ____{gap}{tail}"


def question(step):
    if step["type"] == "inline":
        return {lang: blank(step["before"][lang], step["after"][lang]) for lang in ("en", "as")}
    return step["q"]


def main():
    course = json.loads((ROOT / "content/courses/indian-constitution.json").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "content/catalog.json").read_text(encoding="utf-8"))
    exams = next(s for s in catalog["subjects"] if s["id"] == "polity")["exams"]
    era_of = {k["n"]: e["id"] for e in course["eras"] for k in course["kings"] if e["from"] <= k["n"] <= e["to"]}
    out = []
    for king in course["kings"]:
        lesson = json.loads((ROOT / f"content/lessons/{king['lesson']}.json").read_text(encoding="utf-8"))
        for part in lesson["units"] + [lesson["test"]]:
            for step in part["steps"]:
                if step["type"] not in TYPES:
                    continue
                if len({o["en"].strip().lower() for o in step["options"]}) != len(step["options"]):
                    raise SystemExit(f"duplicate options in {step['id']}")
                out.append({
                    "id": f"bank.{step['id']}",
                    "type": "mcq",
                    "era": era_of[king["n"]],
                    "lesson": king["lesson"],
                    "difficulty": "hard" if step["type"] == "mcq" else "medium" if len(step["options"]) > 2 else "easy",
                    "exams": exams,
                    "q": question(step),
                    "options": step["options"],
                    "answer": step["answer"],
                    "why": step["why"],
                    "source_step": step["id"],
                })
    bank = {"note": "Checkpoint questions built by scripts/build_constitution_bank.py from the lessons' choice steps; each keeps its source_step.", "questions": out}
    (ROOT / "content/questions/indian-constitution.json").write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"bank: {len(out)} questions")


if __name__ == "__main__":
    main()
