"""Lessons 21 to 23: Data, Communication and Decision making.

Data sets are invented for practice. Lessons 22 and 23 teach principles: scenarios are written
so that one choice is clearly best, because these answers can otherwise be arguable.
"""
from math_kit import B, explore, match, mcq, order, part, solve, stepwise, tf, unit
from math_lessons_c import diagram
from reason_kit import inlines, same

TABLE = "r-dtable"; CHART = "r-dchart"; PIE = "r-dpie"; CHANGE = "r-dchange"
LISTEN = "r-clisten"; FEED = "r-cfeed"; BODY = "r-cbody"; CLEAR = "r-cclear"; EMP = "r-cempathy"; BARR = "r-cbarrier"
DUTY = "r-dduty"; SAFE = "r-dsafe"; FAIR = "r-dfair"; HONEST = "r-dhonest"; TEAM = "r-dteam"; CRISIS = "r-dcrisis"
SKILLS = {TABLE: ("data", B("Read a table", "তালিকা পঢ়া"), []), CHART: ("data", B("Read a chart", "লেখ পঢ়া"), []), PIE: ("data", B("Percent shares", "শতাংশ ভাগ"), []), CHANGE: ("data", B("Rise and fall", "বৃদ্ধি আৰু হ্ৰাস"), [TABLE]),
          LISTEN: ("communication", B("Active listening", "সক্ৰিয় শ্ৰৱণ"), []), FEED: ("communication", B("Giving feedback", "মতামত দিয়া"), []), BODY: ("communication", B("Non-verbal signals", "অশাব্দিক সংকেত"), []), CLEAR: ("communication", B("Clear messages", "স্পষ্ট বাৰ্তা"), []), EMP: ("communication", B("Empathy", "সমবেদনা"), []), BARR: ("communication", B("Barriers", "বাধা"), []),
          DUTY: ("decisions", B("Rules and duty", "নিয়ম আৰু কৰ্তব্য"), []), SAFE: ("decisions", B("Safety first", "সুৰক্ষা আগতে"), []), FAIR: ("decisions", B("Fairness", "ন্যায্যতা"), []), HONEST: ("decisions", B("Integrity", "সততা"), []), TEAM: ("decisions", B("Teamwork", "দলীয় কাম"), []), CRISIS: ("decisions", B("Crisis steps", "সংকটৰ খোজ"), [SAFE])}
TAGS = {"r-m-units": (TABLE, B("Ignoring the unit", "একক পাহৰা")), "r-m-base": (CHANGE, B("Using the wrong base for a percent", "শতাংশৰ ভুল ভেটি")), "r-m-interrupt": (LISTEN, B("Replying before listening", "নুশুনি উত্তৰ দিয়া"))}
UNIT = B("Read the column heading: the table may be in thousands.", "স্তম্ভৰ শিৰোনাম পঢ়া: তালিকা হাজাৰত হ'ব পাৰে।")
BASE = B("Percent change divides by the starting value.", "শতাংশ সলনি আৰম্ভণিৰ মানেৰে হৰণ কৰা।")
INT = B("Hear the whole message before replying.", "উত্তৰৰ আগতে গোটেই কথা শুনা।")


def s(sc, q, right, wrong, why):
    """A scenario row for inlines."""
    return (B(sc[0] + " " + q[0], sc[1] + " " + q[1]), B(".", "।"), B(*right), [B(*x) for x in wrong], why)


BEST = ("The best response is:", "আটাইতকৈ ভাল সঁহাৰি:")
FIRST = ("The best first step is:", "প্ৰথম ভাল খোজ:")


def read_table(rows, col, name):
    head, data = rows
    return {"q": B(f"Monthly sales in units. {data}. What did {name} sell?", f"মাহেকীয়া বিক্ৰী। {data}। {name} কিমান বিক্ৰী কৰিলে?"), "answer": str(col), "why": B("Read the row.", "শাৰী পঢ়া।")}


def bar_top(labels, vals):
    k = vals.index(max(vals))
    return {"q": B("Tap the year with the highest output.", "আটাইতকৈ বেছি উৎপাদনৰ বছৰ টিপা।"), "widget": {"kind": "bars", "labels": labels, "vals": vals}, "target": k, "answerText": same(labels[k]), "why": B(f"{labels[k]} has the tallest bar.", f"{labels[k]} ৰ বাৰ ওখ।"), "traps": []}


def bar_rise(labels, vals):
    rises = [vals[i] - vals[i - 1] for i in range(1, len(vals))]
    k = rises.index(max(rises)) + 1
    return {"q": B("Tap the year with the largest rise from the year before.", "আগৰ বছৰৰ তুলনাত আটাইতকৈ বেছি বৃদ্ধিৰ বছৰ টিপা।"), "widget": {"kind": "bars", "labels": labels, "vals": vals}, "target": k, "answerText": same(labels[k]), "why": B(f"The rise of {rises[k - 1]} is largest.", f"{rises[k - 1]} বৃদ্ধি আটাইতকৈ বেছি।"), "traps": [{"val": vals.index(max(vals)), "tag": "r-m-base", "why": B("The tallest bar need not have the biggest rise.", "ওখ বাৰ মানে বেছি বৃদ্ধি নহয়।")}] if vals.index(max(vals)) != k else []}


def pct(total, p):
    return {"q": B(f"A budget of {total} gives {p}% to health. How much is that?", f"{total} ৰ বাজেটৰ {p}% স্বাস্থ্যলৈ। কিমান?"), "answer": str(total * p // 100), "why": B(f"{total} × {p} ÷ 100.", f"{total} × {p} ÷ 100।")}


def change(a, b):
    return {"q": B(f"Sales went from {a} to {b}. What is the percent rise?", f"বিক্ৰী {a} ৰ পৰা {b} হ'ল। শতাংশ বৃদ্ধি কিমান?"), "answer": str((b - a) * 100 // a), "suffix": B("%", "%"), "why": B(f"{b - a} ÷ {a} × 100.", f"{b - a} ÷ {a} × 100।"), "traps": [{"ans": str((b - a) * 100 // b), "tag": "r-m-base", "why": BASE}]}


def lesson_data():
    p = "rs21"
    u1 = unit("u1", B("Read before you calculate", "গণনাৰ আগতে পঢ়া"), "star", [B("Read the title first.", "প্ৰথমে শিৰোনাম।"), B("Check the units.", "একক চোৱা।"), B("Find the row, then the column.", "শাৰী, তাৰ পিছত স্তম্ভ।"), B("Only then calculate.", "তাৰ পিছত গণনা।")], [
        diagram(f"{p}.u1.s1", B("Headings first", "শিৰোনাম আগতে"), [B("Most table errors come from misreading a heading, not from the arithmetic.", "তালিকাৰ বেছিভাগ ভুল শিৰোনামৰ, অংকৰ নহয়।")], "flow", [B("Title", "শিৰোনাম"), B("Unit", "একক"), B("Row and column", "শাৰী আৰু স্তম্ভ")]),
        diagram(f"{p}.u1.s2", B("Watch the unit", "একক চোৱা"), [B("'In thousands' turns 42 into 42,000.", "'হাজাৰত' হ'লে 42 মানে 42,000।")], "flow", [same("42"), B("in thousands", "হাজাৰত"), same("42,000")]),
        solve(f"{p}.u1.q1", TABLE, read_table, [((0, "Asha 30, Bina 45, Rita 25"), 45, "Bina"), ((0, "Ali 52, Ravi 38, Sam 41"), 41, "Sam"), ((0, "Jyoti 60, Mina 75"), 60, "Jyoti")]),
        solve(f"{p}.u1.q2", TABLE, lambda a, b, c: {"q": B(f"Three shops sold {a}, {b} and {c}. What is the total?", f"তিনিখন দোকানত {a}, {b}, {c} বিক্ৰী। মুঠ কিমান?"), "answer": str(a + b + c), "why": B("Add the column.", "স্তম্ভ যোগ।")}, [(24, 36, 40), (120, 85, 95), (66, 34, 50)]),
        tf(f"{p}.u1.q3", TABLE, B("A table headed 'in thousands' showing 5 means 5,000.", "'হাজাৰত' তালিকাত 5 মানে 5,000।"), True, B("Multiply by the unit.", "এককেৰে পূৰণ।"), ("r-m-units", UNIT)),
        match(f"{p}.u1.q4", TABLE, B("Match the entry to its value", "মানৰ লগত মিলোৱা"), [[B("7 in hundreds", "শতত 7"), same(700)], [B("7 in thousands", "হাজাৰত 7"), same(7000)], [B("7 in lakhs", "লাখত 7"), same(700000)]], B("Read the unit.", "একক পঢ়া।")),
        order(f"{p}.u1.q5", TABLE, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the title", "শিৰোনাম"), B("Note the unit", "একক"), B("Find the cell", "ঘৰ উলিওৱা"), B("Calculate", "গণনা")], B("Reading first.", "পঢ়া আগতে।")),
    ])
    u2 = unit("u2", B("Reading charts", "লেখ পঢ়া"), "star", [B("Height shows the value.", "উচ্চতাই মান দেখুৱায়।"), B("Compare bars before reading numbers.", "সংখ্যাৰ আগতে বাৰ তুলনা।"), B("Rises sit between bars.", "বৃদ্ধি বাৰৰ মাজত।"), B("A line chart shows change over time.", "ৰেখা লেখে সময়ৰ সলনি দেখুৱায়।")], [
        diagram(f"{p}.u2.s1", B("Bars compare, lines trend", "বাৰে তুলনা, ৰেখাই গতি"), [B("A bar chart compares groups. A line chart follows one thing through time.", "বাৰ লেখে গোট তুলনা কৰে। ৰেখা লেখে সময়ত অনুসৰণ কৰে।")], "grid", [B("Bar: compare", "বাৰ: তুলনা"), B("Line: trend", "ৰেখা: গতি"), B("Pie: shares", "বৃত্ত: ভাগ")]),
        diagram(f"{p}.u2.s2", B("Highest is not fastest", "ওখ মানে খৰ নহয়"), [B("The tallest bar shows the most. The steepest step shows the fastest rise.", "ওখ বাৰে বেছি দেখুৱায়। খৰ বৃদ্ধি বেলেগ।")], "flow", [B("Highest", "আটাইতকৈ ওখ"), B("Largest rise", "বেছি বৃদ্ধি"), B("Different question", "বেলেগ প্ৰশ্ন")]),
        explore(f"{p}.u2.q1", CHART, bar_top, [(["2020", "2021", "2022", "2023"], [40, 65, 55, 30]), (["2019", "2020", "2021", "2022"], [20, 35, 50, 45])]),
        explore(f"{p}.u2.q2", CHART, bar_rise, [(["2020", "2021", "2022", "2023"], [30, 35, 60, 70]), (["2019", "2020", "2021", "2022"], [50, 45, 70, 80])]),
        tf(f"{p}.u2.q3", CHART, B("The tallest bar always has the biggest rise.", "ওখ বাৰত সদায় বেছি বৃদ্ধি।"), False, B("Rise compares neighbours.", "বৃদ্ধি কাষৰ বাৰৰ তুলনা।")),
        match(f"{p}.u2.q4", CHART, B("Match the chart to its job", "লেখক কামৰ লগত মিলোৱা"), [[B("Bar chart", "বাৰ লেখ"), B("Compare groups", "গোট তুলনা")], [B("Line chart", "ৰেখা লেখ"), B("Trend over time", "সময়ৰ গতি")], [B("Pie chart", "বৃত্ত লেখ"), B("Parts of a whole", "গোটাৰ অংশ")]], B("Each has a job.", "প্ৰতিটোৰ কাম আছে।")),
        order(f"{p}.u2.q5", CHART, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the axes", "অক্ষ পঢ়া"), B("Note the unit", "একক"), B("Compare bars", "বাৰ তুলনা"), B("Answer", "উত্তৰ")], B("Axes first.", "অক্ষ আগতে।")),
    ])
    u3 = unit("u3", B("Parts of a whole", "গোটাৰ অংশ"), "star", [B("All shares add to 100%.", "সকলো ভাগৰ যোগফল 100%।"), B("Share value = total × percent ÷ 100.", "ভাগ = মুঠ × শতাংশ ÷ 100।"), B("A full circle is 360°.", "পূৰ্ণ বৃত্ত 360°।"), B("1% of a circle is 3.6°.", "বৃত্তৰ 1% = 3.6°।")], [
        diagram(f"{p}.u3.s1", B("A whole is 100", "গোটা মানে 100"), [B("If three shares are known, the fourth is what is left of 100.", "তিনিটা ভাগ জানিলে চতুৰ্থটো 100 ৰ বাকী।")], "flow", [same("30%"), same("25%"), same("20%"), same("25%")]),
        diagram(f"{p}.u3.s2", B("Degrees to percent", "ডিগ্ৰীৰ পৰা শতাংশ"), [B("A 90° slice is a quarter of 360°, so 25%.", "90° মানে 360° ৰ চতুৰ্থাংশ, 25%।")], "flow", [same("90°"), same("÷ 360"), same("25%")]),
        solve(f"{p}.u3.q1", PIE, pct, [(800, 25), (1200, 15), (2000, 30)]),
        solve(f"{p}.u3.q2", PIE, lambda a, b, c: {"q": B(f"Shares are {a}%, {b}% and {c}%. What is the remaining share?", f"ভাগ {a}%, {b}%, {c}%। বাকী ভাগ কিমান?"), "answer": str(100 - a - b - c), "suffix": B("%", "%"), "why": B("Shares add to 100.", "ভাগৰ যোগফল 100।")}, [(30, 25, 20), (40, 15, 10), (35, 35, 5)]),
        tf(f"{p}.u3.q3", PIE, B("A 180° slice is 50% of a pie chart.", "বৃত্ত লেখৰ 180° মানে 50%।"), True, B("Half of 360°.", "360° ৰ আধা।")),
        match(f"{p}.u3.q4", PIE, B("Match the slice to its share", "খণ্ডক ভাগৰ লগত মিলোৱা"), [[same("90°"), same("25%")], [same("36°"), same("10%")], [same("72°"), same("20%")]], B("Divide by 3.6.", "3.6 ৰে হৰণ।")),
        order(f"{p}.u3.q5", PIE, B("Smallest slice first", "সৰু খণ্ড আগতে"), [same("10%"), same("25%"), same("50%"), same("75%")], B("Ascending.", "উৰ্ধ্বক্ৰম।")),
    ])
    u4 = unit("u4", B("Rise and fall", "বৃদ্ধি আৰু হ্ৰাস"), "star", [B("Change = new − old.", "সলনি = নতুন − পুৰণি।"), B("Percent change uses the old value.", "শতাংশ সলনিত পুৰণি মান।"), B("Average = total ÷ count.", "গড় = মুঠ ÷ সংখ্যা।"), B("Check the base year.", "ভেটি বছৰ চোৱা।")], [
        diagram(f"{p}.u4.s1", B("The base is the start", "ভেটি আৰম্ভণি"), [B("From 40 to 50 is a rise of 10 on a base of 40, so 25%.", "40 ৰ পৰা 50 মানে 40 ৰ ওপৰত 10, 25%।")], "flow", [same("50 − 40"), same("10 ÷ 40"), same("25%")]),
        diagram(f"{p}.u4.s2", B("Averages", "গড়"), [B("Add the values and divide by how many there are.", "মান যোগ কৰি সংখ্যাৰে হৰণ।")], "flow", [B("Add", "যোগ"), B("Count", "গণনা"), B("Divide", "হৰণ")]),
        solve(f"{p}.u4.q1", CHANGE, change, [(40, 50), (80, 100), (200, 250), (50, 60)]),
        solve(f"{p}.u4.q2", CHANGE, lambda *v: {"q": B(f"Yearly output was {', '.join(map(str, v))}. What is the average?", f"বছৰেকীয়া উৎপাদন {', '.join(map(str, v))}। গড় কিমান?"), "answer": str(sum(v) // len(v)), "why": B(f"{sum(v)} ÷ {len(v)}.", f"{sum(v)} ÷ {len(v)}।")}, [(30, 40, 50), (20, 25, 30, 45), (60, 70, 80)]),
        tf(f"{p}.u4.q3", CHANGE, B("A rise from 50 to 100 is a 100% rise.", "50 ৰ পৰা 100 মানে 100% বৃদ্ধি।"), True, B("It doubled.", "দুগুণ।"), ("r-m-base", BASE)),
        match(f"{p}.u4.q4", CHANGE, B("Match the change to its percent", "সলনিক শতাংশৰ লগত মিলোৱা"), [[same("20 to 30"), same("50%")], [same("40 to 44"), same("10%")], [same("10 to 40"), same("300%")]], B("Divide by the start.", "আৰম্ভণিৰে হৰণ।")),
        order(f"{p}.u4.q5", CHANGE, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Find the change", "সলনি"), B("Divide by the start", "আৰম্ভণিৰে হৰণ"), B("Multiply by 100", "100 ৰে পূৰণ"), B("Add the % sign", "% দিয়া")], B("Base is the start.", "ভেটি আৰম্ভণি।")),
    ])
    test = {"id": "test", "title": B("Data test", "তথ্যৰ পৰীক্ষা"), "steps": [
        explore(f"{p}.t.q1", CHART, bar_top, [(["A", "B", "C", "D"], [15, 40, 25, 30]), (["P", "Q", "R", "S"], [60, 20, 45, 50])]),
        solve(f"{p}.t.q2", PIE, pct, [(600, 20), (1500, 40)]),
        solve(f"{p}.t.q3", CHANGE, change, [(25, 30), (60, 90)]),
        solve(f"{p}.t.q4", TABLE, lambda a, b: {"q": B(f"A table in hundreds shows {a} and {b}. What is the real total?", f"শতৰ তালিকাত {a} আৰু {b}। প্ৰকৃত মুঠ?"), "answer": str((a + b) * 100), "why": B("Add, then multiply by 100.", "যোগ কৰি 100 ৰে পূৰণ।"), "traps": [{"ans": str(a + b), "tag": "r-m-units", "why": UNIT}]}, [(12, 8), (25, 15)]),
        tf(f"{p}.t.q5", PIE, B("A pie chart's shares add to 100%.", "বৃত্ত লেখৰ ভাগৰ যোগফল 100%।"), True, B("It is one whole.", "ই এক গোটা।")),
        tf(f"{p}.t.q6", CHANGE, B("Percent change divides by the new value.", "শতাংশ সলনি নতুন মানেৰে হৰণ।"), False, B("By the old value.", "পুৰণি মানেৰে।"), ("r-m-base", BASE)),
    ]}
    return {"id": "rs-21-data", "no": 21, "slug": "data", "title": B("Tables and charts", "তালিকা আৰু লেখ"), "reign": B("Tables, bars, shares, change", "তালিকা, বাৰ, ভাগ, সলনি"), "units": [u1, u2, u3, u4], "test": test}


def unit_of(p, uid, title, learned, d1, d2, q1, tf_q, m_q, o_q, q5):
    return unit(uid, title, "star", learned, [d1, d2, q1, tf_q, m_q, o_q, q5])


def lesson_comm():
    p = "rs22"
    def st(n, *a):
        return stepwise(f"{p}.{n}", a[0], lambda q, x, y, why: {"q": q, "parts": [part(B("Best choice?", "ভাল বাছনি?"), B(*x), [B(*i) for i in y], why, sid=f"{p}.{n}")], "why": why}, a[1])
    u1 = unit("u1", B("Listening is active", "শ্ৰৱণ সক্ৰিয়"), "star", [B("Give full attention.", "সম্পূৰ্ণ মনোযোগ দিয়া।"), B("Do not interrupt.", "বাধা নিদিবা।"), B("Check that you understood.", "বুজিলানে নিশ্চিত হোৱা।"), B("Respond to what was said.", "কোৱা কথাৰ উত্তৰ দিয়া।")], [
        diagram(f"{p}.u1.s1", B("Hearing is not listening", "শুনা মানে শ্ৰৱণ নহয়"), [B("Active listening means attending, understanding and showing that you did.", "সক্ৰিয় শ্ৰৱণ মানে মনোযোগ, বুজা আৰু সেয়া দেখুওৱা।")], "flow", [B("Attend", "মনোযোগ"), B("Understand", "বুজা"), B("Respond", "সঁহাৰি")]),
        diagram(f"{p}.u1.s2", B("Paraphrase to check", "নিজৰ ভাষাত কোৱা"), [B("'So you mean...' shows you heard and lets the speaker correct you.", "'তেন্তে আপুনি কৈছে...' দেখুৱায় যে শুনিছা।")], "flow", [B("Hear it", "শুনা"), B("Say it back", "ঘূৰাই কোৱা"), B("Confirm", "নিশ্চিত")]),
        inlines(f"{p}.u1.q1", LISTEN, [s(("A colleague is explaining a problem at length.", "এজন সহকৰ্মীয়ে সমস্যা বহলাই কৈছে।"), BEST, ("Listen fully, then ask a question", "সম্পূৰ্ণ শুনি প্ৰশ্ন সোধা"), [("Interrupt with your solution", "বাধা দি সমাধান কোৱা"), ("Check your phone", "ফোন চোৱা")], B("Listen first.", "প্ৰথমে শুনা।")), s(("A citizen is upset at your counter.", "এজন নাগৰিক আপোনাৰ কাউণ্টাৰত অসন্তুষ্ট।"), BEST, ("Let them finish, then restate the issue", "শেষ কৰিবলৈ দি বিষয়টো ঘূৰাই কোৱা"), [("Tell them to calm down", "শান্ত হ'বলৈ কোৱা"), ("Walk away", "গুচি যোৱা")], B("Being heard calms people.", "শুনিলে মানুহ শান্ত হয়।"))]),
        tf(f"{p}.u1.q2", LISTEN, B("Planning your reply while someone speaks is good listening.", "কোনোবাই কওঁতে উত্তৰ ভবা ভাল শ্ৰৱণ।"), False, B("It splits attention.", "ই মনোযোগ ভাগে।"), ("r-m-interrupt", INT)),
        match(f"{p}.u1.q3", LISTEN, B("Match the behaviour to its effect", "আচৰণক ফলৰ লগত মিলোৱা"), [[B("Nodding", "মূৰ দোঁওৱা"), B("Shows attention", "মনোযোগ দেখুৱায়")], [B("Paraphrasing", "ঘূৰাই কোৱা"), B("Checks meaning", "অৰ্থ নিশ্চিত কৰে")], [B("Interrupting", "বাধা দিয়া"), B("Blocks the speaker", "বক্তাক ৰোধ কৰে")]], B("Each has an effect.", "প্ৰতিটোৰ ফল আছে।")),
        order(f"{p}.u1.q4", LISTEN, B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Stop other tasks", "আন কাম ৰখোৱা"), B("Listen to the end", "শেষলৈ শুনা"), B("Paraphrase", "ঘূৰাই কোৱা"), B("Respond", "সঁহাৰি")], B("Attend before responding.", "সঁহাৰিৰ আগতে মনোযোগ।")),
        st("u1.q5", LISTEN, [(B("Someone gives directions too fast.", "কোনোবাই খৰকৈ পথ কৈছে।"), ("Ask them to repeat", "পুনৰ ক'বলৈ কোৱা"), [("Pretend you understood", "বুজা যেন কৰা"), ("Leave", "গুচি যোৱা")], B("Clarify rather than pretend.", "ভাও নকৰি স্পষ্ট কৰা।")), (B("You miss a point in a meeting.", "সভাত এটা কথা নুশুনিলা।"), ("Ask politely afterward", "পিছত ভদ্ৰভাৱে সোধা"), [("Ignore it", "এৰি দিয়া"), ("Guess", "অনুমান কৰা")], B("Ask, do not guess.", "অনুমান নকৰি সোধা।"))]),
    ])
    u2 = unit("u2", B("Giving feedback", "মতামত দিয়া"), "star", [B("Be specific.", "নিৰ্দিষ্ট হোৱা।"), B("Discuss the work, not the person.", "ব্যক্তি নহয়, কাম।"), B("Give it privately when it is critical.", "সমালোচনা গোপনে।"), B("Suggest a next step.", "পিছৰ খোজ কোৱা।")], [
        diagram(f"{p}.u2.s1", B("Work, not person", "ব্যক্তি নহয়, কাম"), [B("'This report missed the date' helps. 'You are careless' only hurts.", "'প্ৰতিবেদনত তাৰিখ নাই' সহায়ক। 'তুমি অসাৱধান' কেৱল দুখ দিয়ে।")], "grid", [B("Specific", "নিৰ্দিষ্ট"), B("About the task", "কামৰ বিষয়ে"), B("Timely", "সময়ত")]),
        diagram(f"{p}.u2.s2", B("Private, then forward", "গোপনে, তাৰ পিছত আগলৈ"), [B("Correct in private and offer a way forward.", "গোপনে শুধৰাই আগবঢ়াৰ পথ দিয়া।")], "flow", [B("In private", "গোপনে"), B("Be specific", "নিৰ্দিষ্ট"), B("Next step", "পিছৰ খোজ")]),
        inlines(f"{p}.u2.q1", FEED, [s(("A junior's report has errors.", "কনিষ্ঠজনৰ প্ৰতিবেদনত ভুল।"), BEST, ("Point out the errors privately", "গোপনে ভুল দেখুওৱা"), [("Announce them in the meeting", "সভাত ঘোষণা কৰা"), ("Say nothing", "একো নকোৱা")], B("Private and specific.", "গোপনে আৰু নিৰ্দিষ্টকৈ।")), s(("A teammate did well on a task.", "সতীৰ্থই ভাল কাম কৰিলে।"), BEST, ("Praise the specific work", "নিৰ্দিষ্ট কামৰ প্ৰশংসা"), [("Say nothing", "একো নকোৱা"), ("Take the credit", "কৃতিত্ব লোৱা")], B("Specific praise helps.", "নিৰ্দিষ্ট প্ৰশংসা সহায়ক।"))]),
        tf(f"{p}.u2.q2", FEED, B("Feedback should target the person's character.", "মতামত ব্যক্তিৰ চৰিত্ৰৰ বিষয়ে হ'ব লাগে।"), False, B("Target the work.", "কামৰ বিষয়ে।")),
        match(f"{p}.u2.q3", FEED, B("Match the phrase to its kind", "বাক্যক ধৰণৰ লগত মিলোৱা"), [[B("'Add the date here'", "'ইয়াত তাৰিখ দিয়া'"), B("Specific", "নিৰ্দিষ্ট")], [B("'This is bad'", "'এয়া বেয়া'"), B("Vague", "অস্পষ্ট")], [B("'You always fail'", "'তুমি সদায় ব্যৰ্থ'"), B("Personal", "ব্যক্তিগত")]], B("Prefer specific.", "নিৰ্দিষ্ট ভাল।")),
        order(f"{p}.u2.q4", FEED, B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Find a private place", "গোপন ঠাই"), B("State what you saw", "দেখাখিনি কোৱা"), B("Say the effect", "ফল কোৱা"), B("Agree a next step", "পিছৰ খোজ")], B("Facts, effect, next step.", "তথ্য, ফল, পিছৰ খোজ।")),
        st("u2.q5", FEED, [(B("You receive criticism at work.", "কামত সমালোচনা পালে।"), ("Listen and ask for examples", "শুনি উদাহৰণ সোধা"), [("Argue at once", "লগে লগে তৰ্ক"), ("Blame others", "আনক দোষ")], B("Treat it as information.", "ইয়াক তথ্য বুলি লোৱা।")), (B("A colleague repeats a mistake.", "সহকৰ্মীয়ে একে ভুল কৰে।"), ("Talk with them calmly", "শান্তভাৱে কোৱা"), [("Mock them", "উপহাস"), ("Complain to all", "সকলোকে অভিযোগ")], B("Direct and calm.", "পোনে পোনে, শান্তভাৱে।"))]),
    ])
    u3 = unit("u3", B("Signals without words", "শব্দহীন সংকেত"), "star", [B("Face and posture carry meaning.", "মুখ আৰু ভংগীয়ে অৰ্থ কঢ়িয়ায়।"), B("Tone can change the words.", "সুৰে শব্দ সলাব পাৰে।"), B("Personal space varies by culture.", "ব্যক্তিগত দূৰত্ব সংস্কৃতি অনুসৰি।"), B("Read signals together, not alone.", "সংকেত একেলগে পঢ়া।")], [
        diagram(f"{p}.u3.s1", B("Beyond the words", "শব্দৰ বাহিৰত"), [B("Tone, face and posture often decide how a message lands.", "সুৰ, মুখ, ভংগীয়ে বাৰ্তা কেনেকৈ পায় ঠিক কৰে।")], "grid", [B("Face", "মুখ"), B("Tone", "সুৰ"), B("Posture", "ভংগী"), B("Distance", "দূৰত্ব")]),
        diagram(f"{p}.u3.s2", B("Do not over-read", "বেছি অৰ্থ নকৰিবা"), [B("Crossed arms may mean cold, not anger. Read several signals together.", "হাত বান্ধি থকা মানে ঠাণ্ডা হ'ব পাৰে। একেলগে পঢ়া।")], "flow", [B("One signal", "এটা সংকেত"), B("More signals", "অধিক সংকেত"), B("Context", "প্ৰসংগ")]),
        inlines(f"{p}.u3.q1", BODY, [s(("You are greeting a visitor.", "আলহী আদৰিছা।"), BEST, ("Stand, smile and face them", "থিয় হৈ হাঁহি মুখামুখি হোৱা"), [("Keep typing", "টাইপ কৰি থকা"), ("Look away", "আনফালে চোৱা")], B("Posture shows respect.", "ভংগীয়ে সন্মান দেখুৱায়।")), s(("Someone leans away as you talk.", "কথা কওঁতে কোনোবা আঁতৰি গৈছে।"), BEST, ("Give more space", "অলপ দূৰত্ব দিয়া"), [("Move closer", "ওচৰলৈ যোৱা"), ("Speak louder", "জোৰে কোৱা")], B("Respect their space.", "তেওঁৰ দূৰত্ব সন্মান কৰা।"))]),
        tf(f"{p}.u3.q2", BODY, B("One gesture proves what a person feels.", "এটা অংগভংগীয়ে অনুভৱ প্ৰমাণ কৰে।"), False, B("Read several signals together.", "একেলগে পঢ়া।")),
        match(f"{p}.u3.q3", BODY, B("Match the channel to an example", "মাধ্যমক উদাহৰণৰ লগত মিলোৱা"), [[B("Verbal", "শাব্দিক"), B("Spoken words", "কোৱা শব্দ")], [B("Written", "লিখিত"), B("A letter", "চিঠি")], [B("Non-verbal", "অশাব্দিক"), B("A nod", "মূৰ দোঁওৱা")]], B("Three channels.", "তিনি মাধ্যম।")),
        order(f"{p}.u3.q4", BODY, B("Put the reading in order", "পঢ়া ক্ৰমে সজোৱা"), [B("Notice the signal", "সংকেত মন কৰা"), B("Look for others", "আনবোৰ চোৱা"), B("Consider context", "প্ৰসংগ"), B("Then respond", "তাৰ পিছত সঁহাৰি")], B("Context before conclusion.", "সিদ্ধান্তৰ আগতে প্ৰসংগ।")),
        st("u3.q5", BODY, [(B("A speaker's words are calm but their voice shakes.", "বক্তাৰ শব্দ শান্ত, কিন্তু মাত কঁপিছে।"), ("Check how they are", "কেনে আছে সোধা"), [("Ignore it", "এৰি দিয়া"), ("Laugh", "হাঁহা")], B("Tone adds information.", "সুৰে তথ্য দিয়ে।")), (B("You must give bad news.", "বেয়া খবৰ দিব লাগে।"), ("Use a calm, kind tone", "শান্ত, মৰমীয়াল সুৰ"), [("Sound cheerful", "ফুৰ্তিত"), ("Shout", "চিঞৰ")], B("Tone must fit.", "সুৰ মিলিব লাগে।"))]),
    ])
    u4 = unit("u4", B("Clear messages", "স্পষ্ট বাৰ্তা"), "star", [B("Know your audience.", "শ্ৰোতা জানা।"), B("State the main point first.", "মূল কথা আগতে।"), B("Use plain words.", "সৰল শব্দ।"), B("Ask for confirmation.", "নিশ্চিত হোৱা।")], [
        diagram(f"{p}.u4.s1", B("Sender to receiver", "প্ৰেৰকৰ পৰা গ্ৰাহকলৈ"), [B("Communication is sender, message, channel, receiver and feedback.", "যোগাযোগ মানে প্ৰেৰক, বাৰ্তা, মাধ্যম, গ্ৰাহক, প্ৰতিক্ৰিয়া।")], "flow", [B("Sender", "প্ৰেৰক"), B("Message", "বাৰ্তা"), B("Receiver", "গ্ৰাহক"), B("Feedback", "প্ৰতিক্ৰিয়া")]),
        diagram(f"{p}.u4.s2", B("Say the point first", "মূল কথা আগতে"), [B("Busy readers stop early. Put what you need in the first line.", "ব্যস্ত পাঠকে সোনকালে ৰয়। প্ৰথম শাৰীতে কোৱা।")], "flow", [B("Point", "মূল কথা"), B("Reason", "কাৰণ"), B("Action", "কাম")]),
        inlines(f"{p}.u4.q1", CLEAR, [s(("You are explaining a form to a farmer.", "খেতিয়কক প্ৰপত্ৰ বুজাইছা।"), BEST, ("Use simple local words", "সৰল স্থানীয় শব্দ"), [("Use official terms only", "কেৱল চৰকাৰী শব্দ"), ("Speak faster", "খৰকৈ কোৱা")], B("Fit the audience.", "শ্ৰোতাৰ উপযোগী।")), s(("You email your officer about a delay.", "পলমৰ বিষয়ে বিষয়াক ইমেইল।"), BEST, ("State the delay and new date first", "পলম আৰু নতুন তাৰিখ আগতে"), [("Start with long background", "দীঘল পটভূমিৰে"), ("Leave out the date", "তাৰিখ এৰা")], B("Point first.", "মূল কথা আগতে।"))]),
        tf(f"{p}.u4.q2", CLEAR, B("Decoding means understanding a received message.", "ডিক'ডিং মানে পোৱা বাৰ্তা বুজা।"), True, B("The receiver decodes.", "গ্ৰাহকে কৰে।")),
        match(f"{p}.u4.q3", CLEAR, B("Match the part to its role", "অংশক ভূমিকাৰ লগত মিলোৱা"), [[B("Sender", "প্ৰেৰক"), B("Encodes", "সংকেতিত কৰে")], [B("Receiver", "গ্ৰাহক"), B("Decodes", "অৰ্থ কৰে")], [B("Feedback", "প্ৰতিক্ৰিয়া"), B("Closes the loop", "চক্ৰ সম্পূৰ্ণ")]], B("A loop, not a line.", "শাৰী নহয়, চক্ৰ।")),
        order(f"{p}.u4.q4", CLEAR, B("Process in order", "প্ৰক্ৰিয়া ক্ৰমে"), [B("Sender forms the idea", "প্ৰেৰকৰ ধাৰণা"), B("Message is sent", "বাৰ্তা প্ৰেৰণ"), B("Receiver decodes", "গ্ৰাহকে বুজে"), B("Feedback returns", "প্ৰতিক্ৰিয়া")], B("The loop.", "চক্ৰ।")),
        st("u4.q5", CLEAR, [(B("You must tell 200 villagers about a camp.", "200 গাঁওবাসীক শিবিৰৰ কথা ক'ব লাগে।"), ("Use a local announcement", "স্থানীয় ঘোষণা"), [("Email each one", "প্ৰত্যেককে ইমেইল"), ("Tell one person", "এজনক কোৱা")], B("Pick the fitting channel.", "উপযুক্ত মাধ্যম।")), (B("A sensitive personal matter must be raised.", "সংবেদনশীল ব্যক্তিগত কথা ক'ব লাগে।"), ("Talk face to face", "মুখামুখি"), [("Post on a group", "গোটত দিয়া"), ("Use a notice board", "জাননী ফলক")], B("Sensitive means private.", "সংবেদনশীল মানে ব্যক্তিগত।"))]),
    ])
    u5 = unit("u5", B("Empathy and rapport", "সমবেদনা আৰু সম্পৰ্ক"), "star", [B("Empathy understands another's view.", "সমবেদনাই আনৰ দৃষ্টিভংগী বুজে।"), B("Sympathy feels sorry for someone.", "সহানুভূতি মানে দুখ পোৱা।"), B("Rapport grows from respect.", "সন্মানৰ পৰা সম্পৰ্ক।"), B("Acknowledge feelings before facts.", "তথ্যৰ আগতে অনুভৱ।")], [
        diagram(f"{p}.u5.s1", B("With them, not for them", "তেওঁৰ লগত"), [B("Empathy says 'I see why this is hard', not 'poor you'.", "সমবেদনাই কয় 'টান বুলি বুজিছোঁ', 'বেচেৰা' নহয়।")], "grid", [B("Empathy: feel with", "সমবেদনা: লগত অনুভৱ"), B("Sympathy: feel for", "সহানুভূতি: কাৰণে অনুভৱ")]),
        diagram(f"{p}.u5.s2", B("Feelings first", "অনুভৱ আগতে"), [B("An upset person cannot take in facts until they feel heard.", "অসন্তুষ্ট মানুহে শুনা নাপালে তথ্য নলয়।")], "flow", [B("Acknowledge", "স্বীকাৰ"), B("Then explain", "তাৰ পিছত বুজোৱা"), B("Then solve", "তাৰ পিছত সমাধান")]),
        inlines(f"{p}.u5.q1", EMP, [s(("A student failed and is upset.", "ছাত্ৰ অনুত্তীৰ্ণ হৈ দুখিত।"), BEST, ("Acknowledge it and offer help", "স্বীকাৰ কৰি সহায় আগবঢ়োৱা"), [("Say it does not matter", "একো নহয় বুলি কোৱা"), ("Compare with toppers", "শীৰ্ষস্থানীয়ৰ লগত তুলনা")], B("Acknowledge, then support.", "স্বীকাৰ, তাৰ পিছত সহায়।")), s(("An elder struggles with an online form.", "জ্যেষ্ঠজনক অনলাইন প্ৰপত্ৰত অসুবিধা।"), BEST, ("Sit with them and guide patiently", "লগত বহি ধৈৰ্যৰে বুজোৱা"), [("Tell them to ask their children", "সন্তানক সুধিবলৈ কোৱা"), ("Fill it without asking", "নুসুধি পূৰণ")], B("Respect and patience.", "সন্মান আৰু ধৈৰ্য।"))]),
        tf(f"{p}.u5.q2", EMP, B("Empathy and sympathy mean exactly the same.", "সমবেদনা আৰু সহানুভূতিৰ অৰ্থ একে।"), False, B("They differ.", "বেলেগ।")),
        match(f"{p}.u5.q3", EMP, B("Match the term to its meaning", "শব্দক অৰ্থৰ লগত মিলোৱা"), [[B("Empathy", "সমবেদনা"), B("Feeling with someone", "লগত অনুভৱ")], [B("Rapport", "সুসম্পৰ্ক"), B("Mutual trust", "পাৰস্পৰিক বিশ্বাস")], [B("Self-awareness", "আত্মসচেতনতা"), B("Knowing yourself", "নিজক জনা")]], B("Three skills.", "তিনি দক্ষতা।")),
        order(f"{p}.u5.q4", EMP, B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Listen", "শুনা"), B("Acknowledge", "স্বীকাৰ"), B("Explain", "বুজোৱা"), B("Agree a way forward", "আগবঢ়াৰ পথ")], B("Feelings before facts.", "তথ্যৰ আগতে অনুভৱ।")),
        st("u5.q5", EMP, [(B("A new colleague eats lunch alone.", "নতুন সহকৰ্মীয়ে অকলে খায়।"), ("Invite them to join", "লগ দিবলৈ মাতা"), [("Ignore them", "এৰি দিয়া"), ("Gossip", "কথা পতা")], B("Include them.", "সামৰি লোৱা।")), (B("A colleague is being teased.", "সহকৰ্মীক জোকোৱা হৈছে।"), ("Speak up respectfully", "সন্মানেৰে মাত মতা"), [("Join in", "লগ লগা"), ("Watch silently", "মনে মনে চোৱা")], B("Do not stay silent.", "মনে মনে নাথাকিবা।"))]),
    ])
    u6 = unit("u6", B("Barriers", "বাধা"), "star", [B("Noise blocks messages.", "কোলাহলে বাৰ্তা ৰোধ কৰে।"), B("Language can divide.", "ভাষাই ভাগ কৰিব পাৰে।"), B("Assumptions distort meaning.", "ধাৰণাই অৰ্থ বিগাৰে।"), B("Culture shapes understanding.", "সংস্কৃতিয়ে বুজাবুজি গঢ়ে।")], [
        diagram(f"{p}.u6.s1", B("Name the barrier", "বাধাৰ নাম কোৱা"), [B("Most failures have a simple cause. Name it, then remove it.", "বেছিভাগ ব্যৰ্থতাৰ সৰল কাৰণ। নাম দি আঁতৰোৱা।")], "grid", [B("Physical: noise", "ভৌতিক: কোলাহল"), B("Language: jargon", "ভাষা: কঠিন শব্দ"), B("Emotional: anger", "আৱেগিক: খং"), B("Cultural: customs", "সাংস্কৃতিক: ৰীতি")]),
        diagram(f"{p}.u6.s2", B("Check, do not assume", "ধৰি নলৈ পৰীক্ষা"), [B("Ask rather than guess what someone meant.", "অনুমান নকৰি সোধা।")], "flow", [B("Notice confusion", "বিভ্ৰান্তি"), B("Ask", "সোধা"), B("Clarify", "স্পষ্ট")]),
        inlines(f"{p}.u6.q1", BARR, [s(("A meeting is drowned by construction noise.", "নিৰ্মাণৰ শব্দত সভা নুশুনা।"), BEST, ("Move to a quieter room", "নিৰিবিলি কোঠালৈ যোৱা"), [("Shout louder", "জোৰে চিঞৰা"), ("Carry on anyway", "তেনেকৈয়ে চলোৱা")], B("Remove the barrier.", "বাধা আঁতৰোৱা।")), s(("A visitor does not follow your language.", "আলহীয়ে তোমাৰ ভাষা নুবুজে।"), BEST, ("Use simple words or a translator", "সৰল শব্দ বা অনুবাদক"), [("Repeat louder", "জোৰে পুনৰাবৃত্তি"), ("Send them away", "পঠিয়াই দিয়া")], B("Bridge the language.", "ভাষাৰ দলং।"))]),
        tf(f"{p}.u6.q2", BARR, B("Jargon can be a barrier for outsiders.", "কঠিন পৰিভাষা বাহিৰৰ মানুহৰ বাবে বাধা।"), True, B("Use plain words.", "সৰল শব্দ।")),
        match(f"{p}.u6.q3", BARR, B("Match the barrier to its type", "বাধাক ধৰণৰ লগত মিলোৱা"), [[B("Loud traffic", "জোৰ যান-বাহন"), B("Physical", "ভৌতিক")], [B("Technical terms", "কাৰিকৰী শব্দ"), B("Language", "ভাষা")], [B("Anger", "খং"), B("Emotional", "আৱেগিক")]], B("Name it.", "নাম কোৱা।")),
        order(f"{p}.u6.q4", BARR, B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Spot the problem", "সমস্যা চিনা"), B("Name the barrier", "বাধাৰ নাম"), B("Change approach", "পদ্ধতি সলনি"), B("Confirm it worked", "নিশ্চিত")], B("Name, then fix.", "নাম, তাৰ পিছত সমাধান।")),
        st("u6.q5", BARR, [(B("Colleagues from different cultures disagree on a greeting.", "বেলেগ সংস্কৃতিৰ সহকৰ্মীৰ অভিবাদনৰ মতভেদ।"), ("Ask and respect the custom", "সুধি ৰীতি সন্মান"), [("Mock it", "উপহাস"), ("Insist on yours", "নিজৰটো জোৰ")], B("Respect difference.", "পাৰ্থক্য সন্মান।")), (B("You are unsure what a message meant.", "বাৰ্তাৰ অৰ্থত সন্দেহ।"), ("Ask the sender", "প্ৰেৰকক সোধা"), [("Assume the worst", "বেয়াটো ধৰা"), ("Ignore it", "এৰি দিয়া")], B("Clarify.", "স্পষ্ট কৰা।"))]),
    ])
    test = {"id": "test", "title": B("Communication test", "যোগাযোগৰ পৰীক্ষা"), "steps": [
        tf(f"{p}.t.q1", LISTEN, B("Paraphrasing checks understanding.", "ঘূৰাই কোৱাই বুজাবুজি নিশ্চিত কৰে।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q2", FEED, B("Critical feedback is best given in public.", "সমালোচনা ৰাজহুৱাকৈ দিয়া ভাল।"), False, B("Give it privately.", "গোপনে দিয়া।")),
        tf(f"{p}.t.q3", BODY, B("Tone can change a message's meaning.", "সুৰে বাৰ্তাৰ অৰ্থ সলাব পাৰে।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q4", CLEAR, B("Feedback completes the communication loop.", "প্ৰতিক্ৰিয়াই যোগাযোগৰ চক্ৰ সম্পূৰ্ণ কৰে।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q5", EMP, B("Empathy means feeling with someone.", "সমবেদনা মানে লগত অনুভৱ।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q6", BARR, B("Assumptions can distort a message.", "ধাৰণাই বাৰ্তা বিগাৰিব পাৰে।"), True, B("Yes.", "হয়।")),
    ]}
    return {"id": "rs-22-communication", "no": 22, "slug": "communication", "title": B("Communication", "যোগাযোগ"), "reign": B("Listening, feedback, empathy", "শ্ৰৱণ, মতামত, সমবেদনা"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


def dec_unit(p, n, skill, title, learned, d1, d2, rows, tfq, m, o, st_rows):
    uid = f"u{n}"
    return unit(uid, title, "star", learned, [
        diagram(f"{p}.{uid}.s1", *d1), diagram(f"{p}.{uid}.s2", *d2), inlines(f"{p}.{uid}.q1", skill, rows),
        tf(f"{p}.{uid}.q2", skill, *tfq), match(f"{p}.{uid}.q3", skill, *m), order(f"{p}.{uid}.q4", skill, *o),
        stepwise(f"{p}.{uid}.q5", skill, lambda q, x, y, why: {"q": q, "parts": [part(B("Best choice?", "ভাল বাছনি?"), B(*x), [B(*i) for i in y], why, sid=f"{p}.{uid}.q5")], "why": why}, st_rows),
    ])


def lesson_decisions():
    p = "rs23"
    fl = "flow"
    u1 = dec_unit(p, 1, DUTY, B("Rules and duty", "নিয়ম আৰু কৰ্তব্য"), [B("Know the rule first.", "প্ৰথমে নিয়ম জানা।"), B("Follow procedure even under pressure.", "হেঁচাতো পদ্ধতি মানা।"), B("Escalate what you cannot decide.", "ঠিক কৰিব নোৱৰা কথা ওপৰলৈ।"), B("Record what you did.", "কৰা কাম লিখি ৰাখা।")],
        (B("Duty comes before convenience", "সুবিধাতকৈ কৰ্তব্য"), [B("Public service means applying rules equally, even when bending them seems easier.", "ৰাজহুৱা সেৱা মানে নিয়ম সমানে প্ৰয়োগ।")], fl, [B("Know the rule", "নিয়ম জানা"), B("Apply it", "প্ৰয়োগ"), B("Record it", "লিখা")]),
        (B("When to escalate", "কেতিয়া ওপৰলৈ"), [B("If a decision is beyond your authority, refer it with the facts.", "তোমাৰ ক্ষমতাৰ বাহিৰ হ'লে তথ্যসহ ওপৰলৈ পঠিওৱা।")], fl, [B("Check authority", "ক্ষমতা"), B("Gather facts", "তথ্য"), B("Refer upward", "ওপৰলৈ")]),
        [s(("A friend asks you to skip the queue for a certificate.", "বন্ধুৱে প্ৰমাণপত্ৰৰ শাৰী এৰিবলৈ ক'লে।"), BEST, ("Politely ask them to follow the queue", "ভদ্ৰভাৱে শাৰীত থাকিবলৈ কোৱা"), [("Do it quietly", "গোপনে কৰা"), ("Refuse rudely", "ৰূঢ়ভাৱে নাকচ")], B("Treat all equally.", "সকলোক সমান।")), s(("You find a rule that seems outdated.", "নিয়ম পুৰণি যেন লাগিল।"), BEST, ("Follow it and report the issue", "মানি বিষয়টো জনোৱা"), [("Ignore it", "এৰি দিয়া"), ("Change it yourself", "নিজে সলোৱা")], B("Raise it through the proper channel.", "সঠিক পথে জনোৱা।"))],
        (B("Following procedure is part of public duty.", "পদ্ধতি মানা ৰাজহুৱা কৰ্তব্যৰ অংশ।"), True, B("It protects fairness.", "ই ন্যায্যতা ৰক্ষা কৰে।")),
        (B("Match the action to its reason", "কামক কাৰণৰ লগত মিলোৱা"), [[B("Record decisions", "সিদ্ধান্ত লিখা"), B("Accountability", "জবাবদিহিতা")], [B("Apply rules equally", "নিয়ম সমানে"), B("Fairness", "ন্যায্যতা")], [B("Refer upward", "ওপৰলৈ"), B("Proper authority", "সঠিক কৰ্তৃপক্ষ")]], B("Each protects something.", "প্ৰতিটোৱে কিবা ৰক্ষা কৰে।")),
        (B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Read the rule", "নিয়ম পঢ়া"), B("Check the facts", "তথ্য"), B("Act or refer", "কাম বা ওপৰলৈ"), B("Record it", "লিখা")], B("Rule, facts, action, record.", "নিয়ম, তথ্য, কাম, লিখা।")),
        [(B("A senior asks you to backdate a file.", "জ্যেষ্ঠজনে ফাইলৰ তাৰিখ আগৰ কৰিবলৈ ক'লে।"), ("Decline and note it", "নাকচ কৰি লিখি ৰাখা"), [("Do it", "কৰা"), ("Tell everyone", "সকলোকে কোৱা")], B("Records must be true.", "নথি সত্য হ'ব লাগে।")), (B("A request falls outside your office.", "অনুৰোধ তোমাৰ কাৰ্যালয়ৰ বাহিৰৰ।"), ("Direct them to the right office", "সঠিক কাৰ্যালয়লৈ পঠিওৱা"), [("Ignore them", "এৰি দিয়া"), ("Decide anyway", "তথাপি সিদ্ধান্ত")], B("Guide, do not guess.", "পথ দেখুওৱা।"))])
    u2 = dec_unit(p, 2, SAFE, B("Safety comes first", "সুৰক্ষা আগতে"), [B("Protect life first.", "প্ৰথমে জীৱন।"), B("Then property.", "তাৰ পিছত সম্পত্তি।"), B("Call for help early.", "সোনকালে সহায় মাতা।"), B("Warn others.", "আনক সতৰ্ক কৰা।")],
        (B("Life before property", "সম্পত্তিৰ আগত জীৱন"), [B("In an emergency, ask who is in danger before what might be lost.", "জৰুৰী অৱস্থাত কি হেৰাব তাৰ আগতে কোন বিপদত সোধা।")], fl, [B("People", "মানুহ"), B("Help", "সহায়"), B("Property", "সম্পত্তি")]),
        (B("Report a hazard", "বিপদ জনোৱা"), [B("A hazard you ignore becomes someone else's accident.", "এৰি দিয়া বিপদ আনৰ দুৰ্ঘটনা হয়।")], fl, [B("Notice", "মন কৰা"), B("Warn", "সতৰ্ক"), B("Report", "জনোৱা")]),
        [s(("You smell gas in the office.", "কাৰ্যালয়ত গেছৰ গোন্ধ।"), FIRST, ("Get people out and call for help", "মানুহ উলিয়াই সহায় মাতা"), [("Finish your work", "কাম শেষ কৰা"), ("Light a match to check", "জুই জ্বলাই চোৱা")], B("Life first.", "জীৱন আগতে।")), s(("A road is flooding near a school.", "বিদ্যালয়ৰ ওচৰৰ পথ বুৰিছে।"), FIRST, ("Warn the school and authorities", "বিদ্যালয় আৰু কৰ্তৃপক্ষক জনোৱা"), [("Post a photo", "ফটো দিয়া"), ("Wait and see", "অপেক্ষা")], B("Warn early.", "সোনকালে সতৰ্ক।"))],
        (B("Saving files comes before leaving a burning building.", "জ্বলি থকা ঘৰৰ পৰা ওলোৱাৰ আগতে ফাইল বচোৱা।"), False, B("Leave at once.", "লগে লগে ওলোৱা।")),
        (B("Match the order of care", "যত্নৰ ক্ৰম মিলোৱা"), [[B("First", "প্ৰথম"), B("People", "মানুহ")], [B("Second", "দ্বিতীয়"), B("Environment", "পৰিৱেশ")], [B("Third", "তৃতীয়"), B("Property", "সম্পত্তি")]], B("Life leads.", "জীৱন আগত।")),
        (B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Check for danger", "বিপদ চোৱা"), B("Move people", "মানুহ আঁতৰোৱা"), B("Call for help", "সহায় মাতা"), B("Report", "জনোৱা")], B("People first.", "মানুহ আগতে।")),
        [(B("You see a bare wire on a wet floor.", "তিতা মজিয়াত উদং তাঁৰ।"), ("Keep people away and report it", "মানুহ আঁতৰাই জনোৱা"), [("Touch it", "চুই চোৱা"), ("Ignore it", "এৰি দিয়া")], B("Isolate and report.", "পৃথক কৰি জনোৱা।")), (B("A colleague faints.", "সহকৰ্মী অচেতন।"), ("Get medical help", "চিকিৎসা সহায়"), [("Keep working", "কাম চলোৱা"), ("Film it", "ভিডিঅ'")], B("Help first.", "সহায় আগতে।"))])
    u3 = dec_unit(p, 3, FAIR, B("Fairness and inclusion", "ন্যায্যতা আৰু সামৰণি"), [B("Treat people equally.", "সকলোক সমান।"), B("Adjust for disability.", "দিব্যাংগৰ বাবে সলনি।"), B("Avoid favouritism.", "পক্ষপাত নকৰিবা।"), B("Give reasons for decisions.", "সিদ্ধান্তৰ কাৰণ দিয়া।")],
        (B("Equal is not always same", "সমান মানে সদায় একে নহয়"), [B("A ramp treats a wheelchair user fairly, though stairs are 'the same for all'.", "চকীৰ বাবে ৰেম্পেহে ন্যায্য।")], fl, [B("See the need", "প্ৰয়োজন"), B("Remove the barrier", "বাধা আঁতৰোৱা"), B("Equal access", "সমান সুযোগ")]),
        (B("No favourites", "পক্ষপাত নাই"), [B("Relatives and friends get the same process as everyone.", "আত্মীয়-বন্ধুৱেও একে প্ৰক্ৰিয়া পায়।")], fl, [B("Declare the link", "সম্পৰ্ক জনোৱা"), B("Step aside", "আঁতৰি থকা"), B("Same process", "একে প্ৰক্ৰিয়া")]),
        [s(("A candidate who uses a wheelchair arrives at an upstairs office.", "চকী ব্যৱহাৰকাৰী প্ৰাৰ্থী ওপৰ মহলাৰ কাৰ্যালয়লৈ আহিল।"), BEST, ("Meet them on the ground floor", "তলৰ মহলাত লগ কৰা"), [("Tell them to climb", "উঠিবলৈ কোৱা"), ("Send them away", "পঠিয়াই দিয়া")], B("Remove the barrier.", "বাধা আঁতৰোৱা।")), s(("Your cousin applies to a post you are selecting for.", "সম্পৰ্কীয়জনে তোমাৰ বাছনিৰ পদত আবেদন কৰিলে।"), BEST, ("Declare it and step aside", "জনাই আঁতৰি থকা"), [("Help them quietly", "গোপনে সহায়"), ("Say nothing", "একো নকোৱা")], B("Declare conflicts.", "স্বাৰ্থৰ সংঘাত জনোৱা।"))],
        (B("Reasonable adjustment for disability is unfair to others.", "দিব্যাংগৰ বাবে সলনি আনৰ প্ৰতি অন্যায়।"), False, B("It gives equal access.", "ই সমান সুযোগ দিয়ে।")),
        (B("Match the principle", "নীতি মিলোৱা"), [[B("Equal treatment", "সমান ব্যৱহাৰ"), B("Same rules for all", "সকলোলৈ একে নিয়ম")], [B("Equity", "সমতা"), B("Support by need", "প্ৰয়োজন অনুসৰি সহায়")], [B("Impartiality", "নিৰপেক্ষতা"), B("No favourites", "পক্ষপাত নাই")]], B("Three ideas.", "তিনিটা ধাৰণা।")),
        (B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Spot the barrier", "বাধা চিনা"), B("Ask what is needed", "প্ৰয়োজন সোধা"), B("Adjust", "সলনি"), B("Check it worked", "নিশ্চিত")], B("Ask, do not assume.", "ধৰি নলৈ সোধা।")),
        [(B("Two equal applicants differ only by religion.", "দুজন সমান প্ৰাৰ্থীৰ কেৱল ধৰ্ম বেলেগ।"), ("Ignore religion entirely", "ধৰ্ম এৰি চলা"), [("Prefer your own", "নিজৰটো"), ("Ask about it", "সোধা")], B("It is irrelevant.", "ই অপ্ৰাসংগিক।")), (B("A rural woman cannot read the form.", "গ্ৰাম্য মহিলাই প্ৰপত্ৰ পঢ়িব নোৱাৰে।"), ("Read it out and help", "পঢ়ি শুনাই সহায়"), [("Refuse service", "সেৱা নাকচ"), ("Laugh", "হাঁহা")], B("Serve all.", "সকলোক সেৱা।"))])
    u4 = dec_unit(p, 4, HONEST, B("Integrity", "সততা"), [B("Refuse gifts for duty.", "কৰ্তব্যৰ বাবে উপহাৰ নলবা।"), B("Admit your mistakes.", "ভুল স্বীকাৰ কৰা।"), B("Protect public money.", "ৰাজহুৱা ধন ৰক্ষা কৰা।"), B("Report wrongdoing.", "অন্যায় জনোৱা।")],
        (B("Doing right when unseen", "নেদেখাতো শুদ্ধ কাম"), [B("Integrity is the same conduct whether watched or not.", "সততা মানে চোৱা হওক বা নহওক, একে আচৰণ।")], fl, [B("Right action", "শুদ্ধ কাম"), B("No audience", "দৰ্শক নাই"), B("Same choice", "একে বাছনি")]),
        (B("Own your mistakes", "ভুল স্বীকাৰ"), [B("Reporting your error early limits harm and keeps trust.", "সোনকালে ভুল জনালে ক্ষতি কম, বিশ্বাস থাকে।")], fl, [B("Notice", "মন কৰা"), B("Report", "জনোৱা"), B("Correct", "শুধৰোৱা")]),
        [s(("A contractor offers you a gift before a tender decision.", "নিবিদাৰ আগতে ঠিকাদাৰে উপহাৰ দিলে।"), BEST, ("Refuse and report it", "নাকচ কৰি জনোৱা"), [("Accept quietly", "গোপনে লোৱা"), ("Ask for more", "আৰু বিচৰা")], B("Gifts compromise decisions.", "উপহাৰে সিদ্ধান্ত বিগাৰে।")), s(("You notice your own error in a payment list.", "পৰিশোধৰ তালিকাত নিজৰ ভুল দেখিলে।"), BEST, ("Report and correct it", "জনাই শুধৰোৱা"), [("Hide it", "লুকুওৱা"), ("Blame a clerk", "কেৰাণীক দোষ")], B("Own it.", "স্বীকাৰ কৰা।"))],
        (B("Small bribes are acceptable if everyone takes them.", "সকলোৱে ল'লে সৰু উৎকোচ চলে।"), False, B("A bribe is a bribe.", "উৎকোচ উৎকোচেই।")),
        (B("Match the action to the value", "কামক মূল্যবোধৰ লগত মিলোৱা"), [[B("Refuse a gift", "উপহাৰ নাকচ"), B("Honesty", "সততা")], [B("Admit an error", "ভুল স্বীকাৰ"), B("Accountability", "জবাবদিহিতা")], [B("Save public funds", "ৰাজহুৱা ধন ৰক্ষা"), B("Stewardship", "ন্যাসৰক্ষা")]], B("Name the value.", "মূল্যবোধৰ নাম।")),
        (B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Notice the error", "ভুল মন কৰা"), B("Stop further harm", "ক্ষতি ৰখোৱা"), B("Report it", "জনোৱা"), B("Correct it", "শুধৰোৱা")], B("Stop, tell, fix.", "ৰখোৱা, জনোৱা, শুধৰোৱা।")),
        [(B("A colleague misuses office funds.", "সহকৰ্মীয়ে কাৰ্যালয়ৰ ধন অপব্যৱহাৰ কৰিছে।"), ("Report through proper channels", "সঠিক পথে জনোৱা"), [("Ask for a share", "ভাগ বিচৰা"), ("Post online", "অনলাইনত দিয়া")], B("Use the right channel.", "সঠিক পথ।")), (B("You are told exam questions early.", "তোমাক আগতে প্ৰশ্ন জনোৱা হ'ল।"), ("Refuse and report", "নাকচ কৰি জনোৱা"), [("Use them", "ব্যৱহাৰ"), ("Share them", "বিলোৱা")], B("Protect fairness.", "ন্যায্যতা ৰক্ষা।"))])
    u5 = dec_unit(p, 5, TEAM, B("Working in teams", "দলত কাম"), [B("Share credit.", "কৃতিত্ব ভগাই লোৱা।"), B("Resolve conflict directly.", "সংঘাত পোনে পোনে সমাধান।"), B("Divide work by strength.", "দক্ষতা অনুসৰি কাম।"), B("Support weaker members.", "দুৰ্বলক সহায়।")],
        (B("Conflict is about issues", "সংঘাত বিষয়ৰ"), [B("Discuss the problem, not the person, and look for shared goals.", "ব্যক্তি নহয়, সমস্যা; উমৈহতীয়া লক্ষ্য বিচাৰা।")], fl, [B("Listen to both", "দুয়োজনক শুনা"), B("Find common ground", "উমৈহতীয়া"), B("Agree a step", "খোজত সন্মতি")]),
        (B("Leaders serve the team", "নেতাই দলক সেৱা কৰে"), [B("Good leaders share credit and take responsibility.", "ভাল নেতাই কৃতিত্ব ভগায়, দায়িত্ব লয়।")], fl, [B("Clear roles", "স্পষ্ট ভূমিকা"), B("Support", "সহায়"), B("Shared credit", "ভগোৱা কৃতিত্ব")]),
        [s(("Two team members argue over a task.", "দুজন সদস্যৰ কামৰ বিষয়ে তৰ্ক।"), BEST, ("Hear both and agree roles", "দুয়োজনক শুনি ভূমিকা ঠিক কৰা"), [("Take one side", "এফাল লোৱা"), ("Ignore it", "এৰি দিয়া")], B("Hear both.", "দুয়োজনক শুনা।")), s(("Your team's project wins praise.", "দলৰ প্ৰকল্পে প্ৰশংসা পালে।"), BEST, ("Credit the whole team", "গোটেই দলক কৃতিত্ব"), [("Claim it alone", "অকলে দাবী"), ("Stay away", "আঁতৰি থকা")], B("Share credit.", "কৃতিত্ব ভগোৱা।"))],
        (B("A leader should take credit and share blame.", "নেতাই কৃতিত্ব ল'ব, দোষ ভগাব লাগে।"), False, B("It is the reverse.", "ওলোটা।")),
        (B("Match the situation to the action", "অৱস্থাক কামৰ লগত মিলোৱা"), [[B("Unclear roles", "অস্পষ্ট ভূমিকা"), B("Define them", "ঠিক কৰা")], [B("A struggling member", "অসুবিধাত সদস্য"), B("Support them", "সহায়")], [B("A dispute", "বিবাদ"), B("Hear both", "দুয়োকে শুনা")]], B("Name the need.", "প্ৰয়োজনৰ নাম।")),
        (B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Hear each side", "প্ৰতিফাল শুনা"), B("Find the issue", "বিষয় উলিওৱা"), B("Agree a step", "খোজত সন্মতি"), B("Check back", "পৰীক্ষা")], B("Listen first.", "শুনা আগতে।")),
        [(B("A teammate misses a deadline.", "সতীৰ্থই সময়সীমা হেৰুৱালে।"), ("Ask what happened and help", "কি হ'ল সুধি সহায়"), [("Scold publicly", "ৰাজহুৱাকৈ গালি"), ("Do nothing", "একো নকৰা")], B("Understand, then act.", "বুজি কাম।")), (B("A task needs skills you lack.", "কামত তোমাৰ নথকা দক্ষতা লাগে।"), ("Ask a skilled colleague", "দক্ষ সহকৰ্মীক সোধা"), [("Hide it", "লুকুওৱা"), ("Quit", "এৰি দিয়া")], B("Use the team.", "দল ব্যৱহাৰ।"))])
    u6 = dec_unit(p, 6, CRISIS, B("In a crisis", "সংকটত"), [B("Stay calm.", "শান্ত থাকা।"), B("Get accurate facts.", "সঠিক তথ্য।"), B("Inform the public truthfully.", "ৰাইজক সত্য জনোৱা।"), B("Stop rumours early.", "গুজৱ সোনকালে ৰখোৱা।")],
        (B("Facts beat rumours", "তথ্যই গুজৱ হৰায়"), [B("In a flood or outbreak, clear official information stops panic.", "বান বা মহামাৰীত স্পষ্ট চৰকাৰী তথ্যই আতংক ৰখায়।")], fl, [B("Check facts", "তথ্য চোৱা"), B("Tell the public", "ৰাইজক জনোৱা"), B("Update often", "সঘনে জনোৱা")]),
        (B("First steps", "প্ৰথম খোজ"), [B("Protect people, inform authorities, then organise relief.", "মানুহ ৰক্ষা, কৰ্তৃপক্ষক জনোৱা, তাৰ পিছত সাহায্য।")], fl, [B("Rescue", "উদ্ধাৰ"), B("Report", "জনোৱা"), B("Relief", "সাহায্য")]),
        [s(("A rumour says a dam will burst.", "গুজৱ: বান্ধ ভাঙিব।"), FIRST, ("Verify and share official facts", "সত্য চাই চৰকাৰী তথ্য দিয়া"), [("Forward it", "আগবঢ়োৱা"), ("Say nothing", "একো নকোৱা")], B("Check, then tell.", "চাই জনোৱা।")), s(("Relief supplies are short in your block.", "খণ্ডত সাহায্য কম।"), FIRST, ("Prioritise the most vulnerable", "দুৰ্বলক অগ্ৰাধিকাৰ"), [("Serve friends first", "বন্ধুক আগতে"), ("Stop distribution", "বিতৰণ বন্ধ")], B("Greatest need first.", "বেছি প্ৰয়োজন আগতে।"))],
        (B("Forwarding unverified warnings helps in a crisis.", "সংকটত অপ্ৰমাণিত সতৰ্কবাণী আগবঢ়োৱা সহায়ক।"), False, B("It spreads panic.", "ই আতংক বিয়পায়।")),
        (B("Match the crisis step", "সংকটৰ খোজ মিলোৱা"), [[B("Rumour", "গুজৱ"), B("Verify", "সত্যাপন")], [B("Injury", "আঘাত"), B("First aid", "প্ৰাথমিক চিকিৎসা")], [B("Shortage", "অভাৱ"), B("Prioritise", "অগ্ৰাধিকাৰ")]], B("Each has a response.", "প্ৰতিটোৰ সঁহাৰি।")),
        (B("Put the steps in order", "খোজ ক্ৰমে সজোৱা"), [B("Make people safe", "মানুহ সুৰক্ষিত"), B("Get the facts", "তথ্য"), B("Inform the public", "ৰাইজক জনোৱা"), B("Review afterwards", "পিছত পৰ্যালোচনা")], B("Safety, facts, information, review.", "সুৰক্ষা, তথ্য, জনোৱা, পৰ্যালোচনা।")),
        [(B("Crowds gather at a relief camp.", "সাহায্য শিবিৰত ভিৰ।"), ("Organise queues calmly", "শান্তভাৱে শাৰী"), [("Close the camp", "শিবিৰ বন্ধ"), ("Shout at them", "চিঞৰা")], B("Order saves time.", "শৃংখলাই সময় ৰাহি।")), (B("The media asks for details you lack.", "সংবাদ মাধ্যমে নথকা তথ্য সুধিলে।"), ("Say what is known and promise updates", "জনাখিনি কৈ পিছত জনাম বুলি কোৱা"), [("Guess", "অনুমান"), ("Lie", "মিছা")], B("Honest and brief.", "সৎ আৰু চুটি।"))])
    test = {"id": "test", "title": B("Decision making test", "সিদ্ধান্ত গ্ৰহণৰ পৰীক্ষা"), "steps": [
        tf(f"{p}.t.q1", DUTY, B("Refer decisions beyond your authority.", "ক্ষমতাৰ বাহিৰৰ সিদ্ধান্ত ওপৰলৈ।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q2", SAFE, B("Life comes before property.", "সম্পত্তিৰ আগত জীৱন।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q3", FAIR, B("Declare any personal link to a candidate.", "প্ৰাৰ্থীৰ লগত ব্যক্তিগত সম্পৰ্ক জনোৱা।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q4", HONEST, B("A gift before a tender can be kept if small.", "নিবিদাৰ আগৰ সৰু উপহাৰ ৰাখিব পাৰি।"), False, B("Refuse it.", "নাকচ কৰা।")),
        tf(f"{p}.t.q5", TEAM, B("Good leaders share credit.", "ভাল নেতাই কৃতিত্ব ভগায়।"), True, B("Yes.", "হয়।")),
        tf(f"{p}.t.q6", CRISIS, B("Verify before sharing in a crisis.", "সংকটত বিলোৱাৰ আগতে সত্য চোৱা।"), True, B("Yes.", "হয়।")),
    ]}
    return {"id": "rs-23-decisions", "no": 23, "slug": "decisions", "title": B("Decision making", "সিদ্ধান্ত গ্ৰহণ"), "reign": B("Duty, safety, integrity, crisis", "কৰ্তব্য, সুৰক্ষা, সততা, সংকট"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


def mod(fn):
    return type("L", (), {"lesson": staticmethod(fn)})


LESSONS = [mod(lesson_data), mod(lesson_comm), mod(lesson_decisions)]
