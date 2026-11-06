"""Do-to-discover cards for the Mathematics course, and the number-line unit.

LABS replaces a story card's picture with a playable scene: each task has something to do,
a goal the scene must reach, and the insight that follows. Step ids do not change.
docs/MATHEMATICS-VISUALS.md explains why each scene shows its concept this way.
"""
from math_kit import B, explore, fr, order, solve, story, tf, unit


def task(do, goal, then):
    return {"do": do, "goal": goal, "then": then}


LABS = {
    "m1.u1.s2": (B("A factor is a rectangle", "গুণনীয়ক মানে এটা আয়ত"), B("Line up 24 dots in equal rows. When they make a clean rectangle, you have found a factor.", "24টা বিন্দু সমান শাৰীত সজোৱা। পৰিষ্কাৰ আয়ত হ'লে এটা গুণনীয়ক পালা।"), {"kind": "array", "n": 24, "max": 12, "c": 2}, [
        task(B("Slide to 6 dots in each row.", "প্ৰতি শাৰীত 6টা বিন্দু কৰা।"), {"c": 6}, B("24 = 6 × 4. A clean rectangle means 6 and 4 are factors.", "24 = 6 × 4। পৰিষ্কাৰ আয়ত মানে 6 আৰু 4 গুণনীয়ক।")),
        task(B("Find a row length that leaves dots over.", "বিন্দু বাকী থকা এটা শাৰী বিচাৰা।"), {"broke": 1}, B("Red dots are the remainder. That number is not a factor.", "ৰঙা বিন্দুবোৰ ভাগশেষ। সেই সংখ্যাটো গুণনীয়ক নহয়।")),
    ]),
    "m1.u3.s1": (B("Last digits walk in a circle", "শেষৰ অংক বৃত্তত ঘূৰে"), B("Mark the last digit of each power of 3 on a dial of ten digits.", "3ৰ প্ৰতিটো ঘাতৰ শেষৰ অংক দহ অংকৰ ডায়েলত চিহ্নিত কৰা।"), {"kind": "dial", "b": 3}, [
        task(B("Tap Next power until a digit comes back.", "কোনো অংক উভতি নহালৈ 'পিছৰ ঘাত' টিপা।"), {"closed": 1}, B("3, 9, 7, 1, then 3 again. The path closes after 4 steps, so the pattern repeats every 4.", "3, 9, 7, 1, তাৰ পিছত আকৌ 3। 4 খোজত পথ বন্ধ হয়, সেয়ে প্ৰতি 4 ঘাতত আৰ্হি ঘূৰে।")),
    ]),
    "m2.u1.s1": (B("The largest square tile", "সৰ্ববৃহৎ বৰ্গ টাইল"), B("Fill an 18 by 12 floor with squares. The side of the last square is the HCF.", "18 বাই 12 মজিয়া বৰ্গেৰে ভৰোৱা। শেষৰ বৰ্গৰ বাহুৱেই গ.সা.গু.।"), {"kind": "tiles", "a": 18, "b": 12}, [
        task(B("Keep cutting the biggest square.", "সৰ্ববৃহৎ বৰ্গটো কাটি থাকা।"), {"done": 1}, B("Squares of side 6 fit both 18 and 12 exactly, and nothing larger does. So the HCF is 6.", "6 বাহুৰ বৰ্গ 18 আৰু 12 দুয়োটাত ঠিক মিলে, ইয়াতকৈ ডাঙৰটো নিমিলে। সেয়ে গ.সা.গু. 6।")),
    ]),
    "m2.u2.s1": (B("When two rhythms meet", "দুটা ছন্দ ক'ত লগ হয়"), B("These gears have 4 and 6 teeth. Each red mark starts at home.", "এই গিয়াৰ দুটাৰ 4 আৰু 6টা দাঁত। প্ৰতিটো ৰঙা চিন আৰম্ভণিৰ ঠাইত।"), {"kind": "gears", "a": 4, "b": 6}, [
        task(B("Turn until both marks are home together.", "দুয়োটা চিন একেলগে ঘৰলৈ নহালৈ ঘূৰোৱা।"), {"meet": 1}, B("12 teeth: 3 turns of one gear, 2 of the other. 12 is the Lowest Common Multiple.", "12টা দাঁত: এটাৰ 3 পাক, আনটোৰ 2 পাক। 12 লঘিষ্ঠ সাধাৰণ গুণিতক।")),
        task(B("Keep turning to the next meeting.", "পিছৰ মিলনলৈ ঘূৰাই থাকা।"), {"meets": {"gt": 1}}, B("They meet again at 24. Every common multiple is a multiple of the LCM.", "আকৌ 24ত মিলে। প্ৰতিটো উমৈহতীয়া গুণিতক ল.সা.গু.ৰ গুণিতক।")),
    ]),
    "m3.u1.s1": (B("Cut, then count", "কাটা, তাৰ পিছত গণা"), B("A fraction is two instructions: cut into equal parts, then take some.", "ভগ্নাংশ দুটা নিৰ্দেশ: সমান ভাগত কাটা, তাৰ পিছত কিছু লোৱা।"), {"kind": "fracbar", "n": 4, "split": True}, [
        task(B("Shade three quarters of the bar.", "বাৰৰ তিনি-চতুৰ্থাংশ ৰঙোৱা।"), {"value": 0.75}, B("Three of four equal parts. Now try + and see that 6 of 8 is the same amount.", "চাৰিটা সমান ভাগৰ তিনিটা। এতিয়া + টিপি চোৱা 8ৰ 6 একে পৰিমাণ।")),
    ]),
    "m3.u2.s1": (B("Fractions live on the line", "ভগ্নাংশ ৰেখাত থাকে"), B("Here is the piece from 0 to 1, cut into eighths. Every fraction is a place.", "0ৰ পৰা 1লৈ অংশটো অষ্টমাংশত কটা। প্ৰতিটো ভগ্নাংশ এটা স্থান।"), {"kind": "line", "min": 0, "max": 1, "den": 8, "value": 0.25, "percent": True}, [
        task(B("Drag the pin to $\\frac{5}{8}$.", "পিনটো $\\frac{5}{8}$লৈ টানা।"), {"value": 0.625}, B("Five steps of one eighth. The same point is 0.625.", "এক-অষ্টমাংশৰ পাঁচ খোজ। একে বিন্দুটো 0.625।")),
        task(B("Now find $\\frac{1}{2}$.", "এতিয়া $\\frac{1}{2}$ বিচাৰা।"), {"value": 0.5}, B("It is also $\\frac{4}{8}$. Equal fractions are one point with many names.", "ইয়াৰ নাম $\\frac{4}{8}$ও। সমান ভগ্নাংশ মানে এটা বিন্দুৰ বহু নাম।")),
    ]),
    "m3.u2.s2": (B("Same-size pieces first", "প্ৰথমে একে আকাৰৰ টুকুৰা"), B("Blue marks cut thirds and green marks cut quarters. They need cuts they can share.", "নীলা চিনে তৃতীয়াংশ, সেউজীয়া চিনে চতুৰ্থাংশ কাটে। উমৈহতীয়া কাট লাগিব।"), {"kind": "cuts", "a": [1, 3], "b": [1, 4], "d": 5}, [
        task(B("Change the cuts until every mark lands on one.", "প্ৰতিটো চিন কাটত নপৰালৈ সলনি কৰা।"), {"common": 1}, B("12 cuts fit both, because 12 is the LCM of 3 and 4. Now the pieces can be counted together.", "12টা কাট দুয়োটাতে মিলে, কাৰণ 12 হৈছে 3 আৰু 4ৰ ল.সা.গু.। এতিয়া টুকুৰাবোৰ একেলগে গণিব পাৰি।")),
    ]),
    "m3.u3.s2": (B("The decimal that never lands", "কেতিয়াও শেষ নোহোৱা দশমিক"), B("The green pin is $\\frac{1}{3}$. Decimals only have tenths, hundredths and so on. Can they reach it?", "সেউজীয়া পিনটো $\\frac{1}{3}$। দশমিকত কেৱল দশমাংশ, শতাংশ আদি থাকে। ই পাব পাৰিবনে?"), {"kind": "line", "min": 0, "max": 1, "pin": {"v": 0.3333333333333333, "t": "1/3"}, "readonly": True}, [
        task(B("Zoom in once.", "এবাৰ জুম কৰা।"), {"zoom": {"gt": 8}}, B("It sits between 0.3 and 0.4.", "ই 0.3 আৰু 0.4ৰ মাজত।")),
        task(B("Zoom in again.", "আকৌ জুম কৰা।"), {"zoom": {"gt": 80}}, B("Now between 0.33 and 0.34.", "এতিয়া 0.33 আৰু 0.34ৰ মাজত।")),
        task(B("Once more.", "আৰু এবাৰ।"), {"zoom": {"gt": 800}}, B("Between 0.333 and 0.334. Each zoom adds another 3 and it never lands, so $\\frac{1}{3} = 0.\\overline{3}$.", "0.333 আৰু 0.334ৰ মাজত। প্ৰতিটো জুমে আৰু এটা 3 যোগ কৰে, কিন্তু ই কেতিয়াও ঠিক বিন্দুত নপৰে, সেয়ে $\\frac{1}{3} = 0.\\overline{3}$।")),
    ]),
    "m5.u1.s2": (B("Two rulers, one length", "দুডাল জোখ, এটা দৈৰ্ঘ্য"), B("The top ruler counts percent. The bottom ruler counts the same length as an amount of 240.", "ওপৰৰ জোখে শতাংশ গণে। তলৰ জোখে একে দৈৰ্ঘ্যক 240ৰ পৰিমাণ হিচাপে গণে।"), {"kind": "dual", "base": 240}, [
        task(B("Drag to 10%.", "10%লৈ টানা।"), {"pct": 10}, B("10% of 240 is 24: the decimal point moved one place.", "240ৰ 10% হ'ল 24: দশমিক এঘৰ সৰিল।")),
        task(B("Drag to 15%.", "15%লৈ টানা।"), {"pct": 15}, B("10% and half of it again: 24 + 12 = 36.", "10% আৰু তাৰ আধা: 24 + 12 = 36।")),
    ]),
    "m5.u3.s1": (B("The corner that gets forgotten", "পাহৰি যোৱা চুক"), B("The dashed square is 100%. Two percentage changes stretch its two sides.", "ডেচ দিয়া বৰ্গটো 100%। দুটা শতাংশ পৰিৱৰ্তনে দুটা বাহু টানে।"), {"kind": "area", "a": 0, "b": 0}, [
        task(B("Set width +10% and height +10%.", "প্ৰস্থ +10% আৰু উচ্চতা +10% কৰা।"), {"a": 10, "b": 10}, B("10 + 10 is not all of it. The gold corner adds 1, making 21%. That corner is the $\\frac{ab}{100}$.", "10 + 10তে শেষ নহয়। সোণালী চুকে 1 যোগ কৰি 21% কৰে। সেই চুকেই $\\frac{ab}{100}$।")),
        task(B("Now width +20% and height −20%.", "এতিয়া প্ৰস্থ +20% আৰু উচ্চতা −20% কৰা।"), {"a": 20, "b": -20}, B("Up 20 and down 20 does not cancel: the corner costs 4, so the total is −4%.", "20 বাঢ়ি 20 কমিলেও সমান নহয়: চুকে 4 কমায়, মুঠ −4%।")),
    ]),
}

EXTRA_STORIES = {
    "m1.u1.s2": [story("m1.u1.s3", B("Why primes refuse", "মৌলিকে কিয় নামানে"), [B("Now try 13 dots, the same way.", "এতিয়া 13টা বিন্দুৰে একেদৰে চেষ্টা কৰা।")], widget={"kind": "array", "n": 13, "max": 12, "c": 2})],
}
EXTRA_TASKS = {
    "m1.u1.s3": [task(B("Slide all the way to 12.", "12লৈকে টানা।"), {"c": 12}, B("Red dots every time. 13 only makes one long row, and that is what prime means.", "প্ৰতিবাৰে ৰঙা বিন্দু। 13ৰ কেৱল এটা দীঘল শাৰী হয়, মৌলিক মানে এয়াই।"))],
}


def line_unit():
    p = "m1.l"
    mirror = B("−8 is further left. Further left is always smaller, even though 8 looks bigger.", "−8 আৰু বাওঁফালে। যিমান বাওঁফালে সিমান সৰু, 8 ডাঙৰ যেন লাগিলেও।")
    return unit("line", B("The number line", "সংখ্যা ৰেখা"), "star", [
        B("A number is a place: positive to the right of 0, negative to the left.", "সংখ্যা এটা স্থান: 0ৰ সোঁফালে ধনাত্মক, বাওঁফালে ঋণাত্মক।"),
        B("On the line, further left always means smaller.", "ৰেখাত যিমান বাওঁফালে সিমান সৰু।"),
        B("Each ×10 zoom opens one more decimal place.", "প্ৰতিটো ×10 জুমে এটা দশমিক স্থান খোলে।"),
        B("A decimal and a fraction can be two names for one point.", "দশমিক আৰু ভগ্নাংশ এটা বিন্দুৰ দুটা নাম হ'ব পাৰে।"),
    ], [
        {**story(f"{p}.s1", B("Zero is a mirror", "শূন্য এখন দাপোণ"), [B("Every number is a place on this line. Right of 0 is positive and left of 0 is negative.", "প্ৰতিটো সংখ্যা এই ৰেখাৰ এটা স্থান। 0ৰ সোঁফালে ধনাত্মক, বাওঁফালে ঋণাত্মক।")], widget={"kind": "line", "value": 3, "mirror": True, "fractions": False}), "tasks": [
            task(B("Drag the pin to 7.", "পিনটো 7লৈ টানা।"), {"value": 7}, B("7 is seven steps right of zero. The faint pin is its mirror, −7.", "7 শূন্যৰ সোঁফালে সাত খোজ। পাতল পিনটো ইয়াৰ দাপোণৰ ছবি, −7।")),
            task(B("Now drag it to −2.", "এতিয়া −2লৈ টানা।"), {"value": -2}, B("−2 is right of −7, so −2 is the bigger number. Size is about position.", "−2 −7ৰ সোঁফালে, সেয়ে −2 ডাঙৰ। ডাঙৰ-সৰু স্থানৰ কথা।")),
        ]},
        {**story(f"{p}.s2", B("Zoom between two numbers", "দুটা সংখ্যাৰ মাজলৈ জুম"), [B("There is always more room between two numbers. Pinch the line, or use the zoom button.", "দুটা সংখ্যাৰ মাজত সদায় ঠাই থাকে। ৰেখাত আঙুলিৰে জুম কৰা বা বুটাম টিপা।")], widget={"kind": "line", "value": 2}), "tasks": [
            task(B("Zoom in on the pin once.", "পিনটোত এবাৰ জুম কৰা।"), {"zoom": {"gt": 8}}, B("Each step became ten: 2.1, 2.2, 2.3. These are tenths.", "প্ৰতিটো খোজ দহটা হ'ল: 2.1, 2.2, 2.3। এইবোৰ দশমাংশ।")),
            task(B("Zoom in again.", "আকৌ জুম কৰা।"), {"zoom": {"gt": 80}}, B("Now hundredths. Place value is simply how far you have zoomed.", "এতিয়া শতাংশ। স্থানীয় মান মানে তুমি কিমান জুম কৰিছা।")),
        ]},
        {**story(f"{p}.s3", B("One point, two names", "এটা বিন্দু, দুটা নাম"), [B("Decimals are written above the line and fractions below it. They name the same points.", "ৰেখাৰ ওপৰত দশমিক, তলত ভগ্নাংশ। দুয়োটাই একে বিন্দুৰ নাম।")], widget={"kind": "line", "min": -1, "max": 1, "value": 0.5, "fractions": True, "percent": True}), "tasks": [
            task(B("Drag the pin to $\\frac{3}{4}$.", "পিনটো $\\frac{3}{4}$লৈ টানা।"), {"value": 0.75}, B("$\\frac{3}{4}$, 0.75 and 75% are three names for one point.", "$\\frac{3}{4}$, 0.75 আৰু 75% এটা বিন্দুৰ তিনিটা নাম।")),
            task(B("Now find $-\\frac{1}{4}$.", "এতিয়া $-\\frac{1}{4}$ বিচাৰা।"), {"value": -0.25}, B("Negative fractions sit to the left, exactly as whole numbers do.", "ঋণাত্মক ভগ্নাংশও অখণ্ড সংখ্যাৰ দৰে বাওঁফালে থাকে।")),
        ]},
        explore(f"{p}.q1", "n-line", lambda v: {"q": B(f"Put the pin on {str(v).replace('-', '−')}.", f"পিনটো {str(v).replace('-', '−')}ত ৰাখা।"), "widget": {"kind": "line", "fractions": False}, "target": v, "answerText": B(f"{str(v).replace('-', '−')} on the line", f"ৰেখাত {str(v).replace('-', '−')}"), "why": B("Negative numbers are left of zero; count steps out from 0.", "ঋণাত্মক সংখ্যা শূন্যৰ বাওঁফালে; 0ৰ পৰা খোজ গণা।")}, [(-7,), (-4,), (6,), (-9,)]),
        tf(f"{p}.q2", "n-line", B("−8 is greater than −3.", "−8 −3তকৈ ডাঙৰ।"), False, B("−3 is to the right of −8, so −3 is greater.", "−3 −8ৰ সোঁফালে, সেয়ে −3 ডাঙৰ।"), ("m-neg-order", mirror)),
        order(f"{p}.q3", "n-line", B("Put these in order, smallest first", "সৰুৰ পৰা ডাঙৰলৈ সজোৱা"), [B("−5", "−5"), B("−2", "−2"), B("0", "0"), B("3", "3")], B("Read the line from left to right.", "ৰেখাডাল বাওঁৰ পৰা সোঁলৈ পঢ়া।")),
        explore(f"{p}.q4", "n-decimal", lambda v: {"q": B(f"Zoom in and put the pin on {v}.", f"জুম কৰি পিনটো {v}ত ৰাখা।"), "widget": {"kind": "line", "min": 0, "max": 10, "fractions": False}, "target": v, "answerText": B(f"{v} on the line", f"ৰেখাত {v}"), "why": B("Whole number first, then one zoom for each decimal digit.", "প্ৰথমে গোটা সংখ্যা, তাৰ পিছত প্ৰতিটো দশমিক অংকৰ বাবে এবাৰ জুম।")}, [(2.37,), (5.81,), (7.25,)], hints=[B("Put the pin near the number, then press Zoom in ×10.", "সংখ্যাটোৰ ওচৰত পিন ৰাখি ×10 জুম টিপা।")]),
        tf(f"{p}.q5", "n-decimal", B("0.25 is greater than 0.3.", "0.25 0.3তকৈ ডাঙৰ।"), False, B("0.3 is 0.30, which is further right than 0.25.", "0.3 মানে 0.30, ই 0.25ৰ সোঁফালে।"), ("m-dec-long", B("More digits does not mean bigger. Compare place by place: 3 tenths beats 2 tenths.", "বেছি অংক মানে ডাঙৰ নহয়। স্থান অনুসৰি তুলনা কৰা: 3 দশমাংশ 2 দশমাংশতকৈ ডাঙৰ।"))),
        solve(f"{p}.q6", "n-line", lambda a, b: {"q": B(f"How many steps is it from {str(a).replace('-', '−')} to {b}?", f"{str(a).replace('-', '−')}ৰ পৰা {b}লৈ কিমান খোজ?"), "answer": str(b - a), "why": B(f"{-a} steps to reach 0, then {b} more.", f"0 পাবলৈ {-a} খোজ, তাৰ পিছত আৰু {b}।"), "traps": [{"ans": str(b + a), "tag": "m-neg-order", "why": B("Distance through zero adds the two sizes: count to 0, then on.", "শূন্যৰ মাজেৰে দূৰত্বত দুয়োটা আকাৰ যোগ হয়: 0লৈ গণি আগবাঢ়া।")}]}, [(-3, 4), (-6, 2), (-5, 7)]),
        explore(f"{p}.q7", "n-decimal", lambda p_, q, v: {"q": B(f"Put the pin on ${fr(p_, q)}$. The fractions are below the line.", f"পিনটো ${fr(p_, q)}ত ৰাখা। ভগ্নাংশবোৰ ৰেখাৰ তলত।"), "widget": {"kind": "line", "min": 0, "max": 1, "fractions": True, "percent": True}, "target": v, "answerText": B(f"{v}", f"{v}"), "why": B(f"${fr(p_, q)}$ is the same point as {v}.", f"${fr(p_, q)}$ আৰু {v} একে বিন্দু।")}, [(3, 4, 0.75), (1, 4, 0.25), (1, 2, 0.5)]),
    ])


NEW_EXERCISES = {
    "m2.u2": lambda: explore("m2.u2.q6", "l-lcm", lambda a, b, l: {"q": B(f"Turn the gears until they first meet again. How many teeth for {a} and {b}?", f"প্ৰথমবাৰ আকৌ নিমিলালৈ গিয়াৰ ঘূৰোৱা। {a} আৰু {b}ৰ বাবে কিমান দাঁত?"), "widget": {"kind": "gears", "a": a, "b": b}, "target": l, "answerText": B(f"{l} teeth", f"{l}টা দাঁত"), "why": B(f"{l} is the first multiple of both {a} and {b}.", f"{l} {a} আৰু {b} দুয়োটাৰে প্ৰথম গুণিতক।")}, [(6, 8, 24), (4, 10, 20), (6, 9, 18)]),
    "m5.u1": lambda: explore("m5.u1.q6", "p-of", lambda base, pct: {"q": B(f"Drag until the amount reads {base * pct // 100}. What percent of {base} is it?", f"পৰিমাণ {base * pct // 100} নোহোৱালৈ টানা। ই {base}ৰ কিমান শতাংশ?"), "widget": {"kind": "dual", "base": base}, "target": pct, "answerText": B(f"{pct}%", f"{pct}%"), "why": B(f"Both rulers measure one length, so {pct}% of {base} is {base * pct // 100}.", f"দুয়োডাল জোখে একে দৈৰ্ঘ্য জোখে, সেয়ে {base}ৰ {pct}% হ'ল {base * pct // 100}।")}, [(240, 35), (80, 45), (600, 15)]),
}


def apply(lessons):
    """Turn the listed story cards into scenes and add the number-line unit."""
    for L in lessons:
        for u in L["units"]:
            steps = []
            for s in u["steps"]:
                lab = LABS.get(s["id"])
                if lab:
                    title, text, widget, tasks = lab
                    s = {"id": s["id"], "type": "story", "title": title, "text": [text], "widget": widget, "tasks": tasks}
                steps.append(s)
                for extra in EXTRA_STORIES.get(s["id"], []):
                    steps.append({**extra, "tasks": EXTRA_TASKS[extra["id"]]})
            u["steps"] = steps
            prefix = f"m{L['no']}.{u['id']}"
            if prefix in NEW_EXERCISES:
                u["steps"].append(NEW_EXERCISES[prefix]())
        if L["no"] == 1:
            L["units"].insert(0, line_unit())
    return lessons
