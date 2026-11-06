"""Lesson 14: Venn diagrams."""
from math_kit import B, match, mcq, part, solve, stepwise, tf, unit, with_variants
from math_lessons_c import diagram, lab
from math_labs import task
from reason_kit import bits

REGION = "r-region"; RELATE = "r-relate"; COUNT = "r-count"; THREE = "r-three"
DOUBLE = B("You counted the overlap twice. It sits inside both circles, so subtract it once.", "তুমি সাধাৰণ অংশ দুবাৰ গণিলা। ই দুয়োটা বৃত্তত আছে, গতিকে এবাৰ বিয়োগ কৰা।")
ONLY = B("'Only' leaves out the overlap. Shade just the part of the circle that no other circle covers.", "'কেৱল' কোৱাত সাধাৰণ অংশ নপৰে। বৃত্তৰ আন বৃত্তই নুঢকা অংশহে ছাঁ দিয়া।")
INSIDE = B("If every X is a Y, circle X sits wholly inside circle Y.", "প্ৰতিটো X যদি Y হয়, X ৰ বৃত্ত গোটেই Y ৰ বৃত্তৰ ভিতৰত থাকে।")
T2 = [B("Tea", "চাহ"), B("Coffee", "কফি")]
T3 = [B("Tea", "চাহ"), B("Coffee", "কফি"), B("Milk", "গাখীৰ")]

# Diagrams for setpick, in a 100-unit box.
INSIDE2 = [[50, 50, 44], [50, 50, 22]]
APART2 = [[27, 50, 23], [73, 50, 23]]
CROSS2 = [[36, 50, 30], [64, 50, 30]]
APART3 = [[21, 50, 18], [50, 50, 10], [79, 50, 18]]
NEST3 = [[50, 50, 46], [50, 50, 30], [50, 50, 14]]
TWOIN = [[50, 50, 46], [31, 50, 15], [69, 50, 15]]
CROSS3 = [[38, 40, 26], [62, 40, 26], [50, 62, 26]]
ONEOUT = [[32, 50, 26], [32, 50, 13], [80, 50, 15]]
CROSSIN = [[50, 55, 42], [38, 55, 17], [62, 55, 17]]


def tap(phrase, regions, why, sets=T2, n=2, trap=None):
    # Every version sets traps: a version without them would inherit the first version's.
    return {"q": phrase, "widget": {"kind": "venn", "n": n, "sets": sets}, "target": bits(*regions), "answerText": why, "why": why,
            "traps": [{"val": bits(*trap), "tag": "r-m-only", "why": ONLY}] if trap is not None else []}


def pick(q, options, answer, why):
    return {"q": q, "widget": {"kind": "setpick", "options": options}, "target": answer, "answerText": why, "why": why}


def within(only_a, both):
    return {"q": B(f"{only_a} people drink only tea and {both} drink both tea and coffee. How many drink tea?", f"{only_a} জনে কেৱল চাহ খায়, {both} জনে চাহ আৰু কফি দুয়োটা খায়। চাহ খোৱা মুঠ কিমান?"), "answer": str(only_a + both),
            "why": B(f"The tea circle holds both regions: {only_a} + {both} = {only_a + both}.", f"চাহৰ বৃত্তত দুয়োটা অংশ আছে: {only_a} + {both} = {only_a + both}।"), "traps": [{"ans": str(only_a), "tag": "r-m-only", "why": ONLY}]}


def union(a, b, both):
    return {"q": B(f"{a} students play football, {b} play cricket and {both} play both. How many play at least one?", f"{a} জন ছাত্ৰই ফুটবল, {b} জনে ক্ৰিকেট আৰু {both} জনে দুয়োটা খেলে। অন্ততঃ এটা খেলা ছাত্ৰ কিমান?"), "answer": str(a + b - both),
            "why": B(f"{a} + {b} counts the {both} twice, so subtract once: {a + b - both}.", f"{a} + {b} ত {both} দুবাৰ পৰিছে, এবাৰ বিয়োগ কৰা: {a + b - both}।"), "traps": [{"ans": str(a + b), "tag": "r-m-double", "why": DOUBLE}]}


def neither(total, a, b, both):
    u = a + b - both
    return {"q": B(f"In a class of {total}, {a} read Assamese, {b} read English and {both} read both. How many read neither?", f"{total} জনৰ শ্ৰেণীত {a} জনে অসমীয়া, {b} জনে ইংৰাজী আৰু {both} জনে দুয়োটা পঢ়ে। কোনোটো নপঢ়া কিমান?"), "answer": str(total - u),
            "why": B(f"At least one is {u}, so {total} − {u} = {total - u} read neither.", f"অন্ততঃ এটা পঢ়া {u} জন, গতিকে {total} − {u} = {total - u} জনে কোনোটো নপঢ়ে।"), "traps": [{"ans": str(total - a - b), "tag": "r-m-double", "why": DOUBLE}]}


def count_steps(total, a, b, both):
    s = "rs14.u3.q3"
    oa, ob, u = a - both, b - both, a + b - both
    return {"q": B(f"Of {total} farmers, {a} grow rice, {b} grow tea and {both} grow both.", f"{total} জন খেতিয়কৰ {a} জনে ধান, {b} জনে চাহ আৰু {both} জনে দুয়োটা খেতি কৰে।"), "parts": [
        part(B("Rice only?", "কেৱল ধান?"), B(str(oa), str(oa)), [B(str(a), str(a)), B(str(a + both), str(a + both))], B(f"{a} − {both} = {oa}.", f"{a} − {both} = {oa}।"), tag="r-m-only", sid=s),
        part(B("Tea only?", "কেৱল চাহ?"), B(str(ob), str(ob)), [B(str(b), str(b)), B(str(b + both), str(b + both))], B(f"{b} − {both} = {ob}.", f"{b} − {both} = {ob}।"), tag="r-m-only", sid=s),
        part(B("Neither?", "কোনোটো নহয়?"), B(str(total - u), str(total - u)), [B(str(total - a - b), str(total - a - b)), B(str(total - both), str(total - both))], B(f"{total} − ({oa} + {ob} + {both}) = {total - u}.", f"{total} − ({oa} + {ob} + {both}) = {total - u}।"), tag="r-m-double", sid=s),
    ], "why": B("Fill the overlap first, then each 'only' region, then the outside.", "প্ৰথমে সাধাৰণ অংশ, তাৰ পিছত 'কেৱল' অংশ, শেষত বাহিৰ।")}


def exactly_one(oa, ob, both):
    return {"q": B("Shade everyone who likes exactly one of the two.", "দুটাৰ ঠিক এটা ভাল পোৱা সকলোকে ছাঁ দিয়া।"), "widget": {"kind": "venn", "n": 2, "sets": T2, "counts": {1: oa, 2: ob, 3: both}, "showTotal": True}, "target": bits(1, 2), "answerText": B(f"{oa + ob} people", f"{oa + ob} জন"),
            "traps": [{"val": bits(1, 2, 3), "tag": "r-m-only", "why": ONLY}], "why": B(f"Exactly one excludes the overlap: {oa} + {ob} = {oa + ob}.", f"ঠিক এটা মানে সাধাৰণ অংশ নপৰে: {oa} + {ob} = {oa + ob}।")}


def three_total(c):
    regs = {k: v for k, v in zip((1, 2, 3, 4, 5, 6, 7), c)}
    two = regs[3] + regs[5] + regs[6]
    return {"q": B("Shade everyone in exactly two circles.", "ঠিক দুটা বৃত্তত থকা সকলোকে ছাঁ দিয়া।"), "widget": {"kind": "venn", "n": 3, "sets": T3, "counts": regs, "showTotal": True}, "target": bits(3, 5, 6), "answerText": B(f"{two} people", f"{two} জন"),
            "traps": [{"val": bits(3, 5, 6, 7), "tag": "r-m-double", "why": DOUBLE}], "why": B(f"Exactly two leaves out the centre: {regs[3]} + {regs[5]} + {regs[6]} = {two}.", f"ঠিক দুটা হ'লে মাজৰ অংশ নপৰে: {regs[3]} + {regs[5]} + {regs[6]} = {two}।")}


def three_sum(oa, ab, ac, abc):
    return {"q": B(f"In the tea circle, {oa} are tea only, {ab} tea and coffee only, {ac} tea and milk only, and {abc} all three. How many are in the tea circle?", f"চাহৰ বৃত্তত {oa} জন কেৱল চাহ, {ab} জন কেৱল চাহ আৰু কফি, {ac} জন কেৱল চাহ আৰু গাখীৰ, {abc} জন তিনিওটা। চাহৰ বৃত্তত মুঠ কিমান?"), "answer": str(oa + ab + ac + abc),
            "why": B(f"A circle of three sets has four regions: {oa + ab + ac + abc}.", f"তিনি সংহতিত এটা বৃত্তৰ চাৰিটা অংশ: {oa + ab + ac + abc}।"), "traps": [{"ans": str(oa), "tag": "r-m-only", "why": ONLY}]}


def three_steps(a, ab, ac, abc):
    s = "rs14.u4.q4"
    oa = a - ab - ac - abc
    return {"q": B(f"{a} like tea. Of these, {ab} like tea and coffee only, {ac} like tea and milk only and {abc} like all three.", f"{a} জনে চাহ ভাল পায়। ইয়াৰে {ab} জনে কেৱল চাহ আৰু কফি, {ac} জনে কেৱল চাহ আৰু গাখীৰ, {abc} জনে তিনিওটা ভাল পায়।"), "parts": [
        part(B("Start with which region?", "কোন অংশৰ পৰা আৰম্ভ?"), B("The centre", "মাজৰ অংশ"), [B("Tea only", "কেৱল চাহ"), B("The outside", "বাহিৰ")], B("The centre has one meaning, so it is the safest start.", "মাজৰ অংশৰ অৰ্থ এটাই, সেয়ে ইয়াৰ পৰা আৰম্ভ কৰা সুৰক্ষিত।"), sid=s),
        part(B("Together, the shared parts of tea are?", "চাহৰ সাধাৰণ অংশবোৰৰ মুঠ?"), B(str(ab + ac + abc), str(ab + ac + abc)), [B(str(ab + ac), str(ab + ac)), B(str(ab + abc), str(ab + abc))], B(f"{ab} + {ac} + {abc}.", f"{ab} + {ac} + {abc}।"), tag="r-m-double", sid=s),
        part(B("Tea only?", "কেৱল চাহ?"), B(str(oa), str(oa)), [B(str(a), str(a)), B(str(a - ab - ac), str(a - ab - ac))], B(f"{a} − {ab + ac + abc} = {oa}.", f"{a} − {ab + ac + abc} = {oa}।"), tag="r-m-only", sid=s),
    ], "why": B("Work outwards from the centre, subtracting what is already placed.", "মাজৰ পৰা বাহিৰলৈ গৈ বহুওৱাখিনি বিয়োগ কৰা।")}


def relate_steps(big, small, other):
    s = "rs14.u2.q3"
    return {"q": B(f"Decide the diagram for {big[0]}, {small[0]} and {other[0]}.", f"{big[1]}, {small[1]} আৰু {other[1]} ৰ চিত্ৰ ঠিক কৰা।"), "parts": [
        part(B(f"{big[0].capitalize()} and {small[0]}?", f"{big[1]} আৰু {small[1]}?"), B(f"{small[0].capitalize()} inside {big[0]}", f"{small[1]} {big[1]} ৰ ভিতৰত"), [B("Apart", "আঁতৰত"), B("Overlapping", "ওপৰা-ওপৰি")], B(f"All {small[0]} are {big[0]}.", f"সকলো {small[1]} {big[1]}।"), tag="r-m-inside", sid=s),
        part(B(f"{big[0].capitalize()} and {other[0]}?", f"{big[1]} আৰু {other[1]}?"), B("Apart", "আঁতৰত"), [B(f"{other[0].capitalize()} inside {big[0]}", f"{other[1]} {big[1]} ৰ ভিতৰত"), B("Overlapping", "ওপৰা-ওপৰি")], B("Nothing is both.", "কোনো বস্তু দুয়োটা নহয়।"), sid=s),
    ], "why": B("A nested pair, with one circle apart.", "এটা ভিতৰৰ যোৰ, আৰু এটা আঁতৰৰ বৃত্ত।")}


def lesson():
    p = "rs14"
    u1 = unit("u1", B("Every region has a name", "প্ৰতিটো অংশৰ এটা নাম"), "star", [
        B("A circle holds everything with one property.", "এটা বৃত্তত এটা গুণ থকা সকলো থাকে।"),
        B("The overlap holds what has both properties.", "সাধাৰণ অংশত দুয়োটা গুণ থকাখিনি থাকে।"),
        B("'Only' leaves out the overlap.", "'কেৱল' কোৱাত সাধাৰণ অংশ নপৰে।"),
        B("The outside holds what has neither.", "বাহিৰত দুয়োটা নথকাখিনি থাকে।"),
    ], [
        lab(f"{p}.u1.s1", B("Four places to stand", "থিয় হোৱাৰ চাৰি ঠাই"), B("Each person belongs to exactly one region. Tap a region to shade it, and tap again to clear it.", "প্ৰতিজন ঠিক এটা অংশত থাকে। অংশত টিপি ছাঁ দিয়া, আকৌ টিপিলে আঁতৰে।"), {"kind": "venn", "n": 2, "sets": T2}, [
            task(B("Shade the people who drink both.", "দুয়োটা খোৱা সকলোক ছাঁ দিয়া।"), {"sel": bits(3)}, B("The overlap is both circles at once.", "সাধাৰণ অংশ একেলগে দুয়োটা বৃত্ত।")),
            task(B("Now shade only those who drink tea only.", "এতিয়া কেৱল চাহ খোৱাসকলকহে ছাঁ দিয়া।"), {"sel": bits(1)}, B("'Only' removed the overlap.", "'কেৱল' কোৱাত সাধাৰণ অংশ আঁতৰিল।")),
        ]),
        lab(f"{p}.u1.s2", B("The space outside counts", "বাহিৰৰ ঠাইও গণনাত"), B("Someone who drinks neither still belongs on the page. They stand outside both circles.", "দুয়োটা নোখোৱাজনো চিত্ৰত থাকে। তেওঁ দুয়োটা বৃত্তৰ বাহিৰত।"), {"kind": "venn", "n": 2, "sets": T2}, [
            task(B("Shade those who drink neither.", "দুয়োটা নোখোৱাসকলক ছাঁ দিয়া।"), {"sel": bits(0)}, B("That is the fourth region. Exams often ask for it.", "সেয়া চতুৰ্থ অংশ। পৰীক্ষাত সঘনাই সোধে।")),
        ]),
        with_variants({"id": f"{p}.u1.q1", "type": "explore", "skill": REGION}, tap, [
            (B("Shade those who drink coffee only.", "কেৱল কফি খোৱাসকলক ছাঁ দিয়া।"), [2], B("Coffee without the overlap.", "সাধাৰণ অংশ বাদে কফি।"), T2, 2, [2, 3]),
            (B("Shade those who drink tea but not coffee.", "চাহ খায় কিন্তু কফি নোখোৱাসকলক ছাঁ দিয়া।"), [1], B("Tea without the overlap.", "সাধাৰণ অংশ বাদে চাহ।"), T2, 2, [1, 3]),
            (B("Shade everyone who drinks tea.", "চাহ খোৱা সকলোকে ছাঁ দিয়া।"), [1, 3], B("All of the tea circle, overlap included.", "সাধাৰণ অংশসহ গোটেই চাহৰ বৃত্ত।"), T2, 2, [1]),
        ]),
        with_variants({"id": f"{p}.u1.q2", "type": "explore", "skill": REGION}, tap, [
            (B("Shade those who drink at least one of the two.", "দুটাৰ অন্ততঃ এটা খোৱাসকলক ছাঁ দিয়া।"), [1, 2, 3], B("Everything inside the circles.", "বৃত্তৰ ভিতৰৰ সকলো।")),
            (B("Shade those who do not drink tea.", "চাহ নোখোৱাসকলক ছাঁ দিয়া।"), [0, 2], B("Everything outside the tea circle.", "চাহৰ বৃত্তৰ বাহিৰৰ সকলো।")),
        ]),
        tf(f"{p}.u1.q3", REGION, B("'Tea only' includes people who drink both.", "'কেৱল চাহ' ত দুয়োটা খোৱাসকল থাকে।"), False, B("'Only' excludes the overlap.", "'কেৱল' ত সাধাৰণ অংশ নপৰে।"), ("r-m-only", ONLY)),
        match(f"{p}.u1.q4", REGION, B("Match the words to the region", "শব্দক অংশৰ লগত মিলোৱা"), [[B("Both", "দুয়োটা"), B("The overlap", "সাধাৰণ অংশ")], [B("Neither", "কোনোটো নহয়"), B("Outside the circles", "বৃত্তৰ বাহিৰত")], [B("Tea only", "কেৱল চাহ"), B("Tea minus the overlap", "সাধাৰণ অংশ বাদে চাহ")], [B("At least one", "অন্ততঃ এটা"), B("Inside any circle", "যিকোনো বৃত্তৰ ভিতৰত")]], B("Each phrase names a fixed region.", "প্ৰতিটো শব্দই নিৰ্দিষ্ট অংশ বুজায়।")),
        solve(f"{p}.u1.q5", REGION, within, [(12, 5), (20, 8), (15, 9)]),
    ])
    u2 = unit("u2", B("Pick the right diagram", "সঠিক চিত্ৰ বাছনি"), "star", [
        B("If every X is a Y, X sits inside Y.", "প্ৰতিটো X যদি Y হয়, X, Y ৰ ভিতৰত।"),
        B("If nothing is both, the circles stay apart.", "কোনোবাই দুয়োটা নহ'লে বৃত্ত আঁতৰত থাকে।"),
        B("If some are both, the circles overlap.", "কিছুমান দুয়োটা হ'লে বৃত্ত ওপৰা-ওপৰি হয়।"),
        B("Decide three sets two at a time.", "তিনিটা সংহতি দুটাকৈ চোৱা।"),
    ], [
        diagram(f"{p}.u2.s1", B("Three ways two sets can sit", "দুটা সংহতিৰ তিনি অৱস্থা"), [B("Ask one question: can something be both? The answer decides the picture.", "এটা প্ৰশ্ন সোধা: কোনোবা দুয়োটা হ'ব পাৰেনে? উত্তৰে চিত্ৰ ঠিক কৰে।")], "grid", [B("Inside: Guwahati, Assam", "ভিতৰত: গুৱাহাটী, অসম"), B("Apart: rivers, hills", "আঁতৰত: নদী, পাহাৰ"), B("Overlap: women, teachers", "ওপৰা-ওপৰি: মহিলা, শিক্ষক")]),
        diagram(f"{p}.u2.s2", B("Three sets, two at a time", "তিনি সংহতি, দুটাকৈ"), [B("Compare the first pair, then the next, and keep only diagrams that fit every pair.", "প্ৰথম যোৰ, তাৰ পিছত পিছৰ যোৰ তুলনা কৰা। সকলো যোৰত মিলা চিত্ৰহে ৰাখা।")], "flow", [B("First pair", "প্ৰথম যোৰ"), B("Second pair", "দ্বিতীয় যোৰ"), B("Third pair", "তৃতীয় যোৰ")]),
        with_variants({"id": f"{p}.u2.q1", "type": "explore", "skill": RELATE, "traps": [{"val": 2, "tag": "r-m-inside", "why": INSIDE}]}, pick, [
            (B("Which diagram shows Assam and India?", "কোন চিত্ৰই অসম আৰু ভাৰত দেখুৱায়?"), [APART2, INSIDE2, CROSS2], 1, B("All of Assam is in India, so one circle sits inside the other.", "গোটেই অসম ভাৰতত, গতিকে এটা বৃত্ত আনটোৰ ভিতৰত।")),
            (B("Which diagram shows mangoes and fruit?", "কোন চিত্ৰই আম আৰু ফল দেখুৱায়?"), [APART2, INSIDE2, CROSS2], 1, B("Every mango is a fruit.", "প্ৰতিটো আম ফল।")),
        ]),
        with_variants({"id": f"{p}.u2.q2", "type": "explore", "skill": RELATE}, pick, [
            (B("Which diagram shows fruit, mangoes and bananas?", "কোন চিত্ৰই ফল, আম আৰু কল দেখুৱায়?"), [APART3, NEST3, TWOIN, CROSS3], 2, B("Two separate groups sit inside one larger group.", "দুটা পৃথক গোট এটা ডাঙৰ গোটৰ ভিতৰত।")),
            (B("Which diagram shows India, Assam and Guwahati?", "কোন চিত্ৰই ভাৰত, অসম আৰু গুৱাহাটী দেখুৱায়?"), [APART3, NEST3, TWOIN, CROSS3], 1, B("Each sits wholly inside the next.", "প্ৰতিটো পিছৰটোৰ ভিতৰত।")),
            (B("Which diagram shows rivers, hills and cups?", "কোন চিত্ৰই নদী, পাহাৰ আৰু কাপ দেখুৱায়?"), [APART3, NEST3, TWOIN, CROSS3], 0, B("Nothing is two of these at once.", "কোনো বস্তু একেলগে দুটা নহয়।")),
            (B("Which diagram shows women, teachers and singers?", "কোন চিত্ৰই মহিলা, শিক্ষক আৰু গায়ক দেখুৱায়?"), [APART3, NEST3, TWOIN, CROSS3], 3, B("A person can be any mix of the three.", "এজন ব্যক্তি তিনিওটাৰ যিকোনো মিশ্ৰণ হ'ব পাৰে।")),
        ]),
        stepwise(f"{p}.u2.q3", RELATE, relate_steps, [(("animals", "জীৱ"), ("cows", "গৰু"), ("tables", "টেবুল")), (("birds", "চৰাই"), ("crows", "কাউৰী"), ("chairs", "চকী")), (("flowers", "ফুল"), ("roses", "গোলাপ"), ("stones", "শিল"))]),
        tf(f"{p}.u2.q4", RELATE, B("Doctors and women should be drawn as two separate circles.", "চিকিৎসক আৰু মহিলাক দুটা পৃথক বৃত্তত আঁকিব লাগে।"), False, B("Some doctors are women, so the circles overlap.", "কিছুমান চিকিৎসক মহিলা, গতিকে বৃত্ত ওপৰা-ওপৰি।"), ("r-m-inside", INSIDE)),
        match(f"{p}.u2.q5", RELATE, B("Match the pair to how the circles sit", "যোৰক বৃত্তৰ অৱস্থাৰ লগত মিলোৱা"), [[B("Rice, food", "ভাত, খাদ্য"), B("Inside", "ভিতৰত")], [B("Boats, birds", "নাও, চৰাই"), B("Apart", "আঁতৰত")], [B("Men, singers", "পুৰুষ, গায়ক"), B("Overlap", "ওপৰা-ওপৰি")]], B("Ask whether something can be both.", "কোনোবা দুয়োটা হ'ব পাৰেনে সোধা।")),
    ])
    u3 = unit("u3", B("Count each region once", "প্ৰতিটো অংশ এবাৰ গণা"), "star", [
        B("Adding two circles counts the overlap twice.", "দুটা বৃত্ত যোগ কৰিলে সাধাৰণ অংশ দুবাৰ পৰে।"),
        B("At least one = A + B − both.", "অন্ততঃ এটা = A + B − দুয়োটা।"),
        B("Neither = total − at least one.", "কোনোটো নহয় = মুঠ − অন্ততঃ এটা।"),
        B("Fill the overlap first, then work outwards.", "প্ৰথমে সাধাৰণ অংশ, তাৰ পিছত বাহিৰলৈ।"),
    ], [
        lab(f"{p}.u3.s1", B("Why adding counts twice", "যোগত কিয় দুবাৰ পৰে"), B("Twenty people drink tea only, eight drink both and twelve drink coffee only. Shade the tea circle and read the total.", "20 জনে কেৱল চাহ, 8 জনে দুয়োটা, 12 জনে কেৱল কফি খায়। চাহৰ বৃত্ত ছাঁ দি মুঠ পঢ়া।"), {"kind": "venn", "n": 2, "sets": T2, "counts": {1: 20, 2: 12, 3: 8}, "showTotal": True}, [
            task(B("Shade all of the tea circle.", "গোটেই চাহৰ বৃত্ত ছাঁ দিয়া।"), {"sel": bits(1, 3)}, B("Tea is 28. Coffee is 20. But 28 + 20 counts the 8 twice.", "চাহ 28, কফি 20। কিন্তু 28 + 20 ত 8 দুবাৰ পৰে।")),
            task(B("Now shade all three regions.", "এতিয়া তিনিওটা অংশ ছাঁ দিয়া।"), {"sel": bits(1, 2, 3)}, B("The real total is 40, which is 48 − 8.", "প্ৰকৃত মুঠ 40, অৰ্থাৎ 48 − 8।")),
        ]),
        diagram(f"{p}.u3.s2", B("The overlap comes first", "সাধাৰণ অংশ প্ৰথমে"), [B("Write the overlap first. Subtract it from each circle, then deal with the outside.", "প্ৰথমে সাধাৰণ অংশ লিখা। প্ৰতিটো বৃত্তৰ পৰা বিয়োগ কৰা, তাৰ পিছত বাহিৰ চোৱা।")], "flow", [B("Overlap", "সাধাৰণ অংশ"), B("Each 'only'", "প্ৰতিটো 'কেৱল'"), B("Outside", "বাহিৰ")]),
        solve(f"{p}.u3.q1", COUNT, union, [(30, 25, 10), (42, 18, 12), (26, 34, 15), (50, 40, 22)]),
        solve(f"{p}.u3.q2", COUNT, neither, [(50, 30, 25, 15), (60, 35, 30, 20), (40, 22, 18, 8)]),
        stepwise(f"{p}.u3.q3", COUNT, count_steps, [(50, 30, 28, 12), (70, 40, 35, 15), (45, 25, 20, 10)]),
        tf(f"{p}.u3.q4", COUNT, B("If 20 like A, 15 like B and 5 like both, then 35 like at least one.", "20 জনে A, 15 জনে B, 5 জনে দুয়োটা ভাল পালে অন্ততঃ এটা ভাল পোৱা 35 জন।"), False, B("20 + 15 − 5 = 30.", "20 + 15 − 5 = 30।"), ("r-m-double", DOUBLE)),
        with_variants({"id": f"{p}.u3.q5", "type": "explore", "skill": COUNT}, exactly_one, [(14, 9, 6), (21, 12, 7), (8, 16, 5)]),
    ])
    u4 = unit("u4", B("Three circles", "তিনিটা বৃত্ত"), "star", [
        B("Three circles make seven inside regions.", "তিনিটা বৃত্তই ভিতৰত সাতটা অংশ বনায়।"),
        B("The centre belongs to all three.", "মাজৰ অংশ তিনিওটাৰে।"),
        B("'Exactly two' leaves out the centre.", "'ঠিক দুটা' ত মাজৰ অংশ নপৰে।"),
        B("Fill from the centre outwards.", "মাজৰ পৰা বাহিৰলৈ পূৰণ কৰা।"),
    ], [
        lab(f"{p}.u4.s1", B("Seven rooms in three circles", "তিনি বৃত্তত সাতটা কোঠা"), B("Add a third circle and every old region splits. Tap to find the centre and the 'only' rooms.", "তৃতীয় বৃত্তই পুৰণি অংশবোৰ ভাগ কৰে। টিপি মাজৰ অংশ আৰু 'কেৱল' অংশ বিচাৰা।"), {"kind": "venn", "n": 3, "sets": T3}, [
            task(B("Shade those who take all three.", "তিনিওটা খোৱাসকলক ছাঁ দিয়া।"), {"sel": bits(7)}, B("The centre is the one room inside every circle.", "মাজৰ অংশ সকলো বৃত্তৰ ভিতৰৰ একমাত্ৰ অংশ।")),
            task(B("Now shade only those who take milk only.", "এতিয়া কেৱল গাখীৰ খোৱাসকলকহে ছাঁ দিয়া।"), {"sel": bits(4)}, B("'Only' now removes two other circles.", "'কেৱল' এতিয়া আন দুটা বৃত্ত আঁতৰায়।")),
        ]),
        diagram(f"{p}.u4.s2", B("Read three-set questions inside out", "ভিতৰৰ পৰা বাহিৰলৈ পঢ়া"), [B("The centre has one meaning, so write it first. Then fill the pairs, then each 'only' room.", "মাজৰ অংশৰ অৰ্থ এটাই, সেয়ে প্ৰথমে লিখা। তাৰ পিছত যোৰ, শেষত 'কেৱল' অংশ।")], "flow", [B("Centre", "মাজ"), B("Pairs", "যোৰ"), B("'Only' rooms", "'কেৱল' অংশ")]),
        with_variants({"id": f"{p}.u4.q1", "type": "explore", "skill": THREE}, tap, [
            (B("Shade those who take tea and coffee but not milk.", "চাহ আৰু কফি খায় কিন্তু গাখীৰ নোখোৱাসকলক ছাঁ দিয়া।"), [3], B("The tea-coffee overlap without the centre.", "মাজৰ অংশ বাদে চাহ-কফিৰ সাধাৰণ অংশ।"), T3, 3, [3, 7]),
            (B("Shade those who take coffee and milk but not tea.", "কফি আৰু গাখীৰ খায় কিন্তু চাহ নোখোৱাসকলক ছাঁ দিয়া।"), [6], B("The coffee-milk overlap without the centre.", "মাজৰ অংশ বাদে কফি-গাখীৰৰ সাধাৰণ অংশ।"), T3, 3, [6, 7]),
            (B("Shade those who take tea only.", "কেৱল চাহ খোৱাসকলক ছাঁ দিয়া।"), [1], B("The part of tea that no other circle covers.", "চাহৰ আন বৃত্তই নুঢকা অংশ।"), T3, 3, [1, 3, 5, 7]),
        ]),
        with_variants({"id": f"{p}.u4.q2", "type": "explore", "skill": THREE}, three_total, [((10, 8, 3, 6, 4, 5, 2),), ((7, 9, 5, 4, 2, 6, 3),), ((12, 5, 4, 8, 6, 3, 1),)]),
        solve(f"{p}.u4.q3", THREE, three_sum, [(10, 4, 3, 2), (15, 6, 5, 3), (8, 7, 2, 4)]),
        stepwise(f"{p}.u4.q4", THREE, three_steps, [(30, 6, 5, 3), (40, 8, 7, 5), (25, 4, 6, 2)]),
        tf(f"{p}.u4.q5", THREE, B("Three overlapping circles make seven regions inside them.", "তিনিটা ওপৰা-ওপৰি বৃত্তই ভিতৰত সাতটা অংশ বনায়।"), True, B("Three 'only' rooms, three pairs and one centre.", "তিনিটা 'কেৱল', তিনিটা যোৰ আৰু এটা মাজৰ অংশ।")),
        match(f"{p}.u4.q6", THREE, B("Match the phrase to how many circles it means", "শব্দক বৃত্তৰ সংখ্যাৰ লগত মিলোৱা"), [[B("Only", "কেৱল"), B("One", "এটা")], [B("Exactly two", "ঠিক দুটা"), B("Two", "দুটা")], [B("All", "সকলো"), B("Three", "তিনিটা")], [B("Neither", "কোনোটো নহয়"), B("No circle", "এটাও নহয়")]], B("Count the circles that contain the region.", "অংশটো থকা বৃত্ত গণা।")),
    ])
    test = {"id": "test", "title": B("Venn test", "ভেন পৰীক্ষা"), "steps": [
        mcq(f"{p}.t.q1", COUNT, lambda a, b, c: {"q": B(f"{a} like A, {b} like B and {c} like both. How many like at least one?", f"{a} জনে A, {b} জনে B, {c} জনে দুয়োটা ভাল পায়। অন্ততঃ এটা ভাল পোৱা কিমান?"), "right": a + b - c, "wrong": [(a + b, "r-m-double", DOUBLE)], "fill": [a + b - 2 * c, a - c, b - c, c], "why": B(f"{a} + {b} − {c} = {a + b - c}.", f"{a} + {b} − {c} = {a + b - c}।")}, [(24, 18, 6), (35, 25, 10), (40, 15, 7)]),
        mcq(f"{p}.t.q2", COUNT, lambda t, a, b, c: {"q": B(f"Of {t} people, {a} like A, {b} like B and {c} like both. How many like neither?", f"{t} জনৰ {a} জনে A, {b} জনে B, {c} জনে দুয়োটা ভাল পায়। কোনোটো ভাল নোপোৱা কিমান?"), "right": t - a - b + c, "wrong": [(t - a - b, "r-m-double", DOUBLE)], "fill": [t - c, a + b - c, t - a, c + 1], "why": B(f"{t} − ({a} + {b} − {c}) = {t - a - b + c}.", f"{t} − ({a} + {b} − {c}) = {t - a - b + c}।")}, [(60, 30, 25, 10), (50, 28, 20, 8), (45, 20, 22, 7)]),
        mcq(f"{p}.t.q3", REGION, lambda a, b: {"q": B(f"{a} people like A and {b} of them also like B. How many like A only?", f"{a} জনে A ভাল পায়, ইয়াৰে {b} জনে B ও ভাল পায়। কেৱল A ভাল পোৱা কিমান?"), "right": a - b, "wrong": [(a, "r-m-only", ONLY)], "fill": [a + b, b, a - b + 1], "why": B(f"Remove the overlap: {a} − {b} = {a - b}.", f"সাধাৰণ অংশ আঁতৰোৱা: {a} − {b} = {a - b}।")}, [(30, 12), (45, 20), (28, 9)]),
        with_variants({"id": f"{p}.t.q4", "type": "explore", "skill": RELATE}, pick, [
            (B("Which diagram shows vegetables, potatoes and cars?", "কোন চিত্ৰই পাচলি, আলু আৰু গাড়ী দেখুৱায়?"), [ONEOUT, NEST3, TWOIN, CROSS3], 0, B("Potatoes sit inside vegetables, and cars stand apart.", "আলু পাচলিৰ ভিতৰত, গাড়ী আঁতৰত।")),
            (B("Which diagram shows birds, crows and pens?", "কোন চিত্ৰই চৰাই, কাউৰী আৰু কলম দেখুৱায়?"), [ONEOUT, NEST3, TWOIN, CROSS3], 0, B("Crows sit inside birds, and pens stand apart.", "কাউৰী চৰাইৰ ভিতৰত, কলম আঁতৰত।")),
        ]),
        tf(f"{p}.t.q5", THREE, B("'Exactly two' includes people in all three circles.", "'ঠিক দুটা' ত তিনিওটা বৃত্তত থকাসকল থাকে।"), False, B("'Exactly two' leaves out the centre.", "'ঠিক দুটা' ত মাজৰ অংশ নপৰে।"), ("r-m-double", DOUBLE)),
        solve(f"{p}.t.q6", THREE, three_sum, [(9, 3, 4, 2), (12, 5, 2, 6)]),
    ]}
    return {"id": "rs-14-venn", "no": 14, "slug": "venn", "title": B("Venn diagrams", "ভেন চিত্ৰ"), "reign": B("Regions, relations, counting, three sets", "অংশ, সম্পৰ্ক, গণনা, তিনিটা সংহতি"), "units": [u1, u2, u3, u4], "test": test}
