#!/usr/bin/env python3
"""Build the Indian History checkpoint bank from the lessons' choice steps.

Every question keeps its source_step, and ids come from step ids, so they stay
stable when the bank is rebuilt. No previous-year provenance is claimed.
"""
import json
from pathlib import Path

from build_constitution_bank import ROOT, TYPES, question


def main():
    course = json.loads((ROOT / "content/courses/indian-history.json").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "content/catalog.json").read_text(encoding="utf-8"))
    exams = next(s for s in catalog["subjects"] if s["id"] == "indian-history")["exams"]
    era_of = {k["n"]: e["id"] for e in course["eras"] for k in course["kings"] if e["from"] <= k["n"] <= e["to"]}
    out = []
    for king in course["kings"]:
        lesson = json.loads((ROOT / f"content/lessons/{king['lesson']}.json").read_text(encoding="utf-8"))
        for part in lesson["units"] + [lesson["test"]]:
            for step in part["steps"]:
                if step["type"] not in TYPES or step.get("guess"):
                    continue
                if len({o["en"].strip().lower() for o in step["options"]}) != len(step["options"]):
                    raise SystemExit(f"duplicate options in {step['id']}")
                out.append({"id": f"bank.{step['id']}", "type": "mcq", "era": era_of[king["n"]], "lesson": king["lesson"],
                            "difficulty": "hard" if step["type"] == "mcq" else "medium", "exams": exams, "q": question(step),
                            "options": step["options"], "answer": step["answer"], "why": step["why"], "source_step": step["id"]})
    bank = {"note": "Checkpoint questions built by scripts/build_indian_history_bank.py from the lessons' choice steps; each keeps its source_step. No previous-year provenance is claimed.", "questions": out}
    (ROOT / "content/questions/indian-history.json").write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"bank: {len(out)} questions")


if __name__ == "__main__":
    main()
