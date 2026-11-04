#!/usr/bin/env python3
"""Write article entities (art-21a) from the Constitution register and glossary.

The English heading comes from docs/research/constitution-article-register.json
and the Assamese heading from docs/research/constitution-glossary.json, so an
entity is only the official heading, with no new wording. Safe to run again.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
LETTERS = {"A": "ক", "B": "খ", "C": "গ"}   # the Assamese edition's letters for lettered articles


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def assamese_number(no):
    return no.translate(DIGITS).translate(str.maketrans(LETTERS))


articles = {a["no"]: a for a in read("docs/research/constitution-article-register.json")["articles"]}
entities = read("content/entities.json")
headings = read("docs/research/constitution-glossary.json")["articleHeadings"]
for h in headings:
    no = h["no"]
    entities[f"art-{no.lower()}"] = {
        "type": "article",
        "name": {"en": f"Article {no}", "as": f"অনুচ্ছেদ {assamese_number(no)}"},
        "meaning": {"en": articles[no]["title"], "as": h["as"]},
    }
(ROOT / "content/entities.json").write_text(json.dumps(entities, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"Article entities: {len(headings)}")
