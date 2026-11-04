#!/usr/bin/env python3
"""Short forms for writing Constitution lessons.

Text is one string, "English|Assamese". A spot exercise marks the wrong word in
each language with *stars*. Ids follow unit and step order, so once a lesson is
published, add new steps only at the end of a unit.
"""
import json
import re

from constitution_pilot import B, ROOT, unit, write, add_entities


def split(s):
    """Split on the "|" that is not inside a [[name|shown]] link."""
    parts = re.split(r"\|(?![^\[]*\]\])", s)
    assert len(parts) == 2, s
    return parts


def t(s):
    """Turn "en|as" into a bilingual value."""
    if isinstance(s, dict):
        return s
    en, as_ = split(s)
    return B(en.strip(), as_.strip())


def many(items):
    return [t(x) for x in items]


def S(title, *paras, art="scroll", map=None):
    s = {"type": "story", "title": t(title), "text": many(paras)}
    if map:
        s["map"] = map
    else:
        s["art"] = art
    return s


def TF(s, answer, why):
    return {"type": "tf", "s": t(s), "answer": answer, "why": t(why)}


def IN(before, after, options, answer, why):
    return {"type": "inline", "before": t(before), "after": t(after), "options": many(options), "answer": answer, "why": t(why)}


def MA(pairs, why):
    return {"type": "match", "pairs": [[t(a), t(b)] for a, b in pairs], "why": t(why)}


def OR(q, items, why):
    return {"type": "order", "q": t(q), "items": many(items), "why": t(why)}


def OD(q, options, answer, why):
    return {"type": "odd", "q": t(q), "options": many(options), "answer": answer, "why": t(why)}


def SP(sentence, fix, why):
    """Sentence with the wrong word in *stars* in both languages; fix is "right|ঠিক"."""
    en, as_ = split(sentence)
    tokens, wrong, shown = {}, {}, {}
    for lang, text in (("en", en), ("as", as_)):
        words = text.strip().split()
        at = [i for i, w in enumerate(words) if w.startswith("*") or "*" in w]
        assert len(at) == 1, sentence
        wrong[lang] = at[0]
        shown[lang] = words[at[0]].replace("*", "").strip(".,।")
        tokens[lang] = [w.replace("*", "") for w in words]
    f = t(fix)
    return {"type": "spot", "q": B("One word is wrong. Tap it.", "এটা শব্দ ভুল। সেইটো টিপা।"), "tokens": tokens, "wrong": wrong,
            "fix": B("→ " + f["en"], "→ " + f["as"]), "answerText": B(f'{shown["en"]} → {f["en"]}', f'{shown["as"]} → {f["as"]}'), "why": t(why)}


def WH(clues, options, answer, why):
    return {"type": "whoami", "clues": many(clues), "options": many(options), "answer": answer, "why": t(why)}


def _timeline(q, anchors, items, why):
    return {"type": "timeline", "q": t(q), "anchors": [{"y": str(y), "l": t(l)} for y, l in anchors], "items": [{"t": t(x), "slot": n} for x, n in items], "why": t(why)}


def LI(q, anchors, items, why):
    """Article line. Anchors are (number, label); items are (text, slot)."""
    s = _timeline(q, anchors, items, why)
    s["scale"] = "articles"
    return s


def YR(q, anchors, items, why):
    return _timeline(q, anchors, items, why)


def SC(q, word, as_syllables, why):
    return {"type": "unscramble", "q": t(q), "word": {"en": list(word), "as": as_syllables}, "answerText": B(word, "".join(as_syllables)), "why": t(why)}


def MC(q, options, answer, why):
    return {"type": "mcq", "q": t(q), "options": many(options), "answer": answer, "why": t(why)}


def U(n, icon, title, objective, result, learned, *steps):
    return unit(f"u{n}", icon, t(title), t(objective), t(result), many(learned), list(steps))


def TEST(objective, result, *steps):
    return {"id": "test", "title": B("Lesson test", "পাঠৰ পৰীক্ষা"), "mission": {"objective": t(objective), "result": t(result)}, "learned": [], "steps": list(steps)}


COI = {"title": "The Constitution of India, as on 10 September 2026", "url": "https://www.legislative.gov.in/static/uploads/2025/07/95ef471035ee0b5e4e5b1cac3d3584c1.pdf", "local_source": "Constitution sources/constitution-of-india-2026-en.pdf"}


def coi(used_for):
    return {**COI, "used_for": used_for}


def src(title, url, used_for):
    return {"title": title, "url": url, "used_for": used_for}


def LESSON(no, slug, king, reign, area, label, title, hook, sources, units, test, timeline=None):
    """area is the section name; label, title and hook form the mission."""
    mission = {"label": t(label), "title": t(title), "hook": t(hook)}
    a = t(area)
    eyebrow = B("The Constitution of India · " + a["en"], "ভাৰতৰ সংবিধান · " + a["as"])
    tl = [{"y": str(y), "t": t(x), "unit": u} for y, x, u in (timeline or [])]
    course = json.loads((ROOT / "content/courses/indian-constitution.json").read_text(encoding="utf-8"))
    entry = next(k for k in course["kings"] if k["n"] == no)
    if "|" in str(reign):
        label = t(reign)
    elif isinstance(reign, str):
        label = B(reign, reign.translate(str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")))
    else:
        label = reign
    write(no, entry["id"], t(king), label, eyebrow, mission, sources, units, test, timeline=tl)
