"""Mathematics lessons 3 and 5: fractions and percentage. All worked numbers are original."""
from fractions import Fraction as F
from math import gcd
from math_kit import B, explore, fr, match, mcq, num, odd, order, part, show, solve, story, stepwise, tf, unit


def lcm(a, b):
    return a * b // gcd(a, b)


# ---------------------------------------------------------------- Lesson 3
def l3():
    p = "m3"
    tops = B("You added tops and bottoms. Fractions add only when the pieces are the same size, so make the denominators equal first.", "তুমি লব আৰু হৰ যোগ কৰিলা। টুকুৰা একে আকাৰৰ হ'লেহে যোগ হয়, সেয়ে প্ৰথমে হৰ সমান কৰা।")
    u1 = unit("u1", B("What a fraction is", "ভগ্নাংশ কি"), "star", [
        B("The denominator says how many equal parts; the numerator says how many you take.", "হৰে সমান ভাগৰ সংখ্যা কয়; লবে কয় কিমান ভাগ ল'বা।"),
        B("The parts must be equal, or the fraction means nothing.", "ভাগবোৰ সমান হ'বই লাগিব।"),
        B("Multiplying top and bottom by the same number keeps the value.", "লব আৰু হৰক একে সংখ্যাৰে পূৰণ কৰিলে মান নসলনি হয়।"),
        B("Simplest form: divide top and bottom by their HCF.", "সৰলতম ৰূপ: লব আৰু হৰক সিহঁতৰ গ.সা.গু.ৰে হৰণ কৰা।"),
    ], [
        story(f"{p}.u1.s1", B("Cut, then count", "কাটা, তাৰ পিছত গণা"), [
            B("A fraction is two instructions: cut into equal parts, then take some.", "ভগ্নাংশ দুটা নিৰ্দেশ: সমান ভাগত কাটা, তাৰ পিছত কিছু লোৱা।"),
            B("Change the number of parts and tap some. Watch the fraction change.", "ভাগৰ সংখ্যা সলনি কৰি কিছুমান টিপা। ভগ্নাংশ কেনেকৈ সলনি হয় চোৱা।"),
        ], widget={"kind": "fracbar", "n": 4, "shade": 1, "split": True}),
        story(f"{p}.u1.s2", B("Same amount, new name", "একে পৰিমাণ, নতুন নাম"), [
            B("Cut each piece in two: there are twice as many parts, and you take twice as many.", "প্ৰতিটো টুকুৰা দুভাগ কৰা: ভাগ দুগুণ হ'ল, লোৱা ভাগো দুগুণ হ'ল।"),
            B("The shaded amount has not moved, so $\\frac{1}{2} = \\frac{2}{4} = \\frac{4}{8}$.", "ৰঙোৱা পৰিমাণ সলনি হোৱা নাই, সেয়ে $\\frac{1}{2} = \\frac{2}{4} = \\frac{4}{8}$।"),
        ], widget={"kind": "fracbar", "n": 8, "shade": 4, "ref": [1, 2], "split": True}),
        explore(f"{p}.u1.q1", "f-meaning", lambda a, b: {"q": B(f"Shade ${fr(a, b)}$ of the bar.", f"বাৰডালৰ ${fr(a, b)}$ অংশ ৰঙোৱা।"), "widget": {"kind": "fracbar", "n": b}, "target": a / b, "answerText": B(f"{a} of {b} parts", f"{b}টাৰ {a}টা ভাগ"), "why": B(f"The bar has {b} equal parts, so take {a} of them.", f"বাৰত {b}টা সমান ভাগ, তাৰ {a}টা লোৱা।")}, [(3, 4), (2, 5), (5, 6), (3, 8)]),
        explore(f"{p}.u1.q2", "f-equiv", lambda a, b, k: {"q": B(f"The top bar shows ${fr(a, b)}$. Shade the same amount on the bar with {b * k} parts.", f"ওপৰৰ বাৰত ${fr(a, b)}$ দেখুওৱা আছে। {b * k}টা ভাগৰ বাৰত একে পৰিমাণ ৰঙোৱা।"), "widget": {"kind": "fracbar", "n": b * k, "ref": [a, b]}, "target": a / b, "answerText": B(f"${fr(a * k, b * k)}$", f"${fr(a * k, b * k)}$"), "why": B(f"Multiply top and bottom by {k}: ${fr(a, b)} = {fr(a * k, b * k)}$.", f"লব আৰু হৰক {k}ৰে পূৰণ কৰা: ${fr(a, b)} = {fr(a * k, b * k)}$।")}, [(2, 3, 2), (3, 4, 2), (1, 3, 3), (2, 5, 2)]),
        solve(f"{p}.u1.q3", "f-equiv", lambda a, b, h: {"q": B(f"Write ${fr(a, b)}$ in simplest form.", f"${fr(a, b)}$ক সৰলতম ৰূপত লিখা।"), "answer": f"{a // h}/{b // h}", "exact": True, "why": B(f"The HCF is {h}: divide top and bottom by it.", f"গ.সা.গু. {h}: লব আৰু হৰক ইয়াৰে হৰণ কৰা।"), "traps": [{"ans": f"{a // 2}/{b // 2}", "tag": "m-simplify-partial", "why": B("That is equal, but not finished. Keep dividing until nothing is shared.", "সেয়া সমান, কিন্তু শেষ হোৱা নাই। উমৈহতীয়া গুণনীয়ক নোহোৱালৈ হৰণ কৰি থাকা।")}]}, [(18, 24, 6), (36, 48, 12), (24, 60, 12), (32, 48, 16)], hints=[B("Type your answer as top/bottom, using the / key.", "উত্তৰ লব/হৰ ৰূপত লিখা, / বুটাম টিপি।")]),
        tf(f"{p}.u1.q4", "f-meaning", B("$\\frac{3}{4}$ means 3 parts out of 4 parts of any size.", "$\\frac{3}{4}$ মানে যিকোনো আকাৰৰ 4 ভাগৰ 3 ভাগ।"), False, B("The four parts must be equal. Without equal parts it is not three quarters.", "চাৰিওটা ভাগ সমান হ'বই লাগিব। সমান নহ'লে সেয়া তিনি-চতুৰ্থাংশ নহয়।")),
        match(f"{p}.u1.q5", "f-equiv", B("Match the equal fractions", "সমান ভগ্নাংশবোৰ মিলোৱা"), [
            [B("$\\frac{1}{2}$", "$\\frac{1}{2}$"), B("$\\frac{7}{14}$", "$\\frac{7}{14}$")], [B("$\\frac{2}{3}$", "$\\frac{2}{3}$"), B("$\\frac{10}{15}$", "$\\frac{10}{15}$")], [B("$\\frac{3}{5}$", "$\\frac{3}{5}$"), B("$\\frac{12}{20}$", "$\\frac{12}{20}$")], [B("$\\frac{5}{6}$", "$\\frac{5}{6}$"), B("$\\frac{15}{18}$", "$\\frac{15}{18}$")],
        ], B("Divide top and bottom of the longer fraction by their HCF.", "ডাঙৰ ভগ্নাংশৰ লব আৰু হৰক গ.সা.গু.ৰে হৰণ কৰা।")),
    ])
    u2 = unit("u2", B("Compare and add", "তুলনা আৰু যোগ"), "star", [
        B("Same denominator: the bigger numerator wins.", "হৰ একে হ'লে ডাঙৰ লবৰ ভগ্নাংশ ডাঙৰ।"),
        B("Same numerator: the smaller denominator wins, because the pieces are bigger.", "লব একে হ'লে সৰু হৰৰ ভগ্নাংশ ডাঙৰ, কাৰণ টুকুৰা ডাঙৰ।"),
        B("Otherwise cross-multiply, or use the LCM of the denominators.", "নহ'লে তিৰ্যক পূৰণ কৰা বা হৰবোৰৰ ল.সা.গু. লোৱা।"),
        B("To add, make the denominators equal, then add only the tops.", "যোগ কৰিবলৈ হৰ সমান কৰি কেৱল লব যোগ কৰা।"),
    ], [
        story(f"{p}.u2.s1", B("Fractions live on a line", "ভগ্নাংশ ৰেখাত থাকে"), [
            B("Every fraction is a point. Drag along the line in steps of one eighth.", "প্ৰতিটো ভগ্নাংশ এটা বিন্দু। এক-অষ্টমাংশকৈ ৰেখাত টানি চোৱা।"),
            B("Where the point sits decides which fraction is bigger, not how big the digits look.", "কোনটো ডাঙৰ সেয়া বিন্দুৰ স্থানে ঠিক কৰে, অংকৰ আকাৰে নহয়।"),
        ], widget={"kind": "numline", "max": 1, "den": 8, "start": 0.25}),
        story(f"{p}.u2.s2", B("Same-size pieces first", "প্ৰথমে একে আকাৰৰ টুকুৰা"), [
            B("You cannot add thirds to quarters directly, just as you cannot add rupees to kilograms.", "তৃতীয়াংশ আৰু চতুৰ্থাংশ পোনে পোনে যোগ নহয়, টকা আৰু কিলোগ্ৰাম যোগ নোহোৱাৰ দৰে।"),
            B("The LCM of the denominators gives a common piece size.", "হৰবোৰৰ ল.সা.গু.য়ে একে আকাৰৰ টুকুৰা দিয়ে।"),
        ], diagram={"layout": "flow", "items": [B("$\\frac{1}{3} + \\frac{1}{4}$", "$\\frac{1}{3} + \\frac{1}{4}$"), B("LCM of 3, 4 is 12", "3, 4ৰ ল.সা.গু. 12"), B("$\\frac{4}{12} + \\frac{3}{12}$", "$\\frac{4}{12} + \\frac{3}{12}$"), B("$\\frac{7}{12}$", "$\\frac{7}{12}$")]}),
        explore(f"{p}.u2.q1", "f-compare", lambda a, d: {"q": B(f"Place ${fr(a, d)}$ on the line.", f"${fr(a, d)}$ক ৰেখাত ৰাখা।"), "widget": {"kind": "numline", "max": 1, "den": d}, "target": a / d, "answerText": B(f"Notch {a} of {d}", f"{d}ৰ {a} নম্বৰ দাগ"), "why": B(f"The line is cut into {d} equal steps. Go {a} steps from 0.", f"ৰেখাডাল {d}টা সমান খোজত ভগোৱা। 0ৰ পৰা {a} খোজ যোৱা।")}, [(5, 8), (3, 10), (7, 12), (2, 6)]),
        order(f"{p}.u2.q2", "f-compare", B("Put these in order, smallest first", "সৰুৰ পৰা ডাঙৰলৈ সজোৱা"), [B("$\\frac{1}{5}$", "$\\frac{1}{5}$"), B("$\\frac{1}{4}$", "$\\frac{1}{4}$"), B("$\\frac{1}{3}$", "$\\frac{1}{3}$"), B("$\\frac{1}{2}$", "$\\frac{1}{2}$")], B("With equal numerators, a bigger denominator means smaller pieces.", "লব একে হ'লে ডাঙৰ হৰ মানে সৰু টুকুৰা।")),
        tf(f"{p}.u2.q3", "f-compare", B("$\\frac{1}{8}$ is bigger than $\\frac{1}{6}$ because 8 is bigger than 6.", "8 ডাঙৰ, সেয়ে $\\frac{1}{8}$ $\\frac{1}{6}$তকৈ ডাঙৰ।"), False, B("Cutting into 8 gives smaller pieces than cutting into 6.", "8 ভাগ কৰিলে টুকুৰা 6 ভাগতকৈ সৰু হয়।"), ("m-cmp-denom", B("A bigger denominator means smaller pieces, not a bigger fraction.", "ডাঙৰ হৰ মানে সৰু টুকুৰা, ডাঙৰ ভগ্নাংশ নহয়।"))),
        solve(f"{p}.u2.q4", "f-add", lambda a, b, c, d: {"q": B(f"Add: ${fr(a, b)} + {fr(c, d)}$", f"যোগ কৰা: ${fr(a, b)} + {fr(c, d)}$"), "answer": num(F(a, b) + F(c, d)), "why": B(f"Common denominator {(F(a, b) + F(c, d)).denominator}: the sum is ${fr((F(a, b) + F(c, d)).numerator, (F(a, b) + F(c, d)).denominator)}$.", f"উমৈহতীয়া হৰ {(F(a, b) + F(c, d)).denominator}: যোগফল ${fr((F(a, b) + F(c, d)).numerator, (F(a, b) + F(c, d)).denominator)}$।"), "traps": [{"ans": f"{a + c}/{b + d}", "tag": "m-add-tops", "why": tops}]}, [(1, 3, 1, 4), (2, 5, 1, 3), (1, 6, 3, 8), (3, 10, 2, 5)], hints=[B("Find the LCM of the denominators.", "হৰবোৰৰ ল.সা.গু. উলিওৱা।"), B("Rewrite both fractions with that denominator.", "দুয়োটা ভগ্নাংশ সেই হৰত লিখা।")]),
        stepwise(f"{p}.u2.q5", "f-add", lambda a, b, c, d: {"q": B(f"A tank is ${fr(a, b)}$ full. Then ${fr(c, d)}$ of the tank is added. How full is it?", f"টেংকী এটা ${fr(a, b)}$ অংশ ভৰ্তি। পিছত টেংকীৰ ${fr(c, d)}$ অংশ যোগ হ'ল। এতিয়া কিমান ভৰ্তি?"), "parts": [
            part(B("Common denominator?", "উমৈহতীয়া হৰ?"), B(str(lcm(b, d)), str(lcm(b, d))), [B(str(b + d), str(b + d)), B(str(b * d * 2), str(b * d * 2))], B("Use the LCM of the denominators.", "হৰবোৰৰ ল.সা.গু. লোৱা।"), skill="l-lcm", tag="m-add-tops", sid=str(a * d)),
            part(B("Add the tops", "লব যোগ কৰা"), B(f"${fr((F(a, b) + F(c, d)).numerator, (F(a, b) + F(c, d)).denominator)}$", f"${fr((F(a, b) + F(c, d)).numerator, (F(a, b) + F(c, d)).denominator)}$"), [B(f"${fr(a + c, b + d)}$", f"${fr(a + c, b + d)}$"), B(f"${fr(a * c, b * d)}$", f"${fr(a * c, b * d)}$")], B("Rewrite both over the common denominator, then add tops.", "দুয়োটা উমৈহতীয়া হৰত লিখি লব যোগ কৰা।"), tag="m-add-tops", sid=str(a * d)),
        ], "why": B("A weak LCM makes fractions hard, so this problem checks both.", "ল.সা.গু. দুৰ্বল হ'লে ভগ্নাংশ টান হয়, সেয়ে এই সমস্যাই দুয়োটা পৰীক্ষা কৰে।")}, [(1, 4, 1, 6), (1, 3, 2, 9), (1, 2, 3, 10)]),
    ])
    u3 = unit("u3", B("Fractions at work", "কামত ভগ্নাংশ"), "star", [
        B("To find $\\frac{3}{5}$ of 40: divide by 5, then multiply by 3.", "40ৰ $\\frac{3}{5}$ উলিয়াবলৈ 5ৰে হৰণ কৰি 3ৰে পূৰণ কৰা।"),
        B("To multiply fractions, multiply tops and bottoms.", "ভগ্নাংশ পূৰণত লব লবৰ সৈতে, হৰ হৰৰ সৈতে পূৰণ কৰা।"),
        B("Dividing by a fraction is multiplying by its flip.", "ভগ্নাংশেৰে হৰণ মানে ওলোটা ভগ্নাংশেৰে পূৰণ।"),
        B("A repeating digit is that digit over 9: $0.\\overline{4} = \\frac{4}{9}$.", "পুনৰাবৃত্ত অংক মানে অংকটো ভাগ 9: $0.\\overline{4} = \\frac{4}{9}$।"),
    ], [
        story(f"{p}.u3.s1", B("Blocks do the division", "খণ্ডই হৰণ কৰি দিয়ে"), [
            B("Five equal blocks must make 40. Slide until the total fits.", "পাঁচটা সমান খণ্ডই 40 হ'ব লাগে। মুঠ নিমিলা লৈকে টানা।"),
            B("One block is 8, so three blocks, the $\\frac{3}{5}$, are worth 24.", "এটা খণ্ড 8, সেয়ে তিনিটা খণ্ড অৰ্থাৎ $\\frac{3}{5}$ অংশ 24।"),
        ], widget={"kind": "blocks", "parts": [5], "take": 3, "total": 40, "max": 12}),
        story(f"{p}.u3.s2", B("Fractions wearing decimals", "দশমিকত ভগ্নাংশ"), [
            B("$\\frac{1}{4}$ and 0.25 are one number with two names. Learn the common pairs by heart.", "$\\frac{1}{4}$ আৰু 0.25 একেটা সংখ্যা। সাধাৰণ যোৰবোৰ মুখস্থ ৰাখা।"),
            B("Repeating decimals are fractions too: one repeating digit goes over 9, two go over 99.", "পুনৰাবৃত্ত দশমিকো ভগ্নাংশ: এটা অংক 9ৰ ওপৰত, দুটা অংক 99ৰ ওপৰত।"),
        ], diagram={"layout": "grid", "items": [B("$\\frac{1}{2} = 0.5$", "$\\frac{1}{2} = 0.5$"), B("$\\frac{1}{4} = 0.25$", "$\\frac{1}{4} = 0.25$"), B("$\\frac{1}{8} = 0.125$", "$\\frac{1}{8} = 0.125$"), B("$\\frac{1}{3} = 0.\\overline{3}$", "$\\frac{1}{3} = 0.\\overline{3}$")]}),
        explore(f"{p}.u3.q1", "f-of", lambda t, d, a: {"q": B(f"${fr(a, d)}$ of a sum is shaded and the whole is {d * t}. Slide to find one block.", f"মুঠ {d * t}ৰ ${fr(a, d)}$ অংশ ৰঙোৱা। এটা খণ্ডৰ মান টানি উলিওৱা।"), "widget": {"kind": "blocks", "parts": [d], "take": a, "total": d * t, "max": t + 8}, "target": t, "answerText": B(f"One block = {t}, so the shaded part = {t * a}", f"এটা খণ্ড = {t}, ৰঙোৱা অংশ = {t * a}"), "why": B(f"{d * t} ÷ {d} = {t} for one block, and {a} blocks are {t * a}.", f"{d * t} ÷ {d} = {t} এটা খণ্ড, {a}টা খণ্ড {t * a}।")}, [(7, 4, 3), (6, 5, 2), (9, 3, 2), (8, 6, 5)]),
        solve(f"{p}.u3.q2", "f-of", lambda t, d, a, what_en, what_as: {"q": B(f"${fr(a, d)}$ of {d * t} {what_en} is how many?", f"{d * t} {what_as}ৰ ${fr(a, d)}$ অংশ কিমান?"), "answer": str(a * t), "why": B(f"Divide by {d} to get {t}, then multiply by {a}.", f"{d}ৰে হৰণ কৰি {t}, তাৰ পিছত {a}ৰে পূৰণ।"), "traps": [{"ans": str(d * t // a) if d * t % a == 0 else str(t), "tag": "m-frac-of", "why": B("Divide by the bottom number and multiply by the top one, not the other way round.", "তলৰ সংখ্যাৰে হৰণ, ওপৰৰ সংখ্যাৰে পূৰণ; ওলোটাকৈ নহয়।")}]}, [(9, 5, 3, "mangoes", "আম"), (12, 4, 3, "students", "ছাত্ৰ"), (15, 3, 2, "rupees", "টকা"), (11, 6, 5, "metres", "মিটাৰ")]),
        match(f"{p}.u3.q3", "f-dec", B("Match each fraction to its decimal", "প্ৰতিটো ভগ্নাংশক দশমিকৰ সৈতে মিলোৱা"), [
            [B("$\\frac{3}{4}$", "$\\frac{3}{4}$"), B("0.75", "0.75")], [B("$\\frac{2}{5}$", "$\\frac{2}{5}$"), B("0.4", "0.4")], [B("$\\frac{3}{8}$", "$\\frac{3}{8}$"), B("0.375", "0.375")], [B("$\\frac{2}{3}$", "$\\frac{2}{3}$"), B("$0.\\overline{6}$", "$0.\\overline{6}$")],
        ], B("Divide the top by the bottom, or use the pairs you know.", "লবক হৰেৰে হৰণ কৰা, বা জনা যোৰবোৰ ব্যৱহাৰ কৰা।")),
        solve(f"{p}.u3.q4", "f-dec", lambda d, s_, ans, h: {"q": B(f"Write ${s_}$ as a fraction in simplest form.", f"${s_}$ক সৰলতম ভগ্নাংশ হিচাপে লিখা।"), "answer": ans, "why": B(f"{h} Then cancel any common factor.", f"{h} তাৰ পিছত উমৈহতীয়া গুণনীয়ক কাটা।")}, [
            (0, "0.\\overline{7}", "7/9", "One repeating digit goes over 9."), (0, "0.\\overline{36}", "4/11", "Two repeating digits go over 99: 36/99."), (0, "0.\\overline{12}", "4/33", "Two repeating digits go over 99: 12/99."), (0, "0.\\overline{5}", "5/9", "One repeating digit goes over 9."),
        ], hints=[B("One repeating digit: over 9. Two: over 99.", "এটা পুনৰাবৃত্ত অংক: 9ৰ ওপৰত। দুটা: 99ৰ ওপৰত।")]),
        tf(f"{p}.u3.q5", "f-of", B("Dividing by $\\frac{1}{2}$ doubles a number.", "$\\frac{1}{2}$ৰে হৰণ কৰিলে সংখ্যা দুগুণ হয়।"), True, B("It asks how many halves fit in. There are 2 in every whole, so the answer doubles.", "ইয়াৰ অৰ্থ কেইটা আধা সোমাব। প্ৰতিটো গোটাত 2টা, সেয়ে উত্তৰ দুগুণ।")),
        stepwise(f"{p}.u3.q6", "f-of", lambda w, a, d, b, e: {"q": B(f"Mina spends ${fr(a, d)}$ of ₹{w} on food and ${fr(b, e)}$ of what is left on books. How much remains?", f"মিনাই ₹{w}ৰ ${fr(a, d)}$ অংশ খাদ্যত আৰু বাকীৰ ${fr(b, e)}$ অংশ কিতাপত খৰচ কৰে। কিমান বাকী থাকিল?"), "parts": [
            part(B("Left after food?", "খাদ্যৰ পিছত বাকী?"), B(f"₹{w - w * a // d}", f"₹{w - w * a // d}"), [B(f"₹{w * a // d}", f"₹{w * a // d}"), B(f"₹{w - a}", f"₹{w - a}")], B("Take the food share away from the whole sum.", "গোটা ধনৰ পৰা খাদ্যৰ অংশ বাদ দিয়া।"), sid=str(w)),
            part(B("Books cost?", "কিতাপৰ খৰচ?"), B(f"₹{(w - w * a // d) * b // e}", f"₹{(w - w * a // d) * b // e}"), [B(f"₹{w * b // e}", f"₹{w * b // e}"), B(f"₹{(w - w * a // d) // e + 1}", f"₹{(w - w * a // d) // e + 1}")], B("The share is of what is left, not of the first sum.", "অংশটো বাকী ধনৰ, প্ৰথম ধনৰ নহয়।"), tag="m-pct-base", sid=str(w)),
            part(B("So what remains?", "তেনেহ'লে বাকী?"), B(f"₹{(w - w * a // d) - (w - w * a // d) * b // e}", f"₹{(w - w * a // d) - (w - w * a // d) * b // e}"), [B(f"₹{w - w * b // e}", f"₹{w - w * b // e}"), B(f"₹{w * a // d}", f"₹{w * a // d}")], B("Subtract the books from what was left.", "বাকী ধনৰ পৰা কিতাপৰ খৰচ বিয়োগ কৰা।"), sid=str(w)),
        ], "why": B("\"Of what is left\" always changes the base.", "\"বাকীৰ\" বুলি ক'লে ভিত্তি সলনি হয়।")}, [(600, 1, 3, 1, 4), (800, 1, 4, 1, 3), (900, 2, 3, 1, 5)]),
    ])
    test = {"id": "test", "title": B("Fractions test", "ভগ্নাংশৰ পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "f-add", lambda a, b, c, d: {"q": B(f"${fr(a, b)} + {fr(c, d)}$ equals", f"${fr(a, b)} + {fr(c, d)}$ৰ মান"), "right": F(a, b) + F(c, d), "wrong": [(F(a + c, b + d), "m-add-tops", tops)], "fill": [F(a * c, b * d), F(a, b) + F(c, d) + F(1, b * d), F(a + c, b * d)], "why": B("Make the denominators equal first.", "প্ৰথমে হৰ সমান কৰা।")}, [(2, 3, 1, 4), (3, 5, 1, 4), (5, 6, 1, 9)]),
        mcq(f"{p}.t.q2", "f-compare", lambda x, y, z, w: {"q": B("Which is the largest?", "কোনটো আটাইতকৈ ডাঙৰ?"), "right": max(x, y, z, w), "wrong": [(min(x, y, z, w), "m-cmp-denom", B("A bigger denominator does not make a bigger fraction. Cross-multiply to compare.", "ডাঙৰ হৰে ভগ্নাংশ ডাঙৰ নকৰে। তিৰ্যক পূৰণ কৰি তুলনা কৰা।"))], "fill": sorted([x, y, z, w]), "why": B("Compare by cross-multiplying, or turn each into a decimal.", "তিৰ্যক পূৰণ কৰি বা দশমিক কৰি তুলনা কৰা।")}, [(F(3, 4), F(5, 7), F(2, 3), F(4, 9)), (F(5, 6), F(7, 9), F(3, 5), F(2, 3)), (F(4, 5), F(5, 8), F(3, 4), F(2, 7))]),
        mcq(f"{p}.t.q3", "f-of", lambda t, d, a: {"q": B(f"${fr(a, d)}$ of a number is {t * a}. The number is", f"এটা সংখ্যাৰ ${fr(a, d)}$ অংশ {t * a}। সংখ্যাটো হ'ল"), "right": t * d, "wrong": [(F(t * a * a, d), "m-frac-of", B("The fraction of the number is given, so divide by the fraction rather than multiplying.", "সংখ্যাৰ অংশ দিয়া আছে, সেয়ে ভগ্নাংশেৰে হৰণ কৰা, পূৰণ নকৰিবা।"))], "fill": [t * d + t, t * a, t * d - t, t * d * 2], "why": B(f"One part is {t}, and the whole is {d} parts.", f"এটা ভাগ {t}, গোটা {d} ভাগ।")}, [(8, 5, 3), (6, 7, 4), (9, 4, 3)]),
        mcq(f"{p}.t.q4", "f-dec", lambda s_, right, w1, w2, w3: {"q": B(f"${s_}$ is equal to", f"${s_}$ৰ মান"), "right": right, "wrong": [], "fill": [w1, w2, w3], "why": B("Repeating digits go over 9s, one 9 for each digit.", "পুনৰাবৃত্ত অংক 9ৰ ওপৰত, প্ৰতিটো অংকৰ বাবে এটা 9।")}, [("0.\\overline{8}", F(8, 9), F(4, 5), F(22, 25), F(7, 9)), ("0.\\overline{27}", F(3, 11), F(27, 100), F(2, 7), F(1, 4)), ("0.\\overline{45}", F(5, 11), F(9, 20), F(4, 9), F(1, 2))]),
        solve(f"{p}.t.q5", "f-equiv", lambda a, b, ans: {"q": B(f"Simplify ${fr(a, b)}$.", f"${fr(a, b)}$ সৰল কৰা।"), "answer": ans, "exact": True, "why": B("Divide top and bottom by their HCF.", "লব আৰু হৰক গ.সা.গু.ৰে হৰণ কৰা।")}, [(45, 75, "3/5"), (56, 84, "2/3"), (72, 96, "3/4")]),
    ]}
    return {"id": "math-03-fractions", "no": 3, "tier": "A", "face": "fractions", "title": B("Fractions you can see", "দেখিব পৰা ভগ্নাংশ"), "reign": B("Meaning, adding, decimals", "অৰ্থ, যোগ, দশমিক"), "units": [u1, u2, u3], "test": test}


# ---------------------------------------------------------------- Lesson 5
def l5():
    p = "m5"
    base = B("You used the new value as the base. A percentage change is always out of the original value.", "তুমি নতুন মানক ভিত্তি ধৰিলা। শতাংশ পৰিৱৰ্তন সদায় মূল মানৰ ওপৰত।")
    addup = B("You added the two percentages. The second change acts on the new value, so use $a + b + \\frac{ab}{100}$.", "তুমি দুটা শতাংশ যোগ কৰিলা। দ্বিতীয় পৰিৱৰ্তন নতুন মানৰ ওপৰত হয়, সেয়ে $a + b + \\frac{ab}{100}$ ব্যৱহাৰ কৰা।")
    u1 = unit("u1", B("Out of a hundred", "এশৰ ভিতৰত"), "star", [
        B("Percent means out of 100: 37% is $\\frac{37}{100}$ or 0.37.", "শতাংশ মানে এশৰ ভিতৰত: 37% মানে $\\frac{37}{100}$ বা 0.37।"),
        B("Build any percentage from 10% and 1%.", "10% আৰু 1%ৰ পৰা যিকোনো শতাংশ গঢ়িব পাৰি।"),
        B("x% of y equals y% of x, so choose the easier one.", "yৰ x% আৰু xৰ y% সমান, সেয়ে সহজটো লোৱা।"),
        B("Know the pairs: 25% is $\\frac{1}{4}$, 12.5% is $\\frac{1}{8}$, 20% is $\\frac{1}{5}$.", "যোৰবোৰ জানা: 25% = $\\frac{1}{4}$, 12.5% = $\\frac{1}{8}$, 20% = $\\frac{1}{5}$।"),
    ], [
        story(f"{p}.u1.s1", B("A hundred squares", "এশটা বৰ্গ"), [
            B("Drag across the grid. Every square is 1%, so the whole grid is 100%.", "জালখনত টানা। প্ৰতিটো বৰ্গ 1%, গোটা জাল 100%।"),
            B("One picture gives three names: 25%, $\\frac{1}{4}$ and 0.25.", "এখন ছবিৰ তিনিটা নাম: 25%, $\\frac{1}{4}$ আৰু 0.25।"),
        ], widget={"kind": "grid100", "shade": 25}),
        story(f"{p}.u1.s2", B("The 10% trick", "10%ৰ কৌশল"), [
            B("To find 10%, move the decimal point one place left. 1% moves it two places.", "10%ৰ বাবে দশমিক এঘৰ বাওঁলৈ নিয়া। 1%ৰ বাবে দুঘৰ।"),
            B("Then any percentage is a mental sum, such as 35% = 30% + 5%.", "তেতিয়া যিকোনো শতাংশ মনতে হয়, যেনে 35% = 30% + 5%।"),
        ], diagram={"layout": "flow", "items": [B("10% of 240 = 24", "240ৰ 10% = 24"), B("5% = half of that = 12", "5% = তাৰ আধা = 12"), B("15% = 24 + 12 = 36", "15% = 24 + 12 = 36")]}),
        explore(f"{p}.u1.q1", "p-meaning", lambda k, of: {"q": B(f"Shade {k}% of the grid.", f"জালখনৰ {k}% ৰঙোৱা।"), "widget": {"kind": "grid100", "of": of}, "target": k, "answerText": B(f"{k} squares", f"{k}টা বৰ্গ"), "why": B(f"{k}% is {k} squares out of 100.", f"{k}% মানে 100ৰ {k}টা বৰ্গ।")}, [(35, 200), (60, 50), (72, 300), (15, 400)]),
        match(f"{p}.u1.q2", "p-meaning", B("Match each percentage to its fraction", "প্ৰতিটো শতাংশক ভগ্নাংশৰ সৈতে মিলোৱা"), [
            [B("25%", "25%"), B("$\\frac{1}{4}$", "$\\frac{1}{4}$")], [B("12.5%", "12.5%"), B("$\\frac{1}{8}$", "$\\frac{1}{8}$")], [B("20%", "20%"), B("$\\frac{1}{5}$", "$\\frac{1}{5}$")], [B("$33\\frac{1}{3}$%", "$33\\frac{1}{3}$%"), B("$\\frac{1}{3}$", "$\\frac{1}{3}$")],
        ], B("Keep these four: they turn many exam questions into one division.", "এই চাৰিটা মনত ৰাখা: বহু প্ৰশ্ন এটা হৰণতে শেষ হয়।")),
        solve(f"{p}.u1.q3", "p-of", lambda k, n: {"q": B(f"Find {k}% of {n}.", f"{n}ৰ {k}% উলিওৱা।"), "answer": num(F(k * n, 100)), "why": B(f"10% of {n} is {num(F(n, 10))}; build {k}% from that to get {num(F(k * n, 100))}.", f"{n}ৰ 10% হ'ল {num(F(n, 10))}; ইয়াৰ পৰা {k}% গঢ়িলে {num(F(k * n, 100))} হয়।")}, [(15, 240), (35, 600), (45, 80), (12, 250)], hints=[B("Find 10% first by moving the decimal point.", "প্ৰথমে দশমিক সৰাই 10% উলিওৱা।")]),
        tf(f"{p}.u1.q4", "p-of", B("8% of 25 is the same as 25% of 8.", "25ৰ 8% আৰু 8ৰ 25% একে।"), True, B("Both are $\\frac{8 \\times 25}{100} = 2$, and 25% of 8 is easy: a quarter of 8.", "দুয়োটা $\\frac{8 \\times 25}{100} = 2$; 8ৰ 25% সহজ: 8ৰ এক-চতুৰ্থাংশ।")),
        solve(f"{p}.u1.q5", "p-of", lambda a, b: {"q": B(f"What percentage is {a} of {b}?", f"{b}ৰ কিমান শতাংশ {a}?"), "answer": num(F(a * 100, b)), "suffix": B("%", "%"), "why": B(f"${fr(a, b)} \\times 100 = {num(F(a * 100, b))}$.", f"${fr(a, b)} \\times 100 = {num(F(a * 100, b))}$।"), "traps": [{"ans": num(F(b * 100, a)), "tag": "m-pct-base", "why": B("You divided the wrong way. The number after \"of\" is the base.", "তুমি ওলোটাকৈ হৰণ কৰিলা। যাৰ শতাংশ উলিয়াব লাগে সেয়াই ভিত্তি।")}]}, [(18, 72), (30, 120), (14, 35), (9, 45)]),
    ])
    u2 = unit("u2", B("Rise and fall", "বৃদ্ধি আৰু হ্ৰাস"), "star", [
        B("Percent change = change ÷ original × 100.", "শতাংশ পৰিৱৰ্তন = পৰিৱৰ্তন ÷ মূল মান × 100।"),
        B("A 20% rise multiplies by 1.2; a 20% fall multiplies by 0.8.", "20% বৃদ্ধিত 1.2ৰে পূৰণ; 20% হ্ৰাসত 0.8ৰে পূৰণ।"),
        B("To undo a change, divide by the multiplier.", "পৰিৱৰ্তন ওভতাবলৈ গুণকেৰে হৰণ কৰা।"),
        B("The same percent up and then down does not return you to the start.", "একে শতাংশ বাঢ়ি কমিলে আগৰ ঠাইলৈ উভতি নাহে।"),
    ], [
        story(f"{p}.u2.s1", B("Always ask: out of what?", "সদায় সোধা: কিহৰ ওপৰত?"), [
            B("A price goes from ₹50 to ₹60. The rise is ₹10, measured against the old ₹50.", "দাম ₹50ৰ পৰা ₹60 হ'ল। বৃদ্ধি ₹10, পুৰণি ₹50ৰ ওপৰত।"),
            B("So it rose 20%, not $16\\frac{2}{3}$%. The original is the base every time.", "সেয়ে বৃদ্ধি 20%, $16\\frac{2}{3}$% নহয়। সদায় মূল মানেই ভিত্তি।"),
        ], diagram={"layout": "flow", "items": [B("Change: ₹10", "পৰিৱৰ্তন: ₹10"), B("Original: ₹50", "মূল: ₹50"), B("$\\frac{10}{50} \\times 100 = 20$%", "$\\frac{10}{50} \\times 100 = 20$%")]}),
        story(f"{p}.u2.s2", B("Multipliers save time", "গুণকে সময় বচায়"), [
            B("A rise of r% means multiply by $1 + \\frac{r}{100}$. A fall means multiply by $1 - \\frac{r}{100}$.", "r% বৃদ্ধি মানে $1 + \\frac{r}{100}$ৰে পূৰণ। হ্ৰাস মানে $1 - \\frac{r}{100}$ৰে পূৰণ।"),
            B("One multiplication replaces two steps, and undoing it is one division.", "এটা পূৰণে দুটা খোজৰ কাম কৰে, ওভতাবলৈ এটা হৰণ।"),
        ], diagram={"layout": "grid", "items": [B("+25%: × 1.25", "+25%: × 1.25"), B("−25%: × 0.75", "−25%: × 0.75"), B("+8%: × 1.08", "+8%: × 1.08"), B("−8%: × 0.92", "−8%: × 0.92")]}),
        solve(f"{p}.u2.q1", "p-change", lambda o, n: {"q": B(f"A value goes from {o} to {n}. What is the percentage change?", f"এটা মান {o}ৰ পৰা {n} হ'ল। শতাংশ পৰিৱৰ্তন কিমান?"), "answer": num(F(abs(n - o) * 100, o)), "suffix": B("%", "%"), "why": B(f"Change {abs(n - o)}, original {o}: ${fr(abs(n - o), o)} \\times 100 = {num(F(abs(n - o) * 100, o))}$.", f"পৰিৱৰ্তন {abs(n - o)}, মূল {o}: ${fr(abs(n - o), o)} \\times 100 = {num(F(abs(n - o) * 100, o))}$।"), "traps": [{"ans": num(F(abs(n - o) * 100, n)), "tag": "m-pct-base", "why": base}]}, [(50, 60), (80, 100), (40, 30), (120, 150)], hints=[B("Divide the change by the original value.", "পৰিৱৰ্তনক মূল মানেৰে হৰণ কৰা।")]),
        match(f"{p}.u2.q2", "p-change", B("Match each change to its multiplier", "প্ৰতিটো পৰিৱৰ্তনক গুণকৰ সৈতে মিলোৱা"), [
            [B("12% rise", "12% বৃদ্ধি"), B("1.12", "1.12")], [B("12% fall", "12% হ্ৰাস"), B("0.88", "0.88")], [B("30% rise", "30% বৃদ্ধি"), B("1.3", "1.3")], [B("30% fall", "30% হ্ৰাস"), B("0.7", "0.7")],
        ], B("Rise: add to 1. Fall: subtract from 1.", "বৃদ্ধি: 1ৰ লগত যোগ। হ্ৰাস: 1ৰ পৰা বিয়োগ।")),
        solve(f"{p}.u2.q3", "p-change", lambda o, r: {"q": B(f"After a {r}% rise a price is ₹{o * (100 + r) // 100}. What was it before?", f"{r}% বৃদ্ধিৰ পিছত দাম ₹{o * (100 + r) // 100}। আগতে কিমান আছিল?"), "answer": str(o), "prefix": B("₹", "₹"), "why": B(f"Divide by the multiplier {num(F(100 + r, 100))} rather than subtracting {r}%.", f"{r}% বিয়োগ নকৰি গুণক {num(F(100 + r, 100))}ৰে হৰণ কৰা।"), "traps": [{"ans": num(F(o * (100 + r) * (100 - r), 10000)), "tag": "m-pct-base", "why": base}]}, [(200, 20), (400, 25), (500, 10), (800, 15)], hints=[B("New = old × multiplier, so old = new ÷ multiplier.", "নতুন = পুৰণি × গুণক, সেয়ে পুৰণি = নতুন ÷ গুণক।")]),
        tf(f"{p}.u2.q4", "p-change", B("If a price rises 20% and then falls 20%, it returns to the original.", "দাম 20% বাঢ়ি পিছত 20% কমিলে আগৰ দামলৈ উভতি আহে।"), False, B("₹100 becomes ₹120, then falls by ₹24 to ₹96. The fall acts on a bigger base.", "₹100 ₹120 হয়, তাৰ পিছত ₹24 কমি ₹96। হ্ৰাসটো ডাঙৰ ভিত্তিৰ ওপৰত।"), ("m-pct-undo", B("The fall is 20% of the raised price, so it removes more than the rise added.", "হ্ৰাসটো বৰ্ধিত দামৰ 20%, সেয়ে বৃদ্ধিতকৈ বেছি কমে।"))),
        stepwise(f"{p}.u2.q5", "p-change", lambda s_, r: {"q": B(f"A salary of ₹{s_} rises by {r}%. What is the new salary, by multiplier?", f"₹{s_} দৰমহা {r}% বাঢ়িল। গুণকেৰে নতুন দৰমহা কিমান?"), "parts": [
            part(B("Which multiplier?", "কোনটো গুণক?"), B(str((100 + r) / 100), str((100 + r) / 100)), [B(str((100 - r) / 100), str((100 - r) / 100)), B(str(r / 100), str(r / 100))], B("A rise adds to 1.", "বৃদ্ধি 1ৰ লগত যোগ হয়।"), sid=str(s_)),
            part(B("New salary?", "নতুন দৰমহা?"), B(f"₹{s_ * (100 + r) // 100}", f"₹{s_ * (100 + r) // 100}"), [B(f"₹{s_ + r}", f"₹{s_ + r}"), B(f"₹{s_ * (100 - r) // 100}", f"₹{s_ * (100 - r) // 100}")], B("Multiply the salary by the multiplier.", "দৰমহাক গুণকেৰে পূৰণ কৰা।"), sid=str(s_)),
        ], "why": B("One multiplication does the whole job.", "এটা পূৰণতে সকলো কাম হয়।")}, [(20000, 15), (15000, 20), (24000, 25)]),
    ])
    u3 = unit("u3", B("Changes on changes", "পৰিৱৰ্তনৰ ওপৰত পৰিৱৰ্তন"), "star", [
        B("Two changes in a row: $a + b + \\frac{ab}{100}$, with falls written as negative.", "পৰ পৰ দুটা পৰিৱৰ্তন: $a + b + \\frac{ab}{100}$; হ্ৰাসক ঋণাত্মক লিখা।"),
        B("Multiplying both sides of a rectangle by rises uses the same formula.", "আয়তৰ দুয়োটা বাহু বাঢ়িলেও একে সূত্ৰ।"),
        B("If a price rises r%, cut use by $\\frac{r}{100 + r} \\times 100$% to keep spending level.", "দাম r% বাঢ়িলে খৰচ একে ৰাখিবলৈ ব্যৱহাৰ $\\frac{r}{100 + r} \\times 100$% কমোৱা।"),
        B("If A is r% more than B, then B is $\\frac{r}{100 + r} \\times 100$% less than A.", "A Bতকৈ r% বেছি হ'লে B Aতকৈ $\\frac{r}{100 + r} \\times 100$% কম।"),
    ], [
        story(f"{p}.u3.s1", B("Second change, new number", "দ্বিতীয় পৰিৱৰ্তন, নতুন সংখ্যা"), [
            B("Raise 100 by 10%, then by 10% again. You get 121, not 120.", "100ক 10% বঢ়োৱা, আকৌ 10% বঢ়োৱা। 121 হয়, 120 নহয়।"),
            B("The extra 1 is the percentage of a percentage: $\\frac{10 \\times 10}{100}$.", "অতিৰিক্ত 1টো শতাংশৰ শতাংশ: $\\frac{10 \\times 10}{100}$।"),
        ], diagram={"layout": "flow", "items": [B("$a + b$", "$a + b$"), B("$+\\frac{ab}{100}$", "$+\\frac{ab}{100}$"), B("$10 + 10 + 1 = 21$%", "$10 + 10 + 1 = 21$%")]}),
        story(f"{p}.u3.s2", B("More than is not less than", "বেছি আৰু কম একে নহয়"), [
            B("If A is 25% more than B, take B as 100 and A as 125.", "A Bতকৈ 25% বেছি হ'লে B = 100, A = 125 ধৰা।"),
            B("B is 25 below A, but A is the base now: $\\frac{25}{125} = 20$%.", "B Aতকৈ 25 কম, কিন্তু এতিয়া A ভিত্তি: $\\frac{25}{125} = 20$%।"),
        ], diagram={"layout": "flow", "items": [B("B = 100", "B = 100"), B("A = 125", "A = 125"), B("B is 20% less than A", "B Aতকৈ 20% কম")]}),
        solve(f"{p}.u3.q1", "p-succ", lambda a, b: {"q": B(f"A number rises {a}% and then {b}%. What is the total rise?", f"এটা সংখ্যা {a}% বাঢ়ি তাৰ পিছত {b}% বাঢ়িল। মুঠ বৃদ্ধি কিমান?"), "answer": num(F(a + b) + F(a * b, 100)), "suffix": B("%", "%"), "why": B(f"${a} + {b} + {fr(f'{a} \\times {b}', 100)} = {num(F(a + b) + F(a * b, 100))}$.", f"${a} + {b} + {fr(f'{a} \\times {b}', 100)} = {num(F(a + b) + F(a * b, 100))}$।"), "traps": [{"ans": str(a + b), "tag": "m-pct-add", "why": addup}]}, [(10, 20), (20, 30), (25, 20), (10, 50)], hints=[B("Use $a + b + \\frac{ab}{100}$.", "$a + b + \\frac{ab}{100}$ ব্যৱহাৰ কৰা।")]),
        solve(f"{p}.u3.q2", "p-succ", lambda a, b: {"q": B(f"A number rises {a}% and then falls {b}%. By what percentage does it finally rise?", f"এটা সংখ্যা {a}% বাঢ়ি তাৰ পিছত {b}% কমিল। শেষত কিমান শতাংশ বাঢ়িল?"), "answer": num(F(a - b) - F(a * b, 100)), "suffix": B("%", "%"), "why": B(f"Falls are negative: ${a} - {b} - {fr(f'{a} \\times {b}', 100)} = {num(F(a - b) - F(a * b, 100))}$.", f"হ্ৰাস ঋণাত্মক: ${a} - {b} - {fr(f'{a} \\times {b}', 100)} = {num(F(a - b) - F(a * b, 100))}$।"), "traps": [{"ans": str(a - b), "tag": "m-pct-add", "why": addup}]}, [(25, 10), (50, 20), (40, 25), (30, 10)]),
        tf(f"{p}.u3.q3", "p-compare", B("If A is 50% more than B, then B is 50% less than A.", "A Bতকৈ 50% বেছি হ'লে B Aতকৈ 50% কম।"), False, B("Take B = 100, so A = 150. B is 50 below 150, which is $33\\frac{1}{3}$%.", "B = 100 ধৰিলে A = 150। B 150তকৈ 50 কম, অৰ্থাৎ $33\\frac{1}{3}$%।"), ("m-pct-more-less", B("The base changes from B to A, so the percentage changes too.", "ভিত্তি Bৰ পৰা Aলৈ সলনি হয়, সেয়ে শতাংশও সলনি হয়।"))),
        stepwise(f"{p}.u3.q4", "p-compare", lambda r: {"q": B(f"A is {r}% more than B. By what percentage is B less than A?", f"A Bতকৈ {r}% বেছি। B Aতকৈ কিমান শতাংশ কম?"), "parts": [
            part(B("Take B = 100. Then A =", "B = 100 ধৰা। তেনেহ'লে A ="), B(str(100 + r), str(100 + r)), [B(str(100 - r), str(100 - r)), B(str(r), str(r))], B(f"A is {r} more than 100.", f"A 100তকৈ {r} বেছি।"), sid=str(r)),
            part(B("Difference?", "পাৰ্থক্য?"), B(str(r), str(r)), [B(str(100 + r), str(100 + r)), B(str(2 * r), str(2 * r))], B("Subtract B from A.", "Aৰ পৰা B বিয়োগ কৰা।"), sid=str(r)),
            part(B("Base for \"less than A\"?", "\"Aতকৈ কম\"ৰ ভিত্তি?"), B(f"A: {100 + r}", f"A: {100 + r}"), [B("B: 100", "B: 100")], B("The comparison is against A.", "তুলনা Aৰ সৈতে।"), tag="m-pct-more-less", sid=str(r)),
            part(B("So B is less by", "তেনেহ'লে B কম"), B(show(F(r * 100, 100 + r), "%"), show(F(r * 100, 100 + r), "%")), [B(f"{r}%", f"{r}%"), B(f"{r + 5}%", f"{r + 5}%")], B(f"${fr(r, 100 + r)} \\times 100$.", f"${fr(r, 100 + r)} \\times 100$।"), tag="m-pct-more-less", sid=str(r)),
        ], "why": B("Choosing 100 for the base makes these questions simple.", "ভিত্তি 100 ধৰিলে এই প্ৰশ্নবোৰ সহজ হয়।")}, [(25,), (60,), (20,)]),
        solve(f"{p}.u3.q5", "p-compare", lambda r, a: {"q": B(f"The price of oil rises {r}%. By what percentage must a family cut use to keep spending the same?", f"তেলৰ দাম {r}% বাঢ়িল। খৰচ একে ৰাখিবলৈ পৰিয়াল এটাই ব্যৱহাৰ কিমান শতাংশ কমাব লাগিব?"), "answer": a, "suffix": B("%", "%"), "why": B(f"${fr(r, 100 + r)} \\times 100 = {a}$.", f"${fr(r, 100 + r)} \\times 100 = {a}$।"), "traps": [{"ans": str(r), "tag": "m-pct-more-less", "why": B("Cutting by the same percent is too much, because the cut is measured on the higher price.", "একে শতাংশ কমালে বেছি হয়, কাৰণ হ্ৰাস বৰ্ধিত দামৰ ওপৰত জোখা হয়।")}]}, [(25, "20"), (100, "50"), (60, "37.5"), (50, "100/3")], hints=[B("Use $\\frac{r}{100 + r} \\times 100$.", "$\\frac{r}{100 + r} \\times 100$ ব্যৱহাৰ কৰা।")]),
        match(f"{p}.u3.q6", "p-succ", B("Match the pair of changes to the total", "দুটা পৰিৱৰ্তনক মুঠৰ সৈতে মিলোৱা"), [
            [B("+10% then +10%", "+10% তাৰ পিছত +10%"), B("+21%", "+21%")], [B("+20% then −20%", "+20% তাৰ পিছত −20%"), B("−4%", "−4%")], [B("−10% then −10%", "−10% তাৰ পিছত −10%"), B("−19%", "−19%")], [B("+50% then −50%", "+50% তাৰ পিছত −50%"), B("−25%", "−25%")],
        ], B("Use $a + b + \\frac{ab}{100}$ with falls as negative.", "হ্ৰাস ঋণাত্মক লৈ $a + b + \\frac{ab}{100}$ ব্যৱহাৰ কৰা।")),
    ])
    test = {"id": "test", "title": B("Percentage test", "শতাংশৰ পৰীক্ষা"), "learned": [], "steps": [
        mcq(f"{p}.t.q1", "p-change", lambda o, n: {"q": B(f"A price rises from ₹{o} to ₹{n}. The percentage rise is", f"দাম ₹{o}ৰ পৰা ₹{n} হ'ল। শতাংশ বৃদ্ধি হ'ল"), "right": F((n - o) * 100, o), "wrong": [(F((n - o) * 100, n), "m-pct-base", base)], "fill": [n - o, F((n - o) * 100, o) + 5, F((n - o) * 100, o) + 10], "unit": "%", "why": B("Change divided by the original, times 100.", "পৰিৱৰ্তন ভাগ মূল মান, পূৰণ 100।")}, [(40, 50), (60, 75), (80, 92)]),
        mcq(f"{p}.t.q2", "p-succ", lambda a, b: {"q": B(f"Two discounts of {a}% and {b}% equal a single discount of", f"{a}% আৰু {b}% দুটা ৰেহাই একক কিমান ৰেহাইৰ সমান?"), "right": F(a + b) - F(a * b, 100), "wrong": [(a + b, "m-pct-add", addup)], "fill": [F(a + b) + F(a * b, 100), a + b - 1, a + b - 2, a + b - 3], "unit": "%", "why": B("Use $a + b - \\frac{ab}{100}$ for two falls.", "দুটা হ্ৰাসৰ বাবে $a + b - \\frac{ab}{100}$।")}, [(10, 20), (20, 25), (10, 30)]),
        mcq(f"{p}.t.q3", "p-compare", lambda r: {"q": B(f"If A's income is {r}% more than B's, B's income is less than A's by", f"Aৰ আয় Bতকৈ {r}% বেছি হ'লে Bৰ আয় Aতকৈ কম"), "right": F(r * 100, 100 + r), "wrong": [(r, "m-pct-more-less", B("The base switches to A, so the percentage is smaller.", "ভিত্তি Aলৈ সলনি হয়, সেয়ে শতাংশ সৰু হয়।"))], "fill": [F(r * 100, 100 + r) + 5, r + 5, r - 2], "unit": "%", "why": B("Take B as 100 and compare with A.", "B = 100 ধৰি Aৰ সৈতে তুলনা কৰা।")}, [(25,), (100,), (60,)]),
        mcq(f"{p}.t.q4", "p-of", lambda k, n: {"q": B(f"{k}% of a number is {k * n // 100}. The number is", f"এটা সংখ্যাৰ {k}% হ'ল {k * n // 100}। সংখ্যাটো হ'ল"), "right": n, "wrong": [(F((k * n // 100) * k, 100), "m-pct-base", B("You took a percentage of the part. Here the part is given, so divide up to 100%.", "তুমি অংশটোৰে শতাংশ ল'লা। অংশটো দিয়া আছে, সেয়ে 100%লৈ হৰণ কৰা।"))], "fill": [n + 20, n - 20, n * 2], "why": B(f"1% is the part ÷ {k}; 100% is that times 100.", f"1% = অংশ ÷ {k}; 100% = তাৰ 100 গুণ।")}, [(30, 240), (15, 300), (40, 150)]),
        solve(f"{p}.t.q5", "p-change", lambda o, r: {"q": B(f"After a {r}% fall a value is {o * (100 - r) // 100}. What was the original?", f"{r}% হ্ৰাসৰ পিছত মান {o * (100 - r) // 100}। মূল মান কিমান আছিল?"), "answer": str(o), "why": B(f"Divide by {num(F(100 - r, 100))}.", f"{num(F(100 - r, 100))}ৰে হৰণ কৰা।")}, [(500, 20), (800, 25), (600, 10)]),
    ]}
    return {"id": "math-05-percentage", "no": 5, "tier": "A", "face": "percentage", "title": B("Percentage", "শতাংশ"), "reign": B("Out of 100, change, successive change", "এশৰ ভিতৰত, পৰিৱৰ্তন, ক্ৰমিক পৰিৱৰ্তন"), "units": [u1, u2, u3], "test": test}
