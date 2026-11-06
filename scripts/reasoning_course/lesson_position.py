"""Lessons 10 to 13: Blood relations, Ranking, Arrangements, Calendar and clocks."""
from math_kit import B, explore, match, order, part, solve, stepwise, tf, unit
from math_lessons_c import diagram, lab
from math_labs import task
from reason_kit import same

GEN = "r-bgen"; NAME = "r-bname"; GENDER = "r-bgender"; CODE = "r-bcode"
RANK = "r-rank"; TOTAL = "r-rtotal"; SWAPR = "r-rswap"; TIMEO = "r-rtime"
LINE = "r-aline"; ROUND = "r-around"; MATCHA = "r-amatch"; FIXED = "r-afixed"
ODDD = "r-codd"; CDATE = "r-cdate"; CLOCK = "r-cangle"; MEET = "r-cmeet"
SKILLS = {GEN: ("blood-relations", B("Generations", "প্ৰজন্ম"), []), NAME: ("blood-relations", B("Name the relation", "সম্পৰ্কৰ নাম"), [GEN]), GENDER: ("blood-relations", B("Stated gender only", "কোৱা লিংগহে"), []), CODE: ("blood-relations", B("Coded relations", "সংকেতৰ সম্পৰ্ক"), [NAME]),
          RANK: ("ranking", B("Ranks from both ends", "দুই মূৰৰ স্থান"), []), TOTAL: ("ranking", B("Find the total", "মুঠ উলিওৱা"), [RANK]), SWAPR: ("ranking", B("Ranks after a swap", "সলনিৰ পিছৰ স্থান"), [RANK]), TIMEO: ("ranking", B("Order by time", "সময়ৰ ক্ৰম"), []),
          LINE: ("arrangement", B("Sitting in a row", "শাৰীত বহা"), []), ROUND: ("arrangement", B("Sitting in a circle", "বৃত্তত বহা"), [LINE]), MATCHA: ("arrangement", B("Match people to things", "ব্যক্তি আৰু বস্তু মিলোৱা"), []), FIXED: ("arrangement", B("Fixed facts first", "নিশ্চিত তথ্য আগতে"), []),
          ODDD: ("calendar-clock", B("Odd days", "অতিৰিক্ত দিন"), []), CDATE: ("calendar-clock", B("Dates across years", "বছৰৰ মাজৰ তাৰিখ"), [ODDD]), CLOCK: ("calendar-clock", B("Clock angles", "ঘড়ীৰ কোণ"), []), MEET: ("calendar-clock", B("When hands meet", "কাঁটা লগ লগা সময়"), [CLOCK])}
TAGS = {"r-m-gender": (GENDER, B("Assuming gender from a name", "নামৰ পৰা লিংগ ধৰা")), "r-m-twice": (TOTAL, B("Counting the person twice", "ব্যক্তিজনক দুবাৰ গণা")), "r-m-maybe": (FIXED, B("Treating a possibility as a fact", "সম্ভাৱনাক তথ্য ধৰা")), "r-m-sidecircle": (ROUND, B("Reversing left and right in a circle", "বৃত্তত বাওঁ-সোঁ ওলোটা")), "r-m-leap": (CDATE, B("Ignoring the leap year", "অধিবৰ্ষ পাহৰা")), "r-m-hourhand": (CLOCK, B("Forgetting the hour hand moves", "ঘণ্টাৰ কাঁটা লৰে পাহৰা"))}
GEND = B("A name does not state gender. Use only what the words say.", "নামে লিংগ নকয়। শব্দই কোৱাখিনিহে ব্যৱহাৰ কৰা।")
TWICE = B("The person is counted from both ends, so subtract 1.", "ব্যক্তিজন দুয়োফালৰ পৰা গণা হৈছে, 1 বিয়োগ কৰা।")
MAYBE = B("That is possible, not certain. Keep only what must be true.", "সেয়া সম্ভৱ, নিশ্চিত নহয়। লাগিবই লগাখিনি ৰাখা।")
CIRC = B("Facing the centre, your left is clockwise.", "কেন্দ্ৰমুখী হ'লে বাওঁফাল ঘড়ীৰ দিশে।")
LEAP = B("February has 29 days in a leap year.", "অধিবৰ্ষত ফেব্ৰুৱাৰী 29 দিনৰ।")
HOUR = B("The hour hand also moves, at half a degree a minute.", "ঘণ্টাৰ কাঁটাও লৰে, মিনিটত আধা ডিগ্ৰী।")


def gen_q(q_en, q_as, gen, why):
    return {"q": B(q_en, q_as), "widget": {"kind": "tree"}, "target": gen, "answerText": B(f"{abs(gen)} generation(s) {'up' if gen > 0 else 'down'}" if gen else "Same generation", f"{abs(gen)} প্ৰজন্ম {'ওপৰত' if gen > 0 else 'তলত'}" if gen else "একে প্ৰজন্ম"), "why": why}


def rel_step(sid, q, steps, why):
    return {"q": q, "parts": [part(ask, right, wrong, note, tag=tag, sid=sid) for ask, right, wrong, note, tag in steps], "why": why}


def lesson_blood():
    p = "rs10"
    u1 = unit("u1", B("Draw the generations", "প্ৰজন্ম আঁকা"), "star", [B("Parents sit one level above you.", "পিতৃ-মাতৃ এক স্তৰ ওপৰত।"), B("Siblings sit on your level.", "ভাই-ভনী তোমাৰ স্তৰত।"), B("Children sit one level below.", "সন্তান এক স্তৰ তলত।"), B("Start from the last name and work back.", "শেষৰ নামৰ পৰা উভতি আহা।")], [
        lab(f"{p}.u1.s1", B("A family is a ladder", "পৰিয়াল এখন জখলা"), B("Every relation is a move up, down or sideways. Climb the ladder to your grandfather.", "প্ৰতিটো সম্পৰ্ক ওপৰ, তল বা কাষলৈ যোৱা। জখলাৰে ককালৈ উঠা।"), {"kind": "tree"}, [
            task(B("Go to your parents' level.", "পিতৃ-মাতৃৰ স্তৰলৈ যোৱা।"), {"gen": 1}, B("One step up.", "এক খোজ ওপৰ।")),
            task(B("Go to your grandparents' level.", "আজোককাৰ স্তৰলৈ যোৱা।"), {"gen": 2}, B("Two steps up.", "দুই খোজ ওপৰ।")),
        ]),
        diagram(f"{p}.u1.s2", B("Say it from the end", "শেষৰ পৰা কোৱা"), [B("'My father's sister's son' reads easiest backward: son, of sister, of father.", "'মোৰ দেউতাৰ ভনীয়েকৰ পুতেক' শেষৰ পৰা পঢ়াই সহজ।")], "flow", [B("My father", "মোৰ দেউতা"), B("His sister", "তেওঁৰ ভনী"), B("Her son", "তেওঁৰ পুতেক")]),
        explore(f"{p}.u1.q1", GEN, gen_q, [("Move to your mother's father.", "তোমাৰ মাকৰ দেউতাকলৈ যোৱা।", 2, B("Two levels up.", "দুই স্তৰ ওপৰ।")), ("Move to your son's son.", "তোমাৰ পুতেকৰ পুতেকলৈ যোৱা।", -2, B("Two levels down.", "দুই স্তৰ তল।")), ("Move to your father's brother.", "তোমাৰ দেউতাকৰ ককায়েকলৈ যোৱা।", 1, B("A sibling stays on the parent's level.", "ভাই-ভনী পিতৃৰ স্তৰতে।"))]),
        tf(f"{p}.u1.q2", GEN, B("Your father's sister's son is on your generation.", "তোমাৰ দেউতাকৰ ভনীয়েকৰ পুতেক তোমাৰ প্ৰজন্মৰ।"), True, B("Up one, sideways, down one.", "এক ওপৰ, কাষ, এক তল।")),
        match(f"{p}.u1.q3", GEN, B("Match the relation to the level", "সম্পৰ্কক স্তৰৰ লগত মিলোৱা"), [[B("Grandmother", "আইতা"), same("+2")], [B("Uncle", "খুড়া"), same("+1")], [B("Cousin", "সম্পৰ্কীয় ভাই"), same("0")], [B("Son", "পুতেক"), same("−1")]], B("Count the moves.", "খোজ গণা।")),
        stepwise(f"{p}.u1.q4", GEN, rel_step, [(f"{p}.u1.q4", B("Who is your mother's brother's son to you?", "তোমাৰ মাকৰ ককায়েকৰ পুতেক তোমাৰ কি?"), [(B("Your mother's brother?", "মাকৰ ককায়েক?"), B("Uncle", "মোমায়েক"), [B("Brother", "ককায়েক"), B("Father", "দেউতাক")], B("He is on the parents' level.", "তেওঁ পিতৃৰ স্তৰত।"), None), (B("His son?", "তেওঁৰ পুতেক?"), B("Cousin", "সম্পৰ্কীয় ভাই"), [B("Nephew", "ভতিজা"), B("Uncle", "খুড়া")], B("One down from the uncle.", "মোমায়েকৰ পৰা এক তল।"), None)], B("He is your cousin.", "তেওঁ সম্পৰ্কীয় ভাই।")), (f"{p}.u1.q4", B("Who is your father's father's son, if not your father?", "তোমাৰ দেউতাকৰ দেউতাকৰ পুতেক, দেউতাক নহ'লে কি?"), [(B("Your father's father?", "দেউতাকৰ দেউতাক?"), B("Grandfather", "ককা"), [B("Uncle", "খুড়া"), B("Brother", "ককায়েক")], B("Two levels up.", "দুই স্তৰ ওপৰ।"), None), (B("His other son?", "তেওঁৰ আন পুতেক?"), B("Uncle", "খুড়া"), [B("Father", "দেউতাক"), B("Cousin", "সম্পৰ্কীয় ভাই")], B("Your father's brother.", "দেউতাকৰ ভাই।"), None)], B("He is your uncle.", "তেওঁ খুড়া।"))]),
        order(f"{p}.u1.q5", GEN, B("Oldest level to youngest", "ওপৰৰ স্তৰৰ পৰা তলৰ"), [B("Grandfather", "ককা"), B("Father", "দেউতা"), B("Me", "মই"), B("Son", "পুতেক")], B("Top to bottom.", "ওপৰৰ পৰা তললৈ।")),
    ])
    u2 = unit("u2", B("Name the relation", "সম্পৰ্কৰ নাম"), "star", [B("Reduce a chain one link at a time.", "এটা এটা গাঁঠি কমোৱা।"), B("Father's brother is an uncle.", "দেউতাৰ সৰু ভাই খুড়া।"), B("Mother's brother is also an uncle.", "মাকৰ ভাই মোমাই।"), B("'Only son' means there is no other.", "'একমাত্ৰ পুত্ৰ' মানে আন নাই।")], [
        diagram(f"{p}.u2.s1", B("Shrink the chain", "শিকলি চুটি কৰা"), [B("Replace two links by one word, again and again, until one is left.", "দুটা গাঁঠিক এটা শব্দ কৰা, এটা নথকালৈ।")], "flow", [B("Father's father", "দেউতাৰ দেউতা"), B("Grandfather", "ককা"), B("Grandfather's son", "ককাৰ পুত্ৰ")]),
        diagram(f"{p}.u2.s2", B("Pointing puzzles", "আঙুলিয়াই দেখুওৱা সাঁথৰ"), [B("'She is my mother's only daughter' means she is the speaker.", "'তেওঁ মোৰ মাকৰ একমাত্ৰ জীয়েক' মানে কথকজনীয়েই।")], "flow", [B("Mother's only daughter", "মাকৰ একমাত্ৰ জীয়েক"), B("The speaker", "কথকজনী")]),
        stepwise(f"{p}.u2.q1", NAME, rel_step, [(f"{p}.u2.q1", B("A man says: 'Her mother is my mother's only daughter.' Who is she to him?", "এজন পুৰুষে ক'লে: 'তেওঁৰ মাক মোৰ মাকৰ একমাত্ৰ জীয়েক।' তেওঁ পুৰুষজনৰ কি?"), [(B("My mother's only daughter?", "মোৰ মাকৰ একমাত্ৰ জীয়েক?"), B("My sister", "মোৰ ভনী"), [B("Me", "মই"), B("My aunt", "মোৰ খুড়ী")], B("He is a man, so she is his sister.", "তেওঁ পুৰুষ, গতিকে ভনী।"), None), (B("Her daughter?", "তেওঁৰ জীয়েক?"), B("Niece", "ভাগিনী"), [B("Sister", "ভনী"), B("Cousin", "সম্পৰ্কীয় ভনী")], B("A sister's daughter.", "ভনীয়েকৰ জীয়েক।"), None)], B("She is his niece.", "তেওঁ ভাগিনী।")), (f"{p}.u2.q1", B("A woman says: 'His father is my father's only son.' Who is he to her?", "এগৰাকী মহিলাই ক'লে: 'তেওঁৰ দেউতাক মোৰ দেউতাকৰ একমাত্ৰ পুত্ৰ।' তেওঁ মহিলাগৰাকীৰ কি?"), [(B("My father's only son?", "মোৰ দেউতাকৰ একমাত্ৰ পুত্ৰ?"), B("My brother", "মোৰ ভাই"), [B("Me", "মই"), B("My uncle", "মোৰ খুড়া")], B("She is a woman, so it is her brother.", "তেওঁ মহিলা, গতিকে ভায়েক।"), None), (B("His son?", "তেওঁৰ পুত্ৰ?"), B("Nephew", "ভতিজা"), [B("Brother", "ভাই"), B("Cousin", "সম্পৰ্কীয় ভাই")], B("A brother's son.", "ভায়েকৰ পুত্ৰ।"), None)], B("He is her nephew.", "তেওঁ ভতিজা।"))]),
        tf(f"{p}.u2.q2", NAME, B("Your mother's sister's daughter is your cousin.", "তোমাৰ মাকৰ ভনীয়েকৰ জীয়েক তোমাৰ সম্পৰ্কীয় ভনী।"), True, B("Same generation, different parents.", "একে প্ৰজন্ম, বেলেগ পিতৃ-মাতৃ।")),
        match(f"{p}.u2.q3", NAME, B("Shrink each chain", "প্ৰতিটো শিকলি চুটি কৰা"), [[B("Father's father", "দেউতাৰ দেউতা"), B("Grandfather", "ককা")], [B("Brother's son", "ভাইৰ পুত্ৰ"), B("Nephew", "ভতিজা")], [B("Sister's daughter", "ভনীৰ জীয়েক"), B("Niece", "ভাগিনী")], [B("Son's wife", "পুত্ৰৰ পত্নী"), B("Daughter-in-law", "বোৱাৰী")]], B("Two links become one word.", "দুটা গাঁঠি এটা শব্দ।")),
        explore(f"{p}.u2.q4", NAME, gen_q, [("Go to your sister's son.", "ভনীয়েকৰ পুত্ৰলৈ যোৱা।", -1, B("One level below you.", "তোমাৰ এক স্তৰ তল।")), ("Go to your wife's mother.", "পত্নীৰ মাকলৈ যোৱা।", 1, B("One level above you.", "এক স্তৰ ওপৰ।")), ("Go to your son's daughter.", "পুত্ৰৰ জীয়েকলৈ যোৱা।", -2, B("Two levels below.", "দুই স্তৰ তল।"))]),
        order(f"{p}.u2.q5", NAME, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find the far end", "দূৰৰ মূৰ উলিওৱা"), B("Shrink two links", "দুটা গাঁঠি চুটি"), B("Repeat", "পুনৰ"), B("Name the result", "ফলৰ নাম")], B("One link at a time.", "এটা গাঁঠিকৈ।")),
    ])
    u3 = unit("u3", B("Gender is a separate fact", "লিংগ পৃথক তথ্য"), "star", [B("A name does not state gender.", "নামে লিংগ নকয়।"), B("Words like 'brother' do state it.", "'ভাই'ৰ দৰে শব্দই কয়।"), B("'Child' or 'sibling' says nothing.", "'সন্তান' শব্দই নকয়।"), B("'Cannot be determined' can be right.", "'ঠিক কৰিব নোৱাৰি' শুদ্ধ হ'ব পাৰে।")], [
        diagram(f"{p}.u3.s1", B("Do not guess from names", "নামৰ পৰা নুধৰিবা"), [B("If P is the child of Q, we know nothing about P's gender.", "P, Q ৰ সন্তান হ'লে P ৰ লিংগ নাজানো।")], "grid", [B("Son: male", "পুত্ৰ: পুৰুষ"), B("Daughter: female", "জীয়েক: মহিলা"), B("Child: unknown", "সন্তান: অজ্ঞাত")]),
        diagram(f"{p}.u3.s2", B("Unknown is an answer", "অজ্ঞাতও উত্তৰ"), [B("Exams test this. If the words stop short, the data is not enough.", "পৰীক্ষাত সোধে। শব্দই নক'লে তথ্য অপ্ৰতুল।")], "flow", [B("Stated?", "কোৱা হৈছে?"), B("Yes: use it", "হয়: ব্যৱহাৰ"), B("No: unknown", "নহয়: অজ্ঞাত")]),
        tf(f"{p}.u3.q1", GENDER, B("If R is the sibling of S, then R is male.", "R, S ৰ ভাই-ভনী হ'লে R পুৰুষ।"), False, B("Sibling states no gender.", "'ভাই-ভনী' ত লিংগ নাই।"), ("r-m-gender", GEND)),
        tf(f"{p}.u3.q2", GENDER, B("If R is the brother of S, we know S is male.", "R, S ৰ ভাই হ'লে S পুৰুষ।"), False, B("Only R's gender is stated.", "কেৱল R ৰ লিংগ কোৱা হৈছে।"), ("r-m-gender", GEND)),
        match(f"{p}.u3.q3", GENDER, B("Match the word to what it states", "শব্দক অৰ্থৰ লগত মিলোৱা"), [[B("Aunt", "খুড়ী"), B("Female", "মহিলা")], [B("Nephew", "ভতিজা"), B("Male", "পুৰুষ")], [B("Cousin", "সম্পৰ্কীয়"), B("Not stated", "কোৱা নাই")]], B("Check each word.", "প্ৰতিটো শব্দ চোৱা।")),
        stepwise(f"{p}.u3.q4", GENDER, rel_step, [(f"{p}.u3.q4", B("A is B's child. B is C's son. What is A to C?", "A, B ৰ সন্তান। B, C ৰ পুত্ৰ। A, C ৰ কি?"), [(B("B to C?", "B, C ৰ কি?"), B("Son", "পুত্ৰ"), [B("Father", "দেউতাক"), B("Brother", "ভাই")], B("Stated.", "কোৱা হৈছে।"), None), (B("A to C?", "A, C ৰ কি?"), B("Grandchild", "নাতি-নাতিনী"), [B("Grandson", "নাতি"), B("Granddaughter", "নাতিনী")], GEND, "r-m-gender")], B("A's gender is not stated.", "A ৰ লিংগ কোৱা নাই।")), (f"{p}.u3.q4", B("P is Q's sister. Q is R's child. What is P to R?", "P, Q ৰ ভনী। Q, R ৰ সন্তান। P, R ৰ কি?"), [(B("P's gender?", "P ৰ লিংগ?"), B("Female", "মহিলা"), [B("Male", "পুৰুষ"), B("Unknown", "অজ্ঞাত")], B("Sister states it.", "'ভনী'য়ে কয়।"), None), (B("P to R?", "P, R ৰ কি?"), B("Daughter", "জীয়েক"), [B("Son", "পুত্ৰ"), B("Mother", "মাক")], B("Q's sister is also R's child.", "Q ৰ ভনীও R ৰ সন্তান।"), None)], B("P is R's daughter.", "P, R ৰ জীয়েক।"))]),
        order(f"{p}.u3.q5", GENDER, B("Put the check in order", "পৰীক্ষা ক্ৰমে সজোৱা"), [B("Read the exact word", "ঠিক শব্দ পঢ়া"), B("Is gender stated?", "লিংগ কোৱা হৈছে?"), B("Mark it or leave it", "চিন বা এৰা"), B("Answer only from marks", "চিনৰ পৰা উত্তৰ")], B("Mark only stated facts.", "কোৱা তথ্যহে চিন কৰা।")),
    ])
    u4 = unit("u4", B("Coded families", "সংকেতৰ পৰিয়াল"), "star", [B("Write what each symbol means.", "প্ৰতিটো চিহ্নৰ অৰ্থ লিখা।"), B("Read the code left to right.", "সংকেত বাওঁৰ পৰা সোঁলৈ।"), B("A + B reads as a stated relation.", "A + B কোৱা সম্পৰ্ক।"), B("Draw it, then name the ends.", "আঁকি দুই মূৰৰ নাম কোৱা।")], [
        diagram(f"{p}.u4.s1", B("Symbols replace words", "চিহ্নই শব্দ সলায়"), [B("A + B may mean 'A is B's father'. Rewrite the code in words first.", "A + B মানে 'A, B ৰ দেউতাক' হ'ব পাৰে। প্ৰথমে শব্দত লিখা।")], "flow", [B("Read the key", "চাবি পঢ়া"), B("Rewrite", "লিখা"), B("Draw it", "আঁকা")]),
        diagram(f"{p}.u4.s2", B("One link at a time", "এটা গাঁঠিকৈ"), [B("P + Q − R is two links. Draw each separately, then join at Q.", "P + Q − R দুটা গাঁঠি। পৃথকে আঁকি Q ত জোৰা।")], "flow", [B("P to Q", "P ৰ পৰা Q"), B("Q to R", "Q ৰ পৰা R"), B("Join at Q", "Q ত জোৰা")]),
        stepwise(f"{p}.u4.q1", CODE, rel_step, [(f"{p}.u4.q1", B("A + B means A is B's father. A − B means A is B's sister. What is P in P + Q − R?", "A + B মানে A, B ৰ দেউতাক। A − B মানে A, B ৰ ভনী। P + Q − R ত P কি?"), [(B("Q to R?", "Q, R ৰ কি?"), B("Sister", "ভনী"), [B("Father", "দেউতাক"), B("Brother", "ভাই")], B("− means sister.", "− মানে ভনী।"), None), (B("P to R?", "P, R ৰ কি?"), B("Father", "দেউতাক"), [B("Uncle", "খুড়া"), B("Brother", "ভাই")], B("Q's father is also R's father.", "Q ৰ দেউতাকেই R ৰ দেউতাক।"), None)], B("P is R's father.", "P, R ৰ দেউতাক।")), (f"{p}.u4.q1", B("A × B means A is B's mother. A ÷ B means A is B's brother. What is P in P × Q ÷ R?", "A × B মানে A, B ৰ মাক। A ÷ B মানে A, B ৰ ভাই। P × Q ÷ R ত P কি?"), [(B("Q to R?", "Q, R ৰ কি?"), B("Brother", "ভাই"), [B("Mother", "মাক"), B("Sister", "ভনী")], B("÷ means brother.", "÷ মানে ভাই।"), None), (B("P to R?", "P, R ৰ কি?"), B("Mother", "মাক"), [B("Aunt", "খুড়ী"), B("Sister", "ভনী")], B("Q's mother is also R's mother.", "Q ৰ মাকেই R ৰ মাক।"), None)], B("P is R's mother.", "P, R ৰ মাক।"))]),
        tf(f"{p}.u4.q2", CODE, B("Rewriting a coded relation in words comes first.", "সংকেতৰ সম্পৰ্ক প্ৰথমে শব্দত লিখা।"), True, B("It prevents slips.", "ই ভুল ৰোধ কৰে।")),
        match(f"{p}.u4.q3", CODE, B("+ father, − sister, × son: match", "+ দেউতাক, − ভনী, × পুত্ৰ: মিলোৱা"), [[same("A + B"), B("A is B's father", "A, B ৰ দেউতাক")], [same("A − B"), B("A is B's sister", "A, B ৰ ভনী")], [same("A × B"), B("A is B's son", "A, B ৰ পুত্ৰ")]], B("Read the key.", "চাবি পঢ়া।")),
        order(f"{p}.u4.q4", CODE, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the key", "চাবি পঢ়া"), B("Rewrite each link", "প্ৰতিটো গাঁঠি লিখা"), B("Draw them", "আঁকা"), B("Name the ends", "মূৰৰ নাম")], B("Words, drawing, answer.", "শব্দ, চিত্ৰ, উত্তৰ।")),
        explore(f"{p}.u4.q5", CODE, gen_q, [("A + B means A is B's father. Start at P in P + Q + R, and move to R's level.", "A + B মানে A, B ৰ দেউতাক। P + Q + R ত P ৰ পৰা R ৰ স্তৰলৈ যোৱা।", -2, B("Two fathers down.", "দুই স্তৰ তল।")), ("A − B means A is B's child. Start at P in P − Q − R, and move to R's level.", "A − B মানে A, B ৰ সন্তান। P − Q − R ত P ৰ পৰা R ৰ স্তৰলৈ যোৱা।", 2, B("Two levels up.", "দুই স্তৰ ওপৰ।"))]),
    ])
    test = {"id": "test", "title": B("Blood relations test", "তেজৰ সম্পৰ্কৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", GEN, gen_q, [("Go to your father's mother.", "দেউতাকৰ মাকলৈ যোৱা।", 2, B("Two levels up.", "দুই স্তৰ ওপৰ।")), ("Go to your daughter's son.", "জীয়েকৰ পুত্ৰলৈ যোৱা।", -2, B("Two levels down.", "দুই স্তৰ তল।"))]),
        tf(f"{p}.t.q2", NAME, B("Your brother's daughter is your niece.", "ভাইৰ জীয়েক তোমাৰ ভতিজী।"), True, B("A sibling's daughter.", "ভাই-ভনীৰ জীয়েক।")),
        tf(f"{p}.t.q3", GENDER, B("'Child' states gender.", "'সন্তান' শব্দই লিংগ কয়।"), False, B("It does not.", "নকয়।"), ("r-m-gender", GEND)),
        tf(f"{p}.t.q4", GENDER, B("Sister states that a person is female.", "'ভনী' শব্দই মহিলা বুলি কয়।"), True, B("It does.", "কয়।")),
        stepwise(f"{p}.t.q5", NAME, rel_step, [(f"{p}.t.q5", B("My father's only son's son is my?", "মোৰ দেউতাকৰ একমাত্ৰ পুত্ৰৰ পুত্ৰ মোৰ কি? (মই পুৰুষ)"), [(B("Father's only son?", "দেউতাকৰ একমাত্ৰ পুত্ৰ?"), B("Me", "মই"), [B("Uncle", "খুড়া"), B("Brother", "ভাই")], B("I am male, so it is me.", "মই পুৰুষ, গতিকে ময়েই।"), None), (B("Then his son?", "তেন্তে পুত্ৰ?"), B("My son", "মোৰ পুত্ৰ"), [B("My nephew", "মোৰ ভতিজা"), B("My brother", "মোৰ ভাই")], B("Follows at once.", "লগে লগে ওলায়।"), None)], B("He is my son.", "তেওঁ মোৰ পুত্ৰ।")), (f"{p}.t.q5", B("My mother's only daughter's son is my? (I am female)", "মোৰ মাকৰ একমাত্ৰ জীয়েকৰ পুত্ৰ মোৰ কি? (মই মহিলা)"), [(B("Mother's only daughter?", "মাকৰ একমাত্ৰ জীয়েক?"), B("Me", "মই"), [B("Aunt", "খুড়ী"), B("Sister", "ভনী")], B("I am female, so it is me.", "মই মহিলা, গতিকে ময়েই।"), None), (B("Then her son?", "তেন্তে পুত্ৰ?"), B("My son", "মোৰ পুত্ৰ"), [B("My nephew", "মোৰ ভতিজা"), B("My cousin", "মোৰ সম্পৰ্কীয়")], B("Follows at once.", "লগে লগে ওলায়।"), None)], B("He is my son.", "তেওঁ মোৰ পুত্ৰ।"))]),
        tf(f"{p}.t.q6", CODE, B("Coded relations join at the shared letter.", "সংকেতৰ সম্পৰ্ক উমৈহতীয়া আখৰত জোৰা লাগে।"), True, B("Q joins P + Q − R.", "Q ত P + Q − R জোৰা লাগে।")),
    ]}
    return {"id": "rs-10-blood-relations", "no": 10, "slug": "blood-relations", "title": B("Blood relations", "তেজৰ সম্পৰ্ক"), "reign": B("Generations, gender, coded relations", "প্ৰজন্ম, লিংগ, সংকেত"), "units": [u1, u2, u3, u4], "test": test}


def rank_right(n, a):
    return {"q": B(f"Slide to the {a}th place from the left in a line of {n}. Then answer: what is the place from the right?", f"{n} জনৰ শাৰীত বাওঁৰ পৰা {a} নম্বৰলৈ টানা।"), "widget": {"kind": "queue", "n": n}, "target": a, "answerText": B(f"{n - a + 1}th from the right", f"সোঁৰ পৰা {n - a + 1}"), "why": B(f"{n} − {a} + 1 = {n - a + 1}.", f"{n} − {a} + 1 = {n - a + 1}।")}


def rank_total(l, r):
    return {"q": B(f"Someone is {l}th from the left and {r}th from the right. How many are in the line?", f"এজন বাওঁৰ পৰা {l} আৰু সোঁৰ পৰা {r} নম্বৰ। শাৰীত মুঠ কিমান?"), "answer": str(l + r - 1), "why": B(f"{l} + {r} − 1 = {l + r - 1}.", f"{l} + {r} − 1 = {l + r - 1}।"), "traps": [{"ans": str(l + r), "tag": "r-m-twice", "why": TWICE}]}


def between(a, b, n):
    return {"q": B(f"In a line of {n}, A is {a}th from the left and B is {b}th from the right. How many stand between them?", f"{n} জনৰ শাৰীত A বাওঁৰ পৰা {a}, B সোঁৰ পৰা {b}। মাজত কিমান?"), "answer": str(n - a - b), "why": B(f"{n} − {a} − {b} = {n - a - b}.", f"{n} − {a} − {b} = {n - a - b}।")}


def swap_rank(a, b, new_a):
    d = new_a - a
    return {"q": B(f"A is {a}th and B is {b}th from the left. They swap, and A is now {b}th. What is B's new place?", f"A বাওঁৰ পৰা {a}, B {b}। ঠাই সলনি কৰাত A এতিয়া {b}। B ৰ নতুন স্থান?"), "answer": str(a), "why": B("Each takes the other's place.", "প্ৰত্যেকে আনজনৰ ঠাই লয়।")}


def lesson_rank():
    p = "rs11"
    u1 = unit("u1", B("Two ends, one person", "দুই মূৰ, এজন ব্যক্তি"), "star", [B("Left + right − 1 = total.", "বাওঁ + সোঁ − 1 = মুঠ।"), B("The person is counted twice.", "ব্যক্তিজন দুবাৰ গণা হয়।"), B("From right = total − left + 1.", "সোঁ = মুঠ − বাওঁ + 1।"), B("Top and bottom work the same.", "ওপৰ-তলো একে।")], [
        lab(f"{p}.u1.s1", B("Slide and watch both ranks", "টানি দুয়োটা স্থান চোৱা"), B("Move one person along a line of 10. As one rank rises, the other falls.", "10 জনৰ শাৰীত এজনক টানা। এটা স্থান বাঢ়িলে আনটো কমে।"), {"kind": "queue", "n": 10}, [
            task(B("Slide to 4th from the left.", "বাওঁৰ পৰা 4 লৈ টানা।"), {"pos": 4}, B("That is 7th from the right, and 4 + 7 = 11.", "সোঁৰ পৰা 7, 4 + 7 = 11।")),
            task(B("Slide to 8th from the left.", "বাওঁৰ পৰা 8 লৈ টানা।"), {"pos": 8}, B("Again 8 + 3 = 11. One more than the total, always.", "আকৌ 8 + 3 = 11। সদায় মুঠতকৈ এক বেছি।")),
        ]),
        diagram(f"{p}.u1.s2", B("Why subtract one", "কিয় এক বিয়োগ"), [B("Both counts include the same person, so one count is extra.", "দুয়োটা গণনাত একেজন আছে, সেয়ে এটা গণনা অতিৰিক্ত।")], "flow", [B("Left count", "বাওঁ গণনা"), B("Right count", "সোঁ গণনা"), B("Minus one", "এক বিয়োগ")]),
        explore(f"{p}.u1.q1", RANK, rank_right, [(12, 5), (15, 9), (9, 2)]),
        solve(f"{p}.u1.q2", RANK, lambda n, a: {"q": B(f"In a class of {n}, a student is {a}th from the top. What is the rank from the bottom?", f"{n} জনৰ শ্ৰেণীত এজন ওপৰৰ পৰা {a}। তলৰ পৰা স্থান?"), "answer": str(n - a + 1), "why": B(f"{n} − {a} + 1.", f"{n} − {a} + 1।")}, [(40, 11), (52, 20), (35, 7)]),
        tf(f"{p}.u1.q3", RANK, B("10th from left in a line of 20 is 11th from right.", "20 জনৰ শাৰীত বাওঁৰ 10 সোঁৰ 11।"), True, B("20 − 10 + 1 = 11.", "20 − 10 + 1 = 11।")),
        match(f"{p}.u1.q4", RANK, B("Line of 8: match", "8 জনৰ শাৰী: মিলোৱা"), [[B("1st left", "বাওঁৰ ১ম"), same(8)], [B("3rd left", "বাওঁৰ ৩য়"), same(6)], [B("6th left", "বাওঁৰ ৬ষ্ঠ"), same(3)]], B("Total − left + 1.", "মুঠ − বাওঁ + 1।")),
        order(f"{p}.u1.q5", RANK, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Note the total", "মুঠ লিখা"), B("Note the rank", "স্থান লিখা"), B("Subtract", "বিয়োগ"), B("Add one", "এক যোগ")], B("Total − rank + 1.", "মুঠ − স্থান + 1।")),
    ])
    u2 = unit("u2", B("Totals and gaps", "মুঠ আৰু মাজৰ সংখ্যা"), "star", [B("Total = both ranks − 1.", "মুঠ = দুয়োটা স্থান − 1।"), B("Between = total − both end counts.", "মাজত = মুঠ − দুই মূৰৰ গণনা।"), B("Draw a quick line.", "খৰকৈ শাৰী আঁকা।"), B("Watch whether they overlap.", "ওপৰা-ওপৰি হয় নেকি চোৱা।")], [
        diagram(f"{p}.u2.s1", B("Sketch the line", "শাৰী আঁকা"), [B("Mark who is counted from which end, then what is left.", "কোন কোন মূৰৰ পৰা চিন কৰি বাকীখিনি চোৱা।")], "flow", [B("Left block", "বাওঁ খণ্ড"), B("Middle", "মাজ"), B("Right block", "সোঁ খণ্ড")]),
        diagram(f"{p}.u2.s2", B("Between is a subtraction", "মাজ এটা বিয়োগ"), [B("Remove both end blocks from the total. What remains stands between.", "মুঠৰ পৰা দুই মূৰৰ খণ্ড আঁতৰোৱা। বাকীখিনি মাজত।")], "flow", [same("Total 30"), same("− 8 − 12"), B("10 between", "মাজত 10")]),
        solve(f"{p}.u2.q1", TOTAL, rank_total, [(14, 9), (21, 17), (8, 13)]),
        solve(f"{p}.u2.q2", TOTAL, between, [(7, 9, 30), (10, 12, 40), (5, 6, 25)]),
        stepwise(f"{p}.u2.q3", TOTAL, lambda l, r: {"q": B(f"Left rank {l}, right rank {r}. Find the total.", f"বাওঁ {l}, সোঁ {r}। মুঠ উলিওৱা।"), "parts": [
            part(B("Add the ranks?", "স্থান যোগ?"), same(l + r), [same(l * r), same(l - r)], B("First add.", "আগতে যোগ।"), sid=f"{p}.u2.q3"),
            part(B("Then?", "তাৰ পিছত?"), same(l + r - 1), [same(l + r), same(l + r + 1)], TWICE, tag="r-m-twice", sid=f"{p}.u2.q3"),
        ], "why": B("Subtract the double count.", "দুবাৰ গণা আঁতৰোৱা।")}, [(6, 15), (11, 8), (19, 4)]),
        tf(f"{p}.u2.q4", TOTAL, B("Left rank 5 and right rank 5 mean a line of 10.", "বাওঁ 5, সোঁ 5 মানে 10 জন।"), False, B("It is 9.", "ই 9।"), ("r-m-twice", TWICE)),
        match(f"{p}.u2.q5", TOTAL, B("Match the ranks to the total", "স্থানক মুঠৰ লগত মিলোৱা"), [[same("3 and 3"), same(5)], [same("6 and 8"), same(13)], [same("10 and 11"), same(20)]], B("Add, then minus 1.", "যোগ, তাৰ পিছত − 1।")),
    ])
    u3 = unit("u3", B("When people swap", "ঠাই সলনি হ'লে"), "star", [B("In a swap, each takes the other's place.", "সলনিত প্ৰত্যেকে আনজনৰ ঠাই লয়।"), B("The total never changes.", "মুঠ সলনি নহয়।"), B("Use the changed rank to find the gap.", "সলনি হোৱা স্থানৰ পৰা ব্যৱধান।"), B("Add gaps to known ranks.", "জনা স্থানত ব্যৱধান যোগ।")], [
        diagram(f"{p}.u3.s1", B("Swap places, keep the line", "ঠাই সলনি, শাৰী একে"), [B("If A moves from 5th to 9th by swapping, B moves from 9th to 5th.", "A সলনি কৰি 5 ৰ পৰা 9 গ'লে B, 9 ৰ পৰা 5।")], "flow", [same("A: 5 → 9"), same("B: 9 → 5"), B("Gap: 4", "ব্যৱধান: 4")]),
        diagram(f"{p}.u3.s2", B("Using the gap", "ব্যৱধান ব্যৱহাৰ"), [B("If B's new rank from the other end is known, the gap gives the total.", "আনটো মূৰৰ পৰা B ৰ নতুন স্থান জানিলে মুঠ পোৱা যায়।")], "flow", [B("Old rank", "পুৰণি স্থান"), B("Gap", "ব্যৱধান"), B("New rank", "নতুন স্থান")]),
        solve(f"{p}.u3.q1", SWAPR, swap_rank, [(6, 12, 12), (9, 15, 15), (4, 11, 11)]),
        solve(f"{p}.u3.q2", SWAPR, lambda a, b, r: {"q": B(f"A is {a}th from the left. After swapping with B, A is {b}th from the left and {r}th from the right. How many are in the line?", f"A বাওঁৰ পৰা {a}। B ৰ লগত সলনিৰ পিছত A বাওঁৰ পৰা {b}, সোঁৰ পৰা {r}। মুঠ কিমান?"), "answer": str(b + r - 1), "why": B(f"Use A's new ranks: {b} + {r} − 1.", f"A ৰ নতুন স্থান: {b} + {r} − 1।"), "traps": [{"ans": str(a + r - 1), "tag": "r-m-twice", "why": B("Use both ranks at the same moment, after the swap.", "সলনিৰ পিছৰ দুয়োটা স্থান লোৱা।")}]}, [(5, 11, 7), (8, 14, 9), (3, 10, 12)]),
        tf(f"{p}.u3.q3", SWAPR, B("A swap changes the total in the line.", "সলনিয়ে মুঠ সলায়।"), False, B("People only change places.", "কেৱল ঠাই সলনি।")),
        match(f"{p}.u3.q4", SWAPR, B("A was 3rd, B was 8th. After swapping", "A 3, B 8। সলনিৰ পিছত"), [[B("A's place", "A ৰ স্থান"), same(8)], [B("B's place", "B ৰ স্থান"), same(3)], [B("Gap", "ব্যৱধান"), same(5)]], B("They trade.", "সলনি হয়।")),
        order(f"{p}.u3.q5", SWAPR, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Note old ranks", "পুৰণি স্থান"), B("Trade them", "সলনি কৰা"), B("Take ranks after the swap", "সলনিৰ পিছৰ স্থান"), B("Find the total", "মুঠ উলিওৱা")], B("Use one moment only.", "একে সময়ৰ স্থান।")),
    ])
    u4 = unit("u4", B("Order by time", "সময়ৰ ক্ৰম"), "star", [B("Earlier sits before later.", "আগৰটো আগত।"), B("Convert to one clock.", "এটা ঘড়ীলৈ আনা।"), B("Add late, subtract early.", "পলম যোগ, আগতীয়া বিয়োগ।"), B("Draw comparisons as a line.", "তুলনা শাৰীত আঁকা।")], [
        diagram(f"{p}.u4.s1", B("Build one line from clues", "ইংগিতৰ পৰা এটা শাৰী"), [B("A is taller than B, and B than C. That makes one line: A, B, C.", "A, B তকৈ ওখ, B, C তকৈ। এটা শাৰী: A, B, C।")], "flow", [same("A"), same("B"), same("C")]),
        diagram(f"{p}.u4.s2", B("Late and early", "পলম আৰু আগতীয়া"), [B("A train due at 4:20 runs 15 minutes late, so it comes at 4:35.", "4:20 ৰ ৰেল 15 মিনিট পলম, গতিকে 4:35।")], "flow", [same("4:20"), same("+ 15"), same("4:35")]),
        order(f"{p}.u4.q1", TIMEO, B("A is older than B, and C is older than A. Oldest first", "A, B তকৈ ডাঙৰ, C, A তকৈ ডাঙৰ। ডাঙৰৰ পৰা"), [same("C"), same("A"), same("B")], B("C, then A, then B.", "C, A, B।")),
        solve(f"{p}.u4.q2", TIMEO, lambda h, m, late: {"q": B(f"A meeting set for {h}:{m:02d} starts {late} minutes late. How many minutes past {h} does it start?", f"{h}:{m:02d} ৰ সভা {late} মিনিট পলমকৈ আৰম্ভ হ'ল। {h} ৰ পিছত কিমান মিনিটত?"), "answer": str(m + late), "why": B(f"{m} + {late} = {m + late}.", f"{m} + {late} = {m + late}।")}, [(4, 20, 15), (9, 5, 25), (2, 30, 12)]),
        tf(f"{p}.u4.q3", TIMEO, B("If P is taller than Q, and R shorter than Q, then P is tallest.", "P, Q তকৈ ওখ, R, Q তকৈ চুটি হ'লে P আটাইতকৈ ওখ।"), True, B("P, Q, R.", "P, Q, R।")),
        match(f"{p}.u4.q4", TIMEO, B("Due 6:10: match", "6:10 ত: মিলোৱা"), [[B("10 late", "10 পলম"), same("6:20")], [B("5 early", "5 আগতীয়া"), same("6:05")], [B("On time", "সময়ত"), same("6:10")]], B("Add or subtract.", "যোগ বা বিয়োগ।")),
        stepwise(f"{p}.u4.q5", TIMEO, lambda a, b: {"q": B(f"{a} arrived before Bina. {b} arrived after Bina. Who was last?", f"{a} বীণাৰ আগত আহিল। {b} বীণাৰ পিছত আহিল। শেষত কোন?"), "parts": [
            part(B("Who was before Bina?", "বীণাৰ আগত কোন?"), same(a), [same(b), B("Nobody", "কোনো নাই")], B("Stated.", "কোৱা হৈছে।"), sid=f"{p}.u4.q5"),
            part(B("Who was last?", "শেষত কোন?"), same(b), [same(a), B("Bina", "বীণা")], B("Build the line.", "শাৰী বনোৱা।"), sid=f"{p}.u4.q5"),
        ], "why": B(f"{a}, Bina, {b}.", f"{a}, বীণা, {b}।")}, [("Asha", "Jonali"), ("Rupa", "Mina"), ("Nita", "Purabi")]),
    ])
    test = {"id": "test", "title": B("Ranking test", "স্থানৰ পৰীক্ষা"), "steps": [
        solve(f"{p}.t.q1", TOTAL, rank_total, [(17, 12), (9, 22)]),
        solve(f"{p}.t.q2", TOTAL, between, [(8, 10, 32), (6, 15, 28)]),
        solve(f"{p}.t.q3", RANK, lambda n, a: {"q": B(f"{a}th from the left in a line of {n}: what place from the right?", f"{n} জনৰ শাৰীত বাওঁৰ {a}: সোঁৰ পৰা?"), "answer": str(n - a + 1), "why": B(f"{n} − {a} + 1.", f"{n} − {a} + 1।")}, [(45, 19), (28, 6)]),
        solve(f"{p}.t.q4", SWAPR, swap_rank, [(7, 13, 13), (2, 9, 9)]),
        tf(f"{p}.t.q5", TOTAL, B("Ranks 7 and 7 give 13 people.", "7 আৰু 7 ৰ স্থানে 13 জন দিয়ে।"), True, B("7 + 7 − 1 = 13.", "7 + 7 − 1 = 13।")),
        tf(f"{p}.t.q6", TIMEO, B("If A is before B and B before C, then C is first.", "A, B ৰ আগত, B, C ৰ আগত হ'লে C প্ৰথম।"), False, B("A is first.", "A প্ৰথম।")),
    ]}
    return {"id": "rs-11-ranking", "no": 11, "slug": "ranking", "title": B("Ranking and order", "স্থান আৰু ক্ৰম"), "reign": B("Ranks, totals, swaps, time order", "স্থান, মুঠ, সলনি, সময়"), "units": [u1, u2, u3, u4], "test": test}


def seat_q(q, names, order_, round_, why):
    target = int("".join(str(names.index(n) + 1) for n in order_))
    return {"q": q, "widget": {"kind": "seats", "names": names, "round": round_}, "target": target, "answerText": same(" ".join(order_)), "why": why}


def lesson_arrange():
    p = "rs12"
    u1 = unit("u1", B("Fixed facts first", "নিশ্চিত তথ্য আগতে"), "star", [B("Start with the clue that fixes a seat.", "আসন ঠিক কৰা ইংগিতৰ পৰা আৰম্ভ।"), B("Add clues that link to it.", "লগ লগা ইংগিত যোগ কৰা।"), B("Keep 'next to' for later.", "'কাষত' পিছলৈ ৰাখা।"), B("Check all clues at the end.", "শেষত সকলো চোৱা।")], [
        diagram(f"{p}.u1.s1", B("Sort the clues", "ইংগিত বাছা"), [B("Some clues fix a place. Others only link people. Place the fixed ones first.", "কিছুমান ইংগিতে ঠাই ঠিক কৰে। আন কিছুমানে কেৱল সংযোগ কৰে। ঠিকখিনি আগতে।")], "grid", [B("Fixed: A is at the left end", "ঠিক: A বাওঁ মূৰত"), B("Link: B is next to C", "সংযোগ: B, C ৰ কাষত")]),
        diagram(f"{p}.u1.s2", B("Must, not may", "লাগিবই, হ'ব পাৰে নহয়"), [B("Write only what must be true. If two seats are possible, keep both in mind.", "লাগিবই লগাখিনিহে লিখা। দুটা আসন সম্ভৱ হ'লে দুয়োটা মনত ৰাখা।")], "flow", [B("Fixed", "ঠিক"), B("Linked", "সংযোগ"), B("Possible", "সম্ভৱ")]),
        explore(f"{p}.u1.q1", FIXED, seat_q, [(B("Seat them left to right: A is at the left end, and C is at the right end.", "বাওঁৰ পৰা সোঁলৈ বহুওৱা: A বাওঁ মূৰত, C সোঁ মূৰত।"), ["A", "B", "C"], ["A", "B", "C"], False, B("B takes the seat left over.", "B বাকী আসনত।")), (B("Seat them left to right: Q is in the middle, and R is left of Q.", "বাওঁৰ পৰা সোঁলৈ: Q মাজত, R, Q ৰ বাওঁফালে।"), ["P", "Q", "R"], ["R", "Q", "P"], False, B("P takes the right end.", "P সোঁ মূৰত।"))]),
        tf(f"{p}.u1.q2", FIXED, B("'B is next to C' fixes B's exact seat.", "'B, C ৰ কাষত' ই B ৰ ঠিক আসন কয়।"), False, B("B could be on either side.", "B যিকোনো ফালে হ'ব পাৰে।"), ("r-m-maybe", MAYBE)),
        match(f"{p}.u1.q3", FIXED, B("Match the clue to its kind", "ইংগিতক ধৰণৰ লগত মিলোৱা"), [[B("A is at the end", "A মূৰত"), B("Fixed", "ঠিক")], [B("B is beside C", "B, C ৰ কাষত"), B("Link", "সংযোগ")], [B("D is not first", "D প্ৰথম নহয়"), B("Exclusion", "বাদ")]], B("Sort before seating.", "বহুওৱাৰ আগতে বাছা।")),
        order(f"{p}.u1.q4", FIXED, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Draw empty seats", "খালী আসন আঁকা"), B("Place fixed clues", "ঠিক ইংগিত"), B("Add linked clues", "সংযোগ ইংগিত"), B("Check all clues", "সকলো চোৱা")], B("Fixed first.", "ঠিকখিনি আগতে।")),
        stepwise(f"{p}.u1.q5", FIXED, lambda a, b, c: {"q": B(f"{a} sits left of {b}. {c} sits at the right end. Three seats in a row. Who is in the middle?", f"{a}, {b} ৰ বাওঁফালে। {c} সোঁ মূৰত। তিনি আসন। মাজত কোন?"), "parts": [
            part(B("Right end?", "সোঁ মূৰত?"), same(c), [same(a), same(b)], B("Stated.", "কোৱা হৈছে।"), sid=f"{p}.u1.q5"),
            part(B("Left end?", "বাওঁ মূৰত?"), same(a), [same(b), same(c)], B(f"{a} is left of {b}.", f"{a}, {b} ৰ বাওঁফালে।"), sid=f"{p}.u1.q5"),
            part(B("Middle?", "মাজত?"), same(b), [same(a), same(c)], B("The seat left.", "বাকী আসন।"), sid=f"{p}.u1.q5"),
        ], "why": B(f"{a}, {b}, {c}.", f"{a}, {b}, {c}।")}, [("X", "Y", "Z"), ("L", "M", "N"), ("D", "E", "F")]),
    ])
    u2 = unit("u2", B("Sitting in a row", "শাৰীত বহা"), "star", [B("Decide which way they face.", "কোন ফালে মুখ চোৱা।"), B("Your left is the page's left if facing you.", "তোমাৰ ফালে মুখ হ'লে কথা বেলেগ।"), B("'Between' needs one on each side.", "'মাজত' মানে দুয়োফালে।"), B("'Immediately' means next seat.", "'ঠিক' মানে কাষৰ আসন।")], [
        diagram(f"{p}.u2.s1", B("Mind the facing", "মুখৰ দিশ চোৱা"), [B("When a row faces north, left and right match the page. Facing south, they flip.", "শাৰী উত্তৰমুখী হ'লে পৃষ্ঠাৰ দৰে। দক্ষিণমুখী হ'লে ওলোটা।")], "grid", [B("North: page left is left", "উত্তৰ: পৃষ্ঠাৰ বাওঁ বাওঁ"), B("South: page left is right", "দক্ষিণ: পৃষ্ঠাৰ বাওঁ সোঁ")]),
        diagram(f"{p}.u2.s2", B("Exact words matter", "শব্দ গুৰুত্বপূৰ্ণ"), [B("'Left of' can be any seat. 'Immediately left of' is the next seat.", "'বাওঁফালে' যিকোনো আসন। 'ঠিক বাওঁফালে' কাষৰ আসন।")], "flow", [B("Left of: far or near", "বাওঁ: দূৰ বা ওচৰ"), B("Immediately left: next", "ঠিক বাওঁ: কাষত")]),
        explore(f"{p}.u2.q1", LINE, seat_q, [(B("Facing north, left to right: B is between A and C, and A is at the left end. D is at the right end.", "উত্তৰমুখী, বাওঁৰ পৰা: B, A আৰু C ৰ মাজত, A বাওঁ মূৰত। D সোঁ মূৰত।"), ["A", "B", "C", "D"], ["A", "B", "C", "D"], False, B("A, B, C, D.", "A, B, C, D।")), (B("Facing north, left to right: S is immediately right of Q. P is at the right end. R is at the left end.", "উত্তৰমুখী, বাওঁৰ পৰা: S, Q ৰ ঠিক সোঁফালে। P সোঁ মূৰত। R বাওঁ মূৰত।"), ["P", "Q", "R", "S"], ["R", "Q", "S", "P"], False, B("R, Q, S, P.", "R, Q, S, P।"))]),
        tf(f"{p}.u2.q2", LINE, B("'Immediately right of' means the very next seat.", "'ঠিক সোঁফালে' মানে কাষৰ আসন।"), True, B("Yes.", "হয়।")),
        match(f"{p}.u2.q3", LINE, B("Row: A B C D (facing north). Match", "শাৰী: A B C D (উত্তৰমুখী)। মিলোৱা"), [[B("Immediately left of C", "C ৰ ঠিক বাওঁফালে"), same("B")], [B("Right end", "সোঁ মূৰ"), same("D")], [B("Left end", "বাওঁ মূৰ"), same("A")]], B("Read the row.", "শাৰী পঢ়া।")),
        order(f"{p}.u2.q4", LINE, B("Seat: B between A and C, with A first", "B, A আৰু C ৰ মাজত, A প্ৰথম"), [same("A"), same("B"), same("C")], B("Between means both sides.", "মাজ মানে দুয়োফালে।")),
        solve(f"{p}.u2.q5", LINE, lambda a, b: {"q": B(f"In a row, {a} people sit left of X and {b} sit right of X. How many are in the row?", f"শাৰীত X ৰ বাওঁফালে {a}, সোঁফালে {b} জন। মুঠ কিমান?"), "answer": str(a + b + 1), "why": B(f"{a} + {b} + X = {a + b + 1}.", f"{a} + {b} + X = {a + b + 1}।")}, [(3, 5), (7, 2), (4, 6)]),
    ])
    u3 = unit("u3", B("Sitting in a circle", "বৃত্তত বহা"), "star", [B("In a circle, pick any seat as the start.", "বৃত্তত যিকোনো আসনৰ পৰা আৰম্ভ।"), B("Facing the centre, left is clockwise.", "কেন্দ্ৰমুখী হ'লে বাওঁ ঘড়ীৰ দিশে।"), B("'Opposite' needs an even number.", "'সন্মুখত'ৰ বাবে যোৰ সংখ্যা।"), B("Neighbours are both sides.", "দুয়োফাল কাষৰীয়া।")], [
        lab(f"{p}.u3.s1", B("Circles have no ends", "বৃত্তৰ মূৰ নাই"), B("With no ends, fix one person and build around them. Seat A, then the rest.", "মূৰ নাই, এজনক ঠিক কৰি তাৰ চাৰিওফালে বনোৱা।"), {"kind": "seats", "names": ["A", "B", "C", "D"], "round": True}, [
            task(B("Seat A, B, C, D clockwise from the top.", "ওপৰৰ পৰা ঘড়ীৰ দিশে A, B, C, D বহুওৱা।"), {"code": 1234}, B("A is opposite C, and B is opposite D.", "A ৰ সন্মুখত C, B ৰ সন্মুখত D।")),
        ]),
        diagram(f"{p}.u3.s2", B("Left in a circle", "বৃত্তত বাওঁ"), [B("Facing the centre, your left neighbour is the next seat clockwise.", "কেন্দ্ৰমুখী হ'লে বাওঁ কাষৰীয়া ঘড়ীৰ দিশৰ পিছৰ আসন।")], "flow", [B("Face centre", "কেন্দ্ৰমুখী"), B("Left = clockwise", "বাওঁ = ঘড়ীৰ দিশ"), B("Right = anticlockwise", "সোঁ = ওলোটা")]),
        explore(f"{p}.u3.q1", ROUND, seat_q, [(B("Four face the centre. Put P at the top. Q is opposite P. R is on P's left.", "চাৰিজন কেন্দ্ৰমুখী। P ওপৰত। Q, P ৰ সন্মুখত। R, P ৰ বাওঁফালে।"), ["P", "Q", "R", "S"], ["P", "R", "Q", "S"], True, B("Left is clockwise, so R follows P.", "বাওঁ ঘড়ীৰ দিশে, গতিকে R, P ৰ পিছত।")), (B("Four face the centre. Put A at the top. C is on A's right. B is opposite A.", "চাৰিজন কেন্দ্ৰমুখী। A ওপৰত। C, A ৰ সোঁফালে। B, A ৰ সন্মুখত।"), ["A", "B", "C", "D"], ["A", "D", "B", "C"], True, B("Right is anticlockwise, so C sits last.", "সোঁ ঘড়ীৰ ওলোটা, গতিকে C শেষত।"))]),
        tf(f"{p}.u3.q2", ROUND, B("Facing the centre, your left neighbour is the next seat clockwise.", "কেন্দ্ৰমুখী হ'লে বাওঁ কাষৰীয়া ঘড়ীৰ দিশৰ পিছৰ আসন।"), True, B("Try it at a round table.", "ঘূৰণীয়া মেজত চোৱা।"), ("r-m-sidecircle", CIRC)),
        match(f"{p}.u3.q3", ROUND, B("Clockwise A B C D, facing centre: match", "ঘড়ীৰ দিশে A B C D, কেন্দ্ৰমুখী: মিলোৱা"), [[B("Opposite A", "A ৰ সন্মুখত"), same("C")], [B("Left of A", "A ৰ বাওঁফালে"), same("B")], [B("Right of A", "A ৰ সোঁফালে"), same("D")]], B("Left is clockwise.", "বাওঁ ঘড়ীৰ দিশে।")),
        solve(f"{p}.u3.q4", ROUND, lambda n: {"q": B(f"{n} people sit evenly around a table. How many seats lie between two people sitting opposite, on one side?", f"{n} জন ঘূৰণীয়া মেজত সমানে বহিছে। সন্মুখা-সন্মুখি দুজনৰ মাজত এফালে কিমান আসন?"), "answer": str(n // 2 - 1), "why": B(f"{n} ÷ 2 − 1 = {n // 2 - 1}.", f"{n} ÷ 2 − 1 = {n // 2 - 1}।")}, [(8,), (10,), (12,)]),
        order(f"{p}.u3.q5", ROUND, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Fix one person", "এজনক ঠিক"), B("Note the facing", "মুখ চোৱা"), B("Add neighbours", "কাষৰীয়া যোগ"), B("Check opposites", "সন্মুখ চোৱা")], B("Fix first, then build.", "ঠিক কৰি বনোৱা।")),
    ])
    u4 = unit("u4", B("Who has what", "কাৰ কি আছে"), "star", [B("Draw a table: people by things.", "তালিকা আঁকা: ব্যক্তি আৰু বস্তু।"), B("Cross out what is ruled out.", "বাদ পৰাখিনি কাটা।"), B("One option left is an answer.", "এটা বাকী থাকিলে উত্তৰ।"), B("Each answer removes more.", "প্ৰতিটো উত্তৰে আৰু কমায়।")], [
        diagram(f"{p}.u4.s1", B("A table beats memory", "তালিকা স্মৃতিতকৈ ভাল"), [B("With three people and three sports, a small grid does the thinking.", "তিনি ব্যক্তি, তিনি খেলত সৰু তালিকাই চিন্তা কৰে।")], "flow", [B("Draw a grid", "তালিকা আঁকা"), B("Cross out", "কাটা"), B("Read what is left", "বাকী পঢ়া")]),
        diagram(f"{p}.u4.s2", B("Each tick clears a line", "প্ৰতিটো টিকে শাৰী মচে"), [B("Once A plays chess, nobody else does and A plays nothing else.", "A য়ে দবা খেলিলে আন কোনেও নেখেলে, A য়ে আন নেখেলে।")], "flow", [B("Tick one", "এটা টিক"), B("Clear the row", "শাৰী মচা"), B("Clear the column", "স্তম্ভ মচা")]),
        stepwise(f"{p}.u4.q1", MATCHA, lambda a, b, c, x, y, z: {"q": B(f"{a}, {b} and {c} play {x[0]}, {y[0]} and {z[0]}, one each. {a} does not play {x[0]} or {y[0]}. {b} does not play {x[0]}. Who plays {x[0]}?", f"{a}, {b}, {c} এ {x[1]}, {y[1]}, {z[1]} এটাকৈ খেলে। {a} য়ে {x[1]} বা {y[1]} নেখেলে। {b} য়ে {x[1]} নেখেলে। {x[1]} কোনে খেলে?"), "parts": [
            part(B(f"What does {a} play?", f"{a} য়ে কি খেলে?"), B(*z), [B(*x), B(*y)], B("Only one is left.", "এটাহে বাকী।"), sid=f"{p}.u4.q1"),
            part(B(f"Who plays {x[0]}?", f"{x[1]} কোনে খেলে?"), same(c), [same(a), same(b)], B(f"{a} and {b} are ruled out.", f"{a} আৰু {b} বাদ।"), sid=f"{p}.u4.q1"),
        ], "why": B(f"{c} plays {x[0]}.", f"{c} য়ে {x[1]} খেলে।")}, [("Ria", "Tina", "Maya", ("chess", "দবা"), ("tennis", "টেনিছ"), ("cricket", "ক্ৰিকেট")), ("Bipul", "Dipen", "Hiren", ("hockey", "হকী"), ("football", "ফুটবল"), ("carrom", "কেৰম"))]),
        tf(f"{p}.u4.q2", MATCHA, B("If each person has one item, a tick clears its row and column.", "প্ৰত্যেকৰ এটা বস্তু হ'লে টিকে শাৰী আৰু স্তম্ভ মচে।"), True, B("That is why grids work.", "সেয়ে তালিকা কাম কৰে।")),
        match(f"{p}.u4.q3", MATCHA, B("A, B, C with red, blue, green. A not red or blue. B not red. Match", "A, B, C; ৰঙা, নীলা, সেউজীয়া। A ৰঙা বা নীলা নহয়। B ৰঙা নহয়। মিলোৱা"), [[same("A"), B("Green", "সেউজীয়া")], [same("B"), B("Blue", "নীলা")], [same("C"), B("Red", "ৰঙা")]], B("A is fixed first.", "A আগতে ঠিক।")),
        order(f"{p}.u4.q4", MATCHA, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Draw the grid", "তালিকা"), B("Cross out clues", "ইংগিত কাটা"), B("Tick the forced", "নিশ্চিত টিক"), B("Repeat", "পুনৰ")], B("Forced ticks spread.", "নিশ্চিত টিকে আগবাঢ়ে।")),
        solve(f"{p}.u4.q5", MATCHA, lambda p_, t: {"q": B(f"How many cells has a grid of {p_} people by {t} sports?", f"{p_} ব্যক্তি আৰু {t} খেলৰ তালিকাত কিমান ঘৰ?"), "answer": str(p_ * t), "why": B(f"{p_} × {t}.", f"{p_} × {t}।")}, [(3, 3), (4, 4), (5, 3)]),
    ])
    test = {"id": "test", "title": B("Arrangement test", "সজ্জাৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", FIXED, seat_q, [(B("Left to right: K is first, and M is immediately left of L.", "বাওঁৰ পৰা: K প্ৰথম, M, L ৰ ঠিক বাওঁফালে।"), ["K", "L", "M"], ["K", "M", "L"], False, B("K, M, L.", "K, M, L।")), (B("Left to right: U is last, and V is first.", "বাওঁৰ পৰা: U শেষত, V প্ৰথম।"), ["U", "V", "W"], ["V", "W", "U"], False, B("V, W, U.", "V, W, U।"))]),
        tf(f"{p}.t.q2", LINE, B("'Between' needs someone on both sides.", "'মাজত' মানে দুয়োফালে কোনোবা।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q3", ROUND, B("Facing the centre, right is clockwise.", "কেন্দ্ৰমুখী হ'লে সোঁ ঘড়ীৰ দিশে।"), False, B("Right is anticlockwise.", "সোঁ ঘড়ীৰ ওলোটা।"), ("r-m-sidecircle", CIRC)),
        solve(f"{p}.t.q4", LINE, lambda a, b: {"q": B(f"{a} on the left and {b} on the right of X. How many in the row?", f"X ৰ বাওঁফালে {a}, সোঁফালে {b}। মুঠ?"), "answer": str(a + b + 1), "why": B("Count X too.", "X কো গণা।")}, [(6, 9), (5, 3)]),
        tf(f"{p}.t.q5", MATCHA, B("A grid makes matching puzzles easier.", "তালিকাই মিলোৱা সাঁথৰ সহজ কৰে।"), True, B("It holds what memory drops.", "ই স্মৃতিৰ কাম কৰে।")),
        tf(f"{p}.t.q6", FIXED, B("Place clues that fix a seat first.", "আসন ঠিক কৰা ইংগিত আগতে।"), True, B("They anchor the rest.", "ই বাকীখিনি ধৰি ৰাখে।")),
    ]}
    return {"id": "rs-12-arrangement", "no": 12, "slug": "arrangement", "title": B("Arrangements", "সজ্জা"), "reign": B("Rows, circles, matching", "শাৰী, বৃত্ত, মিলোৱা"), "units": [u1, u2, u3, u4], "test": test}


DN = [("Sunday", "দেওবাৰ"), ("Monday", "সোমবাৰ"), ("Tuesday", "মঙ্গলবাৰ"), ("Wednesday", "বুধবাৰ"), ("Thursday", "বৃহস্পতিবাৰ"), ("Friday", "শুক্ৰবাৰ"), ("Saturday", "শনিবাৰ")]


def day_after(d, n):
    e = (d + n) % 7
    return {"q": B(f"Today is {DN[d][0]}. Which day comes in {n} days? Step the wheel using the remainder.", f"আজি {DN[d][1]}। {n} দিনৰ পিছত কি বাৰ? ভাগশেষেৰে চকৰি আগবঢ়োৱা।"), "widget": {"kind": "oddday", "start": d}, "target": e, "answerText": B(*DN[e]), "why": B(f"{n} leaves {n % 7} after sevens, so {DN[e][0]}.", f"{n} ৰ ভাগশেষ {n % 7}, গতিকে {DN[e][1]}।")}


def year_next(d, leap):
    e = (d + (2 if leap else 1)) % 7
    return {"q": B(f"A date falls on {DN[d][0]}. On which day is it one year later, with {'a' if leap else 'no'} 29 February in between?", f"এটা তাৰিখ {DN[d][1]}। মাজত {'২৯ ফেব্ৰুৱাৰী থাকিলে' if leap else '২৯ ফেব্ৰুৱাৰী নাথাকিলে'} এবছৰ পিছত কি বাৰ?"), "widget": {"kind": "oddday", "start": d}, "target": e, "answerText": B(*DN[e]), "traps": [{"val": (d + (1 if leap else 2)) % 7, "tag": "r-m-leap", "why": LEAP}], "why": B(f"{'A leap year adds 2 days.' if leap else 'An ordinary year adds 1 day.'}", f"{'অধিবৰ্ষে 2 দিন আগবঢ়ায়।' if leap else 'সাধাৰণ বছৰে 1 দিন আগবঢ়ায়।'}")}


def angle(h, m):
    a = abs(30 * h - 5.5 * m)
    a = min(a, 360 - a)
    return {"q": B(f"What is the angle between the hands at {h}:{m:02d}?", f"{h}:{m:02d} ত কাঁটাৰ মাজৰ কোণ কিমান?"), "answer": str(int(a)) if a == int(a) else str(a), "suffix": B("°", "°"), "why": B(f"|30 × {h} − 5.5 × {m}| = {a:g}.", f"|30 × {h} − 5.5 × {m}| = {a:g}।"), "traps": [{"ans": str(abs(30 * h - 6 * m)), "tag": "r-m-hourhand", "why": HOUR}] if abs(30 * h - 6 * m) != a else []}


def lesson_calendar():
    p = "rs13"
    u1 = unit("u1", B("Odd days", "অতিৰিক্ত দিন"), "star", [B("Days repeat every 7.", "দিন 7 ত ঘূৰি আহে।"), B("Only the remainder matters.", "কেৱল ভাগশেষৰ মূল্য আছে।"), B("Move forward by the remainder.", "ভাগশেষ আগবাঢ়া।"), B("Go backward by subtracting.", "বিয়োগেৰে পিছলৈ।")], [
        lab(f"{p}.u1.s1", B("A week is a wheel", "সপ্তাহ এটা চকৰি"), B("Seven days later is the same day. So 15 days is just 1 day ahead.", "সাত দিন পিছত একে বাৰ। গতিকে 15 দিন মানে 1 দিন আগ।"), {"kind": "oddday", "start": 1}, [
            task(B("From Monday, go 3 days on.", "সোমবাৰৰ পৰা 3 দিন আগবাঢ়া।"), {"day": 4}, B("Thursday. Now 10 days on is also Thursday.", "বৃহস্পতিবাৰ। 10 দিন পিছতো একে।")),
        ]),
        diagram(f"{p}.u1.s2", B("Divide by seven", "7 ৰে হৰণ"), [B("Throw away whole weeks. Keep what is left.", "গোটা সপ্তাহ বাদ দিয়া। বাকীখিনি ৰাখা।")], "flow", [same("45 days"), same("45 ÷ 7 = 6 r 3"), B("3 ahead", "3 আগ")]),
        explore(f"{p}.u1.q1", ODDD, day_after, [(1, 15), (3, 30), (5, 50), (0, 100)]),
        solve(f"{p}.u1.q2", ODDD, lambda n: {"q": B(f"What is the remainder of {n} days after whole weeks?", f"গোটা সপ্তাহ বাদ দিলে {n} দিনৰ ভাগশেষ কিমান?"), "answer": str(n % 7), "why": B(f"{n} ÷ 7 leaves {n % 7}.", f"{n} ÷ 7 ৰ ভাগশেষ {n % 7}।")}, [(40,), (66,), (92,)]),
        tf(f"{p}.u1.q3", ODDD, B("21 days after a Friday is a Friday.", "শুক্ৰবাৰৰ 21 দিন পিছত শুক্ৰবাৰ।"), True, B("21 is three whole weeks.", "21 মানে তিনি সপ্তাহ।")),
        match(f"{p}.u1.q4", ODDD, B("From Sunday, match", "দেওবাৰৰ পৰা মিলোৱা"), [[B("8 days on", "8 দিন পিছত"), B("Monday", "সোমবাৰ")], [B("16 days on", "16 দিন পিছত"), B("Tuesday", "মঙ্গলবাৰ")], [B("24 days on", "24 দিন পিছত"), B("Wednesday", "বুধবাৰ")]], B("Use remainders.", "ভাগশেষ ব্যৱহাৰ।")),
        order(f"{p}.u1.q5", ODDD, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Count days", "দিন গণা"), B("Divide by 7", "7 ৰে হৰণ"), B("Keep the remainder", "ভাগশেষ ৰাখা"), B("Move ahead", "আগবাঢ়া")], B("Remainder decides.", "ভাগশেষে ঠিক কৰে।")),
    ])
    u2 = unit("u2", B("Across years", "বছৰে বছৰে"), "star", [B("An ordinary year has 1 odd day.", "সাধাৰণ বছৰত 1 অতিৰিক্ত দিন।"), B("A leap year has 2.", "অধিবৰ্ষত 2।"), B("Leap years divide by 4.", "অধিবৰ্ষ 4 ৰে হৰণ হয়।"), B("Century years need 400.", "শতাব্দী বছৰত 400 লাগে।")], [
        diagram(f"{p}.u2.s1", B("Why a year shifts the day", "বছৰে বাৰ কিয় সলায়"), [B("365 days is 52 weeks and 1 day, so dates drift one day each year.", "365 দিন মানে 52 সপ্তাহ আৰু 1 দিন, সেয়ে তাৰিখ এদিন আগবাঢ়ে।")], "flow", [same("365 ÷ 7"), same("52 r 1"), B("1 day on", "1 দিন আগ")]),
        diagram(f"{p}.u2.s2", B("Spotting a leap year", "অধিবৰ্ষ চিনা"), [B("2024 divides by 4. 1900 does not divide by 400, so it is not leap. 2000 is.", "2024, 4 ৰে হৰণ হয়। 1900, 400 ৰে নহয়, গতিকে অধিবৰ্ষ নহয়। 2000 অধিবৰ্ষ।")], "grid", [B("2024: leap", "2024: অধিবৰ্ষ"), B("1900: not leap", "1900: নহয়"), B("2000: leap", "2000: অধিবৰ্ষ")]),
        explore(f"{p}.u2.q1", CDATE, year_next, [(1, False), (2, True), (5, False), (4, True)]),
        tf(f"{p}.u2.q2", CDATE, B("1900 was a leap year.", "1900 অধিবৰ্ষ আছিল।"), False, B("Century years must divide by 400.", "শতাব্দী বছৰ 400 ৰে হৰণ হ'ব লাগে।"), ("r-m-leap", LEAP)),
        match(f"{p}.u2.q3", CDATE, B("Match the year to its kind", "বছৰক ধৰণৰ লগত মিলোৱা"), [[same("2028"), B("Leap", "অধিবৰ্ষ")], [same("2027"), B("Ordinary", "সাধাৰণ")], [same("2100"), B("Century, not leap", "শতাব্দী, অধিবৰ্ষ নহয়")]], B("Test by 4, then 400.", "4, তাৰ পিছত 400।")),
        solve(f"{p}.u2.q4", CDATE, lambda a, b: {"q": B(f"How many leap years lie from {a} to {b}, including both?", f"{a} ৰ পৰা {b} লৈ (দুয়োটা ধৰি) অধিবৰ্ষ কিমান?"), "answer": str(sum(1 for y in range(a, b + 1) if (y % 4 == 0 and y % 100) or y % 400 == 0)), "why": B("Count the years that divide by 4.", "4 ৰে হৰণ হোৱা বছৰ গণা।")}, [(2001, 2020), (2010, 2030), (2000, 2012)]),
        stepwise(f"{p}.u2.q5", CDATE, lambda y: {"q": B(f"Is {y} a leap year?", f"{y} অধিবৰ্ষ নেকি?"), "parts": [
            part(B("Century year?", "শতাব্দী বছৰ?"), B("Yes" if y % 100 == 0 else "No", "হয়" if y % 100 == 0 else "নহয়"), [B("No" if y % 100 == 0 else "Yes", "নহয়" if y % 100 == 0 else "হয়"), B("Cannot tell", "ক'ব নোৱাৰি")], B("Ends in 00?", "শেষত 00?"), sid=f"{p}.u2.q5"),
            part(B("Leap?", "অধিবৰ্ষ?"), B("Yes" if (y % 4 == 0 and y % 100) or y % 400 == 0 else "No", "হয়" if (y % 4 == 0 and y % 100) or y % 400 == 0 else "নহয়"), [B("No" if (y % 4 == 0 and y % 100) or y % 400 == 0 else "Yes", "নহয়" if (y % 4 == 0 and y % 100) or y % 400 == 0 else "হয়"), B("Cannot tell", "ক'ব নোৱাৰি")], LEAP, tag="r-m-leap", sid=f"{p}.u2.q5"),
        ], "why": B("Test by 4, or by 400 for a century.", "4 ৰে, শতাব্দী হ'লে 400 ৰে পৰীক্ষা।")}, [(2024,), (1900,), (2000,)]),
    ])
    u3 = unit("u3", B("Angles on a clock", "ঘড়ীৰ কোণ"), "star", [B("The minute hand moves 6° a minute.", "মিনিটৰ কাঁটা মিনিটত 6°।"), B("The hour hand moves 0.5° a minute.", "ঘণ্টাৰ কাঁটা মিনিটত 0.5°।"), B("Angle = |30H − 5.5M|.", "কোণ = |30H − 5.5M|।"), B("Take the smaller of the two angles.", "দুটাৰ সৰুটো লোৱা।")], [
        lab(f"{p}.u3.s1", B("The hour hand creeps", "ঘণ্টাৰ কাঁটা লাহে লৰে"), B("At 3:00 the hands are 90° apart. Run the clock and watch the hour hand creep.", "3:00 ত কোণ 90°। ঘড়ী চলাই ঘণ্টাৰ কাঁটা চোৱা।"), {"kind": "hands", "hour": 3, "angle": True}, [
            task(B("Run to 3:30.", "3:30 লৈ চলোৱা।"), {"min": 30}, B("The angle is 75°, not 90°, because the hour hand moved 15°.", "কোণ 75°, 90° নহয়, কাৰণ ঘণ্টাৰ কাঁটা 15° গ'ল।")),
        ]),
        diagram(f"{p}.u3.s2", B("One formula", "এটা সূত্ৰ"), [B("Each hour mark is 30°, and the gap closes at 5.5° a minute.", "প্ৰতি ঘণ্টা 30°, ব্যৱধান মিনিটত 5.5° কমে।")], "flow", [same("30 × H"), same("5.5 × M"), B("Difference", "পাৰ্থক্য")]),
        solve(f"{p}.u3.q1", CLOCK, angle, [(3, 30), (4, 20), (6, 30), (2, 40)]),
        solve(f"{p}.u3.q2", CLOCK, lambda h: {"q": B(f"What is the angle between the hands at exactly {h}:00?", f"ঠিক {h}:00 ত কাঁটাৰ কোণ কিমান?"), "answer": str(min(30 * h, 360 - 30 * h)), "suffix": B("°", "°"), "why": B("30° per hour mark.", "প্ৰতি ঘণ্টা 30°।")}, [(2,), (5,), (10,)]),
        tf(f"{p}.u3.q3", CLOCK, B("At 6:30 the hands point the same way.", "6:30 ত কাঁটা দুটা একে ফালে।"), False, B("The hour hand has moved 15° past 6.", "ঘণ্টাৰ কাঁটা 6 ৰ পৰা 15° আগবাঢ়িছে।"), ("r-m-hourhand", HOUR)),
        match(f"{p}.u3.q4", CLOCK, B("Match the rate", "হাৰ মিলোৱা"), [[B("Minute hand", "মিনিটৰ কাঁটা"), same("6° / min")], [B("Hour hand", "ঘণ্টাৰ কাঁটা"), same("0.5° / min")], [B("Closing speed", "নিকা হাৰ"), same("5.5° / min")]], B("Subtract the rates.", "হাৰ বিয়োগ।")),
        order(f"{p}.u3.q5", CLOCK, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find 30 × H", "30 × H"), B("Find 5.5 × M", "5.5 × M"), B("Subtract", "বিয়োগ"), B("Take the smaller angle", "সৰু কোণ")], B("Formula, then smaller angle.", "সূত্ৰ, তাৰ পিছত সৰু কোণ।")),
    ])
    u4 = unit("u4", B("When the hands meet", "কাঁটা লগ লগা সময়"), "star", [B("Hands meet 11 times in 12 hours.", "12 ঘণ্টাত 11 বাৰ লগ লাগে।"), B("Hands meet 22 times a day.", "দিনত 22 বাৰ।"), B("They are opposite 22 times a day.", "দিনত 22 বাৰ বিপৰীত।"), B("A right angle occurs 44 times a day.", "দিনত 44 বাৰ সমকোণ।")], [
        lab(f"{p}.u4.s1", B("Meeting after three o'clock", "তিনিটাৰ পিছত সাক্ষাৎ"), B("Run the clock from 3:00 until the hands nearly meet. It happens just after 3:16.", "3:00 ৰ পৰা কাঁটা ওচৰ নোহোৱালৈ চলোৱা। 3:16 ৰ অলপ পিছত।"), {"kind": "hands", "hour": 3, "angle": True}, [
            task(B("Run to 3:16.", "3:16 লৈ চলোৱা।"), {"min": 16}, B("The angle is only 2°. They meet moments later.", "কোণ মাত্ৰ 2°। অলপ পিছতে লগ লাগে।")),
        ]),
        diagram(f"{p}.u4.s2", B("Why 11 and not 12", "12 নহয়, 11 কিয়"), [B("Between 11 and 1 they meet only once, at 12. So 12 hours hold 11 meetings.", "11 আৰু 1 ৰ মাজত এবাৰহে, 12 ত। গতিকে 12 ঘণ্টাত 11 বাৰ।")], "flow", [B("12 hours", "12 ঘণ্টা"), B("11 meetings", "11 সাক্ষাৎ"), B("24 hours: 22", "24 ঘণ্টা: 22")]),
        explore(f"{p}.u4.q1", MEET, lambda h, m: {"q": B(f"Run the clock to the minute nearest when the hands first meet after {h}:00.", f"{h}:00 ৰ পিছত কাঁটা প্ৰথম লগ লগাৰ ওচৰৰ মিনিটলৈ চলোৱা।"), "widget": {"kind": "hands", "hour": h, "angle": True}, "target": m, "answerText": B(f"{h}:{m:02d}", f"{h}:{m:02d}"), "why": B("The gap closes at 5.5° a minute.", "ব্যৱধান মিনিটত 5.5° কমে।")}, [(2, 11), (4, 22), (5, 27)]),
        tf(f"{p}.u4.q2", MEET, B("The hands meet 24 times a day.", "দিনত 24 বাৰ কাঁটা লগ লাগে।"), False, B("It is 22 times.", "22 বাৰ।")),
        match(f"{p}.u4.q3", MEET, B("In 24 hours, match", "24 ঘণ্টাত মিলোৱা"), [[B("Hands together", "কাঁটা একেলগে"), same(22)], [B("Hands opposite", "কাঁটা বিপৰীত"), same("22 more")], [B("Right angles", "সমকোণ"), same(44)]], B("Know these three.", "তিনিটা মনত ৰাখা।")),
        solve(f"{p}.u4.q4", MEET, lambda h: {"q": B(f"How many times do the hands meet in {h} hours?", f"{h} ঘণ্টাত কাঁটা কিমানবাৰ লগ লাগে?"), "answer": str(h * 11 // 12), "why": B("11 times per 12 hours.", "12 ঘণ্টাত 11 বাৰ।")}, [(12,), (24,), (48,)]),
        order(f"{p}.u4.q5", MEET, B("Smallest count first", "সৰু সংখ্যা আগতে"), [same(11), same(22), same(44)], B("12 hours, 24 hours, right angles.", "12 ঘণ্টা, 24 ঘণ্টা, সমকোণ।")),
    ])
    test = {"id": "test", "title": B("Calendar and clock test", "কেলেণ্ডাৰ আৰু ঘড়ীৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", ODDD, day_after, [(2, 26), (6, 60)]),
        explore(f"{p}.t.q2", CDATE, year_next, [(3, False), (0, True)]),
        solve(f"{p}.t.q3", CLOCK, angle, [(9, 0), (3, 40)]),
        tf(f"{p}.t.q4", CDATE, B("2000 was a leap year.", "2000 অধিবৰ্ষ আছিল।"), True, B("It divides by 400.", "ই 400 ৰে হৰণ হয়।")),
        tf(f"{p}.t.q5", MEET, B("Hands meet 11 times in 12 hours.", "12 ঘণ্টাত 11 বাৰ লগ লাগে।"), True, B("Not 12.", "12 নহয়।")),
        tf(f"{p}.t.q6", ODDD, B("14 days after Tuesday is Tuesday.", "মঙ্গলবাৰৰ 14 দিন পিছত মঙ্গলবাৰ।"), True, B("Two weeks.", "দুই সপ্তাহ।")),
    ]}
    return {"id": "rs-13-calendar-clock", "no": 13, "slug": "calendar-clock", "title": B("Calendar and clocks", "কেলেণ্ডাৰ আৰু ঘড়ী"), "reign": B("Odd days, leap years, angles", "অতিৰিক্ত দিন, অধিবৰ্ষ, কোণ"), "units": [u1, u2, u3, u4], "test": test}


def mod(fn):
    return type("L", (), {"lesson": staticmethod(fn)})


LESSONS = [mod(lesson_blood), mod(lesson_rank), mod(lesson_arrange), mod(lesson_calendar)]
