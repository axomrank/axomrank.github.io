"""Helpers for the Mathematics course generator (scripts/build_math_course.py).

Every answer, option and trap is computed here from the numbers of a variant, so
text and answer cannot drift apart. A step's id is permanent; its variants may grow.
"""
import random
from fractions import Fraction as F


def B(en, as_):
    return {"en": en, "as": as_}


def fr(a, b):
    return f"\\frac{{{a}}}{{{b}}}"


def num(x):
    """A value as plain text: 3/4, 12, 2.5."""
    if isinstance(x, F):
        if x.denominator == 1:
            return str(x.numerator)
        return f"{x.numerator}/{x.denominator}"
    if isinstance(x, float):
        return f"{x:g}"
    return str(x)


def show(x, unit=""):
    """A value inside text, typeset when it is a fraction."""
    if isinstance(x, F) and x.denominator != 1:
        if unit == "%" and (x * 1000).denominator == 1:   # 37.5% reads better than 75/2 %
            return f"{float(x):g}%"
        return f"${fr(x.numerator, x.denominator)}${unit}"
    return f"{num(x)}{unit}"


def options(sid, right, traps, fill=(), unit=""):
    """Four options: the answer, its traps, then fillers. traps: [(value, tag, why)]."""
    seen = {num(right)}
    chosen = []
    for value, tag, why in traps:
        if num(value) in seen:
            continue
        seen.add(num(value))
        chosen.append((value, tag, why))
    for value in fill:
        if len(chosen) >= 3:
            break
        if num(value) not in seen:
            seen.add(num(value))
            chosen.append((value, None, None))
    assert len(chosen) >= 3, f"{sid}: needs three distinct wrong options"
    rows = [(right, None, None)] + chosen[:3]
    random.Random(f"{sid}:{num(right)}").shuffle(rows)
    answer = next(k for k, r in enumerate(rows) if num(r[0]) == num(right))
    out = {"options": [B(show(r[0], unit), show(r[0], unit)) for r in rows], "answer": answer}
    tagged = [{"opt": k, "tag": r[1], "why": r[2]} for k, r in enumerate(rows) if r[1]]
    if tagged:
        out["traps"] = tagged
    return out


def with_variants(base, fn, params):
    versions = [fn(*p) for p in params]
    assert len(versions) >= 2, f"{base['id']}: a numeric step needs at least two variants"
    return {**base, **versions[0], "variants": versions}


def solve(sid, skill, fn, params, **extra):
    return with_variants({"id": sid, "type": "solve", "skill": skill, **extra}, fn, params)


def explore(sid, skill, fn, params, **extra):
    return with_variants({"id": sid, "type": "explore", "skill": skill, **extra}, fn, params)


def stepwise(sid, skill, fn, params, **extra):
    return with_variants({"id": sid, "type": "stepwise", "skill": skill, **extra}, fn, params)


def mcq(sid, skill, fn, params, **extra):
    def build(*p):
        v = fn(*p)
        made = options(sid, v.pop("right"), v.pop("wrong"), v.pop("fill", ()), v.pop("unit", ""))
        return {**v, **made}
    return with_variants({"id": sid, "type": "mcq", "skill": skill, **extra}, build, params)


def odd(sid, skill, fn, params):
    def build(*p):
        v = fn(*p)
        made = options(sid, v.pop("right"), [], v.pop("fill"))
        return {**v, **made}
    return with_variants({"id": sid, "type": "odd", "skill": skill}, build, params)


def tf(sid, skill, s, answer, why, trap=None):
    step = {"id": sid, "type": "tf", "skill": skill, "s": s, "answer": answer, "why": why}
    if trap:
        step["traps"] = [{"opt": not answer, "tag": trap[0], "why": trap[1]}]
    return step


def match(sid, skill, q, pairs, why):
    return {"id": sid, "type": "match", "skill": skill, "q": q, "pairs": pairs, "why": why}


def order(sid, skill, q, items, why):
    return {"id": sid, "type": "order", "skill": skill, "q": q, "items": items, "why": why}


def story(sid, title, text, widget=None, diagram=None):
    step = {"id": sid, "type": "story", "title": title, "text": text}
    if widget:
        step["widget"] = widget
    else:
        step["art"] = "scroll"
        step["diagram"] = diagram
    return step


def part(ask, right, wrong, note, skill=None, tag=None, sid=""):
    """One decision of a stepwise problem. right and wrong are ready-made bilingual options."""
    rows = [right] + wrong
    random.Random(f"{sid}:{right['en']}").shuffle(rows)
    p = {"ask": ask, "options": rows, "answer": rows.index(right), "note": note}
    if skill:
        p["skill"] = skill
    if tag:
        p["tag"] = tag
    return p


def unit(uid, title, icon, learned, steps):
    assert len(learned) == 4, f"{uid}: four learned points"
    return {"id": uid, "title": title, "icon": icon, "learned": learned, "steps": steps}
