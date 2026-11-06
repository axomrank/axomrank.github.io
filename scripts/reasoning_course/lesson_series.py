"""Lessons 2 and 3: Number series and letter series."""
from math_kit import B, explore, match, mcq, order, part, solve, stepwise, tf, unit
from math_lessons_c import diagram, lab
from math_labs import task
from reason_kit import AZ, same, signed

ADD = "r-sadd"; TWO = "r-stwo"; MULT = "r-smult"; MIX = "r-smix"; WRONG = "r-swrong"; SPEC = "r-sspecial"
LGAP = "r-lgap"; LMIX = "r-lmix"; LGROUP = "r-lgroup"; LFILL = "r-lfill"; LNUM = "r-lnum"; LODD = "r-lodd"
SKILLS = {ADD: ("number-series", B("Add-a-gap series", "ব্যৱধান যোগৰ শৃংখল"), []), TWO: ("number-series", B("Gaps of gaps", "ব্যৱধানৰ ব্যৱধান"), [ADD]), MULT: ("number-series", B("Multiplying series", "গুণনৰ শৃংখল"), []),
          MIX: ("number-series", B("Two series woven together", "দুটা শৃংখলৰ বুনন"), [ADD]), WRONG: ("number-series", B("Find the wrong term", "ভুল পদ বিচৰা"), [ADD]), SPEC: ("number-series", B("Squares, cubes and primes", "বৰ্গ, ঘন আৰু মৌলিক"), []),
          LGAP: ("letter-series", B("Letter gaps", "আখৰৰ ব্যৱধান"), []), LMIX: ("letter-series", B("Woven letter series", "বোৱা আখৰ শৃংখল"), [LGAP]), LGROUP: ("letter-series", B("Letter groups", "আখৰৰ গোট"), [LGAP]),
          LFILL: ("letter-series", B("Fill the blanks", "খালী ঠাই পূৰণ"), []), LNUM: ("letter-series", B("Letters with numbers", "আখৰ আৰু সংখ্যা"), [LGAP]), LODD: ("letter-series", B("The group that breaks the rule", "নিয়ম ভঙা গোট"), [LGROUP])}
TAGS = {"r-m-firstgap": (TWO, B("Stopping at the first gaps", "প্ৰথম ব্যৱধানতে ৰোৱা")), "r-m-addmult": (MULT, B("Adding when the rule multiplies", "গুণনৰ ঠাইত যোগ")), "r-m-oneline": (MIX, B("Reading two series as one", "দুটা শৃংখলক এটা পঢ়া")), "r-m-lettergap": (LGAP, B("Miscounting letter gaps", "আখৰৰ ব্যৱধান ভুল গণা"))}
GAP2 = B("The gaps themselves grow. Look at the gaps of the gaps.", "ব্যৱধান নিজেই বাঢ়ে। ব্যৱধানৰ ব্যৱধান চোৱা।")
TIMES = B("The terms multiply, so the gaps grow fast. Divide neighbours to check.", "পদবোৰ পূৰণ হয়, সেয়ে ব্যৱধান সোনকালে বাঢ়ে। কাষৰ পদ হৰণ কৰি চোৱা।")
WOVEN = B("Take every second term. Two series take turns here.", "প্ৰতি দ্বিতীয় পদ লোৱা। ইয়াত দুটা শৃংখলে পাল পাতিছে।")
LGAPW = B("Count the letters skipped between, then add one.", "মাজত এৰা আখৰ গণি এক যোগ কৰা।")


def letters(sid, skill, fn, params, **extra):
    return solve(sid, skill, fn, params, input="letters", **extra)


def seq(q, terms, answer, why, skill_traps=None):
    return {"q": q, "answer": str(answer), "why": why, "traps": skill_traps or []}


def show(terms):
    return ", ".join(str(t) for t in terms)


def add_gap(a, d, n=5):
    t = [a + d * i for i in range(n)]
    return {"q": B(f"Open the gaps of {show(t)}, then set the next term.", f"{show(t)} ৰ ব্যৱধান খুলি পিছৰ পদ ঠিক কৰা।"), "widget": {"kind": "gaps", "terms": t}, "target": t[-1] + d, "answerText": same(t[-1] + d), "why": B(f"Every gap is {signed(d)}.", f"প্ৰতিটো ব্যৱধান {signed(d)}।")}


def next_add(a, d):
    t = [a + d * i for i in range(5)]
    return seq(B(f"What comes next: {show(t)}, ?", f"পিছত কি: {show(t)}, ?"), t, t[-1] + d, B(f"Each term changes by {signed(d)}.", f"প্ৰতিটো পদ {signed(d)} সলনি হয়।"))


def rising(a, d, s):
    t = [a]
    for i in range(4):
        t.append(t[-1] + d + s * i)
    n = t[-1] + d + s * 4
    return {"q": B(f"Find the next term: {show(t)}.", f"পিছৰ পদ: {show(t)}।"), "widget": {"kind": "gaps", "terms": t}, "target": n, "answerText": same(n), "traps": [{"val": t[-1] + (t[-1] - t[-2]), "tag": "r-m-firstgap", "why": GAP2}], "why": B(f"The gaps grow by {s} each time, so the next gap is {d + s * 4}.", f"ব্যৱধান প্ৰতিবাৰ {s} বাঢ়ে, পিছৰ ব্যৱধান {d + s * 4}।")}


def rising_solve(a, d, s):
    v = rising(a, d, s)
    return {"q": B(f"What comes next: {show(v['widget']['terms'])}, ?", f"পিছত কি: {show(v['widget']['terms'])}, ?"), "answer": str(v["target"]), "why": v["why"], "traps": [{"ans": str(v["traps"][0]["val"]), "tag": "r-m-firstgap", "why": GAP2}]}


def times(a, r):
    t = [a * r ** i for i in range(4)]
    return seq(B(f"What comes next: {show(t)}, ?", f"পিছত কি: {show(t)}, ?"), t, t[-1] * r, B(f"Each term is multiplied by {r}.", f"প্ৰতিটো পদ {r} ৰে পূৰণ হয়।"), [{"ans": str(t[-1] + t[-1] - t[-2]), "tag": "r-m-addmult", "why": TIMES}])


def timesplus(a, r, c):
    t = [a]
    for _ in range(3):
        t.append(t[-1] * r + c)
    return seq(B(f"Each term is the last times {r}, plus {c}. What comes next: {show(t)}, ?", f"প্ৰতিটো পদ আগৰটোৰ {r} গুণ, লগত {c}। পিছত কি: {show(t)}, ?"), t, t[-1] * r + c, B(f"{t[-1]} × {r} + {c} = {t[-1] * r + c}.", f"{t[-1]} × {r} + {c} = {t[-1] * r + c}।"))


def weave(a, d, b, e):
    t = []
    for i in range(3):
        t += [a + d * i, b + e * i]
    return seq(B(f"Two series take turns. What comes next: {show(t)}, ?", f"দুটা শৃংখলে পাল পাতিছে। পিছত কি: {show(t)}, ?"), t, a + d * 3, B(f"Odd places run {a}, {a + d}, {a + 2 * d}, so the next is {a + 3 * d}.", f"বিজোৰ স্থানত {a}, {a + d}, {a + 2 * d}, গতিকে পিছৰটো {a + 3 * d}।"), [{"ans": str(2 * t[-1] - t[-2]), "tag": "r-m-oneline", "why": WOVEN}])


def weave_steps(a, d, b, e):
    s = "rs2.u4.q2"
    t = []
    for i in range(3):
        t += [a + d * i, b + e * i]
    return {"q": B(f"Split {show(t)}, ?", f"{show(t)}, ? ভাগ কৰা"), "parts": [
        part(B("1st, 3rd and 5th terms?", "১ম, ৩য়, ৫ম পদ?"), same(show(t[0::2])), [same(show(t[1::2])), same(show(t[:3]))], WOVEN, tag="r-m-oneline", sid=s),
        part(B("Their gap?", "সিহঁতৰ ব্যৱধান?"), same(signed(d)), [same(signed(e)), same(signed(d + 1))], B("Compare neighbours in that list.", "সেই তালিকাৰ কাষৰ পদ তুলনা কৰা।"), sid=s),
        part(B("The next term?", "পিছৰ পদ?"), same(a + 3 * d), [same(b + 3 * e), same(t[-1] + d)], B("It continues the odd places.", "ই বিজোৰ স্থান আগবঢ়ায়।"), sid=s),
    ], "why": B(f"The answer is {a + 3 * d}.", f"উত্তৰ {a + 3 * d}।")}


def spot_wrong(a, d, i, bad):
    t = [a + d * k for k in range(6)]
    good = t[i]
    t[i] = bad
    return {"q": B(f"One term breaks the pattern: {show(t)}. Which should replace it?", f"এটা পদে আৰ্হি ভাঙিছে: {show(t)}। শুদ্ধ পদটো কি হ'ব?"), "answer": str(good), "why": B(f"The gap is {signed(d)}, so {bad} should be {good}.", f"ব্যৱধান {signed(d)}, গতিকে {bad} ৰ ঠাইত {good}।"), "traps": [{"ans": str(bad), "tag": "r-m-firstgap", "why": B("That is the wrong term itself.", "সেয়াই ভুল পদটো।")}]}


def squares(start, power):
    t = [(start + i) ** power for i in range(4)]
    n = (start + 4) ** power
    return seq(B(f"What comes next: {show(t)}, ?", f"পিছত কি: {show(t)}, ?"), t, n, B(f"These are {'squares' if power == 2 else 'cubes'}: {start + 4}{'²' if power == 2 else '³'} = {n}.", f"এইবোৰ {'বৰ্গ' if power == 2 else 'ঘন'}: {start + 4}{'²' if power == 2 else '³'} = {n}।"))


def lesson_numbers():
    p = "rs2"
    u1 = unit("u1", B("Start with the gaps", "ব্যৱধানৰ পৰা আৰম্ভ"), "star", [B("Write the gap between neighbours.", "কাষৰ পদৰ ব্যৱধান লিখা।"), B("A steady gap means add that gap.", "একে ব্যৱধান মানে সেয়া যোগ।"), B("A gap can be negative.", "ব্যৱধান ঋণাত্মক হ'ব পাৰে।"), B("Check the rule on every term.", "প্ৰতিটো পদত নিয়ম চোৱা।")], [
        lab(f"{p}.u1.s1", B("A series hides in its gaps", "শৃংখল ব্যৱধানত লুকাই থাকে"), B("Do not stare at the numbers. Open the gaps and the rule appears.", "সংখ্যালৈ চাই নাথাকিবা। ব্যৱধান খুলিলেই নিয়ম ওলায়।"), {"kind": "gaps", "terms": [3, 7, 11, 15, 19]}, [
            task(B("Open the gaps.", "ব্যৱধান খোলা।"), {"opened": 1}, B("Every gap is +4.", "প্ৰতিটো ব্যৱধান +4।")),
            task(B("Set the next term to 23.", "পিছৰ পদ 23 কৰা।"), {"next": 23}, B("19 + 4 = 23. The gap did all the work.", "19 + 4 = 23। ব্যৱধানেই সকলো কৰিলে।")),
        ]),
        diagram(f"{p}.u1.s2", B("Three steps, every time", "সদায় তিনি খোজ"), [B("Most exam series fall at the first step, so always begin there.", "পৰীক্ষাৰ বেছিভাগ শৃংখল প্ৰথম খোজতে হয়, সেয়ে তাৰ পৰাই আৰম্ভ কৰা।")], "flow", [B("Write gaps", "ব্যৱধান লিখা"), B("Find the rule", "নিয়ম উলিওৱা"), B("Test it", "পৰীক্ষা কৰা")]),
        explore(f"{p}.u1.q1", ADD, add_gap, [(5, 3), (40, -4), (2, 7), (90, -9)]),
        solve(f"{p}.u1.q2", ADD, next_add, [(11, 6), (100, -8), (6, 13), (51, -6)]),
        tf(f"{p}.u1.q3", ADD, B("In 9, 14, 19, 24 the gap is +5.", "9, 14, 19, 24 ত ব্যৱধান +5।"), True, B("Each term adds 5.", "প্ৰতিটো পদত 5 যোগ।")),
        match(f"{p}.u1.q4", ADD, B("Match the series to its gap", "শৃংখলক ব্যৱধানৰ লগত মিলোৱা"), [[same("4, 7, 10"), same("+3")], [same("20, 15, 10"), same("−5")], [same("2, 10, 18"), same("+8")]], B("Subtract neighbours.", "কাষৰ পদ বিয়োগ কৰা।")),
        order(f"{p}.u1.q5", ADD, B("Smallest term first: 7, 12, 17, 22", "সৰু পদ আগতে: 7, 12, 17, 22"), [same(n) for n in (7, 12, 17, 22)], B("The gap is +5.", "ব্যৱধান +5।")),
    ])
    u2 = unit("u2", B("Gaps of the gaps", "ব্যৱধানৰ ব্যৱধান"), "star", [B("If gaps change, write the gaps of the gaps.", "ব্যৱধান সলনি হ'লে ব্যৱধানৰ ব্যৱধান লিখা।"), B("A steady second gap means the gaps grow evenly.", "একে দ্বিতীয় ব্যৱধান মানে সমানে বৃদ্ধি।"), B("Build the next gap first, then the next term.", "প্ৰথমে পিছৰ ব্যৱধান, তাৰ পিছত পদ।"), B("Do not stop at the first row.", "প্ৰথম শাৰীতে নৰবা।")], [
        lab(f"{p}.u2.s1", B("One row is not enough", "এটা শাৰী নহয়"), B("Here the gaps are not steady. Open a second row.", "ইয়াত ব্যৱধান একে নহয়। দ্বিতীয় শাৰী খোলা।"), {"kind": "gaps", "terms": [2, 3, 6, 11, 18]}, [
            task(B("Open both rows.", "দুয়োটা শাৰী খোলা।"), {"opened": 2}, B("The gaps run +1, +3, +5, +7, and each grows by 2.", "ব্যৱধান +1, +3, +5, +7, প্ৰতিটো 2 বাঢ়ে।")),
            task(B("Set the next term to 27.", "পিছৰ পদ 27 কৰা।"), {"next": 27}, B("The next gap is +9, so 18 + 9 = 27.", "পিছৰ ব্যৱধান +9, গতিকে 18 + 9 = 27।")),
        ]),
        diagram(f"{p}.u2.s2", B("Build upward from the bottom", "তলৰ পৰা ওপৰলৈ"), [B("Extend the bottom row, then use it to extend the row above.", "তলৰ শাৰী আগবঢ়াই ওপৰৰ শাৰী আগবঢ়োৱা।")], "flow", [B("Second gap", "দ্বিতীয় ব্যৱধান"), B("Next gap", "পিছৰ ব্যৱধান"), B("Next term", "পিছৰ পদ")]),
        explore(f"{p}.u2.q1", TWO, rising, [(1, 2, 2), (4, 1, 3), (10, 3, 1)]),
        solve(f"{p}.u2.q2", TWO, rising_solve, [(2, 2, 2), (5, 1, 2), (3, 4, 3)]),
        stepwise(f"{p}.u2.q3", TWO, lambda a, d, s_: _gap_steps(a, d, s_), [(1, 1, 1), (2, 3, 2), (7, 2, 2)]),
        tf(f"{p}.u2.q4", TWO, B("In 1, 2, 4, 7, 11 the next gap is 5.", "1, 2, 4, 7, 11 ত পিছৰ ব্যৱধান 5।"), True, B("The gaps are 1, 2, 3, 4, so 5 follows.", "ব্যৱধান 1, 2, 3, 4, গতিকে 5।"), ("r-m-firstgap", GAP2)),
        match(f"{p}.u2.q5", TWO, B("Match the gaps to the next gap", "ব্যৱধানক পিছৰ ব্যৱধানৰ লগত মিলোৱা"), [[same("2, 4, 6"), same("8")], [same("1, 4, 7"), same("10")], [same("5, 10, 15"), same("20")]], B("Each row has its own steady change.", "প্ৰতিটো শাৰীৰ নিজা স্থিৰ সলনি।")),
    ])
    u3 = unit("u3", B("When numbers multiply", "সংখ্যা পূৰণ হ'লে"), "star", [B("Fast growth suggests multiplying.", "খৰ বৃদ্ধি মানে পূৰণ।"), B("Divide neighbours to test it.", "কাষৰ পদ হৰণ কৰি চোৱা।"), B("Some rules multiply, then add.", "কিছুমান নিয়মে পূৰণ কৰি যোগ কৰে।"), B("Halving is multiplying by one half.", "আধা কৰাও পূৰণ।")], [
        diagram(f"{p}.u3.s1", B("Quick growth is a clue", "খৰ বৃদ্ধি এটা ইংগিত"), [B("3, 6, 12, 24 doubles. Adding cannot keep up with that speed.", "3, 6, 12, 24 দুগুণ হয়। যোগে এই বেগ ধৰিব নোৱাৰে।")], "flow", [same("3"), same("6"), same("12"), same("24")]),
        diagram(f"{p}.u3.s2", B("Multiply, then add", "পূৰণ, তাৰ পিছত যোগ"), [B("If division gives no whole number, try twice a term plus a small number.", "হৰণত পূৰ্ণ সংখ্যা নহ'লে দুগুণ কৰি অলপ যোগ কৰি চোৱা।")], "flow", [B("3 × 2 + 1 = 7", "3 × 2 + 1 = 7"), B("7 × 2 + 1 = 15", "7 × 2 + 1 = 15"), B("15 × 2 + 1 = 31", "15 × 2 + 1 = 31")]),
        solve(f"{p}.u3.q1", MULT, times, [(2, 3), (5, 2), (1, 4), (3, 3)]),
        solve(f"{p}.u3.q2", MULT, timesplus, [(2, 2, 1), (1, 3, 1), (3, 2, 3)]),
        tf(f"{p}.u3.q3", MULT, B("In 2, 6, 18, 54 each term is multiplied by 3.", "2, 6, 18, 54 ত প্ৰতিটো পদ 3 ৰে পূৰণ।"), True, B("6 ÷ 2 = 3 and 18 ÷ 6 = 3.", "6 ÷ 2 = 3, 18 ÷ 6 = 3।"), ("r-m-addmult", TIMES)),
        match(f"{p}.u3.q4", MULT, B("Match the series to its multiplier", "শৃংখলক গুণকৰ লগত মিলোৱা"), [[same("1, 2, 4"), same("× 2")], [same("1, 5, 25"), same("× 5")], [same("80, 40, 20"), same("× ½")]], B("Divide neighbours.", "কাষৰ পদ হৰণ কৰা।")),
        order(f"{p}.u3.q5", MULT, B("Test a series in this order", "এই ক্ৰমত শৃংখল পৰীক্ষা কৰা"), [B("Write the gaps", "ব্যৱধান লিখা"), B("Try gaps of gaps", "ব্যৱধানৰ ব্যৱধান"), B("Divide neighbours", "হৰণ কৰা"), B("Try two series", "দুটা শৃংখল চোৱা")], B("Simple tests first.", "সহজ পৰীক্ষা আগতে।")),
    ])
    u4 = unit("u4", B("Two series at once", "একেলগে দুটা শৃংখল"), "star", [B("Rules that zigzag may be two series.", "জিগজাগ মানে দুটা শৃংখল হ'ব পাৰে।"), B("Split odd and even places.", "বিজোৰ আৰু যোৰ স্থান পৃথক কৰা।"), B("Find which series the blank belongs to.", "খালী ঠাই কোন শৃংখলৰ চোৱা।"), B("Each series has its own gap.", "প্ৰতিটো শৃংখলৰ নিজা ব্যৱধান।")], [
        diagram(f"{p}.u4.s1", B("Zigzag means split", "জিগজাগ মানে ভাগ"), [B("If the numbers rise and fall, take every second term.", "সংখ্যা উঠা-নমা কৰিলে প্ৰতি দ্বিতীয় পদ লোৱা।")], "grid", [B("Odd places: 2, 4, 6", "বিজোৰ: 2, 4, 6"), B("Even places: 50, 45, 40", "যোৰ: 50, 45, 40")]),
        diagram(f"{p}.u4.s2", B("Which one is next?", "পিছৰটো কোন?"), [B("Count the place of the blank. Its parity tells you which series continues.", "খালী ঠাইৰ স্থান গণা। বিজোৰ নে যোৰ চোৱা।")], "flow", [B("Place of blank", "খালী ঠাইৰ স্থান"), B("Odd or even", "বিজোৰ নে যোৰ"), B("Continue it", "আগবঢ়োৱা")]),
        solve(f"{p}.u4.q1", MIX, weave, [(2, 3, 40, -2), (5, 5, 30, -3), (1, 4, 20, 2)]),
        stepwise(f"{p}.u4.q2", MIX, weave_steps, [(3, 2, 30, -5), (10, 5, 4, 3), (7, 3, 50, -6)]),
        tf(f"{p}.u4.q3", MIX, B("In 2, 90, 4, 80, 6, 70 the next term is 8.", "2, 90, 4, 80, 6, 70 ত পিছৰ পদ 8।"), True, B("Odd places rise by 2.", "বিজোৰ স্থান 2 ৰে বাঢ়ে।"), ("r-m-oneline", WOVEN)),
        match(f"{p}.u4.q4", MIX, B("Split 1, 9, 2, 8, 3, 7", "1, 9, 2, 8, 3, 7 ভাগ কৰা"), [[B("Odd places", "বিজোৰ স্থান"), same("1, 2, 3")], [B("Even places", "যোৰ স্থান"), same("9, 8, 7")], [B("Next term", "পিছৰ পদ"), same("4")]], B("Each list has a steady gap.", "প্ৰতিটো তালিকাৰ ব্যৱধান একে।")),
        order(f"{p}.u4.q5", MIX, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("See the zigzag", "জিগজাগ চোৱা"), B("Split the places", "স্থান ভাগ কৰা"), B("Find each gap", "প্ৰতিটো ব্যৱধান"), B("Continue one", "এটা আগবঢ়োৱা")], B("Split before you calculate.", "গণনাৰ আগতে ভাগ কৰা।")),
    ])
    u5 = unit("u5", B("Find the wrong term", "ভুল পদ বিচৰা"), "star", [B("Most gaps agree; one or two do not.", "বেছিভাগ ব্যৱধান মিলে; এটা-দুটা নিমিলে।"), B("A wrong term spoils two gaps.", "এটা ভুল পদে দুটা ব্যৱধান নষ্ট কৰে।"), B("The term between the two bad gaps is wrong.", "দুটা বেয়া ব্যৱধানৰ মাজৰ পদ ভুল।"), B("Rebuild it from its neighbour.", "কাষৰ পদৰ পৰা আকৌ বনোৱা।")], [
        lab(f"{p}.u5.s1", B("One bad term, two bad gaps", "এটা বেয়া পদ, দুটা বেয়া ব্যৱধান"), B("A wrong term sits between two gaps, so both look odd. Open them.", "ভুল পদ দুটা ব্যৱধানৰ মাজত, সেয়ে দুয়োটা বেলেগ। খুলি চোৱা।"), {"kind": "gaps", "terms": [4, 8, 12, 17, 20, 24]}, [
            task(B("Open the gaps.", "ব্যৱধান খোলা।"), {"opened": 1}, B("+4, +4, +5, +3, +4: the +5 and +3 surround 17. It should be 16.", "+4, +4, +5, +3, +4: 17 ৰ দুয়োফালে +5 আৰু +3। ই 16 হ'ব লাগে।")),
        ]),
        diagram(f"{p}.u5.s2", B("The pair points at it", "যোৰে দেখুৱায়"), [B("Find two bad gaps side by side. The term they share is the wrong one.", "কাষে কাষে দুটা বেয়া ব্যৱধান বিচাৰা। উমৈহতীয়া পদটোৱেই ভুল।")], "flow", [B("Bad gap", "বেয়া ব্যৱধান"), B("Shared term", "উমৈহতীয়া পদ"), B("Bad gap", "বেয়া ব্যৱধান")]),
        solve(f"{p}.u5.q1", WRONG, spot_wrong, [(3, 4, 3, 16), (10, 5, 2, 21), (6, 3, 4, 19)]),
        tf(f"{p}.u5.q2", WRONG, B("One wrong term usually disturbs two gaps.", "এটা ভুল পদে সাধাৰণতে দুটা ব্যৱধান বিগাৰে।"), True, B("It sits between two neighbours.", "ই দুটা কাষৰ পদৰ মাজত।")),
        match(f"{p}.u5.q3", WRONG, B("Match the series to its wrong term", "শৃংখলক ভুল পদৰ লগত মিলোৱা"), [[same("2, 4, 7, 8, 10"), same("7")], [same("5, 10, 16, 20"), same("16")], [same("9, 12, 15, 19, 21"), same("19")]], B("Rebuild each from its gap.", "ব্যৱধানৰ পৰা আকৌ বনোৱা।")),
        order(f"{p}.u5.q4", WRONG, B("Find a wrong term in order", "ভুল পদ ক্ৰমে উলিওৱা"), [B("Write the gaps", "ব্যৱধান লিখা"), B("Find the common gap", "সাধাৰণ ব্যৱধান"), B("Spot the odd pair", "বেলেগ যোৰ"), B("Rebuild the term", "পদ বনোৱা")], B("Common gap first.", "সাধাৰণ ব্যৱধান আগতে।")),
        stepwise(f"{p}.u5.q5", WRONG, lambda a, d, bad: _wrong_steps(a, d, bad), [(5, 3, 15), (8, 4, 21), (2, 6, 15)]),
    ])
    u6 = unit("u6", B("Numbers you should recognise", "চিনিব লগা সংখ্যা"), "star", [B("1, 4, 9, 16 are squares.", "1, 4, 9, 16 বৰ্গ।"), B("1, 8, 27, 64 are cubes.", "1, 8, 27, 64 ঘন।"), B("2, 3, 5, 7, 11 are primes.", "2, 3, 5, 7, 11 মৌলিক।"), B("If gaps fail, test these sets.", "ব্যৱধানে নহ'লে এইবোৰ চোৱা।")], [
        diagram(f"{p}.u6.s1", B("Three families of numbers", "সংখ্যাৰ তিনিটা পৰিয়াল"), [B("Learn these on sight. They hide inside many exam series.", "এইবোৰ চিনি পোৱা হোৱা। পৰীক্ষাৰ বহু শৃংখলত লুকাই থাকে।")], "grid", [B("Squares: 25, 36, 49", "বৰ্গ: 25, 36, 49"), B("Cubes: 27, 64, 125", "ঘন: 27, 64, 125"), B("Primes: 13, 17, 19", "মৌলিক: 13, 17, 19")]),
        diagram(f"{p}.u6.s2", B("Near misses count too", "ওচৰৰ সংখ্যাও গণা"), [B("Sometimes each term is a square plus one. Compare it with the nearest square.", "কেতিয়াবা পদবোৰ বৰ্গ যোগ এক। ওচৰৰ বৰ্গৰ লগত তুলনা কৰা।")], "flow", [B("2 = 1 + 1", "2 = 1 + 1"), B("5 = 4 + 1", "5 = 4 + 1"), B("10 = 9 + 1", "10 = 9 + 1")]),
        solve(f"{p}.u6.q1", SPEC, squares, [(2, 2), (3, 2), (1, 3), (2, 3)]),
        solve(f"{p}.u6.q2", SPEC, lambda start: {"q": B(f"Each term is a square plus 1. What comes next: {show([(start + i) ** 2 + 1 for i in range(4)])}, ?", f"প্ৰতিটো পদ বৰ্গ যোগ 1। পিছত কি: {show([(start + i) ** 2 + 1 for i in range(4)])}, ?"), "answer": str((start + 4) ** 2 + 1), "why": B(f"{start + 4}² + 1 = {(start + 4) ** 2 + 1}.", f"{start + 4}² + 1 = {(start + 4) ** 2 + 1}।")}, [(1,), (2,), (3,)]),
        tf(f"{p}.u6.q3", SPEC, B("The next prime after 13 is 15.", "13 ৰ পিছৰ মৌলিক সংখ্যা 15।"), False, B("15 = 3 × 5. The next prime is 17.", "15 = 3 × 5। পিছৰ মৌলিক 17।")),
        match(f"{p}.u6.q4", SPEC, B("Match the number to its family", "সংখ্যাক পৰিয়ালৰ লগত মিলোৱা"), [[same("49"), B("Square", "বৰ্গ")], [same("125"), B("Cube", "ঘন")], [same("23"), B("Prime", "মৌলিক")]], B("Know them on sight.", "চিনি পোৱা হোৱা।")),
        order(f"{p}.u6.q5", SPEC, B("Put these squares in order", "এই বৰ্গবোৰ ক্ৰমে সজোৱা"), [same(n) for n in (16, 25, 36, 49)], B("4², 5², 6², 7².", "4², 5², 6², 7²।")),
    ])
    test = {"id": "test", "title": B("Number series test", "সংখ্যা শৃংখলৰ পৰীক্ষা"), "steps": [
        solve(f"{p}.t.q1", ADD, next_add, [(13, 7), (77, -7), (9, 11)]),
        solve(f"{p}.t.q2", TWO, rising_solve, [(1, 3, 2), (6, 2, 3)]),
        solve(f"{p}.t.q3", MULT, times, [(3, 2), (2, 5)]),
        solve(f"{p}.t.q4", MIX, weave, [(4, 4, 60, -5), (9, 2, 15, 5)]),
        solve(f"{p}.t.q5", WRONG, spot_wrong, [(7, 5, 3, 23), (20, 3, 1, 24)]),
        solve(f"{p}.t.q6", SPEC, squares, [(4, 2), (3, 3)]),
    ]}
    return {"id": "rs-02-number-series", "no": 2, "slug": "number-series", "title": B("Number series", "সংখ্যা শৃংখল"), "reign": B("Gaps, multiples, two series, wrong terms", "ব্যৱধান, গুণিতক, দুটা শৃংখল, ভুল পদ"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


def _gap_steps(a, d, s_):
    s = "rs2.u2.q3"
    t = [a]
    for i in range(4):
        t.append(t[-1] + d + s_ * i)
    g = [t[i + 1] - t[i] for i in range(4)]
    nxt = g[-1] + s_
    return {"q": B(f"Work through {show(t)}, ?", f"{show(t)}, ? সমাধান কৰা"), "parts": [
        part(B("The gaps?", "ব্যৱধান?"), same(show(g)), [same(show([x + 1 for x in g])), same(show(t[:4]))], B("Subtract neighbours.", "কাষৰ পদ বিয়োগ কৰা।"), sid=s),
        part(B("The next gap?", "পিছৰ ব্যৱধান?"), same(nxt), [same(g[-1]), same(nxt + 1)], GAP2, tag="r-m-firstgap", sid=s),
        part(B("The next term?", "পিছৰ পদ?"), same(t[-1] + nxt), [same(t[-1] + g[-1]), same(t[-1] + nxt + 1)], B("Add the next gap.", "পিছৰ ব্যৱধান যোগ কৰা।"), sid=s),
    ], "why": B(f"The answer is {t[-1] + nxt}.", f"উত্তৰ {t[-1] + nxt}।")}


def _wrong_steps(a, d, bad):
    s = "rs2.u5.q5"
    t = [a + d * k for k in range(5)]
    good = t[3]
    t[3] = bad
    return {"q": B(f"Find the wrong term in {show(t)}.", f"{show(t)} ৰ ভুল পদ উলিওৱা।"), "parts": [
        part(B("The common gap?", "সাধাৰণ ব্যৱধান?"), same(signed(d)), [same(signed(d + 1)), same(signed(d - 1))], B("Most gaps show it.", "বেছিভাগ ব্যৱধানত আছে।"), sid=s),
        part(B("The wrong term?", "ভুল পদ?"), same(bad), [same(t[2]), same(t[4])], B("It sits between the two bad gaps.", "ই দুটা বেয়া ব্যৱধানৰ মাজত।"), sid=s),
        part(B("It should be?", "ই কি হ'ব লাগে?"), same(good), [same(good + 1), same(good - 1)], B("Add the common gap to the term before.", "আগৰ পদত সাধাৰণ ব্যৱধান যোগ।"), sid=s),
    ], "why": B(f"{bad} should be {good}.", f"{bad} ৰ ঠাইত {good}।")}


# ---------------------------------------------------------------- letters
def pos(c):
    return AZ.index(c) + 1


def lseq(a, d, n=5):
    return "".join(AZ[(pos(a) - 1 + d * i) % 26] for i in range(n))


def l_gaps(a, d):
    t = [pos(a) + d * i for i in range(5)]
    n = t[-1] + d
    return {"q": B(f"Find the next letter: {', '.join(AZ[x - 1] for x in t)}.", f"পিছৰ আখৰ: {', '.join(AZ[x - 1] for x in t)}।"), "widget": {"kind": "gaps", "terms": t, "letters": True}, "target": n, "answerText": same(AZ[n - 1]), "traps": [{"val": n - 1, "tag": "r-m-lettergap", "why": LGAPW}], "why": B(f"The gap is {signed(d)}.", f"ব্যৱধান {signed(d)}।")}


def l_next(a, d):
    s = lseq(a, d)
    return {"q": B(f"What comes next: {', '.join(s)}, ?", f"পিছত কি: {', '.join(s)}, ?"), "answer": lseq(a, d, 6)[-1], "why": B(f"Each letter moves {signed(d)}.", f"প্ৰতিটো আখৰ {signed(d)} সৰে।"), "traps": [{"ans": lseq(a, d - 1 if d > 1 else d + 1, 6)[-1], "tag": "r-m-lettergap", "why": LGAPW}]}


def l_grow(a, s_):
    t = [pos(a)]
    for i in range(4):
        t.append(t[-1] + s_ + i)
    n = t[-1] + s_ + 4
    return {"q": B(f"The gaps grow by one. What comes next: {', '.join(AZ[x - 1] for x in t)}, ?", f"ব্যৱধান এক এক বাঢ়ে। পিছত কি: {', '.join(AZ[x - 1] for x in t)}, ?"), "answer": AZ[n - 1], "why": B(f"The next gap is {s_ + 4}.", f"পিছৰ ব্যৱধান {s_ + 4}।")}


def l_weave(a, d, b, e):
    x, y = lseq(a, d, 3), lseq(b, e, 3)
    t = [c for pair in zip(x, y) for c in pair]
    return {"q": B(f"Two series take turns. What comes next: {', '.join(t)}, ?", f"দুটা শৃংখলে পাল পাতিছে। পিছত কি: {', '.join(t)}, ?"), "answer": lseq(a, d, 4)[-1], "why": B(f"Odd places run {', '.join(x)}.", f"বিজোৰ স্থানত {', '.join(x)}।"), "traps": [{"ans": lseq(b, e, 4)[-1], "tag": "r-m-oneline", "why": WOVEN}]}


def l_group(a, gap, step):
    groups = ["".join(AZ[(pos(a) - 1 + i * step + j * gap) % 26] for j in range(3)) for i in range(4)]
    return {"q": B(f"Each group follows the last. What comes next: {', '.join(groups[:3])}, ?", f"প্ৰতিটো গোট আগৰটোৰ পিছত। পিছত কি: {', '.join(groups[:3])}, ?"), "answer": groups[3], "why": B(f"Each group's first letter moves {signed(step)}.", f"প্ৰতিটো গোটৰ প্ৰথম আখৰ {signed(step)} সৰে।")}


def lesson_letters():
    p = "rs3"
    u1 = unit("u1", B("Letters are numbers in disguise", "আখৰ মানে ছদ্মবেশী সংখ্যা"), "star", [B("Change letters to places.", "আখৰক স্থানলৈ সলনি কৰা।"), B("Find the gap as with numbers.", "সংখ্যাৰ দৰে ব্যৱধান উলিওৱা।"), B("Skipping two letters is a gap of 3.", "দুটা আখৰ এৰিলে ব্যৱধান 3।"), B("After Z the count returns to A.", "Z ৰ পিছত A লৈ উভতে।")], [
        lab(f"{p}.u1.s1", B("Same trick, new costume", "একে কৌশল, নতুন সাজ"), B("Letters hide numbers. A, D, G, J are really 1, 4, 7, 10.", "আখৰৰ আঁৰত সংখ্যা। A, D, G, J আচলতে 1, 4, 7, 10।"), {"kind": "gaps", "terms": [1, 4, 7, 10], "letters": True}, [
            task(B("Open the gaps.", "ব্যৱধান খোলা।"), {"opened": 1}, B("Every gap is +3.", "প্ৰতিটো ব্যৱধান +3।")),
            task(B("Move to the next letter, M.", "পিছৰ আখৰ M লৈ যোৱা।"), {"next": 13}, B("J + 3 = M.", "J + 3 = M।")),
        ]),
        diagram(f"{p}.u1.s2", B("Count the gap correctly", "ব্যৱধান শুদ্ধকৈ গণা"), [B("A to D skips B and C, but the gap is 3, not 2.", "A ৰ পৰা D ত B, C এৰে, কিন্তু ব্যৱধান 3, 2 নহয়।")], "flow", [B("Skipped: 2", "এৰা: 2"), B("Add one", "এক যোগ"), B("Gap: 3", "ব্যৱধান: 3")]),
        explore(f"{p}.u1.q1", LGAP, l_gaps, [("B", 3), ("C", 4), ("A", 5)]),
        solve(f"{p}.u1.q2", LGAP, l_next, [("D", 2), ("F", 3), ("Z", -2), ("Y", -4)], input="letters"),
        solve(f"{p}.u1.q3", LGAP, l_grow, [("A", 1), ("C", 2), ("B", 1)], input="letters"),
        tf(f"{p}.u1.q4", LGAP, B("From C to H the gap is 5.", "C ৰ পৰা H লৈ ব্যৱধান 5।"), True, B("3 to 8 is 5.", "3 ৰ পৰা 8 মানে 5।"), ("r-m-lettergap", LGAPW)),
        match(f"{p}.u1.q5", LGAP, B("Match the series to its gap", "শৃংখলক ব্যৱধানৰ লগত মিলোৱা"), [[same("B, D, F"), same("+2")], [same("A, E, I"), same("+4")], [same("Z, W, T"), same("−3")]], B("Convert to places.", "স্থানলৈ সলনি কৰা।")),
    ])
    u2 = unit("u2", B("Two letter series", "দুটা আখৰ শৃংখল"), "star", [B("Letters may take turns.", "আখৰে পাল ল'ব পাৰে।"), B("Split odd and even places.", "বিজোৰ-যোৰ স্থান পৃথক কৰা।"), B("One series may run backward.", "এটা শৃংখল ওলোটা হ'ব পাৰে।"), B("Find which series is next.", "পিছৰটো কোন শৃংখলৰ চোৱা।")], [
        diagram(f"{p}.u2.s1", B("One from each end", "দুই মূৰৰ পৰা এটাকৈ"), [B("A, Z, B, Y, C is two series: one forward from A and one backward from Z.", "A, Z, B, Y, C দুটা শৃংখল: A ৰ পৰা আগলৈ, Z ৰ পৰা পিছলৈ।")], "grid", [B("Odd: A, B, C", "বিজোৰ: A, B, C"), B("Even: Z, Y, X", "যোৰ: Z, Y, X")]),
        diagram(f"{p}.u2.s2", B("Blank's place decides", "খালী ঠাইৰ স্থানে ঠিক কৰে"), [B("Count to the blank. Odd place continues the first series.", "খালী ঠাইলৈ গণা। বিজোৰ স্থান প্ৰথম শৃংখল।")], "flow", [B("Place of blank", "খালী ঠাইৰ স্থান"), B("Pick the series", "শৃংখল বাছা"), B("Continue", "আগবঢ়োৱা")]),
        solve(f"{p}.u2.q1", LMIX, l_weave, [("A", 2, "Z", -2), ("C", 3, "X", -1), ("B", 1, "M", 2)], input="letters"),
        stepwise(f"{p}.u2.q2", LMIX, lambda a, d, b, e: {"q": B(f"Split {', '.join(c for pair in zip(lseq(a, d, 3), lseq(b, e, 3)) for c in pair)}, ?", f"{', '.join(c for pair in zip(lseq(a, d, 3), lseq(b, e, 3)) for c in pair)}, ? ভাগ কৰা"), "parts": [
            part(B("Odd places?", "বিজোৰ স্থান?"), same(", ".join(lseq(a, d, 3))), [same(", ".join(lseq(b, e, 3))), same(", ".join(lseq(a, d + 1, 3)))], WOVEN, tag="r-m-oneline", sid="rs3.u2.q2"),
            part(B("Their gap?", "সিহঁতৰ ব্যৱধান?"), same(signed(d)), [same(signed(e)), same(signed(d + 1))], LGAPW, sid="rs3.u2.q2"),
            part(B("Next letter?", "পিছৰ আখৰ?"), same(lseq(a, d, 4)[-1]), [same(lseq(b, e, 4)[-1]), same(lseq(a, d + 1, 4)[-1])], B("It continues the odd places.", "ই বিজোৰ স্থান আগবঢ়ায়।"), sid="rs3.u2.q2"),
        ], "why": B(f"The answer is {lseq(a, d, 4)[-1]}.", f"উত্তৰ {lseq(a, d, 4)[-1]}।")}, [("D", 2, "W", -2), ("E", 3, "T", -3), ("A", 4, "P", 1)]),
        tf(f"{p}.u2.q3", LMIX, B("In A, Z, B, Y, C the next letter is X.", "A, Z, B, Y, C ত পিছৰ আখৰ X।"), True, B("Even places run backward from Z.", "যোৰ স্থান Z ৰ পৰা পিছলৈ।"), ("r-m-oneline", WOVEN)),
        match(f"{p}.u2.q4", LMIX, B("Split C, W, E, U, G", "C, W, E, U, G ভাগ কৰা"), [[B("Odd places", "বিজোৰ স্থান"), same("C, E, G")], [B("Even places", "যোৰ স্থান"), same("W, U")], [B("Next letter", "পিছৰ আখৰ"), same("S")]], B("Each has its own gap.", "প্ৰতিটোৰ নিজা ব্যৱধান।")),
        order(f"{p}.u2.q5", LMIX, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Suspect two series", "দুটা শৃংখল সন্দেহ"), B("Split the places", "স্থান ভাগ"), B("Find the gaps", "ব্যৱধান"), B("Continue one", "এটা আগবঢ়োৱা")], B("Split, then calculate.", "ভাগ কৰি গণা।")),
    ])
    u3 = unit("u3", B("Groups of letters", "আখৰৰ গোট"), "star", [B("Read groups position by position.", "গোট স্থান অনুসৰি পঢ়া।"), B("Compare first letters, then second.", "প্ৰথম আখৰ, তাৰ পিছত দ্বিতীয় তুলনা।"), B("Each position has its own gap.", "প্ৰতিটো স্থানৰ নিজা ব্যৱধান।"), B("Build the answer letter by letter.", "আখৰে আখৰে উত্তৰ বনোৱা।")], [
        diagram(f"{p}.u3.s1", B("Read down, not across", "আঁতৰি নহয়, তললৈ পঢ়া"), [B("Stack the groups. Each column is a small series of its own.", "গোটবোৰ ওপৰা-ওপৰি ৰাখা। প্ৰতিটো স্তম্ভ এটা সৰু শৃংখল।")], "grid", [same("ACE"), same("BDF"), same("CEG"), B("Next: DFH", "পিছৰটো: DFH")]),
        diagram(f"{p}.u3.s2", B("Columns may differ", "স্তম্ভ বেলেগ হ'ব পাৰে"), [B("One column can rise while another falls. Check each one.", "এটা স্তম্ভ বাঢ়িব, আনটো কমিব পাৰে। প্ৰতিটো চোৱা।")], "flow", [B("Column 1", "স্তম্ভ ১"), B("Column 2", "স্তম্ভ ২"), B("Column 3", "স্তম্ভ ৩")]),
        solve(f"{p}.u3.q1", LGROUP, l_group, [("A", 2, 1), ("C", 1, 2), ("B", 3, 2)], input="letters"),
        solve(f"{p}.u3.q2", LGROUP, l_group, [("D", 2, 3), ("F", 1, 1), ("H", 2, -1)], input="letters"),
        tf(f"{p}.u3.q3", LGROUP, B("After ABC, BCD, CDE comes DEF.", "ABC, BCD, CDE ৰ পিছত DEF।"), True, B("Each column moves +1.", "প্ৰতিটো স্তম্ভ +1।")),
        match(f"{p}.u3.q4", LGROUP, B("Match the groups to the next group", "গোটক পিছৰ গোটৰ লগত মিলোৱা"), [[same("AB, CD, EF"), same("GH")], [same("ZY, XW, VU"), same("TS")], [same("AC, BD, CE"), same("DF")]], B("Read each column.", "প্ৰতিটো স্তম্ভ পঢ়া।")),
        order(f"{p}.u3.q5", LGROUP, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Stack the groups", "গোট ওপৰা-ওপৰি"), B("Read each column", "প্ৰতিটো স্তম্ভ পঢ়া"), B("Find each gap", "প্ৰতিটো ব্যৱধান"), B("Build the group", "গোট বনোৱা")], B("Columns first.", "স্তম্ভ আগতে।")),
    ])
    u4 = unit("u4", B("Fill the blanks", "খালী ঠাই পূৰণ"), "star", [B("Look for a repeating block.", "পুনৰাবৃত্ত খণ্ড বিচাৰা।"), B("Try block lengths of 2, 3 and 4.", "2, 3, 4 দীঘল খণ্ড চোৱা।"), B("Write the block under the blanks.", "খালী ঠাইৰ তলত খণ্ড লিখা।"), B("Check the whole line.", "গোটেই শাৰী পৰীক্ষা কৰা।")], [
        diagram(f"{p}.u4.s1", B("Find the repeating block", "পুনৰাবৃত্ত খণ্ড বিচাৰা"), [B("Blank series usually repeat a short block. Cut the line into equal pieces.", "খালী ঠাইৰ শৃংখলত সাধাৰণতে চুটি খণ্ড ঘূৰি আহে। সমান টুকুৰা কৰা।")], "flow", [same("ab_"), same("a_c"), same("_bc"), B("Block: abc", "খণ্ড: abc")]),
        diagram(f"{p}.u4.s2", B("Blanks in order", "খালী ঠাই ক্ৰমে"), [B("Write the missing letters in the order the blanks appear.", "খালী ঠাইৰ ক্ৰমতে আখৰ লিখা।")], "flow", [B("Find the block", "খণ্ড উলিওৱা"), B("Fill each blank", "খালী পূৰণ"), B("Read them in order", "ক্ৰমে পঢ়া")]),
        solve(f"{p}.u4.q1", LFILL, lambda blk, line: _blanks(blk, line), [("abc", "ab_a_c_bc"), ("mno", "m_om_o_no"), ("pq", "p_p_pq_q")], input="letters"),
        solve(f"{p}.u4.q2", LFILL, lambda blk, line: _blanks(blk, line), [("xyz", "_yzx_zxy_"), ("abcd", "a_cda_cd_bcd"), ("rs", "r_r_rs_s")], input="letters"),
        tf(f"{p}.u4.q3", LFILL, B("The blanks in ab_ab_ are c and c when the block is abc.", "খণ্ড abc হ'লে ab_ab_ ৰ খালী ঠাই c, c।"), True, B("Each block ends in c.", "প্ৰতিটো খণ্ড c ত শেষ।")),
        match(f"{p}.u4.q4", LFILL, B("Match the line to its block", "শাৰীক খণ্ডৰ লগত মিলোৱা"), [[same("ababab"), same("ab")], [same("abcabc"), same("abc")], [same("aabbaabb"), same("aabb")]], B("Cut into equal pieces.", "সমান টুকুৰা কৰা।")),
        order(f"{p}.u4.q5", LFILL, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Guess a block length", "খণ্ডৰ দীঘ"), B("Cut the line", "শাৰী কটা"), B("Fill each blank", "খালী পূৰণ"), B("Read in order", "ক্ৰমে পঢ়া")], B("Length first.", "দীঘ আগতে।")),
    ])
    u5 = unit("u5", B("Letters with numbers", "আখৰ আৰু সংখ্যা"), "star", [B("Split a mixed term into parts.", "মিশ্ৰ পদ ভাগ কৰা।"), B("Each part has its own rule.", "প্ৰতিটো ভাগৰ নিজা নিয়ম।"), B("The number may count something.", "সংখ্যাই কিবা গণিব পাৰে।"), B("Combine the parts at the end.", "শেষত ভাগবোৰ জোৰা।")], [
        diagram(f"{p}.u5.s1", B("Split the mixed term", "মিশ্ৰ পদ ভাগ কৰা"), [B("B2, D4, F6: letters run +2 and numbers run +2, on separate tracks.", "B2, D4, F6: আখৰ +2, সংখ্যা +2, পৃথক পথত।")], "grid", [B("Letters: B, D, F", "আখৰ: B, D, F"), B("Numbers: 2, 4, 6", "সংখ্যা: 2, 4, 6"), B("Next: H8", "পিছৰটো: H8")]),
        diagram(f"{p}.u5.s2", B("The number can be the gap", "সংখ্যাই ব্যৱধান হ'ব পাৰে"), [B("In A2C3F, each digit tells how far the next letter jumps.", "A2C3F ত প্ৰতিটো অংকই কয় পিছৰ আখৰ কিমান জঁপিয়ায়।")], "flow", [B("A + 2 = C", "A + 2 = C"), B("C + 3 = F", "C + 3 = F"), B("F + 4 = J", "F + 4 = J")]),
        solve(f"{p}.u5.q1", LNUM, lambda a, d, n, e: {"q": B(f"What comes next: {', '.join(lseq(a, d, 4)[i] + str(n + e * i) for i in range(4))}, ?", f"পিছত কি: {', '.join(lseq(a, d, 4)[i] + str(n + e * i) for i in range(4))}, ?"), "answer": f"{n + e * 4}", "why": B(f"Numbers move {signed(e)}; this asks for the number of the next term.", f"সংখ্যা {signed(e)} সৰে; ইয়াত পিছৰ পদৰ সংখ্যাটো সোধা হৈছে।")}, [("B", 2, 3, 2), ("A", 3, 5, 5), ("C", 1, 2, 3)]),
        solve(f"{p}.u5.q2", LNUM, lambda a, d, n, e: {"q": B(f"What letter comes next: {', '.join(lseq(a, d, 4)[i] + str(n + e * i) for i in range(4))}, ?", f"পিছৰ আখৰ কি: {', '.join(lseq(a, d, 4)[i] + str(n + e * i) for i in range(4))}, ?"), "answer": lseq(a, d, 5)[-1], "why": B(f"Letters move {signed(d)}.", f"আখৰ {signed(d)} সৰে।")}, [("B", 2, 3, 2), ("A", 3, 5, 5), ("C", 1, 2, 3)], input="letters"),
        tf(f"{p}.u5.q3", LNUM, B("In A1, C3, E5 the next term is G7.", "A1, C3, E5 ৰ পিছত G7।"), True, B("Both parts move +2.", "দুয়োটা ভাগ +2।")),
        match(f"{p}.u5.q4", LNUM, B("Match the series to the next term", "শৃংখলক পিছৰ পদৰ লগত মিলোৱা"), [[same("A1, B2, C3"), same("D4")], [same("Z1, Y2, X3"), same("W4")], [same("B2, D4, F6"), same("H8")]], B("Handle each track.", "প্ৰতিটো পথ চোৱা।")),
        order(f"{p}.u5.q5", LNUM, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Split each term", "পদ ভাগ"), B("Read the letters", "আখৰ পঢ়া"), B("Read the numbers", "সংখ্যা পঢ়া"), B("Join the next parts", "ভাগ জোৰা")], B("Separate tracks.", "পৃথক পথ।")),
    ])
    u6 = unit("u6", B("The odd group out", "বেলেগ গোট"), "star", [B("Find the rule in most groups.", "বেছিভাগ গোটৰ নিয়ম উলিওৱা।"), B("Compare gaps inside each group.", "প্ৰতিটো গোটৰ ভিতৰৰ ব্যৱধান তুলনা।"), B("Vowels are often a hidden rule.", "স্বৰবৰ্ণ প্ৰায়ে লুকাই থকা নিয়ম।"), B("One mismatch settles it.", "এটা অমিলেই যথেষ্ট।")], [
        diagram(f"{p}.u6.s1", B("Gaps inside the group", "গোটৰ ভিতৰৰ ব্যৱধান"), [B("Find the gaps inside each group. Three match; the fourth does not.", "প্ৰতিটো গোটৰ ভিতৰৰ ব্যৱধান উলিওৱা। তিনিটা মিলে; চতুৰ্থটো নিমিলে।")], "grid", [B("ACE: +2, +2", "ACE: +2, +2"), B("GIK: +2, +2", "GIK: +2, +2"), B("MOR: +2, +3", "MOR: +2, +3")]),
        diagram(f"{p}.u6.s2", B("Remember the vowels", "স্বৰবৰ্ণ মনত ৰাখা"), [B("A, E, I, O, U are spaced unevenly, which makes them easy to spot.", "A, E, I, O, U অসমানকৈ থাকে, সেয়ে চিনি পোৱা সহজ।")], "flow", [same("A"), same("E"), same("I"), same("O")]),
        _odd_group(f"{p}.u6.q1"),
        tf(f"{p}.u6.q2", LODD, B("Among ACE, GIK and MPQ, the odd group is MPQ.", "ACE, GIK, MPQ ৰ ভিতৰত বেলেগ MPQ।"), True, B("MPQ has gaps +3, +1.", "MPQ ৰ ব্যৱধান +3, +1।")),
        match(f"{p}.u6.q3", LODD, B("Match the group to its gaps", "গোটক ব্যৱধানৰ লগত মিলোৱা"), [[same("ADG"), same("+3, +3")], [same("BCD"), same("+1, +1")], [same("CGK"), same("+4, +4")]], B("Convert to places.", "স্থানলৈ সলনি কৰা।")),
        order(f"{p}.u6.q4", LODD, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Take a group", "গোট লোৱা"), B("Find its gaps", "ব্যৱধান"), B("Compare the rest", "বাকীবোৰ তুলনা"), B("Pick the mismatch", "অমিল বাছা")], B("Rule first.", "নিয়ম আগতে।")),
        solve(f"{p}.u6.q5", LODD, lambda a, b: {"q": B(f"What is the gap from {a} to {b}?", f"{a} ৰ পৰা {b} লৈ ব্যৱধান কিমান?"), "answer": str(pos(b) - pos(a)), "why": B(f"{pos(b)} − {pos(a)} = {pos(b) - pos(a)}.", f"{pos(b)} − {pos(a)} = {pos(b) - pos(a)}।"), "traps": [{"ans": str(pos(b) - pos(a) - 1), "tag": "r-m-lettergap", "why": LGAPW}]}, [("C", "K"), ("E", "R"), ("J", "U")]),
    ])
    test = {"id": "test", "title": B("Letter series test", "আখৰ শৃংখলৰ পৰীক্ষা"), "steps": [
        solve(f"{p}.t.q1", LGAP, l_next, [("E", 3), ("X", -3), ("B", 4)], input="letters"),
        solve(f"{p}.t.q2", LMIX, l_weave, [("B", 2, "Y", -2), ("D", 3, "V", -1)], input="letters"),
        solve(f"{p}.t.q3", LGROUP, l_group, [("E", 2, 1), ("A", 3, 2)], input="letters"),
        tf(f"{p}.t.q4", LFILL, B("The block of abcabc is abc.", "abcabc ৰ খণ্ড abc।"), True, B("It repeats after three letters.", "তিনি আখৰৰ পিছত ঘূৰি আহে।")),
        tf(f"{p}.t.q5", LNUM, B("In C3, E5, G7 the next term is I9.", "C3, E5, G7 ৰ পিছত I9।"), True, B("Both parts move +2.", "দুয়োটা ভাগ +2।")),
        tf(f"{p}.t.q6", LODD, B("Among BDF, HJL and PQT, the odd group is PQT.", "BDF, HJL, PQT ৰ ভিতৰত বেলেগ PQT।"), True, B("PQT has gaps +1, +3.", "PQT ৰ ব্যৱধান +1, +3।")),
    ]}
    return {"id": "rs-03-letter-series", "no": 3, "slug": "letter-series", "title": B("Letter series", "আখৰ শৃংখল"), "reign": B("Gaps, woven series, groups, blanks", "ব্যৱধান, বোৱা শৃংখল, গোট, খালী ঠাই"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


def _blanks(block, line):
    n = len(block)
    missing = "".join(block[i % n] for i, c in enumerate(line) if c == "_")
    return {"q": B(f"The block is {block}. Which letters fill {line}? Type them in order.", f"খণ্ড {block}। {line} ৰ খালী ঠাইত কি আখৰ? ক্ৰমে লিখা।"), "answer": missing.upper(), "why": B(f"The block repeats, so the blanks read {missing}.", f"খণ্ড ঘূৰি আহে, খালী ঠাইত {missing}।")}


def _odd_group(sid):
    from math_kit import odd
    return odd(sid, LODD, lambda good, bad, g: {"q": B("Three groups share a rule. Which does not?", "তিনিটা গোটৰ নিয়ম একে। কোনটোৰ নহয়?"), "right": bad, "fill": good, "why": B(f"The others have gaps {g}.", f"বাকীবোৰৰ ব্যৱধান {g}।")}, [(("ACE", "GIK", "NPR"), "SUX", "+2, +2"), (("ADG", "HKN", "PSV"), "BEI", "+3, +3"), (("BCD", "KLM", "RST"), "EFH", "+1, +1")])


class _Numbers:
    SKILLS = {k: v for k, v in SKILLS.items() if v[0] == "number-series"}
    lesson = staticmethod(lesson_numbers)


class _Letters:
    SKILLS = {k: v for k, v in SKILLS.items() if v[0] == "letter-series"}
    lesson = staticmethod(lesson_letters)


NUMBERS, LETTERS = _Numbers, _Letters
