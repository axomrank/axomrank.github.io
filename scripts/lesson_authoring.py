"""Small authoring helpers; lessons remain explicitly authored bilingual content.

These helpers do not choose facts, answers, sources, or translations.
"""
import copy


def bi(en, assamese):
    return {"en": en, "as": assamese}


def story(title, paragraphs, image, link=None):
    step = {"type": "story", "title": title, "text": paragraphs, "img": image}
    if link:
        step["link"] = link
    return step


def tf(statement, answer, why):
    return {"type": "tf", "s": statement, "answer": answer, "why": why}


def choice(kind, question, options, answer, why):
    return {"type": kind, "q": question, "options": options, "answer": answer, "why": why}


def who(clues, options, answer, why):
    return {"type": "whoami", "clues": clues, "options": options, "answer": answer, "why": why}


def match(pairs, why):
    return {"type": "match", "pairs": pairs, "why": why}


def order(items, why):
    return {"type": "order", "items": items, "why": why}


def inline(before, after, options, answer, why):
    return {"type": "inline", "before": before, "after": after,
            "options": options, "answer": answer, "why": why}


def map_question(question, target, choices, why):
    return {"type": "map", "q": question, "target": target, "choices": choices, "why": why}


def unit(uid, title, learned, steps, icon="scroll"):
    return {"id": uid, "icon": icon, "title": title, "learned": learned, "steps": steps}


def identify(lesson, prefix):
    """Assign ids only to a newly authored lesson, before its first publication."""
    for u in lesson["units"] + [lesson["test"]]:
        for n, s in enumerate(u["steps"], 1):
            if "id" in s:
                raise ValueError("Never regenerate ids on an existing lesson")
            s["id"] = f"{prefix}.{u['id']}.{n:02}"
    return lesson


def new_test(steps):
    return {"id": "test", "title": bi("Lesson test", "পাঠৰ পৰীক্ষা"),
            "learned": [], "steps": copy.deepcopy(steps)}
