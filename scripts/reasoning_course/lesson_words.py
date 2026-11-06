"""Lessons 4 and 5: Analogy and Odd one out. Written by hand: each pair must hold in both languages."""
from math_kit import B, match, mcq, odd, order, part, solve, stepwise, tf, unit, with_variants
from math_lessons_c import diagram
from reason_kit import AZ, enc, inlines, same

NAME = "r-relname"; PAIR = "r-relpair"; LETT = "r-relletter"; NUMB = "r-relnum"; TYPE = "r-reltype"; ASSOC = "r-relassoc"
GROUP = "r-oddgroup"; ODDN = "r-oddnum"; ODDL = "r-oddletter"; ODDP = "r-oddpair"; PROP = "r-oddprop"; SKIM = "r-oddskim"
SKILLS = {NAME: ("analogy", B("Name the relation", "সম্পৰ্কৰ নাম"), []), PAIR: ("analogy", B("Word pairs", "শব্দ যোৰ"), [NAME]), TYPE: ("analogy", B("Kinds of relation", "সম্পৰ্কৰ ধৰণ"), [NAME]), LETT: ("analogy", B("Letter analogies", "আখৰৰ সাদৃশ্য"), []), NUMB: ("analogy", B("Number analogies", "সংখ্যাৰ সাদৃশ্য"), []), ASSOC: ("analogy", B("What goes with what", "কিহৰ লগত কি"), [NAME]),
          GROUP: ("odd-one-out", B("Find the group", "গোট বিচৰা"), []), PROP: ("odd-one-out", B("Find the deeper property", "গভীৰ গুণ বিচৰা"), [GROUP]), ODDN: ("odd-one-out", B("Odd number out", "বেলেগ সংখ্যা"), []), ODDL: ("odd-one-out", B("Odd letters out", "বেলেগ আখৰ"), []), ODDP: ("odd-one-out", B("Odd pair out", "বেলেগ যোৰ"), [GROUP]), SKIM: ("odd-one-out", B("Check every option", "সকলো বিকল্প চোৱা"), [GROUP])}
TAGS = {"r-m-topic": (NAME, B("Matching the topic, not the relation", "সম্পৰ্কৰ সলনি বিষয় মিলোৱা")), "r-m-reverse": (PAIR, B("Reversing the relation", "সম্পৰ্ক ওলোটোৱা")), "r-m-surface": (GROUP, B("Picking a surface difference", "ওপৰুৱা পাৰ্থক্য বাছনি"))}
TOPIC = B("That word shares the topic but not the relation. State the relation in a sentence.", "সেই শব্দৰ বিষয় একে, সম্পৰ্ক নহয়। সম্পৰ্কটো এটা বাক্যত কোৱা।")
REV = B("Keep the same direction: if the first word is the worker, the third is too.", "দিশ একে ৰাখা: প্ৰথম শব্দ কৰ্মী হ'লে তৃতীয়টোও কৰ্মী।")
SURF = B("Look for what the other three share, not how one looks.", "এটাৰ চেহেৰা নহয়, বাকী তিনিটাৰ উমৈহতীয়া গুণ চোৱা।")


def W(en, as_):
    return B(en, as_)


def a_row(a, b, c, right, wrong, why):
    """a : b :: c : ?"""
    return (B(f"{a[0]} is to {b[0]} as {c[0]} is to", f"{a[1]}ৰ লগত {b[1]}ৰ যি সম্পৰ্ক, {c[1]}ৰ লগত"), B(".", " ৰ সেই সম্পৰ্ক।"), B(*right), [B(*x) for x in wrong], why)


def rel_steps(sid, a, b, c, rel, right, wrongrel, wrong):
    return {"q": B(f"{a[0]} : {b[0]} :: {c[0]} : ?", f"{a[1]} : {b[1]} :: {c[1]} : ?"), "parts": [
        part(B("The relation?", "সম্পৰ্ক?"), B(*rel), [B(*x) for x in wrongrel], B("Say it as a sentence.", "এটা বাক্যত কোৱা।"), tag="r-m-topic", sid=sid),
        part(B("So the answer?", "তেন্তে উত্তৰ?"), B(*right), [B(*x) for x in wrong], B("Apply the same relation.", "একে সম্পৰ্ক প্ৰয়োগ কৰা।"), sid=sid),
    ], "why": B(f"The relation holds for {c[0]} and {right[0]}.", f"{c[1]} আৰু {right[1]} ত একে সম্পৰ্ক।")}


def l_analogy(a, k, c):
    return {"q": B(f"{a} : {enc(a, k)} :: {c} : ?", f"{a} : {enc(a, k)} :: {c} : ?"), "answer": enc(c, k), "why": B(f"Every letter moves {k:+d}.", f"প্ৰতিটো আখৰ {k:+d} সৰে।"), "traps": [{"ans": enc(c, -k), "tag": "r-m-reverse", "why": REV}]}


def n_square(a, c):
    return {"q": B(f"{a} : {a * a} :: {c} : ?", f"{a} : {a * a} :: {c} : ?"), "answer": str(c * c), "why": B("The second number is the square of the first.", "দ্বিতীয় সংখ্যাটো প্ৰথমটোৰ বৰ্গ।")}


def n_rule(a, m, s_, c):
    return {"q": B(f"{a} : {a * m + s_} :: {c} : ?", f"{a} : {a * m + s_} :: {c} : ?"), "answer": str(c * m + s_), "hints": [B(f"Try multiplying by {m}.", f"{m} ৰে পূৰণ কৰি চোৱা।")], "why": B(f"The rule is × {m}, then {s_:+d}.", f"নিয়ম × {m}, তাৰ পিছত {s_:+d}।")}


def lesson_analogy():
    p = "rs4"
    # (word, relation sentence pairs) are hand-written so that both languages keep the relation.
    u1 = unit("u1", B("Say the relation aloud", "সম্পৰ্কটো মাতি কোৱা"), "star", [B("First name the link between the first pair.", "প্ৰথমে প্ৰথম যোৰৰ সম্পৰ্ক কোৱা।"), B("Put it in a short sentence.", "চুটি বাক্যত কোৱা।"), B("Then apply the same sentence.", "তাৰ পিছত একে বাক্য প্ৰয়োগ কৰা।"), B("Same topic does not mean same relation.", "একে বিষয় মানে একে সম্পৰ্ক নহয়।")], [
        diagram(f"{p}.u1.s1", B("The sentence does the work", "বাক্যই কাম কৰে"), [B("Doctor : Hospital. Say it: a doctor works in a hospital. Now test each option.", "চিকিৎসক : চিকিৎসালয়। কোৱা: চিকিৎসকে চিকিৎসালয়ত কাম কৰে। এতিয়া বিকল্প চোৱা।")], "flow", [B("First pair", "প্ৰথম যোৰ"), B("A sentence", "এটা বাক্য"), B("Test the option", "বিকল্প চোৱা")]),
        diagram(f"{p}.u1.s2", B("Beware the topic trap", "বিষয়ৰ ফান্দ"), [B("Teacher : School wants Farmer : Field, not Farmer : Rice. One is a workplace, the other a product.", "শিক্ষক : বিদ্যালয়ৰ বাবে খেতিয়ক : পথাৰ, খেতিয়ক : ধান নহয়। এটা কৰ্মস্থান, আনটো উৎপাদন।")], "grid", [B("Workplace: field", "কৰ্মস্থান: পথাৰ"), B("Product: rice", "উৎপাদন: ধান")]),
        inlines(f"{p}.u1.q1", NAME, [a_row(("Doctor", "চিকিৎসক"), ("Hospital", "চিকিৎসালয়"), ("Teacher", "শিক্ষক"), ("School", "বিদ্যালয়"), [("Book", "কিতাপ"), ("Student", "ছাত্ৰ")], B("A workplace.", "কৰ্মস্থান।")), a_row(("Bird", "চৰাই"), ("Nest", "বাঁহ"), ("Bee", "মৌমাখি"), ("Hive", "মৌচাক"), [("Honey", "মৌ"), ("Flower", "ফুল")], B("A home.", "বাসস্থান।")), a_row(("Pen", "কলম"), ("Write", "লিখা"), ("Knife", "কটাৰী"), ("Cut", "কটা"), [("Sharp", "চোকা"), ("Steel", "তীখা")], B("A tool and its use.", "সঁজুলি আৰু ব্যৱহাৰ।"))]),
        with_variants({"id": f"{p}.u1.q2", "type": "stepwise", "skill": NAME}, lambda *a: rel_steps(f"{p}.u1.q2", *a), [(("Fish", "মাছ"), ("Water", "পানী"), ("Camel", "উট"), ("It lives there", "তাত বাস কৰে"), ("Desert", "মৰুভূমি"), [("It eats it", "তাক খায়"), ("It looks alike", "একে দেখি")], [("Hump", "কুঁজ"), ("Grass", "ঘাঁহ")]), (("Eye", "চকু"), ("See", "চোৱা"), ("Ear", "কাণ"), ("Its function", "ইয়াৰ কাম"), ("Hear", "শুনা"), [("Its shape", "ইয়াৰ আকৃতি"), ("Its colour", "ইয়াৰ ৰং")], [("Head", "মূৰ"), ("Sound", "শব্দ")])]),
        tf(f"{p}.u1.q3", NAME, B("Farmer : Rice has the same relation as Teacher : School.", "খেতিয়ক : ধান আৰু শিক্ষক : বিদ্যালয়ৰ সম্পৰ্ক একে।"), False, B("Rice is a product; school is a workplace.", "ধান উৎপাদন; বিদ্যালয় কৰ্মস্থান।"), ("r-m-topic", TOPIC)),
        match(f"{p}.u1.q4", NAME, B("Match the pair to its relation", "যোৰক সম্পৰ্কৰ লগত মিলোৱা"), [[B("Pen, write", "কলম, লিখা"), B("Tool and use", "সঁজুলি, ব্যৱহাৰ")], [B("Cow, calf", "গাই, পোৱালি"), B("Adult and young", "ডাঙৰ, পোৱালি")], [B("Tiger, forest", "বাঘ, হাবি"), B("Animal and home", "জীৱ, বাসস্থান")]], B("Say each in a sentence.", "প্ৰতিটো বাক্যত কোৱা।")),
        order(f"{p}.u1.q5", NAME, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the first pair", "প্ৰথম যোৰ পঢ়া"), B("Make a sentence", "বাক্য বনোৱা"), B("Try each option", "বিকল্প চোৱা"), B("Keep the exact fit", "ঠিক মিলাটো ৰাখা")], B("Sentence before options.", "বিকল্পৰ আগতে বাক্য।")),
    ])
    u2 = unit("u2", B("Keep the direction", "দিশ একে ৰাখা"), "star", [B("Order matters in an analogy.", "সাদৃশ্যত ক্ৰম গুৰুত্বপূৰ্ণ।"), B("Part : Whole cannot match Whole : Part.", "অংশ : গোটা, গোটা : অংশৰ লগত নিমিলে।"), B("Worker : Tool stays in that order.", "কৰ্মী : সঁজুলি ক্ৰমেই থাকে।"), B("Check your answer sits in the same slot.", "উত্তৰ একে ঠাইত আছেনে চোৱা।")], [
        diagram(f"{p}.u2.s1", B("Analogies have a direction", "সাদৃশ্যৰ দিশ আছে"), [B("Wheel : Car is part to whole. So Petal : Flower fits, but Flower : Petal does not.", "চকা : গাড়ী অংশৰ পৰা গোটালৈ। পাহি : ফুল মিলে, ফুল : পাহি নিমিলে।")], "flow", [B("Part", "অংশ"), B("Whole", "গোটা"), B("Same order", "একে ক্ৰম")]),
        diagram(f"{p}.u2.s2", B("Common directions", "সাধাৰণ দিশ"), [B("Most exam relations come from a short list. Learn these.", "পৰীক্ষাৰ বেছিভাগ সম্পৰ্ক এটা চুটি তালিকাৰ পৰা। এইবোৰ শিকা।")], "grid", [B("Part : Whole", "অংশ : গোটা"), B("Worker : Tool", "কৰ্মী : সঁজুলি"), B("Cause : Effect", "কাৰণ : ফল"), B("Young : Adult", "পোৱালি : ডাঙৰ")]),
        inlines(f"{p}.u2.q1", PAIR, [a_row(("Wheel", "চকা"), ("Car", "গাড়ী"), ("Petal", "পাহি"), ("Flower", "ফুল"), [("Garden", "বাগিচা"), ("Scent", "গোন্ধ")], B("Part to whole.", "অংশৰ পৰা গোটা।")), a_row(("Carpenter", "কাঠমিস্ত্ৰী"), ("Saw", "কৰত"), ("Tailor", "দৰ্জী"), ("Needle", "বেজী"), [("Cloth", "কাপোৰ"), ("Shirt", "চোলা")], B("Worker to tool.", "কৰ্মীৰ পৰা সঁজুলি।")), a_row(("Calf", "দামুৰি"), ("Cow", "গৰু"), ("Kid", "ছাগলী পোৱালি"), ("Goat", "ছাগলী"), [("Grass", "ঘাঁহ"), ("Milk", "গাখীৰ")], B("Young to adult.", "পোৱালিৰ পৰা ডাঙৰ।"))]),
        with_variants({"id": f"{p}.u2.q2", "type": "stepwise", "skill": PAIR}, lambda *a: rel_steps(f"{p}.u2.q2", *a), [(("Rain", "বৰষুণ"), ("Flood", "বান"), ("Fire", "জুই"), ("Cause then effect", "কাৰণ, তাৰ পিছত ফল"), ("Ash", "ছাঁই"), [("Part then whole", "অংশ, তাৰ পিছত গোটা"), ("Tool then user", "সঁজুলি, তাৰ পিছত ব্যৱহাৰকাৰী")], [("Match", "জুইশলা"), ("Wood", "কাঠ")]), (("Hand", "হাত"), ("Finger", "আঙুলি"), ("Foot", "ভৰি"), ("Whole then part", "গোটা, তাৰ পিছত অংশ"), ("Toe", "ভৰিৰ আঙুলি"), [("Part then whole", "অংশ, তাৰ পিছত গোটা"), ("Cause then effect", "কাৰণ, তাৰ পিছত ফল")], [("Leg", "ঠেং"), ("Shoe", "জোতা")])]),
        tf(f"{p}.u2.q3", PAIR, B("Tree : Leaf matches Petal : Flower.", "গছ : পাত, পাহি : ফুলৰ লগত মিলে।"), False, B("The first is whole to part; the second is part to whole.", "প্ৰথমটো গোটাৰ পৰা অংশ; দ্বিতীয়টো অংশৰ পৰা গোটা।"), ("r-m-reverse", REV)),
        match(f"{p}.u2.q4", PAIR, B("Match the pair to its direction", "যোৰক দিশৰ লগত মিলোৱা"), [[B("Page, book", "পৃষ্ঠা, কিতাপ"), B("Part : Whole", "অংশ : গোটা")], [B("Cook, ladle", "ৰান্ধনী, হেতা"), B("Worker : Tool", "কৰ্মী : সঁজুলি")], [B("Germ, disease", "বীজাণু, ৰোগ"), B("Cause : Effect", "কাৰণ : ফল")]], B("Read each in order.", "ক্ৰমে পঢ়া।")),
        order(f"{p}.u2.q5", PAIR, B("From part to whole", "অংশৰ পৰা গোটালৈ"), [B("Word", "শব্দ"), B("Sentence", "বাক্য"), B("Paragraph", "অনুচ্ছেদ"), B("Page", "পৃষ্ঠা")], B("Each sits inside the next.", "প্ৰতিটো পিছৰটোৰ ভিতৰত।")),
    ])
    u3 = unit("u3", B("A list of relations", "সম্পৰ্কৰ তালিকা"), "star", [B("Opposites make a common pair.", "বিপৰীত সাধাৰণ যোৰ।"), B("Synonyms mean the same.", "সমাৰ্থক শব্দৰ অৰ্থ একে।"), B("Country and capital is a fact relation.", "দেশ আৰু ৰাজধানী তথ্যৰ সম্পৰ্ক।"), B("Degree pairs differ in strength.", "মাত্ৰাৰ যোৰত তীব্ৰতা বেলেগ।")], [
        diagram(f"{p}.u3.s1", B("Word meaning relations", "অৰ্থৰ সম্পৰ্ক"), [B("Many pairs are about meaning: same, opposite or stronger.", "বহু যোৰ অৰ্থৰ: একে, ওলোটা বা বেছি তীব্ৰ।")], "grid", [B("Same: big, large", "একে: ডাঙৰ, বৃহৎ"), B("Opposite: hot, cold", "ওলোটা: গৰম, ঠাণ্ডা"), B("Stronger: warm, hot", "তীব্ৰ: উষ্ণ, গৰম")]),
        diagram(f"{p}.u3.s2", B("Fact relations", "তথ্যৰ সম্পৰ্ক"), [B("Others rest on knowledge: state and capital, or measure and unit.", "আন কিছুমান জ্ঞানৰ: ৰাজ্য আৰু ৰাজধানী, জোখ আৰু একক।")], "grid", [B("Assam : Dispur", "অসম : দিশপুৰ"), B("Length : Metre", "দৈৰ্ঘ্য : মিটাৰ"), B("Time : Second", "সময় : ছেকেণ্ড")]),
        inlines(f"{p}.u3.q1", TYPE, [a_row(("Hot", "গৰম"), ("Cold", "ঠাণ্ডা"), ("Tall", "ওখ"), ("Short", "চুটি"), [("Big", "ডাঙৰ"), ("High", "উচ্চ")], B("Opposites.", "বিপৰীত।")), a_row(("Length", "দৈৰ্ঘ্য"), ("Metre", "মিটাৰ"), ("Weight", "ওজন"), ("Kilogram", "কিলোগ্ৰাম"), [("Litre", "লিটাৰ"), ("Second", "ছেকেণ্ড")], B("A measure and its unit.", "জোখ আৰু একক।")), a_row(("Big", "ডাঙৰ"), ("Huge", "বিশাল"), ("Cold", "ঠাণ্ডা"), ("Freezing", "কঁপনি উঠা ঠাণ্ডা"), [("Warm", "উষ্ণ"), ("Wet", "তিতা")], B("A stronger degree.", "অধিক তীব্ৰতা।"))]),
        tf(f"{p}.u3.q2", TYPE, B("Assam : Dispur is a state and capital relation.", "অসম : দিশপুৰ ৰাজ্য আৰু ৰাজধানীৰ সম্পৰ্ক।"), True, B("Dispur is the capital of Assam.", "দিশপুৰ অসমৰ ৰাজধানী।")),
        match(f"{p}.u3.q3", TYPE, B("Match the pair to its kind", "যোৰক ধৰণৰ লগত মিলোৱা"), [[B("Day, night", "দিন, ৰাতি"), B("Opposite", "বিপৰীত")], [B("Start, begin", "আৰম্ভ, শুভাৰম্ভ"), B("Same meaning", "সমাৰ্থক")], [B("Time, second", "সময়, ছেকেণ্ড"), B("Measure, unit", "জোখ, একক")]], B("Name each kind.", "প্ৰতিটো ধৰণৰ নাম কোৱা।")),
        with_variants({"id": f"{p}.u3.q4", "type": "stepwise", "skill": TYPE}, lambda *a: rel_steps(f"{p}.u3.q4", *a), [(("Happy", "সুখী"), ("Sad", "দুখী"), ("Rich", "ধনী"), ("Opposites", "বিপৰীত"), ("Poor", "দুখীয়া"), [("Same meaning", "সমাৰ্থক"), ("Part and whole", "অংশ, গোটা")], [("Wealthy", "সম্পদশালী"), ("Gold", "সোণ")]), (("Fast", "খৰ"), ("Quick", "দ্ৰুত"), ("Near", "ওচৰ"), ("Same meaning", "সমাৰ্থক"), ("Close", "কাষ"), [("Opposites", "বিপৰীত"), ("Cause and effect", "কাৰণ, ফল")], [("Far", "দূৰ"), ("Road", "বাট")])]),
        odd(f"{p}.u3.q5", TYPE, lambda r, a, b, c: {"q": B(f"Which pair is not {r[0]}?", f"কোন যোৰ {r[1]} নহয়?"), "right": a, "fill": [b, c, "Up, down" if r[0] == "opposites" else "Big, large"], "why": B(f"{a} is the odd pair.", f"{a} বেলেগ যোৰ।")}, [(("opposites", "বিপৰীত"), "Tall, high", "Wet, dry", "Old, new"), (("same in meaning", "সমাৰ্থক"), "Hot, cold", "Small, tiny", "Rich, wealthy")]),
    ])
    u4 = unit("u4", B("Letter analogies", "আখৰৰ সাদৃশ্য"), "star", [B("Compare letter by letter.", "আখৰে আখৰে তুলনা কৰা।"), B("Find the gap in each position.", "প্ৰতিটো স্থানৰ ব্যৱধান।"), B("Apply the same gaps to the third term.", "তৃতীয় পদত একে ব্যৱধান।"), B("Reversal and opposites also appear.", "ওলোটা আৰু বিপৰীতো আহে।")], [
        diagram(f"{p}.u4.s1", B("It is a code in disguise", "ই ছদ্মবেশী সংকেত"), [B("AB : CD is a shift of 2. A letter analogy is a code you already know.", "AB : CD ত স্থানান্তৰ 2। আখৰৰ সাদৃশ্য মানে চিনাকি সংকেত।")], "flow", [same("AB : CD"), B("+2 each", "প্ৰতিটো +2"), same("KL : MN")]),
        diagram(f"{p}.u4.s2", B("Other rules to test", "আন নিয়ম"), [B("If a shift fails, try reversing the group or taking opposite letters.", "স্থানান্তৰে নহ'লে গোট ওলোটোৱা বা বিপৰীত আখৰ লোৱা।")], "grid", [B("Reverse: ABC, CBA", "ওলোটা: ABC, CBA"), B("Opposite: ACE, ZXV", "বিপৰীত: ACE, ZXV")]),
        solve(f"{p}.u4.q1", LETT, l_analogy, [("BAD", 2, "CUP"), ("TOP", 1, "SUN"), ("ROW", 3, "FAN")], input="letters"),
        solve(f"{p}.u4.q2", LETT, lambda a, c: {"q": B(f"{a} : {a[::-1]} :: {c} : ?", f"{a} : {a[::-1]} :: {c} : ?"), "answer": c[::-1], "why": B("The group is reversed.", "গোটটো ওলোটোৱা হৈছে।")}, [("LID", "MAP"), ("ARM", "NET"), ("BOX", "HEN")], input="letters"),
        tf(f"{p}.u4.q3", LETT, B("AC : DF follows a shift of +3.", "AC : DF ত স্থানান্তৰ +3।"), True, B("A to D and C to F are both +3.", "A ৰ পৰা D আৰু C ৰ পৰা F দুয়োটা +3।")),
        match(f"{p}.u4.q4", LETT, B("Match the pair to its rule", "যোৰক নিয়মৰ লগত মিলোৱা"), [[same("AB : BC"), same("+1")], [same("AD : CF"), same("+2")], [same("EF : FE"), B("Reverse", "ওলোটা")]], B("Check each position.", "প্ৰতিটো স্থান চোৱা।")),
        order(f"{p}.u4.q5", LETT, B("Test a letter analogy in order", "আখৰৰ সাদৃশ্য ক্ৰমে চোৱা"), [B("Try a shift", "স্থানান্তৰ"), B("Try a reversal", "ওলোটা"), B("Try opposites", "বিপৰীত"), B("Apply the rule", "নিয়ম প্ৰয়োগ")], B("Most common first.", "সাধাৰণটো আগতে।")),
    ])
    u5 = unit("u5", B("Number analogies", "সংখ্যাৰ সাদৃশ্য"), "star", [B("Look for squares and cubes first.", "প্ৰথমে বৰ্গ আৰু ঘন চোৱা।"), B("Try multiplying, then adding.", "পূৰণ কৰি যোগ কৰি চোৱা।"), B("Test the rule on the first pair.", "প্ৰথম যোৰত নিয়ম চোৱা।"), B("Digit sums can also link numbers.", "অংকৰ যোগফলেও সংযোগ কৰিব পাৰে।")], [
        diagram(f"{p}.u5.s1", B("Familiar pairs first", "চিনাকি যোৰ আগতে"), [B("Check squares and cubes before anything clever.", "কৌশলৰ আগতে বৰ্গ আৰু ঘন চোৱা।")], "grid", [same("3 : 9"), same("3 : 27"), same("4 : 16"), same("4 : 64")]),
        diagram(f"{p}.u5.s2", B("Multiply, then adjust", "পূৰণ, তাৰ পিছত মিলোৱা"), [B("7 : 15 is twice 7 plus 1. Then 9 : 19 follows.", "7 : 15 মানে 7 ৰ দুগুণ যোগ 1। তেন্তে 9 : 19।")], "flow", [same("7 × 2 = 14"), same("14 + 1 = 15"), same("9 : 19")]),
        solve(f"{p}.u5.q1", NUMB, n_square, [(4, 7), (6, 9), (8, 11)]),
        solve(f"{p}.u5.q2", NUMB, n_rule, [(5, 2, 1, 8), (4, 3, -1, 7), (6, 2, 3, 9)]),
        tf(f"{p}.u5.q3", NUMB, B("3 : 27 and 2 : 8 follow the same rule.", "3 : 27 আৰু 2 : 8 ৰ নিয়ম একে।"), True, B("Both cube the first number.", "দুয়োটা প্ৰথম সংখ্যাৰ ঘন।")),
        match(f"{p}.u5.q4", NUMB, B("Match the pair to its rule", "যোৰক নিয়মৰ লগত মিলোৱা"), [[same("5 : 25"), B("Square", "বৰ্গ")], [same("2 : 8"), B("Cube", "ঘন")], [same("6 : 12"), same("× 2")]], B("Test each rule.", "প্ৰতিটো নিয়ম চোৱা।")),
        stepwise(f"{p}.u5.q5", NUMB, lambda a, m, s_, c: {"q": B(f"{a} : {a * m + s_} :: {c} : ?", f"{a} : {a * m + s_} :: {c} : ?"), "parts": [
            part(B("The rule?", "নিয়ম?"), same(f"× {m}, {s_:+d}"), [same(f"× {m + 1}, {s_ - 1:+d}"), same(f"+ {a * m + s_ - a}, × 2")], B("Test it on the first pair.", "প্ৰথম যোৰত চোৱা।"), sid=f"{p}.u5.q5"),
            part(B("The answer?", "উত্তৰ?"), same(c * m + s_), [same(c * m + s_ + 2), same(c * m + s_ - 2)], B("Apply it to the third number.", "তৃতীয় সংখ্যাত প্ৰয়োগ কৰা।"), sid=f"{p}.u5.q5"),
        ], "why": B(f"The answer is {c * m + s_}.", f"উত্তৰ {c * m + s_}।")}, [(3, 3, 1, 5), (7, 2, -1, 10), (6, 3, 2, 4)]),
    ])
    u6 = unit("u6", B("What goes with what", "কিহৰ লগত কি"), "star", [B("Time units scale evenly.", "সময়ৰ একক সমানে বাঢ়ে।"), B("Groups of animals have names.", "জীৱৰ গোটৰ নাম আছে।"), B("Think of where a thing is kept.", "বস্তু ক'ত ৰখা হয় ভাবা।"), B("Use the same sentence test.", "একে বাক্য পৰীক্ষা।")], [
        diagram(f"{p}.u6.s1", B("Everyday links", "দৈনন্দিন সম্পৰ্ক"), [B("Many pairs are simply things that belong together.", "বহু যোৰ কেৱল একেলগে থকা বস্তু।")], "grid", [B("Book : Shelf", "কিতাপ : আলমাৰি"), B("Car : Garage", "গাড়ী : গেৰেজ"), B("Money : Bank", "ধন : বেংক")]),
        diagram(f"{p}.u6.s2", B("Time scale pairs", "সময়ৰ যোৰ"), [B("Week : Day is 7 to 1. Year : Month is 12 to 1.", "সপ্তাহ : দিন 7 : 1। বছৰ : মাহ 12 : 1।")], "flow", [same("60 s = 1 min"), same("7 days = 1 week"), same("12 months = 1 year")]),
        inlines(f"{p}.u6.q1", ASSOC, [a_row(("Book", "কিতাপ"), ("Library", "পুথিভঁৰাল"), ("Money", "ধন"), ("Bank", "বেংক"), [("Coin", "মুদ্ৰা"), ("Shop", "দোকান")], B("Where it is kept.", "ক'ত ৰখা হয়।")), a_row(("Bird", "চৰাই"), ("Flock", "জাক"), ("Cow", "গৰু"), ("Herd", "জাক"), [("Stable", "গোহালি"), ("Milk", "গাখীৰ")], B("A group of them.", "সিহঁতৰ গোট।")), a_row(("Minute", "মিনিট"), ("Hour", "ঘণ্টা"), ("Month", "মাহ"), ("Year", "বছৰ"), [("Week", "সপ্তাহ"), ("Day", "দিন")], B("A larger unit of time.", "ডাঙৰ সময় একক।"))]),
        tf(f"{p}.u6.q2", ASSOC, B("Second : Minute matches Day : Week.", "ছেকেণ্ড : মিনিট, দিন : সপ্তাহৰ লগত মিলে।"), True, B("Small unit to larger unit.", "সৰু এককৰ পৰা ডাঙৰ একক।")),
        match(f"{p}.u6.q3", ASSOC, B("Match the thing to its place", "বস্তুক ঠাইৰ লগত মিলোৱা"), [[B("Train", "ৰেল"), B("Station", "ষ্টেচন")], [B("Plane", "বিমান"), B("Airport", "বিমানবন্দৰ")], [B("Boat", "নাও"), B("Ghat", "ঘাট")]], B("Where each stops.", "ক'ত ৰয়।")),
        order(f"{p}.u6.q4", ASSOC, B("Small to large", "সৰুৰ পৰা ডাঙৰলৈ"), [B("Minute", "মিনিট"), B("Hour", "ঘণ্টা"), B("Day", "দিন"), B("Week", "সপ্তাহ")], B("Each contains the last.", "প্ৰতিটোৱে আগৰটোক সামৰে।")),
        solve(f"{p}.u6.q5", ASSOC, lambda a, u: {"q": B(f"Week : 7 :: {a} : ?, counting {u[0]}.", f"সপ্তাহ : 7 :: {u[1]} : ?"), "answer": str(u[2]), "why": B(f"{u[2]} is the count.", f"{u[2]} সংখ্যাটো।")}, [("Year", ("months in a year", "বছৰৰ মাহ", 12)), ("Minute", ("seconds in a minute", "মিনিটৰ ছেকেণ্ড", 60)), ("Day", ("hours in a day", "দিনৰ ঘণ্টা", 24))]),
    ])
    test = {"id": "test", "title": B("Analogy test", "সাদৃশ্যৰ পৰীক্ষা"), "steps": [
        mcq(f"{p}.t.q1", NAME, lambda a, b, c, r, f: {"q": B(f"{a[0]} : {b[0]} :: {c[0]} : ?", f"{a[1]} : {b[1]} :: {c[1]} : ?"), "right": r, "wrong": [], "fill": f, "why": B("Apply the same relation.", "একে সম্পৰ্ক প্ৰয়োগ কৰা।")}, [(("Author", "লেখক"), ("Book", "কিতাপ"), ("Painter", "চিত্ৰকৰ"), "Picture", ["Brush", "Colour", "Wall"]), (("Cow", "গৰু"), ("Milk", "গাখীৰ"), ("Bee", "মৌমাখি"), "Honey", ["Hive", "Sting", "Wing"])]),
        tf(f"{p}.t.q2", PAIR, B("Petal : Flower matches Page : Book.", "পাহি : ফুল, পৃষ্ঠা : কিতাপৰ লগত মিলে।"), True, B("Both are part to whole.", "দুয়োটা অংশৰ পৰা গোটা।")),
        solve(f"{p}.t.q3", LETT, l_analogy, [("PEN", 2, "BAT"), ("DOG", 1, "RAT")], input="letters"),
        solve(f"{p}.t.q4", NUMB, n_square, [(5, 12), (9, 13)]),
        solve(f"{p}.t.q5", NUMB, n_rule, [(3, 4, 1, 6), (8, 2, -3, 5)]),
        tf(f"{p}.t.q6", TYPE, B("Rich : Poor is a pair of opposites.", "ধনী : দুখীয়া বিপৰীত যোৰ।"), True, B("They are opposite in meaning.", "অৰ্থ ওলোটা।")),
    ]}
    return {"id": "rs-04-analogy", "no": 4, "slug": "analogy", "title": B("Analogy", "সাদৃশ্য"), "reign": B("Relations, letters, numbers", "সম্পৰ্ক, আখৰ, সংখ্যা"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


def o4(sid, skill, rows):
    """rows: (good three, odd one, why). Bilingual options."""
    import random
    versions = []
    for k, (good, bad, why) in enumerate(rows):
        opts = [B(*x) for x in good] + [B(*bad)]
        random.Random(f"{sid}:{k}").shuffle(opts)
        versions.append({"q": B("Which one does not belong?", "কোনটো নিমিলে?"), "options": opts, "answer": opts.index(B(*bad)), "why": why})
    return {"id": sid, "type": "odd", "skill": skill, **versions[0], "variants": versions}


def numodd(sid, skill, rows):
    return o4(sid, skill, [([(str(g), str(g)) for g in good], (str(bad), str(bad)), why) for good, bad, why in rows])


def lesson_odd():
    p = "rs5"
    u1 = unit("u1", B("Find the group first", "প্ৰথমে গোট বিচৰা"), "star", [B("Name what three share.", "তিনিটাৰ উমৈহতীয়া গুণ কোৱা।"), B("The fourth then stands out.", "চতুৰ্থটো নিজে ওলায়।"), B("Do not start from how one looks.", "চেহেৰাৰ পৰা আৰম্ভ নকৰিবা।"), B("Check that your group fits exactly three.", "গোটত ঠিক তিনিটা মিলিছে চোৱা।")], [
        diagram(f"{p}.u1.s1", B("Look for three, not one", "এটা নহয়, তিনিটা চোৱা"), [B("The answer is defined by the other three. Name their group.", "উত্তৰ বাকী তিনিটাৰ দ্বাৰা ঠিক হয়। সিহঁতৰ গোটৰ নাম কোৱা।")], "flow", [B("Name a group", "গোটৰ নাম"), B("Three fit", "তিনিটা মিলে"), B("One left", "এটা বাকী")]),
        diagram(f"{p}.u1.s2", B("Common groups", "সাধাৰণ গোট"), [B("Most word groups come from everyday life.", "বেছিভাগ শব্দৰ গোট দৈনন্দিন জীৱনৰ।")], "grid", [B("Fruits", "ফল"), B("Tools", "সঁজুলি"), B("Rivers", "নদী"), B("Animals", "জীৱ")]),
        o4(f"{p}.u1.q1", GROUP, [([("Mango", "আম"), ("Banana", "কল"), ("Guava", "মধুৰিআম")], ("Potato", "আলু"), B("The others are fruits.", "বাকীবোৰ ফল।")), ([("Hammer", "হাতুৰী"), ("Saw", "কৰত"), ("Axe", "কুঠাৰ")], ("Chair", "চকী"), B("The others are tools.", "বাকীবোৰ সঁজুলি।")), ([("Tiger", "বাঘ"), ("Lion", "সিংহ"), ("Leopard", "নাহৰফুটুকী")], ("Cow", "গৰু"), B("The others are wild cats.", "বাকীবোৰ বনৰীয়া মেকুৰী জাতীয়।"))]),
        o4(f"{p}.u1.q2", GROUP, [([("Red", "ৰঙা"), ("Blue", "নীলা"), ("Green", "সেউজীয়া")], ("Round", "ঘূৰণীয়া"), B("The others are colours.", "বাকীবোৰ ৰং।")), ([("Brahmaputra", "ব্ৰহ্মপুত্ৰ"), ("Ganga", "গংগা"), ("Barak", "বৰাক")], ("Himalaya", "হিমালয়"), B("The others are rivers.", "বাকীবোৰ নদী।"))]),
        tf(f"{p}.u1.q3", GROUP, B("In odd one out, start by finding what three share.", "বেলেগটো উলিয়াবলৈ তিনিটাৰ উমৈহতীয়া গুণৰ পৰা আৰম্ভ কৰা।"), True, B("The group defines the odd one.", "গোটে বেলেগটো ঠিক কৰে।"), ("r-m-surface", SURF)),
        match(f"{p}.u1.q4", GROUP, B("Match the words to their group", "শব্দক গোটৰ লগত মিলোৱা"), [[B("Rice, wheat, maize", "ধান, ঘেঁহু, মাকৈ"), B("Cereals", "শস্য")], [B("Spoon, fork, plate", "চামুচ, কাঁটাচামুচ, কাঁহী"), B("Tableware", "খোৱাৰ সঁজুলি")], [B("Bus, train, car", "বাছ, ৰেল, গাড়ী"), B("Transport", "যাতায়াত")]], B("Name each group.", "প্ৰতিটো গোটৰ নাম কোৱা।")),
        order(f"{p}.u1.q5", GROUP, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read all four", "চাৰিওটা পঢ়া"), B("Name a group", "গোটৰ নাম"), B("Test each word", "প্ৰতিটো শব্দ চোৱা"), B("Choose the misfit", "নিমিলাটো বাছা")], B("All four first.", "প্ৰথমে চাৰিওটা।")),
    ])
    u2 = unit("u2", B("Look one level deeper", "অলপ গভীৰলৈ চোৱা"), "star", [B("All four may look alike.", "চাৰিওটা একে দেখিব পাৰে।"), B("Ask how each is used or made.", "কেনেকৈ ব্যৱহাৰ বা বনোৱা হয় সোধা।"), B("Living and non-living is a common split.", "জীৱ আৰু অজীৱ সাধাৰণ বিভাজন।"), B("Try a second property if the first fails.", "প্ৰথম গুণে নহ'লে দ্বিতীয় চোৱা।")], [
        diagram(f"{p}.u2.s1", B("When all look alike", "সকলো একে দেখিলে"), [B("If four things seem one family, ask how they work.", "চাৰিওটা এক পৰিয়াল যেন লাগিলে কেনেকৈ কাম কৰে সোধা।")], "grid", [B("Walks on land", "মাটিত খোজ"), B("Lives in water", "পানীত থাকে"), B("Flies", "উৰে"), B("Grows from seed", "বীজৰ পৰা গজে")]),
        diagram(f"{p}.u2.s2", B("Questions to try", "সোধা প্ৰশ্ন"), [B("Ask about use, material, place and life.", "ব্যৱহাৰ, সামগ্ৰী, ঠাই, জীৱন সোধা।")], "flow", [B("Use?", "ব্যৱহাৰ?"), B("Made of?", "সামগ্ৰী?"), B("Where?", "ক'ত?"), B("Alive?", "জীৱিত?")]),
        o4(f"{p}.u2.q1", PROP, [([("Crow", "কাউৰী"), ("Sparrow", "ঘৰচিৰিকা"), ("Eagle", "ঈগল")], ("Bat", "বাদুলি"), B("Bats are mammals; the others are birds.", "বাদুলি স্তন্যপায়ী; বাকীবোৰ চৰাই।")), ([("Carrot", "গাজৰ"), ("Radish", "মূলা"), ("Beetroot", "বিট")], ("Tomato", "বিলাহী"), B("The others grow as roots.", "বাকীবোৰ শিপা হিচাপে গজে।")), ([("Whale", "তিমি"), ("Dolphin", "ডলফিন"), ("Seal", "চীল")], ("Shark", "হাঙৰ"), B("Sharks are fish; the others are mammals.", "হাঙৰ মাছ; বাকীবোৰ স্তন্যপায়ী।"))]),
        tf(f"{p}.u2.q2", PROP, B("A bat belongs in the group of birds.", "বাদুলি চৰাইৰ গোটত পৰে।"), False, B("It is a mammal that flies.", "ই উৰিব পৰা স্তন্যপায়ী।"), ("r-m-surface", SURF)),
        match(f"{p}.u2.q3", PROP, B("Match the thing to its property", "বস্তুক গুণৰ লগত মিলোৱা"), [[B("Iron", "লো"), B("Metal", "ধাতু")], [B("Rose", "গোলাপ"), B("Plant", "উদ্ভিদ")], [B("Oxygen", "অক্সিজেন"), B("Gas", "গেছ")]], B("Each belongs to a class.", "প্ৰতিটো এটা শ্ৰেণীৰ।")),
        o4(f"{p}.u2.q4", PROP, [([("Iron", "লো"), ("Copper", "তাম"), ("Gold", "সোণ")], ("Wood", "কাঠ"), B("The others are metals.", "বাকীবোৰ ধাতু।")), ([("Square", "বৰ্গ"), ("Triangle", "ত্ৰিভুজ"), ("Rectangle", "আয়ত")], ("Circle", "বৃত্ত"), B("The others have straight sides.", "বাকীবোৰৰ বাহু পোন।"))]),
        order(f"{p}.u2.q5", PROP, B("Questions from simple to deep", "সহজৰ পৰা গভীৰ প্ৰশ্নলৈ"), [B("What is it?", "ই কি?"), B("What is it used for?", "ইয়াৰ ব্যৱহাৰ কি?"), B("What is it made of?", "ই কিহেৰে বনোৱা?"), B("How does it live?", "ই কেনেকৈ জীয়াই থাকে?")], B("Go deeper only if needed.", "প্ৰয়োজন হ'লেহে গভীৰলৈ।")),
    ])
    u3 = unit("u3", B("Numbers that do not fit", "নিমিলা সংখ্যা"), "star", [B("Test odd and even first.", "প্ৰথমে যুগ্ম-অযুগ্ম চোৱা।"), B("Then primes, squares and cubes.", "তাৰ পিছত মৌলিক, বৰ্গ, ঘন।"), B("Then multiples of one number.", "তাৰ পিছত গুণিতক।"), B("Digit sums can be the link.", "অংকৰ যোগফলো সংযোগ হ'ব পাৰে।")], [
        diagram(f"{p}.u3.s1", B("A checklist for numbers", "সংখ্যাৰ তালিকা"), [B("Run the same quick checks every time.", "সদায় একে দ্ৰুত পৰীক্ষা কৰা।")], "flow", [B("Odd or even", "অযুগ্ম, যুগ্ম"), B("Prime", "মৌলিক"), B("Square", "বৰ্গ"), B("Multiple", "গুণিতক")]),
        diagram(f"{p}.u3.s2", B("Digit sums", "অংকৰ যোগফল"), [B("23, 41, 50 all have digits adding to 5. 62 does not.", "23, 41, 50 ৰ অংকৰ যোগফল 5। 62 ৰ নহয়।")], "grid", [same("2 + 3 = 5"), same("4 + 1 = 5"), same("5 + 0 = 5"), same("6 + 2 = 8")]),
        numodd(f"{p}.u3.q1", ODDN, [((2, 4, 8), 9, B("The others are even.", "বাকীবোৰ যুগ্ম।")), ((13, 17, 19), 21, B("The others are prime.", "বাকীবোৰ মৌলিক।")), ((16, 25, 49), 30, B("The others are squares.", "বাকীবোৰ বৰ্গ।"))]),
        numodd(f"{p}.u3.q2", ODDN, [((14, 21, 35), 40, B("The others are multiples of 7.", "বাকীবোৰ 7 ৰ গুণিতক।")), ((8, 27, 64), 81, B("The others are cubes.", "বাকীবোৰ ঘন।")), ((23, 41, 50), 62, B("The others have digits adding to 5.", "বাকীবোৰৰ অংকৰ যোগফল 5।"))]),
        tf(f"{p}.u3.q3", ODDN, B("51 is a prime number.", "51 মৌলিক সংখ্যা।"), False, B("51 = 3 × 17.", "51 = 3 × 17।")),
        match(f"{p}.u3.q4", ODDN, B("Match the number to its family", "সংখ্যাক পৰিয়ালৰ লগত মিলোৱা"), [[same("36"), B("Square", "বৰ্গ")], [same("29"), B("Prime", "মৌলিক")], [same("27"), B("Cube", "ঘন")]], B("Know them on sight.", "চিনি পোৱা হোৱা।")),
        solve(f"{p}.u3.q5", ODDN, lambda n: {"q": B(f"What is the digit sum of {n}?", f"{n} ৰ অংকৰ যোগফল কিমান?"), "answer": str(sum(map(int, str(n)))), "why": B("Add the digits.", "অংকবোৰ যোগ কৰা।")}, [(47,), (163,), (258,)]),
    ])
    u4 = unit("u4", B("Letters that do not fit", "নিমিলা আখৰ"), "star", [B("Vowels and consonants are the first split.", "স্বৰ আৰু ব্যঞ্জন প্ৰথম বিভাজন।"), B("Then check the gaps in a group.", "তাৰ পিছত গোটৰ ব্যৱধান।"), B("Then opposite-letter pairs.", "তাৰ পিছত বিপৰীত যোৰ।"), B("Convert to places when unsure.", "সন্দেহ হ'লে স্থানলৈ সলনি কৰা।")], [
        diagram(f"{p}.u4.s1", B("Five letters are special", "পাঁচটা আখৰ বিশেষ"), [B("If only one option holds a vowel, or lacks one, that is the rule.", "এটা বিকল্পত স্বৰ থাকিলে বা নাথাকিলে, সেয়াই নিয়ম।")], "flow", [same("A"), same("E"), same("I"), same("O")]),
        diagram(f"{p}.u4.s2", B("Gaps again", "আকৌ ব্যৱধান"), [B("BD, FH, JL all skip one letter. MQ does not.", "BD, FH, JL ত এটা আখৰ এৰে। MQ ত নহয়।")], "grid", [same("BD: +2"), same("FH: +2"), same("JL: +2"), same("MQ: +4")]),
        numodd(f"{p}.u4.q1", ODDL, [(("BD", "FH", "JL"), "MQ", B("The others have a gap of 2.", "বাকীবোৰৰ ব্যৱধান 2।")), (("AE", "IO", "OU"), "AB", B("The others are all vowels.", "বাকীবোৰ সকলো স্বৰবৰ্ণ।")), (("AZ", "BY", "CX"), "DV", B("The others are opposite pairs.", "বাকীবোৰ বিপৰীত যোৰ।"))]),
        tf(f"{p}.u4.q2", ODDL, B("BY is an opposite-letter pair.", "BY বিপৰীত আখৰৰ যোৰ।"), True, B("2 + 25 = 27.", "2 + 25 = 27।")),
        match(f"{p}.u4.q3", ODDL, B("Match the letters to their kind", "আখৰক ধৰণৰ লগত মিলোৱা"), [[same("E"), B("Vowel", "স্বৰবৰ্ণ")], [same("K"), B("Consonant", "ব্যঞ্জনবৰ্ণ")], [same("CX"), B("Opposite pair", "বিপৰীত যোৰ")]], B("Check each.", "প্ৰতিটো চোৱা।")),
        solve(f"{p}.u4.q4", ODDL, lambda w: {"q": B(f"How many vowels are in {w}?", f"{w} ত কিমান স্বৰবৰ্ণ?"), "answer": str(sum(c in "AEIOU" for c in w)), "why": B("Count A, E, I, O and U.", "A, E, I, O, U গণা।")}, [("MOUNTAIN",), ("GUWAHATI",), ("EDUCATION",)]),
        order(f"{p}.u4.q5", ODDL, B("Letter checks in order", "আখৰৰ পৰীক্ষা ক্ৰমে"), [B("Vowels", "স্বৰবৰ্ণ"), B("Gaps", "ব্যৱধান"), B("Opposites", "বিপৰীত"), B("Places", "স্থান")], B("Quick checks first.", "দ্ৰুত পৰীক্ষা আগতে।")),
    ])
    u5 = unit("u5", B("The odd pair", "বেলেগ যোৰ"), "star", [B("Find the relation in each pair.", "প্ৰতিটো যোৰৰ সম্পৰ্ক উলিওৱা।"), B("Three pairs share one relation.", "তিনিটা যোৰৰ সম্পৰ্ক একে।"), B("This is an analogy with four choices.", "ই চাৰি বিকল্পৰ সাদৃশ্য।"), B("State each relation in a sentence.", "প্ৰতিটো সম্পৰ্ক বাক্যত কোৱা।")], [
        diagram(f"{p}.u5.s1", B("Pairs hide a relation", "যোৰত সম্পৰ্ক লুকাই থাকে"), [B("Treat each pair as a small analogy. Three follow one sentence.", "প্ৰতিটো যোৰক সৰু সাদৃশ্য ধৰা। তিনিটাই এটা বাক্য মানে।")], "grid", [B("Dog, puppy", "কুকুৰ, পোৱালি"), B("Cat, kitten", "মেকুৰী, পোৱালি"), B("Tree, leaf", "গছ, পাত")]),
        diagram(f"{p}.u5.s2", B("Number pairs too", "সংখ্যাৰ যোৰো"), [B("In 2, 4 and 3, 9 and 5, 25 the second is a square. 6, 30 is not.", "2, 4; 3, 9; 5, 25 ত দ্বিতীয়টো বৰ্গ। 6, 30 নহয়।")], "flow", [same("2, 4"), same("3, 9"), same("5, 25"), same("6, 30")]),
        o4(f"{p}.u5.q1", ODDP, [([("Dog, puppy", "কুকুৰ, কুকুৰ পোৱালি"), ("Cat, kitten", "মেকুৰী, মেকুৰী পোৱালি"), ("Cow, calf", "গৰু, দামুৰি")], ("Tree, leaf", "গছ, পাত"), B("The others are adult and young.", "বাকীবোৰ ডাঙৰ আৰু পোৱালি।")), ([("Pen, write", "কলম, লিখা"), ("Knife, cut", "কটাৰী, কটা"), ("Broom, sweep", "ঝাৰু, সৰা")], ("Sun, shine", "সূৰ্য, পোহৰ"), B("The others are tools and uses.", "বাকীবোৰ সঁজুলি আৰু ব্যৱহাৰ।"))]),
        numodd(f"{p}.u5.q2", ODDP, [(("2, 4", "3, 9", "5, 25"), "6, 30", B("The others are squares.", "বাকীবোৰ বৰ্গ।")), (("3, 6", "5, 10", "7, 14"), "9, 16", B("The others double.", "বাকীবোৰ দুগুণ।"))]),
        tf(f"{p}.u5.q3", ODDP, B("Tiger, cub has the same relation as Dog, puppy.", "বাঘ, পোৱালি আৰু কুকুৰ, পোৱালিৰ সম্পৰ্ক একে।"), True, B("Adult and young.", "ডাঙৰ আৰু পোৱালি।")),
        match(f"{p}.u5.q4", ODDP, B("Match the pair to its relation", "যোৰক সম্পৰ্কৰ লগত মিলোৱা"), [[B("Rain, flood", "বৰষুণ, বান"), B("Cause, effect", "কাৰণ, ফল")], [B("Wheel, car", "চকা, গাড়ী"), B("Part, whole", "অংশ, গোটা")], [B("Hot, cold", "গৰম, ঠাণ্ডা"), B("Opposites", "বিপৰীত")]], B("Sentence test.", "বাক্য পৰীক্ষা।")),
        order(f"{p}.u5.q5", ODDP, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Take a pair", "যোৰ লোৱা"), B("State its relation", "সম্পৰ্ক কোৱা"), B("Test the others", "বাকীবোৰ চোৱা"), B("Pick the misfit", "নিমিলা বাছা")], B("One sentence, four tests.", "এটা বাক্য, চাৰি পৰীক্ষা।")),
    ])
    u6 = unit("u6", B("Check all four", "চাৰিওটা চোৱা"), "star", [B("Do not stop at the first idea.", "প্ৰথম চিন্তাতে নৰবা।"), B("A second answer means your group is weak.", "দ্বিতীয় উত্তৰ মানে গোট দুৰ্বল।"), B("Prefer the narrower group.", "ঠেক গোট ভাল।"), B("Under time pressure, still check all four.", "সময় কম হ'লেও চাৰিওটা চোৱা।")], [
        diagram(f"{p}.u6.s1", B("Two answers? Sharpen the group", "দুটা উত্তৰ? গোট চোকা কৰা"), [B("If two options seem odd, your group is too loose. Make it narrower.", "দুটা বেলেগ যেন লাগিলে গোট ঢিলা। ঠেক কৰা।")], "flow", [B("Two misfits", "দুটা নিমিলা"), B("Narrow the group", "গোট ঠেক"), B("One misfit", "এটা নিমিলা")]),
        diagram(f"{p}.u6.s2", B("Narrow beats wide", "ঠেকেই ভাল"), [B("Sparrow, crow, owl, duck: all birds, but only a duck swims.", "ঘৰচিৰিকা, কাউৰী, ফেঁচা, হাঁহ: সকলো চৰাই, কেৱল হাঁহে সাঁতোৰে।")], "flow", [B("Birds", "চৰাই"), B("Birds that swim", "সাঁতোৰা চৰাই"), B("Duck", "হাঁহ")]),
        o4(f"{p}.u6.q1", SKIM, [([("Sparrow", "ঘৰচিৰিকা"), ("Crow", "কাউৰী"), ("Owl", "ফেঁচা")], ("Duck", "হাঁহ"), B("Only a duck swims.", "কেৱল হাঁহে সাঁতোৰে।")), ([("Bus", "বাছ"), ("Car", "গাড়ী"), ("Truck", "ট্ৰাক")], ("Boat", "নাও"), B("The others run on roads.", "বাকীবোৰ পথত চলে।"))]),
        tf(f"{p}.u6.q2", SKIM, B("If two options seem odd, your group is too loose.", "দুটা বেলেগ যেন লাগিলে গোট ঢিলা।"), True, B("Narrow the group.", "গোট ঠেক কৰা।")),
        match(f"{p}.u6.q3", SKIM, B("Match the wide group to a narrower one", "বহল গোটক ঠেক গোটৰ লগত মিলোৱা"), [[B("Animals", "জীৱ"), B("Mammals", "স্তন্যপায়ী")], [B("Plants", "উদ্ভিদ"), B("Trees", "গছ")], [B("Vehicles", "বাহন"), B("Road vehicles", "পথৰ বাহন")]], B("Narrow is sharper.", "ঠেক গোট চোকা।")),
        order(f"{p}.u6.q4", SKIM, B("Wide to narrow", "বহলৰ পৰা ঠেকলৈ"), [B("Living things", "জীৱ"), B("Animals", "জন্তু"), B("Birds", "চৰাই"), B("Sparrows", "ঘৰচিৰিকা")], B("Each sits inside the last.", "প্ৰতিটো আগৰটোৰ ভিতৰত।")),
        o4(f"{p}.u6.q5", SKIM, [([("Monday", "সোমবাৰ"), ("Friday", "শুক্ৰবাৰ"), ("Sunday", "দেওবাৰ")], ("March", "মাৰ্চ"), B("The others are days.", "বাকীবোৰ দিন।")), ([("Spring", "বসন্ত"), ("Summer", "গ্ৰীষ্ম"), ("Winter", "শীত")], ("Morning", "ৰাতিপুৱা"), B("The others are seasons.", "বাকীবোৰ ঋতু।"))]),
    ])
    test = {"id": "test", "title": B("Odd one out test", "বেলেগটো উলিওৱাৰ পৰীক্ষা"), "steps": [
        mcq(f"{p}.t.q1", GROUP, lambda r, f: {"q": B("Which one does not belong?", "কোনটো নিমিলে?"), "right": r, "wrong": [], "fill": f, "why": B(f"{r} is outside the group.", f"{r} গোটৰ বাহিৰত।")}, [("Spoon", ["Apple", "Orange", "Plum"]), ("Pencil", ["Horse", "Sheep", "Goat"])]),
        mcq(f"{p}.t.q2", ODDN, lambda r, f: {"q": B("Which number does not belong?", "কোন সংখ্যা নিমিলে?"), "right": r, "wrong": [], "fill": f, "why": B("Test the families.", "পৰিয়াল চোৱা।")}, [(26, [25, 36, 49]), (15, [11, 13, 17])]),
        tf(f"{p}.t.q3", PROP, B("A whale is a mammal.", "তিমি স্তন্যপায়ী।"), True, B("It feeds its young with milk.", "ই পোৱালিক গাখীৰ খুৱায়।")),
        tf(f"{p}.t.q4", ODDL, B("AZ and DW are both opposite pairs.", "AZ আৰু DW দুয়োটা বিপৰীত যোৰ।"), True, B("Both add to 27.", "দুয়োটাৰ যোগফল 27।")),
        mcq(f"{p}.t.q5", ODDP, lambda r, f: {"q": B("Which pair does not belong?", "কোন যোৰ নিমিলে?"), "right": r, "wrong": [], "fill": f, "why": B("The others double.", "বাকীবোৰ দুগুণ।")}, [("4, 7", ["2, 4", "6, 12", "8, 16"]), ("5, 11", ["3, 6", "7, 14", "9, 18"])]),
        tf(f"{p}.t.q6", SKIM, B("Always check all four options.", "সদায় চাৰিওটা বিকল্প চোৱা।"), True, B("A second misfit shows a weak group.", "দ্বিতীয় নিমিলাই দুৰ্বল গোট দেখুৱায়।")),
    ]}
    return {"id": "rs-05-odd-one-out", "no": 5, "slug": "odd-one-out", "title": B("Odd one out", "বেলেগটো উলিওৱা"), "reign": B("Groups, numbers, letters, pairs", "গোট, সংখ্যা, আখৰ, যোৰ"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


class ANALOGY:
    lesson = staticmethod(lesson_analogy)


class ODD:
    lesson = staticmethod(lesson_odd)
