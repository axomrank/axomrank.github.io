"""Lesson 6: Coding and decoding."""
from math_kit import B, match, mcq, order, part, solve, stepwise, tf, unit, with_variants
from math_lessons_c import diagram, lab
from math_labs import task
from reason_kit import enc, enc_steps, half_swap, pair_swap, pos, rev_pos, signed, word_sum

SHIFT = "r-shift"; DECODE = "r-decode"; PATTERN = "r-pattern"; MOVE = "r-move"; VALUE = "r-value"; COMPARE = "r-compare"
BACK = B("You counted backwards. A + rule moves forward through the alphabet.", "তুমি পিছলৈ গণিলা। + নিয়মে বৰ্ণমালাত আগলৈ নিয়ে।")
ENCODED = B("You applied the rule again. To decode, undo it by counting the other way.", "তুমি নিয়মটো আকৌ প্ৰয়োগ কৰিলা। সংকেত ভাঙিবলৈ ওলোটা ফালে গণিব লাগে।")
ONE = B("You used one shift for every letter. Here each letter has its own gap.", "তুমি সকলো আখৰত একেটা স্থানান্তৰ দিলা। ইয়াত প্ৰতিটো আখৰৰ বেলেগ ব্যৱধান।")
REVERSED = B("You reversed the whole word. This rule moves letters in smaller groups.", "তুমি গোটেই শব্দটো ওলোটালা। এই নিয়মে সৰু গোটত আখৰ সলায়।")
WRONGEND = B("That is its place from A. Counting from Z gives 27 minus that place.", "সেয়া A ৰ পৰা স্থান। Z ৰ পৰা গণিলে 27 ৰ পৰা সেই স্থান বিয়োগ কৰিব লাগে।")


def letters(sid, skill, fn, params, **extra):
    return solve(sid, skill, fn, params, input="letters", **extra)


def shift_q(word, n):
    return {"q": B(f"Slide the wheel until {word} becomes {enc(word, n)}.", f"{word} ৰ পৰা {enc(word, n)} নোহোৱালৈ চকৰিটো টানা।"),
            "widget": {"kind": "shift", "word": word, "code": enc(word, n)}, "target": n, "answerText": B(f"Shift {signed(n)}", f"স্থানান্তৰ {signed(n)}"),
            "traps": [{"val": -n, "tag": "r-m-shiftback", "why": BACK}],
            "why": B(f"{word[0]} becomes {enc(word, n)[0]}, a move of {signed(n)}. Every other letter moves the same.", f"{word[0]} ৰ পৰা {enc(word, n)[0]} হৈছে, অৰ্থাৎ {signed(n)}। আন আখৰবোৰো একেদৰে যায়।")}


def forward(word, n):
    code = enc(word, n)
    return {"q": B(f"Every letter moves {n} places forward. Write the code for {word}.", f"প্ৰতিটো আখৰ {n} ঘৰ আগবাঢ়ে। {word} ৰ সংকেত লিখা।"), "answer": code,
            "why": B(f"Move each letter {n} forward: {word} → {code}.", f"প্ৰতিটো আখৰ {n} ঘৰ আগবঢ়োৱা: {word} → {code}।"),
            "traps": [{"ans": enc(word, -n), "tag": "r-m-shiftback", "why": BACK}]}


def nth(c, n):
    return {"q": B(f"Which letter comes {n} places after {c}?", f"{c} ৰ {n} ঘৰ পিছত কোন আখৰ?"), "answer": enc(c, n),
            "why": B(f"Count on {n} from {c} and you reach {enc(c, n)}.", f"{c} ৰ পৰা {n} ঘৰ গণিলে {enc(c, n)} পোৱা যায়।"),
            "traps": [{"ans": enc(c, -n), "tag": "r-m-shiftback", "why": BACK}]}


def decode(word, n):
    code = enc(word, n)
    return {"q": B(f"The rule was {signed(n)}. The code reads {code}. What was the word?", f"নিয়ম আছিল {signed(n)}। সংকেতটো {code}। মূল শব্দটো কি আছিল?"), "answer": word,
            "why": B(f"Undo {signed(n)} by moving each letter {n} back: {code} → {word}.", f"{signed(n)} উভতাবলৈ প্ৰতিটো আখৰ {n} ঘৰ পিছুৱাই আনা: {code} → {word}।"),
            "traps": [{"ans": enc(word, 2 * n), "tag": "r-m-encode", "why": ENCODED}]}


def wrap(word, n):
    code = enc(word, n)
    return {"q": B(f"Use the ring: after Z comes A. Move every letter of {word} forward {n}.", f"চক্ৰ মনত ৰাখা: Z ৰ পিছত A। {word} ৰ প্ৰতিটো আখৰ {n} ঘৰ আগবঢ়োৱা।"), "answer": code,
            "why": B(f"Letters near Z pass round to the start: {word} → {code}.", f"Z ৰ ওচৰৰ আখৰ আকৌ আৰম্ভণিলৈ যায়: {word} → {code}।"),
            "traps": [{"ans": enc(word, -n), "tag": "r-m-shiftback", "why": BACK}]}


def decode_steps(word, n):
    code = enc(word, n)
    s = "rs6.u2.q1"
    return {"q": B(f"{word[0]} is written as {code[0]}. Find what {code} stands for.", f"{word[0]} ক {code[0]} ৰূপে লিখা হৈছে। {code} ৰ অৰ্থ উলিওৱা।"), "parts": [
        part(B("What is the rule?", "নিয়মটো কি?"), B(signed(n), signed(n)), [B(signed(-n), signed(-n)), B(signed(n + 1), signed(n + 1))], B(f"{word[0]} to {code[0]} is {signed(n)}.", f"{word[0]} ৰ পৰা {code[0]} মানে {signed(n)}।"), sid=s),
        part(B("Which way do you count to decode?", "সংকেত ভাঙিবলৈ কোন ফালে গণিবা?"), B("Backwards", "পিছলৈ"), [B("Forwards", "আগলৈ"), B("It does not matter", "একো নহয়")], B("Decoding undoes the rule.", "সংকেত ভঙা মানে নিয়মটো উভতাই আনা।"), tag="r-m-encode", sid=s),
        part(B("What is the word?", "শব্দটো কি?"), B(word, word), [B(enc(word, 2 * n), enc(word, 2 * n)), B(code, code)], B(f"Each letter moves {n} back.", f"প্ৰতিটো আখৰ {n} ঘৰ পিছুৱায়।"), sid=s),
    ], "why": B(f"The rule {signed(n)} undone gives {word}.", f"{signed(n)} নিয়ম উভতালে {word} পোৱা যায়।")}


def alternate(word, a, b):
    code = enc_steps(word, [a, b])
    return {"q": B(f"Letters take turns: {signed(a)}, then {signed(b)}, and so on. Write the code for {word}.", f"আখৰবোৰে পাল পাতি লয়: {signed(a)}, তাৰ পিছত {signed(b)}, এনেদৰে। {word} ৰ সংকেত লিখা।"), "answer": code,
            "why": B(f"Apply the two gaps in turn: {word} → {code}.", f"দুটা ব্যৱধান পাল পাতি দিয়া: {word} → {code}।"),
            "traps": [{"ans": enc(word, a), "tag": "r-m-oneshift", "why": ONE}]}


def growing(word, start):
    gaps = [start + i for i in range(len(word))]
    code = enc_steps(word, gaps)
    return {"q": B(f"The gaps grow: {signed(gaps[0])}, {signed(gaps[1])}, {signed(gaps[2])} and so on. Write the code for {word}.", f"ব্যৱধান বাঢ়ে: {signed(gaps[0])}, {signed(gaps[1])}, {signed(gaps[2])}, এনেদৰে। {word} ৰ সংকেত লিখা।"), "answer": code,
            "why": B(f"Give each letter the next gap: {word} → {code}.", f"প্ৰতিটো আখৰক পিছৰ ব্যৱধান দিয়া: {word} → {code}।"),
            "traps": [{"ans": enc(word, gaps[0]), "tag": "r-m-oneshift", "why": ONE}]}


def gaps_steps(word, a, b):
    code = enc_steps(word, [a, b])
    s = "rs6.u3.q1"
    nxt = enc_steps(word, [a, b])[2]
    return {"q": B(f"{word} is coded as {code}. Find the rule, one letter at a time.", f"{word} ৰ সংকেত {code}। এটা এটাকৈ আখৰ চাই নিয়ম উলিওৱা।"), "parts": [
        part(B(f"Gap from {word[0]} to {code[0]}?", f"{word[0]} ৰ পৰা {code[0]} লৈ ব্যৱধান?"), B(signed(a), signed(a)), [B(signed(-a), signed(-a)), B(signed(a + 2), signed(a + 2))], B("Count from the plain letter to the code letter.", "মূল আখৰৰ পৰা সংকেত আখৰলৈ গণা।"), sid=s),
        part(B(f"Gap from {word[1]} to {code[1]}?", f"{word[1]} ৰ পৰা {code[1]} লৈ ব্যৱধান?"), B(signed(b), signed(b)), [B(signed(a), signed(a)), B(signed(b - 2), signed(b - 2))], B("The second gap differs, so one shift cannot explain the code.", "দ্বিতীয় ব্যৱধান বেলেগ, গতিকে এটা স্থানান্তৰেৰে নহ'ব।"), tag="r-m-oneshift", sid=s),
        part(B(f"So {word[2]} becomes?", f"তেন্তে {word[2]} কি হ'ব?"), B(nxt, nxt), [B(enc(word[2], b), enc(word[2], b)), B(enc(word[2], a + 1), enc(word[2], a + 1))], B(f"The gaps take turns, so the third letter takes {signed(a)} again.", f"ব্যৱধান পাল পাতি লয়, তৃতীয় আখৰে আকৌ {signed(a)} লয়।"), sid=s),
    ], "why": B(f"The rule alternates {signed(a)} and {signed(b)}.", f"নিয়মটো {signed(a)} আৰু {signed(b)} ৰ পাল।")}


def pairswap(word):
    return {"q": B(f"Swap each neighbouring pair of letters in {word}. Write the code.", f"{word} ৰ প্ৰতিটো কাষৰীয়া আখৰ যোৰ সলনা-সলনি কৰা। সংকেত লিখা।"), "answer": pair_swap(word),
            "why": B(f"Pair by pair: {word} → {pair_swap(word)}.", f"যোৰে যোৰে: {word} → {pair_swap(word)}।"), "traps": [{"ans": word[::-1], "tag": "r-m-order", "why": REVERSED}]}


def halves(word):
    return {"q": B(f"Split {word} into two halves and swap the halves, keeping each half's order.", f"{word} ক আধা আধি ভাগ কৰি ভাগ দুটা সলনা-সলনি কৰা। প্ৰতিটো ভাগৰ ভিতৰৰ ক্ৰম একে ৰাখা।"), "answer": half_swap(word),
            "why": B(f"{word[:len(word) // 2]} and {word[len(word) // 2:]} change places.", f"{word[:len(word) // 2]} আৰু {word[len(word) // 2:]} ঠাই সলায়।"), "traps": [{"ans": word[::-1], "tag": "r-m-order", "why": REVERSED}]}


def flip(word):
    code = word[::-1]
    return {"q": B(f"The code reverses the word. Build the code for {word}.", f"সংকেতে শব্দটো ওলোটায়। {word} ৰ সংকেত সজোৱা।"), "word": {"en": list(code), "as": list(code)},
            "why": B(f"Read {word} from its last letter: {code}.", f"{word} শেষৰ আখৰৰ পৰা পঢ়া: {code}।")}


def total(word):
    return {"q": B(f"With A = 1, B = 2 and so on, what is the sum of the letters in {word}?", f"A = 1, B = 2 এনেদৰে ধৰিলে {word} ৰ আখৰবোৰৰ যোগফল কিমান?"), "answer": str(word_sum(word)),
            "why": B(" + ".join(str(pos(c)) for c in word) + f" = {word_sum(word)}.", " + ".join(str(pos(c)) for c in word) + f" = {word_sum(word)}।")}


def from_z(c):
    return {"q": B(f"Now Z = 1, Y = 2 and so on. What number is {c}?", f"এতিয়া Z = 1, Y = 2 এনেদৰে। {c} ৰ মান কিমান?"), "answer": str(rev_pos(c)),
            "why": B(f"{c} is {pos(c)} from A, so 27 − {pos(c)} = {rev_pos(c)}.", f"A ৰ পৰা {c} {pos(c)} নম্বৰ, গতিকে 27 − {pos(c)} = {rev_pos(c)}।"),
            "traps": [{"ans": str(pos(c)), "tag": "r-m-position", "why": WRONGEND}]}


def same_rule(a, b):
    return {"q": B(f"If {a} = {word_sum(a)}, what does {b} equal by the same rule?", f"যদি {a} = {word_sum(a)}, একে নিয়মত {b} কিমান?"), "answer": str(word_sum(b)),
            "hints": [B("Try adding the place value of each letter.", "প্ৰতিটো আখৰৰ স্থানীয় মান যোগ কৰি চোৱা।")],
            "why": B(f"The rule adds letter places, so {b} = {word_sum(b)}.", f"নিয়মটোৱে আখৰৰ স্থান যোগ কৰে, গতিকে {b} = {word_sum(b)}।")}


def rule_steps(a, b):
    s = "rs6.u5.q4"
    return {"q": B(f"{a} is written as {word_sum(a)}. Find the rule, then use it on {b}.", f"{a} ক {word_sum(a)} ৰূপে লিখা হৈছে। নিয়ম উলিয়াই {b} ত প্ৰয়োগ কৰা।"), "parts": [
        part(B(f"Letter places in {a}?", f"{a} ৰ আখৰবোৰৰ স্থান?"), B(", ".join(str(pos(c)) for c in a), ", ".join(str(pos(c)) for c in a)), [B(", ".join(str(rev_pos(c)) for c in a), ", ".join(str(rev_pos(c)) for c in a)), B(", ".join(str(pos(c) + 1) for c in a), ", ".join(str(pos(c) + 1) for c in a))], B("Count each letter from A.", "প্ৰতিটো আখৰ A ৰ পৰা গণা।"), tag="r-m-position", sid=s),
        part(B("What gives the total?", "মুঠ কেনেকৈ পোৱা যায়?"), B("Adding them", "যোগ কৰি"), [B("Multiplying them", "পূৰণ কৰি"), B("Counting the letters", "আখৰ গণি")], B(f"The places add to {word_sum(a)}.", f"স্থানবোৰৰ যোগফল {word_sum(a)}।"), sid=s),
        part(B(f"So {b} is?", f"তেন্তে {b} কিমান?"), B(str(word_sum(b)), str(word_sum(b))), [B(str(word_sum(b) + 1), str(word_sum(b) + 1)), B(str(word_sum(a)), str(word_sum(a)))], B("Add the places of its letters.", "ইয়াৰ আখৰবোৰৰ স্থান যোগ কৰা।"), sid=s),
    ], "why": B("Find the rule from the example, then apply it unchanged.", "উদাহৰণৰ পৰা নিয়ম উলিয়াই একেদৰে প্ৰয়োগ কৰা।")}


# Three shared-word sentences. Words are bilingual; the coded words are made up.
def common(w1, w2, w3, w4, w5, x, a, b, c, d):
    """Sentence one: w1 w2 w3. Sentence two: w1 w4 w5. x is the code of w1."""
    s1, s2 = f"{a} {x} {b}", f"{c} {d} {x}"
    return {"q": B(f"'{s1}' means '{w1[0]} {w2[0]} {w3[0]}'. '{s2}' means '{w4[0]} {w1[0]} {w5[0]}'. Which code means '{w1[0]}'?", f"'{s1}' মানে '{w1[1]} {w2[1]} {w3[1]}'। '{s2}' মানে '{w4[1]} {w1[1]} {w5[1]}'। '{w1[1]}' ৰ সংকেত কোনটো?"), "answer": x,
            "why": B(f"'{w1[0]}' is the only shared word and {x} the only shared code.", f"'{w1[1]}' একমাত্ৰ উমৈহতীয়া শব্দ, {x} একমাত্ৰ উমৈহতীয়া সংকেত।"),
            "traps": [{"ans": a, "tag": "r-m-wordorder", "why": B("Code order need not follow word order. Compare the two sentences.", "সংকেতৰ ক্ৰম শব্দৰ ক্ৰমৰ দৰে নহ'বও পাৰে। দুটা বাক্য তুলনা কৰা।")}]}


def common_steps(w1, w2, w3, x, y, z):
    s = "rs6.u6.q2"
    return {"q": B(f"'{x} {y}' means '{w1[0]} {w2[0]}'. '{y} {z}' means '{w2[0]} {w3[0]}'. Which code means '{w3[0]}'?", f"'{x} {y}' মানে '{w1[1]} {w2[1]}'। '{y} {z}' মানে '{w2[1]} {w3[1]}'। '{w3[1]}' ৰ সংকেত কোনটো?"), "parts": [
        part(B("Which word is in both?", "দুয়োটাতে কোন শব্দ আছে?"), B(w2[0], w2[1]), [B(w1[0], w1[1]), B(w3[0], w3[1])], B("Compare the meanings first.", "প্ৰথমে অৰ্থ তুলনা কৰা।"), sid=s),
        part(B("Which code is in both?", "দুয়োটাতে কোন সংকেত আছে?"), B(y, y), [B(x, x), B(z, z)], B("The shared code belongs to the shared word.", "উমৈহতীয়া সংকেত উমৈহতীয়া শব্দৰ।"), sid=s),
        part(B(f"So '{w3[0]}' is?", f"তেন্তে '{w3[1]}' কি?"), B(z, z), [B(y, y), B(x, x)], B("It is the code left in the second sentence.", "দ্বিতীয় বাক্যত বাকী থকা সংকেতটো।"), sid=s),
    ], "why": B(f"{y} is '{w2[0]}', so the other code in that sentence, {z}, is '{w3[0]}'.", f"{y} মানে '{w2[1]}', গতিকে সেই বাক্যৰ আনটো সংকেত {z} মানে '{w3[1]}'।")}


TEA, RED, HOT, BOAT, RIVER, BIG, RICE, FISH, SMALL = ("tea", "চাহ"), ("red", "ৰঙা"), ("hot", "গৰম"), ("boat", "নাও"), ("river", "নদী"), ("big", "ডাঙৰ"), ("rice", "ভাত"), ("fish", "মাছ"), ("small", "সৰু")


def lesson():
    p = "rs6"
    u1 = unit("u1", B("Every letter moves", "প্ৰতিটো আখৰ আগবাঢ়ে"), "star", [
        B("A simple code moves every letter by the same amount.", "সৰল সংকেতে প্ৰতিটো আখৰ একে পৰিমাণে সৰায়।"),
        B("Find the rule from one letter, then test it on another.", "এটা আখৰৰ পৰা নিয়ম উলিয়াই আন এটাত পৰীক্ষা কৰা।"),
        B("+ means forward through the alphabet.", "+ মানে বৰ্ণমালাত আগলৈ।"),
        B("− means backward.", "− মানে পিছলৈ।"),
    ], [
        lab(f"{p}.u1.s1", B("A wheel that writes codes", "সংকেত লিখা চকৰি"), B("A simple code moves every letter the same distance. Slide the wheel and watch TEA change.", "সৰল সংকেতে প্ৰতিটো আখৰ একে দূৰত্ব সৰায়। চকৰিটো টানি TEA ৰ সলনি চোৱা।"), {"kind": "shift", "word": "TEA"}, [
            task(B("Slide to +1.", "+1 লৈ টানা।"), {"k": 1}, B("T became U, E became F and A became B. All moved one place.", "T ৰ পৰা U, E ৰ পৰা F, A ৰ পৰা B হ'ল। সকলো এক ঘৰ আগবাঢ়িল।")),
            task(B("Now slide to +3.", "এতিয়া +3 লৈ টানা।"), {"k": 3}, B("The word looks new, but the rule is still one number.", "শব্দটো নতুন দেখি, কিন্তু নিয়মটো এটা সংখ্যাই।")),
        ]),
        diagram(f"{p}.u1.s2", B("Find the rule from one letter", "এটা আখৰৰ পৰা নিয়ম"), [B("Count from the plain letter to the code letter. Then check a second letter before you trust it.", "মূল আখৰৰ পৰা সংকেত আখৰলৈ গণা। বিশ্বাস কৰাৰ আগতে দ্বিতীয় আখৰত পৰীক্ষা কৰা।")], "flow", [B("Plain letter", "মূল আখৰ"), B("Count the gap", "ব্যৱধান গণা"), B("Test another", "আনটোত পৰীক্ষা")]),
        with_variants({"id": f"{p}.u1.q1", "type": "explore", "skill": SHIFT}, shift_q, [("BOAT", 2), ("SILK", 3), ("RICE", 1), ("GAMOSA", 4)]),
        letters(f"{p}.u1.q2", SHIFT, forward, [("BIHU", 2), ("TEA", 3), ("DEER", 1), ("JAPI", 2)]),
        letters(f"{p}.u1.q3", SHIFT, nth, [("H", 3), ("M", 5), ("C", 4), ("Q", 2)]),
        tf(f"{p}.u1.q4", SHIFT, B("If A becomes D in a simple code, then B becomes E.", "সৰল সংকেতত A ৰ পৰা D হ'লে B ৰ পৰা E হ'ব।"), True, B("Both move +3.", "দুয়োটা +3 সৰে।")),
        match(f"{p}.u1.q5", SHIFT, B("Rule +2: match each letter to its code", "নিয়ম +2: আখৰক সংকেতৰ লগত মিলোৱা"), [[B(c, c), B(enc(c, 2), enc(c, 2))] for c in "DKPS"], B("Each letter moves two places forward.", "প্ৰতিটো আখৰ দুই ঘৰ আগবাঢ়ে।")),
    ])
    u2 = unit("u2", B("Breaking a code", "সংকেত ভঙা"), "star", [
        B("The alphabet closes into a ring: after Z comes A.", "বৰ্ণমালা এটা চক্ৰ: Z ৰ পিছত A।"),
        B("To decode, count the opposite way.", "সংকেত ভাঙিবলৈ ওলোটা ফালে গণা।"),
        B("A +3 code is undone by −3.", "+3 সংকেত −3 ৰে উভতি যায়।"),
        B("Use a second letter to confirm the rule.", "দ্বিতীয় আখৰেৰে নিয়ম নিশ্চিত কৰা।"),
    ], [
        lab(f"{p}.u2.s1", B("The alphabet is a ring", "বৰ্ণমালা এটা চক্ৰ"), B("Z has nothing after it, so the wheel closes the alphabet into a ring. Watch ZOO.", "Z ৰ পিছত একো নাই, সেয়ে চকৰিয়ে বৰ্ণমালাক চক্ৰ কৰে। ZOO চোৱা।"), {"kind": "shift", "word": "ZOO"}, [
            task(B("Slide to +1.", "+1 লৈ টানা।"), {"k": 1}, B("Z wrapped round to A, so ZOO became APP.", "Z ঘূৰি A হ'ল, ZOO ৰ পৰা APP হ'ল।")),
            task(B("Slide to −1.", "−1 লৈ টানা।"), {"k": -1}, B("Backward, A would wrap to Z in the same way.", "পিছলৈ গ'লে A একেদৰে ঘূৰি Z হ'ব।")),
        ]),
        diagram(f"{p}.u2.s2", B("Decoding runs the rule backwards", "সংকেত ভঙা মানে উভতি যোৱা"), [B("Coding and decoding are one rule, used in opposite directions.", "সংকেত দিয়া আৰু ভঙা একেটা নিয়ম, ওলোটা ফালে ব্যৱহাৰ।")], "flow", [B("Word", "শব্দ"), B("+3 makes the code", "+3 ত সংকেত"), B("−3 returns the word", "−3 ত শব্দ")]),
        stepwise(f"{p}.u2.q1", DECODE, decode_steps, [("ROOF", 2), ("GATE", 3), ("HILL", 1)]),
        letters(f"{p}.u2.q2", DECODE, decode, [("BOAT", 2), ("MILK", 3), ("FISH", 1), ("TEA", 4)]),
        letters(f"{p}.u2.q3", SHIFT, wrap, [("ZEBRA", 2), ("XRAY", 3), ("WAX", 4)]),
        order(f"{p}.u2.q4", DECODE, B("Put the decoding steps in order", "সংকেত ভঙাৰ খোজবোৰ ক্ৰমে সজোৱা"), [B("Find the gap from one known letter", "জনা আখৰৰ পৰা ব্যৱধান উলিওৱা"), B("Confirm it on a second letter", "দ্বিতীয় আখৰত নিশ্চিত কৰা"), B("Flip the rule's direction", "নিয়মৰ দিশ ওলোটোৱা"), B("Apply it to every code letter", "সকলো সংকেত আখৰত প্ৰয়োগ কৰা")], B("Find, confirm, flip, then apply.", "উলিওৱা, নিশ্চিত কৰা, ওলোটোৱা, প্ৰয়োগ কৰা।")),
        tf(f"{p}.u2.q5", DECODE, B("A code made with +4 is decoded with +4.", "+4 ৰে বনোৱা সংকেত +4 ৰেই ভাঙিব লাগে।"), False, B("It is undone with −4.", "ইয়াক −4 ৰে উভতাব লাগে।"), ("r-m-encode", ENCODED)),
    ])
    u3 = unit("u3", B("When the shift changes", "স্থানান্তৰ সলনি হ'লে"), "star", [
        B("Check at least two letters before naming a rule.", "নিয়ম কোৱাৰ আগতে কমেও দুটা আখৰ পৰীক্ষা কৰা।"),
        B("Gaps may take turns, such as +1 then −1.", "ব্যৱধানে পাল ল'ব পাৰে, যেনে +1 তাৰ পিছত −1।"),
        B("Gaps may grow, such as +1, +2, +3.", "ব্যৱধান বাঢ়িব পাৰে, যেনে +1, +2, +3।"),
        B("Write the gaps in a row and the pattern shows itself.", "ব্যৱধানবোৰ শাৰীত লিখিলে আৰ্হি ওলায়।"),
    ], [
        diagram(f"{p}.u3.s1", B("One letter can mislead you", "এটা আখৰে ভুল বুজাব পাৰে"), [B("The first gap may not be the rule. Write every gap in a row before you decide.", "প্ৰথম ব্যৱধানেই নিয়ম নহ'বও পাৰে। সিদ্ধান্তৰ আগতে সকলো ব্যৱধান শাৰীত লিখা।")], "flow", [B("Gap 1", "ব্যৱধান ১"), B("Gap 2", "ব্যৱধান ২"), B("Gap 3", "ব্যৱধান ৩"), B("The pattern", "আৰ্হি")]),
        diagram(f"{p}.u3.s2", B("Two common gap patterns", "দুটা সাধাৰণ আৰ্হি"), [B("Exams favour patterns you can see once the gaps are written down.", "ব্যৱধান লিখিলে দেখা আৰ্হিকে পৰীক্ষাত সঘনাই সোধে।")], "grid", [B("Taking turns: +1, −1, +1", "পাল: +1, −1, +1"), B("Growing: +1, +2, +3", "বৃদ্ধি: +1, +2, +3")]),
        stepwise(f"{p}.u3.q1", PATTERN, gaps_steps, [("ROOF", 1, -1), ("HILL", 2, -1), ("GATE", 2, 1)]),
        letters(f"{p}.u3.q2", PATTERN, alternate, [("JUMP", 1, -1), ("FARM", 2, -1), ("ROAD", 1, 2)]),
        letters(f"{p}.u3.q3", PATTERN, growing, [("SEED", 1), ("CORN", 1), ("LEAF", 2)]),
        with_variants({"id": f"{p}.u3.q4", "type": "odd", "skill": PATTERN}, lambda a, k, bad: {"q": B("Three pairs follow one shift. Which pair does not?", "তিনিটা যোৰে একে স্থানান্তৰ মানে। কোন যোৰে নামানে?"), **_odd(a, k, bad), "why": B(f"The others all move {signed(k)}.", f"বাকীবোৰ {signed(k)} সৰে।")}, [("CGLR", 2, "P"), ("BHKT", 3, "D"), ("DJNS", 4, "M")]),
        tf(f"{p}.u3.q5", PATTERN, B("If the first letter moves +2, every letter must move +2.", "প্ৰথম আখৰ +2 সৰিলে সকলো আখৰেই +2 সৰিব লাগে।"), False, B("Check more letters: gaps can change.", "আৰু আখৰ চোৱা: ব্যৱধান সলনি হ'ব পাৰে।"), ("r-m-oneshift", ONE)),
    ])
    u4 = unit("u4", B("Letters that change places", "ঠাই সলোৱা আখৰ"), "star", [
        B("Some codes keep the letters and only move them.", "কিছুমান সংকেতে আখৰ ৰাখি কেৱল ঠাই সলায়।"),
        B("Compare the two sets of letters first.", "প্ৰথমে দুয়োটা আখৰৰ গোট তুলনা কৰা।"),
        B("Reverse, pair swap and half swap are the usual rules.", "ওলোটা, যোৰ সলনি আৰু আধা সলনি সাধাৰণ নিয়ম।"),
        B("Test the rule on the whole word.", "নিয়মটো গোটেই শব্দত পৰীক্ষা কৰা।"),
    ], [
        diagram(f"{p}.u4.s1", B("Same letters, new order", "একে আখৰ, নতুন ক্ৰম"), [B("If the code uses exactly the word's letters, nothing shifted. Look for a movement rule.", "সংকেতত শব্দটোৰ একে আখৰ থাকিলে স্থানান্তৰ হোৱা নাই। ঠাই সলোৱা নিয়ম বিচাৰা।")], "flow", [B("Compare letters", "আখৰ তুলনা"), B("Same set?", "একে গোট?"), B("Find the movement", "ঠাই সলনি চোৱা")]),
        diagram(f"{p}.u4.s2", B("Three ways to rearrange", "সজাবলৈ তিনিটা উপায়"), [B("Each example starts from BOATS or FARM.", "প্ৰতিটো উদাহৰণ BOATS বা FARM ৰ পৰা।")], "grid", [B("Reverse: BOATS → STAOB", "ওলোটা: BOATS → STAOB"), B("Pair swap: FARM → AFMR", "যোৰ সলনি: FARM → AFMR"), B("Half swap: FARM → RMFA", "আধা সলনি: FARM → RMFA")]),
        with_variants({"id": f"{p}.u4.q1", "type": "unscramble", "skill": MOVE}, flip, [("BIHU",), ("LOTUS",), ("MAJULI",)]),
        letters(f"{p}.u4.q2", MOVE, pairswap, [("CAMEL",), ("HOUSE",), ("PLANET",)]),
        letters(f"{p}.u4.q3", MOVE, halves, [("SONG",), ("GARDEN",), ("MARKET",)]),
        match(f"{p}.u4.q4", MOVE, B("Match the rule to the example for STREAM", "STREAM ৰ বাবে নিয়মৰ লগত উদাহৰণ মিলোৱা"), [[B("Reverse", "ওলোটা"), B("MAERTS", "MAERTS")], [B("Pair swap", "যোৰ সলনি"), B(pair_swap("STREAM"), pair_swap("STREAM"))], [B("Half swap", "আধা সলনি"), B(half_swap("STREAM"), half_swap("STREAM"))]], B("Try each rule on the word and compare.", "প্ৰতিটো নিয়ম শব্দত প্ৰয়োগ কৰি তুলনা কৰা।")),
        tf(f"{p}.u4.q5", MOVE, B("A rearranged code uses exactly the same letters as the word.", "ঠাই সলোৱা সংকেতত শব্দটোৰ একে আখৰ থাকে।"), True, B("Only their order changes.", "কেৱল ক্ৰম সলনি হয়।")),
    ])
    u5 = unit("u5", B("Letters become numbers", "আখৰ সংখ্যা হয়"), "star", [
        B("A = 1 and Z = 26 give each letter a place.", "A = 1 আৰু Z = 26 এ প্ৰতিটো আখৰক স্থান দিয়ে।"),
        B("Counted from Z, a letter's value is 27 minus its place.", "Z ৰ পৰা গণিলে মান হ'ল 27 বিয়োগ স্থান।"),
        B("Number codes are often sums of letter places.", "সংখ্যা সংকেত প্ৰায়ে আখৰৰ স্থানৰ যোগফল।"),
        B("Find the rule from the example before you calculate.", "গণনাৰ আগতে উদাহৰণৰ পৰা নিয়ম উলিওৱা।"),
    ], [
        diagram(f"{p}.u5.s1", B("Letters have addresses", "আখৰৰো ঠিকনা আছে"), [B("Learn three anchors: E is 5, J is 10 and T is 20. Count from the nearest one.", "তিনিটা ভেটি মনত ৰাখা: E 5, J 10, T 20। ওচৰৰটোৰ পৰা গণা।")], "flow", [B("E = 5", "E = 5"), B("J = 10", "J = 10"), B("T = 20", "T = 20")]),
        diagram(f"{p}.u5.s2", B("Pairs that make 27", "27 হোৱা যোৰ"), [B("A and Z, B and Y, M and N: each pair adds to 27. That turns counting from Z into one subtraction.", "A আৰু Z, B আৰু Y, M আৰু N: প্ৰতিটো যোৰৰ যোগফল 27। Z ৰ পৰা গণনা এটা বিয়োগ হৈ পৰে।")], "flow", [B("A + Z = 27", "A + Z = 27"), B("B + Y = 27", "B + Y = 27"), B("M + N = 27", "M + N = 27")]),
        solve(f"{p}.u5.q1", VALUE, total, [("CAT",), ("BOAT",), ("GATE",), ("TEA",)]),
        solve(f"{p}.u5.q2", VALUE, from_z, [("C",), ("H",), ("T",), ("W",)]),
        solve(f"{p}.u5.q3", VALUE, same_rule, [("BAG", "CUP"), ("HEN", "COW"), ("SUN", "SKY")]),
        stepwise(f"{p}.u5.q4", VALUE, rule_steps, [("BED", "CAR"), ("DOG", "PEN"), ("ARM", "LEG")]),
        match(f"{p}.u5.q5", VALUE, B("Match each letter to its partner that makes 27", "যোগফল 27 হোৱা সংগী আখৰ মিলোৱা"), [[B(c, c), B(enc("A", 26 - pos(c)), enc("A", 26 - pos(c)))] for c in "ADGK"], B("Partners sit the same distance from each end.", "সংগী দুয়োটা দুই মূৰৰ পৰা একে দূৰত্বত।")),
        tf(f"{p}.u5.q6", VALUE, B("M and N are the two middle letters of the alphabet.", "M আৰু N বৰ্ণমালাৰ মাজৰ দুটা আখৰ।"), True, B("They are the 13th and 14th of 26.", "26 টাৰ ভিতৰত সিহঁত 13 আৰু 14 নম্বৰ।")),
    ])
    u6 = unit("u6", B("Coded sentences", "সংকেতৰ বাক্য"), "star", [
        B("A shared word means a shared code.", "উমৈহতীয়া শব্দ মানে উমৈহতীয়া সংকেত।"),
        B("Code order need not follow word order.", "সংকেতৰ ক্ৰম শব্দৰ ক্ৰমৰ দৰে নহ'বও পাৰে।"),
        B("Compare two sentences at a time.", "এবাৰত দুটা বাক্য তুলনা কৰা।"),
        B("What is left over belongs to the unshared word.", "বাকী থকাখিনি নিমিলা শব্দৰ।"),
    ], [
        diagram(f"{p}.u6.s1", B("Look for what is shared", "উমৈহতীয়াখিনি বিচাৰা"), [B("Here you never decode a letter. You compare two sentences and match what they share.", "ইয়াত আখৰ ভঙা নাই। দুটা বাক্য তুলনা কৰি উমৈহতীয়াখিনি মিলোৱা।")], "flow", [B("Shared word", "উমৈহতীয়া শব্দ"), B("Shared code", "উমৈহতীয়া সংকেত"), B("A match", "মিল")]),
        diagram(f"{p}.u6.s2", B("Do not trust the order", "ক্ৰমক বিশ্বাস নকৰিবা"), [B("The second code need not be the second word. Only shared items prove a match.", "দ্বিতীয় সংকেত দ্বিতীয় শব্দ নহ'বও পাৰে। উমৈহতীয়াখিনিয়েহে মিল প্ৰমাণ কৰে।")], "flow", [B("Find the pair", "যোৰ উলিওৱা"), B("Remove it", "আঁতৰোৱা"), B("Compare again", "আকৌ তুলনা")]),
        letters(f"{p}.u6.q1", COMPARE, common, [(TEA, RED, HOT, BIG, SMALL, "KO", "LI", "MU", "ZA", "PE"), (BOAT, BIG, RED, SMALL, HOT, "RA", "TU", "NI", "SO", "VE"), (RICE, HOT, SMALL, RED, BIG, "DO", "FE", "GU", "HA", "JI")]),
        stepwise(f"{p}.u6.q2", COMPARE, common_steps, [(FISH, RIVER, BOAT, "KA", "LO", "MI"), (RED, TEA, RICE, "PA", "SU", "TE"), (BIG, BOAT, FISH, "BE", "CO", "DU")]),
        match(f"{p}.u6.q3", COMPARE, B("'bo ti' means 'big river'. 'ti na' means 'river boat'. 'na ve' means 'boat fish'. Match the codes", "'bo ti' মানে 'ডাঙৰ নদী'। 'ti na' মানে 'নদী নাও'। 'na ve' মানে 'নাও মাছ'। সংকেত মিলোৱা"), [[B("big", "ডাঙৰ"), B("bo", "bo")], [B("river", "নদী"), B("ti", "ti")], [B("boat", "নাও"), B("na", "na")], [B("fish", "মাছ"), B("ve", "ve")]], B("Each shared word fixes one code, and the rest follow.", "প্ৰতিটো উমৈহতীয়া শব্দই এটা সংকেত ঠিক কৰে, বাকীবোৰ তাৰ পিছত ওলায়।")),
        tf(f"{p}.u6.q4", COMPARE, B("In a coded sentence, the first code always means the first word.", "সংকেতৰ বাক্যত প্ৰথম সংকেত সদায় প্ৰথম শব্দৰ।"), False, B("Only comparison proves a match.", "তুলনায়েহে মিল প্ৰমাণ কৰে।"), ("r-m-wordorder", B("Code order need not follow word order.", "সংকেতৰ ক্ৰম শব্দৰ ক্ৰমৰ দৰে নহ'বও পাৰে।"))),
        order(f"{p}.u6.q5", COMPARE, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find the word in both sentences", "দুয়োটা বাক্যৰ শব্দ উলিওৱা"), B("Find the code in both sentences", "দুয়োটা বাক্যৰ সংকেত উলিওৱা"), B("Pair them", "যোৰ মিলোৱা"), B("Compare what is left", "বাকীখিনি তুলনা কৰা")], B("Shared items first, then the remainder.", "প্ৰথমে উমৈহতীয়া, তাৰ পিছত বাকীখিনি।")),
    ])
    wrong = lambda word, n: [(enc(word, -n), "r-m-shiftback", BACK), (enc(word, n + 1), None, None)]
    test = {"id": "test", "title": B("Coding test", "সংকেতৰ পৰীক্ষা"), "steps": [
        mcq(f"{p}.t.q1", SHIFT, lambda w, n: {"q": B(f"Every letter moves {n} forward. What is the code for {w}?", f"প্ৰতিটো আখৰ {n} ঘৰ আগবাঢ়ে। {w} ৰ সংকেত কি?"), "right": enc(w, n), "wrong": wrong(w, n), "fill": [enc(w, n + 2), enc(w, n + 3)], "why": B(f"{w} → {enc(w, n)}.", f"{w} → {enc(w, n)}।")}, [("LAMP", 2), ("KITE", 3), ("MANGO", 1)]),
        mcq(f"{p}.t.q2", DECODE, lambda w, n: {"q": B(f"The rule was {signed(n)} and the code reads {enc(w, n)}. What was the word?", f"নিয়ম {signed(n)}, সংকেত {enc(w, n)}। মূল শব্দ কি?"), "right": w, "wrong": [(enc(w, 2 * n), "r-m-encode", ENCODED)], "fill": [enc(w, 1), enc(w, -1), enc(w, 5)], "why": B(f"Move each letter {n} back to get {w}.", f"প্ৰতিটো আখৰ {n} ঘৰ পিছুৱালে {w} পোৱা যায়।")}, [("MOON", 2), ("SHOE", 3), ("WIND", 4)]),
        mcq(f"{p}.t.q3", PATTERN, lambda w, a, b: {"q": B(f"Gaps alternate {signed(a)}, {signed(b)}. What is the code for {w}?", f"ব্যৱধান পাল পাতি {signed(a)}, {signed(b)}। {w} ৰ সংকেত কি?"), "right": enc_steps(w, [a, b]), "wrong": [(enc(w, a), "r-m-oneshift", ONE)], "fill": [enc_steps(w, [b, a]), enc(w, b), enc_steps(w, [a, a + b])], "why": B(f"Letters take the gaps in turn: {enc_steps(w, [a, b])}.", f"আখৰবোৰে পাল পাতি ব্যৱধান লয়: {enc_steps(w, [a, b])}।")}, [("GOLD", 1, -1), ("WARM", 2, -1), ("SHIP", 1, 2)]),
        mcq(f"{p}.t.q4", MOVE, lambda w: {"q": B(f"Swap each neighbouring pair. What is the code for {w}?", f"প্ৰতিটো কাষৰীয়া যোৰ সলনা-সলনি কৰা। {w} ৰ সংকেত কি?"), "right": pair_swap(w), "wrong": [(w[::-1], "r-m-order", REVERSED)], "fill": [half_swap(w), w[1:] + w[0], w[-1] + w[:-1]], "why": B(f"Pair by pair: {pair_swap(w)}.", f"যোৰে যোৰে: {pair_swap(w)}।")}, [("BRICK",), ("CLOUD",), ("FLOWER",)]),
        solve(f"{p}.t.q5", VALUE, total, [("DOOR",), ("HAND",), ("MILK",)]),
        tf(f"{p}.t.q6", COMPARE, B("If two coded sentences share one word and one code, that code is that word.", "দুটা সংকেতৰ বাক্যত এটা শব্দ আৰু এটা সংকেত উমৈহতীয়া হ'লে সেই সংকেতেই সেই শব্দ।"), True, B("That is how shared-word codes are solved.", "এনে সংকেত এইদৰেই সমাধান হয়।")),
    ]}
    return {"id": "rs-06-coding", "no": 6, "slug": "coding", "title": B("Coding and decoding", "সংকেত আৰু সংকেত ভঙা"), "reign": B("Shifts, rearranging, number and sentence codes", "স্থানান্তৰ, পুনৰ সজ্জা, সংখ্যা আৰু বাক্য সংকেত"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


def _odd(letters_, k, bad):
    """Pairs that all shift by k, with one that does not."""
    good = [f"{c} → {enc(c, k)}" for c in letters_[:3]]
    odd_one = f"{bad} → {enc(bad, k + 1)}"
    rows = good + [odd_one]
    rows.sort()
    return {"options": [B(r, r) for r in rows], "answer": rows.index(odd_one)}
