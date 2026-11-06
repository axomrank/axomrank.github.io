"""Lesson 1: Alphabet tools."""
from math_kit import B, explore, match, mcq, odd, order, part, solve, stepwise, tf, unit
from math_lessons_c import diagram, lab
from math_labs import task
from reason_kit import AZ, ORD, same

POS = "r-pos"; OPP = "r-opp"; COUNT = "r-lcount"; DICT = "r-dict"; LOGIC = "r-logorder"; WORD = "r-wordform"
SKILLS = {POS: ("alphabet", B("Letter positions", "আখৰৰ স্থান"), []), OPP: ("alphabet", B("Opposite letters", "বিপৰীত আখৰ"), [POS]), COUNT: ("alphabet", B("Count within the alphabet", "বৰ্ণমালাত গণনা"), [POS]),
          DICT: ("alphabet", B("Dictionary order", "অভিধানৰ ক্ৰম"), []), LOGIC: ("alphabet", B("Logical order of words", "শব্দৰ যুক্তিসংগত ক্ৰম"), []), WORD: ("alphabet", B("Words from letters", "আখৰৰ পৰা শব্দ"), [])}
TAGS = {"r-m-oppsum": (OPP, B("Forgetting opposites add to 27", "বিপৰীতৰ যোগফল 27 পাহৰা")), "r-m-sideflip": (COUNT, B("Counting left when asked for right", "সোঁফালৰ সলনি বাওঁফালে গণা")), "r-m-firstonly": (DICT, B("Comparing only the first letter", "কেৱল প্ৰথম আখৰ তুলনা"))}
OPPW = B("Opposites add to 27. Subtract the place from 27.", "বিপৰীত আখৰৰ যোগফল 27। 27 ৰ পৰা স্থান বিয়োগ কৰা।")
SIDE = B("Left means earlier in the alphabet, and right means later.", "বাওঁ মানে বৰ্ণমালাৰ আগলৈ, সোঁ মানে পিছলৈ।")
FIRST = B("When the first letters match, compare the next letters.", "প্ৰথম আখৰ একে হ'লে পিছৰ আখৰ তুলনা কৰা।")


def letters(sid, skill, fn, params, **extra):
    return solve(sid, skill, fn, params, input="letters", **extra)


def p_of(c):
    return AZ.index(c) + 1


def pick_place(n):
    return {"q": B(f"Tap the {ORD[n]} letter of the alphabet.", f"বৰ্ণমালাৰ {n} নম্বৰ আখৰটো টিপা।"), "widget": {"kind": "alpha"}, "target": n, "answerText": same(AZ[n - 1]), "why": B(f"Count from the nearest anchor to reach {AZ[n - 1]}.", f"ওচৰৰ ভেটিৰ পৰা গণিলে {AZ[n - 1]} পোৱা যায়।")}


def place_of(c):
    return {"q": B(f"What is the place of {c} in the alphabet?", f"বৰ্ণমালাত {c} ৰ স্থান কিমান?"), "answer": str(p_of(c)), "why": B(f"{c} is letter number {p_of(c)}.", f"{c} {p_of(c)} নম্বৰ আখৰ।")}


def pick_opp(c):
    o = AZ[26 - p_of(c)]
    return {"q": B(f"Tap the opposite of {c}.", f"{c} ৰ বিপৰীত আখৰটো টিপা।"), "widget": {"kind": "alpha", "fold": True}, "target": p_of(o), "answerText": same(o), "traps": [{"val": p_of(c), "tag": "r-m-oppsum", "why": OPPW}], "why": B(f"{p_of(c)} + {p_of(o)} = 27.", f"{p_of(c)} + {p_of(o)} = 27।")}


def opp_letter(c):
    o = AZ[26 - p_of(c)]
    return {"q": B(f"Which letter is opposite {c}?", f"{c} ৰ বিপৰীত কোন আখৰ?"), "answer": o, "why": B(f"27 − {p_of(c)} = {p_of(o)}, which is {o}.", f"27 − {p_of(c)} = {p_of(o)}, অৰ্থাৎ {o}।")}


def opp_word(w):
    a = "".join(AZ[26 - p_of(c)] for c in w)
    return {"q": B(f"Replace each letter of {w} with its opposite.", f"{w} ৰ প্ৰতিটো আখৰ বিপৰীত আখৰেৰে সলনি কৰা।"), "answer": a, "why": B(f"{w} → {a}, with each pair adding to 27.", f"{w} → {a}, প্ৰতিটো যোৰৰ যোগফল 27।")}


def from_right(n):
    p = 27 - n
    return {"q": B(f"Which is the {ORD[n]} letter from the right end of the alphabet?", f"বৰ্ণমালাৰ সোঁ মূৰৰ পৰা {n} নম্বৰ আখৰ কোনটো?"), "answer": AZ[p - 1], "why": B(f"27 − {n} = {p}, which is {AZ[p - 1]}.", f"27 − {n} = {p}, অৰ্থাৎ {AZ[p - 1]}।"), "traps": [{"ans": AZ[n - 1], "tag": "r-m-sideflip", "why": SIDE}]}


def left_of(n, k):
    a = 27 - n
    return {"q": B(f"Find the {ORD[n]} letter from the right. Which letter is {k} places to its left?", f"সোঁফালৰ পৰা {n} নম্বৰ আখৰ উলিওৱা। তাৰ {k} ঘৰ বাওঁফালে কোন আখৰ?"), "answer": AZ[a - k - 1], "why": B(f"The letter is at {a}. Going left: {a} − {k} = {a - k}, which is {AZ[a - k - 1]}.", f"আখৰটো {a} ত। বাওঁফালে: {a} − {k} = {a - k}, অৰ্থাৎ {AZ[a - k - 1]}।"), "traps": [{"ans": AZ[a + k - 1], "tag": "r-m-sideflip", "why": SIDE}]}


def steps_lr(n, k):
    s = "rs1.u3.q3"
    a = n + k
    return {"q": B(f"Which letter is {k} places to the right of the {ORD[n]} letter?", f"{n} নম্বৰ আখৰৰ {k} ঘৰ সোঁফালে কোন আখৰ?"), "parts": [
        part(B("Right means?", "সোঁ মানে?"), B("Add", "যোগ"), [B("Subtract", "বিয়োগ"), B("Start from Z", "Z ৰ পৰা আৰম্ভ")], SIDE, tag="r-m-sideflip", sid=s),
        part(B("New place?", "নতুন স্থান?"), same(a), [same(n - k), same(n)], B(f"{n} + {k} = {a}.", f"{n} + {k} = {a}।"), sid=s),
        part(B("Letter?", "আখৰ?"), same(AZ[a - 1]), [same(AZ[a]), same(AZ[a - 2])], B("Use the nearest anchor to read it.", "ওচৰৰ ভেটিৰ পৰা পঢ়া।"), sid=s),
    ], "why": B(f"The answer is {AZ[a - 1]}.", f"উত্তৰ {AZ[a - 1]}।")}


def first_word(words):
    best = sorted(words)[0]
    return {"q": B("Which word comes first in a dictionary?", "অভিধানত কোন শব্দ প্ৰথমে আহে?"), "right": best, "wrong": [(sorted(words)[-1], "r-m-firstonly", FIRST)], "fill": sorted(words)[1:], "why": B(f"Compare letter by letter: {best} comes first.", f"আখৰে আখৰে তুলনা কৰিলে {best} প্ৰথম।")}


def compare_steps(a, b):
    s = "rs1.u4.q1"
    i = next(k for k, (x, y) in enumerate(zip(a, b)) if x != y)
    first = min(a, b)
    return {"q": B(f"Which comes first, {a} or {b}?", f"{a} আৰু {b} ৰ ভিতৰত কোনটো আগতে?"), "parts": [
        part(B("First place where they differ?", "প্ৰথম ক'ত বেলেগ?"), same(f"{ORD[i + 1]} letter"), [same(f"{ORD[i + 2]} letter"), same("1st letter" if i else "2nd letter")], FIRST, tag="r-m-firstonly", sid=s),
        part(B("So which comes first?", "তেন্তে কোনটো আগতে?"), same(first), [same(max(a, b)), B("They tie", "সমান")], B(f"{a[i]} and {b[i]} decide it.", f"{a[i]} আৰু {b[i]} এ ঠিক কৰে।"), sid=s),
    ], "why": B(f"{first} comes first.", f"{first} আগতে।")}


def dict_order(words):
    return sorted(words)


def lesson():
    p = "rs1"
    u1 = unit("u1", B("Every letter has an address", "প্ৰতিটো আখৰৰ ঠিকনা"), "star", [B("A is 1 and Z is 26.", "A 1, Z 26।"), B("E, J, O, T and Y are 5, 10, 15, 20 and 25.", "E, J, O, T, Y হ'ল 5, 10, 15, 20, 25।"), B("Count from the nearest anchor.", "ওচৰৰ ভেটিৰ পৰা গণা।"), B("M is 13, the end of the first half.", "M 13, প্ৰথম আধাৰ শেষ।")], [
        lab(f"{p}.u1.s1", B("Five anchors do the work", "পাঁচটা ভেটিয়েই যথেষ্ট"), B("Nobody counts from A. Learn every fifth letter, then step from the nearest one.", "A ৰ পৰা কোনেও নগণে। প্ৰতি পঞ্চম আখৰ মনত ৰাখি ওচৰৰটোৰ পৰা গণা।"), {"kind": "alpha", "nums": True}, [
            task(B("Tap the 10th letter.", "10 নম্বৰ আখৰ টিপা।"), {"pick": 10}, B("J is 10. It is one of your anchors.", "J 10। ই এটা ভেটি।")),
            task(B("Tap the 20th letter.", "20 নম্বৰ আখৰ টিপা।"), {"pick": 20}, B("T is 20. Now 18 is just two back: R.", "T 20। এতিয়া 18 মানে দুই ঘৰ পিছ: R।")),
        ]),
        diagram(f"{p}.u1.s2", B("A line to remember them", "মনত ৰখাৰ শাৰী"), [B("Say EJOTY aloud. Each letter is five places after the last.", "EJOTY মাতি কোৱা। প্ৰতিটো আখৰ আগৰটোৰ পাঁচ ঘৰ পিছত।")], "flow", [B("E 5", "E 5"), B("J 10", "J 10"), B("O 15", "O 15"), B("T 20", "T 20")]),
        explore(f"{p}.u1.q1", POS, pick_place, [(7,), (12,), (18,), (23,)]),
        solve(f"{p}.u1.q2", POS, place_of, [("H",), ("L",), ("Q",), ("V",)]),
        match(f"{p}.u1.q3", POS, B("Match the letter to its place", "আখৰক স্থানৰ লগত মিলোৱা"), [[same(c), same(p_of(c))] for c in "EJOT"], B("These are the anchors.", "এইবোৰ ভেটি।")),
        tf(f"{p}.u1.q4", POS, B("M is the 13th letter.", "M 13 নম্বৰ আখৰ।"), True, B("It ends the first half.", "ই প্ৰথম আধাৰ শেষ।")),
        order(f"{p}.u1.q5", POS, B("Put the letters in alphabet order", "আখৰবোৰ বৰ্ণমালাৰ ক্ৰমে সজোৱা"), [same(c) for c in "CKPW"], B("Lower place first.", "কম স্থান আগতে।")),
    ])
    u2 = unit("u2", B("Letters come in opposite pairs", "বিপৰীত আখৰৰ যোৰ"), "star", [B("Fold the alphabet and A meets Z.", "বৰ্ণমালা ভাঁজ কৰিলে A আৰু Z লগ লাগে।"), B("Opposite pairs add to 27.", "বিপৰীত যোৰৰ যোগফল 27।"), B("M and N meet in the middle.", "M আৰু N মাজত লগ লাগে।"), B("The opposite of the opposite is the same letter.", "বিপৰীতৰ বিপৰীত একেটা আখৰ।")], [
        lab(f"{p}.u2.s1", B("Fold the alphabet in half", "বৰ্ণমালা আধা ভাঁজ কৰা"), B("Here the second row runs backward, so each letter sits above its opposite.", "ইয়াত দ্বিতীয় শাৰী ওলোটা, সেয়ে প্ৰতিটো আখৰৰ তলত তাৰ বিপৰীত।"), {"kind": "alpha", "fold": True, "nums": True}, [
            task(B("Tap Z.", "Z টিপা।"), {"pick": 26}, B("Z sits below A: 1 + 26 = 27.", "Z, A ৰ তলত: 1 + 26 = 27।")),
            task(B("Tap T.", "T টিপা।"), {"pick": 20}, B("G is above it: 7 + 20 = 27.", "ওপৰত G: 7 + 20 = 27।")),
        ]),
        diagram(f"{p}.u2.s2", B("One sum replaces the counting", "এটা যোগেই যথেষ্ট"), [B("Find the place, subtract it from 27, and read the letter.", "স্থান উলিয়াই 27 ৰ পৰা বিয়োগ কৰা, তাৰ পিছত আখৰ পঢ়া।")], "flow", [B("Place of D = 4", "D ৰ স্থান = 4"), B("27 − 4 = 23", "27 − 4 = 23"), B("23 is W", "23 মানে W")]),
        explore(f"{p}.u2.q1", OPP, pick_opp, [("D",), ("K",), ("R",)]),
        letters(f"{p}.u2.q2", OPP, opp_letter, [("B",), ("H",), ("S",), ("V",)]),
        letters(f"{p}.u2.q3", OPP, opp_word, [("BAG",), ("HOT",), ("SKY",)]),
        tf(f"{p}.u2.q4", OPP, B("The opposite of L is O.", "L ৰ বিপৰীত O।"), True, B("12 + 15 = 27.", "12 + 15 = 27।"), ("r-m-oppsum", OPPW)),
        match(f"{p}.u2.q5", OPP, B("Match the opposites", "বিপৰীত আখৰ মিলোৱা"), [[same(c), same(AZ[26 - p_of(c)])] for c in "AGMQ"], B("Each pair adds to 27.", "প্ৰতিটো যোৰৰ যোগফল 27।")),
    ])
    u3 = unit("u3", B("Left, right and from the end", "বাওঁ, সোঁ আৰু শেষৰ পৰা"), "star", [B("From the right, place = 27 − n.", "সোঁফালৰ পৰা, স্থান = 27 − n।"), B("Left of a letter means subtract.", "আখৰৰ বাওঁফাল মানে বিয়োগ।"), B("Right of a letter means add.", "আখৰৰ সোঁফাল মানে যোগ।"), B("Change everything to places first.", "প্ৰথমে সকলো স্থানলৈ সলনি কৰা।")], [
        diagram(f"{p}.u3.s1", B("Turn words into sums", "শব্দক অংকলৈ আনা"), [B("Long wording hides short sums. Convert to a place, then add or subtract.", "দীঘল ভাষাৰ আঁৰত চুটি অংক। স্থানলৈ আনি যোগ বা বিয়োগ কৰা।")], "flow", [B("Find the place", "স্থান উলিওৱা"), B("Add or subtract", "যোগ বা বিয়োগ"), B("Read the letter", "আখৰ পঢ়া")]),
        diagram(f"{p}.u3.s2", B("From the right end", "সোঁ মূৰৰ পৰা"), [B("The 1st from the right is Z, at place 26. So the n-th from the right is 27 − n.", "সোঁফালৰ পৰা প্ৰথম Z, স্থান 26। সেয়ে n নম্বৰ মানে 27 − n।")], "grid", [B("1st from right: Z", "সোঁফালৰ ১ম: Z"), B("5th from right: V", "সোঁফালৰ ৫ম: V"), B("10th from right: Q", "সোঁফালৰ ১০ম: Q")]),
        letters(f"{p}.u3.q1", COUNT, from_right, [(3,), (8,), (14,), (20,)]),
        letters(f"{p}.u3.q2", COUNT, left_of, [(9, 5), (12, 3), (10, 6)]),
        stepwise(f"{p}.u3.q3", COUNT, steps_lr, [(6, 8), (11, 5), (3, 13)]),
        tf(f"{p}.u3.q4", COUNT, B("The letter 3 places to the left of K is H.", "K ৰ 3 ঘৰ বাওঁফালে H।"), True, B("11 − 3 = 8.", "11 − 3 = 8।"), ("r-m-sideflip", SIDE)),
        order(f"{p}.u3.q5", COUNT, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the instruction", "নিৰ্দেশ পঢ়া"), B("Find the place", "স্থান উলিওৱা"), B("Add or subtract", "যোগ বা বিয়োগ"), B("Read the letter", "আখৰ পঢ়া")], B("Words, place, sum, letter.", "শব্দ, স্থান, অংক, আখৰ।")),
    ])
    u4 = unit("u4", B("Dictionary order", "অভিধানৰ ক্ৰম"), "star", [B("Compare the first letters.", "প্ৰথম আখৰ তুলনা কৰা।"), B("If they match, compare the second letters.", "একে হ'লে দ্বিতীয় আখৰ তুলনা কৰা।"), B("Keep going until two letters differ.", "বেলেগ নোহোৱালৈ আগবাঢ়া।"), B("A shorter word that matches comes first.", "একে আৰম্ভণিৰ চুটি শব্দ আগতে।")], [
        diagram(f"{p}.u4.s1", B("Letter by letter", "আখৰে আখৰে"), [B("The first difference decides the order. Everything after it does not matter.", "প্ৰথম পাৰ্থক্যই ক্ৰম ঠিক কৰে। তাৰ পিছৰখিনিৰ মূল্য নাই।")], "flow", [B("TEACH", "TEACH"), B("TEAM", "TEAM"), B("C before M", "M ৰ আগত C")]),
        diagram(f"{p}.u4.s2", B("Short words come first", "চুটি শব্দ আগতে"), [B("BOOK comes before BOOKS, because nothing comes before something.", "BOOK, BOOKS ৰ আগত, কাৰণ একো নথকাটো আগত।")], "flow", [B("BOOK", "BOOK"), B("BOOKS", "BOOKS"), B("BOOKSHOP", "BOOKSHOP")]),
        stepwise(f"{p}.u4.q1", DICT, compare_steps, [("PLANT", "PLATE"), ("STONE", "STORE"), ("BREAD", "BRICK")]),
        order(f"{p}.u4.q2", DICT, B("Put the words in dictionary order", "শব্দবোৰ অভিধানৰ ক্ৰমে সজোৱা"), [same(w) for w in dict_order(["MANGO", "MANNER", "MAPLE", "MARKET"])], B("The third letters decide it: N, N, P, R.", "তৃতীয় আখৰে ঠিক কৰে: N, N, P, R।")),
        order(f"{p}.u4.q3", DICT, B("Put these in dictionary order", "এইবোৰ অভিধানৰ ক্ৰমে সজোৱা"), [same(w) for w in dict_order(["RIVER", "RIVERS", "RIVET", "ROAD"])], B("RIVER is a shorter match, so it leads.", "RIVER চুটি, সেয়ে আগত।")),
        tf(f"{p}.u4.q4", DICT, B("CART comes before CARD in a dictionary.", "অভিধানত CARD ৰ আগত CART।"), False, B("D comes before T.", "T ৰ আগত D।"), ("r-m-firstonly", FIRST)),
        tf(f"{p}.u4.q5", DICT, B("PEN comes before PENCIL.", "PENCIL ৰ আগত PEN।"), True, B("The shorter match comes first.", "চুটি শব্দ আগতে।")),
        match(f"{p}.u4.q6", DICT, B("Match the pair to the deciding letters", "যোৰক ঠিক কৰা আখৰৰ লগত মিলোৱা"), [[B("FARM, FAST", "FARM, FAST"), B("R before S", "S ৰ আগত R")], [B("GOAT, GOLD", "GOAT, GOLD"), B("A before L", "L ৰ আগত A")], [B("HILL, HOLE", "HILL, HOLE"), B("I before O", "O ৰ আগত I")]], B("The first different letters decide.", "প্ৰথম বেলেগ আখৰে ঠিক কৰে।")),
    ])
    u5 = unit("u5", B("Logical order of words", "শব্দৰ যুক্তিসংগত ক্ৰম"), "star", [B("Find the kind of order first.", "প্ৰথমে কেনে ক্ৰম চোৱা।"), B("Size runs small to large.", "আকাৰ সৰুৰ পৰা ডাঙৰলৈ।"), B("Process runs first step to last.", "প্ৰক্ৰিয়া প্ৰথমৰ পৰা শেষলৈ।"), B("Life runs from birth onward.", "জীৱন জন্মৰ পৰা আগবাঢ়ে।")], [
        diagram(f"{p}.u5.s1", B("Ask what is growing", "কি বাঢ়িছে সোধা"), [B("These lists follow life, not the alphabet. Name what changes from word to word.", "এই তালিকা বৰ্ণমালাৰ দৰে নহয়, জীৱনৰ দৰে। শব্দে শব্দে কি সলনি হয় কোৱা।")], "grid", [B("Size: room, house, village", "আকাৰ: কোঠা, ঘৰ, গাঁও"), B("Process: seed, plant, fruit", "প্ৰক্ৰিয়া: বীজ, গছ, ফল"), B("Age: child, youth, elder", "বয়স: শিশু, যুৱক, বৃদ্ধ")]),
        diagram(f"{p}.u5.s2", B("Fix the two ends", "দুই মূৰ ঠিক কৰা"), [B("Pick the first and last words. The middle usually falls into place.", "প্ৰথম আৰু শেষ শব্দ বাছা। মাজখিনি সাধাৰণতে নিজে মিলে।")], "flow", [B("First word", "প্ৰথম শব্দ"), B("Last word", "শেষ শব্দ"), B("The middle", "মাজখিনি")]),
        order(f"{p}.u5.q1", LOGIC, B("Smallest to largest", "সৰুৰ পৰা ডাঙৰলৈ"), [B("Village", "গাঁও"), B("District", "জিলা"), B("State", "ৰাজ্য"), B("Country", "দেশ")], B("Each contains the one before.", "প্ৰতিটোৱে আগৰটোক সামৰে।")),
        order(f"{p}.u5.q2", LOGIC, B("Put the steps of making tea in order", "চাহ বনোৱাৰ খোজ ক্ৰমে সজোৱা"), [B("Boil water", "পানী উতলোৱা"), B("Add leaves", "পাত দিয়া"), B("Strain", "ছেকা"), B("Serve", "পৰিবেশন")], B("Each step needs the one before.", "প্ৰতিটো খোজৰ বাবে আগৰটো লাগে।")),
        match(f"{p}.u5.q3", LOGIC, B("Match the list to its order", "তালিকাক ক্ৰমৰ লগত মিলোৱা"), [[B("Seed, plant, tree", "বীজ, গছপুলি, গছ"), B("Growth", "বৃদ্ধি")], [B("Page, book, library", "পৃষ্ঠা, কিতাপ, পুথিভঁৰাল"), B("Size", "আকাৰ")], [B("Morning, noon, night", "ৰাতিপুৱা, দুপৰীয়া, ৰাতি"), B("Time", "সময়")]], B("Name what changes.", "কি সলনি হয় কোৱা।")),
        tf(f"{p}.u5.q4", LOGIC, B("In a logical order question, alphabetical order decides the answer.", "যুক্তিসংগত ক্ৰমৰ প্ৰশ্নত বৰ্ণমালাৰ ক্ৰমে উত্তৰ ঠিক কৰে।"), False, B("Meaning decides it.", "অৰ্থই ঠিক কৰে।")),
        odd(f"{p}.u5.q5", LOGIC, lambda a, b, c, d: {"q": B("Which does not belong in this sequence?", "এই ক্ৰমত কোনটো নিমিলে?"), "right": d, "fill": [a, b, c], "why": B(f"{d} is not a stage of the others.", f"{d} বাকীবোৰৰ ধাপ নহয়।")}, [("Egg", "Chick", "Hen", "Stone"), ("Seed", "Shoot", "Flower", "Chair")]),
    ])
    u6 = unit("u6", B("Words inside words", "শব্দৰ ভিতৰত শব্দ"), "star", [B("Count each letter in the long word.", "দীঘল শব্দৰ প্ৰতিটো আখৰ গণা।"), B("A new word can use a letter only as often as it appears.", "নতুন শব্দত আখৰ যিমানবাৰ আছে সিমানেই ব্যৱহাৰ।"), B("Test each option letter by letter.", "প্ৰতিটো বিকল্প আখৰে আখৰে পৰীক্ষা কৰা।"), B("One missing letter rules a word out.", "এটা আখৰ নাথাকিলেই শব্দ বাদ।")], [
        diagram(f"{p}.u6.s1", B("The letters are your budget", "আখৰবোৰেই তোমাৰ পুঁজি"), [B("Think of the long word as stock. Every letter you use must be in stock.", "দীঘল শব্দক ভঁৰাল বুলি ভাবা। ব্যৱহাৰ কৰা আখৰ ভঁৰালত থাকিব লাগিব।")], "flow", [B("List the stock", "ভঁৰাল লিখা"), B("Spend each letter", "আখৰ খৰচ"), B("Out of stock? No", "নাই? নহয়")]),
        diagram(f"{p}.u6.s2", B("Watch double letters", "দুবাৰৰ আখৰ চোৱা"), [B("TEACHER has one A, so AREA cannot be made even though A appears there.", "TEACHER ত এটা A, সেয়ে AREA বনাব নোৱাৰি।")], "flow", [B("TEACHER", "TEACHER"), B("One A", "এটা A"), B("AREA needs two", "AREA ত দুটা")]),
        odd(f"{p}.u6.q1", WORD, lambda w, a, b, c, bad: {"q": B(f"Which word cannot be made from the letters of {w}?", f"{w} ৰ আখৰেৰে কোন শব্দ বনাব নোৱাৰি?"), "right": bad, "fill": [a, b, c], "why": B(f"{bad} needs a letter that {w} lacks.", f"{bad} ত {w} ত নথকা আখৰ লাগে।")}, [("GARDEN", "RANGE", "GRADE", "DEAN", "GREEN"), ("STATION", "TOAST", "SAINT", "STAIN", "TRAIN"), ("MOUNTAIN", "MAIN", "AUNT", "UNIT", "MOTHER")]),
        tf(f"{p}.u6.q2", WORD, B("LETTER can be made from RETAIL.", "RETAIL ৰ আখৰেৰে LETTER বনাব পাৰি।"), False, B("LETTER needs two T's and two E's.", "LETTER ত দুটা T আৰু দুটা E লাগে।")),
        match(f"{p}.u6.q3", WORD, B("Match the word to its count of E", "শব্দক E ৰ সংখ্যাৰ লগত মিলোৱা"), [[B("TREE", "TREE"), same(2)], [B("TEA", "TEA"), same(1)], [B("LEVEE", "LEVEE"), same(3)]], B("Count each one.", "প্ৰতিটো গণা।")),
        solve(f"{p}.u6.q4", WORD, lambda w, c: {"q": B(f"How many times does {c} appear in {w}?", f"{w} ত {c} কিমানবাৰ আছে?"), "answer": str(w.count(c)), "why": B(f"{c} appears {w.count(c)} times.", f"{c} {w.count(c)} বাৰ আছে।")}, [("BANANA", "A"), ("ASSAM", "S"), ("COMMITTEE", "T")]),
        order(f"{p}.u6.q5", WORD, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the long word", "দীঘল শব্দ পঢ়া"), B("Take one option", "এটা বিকল্প লোৱা"), B("Tick off its letters", "আখৰ চিন দিয়া"), B("Reject on any miss", "নাথাকিলে বাদ")], B("Tick letters off one at a time.", "এটা এটাকৈ আখৰ চিন দিয়া।")),
    ])
    test = {"id": "test", "title": B("Alphabet test", "বৰ্ণমালাৰ পৰীক্ষা"), "steps": [
        solve(f"{p}.t.q1", POS, place_of, [("N",), ("U",), ("G",)]),
        letters(f"{p}.t.q2", OPP, opp_letter, [("C",), ("P",), ("X",)]),
        letters(f"{p}.t.q3", COUNT, from_right, [(5,), (11,), (17,)]),
        mcq(f"{p}.t.q4", DICT, first_word, [(("CLOUD", "CLOTH", "CLOCK", "CLOSE"),), (("GRAIN", "GRASS", "GRAPE", "GRADE"),)]),
        tf(f"{p}.t.q5", WORD, B("RANGE can be made from GARDEN.", "GARDEN ৰ আখৰেৰে RANGE বনাব পাৰি।"), True, B("All five letters are in stock.", "পাঁচোটা আখৰেই আছে।")),
        tf(f"{p}.t.q6", LOGIC, B("Page, chapter, book runs from small to large.", "পৃষ্ঠা, অধ্যায়, কিতাপ সৰুৰ পৰা ডাঙৰলৈ।"), True, B("Each contains the one before.", "প্ৰতিটোৱে আগৰটোক সামৰে।")),
    ]}
    return {"id": "rs-01-alphabet", "no": 1, "slug": "alphabet", "title": B("Alphabet tools", "বৰ্ণমালাৰ কৌশল"), "reign": B("Positions, opposites, dictionary order", "স্থান, বিপৰীত, অভিধানৰ ক্ৰম"), "units": [u1, u2, u3, u4, u5, u6], "test": test}
