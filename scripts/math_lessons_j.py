"""Gap units, part two: interest, work, speed, sequences, trigonometry and figures.

extend() adds both parts to the lessons. New units and steps only: existing ids are untouched.
"""
from fractions import Fraction as F
from math import isqrt
from math_kit import B, explore, fr, match, num, order, part, show, solve, stepwise, tf, unit
from math_labs import task
from math_lessons_c import diagram, lab
from math_lessons_h import ex, pi
from math_lessons_i import average_extras, cubes, lcm_more, number_facts, percent_more, profit_more, ratio_values, surds, word_fraction


def t(x):
    """Same text in both languages."""
    return B(str(x), str(x))


def interest_more():
    p = "m9.x"
    return unit("u4", B("Other ways of counting", "গণনাৰ আন ধৰণ"), "star", [
        B("Half-yearly: halve the rate and double the periods.", "ছমহীয়া: হাৰ আধা আৰু সময়কাল দুগুণ।"),
        B("When the rate changes yearly, multiply each year's multiplier.", "হাৰ বছৰে সলনি হ'লে প্ৰতিবছৰৰ গুণক পূৰণ কৰা।"),
        B("Months go into the formula as a fraction of a year.", "মাহ সূত্ৰত বছৰৰ ভগ্নাংশ হিচাপে সোমায়।"),
        B("Over three years, compound beats simple by interest on interest, twice over and more.", "তিনি বছৰত চক্ৰবৃদ্ধি সুত সুতৰ সুতৰ বাবে সৰল সুততকৈ বেছি।"),
    ], [
        lab(f"{p}.s1", B("Twice a year", "বছৰত দুবাৰ"), B("A bank pays 10% a year, half-yearly. That means 5% every six months, so interest starts earning sooner.", "বেংকে বছৰত 10% ছমহীয়াকৈ দিয়ে। মানে প্ৰতি ছমাহত 5%, সেয়ে সুতে সোনকালে সুত আনে।"), {"kind": "growth", "fixRate": True, "rate": 5, "years": 1, "p": 100}, [
            task(B("Move on to two periods, one full year.", "দুটা সময়কাললৈ যোৱা, গোটেই এবছৰ।"), {"years": 2}, B("100 grows to 110.25, more than the 110 that yearly payment gives.", "100 বাঢ়ি 110.25 হয়, বছৰি দিয়া 110তকৈ বেছি।")),
        ]),
        diagram(f"{p}.s2", B("Months are part of a year", "মাহ বছৰৰ অংশ"), [B("The rate in the formula is for a year, so 9 months must enter as $\\frac{9}{12}$ of a year.", "সূত্ৰৰ হাৰ বছৰৰ বাবে, সেয়ে 9 মাহ $\\frac{9}{12}$ বছৰ হিচাপে সোমাব লাগিব।"), B("Forget that and the interest comes out twelve times too big.", "পাহৰিলে সুত বাৰগুণ ডাঙৰ ওলায়।")], "flow", [B("9 months", "9 মাহ"), B("$\\frac{3}{4}$ of a year", "বছৰৰ $\\frac{3}{4}$"), B("P × r × $\\frac{3}{4}$ ÷ 100", "P × r × $\\frac{3}{4}$ ÷ 100")]),
        solve(f"{p}.q1", "i-half", lambda P, r: {"q": B(f"Find the amount on ₹{P} at {r}% a year for 1 year, compounded half-yearly.", f"₹{P}ৰ {r}% বাৰ্ষিক হাৰত 1 বছৰৰ ছমহীয়া চক্ৰবৃদ্ধি সমূল ধন উলিওৱা।"), "answer": str(ex(F(P) * (100 + F(r, 2)) ** 2, 10000)), "prefix": B("₹", "₹"), "why": B(f"{F(r, 2)}% for two periods.", f"দুটা সময়কালৰ বাবে {F(r, 2)}%।"), "traps": [{"ans": str(ex(P * (100 + r), 100)), "tag": "m-halfyear", "why": B("That counts one yearly payment. Half-yearly means two smaller ones.", "সেয়া এবছৰৰ এবাৰৰ হিচাপ। ছমহীয়া মানে দুবাৰ সৰুকৈ।")}]}, [(8000, 10), (4000, 20), (10000, 10), (2000, 20)], hints=[B("Halve the rate, double the periods.", "হাৰ আধা, সময়কাল দুগুণ।")]),
        solve(f"{p}.q2", "i-half", lambda P, a, b: {"q": B(f"₹{P} is invested at {a}% for the first year and {b}% for the second, compounded yearly. Find the amount.", f"₹{P} প্ৰথম বছৰ {a}% আৰু দ্বিতীয় বছৰ {b}%ত চক্ৰবৃদ্ধিত ৰখা হ'ল। সমূল ধন উলিওৱা।"), "answer": str(ex(P * (100 + a) * (100 + b), 10000)), "prefix": B("₹", "₹"), "why": B("Multiply both years' multipliers.", "দুয়োবছৰৰ গুণক পূৰণ কৰা।"), "traps": [{"ans": str(ex(P * (100 + a + b), 100)), "tag": "m-si-ci", "why": B("Adding the rates is simple interest. The second year works on the grown sum.", "হাৰ যোগ কৰা সৰল সুত। দ্বিতীয় বছৰ বঢ়া ধনৰ ওপৰত হয়।")}]}, [(1000, 10, 20), (2000, 10, 5), (5000, 20, 10)]),
        stepwise(f"{p}.q3", "i-diff", lambda P, r: {"q": B(f"Find the difference between compound and simple interest on ₹{P} at {r}% for 3 years.", f"₹{P}ৰ {r}%ত 3 বছৰৰ চক্ৰবৃদ্ধি আৰু সৰল সুতৰ পাৰ্থক্য উলিওৱা।"), "parts": [
            part(B("Simple interest?", "সৰল সুত?"), t(f"₹{ex(P * r * 3, 100)}"), [t(f"₹{ex(P * r, 100)}"), t(f"₹{ex(P * r * 2, 100)}")], B("Three equal slices.", "তিনিটা সমান ভাগ।"), sid=str(P)),
            part(B("Compound interest?", "চক্ৰবৃদ্ধি সুত?"), t(f"₹{ex(F(P) * (100 + r) ** 3, 10 ** 6) - P}"), [t(f"₹{ex(F(P) * (100 + r) ** 3, 10 ** 6)}"), t(f"₹{ex(P * r * 3, 100) + 1}")], B("Multiply three times, then take off the principal.", "তিনিবাৰ পূৰণ কৰি মূলধন বিয়োগ কৰা।"), sid=str(P)),
            part(B("Difference?", "পাৰ্থক্য?"), t(f"₹{ex(F(P) * (100 + r) ** 3, 10 ** 6) - P - ex(P * r * 3, 100)}"), [t(f"₹{ex(P * r * r, 10000)}"), t(f"₹{ex(P * r * r * 2, 10000)}")], B("Two years would give the smaller figure; three years add more.", "দুবছৰত সৰু সংখ্যাটো হয়; তিনি বছৰত আৰু বাঢ়ে।"), sid=str(P)),
        ], "why": B("The gap grows faster than the years.", "পাৰ্থক্য বছৰতকৈ বেগাই বাঢ়ে।")}, [(1000, 10), (8000, 5), (2000, 10)]),
        solve(f"{p}.q4", "i-si", lambda P, r, m: {"q": B(f"Find the simple interest on ₹{P} at {r}% a year for {m} months.", f"₹{P}ৰ {r}% বাৰ্ষিক হাৰত {m} মাহৰ সৰল সুত উলিওৱা।"), "answer": str(ex(P * r * m, 1200)), "prefix": B("₹", "₹"), "why": B(f"{m} months is ${fr(m, 12)}$ of a year.", f"{m} মাহ বছৰৰ ${fr(m, 12)}$।"), "traps": [{"ans": str(ex(P * r * m, 100)), "tag": "m-month-years", "why": B("The rate is yearly, so turn months into a fraction of a year.", "হাৰ বাৰ্ষিক, সেয়ে মাহক বছৰৰ ভগ্নাংশ কৰা।")}]}, [(1500, 8, 9), (1200, 5, 6), (2400, 10, 8)], hints=[B("Divide the months by 12.", "মাহক 12ৰে হৰণ কৰা।")]),
        solve(f"{p}.q5", "i-solve", lambda a, b, r: {"q": B(f"Simple interest at {r}% a year is ${fr(a, b)}$ of the principal. How many years?", f"{r}% বাৰ্ষিক হাৰত সৰল সুত মূলধনৰ ${fr(a, b)}$। কিমান বছৰ?"), "answer": str(ex(F(a, b) * 100, r)), "suffix": B("years", "বছৰ"), "why": B(f"Take principal 100. Interest is {num(F(a, b) * 100)}, at {r} a year.", f"মূলধন 100 ধৰা। সুত {num(F(a, b) * 100)}, বছৰি {r}।")}, [(2, 5, 5), (1, 4, 5), (1, 2, 10), (3, 5, 12)]),
        match(f"{p}.q6", "i-si", B("Match each period to its share of a year", "প্ৰতিটো সময়ক বছৰৰ অংশৰ সৈতে মিলোৱা"), [
            [B("3 months", "3 মাহ"), t("$\\frac{1}{4}$")], [B("6 months", "6 মাহ"), t("$\\frac{1}{2}$")], [B("8 months", "8 মাহ"), t("$\\frac{2}{3}$")], [B("9 months", "9 মাহ"), t("$\\frac{3}{4}$")],
        ], B("Divide the months by 12.", "মাহক 12ৰে হৰণ কৰা।")),
        tf(f"{p}.q7", "i-half", B("At one yearly rate, half-yearly compounding gives more than yearly compounding.", "একে বাৰ্ষিক হাৰত ছমহীয়া চক্ৰবৃদ্ধিয়ে বছৰি চক্ৰবৃদ্ধিতকৈ বেছি দিয়ে।"), True, B("Interest joins the principal sooner, so it earns for longer.", "সুত সোনকালে মূলধনত মিলে, সেয়ে বেছি সময় সুত আনে।")),
    ])


def work_more():
    p = "m10.x"
    return unit("u4", B("Sharing work and pay", "কাম আৰু মজুৰি ভাগ"), "star", [
        B("Pay is shared in the ratio of work rates, the reverse of days.", "মজুৰি কামৰ হাৰৰ অনুপাতত ভাগ হয়, দিনৰ ওলোটা।"),
        B("Part done = days worked ÷ days needed alone.", "কৰা অংশ = কাম কৰা দিন ÷ অকলে লগা দিন।"),
        B("A group's rate minus one member's rate leaves the rest.", "গোটৰ হাৰৰ পৰা এজনৰ হাৰ বিয়োগ কৰিলে বাকীখিনি থাকে।"),
        B("$\\frac{M_1 D_1 H_1}{W_1} = \\frac{M_2 D_2 H_2}{W_2}$ when work also changes.", "কামো সলনি হ'লে $\\frac{M_1 D_1 H_1}{W_1} = \\frac{M_2 D_2 H_2}{W_2}$।"),
    ], [
        lab(f"{p}.s1", B("Who earned what", "কোনে কিমান পালে"), B("A alone needs 10 days and B alone 15. Together they get ₹500. Watch the tank to see who did how much.", "A অকলে 10 দিন, B অকলে 15 দিন। দুয়ো একেলগে ₹500 পায়। কোনে কিমান কৰিলে টেংকীত চোৱা।"), {"kind": "tank", "taps": [{"n": "A", "t": 10}, {"n": "B", "t": 15}]}, [
            task(B("Run the days until it is full.", "ভৰি নোহোৱালৈ দিন চলাই যোৱা।"), {"full": 1}, B("A pours 3 parts a day and B pours 2. So A earns ₹300 and B ₹200.", "A দিনে 3 ভাগ, B 2 ভাগ দিয়ে। সেয়ে A ₹300, B ₹200 পায়।")),
        ]),
        diagram(f"{p}.s2", B("When hours and work change too", "ঘণ্টা আৰু কামো সলনি হ'লে"), [B("People, days and hours multiply to give effort. More work needs more effort.", "মানুহ, দিন, ঘণ্টা পূৰণ কৰিলে শ্ৰম হয়। বেছি কামত বেছি শ্ৰম লাগে।"), B("So effort per unit of work stays the same on both sides.", "সেয়ে কামৰ প্ৰতি একক শ্ৰম দুয়োফালে সমান।")], "flow", [B("People × days × hours", "মানুহ × দিন × ঘণ্টা"), B("÷ work done", "÷ কৰা কাম"), B("Equal on both sides", "দুয়োফালে সমান")]),
        solve(f"{p}.q1", "w-share", lambda a, b, w_: {"q": B(f"A alone takes {a} days and B alone {b} days. Together they finish and earn ₹{w_}. Find A's share.", f"A অকলে {a} দিন, B অকলে {b} দিন লয়। একেলগে শেষ কৰি ₹{w_} পায়। Aৰ ভাগ উলিওৱা।"), "answer": str(ex(w_ * b, a + b)), "prefix": B("₹", "₹"), "why": B(f"Rates are ${fr(1, a)}$ and ${fr(1, b)}$, which is {b} : {a}.", f"হাৰ ${fr(1, a)}$ আৰু ${fr(1, b)}$, অৰ্থাৎ {b} : {a}।"), "traps": [{"ans": str(ex(w_ * a, a + b)), "tag": "m-wage-days", "why": B("More days means a slower worker, so less pay. Share by rate, not days.", "বেছি দিন মানে লাহে কৰা, সেয়ে কম মজুৰি। দিনেৰে নহয়, হাৰেৰে ভাগ কৰা।")}]}, [(10, 15, 500), (12, 6, 900), (20, 30, 1000)], hints=[B("Flip the days to get the ratio of pay.", "দিন ওলোটাই মজুৰিৰ অনুপাত পোৱা।")]),
        stepwise(f"{p}.q2", "w-share", lambda a, b, d: {"q": B(f"A can do a job in {a} days and B in {b} days. A works {d} days and leaves. How long does B take to finish?", f"A এটা কাম {a} দিনত, B {b} দিনত কৰিব পাৰে। A {d} দিন কৰি গুচি যায়। বাকী কৰিবলৈ Bৰ কিমান দিন লাগিব?"), "parts": [
            part(B("Part A did?", "Aই কৰা অংশ?"), t(show(F(d, a))), [t(show(F(d, b))), t(show(F(1, a)))], B("Days worked over days alone.", "কৰা দিন ভাগ অকলে লগা দিন।"), sid=str(a)),
            part(B("Part left?", "বাকী অংশ?"), t(show(1 - F(d, a))), [t(show(F(d, a) + F(1, 12))), t("1")], B("Take it from the whole job.", "গোটেই কামৰ পৰা বিয়োগ কৰা।"), sid=str(a)),
            part(B("B's days?", "Bৰ দিন?"), t(ex((1 - F(d, a)) * b)), [t(b), t(ex((1 - F(d, a)) * b) + d)], B("Part left × B's days for the whole job.", "বাকী অংশ × Bৰ গোটেই কামৰ দিন।"), sid=str(a)),
        ], "why": B("Each part of a job has its own share of the days.", "কামৰ প্ৰতিটো অংশৰ নিজা দিনৰ ভাগ থাকে।")}, [(12, 18, 4), (10, 20, 5), (15, 30, 5)]),
        solve(f"{p}.q3", "w-rate", lambda x, y: {"q": B(f"A and B together take {x} days. A alone takes {y} days. How long does B take alone?", f"A আৰু B একেলগে {x} দিন লয়। A অকলে {y} দিন লয়। B অকলে কিমান দিন ল'ব?"), "answer": num(1 / (F(1, x) - F(1, y))), "suffix": B("days", "দিন"), "why": B(f"${fr(1, x)} - {fr(1, y)}$ is B's daily part.", f"${fr(1, x)} - {fr(1, y)}$ Bৰ দৈনিক অংশ।"), "traps": [{"ans": str(y - x), "tag": "m-work-days", "why": B("Subtract rates, not days.", "দিন নহয়, হাৰ বিয়োগ কৰা।")}]}, [(6, 10), (4, 12), (10, 15), (12, 20)]),
        solve(f"{p}.q4", "w-rate", lambda x, y, z: {"q": B(f"A and B take {x} days, B and C take {y} days, C and A take {z} days. How long do all three take together?", f"A আৰু Bই {x} দিন, B আৰু Cই {y} দিন, C আৰু Aই {z} দিন লয়। তিনিও একেলগে কিমান দিন ল'ব?"), "answer": num(2 / (F(1, x) + F(1, y) + F(1, z))), "suffix": B("days", "দিন"), "why": B("Adding the three pairs counts everyone twice, so halve it.", "তিনিওটা যোৰা যোগ কৰিলে প্ৰত্যেকে দুবাৰ আহে, সেয়ে আধা কৰা।")}, [(6, 10, 15), (8, 12, 24), (6, 12, 4)], hints=[B("Add the three rates, then halve.", "তিনিওটা হাৰ যোগ কৰি আধা কৰা।")]),
        solve(f"{p}.q5", "w-men", lambda m1, h1, d1, w1, m2, h2, w2: {"q": B(f"{m1} people working {h1} hours a day make {w1} chairs in {d1} days. How many days do {m2} people working {h2} hours a day need for {w2} chairs?", f"{m1} জনে দিনে {h1} ঘণ্টাকৈ {d1} দিনত {w1}খন চকী বনায়। {m2} জনে দিনে {h2} ঘণ্টাকৈ {w2}খন চকী কিমান দিনত বনাব?"), "answer": str(ex(F(m1 * d1 * h1 * w2), w1 * m2 * h2)), "suffix": B("days", "দিন"), "why": B("Effort per chair is the same on both sides.", "প্ৰতিখন চকীৰ শ্ৰম দুয়োফালে সমান।")}, [(12, 8, 10, 120, 8, 6, 90), (10, 8, 6, 80, 12, 5, 100), (15, 10, 4, 60, 10, 6, 90)]),
        tf(f"{p}.q6", "w-share", B("The worker who needs more days gets the bigger share of the pay.", "বেছি দিন লগা জনে মজুৰিৰ ডাঙৰ ভাগ পায়।"), False, B("Needing more days means doing less each day.", "বেছি দিন লগা মানে দিনে কম কৰা।"), ("m-wage-days", B("Pay follows work done, not days taken.", "মজুৰি কৰা কামৰ ওপৰত, লগা দিনৰ ওপৰত নহয়।"))),
        match(f"{p}.q7", "w-share", B("Match each pair of workers to their pay ratio", "প্ৰতিটো যোৰাক মজুৰিৰ অনুপাতৰ সৈতে মিলোৱা"), [
            [B("10 and 15 days", "10 আৰু 15 দিন"), B("3 : 2", "3 : 2")], [B("12 and 6 days", "12 আৰু 6 দিন"), B("1 : 2", "1 : 2")], [B("8 and 24 days", "8 আৰু 24 দিন"), B("3 : 1", "3 : 1")], [B("20 and 25 days", "20 আৰু 25 দিন"), B("5 : 4", "5 : 4")],
        ], B("Flip the days, then simplify.", "দিন ওলোটাই সৰল কৰা।")),
    ])


def speed_extras():
    return {
        "u1": [solve("m11.u1.q6", "sp-rel", lambda L, v, b: {"q": B(f"A train {L} m long runs at {v} km/h. How many seconds does it take to cross a bridge {b} m long?", f"{L} মিটাৰ দীঘল ৰেল {v} km/hত চলে। {b} মিটাৰ দীঘল দলং পাৰ হ'বলৈ কিমান ছেকেণ্ড লাগিব?"), "answer": str(ex((L + b) * 18, v * 5)), "suffix": B("seconds", "ছেকেণ্ড"), "why": B(f"{L} + {b} m at {ex(v * 5, 18)} m/s.", f"{ex(v * 5, 18)} m/sত {L} + {b} মিটাৰ।"), "traps": [{"ans": str(ex(b * 18, v * 5)), "tag": "m-train-length", "why": B("The whole train must clear, so add its own length.", "গোটেই ৰেলখন পাৰ হ'ব লাগে, সেয়ে নিজৰ দৈৰ্ঘ্য যোগ কৰা।")}]}, [(120, 54, 180), (200, 72, 100), (150, 36, 250)], hints=[B("× 5/18 turns km/h into m/s.", "× 5/18ই km/hক m/s কৰে।")])],
        "u3": [stepwise("m11.u3.q7", "sp-rel", lambda t1, t2, P: {"q": B(f"A train passes a man in {t1} seconds and a {P} m platform in {t2} seconds. Find its length.", f"এখন ৰেলে এজন মানুহক {t1} ছেকেণ্ডত আৰু {P} মিটাৰৰ প্লেটফৰ্ম {t2} ছেকেণ্ডত পাৰ হয়। ইয়াৰ দৈৰ্ঘ্য উলিওৱা।"), "parts": [
            part(B("Extra seconds for the platform?", "প্লেটফৰ্মৰ বাবে অতিৰিক্ত ছেকেণ্ড?"), t(t2 - t1), [t(t2), t(t2 + t1)], B("The train's own length costs the same in both.", "ৰেলৰ নিজৰ দৈৰ্ঘ্যৰ সময় দুয়োটাত একে।"), sid=str(P)),
            part(B("Speed?", "গতি?"), t(f"{ex(P, t2 - t1)} m/s"), [t(f"{ex(P, t2 - t1) + 5} m/s"), t(f"{ex(P, t2 - t1) - 5} m/s")], B("Platform length over extra seconds.", "প্লেটফৰ্মৰ দৈৰ্ঘ্য ভাগ অতিৰিক্ত ছেকেণ্ড।"), sid=str(P)),
            part(B("Train length?", "ৰেলৰ দৈৰ্ঘ্য?"), t(f"{ex(P, t2 - t1) * t1} m"), [t(f"{P} m "), t(f"{ex(P, t2 - t1) * t2} m")], B("Speed × time to pass the man.", "গতি × মানুহক পাৰ হোৱা সময়।"), tag="m-train-length", sid=str(P)),
        ], "why": B("The gap between the two times is the platform alone.", "দুই সময়ৰ পাৰ্থক্য কেৱল প্লেটফৰ্মৰ।")}, [(8, 20, 240), (12, 30, 270), (10, 25, 300)])],
    }


def sequence_more():
    p = "m13.x"
    return unit("u4", B("Sequences in disguise", "ছদ্মবেশী শ্ৰেণী"), "star", [
        B("In any three AP terms, twice the middle equals the two outer terms added.", "সমান্তৰ শ্ৰেণীৰ তিনিটা পদত মাজৰ পদৰ দুগুণ = বাহিৰৰ দুটাৰ যোগফল।"),
        B("Given a sum, put it in $S = \\frac{n}{2}(2a + (n - 1)d)$ and solve.", "যোগফল দিলে $S = \\frac{n}{2}(2a + (n - 1)d)$ত বহুৱাই সমাধান কৰা।"),
        B("When a list zigzags, read odd and even places apart.", "তালিকা আঁকাবাঁকা হ'লে অযুগ্ম আৰু যুগ্ম স্থান বেলেগকৈ পঢ়া।"),
        B("A fixed yearly rise in pay is an AP.", "বছৰি নিৰ্দিষ্ট দৰমহা বৃদ্ধি সমান্তৰ শ্ৰেণী।"),
    ], [
        lab(f"{p}.s1", B("A salary is a staircase", "দৰমহা এখন জখলা"), B("Pay starts at ₹2 thousand and rises ₹2 thousand a year. Each stair is one year.", "দৰমহা ₹2 হাজাৰৰ পৰা আৰম্ভ হৈ বছৰি ₹2 হাজাৰ বাঢ়ে। প্ৰতিটো খটখটি এবছৰ।"), {"kind": "stairs", "a": 2, "d": 2, "n": 2, "max": 10}, [
            task(B("Climb to year 5.", "পাঁচ বছৰলৈ উঠা।"), {"n": 5}, B("Year 5 pays 2 + 4 × 2 = ₹10 thousand. Four rises, not five.", "পঞ্চম বছৰত 2 + 4 × 2 = ₹10 হাজাৰ। পাঁচ নহয়, চাৰিটা বৃদ্ধি।")),
        ]),
        diagram(f"{p}.s2", B("Two lists in one", "এটাত দুটা তালিকা"), [B("1, 4, 2, 5, 3 looks random until you read every second number.", "1, 4, 2, 5, 3 এটা এৰি এটা নপঢ়ালৈ এলোমেলো যেন লাগে।"), B("Then there are two calm lists taking turns.", "তেতিয়া দুটা শান্ত তালিকা পাল পাতি আহে।")], "flow", [B("Places 1, 3, 5: 1, 2, 3", "1, 3, 5 স্থান: 1, 2, 3"), B("Places 2, 4, 6: 4, 5, 6", "2, 4, 6 স্থান: 4, 5, 6"), B("Next is 6", "পিছৰটো 6")]),
        solve(f"{p}.q1", "ap", lambda c, e: {"q": B(f"$x$, $2x + {c}$ and $4x - {e}$ are in AP. Find $x$.", f"$x$, $2x + {c}$ আৰু $4x - {e}$ সমান্তৰ শ্ৰেণীত আছে। $x$ উলিওৱা।"), "answer": str(2 * c + e), "why": B(f"$2(2x + {c}) = x + 4x - {e}$.", f"$2(2x + {c}) = x + 4x - {e}$।")}, [(1, 2), (3, 1), (2, 5)], hints=[B("Twice the middle equals the outer two added.", "মাজৰ দুগুণ = বাহিৰৰ দুটাৰ যোগফল।")]),
        solve(f"{p}.q2", "ap-sum", lambda n, d, s_: {"q": B(f"The sum of the first {n} terms of an AP with common difference {d} is {s_}. Find the first term.", f"সাধাৰণ অন্তৰ {d} হোৱা সমান্তৰ শ্ৰেণীৰ প্ৰথম {n}টা পদৰ যোগফল {s_}। প্ৰথম পদ উলিওৱা।"), "answer": str(ex(F(2 * s_, n) - (n - 1) * d, 2)), "why": B(f"$\\frac{{{n}}}{{2}}(2a + {(n - 1) * d}) = {s_}$.", f"$\\frac{{{n}}}{{2}}(2a + {(n - 1) * d}) = {s_}$।")}, [(10, 3, 155), (20, 2, 420), (8, 5, 180), (12, 4, 300)]),
        solve(f"{p}.q3", "ap-sum", lambda a, n, s_: {"q": B(f"The sum of the first {n} terms of an AP starting at {a} is {s_}. Find the common difference.", f"{a}ৰে আৰম্ভ হোৱা সমান্তৰ শ্ৰেণীৰ প্ৰথম {n}টা পদৰ যোগফল {s_}। সাধাৰণ অন্তৰ উলিওৱা।"), "answer": str(ex(F(2 * s_, n) - 2 * a, n - 1)), "why": B(f"$\\frac{{{n}}}{{2}}({2 * a} + {n - 1}d) = {s_}$.", f"$\\frac{{{n}}}{{2}}({2 * a} + {n - 1}d) = {s_}$।")}, [(3, 10, 165), (5, 8, 124), (2, 6, 87)]),
        stepwise(f"{p}.q4", "ap-sum", lambda a, d, n: {"q": B(f"A salary starts at ₹{a} a month and rises ₹{d} a month every year. Find the monthly pay in year {n} and the sum of the {n} monthly rates.", f"দৰমহা মাহে ₹{a}ৰে আৰম্ভ হৈ প্ৰতিবছৰে মাহে ₹{d} বাঢ়ে। {n} নং বছৰৰ মাহিলী দৰমহা আৰু {n}টা মাহিলী হাৰৰ যোগফল উলিওৱা।"), "parts": [
            part(B("Pay in the last year?", "শেষ বছৰৰ দৰমহা?"), t(f"₹{a + (n - 1) * d}"), [t(f"₹{a + n * d}"), t(f"₹{a + (n - 2) * d}")], B(f"{n - 1} rises.", f"{n - 1}টা বৃদ্ধি।"), tag="m-ap-n", sid=str(a)),
            part(B("Sum?", "যোগফল?"), t(f"₹{ex(n * (2 * a + (n - 1) * d), 2)}"), [t(f"₹{n * (2 * a + (n - 1) * d)}"), t(f"₹{a * n}")], B("Number × average of first and last.", "সংখ্যা × প্ৰথম আৰু শেষৰ গড়।"), tag="m-sum-half", sid=str(a)),
        ], "why": B("Pay rises are an AP, whatever the story says.", "কাহিনী যিয়েই নহওক, দৰমহা বৃদ্ধি সমান্তৰ শ্ৰেণী।")}, [(20000, 1000, 10), (30000, 2000, 5), (12000, 500, 8)]),
        solve(f"{p}.q5", "ap", lambda s_, a: {"q": B(f"Find the next number: {s_}, ?", f"পিছৰ সংখ্যাটো উলিওৱা: {s_}, ?"), "answer": str(a), "why": B("Two lists take turns.", "দুটা তালিকা পাল পাতি আহে।")}, [("1, 4, 2, 5, 3", 6), ("2, 10, 4, 20, 6", 30), ("5, 3, 6, 5, 7", 7), ("10, 1, 9, 2, 8", 3)], hints=[B("Read every second number.", "এটা এৰি এটা পঢ়া।")]),
        tf(f"{p}.q6", "ap", B("The middle of three AP terms is the average of the other two.", "সমান্তৰ শ্ৰেণীৰ তিনিটা পদৰ মাজৰটো আন দুটাৰ গড়।"), True, B("Equal steps either side make it the exact centre.", "দুয়োফালে সমান খোজ, সেয়ে ই ঠিক মাজ।")),
        order(f"{p}.q7", "ap-sum", B("Put the steps for finding the first term in order", "প্ৰথম পদ উলিওৱাৰ খোজ ক্ৰমত সজোৱা"), [B("Write the sum formula", "যোগফলৰ সূত্ৰ লিখা"), B("Put in n, d and S", "n, d আৰু S বহুওৱা"), B("Clear the $\\frac{n}{2}$", "$\\frac{n}{2}$ আঁতৰোৱা"), B("Solve for a", "aৰ মান উলিওৱা")], B("Same formula, read backwards.", "একে সূত্ৰ, ওলোটাকৈ পঢ়া।")),
    ])


def interest_extras():
    return {"u2": [solve("m9.u2.q7", "i-solve", lambda P, r1, t1, r2, t2: {"q": B(f"₹{P} at {r1}% for {t1} years earns the same simple interest as how much at {r2}% for {t2} years?", f"₹{P}ৰ {r1}%ত {t1} বছৰৰ সৰল সুত কিমান ধনৰ {r2}%ত {t2} বছৰৰ সুতৰ সমান?"), "answer": str(ex(P * r1 * t1, r2 * t2)), "prefix": B("₹", "₹"), "why": B("Put P × r × t equal on both sides.", "দুয়োফালে P × r × t সমান কৰা।")}, [(1000, 6, 5, 5, 3), (1500, 4, 5, 5, 2), (2000, 3, 4, 6, 2)])]}


def trig_extras():
    return {
        "u2": [solve("m14.u2.q7", "tr-values", lambda text, a, doubled: {"q": B(f"If ${text}$, find A in degrees.", f"${text}$ হ'লে A ডিগ্ৰীত উলিওৱা।"), "answer": str(a), "suffix": B("°", "°"), "why": B(f"The whole angle is {doubled}°, so divide it.", f"গোটেই কোণ {doubled}°, সেয়ে হৰণ কৰা।"), "traps": [{"ans": str(doubled), "tag": "m-angle-double", "why": B("That is the whole bracket. A is only part of it.", "সেয়া গোটেই বন্ধনীটো। A তাৰ এটা অংশ।")}]}, [("\\sin 2A = \\frac{\\sqrt{3}}{2}", 30, 60), ("\\cos 2A = \\frac{1}{2}", 30, 60), ("\\tan 3A = 1", 15, 45), ("\\sin 2A = 1", 45, 90)])],
        "u3": [stepwise("m14.u3.q7", "tr-height", lambda d: {"q": B(f"From two points {d} m apart in line with a tower, the top is seen at 60° and 30°. Find its height.", f"টাৱাৰৰ সৈতে এক ৰেখাত থকা {d} মিটাৰ আঁতৰৰ দুটা বিন্দুৰ পৰা শীৰ্ষ 60° আৰু 30°ত দেখা যায়। উচ্চতা উলিওৱা।"), "parts": [
            part(B("Near distance x. Far distance?", "ওচৰৰ দূৰত্ব x। দূৰৰ দূৰত্ব?"), t("3x"), [t("2x"), t("$\\sqrt{3}x$")], B("$\\tan 30^\\circ$ is a third of $\\tan 60^\\circ$.", "$\\tan 30^\\circ$ হৈছে $\\tan 60^\\circ$ৰ তিনিভাগৰ এভাগ।"), sid=str(d)),
            part(B("So x =", "সেয়ে x ="), t(f"{ex(d, 2)} m"), [t(f"{d} m"), t(f"{ex(d, 2) * 3} m")], B(f"The gap 2x is {d}.", f"ব্যৱধান 2x = {d}।"), sid=str(d)),
            part(B("Height?", "উচ্চতা?"), t(f"${ex(d, 2)}\\sqrt{{3}}$ m"), [t(f"${d}\\sqrt{{3}}$ m"), t(f"{ex(d, 2)} m")], B("x × $\\tan 60^\\circ$.", "x × $\\tan 60^\\circ$।"), sid=str(d)),
        ], "why": B("Two angles of 30° and 60° always give distances of x and 3x.", "30° আৰু 60°ই সদায় x আৰু 3x দূৰত্ব দিয়ে।")}, [(16,), (30,), (50,)])],
    }


def identities():
    p = "m14.x"
    return unit("u4", B("Identities", "অভেদ"), "star", [
        B("$\\sin^2\\theta + \\cos^2\\theta = 1$ for every angle.", "প্ৰতিটো কোণৰ বাবে $\\sin^2\\theta + \\cos^2\\theta = 1$।"),
        B("$\\sec^2\\theta - \\tan^2\\theta = 1$, so sec − tan and sec + tan are reciprocals.", "$\\sec^2\\theta - \\tan^2\\theta = 1$, সেয়ে sec − tan আৰু sec + tan পৰস্পৰ ওলোটা।"),
        B("$\\mathrm{cosec}^2\\theta - \\cot^2\\theta = 1$.", "$\\mathrm{cosec}^2\\theta - \\cot^2\\theta = 1$।"),
        B("sin θ = cos θ only at 45°, where tan θ = 1.", "sin θ = cos θ কেৱল 45°ত, তাত tan θ = 1।"),
    ], [
        lab(f"{p}.s1", B("It never changes", "ই কেতিয়াও নসলনে"), B("Grow this triangle and watch sin and cos. Then square each and add: $\\frac{9}{25} + \\frac{16}{25}$.", "ত্ৰিভুজটো ডাঙৰ কৰি sin আৰু cos চোৱা। প্ৰতিটো বৰ্গ কৰি যোগ কৰা: $\\frac{9}{25} + \\frac{16}{25}$।"), {"kind": "triangle", "triple": [3, 4, 5], "k": 1, "max": 4}, [
            task(B("Make it three times bigger.", "তিনিগুণ ডাঙৰ কৰা।"), {"k": 3}, B("Sides change, ratios do not. The squares still add to 1 because of Pythagoras.", "বাহু সলনি হয়, অনুপাত নহয়। পাইথাগোৰাছৰ বাবে বৰ্গৰ যোগফল 1 থাকে।")),
        ]),
        lab(f"{p}.s2", B("Where sine meets cosine", "য'ত ছাইন আৰু কছাইন লগ হয়"), B("Turn the arm. Sine is its height and cosine its reach.", "বাহুটো ঘূৰোৱা। ছাইন উচ্চতা, কছাইন বিস্তাৰ।"), {"kind": "quarter", "deg": 0}, [
            task(B("Stop at 45°.", "45°ত ৰখা।"), {"deg": 45}, B("Height equals reach, so sin θ = cos θ and tan θ = 1. No other angle in the quarter does this.", "উচ্চতা বিস্তাৰৰ সমান, সেয়ে sin θ = cos θ, tan θ = 1। এই চতুৰ্থাংশত আন কোনো কোণে এনে নকৰে।")),
        ]),
        solve(f"{p}.q1", "tr-ident", lambda k: {"q": B(f"Find ${k}\\sec^2 A - {k}\\tan^2 A$", f"${k}\\sec^2 A - {k}\\tan^2 A$ উলিওৱা"), "answer": str(k), "why": B(f"Take out {k}. The bracket is 1.", f"{k} উলিয়াই লোৱা। বন্ধনীটো 1।")}, [(8,), (7,), (4,)], hints=[B("Common factor first.", "প্ৰথমে উমৈহতীয়া গুণক।")]),
        match(f"{p}.q2", "tr-ident", B("Match each expression to its value", "প্ৰতিটো ৰাশিক মানৰ সৈতে মিলোৱা"), [
            [B("$1 - \\sin^2\\theta$", "$1 - \\sin^2\\theta$"), B("$\\cos^2\\theta$", "$\\cos^2\\theta$")], [B("$1 + \\tan^2\\theta$", "$1 + \\tan^2\\theta$"), B("$\\sec^2\\theta$", "$\\sec^2\\theta$")], [B("$1 + \\cot^2\\theta$", "$1 + \\cot^2\\theta$"), B("$\\mathrm{cosec}^2\\theta$", "$\\mathrm{cosec}^2\\theta$")], [B("$\\sec^2\\theta - \\tan^2\\theta$", "$\\sec^2\\theta - \\tan^2\\theta$"), B("1", "1")],
        ], B("All three come from one Pythagoras line.", "তিনিওটা একে পাইথাগোৰাছৰ পৰা আহে।")),
        solve(f"{p}.q3", "tr-ident", lambda a, b: {"q": B(f"If $\\sec\\theta - \\tan\\theta = {fr(a, b)}$, find $\\sec\\theta + \\tan\\theta$.", f"$\\sec\\theta - \\tan\\theta = {fr(a, b)}$ হ'লে $\\sec\\theta + \\tan\\theta$ উলিওৱা।"), "answer": num(F(b, a)), "why": B("Their product is $\\sec^2\\theta - \\tan^2\\theta = 1$, so flip it.", "পূৰণফল $\\sec^2\\theta - \\tan^2\\theta = 1$, সেয়ে ওলোটোৱা।"), "traps": [{"ans": num(F(a, b)), "tag": "m-trig-flip", "why": B("The product is 1, so the second is the flip of the first.", "পূৰণফল 1, সেয়ে দ্বিতীয়টো প্ৰথমটোৰ ওলোটা।")}]}, [(1, 7), (1, 3), (2, 9)], hints=[B("Think $(a - b)(a + b)$.", "$(a - b)(a + b)$ ভাবা।")]),
        tf(f"{p}.q4", "tr-ident", B("If $\\tan\\theta + \\cot\\theta = 2$, then $\\tan\\theta = 1$.", "$\\tan\\theta + \\cot\\theta = 2$ হ'লে $\\tan\\theta = 1$।"), True, B("A positive number and its flip add to 2 only when the number is 1.", "ধনাত্মক সংখ্যা আৰু ওলোটাৰ যোগফল 2 হয় কেৱল সংখ্যাটো 1 হ'লে।")),
        stepwise(f"{p}.q5", "tr-ident", lambda eq, tan_, deg, val, w1, w2: {"q": B(f"If ${eq}$, find $\\sec\\theta + \\mathrm{{cosec}}\\,\\theta$.", f"${eq}$ হ'লে $\\sec\\theta + \\mathrm{{cosec}}\\,\\theta$ উলিওৱা।"), "parts": [
            part(B("tan θ?", "tan θ?"), t(f"${tan_}$"), [t("$2$"), t("$0$")], B("Divide through by cos θ.", "cos θৰে হৰণ কৰা।"), sid=eq),
            part(B("θ?", "θ?"), t(f"{deg}°"), [t(f"{deg + 15}°"), t("90°")], B("Read it from the table.", "তালিকাৰ পৰা পঢ়া।"), sid=eq),
            part(B("Value?", "মান?"), t(f"${val}$"), [t(f"${w1}$"), t(f"${w2}$")], B("sec and cosec are flips of cos and sin.", "sec আৰু cosec cos আৰু sinৰ ওলোটা।"), sid=eq),
        ], "why": B("A ratio equation points straight to one angle.", "অনুপাতৰ সমীকৰণে এটা কোণলৈ পোনে পোনে নিয়ে।")}, [("\\sin\\theta - \\cos\\theta = 0", "1", 45, "2\\sqrt{2}", "\\sqrt{2}", "2"), ("\\sqrt{3}\\sin\\theta - \\cos\\theta = 0", "\\frac{1}{\\sqrt{3}}", 30, "2 + \\frac{2}{\\sqrt{3}}", "2\\sqrt{3}", "\\frac{4}{\\sqrt{3}}"), ("\\sin\\theta - \\sqrt{3}\\cos\\theta = 0", "\\sqrt{3}", 60, "2 + \\frac{2}{\\sqrt{3}}", "2\\sqrt{3}", "\\frac{4}{\\sqrt{3}}")]),
        stepwise(f"{p}.q6", "tr-ratio", lambda a, b: {"q": B(f"If $\\tan\\theta = {fr(a, b)}$, find $\\cos\\theta$.", f"$\\tan\\theta = {fr(a, b)}$ হ'লে $\\cos\\theta$ উলিওৱা।"), "parts": [
            part(B("Hypotenuse?", "অতিভুজ?"), t(f"$\\sqrt{{{a * a + b * b}}}$"), [t(f"$\\sqrt{{{b * b - a * a}}}$"), t(str(a + b))], B("Pythagoras on sides of the tan fraction.", "tan ভগ্নাংশৰ বাহুত পাইথাগোৰাছ।"), sid=str(a * 10 + b)),
            part(B("cos θ?", "cos θ?"), t(f"$\\frac{{{b}}}{{\\sqrt{{{a * a + b * b}}}}}$"), [t(f"$\\frac{{{a}}}{{\\sqrt{{{a * a + b * b}}}}}$"), t(f"${fr(b, a)}$")], B("Adjacent over hypotenuse.", "কাষৰ বাহু ভাগ অতিভুজ।"), tag="m-trig-swap", sid=str(a * 10 + b)),
        ], "why": B("The hypotenuse need not be a whole number.", "অতিভুজ পূৰ্ণ সংখ্যা নহ'বও পাৰে।")}, [(3, 7), (2, 3), (1, 4)]),
        solve(f"{p}.q7", "tr-ident", lambda x: {"q": B(f"If $\\tan A = {num(x) if x.denominator == 1 else fr(x.numerator, x.denominator)}$, find $\\frac{{1 + \\tan^2 A}}{{1 + \\cot^2 A}}$.", f"$\\tan A = {num(x) if x.denominator == 1 else fr(x.numerator, x.denominator)}$ হ'লে $\\frac{{1 + \\tan^2 A}}{{1 + \\cot^2 A}}$ উলিওৱা।"), "answer": num(x * x), "why": B("$\\frac{\\sec^2 A}{\\mathrm{cosec}^2 A} = \\tan^2 A$.", "$\\frac{\\sec^2 A}{\\mathrm{cosec}^2 A} = \\tan^2 A$।")}, [(F(2),), (F(3),), (F(1, 2),)]),
    ])


def triangle_kinds():
    p = "m15.x"
    return unit("u5", B("Triangle names and outer angles", "ত্ৰিভুজৰ নাম আৰু বাহিৰৰ কোণ"), "star", [
        B("Angles name a triangle: acute, right or obtuse.", "কোণে ত্ৰিভুজৰ নাম দিয়ে: সূক্ষ্মকোণী, সমকোণী বা স্থূলকোণী।"),
        B("Sides name it too: equilateral, isosceles or scalene.", "বাহুৱেও নাম দিয়ে: সমবাহু, সমদ্বিবাহু বা বিষমবাহু।"),
        B("An outer angle equals the two far inner angles added.", "বাহিৰৰ কোণ দূৰৰ ভিতৰৰ দুটা কোণৰ যোগফলৰ সমান।"),
        B("In a ratio of angles, the parts together make 180°.", "কোণৰ অনুপাতত সকলো ভাগ মিলি 180° হয়।"),
    ], [
        lab(f"{p}.s1", B("The outside tells on the inside", "বাহিৰে ভিতৰৰ কথা কয়"), B("One side runs on past the corner in gold. Move the two blue angles and watch the gold one.", "এটা বাহু চুককৈ সোণালীকৈ আগবাঢ়ে। নীলা কোণ দুটা লৰচৰ কৰি সোণালীটো চোৱা।"), {"kind": "exterior", "a": 50, "b": 60}, [
            task(B("Set A to 80°.", "A 80° কৰা।"), {"a": 80}, B("The gold angle follows: 80 + 60 = 140°. It always equals the two far angles added.", "সোণালী কোণে অনুসৰণ কৰে: 80 + 60 = 140°। ই সদায় দূৰৰ দুটাৰ যোগফল।")),
        ]),
        lab(f"{p}.s2", B("Every triangle has two names", "প্ৰতিটো ত্ৰিভুজৰ দুটা নাম"), B("The reading names the triangle by its biggest angle and by its equal sides.", "ডাঙৰ কোণ আৰু সমান বাহুৰ পৰা ত্ৰিভুজটোৰ নাম ওলায়।"), {"kind": "exterior", "a": 50, "b": 60}, [
            task(B("Make all three angles 60°.", "তিনিওটা কোণ 60° কৰা।"), {"a": 60, "b": 60}, B("Equal angles mean equal sides: acute and equilateral.", "সমান কোণ মানে সমান বাহু: সূক্ষ্মকোণী আৰু সমবাহু।")),
            task(B("Now set A = 90° and B = 45°.", "এতিয়া A = 90° আৰু B = 45° কৰা।"), {"a": 90, "b": 45}, B("A right angle with two equal angles: right and isosceles.", "সমকোণ আৰু দুটা সমান কোণ: সমকোণী আৰু সমদ্বিবাহু।")),
        ]),
        explore(f"{p}.q1", "g-types", lambda c: {"q": B(f"Set A and B so that the third angle is {c}°.", f"A আৰু B এনেকৈ সলোৱা যাতে তৃতীয় কোণ {c}° হয়।"), "widget": {"kind": "exterior", "a": 30, "b": 40}, "target": c, "answerText": B(f"The third angle is {c}°", f"তৃতীয় কোণ {c}°"), "why": B(f"A + B must be {180 - c}°, the outer angle.", f"A + B {180 - c}° হ'ব লাগিব, বাহিৰৰ কোণটো।")}, [(70,), (50,), (90,)]),
        solve(f"{p}.q2", "g-types", lambda o, a: {"q": B(f"An outer angle of a triangle is {o}° and one far inner angle is {a}°. Find the other far inner angle.", f"ত্ৰিভুজৰ বাহিৰৰ কোণ {o}° আৰু দূৰৰ এটা ভিতৰৰ কোণ {a}°। আনটো উলিওৱা।"), "answer": str(o - a), "suffix": B("°", "°"), "why": B(f"The outer angle is the two far angles added: {o} − {a}.", f"বাহিৰৰ কোণ দূৰৰ দুটাৰ যোগফল: {o} − {a}।"), "traps": [{"ans": str(180 - o), "tag": "m-outer-next", "why": B("That is the angle next to the outer one. The question asks for the far one.", "সেয়া বাহিৰৰ কোণৰ কাষৰটো। প্ৰশ্নই দূৰৰটো সুধিছে।")}]}, [(110, 30), (125, 60), (130, 45)]),
        solve(f"{p}.q3", "g-types", lambda a, b, c: {"q": B(f"The angles of a triangle are in the ratio {a} : {b} : {c}. Find the largest.", f"ত্ৰিভুজৰ কোণবোৰৰ অনুপাত {a} : {b} : {c}। ডাঙৰটো উলিওৱা।"), "answer": str(ex(180 * max(a, b, c), a + b + c)), "suffix": B("°", "°"), "why": B(f"{a + b + c} parts make 180°, so one part is {ex(180, a + b + c)}°.", f"{a + b + c} ভাগ 180°, এটা ভাগ {ex(180, a + b + c)}°।"), "traps": [{"ans": str(ex(360 * max(a, b, c), a + b + c)), "tag": "m-angle-sum", "why": B("A triangle's angles add to 180°.", "ত্ৰিভুজৰ কোণৰ যোগফল 180°।")}]}, [(2, 3, 4), (1, 2, 3), (3, 5, 10)]),
        solve(f"{p}.q4", "g-types", lambda q_, r: {"q": B(f"In triangle PQR, $P = \\frac{{Q}}{{{q_}}} = \\frac{{R}}{{{r}}}$. Find R.", f"PQR ত্ৰিভুজত $P = \\frac{{Q}}{{{q_}}} = \\frac{{R}}{{{r}}}$। R উলিওৱা।"), "answer": str(ex(180 * r, 1 + q_ + r)), "suffix": B("°", "°"), "why": B(f"The angles are in the ratio 1 : {q_} : {r}.", f"কোণৰ অনুপাত 1 : {q_} : {r}।")}, [(2, 3), (2, 6), (3, 5)], hints=[B("Call P one part.", "Pক এটা ভাগ ধৰা।")]),
        stepwise(f"{p}.q5", "g-types", lambda per: {"q": B(f"An equilateral triangle has perimeter {per} cm. Find its area.", f"সমবাহু ত্ৰিভুজৰ পৰিসীমা {per} ছেমি। কালি উলিওৱা।"), "parts": [
            part(B("Side?", "বাহু?"), t(f"{ex(per, 3)} cm"), [t(f"{ex(per, 2)} cm"), t(f"{per} cm")], B("Three equal sides.", "তিনিটা সমান বাহু।"), sid=str(per)),
            part(B("Area formula?", "কালিৰ সূত্ৰ?"), t("$\\frac{\\sqrt{3}}{4}a^2$"), [t("$\\frac{1}{2}a^2$"), t("$\\frac{\\sqrt{3}}{2}a$")], B("It comes from half a base times the height.", "ই আধা ভূমি × উচ্চতাৰ পৰা আহে।"), sid=str(per)),
            part(B("Area?", "কালি?"), t(f"${ex(ex(per, 3) ** 2, 4)}\\sqrt{{3}}$"), [t(f"${ex(per, 3) ** 2}\\sqrt{{3}}$"), t(f"${ex(ex(per, 3) ** 2, 2)}\\sqrt{{3}}$")], B("Put the side in.", "বাহু বহুওৱা।"), sid=str(per)),
        ], "why": B("Find the side, then the formula does the rest.", "বাহু উলিয়ালে বাকীখিনি সূত্ৰই কৰে।")}, [(30,), (12,), (18 * 2,)]),
        tf(f"{p}.q6", "g-types", B("A triangle can have two right angles.", "ত্ৰিভুজৰ দুটা সমকোণ থাকিব পাৰে।"), False, B("Two right angles already use 180°, leaving nothing for the third.", "দুটা সমকোণেই 180° হৈ যায়, তৃতীয়টোৰ বাবে একো নাথাকে।")),
        match(f"{p}.q7", "g-types", B("Match each triangle's angles to its name", "প্ৰতিটো ত্ৰিভুজৰ কোণক নামৰ সৈতে মিলোৱা"), [
            [t("60°, 60°, 60°"), B("Equilateral", "সমবাহু")], [t("90°, 45°, 45°"), B("Right isosceles", "সমকোণী সমদ্বিবাহু")], [t("120°, 40°, 20°"), B("Obtuse scalene", "স্থূলকোণী বিষমবাহু")], [t("70°, 70°, 40°"), B("Acute isosceles", "সূক্ষ্মকোণী সমদ্বিবাহু")],
        ], B("Check the biggest angle, then look for equal ones.", "ডাঙৰ কোণ চোৱা, তাৰ পিছত সমান কোণ।")),
    ])


def similar():
    p = "m15.y"
    return unit("u6", B("Same shape, new size", "একে আকৃতি, নতুন আকাৰ"), "star", [
        B("Similar triangles have equal angles and sides in one ratio.", "সদৃশ ত্ৰিভুজৰ কোণ সমান, বাহু একে অনুপাতত।"),
        B("Their areas are in the square of that ratio.", "কালি সেই অনুপাতৰ বৰ্গত থাকে।"),
        B("An isosceles right triangle has sides a, a and $a\\sqrt{2}$.", "সমকোণী সমদ্বিবাহু ত্ৰিভুজৰ বাহু a, a আৰু $a\\sqrt{2}$।"),
        B("A side ratio with a perimeter gives the real sides.", "বাহুৰ অনুপাত আৰু পৰিসীমাই আচল বাহু দিয়ে।"),
    ], [
        lab(f"{p}.s1", B("Blow it up", "ডাঙৰ কৰা"), B("Stretch this triangle evenly. The angles stay; only the size changes.", "ত্ৰিভুজটো সমানে টানা। কোণ থাকে; আকাৰহে সলনি হয়।"), {"kind": "triangle", "triple": [3, 4, 5], "k": 1, "max": 4}, [
            task(B("Double it.", "দুগুণ কৰা।"), {"k": 2}, B("Sides double, so 6, 8, 10. But the area goes from 6 to 24, four times.", "বাহু দুগুণ: 6, 8, 10। কিন্তু কালি 6ৰ পৰা 24, চাৰিগুণ।")),
        ]),
        diagram(f"{p}.s2", B("The half-square triangle", "আধা বৰ্গৰ ত্ৰিভুজ"), [B("Cut a square along its diagonal to get two isosceles right triangles.", "বৰ্গ এটা কৰ্ণেৰে কাটিলে দুটা সমকোণী সমদ্বিবাহু ত্ৰিভুজ হয়।"), B("So the long side is the square's diagonal.", "সেয়ে দীঘল বাহুটো বৰ্গৰ কৰ্ণ।")], "flow", [B("Legs a, a", "বাহু a, a"), B("Long side $a\\sqrt{2}$", "দীঘল বাহু $a\\sqrt{2}$"), B("Area $\\frac{a^2}{2}$", "কালি $\\frac{a^2}{2}$")]),
        solve(f"{p}.q1", "g-similar", lambda a, b: {"q": B(f"Two similar triangles have sides in the ratio {a} : {b}. Write the ratio of their areas as a fraction.", f"দুটা সদৃশ ত্ৰিভুজৰ বাহুৰ অনুপাত {a} : {b}। কালিৰ অনুপাত ভগ্নাংশত লিখা।"), "answer": num(F(a * a, b * b)), "why": B("Square the side ratio.", "বাহুৰ অনুপাত বৰ্গ কৰা।"), "traps": [{"ans": num(F(a, b)), "tag": "m-scale-linear", "why": B("Area grows in two directions, so square the ratio.", "কালি দুই দিশে বাঢ়ে, সেয়ে অনুপাত বৰ্গ কৰা।")}]}, [(3, 5), (2, 3), (4, 7)]),
        solve(f"{p}.q2", "g-similar", lambda s_, l_, o: {"q": B(f"In similar triangles, a side of {s_} cm matches a side of {l_} cm. Another side of the smaller one is {o} cm. Find the matching larger side.", f"সদৃশ ত্ৰিভুজত {s_} ছেমি বাহু {l_} ছেমি বাহুৰ অনুৰূপ। সৰুটোৰ আন এটা বাহু {o} ছেমি। ডাঙৰটোৰ অনুৰূপ বাহু উলিওৱা।"), "answer": str(ex(o * l_, s_)), "suffix": B("cm", "ছেমি"), "why": B(f"Every side scales by ${fr(l_, s_)}$.", f"প্ৰতিটো বাহু ${fr(l_, s_)}$গুণ হয়।"), "traps": [{"ans": str(o + l_ - s_), "tag": "m-ratio-add", "why": B("Sides scale by multiplying, not by adding the same amount.", "বাহু পূৰণেৰে বাঢ়ে, একে সংখ্যা যোগেৰে নহয়।")}]}, [(6, 10, 9), (4, 12, 5), (8, 12, 10)]),
        solve(f"{p}.q3", "g-similar", lambda a, b: {"q": B(f"Two similar triangles have areas in the ratio {a * a} : {b * b}. Write the ratio of their sides as a fraction.", f"দুটা সদৃশ ত্ৰিভুজৰ কালিৰ অনুপাত {a * a} : {b * b}। বাহুৰ অনুপাত ভগ্নাংশত লিখা।"), "answer": num(F(a, b)), "why": B("Take the square root.", "বৰ্গমূল লোৱা।")}, [(2, 3), (5, 7), (3, 4)]),
        stepwise(f"{p}.q4", "g-similar", lambda a: {"q": B(f"An isosceles right triangle has hypotenuse ${a}\\sqrt{{2}}$ cm. Find its area.", f"সমকোণী সমদ্বিবাহু ত্ৰিভুজৰ অতিভুজ ${a}\\sqrt{{2}}$ ছেমি। কালি উলিওৱা।"), "parts": [
            part(B("Each equal side?", "প্ৰতিটো সমান বাহু?"), t(f"{a} cm"), [t(f"{a * 2} cm"), t(f"${a}\\sqrt{{2}}$ cm")], B("Long side is a√2.", "দীঘল বাহু a√2।"), sid=str(a)),
            part(B("Area?", "কালি?"), t(f"{ex(a * a, 2)} sq cm"), [t(f"{a * a} sq cm"), t(f"{a * 2} sq cm")], B("Half of side × side.", "বাহু × বাহুৰ আধা।"), tag="m-tri-area", sid=str(a)),
        ], "why": B("The two equal sides are base and height.", "দুটা সমান বাহুৱেই ভূমি আৰু উচ্চতা।")}, [(10,), (6,), (8,)]),
        solve(f"{p}.q5", "g-similar", lambda per: {"q": B(f"A triangle has sides in the ratio 3 : 4 : 5 and perimeter {per} cm. Find its area.", f"ত্ৰিভুজৰ বাহুৰ অনুপাত 3 : 4 : 5, পৰিসীমা {per} ছেমি। কালি উলিওৱা।"), "answer": str(6 * ex(per, 12) ** 2), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B("3-4-5 has a right angle, so 3 and 4 are base and height.", "3-4-5ত সমকোণ আছে, সেয়ে 3 আৰু 4 ভূমি আৰু উচ্চতা।")}, [(36,), (24,), (48,)], hints=[B("One part is the perimeter ÷ 12.", "এটা ভাগ = পৰিসীমা ÷ 12।")]),
        tf(f"{p}.q6", "g-similar", B("Doubling every side of a triangle doubles its area.", "ত্ৰিভুজৰ প্ৰতিটো বাহু দুগুণ কৰিলে কালি দুগুণ হয়।"), False, B("It becomes four times the area.", "কালি চাৰিগুণ হয়।"), ("m-scale-linear", B("Area scales by the square.", "কালি বৰ্গ হিচাপে বাঢ়ে।"))),
        match(f"{p}.q7", "g-similar", B("Match each side ratio to its area ratio", "প্ৰতিটো বাহুৰ অনুপাতক কালিৰ অনুপাতৰ সৈতে মিলোৱা"), [
            [t("1 : 2"), t("1 : 4")], [t("2 : 3"), t("4 : 9")], [t("3 : 4"), t("9 : 16")], [t("3 : 5"), t("9 : 25")],
        ], B("Square both sides of the ratio.", "অনুপাতৰ দুয়োফাল বৰ্গ কৰা।")),
    ])


def rect_clues():
    p = "m15.z"
    return unit("u7", B("Rectangles from clues", "সূত্ৰৰ পৰা আয়ত"), "star", [
        B("Half the perimeter is length + breadth.", "পৰিসীমাৰ আধা = দৈৰ্ঘ্য + প্ৰস্থ।"),
        B("The diagonal is the long side of a right triangle.", "কৰ্ণ সমকোণী ত্ৰিভুজৰ দীঘল বাহু।"),
        B("$(l + b)^2 = d^2 + 2 \\times$ area links the clues.", "$(l + b)^2 = d^2 + 2 \\times$ কালিয়ে সূত্ৰবোৰ জোৰে।"),
        B("For a fixed perimeter, the square has the largest area.", "নিৰ্দিষ্ট পৰিসীমাত বৰ্গৰ কালি আটাইতকৈ বেছি।"),
    ], [
        lab(f"{p}.s1", B("One fence, many fields", "এটা বেৰ, বহু পথাৰ"), B("This fence is 28 m long. Change the length of the field; the breadth must give way.", "এই বেৰ 28 মিটাৰ দীঘল। পথাৰৰ দৈৰ্ঘ্য সলোৱা; প্ৰস্থই সেই অনুসৰি সলনি হ'ব।"), {"kind": "fence", "p": 28, "l": 12}, [
            task(B("Make the length 8.", "দৈৰ্ঘ্য 8 কৰা।"), {"l": 8}, B("8 by 6 has area 48 and diagonal 10. Same fence, bigger field than 12 by 2.", "8 বাই 6ৰ কালি 48, কৰ্ণ 10। একে বেৰ, 12 বাই 2তকৈ ডাঙৰ পথাৰ।")),
            task(B("Now make it square.", "এতিয়া বৰ্গ কৰা।"), {"l": 7}, B("7 by 7 has area 49, the most this fence can hold.", "7 বাই 7ৰ কালি 49, এই বেৰে ধৰিব পৰা সৰ্বাধিক।")),
        ]),
        diagram(f"{p}.s2", B("Two clues are enough", "দুটা সূত্ৰই যথেষ্ট"), [B("Diagonal and area look unrelated, but both sit inside one square of the sum.", "কৰ্ণ আৰু কালি সম্পৰ্কহীন যেন লাগে, কিন্তু দুয়ো যোগফলৰ বৰ্গত থাকে।"), B("With diagonal 13 and area 60: $13^2 + 120 = 289$, so l + b = 17.", "কৰ্ণ 13, কালি 60 হ'লে: $13^2 + 120 = 289$, সেয়ে l + b = 17।")], "flow", [B("$d^2 + 2 \\times$ area", "$d^2 + 2 \\times$ কালি"), B("Root gives l + b", "মূলে l + b দিয়ে"), B("Double for perimeter", "দুগুণ কৰিলে পৰিসীমা")]),
        explore(f"{p}.q1", "g-rect", lambda per, l_, b_: {"q": B(f"A rectangle has perimeter {per} m and area {l_ * b_} sq m. Slide to find its length, the longer side.", f"আয়তৰ পৰিসীমা {per} মিটাৰ, কালি {l_ * b_} বৰ্গ মিটাৰ। টানি ইয়াৰ দৈৰ্ঘ্য, দীঘল বাহুটো, উলিওৱা।"), "widget": {"kind": "fence", "p": per, "l": ex(per, 2) - 1}, "target": l_, "answerText": B(f"Length {l_} m", f"দৈৰ্ঘ্য {l_} মিটাৰ"), "why": B(f"{l_} × {b_} = {l_ * b_}.", f"{l_} × {b_} = {l_ * b_}।")}, [(34, 12, 5), (28, 8, 6), (46, 15, 8)]),
        solve(f"{p}.q2", "g-rect", lambda l_, b_: {"q": B(f"Find the diagonal of a rectangle {l_} cm by {b_} cm.", f"{l_} ছেমি বাই {b_} ছেমি আয়তৰ কৰ্ণ উলিওৱা।"), "answer": str(isqrt(l_ * l_ + b_ * b_)), "suffix": B("cm", "ছেমি"), "why": B(f"$\\sqrt{{{l_ * l_} + {b_ * b_}}}$.", f"$\\sqrt{{{l_ * l_} + {b_ * b_}}}$।"), "traps": [{"ans": str(l_ + b_), "tag": "m-root-add", "why": B("Square, add, then take the root.", "বৰ্গ কৰি যোগ কৰি মূল লোৱা।")}]}, [(8, 15), (12, 5), (24, 7), (40, 9)]),
        stepwise(f"{p}.q3", "g-rect", lambda a, b, per: {"q": B(f"A rectangle's sides are in the ratio {a} : {b} and its perimeter is {per} m. Find its area.", f"আয়তৰ বাহুৰ অনুপাত {a} : {b}, পৰিসীমা {per} মিটাৰ। কালি উলিওৱা।"), "parts": [
            part(B("Length + breadth?", "দৈৰ্ঘ্য + প্ৰস্থ?"), t(ex(per, 2)), [t(per), t(per * 2)], B("Half the perimeter.", "পৰিসীমাৰ আধা।"), tag="m-perim-half", sid=str(per)),
            part(B("Sides?", "বাহু?"), t(f"{a * ex(per, 2 * (a + b))} and {b * ex(per, 2 * (a + b))}"), [t(f"{a} and {b}"), t(f"{a * ex(per, 2 * (a + b)) * 2} and {b * ex(per, 2 * (a + b)) * 2}")], B(f"Share in the ratio {a} : {b}.", f"{a} : {b} অনুপাতত ভাগ কৰা।"), sid=str(per)),
            part(B("Area?", "কালি?"), t(a * b * ex(per, 2 * (a + b)) ** 2), [t(a * b * ex(per, 2 * (a + b))), t(per)], B("Length × breadth.", "দৈৰ্ঘ্য × প্ৰস্থ।"), sid=str(per)),
        ], "why": B("A ratio needs one real total to become real sides.", "অনুপাতক আচল বাহু কৰিবলৈ এটা আচল মুঠ লাগে।")}, [(3, 2, 50), (4, 3, 56), (5, 2, 84)]),
        stepwise(f"{p}.q4", "g-rect", lambda d, a: {"q": B(f"A rectangle has diagonal {d} m and area {a} sq m. Find its perimeter.", f"আয়তৰ কৰ্ণ {d} মিটাৰ, কালি {a} বৰ্গ মিটাৰ। পৰিসীমা উলিওৱা।"), "parts": [
            part(B("$(l + b)^2$?", "$(l + b)^2$?"), t(d * d + 2 * a), [t(d * d + a), t(d * d)], B("$d^2 + 2 \\times$ area.", "$d^2 + 2 \\times$ কালি।"), sid=str(d)),
            part(B("l + b?", "l + b?"), t(isqrt(d * d + 2 * a)), [t(d), t(isqrt(d * d + 2 * a) * 2)], B("Take the root.", "মূল লোৱা।"), sid=str(d)),
            part(B("Perimeter?", "পৰিসীমা?"), t(2 * isqrt(d * d + 2 * a)), [t(isqrt(d * d + 2 * a)), t(4 * d)], B("Double it.", "দুগুণ কৰা।"), tag="m-perim-half", sid=str(d)),
        ], "why": B("You never needed the sides themselves.", "বাহু নিজে কেতিয়াও নালাগিল।")}, [(13, 60), (10, 48), (17, 120)]),
        solve(f"{p}.q5", "g-rect", lambda l_, b_: {"q": B(f"A square and a {l_} by {b_} rectangle have equal perimeters. By how much is the square's area bigger?", f"এটা বৰ্গ আৰু {l_} বাই {b_} আয়তৰ পৰিসীমা সমান। বৰ্গৰ কালি কিমান বেছি?"), "answer": str(ex(l_ + b_, 2) ** 2 - l_ * b_), "why": B(f"The square's side is {ex(l_ + b_, 2)}.", f"বৰ্গৰ বাহু {ex(l_ + b_, 2)}।")}, [(18, 12), (20, 10), (16, 10)]),
        tf(f"{p}.q6", "g-rect", B("Two rectangles with the same perimeter have the same area.", "একে পৰিসীমাৰ দুটা আয়তৰ কালি একে।"), False, B("12 by 2 and 7 by 7 share a perimeter but have areas 24 and 49.", "12 বাই 2 আৰু 7 বাই 7ৰ পৰিসীমা একে, কালি 24 আৰু 49।")),
        match(f"{p}.q7", "g-rect", B("Match each square's side to its diagonal", "প্ৰতিটো বৰ্গৰ বাহুক কৰ্ণৰ সৈতে মিলোৱা"), [
            [t("5"), t("$5\\sqrt{2}$")], [t("$\\sqrt{2}$"), t("2")], [t("$3\\sqrt{2}$"), t("6")], [t("10"), t("$10\\sqrt{2}$")],
        ], B("Diagonal = side × √2.", "কৰ্ণ = বাহু × √2।")),
    ])


def circle_parts():
    p = "m15.w"
    return unit("u8", B("Chords, tangents, sectors", "জ্যা, স্পৰ্শক, বৃত্তকলা"), "star", [
        B("A tangent meets the radius at exactly 90°.", "স্পৰ্শক ব্যাসাৰ্ধক ঠিক 90°ত লগ পায়।"),
        B("A line from the centre at right angles halves a chord.", "কেন্দ্ৰৰ পৰা লম্ব ৰেখাই জ্যা আধা কৰে।"),
        B("A sector is a fraction of the circle: angle ÷ 360.", "বৃত্তকলা বৃত্তৰ ভগ্নাংশ: কোণ ÷ 360।"),
        B("Two tangents and two radii make a four-sided shape with 360°.", "দুটা স্পৰ্শক আৰু দুটা ব্যাসাৰ্ধে 360°ৰ চতুৰ্ভুজ বনায়।"),
    ], [
        lab(f"{p}.s1", B("A line that only touches", "কেৱল চুই যোৱা ৰেখা"), B("The gold line touches the circle once. Where it touches, it makes a right angle with the radius.", "সোণালী ৰেখাই বৃত্তক এবাৰহে চুয়ে। চোৱা ঠাইত ই ব্যাসাৰ্ধৰ সৈতে সমকোণ কৰে।"), {"kind": "tangent", "r": 5, "pq": 3, "max": 24}, [
            task(B("Slide Q out until the tangent is 12.", "স্পৰ্শক 12 নোহোৱালৈ Q টানা।"), {"pq": 12}, B("Radius 5 and tangent 12 are the short sides of a right triangle, so OQ = 13.", "ব্যাসাৰ্ধ 5 আৰু স্পৰ্শক 12 সমকোণী ত্ৰিভুজৰ সৰু বাহু, সেয়ে OQ = 13।")),
        ]),
        diagram(f"{p}.s2", B("Half a chord", "আধা জ্যা"), [B("Drop a line from the centre to a chord at right angles. It lands exactly on the middle.", "কেন্দ্ৰৰ পৰা জ্যালৈ লম্ব টানা। ই ঠিক মাজত পৰে।"), B("The radius, that line and half the chord make a right triangle.", "ব্যাসাৰ্ধ, সেই ৰেখা আৰু আধা জ্যাই সমকোণী ত্ৰিভুজ বনায়।")], "flow", [B("Radius 13", "ব্যাসাৰ্ধ 13"), B("Distance 5", "দূৰত্ব 5"), B("Half chord 12, chord 24", "আধা জ্যা 12, জ্যা 24")]),
        explore(f"{p}.q1", "g-parts", lambda r, oq, pq: {"q": B(f"A circle has radius {r}. A point Q is {oq} from the centre. Slide to find the tangent from Q.", f"বৃত্তৰ ব্যাসাৰ্ধ {r}। Q বিন্দু কেন্দ্ৰৰ পৰা {oq} দূৰত। টানি Qৰ পৰা স্পৰ্শকৰ দৈৰ্ঘ্য উলিওৱা।"), "widget": {"kind": "tangent", "r": r, "pq": 1, "max": 24}, "target": pq, "answerText": B(f"Tangent {pq}", f"স্পৰ্শক {pq}"), "why": B(f"${oq}^2 - {r}^2 = {pq}^2$.", f"${oq}^2 - {r}^2 = {pq}^2$।")}, [(5, 13, 12), (8, 17, 15), (7, 25, 24)]),
        solve(f"{p}.q2", "g-parts", lambda r, d: {"q": B(f"A chord is {d} cm from the centre of a circle of radius {r} cm. Find its length.", f"{r} ছেমি ব্যাসাৰ্ধৰ বৃত্তৰ কেন্দ্ৰৰ পৰা এটা জ্যা {d} ছেমি দূৰত। ইয়াৰ দৈৰ্ঘ্য উলিওৱা।"), "answer": str(2 * isqrt(r * r - d * d)), "suffix": B("cm", "ছেমি"), "why": B(f"Half the chord is $\\sqrt{{{r * r} - {d * d}}}$.", f"আধা জ্যা $\\sqrt{{{r * r} - {d * d}}}$।"), "traps": [{"ans": str(isqrt(r * r - d * d)), "tag": "m-chord-half", "why": B("That is half the chord. Double it.", "সেয়া আধা জ্যা। দুগুণ কৰা।")}]}, [(13, 5), (5, 3), (10, 6), (17, 8)]),
        solve(f"{p}.q3", "g-parts", lambda r, a: {"q": B(f"Find the area of a sector of radius {r} cm and angle {a}°. Take π = 22/7.", f"{r} ছেমি ব্যাসাৰ্ধ আৰু {a}° কোণৰ বৃত্তকলাৰ কালি উলিওৱা। π = 22/7 লোৱা।"), "answer": str(pi(r, r, F(a, 360))), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B(f"${fr(a, 360)}$ of the circle's area.", f"বৃত্তৰ কালিৰ ${fr(a, 360)}$ অংশ।")}, [(14, 90), (21, 60), (28, 45)], hints=[B("Angle ÷ 360 is the fraction.", "কোণ ÷ 360 ভগ্নাংশটো।")]),
        solve(f"{p}.q4", "g-parts", lambda r, a: {"q": B(f"Find the arc length of a sector of radius {r} cm and angle {a}°. Take π = 22/7.", f"{r} ছেমি ব্যাসাৰ্ধ আৰু {a}° কোণৰ বৃত্তকলাৰ চাপৰ দৈৰ্ঘ্য উলিওৱা। π = 22/7 লোৱা।"), "answer": str(pi(2, r, F(a, 360))), "suffix": B("cm", "ছেমি"), "why": B("Arc is the same fraction of the circumference.", "চাপ পৰিধিৰ একে ভগ্নাংশ।"), "traps": [{"ans": str(pi(r, r, F(a, 360))), "tag": "m-circle-formula", "why": B("That is area. An arc is a length, from $2\\pi r$.", "সেয়া কালি। চাপ দৈৰ্ঘ্য, $2\\pi r$ৰ পৰা।")}]}, [(21, 120), (14, 90), (42, 60)]),
        solve(f"{p}.q5", "g-parts", lambda x: {"q": B(f"Tangents from P touch a circle with centre O at A and B. Angle APB is {x}°. Find angle AOB.", f"Pৰ পৰা স্পৰ্শকে O কেন্দ্ৰৰ বৃত্তক A আৰু Bত চুয়ে। APB কোণ {x}°। AOB কোণ উলিওৱা।"), "answer": str(180 - x), "suffix": B("°", "°"), "why": B(f"The shape has 360°, with two right angles: 360 − 180 − {x}.", f"আকৃতিত 360°, দুটা সমকোণ: 360 − 180 − {x}।"), "traps": [{"ans": str(360 - x), "tag": "m-tangent-right", "why": B("Each tangent makes 90° with a radius. Take those off too.", "প্ৰতিটো স্পৰ্শকে ব্যাসাৰ্ধৰ সৈতে 90° কৰে। সেইবোৰো বিয়োগ কৰা।")}]}, [(60,), (70,), (45,), (100,)]),
        tf(f"{p}.q6", "g-parts", B("Two tangents drawn from one outside point are equal in length.", "বাহিৰৰ এটা বিন্দুৰ পৰা টনা দুটা স্পৰ্শকৰ দৈৰ্ঘ্য সমান।"), True, B("The two right triangles they form match exactly.", "সিহঁতে বনোৱা দুটা সমকোণী ত্ৰিভুজ হুবহু মিলে।")),
        match(f"{p}.q7", "g-parts", B("Match each sector angle to its share of the circle", "প্ৰতিটো বৃত্তকলাৰ কোণক বৃত্তৰ অংশৰ সৈতে মিলোৱা"), [
            [t("90°"), t("$\\frac{1}{4}$")], [t("60°"), t("$\\frac{1}{6}$")], [t("120°"), t("$\\frac{1}{3}$")], [t("45°"), t("$\\frac{1}{8}$")],
        ], B("Divide by 360.", "360ৰে হৰণ কৰা।")),
    ])


def full_surfaces():
    p = "m16.x"
    return unit("u4", B("Slant, full surface, half spheres", "হেলনীয়া, সম্পূৰ্ণ পৃষ্ঠ, অৰ্ধগোলক"), "star", [
        B("A cone's slant is $l = \\sqrt{r^2 + h^2}$.", "শংকুৰ হেলনীয়া উচ্চতা $l = \\sqrt{r^2 + h^2}$।"),
        B("A cone's curved surface is $\\pi r l$, using slant, not height.", "শংকুৰ বক্ৰ পৃষ্ঠ $\\pi r l$, উচ্চতা নহয়, হেলনীয়া লোৱা।"),
        B("A closed cylinder's whole surface is $2\\pi r(r + h)$.", "বন্ধ চুঙাৰ সম্পূৰ্ণ পৃষ্ঠ $2\\pi r(r + h)$।"),
        B("A hemisphere's volume is $\\frac{2}{3}\\pi r^3$.", "অৰ্ধগোলকৰ আয়তন $\\frac{2}{3}\\pi r^3$।"),
    ], [
        lab(f"{p}.s1", B("Unfold it", "খুলি চোৱা"), B("Any surface is what you would paint. Open a box flat to count it.", "পৃষ্ঠ মানে তুমি ৰং কৰিবলগীয়াখিনি। গণিবলৈ বাকচ খুলি মেলা।"), {"kind": "net", "a": 4}, [
            task(B("Unfold the shape.", "আকৃতিটো খোলা।"), {"open": 1}, B("A cylinder opens the same way: two circles and one rectangle, $2\\pi r^2 + 2\\pi r h$.", "চুঙাও একেদৰে খোল খায়: দুটা বৃত্ত আৰু এটা আয়ত, $2\\pi r^2 + 2\\pi r h$।")),
        ]),
        diagram(f"{p}.s2", B("The slant is hiding", "হেলনীয়া লুকাই আছে"), [B("Slice a cone down the middle. Height, radius and slant form a right triangle.", "শংকু মাজেৰে কাটা। উচ্চতা, ব্যাসাৰ্ধ আৰু হেলনীয়াই সমকোণী ত্ৰিভুজ বনায়।"), B("The surface runs along the slant, so that is the length it needs.", "পৃষ্ঠ হেলনীয়াৰে যায়, সেয়ে সেই দৈৰ্ঘ্যই লাগে।")], "flow", [B("r = 5, h = 12", "r = 5, h = 12"), B("l = 13", "l = 13"), B("Surface = π × 5 × 13", "পৃষ্ঠ = π × 5 × 13")]),
        stepwise(f"{p}.q1", "g-full", lambda r, h, l_: {"q": B(f"A cone has radius {r} cm and height {h} cm. Find its curved surface in terms of π.", f"শংকুৰ ব্যাসাৰ্ধ {r} ছেমি, উচ্চতা {h} ছেমি। বক্ৰ পৃষ্ঠ π-ত উলিওৱা।"), "parts": [
            part(B("Slant?", "হেলনীয়া?"), t(f"{l_} cm"), [t(f"{r + h} cm"), t(f"{h} cm")], B("Pythagoras.", "পাইথাগোৰাছ।"), sid=str(r)),
            part(B("Curved surface?", "বক্ৰ পৃষ্ঠ?"), t(f"{r * l_}π"), [t(f"{r * h}π"), t(f"{r * r + r * l_}π")], B("π × r × slant.", "π × r × হেলনীয়া।"), tag="m-cone-height", sid=str(r)),
        ], "why": B("Slant goes in the surface; height goes in the volume.", "পৃষ্ঠত হেলনীয়া, আয়তনত উচ্চতা।")}, [(5, 12, 13), (3, 4, 5), (8, 15, 17)]),
        stepwise(f"{p}.q2", "g-full", lambda r, h: {"q": B(f"Find the whole surface of a closed cylinder of radius {r} cm and height {h} cm. Take π = 22/7.", f"{r} ছেমি ব্যাসাৰ্ধ আৰু {h} ছেমি উচ্চতাৰ বন্ধ চুঙাৰ সম্পূৰ্ণ পৃষ্ঠ উলিওৱা। π = 22/7 লোৱা।"), "parts": [
            part(B("Curved part?", "বক্ৰ অংশ?"), t(pi(2, r, h)), [t(pi(r, h)), t(pi(r, r, h))], B("$2\\pi r h$.", "$2\\pi r h$।"), sid=str(r)),
            part(B("Two ends?", "দুটা মূৰ?"), t(pi(2, r, r)), [t(pi(r, r)), t(pi(2, r))], B("Two circles.", "দুটা বৃত্ত।"), sid=str(r)),
            part(B("Whole surface?", "সম্পূৰ্ণ পৃষ্ঠ?"), t(pi(2, r, r + h)), [t(pi(2, r, h)), t(pi(r, r + h))], B("Add them.", "যোগ কৰা।"), sid=str(r)),
        ], "why": B("Unfolded, it is one rectangle and two circles.", "খুলিলে এটা আয়ত আৰু দুটা বৃত্ত।")}, [(7, 3), (14, 6), (7, 10)]),
        solve(f"{p}.q3", "g-full", lambda r, h: {"q": B(f"A cylinder of height {h} cm has curved surface {pi(2, r, h)} sq cm. Find its radius. Take π = 22/7.", f"{h} ছেমি উচ্চতাৰ চুঙাৰ বক্ৰ পৃষ্ঠ {pi(2, r, h)} বৰ্গ ছেমি। ব্যাসাৰ্ধ উলিওৱা। π = 22/7 লোৱা।"), "answer": str(r), "suffix": B("cm", "ছেমি"), "why": B("Divide by $2\\pi h$.", "$2\\pi h$ৰে হৰণ কৰা।")}, [(7, 10), (14, 5), (21, 2)]),
        solve(f"{p}.q4", "g-full", lambda r: {"q": B(f"Find the volume of a hemisphere of radius {r} cm. Take π = 22/7.", f"{r} ছেমি ব্যাসাৰ্ধৰ অৰ্ধগোলকৰ আয়তন উলিওৱা। π = 22/7 লোৱা।"), "answer": str(pi(F(2, 3), r, r, r)), "suffix": B("cu cm", "ঘন ছেমি"), "why": B("Half of $\\frac{4}{3}\\pi r^3$.", "$\\frac{4}{3}\\pi r^3$ৰ আধা।"), "traps": [{"ans": str(pi(F(4, 3), r, r, r)), "tag": "m-sphere-hemi", "why": B("That is the whole sphere.", "সেয়া গোটেই গোলক।")}]}, [(21,), (42,), (84,)]),
        solve(f"{p}.q5", "g-full", lambda k: {"q": B(f"A sphere has radius r and a hemisphere has radius {k}r. Write sphere volume ÷ hemisphere volume as a fraction.", f"গোলকৰ ব্যাসাৰ্ধ r, অৰ্ধগোলকৰ ব্যাসাৰ্ধ {k}r। গোলকৰ আয়তন ÷ অৰ্ধগোলকৰ আয়তন ভগ্নাংশত লিখা।"), "answer": num(F(2, k ** 3)), "why": B(f"$\\frac{{4}}{{3}}$ against $\\frac{{2}}{{3}} \\times {k ** 3}$.", f"$\\frac{{4}}{{3}}$ বনাম $\\frac{{2}}{{3}} \\times {k ** 3}$।")}, [(2,), (3,), (4,)]),
        tf(f"{p}.q6", "g-solid", B("One cubic metre is 100 cubic centimetres.", "এক ঘন মিটাৰ 100 ঘন ছেমি।"), False, B("It is 100 × 100 × 100 = 1 000 000.", "ই 100 × 100 × 100 = 1 000 000।"), ("m-litre", B("Each of the three directions has 100 cm.", "তিনিওটা দিশতে 100 ছেমি।"))),
        match(f"{p}.q7", "g-full", B("Double the radius. Match each to how it grows", "ব্যাসাৰ্ধ দুগুণ কৰা। প্ৰতিটোক বৃদ্ধিৰ সৈতে মিলোৱা"), [
            [B("Circumference", "পৰিধি"), B("× 2", "× 2")], [B("Sphere surface", "গোলকৰ পৃষ্ঠ"), B("× 4", "× 4")], [B("Sphere volume", "গোলকৰ আয়তন"), B("× 8", "× 8")], [B("Cylinder volume, same height", "চুঙাৰ আয়তন, একে উচ্চতা"), B("× 4 ", "× 4 ")],
        ], B("Length, area and volume scale by k, k² and k³.", "দৈৰ্ঘ্য, কালি, আয়তন k, k², k³ হিচাপে বাঢ়ে।")),
    ])


def more_extras():
    """Single steps that close the last gaps, each in the unit it belongs to."""
    return {
        1: {},
        3: {"u2": [solve("m3.u2.q6", "f-of", lambda n, left: {"q": B(f"A sum loses ${fr(1, n)}$ of itself and ₹{left} remains. Find the sum.", f"এটা ধনৰ ${fr(1, n)}$ অংশ কমি ₹{left} থাকে। ধন উলিওৱা।"), "answer": str(ex(left * n, n - 1)), "prefix": B("₹", "₹"), "why": B(f"${fr(n - 1, n)}$ of the sum is ₹{left}.", f"ধনৰ ${fr(n - 1, n)}$ অংশ ₹{left}।"), "traps": [{"ans": str(ex(left * (n + 1), n) if left * (n + 1) % n == 0 else left + 1), "tag": "m-frac-of", "why": B("Find what fraction remains, then divide by it.", "কিমান ভগ্নাংশ থাকিল উলিয়াই তাৰে হৰণ কৰা।")}]}, [(5, 40), (6, 75), (8, 70)])]},
        4: {"u1": [solve("m4.u1.q7", "s-bodmas", lambda a, b, c, d, e: {"q": B(f"Work out ${a} + \\{{{b} \\div ({c} - \\overline{{{d} + {e}}})\\}}$", f"${a} + \\{{{b} \\div ({c} - \\overline{{{d} + {e}}})\\}}$ৰ মান উলিওৱা"), "answer": str(a + ex(b, c - d - e)), "why": B(f"The bar is done first: {d} + {e} = {d + e}.", f"ৰেখাৰ তলৰটো আগতে: {d} + {e} = {d + e}।"), "traps": [{"ans": str(a + ex(b, c - d + e)), "tag": "m-bodmas-lr", "why": B("A bar groups like a bracket, so add under it before you subtract.", "ৰেখাই বন্ধনীৰ দৰে গোট কৰে, সেয়ে বিয়োগৰ আগতে তলৰটো যোগ কৰা।")}]}, [(4, 12, 8, 3, 1), (5, 24, 10, 4, 2), (2, 36, 10, 4, 3)], hints=[B("V comes first in VBODMAS: the bar over the numbers.", "VBODMASত V আগত: সংখ্যাৰ ওপৰৰ ৰেখা।")])]},
        10: {"u1": [solve("m10.u1.q6", "w-rate", lambda a, b, d1, c, e, d2: {"q": B(f"A does ${fr(a, b)}$ of a job in {d1} days. B does ${fr(c, e)}$ of it in {d2} days. How long do they take together?", f"Aই {d1} দিনত কামৰ ${fr(a, b)}$ অংশ কৰে। Bই {d2} দিনত ${fr(c, e)}$ অংশ কৰে। একেলগে কিমান দিন ল'ব?"), "answer": num(1 / (F(a, b) / d1 + F(c, e) / d2)), "suffix": B("days", "দিন"), "why": B("First find each person's days for the whole job.", "প্ৰথমে গোটেই কামৰ বাবে প্ৰত্যেকৰ দিন উলিওৱা।")}, [(2, 3, 8, 3, 4, 18), (1, 2, 5, 1, 3, 5), (3, 4, 15, 1, 2, 15)], hints=[B("Whole job = days ÷ part done.", "গোটেই কাম = দিন ÷ কৰা অংশ।")])]},
        13: {"u1": [solve("m13.u1.q7", "ap", lambda c, e: {"q": B(f"In an AP the third term is {c} and the fifth is {e}. Find the first term.", f"সমান্তৰ শ্ৰেণীৰ তৃতীয় পদ {c}, পঞ্চম পদ {e}। প্ৰথম পদ উলিওৱা।"), "answer": str(c - (e - c)), "why": B(f"Two steps make {e - c}, so go back two steps from {c}.", f"দুটা খোজত {e - c}, সেয়ে {c}ৰ পৰা দুখোজ পিছলৈ যোৱা।")}, [(11, 17), (16, 24), (20, 26), (14, 22)], hints=[B("Term 3 to term 5 is two common differences.", "3 নং পদৰ পৰা 5 নং পদলৈ দুটা সাধাৰণ অন্তৰ।")])],
             "u2": [solve("m13.u2.q7", "ap", lambda y, a, d, t_: {"q": B(f"A worker starts in {y} on ₹{a} a year with a rise of ₹{d} each year. In which year does the pay reach ₹{t_}?", f"এজন কৰ্মীয়ে {y}ত বছৰি ₹{a}ৰে আৰম্ভ কৰে, প্ৰতিবছৰে ₹{d} বাঢ়ে। কোন বছৰত দৰমহা ₹{t_} হ'ব?"), "answer": str(y + ex(t_ - a, d)), "why": B(f"{ex(t_ - a, d)} rises after {y}.", f"{y}ৰ পিছত {ex(t_ - a, d)}টা বৃদ্ধি।"), "traps": [{"ans": str(y + ex(t_ - a, d) + 1), "tag": "m-ap-n", "why": B("The first year has no rise yet, so count rises from the start year.", "প্ৰথম বছৰত বৃদ্ধি নাই, সেয়ে আৰম্ভণিৰ বছৰৰ পৰা বৃদ্ধি গণা।")}]}, [(2004, 6000, 250, 7500), (2010, 8000, 400, 10000), (1998, 4000, 300, 5500)])]},
        14: {"u1": [solve("m14.u1.q7", "tr-values", lambda name, a, ans, other: {"q": B(f"In triangle PQR, Q = 90°, {name} = {a} cm and PR = {2 * a} cm. Find angle R.", f"PQR ত্ৰিভুজত Q = 90°, {name} = {a} ছেমি, PR = {2 * a} ছেমি। R কোণ উলিওৱা।"), "answer": str(ans), "suffix": B("°", "°"), "why": B("One side is half the hypotenuse, so a ratio is $\\frac{1}{2}$.", "এটা বাহু অতিভুজৰ আধা, সেয়ে অনুপাত $\\frac{1}{2}$।"), "traps": [{"ans": str(other), "tag": "m-trig-swap", "why": B("That is angle P. Look from R: which side faces it?", "সেয়া P কোণ। Rৰ পৰা চোৱা: কোন বাহু বিপৰীতে?")}]}, [("PQ", 5, 30, 60), ("QR", 4, 60, 30), ("PQ", 7, 30, 60)], hints=[B("Name the sides from R first.", "প্ৰথমে Rৰ পৰা বাহুৰ নাম দিয়া।")])]},
    }


def tanks():
    p = "m16.y"
    return unit("u5", B("Rooms, tanks and cut cubes", "কোঠা, টেংকী আৰু কটা ঘনক"), "star", [
        B("The four walls of a room are $2h(l + b)$.", "কোঠাৰ চাৰিখন বেৰ $2h(l + b)$।"),
        B("A cube's four sides are $4a^2$; all six faces are $6a^2$.", "ঘনকৰ চাৰিটা পাৰ্শ্ব $4a^2$; ছয়টা পৃষ্ঠ $6a^2$।"),
        B("1 cubic metre holds 1000 litres.", "1 ঘন মিটাৰত 1000 লিটাৰ।"),
        B("Small cubes from a big one: divide the volumes, not the edges.", "ডাঙৰ ঘনকৰ পৰা সৰু ঘনক: কাষ নহয়, আয়তন হৰণ কৰা।"),
    ], [
        lab(f"{p}.s1", B("Water has a height", "পানীৰো উচ্চতা আছে"), B("A tank floor is 4 by 3. Each layer of water sits on that floor.", "টেংকীৰ তল 4 বাই 3। পানীৰ প্ৰতিটো স্তৰ সেই তলত থাকে।"), {"kind": "stack", "l": 4, "b": 3, "h": 1, "max": 5}, [
            task(B("Raise it to height 4.", "উচ্চতা 4 কৰা।"), {"h": 4}, B("48 units on a floor of 12. Height is always volume ÷ floor.", "12ৰ তলত 48 একক। উচ্চতা সদায় আয়তন ÷ তল।")),
        ]),
        diagram(f"{p}.s2", B("Litres to a height", "লিটাৰৰ পৰা উচ্চতা"), [B("Capacity often comes in litres while the tank is measured in metres.", "ধাৰকত্ব প্ৰায়ে লিটাৰত থাকে, টেংকীৰ জোখ মিটাৰত।"), B("Change litres to cubic metres first, then divide by the floor.", "প্ৰথমে লিটাৰক ঘন মিটাৰ কৰা, তাৰ পিছত তলেৰে হৰণ কৰা।")], "flow", [B("600 litres", "600 লিটাৰ"), B("0.6 cubic m", "0.6 ঘন মিটাৰ"), B("0.6 ÷ floor", "0.6 ÷ তল")]),
        solve(f"{p}.q1", "g-solid", lambda a, b: {"q": B(f"How many cubes of edge {b} cm can be cut from a cube of edge {a} cm?", f"{a} ছেমি কাষৰ ঘনকৰ পৰা {b} ছেমি কাষৰ কিমান ঘনক কাটিব পাৰি?"), "answer": str(ex(a ** 3, b ** 3)), "why": B(f"${a}^3 \\div {b}^3$.", f"${a}^3 \\div {b}^3$।"), "traps": [{"ans": str(ex(a, b)), "tag": "m-scale-linear", "why": B("That fits along one edge only. Space has three directions.", "সেয়া এটা কাষতহে। ঠাইৰ তিনিটা দিশ।")}]}, [(10, 2), (12, 3), (20, 5)]),
        solve(f"{p}.q2", "g-solid", lambda l_, b_, h: {"q": B(f"Find the area of the four walls of a room {l_} m long, {b_} m wide and {h} m high.", f"{l_} মিটাৰ দীঘল, {b_} মিটাৰ বহল, {h} মিটাৰ ওখ কোঠাৰ চাৰিখন বেৰৰ কালি উলিওৱা।"), "answer": str(2 * h * (l_ + b_)), "suffix": B("sq m", "বৰ্গ মিটাৰ"), "why": B("Open the walls into one strip: perimeter × height.", "বেৰবোৰ মেলি এটা পট্টী কৰা: পৰিসীমা × উচ্চতা।"), "traps": [{"ans": str(2 * (l_ * b_ + b_ * h + h * l_)), "tag": "m-area-volume", "why": B("That adds the floor and ceiling too.", "তাত মজিয়া আৰু চিলিংও আছে।")}]}, [(6, 4, 3), (5, 4, 3), (8, 6, 3)]),
        solve(f"{p}.q3", "g-solid", lambda l_, b_, c: {"q": B(f"A tank {l_} m by {b_} m holds {c} litres when full. Find its height in cm.", f"{l_} মিটাৰ বাই {b_} মিটাৰ টেংকীত ভৰিলে {c} লিটাৰ ধৰে। উচ্চতা ছেমিত উলিওৱা।"), "answer": str(ex(F(c) / 10, F(l_) * F(b_))), "suffix": B("cm", "ছেমি"), "why": B(f"{c} litres is ${num(F(c, 1000))}$ cubic m; divide by the floor.", f"{c} লিটাৰ ${num(F(c, 1000))}$ ঘন মিটাৰ; তলেৰে হৰণ কৰা।"), "traps": [{"ans": str(ex(F(c), F(l_) * F(b_))), "tag": "m-litre", "why": B("Litres must become cubic metres first.", "প্ৰথমে লিটাৰক ঘন মিটাৰ কৰিব লাগিব।")}]}, [(2, 1, 600), (3, 2, 1800), (4, 2, 3200)]),
        stepwise(f"{p}.q4", "g-solid", lambda s_: {"q": B(f"A cube has total surface {6 * s_ * s_} sq cm. Find its volume.", f"ঘনকৰ মুঠ পৃষ্ঠকালি {6 * s_ * s_} বৰ্গ ছেমি। আয়তন উলিওৱা।"), "parts": [
            part(B("One face?", "এটা পৃষ্ঠ?"), t(s_ * s_), [t(6 * s_ * s_ // 4), t(s_)], B("Six equal faces.", "ছয়টা সমান পৃষ্ঠ।"), sid=str(s_)),
            part(B("Edge?", "কাষ?"), t(s_), [t(s_ * s_), t(s_ * 2)], B("Root of one face.", "এটা পৃষ্ঠৰ মূল।"), sid=str(s_)),
            part(B("Volume?", "আয়তন?"), t(s_ ** 3), [t(s_ * s_ * 6), t(s_ * 3)], B("Edge × edge × edge.", "কাষ × কাষ × কাষ।"), tag="m-area-volume", sid=str(s_)),
        ], "why": B("Surface to edge to volume.", "পৃষ্ঠৰ পৰা কাষ, তাৰ পিছত আয়তন।")}, [(5,), (7,), (3,)]),
        solve(f"{p}.q5", "g-solid", lambda a: {"q": B(f"Find the area of the four side faces of a cube of edge {a} cm.", f"{a} ছেমি কাষৰ ঘনকৰ চাৰিটা পাৰ্শ্বৰ কালি উলিওৱা।"), "answer": str(4 * a * a), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B("Four faces, leaving out top and bottom.", "ওপৰ আৰু তল বাদ দি চাৰিটা পৃষ্ঠ।"), "traps": [{"ans": str(6 * a * a), "tag": "m-area-volume", "why": B("That counts all six faces.", "তাত ছয়টা পৃষ্ঠই আছে।")}]}, [(5,), (7,), (3,)]),
        tf(f"{p}.q6", "g-solid", B("A tank of 1 cubic metre holds 1000 litres.", "1 ঘন মিটাৰৰ টেংকীত 1000 লিটাৰ ধৰে।"), True, B("One litre is 1000 cubic cm, and a cubic metre is a million of those.", "এক লিটাৰ 1000 ঘন ছেমি, ঘন মিটাৰ তাৰ দহ লাখ।")),
        match(f"{p}.q7", "g-solid", B("Match each shape to its formula", "প্ৰতিটো আকৃতিক সূত্ৰৰ সৈতে মিলোৱা"), [
            [B("Cube, all faces", "ঘনক, সকলো পৃষ্ঠ"), t("$6a^2$")], [B("Cube, four sides", "ঘনক, চাৰি পাৰ্শ্ব"), t("$4a^2$")], [B("Cuboid, four sides", "চতুৰ্ভুজীয় ঘন, চাৰি পাৰ্শ্ব"), t("$2h(l + b)$")], [B("Cuboid, all faces", "চতুৰ্ভুজীয় ঘন, সকলো পৃষ্ঠ"), t("$2(lb + bh + hl)$")],
        ], B("Four sides leave out top and bottom.", "চাৰি পাৰ্শ্বত ওপৰ-তল নাথাকে।")),
    ])


NEW_UNITS = {1: [number_facts], 2: [lcm_more], 4: [cubes, surds], 5: [percent_more], 6: [ratio_values], 8: [profit_more], 9: [interest_more], 10: [work_more], 13: [sequence_more], 14: [identities], 15: [triangle_kinds, similar, rect_clues, circle_parts], 16: [full_surfaces, tanks]}


def extend(lessons):
    """Add the gap units and steps. Everything already published keeps its id and place."""
    extra = {3: {"u3": [word_fraction()]}, 7: average_extras(), 9: interest_extras(), 11: speed_extras(), 14: trig_extras()}
    for L in lessons:
        by_id = {u["id"]: u for u in L["units"]}
        for uid, steps in extra.get(L["no"], {}).items():
            by_id[uid]["steps"].extend(steps)
        for uid, steps in more_extras().get(L["no"], {}).items():
            by_id[uid]["steps"].extend(steps)
        L["units"].extend(make() for make in NEW_UNITS.get(L["no"], []))
    return lessons
