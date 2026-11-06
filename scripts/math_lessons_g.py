"""Mathematics lessons 13 and 14: AP and GP, then trigonometry. All worked numbers are original."""
from fractions import Fraction as F
from math import isqrt
from math_kit import B, explore, fr, match, mcq, num, part, solve, stepwise, tf, unit
from math_labs import task
from math_lessons_c import diagram, lab


def m(n):
    return str(n).replace("-", "−")


# ---------------------------------------------------------------- Lesson 13
def l13():
    p = "m13"
    steps = B("The first term has no steps added, so the nth term has n − 1 steps, not n.", "প্ৰথম পদত কোনো খোজ নাই, সেয়ে n তম পদত n − 1 খোজ, n নহয়।")
    power = B("The first term has no multiplying, so the power is n − 1.", "প্ৰথম পদত পূৰণ নাই, সেয়ে ঘাত n − 1।")
    half = B("Two copies make the rectangle, so the sum is half of it. Remember to divide by 2.", "দুটা প্ৰতিলিপিয়ে আয়ত বনায়, সেয়ে যোগফল তাৰ আধা। 2ৰে হৰণ কৰিবলৈ নাপাহৰিবা।")
    u1 = unit("u1", B("Equal steps", "সমান খোজ"), "star", [
        B("An AP adds the same number d each time.", "সমান্তৰ শ্ৰেণীত প্ৰতিবাৰে একে সংখ্যা d যোগ হয়।"),
        B("nth term = $a + (n - 1)d$.", "n তম পদ = $a + (n - 1)d$।"),
        B("The middle of three terms in AP is their average.", "সমান্তৰ শ্ৰেণীৰ তিনিটা পদৰ মাজৰটো সিহঁতৰ গড়।"),
        B("Count terms with $\\frac{\\text{last} - \\text{first}}{d} + 1$.", "পদ গণা: $\\frac{\\text{শেষ} - \\text{প্ৰথম}}{d} + 1$।"),
    ], [
        lab(f"{p}.u1.s1", B("Count the steps, not the terms", "পদ নহয়, খোজ গণা"), B("The sequence 1, 4, 7, 10 climbs by 3. Blue is the start and gold is the climbing.", "1, 4, 7, 10 শ্ৰেণীটো 3কৈ বাঢ়ে। নীলা আৰম্ভণি, সোণালী বৃদ্ধি।"), {"kind": "stairs", "a": 1, "d": 3, "n": 2, "max": 12}, [
            task(B("Slide to term 5.", "5 নং পদলৈ টানা।"), {"n": 5}, B("Term 5 has only 4 gold steps. The first term has none, so it is n − 1.", "5 নং পদত মাত্ৰ 4টা সোণালী খোজ। প্ৰথম পদত নাই, সেয়ে n − 1।")),
            task(B("Slide to term 12.", "12 নং পদলৈ টানা।"), {"n": 12}, B("1 + 11 × 3 = 34. One formula reaches any term with no counting.", "1 + 11 × 3 = 34। এটা সূত্ৰই গণনা নকৰাকৈ যিকোনো পদ দিয়ে।")),
        ]),
        diagram(f"{p}.u1.s2", B("The middle term is the average", "মাজৰ পদ গড়"), [B("Equal steps mean the middle sits exactly halfway, the same symmetry as consecutive numbers.", "সমান খোজ মানে মাজৰটো ঠিক আধাত, ক্ৰমিক সংখ্যাৰ একে সমমিতি।"), B("If 5, x, 27 are in AP, x is the average of 5 and 27.", "5, x, 27 সমান্তৰ হ'লে x হৈছে 5 আৰু 27ৰ গড়।")], "flow", [B("5, x, 27", "5, x, 27"), B("$\\frac{5 + 27}{2}$", "$\\frac{5 + 27}{2}$"), B("x = 16", "x = 16")]),
        solve(f"{p}.u1.q1", "ap", lambda a, d, n: {"q": B(f"Find term {n} of {m(a)}, {m(a + d)}, {m(a + 2 * d)}, …", f"{m(a)}, {m(a + d)}, {m(a + 2 * d)}, … ৰ {n} নং পদ উলিওৱা।"), "answer": str(a + (n - 1) * d), "why": B(f"{m(a)} + {n - 1} × {m(d)}.", f"{m(a)} + {n - 1} × {m(d)}।"), "traps": [{"ans": str(a + n * d), "tag": "m-ap-n", "why": steps}]}, [(2, 3, 17), (6, 4, 13), (11, -4, 18), (12, -3, 25)], hints=[B("How many steps from term 1 to this term?", "1 নং পদৰ পৰা কিমান খোজ?")]),
        explore(f"{p}.u1.q2", "ap", lambda a, d, v: {"q": B(f"In {a}, {a + d}, {a + 2 * d}, …, which term equals {v}?", f"{a}, {a + d}, {a + 2 * d}, …ত কোনটো পদ {v}?"), "widget": {"kind": "stairs", "a": a, "d": d, "n": 1, "max": 15}, "target": (v - a) // d + 1, "answerText": B(f"Term {(v - a) // d + 1}", f"{(v - a) // d + 1} নং পদ"), "why": B(f"{v - a} ÷ {d} = {(v - a) // d} steps, plus 1 for the first term.", f"{v - a} ÷ {d} = {(v - a) // d} খোজ, প্ৰথম পদৰ বাবে 1 যোগ।")}, [(2, 3, 38), (5, 4, 45), (2, 5, 62)]),
        solve(f"{p}.u1.q3", "ap", lambda a, c: {"q": B(f"If {a}, x, {c} are in AP, find x.", f"{a}, x, {c} সমান্তৰ শ্ৰেণীত থাকিলে x উলিওৱা।"), "answer": num(F(a + c, 2)), "why": B("The middle term is the average.", "মাজৰ পদ গড়।")}, [(7, 29), (8, 20), (3, 17), (11, 29)]),
        solve(f"{p}.u1.q4", "ap", lambda d, lo, hi, first, last: {"q": B(f"How many multiples of {d} lie between {lo} and {hi}?", f"{lo} আৰু {hi}ৰ মাজত {d}ৰ কেইটা গুণিতক আছে?"), "answer": str((last - first) // d + 1), "why": B(f"From {first} to {last}: ({last} − {first}) ÷ {d} + 1.", f"{first}ৰ পৰা {last}লৈ: ({last} − {first}) ÷ {d} + 1।"), "traps": [{"ans": str((last - first) // d), "tag": "m-ap-n", "why": B("That counts the steps. Add 1 for the first term.", "সেয়া খোজ। প্ৰথম পদৰ বাবে 1 যোগ কৰা।")}]}, [(4, 15, 230, 16, 228), (6, 10, 100, 12, 96), (7, 20, 200, 21, 196)], hints=[B("Find the first and last multiples inside the range.", "সীমাৰ ভিতৰৰ প্ৰথম আৰু শেষ গুণিতক উলিওৱা।")]),
        tf(f"{p}.u1.q5", "ap", B("The 10th term of an AP is a + 10d.", "সমান্তৰ শ্ৰেণীৰ 10 নং পদ a + 10d।"), False, B("There are 9 steps between term 1 and term 10.", "1 নং আৰু 10 নং পদৰ মাজত 9 খোজ।"), ("m-ap-n", steps)),
        match(f"{p}.u1.q6", "ap", B("Match each AP to its next term", "প্ৰতিটো শ্ৰেণীক পৰৱৰ্তী পদৰ সৈতে মিলোৱা"), [
            [B("2, 5, 8", "2, 5, 8"), B("11", "11")], [B("20, 16, 12", "20, 16, 12"), B("8", "8")], [B("−3, −1, 1", "−3, −1, 1"), B("3", "3")], [B("0.5, 1, 1.5", "0.5, 1, 1.5"), B("2", "2")],
        ], B("A step can be negative or a decimal.", "খোজ ঋণাত্মক বা দশমিক হ'ব পাৰে।")),
    ])
    u2 = unit("u2", B("Adding an AP", "শ্ৰেণীৰ যোগফল"), "star", [
        B("Two copies of an AP, one flipped, make a rectangle.", "এটা ওলোটাকৈ দুটা প্ৰতিলিপিয়ে আয়ত বনায়।"),
        B("Sum = $\\frac{n(a + l)}{2}$: number of terms × average of the ends.", "যোগফল = $\\frac{n(a + l)}{2}$: পদৰ সংখ্যা × দুয়োমূৰৰ গড়।"),
        B("Sum of 1 to n is $\\frac{n(n + 1)}{2}$.", "1ৰ পৰা nৰ যোগফল $\\frac{n(n + 1)}{2}$।"),
        B("If the last term is unknown, find it first.", "শেষ পদ অজ্ঞাত হ'লে প্ৰথমে উলিওৱা।"),
    ], [
        lab(f"{p}.u2.s1", B("Two copies make a rectangle", "দুটা প্ৰতিলিপিয়ে আয়ত বনায়"), B("Adding terms one by one is slow. There is a better way, by building a rectangle.", "এটা এটাকৈ যোগ কৰাটো লেহেমীয়া। আয়ত বনোৱা আৰু ভাল উপায়।"), {"kind": "stairs", "a": 2, "d": 3, "n": 6, "max": 10, "sum": True}, [
            task(B("Add a flipped copy on top.", "ওপৰত ওলোটা প্ৰতিলিপি যোগ কৰা।"), {"paired": 1}, B("Every column is now the same height: first + last. The rectangle is n × (a + l), and the sum is half of it.", "প্ৰতিটো স্তম্ভ এতিয়া একে উচ্চতাৰ: প্ৰথম + শেষ। আয়ত n × (a + l), যোগফল তাৰ আধা।")),
        ]),
        diagram(f"{p}.u2.s2", B("The first ten numbers", "প্ৰথম দহটা সংখ্যা"), [B("1 to 100 pairs up as 1 + 100, 2 + 99, and so on: fifty pairs of 101.", "1ৰ পৰা 100 যোৰা হয় 1 + 100, 2 + 99 এনেকৈ: 101ৰ পঞ্চাশটা যোৰা।"), B("That is the formula: $\\frac{100 \\times 101}{2} = 5050$.", "এয়াই সূত্ৰ: $\\frac{100 \\times 101}{2} = 5050$।")], "flow", [B("1 + 100 = 101", "1 + 100 = 101"), B("50 pairs", "50 যোৰা"), B("50 × 101 = 5050", "50 × 101 = 5050")]),
        solve(f"{p}.u2.q1", "ap-sum", lambda n: {"q": B(f"Find 1 + 2 + 3 + … + {n}.", f"1 + 2 + 3 + … + {n} উলিওৱা।"), "answer": str(n * (n + 1) // 2), "why": B(f"$\\frac{{{n} \\times {n + 1}}}{{2}}$.", f"$\\frac{{{n} \\times {n + 1}}}{{2}}$।"), "traps": [{"ans": str(n * (n + 1)), "tag": "m-sum-half", "why": half}]}, [(20,), (50,), (100,), (30,)], hints=[B("Use $\\frac{n(n + 1)}{2}$.", "$\\frac{n(n + 1)}{2}$ ব্যৱহাৰ কৰা।")]),
        stepwise(f"{p}.u2.q2", "ap-sum", lambda a, d, last: {"q": B(f"Find {a} + {a + d} + {a + 2 * d} + … + {last}.", f"{a} + {a + d} + {a + 2 * d} + … + {last} উলিওৱা।"), "parts": [
            part(B("Number of terms?", "পদৰ সংখ্যা?"), B(str((last - a) // d + 1), str((last - a) // d + 1)), [B(str((last - a) // d), str((last - a) // d)), B(str(last - a), str(last - a))], B("Steps + 1.", "খোজ + 1।"), skill="ap", tag="m-ap-n", sid=str(a)),
            part(B("First + last?", "প্ৰথম + শেষ?"), B(str(a + last), str(a + last)), [B(str(last - a), str(last - a)), B(str(a * last), str(a * last))], B("The height of each column.", "প্ৰতিটো স্তম্ভৰ উচ্চতা।"), sid=str(a)),
            part(B("Sum?", "যোগফল?"), B(str(((last - a) // d + 1) * (a + last) // 2), str(((last - a) // d + 1) * (a + last) // 2)), [B(str(((last - a) // d + 1) * (a + last)), str(((last - a) // d + 1) * (a + last))), B(str((a + last) // 2), str((a + last) // 2))], B("Half the rectangle.", "আয়তৰ আধা।"), tag="m-sum-half", sid=str(a)),
        ], "why": B("Count, add the ends, halve.", "গণা, দুয়োমূৰ যোগ, আধা।")}, [(14, 3, 41), (5, 5, 50), (7, 2, 25)]),
        solve(f"{p}.u2.q3", "ap-sum", lambda a, d, n: {"q": B(f"Find the sum of the first {n} terms of {a}, {a + d}, {a + 2 * d}, …", f"{a}, {a + d}, {a + 2 * d}, …ৰ প্ৰথম {n}টা পদৰ যোগফল উলিওৱা।"), "answer": str(n * (2 * a + (n - 1) * d) // 2), "why": B(f"Last term {a + (n - 1) * d}, then $\\frac{{{n}({a} + {a + (n - 1) * d})}}{{2}}$.", f"শেষ পদ {a + (n - 1) * d}, তাৰ পিছত $\\frac{{{n}({a} + {a + (n - 1) * d})}}{{2}}$।"), "traps": [{"ans": str(n * (2 * a + (n - 1) * d)), "tag": "m-sum-half", "why": half}]}, [(9, 5, 16), (1, 2, 20), (3, 4, 10)]),
        tf(f"{p}.u2.q4", "ap-sum", B("The sum of an AP equals the number of terms × the average of first and last.", "সমান্তৰ শ্ৰেণীৰ যোগফল = পদৰ সংখ্যা × প্ৰথম আৰু শেষৰ গড়।"), True, B("It is the Average lesson again: evenly spaced numbers average to the middle.", "গড় পাঠৰ একে কথা: সমান ব্যৱধানৰ সংখ্যাৰ গড় মাজৰটো।")),
        solve(f"{p}.u2.q5", "ap-sum", lambda s0, r, y: {"q": B(f"A worker earns ₹{s0} in the first year with a rise of ₹{r} every year. What is the total earned in {y} years?", f"এজন কৰ্মীয়ে প্ৰথম বছৰত ₹{s0} পায়, প্ৰতি বছৰে ₹{r} বাঢ়ে। {y} বছৰত মুঠ কিমান পাব?"), "answer": str(y * (2 * s0 + (y - 1) * r) // 2), "prefix": B("₹", "₹"), "why": B("Yearly pay is an AP: add it with the sum formula.", "বছৰি দৰমহা সমান্তৰ শ্ৰেণী: যোগফলৰ সূত্ৰ লোৱা।"), "traps": [{"ans": str(s0 + (y - 1) * r), "tag": "m-ap-n", "why": B("That is the last year's pay. The question asks for the total.", "সেয়া শেষ বছৰৰ দৰমহা। প্ৰশ্নত মুঠ বিচাৰিছে।")}]}, [(5000, 500, 10), (8000, 1000, 6), (12000, 2000, 5)]),
        match(f"{p}.u2.q6", "ap-sum", B("Match each list to its sum", "প্ৰতিটো তালিকাক যোগফলৰ সৈতে মিলোৱা"), [
            [B("1 to 10", "1ৰ পৰা 10"), B("55", "55")], [B("1 to 20", "1ৰ পৰা 20"), B("210", "210")], [B("Odd numbers 1 to 9", "1ৰ পৰা 9লৈ অযুগ্ম"), B("25", "25")], [B("Even numbers 2 to 10", "2ৰ পৰা 10লৈ যুগ্ম"), B("30", "30")],
        ], B("n odd numbers add to $n^2$: the L shapes from Squares.", "n টা অযুগ্ম সংখ্যাৰ যোগফল $n^2$: বৰ্গৰ L আকৃতি।")),
    ])
    u3 = unit("u3", B("Multiplying steps", "পূৰণৰ খোজ"), "star", [
        B("A GP multiplies by the same ratio r each time.", "গুণোত্তৰ শ্ৰেণীত প্ৰতিবাৰে একে অনুপাত rৰে পূৰণ।"),
        B("nth term = $ar^{n-1}$.", "n তম পদ = $ar^{n-1}$।"),
        B("Sum of n terms = $\\frac{a(r^n - 1)}{r - 1}$.", "nটা পদৰ যোগফল = $\\frac{a(r^n - 1)}{r - 1}$।"),
        B("Multiplying grows far faster than adding.", "পূৰণ যোগতকৈ বহুত সোনকালে বাঢ়ে।"),
    ], [
        lab(f"{p}.u3.s1", B("Doubling runs away", "দুগুণ হৈ আগবাঢ়ে"), B("Start at 1 and double each time. Compare this with the stairs from before.", "1ৰ পৰা আৰম্ভ কৰি প্ৰতিবাৰে দুগুণ। আগৰ খটখটিৰ সৈতে তুলনা কৰা।"), {"kind": "stairs", "mode": "gp", "a": 1, "r": 2, "n": 3, "max": 10}, [
            task(B("Slide to term 7.", "7 নং পদলৈ টানা।"), {"n": 7}, B("64 has appeared, and the early terms already look flat.", "64 ওলাইছে, আগৰ পদবোৰ চেপেটা দেখা গৈছে।")),
            task(B("Slide to term 10.", "10 নং পদলৈ টানা।"), {"n": 10}, B("512 = $2^9$. Again the power is n − 1, for the same reason as the steps.", "512 = $2^9$। ঘাত আকৌ n − 1, খোজৰ একে কাৰণত।")),
        ]),
        diagram(f"{p}.u3.s2", B("Add or multiply?", "যোগ নে পূৰণ?"), [B("Check the gaps first: equal gaps mean AP, equal ratios mean GP.", "প্ৰথমে ব্যৱধান চোৱা: সমান ব্যৱধান মানে সমান্তৰ, সমান অনুপাত মানে গুণোত্তৰ।"), B("2, 6, 18 has gaps of 4 and 12 but a steady ratio of 3.", "2, 6, 18ৰ ব্যৱধান 4 আৰু 12, কিন্তু অনুপাত সদায় 3।")], "grid", [B("AP: 2, 5, 8 adds 3", "সমান্তৰ: 2, 5, 8ত 3 যোগ"), B("GP: 2, 6, 18 multiplies by 3", "গুণোত্তৰ: 2, 6, 18ত 3ৰে পূৰণ")]),
        solve(f"{p}.u3.q1", "gp", lambda a, r, n: {"q": B(f"Find term {n} of {a}, {a * r}, {a * r * r}, …", f"{a}, {a * r}, {a * r * r}, …ৰ {n} নং পদ উলিওৱা।"), "answer": str(a * r ** (n - 1)), "why": B(f"${a} \\times {r}^{{{n - 1}}}$.", f"${a} \\times {r}^{{{n - 1}}}$।"), "traps": [{"ans": str(a * r ** n), "tag": "m-gp-power", "why": power}, {"ans": str(a + (n - 1) * r), "tag": "m-gp-add", "why": B("You added the ratio. A GP multiplies.", "তুমি অনুপাত যোগ কৰিলা। গুণোত্তৰ শ্ৰেণীত পূৰণ হয়।")}]}, [(5, 2, 7), (3, 3, 6), (3, 2, 8), (5, 3, 5)], hints=[B("The power is one less than the term number.", "ঘাত পদৰ নম্বৰতকৈ এক কম।")]),
        solve(f"{p}.u3.q2", "gp", lambda a, r, n: {"q": B(f"Add the first {n} terms: {a} + {a * r} + {a * r * r} + …", f"প্ৰথম {n}টা পদ যোগ কৰা: {a} + {a * r} + {a * r * r} + …"), "answer": str(a * (r ** n - 1) // (r - 1)), "why": B(f"$\\frac{{{a}({r}^{{{n}}} - 1)}}{{{r} - 1}}$.", f"$\\frac{{{a}({r}^{{{n}}} - 1)}}{{{r} - 1}}$।")}, [(5, 3, 4), (3, 2, 9), (1, 3, 6)], hints=[B("Use $\\frac{a(r^n - 1)}{r - 1}$.", "$\\frac{a(r^n - 1)}{r - 1}$ ব্যৱহাৰ কৰা।")]),
        stepwise(f"{p}.u3.q3", "gp", lambda a, r, last, n: {"q": B(f"How many terms are in {a}, {a * r}, {a * r * r}, …, {last}?", f"{a}, {a * r}, {a * r * r}, …, {last}ত কেইটা পদ আছে?"), "parts": [
            part(B("Ratio?", "অনুপাত?"), B(str(r), str(r)), [B(str(r + 1), str(r + 1)), B(str(r + 3), str(r + 3))], B("Divide neighbours.", "ওচৰৰ দুটা হৰণ কৰা।"), tag="m-gp-add", sid=str(last)),
            part(B(f"{last} ÷ {a} =", f"{last} ÷ {a} ="), B(str(last // a), str(last // a)), [B(str(last - a), str(last - a)), B(str(last // a + 1), str(last // a + 1))], B("How many times was it multiplied in all?", "মুঠতে কিমান গুণ হ'ল?"), sid=str(last)),
            part(B("Number of terms?", "পদৰ সংখ্যা?"), B(str(n), str(n)), [B(str(n - 1), str(n - 1)), B(str(n + 1), str(n + 1))], B("Power of r, plus 1.", "rৰ ঘাত, যোগ 1।"), tag="m-gp-power", sid=str(last)),
        ], "why": B("Count multiplications, then add 1 for the first term.", "পূৰণ গণা, প্ৰথম পদৰ বাবে 1 যোগ।")}, [(2, 3, 162, 5), (3, 2, 96, 6), (5, 2, 320, 7)]),
        tf(f"{p}.u3.q4", "gp", B("3, 6, 12, 24 is an AP.", "3, 6, 12, 24 সমান্তৰ শ্ৰেণী।"), False, B("The gaps grow, but the ratio is always 2, so it is a GP.", "ব্যৱধান বাঢ়ে, অনুপাত সদায় 2, সেয়ে ই গুণোত্তৰ।"), ("m-gp-add", B("Look for a steady ratio, not a steady gap.", "স্থিৰ ব্যৱধান নহয়, স্থিৰ অনুপাত বিচাৰা।"))),
        solve(f"{p}.u3.q5", "gp", lambda a, c: {"q": B(f"If {a}, x, {c} are in GP, find positive x.", f"{a}, x, {c} গুণোত্তৰ শ্ৰেণীত থাকিলে ধনাত্মক x উলিওৱা।"), "answer": str(isqrt(a * c)), "why": B(f"$x^2 = {a} \\times {c}$: the continued proportion from Ratio.", f"$x^2 = {a} \\times {c}$: অনুপাত পাঠৰ ক্ৰমিক সমানুপাত।"), "traps": [{"ans": num(F(a + c, 2)), "tag": "m-gp-add", "why": B("That is the AP middle. In a GP the middle is $\\sqrt{ac}$.", "সেয়া সমান্তৰৰ মাজ। গুণোত্তৰৰ মাজ $\\sqrt{ac}$।")}]}, [(4, 25), (5, 20), (2, 18)]),
        match(f"{p}.u3.q6", "gp", B("Match each list to its type", "প্ৰতিটো তালিকাক ইয়াৰ প্ৰকাৰৰ সৈতে মিলোৱা"), [
            [B("5, 10, 15", "5, 10, 15"), B("AP, d = 5", "সমান্তৰ, d = 5")], [B("5, 10, 20", "5, 10, 20"), B("GP, r = 2", "গুণোত্তৰ, r = 2")], [B("9, 3, 1", "9, 3, 1"), B("GP, r = $\\frac{1}{3}$", "গুণোত্তৰ, r = $\\frac{1}{3}$")], [B("9, 6, 3", "9, 6, 3"), B("AP, d = −3", "সমান্তৰ, d = −3")],
        ], B("Ratios can shrink and steps can be negative.", "অনুপাত সৰু হ'ব পাৰে, খোজ ঋণাত্মক হ'ব পাৰে।")),
    ])
    test = {"id": "test", "title": B("AP and GP test", "সমান্তৰ আৰু গুণোত্তৰ পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "ap", lambda a, d, n: {"q": B(f"Term {n} of {m(a)}, {m(a + d)}, {m(a + 2 * d)}, … is", f"{m(a)}, {m(a + d)}, {m(a + 2 * d)}, …ৰ {n} নং পদ"), "right": a + (n - 1) * d, "wrong": [(a + n * d, "m-ap-n", steps)], "fill": [a + (n - 2) * d, a * n, a + (n + 1) * d], "why": B("$a + (n - 1)d$.", "$a + (n - 1)d$।")}, [(4, 7, 11), (3, 6, 25), (2, 9, 12)]),
        mcq(f"{p}.t.q2", "ap-sum", lambda a, d, n: {"q": B(f"The sum of the first {n} terms of {a}, {a + d}, … is", f"{a}, {a + d}, …ৰ প্ৰথম {n}টা পদৰ যোগফল"), "right": n * (2 * a + (n - 1) * d) // 2, "wrong": [(n * (2 * a + (n - 1) * d), "m-sum-half", half)], "fill": [a + (n - 1) * d, n * a, n * (2 * a + (n - 1) * d) // 2 + d], "why": B("$\\frac{n(a + l)}{2}$.", "$\\frac{n(a + l)}{2}$।")}, [(2, 3, 20), (5, 4, 15), (1, 2, 30)]),
        mcq(f"{p}.t.q3", "gp", lambda a, r, n: {"q": B(f"Term {n} of {a}, {a * r}, … is", f"{a}, {a * r}, …ৰ {n} নং পদ"), "right": a * r ** (n - 1), "wrong": [(a * r ** n, "m-gp-power", power)], "fill": [a * r ** (n - 2), a * r * n, a + r * n], "why": B("$ar^{n-1}$.", "$ar^{n-1}$।")}, [(3, 2, 8), (2, 3, 6), (4, 2, 7)]),
        mcq(f"{p}.t.q4", "ap", lambda d, lo, hi, first, last: {"q": B(f"How many numbers between {lo} and {hi} are divisible by {d}?", f"{lo} আৰু {hi}ৰ মাজত {d}ৰে হৰণ যোৱা সংখ্যা কেইটা?"), "right": (last - first) // d + 1, "wrong": [((last - first) // d, "m-ap-n", B("Add 1 for the first term.", "প্ৰথম পদৰ বাবে 1 যোগ কৰা।"))], "fill": [(last - first) // d + 2, (last - first) // d + 3, (last - first) // d - 1], "why": B("Steps + 1.", "খোজ + 1।")}, [(3, 10, 100, 12, 99), (5, 12, 200, 15, 200), (8, 10, 150, 16, 144)]),
        solve(f"{p}.t.q5", "ap-sum", lambda n: {"q": B(f"Find the sum of the first {n} odd numbers.", f"প্ৰথম {n}টা অযুগ্ম সংখ্যাৰ যোগফল উলিওৱা।"), "answer": str(n * n), "why": B("n odd numbers add to $n^2$.", "nটা অযুগ্ম সংখ্যাৰ যোগফল $n^2$।")}, [(10,), (15,), (20,)]),
    ]}
    return {"id": "math-13-sequences", "no": 13, "tier": "B", "face": "sequence", "title": B("AP and GP", "সমান্তৰ আৰু গুণোত্তৰ শ্ৰেণী"), "reign": B("Terms and sums", "পদ আৰু যোগফল"), "units": [u1, u2, u3], "test": test}


# ---------------------------------------------------------------- Lesson 14
def l14():
    p = "m14"
    swap = B("Sine is opposite ÷ hypotenuse; cosine is adjacent ÷ hypotenuse. Check which side faces the angle.", "ছাইন = বিপৰীত ÷ অতিভুজ; কছাইন = সংলগ্ন ÷ অতিভুজ। কোন বাহু কোণৰ সন্মুখত চোৱা।")
    flip = B("Secant is the flip of cosine, not of sine. Pair them: sin with cosec, cos with sec, tan with cot.", "ছেকেণ্ট কছাইনৰ ওলোটা, ছাইনৰ নহয়। যোৰা: sin-cosec, cos-sec, tan-cot।")
    u1 = unit("u1", B("Ratios of a shape", "আকৃতিৰ অনুপাত"), "star", [
        B("In a right triangle, sin = opposite ÷ hypotenuse.", "সমকোণী ত্ৰিভুজত sin = বিপৰীত ÷ অতিভুজ।"),
        B("cos = adjacent ÷ hypotenuse and tan = opposite ÷ adjacent.", "cos = সংলগ্ন ÷ অতিভুজ আৰু tan = বিপৰীত ÷ সংলগ্ন।"),
        B("The ratios depend on the angle, not the size.", "অনুপাত কোণৰ ওপৰত নিৰ্ভৰ কৰে, আকাৰৰ ওপৰত নহয়।"),
        B("cosec, sec and cot are the flips of sin, cos and tan.", "cosec, sec আৰু cot হৈছে sin, cos আৰু tanৰ ওলোটা।"),
    ], [
        lab(f"{p}.u1.s1", B("Same shape, same ratio", "একে আকৃতি, একে অনুপাত"), B("Sine is one side divided by another. So what happens when the whole triangle grows?", "ছাইন হৈছে এটা বাহু ভাগ আন এটা। গোটা ত্ৰিভুজ ডাঙৰ হ'লে কি হয়?"), {"kind": "triangle", "triple": [3, 4, 5], "k": 1, "max": 4}, [
            task(B("Make the triangle twice as big.", "ত্ৰিভুজটো দুগুণ ডাঙৰ কৰা।"), {"k": 2}, B("6 over 10 is still $\\frac{3}{5}$. Every side doubled, so the ratio did not move.", "6 ভাগ 10 এতিয়াও $\\frac{3}{5}$। প্ৰতিটো বাহু দুগুণ হ'ল, অনুপাত সলনি নহ'ল।")),
            task(B("Now make it four times as big.", "এতিয়া চাৰিগুণ ডাঙৰ কৰা।"), {"k": 4}, B("Sine belongs to the angle, not the size of the triangle.", "ছাইন কোণৰ, ত্ৰিভুজৰ আকাৰৰ নহয়।")),
        ]),
        diagram(f"{p}.u1.s2", B("Stand at the angle", "কোণত থিয় হোৱা"), [B("Names depend on where the angle is. The hypotenuse is always across from the right angle.", "নাম কোণৰ স্থানৰ ওপৰত নিৰ্ভৰ কৰে। অতিভুজ সদায় সমকোণৰ সন্মুখত।"), B("Opposite faces your angle and adjacent touches it.", "বিপৰীত বাহু কোণৰ সন্মুখত, সংলগ্ন বাহুৱে কোণ স্পৰ্শ কৰে।")], "grid", [B("sin: opposite ÷ hypotenuse", "sin: বিপৰীত ÷ অতিভুজ"), B("cos: adjacent ÷ hypotenuse", "cos: সংলগ্ন ÷ অতিভুজ"), B("tan: opposite ÷ adjacent", "tan: বিপৰীত ÷ সংলগ্ন")]),
        explore(f"{p}.u1.q1", "tr-ratio", lambda name_en, name_as, code, frm: {"q": B(f"Tap the {name_en} side for the angle θ.", f"θ কোণৰ {name_as} বাহুত টিপা।"), "widget": {"kind": "triangle", "triple": [3, 4, 5], "pick": True, "from": frm}, "target": code, "answerText": B(f"The {name_en} side", f"{name_as} বাহু"), "why": B("Opposite faces θ, adjacent touches it, and the hypotenuse faces the right angle.", "বিপৰীতে θৰ সন্মুখত, সংলগ্নই স্পৰ্শ কৰে, অতিভুজ সমকোণৰ সন্মুখত।")}, [("opposite", "বিপৰীত", 1, "base"), ("adjacent", "সংলগ্ন", 2, "base"), ("opposite", "বিপৰীত", 2, "top"), ("adjacent", "সংলগ্ন", 1, "top"), ("longest", "দীঘলীয়া", 3, "top")]),
        solve(f"{p}.u1.q2", "tr-ratio", lambda o, a, h: {"q": B(f"A right triangle has opposite {o}, adjacent {a} and hypotenuse {h}. Find sin θ.", f"সমকোণী ত্ৰিভুজৰ বিপৰীত {o}, সংলগ্ন {a}, অতিভুজ {h}। sin θ উলিওৱা।"), "answer": f"{o}/{h}", "why": B("Opposite ÷ hypotenuse.", "বিপৰীত ÷ অতিভুজ।"), "traps": [{"ans": f"{a}/{h}", "tag": "m-trig-swap", "why": swap}]}, [(5, 12, 13), (8, 15, 17), (7, 24, 25), (3, 4, 5)], hints=[B("Type it as top/bottom.", "লব/হৰ ৰূপত লিখা।")]),
        stepwise(f"{p}.u1.q3", "tr-ratio", lambda o, a, h: {"q": B(f"If sin θ = ${fr(o, h)}$, find cos θ.", f"sin θ = ${fr(o, h)}$ হ'লে cos θ উলিওৱা।"), "parts": [
            part(B("Draw it: opposite and hypotenuse are", "আঁকা: বিপৰীত আৰু অতিভুজ"), B(f"{o} and {h}", f"{o} আৰু {h}"), [B(f"{h} and {o}", f"{h} আৰু {o}"), B(f"{o} and {a}", f"{o} আৰু {a}")], B("Sine gives both.", "ছাইনে দুয়োটা দিয়ে।"), sid=str(h)),
            part(B("By Pythagoras, adjacent is", "পাইথাগোৰাছেৰে সংলগ্ন"), B(str(a), str(a)), [B(str(h - o), str(h - o)), B(str(h + o), str(h + o))], B(f"$\\sqrt{{{h}^2 - {o}^2}}$.", f"$\\sqrt{{{h}^2 - {o}^2}}$।"), skill="s-roots", tag="m-root-add", sid=str(h)),
            part(B("So cos θ is", "তেনেহ'লে cos θ"), B(f"${fr(a, h)}$", f"${fr(a, h)}$"), [B(f"${fr(o, a)}$", f"${fr(o, a)}$"), B(f"${fr(h, a)}$", f"${fr(h, a)}$")], B("Adjacent ÷ hypotenuse.", "সংলগ্ন ÷ অতিভুজ।"), tag="m-trig-swap", sid=str(h)),
        ], "why": B("One ratio plus Pythagoras gives all the others.", "এটা অনুপাত আৰু পাইথাগোৰাছে বাকী সকলো দিয়ে।")}, [(3, 4, 5), (5, 12, 13), (8, 15, 17)]),
        tf(f"{p}.u1.q4", "tr-ratio", B("A bigger triangle with the same angles has a bigger sine.", "একে কোণৰ ডাঙৰ ত্ৰিভুজৰ ছাইন ডাঙৰ।"), False, B("Both sides grow together, so their ratio stays the same.", "দুয়োটা বাহু একেলগে বাঢ়ে, সেয়ে অনুপাত একে থাকে।")),
        solve(f"{p}.u1.q5", "tr-ratio", lambda a, b: {"q": B(f"If cos θ = ${fr(a, b)}$, find sec θ.", f"cos θ = ${fr(a, b)}$ হ'লে sec θ উলিওৱা।"), "answer": f"{b}/{a}", "why": B("Secant is the flip of cosine.", "ছেকেণ্ট কছাইনৰ ওলোটা।"), "traps": [{"ans": f"{a}/{b}", "tag": "m-trig-flip", "why": flip}]}, [(4, 5), (5, 13), (8, 17), (3, 7)]),
        match(f"{p}.u1.q6", "tr-ratio", B("Match each ratio to its flip", "প্ৰতিটো অনুপাতক ওলোটাৰ সৈতে মিলোৱা"), [
            [B("sin θ", "sin θ"), B("cosec θ", "cosec θ")], [B("cos θ", "cos θ"), B("sec θ", "sec θ")], [B("tan θ", "tan θ"), B("cot θ", "cot θ")], [B("sin θ ÷ cos θ", "sin θ ÷ cos θ"), B("tan θ, not a flip", "tan θ, ওলোটা নহয়")],
        ], B("Each pair multiplies to 1.", "প্ৰতিটো যোৰাৰ পূৰণফল 1।")),
    ])
    u2 = unit("u2", B("One circle, the whole table", "এটা বৃত্ত, গোটা তালিকা"), "star", [
        B("On a radius of 1, sin is the height and cos is the width.", "1 ব্যাসাৰ্ধত sin উচ্চতা, cos প্ৰস্থ।"),
        B("As the angle grows, sin rises and cos falls.", "কোণ বাঢ়িলে sin বাঢ়ে, cos কমে।"),
        B("$\\sin^2\\theta + \\cos^2\\theta = 1$: this is Pythagoras on the radius.", "$\\sin^2\\theta + \\cos^2\\theta = 1$: ব্যাসাৰ্ধত পাইথাগোৰাছ।"),
        B("$\\sin(90^\\circ - \\theta) = \\cos\\theta$.", "$\\sin(90^\\circ - \\theta) = \\cos\\theta$।"),
    ], [
        lab(f"{p}.u2.s1", B("The table is one picture", "তালিকা এখন ছবি"), B("A red point moves round a quarter circle of radius 1. Blue is its height, sin. Green is its width, cos.", "ৰঙা বিন্দু 1 ব্যাসাৰ্ধৰ চতুৰ্থাংশ বৃত্তত ঘূৰে। নীলা উচ্চতা, sin। সেউজীয়া প্ৰস্থ, cos।"), {"kind": "quarter", "deg": 0}, [
            task(B("Turn to 30°.", "30°লৈ ঘূৰোৱা।"), {"deg": 30}, B("sin 30° = $\\frac{1}{2}$: the height is exactly half the radius.", "sin 30° = $\\frac{1}{2}$: উচ্চতা ব্যাসাৰ্ধৰ ঠিক আধা।")),
            task(B("Turn to 60°.", "60°লৈ ঘূৰোৱা।"), {"deg": 60}, B("Now cos 60° = $\\frac{1}{2}$. Height and width swapped: sin 30° = cos 60°.", "এতিয়া cos 60° = $\\frac{1}{2}$। উচ্চতা আৰু প্ৰস্থ সলনি হ'ল: sin 30° = cos 60°।")),
            task(B("Turn to 45°.", "45°লৈ ঘূৰোৱা।"), {"deg": 45}, B("Height equals width, so tan 45° = 1. This is the only angle where they match.", "উচ্চতা = প্ৰস্থ, সেয়ে tan 45° = 1। এই এটা কোণতহে সিহঁত সমান।")),
        ]),
        diagram(f"{p}.u2.s2", B("Pythagoras in disguise", "পাইথাগোৰাছৰ আন ৰূপ"), [B("Height, width and radius form a right triangle with hypotenuse 1.", "উচ্চতা, প্ৰস্থ আৰু ব্যাসাৰ্ধে 1 অতিভুজৰ সমকোণী ত্ৰিভুজ গঢ়ে।"), B("So $\\sin^2\\theta + \\cos^2\\theta = 1$ for every angle.", "সেয়ে প্ৰতিটো কোণত $\\sin^2\\theta + \\cos^2\\theta = 1$।")], "flow", [B("Height = sin θ", "উচ্চতা = sin θ"), B("Width = cos θ", "প্ৰস্থ = cos θ"), B("Sum of squares = 1", "বৰ্গৰ যোগফল = 1")]),
        explore(f"{p}.u2.q1", "tr-values", lambda t, deg: {"q": B(f"Find the acute angle where {t}.", f"যি সূক্ষ্ম কোণত {t} সেইটো উলিওৱা।"), "widget": {"kind": "quarter", "deg": 15}, "target": deg, "answerText": B(f"{deg}°", f"{deg}°"), "why": B("Read height for sin and width for cos.", "sinৰ বাবে উচ্চতা, cosৰ বাবে প্ৰস্থ পঢ়া।")}, [("$\\sin\\theta = \\frac{1}{2}$", 30), ("$\\cos\\theta = \\frac{1}{2}$", 60), ("$\\sin\\theta = \\cos\\theta$", 45), ("$\\sin\\theta = 1$", 90), ("$\\cos\\theta = 1$", 0)]),
        match(f"{p}.u2.q2", "tr-values", B("Match each value", "প্ৰতিটো মান মিলোৱা"), [
            [B("sin 30°", "sin 30°"), B("$\\frac{1}{2}$", "$\\frac{1}{2}$")], [B("cos 30°", "cos 30°"), B("$\\frac{\\sqrt{3}}{2}$", "$\\frac{\\sqrt{3}}{2}$")], [B("tan 45°", "tan 45°"), B("1", "1")], [B("tan 60°", "tan 60°"), B("$\\sqrt{3}$", "$\\sqrt{3}$")],
        ], B("The quarter circle gives all of these.", "চতুৰ্থাংশ বৃত্তই এই সকলো দিয়ে।")),
        solve(f"{p}.u2.q3", "tr-values", lambda tex, ans, why_en, why_as: {"q": B(f"Find ${tex}$", f"${tex}$ উলিওৱা"), "answer": ans, "why": B(why_en, why_as)}, [("\\sin 30^\\circ + \\cos 60^\\circ", "1", "$\\frac{1}{2} + \\frac{1}{2}$.", "$\\frac{1}{2} + \\frac{1}{2}$।"), ("\\tan 45^\\circ + \\sin 90^\\circ", "2", "1 + 1.", "1 + 1।"), ("\\sin^2 30^\\circ + \\cos^2 30^\\circ", "1", "The identity holds for every angle.", "প্ৰতিটো কোণত এই অভেদ সত্য।"), ("4 \\sin 30^\\circ \\cos 60^\\circ", "1", "$4 \\times \\frac{1}{2} \\times \\frac{1}{2}$.", "$4 \\times \\frac{1}{2} \\times \\frac{1}{2}$।")]),
        tf(f"{p}.u2.q4", "tr-values", B("$\\sin^2 65^\\circ + \\cos^2 65^\\circ = 1$", "$\\sin^2 65^\\circ + \\cos^2 65^\\circ = 1$"), True, B("It is true for every angle, so you never need the value of sin 65°.", "ই প্ৰতিটো কোণত সত্য, সেয়ে sin 65°ৰ মান নালাগে।")),
        stepwise(f"{p}.u2.q5", "tr-values", lambda a: {"q": B(f"Find $\\frac{{\\sin {a}^\\circ}}{{\\cos {90 - a}^\\circ}}$.", f"$\\frac{{\\sin {a}^\\circ}}{{\\cos {90 - a}^\\circ}}$ উলিওৱা।"), "parts": [
            part(B(f"Add the angles: {a} + {90 - a}", f"কোণ যোগ: {a} + {90 - a}"), B("90", "90"), [B("45", "45"), B("180", "180")], B("They are complementary.", "সিহঁত পূৰক কোণ।"), sid=str(a)),
            part(B(f"So cos {90 - a}° is the same as", f"তেনেহ'লে cos {90 - a}° একে"), B(f"sin {a}°", f"sin {a}°"), [B(f"cos {a}°", f"cos {a}°"), B(f"tan {a}°", f"tan {a}°")], B("Height and width swap at the complement.", "পূৰক কোণত উচ্চতা আৰু প্ৰস্থ সলনি হয়।"), tag="m-trig-swap", sid=str(a)),
            part(B("The value is", "মান"), B("1", "1"), [B("0", "0"), B("2", "2")], B("Something over itself.", "কোনো সংখ্যা ভাগ নিজে।"), sid=str(a)),
        ], "why": B("Look at the angles before the numbers.", "সংখ্যাৰ আগতে কোণ চোৱা।")}, [(70,), (25,), (38,)]),
        solve(f"{p}.u2.q6", "tr-values", lambda k, deg: {"q": B(f"If {k} sin A − 1 = 0 and A is acute, find A in degrees.", f"{k} sin A − 1 = 0 আৰু A সূক্ষ্ম হ'লে A ডিগ্ৰীত উলিওৱা।"), "answer": str(deg), "suffix": B("°", "°"), "why": B(f"sin A = $\\frac{{1}}{{{k}}}$.", f"sin A = $\\frac{{1}}{{{k}}}$।")}, [(2, 30), (1, 90)]),
    ])
    u3 = unit("u3", B("Heights and distances", "উচ্চতা আৰু দূৰত্ব"), "star", [
        B("Angle of elevation: looking up from level ground.", "উন্নতি কোণ: সমতলৰ পৰা ওপৰলৈ চোৱা।"),
        B("tan θ = height ÷ distance.", "tan θ = উচ্চতা ÷ দূৰত্ব।"),
        B("At 45° the height equals the distance.", "45°ত উচ্চতা = দূৰত্ব।"),
        B("Add the observer's own height at the end.", "শেষত পৰ্যবেক্ষকৰ উচ্চতা যোগ কৰা।"),
    ], [
        lab(f"{p}.u3.s1", B("One triangle in the air", "আকাশত এটা ত্ৰিভুজ"), B("You stand 30 m from a tower. Your line of sight to the top rises at 45°.", "তুমি টাৱাৰৰ পৰা 30 মিটাৰ দূৰত। শীৰ্ষলৈ দৃষ্টিৰেখা 45°ত ওপৰলৈ যায়।"), {"kind": "tower", "d": 30, "ang": 45, "k": 10, "max": 45}, [
            task(B("Raise the tower until the line reaches the top.", "ৰেখা শীৰ্ষ নোপোৱালৈ টাৱাৰ তোলা।"), {"hit": 1}, B("30 m: at 45°, tan is 1, so height equals distance.", "30 মিটাৰ: 45°ত tan 1, সেয়ে উচ্চতা = দূৰত্ব।")),
        ]),
        lab(f"{p}.u3.s2", B("Steeper angle, taller tower", "বেছি কোণ, ওখ টাৱাৰ"), B("From 10 m away, the same tower top is at 60°. The answer has a √3, so the slider counts in √3.", "10 মিটাৰৰ পৰা শীৰ্ষ 60°ত। উত্তৰত √3 আছে, সেয়ে স্লাইডাৰে √3ত গণে।"), {"kind": "tower", "d": 10, "ang": 60, "k": 3, "max": 20, "surd": True}, [
            task(B("Raise the tower until the line reaches the top.", "ৰেখা শীৰ্ষ নোপোৱালৈ টাৱাৰ তোলা।"), {"hit": 1}, B("10√3 m: tan 60° = √3, so height = 10 × √3.", "10√3 মিটাৰ: tan 60° = √3, সেয়ে উচ্চতা = 10 × √3।")),
        ]),
        explore(f"{p}.u3.q1", "tr-height", lambda d, ang, k, surd: {"q": B(f"A point is {d} m from a tower and the top is at {ang}°. Raise the tower to the sight line.", f"এটা বিন্দু টাৱাৰৰ পৰা {d} মিটাৰ দূৰত, শীৰ্ষ {ang}°ত। টাৱাৰ দৃষ্টিৰেখালৈ তোলা।"), "widget": {"kind": "tower", "d": d, "ang": ang, "k": 2, "max": 40, "surd": surd}, "target": k, "answerText": B(f"{k}√3 m" if surd else f"{k} m", f"{k}√3 মি" if surd else f"{k} মি"), "why": B(f"tan {ang}° × {d}.", f"tan {ang}° × {d}।")}, [(25, 45, 25, False), (20, 60, 20, True), (30, 30, 10, True)]),
        solve(f"{p}.u3.q2", "tr-height", lambda e, d: {"q": B(f"An observer {e} m tall is {d} m from a chimney. The top is at 45°. How tall is the chimney?", f"{e} মিটাৰ ওখ পৰ্যবেক্ষক চিমনিৰ পৰা {d} মিটাৰ দূৰত। শীৰ্ষ 45°ত। চিমনি কিমান ওখ?"), "answer": num(F(str(e)) + d), "suffix": B("m", "মি"), "why": B(f"From eye level the rise is {d} m, and the eye is {e} m up.", f"চকুৰ স্তৰৰ পৰা {d} মিটাৰ, চকু {e} মিটাৰ ওপৰত।"), "traps": [{"ans": str(d), "tag": "m-height-eye", "why": B("That is measured from eye level. Add the observer's height.", "সেয়া চকুৰ স্তৰৰ পৰা। পৰ্যবেক্ষকৰ উচ্চতা যোগ কৰা।")}]}, [(1.6, 23.4), (1.8, 18.2), (2, 38)], hints=[B("At 45°, rise equals distance.", "45°ত উচ্চতা = দূৰত্ব।")]),
        stepwise(f"{p}.u3.q3", "tr-height", lambda L: {"q": B(f"A {L} m ladder leans on a wall at 60° to the ground. How far is its foot from the wall?", f"{L} মিটাৰ জখলা মাটিৰ সৈতে 60° কৰি বেৰত হেলান দিয়া। ইয়াৰ তলৰ মূৰ বেৰৰ পৰা কিমান দূৰত?"), "parts": [
            part(B("The ladder is the", "জখলাডাল হৈছে"), B("Hypotenuse", "অতিভুজ"), [B("Opposite", "বিপৰীত"), B("Adjacent", "সংলগ্ন")], B("It faces the right angle at the wall.", "ই বেৰৰ সমকোণৰ সন্মুখত।"), sid=str(L)),
            part(B("The foot distance is the", "তলৰ দূৰত্ব হৈছে"), B("Adjacent, so use cos", "সংলগ্ন, সেয়ে cos"), [B("Opposite, so use sin", "বিপৰীত, সেয়ে sin"), B("Use tan", "tan লোৱা")], B("It touches the 60° angle.", "ই 60° কোণ স্পৰ্শ কৰে।"), tag="m-trig-swap", sid=str(L)),
            part(B("Distance?", "দূৰত্ব?"), B(f"{L // 2} m", f"{L // 2} মি"), [B(f"{L} m", f"{L} মি"), B(f"{L // 4} m", f"{L // 4} মি")], B("cos 60° = $\\frac{1}{2}$.", "cos 60° = $\\frac{1}{2}$।"), skill="tr-values", sid=str(L)),
        ], "why": B("Name the sides first, and the ratio chooses itself.", "প্ৰথমে বাহুৰ নাম দিয়া, অনুপাত নিজেই ওলায়।")}, [(20,), (16,), (12,)]),
        tf(f"{p}.u3.q4", "tr-height", B("If the shadow of a pole equals its height, the sun is at 45°.", "খুঁটাৰ ছাঁ উচ্চতাৰ সমান হ'লে সূৰ্য 45°ত।"), True, B("Height ÷ shadow = 1, and tan 45° = 1.", "উচ্চতা ÷ ছাঁ = 1, আৰু tan 45° = 1।")),
        match(f"{p}.u3.q5", "tr-height", B("Distance is 30 m. Match the angle to the height", "দূৰত্ব 30 মিটাৰ। কোণক উচ্চতাৰ সৈতে মিলোৱা"), [
            [B("30°", "30°"), B("$10\\sqrt{3}$ m", "$10\\sqrt{3}$ মি")], [B("45°", "45°"), B("30 m", "30 মি")], [B("60°", "60°"), B("$30\\sqrt{3}$ m", "$30\\sqrt{3}$ মি")], [B("A steeper look", "বেছি খাৰুৱা দৃষ্টি"), B("A taller tower", "ওখ টাৱাৰ")],
        ], B("Distance × tan θ gives the height.", "দূৰত্ব × tan θ = উচ্চতা।")),
        solve(f"{p}.u3.q6", "tr-height", lambda h, ans: {"q": B(f"A tower is {h} m tall. Its shadow is {h}√3 m long. What is the sun's angle in degrees?", f"টাৱাৰ {h} মিটাৰ ওখ। ছাঁ {h}√3 মিটাৰ দীঘল। সূৰ্যৰ কোণ ডিগ্ৰীত কিমান?"), "answer": str(ans), "suffix": B("°", "°"), "why": B("tan θ = $\\frac{1}{\\sqrt{3}}$, which is 30°.", "tan θ = $\\frac{1}{\\sqrt{3}}$, অৰ্থাৎ 30°।"), "traps": [{"ans": "60", "tag": "m-trig-swap", "why": B("Height over shadow is $\\frac{1}{\\sqrt{3}}$, so it is 30°, not 60°.", "উচ্চতা ÷ ছাঁ $\\frac{1}{\\sqrt{3}}$, সেয়ে 30°, 60° নহয়।")}]}, [(20, 30), (50, 30)]),
    ])
    test = {"id": "test", "title": B("Trigonometry test", "ত্ৰিকোণমিতি পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "tr-ratio", lambda o, a, h: {"q": B(f"Opposite {o}, adjacent {a}, hypotenuse {h}. cos θ is", f"বিপৰীত {o}, সংলগ্ন {a}, অতিভুজ {h}। cos θ"), "right": F(a, h), "wrong": [(F(o, h), "m-trig-swap", swap)], "fill": [F(o, a), F(h, a), F(a, o)], "why": B("Adjacent ÷ hypotenuse.", "সংলগ্ন ÷ অতিভুজ।")}, [(7, 24, 25), (9, 40, 41), (20, 21, 29)]),
        mcq(f"{p}.t.q2", "tr-ratio", lambda a, b: {"q": B(f"If sin θ = ${fr(a, b)}$, then cosec θ is", f"sin θ = ${fr(a, b)}$ হ'লে cosec θ"), "right": F(b, a), "wrong": [(F(a, b), "m-trig-flip", flip)], "fill": [F(a + 1, b), F(b, a + 1), F(b - a, b)], "why": B("Cosec is the flip of sin.", "cosec sinৰ ওলোটা।")}, [(3, 5), (5, 13), (2, 7)]),
        mcq(f"{p}.t.q3", "tr-values", lambda en, as_, right, w1, w2, w3: {"q": B(en, as_), "right": right, "wrong": [(w1, "m-trig-swap", swap)], "fill": [w2, w3], "why": B("Use the quarter circle.", "চতুৰ্থাংশ বৃত্ত ব্যৱহাৰ কৰা।")}, [("$\\sin 30^\\circ \\times \\cos 60^\\circ$ equals", "$\\sin 30^\\circ \\times \\cos 60^\\circ$ৰ মান", F(1, 4), F(1, 2), 1, 0), ("$\\sin 90^\\circ + \\cos 90^\\circ$ equals", "$\\sin 90^\\circ + \\cos 90^\\circ$ৰ মান", 1, 0, 2, F(1, 2)), ("$\\tan 45^\\circ - \\cos 0^\\circ$ equals", "$\\tan 45^\\circ - \\cos 0^\\circ$ৰ মান", 0, 1, 2, F(1, 2))]),
        mcq(f"{p}.t.q4", "tr-height", lambda d: {"q": B(f"From {d} m away, the top of a tower is at 45°. Its height is", f"{d} মিটাৰ দূৰৰ পৰা টাৱাৰৰ শীৰ্ষ 45°ত। ইয়াৰ উচ্চতা"), "right": d, "wrong": [(d * 2, "m-trig-swap", B("tan 45° = 1, so height equals distance.", "tan 45° = 1, সেয়ে উচ্চতা = দূৰত্ব।"))], "fill": [d // 2, d + 10, d - 5], "unit": " m", "why": B("tan 45° = 1.", "tan 45° = 1।")}, [(40,), (60,), (24,)]),
        solve(f"{p}.t.q5", "tr-values", lambda a: {"q": B(f"Find $\\sin^2 {a}^\\circ + \\cos^2 {a}^\\circ$.", f"$\\sin^2 {a}^\\circ + \\cos^2 {a}^\\circ$ উলিওৱা।"), "answer": "1", "why": B("True for every angle.", "প্ৰতিটো কোণত সত্য।")}, [(37,), (65,), (12,)]),
    ]}
    return {"id": "math-14-trig", "no": 14, "tier": "B", "face": "trig", "title": B("Trigonometry", "ত্ৰিকোণমিতি"), "reign": B("Ratios, values, height and distance", "অনুপাত, মান, উচ্চতা আৰু দূৰত্ব"), "units": [u1, u2, u3], "test": test}
