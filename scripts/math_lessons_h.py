"""Mathematics lessons 15 and 16: plane figures, then solid figures. All worked numbers are original.

Right answers go through ex(), which refuses a division with a remainder. Taking π as 22/7,
circle answers use radii that are multiples of 7, so they come out whole.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from math_kit import B, explore, match, mcq, num, part, solve, stepwise, tf, unit
from math_labs import task
from math_lessons_c import diagram, lab

PI = F(22, 7)


def ex(a, b=1):
    """Exact division: fails the build rather than round an answer."""
    v = F(a) / b
    assert v.denominator == 1, f"{a} / {b} is not whole"
    return int(v)


def pi(*factors):
    """A value that uses π = 22/7, checked to be whole."""
    v = PI
    for f in factors:
        v *= F(f)
    assert v.denominator == 1, f"π × {factors} is not whole"
    return int(v)


# ---------------------------------------------------------------- Lesson 15
def l15():
    p = "m15"
    linear = B("Area grows with the square of the side: twice the side is four times the area.", "কালি বাহুৰ বৰ্গৰ হাৰে বাঢ়ে: দুগুণ বাহু মানে চাৰিগুণ কালি।")
    half_p = B("That is length + breadth. A perimeter goes all the way round, so double it.", "সেয়া দৈৰ্ঘ্য + প্ৰস্থ। পৰিসীমা গোটেই ঘূৰি যায়, সেয়ে দুগুণ কৰা।")
    triangle = B("A triangle is half its box. Remember the half.", "ত্ৰিভুজ ইয়াৰ বাকচৰ আধা। আধা নাপাহৰিবা।")
    ineq = B("Two sides together must be longer than the third, or they cannot meet.", "দুটা বাহু একেলগে তৃতীয়টোতকৈ দীঘল হ'ব লাগিব, নহ'লে নিমিলে।")
    radius = B("$C = 2\\pi r$ uses the radius, which is half the diameter.", "$C = 2\\pi r$ত ব্যাসাৰ্ধ লাগে, ই ব্যাসৰ আধা।")
    u1 = unit("u1", B("Squares and rectangles", "বৰ্গ আৰু আয়ত"), "star", [
        B("Rectangle: area lb, perimeter 2(l + b).", "আয়ত: কালি lb, পৰিসীমা 2(l + b)।"),
        B("Square: area $a^2$; from its diagonal, area = $\\frac{d^2}{2}$.", "বৰ্গ: কালি $a^2$; কৰ্ণৰ পৰা কালি = $\\frac{d^2}{2}$।"),
        B("k times the side is $k^2$ times the area.", "k গুণ বাহু মানে $k^2$ গুণ কালি।"),
        B("The largest square tile for a floor is the HCF of its sides.", "মজিয়াৰ সৰ্ববৃহৎ বৰ্গ টাইল বাহুবোৰৰ গ.সা.গু.।"),
    ], [
        lab(f"{p}.u1.s1", B("Double side, four times area", "দুগুণ বাহু, চাৰিগুণ কালি"), B("The gold square is the original. Grow the side and count how many copies fit.", "সোণালী বৰ্গটো মূল। বাহু বঢ়াই কেইটা সোমায় গণা।"), {"kind": "scaleup", "dim": 2, "k": 1}, [
            task(B("Make the side 2 times as long.", "বাহু 2 গুণ দীঘল কৰা।"), {"k": 2}, B("Four copies fit: the shape grew in two directions at once.", "চাৰিটা সোমায়: আকৃতি একে সময়তে দুই দিশত বাঢ়িল।")),
            task(B("Now make it 3 times as long.", "এতিয়া 3 গুণ দীঘল কৰা।"), {"k": 3}, B("Nine copies. So diagonals in the ratio 2 : 3 mean areas in the ratio 4 : 9.", "ন টা। সেয়ে কৰ্ণৰ অনুপাত 2 : 3 মানে কালিৰ অনুপাত 4 : 9।")),
        ]),
        lab(f"{p}.u1.s2", B("The biggest tile that fits", "সৰ্ববৃহৎ মিলা টাইল"), B("A floor is 360 by 270. Whole square tiles must cover it exactly, so use the square-cutting from LCM and HCF.", "মজিয়াখন 360 বাই 270। গোটা বৰ্গ টাইলে ঠিক ঢাকিব লাগিব, সেয়ে ল.সা.গু.ৰ বৰ্গ কটা পদ্ধতি লোৱা।"), {"kind": "tiles", "a": 360, "b": 270}, [
            task(B("Cut until nothing is left.", "একো নথকালৈ কাটা।"), {"done": 1}, B("Side 90 is the HCF, so the floor takes 4 × 3 = 12 tiles.", "90 বাহু গ.সা.গু., সেয়ে মজিয়াত 4 × 3 = 12টা টাইল।")),
        ]),
        solve(f"{p}.u1.q1", "g-rect", lambda a: {"q": B(f"A square has area {a * a} sq cm. What is its perimeter?", f"এটা বৰ্গৰ কালি {a * a} বৰ্গ ছেমি। পৰিসীমা কিমান?"), "answer": str(4 * a), "suffix": B("cm", "ছেমি"), "why": B(f"The side is $\\sqrt{{{a * a}}} = {a}$, and there are four sides.", f"বাহু $\\sqrt{{{a * a}}} = {a}$, চাৰিটা বাহু।"), "traps": [{"ans": str(a), "tag": "m-perim-half", "why": B("That is one side. The perimeter is all four.", "সেয়া এটা বাহু। পৰিসীমা চাৰিওটা।")}]}, [(21,), (13,), (15,), (18,)], hints=[B("First find the side.", "প্ৰথমে বাহু উলিওৱা।")]),
        solve(f"{p}.u1.q2", "g-rect", lambda d: {"q": B(f"A square has diagonal {d} cm. Find its area.", f"এটা বৰ্গৰ কৰ্ণ {d} ছেমি। কালি উলিওৱা।"), "answer": str(ex(d * d, 2)), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B(f"$\\frac{{{d}^2}}{{2}}$: the square is half the box on its diagonal.", f"$\\frac{{{d}^2}}{{2}}$: বৰ্গটো কৰ্ণৰ বাকচৰ আধা।"), "traps": [{"ans": str(d * d), "tag": "m-scale-linear", "why": B("Squaring the diagonal gives a square twice as big. Halve it.", "কৰ্ণৰ বৰ্গ দুগুণ ডাঙৰ। আধা কৰা।")}]}, [(6,), (10,), (8,), (12,)]),
        solve(f"{p}.u1.q3", "g-rect", lambda A, l: {"q": B(f"A rectangle has area {A} sq cm and length {l} cm. Find its perimeter.", f"এটা আয়তৰ কালি {A} বৰ্গ ছেমি, দৈৰ্ঘ্য {l} ছেমি। পৰিসীমা উলিওৱা।"), "answer": str(2 * (l + ex(A, l))), "suffix": B("cm", "ছেমি"), "why": B(f"Breadth = {A} ÷ {l} = {ex(A, l)}, then 2({l} + {ex(A, l)}).", f"প্ৰস্থ = {A} ÷ {l} = {ex(A, l)}, তাৰ পিছত 2({l} + {ex(A, l)})।"), "traps": [{"ans": str(l + ex(A, l)), "tag": "m-perim-half", "why": half_p}]}, [(300, 25), (150, 15), (84, 12), (96, 16)]),
        tf(f"{p}.u1.q4", "g-rect", B("If the side of a square doubles, its area doubles.", "বৰ্গৰ বাহু দুগুণ হ'লে কালি দুগুণ হয়।"), False, B("Four copies fit inside, so the area is four times as big.", "ভিতৰত চাৰিটা সোমায়, সেয়ে কালি চাৰিগুণ।"), ("m-scale-linear", linear)),
        stepwise(f"{p}.u1.q5", "g-rect", lambda a, b: {"q": B(f"A floor {a} cm by {b} cm is covered with the largest whole square tiles. How many tiles?", f"{a} ছেমি বাই {b} ছেমি মজিয়া সৰ্ববৃহৎ গোটা বৰ্গ টাইলেৰে ঢকা হ'ল। কেইটা টাইল?"), "parts": [
            part(B("Tile side?", "টাইলৰ বাহু?"), B(str(gcd(a, b)), str(gcd(a, b))), [B(str(gcd(a, b) * 2), str(gcd(a, b) * 2)), B(str(gcd(a, b) // 2), str(gcd(a, b) // 2))], B("The HCF of the two sides.", "দুয়োটা বাহুৰ গ.সা.গু.।"), skill="l-hcf", sid=str(a)),
            part(B("Tiles along each side?", "প্ৰতিটো বাহুত টাইল?"), B(f"{ex(a, gcd(a, b))} and {ex(b, gcd(a, b))}", f"{ex(a, gcd(a, b))} আৰু {ex(b, gcd(a, b))}"), [B(f"{a} and {b}", f"{a} আৰু {b}"), B(f"{ex(a, gcd(a, b)) + 1} and {ex(b, gcd(a, b)) + 1}", f"{ex(a, gcd(a, b)) + 1} আৰু {ex(b, gcd(a, b)) + 1}")], B("Divide each side by the tile.", "প্ৰতিটো বাহু টাইলেৰে হৰণ কৰা।"), sid=str(a)),
            part(B("Total tiles?", "মুঠ টাইল?"), B(str(ex(a * b, gcd(a, b) ** 2)), str(ex(a * b, gcd(a, b) ** 2))), [B(str(ex(a, gcd(a, b)) + ex(b, gcd(a, b))), str(ex(a, gcd(a, b)) + ex(b, gcd(a, b)))), B(str(2 * (ex(a, gcd(a, b)) + ex(b, gcd(a, b)))), str(2 * (ex(a, gcd(a, b)) + ex(b, gcd(a, b)))))], B("Multiply the rows and columns.", "শাৰী আৰু স্তম্ভ পূৰণ কৰা।"), sid=str(a)),
        ], "why": B("Tile counts are HCF first, then a simple multiplication.", "টাইল গণনা: প্ৰথমে গ.সা.গু., তাৰ পিছত পূৰণ।")}, [(240, 180), (360, 270), (150, 120)]),
        explore(f"{p}.u1.q6", "g-rect", lambda times, k: {"q": B(f"A square must have {times} times the area. Slide to the new side multiple.", f"বৰ্গৰ কালি {times} গুণ হ'ব লাগে। নতুন বাহুৰ গুণলৈ টানা।"), "widget": {"kind": "scaleup", "dim": 2, "k": 1}, "target": k, "answerText": B(f"{k} times the side", f"বাহুৰ {k} গুণ"), "why": B(f"{k} × {k} = {times}.", f"{k} × {k} = {times}।"), "traps": [{"val": 2, "tag": "m-scale-linear", "why": linear}] if k != 2 and times == 4 else []}, [(9, 3), (16, 4), (4, 2)]),
        match(f"{p}.u1.q7", "g-rect", B("Match the diagonal ratio to the area ratio", "কৰ্ণৰ অনুপাতক কালিৰ অনুপাতৰ সৈতে মিলোৱা"), [
            [B("1 : 2", "1 : 2"), B("1 : 4", "1 : 4")], [B("2 : 3", "2 : 3"), B("4 : 9", "4 : 9")], [B("3 : 4", "3 : 4"), B("9 : 16", "9 : 16")], [B("5 : 6", "5 : 6"), B("25 : 36", "25 : 36")],
        ], B("Square both sides of the ratio.", "অনুপাতৰ দুয়োফাল বৰ্গ কৰা।")),
    ])
    u2 = unit("u2", B("Triangles", "ত্ৰিভুজ"), "star", [
        B("A triangle's angles add to 180°.", "ত্ৰিভুজৰ কোণৰ যোগফল 180°।"),
        B("Any two sides together must exceed the third.", "যিকোনো দুটা বাহুৰ যোগফল তৃতীয়টোতকৈ ডাঙৰ হ'ব লাগিব।"),
        B("Area = $\\frac{1}{2}$ × base × height.", "কালি = $\\frac{1}{2}$ × ভূমি × উচ্চতা।"),
        B("With three sides, use $\\sqrt{s(s - a)(s - b)(s - c)}$.", "তিনিটা বাহু থাকিলে $\\sqrt{s(s - a)(s - b)(s - c)}$ লোৱা।"),
    ], [
        lab(f"{p}.u2.s1", B("Half the box, every time", "সদায় বাকচৰ আধা"), B("Blue is the triangle, the dashed outline is its box. The white line cuts both pieces in half.", "নীলা ত্ৰিভুজ, ডেচ ৰেখা ইয়াৰ বাকচ। বগা ৰেখাই দুয়োটা টুকুৰা আধা কৰে।"), {"kind": "shear", "b": 12, "h": 8, "x": 4}, [
            task(B("Slide the top corner to 10.", "ওপৰৰ চুক 10লৈ টানা।"), {"x": 10}, B("The shape leans, but the area stays 48: same base, same height.", "আকৃতি হেলে, কিন্তু কালি 48 থাকে: একে ভূমি, একে উচ্চতা।")),
        ]),
        lab(f"{p}.u2.s2", B("Can three sticks close?", "তিনিডাল লাঠি জোৰা লাগিবনে?"), B("Two sticks are 5 and 7. Change the third and see when they make a triangle.", "দুডাল লাঠি 5 আৰু 7। তৃতীয়ডাল সলনি কৰি কেতিয়া ত্ৰিভুজ হয় চোৱা।"), {"kind": "sticks", "a": 5, "b": 7, "c": 6}, [
            task(B("Slide the third stick to 12.", "তৃতীয় লাঠি 12লৈ টানা।"), {"c": 12}, B("5 + 7 = 12 is not enough: they lie flat. The two must be strictly longer.", "5 + 7 = 12 যথেষ্ট নহয়: চেপেটা হয়। দুয়োডাল নিশ্চিতভাৱে দীঘল হ'ব লাগিব।")),
            task(B("Now slide it to 2.", "এতিয়া 2লৈ টানা।"), {"c": 2}, B("5 + 2 = 7 fails too. Always test the two shortest sticks against the longest.", "5 + 2 = 7ও নহয়। সদায় দুটা চুটি লাঠি দীঘলটোৰ সৈতে পৰীক্ষা কৰা।")),
        ]),
        solve(f"{p}.u2.q1", "g-tri", lambda a, b: {"q": B(f"In a triangle two angles are {a}° and {b}°. Find the third.", f"ত্ৰিভুজৰ দুটা কোণ {a}° আৰু {b}°। তৃতীয়টো উলিওৱা।"), "answer": str(180 - a - b), "suffix": B("°", "°"), "why": B(f"180 − {a} − {b}.", f"180 − {a} − {b}।"), "traps": [{"ans": str(360 - a - b), "tag": "m-angle-sum", "why": B("A triangle's angles add to 180°, not 360°.", "ত্ৰিভুজৰ কোণৰ যোগফল 180°, 360° নহয়।")}]}, [(58, 80), (72, 68), (62, 38), (45, 75)]),
        explore(f"{p}.u2.q2", "g-sides", lambda a, b: {"q": B(f"Sticks of {a} and {b}. Slide to the longest whole third stick that still makes a triangle.", f"{a} আৰু {b} লাঠি। ত্ৰিভুজ হোৱা আটাইতকৈ দীঘল গোটা তৃতীয় লাঠিলৈ টানা।"), "widget": {"kind": "sticks", "a": a, "b": b}, "target": a + b - 1, "answerText": B(f"{a + b - 1}", f"{a + b - 1}"), "why": B(f"It must be under {a} + {b}.", f"ই {a} + {b}তকৈ কম হ'ব লাগিব।"), "traps": [{"val": a + b, "tag": "m-tri-ineq", "why": ineq}]}, [(5, 7), (4, 9), (6, 6)]),
        tf(f"{p}.u2.q3", "g-sides", B("Sides of 2, 3 and 6 can form a triangle.", "2, 3 আৰু 6 বাহুৰে ত্ৰিভুজ হ'ব পাৰে।"), False, B("2 + 3 = 5, which cannot reach 6.", "2 + 3 = 5, 6 নাপায়।"), ("m-tri-ineq", ineq)),
        solve(f"{p}.u2.q4", "g-tri", lambda b, h: {"q": B(f"Find the area of a triangle with base {b} cm and height {h} cm.", f"{b} ছেমি ভূমি আৰু {h} ছেমি উচ্চতাৰ ত্ৰিভুজৰ কালি উলিওৱা।"), "answer": str(ex(b * h, 2)), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B(f"Half of {b} × {h}.", f"{b} × {h}ৰ আধা।"), "traps": [{"ans": str(b * h), "tag": "m-tri-area", "why": triangle}]}, [(12, 8), (10, 6), (14, 10), (9, 8)]),
        stepwise(f"{p}.u2.q5", "g-tri", lambda a, b, c: {"q": B(f"Find the area of a triangle with sides {a}, {b} and {c} cm.", f"{a}, {b} আৰু {c} ছেমি বাহুৰ ত্ৰিভুজৰ কালি উলিওৱা।"), "parts": [
            part(B("Half the perimeter, s?", "পৰিসীমাৰ আধা, s?"), B(str(ex(a + b + c, 2)), str(ex(a + b + c, 2))), [B(str(a + b + c), str(a + b + c)), B(str(ex(a + b + c, 2) + 1), str(ex(a + b + c, 2) + 1))], B("Add the sides and halve.", "বাহু যোগ কৰি আধা কৰা।"), sid=str(a)),
            part(B("s(s − a)(s − b)(s − c)?", "s(s − a)(s − b)(s − c)?"), B(str(ex(a + b + c, 2) * (ex(a + b + c, 2) - a) * (ex(a + b + c, 2) - b) * (ex(a + b + c, 2) - c)), str(ex(a + b + c, 2) * (ex(a + b + c, 2) - a) * (ex(a + b + c, 2) - b) * (ex(a + b + c, 2) - c))), [B(str(a * b * c), str(a * b * c)), B(str(ex(a + b + c, 2) * a), str(ex(a + b + c, 2) * a))], B("Multiply the four numbers.", "চাৰিটা সংখ্যা পূৰণ কৰা।"), sid=str(a)),
            part(B("Area?", "কালি?"), B(str(isqrt(ex(a + b + c, 2) * (ex(a + b + c, 2) - a) * (ex(a + b + c, 2) - b) * (ex(a + b + c, 2) - c))), str(isqrt(ex(a + b + c, 2) * (ex(a + b + c, 2) - a) * (ex(a + b + c, 2) - b) * (ex(a + b + c, 2) - c)))), [B(str(a * b), str(a * b)), B(str(a + b), str(a + b))], B("Take the square root.", "বৰ্গমূল লোৱা।"), skill="s-roots", sid=str(a)),
        ], "why": B("This formula works whenever you know all three sides.", "তিনিওটা বাহু জানিলে এই সূত্ৰ চলে।")}, [(13, 14, 15), (6, 8, 10), (5, 5, 6)]),
        match(f"{p}.u2.q6", "g-tri", B("Match the equilateral side to its area", "সমবাহু বাহুক কালিৰ সৈতে মিলোৱা"), [
            [B("2", "2"), B("$\\sqrt{3}$", "$\\sqrt{3}$")], [B("4", "4"), B("$4\\sqrt{3}$", "$4\\sqrt{3}$")], [B("6", "6"), B("$9\\sqrt{3}$", "$9\\sqrt{3}$")], [B("10", "10"), B("$25\\sqrt{3}$", "$25\\sqrt{3}$")],
        ], B("Equilateral area is $\\frac{\\sqrt{3}}{4}a^2$.", "সমবাহুৰ কালি $\\frac{\\sqrt{3}}{4}a^2$।")),
    ])
    u3 = unit("u3", B("Rhombus and trapezium", "ৰম্বাছ আৰু ট্ৰেপিজিয়াম"), "star", [
        B("A rhombus has four equal sides and diagonals that cross at right angles.", "ৰম্বাছৰ চাৰিটা সমান বাহু, কৰ্ণ সমকোণত কাটে।"),
        B("Rhombus area = $\\frac{d_1 \\times d_2}{2}$.", "ৰম্বাছৰ কালি = $\\frac{d_1 \\times d_2}{2}$।"),
        B("Half-diagonals and the side form a right triangle.", "আধা কৰ্ণ আৰু বাহুৱে সমকোণী ত্ৰিভুজ গঢ়ে।"),
        B("Trapezium area = $\\frac{1}{2}$ × sum of parallel sides × height.", "ট্ৰেপিজিয়ামৰ কালি = $\\frac{1}{2}$ × সমান্তৰাল বাহুৰ যোগফল × উচ্চতা।"),
    ], [
        lab(f"{p}.u3.s1", B("A rhombus is half its box", "ৰম্বাছ বাকচৰ আধা"), B("Draw a box around the two diagonals. Each gold corner is a copy of one piece of the rhombus.", "দুটা কৰ্ণৰ চাৰিওফালে বাকচ আঁকা। প্ৰতিটো সোণালী চুক ৰম্বাছৰ এটা টুকুৰাৰ প্ৰতিলিপি।"), {"kind": "kite", "d1": 10, "d2": 6}, [
            task(B("Fold the corners in.", "চুকবোৰ ভিতৰলৈ ভাঁজ কৰা।"), {"folded": 1}, B("The four corners exactly cover the rhombus, so its area is half of 10 × 6.", "চাৰিটা চুকে ৰম্বাছ ঠিক ঢাকে, সেয়ে কালি 10 × 6ৰ আধা।")),
        ]),
        diagram(f"{p}.u3.s2", B("Two copies make a parallelogram", "দুটা প্ৰতিলিপিয়ে সামান্তৰিক বনায়"), [B("Flip a trapezium and join it to itself, like the stairs in AP.", "ট্ৰেপিজিয়াম ওলোটাই নিজৰ লগত জোৰা, সমান্তৰ শ্ৰেণীৰ খটখটিৰ দৰে।"), B("The base becomes a + b, and the trapezium is half of it.", "ভূমি a + b হয়, ট্ৰেপিজিয়াম তাৰ আধা।")], "flow", [B("Two copies", "দুটা প্ৰতিলিপি"), B("Base a + b, height h", "ভূমি a + b, উচ্চতা h"), B("Half of (a + b)h", "(a + b)hৰ আধা")]),
        solve(f"{p}.u3.q1", "g-quad", lambda a, b: {"q": B(f"A rhombus has diagonals {a} cm and {b} cm. Find its area.", f"ৰম্বাছৰ কৰ্ণ {a} ছেমি আৰু {b} ছেমি। কালি উলিওৱা।"), "answer": str(ex(a * b, 2)), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B(f"Half of {a} × {b}.", f"{a} × {b}ৰ আধা।"), "traps": [{"ans": str(a * b), "tag": "m-tri-area", "why": B("That is the whole box. The rhombus is half of it.", "সেয়া গোটা বাকচ। ৰম্বাছ তাৰ আধা।")}]}, [(10, 6), (12, 8), (16, 5), (14, 10)]),
        solve(f"{p}.u3.q2", "g-quad", lambda a, d: {"q": B(f"A rhombus has area {a} sq m and one diagonal of {d} m. Find the other.", f"ৰম্বাছৰ কালি {a} বৰ্গ মি, এটা কৰ্ণ {d} মি। আনটো উলিওৱা।"), "answer": str(ex(2 * a, d)), "suffix": B("m", "মি"), "why": B(f"2 × {a} ÷ {d}.", f"2 × {a} ÷ {d}।"), "traps": [{"ans": str(ex(a, d)), "tag": "m-tri-area", "why": B("Area is half the product, so double it first.", "কালি পূৰণফলৰ আধা, সেয়ে প্ৰথমে দুগুণ কৰা।")}]}, [(96, 12), (60, 10), (84, 14)]),
        stepwise(f"{p}.u3.q3", "g-quad", lambda a, b, c: {"q": B(f"A rhombus has diagonals {a} and {b} cm. Find its side.", f"ৰম্বাছৰ কৰ্ণ {a} আৰু {b} ছেমি। বাহু উলিওৱা।"), "parts": [
            part(B("Half-diagonals?", "আধা কৰ্ণ?"), B(f"{ex(a, 2)} and {ex(b, 2)}", f"{ex(a, 2)} আৰু {ex(b, 2)}"), [B(f"{a} and {b}", f"{a} আৰু {b}"), B(f"{a * 2} and {b * 2}", f"{a * 2} আৰু {b * 2}")], B("Diagonals bisect each other.", "কৰ্ণে পৰস্পৰক আধা কৰে।"), sid=str(a)),
            part(B("The angle where they cross?", "কটা ঠাইৰ কোণ?"), B("90°", "90°"), [B("60°", "60°"), B("45°", "45°")], B("A rhombus's diagonals are perpendicular.", "ৰম্বাছৰ কৰ্ণ লম্ব।"), sid=str(a)),
            part(B("Side?", "বাহু?"), B(str(c), str(c)), [B(str(ex(a, 2) + ex(b, 2)), str(ex(a, 2) + ex(b, 2))), B(str(c + 3), str(c + 3))], B("Pythagoras on the half-diagonals.", "আধা কৰ্ণত পাইথাগোৰাছ।"), skill="s-roots", tag="m-root-add", sid=str(a)),
        ], "why": B("Each quarter of a rhombus is a right triangle.", "ৰম্বাছৰ প্ৰতিটো চতুৰ্থাংশ সমকোণী ত্ৰিভুজ।")}, [(6, 8, 5), (10, 24, 13), (16, 30, 17)]),
        tf(f"{p}.u3.q4", "g-quad", B("The diagonals of a rhombus cross at right angles.", "ৰম্বাছৰ কৰ্ণ সমকোণত কাটে।"), True, B("This is why half-diagonals and a side make a right triangle.", "সেয়ে আধা কৰ্ণ আৰু বাহুৱে সমকোণী ত্ৰিভুজ গঢ়ে।")),
        solve(f"{p}.u3.q5", "g-quad", lambda s_, h: {"q": B(f"A trapezium has parallel sides adding to {s_} cm and height {h} cm. Find its area.", f"ট্ৰেপিজিয়ামৰ সমান্তৰাল বাহুৰ যোগফল {s_} ছেমি, উচ্চতা {h} ছেমি। কালি উলিওৱা।"), "answer": str(ex(s_ * h, 2)), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B(f"Half of {s_} × {h}.", f"{s_} × {h}ৰ আধা।"), "traps": [{"ans": str(s_ * h), "tag": "m-tri-area", "why": B("Two copies make that shape, so the trapezium is half.", "দুটা প্ৰতিলিপিয়েহে সেই আকৃতি বনায়, ট্ৰেপিজিয়াম তাৰ আধা।")}]}, [(20, 8), (15, 6), (24, 5)]),
        match(f"{p}.u3.q6", "g-quad", B("Match the shape to its area", "আকৃতিক কালিৰ সৈতে মিলোৱা"), [
            [B("Rectangle", "আয়ত"), B("$lb$", "$lb$")], [B("Triangle", "ত্ৰিভুজ"), B("$\\frac{1}{2}bh$", "$\\frac{1}{2}bh$")], [B("Rhombus", "ৰম্বাছ"), B("$\\frac{1}{2}d_1 d_2$", "$\\frac{1}{2}d_1 d_2$")], [B("Trapezium", "ট্ৰেপিজিয়াম"), B("$\\frac{1}{2}(a + b)h$", "$\\frac{1}{2}(a + b)h$")],
        ], B("Three of the four are half of something simple.", "চাৰিটাৰ তিনিটা কোনো সহজ আকৃতিৰ আধা।")),
    ])
    u4 = unit("u4", B("Circles", "বৃত্ত"), "star", [
        B("Circumference = $2\\pi r$: one roll of the wheel.", "পৰিধি = $2\\pi r$: চকাৰ এক পাক।"),
        B("Area = $\\pi r^2$.", "কালি = $\\pi r^2$।"),
        B("The diameter is the longest chord.", "ব্যাস আটাইতকৈ দীঘল জ্যা।"),
        B("Radii in the ratio a : b give areas in the ratio $a^2 : b^2$.", "ব্যাসাৰ্ধৰ অনুপাত a : b হ'লে কালিৰ অনুপাত $a^2 : b^2$।"),
    ], [
        lab(f"{p}.u4.s1", B("Roll it out", "ঘূৰাই চোৱা"), B("A wheel of radius 7 rolls along the ground. The green line is the ground it has covered.", "7 ব্যাসাৰ্ধৰ চকা মাটিত ঘূৰে। সেউজীয়া ৰেখা অতিক্ৰম কৰা বাট।"), {"kind": "roll", "r": 7, "max": 4}, [
            task(B("Roll it one full turn.", "এক পাক ঘূৰোৱা।"), {"turns": 1}, B("One turn is 44: the circumference laid flat, $2 \\times \\frac{22}{7} \\times 7$.", "এক পাক 44: পৰিধি সমান কৰি মেলা, $2 \\times \\frac{22}{7} \\times 7$।")),
            task(B("Roll it 3 turns.", "3 পাক ঘূৰোৱা।"), {"turns": 3}, B("132. Distance = turns × circumference, which is how wheel questions work.", "132। দূৰত্ব = পাক × পৰিধি, চকাৰ প্ৰশ্ন এনেকৈয়ে হয়।")),
        ]),
        lab(f"{p}.u4.s2", B("A circle becomes a rectangle", "বৃত্ত আয়ত হয়"), B("Cut a circle into slices and lay them head to tail, half blue and half gold.", "বৃত্ত টুকুৰা কৰি মূৰে-নেজে সজোৱা, আধা নীলা, আধা সোণালী।"), {"kind": "sectors", "n": 6}, [
            task(B("Cut it into 30 slices.", "30 টুকুৰা কৰা।"), {"n": 30}, B("It is nearly a rectangle: half the circumference, $\\pi r$, by the radius r. So the area is $\\pi r^2$.", "প্ৰায় আয়ত: পৰিধিৰ আধা $\\pi r$, ব্যাসাৰ্ধ r। সেয়ে কালি $\\pi r^2$।")),
        ]),
        explore(f"{p}.u4.q1", "g-circle", lambda r, n: {"q": B(f"A wheel of radius {r} must cover {pi(2, r, n)}. Slide to the number of turns.", f"{r} ব্যাসাৰ্ধৰ চকাই {pi(2, r, n)} অতিক্ৰম কৰিব লাগে। পাকৰ সংখ্যালৈ টানা।"), "widget": {"kind": "roll", "r": r, "max": 6}, "target": n, "answerText": B(f"{n} turns", f"{n} পাক"), "why": B(f"One turn is {pi(2, r)}.", f"এক পাক {pi(2, r)}।")}, [(7, 5), (14, 3), (21, 2)]),
        solve(f"{p}.u4.q2", "g-circle", lambda dist, rounds, r: {"q": B(f"A wheel covers {dist} m in {rounds} rounds. Taking $\\pi = \\frac{{22}}{{7}}$, find its radius.", f"এটা চকাই {rounds} পাকত {dist} মিটাৰ যায়। $\\pi = \\frac{{22}}{{7}}$ ধৰি ব্যাসাৰ্ধ উলিওৱা।"), "answer": num(r), "suffix": B("m", "মি"), "why": B(f"One round is {ex(dist, rounds)} m, and $r = \\frac{{C}}{{2\\pi}}$.", f"এক পাক {ex(dist, rounds)} মিটাৰ, আৰু $r = \\frac{{C}}{{2\\pi}}$।"), "traps": [{"ans": num(r * 2), "tag": "m-radius-dia", "why": radius}]}, [(44000, 1000, F(7)), (22000, 1000, F(7, 2)), (88000, 2000, F(7)), (13200, 300, F(7))], hints=[B("Find the distance of one round first.", "প্ৰথমে এক পাকৰ দূৰত্ব উলিওৱা।")]),
        solve(f"{p}.u4.q3", "g-circle", lambda r: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, find the area of a circle of radius {r} cm.", f"$\\pi = \\frac{{22}}{{7}}$ ধৰি {r} ছেমি ব্যাসাৰ্ধৰ বৃত্তৰ কালি উলিওৱা।"), "answer": str(pi(r, r)), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B(f"$\\frac{{22}}{{7}} \\times {r}^2$.", f"$\\frac{{22}}{{7}} \\times {r}^2$।"), "traps": [{"ans": str(pi(2, r)), "tag": "m-circle-formula", "why": B("That is the circumference. Area uses $r^2$.", "সেয়া পৰিধি। কালিত $r^2$ লাগে।")}]}, [(7,), (14,), (21,)]),
        tf(f"{p}.u4.q4", "g-circle", B("If radii are in the ratio 2 : 3, areas are in the ratio 4 : 9.", "ব্যাসাৰ্ধৰ অনুপাত 2 : 3 হ'লে কালিৰ অনুপাত 4 : 9।"), True, B("Area scales with the square, just as for squares.", "কালি বৰ্গৰ হাৰে বাঢ়ে, বৰ্গৰ দৰেই।")),
        stepwise(f"{p}.u4.q5", "g-circle", lambda r: {"q": B(f"A wire bent into a circle of radius {r} cm is reshaped into a square. Find the square's area, taking $\\pi = \\frac{{22}}{{7}}$.", f"{r} ছেমি ব্যাসাৰ্ধৰ বৃত্তাকাৰ তাঁৰ বৰ্গ কৰা হ'ল। $\\pi = \\frac{{22}}{{7}}$ ধৰি বৰ্গৰ কালি উলিওৱা।"), "parts": [
            part(B("Length of the wire?", "তাঁৰৰ দৈৰ্ঘ্য?"), B(f"{pi(2, r)} cm", f"{pi(2, r)} ছেমি"), [B(f"{pi(r, r)} cm", f"{pi(r, r)} ছেমি"), B(f"{pi(r)} cm", f"{pi(r)} ছেমি")], B("The circumference: wire keeps its length.", "পৰিধি: তাঁৰৰ দৈৰ্ঘ্য একে থাকে।"), tag="m-circle-formula", sid=str(r)),
            part(B("Side of the square?", "বৰ্গৰ বাহু?"), B(f"{ex(pi(2, r), 4)} cm", f"{ex(pi(2, r), 4)} ছেমি"), [B(f"{ex(pi(2, r), 2)} cm", f"{ex(pi(2, r), 2)} ছেমি"), B(f"{pi(2, r)} cm", f"{pi(2, r)} ছেমি")], B("Four equal sides.", "চাৰিটা সমান বাহু।"), sid=str(r)),
            part(B("Area?", "কালি?"), B(f"{ex(pi(2, r), 4) ** 2} sq cm", f"{ex(pi(2, r), 4) ** 2} বৰ্গ ছেমি"), [B(f"{pi(r, r)} sq cm", f"{pi(r, r)} বৰ্গ ছেমি"), B(f"{ex(pi(2, r), 4) * 2} sq cm", f"{ex(pi(2, r), 4) * 2} বৰ্গ ছেমি")], B("Side squared.", "বাহুৰ বৰ্গ।"), skill="g-rect", sid=str(r)),
        ], "why": B("The wire's length is the one thing that stays the same.", "তাঁৰৰ দৈৰ্ঘ্যই একমাত্ৰ স্থিৰ কথা।")}, [(7,), (14,), (21,)]),
        match(f"{p}.u4.q6", "g-circle", B("Taking $\\pi = \\frac{22}{7}$, match the radius to the circumference", "$\\pi = \\frac{22}{7}$ ধৰি ব্যাসাৰ্ধক পৰিধিৰ সৈতে মিলোৱা"), [
            [B("3.5", "3.5"), B("22", "22")], [B("7", "7"), B("44", "44")], [B("14", "14"), B("88", "88")], [B("21", "21"), B("132", "132")],
        ], B("Double the radius, double the circumference: a length scales in step.", "ব্যাসাৰ্ধ দুগুণ, পৰিধি দুগুণ: দৈৰ্ঘ্য একে হাৰে বাঢ়ে।")),
    ])
    test = {"id": "test", "title": B("Plane figures test", "সমতল আকৃতি পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "g-rect", lambda a, b: {"q": B(f"The diagonals of two squares are in the ratio {a} : {b}. As a fraction, their areas are in the ratio", f"দুটা বৰ্গৰ কৰ্ণৰ অনুপাত {a} : {b}। ভগ্নাংশত কালিৰ অনুপাত"), "right": F(a * a, b * b), "wrong": [(F(a, b), "m-scale-linear", linear)], "fill": [F(2 * a, 2 * b + 1), F(a + 1, b + 1), F(b, a)], "why": B("Square the ratio.", "অনুপাত বৰ্গ কৰা।")}, [(2, 3), (3, 4), (3, 5)]),
        mcq(f"{p}.t.q2", "g-sides", lambda a, b, c, w1, w2, w3: {"q": B("Which set of sides can form a triangle?", "কোনটো বাহুৰ গোটে ত্ৰিভুজ গঢ়িব পাৰে?"), "right": f"{a}, {b}, {c}", "wrong": [(f"{w1[0]}, {w1[1]}, {w1[2]}", "m-tri-ineq", ineq)], "fill": [f"{w2[0]}, {w2[1]}, {w2[2]}", f"{w3[0]}, {w3[1]}, {w3[2]}"], "why": B("The two shortest must add to more than the longest.", "দুটা চুটি বাহুৰ যোগফল দীঘলটোতকৈ বেছি হ'ব লাগিব।")}, [(3, 4, 5, (1, 2, 3), (2, 3, 6), (2, 4, 7)), (5, 6, 7, (2, 3, 5), (3, 4, 8), (1, 5, 7)), (4, 7, 9, (4, 5, 9), (2, 6, 9), (3, 3, 7))]),
        mcq(f"{p}.t.q3", "g-quad", lambda a, b: {"q": B(f"The area of a rhombus with diagonals {a} and {b} cm is", f"{a} আৰু {b} ছেমি কৰ্ণৰ ৰম্বাছৰ কালি"), "right": ex(a * b, 2), "wrong": [(a * b, "m-tri-area", B("That is the whole box.", "সেয়া গোটা বাকচ।"))], "fill": [a + b, 2 * (a + b), ex(a * b, 2) + 5], "unit": " sq cm", "why": B("$\\frac{d_1 d_2}{2}$.", "$\\frac{d_1 d_2}{2}$।")}, [(18, 10), (24, 7), (20, 12)]),
        mcq(f"{p}.t.q4", "g-circle", lambda r: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, a circle of radius {r} cm has circumference", f"$\\pi = \\frac{{22}}{{7}}$ ধৰি {r} ছেমি ব্যাসাৰ্ধৰ বৃত্তৰ পৰিধি"), "right": pi(2, r), "wrong": [(pi(r), "m-radius-dia", radius), (pi(r, r), "m-circle-formula", B("That is the area.", "সেয়া কালি।"))], "fill": [pi(2, r) + 7, pi(4, r)], "unit": " cm", "why": B("$2\\pi r$.", "$2\\pi r$।")}, [(7,), (14,), (35,)]),
        solve(f"{p}.t.q5", "g-tri", lambda a, b: {"q": B(f"Two angles of a triangle are {a}° and {b}°. Find the third.", f"ত্ৰিভুজৰ দুটা কোণ {a}° আৰু {b}°। তৃতীয়টো উলিওৱা।"), "answer": str(180 - a - b), "why": B("Angles add to 180°.", "কোণৰ যোগফল 180°।")}, [(90, 35), (50, 60), (100, 25)]),
    ]}
    return {"id": "math-15-plane", "no": 15, "tier": "A", "face": "geometry", "title": B("Plane figures", "সমতল আকৃতি"), "reign": B("Triangle, quadrilateral, circle", "ত্ৰিভুজ, চতুৰ্ভুজ, বৃত্ত"), "units": [u1, u2, u3, u4], "test": test}


# ---------------------------------------------------------------- Lesson 16
def l16():
    p = "m16"
    flat = B("That is a surface: a covering measured in squares. Volume fills the inside, in cubes.", "সেয়া পৃষ্ঠ: বৰ্গত জোখা আৱৰণ। আয়তনে ভিতৰ ভৰায়, ঘনকত জোখা হয়।")
    third = B("A cone holds only a third of its cylinder, so keep the $\\frac{1}{3}$.", "শংকুত চুঙাৰ এক-তৃতীয়াংশহে ধৰে, সেয়ে $\\frac{1}{3}$ ৰাখিবা।")
    cubed = B("Volume grows with the cube of the length: 3 times the radius is 27 times the volume.", "আয়তন দৈৰ্ঘ্যৰ ঘনৰ হাৰে বাঢ়ে: 3 গুণ ব্যাসাৰ্ধ মানে 27 গুণ আয়তন।")
    u1 = unit("u1", B("Boxes", "বাকচ"), "star", [
        B("Volume of a cuboid = lbh: base area × layers.", "ঘনকাকাৰৰ আয়তন = lbh: ভূমিৰ কালি × স্তৰ।"),
        B("Cube: volume $a^3$, total surface $6a^2$, side faces $4a^2$.", "ঘনক: আয়তন $a^3$, মুঠ পৃষ্ঠ $6a^2$, কাষৰ পৃষ্ঠ $4a^2$।"),
        B("Cuboid surface = 2(lb + bh + hl).", "ঘনকাকাৰৰ পৃষ্ঠ = 2(lb + bh + hl)।"),
        B("1000 cubic cm make 1 litre.", "1000 ঘন ছেমিয়ে 1 লিটাৰ।"),
    ], [
        lab(f"{p}.u1.s1", B("Volume is layers", "আয়তন মানে স্তৰ"), B("A box starts with a floor of 4 by 3 cubes. Each new layer adds that floor again.", "বাকচৰ তলত 4 বাই 3 ঘনক। প্ৰতিটো নতুন স্তৰে একে তল যোগ কৰে।"), {"kind": "stack", "l": 4, "b": 3, "h": 1, "max": 5}, [
            task(B("Build it up to 3 layers.", "3 স্তৰলৈ বনোৱা।"), {"h": 3}, B("12 cubes a layer, 3 layers: 36. That is why volume is length × breadth × height.", "স্তৰত 12টা, 3 স্তৰ: 36। সেয়ে আয়তন = দৈৰ্ঘ্য × প্ৰস্থ × উচ্চতা।")),
        ]),
        lab(f"{p}.u1.s2", B("Surface is what you can wrap", "পৃষ্ঠ মানে মেৰিয়াব পৰা অংশ"), B("Volume fills a box, but surface covers it. Unfold a cube of side 4.", "আয়তনে বাকচ ভৰায়, পৃষ্ঠই ঢাকে। 4 বাহুৰ ঘনক খুলি দিয়া।"), {"kind": "net", "a": 4}, [
            task(B("Unfold the cube.", "ঘনক খুলি দিয়া।"), {"open": 1}, B("Six squares of 16 make 96. Measured in squares, so it is not a volume.", "16ৰ ছটা বৰ্গ, মুঠ 96। বৰ্গত জোখা, সেয়ে ই আয়তন নহয়।")),
        ]),
        explore(f"{p}.u1.q1", "g-solid", lambda l, b, h: {"q": B(f"A tank has a floor of {l} by {b} and volume {l * b * h}. Build it to the right height.", f"টেংকীৰ তল {l} বাই {b}, আয়তন {l * b * h}। সঠিক উচ্চতালৈ বনোৱা।"), "widget": {"kind": "stack", "l": l, "b": b, "h": 1, "max": 6}, "target": h, "answerText": B(f"Height {h}", f"উচ্চতা {h}"), "why": B(f"{l * b * h} ÷ ({l} × {b}).", f"{l * b * h} ÷ ({l} × {b})।")}, [(4, 3, 3), (5, 4, 3), (6, 2, 4)]),
        solve(f"{p}.u1.q2", "g-solid", lambda n: {"q": B(f"How many 1 cm cubes can be cut from a cube of side {n} cm?", f"{n} ছেমি বাহুৰ ঘনকৰ পৰা 1 ছেমি ঘনক কেইটা কাটিব পাৰি?"), "answer": str(n ** 3), "why": B(f"{n} × {n} × {n}.", f"{n} × {n} × {n}।"), "traps": [{"ans": str(6 * n * n), "tag": "m-area-volume", "why": flat}, {"ans": str(n * n), "tag": "m-scale-linear", "why": cubed}]}, [(5,), (10,), (4,), (7,)]),
        stepwise(f"{p}.u1.q3", "g-solid", lambda a: {"q": B(f"A cube has total surface {6 * a * a} sq cm. Find its volume.", f"ঘনকৰ মুঠ পৃষ্ঠ {6 * a * a} বৰ্গ ছেমি। আয়তন উলিওৱা।"), "parts": [
            part(B("Area of one face?", "এটা পৃষ্ঠৰ কালি?"), B(str(a * a), str(a * a)), [B(str(a * a * 2), str(a * a * 2)), B(str(a * a * 3), str(a * a * 3))], B("Divide by 6 faces.", "6টা পৃষ্ঠৰে হৰণ কৰা।"), sid=str(a)),
            part(B("Side?", "বাহু?"), B(str(a), str(a)), [B(str(a * a // 2), str(a * a // 2)), B(str(a + 2), str(a + 2))], B("Square root of the face.", "পৃষ্ঠৰ বৰ্গমূল।"), skill="s-roots", sid=str(a)),
            part(B("Volume?", "আয়তন?"), B(str(a ** 3), str(a ** 3)), [B(str(a * a), str(a * a)), B(str(6 * a * a), str(6 * a * a))], B("Side cubed.", "বাহুৰ ঘন।"), sid=str(a)),
        ], "why": B("Surface gives the face, the face gives the side, and the side gives the volume.", "পৃষ্ঠৰ পৰা মুখ, মুখৰ পৰা বাহু, বাহুৰ পৰা আয়তন।")}, [(4,), (5,), (3,)]),
        solve(f"{p}.u1.q4", "g-solid", lambda l, b, h: {"q": B(f"Find the total surface of a cuboid {l} × {b} × {h} cm.", f"{l} × {b} × {h} ছেমি ঘনকাকাৰৰ মুঠ পৃষ্ঠ উলিওৱা।"), "answer": str(2 * (l * b + b * h + h * l)), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B("Three pairs of faces.", "তিনি যোৰ পৃষ্ঠ।"), "traps": [{"ans": str(l * b * h), "tag": "m-area-volume", "why": flat}, {"ans": str(l * b + b * h + h * l), "tag": "m-perim-half", "why": B("Each face has an opposite twin, so double it.", "প্ৰতিটো পৃষ্ঠৰ বিপৰীত যমজ আছে, সেয়ে দুগুণ কৰা।")}]}, [(5, 4, 3), (10, 6, 4), (8, 5, 2)]),
        tf(f"{p}.u1.q5", "g-solid", B("Doubling a cube's side doubles its volume.", "ঘনকৰ বাহু দুগুণ কৰিলে আয়তন দুগুণ হয়।"), False, B("It is 8 times: the shape grows in three directions.", "ই 8 গুণ: আকৃতি তিনিটা দিশত বাঢ়ে।"), ("m-scale-linear", cubed)),
        solve(f"{p}.u1.q6", "g-solid", lambda l, b, h: {"q": B(f"How many litres does a tank {l} × {b} × {h} cm hold?", f"{l} × {b} × {h} ছেমি টেংকীত কিমান লিটাৰ ধৰে?"), "answer": str(ex(l * b * h, 1000)), "suffix": B("L", "লিটাৰ"), "why": B("1000 cubic cm make 1 litre.", "1000 ঘন ছেমিয়ে 1 লিটাৰ।"), "traps": [{"ans": str(l * b * h), "tag": "m-litre", "why": B("That is cubic centimetres. Divide by 1000 for litres.", "সেয়া ঘন ছেমি। লিটাৰৰ বাবে 1000ৰে হৰণ কৰা।")}]}, [(40, 30, 50), (50, 40, 20), (100, 50, 30)]),
    ])
    u2 = unit("u2", B("Cylinders and cones", "চুঙা আৰু শংকু"), "star", [
        B("Cylinder volume = $\\pi r^2 h$: circle × height.", "চুঙাৰ আয়তন = $\\pi r^2 h$: বৃত্ত × উচ্চতা।"),
        B("Curved surface = $2\\pi rh$: unroll it into a rectangle.", "বক্ৰ পৃষ্ঠ = $2\\pi rh$: মেলিলে আয়ত।"),
        B("Cone volume = $\\frac{1}{3}\\pi r^2 h$.", "শংকুৰ আয়তন = $\\frac{1}{3}\\pi r^2 h$।"),
        B("r matters twice in volume: halving r quarters it.", "আয়তনত r দুবাৰ: r আধা কৰিলে এক-চতুৰ্থাংশ।"),
    ], [
        lab(f"{p}.u2.s1", B("Three cones fill it", "তিনিটা শংকুৱে ভৰায়"), B("This cone and cylinder share a base and a height. How many cones fill the cylinder?", "এই শংকু আৰু চুঙাৰ ভূমি আৰু উচ্চতা একে। কেইটা শংকুৱে চুঙা ভৰাব?"), {"kind": "pour"}, [
            task(B("Pour until the cylinder is full.", "চুঙা নভৰালৈ ঢালা।"), {"n": 3}, B("Exactly three. So a cone is $\\frac{1}{3}\\pi r^2 h$.", "ঠিক তিনিটা। সেয়ে শংকু $\\frac{1}{3}\\pi r^2 h$।")),
        ]),
        diagram(f"{p}.u2.s2", B("Unroll the label", "লেবেল মেলি দিয়া"), [B("Peel the label off a tin: it is a rectangle.", "টিনৰ লেবেল উলিয়ালে ই আয়ত।"), B("Its width is the circumference and its height is the tin's height.", "ইয়াৰ প্ৰস্থ পৰিধি, উচ্চতা টিনৰ উচ্চতা।")], "flow", [B("Width $2\\pi r$", "প্ৰস্থ $2\\pi r$"), B("Height $h$", "উচ্চতা $h$"), B("Area $2\\pi rh$", "কালি $2\\pi rh$")]),
        solve(f"{p}.u2.q1", "g-round", lambda r, h: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, find the volume of a cylinder with radius {r} cm and height {h} cm.", f"$\\pi = \\frac{{22}}{{7}}$ ধৰি {r} ছেমি ব্যাসাৰ্ধ আৰু {h} ছেমি উচ্চতাৰ চুঙাৰ আয়তন উলিওৱা।"), "answer": str(pi(r, r, h)), "suffix": B("cu cm", "ঘন ছেমি"), "why": B(f"$\\frac{{22}}{{7}} \\times {r}^2 \\times {h}$.", f"$\\frac{{22}}{{7}} \\times {r}^2 \\times {h}$।"), "traps": [{"ans": str(pi(2, r, h)), "tag": "m-area-volume", "why": flat}]}, [(7, 5), (14, 10), (7, 10), (21, 2)], hints=[B("Base circle × height.", "ভূমিৰ বৃত্ত × উচ্চতা।")]),
        solve(f"{p}.u2.q2", "g-round", lambda r, h: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, find the curved surface of a cylinder with radius {r} cm and height {h} cm.", f"$\\pi = \\frac{{22}}{{7}}$ ধৰি {r} ছেমি ব্যাসাৰ্ধ আৰু {h} ছেমি উচ্চতাৰ চুঙাৰ বক্ৰ পৃষ্ঠ উলিওৱা।"), "answer": str(pi(2, r, h)), "suffix": B("sq cm", "বৰ্গ ছেমি"), "why": B("The unrolled rectangle.", "মেলি দিয়া আয়ত।"), "traps": [{"ans": str(pi(r, r, h)), "tag": "m-area-volume", "why": B("That is the volume. The curved surface is $2\\pi rh$.", "সেয়া আয়তন। বক্ৰ পৃষ্ঠ $2\\pi rh$।")}]}, [(7, 5), (14, 3), (7, 10)]),
        solve(f"{p}.u2.q3", "g-round", lambda r, h: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, find the volume of a cone with radius {r} cm and height {h} cm.", f"$\\pi = \\frac{{22}}{{7}}$ ধৰি {r} ছেমি ব্যাসাৰ্ধ আৰু {h} ছেমি উচ্চতাৰ শংকুৰ আয়তন উলিওৱা।"), "answer": str(ex(pi(r, r, h), 3)), "suffix": B("cu cm", "ঘন ছেমি"), "why": B("A third of the cylinder.", "চুঙাৰ এক-তৃতীয়াংশ।"), "traps": [{"ans": str(pi(r, r, h)), "tag": "m-cone-third", "why": third}]}, [(7, 12), (21, 10), (14, 6)]),
        tf(f"{p}.u2.q4", "g-round", B("A cone holds half of a cylinder with the same base and height.", "একে ভূমি আৰু উচ্চতাৰ চুঙাৰ আধা শংকুত ধৰে।"), False, B("It takes three cones to fill the cylinder.", "চুঙা ভৰাবলৈ তিনিটা শংকু লাগে।"), ("m-cone-third", third)),
        stepwise(f"{p}.u2.q5", "g-round", lambda rr, hh, ans: {"q": B(f"A cylinder's radius is multiplied by {rr} and its height by {hh}. What happens to its volume?", f"চুঙাৰ ব্যাসাৰ্ধ {rr}ৰে আৰু উচ্চতা {hh}ৰে পূৰণ কৰা হ'ল। আয়তনৰ কি হ'ব?"), "parts": [
            part(B("r appears how many times in the formula?", "সূত্ৰত r কিমান বাৰ?"), B("Twice", "দুবাৰ"), [B("Once", "এবাৰ"), B("Three times", "তিনিবাৰ")], B("$r^2$.", "$r^2$।"), tag="m-scale-linear", sid=str(rr)),
            part(B(f"Effect of the radius?", "ব্যাসাৰ্ধৰ প্ৰভাৱ?"), B(f"× {num(F(rr) ** 2)}", f"× {num(F(rr) ** 2)}"), [B(f"× {num(F(rr) + 1)}", f"× {num(F(rr) + 1)}"), B(f"× {num(F(rr) ** 3)}", f"× {num(F(rr) ** 3)}")], B("Square the multiplier.", "গুণক বৰ্গ কৰা।"), sid=str(rr)),
            part(B("Total effect?", "মুঠ প্ৰভাৱ?"), B(f"× {num(ans)}", f"× {num(ans)}"), [B(f"× {num(F(rr) * hh + 3)}", f"× {num(F(rr) * hh + 3)}"), B(f"× {num(F(rr) + hh)}", f"× {num(F(rr) + hh)}")], B("Multiply by the height's effect.", "উচ্চতাৰ প্ৰভাৱেৰে পূৰণ কৰা।"), sid=str(rr)),
        ], "why": B("Square what is squared, and leave the rest alone.", "বৰ্গ থকাটো বৰ্গ কৰা, বাকীবোৰ একে ৰাখা।")}, [(2, 3, F(12)), (F(1, 2), 2, F(1, 2)), (3, 1, F(9))]),
        match(f"{p}.u2.q6", "g-round", B("Match each solid to its formula", "প্ৰতিটো ঘন আকৃতিক সূত্ৰৰ সৈতে মিলোৱা"), [
            [B("Cylinder volume", "চুঙাৰ আয়তন"), B("$\\pi r^2 h$", "$\\pi r^2 h$")], [B("Cone volume", "শংকুৰ আয়তন"), B("$\\frac{1}{3}\\pi r^2 h$", "$\\frac{1}{3}\\pi r^2 h$")], [B("Curved surface", "বক্ৰ পৃষ্ঠ"), B("$2\\pi rh$", "$2\\pi rh$")], [B("Cuboid volume", "ঘনকাকাৰৰ আয়তন"), B("$lbh$", "$lbh$")],
        ], B("Volumes have three lengths multiplied; surfaces have two.", "আয়তনত তিনিটা দৈৰ্ঘ্য পূৰণ হয়; পৃষ্ঠত দুটা।")),
    ])
    u3 = unit("u3", B("Spheres and recasting", "গোলক আৰু গলাই নতুন ৰূপ"), "star", [
        B("Sphere surface = $4\\pi r^2$; volume = $\\frac{4}{3}\\pi r^3$.", "গোলকৰ পৃষ্ঠ = $4\\pi r^2$; আয়তন = $\\frac{4}{3}\\pi r^3$।"),
        B("Hemisphere total surface = $3\\pi r^2$: curved $2\\pi r^2$ plus the flat circle.", "অৰ্ধগোলকৰ মুঠ পৃষ্ঠ = $3\\pi r^2$: বক্ৰ $2\\pi r^2$ আৰু সমতল বৃত্ত।"),
        B("k times the radius is $k^3$ times the volume.", "k গুণ ব্যাসাৰ্ধ মানে $k^3$ গুণ আয়তন।"),
        B("Melting and recasting keeps the volume the same.", "গলাই নতুন ৰূপ দিলে আয়তন একে থাকে।"),
    ], [
        lab(f"{p}.u3.s1", B("Three directions at once", "একেলগে তিনিটা দিশ"), B("Area grew by the square. A solid grows in three directions, so count the cubes.", "কালি বৰ্গৰ হাৰে বাঢ়ে। ঘন আকৃতি তিনিটা দিশত বাঢ়ে, সেয়ে ঘনক গণা।"), {"kind": "scaleup", "dim": 3, "k": 1, "max": 3}, [
            task(B("Make the side 2 times as long.", "বাহু 2 গুণ দীঘল কৰা।"), {"k": 2}, B("Eight cubes: 2 × 2 × 2.", "আঠটা ঘনক: 2 × 2 × 2।")),
            task(B("Now 3 times.", "এতিয়া 3 গুণ।"), {"k": 3}, B("27 cubes. So a ball of 3 times the radius can be melted into 27 small balls.", "27টা। সেয়ে 3 গুণ ব্যাসাৰ্ধৰ বলৰ পৰা 27টা সৰু বল হয়।")),
        ]),
        diagram(f"{p}.u3.s2", B("Melting keeps the volume", "গলালে আয়তন একে থাকে"), [B("Whatever new shape the metal takes, it is the same amount of metal.", "ধাতুৱে যি ৰূপ লওক, পৰিমাণ একে থাকে।"), B("So set the two volumes equal and cancel what you can.", "সেয়ে দুটা আয়তন সমান কৰি কাটিব পৰাখিনি কাটা।")], "flow", [B("Old volume", "পুৰণি আয়তন"), B("= number × new volume", "= সংখ্যা × নতুন আয়তন"), B("Cancel $\\frac{4}{3}\\pi$", "$\\frac{4}{3}\\pi$ কাটা")]),
        solve(f"{p}.u3.q1", "g-sphere", lambda r: {"q": B(f"The surface of a sphere of radius {r} cm is how many π sq cm?", f"{r} ছেমি ব্যাসাৰ্ধৰ গোলকৰ পৃষ্ঠ কিমান π বৰ্গ ছেমি?"), "answer": str(4 * r * r), "suffix": B("π", "π"), "why": B(f"$4 \\times {r}^2$.", f"$4 \\times {r}^2$।"), "traps": [{"ans": str(2 * r * r), "tag": "m-sphere-hemi", "why": B("That is a hemisphere's curved surface. A whole sphere is $4\\pi r^2$.", "সেয়া অৰ্ধগোলকৰ বক্ৰ পৃষ্ঠ। গোটা গোলক $4\\pi r^2$।")}]}, [(2,), (5,), (9,), (7,)]),
        solve(f"{p}.u3.q2", "g-sphere", lambda r: {"q": B(f"The volume of a sphere of radius {r} cm is how many π cu cm?", f"{r} ছেমি ব্যাসাৰ্ধৰ গোলকৰ আয়তন কিমান π ঘন ছেমি?"), "answer": str(ex(4 * r ** 3, 3)), "suffix": B("π", "π"), "why": B(f"$\\frac{{4}}{{3}} \\times {r}^3$.", f"$\\frac{{4}}{{3}} \\times {r}^3$।"), "traps": [{"ans": str(4 * r * r), "tag": "m-area-volume", "why": flat}]}, [(6,), (9,), (12,)]),
        stepwise(f"{p}.u3.q3", "g-sphere", lambda r: {"q": B(f"A ball has total surface {4 * r * r}π sq cm. Find its radius.", f"বলৰ মুঠ পৃষ্ঠ {4 * r * r}π বৰ্গ ছেমি। ব্যাসাৰ্ধ উলিওৱা।"), "parts": [
            part(B("Cancel π and 4", "π আৰু 4 কাটা"), B(f"$r^2 = {r * r}$", f"$r^2 = {r * r}$"), [B(f"$r^2 = {2 * r * r}$", f"$r^2 = {2 * r * r}$"), B(f"$r = {r * r}$", f"$r = {r * r}$")], B("Divide by 4.", "4ৰে হৰণ কৰা।"), sid=str(r)),
            part(B("Radius?", "ব্যাসাৰ্ধ?"), B(f"{r} cm", f"{r} ছেমি"), [B(f"{r * 2} cm", f"{r * 2} ছেমি"), B(f"{r + 3} cm", f"{r + 3} ছেমি")], B("Square root.", "বৰ্গমূল।"), skill="s-roots", sid=str(r)),
        ], "why": B("Undo the formula one step at a time.", "সূত্ৰ এটা এটাকৈ ওভতোৱা।")}, [(9,), (5,), (7,)]),
        solve(f"{p}.u3.q4", "g-sphere", lambda R, r: {"q": B(f"A sphere of radius {R} cm is melted into spheres of radius {r} cm. How many?", f"{R} ছেমি ব্যাসাৰ্ধৰ গোলক গলাই {r} ছেমি ব্যাসাৰ্ধৰ গোলক বনোৱা হ'ল। কেইটা?"), "answer": str(ex(R ** 3, r ** 3)), "why": B(f"$({R} \\div {r})^3$.", f"$({R} \\div {r})^3$।"), "traps": [{"ans": str(ex(R, r)), "tag": "m-scale-linear", "why": cubed}, {"ans": str(ex(R * R, r * r)), "tag": "m-scale-linear", "why": cubed}]}, [(18, 9), (27, 9), (20, 5), (12, 4)], hints=[B("Volume ratio is the cube of the radius ratio.", "আয়তনৰ অনুপাত ব্যাসাৰ্ধৰ অনুপাতৰ ঘন।")]),
        solve(f"{p}.u3.q5", "g-sphere", lambda r: {"q": B(f"The total surface of a solid hemisphere of radius {r} cm is how many π sq cm?", f"{r} ছেমি ব্যাসাৰ্ধৰ নিৰেট অৰ্ধগোলকৰ মুঠ পৃষ্ঠ কিমান π বৰ্গ ছেমি?"), "answer": str(3 * r * r), "suffix": B("π", "π"), "why": B("Curved $2\\pi r^2$ plus the flat circle $\\pi r^2$.", "বক্ৰ $2\\pi r^2$ আৰু সমতল বৃত্ত $\\pi r^2$।"), "traps": [{"ans": str(2 * r * r), "tag": "m-sphere-hemi", "why": B("You left out the flat circle on top.", "তুমি ওপৰৰ সমতল বৃত্ত এৰিলা।")}]}, [(6,), (7,), (4,)]),
        tf(f"{p}.u3.q6", "g-sphere", B("If a ball's radius doubles, its surface becomes 4 times as big and its volume 8 times.", "বলৰ ব্যাসাৰ্ধ দুগুণ হ'লে পৃষ্ঠ 4 গুণ আৰু আয়তন 8 গুণ হয়।"), True, B("Surfaces scale with the square and volumes with the cube.", "পৃষ্ঠ বৰ্গৰ হাৰে, আয়তন ঘনৰ হাৰে বাঢ়ে।")),
        match(f"{p}.u3.q7", "g-sphere", B("Length multiplied by 3. Match each to the new measure", "দৈৰ্ঘ্য 3 গুণ। প্ৰতিটোক নতুন মাপৰ সৈতে মিলোৱা"), [
            [B("Perimeter", "পৰিসীমা"), B("× 3", "× 3")], [B("Area", "কালি"), B("× 9", "× 9")], [B("Volume", "আয়তন"), B("× 27", "× 27")], [B("A ratio of two lengths", "দুটা দৈৰ্ঘ্যৰ অনুপাত"), B("× 1", "× 1")],
        ], B("Count the lengths multiplied: one, two or three.", "কিমান দৈৰ্ঘ্য পূৰণ হৈছে গণা: এটা, দুটা বা তিনিটা।")),
    ])
    test = {"id": "test", "title": B("Solid figures test", "ঘন আকৃতি পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "g-solid", lambda a: {"q": B(f"A cube of total surface {6 * a * a} sq cm has volume", f"{6 * a * a} বৰ্গ ছেমি মুঠ পৃষ্ঠৰ ঘনকৰ আয়তন"), "right": a ** 3, "wrong": [(6 * a * a * a, "m-area-volume", flat)], "fill": [a * a, 4 * a * a, a ** 3 + a], "unit": " cu cm", "why": B("Find the side first.", "প্ৰথমে বাহু উলিওৱা।")}, [(4,), (6,), (7,)]),
        mcq(f"{p}.t.q2", "g-round", lambda r, h: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, a cylinder of radius {r} and height {h} has volume", f"$\\pi = \\frac{{22}}{{7}}$ ধৰি ব্যাসাৰ্ধ {r}, উচ্চতা {h} চুঙাৰ আয়তন"), "right": pi(r, r, h), "wrong": [(pi(2, r, h), "m-area-volume", flat)], "fill": [pi(r, h), pi(r, r), pi(r, r, h) + 22], "why": B("$\\pi r^2 h$.", "$\\pi r^2 h$।")}, [(7, 4), (14, 2), (7, 6)]),
        mcq(f"{p}.t.q3", "g-round", lambda r, h: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, a cone of radius {r} and height {h} has volume", f"$\\pi = \\frac{{22}}{{7}}$ ধৰি ব্যাসাৰ্ধ {r}, উচ্চতা {h} শংকুৰ আয়তন"), "right": ex(pi(r, r, h), 3), "wrong": [(pi(r, r, h), "m-cone-third", third)], "fill": [ex(pi(r, r, h), 2) if pi(r, r, h) % 2 == 0 else pi(r, h), pi(r, h), ex(pi(r, r, h), 3) + 22], "why": B("A third of the cylinder.", "চুঙাৰ এক-তৃতীয়াংশ।")}, [(7, 6), (7, 9), (14, 3)]),
        mcq(f"{p}.t.q4", "g-sphere", lambda R, r: {"q": B(f"How many spheres of radius {r} can be cast from one of radius {R}?", f"{R} ব্যাসাৰ্ধৰ গোলকৰ পৰা {r} ব্যাসাৰ্ধৰ কেইটা গোলক হ'ব?"), "right": ex(R ** 3, r ** 3), "wrong": [(ex(R, r), "m-scale-linear", cubed)], "fill": [ex(R * R, r * r), ex(R ** 3, r ** 3) * 2, ex(R ** 3, r ** 3) + 4], "why": B("Cube the radius ratio.", "ব্যাসাৰ্ধৰ অনুপাতৰ ঘন লোৱা।")}, [(18, 6), (10, 5), (16, 4)]),
        solve(f"{p}.t.q5", "g-solid", lambda l, b, h: {"q": B(f"Find the volume of a cuboid {l} × {b} × {h} cm.", f"{l} × {b} × {h} ছেমি ঘনকাকাৰৰ আয়তন উলিওৱা।"), "answer": str(l * b * h), "why": B("Length × breadth × height.", "দৈৰ্ঘ্য × প্ৰস্থ × উচ্চতা।")}, [(12, 5, 4), (9, 8, 3), (20, 10, 2)]),
    ]}
    return {"id": "math-16-solids", "no": 16, "tier": "B", "face": "solids", "title": B("Solid figures", "ঘন আকৃতি"), "reign": B("Surface area and volume", "পৃষ্ঠকালি আৰু আয়তন"), "units": [u1, u2, u3], "test": test}
