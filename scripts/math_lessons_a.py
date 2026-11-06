"""Mathematics lessons 1 and 2: numbers, then factors, LCM and HCF. All worked numbers are original."""
from math import gcd
from math_kit import B, explore, match, mcq, odd, order, solve, story, stepwise, tf, unit, part


def lcm(a, b):
    return a * b // gcd(a, b)


# ---------------------------------------------------------------- Lesson 1
def l1():
    p = "m1"
    u1 = unit("u1", B("Number families", "সংখ্যাৰ পৰিয়াল"), "star", [
        B("Natural numbers start at 1; whole numbers add 0; integers add the negatives.", "স্বাভাৱিক সংখ্যা 1ৰ পৰা আৰম্ভ হয়; পূৰ্ণ সংখ্যাত 0 যোগ হয়; অখণ্ড সংখ্যাত ঋণাত্মক সংখ্যাও থাকে।"),
        B("A prime has exactly two factors: 1 and itself.", "মৌলিক সংখ্যাৰ ঠিক দুটা গুণনীয়ক থাকে: 1 আৰু সংখ্যাটো নিজে।"),
        B("1 is neither prime nor composite, and 2 is the only even prime.", "1 মৌলিকো নহয়, যৌগিকো নহয়; 2 একমাত্ৰ যুগ্ম মৌলিক সংখ্যা।"),
        B("Every number above 1 peels into primes in exactly one way.", "1তকৈ ডাঙৰ প্ৰতিটো সংখ্যা মাত্ৰ এটা ধৰণেৰে মৌলিক গুণনীয়কত ভাঙে।"),
    ], [
        story(f"{p}.u1.s1", B("Numbers come in families", "সংখ্যাৰো পৰিয়াল আছে"), [
            B("Exams ask what kind of number something is. Learn the families once and these marks are free.", "পৰীক্ষাত সোধে সংখ্যা এটা কোন ধৰণৰ। পৰিয়ালকেইটা এবাৰ শিকিলে এই নম্বৰবোৰ সহজ।"),
            B("Each family contains the one before it, like rooms inside a house.", "ঘৰৰ ভিতৰত কোঠাৰ দৰে প্ৰতিটো পৰিয়ালৰ ভিতৰত আগৰটো থাকে।"),
        ], diagram={"layout": "flow", "items": [B("Natural: 1, 2, 3 …", "স্বাভাৱিক: 1, 2, 3 …"), B("Whole: 0, 1, 2 …", "পূৰ্ণ: 0, 1, 2 …"), B("Integers: … −1, 0, 1 …", "অখণ্ড: … −1, 0, 1 …"), B("Rational: any $\\frac{p}{q}$", "পৰিমেয়: যিকোনো $\\frac{p}{q}$")]}),
        match(f"{p}.u1.q1", "n-types", B("Match each number to its smallest family", "প্ৰতিটো সংখ্যাক ইয়াৰ সৰুতম পৰিয়ালৰ সৈতে মিলোৱা"), [
            [B("7", "7"), B("Natural", "স্বাভাৱিক")], [B("0", "0"), B("Whole", "পূৰ্ণ")], [B("−4", "−4"), B("Integer", "অখণ্ড")], [B("$\\frac{2}{3}$", "$\\frac{2}{3}$"), B("Rational", "পৰিমেয়")],
        ], B("0 is the first whole number but not a natural number. −4 needs integers, and $\\frac{2}{3}$ needs rationals.", "0 প্ৰথম পূৰ্ণ সংখ্যা, কিন্তু স্বাভাৱিক সংখ্যা নহয়। −4ৰ বাবে অখণ্ড আৰু $\\frac{2}{3}$ৰ বাবে পৰিমেয় সংখ্যা লাগে।")),
        story(f"{p}.u1.s2", B("Peel a number to its primes", "সংখ্যাক মৌলিকলৈ ভাঙা"), [
            B("A prime cannot be split further. Tap a prime that divides the number and watch it shrink.", "মৌলিক সংখ্যা আৰু ভাঙিব নোৱাৰি। সংখ্যাটোক হৰণ কৰিব পৰা মৌলিকত টিপি সৰু হোৱা চোৱা।"),
            B("Keep going until 1 is left. What you collected is the number's fingerprint.", "1 নোহোৱালৈ চলাই থাকা। যি পালা সেয়াই সংখ্যাটোৰ আঙুলিৰ ছাপ।"),
        ], widget={"kind": "peel", "n": 60}),
        tf(f"{p}.u1.q2", "n-types", B("1 is a prime number.", "1 এটা মৌলিক সংখ্যা।"), False, B("A prime needs exactly two factors. 1 has only one, so it is neither prime nor composite.", "মৌলিক সংখ্যাৰ ঠিক দুটা গুণনীয়ক লাগে। 1ৰ মাত্ৰ এটা, সেয়ে ই মৌলিকো নহয়, যৌগিকো নহয়।"), ("m-one-prime", B("You counted 1 as a prime. It has only one factor.", "তুমি 1ক মৌলিক ধৰিলা। ইয়াৰ মাত্ৰ এটা গুণনীয়ক আছে।"))),
        odd(f"{p}.u1.q3", "n-types", lambda a, x, y, z: {"q": B("Which one is not prime?", "কোনটো মৌলিক নহয়?"), "right": a, "fill": [x, y, z], "why": B(f"{a} looks prime, but it can be divided: {next(d for d in (3, 7, 11, 13) if a % d == 0)} × {a // next(d for d in (3, 7, 11, 13) if a % d == 0)} = {a}.", f"{a} মৌলিক যেন লাগে, কিন্তু ভাঙিব পাৰি: {next(d for d in (3, 7, 11, 13) if a % d == 0)} × {a // next(d for d in (3, 7, 11, 13) if a % d == 0)} = {a}।")}, [(51, 53, 59, 61), (57, 47, 43, 41), (91, 89, 83, 79), (87, 71, 73, 67)]),
        explore(f"{p}.u1.q4", "n-factor", lambda n: {"q": B(f"Peel {n} completely into primes.", f"{n}ক সম্পূৰ্ণকৈ মৌলিকলৈ ভাঙা।"), "widget": {"kind": "peel", "n": n}, "target": n, "answerText": B("Divide only by primes that fit", "কেৱল মিলা মৌলিকেৰে হৰণ কৰা"), "why": B(f"Any order gives the same primes for {n}. A wrong tap is a prime that does not divide what is left.", f"যিকোনো ক্ৰমতে {n}ৰ একেকেইটা মৌলিক পোৱা যায়। ভুল টিপা মানে বাকী থকা সংখ্যাক সেই মৌলিকে হৰণ নকৰে।")}, [(84,), (90,), (126,), (150,)], hints=[B("Even? Start with 2.", "যুগ্ম নেকি? 2ৰে আৰম্ভ কৰা।")]),
        solve(f"{p}.u1.q5", "n-types", lambda a, b, n, ps: {"q": B(f"How many primes lie between {a} and {b}?", f"{a} আৰু {b}ৰ মাজত কেইটা মৌলিক সংখ্যা আছে?"), "answer": str(n), "why": B(f"They are {ps}.", f"সেইবোৰ হ'ল {ps}।"), "traps": [{"ans": str(n + 1), "tag": "m-odd-prime", "why": B("You probably counted an odd number that is not prime, such as 21, 27 or 33.", "তুমি হয়তো মৌলিক নোহোৱা অযুগ্ম সংখ্যা ধৰিলা, যেনে 21, 27 বা 33।")}]}, [(10, 30, 6, "11, 13, 17, 19, 23, 29"), (20, 40, 4, "23, 29, 31, 37"), (30, 50, 5, "31, 37, 41, 43, 47")], hints=[B("List the odd numbers, then strike out multiples of 3, 5 and 7.", "অযুগ্ম সংখ্যাবোৰ লিখা, তাৰ পিছত 3, 5 আৰু 7ৰ গুণিতক কাটি দিয়া।")]),
    ])
    u2 = unit("u2", B("Divisibility shortcuts", "বিভাজ্যতাৰ চুটি পথ"), "star", [
        B("By 2 or 5: look at the last digit. By 4: the last two digits. By 8: the last three.", "2 বা 5ৰ বাবে শেষৰ অংক চোৱা। 4ৰ বাবে শেষৰ দুটা, 8ৰ বাবে শেষৰ তিনিটা।"),
        B("By 3 or 9: add all the digits.", "3 বা 9ৰ বাবে সকলো অংক যোগ কৰা।"),
        B("By 6: the number must pass both 2 and 3.", "6ৰ বাবে 2 আৰু 3 দুয়োটা পৰীক্ষা পাৰ হ'ব লাগিব।"),
        B("By 11: alternate digits' sums must differ by 0 or a multiple of 11.", "11ৰ বাবে এটাৰ পিছত এটা অংকৰ যোগফলৰ পাৰ্থক্য 0 বা 11ৰ গুণিতক হ'ব লাগে।"),
    ], [
        story(f"{p}.u2.s1", B("Test without dividing", "হৰণ নকৰাকৈ পৰীক্ষা"), [
            B("In an exam you have under a minute. These rules answer in seconds.", "পৰীক্ষাত এক মিনিটো নাথাকে। এই নিয়মবোৰে চেকেণ্ডতে উত্তৰ দিয়ে।"),
            B("Each rule looks at only part of the number, so even huge numbers are quick.", "প্ৰতিটো নিয়মে সংখ্যাৰ অলপ অংশহে চায়, সেয়ে বিশাল সংখ্যাও সোনকালে হয়।"),
        ], diagram={"layout": "grid", "items": [B("2, 5: last digit", "2, 5: শেষৰ অংক"), B("4: last two digits", "4: শেষৰ দুটা অংক"), B("3, 9: digit sum", "3, 9: অংকৰ যোগফল"), B("6: passes 2 and 3", "6: 2 আৰু 3 দুয়োটা")]}),
        story(f"{p}.u2.s2", B("Why the digit sum works", "অংকৰ যোগফল কিয় মিলে"), [
            B("$10 = 9 + 1$, so every place value is a multiple of 9 plus 1.", "$10 = 9 + 1$, সেয়ে প্ৰতিটো স্থানীয় মান 9ৰ গুণিতকৰ লগত 1।"),
            B("That leaves only the digits themselves to check, which is the whole rule for 3 and 9.", "তেনেহ'লে কেৱল অংকবোৰ পৰীক্ষা কৰিলেই হয়, এয়াই 3 আৰু 9ৰ নিয়ম।"),
        ], diagram={"layout": "flow", "items": [B("$423 = 400 + 20 + 3$", "$423 = 400 + 20 + 3$"), B("$4 + 2 + 3 = 9$", "$4 + 2 + 3 = 9$"), B("So 423 divides by 9", "সেয়ে 423 9ৰে হৰণ যায়")]}),
        match(f"{p}.u2.q1", "n-div", B("Match each test to what you check", "প্ৰতিটো পৰীক্ষাক কি চাব লাগে তাৰ সৈতে মিলোৱা"), [
            [B("By 5", "5ৰে"), B("Last digit 0 or 5", "শেষৰ অংক 0 বা 5")], [B("By 4", "4ৰে"), B("Last two digits", "শেষৰ দুটা অংক")], [B("By 9", "9ৰে"), B("Digit sum", "অংকৰ যোগফল")], [B("By 6", "6ৰে"), B("Both 2 and 3", "2 আৰু 3 দুয়োটা")],
        ], B("Each rule depends on how place value behaves for that divisor.", "প্ৰতিটো নিয়ম সেই হৰকৰ বাবে স্থানীয় মানৰ আচৰণৰ ওপৰত নিৰ্ভৰ কৰে।")),
        tf(f"{p}.u2.q2", "n-div", B("Any number ending in 3 is divisible by 3.", "3ৰে শেষ হোৱা যিকোনো সংখ্যা 3ৰে হৰণ যায়।"), False, B("13 ends in 3 but is not divisible by 3. For 3, add the digits instead.", "13ৰ শেষত 3 আছে, কিন্তু 3ৰে হৰণ নাযায়। 3ৰ বাবে অংকবোৰ যোগ কৰিব লাগে।"), ("m-div-last", B("The last digit decides 2 and 5, not 3. For 3 use the digit sum.", "শেষৰ অংকই 2 আৰু 5ৰ সিদ্ধান্ত দিয়ে, 3ৰ নহয়। 3ৰ বাবে অংকৰ যোগফল লোৱা।"))),
        solve(f"{p}.u2.q3", "n-div", lambda h, t, d, k: {"q": B(f"$\\mathbf{{{h}\\,?\\,{t}}}$ must be divisible by {d}. What is the smallest digit for ?", f"$\\mathbf{{{h}\\,?\\,{t}}}$ {d}ৰে হৰণ যাব লাগে। ?ৰ সৰুতম অংকটো কি?"), "answer": str(k), "why": B(f"The digits must add to a multiple of {d}: {sum(int(c) for c in str(h) + str(t))} + {k} = {sum(int(c) for c in str(h) + str(t)) + k}.", f"অংকবোৰৰ যোগফল {d}ৰ গুণিতক হ'ব লাগিব: {sum(int(c) for c in str(h) + str(t))} + {k} = {sum(int(c) for c in str(h) + str(t)) + k}।")}, [(52, 4, 9, 7), (31, 6, 9, 8), (74, 1, 3, 0), (23, 8, 3, 2)], hints=[B("Add the digits you can see first.", "প্ৰথমে দেখা অংকবোৰ যোগ কৰা।")]),
        odd(f"{p}.u2.q4", "n-div", lambda a, x, y, z, d: {"q": B(f"Which number is not divisible by {d}?", f"কোনটো সংখ্যা {d}ৰে হৰণ নাযায়?"), "right": a, "fill": [x, y, z], "why": B(f"Use the rule for {d} on each number. {a} is the one that fails it.", f"প্ৰতিটো সংখ্যাত {d}ৰ নিয়ম খটুওৱা। {a}য়েই পাৰ নহয়।")}, [(1234, 2316, 4512, 1116, 3), (5714, 3912, 7116, 2124, 4), (2022, 3024, 5016, 7032, 4), (8164, 7236, 5418, 4374, 9)]),
        stepwise(f"{p}.u2.q5", "n-div", lambda n: {"q": B(f"Is {n} divisible by 6?", f"{n} 6ৰে হৰণ যায় নে?"), "parts": [
            part(B("First check: 2", "প্ৰথম পৰীক্ষা: 2"), B("Yes, it is even", "হয়, যুগ্ম"), [B("No, it is odd", "নহয়, অযুগ্ম")], B("The last digit is even.", "শেষৰ অংক যুগ্ম।"), sid=str(n)),
            part(B("Second check: digit sum", "দ্বিতীয় পৰীক্ষা: অংকৰ যোগফল"), B(f"{sum(map(int, str(n)))}, a multiple of 3", f"{sum(map(int, str(n)))}, 3ৰ গুণিতক"), [B(f"{sum(map(int, str(n))) + 1}, not a multiple of 3", f"{sum(map(int, str(n))) + 1}, 3ৰ গুণিতক নহয়")], B("Add every digit carefully.", "প্ৰতিটো অংক সাৱধানে যোগ কৰা।"), sid=str(n)),
            part(B("So, by 6?", "তেনেহ'লে 6ৰে?"), B("Yes, it passes both", "হয়, দুয়োটা পাৰ"), [B("No", "নহয়")], B("6 needs both tests, and it passed both.", "6ৰ বাবে দুয়োটা পৰীক্ষা লাগে, দুয়োটা পাৰ হ'ল।"), sid=str(n)),
        ], "why": B("Testing by 6 is just two easy tests in a row.", "6ৰ পৰীক্ষা মানে পৰ পৰ দুটা সহজ পৰীক্ষা।")}, [(4518,), (7362,), (1944,)]),
    ])
    u3 = unit("u3", B("Last-digit tricks", "শেষৰ অংকৰ কৌশল"), "star", [
        B("Only last digits affect the last digit of a product.", "পূৰণফলৰ শেষৰ অংক কেৱল শেষৰ অংকবোৰৰ ওপৰত নিৰ্ভৰ কৰে।"),
        B("Powers repeat their last digit in a cycle of at most 4.", "ঘাতৰ শেষৰ অংক সৰ্বাধিক 4ৰ চক্ৰত ঘূৰি আহে।"),
        B("Divide the power by 4 and use the remainder.", "ঘাতক 4ৰে হৰণ কৰি ভাগশেষ ব্যৱহাৰ কৰা।"),
        B("A remainder of 0 means the fourth place in the cycle.", "ভাগশেষ 0 মানে চক্ৰৰ চতুৰ্থ স্থান।"),
    ], [
        story(f"{p}.u3.s1", B("The last digit keeps a rhythm", "শেষৰ অংকৰ এক ছন্দ আছে"), [
            B("Powers of 3 end in 3, 9, 7, 1, then 3 again. The pattern repeats for ever.", "3ৰ ঘাতৰ শেষৰ অংক 3, 9, 7, 1, তাৰ পিছত আকৌ 3। এই ছন্দ চলি থাকে।"),
            B("So you never need the huge number itself, only your place in the rhythm.", "সেয়ে বিশাল সংখ্যাটো লাগে নাই, ছন্দৰ কোন ঠাইত আছা সেইটোহে লাগে।"),
        ], diagram={"layout": "flow", "items": [B("$3^1$ ends 3", "$3^1$: শেষত 3"), B("$3^2$ ends 9", "$3^2$: শেষত 9"), B("$3^3$ ends 7", "$3^3$: শেষত 7"), B("$3^4$ ends 1", "$3^4$: শেষত 1")]}),
        story(f"{p}.u3.s2", B("Find your place in the cycle", "চক্ৰত নিজৰ ঠাই বিচাৰা"), [
            B("For $7^{23}$, divide 23 by 4. The remainder is 3, so use the third digit of 7's cycle.", "$7^{23}$ৰ বাবে 23ক 4ৰে হৰণ কৰা। ভাগশেষ 3, সেয়ে 7ৰ চক্ৰৰ তৃতীয় অংকটো লোৱা।"),
            B("7's cycle is 7, 9, 3, 1, so the answer ends in 3.", "7ৰ চক্ৰ 7, 9, 3, 1, সেয়ে উত্তৰৰ শেষত 3।"),
        ], diagram={"layout": "flow", "items": [B("$23 \\div 4$ leaves 3", "$23 \\div 4$ৰ ভাগশেষ 3"), B("Third in 7, 9, 3, 1", "7, 9, 3, 1ৰ তৃতীয়টো"), B("Unit digit 3", "একক অংক 3")]}),
        order(f"{p}.u3.q1", "n-unit", B("Put the method in order for $8^{50}$", "$8^{50}$ৰ বাবে পদ্ধতিটো ক্ৰমত সজোৱা"), [B("Write the cycle: 8, 4, 2, 6", "চক্ৰ লিখা: 8, 4, 2, 6"), B("Divide 50 by 4: remainder 2", "50ক 4ৰে হৰণ কৰা: ভাগশেষ 2"), B("Take the second digit: 4", "দ্বিতীয় অংকটো লোৱা: 4")], B("Cycle, remainder, position: the same three moves work every time.", "চক্ৰ, ভাগশেষ, স্থান: সদায় এই তিনিটা খোজেই।")),
        solve(f"{p}.u3.q2", "n-unit", lambda a, b, r: {"q": B(f"What is the unit digit of {a} × {b}?", f"{a} × {b}ৰ একক অংকটো কি?"), "answer": str(r), "why": B(f"Only the last digits matter: {a % 10} × {b % 10} = {(a % 10) * (b % 10)}, which ends in {r}.", f"কেৱল শেষৰ অংকবোৰ লাগে: {a % 10} × {b % 10} = {(a % 10) * (b % 10)}, শেষত {r}।")}, [(a, b, a * b % 10) for a, b in [(437, 256), (1283, 479), (6128, 3597), (964, 723)]]),
        solve(f"{p}.u3.q3", "n-unit", lambda b, e, r: {"q": B(f"What is the unit digit of ${b}^{{{e}}}$?", f"${b}^{{{e}}}$ৰ একক অংকটো কি?"), "answer": str(r), "why": B(f"{e} ÷ 4 leaves {e % 4 or 'no remainder, so position 4'}. That place in the cycle of {b % 10} gives {r}.", f"{e} ÷ 4ৰ ভাগশেষ {e % 4 or '0, সেয়ে চতুৰ্থ স্থান'}। {b % 10}ৰ চক্ৰৰ সেই স্থানত {r}।"), "traps": [{"ans": str(b * e % 10), "tag": "m-unit-cycle", "why": B("You multiplied base and power. A power repeats in a cycle, so use the remainder after dividing by 4.", "তুমি ভূমি আৰু ঘাত পূৰণ কৰিলা। ঘাত চক্ৰত ঘূৰে, সেয়ে 4ৰে হৰণ কৰি ভাগশেষ লোৱা।")}] if b * e % 10 != r else []}, [(b, e, pow(b, e, 10)) for b, e in [(3, 23), (7, 41), (2, 35), (8, 27), (13, 18)]], hints=[B("Write the first four powers' last digits.", "প্ৰথম চাৰিটা ঘাতৰ শেষৰ অংক লিখা।"), B("Divide the power by 4 and use the remainder.", "ঘাতক 4ৰে হৰণ কৰি ভাগশেষ লোৱা।")]),
        tf(f"{p}.u3.q4", "n-unit", B("$5^{100}$ ends in 5.", "$5^{100}$ৰ শেষত 5 থাকে।"), True, B("Every power of 5 ends in 5, and every power of 6 ends in 6. Their cycle has length 1.", "5ৰ প্ৰতিটো ঘাত 5ৰে আৰু 6ৰ প্ৰতিটো ঘাত 6ৰে শেষ হয়। সিহঁতৰ চক্ৰৰ দৈৰ্ঘ্য 1।")),
        match(f"{p}.u3.q5", "n-unit", B("Match the base to its cycle", "ভূমিক ইয়াৰ চক্ৰৰ সৈতে মিলোৱা"), [
            [B("2", "2"), B("2, 4, 8, 6", "2, 4, 8, 6")], [B("3", "3"), B("3, 9, 7, 1", "3, 9, 7, 1")], [B("4", "4"), B("4, 6", "4, 6")], [B("9", "9"), B("9, 1", "9, 1")],
        ], B("Bases 4 and 9 have a cycle of 2; 2, 3, 7 and 8 have a cycle of 4.", "4 আৰু 9ৰ চক্ৰ 2ৰ; 2, 3, 7 আৰু 8ৰ চক্ৰ 4ৰ।")),
    ])
    test = {"id": "test", "title": B("Numbers test", "সংখ্যাৰ পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "n-types", lambda a, b, n: {"q": B(f"How many primes are there from {a} to {b}?", f"{a}ৰ পৰা {b}লৈ কেইটা মৌলিক সংখ্যা আছে?"), "right": n, "wrong": [(n + 1, "m-odd-prime", B("An odd number is not always prime, for example 49 or 51.", "অযুগ্ম সংখ্যা সদায় মৌলিক নহয়, যেনে 49 বা 51।"))], "fill": [n - 1, n + 2, n + 3], "why": B("Strike out even numbers and multiples of 3, 5 and 7.", "যুগ্ম আৰু 3, 5, 7ৰ গুণিতক কাটি দিয়া।")}, [(40, 60, 5), (60, 80, 5), (80, 100, 3)]),
        mcq(f"{p}.t.q2", "n-div", lambda a, b, n: {"q": B(f"Which digit in place of ? makes {a}?{b} divisible by 9?", f"{a}?{b} 9ৰে হৰণ যাবলৈ ?ৰ ঠাইত কোন অংক হ'ব?"), "right": n, "wrong": [((n + 3) % 10, "m-div-last", B("Divisibility by 9 depends on the digit sum, not on any one digit.", "9ৰ বিভাজ্যতা অংকৰ যোগফলত নিৰ্ভৰ কৰে, এটা অংকত নহয়।"))], "fill": [(n + 1) % 10, (n + 5) % 10, (n + 7) % 10], "why": B(f"The digit sum becomes {sum(map(int, str(a) + str(b))) + n}, a multiple of 9.", f"অংকৰ যোগফল {sum(map(int, str(a) + str(b))) + n} হয়, 9ৰ গুণিতক।")}, [(52, 7, 4), (63, 4, 5), (81, 2, 7)]),
        mcq(f"{p}.t.q3", "n-unit", lambda b, e: {"q": B(f"The unit digit of ${b}^{{{e}}}$ is", f"${b}^{{{e}}}$ৰ একক অংক হ'ল"), "right": pow(b, e, 10), "wrong": [(b * e % 10, "m-unit-cycle", B("Multiplying base by power is not the rule. Use the cycle.", "ভূমিক ঘাতেৰে পূৰণ কৰা নিয়ম নহয়। চক্ৰ ব্যৱহাৰ কৰা।"))], "fill": [1, 3, 7, 9, 2, 4], "why": B(f"The cycle and the remainder of {e} ÷ 4 give {pow(b, e, 10)}.", f"চক্ৰ আৰু {e} ÷ 4ৰ ভাগশেষে {pow(b, e, 10)} দিয়ে।")}, [(7, 35), (3, 22), (2, 45), (8, 31)]),
        tf(f"{p}.t.q4", "n-types", B("2 is the only even prime number.", "2 একমাত্ৰ যুগ্ম মৌলিক সংখ্যা।"), True, B("Every other even number has 2 as an extra factor.", "আন প্ৰতিটো যুগ্ম সংখ্যাৰ 2 এটা অতিৰিক্ত গুণনীয়ক।")),
        solve(f"{p}.t.q5", "n-factor", lambda n, c: {"q": B(f"How many different primes divide {n}?", f"{n}ক কেইটা বেলেগ মৌলিকে হৰণ কৰে?"), "answer": str(c), "why": B(f"Peel {n} into primes and count each prime once.", f"{n}ক মৌলিকলৈ ভাঙি প্ৰতিটো মৌলিক এবাৰকৈ গণনা কৰা।")}, [(90, 3), (72, 2), (210, 4), (98, 2)]),
    ]}
    return {"id": "math-01-numbers", "no": 1, "tier": "B", "face": "numbers", "title": B("Numbers that talk", "কথা কোৱা সংখ্যা"), "reign": B("Types, divisibility, unit digits", "প্ৰকাৰ, বিভাজ্যতা, একক অংক"), "units": [u1, u2, u3], "test": test}


# ---------------------------------------------------------------- Lesson 2
def l2():
    p = "m2"
    both = (B("You swapped LCM and HCF. LCM is a shared multiple, so it is at least as big as both numbers; HCF is a shared factor.", "তুমি ল.সা.গু. আৰু গ.সা.গু. সলনি কৰিলা। ল.সা.গু. উমৈহতীয়া গুণিতক, দুয়োটা সংখ্যাতকৈ সৰু নহয়; গ.সা.গু. উমৈহতীয়া গুণনীয়ক।"))
    u1 = unit("u1", B("Shared factors: HCF", "উমৈহতীয়া গুণনীয়ক: গ.সা.গু."), "star", [
        B("A factor divides a number exactly.", "গুণনীয়কে সংখ্যাক নিঃশেষে হৰণ কৰে।"),
        B("HCF is the largest factor two numbers share.", "গ.সা.গু. দুটা সংখ্যাৰ সৰ্ববৃহৎ উমৈহতীয়া গুণনীয়ক।"),
        B("From prime peels, keep shared primes at their lower power.", "মৌলিক গুণনীয়কৰ পৰা উমৈহতীয়া মৌলিকবোৰ সৰু ঘাতত লোৱা।"),
        B("\"Largest equal pieces\" questions ask for the HCF.", "\"সৰ্ববৃহৎ সমান টুকুৰা\" ধৰণৰ প্ৰশ্নত গ.সা.গু. লাগে।"),
    ], [
        story(f"{p}.u1.s1", B("See the shared factors", "উমৈহতীয়া গুণনীয়ক চোৱা"), [
            B("Blue marks factors of 12 and yellow marks factors of 18. Red marks both.", "নীলা 12ৰ গুণনীয়ক, হালধীয়া 18ৰ গুণনীয়ক, ৰঙা দুয়োটাৰে।"),
            B("The biggest red number is the Highest Common Factor. Here it is 6.", "সৰ্ববৃহৎ ৰঙা সংখ্যাটোৱেই গৰিষ্ঠ সাধাৰণ গুণনীয়ক। ইয়াত সেয়া 6।"),
        ], widget={"kind": "hops", "a": 12, "b": 18, "mode": "factors", "max": 18}),
        story(f"{p}.u1.s2", B("HCF from prime peels", "মৌলিকৰ পৰা গ.সা.গু."), [
            B("Write both numbers as primes, then keep only what they share.", "দুয়োটা সংখ্যা মৌলিকত লিখা, তাৰ পিছত উমৈহতীয়া অংশখিনিহে ৰাখা।"),
            B("$12 = 2^2 \\times 3$ and $18 = 2 \\times 3^2$ share one 2 and one 3, which makes 6.", "$12 = 2^2 \\times 3$ আৰু $18 = 2 \\times 3^2$ত উমৈহতীয়া এটা 2 আৰু এটা 3, অৰ্থাৎ 6।"),
        ], diagram={"layout": "flow", "items": [B("Peel into primes", "মৌলিকলৈ ভাঙা"), B("Keep shared primes", "উমৈহতীয়াখিনি ৰাখা"), B("Multiply them", "পূৰণ কৰা")]}),
        explore(f"{p}.u1.q1", "l-hcf", lambda a, b: {"q": B(f"The factors of {a} are marked. Tap the largest that also divides {b}.", f"{a}ৰ গুণনীয়কবোৰ চিহ্নিত। {b}কো হৰণ কৰা সৰ্ববৃহৎটোত টিপা।"), "widget": {"kind": "hops", "a": a, "b": b, "mode": "factors", "max": min(a, b), "only": True}, "target": gcd(a, b), "answerText": B(f"HCF = {gcd(a, b)}", f"গ.সা.গু. = {gcd(a, b)}"), "why": B(f"{gcd(a, b)} is the largest number marked as a factor of both.", f"{gcd(a, b)} দুয়োটাৰে সৰ্ববৃহৎ গুণনীয়ক।")}, [(16, 24), (18, 30), (20, 28), (24, 36)]),
        solve(f"{p}.u1.q2", "l-hcf", lambda a, b: {"q": B(f"Find the HCF of {a} and {b}.", f"{a} আৰু {b}ৰ গ.সা.গু. উলিওৱা।"), "answer": str(gcd(a, b)), "why": B(f"Peel both into primes and multiply what they share to get {gcd(a, b)}.", f"দুয়োটা মৌলিকলৈ ভাঙি উমৈহতীয়াখিনি পূৰণ কৰিলে {gcd(a, b)} হয়।"), "traps": [{"ans": str(lcm(a, b)), "tag": "m-lcm-hcf-swap", "why": both}]}, [(48, 180), (84, 126), (72, 120), (60, 150)], hints=[B("Divide both by 2 while you can, then try 3.", "যিমান পাৰা দুয়োটাক 2ৰে হৰণ কৰা, তাৰ পিছত 3ৰে চোৱা।")]),
        tf(f"{p}.u1.q3", "l-hcf", B("Two different primes always have HCF 1.", "দুটা বেলেগ মৌলিকৰ গ.সা.গু. সদায় 1।"), True, B("Each prime has only 1 and itself as factors, so 1 is all they share.", "প্ৰতিটো মৌলিকৰ গুণনীয়ক 1 আৰু নিজে, সেয়ে উমৈহতীয়া কেৱল 1।")),
        stepwise(f"{p}.u1.q4", "l-hcf", lambda a, b, c: {"q": B(f"Ropes of {a} m, {b} m and {c} m must be cut into equal pieces, as long as possible. How long is each piece?", f"{a} মি, {b} মি আৰু {c} মি ৰচী যিমান পাৰি দীঘল সমান টুকুৰাত কাটিব লাগে। প্ৰতিটো টুকুৰা কিমান দীঘল?"), "parts": [
            part(B("What does the question want?", "প্ৰশ্নটোৱে কি বিচাৰিছে?"), B("The HCF: largest equal piece", "গ.সা.গু.: সৰ্ববৃহৎ সমান টুকুৰা"), [B("The LCM: smallest shared length", "ল.সা.গু.: সৰুতম উমৈহতীয়া দৈৰ্ঘ্য")], B("Cutting into largest equal parts is a shared factor.", "সৰ্ববৃহৎ সমান টুকুৰা মানে উমৈহতীয়া গুণনীয়ক।"), tag="m-lcm-hcf-swap", sid=f"{a}"),
            part(B("HCF of the first two?", "প্ৰথম দুটাৰ গ.সা.গু.?"), B(str(gcd(a, b)), str(gcd(a, b))), [B(str(gcd(a, b) * 2), str(gcd(a, b) * 2)), B(str(max(1, gcd(a, b) // 2) + 1), str(max(1, gcd(a, b) // 2) + 1))], B("Peel the two numbers into primes.", "সংখ্যা দুটা মৌলিকলৈ ভাঙা।"), sid=f"{a}"),
            part(B("Now include the third", "এতিয়া তৃতীয়টো লোৱা"), B(f"{gcd(gcd(a, b), c)} m", f"{gcd(gcd(a, b), c)} মি"), [B(f"{gcd(gcd(a, b), c) * 3} m", f"{gcd(gcd(a, b), c) * 3} মি"), B(f"{gcd(gcd(a, b), c) + 1} m", f"{gcd(gcd(a, b), c) + 1} মি")], B("Take the HCF of your result with the third length.", "পোৱা ফল আৰু তৃতীয় দৈৰ্ঘ্যৰ গ.সা.গু. লোৱা।"), sid=f"{a}"),
        ], "why": B("HCF of three numbers: find it for two, then with the third.", "তিনিটা সংখ্যাৰ গ.সা.গু.: দুটাৰ উলিয়াই তৃতীয়টোৰ সৈতে লোৱা।")}, [(84, 126, 210), (60, 96, 132), (72, 108, 180)]),
        odd(f"{p}.u1.q5", "n-factor", lambda a, x, y, z, n: {"q": B(f"Which is not a factor of {n}?", f"কোনটো {n}ৰ গুণনীয়ক নহয়?"), "right": a, "fill": [x, y, z], "why": B(f"{n} ÷ {a} leaves a remainder, so {a} is not a factor.", f"{n} ÷ {a}ত ভাগশেষ থাকে, সেয়ে {a} গুণনীয়ক নহয়।")}, [(8, 3, 6, 9, 54), (12, 7, 3, 14, 42), (9, 5, 4, 15, 60)]),
    ])
    u2 = unit("u2", B("Shared multiples: LCM", "উমৈহতীয়া গুণিতক: ল.সা.গু."), "star", [
        B("A multiple is the number's times table.", "গুণিতক মানে সংখ্যাটোৰ নামতা।"),
        B("LCM is the smallest multiple two numbers share.", "ল.সা.গু. দুটা সংখ্যাৰ সৰুতম উমৈহতীয়া গুণিতক।"),
        B("From prime peels, take every prime at its highest power.", "মৌলিকৰ পৰা প্ৰতিটো মৌলিক ডাঙৰ ঘাতত লোৱা।"),
        B("\"Happen together again\" questions ask for the LCM.", "\"আকৌ একেলগে হ'ব\" ধৰণৰ প্ৰশ্নত ল.সা.গু. লাগে।"),
    ], [
        story(f"{p}.u2.s1", B("When two rhythms meet", "দুটা ছন্দ ক'ত লগ হয়"), [
            B("Hop by 4 and by 6 along the strip. The red squares are where both land.", "পট্টীডালত 4 আৰু 6ৰে জঁপিওৱা। ৰঙা ঘৰত দুয়োটা পৰে।"),
            B("The first red square is the Lowest Common Multiple: 12.", "প্ৰথম ৰঙা ঘৰটোৱেই লঘিষ্ঠ সাধাৰণ গুণিতক: 12।"),
        ], widget={"kind": "hops", "a": 4, "b": 6, "max": 40}),
        story(f"{p}.u2.s2", B("LCM from prime peels", "মৌলিকৰ পৰা ল.সা.গু."), [
            B("Take each prime at its highest power from either number.", "দুয়োটা সংখ্যাৰ পৰা প্ৰতিটো মৌলিক ডাঙৰ ঘাতত লোৱা।"),
            B("$12 = 2^2 \\times 3$ and $18 = 2 \\times 3^2$ give $2^2 \\times 3^2 = 36$.", "$12 = 2^2 \\times 3$ আৰু $18 = 2 \\times 3^2$ৰ পৰা $2^2 \\times 3^2 = 36$।"),
        ], diagram={"layout": "grid", "items": [B("HCF: lower powers of shared primes", "গ.সা.গু.: উমৈহতীয়া মৌলিকৰ সৰু ঘাত"), B("LCM: highest powers of all primes", "ল.সা.গু.: সকলো মৌলিকৰ ডাঙৰ ঘাত")]}),
        explore(f"{p}.u2.q1", "l-lcm", lambda a, b: {"q": B(f"The multiples of {b} are marked. Tap the first one that {a} also divides.", f"{b}ৰ গুণিতকবোৰ চিহ্নিত। {a}য়েও হৰণ কৰা প্ৰথমটোত টিপা।"), "widget": {"kind": "hops", "a": a, "b": b, "max": 60, "only": True}, "target": lcm(a, b), "answerText": B(f"LCM = {lcm(a, b)}", f"ল.সা.গু. = {lcm(a, b)}"), "why": B(f"{lcm(a, b)} is the first number on both lists.", f"{lcm(a, b)} দুয়োটা তালিকাৰ প্ৰথম উমৈহতীয়া সংখ্যা।"), "traps": [{"val": a * b, "tag": "m-lcm-product", "why": B(f"{a} × {b} is a common multiple, but not always the smallest.", f"{a} × {b} উমৈহতীয়া গুণিতক, কিন্তু সদায় সৰুতম নহয়।")}] if a * b <= 60 else []}, [(6, 8), (6, 10), (8, 12), (9, 12)]),
        solve(f"{p}.u2.q2", "l-lcm", lambda a, b: {"q": B(f"Find the LCM of {a} and {b}.", f"{a} আৰু {b}ৰ ল.সা.গু. উলিওৱা।"), "answer": str(lcm(a, b)), "why": B(f"Highest powers of each prime multiply to {lcm(a, b)}.", f"প্ৰতিটো মৌলিকৰ ডাঙৰ ঘাতৰ পূৰণফল {lcm(a, b)}।"), "traps": [{"ans": str(gcd(a, b)), "tag": "m-lcm-hcf-swap", "why": both}, {"ans": str(a * b), "tag": "m-lcm-product", "why": B("Multiplying gives a common multiple, but divide by the HCF to get the lowest one.", "পূৰণ কৰিলে উমৈহতীয়া গুণিতক পোৱা যায়, সৰুতমটোৰ বাবে গ.সা.গু.ৰে হৰণ কৰা।")}]}, [(12, 18), (15, 20), (24, 36), (16, 28)], hints=[B("Peel both into primes.", "দুয়োটা মৌলিকলৈ ভাঙা।"), B("Take each prime at its highest power.", "প্ৰতিটো মৌলিক ডাঙৰ ঘাতত লোৱা।")]),
        tf(f"{p}.u2.q3", "l-lcm", B("The LCM of two numbers can be smaller than the larger number.", "দুটা সংখ্যাৰ ল.সা.গু. ডাঙৰ সংখ্যাটোতকৈ সৰু হ'ব পাৰে।"), False, B("The LCM is a multiple of both, so it is never below the larger number.", "ল.সা.গু. দুয়োটাৰে গুণিতক, সেয়ে ই ডাঙৰ সংখ্যাটোতকৈ কেতিয়াও সৰু নহয়।"), ("m-lcm-hcf-swap", both)),
        match(f"{p}.u2.q4", "l-apply", B("Which one does each question need?", "কোন প্ৰশ্নত কোনটো লাগে?"), [
            [B("Bells ring together again", "ঘণ্টা আকৌ একেলগে বাজে"), B("LCM of the gaps", "সময়বোৰৰ ল.সা.গু.")], [B("Largest tile for a floor", "মজিয়াৰ বাবে সৰ্ববৃহৎ টাইল"), B("HCF of the sides", "বাহুবোৰৰ গ.সা.গু.")], [B("Smallest number divisible by 8 and 12", "8 আৰু 12ৰে হৰণ যোৱা সৰুতম সংখ্যা"), B("24", "24")], [B("Largest number dividing 8 and 12", "8 আৰু 12ক হৰণ কৰা সৰ্ববৃহৎ সংখ্যা"), B("4", "4")],
        ], B("Smallest and repeating: LCM. Largest and dividing up: HCF.", "সৰুতম আৰু পুনৰাবৃত্তি: ল.সা.গু.। সৰ্ববৃহৎ আৰু ভগোৱা: গ.সা.গু.।")),
        stepwise(f"{p}.u2.q5", "l-apply", lambda a, b, c: {"q": B(f"Three bells ring every {a}, {b} and {c} minutes. They ring together at 9:00. After how many minutes do they next ring together?", f"তিনিটা ঘণ্টা {a}, {b} আৰু {c} মিনিটৰ মূৰে মূৰে বাজে। 9:00ত একেলগে বাজিলে পিছত কিমান মিনিটত একেলগে বাজিব?"), "parts": [
            part(B("Which tool fits?", "কোনটো লাগিব?"), B("LCM", "ল.সা.গু."), [B("HCF", "গ.সা.গু."), B("Add the gaps", "সময়বোৰ যোগ কৰা")], B("Repeating events meet at a common multiple.", "পুনৰাবৃত্ত ঘটনা উমৈহতীয়া গুণিতকত মিলে।"), tag="m-lcm-hcf-swap", sid=str(a)),
            part(B(f"LCM of {a} and {b}?", f"{a} আৰু {b}ৰ ল.সা.গু.?"), B(str(lcm(a, b)), str(lcm(a, b))), [B(str(a * b + a), str(a * b + a)), B(str(gcd(a, b)), str(gcd(a, b)))], B("Use prime peels.", "মৌলিক ব্যৱহাৰ কৰা।"), sid=str(a)),
            part(B(f"Now with {c}", f"এতিয়া {c}ৰ সৈতে"), B(f"{lcm(lcm(a, b), c)} minutes", f"{lcm(lcm(a, b), c)} মিনিট"), [B(f"{lcm(a, b) * c * 2} minutes", f"{lcm(a, b) * c * 2} মিনিট"), B(f"{a + b + c} minutes", f"{a + b + c} মিনিট")], B("LCM of your result and the third gap.", "পোৱা ফল আৰু তৃতীয় সময়ৰ ল.সা.গু.।"), sid=str(a)),
        ], "why": B("Find the LCM for two, then with the third.", "দুটাৰ ল.সা.গু. উলিয়াই তৃতীয়টোৰ সৈতে লোৱা।")}, [(6, 8, 12), (4, 6, 15), (10, 12, 15)]),
    ])
    u3 = unit("u3", B("The HCF × LCM rule", "গ.সা.গু. × ল.সা.গু. নিয়ম"), "star", [
        B("For two numbers, HCF × LCM = first × second.", "দুটা সংখ্যাৰ বাবে গ.সা.গু. × ল.সা.গু. = প্ৰথম × দ্বিতীয়।"),
        B("The HCF always divides the LCM.", "গ.সা.গু.য়ে ল.সা.গু.ক সদায় হৰণ কৰে।"),
        B("Numbers in ratio a:b are ax and bx, and their HCF is x when a and b share nothing.", "a:b অনুপাতৰ সংখ্যা ax আৰু bx; a আৰু bৰ উমৈহতীয়া গুণনীয়ক নাথাকিলে সিহঁতৰ গ.সা.গু. x।"),
        B("The remainder trick: subtract the remainder before finding the HCF.", "ভাগশেষৰ কৌশল: গ.সা.গু. উলিওৱাৰ আগতে ভাগশেষ বিয়োগ কৰা।"),
    ], [
        story(f"{p}.u3.s1", B("A shortcut worth marks", "নম্বৰ দিয়া চুটি পথ"), [
            B("For any two numbers, the HCF and LCM multiply to the same value as the numbers themselves.", "যিকোনো দুটা সংখ্যাৰ গ.সা.গু. আৰু ল.সা.গু.ৰ পূৰণফল সংখ্যা দুটাৰ পূৰণফলৰ সমান।"),
            B("Give any three of the four values and the last is one division away.", "চাৰিটাৰ তিনিটা জানিলে চতুৰ্থটো এটা হৰণতে ওলায়।"),
        ], diagram={"layout": "flow", "items": [B("$12 \\times 18 = 216$", "$12 \\times 18 = 216$"), B("$6 \\times 36 = 216$", "$6 \\times 36 = 216$"), B("Always equal", "সদায় সমান")]}),
        story(f"{p}.u3.s2", B("Numbers hidden in a ratio", "অনুপাতৰ ভিতৰত লুকোৱা সংখ্যা"), [
            B("If two numbers are in the ratio 3:4, write them as $3x$ and $4x$.", "দুটা সংখ্যাৰ অনুপাত 3:4 হ'লে সিহঁতক $3x$ আৰু $4x$ বুলি লিখা।"),
            B("Then $x$ is their HCF, and their LCM is $12x$.", "তেতিয়া $x$ সিহঁতৰ গ.সা.গু. আৰু $12x$ ল.সা.গু.।"),
        ], diagram={"layout": "flow", "items": [B("Ratio 3:4", "অনুপাত 3:4"), B("$3x$ and $4x$", "$3x$ আৰু $4x$"), B("HCF $x$, LCM $12x$", "গ.সা.গু. $x$, ল.সা.গু. $12x$")]}),
        solve(f"{p}.u3.q1", "l-apply", lambda a, b: {"q": B(f"Two numbers have HCF {gcd(a, b)} and LCM {lcm(a, b)}. One is {a}. Find the other.", f"দুটা সংখ্যাৰ গ.সা.গু. {gcd(a, b)} আৰু ল.সা.গু. {lcm(a, b)}। এটা {a}। আনটো উলিওৱা।"), "answer": str(b), "why": B(f"{gcd(a, b)} × {lcm(a, b)} ÷ {a} = {b}.", f"{gcd(a, b)} × {lcm(a, b)} ÷ {a} = {b}।")}, [(24, 36), (15, 25), (18, 42), (30, 45)], hints=[B("HCF × LCM = first × second.", "গ.সা.গু. × ল.সা.গু. = প্ৰথম × দ্বিতীয়।")]),
        tf(f"{p}.u3.q2", "l-apply", B("Two numbers can have HCF 8 and LCM 60.", "দুটা সংখ্যাৰ গ.সা.গু. 8 আৰু ল.সা.গু. 60 হ'ব পাৰে।"), False, B("The HCF must divide the LCM, and 8 does not divide 60.", "গ.সা.গু.য়ে ল.সা.গু.ক হৰণ কৰিবই লাগিব, 8য়ে 60ক হৰণ নকৰে।")),
        stepwise(f"{p}.u3.q3", "l-apply", lambda a, b, x: {"q": B(f"Two numbers are in the ratio {a}:{b} and their HCF is {x}. What is their LCM?", f"দুটা সংখ্যাৰ অনুপাত {a}:{b} আৰু গ.সা.গু. {x}। ল.সা.গু. কিমান?"), "parts": [
            part(B("Write the numbers", "সংখ্যা দুটা লিখা"), B(f"{a * x} and {b * x}", f"{a * x} আৰু {b * x}"), [B(f"{a} and {b}", f"{a} আৰু {b}"), B(f"{a + x} and {b + x}", f"{a + x} আৰু {b + x}")], B("Multiply each ratio part by the HCF.", "অনুপাতৰ প্ৰতিটো ভাগক গ.সা.গু.ৰে পূৰণ কৰা।"), tag="m-ratio-part", sid=str(x)),
            part(B("Then the LCM", "তাৰ পিছত ল.সা.গু."), B(str(a * b * x), str(a * b * x)), [B(str(a * b * x * x), str(a * b * x * x)), B(str((a + b) * x), str((a + b) * x))], B("LCM = first × second ÷ HCF.", "ল.সা.গু. = প্ৰথম × দ্বিতীয় ÷ গ.সা.গু.।"), sid=str(x)),
        ], "why": B("Ratio parts with no common factor: LCM is a × b × HCF.", "উমৈহতীয়া গুণনীয়ক নথকা অনুপাতত ল.সা.গু. = a × b × গ.সা.গু.।")}, [(3, 4, 6), (2, 5, 7), (4, 5, 3)]),
        solve(f"{p}.u3.q4", "l-apply", lambda x, y, r: {"q": B(f"Find the largest number that divides {x} and {y} and leaves remainder {r} each time.", f"{x} আৰু {y}ক হৰণ কৰি প্ৰতিবাৰে {r} ভাগশেষ ৰখা সৰ্ববৃহৎ সংখ্যাটো উলিওৱা।"), "answer": str(gcd(x - r, y - r)), "why": B(f"Remove the remainder: {x - r} and {y - r}. Their HCF is {gcd(x - r, y - r)}.", f"ভাগশেষ বাদ দিয়া: {x - r} আৰু {y - r}। সিহঁতৰ গ.সা.গু. {gcd(x - r, y - r)}।"), "traps": [{"ans": str(gcd(x, y)), "tag": "m-hcf-remainder", "why": B("Subtract the remainder from both numbers before finding the HCF.", "গ.সা.গু. উলিওৱাৰ আগতে দুয়োটাৰ পৰা ভাগশেষ বিয়োগ কৰা।")}] if gcd(x, y) != gcd(x - r, y - r) else []}, [(40, 64, 4), (55, 79, 7), (62, 92, 2)], hints=[B("Subtract the remainder from each number.", "প্ৰতিটো সংখ্যাৰ পৰা ভাগশেষ বিয়োগ কৰা।")]),
        odd(f"{p}.u3.q5", "l-apply", lambda a, x, y, z, l: {"q": B(f"Which of these cannot be the HCF of two numbers whose LCM is {l}?", f"ল.সা.গু. {l} হোৱা দুটা সংখ্যাৰ গ.সা.গু. তলৰ কোনটো হ'ব নোৱাৰে?"), "right": a, "fill": [x, y, z], "why": B(f"{a} does not divide {l}, and the HCF always divides the LCM.", f"{a}য়ে {l}ক হৰণ নকৰে, অথচ গ.সা.গু.য়ে ল.সা.গু.ক সদায় হৰণ কৰে।")}, [(8, 3, 4, 6, 60), (7, 5, 3, 15, 90), (9, 4, 6, 12, 120)]),
        match(f"{p}.u3.q6", "l-hcf", B("Match each pair to its HCF", "প্ৰতিটো যোৰক গ.সা.গু.ৰ সৈতে মিলোৱা"), [
            [B("8, 12", "8, 12"), B("4", "4")], [B("9, 15", "9, 15"), B("3", "3")], [B("14, 21", "14, 21"), B("7", "7")], [B("15, 28", "15, 28"), B("1", "1")],
        ], B("15 and 28 share no prime, so they are co-prime and their HCF is 1.", "15 আৰু 28ৰ উমৈহতীয়া মৌলিক নাই, সেয়ে সিহঁত সহমৌলিক, গ.সা.গু. 1।")),
    ])
    test = {"id": "test", "title": B("LCM and HCF test", "ল.সা.গু. আৰু গ.সা.গু. পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "l-lcm", lambda a, b, c: {"q": B(f"The LCM of {a}, {b} and {c} is", f"{a}, {b} আৰু {c}ৰ ল.সা.গু. হ'ল"), "right": lcm(lcm(a, b), c), "wrong": [(a * b * c, "m-lcm-product", B("Multiplying all three gives a common multiple, not the lowest.", "তিনিওটা পূৰণ কৰিলে উমৈহতীয়া গুণিতক পোৱা যায়, সৰুতমটো নহয়।")), (gcd(gcd(a, b), c), "m-lcm-hcf-swap", both)], "fill": [lcm(lcm(a, b), c) * 2, lcm(lcm(a, b), c) * 3], "why": B("Peel into primes and take each at its highest power.", "মৌলিকলৈ ভাঙি প্ৰতিটো ডাঙৰ ঘাতত লোৱা।")}, [(6, 8, 12), (10, 15, 20), (9, 12, 18)]),
        mcq(f"{p}.t.q2", "l-hcf", lambda a, b, c: {"q": B(f"The HCF of {a}, {b} and {c} is", f"{a}, {b} আৰু {c}ৰ গ.সা.গু. হ'ল"), "right": gcd(gcd(a, b), c), "wrong": [(lcm(lcm(a, b), c), "m-lcm-hcf-swap", both)], "fill": [gcd(gcd(a, b), c) * 2, gcd(gcd(a, b), c) * 3, gcd(gcd(a, b), c) + 1], "why": B("It is the largest number dividing all three.", "তিনিওটাকে হৰণ কৰা সৰ্ববৃহৎ সংখ্যা।")}, [(36, 84, 132), (48, 72, 120), (45, 75, 105)]),
        mcq(f"{p}.t.q3", "l-apply", lambda a, b, c, r: {"q": B(f"The smallest number which leaves remainder {r} when divided by {a}, {b} or {c} is", f"{a}, {b} বা {c}ৰে হৰণ কৰিলে {r} ভাগশেষ ৰখা সৰুতম সংখ্যাটো"), "right": lcm(lcm(a, b), c) + r, "wrong": [(lcm(lcm(a, b), c), "m-hcf-remainder", B("That number divides exactly. Add the remainder to the LCM.", "সেই সংখ্যাই নিঃশেষে হৰণ যায়। ল.সা.গু.ত ভাগশেষ যোগ কৰা।"))], "fill": [lcm(lcm(a, b), c) - r, lcm(lcm(a, b), c) + r + a, 2 * lcm(lcm(a, b), c) + r], "why": B("LCM plus the remainder.", "ল.সা.গু. + ভাগশেষ।")}, [(6, 8, 12, 3), (5, 6, 10, 2), (4, 9, 12, 1)]),
        mcq(f"{p}.t.q4", "l-apply", lambda a, b: {"q": B(f"The product of two numbers is {a * b} and their HCF is {gcd(a, b)}. Their LCM is", f"দুটা সংখ্যাৰ পূৰণফল {a * b} আৰু গ.সা.গু. {gcd(a, b)}। ল.সা.গু. হ'ল"), "right": lcm(a, b), "wrong": [(a * b * gcd(a, b), "m-hcf-divide", B("Divide the product by the HCF; do not multiply.", "পূৰণফলক গ.সা.গু.ৰে হৰণ কৰা, পূৰণ নকৰিবা।"))], "fill": [lcm(a, b) * 2, lcm(a, b) + gcd(a, b), lcm(a, b) - gcd(a, b)], "why": B("LCM = product ÷ HCF.", "ল.সা.গু. = পূৰণফল ÷ গ.সা.গু.।")}, [(24, 36), (18, 30), (20, 50)]),
        solve(f"{p}.t.q5", "l-apply", lambda a, b, c: {"q": B(f"Lights flash every {a}, {b} and {c} seconds. How many seconds pass before they flash together again?", f"বন্তি {a}, {b} আৰু {c} ছেকেণ্ডৰ মূৰে মূৰে জ্বলে। কিমান ছেকেণ্ডৰ পিছত আকৌ একেলগে জ্বলিব?"), "answer": str(lcm(lcm(a, b), c)), "why": B("Repeating events meet at the LCM.", "পুনৰাবৃত্ত ঘটনা ল.সা.গু.ত মিলে।")}, [(4, 6, 9), (8, 12, 18), (5, 6, 8)]),
    ]}
    return {"id": "math-02-lcm-hcf", "no": 2, "tier": "A", "face": "lcm", "title": B("LCM and HCF", "ল.সা.গু. আৰু গ.সা.গু."), "reign": B("Factors, multiples, the product rule", "গুণনীয়ক, গুণিতক, পূৰণফলৰ নিয়ম"), "units": [u1, u2, u3], "test": test}
