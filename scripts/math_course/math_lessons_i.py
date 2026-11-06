"""Gap units, part one: every remaining deck pattern in numbers, ratio, percent and money.

Added after reading all 51 decks question by question. New ids only: existing steps are untouched.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from math_kit import B, explore, fr, match, num, odd, order, part, show, solve, stepwise, tf, unit
from math_labs import task
from math_lessons_c import diagram, lab
from math_lessons_h import ex


def lcm(*v):
    out = 1
    for x in v:
        out = out * x // gcd(out, x)
    return out


def number_facts():
    p = "m1.x"
    return unit("u4", B("More number facts", "সংখ্যাৰ আৰু তথ্য"), "star", [
        B("Co-prime numbers share no factor but 1, though neither need be prime.", "সহমৌলিক সংখ্যাৰ উমৈহতীয়া গুণনীয়ক কেৱল 1, যদিও সিহঁত মৌলিক নহ'বও পাৰে।"),
        B("Twin primes differ by 2: 11 and 13.", "যঁজা মৌলিকৰ পাৰ্থক্য 2: 11 আৰু 13।"),
        B("A perfect number equals the sum of its smaller factors: 6 = 1 + 2 + 3.", "নিখুঁত সংখ্যা ইয়াৰ সৰু গুণনীয়কৰ যোগফলৰ সমান: 6 = 1 + 2 + 3।"),
        B("Mixed recurring: all digits minus the plain ones, over 9s then 0s.", "মিশ্ৰ পৌনঃপুনিক: সকলো অংক বিয়োগ সাধাৰণ অংক, তলত 9 তাৰ পিছত 0।"),
    ], [
        lab(f"{p}.s1", B("A number made of its factors", "গুণনীয়কৰ যোগফলেই সংখ্যা"), B("Find every rectangle that 6 dots can make. Each one gives factors.", "6টা বিন্দুৱে বনাব পৰা সকলো আয়ত বিচাৰা। প্ৰতিটোৱে গুণনীয়ক দিয়ে।"), {"kind": "array", "n": 6, "max": 6, "c": 4}, [
            task(B("Find all the factors of 6.", "6ৰ সকলো গুণনীয়ক বিচাৰা।"), {"found": {"gt": 3}}, B("1, 2, 3 and 6. Leave out 6 itself and 1 + 2 + 3 = 6, so 6 is a perfect number. 28 is the next.", "1, 2, 3 আৰু 6। 6 বাদ দিলে 1 + 2 + 3 = 6, সেয়ে 6 নিখুঁত সংখ্যা। পিছৰটো 28।")),
        ]),
        diagram(f"{p}.s2", B("When only some digits repeat", "কিছু অংকহে ঘূৰিলে"), [B("In $0.4\\overline{2}$, the 4 stays once and the 2 repeats for ever.", "$0.4\\overline{2}$ত 4 এবাৰ থাকে, 2 সদায় ঘূৰে।"), B("Take all the digits, subtract the plain ones, and write 9 for each repeating digit and 0 for each plain one.", "সকলো অংকৰ পৰা সাধাৰণ অংক বিয়োগ কৰি ঘূৰা অংকৰ বাবে 9, সাধাৰণ অংকৰ বাবে 0 লিখা।")], "flow", [B("42 − 4 = 38", "42 − 4 = 38"), B("One repeating, one plain: 90", "এটা ঘূৰা, এটা সাধাৰণ: 90"), B("$\\frac{38}{90} = \\frac{19}{45}$", "$\\frac{38}{90} = \\frac{19}{45}$")]),
        solve(f"{p}.q1", "f-dec", lambda tex, ans, top, bot: {"q": B(f"Write ${tex}$ as a fraction.", f"${tex}$ক ভগ্নাংশ হিচাপে লিখা।"), "answer": ans, "why": B(f"$\\frac{{{top}}}{{{bot}}}$, then simplify.", f"$\\frac{{{top}}}{{{bot}}}$, তাৰ পিছত সৰল কৰা।")}, [("0.4\\overline{2}", "19/45", 38, 90), ("0.1\\overline{6}", "1/6", 15, 90), ("0.8\\overline{3}", "5/6", 75, 90), ("0.5\\overline{27}", "29/55", 522, 990)], hints=[B("All digits minus the plain digit, over 9s then 0.", "সকলো অংক বিয়োগ সাধাৰণ অংক, তলত 9 তাৰ পিছত 0।")]),
        solve(f"{p}.q2", "f-dec", lambda a, b: {"q": B(f"Add $0.\\overline{{{a}}} + 0.\\overline{{{b}}}$ as a fraction.", f"$0.\\overline{{{a}}} + 0.\\overline{{{b}}}$ ভগ্নাংশত যোগ কৰা।"), "answer": num(F(a + b, 9)), "why": B(f"$\\frac{{{a}}}{{9}} + \\frac{{{b}}}{{9}}$.", f"$\\frac{{{a}}}{{9}} + \\frac{{{b}}}{{9}}$।"), "traps": [{"ans": num(F(a + b, 10)), "tag": "m-recur-ten", "why": B("Repeating digits go over 9, not 10.", "ঘূৰা অংক 9ৰ ওপৰত, 10ৰ ওপৰত নহয়।")}]}, [(2, 3), (4, 2), (1, 6), (5, 3)]),
        tf(f"{p}.q3", "n-facts", B("Co-prime numbers must both be prime.", "সহমৌলিক সংখ্যা দুয়োটা মৌলিক হ'বই লাগিব।"), False, B("8 and 15 are co-prime, and neither is prime. They only need to share no factor.", "8 আৰু 15 সহমৌলিক, এটাও মৌলিক নহয়। উমৈহতীয়া গুণনীয়ক নাথাকিলেই হ'ল।"), ("m-coprime", B("Co-prime describes a pair, not each number alone.", "সহমৌলিক যোৰাৰ কথা, প্ৰতিটো সংখ্যাৰ নহয়।"))),
        stepwise(f"{p}.q4", "n-facts", lambda n, fs, tot: {"q": B(f"Is {n} a perfect number?", f"{n} নিখুঁত সংখ্যা নেকি?"), "parts": [
            part(B("Its factors, leaving out itself?", "নিজক বাদ দি গুণনীয়ক?"), B(fs, fs), [B("1, 2 only", "কেৱল 1, 2"), B(f"1, {n}", f"1, {n}")], B("Find every rectangle.", "সকলো আয়ত বিচাৰা।"), skill="n-factor", sid=str(n)),
            part(B("Their sum?", "যোগফল?"), B(str(tot), str(tot)), [B(str(tot + 2), str(tot + 2)), B(str(tot - 3), str(tot - 3))], B("Add them.", "যোগ কৰা।"), sid=str(n)),
            part(B("So is it perfect?", "তেনেহ'লে নিখুঁত নে?"), B("Yes" if tot == n else "No", "হয়" if tot == n else "নহয়"), [B("No" if tot == n else "Yes", "নহয়" if tot == n else "হয়")], B("It must equal the number.", "সংখ্যাটোৰ সমান হ'ব লাগিব।"), sid=str(n)),
        ], "why": B("6, 28 and 496 are the first perfect numbers.", "6, 28 আৰু 496 প্ৰথম নিখুঁত সংখ্যা।")}, [(28, "1, 2, 4, 7, 14", 28), (12, "1, 2, 3, 4, 6", 16), (6, "1, 2, 3", 6)]),
        match(f"{p}.q5", "n-facts", B("Match each Roman numeral", "প্ৰতিটো ৰোমান সংখ্যা মিলোৱা"), [
            [B("IX", "IX"), B("9", "9")], [B("XL", "XL"), B("40", "40")], [B("XC", "XC"), B("90", "90")], [B("CD", "CD"), B("400", "400")],
        ], B("A smaller letter before a bigger one subtracts.", "ডাঙৰৰ আগত সৰু আখৰ থাকিলে বিয়োগ হয়।")),
        solve(f"{p}.q6", "n-facts", lambda b: {"q": B(f"Write the binary number {b} in the decimal system.", f"দ্বিমিক সংখ্যা {b}ক দশমিকত লিখা।"), "answer": str(int(b, 2)), "why": B("Each place doubles: 1, 2, 4, 8 from the right.", "প্ৰতিটো স্থান দুগুণ: সোঁফালৰ পৰা 1, 2, 4, 8।")}, [("101",), ("110",), ("1010",), ("1101",)], hints=[B("Place values are 8, 4, 2, 1.", "স্থানীয় মান 8, 4, 2, 1।")]),
        order(f"{p}.q7", "f-dec", B("Put these in order, smallest first", "সৰুৰ পৰা ডাঙৰলৈ সজোৱা"), [B("$0.\\overline{06}$", "$0.\\overline{06}$"), B("$0.0\\overline{6}$", "$0.0\\overline{6}$"), B("$0.6$", "$0.6$"), B("$0.\\overline{6}$", "$0.\\overline{6}$")], B("Write out a few digits of each: 0.0606, 0.0666, 0.6000, 0.6666.", "প্ৰতিটোৰ কেইটামান অংক লিখা: 0.0606, 0.0666, 0.6000, 0.6666।")),
    ])


def lcm_more():
    p = "m2.x"
    swap = B("For fractions the rule mixes: LCM uses LCM of tops and HCF of bottoms.", "ভগ্নাংশত নিয়ম মিহলি: ল.সা.গু.ত লবৰ ল.সা.গু. আৰু হৰৰ গ.সা.গু.।")
    return unit("u4", B("Harder LCM problems", "ল.সা.গু.ৰ টান সমস্যা"), "star", [
        B("LCM of fractions = LCM of tops ÷ HCF of bottoms.", "ভগ্নাংশৰ ল.সা.গু. = লবৰ ল.সা.গু. ÷ হৰৰ গ.সা.গু.।"),
        B("HCF of fractions = HCF of tops ÷ LCM of bottoms.", "ভগ্নাংশৰ গ.সা.গু. = লবৰ গ.সা.গু. ÷ হৰৰ ল.সা.গু.।"),
        B("Given LCM + HCF and LCM − HCF, halve the sum and the difference.", "ল.সা.গু. + গ.সা.গু. আৰু ল.সা.গু. − গ.সা.গু. দিলে যোগফল আৰু বিয়োগফল আধা কৰা।"),
        B("For co-prime numbers, the LCM is their product.", "সহমৌলিক সংখ্যাৰ ল.সা.গু. সিহঁতৰ পূৰণফল।"),
    ], [
        lab(f"{p}.s1", B("Fractions hop too", "ভগ্নাংশেও জঁপিয়ায়"), B("Hop by $\\frac{2}{3}$ and by $\\frac{1}{2}$ along the line. Where do they first meet?", "ৰেখাত $\\frac{2}{3}$ আৰু $\\frac{1}{2}$ৰে জঁপিওৱা। ক'ত প্ৰথম লগ হয়?"), {"kind": "line", "min": 0, "max": 3, "den": 6, "value": 0.5}, [
            task(B("Put the pin on 2.", "পিনটো 2ত ৰাখা।"), {"value": 2}, B("2 is three hops of $\\frac{2}{3}$ and four of $\\frac{1}{2}$. LCM of tops 2 and 1 is 2, HCF of bottoms is 1: 2.", "2 হৈছে $\\frac{2}{3}$ৰ তিনি জঁপ আৰু $\\frac{1}{2}$ৰ চাৰি জঁপ। লবৰ ল.সা.গু. 2, হৰৰ গ.সা.গু. 1: 2।")),
        ]),
        diagram(f"{p}.s2", B("Sum and difference given", "যোগফল আৰু বিয়োগফল দিয়া"), [B("If LCM + HCF = 52 and LCM − HCF = 44, adding the two removes the HCF.", "ল.সা.গু. + গ.সা.গু. = 52 আৰু ল.সা.গু. − গ.সা.গু. = 44 হ'লে যোগ কৰিলে গ.সা.গু. নোহোৱা হয়।"), B("That leaves twice the LCM.", "বাকী থাকে ল.সা.গু.ৰ দুগুণ।")], "flow", [B("52 + 44 = 96", "52 + 44 = 96"), B("LCM = 48", "ল.সা.গু. = 48"), B("HCF = 4", "গ.সা.গু. = 4")]),
        solve(f"{p}.q1", "l-frac", lambda a, b, c, d: {"q": B(f"Find the LCM of ${fr(a, b)}$ and ${fr(c, d)}$.", f"${fr(a, b)}$ আৰু ${fr(c, d)}$ৰ ল.সা.গু. উলিওৱা।"), "answer": num(F(lcm(a, c), gcd(b, d))), "why": B(f"LCM of tops {lcm(a, c)}, HCF of bottoms {gcd(b, d)}.", f"লবৰ ল.সা.গু. {lcm(a, c)}, হৰৰ গ.সা.গু. {gcd(b, d)}।"), "traps": [{"ans": num(F(lcm(a, c), lcm(b, d))), "tag": "m-frac-lcm", "why": swap}]}, [(2, 3, 4, 9), (3, 4, 9, 8), (2, 5, 3, 10), (4, 9, 6, 15)], hints=[B("LCM on top, HCF below.", "ওপৰত ল.সা.গু., তলত গ.সা.গু.।")]),
        solve(f"{p}.q2", "l-frac", lambda a, b, c, d: {"q": B(f"Find the HCF of ${fr(a, b)}$ and ${fr(c, d)}$.", f"${fr(a, b)}$ আৰু ${fr(c, d)}$ৰ গ.সা.গু. উলিওৱা।"), "answer": num(F(gcd(a, c), lcm(b, d))), "why": B(f"HCF of tops {gcd(a, c)}, LCM of bottoms {lcm(b, d)}.", f"লবৰ গ.সা.গু. {gcd(a, c)}, হৰৰ ল.সা.গু. {lcm(b, d)}।"), "traps": [{"ans": num(F(gcd(a, c), gcd(b, d))), "tag": "m-frac-lcm", "why": swap}]}, [(2, 3, 4, 9), (3, 4, 9, 8), (4, 5, 6, 15)]),
        stepwise(f"{p}.q3", "l-apply", lambda s_, d, a: {"q": B(f"The LCM and HCF of two numbers add to {s_} and differ by {d}. One number is {a}. Find the other.", f"দুটা সংখ্যাৰ ল.সা.গু. আৰু গ.সা.গু.ৰ যোগফল {s_}, পাৰ্থক্য {d}। এটা সংখ্যা {a}। আনটো উলিওৱা।"), "parts": [
            part(B("LCM?", "ল.সা.গু.?"), B(str(ex(s_ + d, 2)), str(ex(s_ + d, 2))), [B(str(s_ + d), str(s_ + d)), B(str(ex(s_ - d, 2)), str(ex(s_ - d, 2)))], B("Half of sum + difference.", "যোগফল + বিয়োগফলৰ আধা।"), sid=str(a)),
            part(B("HCF?", "গ.সা.গু.?"), B(str(ex(s_ - d, 2)), str(ex(s_ - d, 2))), [B(str(s_ - d), str(s_ - d)), B(str(ex(s_ + d, 2)), str(ex(s_ + d, 2)))], B("Half of sum − difference.", "যোগফল − বিয়োগফলৰ আধা।"), sid=str(a)),
            part(B("The other number?", "আনটো সংখ্যা?"), B(str(ex(ex(s_ + d, 2) * ex(s_ - d, 2), a)), str(ex(ex(s_ + d, 2) * ex(s_ - d, 2), a))), [B(str(a), str(a)), B(str(ex(s_ + d, 2)), str(ex(s_ + d, 2)))], B("LCM × HCF ÷ the number.", "ল.সা.গু. × গ.সা.গু. ÷ সংখ্যা।"), sid=str(a)),
        ], "why": B("Two equations in LCM and HCF, then the product rule.", "ল.সা.গু. আৰু গ.সা.গু.ৰ দুটা সমীকৰণ, তাৰ পিছত পূৰণফলৰ নিয়ম।")}, [(52, 44, 12), (66, 54, 12), (84, 60, 24)]),
        solve(f"{p}.q4", "l-apply", lambda a, b, c, l: {"q": B(f"Three numbers are in the ratio {a} : {b} : {c} and their LCM is {l}. Find their HCF.", f"তিনিটা সংখ্যাৰ অনুপাত {a} : {b} : {c}, ল.সা.গু. {l}। গ.সা.গু. উলিওৱা।"), "answer": str(ex(l, lcm(a, b, c))), "why": B(f"The numbers are {a}x, {b}x and {c}x, so the LCM is {lcm(a, b, c)}x and x is the HCF.", f"সংখ্যাবোৰ {a}x, {b}x, {c}x, সেয়ে ল.সা.গু. {lcm(a, b, c)}x, x গ.সা.গু.।")}, [(2, 3, 7, 2100), (2, 3, 4, 240), (3, 5, 7, 2100)]),
        tf(f"{p}.q5", "l-apply", B("The LCM of two co-prime numbers is their product.", "দুটা সহমৌলিক সংখ্যাৰ ল.সা.গু. সিহঁতৰ পূৰণফল।"), True, B("Their HCF is 1, so LCM = product ÷ 1.", "গ.সা.গু. 1, সেয়ে ল.সা.গু. = পূৰণফল ÷ 1।")),
        odd(f"{p}.q7", "l-apply", lambda a, b, r, x, y, z: {"q": B(f"Two numbers are in the ratio {a} : {b}. Which cannot be their LCM?", f"দুটা সংখ্যাৰ অনুপাত {a} : {b}। কোনটো সিহঁতৰ ল.সা.গু. হ'ব নোৱাৰে?"), "right": r, "fill": [x, y, z], "why": B(f"The numbers are {a}x and {b}x, so the LCM is {a * b}x. Every possible LCM is a multiple of {a * b}.", f"সংখ্যাবোৰ {a}x আৰু {b}x, সেয়ে ল.সা.গু. {a * b}x। প্ৰতিটো ল.সা.গু. {a * b}ৰ গুণিতক।")}, [(4, 3, 50, 24, 36, 60), (7, 2, 40, 14, 28, 70), (3, 8, 30, 24, 48, 72)]),
        match(f"{p}.q6", "l-frac", B("Match each pair of fractions to its LCM", "প্ৰতিটো ভগ্নাংশৰ যোৰক ল.সা.গু.ৰ সৈতে মিলোৱা"), [
            [B("$\\frac{1}{2}$, $\\frac{1}{3}$", "$\\frac{1}{2}$, $\\frac{1}{3}$"), B("1", "1")], [B("$\\frac{2}{3}$, $\\frac{4}{9}$", "$\\frac{2}{3}$, $\\frac{4}{9}$"), B("$\\frac{4}{3}$", "$\\frac{4}{3}$")], [B("$\\frac{3}{4}$, $\\frac{9}{8}$", "$\\frac{3}{4}$, $\\frac{9}{8}$"), B("$\\frac{9}{4}$", "$\\frac{9}{4}$")], [B("$\\frac{1}{4}$, $\\frac{1}{6}$", "$\\frac{1}{4}$, $\\frac{1}{6}$"), B("$\\frac{1}{2}$", "$\\frac{1}{2}$")],
        ], B("LCM of tops over HCF of bottoms.", "লবৰ ল.সা.গু. ভাগ হৰৰ গ.সা.গু.।")),
    ])


def word_fraction():
    return solve("m3.u3.q7", "f-of", lambda a, b, c, d, gap: {"q": B(f"${fr(a, b)}$ of a number is {gap} more than ${fr(c, d)}$ of it. Find the number.", f"এটা সংখ্যাৰ ${fr(a, b)}$ অংশ ইয়াৰ ${fr(c, d)}$ অংশতকৈ {gap} বেছি। সংখ্যাটো উলিওৱা।"), "answer": num(F(gap) / (F(a, b) - F(c, d))), "why": B(f"The gap is ${num(F(a, b) - F(c, d))}$ of the number, and that part is {gap}.", f"পাৰ্থক্য সংখ্যাৰ ${num(F(a, b) - F(c, d))}$ অংশ, সেই অংশ {gap}।")}, [(3, 5, 1, 2, 10), (2, 3, 1, 4, 20), (3, 4, 2, 3, 5)], hints=[B("Subtract the two fractions first.", "প্ৰথমে দুটা ভগ্নাংশ বিয়োগ কৰা।")])


def cubes():
    p = "m4.c"
    return unit("u4", B("Cubes and cube roots", "ঘন আৰু ঘনমূল"), "star", [
        B("$n^3$ is the volume of a cube of side n; $\\sqrt[3]{n}$ is the side.", "$n^3$ হৈছে n বাহুৰ ঘনকৰ আয়তন; $\\sqrt[3]{n}$ হৈছে বাহু।"),
        B("A perfect cube has every prime in groups of three.", "পূৰ্ণঘনত প্ৰতিটো মৌলিক তিনিটাৰ গোটত থাকে।"),
        B("To make a perfect cube, supply what each group is short of.", "পূৰ্ণঘন কৰিবলৈ প্ৰতিটো গোটৰ অভাৱ পূৰণ কৰা।"),
        B("A root and a cube root of one number are different: $\\sqrt{64} = 8$, $\\sqrt[3]{64} = 4$.", "একে সংখ্যাৰ বৰ্গমূল আৰু ঘনমূল বেলেগ: $\\sqrt{64} = 8$, $\\sqrt[3]{64} = 4$।"),
    ], [
        lab(f"{p}.s1", B("A cube root is an edge", "ঘনমূল মানে কাষ"), B("$\\sqrt[3]{27}$ asks what edge builds a cube of 27 small cubes.", "$\\sqrt[3]{27}$ই সোধে কোন কাষে 27টা সৰু ঘনকৰ ঘনক বনায়।"), {"kind": "scaleup", "dim": 3, "k": 1, "max": 4}, [
            task(B("Build the cube with edge 3.", "3 কাষৰ ঘনক বনোৱা।"), {"k": 3}, B("3 × 3 × 3 = 27, so $\\sqrt[3]{27} = 3$.", "3 × 3 × 3 = 27, সেয়ে $\\sqrt[3]{27} = 3$।")),
        ]),
        lab(f"{p}.s2", B("Groups of three", "তিনিটাৰ গোট"), B("A square needs pairs. A cube needs threes. Group the primes of 8788.", "বৰ্গত যোৰা লাগে। ঘনত তিনিটা লাগে। 8788ৰ মৌলিক গোট কৰা।"), {"kind": "pairs", "n": 8788, "group": 3}, [
            task(B("Tap three matching primes to group them.", "একে তিনিটা মৌলিক টিপি গোট কৰা।"), {"done": 1}, B("The 13s make a group, but 2 × 2 is one short. Multiply by 2 for a perfect cube.", "13ৰ গোট হ'ল, কিন্তু 2 × 2ত এটা কম। পূৰ্ণঘনৰ বাবে 2ৰে পূৰণ কৰা।")),
        ]),
        explore(f"{p}.q1", "s-cube", lambda n, m: {"q": B(f"Group the primes of {n}. What is the least number to multiply by to make a perfect cube?", f"{n}ৰ মৌলিক গোট কৰা। পূৰ্ণঘন কৰিবলৈ আটাইতকৈ সৰু কিহেৰে পূৰণ কৰিব লাগিব?"), "widget": {"kind": "pairs", "n": n, "group": 3}, "target": m, "answerText": B(f"Multiply by {m}", f"{m}ৰে পূৰণ"), "why": B(f"{n} × {m} = {n * m}, a perfect cube.", f"{n} × {m} = {n * m}, এটা পূৰ্ণঘন।")}, [(243, 3), (1372, 2), (250, 4), (72, 3)]),
        solve(f"{p}.q2", "s-cube", lambda n: {"q": B(f"Find $\\sqrt[3]{{{n ** 3}}}$", f"$\\sqrt[3]{{{n ** 3}}}$ উলিওৱা"), "answer": str(n), "why": B(f"{n} × {n} × {n} = {n ** 3}.", f"{n} × {n} × {n} = {n ** 3}।"), "traps": [{"ans": str(ex(n ** 3, 3)), "tag": "m-cube-three", "why": B("A cube root is not division by 3. Find the number multiplied by itself three times.", "ঘনমূল 3ৰে হৰণ নহয়। নিজেৰে তিনিবাৰ পূৰণ হোৱা সংখ্যা বিচাৰা।")}]}, [(6,), (9,), (12,), (15,)], hints=[B("Peel into primes and take one from each group.", "মৌলিকলৈ ভাঙি প্ৰতিটো গোটৰ এটা লোৱা।")]),
        solve(f"{p}.q3", "s-cube", lambda r: {"q": B(f"Find $\\sqrt{{{r ** 6}}} - \\sqrt[3]{{{r ** 6}}}$", f"$\\sqrt{{{r ** 6}}} - \\sqrt[3]{{{r ** 6}}}$ উলিওৱা"), "answer": str(r ** 3 - r ** 2), "why": B(f"{r ** 3} − {r ** 2}.", f"{r ** 3} − {r ** 2}।")}, [(2,), (3,), (4,)]),
        tf(f"{p}.q4", "s-cube", B("$\\sqrt{64}$ and $\\sqrt[3]{64}$ are equal.", "$\\sqrt{64}$ আৰু $\\sqrt[3]{64}$ সমান।"), False, B("One is 8 and the other is 4.", "এটা 8, আনটো 4।")),
        match(f"{p}.q5", "s-cube", B("Match each number to its cube", "প্ৰতিটো সংখ্যাক ঘনৰ সৈতে মিলোৱা"), [
            [B("3", "3"), B("27", "27")], [B("5", "5"), B("125", "125")], [B("7", "7"), B("343", "343")], [B("10", "10"), B("1000", "1000")],
        ], B("Cubes to 10 are worth knowing by heart.", "10লৈ ঘন মুখস্থ ৰখাটো লাভজনক।")),
    ])


def surds():
    p = "m4.s"
    trapmid = B("The roots disappear only in the (a + b)(a − b) pattern. Use it before multiplying out.", "মূল কেৱল (a + b)(a − b) আৰ্হিতে নোহোৱা হয়। পূৰণৰ আগতে ইয়াক লোৱা।")
    return unit("u5", B("Surds and big identities", "কৰণী আৰু ডাঙৰ অভেদ"), "star", [
        B("$(a + \\sqrt{b})(a - \\sqrt{b}) = a^2 - b$: the root vanishes.", "$(a + \\sqrt{b})(a - \\sqrt{b}) = a^2 - b$: মূল নোহোৱা হয়।"),
        B("$\\frac{a^3 + b^3}{a^2 - ab + b^2} = a + b$.", "$\\frac{a^3 + b^3}{a^2 - ab + b^2} = a + b$।"),
        B("$\\frac{a^3 - b^3}{a^2 + ab + b^2} = a - b$.", "$\\frac{a^3 - b^3}{a^2 + ab + b^2} = a - b$।"),
        B("$\\frac{a + b}{a - b} + \\frac{a - b}{a + b} = \\frac{2(a^2 + b^2)}{a^2 - b^2}$.", "$\\frac{a + b}{a - b} + \\frac{a - b}{a + b} = \\frac{2(a^2 + b^2)}{a^2 - b^2}$।"),
    ], [
        lab(f"{p}.s1", B("The root that disappears", "নোহোৱা হোৱা মূল"), B("The strip from before works with roots too: the difference of two squares has no root left in it.", "আগৰ পট্টী মূলতো চলে: দুটা বৰ্গৰ বিয়োগফলত মূল নাথাকে।"), {"kind": "diffsq", "a": 7, "b": 2}, [
            task(B("Slide the strip.", "পট্টী সৰোৱা।"), {"moved": 1}, B("$(7 + 2)(7 - 2) = 7^2 - 2^2$. In the same way $(8 + 3\\sqrt{6})(8 - 3\\sqrt{6}) = 64 - 54 = 10$.", "$(7 + 2)(7 - 2) = 7^2 - 2^2$। একেদৰে $(8 + 3\\sqrt{6})(8 - 3\\sqrt{6}) = 64 - 54 = 10$।")),
        ]),
        diagram(f"{p}.s2", B("Huge numbers, tiny work", "ডাঙৰ সংখ্যা, সৰু কাম"), [B("A sum of cubes factorises, so a frightening fraction often cancels to a simple sum.", "ঘনৰ যোগফলৰ উৎপাদক হয়, সেয়ে ভয়লগা ভগ্নাংশ প্ৰায়ে সৰল যোগফল হয়।"), B("Look for the pattern before you touch the numbers.", "সংখ্যা ছোৱাৰ আগতে আৰ্হি বিচাৰা।")], "flow", [B("$a^3 + b^3$", "$a^3 + b^3$"), B("$(a + b)(a^2 - ab + b^2)$", "$(a + b)(a^2 - ab + b^2)$"), B("Cancels to $a + b$", "কাটিলে $a + b$")]),
        solve(f"{p}.q1", "s-surd", lambda a, b, c: {"q": B(f"Find $({a} - {b}\\sqrt{{{c}}})({a} + {b}\\sqrt{{{c}}})$", f"$({a} - {b}\\sqrt{{{c}}})({a} + {b}\\sqrt{{{c}}})$ উলিওৱা"), "answer": str(a * a - b * b * c), "why": B(f"${a}^2 - ({b}\\sqrt{{{c}}})^2 = {a * a} - {b * b * c}$.", f"${a}^2 - ({b}\\sqrt{{{c}}})^2 = {a * a} - {b * b * c}$।"), "traps": [{"ans": str(a * a - b * c), "tag": "m-surd-square", "why": B(f"Square the whole of {b}√{c}: both the {b} and the root.", f"{b}√{c} গোটেইটো বৰ্গ কৰা: {b} আৰু মূল দুয়োটা।")}]}, [(8, 3, 6), (5, 2, 3), (6, 2, 7), (9, 4, 5)], hints=[B("It is $a^2 - b^2$ with $b = $ the whole root term.", "ই $a^2 - b^2$, য'ত $b$ গোটেই মূলৰ পদ।")]),
        solve(f"{p}.q2", "s-surd", lambda a, b: {"q": B(f"Find $\\frac{{{a}^3 + {b}^3}}{{{a}^2 - {a} \\times {b} + {b}^2}}$", f"$\\frac{{{a}^3 + {b}^3}}{{{a}^2 - {a} \\times {b} + {b}^2}}$ উলিওৱা"), "answer": str(a + b), "why": B("It cancels to a + b.", "কাটিলে a + b হয়।"), "traps": [{"ans": str(abs(a - b)), "tag": "m-surd-square", "why": trapmid}]}, [(8, 3), (416, 184), (73, 27)], hints=[B("Spot the sum of cubes on top.", "ওপৰত ঘনৰ যোগফল চিনি পোৱা।")]),
        solve(f"{p}.q3", "s-surd", lambda a, b: {"q": B(f"Find $\\frac{{{a}^3 - {b}^3}}{{{a}^2 + {a} \\times {b} + {b}^2}}$", f"$\\frac{{{a}^3 - {b}^3}}{{{a}^2 + {a} \\times {b} + {b}^2}}$ উলিওৱা"), "answer": str(a - b), "why": B("It cancels to a − b.", "কাটিলে a − b হয়।")}, [(640, 315), (9, 4), (120, 45)]),
        stepwise(f"{p}.q4", "s-surd", lambda x, y: {"q": B(f"Find $\\frac{{\\sqrt{{{x}}} + \\sqrt{{{y}}}}}{{\\sqrt{{{x}}} - \\sqrt{{{y}}}}} + \\frac{{\\sqrt{{{x}}} - \\sqrt{{{y}}}}}{{\\sqrt{{{x}}} + \\sqrt{{{y}}}}}$", f"$\\frac{{\\sqrt{{{x}}} + \\sqrt{{{y}}}}}{{\\sqrt{{{x}}} - \\sqrt{{{y}}}}} + \\frac{{\\sqrt{{{x}}} - \\sqrt{{{y}}}}}{{\\sqrt{{{x}}} + \\sqrt{{{y}}}}}$ উলিওৱা"), "parts": [
            part(B("Which pattern?", "কোন আৰ্হি?"), B("$\\frac{2(a^2 + b^2)}{a^2 - b^2}$", "$\\frac{2(a^2 + b^2)}{a^2 - b^2}$"), [B("$\\frac{4ab}{a^2 - b^2}$", "$\\frac{4ab}{a^2 - b^2}$"), B("$a + b$", "$a + b$")], B("A sum of the two fractions, not a difference.", "দুটা ভগ্নাংশৰ যোগফল, বিয়োগফল নহয়।"), sid=str(x)),
            part(B("$a^2 + b^2$ and $a^2 - b^2$?", "$a^2 + b^2$ আৰু $a^2 - b^2$?"), B(f"{x + y} and {x - y}", f"{x + y} আৰু {x - y}"), [B(f"{x * y} and {x - y}", f"{x * y} আৰু {x - y}"), B(f"{x - y} and {x + y}", f"{x - y} আৰু {x + y}")], B("Squaring removes the roots.", "বৰ্গ কৰিলে মূল নোহোৱা হয়।"), sid=str(x)),
            part(B("Value?", "মান?"), B(num(F(2 * (x + y), x - y)), num(F(2 * (x + y), x - y))), [B(num(F(x + y, x - y)), num(F(x + y, x - y))), B(num(F(2 * (x + y), x - y) + 2), num(F(2 * (x + y), x - y) + 2))], B("Put them into the pattern.", "আৰ্হিত বহুওৱা।"), sid=str(x)),
        ], "why": B("The pattern replaces a page of working.", "আৰ্হিয়ে এক পৃষ্ঠাৰ কাম কৰে।")}, [(3, 2), (2, 1), (7, 5)]),
        solve(f"{p}.q5", "s-surd", lambda a, b: {"q": B(f"Find $\\sqrt{{\\sqrt{{{a}}} + \\sqrt{{{b}}}}} - \\sqrt{{\\sqrt{{{b}}} - \\sqrt{{{a}}}}}$", f"$\\sqrt{{\\sqrt{{{a}}} + \\sqrt{{{b}}}}} - \\sqrt{{\\sqrt{{{b}}} - \\sqrt{{{a}}}}}$ উলিওৱা"), "answer": str(isqrt(isqrt(a) + isqrt(b)) - isqrt(isqrt(b) - isqrt(a))), "why": B("Work from the inside out.", "ভিতৰৰ পৰা বাহিৰলৈ কৰা।")}, [(36, 100), (16, 25), (144, 169)]),
        tf(f"{p}.q6", "s-surd", B("$(a + b)^3 = a^3 + b^3$", "$(a + b)^3 = a^3 + b^3$"), False, B("It also has $3ab(a + b)$: try 1 and 1, which gives 8 against 2.", "ইয়াত $3ab(a + b)$ও থাকে: 1 আৰু 1 ল'লে 8 আৰু 2 হয়।"), ("m-square-spread", B("Powers do not split across a plus sign.", "ঘাত যোগৰ ওপৰত নাভাঙে।"))),
        match(f"{p}.q7", "s-surd", B("Match each expression to its short form", "প্ৰতিটো ৰাশিক চুটি ৰূপৰ সৈতে মিলোৱা"), [
            [B("$a^3 + b^3$", "$a^3 + b^3$"), B("$(a + b)(a^2 - ab + b^2)$", "$(a + b)(a^2 - ab + b^2)$")], [B("$a^3 - b^3$", "$a^3 - b^3$"), B("$(a - b)(a^2 + ab + b^2)$", "$(a - b)(a^2 + ab + b^2)$")], [B("$(a + b)^3$", "$(a + b)^3$"), B("$a^3 + b^3 + 3ab(a + b)$", "$a^3 + b^3 + 3ab(a + b)$")], [B("$\\frac{(a + b)^2}{a^2 - b^2}$", "$\\frac{(a + b)^2}{a^2 - b^2}$"), B("$\\frac{a + b}{a - b}$", "$\\frac{a + b}{a - b}$")],
        ], B("Each one turns a long sum into a cancel.", "প্ৰতিটোৱে দীঘল হিচাপক কটাকটিলৈ নিয়ে।")),
    ])


def percent_more():
    p = "m5.x"
    return unit("u4", B("Side-by-side change", "কাষে কাষে পৰিৱৰ্তন"), "star", [
        B("Two equal numbers raised by x% and y% end in the ratio (100 + x) : (100 + y).", "দুটা সমান সংখ্যা x% আৰু y% বাঢ়িলে অনুপাত (100 + x) : (100 + y) হয়।"),
        B("A fall of x% is written as 100 − x.", "x% হ্ৰাস 100 − x বুলি লিখা হয়।"),
        B("Spending = price × use, so a fixed spend is a fixed area.", "খৰচ = দাম × ব্যৱহাৰ, সেয়ে নিৰ্দিষ্ট খৰচ মানে নিৰ্দিষ্ট কালি।"),
        B("If a price falls r%, use can rise by $\\frac{r}{100 - r} \\times 100$%.", "দাম r% কমিলে ব্যৱহাৰ $\\frac{r}{100 - r} \\times 100$% বাঢ়িব পাৰে।"),
    ], [
        diagram(f"{p}.s1", B("Change the base to 100", "ভিত্তি 100 কৰা"), [B("If two numbers start level, take each as 100 and apply its own change.", "দুটা সংখ্যা সমানৰ পৰা আৰম্ভ হ'লে প্ৰতিটো 100 ধৰি নিজা পৰিৱৰ্তন কৰা।"), B("30% up and 60% up give 130 and 160, which is 13 : 16.", "30% আৰু 60% বৃদ্ধিয়ে 130 আৰু 160 দিয়ে, অৰ্থাৎ 13 : 16।")], "flow", [B("100 and 100", "100 আৰু 100"), B("130 and 160", "130 আৰু 160"), B("13 : 16", "13 : 16")]),
        lab(f"{p}.s2", B("When a price falls", "দাম কমিলে"), B("Width is the price and height is how much you buy. The area is your spending, which stays fixed.", "প্ৰস্থ দাম, উচ্চতা কিমান কিনা। কালি তোমাৰ খৰচ, ই স্থিৰ।"), {"kind": "mandays", "men": 20, "days": 15, "max": 30, "min": 6}, [
            task(B("Drop the price from 20 to 16, a 20% fall.", "দাম 20ৰ পৰা 16 কৰা, 20% হ্ৰাস।"), {"men": 16}, B("Height rises from 15 to 18.75, which is 25% more. A fall of 20% allows a rise of 25%.", "উচ্চতা 15ৰ পৰা 18.75 হয়, অৰ্থাৎ 25% বেছি। 20% হ্ৰাসে 25% বৃদ্ধি দিয়ে।")),
        ]),
        solve(f"{p}.q1", "p-compare", lambda x, y: {"q": B(f"Two equal numbers change by {'+' if x > 0 else '−'}{abs(x)}% and {'+' if y > 0 else '−'}{abs(y)}%. Write the ratio of the new numbers as a fraction.", f"দুটা সমান সংখ্যাৰ পৰিৱৰ্তন {'+' if x > 0 else '−'}{abs(x)}% আৰু {'+' if y > 0 else '−'}{abs(y)}%। নতুন সংখ্যাৰ অনুপাত ভগ্নাংশত লিখা।"), "answer": num(F(100 + x, 100 + y)), "why": B(f"{100 + x} : {100 + y}.", f"{100 + x} : {100 + y}।"), "traps": [{"ans": num(F(abs(x), abs(y))), "tag": "m-pct-add", "why": B("Compare the new values, 100 + x and 100 + y, not the percentages.", "শতাংশ নহয়, নতুন মান 100 + x আৰু 100 + y তুলনা কৰা।")}]}, [(30, 60), (12, 4), (20, -10), (35, -10)], hints=[B("Take each number as 100.", "প্ৰতিটো সংখ্যা 100 ধৰা।")]),
        solve(f"{p}.q2", "p-compare", lambda r: {"q": B(f"The price of rice falls {r}%. By what percentage can a family buy more for the same money?", f"চাউলৰ দাম {r}% কমিল। একে ধনেৰে এটা পৰিয়ালে কিমান শতাংশ বেছি কিনিব পাৰিব?"), "answer": num(F(r * 100, 100 - r)), "suffix": B("%", "%"), "why": B(f"${fr(r, 100 - r)} \\times 100$.", f"${fr(r, 100 - r)} \\times 100$।"), "traps": [{"ans": str(r), "tag": "m-pct-more-less", "why": B("The rise is measured on the lower price, so it is bigger than the fall.", "বৃদ্ধি কম দামৰ ওপৰত জোখা হয়, সেয়ে ই হ্ৰাসতকৈ ডাঙৰ।")}]}, [(20,), (25,), (50,), (60,)]),
        stepwise(f"{p}.q3", "p-compare", lambda r: {"q": B(f"P is {r}% less than Q. By what percentage is Q more than P?", f"P Qতকৈ {r}% কম। Q Pতকৈ কিমান শতাংশ বেছি?"), "parts": [
            part(B("Take Q = 100. Then P =", "Q = 100 ধৰা। তেনেহ'লে P ="), B(str(100 - r), str(100 - r)), [B(str(100 + r), str(100 + r)), B(str(r), str(r))], B(f"{r} less than 100.", f"100তকৈ {r} কম।"), sid=str(r)),
            part(B("Base for 'more than P'?", "'Pতকৈ বেছি'ৰ ভিত্তি?"), B(f"P: {100 - r}", f"P: {100 - r}"), [B("Q: 100", "Q: 100")], B("The comparison is against P.", "তুলনা Pৰ সৈতে।"), tag="m-pct-more-less", sid=str(r)),
            part(B("Q is more by", "Q বেছি"), B(show(F(r * 100, 100 - r), "%"), show(F(r * 100, 100 - r), "%")), [B(f"{r}%", f"{r}%"), B(f"{r + 10}%", f"{r + 10}%")], B(f"${fr(r, 100 - r)} \\times 100$.", f"${fr(r, 100 - r)} \\times 100$।"), sid=str(r)),
        ], "why": B("Whichever follows 'than' is the base.", "'তকৈ'ৰ আগৰ সংখ্যাটোৱেই ভিত্তি।")}, [(25,), (20,), (40,)]),
        tf(f"{p}.q4", "p-compare", B("If a price falls 50%, you can buy twice as much for the same money.", "দাম 50% কমিলে একে ধনেৰে দুগুণ কিনিব পাৰি।"), True, B("That is a 100% rise in what you can buy.", "ই কিনিব পৰা পৰিমাণৰ 100% বৃদ্ধি।")),
        match(f"{p}.q5", "p-compare", B("Match the change to the ratio against an equal number at 100", "পৰিৱৰ্তনক 100ৰ সৈতে অনুপাতৰ লগত মিলোৱা"), [
            [B("+25%", "+25%"), B("5 : 4", "5 : 4")], [B("−20%", "−20%"), B("4 : 5", "4 : 5")], [B("+50%", "+50%"), B("3 : 2", "3 : 2")], [B("−50%", "−50%"), B("1 : 2", "1 : 2")],
        ], B("Write 100 ± x over 100 and simplify.", "100 ± x ভাগ 100 লিখি সৰল কৰা।")),
    ])


def ratio_values():
    p = "m6.x"
    return unit("u4", B("Values from ratios", "অনুপাতৰ পৰা মান"), "star", [
        B("If $\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$, write x = ak, y = bk, z = ck.", "$\\frac{x}{a} = \\frac{y}{b} = \\frac{z}{c}$ হ'লে x = ak, y = bk, z = ck লিখা।"),
        B("In a ratio expression, k cancels, so any value of k will do.", "অনুপাতৰ ৰাশিত k কাটি যায়, সেয়ে যিকোনো k চলে।"),
        B("Flip a ratio by dividing every term into their LCM.", "প্ৰতিটো পদ ল.সা.গু.ৰ ভিতৰত হৰণ কৰি অনুপাত ওলোটোৱা।"),
        B("Long chains join two at a time.", "দীঘল শিকলি দুটাকৈ জোৰা হয়।"),
    ], [
        diagram(f"{p}.s1", B("Pick a friendly k", "সহজ k বাছি লোৱা"), [B("$\\frac{x}{2} = \\frac{y}{5} = \\frac{z}{9}$ says x, y and z move together as 2, 5 and 9.", "$\\frac{x}{2} = \\frac{y}{5} = \\frac{z}{9}$ মানে x, y, z 2, 5, 9 হিচাপে একেলগে যায়।"), B("So simply put x = 2, y = 5 and z = 9 and calculate.", "সেয়ে পোনে পোনে x = 2, y = 5, z = 9 বহুৱাই হিচাপ কৰা।")], "flow", [B("x = 2, y = 5, z = 9", "x = 2, y = 5, z = 9"), B("$\\frac{x + y + z}{2z}$", "$\\frac{x + y + z}{2z}$"), B("$\\frac{16}{18} = \\frac{8}{9}$", "$\\frac{16}{18} = \\frac{8}{9}$")]),
        lab(f"{p}.s2", B("Flipping a ratio", "অনুপাত ওলোটোৱা"), B("If $\\frac{1}{x} : \\frac{1}{y} : \\frac{1}{z} = 1 : 3 : 4$, the biggest flip belongs to the smallest number.", "$\\frac{1}{x} : \\frac{1}{y} : \\frac{1}{z} = 1 : 3 : 4$ হ'লে ডাঙৰ ওলোটা সৰু সংখ্যাৰ।"), {"kind": "chain", "ab": [1, 3], "bc": [6, 8]}, [
            task(B("Make the two B's match.", "দুটা B মিলোৱা।"), {"match": 1}, B("That joins 2 : 6 : 8, which is 1 : 3 : 4. To flip it, take 12, the LCM, and divide: 12 : 4 : 3.", "ই 2 : 6 : 8 জোৰে, অৰ্থাৎ 1 : 3 : 4। ওলোটাবলৈ ল.সা.গু. 12 লৈ হৰণ কৰা: 12 : 4 : 3।")),
        ]),
        solve(f"{p}.q1", "r-value", lambda a, b, c: {"q": B(f"If $\\frac{{x}}{{{a}}} = \\frac{{y}}{{{b}}} = \\frac{{z}}{{{c}}}$, find $\\frac{{x + y + z}}{{2z}}$.", f"$\\frac{{x}}{{{a}}} = \\frac{{y}}{{{b}}} = \\frac{{z}}{{{c}}}$ হ'লে $\\frac{{x + y + z}}{{2z}}$ উলিওৱা।"), "answer": num(F(a + b + c, 2 * c)), "why": B(f"Put x = {a}, y = {b}, z = {c}.", f"x = {a}, y = {b}, z = {c} বহুওৱা।")}, [(2, 5, 9), (3, 5, 8), (1, 4, 5), (2, 5, 3)], hints=[B("Replace x, y and z with the bottom numbers.", "x, y, zৰ ঠাইত তলৰ সংখ্যা বহুওৱা।")]),
        solve(f"{p}.q2", "r-value", lambda m_, n: {"q": B(f"If m : n = {m_} : {n}, find $\\frac{{3m + n}}{{3m - n}}$.", f"m : n = {m_} : {n} হ'লে $\\frac{{3m + n}}{{3m - n}}$ উলিওৱা।"), "answer": num(F(3 * m_ + n, 3 * m_ - n)), "why": B(f"Put m = {m_} and n = {n}.", f"m = {m_} আৰু n = {n} বহুওৱা।")}, [(4, 9), (2, 1), (3, 4), (5, 3)]),
        solve(f"{p}.q3", "r-value", lambda a, b: {"q": B(f"If $\\frac{{x}}{{{a}}} = \\frac{{y}}{{{b}}}$, find $\\frac{{x^2 - y^2}}{{x + y}}$ when x = {a} and y = {b}.", f"$\\frac{{x}}{{{a}}} = \\frac{{y}}{{{b}}}$ হ'লে x = {a}, y = {b}ত $\\frac{{x^2 - y^2}}{{x + y}}$ উলিওৱা।"), "answer": str(a - b), "why": B("It cancels to x − y.", "কাটিলে x − y হয়।")}, [(11, 4), (12, 5), (20, 7)], hints=[B("Factorise the top.", "ওপৰৰটো উৎপাদক কৰা।")]),
        stepwise(f"{p}.q4", "r-value", lambda a, b, c, top: {"q": B(f"If $\\frac{{1}}{{x}} : \\frac{{1}}{{y}} : \\frac{{1}}{{z}} = {a} : {b} : {c}$, find x : y : z.", f"$\\frac{{1}}{{x}} : \\frac{{1}}{{y}} : \\frac{{1}}{{z}} = {a} : {b} : {c}$ হ'লে x : y : z উলিওৱা।"), "parts": [
            part(B("LCM of the terms?", "পদবোৰৰ ল.সা.গু.?"), B(str(top), str(top)), [B(str(top * 2), str(top * 2)), B(str(top + 1), str(top + 1))], B("It clears every fraction.", "ই সকলো ভগ্নাংশ আঁতৰায়।"), skill="l-lcm", sid=str(a * b)),
            part(B("Flipped ratio?", "ওলোটা অনুপাত?"), B(f"{ex(top, a)} : {ex(top, b)} : {ex(top, c)}", f"{ex(top, a)} : {ex(top, b)} : {ex(top, c)}"), [B(f"{a} : {b} : {c}", f"{a} : {b} : {c}"), B(f"{c} : {b} : {a}", f"{c} : {b} : {a}")], B("Divide the LCM by each term.", "ল.সা.গু.ক প্ৰতিটো পদেৰে হৰণ কৰা।"), tag="m-ratio-flip", sid=str(a * b)),
        ], "why": B("Simply reversing the order works only for two terms.", "ক্ৰম ওলোটোৱা কেৱল দুটা পদতহে চলে।")}, [(1, 3, 4, 12), (2, 5, 6, 30), (3, 4, 6, 12)]),
        solve(f"{p}.q5", "r-combine", lambda t: {"q": B(f"₹{t} is shared among A, B, C and D where A : B = 3 : 4, B : C = 2 : 3 and C : D = 1 : 3. How much does D get?", f"₹{t} A, B, C, Dৰ মাজত ভাগ কৰা হ'ল, য'ত A : B = 3 : 4, B : C = 2 : 3, C : D = 1 : 3। Dই কিমান পাব?"), "answer": str(ex(t * 18, 31)), "prefix": B("₹", "₹"), "why": B("Joined: 3 : 4 : 6 : 18, which is 31 blocks.", "জোৰা: 3 : 4 : 6 : 18, মুঠ 31 খণ্ড।")}, [(3100,), (6200,), (1550,)], hints=[B("Join two ratios at a time.", "দুটা দুটাকৈ অনুপাত জোৰা।")]),
        tf(f"{p}.q6", "r-value", B("If x : y : z = 2 : 5 : 6, then $\\frac{1}{x} : \\frac{1}{y} : \\frac{1}{z}$ = 6 : 5 : 2.", "x : y : z = 2 : 5 : 6 হ'লে $\\frac{1}{x} : \\frac{1}{y} : \\frac{1}{z}$ = 6 : 5 : 2।"), False, B("It is 15 : 6 : 5: divide the LCM, 30, by each term.", "ই 15 : 6 : 5: ল.সা.গু. 30ক প্ৰতিটো পদেৰে হৰণ কৰা।"), ("m-ratio-flip", B("Flipping three terms is not reversing them.", "তিনিটা পদ ওলোটোৱা মানে ক্ৰম সলনি কৰা নহয়।"))),
        match(f"{p}.q7", "r-value", B("Match each ratio to its flip", "প্ৰতিটো অনুপাতক ওলোটাৰ সৈতে মিলোৱা"), [
            [B("1 : 2", "1 : 2"), B("2 : 1", "2 : 1")], [B("1 : 3 : 4", "1 : 3 : 4"), B("12 : 4 : 3", "12 : 4 : 3")], [B("2 : 5 : 6", "2 : 5 : 6"), B("15 : 6 : 5", "15 : 6 : 5")], [B("3 : 4 : 6", "3 : 4 : 6"), B("4 : 3 : 2", "4 : 3 : 2")],
        ], B("Divide the LCM of the terms by each one.", "পদবোৰৰ ল.সা.গু.ক প্ৰতিটোৰে হৰণ কৰা।")),
    ])


def average_extras():
    return {
        "u1": [
            solve("m7.u1.q6", "a-mean", lambda n, a, k: {"q": B(f"The average of {n} consecutive whole numbers is {a}. Find number {k} counting from the top.", f"{n}টা ক্ৰমিক পূৰ্ণ সংখ্যাৰ গড় {a}। ওপৰৰ পৰা গণিলে {k} নং সংখ্যাটো উলিওৱা।"), "answer": num(F(str(a)) + F(n - 1, 2) - (k - 1)), "why": B("With an even count, the average sits between the two middle numbers.", "সংখ্যা যুগ্ম হ'লে গড় মাজৰ দুটাৰ মাজত থাকে।")}, [(6, 62.5, 2), (4, 31.5, 3), (8, 40.5, 2)], hints=[B("Largest = average + half of (count − 1).", "ডাঙৰটো = গড় + (সংখ্যা − 1)ৰ আধা।")]),
            solve("m7.u1.q7", "a-mean", lambda offs, a, text: {"q": B(f"The average of {text} is {a}. Find x.", f"{text}ৰ গড় {a}। x উলিওৱা।"), "answer": num(F(a) - F(sum(offs), len(offs))), "why": B(f"x + {num(F(sum(offs), len(offs)))} = {a}.", f"x + {num(F(sum(offs), len(offs)))} = {a}।")}, [((0, 5, -2, 9), 6, "$x$, $x + 5$, $x - 2$, $x + 9$"), ((-2, -5, -3, 6), 7, "$x - 2$, $x - 5$, $x - 3$, $x + 6$"), ((2, 6, 4), 9, "$x + 2$, $x + 6$, $x + 4$")], hints=[B("Add all the numbers next to x, then share them out.", "xৰ লগৰ সংখ্যাবোৰ যোগ কৰি ভাগ কৰা।")]),
        ],
        "u2": [
            solve("m7.u2.q7", "a-change", lambda abc, ab, bc: {"q": B(f"The average weight of A, B and C is {abc} kg. A and B average {ab} kg, and B and C average {bc} kg. Find B.", f"A, B, Cৰ গড় ওজন {abc} কিলো। A আৰু Bৰ গড় {ab} কিলো, B আৰু Cৰ গড় {bc} কিলো। Bৰ ওজন উলিওৱা।"), "answer": str(2 * ab + 2 * bc - 3 * abc), "suffix": B("kg", "কিলো"), "why": B(f"{2 * ab} + {2 * bc} counts B twice, so subtract {3 * abc}.", f"{2 * ab} + {2 * bc}ত B দুবাৰ, সেয়ে {3 * abc} বিয়োগ কৰা।")}, [(52, 47, 50), (50, 48, 45), (60, 55, 62)], hints=[B("Turn each average into a total.", "প্ৰতিটো গড়ক মুঠ কৰা।")]),
        ],
        "u3": [
            solve("m7.u3.q7", "a-mean", lambda k, s_: {"q": B(f"If {k}a + {k}b + {k}c = {s_}, find the average of a, b and c.", f"{k}a + {k}b + {k}c = {s_} হ'লে a, b, cৰ গড় উলিওৱা।"), "answer": num(F(s_, 3 * k)), "why": B(f"a + b + c = {num(F(s_, k))}, shared among 3.", f"a + b + c = {num(F(s_, k))}, 3ৰে হৰণ।")}, [(4, 48), (2, 36), (5, 75)]),
        ],
    }


def profit_more():
    p = "m8.x"
    addup = B("The next discount acts on what is left. Multiply what remains: 0.9 × 0.8 × 0.75.", "পিছৰ ৰেহাই বাকীৰ ওপৰত। বাকীখিনি পূৰণ কৰা: 0.9 × 0.8 × 0.75।")
    return unit("u4", B("More deals", "আৰু লেনদেন"), "star", [
        B("Profit of r% on selling price is $\\frac{r}{100 - r} \\times 100$% on cost.", "বিক্ৰী মূল্যৰ ওপৰত r% লাভ মানে ক্ৰয় মূল্যৰ ওপৰত $\\frac{r}{100 - r} \\times 100$%।"),
        B("With unequal profit and loss on one price, find both costs.", "একে দামত অসমান লাভ-লোকচান হ'লে দুয়োটা ক্ৰয় মূল্য উলিওৱা।"),
        B("Three discounts: multiply what remains after each.", "তিনিটা ৰেহাই: প্ৰতিটোৰ পিছত বাকীখিনি পূৰণ কৰা।"),
        B("From a known loss to a wanted gain, go through 100% of cost.", "জনা লোকচানৰ পৰা বিচৰা লাভলৈ ক্ৰয় মূল্যৰ 100%ৰ মাজেদি যোৱা।"),
    ], [
        lab(f"{p}.s1", B("Profit on the wrong base", "ভুল ভিত্তিৰ লাভ"), B("Say a seller's profit is 20% of the selling price. Take selling as 100, so cost is 80.", "ধৰা লাভ বিক্ৰী মূল্যৰ 20%। বিক্ৰী 100 ধৰিলে ক্ৰয় 80।"), {"kind": "dual", "base": 80, "max": 150, "pct": 100}, [
            task(B("Drag to 125% of cost.", "ক্ৰয় মূল্যৰ 125%লৈ টানা।"), {"pct": 125}, B("125% of 80 is 100. So 20% on selling is 25% on cost.", "80ৰ 125% হ'ল 100। সেয়ে বিক্ৰীৰ ওপৰত 20% মানে ক্ৰয়ৰ ওপৰত 25%।")),
        ]),
        diagram(f"{p}.s2", B("Costs reveal the truth", "ক্ৰয় মূল্যই সত্য দেখুৱায়"), [B("When two items sell at one price with different rates, the percentages alone tell you nothing.", "দুটা বস্তু একে দামত বেলেগ হাৰত বিক্ৰী হ'লে কেৱল শতাংশই একো নকয়।"), B("Undo each rate, add the costs, and compare with the money received.", "প্ৰতিটো হাৰ ওভতাই ক্ৰয় মূল্য যোগ কৰি পোৱা ধনৰ সৈতে তুলনা কৰা।")], "flow", [B("3780 ÷ 1.05 = 3600", "3780 ÷ 1.05 = 3600"), B("3780 ÷ 0.9 = 4200", "3780 ÷ 0.9 = 4200"), B("7800 against 7560", "7800ৰ বিপৰীতে 7560")]),
        solve(f"{p}.q1", "pl-deals", lambda r: {"q": B(f"A seller's profit is {r}% of the selling price. What is it as a percentage of cost?", f"বিক্ৰেতাৰ লাভ বিক্ৰী মূল্যৰ {r}%। ক্ৰয় মূল্যৰ কিমান শতাংশ?"), "answer": num(F(r * 100, 100 - r)), "suffix": B("%", "%"), "why": B(f"Selling 100, cost {100 - r}, profit {r}.", f"বিক্ৰী 100, ক্ৰয় {100 - r}, লাভ {r}।"), "traps": [{"ans": str(r), "tag": "m-cp-base", "why": B("That is on selling price. Re-measure the same profit on the cost.", "সেয়া বিক্ৰী মূল্যত। একে লাভ ক্ৰয় মূল্যত জোখা।")}]}, [(20,), (25,), (50,), (10,)], hints=[B("Take selling price as 100.", "বিক্ৰী মূল্য 100 ধৰা।")]),
        stepwise(f"{p}.q2", "pl-deals", lambda s_, a, b: {"q": B(f"Two phones sell at ₹{s_} each, one at {a}% profit and one at {b}% loss. Find the overall result.", f"দুটা ফোন প্ৰতিটো ₹{s_}ত বিক্ৰী, এটা {a}% লাভত, আনটো {b}% লোকচানত। মুঠ ফল উলিওৱা।"), "parts": [
            part(B("Cost of the first?", "প্ৰথমটোৰ ক্ৰয় মূল্য?"), B(f"₹{ex(s_ * 100, 100 + a)}", f"₹{ex(s_ * 100, 100 + a)}"), [B(f"₹{s_}", f"₹{s_}"), B(f"₹{s_ * (100 - a) // 100}", f"₹{s_ * (100 - a) // 100}")], B("Divide by the profit multiplier.", "লাভৰ গুণকেৰে হৰণ কৰা।"), sid=str(s_)),
            part(B("Cost of the second?", "দ্বিতীয়টোৰ ক্ৰয় মূল্য?"), B(f"₹{ex(s_ * 100, 100 - b)}", f"₹{ex(s_ * 100, 100 - b)}"), [B(f"₹{s_}", f"₹{s_}"), B(f"₹{s_ * (100 + b) // 100}", f"₹{s_ * (100 + b) // 100}")], B("Divide by the loss multiplier.", "লোকচানৰ গুণকেৰে হৰণ কৰা।"), sid=str(s_)),
            part(B("Overall?", "মুঠতে?"), B(f"Loss of ₹{ex(s_ * 100, 100 + a) + ex(s_ * 100, 100 - b) - 2 * s_}", f"₹{ex(s_ * 100, 100 + a) + ex(s_ * 100, 100 - b) - 2 * s_} লোকচান"), [B("No profit, no loss", "লাভো নাই, লোকচানো নাই"), B(f"Profit of ₹{ex(s_ * 100, 100 + a) + ex(s_ * 100, 100 - b) - 2 * s_}", f"₹{ex(s_ * 100, 100 + a) + ex(s_ * 100, 100 - b) - 2 * s_} লাভ")], B("Compare total cost with the money received.", "মুঠ ক্ৰয় মূল্য পোৱা ধনৰ সৈতে তুলনা কৰা।"), tag="m-two-items", sid=str(s_)),
        ], "why": B("Percentages on different bases never simply cancel.", "বেলেগ ভিত্তিৰ শতাংশ কেতিয়াও সহজে নাকাটে।")}, [(3780, 5, 10), (1320, 10, 12), (2520, 5, 10)]),
        solve(f"{p}.q3", "pl-discount", lambda a, b, c: {"q": B(f"Find the single discount equal to successive discounts of {a}%, {b}% and {c}%.", f"{a}%, {b}% আৰু {c}% ক্ৰমিক ৰেহাইৰ সমান একক ৰেহাই উলিওৱা।"), "answer": num(100 - F(100 - a, 100) * F(100 - b, 100) * F(100 - c) ), "suffix": B("%", "%"), "why": B("Multiply what remains, then take it from 100.", "বাকীখিনি পূৰণ কৰি 100ৰ পৰা বিয়োগ কৰা।"), "traps": [{"ans": str(a + b + c), "tag": "m-discount-add", "why": addup}]}, [(5, 20, 25), (10, 20, 50), (20, 25, 50)], hints=[B("Remaining: multiply (100 − each) as decimals.", "বাকী: (100 − প্ৰতিটো) দশমিকত পূৰণ কৰা।")]),
        solve(f"{p}.q4", "pl-deals", lambda s_, l_, g: {"q": B(f"Selling for ₹{s_} a man loses {l_}%. At what price would he gain {g}%?", f"₹{s_}ত বেচি এজনে {l_}% লোকচান পায়। কিমানত বেচিলে {g}% লাভ হ'ব?"), "answer": str(ex(s_ * (100 + g), 100 - l_)), "prefix": B("₹", "₹"), "why": B(f"Cost is ₹{ex(s_ * 100, 100 - l_)}; then add {g}%.", f"ক্ৰয় মূল্য ₹{ex(s_ * 100, 100 - l_)}; তাৰ পিছত {g}% যোগ।"), "traps": [{"ans": str(ex(s_ * (100 + l_ + g), 100)), "tag": "m-cp-base", "why": B("Percentages are of cost, not of this selling price. Find the cost first.", "শতাংশ ক্ৰয় মূল্যৰ, এই বিক্ৰী মূল্যৰ নহয়। প্ৰথমে ক্ৰয় মূল্য উলিওৱা।")}]}, [(1330, 5, 5), (900, 10, 20), (720, 10, 10)]),
        solve(f"{p}.q5", "pl-discount", lambda g: {"q": B(f"The marked price is twice the cost. What discount gives a {g}% gain?", f"চিহ্নিত মূল্য ক্ৰয় মূল্যৰ দুগুণ। {g}% লাভৰ বাবে কিমান ৰেহাই লাগিব?"), "answer": num(F(100 - g, 2)), "suffix": B("%", "%"), "why": B(f"Cost 100, marked 200, selling {100 + g}. The discount is {100 - g} on 200.", f"ক্ৰয় 100, চিহ্নিত 200, বিক্ৰী {100 + g}। 200ৰ ওপৰত ৰেহাই {100 - g}।")}, [(40,), (20,), (60,)]),
        tf(f"{p}.q6", "pl-deals", B("Profit of 25% on cost is the same as 25% on selling price.", "ক্ৰয় মূল্যৰ ওপৰত 25% লাভ বিক্ৰী মূল্যৰ ওপৰত 25%ৰ সমান।"), False, B("Cost 100, selling 125: the 25 is only 20% of selling price.", "ক্ৰয় 100, বিক্ৰী 125: 25 বিক্ৰী মূল্যৰ মাত্ৰ 20%।"), ("m-cp-base", B("Same rupees, different base, different percent.", "একে টকা, বেলেগ ভিত্তি, বেলেগ শতাংশ।"))),
        match(f"{p}.q7", "pl-deals", B("Match profit on selling price to profit on cost", "বিক্ৰী মূল্যৰ লাভক ক্ৰয় মূল্যৰ লাভৰ সৈতে মিলোৱা"), [
            [B("20%", "20%"), B("25%", "25%")], [B("50%", "50%"), B("100%", "100%")], [B("60%", "60%"), B("150%", "150%")], [B("10%", "10%"), B("$\\frac{100}{9}$%", "$\\frac{100}{9}$%")],
        ], B("Divide r by 100 − r.", "rক 100 − rৰে হৰণ কৰা।")),
    ])
