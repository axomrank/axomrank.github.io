"""Lessons 17 to 20: Figures. Every figure is drawn from data, so nothing comes from a past paper."""
import json
import math
import random

from math_kit import B, explore, match, order, part, solve, stepwise, tf, unit
from math_lessons_c import diagram, lab
from math_labs import task
from reason_kit import same

SERIES = "r-fseries"; ODDF = "r-fodd"; ROT = "r-frot"; COMP = "r-fcomp"
MIRROR = "r-fmirror"; WATER = "r-fwater"; FOLD = "r-ffold"; CUTF = "r-fcut"
DIE = "r-fdie"; NETF = "r-fnet"; COUNTS = "r-fcount"; CUBES = "r-fcubes"
ROWF = "r-nrow"; COLF = "r-ncol"; SUMF = "r-nsum"; MAGIC = "r-nmagic"
SKILLS = {SERIES: ("figure-patterns", B("Figure series", "চিত্ৰ শৃংখল"), []), ROT: ("figure-patterns", B("Rotation", "ঘূৰণি"), []), ODDF: ("figure-patterns", B("Odd figure out", "বেলেগ চিত্ৰ"), []), COMP: ("figure-patterns", B("Complete the figure", "চিত্ৰ সম্পূৰ্ণ"), [ROT]),
          MIRROR: ("mirror-fold", B("Mirror images", "দাপোণৰ প্ৰতিবিম্ব"), []), WATER: ("mirror-fold", B("Water images", "পানীৰ প্ৰতিবিম্ব"), [MIRROR]), FOLD: ("mirror-fold", B("Paper folding", "কাগজ ভাঁজ"), []), CUTF: ("mirror-fold", B("Punched paper", "ফুটা কৰা কাগজ"), [FOLD]),
          DIE: ("cube-count", B("Opposite faces", "বিপৰীত পৃষ্ঠ"), []), NETF: ("cube-count", B("Cube nets", "ঘনকৰ জাল"), [DIE]), COUNTS: ("cube-count", B("Count figures", "চিত্ৰ গণনা"), []), CUBES: ("cube-count", B("Count cubes", "ঘনক গণনা"), []),
          ROWF: ("number-figures", B("Row rules", "শাৰীৰ নিয়ম"), []), COLF: ("number-figures", B("Column rules", "স্তম্ভৰ নিয়ম"), [ROWF]), SUMF: ("number-figures", B("Around a centre", "কেন্দ্ৰৰ চাৰিওফালে"), []), MAGIC: ("number-figures", B("Magic squares", "যাদুকৰী বৰ্গ"), [ROWF])}
TAGS = {"r-m-rotate": (MIRROR, B("Rotating instead of reflecting", "প্ৰতিফলনৰ সলনি ঘূৰোৱা")), "r-m-oneunfold": (FOLD, B("Forgetting that unfolding doubles", "খোলিলে দুগুণ পাহৰা")), "r-m-adjacent": (DIE, B("Treating neighbours as opposite", "কাষৰ পৃষ্ঠক বিপৰীত ধৰা")), "r-m-onerow": (ROWF, B("A rule that fits one row only", "এটা শাৰীতহে মিলা নিয়ম"))}
ROTW = B("A mirror swaps left and right but keeps up and down.", "দাপোণে বাওঁ-সোঁ সলায়, ওপৰ-তল নহয়।")
UNF = B("Each unfold doubles the holes.", "প্ৰতিটো খোলাত ফুটা দুগুণ হয়।")
ADJ = B("Touching squares in a net become neighbours, not opposites.", "জালত লগ লগা বৰ্গ কাষৰীয়া হয়, বিপৰীত নহয়।")
ONER = B("Check the rule on every row.", "প্ৰতিটো শাৰীত নিয়ম চোৱা।")


def arrow(deg, cx=50, cy=50, r=32):
    a = math.radians(deg)
    x, y = round(cx + r * math.sin(a), 1), round(cy - r * math.cos(a), 1)
    bx, by = round(cx - r * math.sin(a), 1), round(cy + r * math.cos(a), 1)
    l = math.radians(deg + 150)
    k = math.radians(deg - 150)
    return [["l", bx, by, x, y], ["p", [[x, y], [round(x + 15 * math.sin(l), 1), round(y - 15 * math.cos(l), 1)], [round(x + 15 * math.sin(k), 1), round(y - 15 * math.cos(k), 1)]], "#D3323F"]]


def dots(n):
    pts = [(30, 30), (70, 30), (30, 70), (70, 70), (50, 50), (50, 15), (50, 85), (15, 50), (85, 50)]
    return [["c", x, y, 8, "#1F5FBF"] for x, y in pts[:n]]


def poly(n):
    pts = [[round(50 + 38 * math.sin(2 * math.pi * k / n), 1), round(50 - 38 * math.cos(2 * math.pi * k / n), 1)] for k in range(n)]
    return [["p", pts, None]]


FIGS = [
    [["l", 30, 15, 30, 85], ["p", [[30, 15], [75, 30], [30, 45]], "#D3323F"], ["r", 55, 70, 15, 10, "#1F5FBF"]],
    [["p", [[20, 20], [45, 20], [45, 60], [80, 60], [80, 85], [20, 85]], None], ["c", 32, 35, 6, "#D3323F"]],
    [["p", [[20, 80], [50, 20], [80, 80]], None], ["l", 50, 20, 20, 80], ["r", 60, 25, 16, 16, "#1F5FBF"]],
]


def flag(flip=False, down=False, kind=0):
    """An asymmetric figure. flip mirrors left-right; down mirrors top-bottom."""
    x = lambda v: 100 - v if flip else v
    y = lambda v: 100 - v if down else v
    out = []
    for s in FIGS[kind % len(FIGS)]:
        if s[0] == "l":
            out.append(["l", x(s[1]), y(s[2]), x(s[3]), y(s[4])])
        elif s[0] == "c":
            out.append(["c", x(s[1]), y(s[2]), s[3], s[4]])
        elif s[0] == "p":
            out.append(["p", [[x(a), y(b)] for a, b in s[1]], s[2]])
        else:
            out.append(["r", min(x(s[1]), x(s[1] + s[3])), min(y(s[2]), y(s[2] + s[4])), s[3], s[4], s[5]])
    return out


def pick_fig(q, stem, options, answer, why, trap=None):
    # Shuffle by a fixed seed, so the right figure is not always in one place.
    order_ = list(range(len(options)))
    random.Random(json.dumps([stem, options])).shuffle(order_)
    step = {"q": q, "widget": {"kind": "figpick", "options": [options[k] for k in order_]}, "target": order_.index(answer), "answerText": why, "why": why, "traps": []}
    if stem:
        step["widget"]["stem"] = stem
    if trap:
        step["traps"] = [{"val": order_.index(trap[0]), "tag": trap[1], "why": trap[2]}]
    return step


def arrow_next(step_, start):
    stem = [arrow(start + step_ * i) for i in range(3)] + [None]
    right = start + step_ * 3
    return pick_fig(B(f"The arrow turns the same amount each time. Pick the next one.", "কাঁড়ডাল প্ৰতিবাৰ একে পৰিমাণে ঘূৰে। পিছৰটো বাছা।"), stem, [arrow(right), arrow(right + 90), arrow(right + 180), arrow(right + 270)], 0, B(f"It turns {step_}° each step.", f"প্ৰতিবাৰ {step_}° ঘূৰে।"))


def dot_next(a, d):
    stem = [dots(a + d * i) for i in range(3)] + [None]
    n = a + d * 3
    return pick_fig(B("How many dots come next?", "পিছত কিমান বিন্দু?"), stem, [dots(n - 1), dots(n), dots(n + 1), dots(n + 2)], 1, B(f"The count rises by {d}.", f"সংখ্যা {d} ৰে বাঢ়ে।"))


def side_next(a):
    stem = [poly(a), poly(a + 1), poly(a + 2), None]
    return pick_fig(B("Which shape continues the pattern?", "কোন আকৃতিয়ে আৰ্হি আগবঢ়ায়?"), stem, [poly(a + 3), poly(a), poly(a + 1), poly(a + 2)], 0, B("Each shape gains one side.", "প্ৰতিটো আকৃতিত এটা বাহু বাঢ়ে।"))


def odd_side(n, bad):
    opts = [poly(n) + [["c", 50, 50, 4 + k, None]] for k in range(3)] + [poly(bad)]
    return pick_fig(B("Which figure is the odd one out?", "কোন চিত্ৰ বেলেগ?"), None, opts, 3, B(f"The others have {n} sides.", f"বাকীবোৰৰ {n} বাহু।"))


def odd_arrow(base):
    return pick_fig(B("Three arrows match when rotated. Which is the odd one, with an extra mark?", "তিনিডাল কাঁড় ঘূৰালে মিলে। বেলেগ চিনযুক্তটো কোনটো?"), None, [arrow(base), arrow(base + 90), arrow(base + 180), arrow(base + 45) + [["c", 15, 15, 6, "#1F5FBF"]]], 3, B("Only one has the extra mark.", "এটাতহে অতিৰিক্ত চিন।"))


def mirror_q(extra):
    return pick_fig(B("A mirror stands to the right of this flag. Pick its image.", "এই ধ্বজাৰ সোঁফালে দাপোণ। প্ৰতিবিম্ব বাছা।"), [flag(kind=extra)], [flag(down=True, kind=extra), flag(flip=True, kind=extra), flag(kind=extra), flag(flip=True, down=True, kind=extra)], 1, B("Left and right swap; up and down stay.", "বাওঁ-সোঁ সলনি; ওপৰ-তল একে।"), (3, "r-m-rotate", ROTW))


def water_q(extra):
    return pick_fig(B("This flag stands above still water. Pick its reflection.", "এই ধ্বজা স্থিৰ পানীৰ ওপৰত। প্ৰতিফলন বাছা।"), [flag(kind=extra)], [flag(flip=True, kind=extra), flag(down=True, kind=extra), flag(kind=extra), flag(flip=True, down=True, kind=extra)], 1, B("Up and down swap; left and right stay.", "ওপৰ-তল সলনি; বাওঁ-সোঁ একে।"), (3, "r-m-rotate", B("Water swaps up and down only.", "পানীয়ে কেৱল ওপৰ-তল সলায়।")))


def sheet(holes):
    return [["r", 12, 12, 76, 76, "#fff"]] + [["c", x, y, 6, "#16305C"] for x, y in holes]


def fold_q(x, y):
    """One fold along the centre line, one hole at (x, y) on the left half."""
    right = sheet([(x, y), (100 - x, y)])
    return pick_fig(B("A square is folded in half left to right, and a hole is punched. Which is it unfolded?", "বৰ্গক বাওঁ-সোঁ আধা ভাঁজ কৰি ফুটা কৰা হ'ল। খুলিলে কোনটো?"), [sheet([(x, y)]) + [["l", 50, 12, 50, 88]]], [sheet([(x, y)]), right, sheet([(x, y), (x, 100 - y)]), sheet([(100 - x, y)])], 1, B("The hole appears on both sides of the fold.", "ফুটা ভাঁজৰ দুয়োফালে হয়।"), (0, "r-m-oneunfold", UNF))


def fold2_q(x, y):
    right = sheet([(x, y), (100 - x, y), (x, 100 - y), (100 - x, 100 - y)])
    return pick_fig(B("A square is folded twice into a quarter, and one hole is punched. Which is it unfolded?", "বৰ্গক দুবাৰ ভাঁজ কৰি চতুৰ্থাংশ কৰি এটা ফুটা কৰা হ'ল। খুলিলে কোনটো?"), [sheet([(x, y)]) + [["l", 50, 12, 50, 88], ["l", 12, 50, 88, 50]]], [sheet([(x, y), (100 - x, y)]), right, sheet([(x, y)]), sheet([(x, y), (100 - x, 100 - y)])], 1, B("Two folds give four holes.", "দুটা ভাঁজত চাৰিটা ফুটা।"), (0, "r-m-oneunfold", UNF))


NET = [[None, 1, None, None], [2, 3, 4, 5], [None, 6, None, None]]
OPP = {1: 6, 6: 1, 2: 4, 4: 2, 3: 5, 5: 3}


def opp_q(m):
    return {"q": B(f"Fold this net into a cube. Tap the face opposite {m}.", f"এই জাল ভাঁজ কৰি ঘনক বনোৱা। {m} ৰ বিপৰীত পৃষ্ঠ টিপা।"), "widget": {"kind": "dicenet", "net": NET, "mark": m}, "target": OPP[m], "answerText": same(OPP[m]), "why": B("In a straight row, faces two apart are opposite.", "পোন শাৰীত এঘৰ এৰি থকা পৃষ্ঠ বিপৰীত।"), "traps": []}


def grid_squares(n):
    return sum((n - k) ** 2 for k in range(n))


def stack_count(layers):
    return sum(layers)


def lesson_patterns():
    p = "rs17"
    u1 = unit("u1", B("Follow one feature", "এটা বৈশিষ্ট্য অনুসৰণ"), "star", [B("Watch one feature at a time.", "এবাৰত এটা বৈশিষ্ট্য চোৱা।"), B("Count sides, dots and lines.", "বাহু, বিন্দু, ৰেখা গণা।"), B("Then look at direction.", "তাৰ পিছত দিশ।"), B("Test the rule on every step.", "প্ৰতিটো খোজত চোৱা।")], [
        diagram(f"{p}.u1.s1", B("One thing changes", "এটা বস্তু সলনি হয়"), [B("Most figure series change one feature. Find it and ignore the rest.", "বেছিভাগ শৃংখলত এটা বৈশিষ্ট্য সলনি হয়। সেইটো বিচাৰা।")], "flow", [B("Count", "গণনা"), B("Direction", "দিশ"), B("Shading", "ছাঁ")]),
        diagram(f"{p}.u1.s2", B("Count before you compare", "তুলনাৰ আগতে গণা"), [B("Numbers are easier than shapes. Turn each figure into a count.", "আকৃতিতকৈ সংখ্যা সহজ। প্ৰতিটো চিত্ৰক গণনালৈ আনা।")], "flow", [same("3"), same("4"), same("5"), same("6")]),
        explore(f"{p}.u1.q1", SERIES, dot_next, [(1, 1), (2, 1), (1, 2)]),
        explore(f"{p}.u1.q2", SERIES, side_next, [(3,), (4,), (5,)]),
        tf(f"{p}.u1.q3", SERIES, B("Compare one feature at a time.", "এবাৰত এটা বৈশিষ্ট্য তুলনা কৰা।"), True, B("Several at once confuse.", "একেলগে বহুত হ'লে বিভ্ৰান্ত হয়।")),
        match(f"{p}.u1.q4", SERIES, B("Match the shape to its sides", "আকৃতিক বাহুৰ লগত মিলোৱা"), [[B("Triangle", "ত্ৰিভুজ"), same(3)], [B("Square", "বৰ্গ"), same(4)], [B("Hexagon", "ষড়ভুজ"), same(6)]], B("Count them.", "গণা।")),
        order(f"{p}.u1.q5", SERIES, B("Features to check in order", "বৈশিষ্ট্য ক্ৰমে চোৱা"), [B("Count", "গণনা"), B("Direction", "দিশ"), B("Shading", "ছাঁ"), B("Position", "স্থান")], B("Quickest first.", "খৰটো আগতে।")),
    ])
    u2 = unit("u2", B("Figures that turn", "ঘূৰা চিত্ৰ"), "star", [B("Clockwise follows the clock.", "ঘড়ীৰ দিশ।"), B("90° is a quarter turn.", "90° এক চতুৰ্থাংশ।"), B("180° points the opposite way.", "180° ওলোটা।"), B("45° is half of a quarter turn.", "45° চতুৰ্থাংশৰ আধা।")], [
        diagram(f"{p}.u2.s1", B("Measure each turn", "প্ৰতিটো ঘূৰণি জোখা"), [B("Compare two neighbours to find the turn, then repeat it.", "দুটা কাষৰ চিত্ৰৰ পৰা ঘূৰণি উলিয়াই পুনৰ কৰা।")], "flow", [same("0°"), same("90°"), same("180°"), same("270°")]),
        diagram(f"{p}.u2.s2", B("Four turns return", "চাৰি ঘূৰণিত উভতে"), [B("Four quarter turns bring a figure home.", "চাৰিটা চতুৰ্থাংশ ঘূৰণিত চিত্ৰ উভতে।")], "flow", [same("× 4"), same("90°"), same("360°")]),
        explore(f"{p}.u2.q1", ROT, arrow_next, [(90, 0), (45, 0), (90, 45), (45, 90)]),
        tf(f"{p}.u2.q2", ROT, B("Two 90° turns equal a 180° turn.", "দুটা 90° ঘূৰণি 180° ৰ সমান।"), True, B("90 + 90 = 180.", "90 + 90 = 180।")),
        match(f"{p}.u2.q3", ROT, B("Start pointing up: match", "ওপৰমুখীৰ পৰা মিলোৱা"), [[same("90°"), B("Right", "সোঁ")], [same("180°"), B("Down", "তল")], [same("270°"), B("Left", "বাওঁ")]], B("Clockwise.", "ঘড়ীৰ দিশে।")),
        solve(f"{p}.u2.q4", ROT, lambda a, n: {"q": B(f"A figure turns {a}° each step. What is the total after {n} steps, within one circle?", f"চিত্ৰ প্ৰতিবাৰ {a}° ঘূৰে। {n} খোজৰ পিছত এক বৃত্তৰ ভিতৰত মুঠ কিমান?"), "answer": str(a * n % 360), "suffix": B("°", "°"), "why": B(f"{a} × {n} = {a * n}, minus whole circles.", f"{a} × {n} = {a * n}, পূৰ্ণ বৃত্ত বাদ।")}, [(90, 3), (45, 10), (90, 6)]),
        order(f"{p}.u2.q5", ROT, B("Clockwise from up", "ওপৰৰ পৰা ঘড়ীৰ দিশে"), [B("Up", "ওপৰ"), B("Right", "সোঁ"), B("Down", "তল"), B("Left", "বাওঁ")], B("Clock order.", "ঘড়ীৰ ক্ৰম।")),
    ])
    u3 = unit("u3", B("The odd figure", "বেলেগ চিত্ৰ"), "star", [B("Find what three share.", "তিনিটাৰ উমৈহতীয়া বিচাৰা।"), B("Rotation may hide a match.", "ঘূৰণিয়ে মিল লুকুৱাব পাৰে।"), B("Count sides first.", "প্ৰথমে বাহু।"), B("Look for one extra mark.", "অতিৰিক্ত চিন বিচাৰা।")], [
        diagram(f"{p}.u3.s1", B("Turn it in your head", "মনতে ঘূৰোৱা"), [B("Rotated figures are the same figure. Look past the direction.", "ঘূৰা চিত্ৰ একেটাই। দিশৰ বাহিৰে চোৱা।")], "flow", [B("Same shape", "একে আকৃতি"), B("New direction", "নতুন দিশ"), B("Still a match", "এতিয়াও মিল")]),
        diagram(f"{p}.u3.s2", B("Hunt small differences", "সৰু পাৰ্থক্য"), [B("If the shapes match, look for a dot, a line or a missing side.", "আকৃতি মিলিলে বিন্দু, ৰেখা বা নোহোৱা বাহু চোৱা।")], "grid", [B("Dot", "বিন্দু"), B("Line", "ৰেখা"), B("Side", "বাহু"), B("Shade", "ছাঁ")]),
        explore(f"{p}.u3.q1", ODDF, odd_side, [(4, 3), (5, 4), (6, 5)]),
        explore(f"{p}.u3.q2", ODDF, odd_arrow, [(0,), (45,), (90,)]),
        tf(f"{p}.u3.q3", ODDF, B("A rotated figure counts as the same figure.", "ঘূৰোৱা চিত্ৰ একেটাই।"), True, B("Rotation keeps the shape.", "ঘূৰণিয়ে আকৃতি নসলায়।")),
        match(f"{p}.u3.q4", ODDF, B("Match the difference to the check", "পাৰ্থক্যক পৰীক্ষাৰ লগত মিলোৱা"), [[B("Number of sides", "বাহুৰ সংখ্যা"), B("Count", "গণনা")], [B("Direction", "দিশ"), B("Rotate", "ঘূৰোৱা")], [B("Extra mark", "অতিৰিক্ত চিন"), B("Look closely", "ভালকৈ চোৱা")]], B("One check per feature.", "প্ৰতিটো বৈশিষ্ট্যৰ এটা পৰীক্ষা।")),
        order(f"{p}.u3.q5", ODDF, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Count sides", "বাহু গণা"), B("Allow rotation", "ঘূৰণি ধৰা"), B("Check marks", "চিন চোৱা"), B("Pick the misfit", "নিমিলা বাছা")], B("Broad to fine.", "বহলৰ পৰা সূক্ষ্মলৈ।")),
    ])
    u4 = unit("u4", B("Complete the figure", "চিত্ৰ সম্পূৰ্ণ কৰা"), "star", [B("Look for symmetry.", "সমমিতি বিচাৰা।"), B("The missing part mirrors another.", "নোহোৱা অংশ আন এটাৰ প্ৰতিবিম্ব।"), B("Lines must continue across.", "ৰেখা আগবাঢ়িব লাগিব।"), B("Test options against the edge.", "বিকল্প কাষত মিলোৱা।")], [
        diagram(f"{p}.u4.s1", B("Symmetry finishes it", "সমমিতিয়ে সম্পূৰ্ণ কৰে"), [B("A patterned square usually repeats across its middle lines.", "আৰ্হিযুক্ত বৰ্গ সাধাৰণতে মাজৰ ৰেখাত ঘূৰি আহে।")], "flow", [B("Find the line", "ৰেখা বিচাৰা"), B("Copy across", "সিপাৰে নকল"), B("Check the edge", "কাষ চোৱা")]),
        diagram(f"{p}.u4.s2", B("Lines cannot stop", "ৰেখা ৰ'ব নোৱাৰে"), [B("A line reaching the gap must continue into the correct piece.", "খালী ঠাইলৈ অহা ৰেখা শুদ্ধ টুকুৰাত আগবাঢ়িব।")], "flow", [B("Line at the gap", "খালী ঠাইৰ ৰেখা"), B("Match its height", "উচ্চতা মিলোৱা"), B("Keep that piece", "টুকুৰা ৰাখা")]),
        explore(f"{p}.u4.q1", COMP, lambda x: pick_fig(B("Which piece completes a figure that is mirrored left to right?", "বাওঁ-সোঁ সমমিত চিত্ৰ কোন টুকুৰাই সম্পূৰ্ণ কৰে?"), [flag(kind=x), None], [flag(down=True, kind=x), flag(flip=True, kind=x), flag(kind=x), flag(flip=True, down=True, kind=x)], 1, B("The second half mirrors the first.", "দ্বিতীয় আধা প্ৰথমৰ প্ৰতিবিম্ব।")), [(0,), (1,), (2,)]),
        tf(f"{p}.u4.q2", COMP, B("A line must continue across a missing piece.", "নোহোৱা টুকুৰাত ৰেখা আগবাঢ়িব লাগে।"), True, B("It cannot just stop.", "হঠাৎ নৰয়।")),
        match(f"{p}.u4.q3", COMP, B("Match the shape to its symmetry lines", "আকৃতিক সমমিতি ৰেখাৰ লগত মিলোৱা"), [[B("Square", "বৰ্গ"), same(4)], [B("Rectangle", "আয়ত"), same(2)], [B("Equilateral triangle", "সমবাহু ত্ৰিভুজ"), same(3)]], B("Fold to test.", "ভাঁজ কৰি চোৱা।")),
        solve(f"{p}.u4.q4", COMP, lambda n: {"q": B(f"How many lines of symmetry has a regular {n}-sided figure?", f"{n} বাহুৰ সুষম চিত্ৰৰ সমমিতি ৰেখা কিমান?"), "answer": str(n), "why": B("One for each side.", "প্ৰতিটো বাহুৰ বাবে এটা।")}, [(5,), (6,), (8,)]),
        order(f"{p}.u4.q5", COMP, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find the symmetry", "সমমিতি"), B("Read the edges", "কাষ পঢ়া"), B("Test pieces", "টুকুৰা চোৱা"), B("Confirm", "নিশ্চিত")], B("Edges decide.", "কাষে ঠিক কৰে।")),
    ])
    test = {"id": "test", "title": B("Figure pattern test", "চিত্ৰ আৰ্হিৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", SERIES, dot_next, [(2, 1), (1, 1)]),
        explore(f"{p}.t.q2", ROT, arrow_next, [(90, 90), (45, 45)]),
        explore(f"{p}.t.q3", SERIES, side_next, [(3,), (5,)]),
        explore(f"{p}.t.q4", ODDF, odd_side, [(3, 4), (6, 7)]),
        tf(f"{p}.t.q5", ROT, B("Four 90° turns return a figure to its start.", "চাৰিটা 90° ঘূৰণিত চিত্ৰ উভতি আহে।"), True, B("360°.", "360°।")),
        tf(f"{p}.t.q6", COMP, B("A square has 4 lines of symmetry.", "বৰ্গৰ 4 টা সমমিতি ৰেখা।"), True, B("Two sides, two diagonals.", "দুটা মাজৰ, দুটা কৰ্ণ।")),
    ]}
    return {"id": "rs-17-figure-patterns", "no": 17, "slug": "figure-patterns", "title": B("Figure patterns", "চিত্ৰৰ আৰ্হি"), "reign": B("Series, rotation, odd figure", "শৃংখল, ঘূৰণি, বেলেগ চিত্ৰ"), "units": [u1, u2, u3, u4], "test": test}


def lesson_mirror():
    p = "rs18"
    u1 = unit("u1", B("A mirror swaps sides", "দাপোণে ফাল সলায়"), "star", [B("A side mirror swaps left and right.", "কাষৰ দাপোণে বাওঁ-সোঁ সলায়।"), B("Up and down stay.", "ওপৰ-তল একে।"), B("Reflection is not rotation.", "প্ৰতিফলন ঘূৰণি নহয়।"), B("Check one corner.", "এটা চুক চোৱা।")], [
        diagram(f"{p}.u1.s1", B("Each point crosses the line", "প্ৰতিটো বিন্দু ৰেখা পাৰ হয়"), [B("A point near the mirror stays near. A far point stays far, on the other side.", "দাপোণৰ ওচৰৰ বিন্দু ওচৰত, দূৰৰটো দূৰত, সিপাৰে।")], "flow", [B("Near stays near", "ওচৰ ওচৰতে"), B("Far stays far", "দূৰ দূৰতে"), B("Sides swap", "ফাল সলনি")]),
        diagram(f"{p}.u1.s2", B("Follow one corner", "এটা চুক অনুসৰণ"), [B("Pick one distinctive corner and track it only.", "এটা বিশেষ চুক বাছি সেইটোহে চোৱা।")], "flow", [B("Pick a corner", "চুক বাছা"), B("Swap its side", "ফাল সলোৱা"), B("Find the option", "বিকল্প উলিওৱা")]),
        explore(f"{p}.u1.q1", MIRROR, mirror_q, [(0,), (1,), (2,)]),
        tf(f"{p}.u1.q2", MIRROR, B("In a side mirror, a figure's top stays at the top.", "কাষৰ দাপোণত ওপৰ ওপৰতে থাকে।"), True, B("Only left and right swap.", "কেৱল বাওঁ-সোঁ।"), ("r-m-rotate", ROTW)),
        match(f"{p}.u1.q3", MIRROR, B("Match the letter to its mirror behaviour", "আখৰক প্ৰতিবিম্বৰ লগত মিলোৱা"), [[same("A"), B("Looks the same", "একে দেখি")], [same("F"), B("Reversed", "ওলোটা")], [same("O"), B("Unchanged", "সলনি নহয়")]], B("Symmetric letters look unchanged.", "সমমিত আখৰ একে।")),
        solve(f"{p}.u1.q4", MIRROR, lambda h, m: {"q": B(f"A clock shows {h}:{m:02d} in a mirror. What is the real minutes value past the hour? Use 11:60 minus the shown time.", f"দাপোণত ঘড়ী {h}:{m:02d}। প্ৰকৃত মিনিট কিমান? 11:60 ৰ পৰা বিয়োগ কৰা।"), "answer": str(60 - m), "why": B(f"60 − {m} = {60 - m}.", f"60 − {m} = {60 - m}।")}, [(3, 20), (4, 45), (7, 10)]),
        order(f"{p}.u1.q5", MIRROR, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find the mirror", "দাপোণ উলিওৱা"), B("Pick a corner", "চুক বাছা"), B("Flip its side", "ফাল সলোৱা"), B("Match the option", "বিকল্প মিলোৱা")], B("One corner decides.", "এটা চুকে ঠিক কৰে।")),
    ])
    u2 = unit("u2", B("Water images", "পানীৰ প্ৰতিবিম্ব"), "star", [B("Water sits below a figure.", "পানী চিত্ৰৰ তলত।"), B("It swaps top and bottom.", "ওপৰ-তল সলায়।"), B("Left and right stay.", "বাওঁ-সোঁ একে।"), B("Do not confuse it with a side mirror.", "কাষৰ দাপোণৰ লগত মিহলাই নাপেলাবা।")], [
        diagram(f"{p}.u2.s1", B("The line is horizontal", "ৰেখা আনুভূমিক"), [B("The water line lies flat, so points cross it up and down.", "পানীৰ ৰেখা আনুভূমিক, বিন্দু ওপৰ-তললৈ পাৰ হয়।")], "flow", [B("Top", "ওপৰ"), B("Water line", "পানীৰ ৰেখা"), B("Bottom", "তল")]),
        diagram(f"{p}.u2.s2", B("Compare the two", "দুয়োটা তুলনা"), [B("Side mirror: left, right. Water: up, down.", "কাষৰ দাপোণ: বাওঁ, সোঁ। পানী: ওপৰ, তল।")], "grid", [B("Mirror swaps sides", "দাপোণে ফাল সলায়"), B("Water swaps ends", "পানীয়ে মূৰ সলায়")]),
        explore(f"{p}.u2.q1", WATER, water_q, [(0,), (1,), (2,)]),
        tf(f"{p}.u2.q2", WATER, B("A water image swaps left and right.", "পানীৰ প্ৰতিবিম্বে বাওঁ-সোঁ সলায়।"), False, B("It swaps up and down.", "ওপৰ-তল সলায়।")),
        match(f"{p}.u2.q3", WATER, B("Match the reflection to the swap", "প্ৰতিফলনক সলনিৰ লগত মিলোৱা"), [[B("Side mirror", "কাষৰ দাপোণ"), B("Left, right", "বাওঁ, সোঁ")], [B("Water", "পানী"), B("Up, down", "ওপৰ, তল")], [B("Half turn", "আধা ঘূৰণি"), B("Both", "দুয়োটা")]], B("Remember all three.", "তিনিওটা মনত ৰাখা।")),
        order(f"{p}.u2.q4", WATER, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find the line", "ৰেখা উলিওৱা"), B("Choose the axis", "অক্ষ বাছা"), B("Flip one corner", "চুক সলোৱা"), B("Match", "মিলোৱা")], B("Axis first.", "অক্ষ আগতে।")),
        explore(f"{p}.u2.q5", WATER, water_q, [(1,), (2,)]),
    ])
    u3 = unit("u3", B("Folded paper", "ভাঁজ কৰা কাগজ"), "star", [B("Each fold halves the sheet.", "প্ৰতিটো ভাঁজে আধা কৰে।"), B("Unfolding mirrors across the fold.", "খোলিলে ভাঁজত প্ৰতিবিম্ব।"), B("Holes double with each unfold.", "ফুটা প্ৰতিবাৰ দুগুণ।"), B("Unfold one step at a time.", "এখোজকৈ খোলা।")], [
        diagram(f"{p}.u3.s1", B("A fold is a mirror", "ভাঁজ এখন দাপোণ"), [B("The fold line acts like a mirror, so each hole gets a partner.", "ভাঁজ দাপোণৰ দৰে, প্ৰতিটো ফুটাৰ সংগী হয়।")], "flow", [B("Fold", "ভাঁজ"), B("Punch", "ফুটা"), B("Unfold", "খোলা")]),
        diagram(f"{p}.u3.s2", B("Work backward", "ওলোটাকৈ"), [B("Unfold the last fold first, then the one before.", "শেষৰ ভাঁজ আগতে খোলা, তাৰ পিছত আগৰটো।")], "flow", [B("Last fold", "শেষৰ ভাঁজ"), B("Earlier fold", "আগৰ ভাঁজ"), B("Whole sheet", "গোটেই কাগজ")]),
        explore(f"{p}.u3.q1", FOLD, fold_q, [(30, 30), (35, 60), (25, 45)]),
        solve(f"{p}.u3.q2", FOLD, lambda f: {"q": B(f"A sheet is folded {f} times and one hole is punched through. How many holes when unfolded?", f"কাগজ {f} বাৰ ভাঁজ কৰি এটা ফুটা কৰা হ'ল। খুলিলে কিমান ফুটা?"), "answer": str(2 ** f), "why": B("Each fold doubles.", "প্ৰতিটো ভাঁজে দুগুণ কৰে।"), "traps": [{"ans": str(f), "tag": "r-m-oneunfold", "why": UNF}]}, [(2,), (3,), (4,)]),
        tf(f"{p}.u3.q3", FOLD, B("One fold and one punch give two holes.", "এটা ভাঁজ আৰু এটা ফুটাত দুটা ফুটা।"), True, B("One each side.", "দুয়োফালে এটাকৈ।")),
        match(f"{p}.u3.q4", FOLD, B("Match folds to holes", "ভাঁজক ফুটাৰ লগত মিলোৱা"), [[same("1 fold"), same(2)], [same("2 folds"), same(4)], [same("3 folds"), same(8)]], B("Powers of 2.", "2 ৰ ঘাত।")),
        order(f"{p}.u3.q5", FOLD, B("Paper steps in order", "কাগজৰ খোজ ক্ৰমে"), [B("Fold", "ভাঁজ"), B("Punch", "ফুটা"), B("Unfold last fold", "শেষৰ ভাঁজ খোলা"), B("Unfold first fold", "প্ৰথম ভাঁজ খোলা")], B("Last fold first.", "শেষৰ ভাঁজ আগতে।")),
    ])
    u4 = unit("u4", B("Two folds and cuts", "দুটা ভাঁজ আৰু কটা"), "star", [B("Two folds make a quarter.", "দুটা ভাঁজত চতুৰ্থাংশ।"), B("A hole becomes four.", "এটা ফুটা চাৰিটা।"), B("Holes keep their distance from a fold.", "ফুটাই ভাঁজৰ পৰা দূৰত্ব ৰাখে।"), B("A cut works like a hole.", "কটাও ফুটাৰ দৰে।")], [
        diagram(f"{p}.u4.s1", B("Quarters", "চতুৰ্থাংশ"), [B("A square folded twice has four layers, so one punch makes four holes.", "দুবাৰ ভাঁজত চাৰি স্তৰ, এটা ফুটাত চাৰিটা।")], "flow", [same("1"), same("2"), same("4")]),
        diagram(f"{p}.u4.s2", B("Keep the distance", "দূৰত্ব ৰাখা"), [B("A hole near a fold stays near it after opening.", "ভাঁজৰ ওচৰৰ ফুটা খোলাৰ পিছতো ওচৰত।")], "flow", [B("Near the fold", "ভাঁজৰ ওচৰত"), B("Mirror it", "প্ৰতিবিম্ব"), B("Near on both sides", "দুয়োফালে ওচৰত")]),
        explore(f"{p}.u4.q1", CUTF, fold2_q, [(30, 30), (35, 25), (25, 35)]),
        tf(f"{p}.u4.q2", CUTF, B("A cut across a fold makes a shape on both sides.", "ভাঁজত কটিলে দুয়োফালে আকৃতি।"), True, B("It opens out.", "ই খোল খায়।")),
        match(f"{p}.u4.q3", CUTF, B("Match the cut to the opened shape", "কটাক খোলা আকৃতিৰ লগত মিলোৱা"), [[B("Half circle on the fold", "ভাঁজত অৰ্ধবৃত্ত"), B("Circle", "বৃত্ত")], [B("Half square on the fold", "ভাঁজত অৰ্ধবৰ্গ"), B("Square", "বৰ্গ")], [B("Half diamond on the fold", "ভাঁজত অৰ্ধ হীৰা"), B("Diamond", "হীৰা")]], B("Mirror the half.", "আধাৰ প্ৰতিবিম্ব।")),
        solve(f"{p}.u4.q4", CUTF, lambda h, f: {"q": B(f"{h} holes are punched through a sheet folded {f} times. How many after opening?", f"{f} বাৰ ভাঁজ কৰা কাগজত {h} টা ফুটা কৰা হ'ল। খুলিলে কিমান?"), "answer": str(h * 2 ** f), "why": B(f"{h} × 2^{f}.", f"{h} × 2^{f}।")}, [(2, 2), (3, 2), (2, 3)]),
        order(f"{p}.u4.q5", CUTF, B("Layers from one fold onward", "ভাঁজৰ পৰা স্তৰ"), [same(2), same(4), same(8), same(16)], B("Each fold doubles.", "প্ৰতিটো ভাঁজে দুগুণ।")),
    ])
    test = {"id": "test", "title": B("Mirror and folding test", "দাপোণ আৰু ভাঁজৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", MIRROR, mirror_q, [(1,), (2,)]),
        explore(f"{p}.t.q2", WATER, water_q, [(0,), (2,)]),
        explore(f"{p}.t.q3", FOLD, fold_q, [(28, 40), (32, 55)]),
        explore(f"{p}.t.q4", CUTF, fold2_q, [(28, 28), (34, 30)]),
        tf(f"{p}.t.q5", MIRROR, B("A side mirror swaps up and down.", "কাষৰ দাপোণে ওপৰ-তল সলায়।"), False, B("It swaps left and right.", "বাওঁ-সোঁ সলায়।"), ("r-m-rotate", ROTW)),
        tf(f"{p}.t.q6", FOLD, B("Three folds give eight layers.", "তিনিটা ভাঁজত আঠটা স্তৰ।"), True, B("2³ = 8.", "2³ = 8।")),
    ]}
    return {"id": "rs-18-mirror-fold", "no": 18, "slug": "mirror-fold", "title": B("Mirrors and folding", "দাপোণ আৰু ভাঁজ"), "reign": B("Reflections, folds, punched holes", "প্ৰতিফলন, ভাঁজ, ফুটা"), "units": [u1, u2, u3, u4], "test": test}


def lesson_cube():
    p = "rs19"
    u1 = unit("u1", B("Opposite faces", "বিপৰীত পৃষ্ঠ"), "star", [B("A cube has 6 faces and 3 opposite pairs.", "ঘনকৰ 6 পৃষ্ঠ, 3 বিপৰীত যোৰ।"), B("Opposite faces never touch.", "বিপৰীত পৃষ্ঠ লগ নালাগে।"), B("Two views sharing a face reveal a pair.", "একে পৃষ্ঠৰ দুটা দৃশ্যই যোৰ দেখুৱায়।"), B("On a standard die, opposites add to 7.", "সাধাৰণ পাশাত বিপৰীতৰ যোগফল 7।")], [
        diagram(f"{p}.u1.s1", B("Neighbours rule out", "কাষৰবোৰ বাদ"), [B("A face touches four others. The one left over is opposite.", "এটা পৃষ্ঠই চাৰিটাক চুৱে। বাকীটো বিপৰীত।")], "flow", [B("List neighbours", "কাষৰ তালিকা"), B("Four found", "চাৰিটা পোৱা"), B("Fifth is opposite", "পঞ্চমটো বিপৰীত")]),
        diagram(f"{p}.u1.s2", B("The seven rule", "সাতৰ নিয়ম"), [B("On a standard die: 1 and 6, 2 and 5, 3 and 4.", "সাধাৰণ পাশাত: 1, 6; 2, 5; 3, 4।")], "grid", [same("1 + 6"), same("2 + 5"), same("3 + 4")]),
        explore(f"{p}.u1.q1", DIE, opp_q, [(1,), (2,), (3,)]),
        solve(f"{p}.u1.q2", DIE, lambda a: {"q": B(f"On a standard die, what is opposite {a}?", f"সাধাৰণ পাশাত {a} ৰ বিপৰীত কি?"), "answer": str(7 - a), "why": B("Opposites add to 7.", "বিপৰীতৰ যোগফল 7।")}, [(2,), (3,), (5,)]),
        tf(f"{p}.u1.q3", DIE, B("Two faces that touch can be opposite.", "লগ লগা দুটা পৃষ্ঠ বিপৰীত হ'ব পাৰে।"), False, B("Opposite faces never touch.", "বিপৰীত পৃষ্ঠ লগ নালাগে।"), ("r-m-adjacent", ADJ)),
        match(f"{p}.u1.q4", DIE, B("Count on a cube", "ঘনকত গণা"), [[B("Faces", "পৃষ্ঠ"), same(6)], [B("Edges", "দাঁতি"), same(12)], [B("Corners", "চুক"), same(8)]], B("Worth knowing.", "জানিব লগীয়া।")),
        order(f"{p}.u1.q5", DIE, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Pick a face", "পৃষ্ঠ বাছা"), B("List touching faces", "লগ লগা পৃষ্ঠ"), B("Cross them out", "কাটা"), B("Read what remains", "বাকী পঢ়া")], B("Elimination.", "বাদ দিয়া।")),
    ])
    u2 = unit("u2", B("Nets of a cube", "ঘনকৰ জাল"), "star", [B("A net folds into a cube.", "জাল ভাঁজ হৈ ঘনক হয়।"), B("In a row, skip one to find opposites.", "শাৰীত এটা এৰি বিপৰীত।"), B("Top and bottom of a cross are opposite.", "ক্ৰছৰ ওপৰ-তল বিপৰীত।"), B("Six squares are needed.", "ছটা বৰ্গ লাগে।")], [
        lab(f"{p}.u2.s1", B("Skip one, find its opposite", "এটা এৰি বিপৰীত"), B("In a straight row, every second square lands opposite. Try it on this net.", "পোন শাৰীত প্ৰতি দ্বিতীয় বৰ্গ বিপৰীত। এই জালত চোৱা।"), {"kind": "dicenet", "net": NET, "mark": 2}, [
            task(B("Tap the face opposite 2.", "2 ৰ বিপৰীত পৃষ্ঠ টিপা।"), {"pick": 4}, B("2 and 4 have one square between them.", "2 আৰু 4 ৰ মাজত এটা বৰ্গ।")),
        ]),
        diagram(f"{p}.u2.s2", B("Top and bottom", "ওপৰ আৰু তল"), [B("The squares above and below the row also face each other.", "শাৰীৰ ওপৰ আৰু তলৰ বৰ্গও মুখামুখি।")], "flow", [B("Above", "ওপৰ"), B("Row", "শাৰী"), B("Below", "তল")]),
        explore(f"{p}.u2.q1", NETF, opp_q, [(4,), (5,), (6,)]),
        tf(f"{p}.u2.q2", NETF, B("In a straight row of a net, neighbouring squares are opposite.", "জালৰ শাৰীত কাষৰ বৰ্গ বিপৰীত।"), False, B("Skip one instead.", "এটা এৰা।"), ("r-m-adjacent", ADJ)),
        match(f"{p}.u2.q3", NETF, B("On the net above, match the opposites", "ওপৰৰ জালৰ বিপৰীত মিলোৱা"), [[same("1 opposite"), same(6)], [same("2 opposite"), same(4)], [same("3 opposite"), same(5)]], B("Skip one in the row.", "শাৰীত এটা এৰা।")),
        solve(f"{p}.u2.q4", NETF, lambda: {"q": B("How many squares does a cube net have?", "ঘনকৰ জালত কিমান বৰ্গ?"), "answer": "6", "why": B("One per face.", "প্ৰতিটো পৃষ্ঠৰ এটা।")}, [(), ()]),
        order(f"{p}.u2.q5", NETF, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find a row", "শাৰী উলিওৱা"), B("Skip one", "এটা এৰা"), B("Pair the rest", "বাকী যোৰ"), B("Check all three", "তিনিওটা চোৱা")], B("Three pairs.", "তিনি যোৰ।")),
    ])
    u3 = unit("u3", B("Count hidden shapes", "লুকাই থকা আকৃতি গণা"), "star", [B("Count by size, smallest first.", "আকাৰ অনুসৰি, সৰুৰ পৰা।"), B("A big shape may contain small ones.", "ডাঙৰ আকৃতিত সৰু থাকে।"), B("An n by n grid has 1² + ... + n² squares.", "n × n জালিত 1² + ... + n² বৰ্গ।"), B("Name corners to avoid doubles.", "চুকৰ নাম দিয়া।")], [
        diagram(f"{p}.u3.s1", B("Size by size", "আকাৰ অনুসৰি"), [B("A 2 by 2 grid has 4 small squares and 1 large one: 5 in all.", "2 × 2 জালিত 4 সৰু, 1 ডাঙৰ: মুঠ 5।")], "flow", [B("Small: 4", "সৰু: 4"), B("Large: 1", "ডাঙৰ: 1"), B("Total: 5", "মুঠ: 5")]),
        diagram(f"{p}.u3.s2", B("Triangles in a triangle", "ত্ৰিভুজৰ ভিতৰত ত্ৰিভুজ"), [B("A line from the top to the base makes 3 triangles: two parts and the whole.", "ওপৰৰ পৰা ভূমিলৈ ৰেখাই 3 টা ত্ৰিভুজ বনায়।")], "flow", [B("Left", "বাওঁ"), B("Right", "সোঁ"), B("Whole", "গোটেই")]),
        solve(f"{p}.u3.q1", COUNTS, lambda n: {"q": B(f"How many squares are in a {n} by {n} grid?", f"{n} × {n} জালিত কিমান বৰ্গ?"), "answer": str(grid_squares(n)), "why": B("Add the squares of 1 to n.", "1 ৰ পৰা n লৈ বৰ্গ যোগ।"), "traps": [{"ans": str(n * n), "tag": "r-m-adjacent", "why": B("That counts only the smallest squares.", "সেয়া কেৱল সৰু বৰ্গ।")}]}, [(2,), (3,), (4,)]),
        solve(f"{p}.u3.q2", COUNTS, lambda k: {"q": B(f"{k} lines from a triangle's top reach its base. How many triangles are there?", f"ত্ৰিভুজৰ শীৰ্ষৰ পৰা ভূমিলৈ {k} ডাল ৰেখা। কিমান ত্ৰিভুজ?"), "answer": str((k + 1) * (k + 2) // 2), "why": B(f"Count parts in a row: {(k + 1) * (k + 2) // 2}.", f"শাৰীৰ অংশ গণা: {(k + 1) * (k + 2) // 2}।")}, [(1,), (2,), (3,)]),
        tf(f"{p}.u3.q3", COUNTS, B("A 3 by 3 grid has 14 squares.", "3 × 3 জালিত 14 বৰ্গ।"), True, B("9 + 4 + 1.", "9 + 4 + 1।")),
        match(f"{p}.u3.q4", COUNTS, B("Match the grid to its squares", "জালিক বৰ্গৰ লগত মিলোৱা"), [[same("1 by 1"), same(1)], [same("2 by 2"), same(5)], [same("3 by 3"), same(14)]], B("Sum of squares.", "বৰ্গৰ যোগফল।")),
        order(f"{p}.u3.q5", COUNTS, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Smallest size", "সৰু আকাৰ"), B("Next size", "পিছৰ আকাৰ"), B("Largest", "ডাঙৰ"), B("Add", "যোগ")], B("Size by size.", "আকাৰ অনুসৰি।")),
    ])
    u4 = unit("u4", B("Count the cubes", "ঘনক গণা"), "star", [B("Count layer by layer.", "স্তৰে স্তৰে গণা।"), B("Hidden cubes hold up those above.", "লুকাই থকাবোৰে ওপৰৰবোৰ ধৰে।"), B("n by n by n has n³ cubes.", "n × n × n ত n³ ঘনক।"), B("Painted cubes depend on position.", "ৰং স্থানৰ ওপৰত নিৰ্ভৰ।")], [
        diagram(f"{p}.u4.s1", B("Layers, not faces", "পৃষ্ঠ নহয়, স্তৰ"), [B("Count each layer from the bottom. Remember cubes you cannot see.", "তলৰ পৰা স্তৰ গণা। নেদেখা ঘনকো গণা।")], "flow", [B("Bottom", "তল"), B("Middle", "মাজ"), B("Top", "ওপৰ")]),
        diagram(f"{p}.u4.s2", B("Painted cubes", "ৰং দিয়া ঘনক"), [B("In a painted 3 by 3 by 3: corners have 3 faces, edges 2, centres 1, and one has none.", "ৰং দিয়া 3 × 3 × 3 ত: চুকত 3, দাঁতিত 2, মাজত 1, এটাত নাই।")], "grid", [B("Corners: 8", "চুক: 8"), B("Edges: 12", "দাঁতি: 12"), B("Centres: 6", "মাজ: 6"), B("Inside: 1", "ভিতৰ: 1")]),
        solve(f"{p}.u4.q1", CUBES, lambda *l: {"q": B(f"Layers from the bottom hold {', '.join(map(str, l))} cubes. How many cubes are there?", f"তলৰ পৰা স্তৰত {', '.join(map(str, l))} ঘনক। মুঠ কিমান?"), "answer": str(sum(l)), "why": B("Add the layers.", "স্তৰ যোগ।")}, [(9, 4, 1), (16, 9, 4), (6, 3, 1)]),
        solve(f"{p}.u4.q2", CUBES, lambda n: {"q": B(f"A {n} by {n} by {n} cube is painted and cut. How many small cubes have exactly 2 painted faces?", f"{n} × {n} × {n} ঘনক ৰং দি কটা হ'ল। ঠিক 2 পৃষ্ঠ ৰং থকা সৰু ঘনক কিমান?"), "answer": str(12 * (n - 2)), "why": B("Edges: 12 × (n − 2).", "দাঁতি: 12 × (n − 2)।")}, [(3,), (4,), (5,)]),
        tf(f"{p}.u4.q3", CUBES, B("A 3 by 3 by 3 cube has 27 small cubes.", "3 × 3 × 3 ত 27 সৰু ঘনক।"), True, B("3³ = 27.", "3³ = 27।")),
        match(f"{p}.u4.q4", CUBES, B("Painted 3 by 3 by 3: match", "ৰং দিয়া 3 × 3 × 3: মিলোৱা"), [[B("3 faces painted", "3 পৃষ্ঠ"), same(8)], [B("2 faces painted", "2 পৃষ্ঠ"), same(12)], [B("1 face painted", "1 পৃষ্ঠ"), same(6)]], B("Corners, edges, centres.", "চুক, দাঁতি, মাজ।")),
        order(f"{p}.u4.q5", CUBES, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find the bottom", "তল"), B("Count that layer", "স্তৰ গণা"), B("Move up", "ওপৰলৈ"), B("Add the layers", "স্তৰ যোগ")], B("Bottom up.", "তলৰ পৰা ওপৰ।")),
    ])
    test = {"id": "test", "title": B("Cubes and counting test", "ঘনক আৰু গণনাৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", NETF, opp_q, [(1,), (3,)]),
        solve(f"{p}.t.q2", DIE, lambda a: {"q": B(f"On a standard die, what is opposite {a}?", f"সাধাৰণ পাশাত {a} ৰ বিপৰীত কি?"), "answer": str(7 - a), "why": B("Add to 7.", "7 হ'ব লাগে।")}, [(1,), (4,)]),
        solve(f"{p}.t.q3", COUNTS, lambda n: {"q": B(f"Squares in a {n} by {n} grid?", f"{n} × {n} জালিত বৰ্গ?"), "answer": str(grid_squares(n)), "why": B("Sum of squares.", "বৰ্গৰ যোগফল।")}, [(3,), (5,)]),
        solve(f"{p}.t.q4", CUBES, lambda n: {"q": B(f"How many small cubes in {n} by {n} by {n}?", f"{n} × {n} × {n} ত কিমান সৰু ঘনক?"), "answer": str(n ** 3), "why": B("n³.", "n³।")}, [(4,), (5,)]),
        tf(f"{p}.t.q5", DIE, B("Touching faces can never be opposite.", "লগ লগা পৃষ্ঠ বিপৰীত নহয়।"), True, B("Opposites never touch.", "বিপৰীত লগ নালাগে।")),
        tf(f"{p}.t.q6", CUBES, B("A painted 3 by 3 by 3 has one unpainted cube.", "ৰং দিয়া 3 × 3 × 3 ত এটা ৰং নোহোৱা।"), True, B("The very centre.", "ঠিক মাজৰটো।")),
    ]}
    return {"id": "rs-19-cube-count", "no": 19, "slug": "cube-count", "title": B("Cubes and counting", "ঘনক আৰু গণনা"), "reign": B("Dice, nets, counting figures", "পাশা, জাল, চিত্ৰ গণনা"), "units": [u1, u2, u3, u4], "test": test}


def grid_q(rows, target, why, start=0):
    return {"q": B("Find the rule across each row, then set the missing number.", "প্ৰতিটো শাৰীৰ নিয়ম উলিয়াই নিৰুদ্দিষ্ট সংখ্যা ঠিক কৰা।"), "widget": {"kind": "numgrid", "rows": rows, "start": start}, "target": target, "answerText": same(target), "why": why, "traps": []}


def row_sum(a, b, c, d):
    return grid_q([[a, b, a + b], [c, d, None]], c + d, B("The third is the sum of the first two.", "তৃতীয়টো প্ৰথম দুটাৰ যোগফল।"))


def row_mul(a, b, c, d):
    return grid_q([[a, b, a * b], [c, d, None]], c * d, B("The third is the product.", "তৃতীয়টো পূৰণফল।"))


def row_rule(a, b, c, d):
    return grid_q([[a, b, 2 * a + b], [c, d, None]], 2 * c + d, B("Double the first, then add the second.", "প্ৰথমটো দুগুণ কৰি দ্বিতীয়টো যোগ।"))


def col_rule(a, b, c, d):
    return grid_q([[a, c], [b, d], [a + b, None]], c + d, B("Each column adds down.", "প্ৰতিটো স্তম্ভ তললৈ যোগ।"))


def lesson_numfig():
    p = "rs20"
    u1 = unit("u1", B("Read across", "শাৰীত পঢ়া"), "star", [B("Try + and × first.", "+ আৰু × আগতে।"), B("The rule must fit every row.", "নিয়ম সকলো শাৰীত মিলিব লাগে।"), B("Then use it on the gap.", "তাৰ পিছত খালী ঠাইত।"), B("Mixed rules double, then add.", "মিশ্ৰ নিয়ম দুগুণ কৰি যোগ।")], [
        lab(f"{p}.u1.s1", B("Test a full row first", "সম্পূৰ্ণ শাৰী আগতে"), B("A complete row is a free example. Find the rule there, then use it on the gap.", "সম্পূৰ্ণ শাৰী বিনামূলীয়া উদাহৰণ। তাত নিয়ম উলিয়াই খালী ঠাইত দিয়া।"), {"kind": "numgrid", "rows": [[3, 4, 7], [5, 2, None]], "start": 0}, [
            task(B("Set the missing number to 7.", "নিৰুদ্দিষ্ট সংখ্যা 7 কৰা।"), {"val": 7}, B("3 + 4 = 7 and 5 + 2 = 7.", "3 + 4 = 7, 5 + 2 = 7।")),
        ]),
        diagram(f"{p}.u1.s2", B("Order of guesses", "অনুমানৰ ক্ৰম"), [B("Try adding, then multiplying, then mixing.", "যোগ, পূৰণ, তাৰ পিছত মিশ্ৰ।")], "flow", [same("a + b"), same("a × b"), same("2a + b")]),
        explore(f"{p}.u1.q1", ROWF, row_sum, [(3, 5, 6, 7), (8, 4, 9, 6), (2, 7, 5, 8)]),
        explore(f"{p}.u1.q2", ROWF, row_mul, [(3, 4, 5, 6), (2, 9, 4, 7), (6, 3, 8, 2)]),
        explore(f"{p}.u1.q3", ROWF, row_rule, [(3, 2, 5, 1), (4, 1, 6, 3), (2, 5, 7, 2)]),
        tf(f"{p}.u1.q4", ROWF, B("A rule that fits one row is enough.", "এটা শাৰীত মিলিলেই হ'ল।"), False, B("It must fit every row.", "সকলো শাৰীত লাগিব।"), ("r-m-onerow", ONER)),
        order(f"{p}.u1.q6", ROWF, B("Rules to try in order", "নিয়ম ক্ৰমে চোৱা"), [same("a + b"), same("a × b"), same("2a + b"), same("a² + b")], B("Simple rules first.", "সহজ নিয়ম আগতে।")),
        match(f"{p}.u1.q5", ROWF, B("Match the row to its rule", "শাৰীক নিয়মৰ লগত মিলোৱা"), [[same("2, 3, 5"), same("a + b")], [same("2, 3, 6"), same("a × b")], [same("2, 3, 7"), same("2a + b")]], B("Test each.", "প্ৰতিটো চোৱা।")),
    ])
    u2 = unit("u2", B("Read down", "স্তম্ভত পঢ়া"), "star", [B("If rows fail, try columns.", "শাৰীয়ে নহ'লে স্তম্ভ।"), B("A rule may go down.", "নিয়ম তললৈ হ'ব পাৰে।"), B("Compare whole columns.", "গোটেই স্তম্ভ তুলনা।"), B("Check the other column.", "আনটো স্তম্ভ চোৱা।")], [
        diagram(f"{p}.u2.s1", B("Rows fail? Turn the grid", "শাৰী বিফল? জালি ঘূৰোৱা"), [B("Many grids run top to bottom. Test a full column.", "বহু জালি ওপৰৰ পৰা তললৈ। সম্পূৰ্ণ স্তম্ভ চোৱা।")], "flow", [B("Row test", "শাৰী পৰীক্ষা"), B("Column test", "স্তম্ভ পৰীক্ষা"), B("Apply", "প্ৰয়োগ")]),
        diagram(f"{p}.u2.s2", B("Both directions", "দুয়োফালে"), [B("Some grids work both ways. Any rule that fits all is fine.", "কিছুমান জালি দুয়োফালে। সকলোতে মিলিলে হ'ল।")], "flow", [B("Across", "শাৰী"), B("Down", "স্তম্ভ"), B("Either", "যিকোনো")]),
        explore(f"{p}.u2.q1", COLF, col_rule, [(3, 4, 5, 6), (7, 2, 4, 8), (6, 5, 3, 9)]),
        explore(f"{p}.u2.q2", COLF, row_sum, [(9, 6, 4, 8), (1, 8, 7, 7)]),
        tf(f"{p}.u2.q3", COLF, B("If rows give no rule, test the columns.", "শাৰীত নিয়ম নহ'লে স্তম্ভ চোৱা।"), True, B("Grids can run either way.", "জালি যিকোনো ফালে।")),
        match(f"{p}.u2.q4", COLF, B("Match the column to the rule", "স্তম্ভক নিয়মৰ লগত মিলোৱা"), [[same("2, 3, 5"), B("Add", "যোগ")], [same("2, 3, 6"), B("Multiply", "পূৰণ")], [same("5, 3, 2"), B("Subtract", "বিয়োগ")]], B("Read down.", "তললৈ পঢ়া।")),
        order(f"{p}.u2.q5", COLF, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Test rows", "শাৰী"), B("Test columns", "স্তম্ভ"), B("Confirm on another", "আনটোত নিশ্চিত"), B("Fill the gap", "খালী পূৰণ")], B("Confirm first.", "নিশ্চিত আগতে।")),
    ])
    u3 = unit("u3", B("Around a centre", "কেন্দ্ৰৰ চাৰিওফালে"), "star", [B("Outer numbers often build the centre.", "বাহিৰৰ সংখ্যাই কেন্দ্ৰ বনায়।"), B("Try the sum of opposite pairs.", "বিপৰীত যোৰৰ যোগফল চোৱা।"), B("Try sum or product of all.", "সকলোৰ যোগফল বা পূৰণফল।"), B("Test on a complete figure.", "সম্পূৰ্ণ চিত্ৰত চোৱা।")], [
        diagram(f"{p}.u3.s1", B("Centre from corners", "চুকৰ পৰা কেন্দ্ৰ"), [B("If the corners add to the centre in one figure, expect it in the next.", "এটা চিত্ৰত চুকৰ যোগফল কেন্দ্ৰ হ'লে পিছৰটোতো।")], "flow", [same("2 + 3 + 4 + 1"), same("= 10"), B("Centre 10", "কেন্দ্ৰ 10")]),
        diagram(f"{p}.u3.s2", B("Pairs across", "সিপাৰৰ যোৰ"), [B("Sometimes opposite pairs multiply and add to the centre.", "কেতিয়াবা বিপৰীত যোৰ পূৰণ কৰি যোগ কৰিলে কেন্দ্ৰ।")], "flow", [same("2 × 3"), same("4 × 1"), same("6 + 4 = 10")]),
        solve(f"{p}.u3.q1", SUMF, lambda a, b, c, d: {"q": B(f"Corners add to the centre. The corners are {a}, {b}, {c} and {d}. What is the centre?", f"চুকৰ যোগফল কেন্দ্ৰ। চুক {a}, {b}, {c}, {d}। কেন্দ্ৰ কিমান?"), "answer": str(a + b + c + d), "why": B("Add all four.", "চাৰিওটা যোগ।")}, [(2, 3, 4, 1), (5, 6, 2, 7), (8, 1, 9, 3)]),
        solve(f"{p}.u3.q2", SUMF, lambda a, b, c, d: {"q": B(f"Centre = {a} × {b} + {c} × {d}. What is the centre?", f"কেন্দ্ৰ = {a} × {b} + {c} × {d}। কেন্দ্ৰ কিমান?"), "answer": str(a * b + c * d), "why": B("Multiply pairs, then add.", "যোৰ পূৰণ কৰি যোগ।")}, [(2, 3, 4, 1), (5, 2, 3, 3), (6, 2, 4, 2)]),
        tf(f"{p}.u3.q3", SUMF, B("Test a rule on a complete figure first.", "সম্পূৰ্ণ চিত্ৰত নিয়ম আগতে।"), True, B("It is a free example.", "ই বিনামূলীয়া উদাহৰণ।")),
        match(f"{p}.u3.q4", SUMF, B("Corners 1, 2, 3, 4: match", "চুক 1, 2, 3, 4: মিলোৱা"), [[B("Sum", "যোগফল"), same(10)], [B("Product", "পূৰণফল"), same(24)], [B("Sum of squares", "বৰ্গৰ যোগফল"), same(30)]], B("Test each.", "প্ৰতিটো চোৱা।")),
        order(f"{p}.u3.q5", SUMF, B("Rules to try in order", "নিয়ম ক্ৰমে চোৱা"), [B("Sum of all", "সকলোৰ যোগফল"), B("Product of pairs", "যোৰৰ পূৰণফল"), B("Difference of pairs", "যোৰৰ পাৰ্থক্য"), B("Squares", "বৰ্গ")], B("Simple first.", "সহজ আগতে।")),
    ])
    u4 = unit("u4", B("Magic squares", "যাদুকৰী বৰ্গ"), "star", [B("Every row, column and diagonal has one sum.", "সকলো শাৰী, স্তম্ভ, কৰ্ণৰ যোগফল একে।"), B("1 to 9 gives a sum of 15.", "1 ৰ পৰা 9 ত 15।"), B("The centre is the middle number.", "কেন্দ্ৰত মাজৰ সংখ্যা।"), B("Find the sum from a full line.", "সম্পূৰ্ণ শাৰীৰ পৰা যোগফল।")], [
        lab(f"{p}.u4.s1", B("One sum everywhere", "সকলোতে একে যোগফল"), B("In a magic square every line adds the same. Use a full line to fill the gap.", "যাদুকৰী বৰ্গত সকলো শাৰীৰ যোগফল একে। সম্পূৰ্ণ শাৰীৰে খালী পূৰণ কৰা।"), {"kind": "numgrid", "rows": [[2, 7, 6], [9, 5, 1], [4, 3, None]], "start": 0}, [
            task(B("Set the gap to 8.", "খালী ঠাই 8 কৰা।"), {"val": 8}, B("2 + 7 + 6 = 15, so 4 + 3 + 8 = 15.", "2 + 7 + 6 = 15, গতিকে 4 + 3 + 8 = 15।")),
        ]),
        diagram(f"{p}.u4.s2", B("The centre rule", "কেন্দ্ৰৰ নিয়ম"), [B("With 1 to 9, the sum is 15 and the centre is 5.", "1 ৰ পৰা 9 ত যোগফল 15, কেন্দ্ৰ 5।")], "flow", [B("Total 45", "মুঠ 45"), B("÷ 3 = 15", "÷ 3 = 15"), B("Centre 5", "কেন্দ্ৰ 5")]),
        explore(f"{p}.u4.q1", MAGIC, lambda k: grid_q([[8 + k, 1 + k, 6 + k], [3 + k, 5 + k, 7 + k], [4 + k, 9 + k, None]], 2 + k, B("Use a full row for the sum.", "সম্পূৰ্ণ শাৰীৰ পৰা যোগফল।")), [(0,), (1,), (2,)]),
        solve(f"{p}.u4.q2", MAGIC, lambda a, b, s_: {"q": B(f"A line of a magic square has {a} and {b}, and the sum is {s_}. Find the third.", f"যাদুকৰী বৰ্গৰ শাৰীত {a}, {b}, যোগফল {s_}। তৃতীয়টো?"), "answer": str(s_ - a - b), "why": B(f"{s_} − {a} − {b}.", f"{s_} − {a} − {b}।")}, [(4, 9, 15), (10, 6, 24), (7, 11, 30)]),
        tf(f"{p}.u4.q3", MAGIC, B("A 1 to 9 magic square has 5 at its centre.", "1 ৰ পৰা 9 ৰ বৰ্গৰ কেন্দ্ৰত 5।"), True, B("It is the middle number.", "ই মাজৰ সংখ্যা।")),
        match(f"{p}.u4.q4", MAGIC, B("For 1 to 9, match", "1 ৰ পৰা 9 ৰ বাবে মিলোৱা"), [[B("Sum of all", "সকলোৰ যোগফল"), same(45)], [B("Each line", "প্ৰতিটো শাৰী"), same(15)], [B("Centre", "কেন্দ্ৰ"), same(5)]], B("45 ÷ 3 = 15.", "45 ÷ 3 = 15।")),
        order(f"{p}.u4.q5", MAGIC, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find a full line", "সম্পূৰ্ণ শাৰী"), B("Get the sum", "যোগফল"), B("Find a line with one gap", "এটা খালী শাৰী"), B("Subtract", "বিয়োগ")], B("Full line first.", "সম্পূৰ্ণ শাৰী আগতে।")),
    ])
    test = {"id": "test", "title": B("Numbers in figures test", "চিত্ৰত সংখ্যাৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", ROWF, row_sum, [(4, 9, 7, 5), (6, 8, 3, 9)]),
        explore(f"{p}.t.q2", ROWF, row_mul, [(4, 5, 6, 3), (7, 2, 3, 8)]),
        explore(f"{p}.t.q3", COLF, col_rule, [(2, 9, 6, 4), (8, 3, 5, 7)]),
        solve(f"{p}.t.q4", SUMF, lambda a, b, c, d: {"q": B(f"Corners add to the centre: {a}, {b}, {c}, {d}. Centre?", f"চুকৰ যোগফল কেন্দ্ৰ: {a}, {b}, {c}, {d}। কেন্দ্ৰ?"), "answer": str(a + b + c + d), "why": B("Add them.", "যোগ কৰা।")}, [(3, 7, 2, 6), (9, 4, 1, 5)]),
        tf(f"{p}.t.q5", MAGIC, B("All lines of a magic square share one sum.", "যাদুকৰী বৰ্গৰ সকলো শাৰীৰ যোগফল একে।"), True, B("That is its rule.", "সেয়াই নিয়ম।")),
        tf(f"{p}.t.q6", ROWF, B("A rule must fit every complete row.", "নিয়ম সকলো সম্পূৰ্ণ শাৰীত মিলিব লাগে।"), True, B("Check them all.", "সকলো চোৱা।")),
    ]}
    return {"id": "rs-20-number-figures", "no": 20, "slug": "number-figures", "title": B("Numbers in figures", "চিত্ৰত সংখ্যা"), "reign": B("Rows, columns, magic squares", "শাৰী, স্তম্ভ, যাদুকৰী বৰ্গ"), "units": [u1, u2, u3, u4], "test": test}


def mod(fn):
    return type("L", (), {"lesson": staticmethod(fn)})


LESSONS = [mod(lesson_patterns), mod(lesson_mirror), mod(lesson_cube), mod(lesson_numfig)]
