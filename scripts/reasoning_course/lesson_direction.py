"""Lesson 9: Direction sense."""
from math_kit import B, match, mcq, order, part, solve, stepwise, tf, unit, with_variants
from math_lessons_c import diagram, lab
from math_labs import task
from reason_kit import face_as, face_en, place, route_text, spot, walk

TURN = "r-turn"; ROUTE = "r-route"; DIST = "r-dist"; SHADOW = "r-shadow"
WEST = B("You took left as west. Left is west only when you face north.", "তুমি বাওঁফালক পশ্চিম বুলি ধৰিলা। উত্তৰলৈ মুখ কৰিলেহে বাওঁফাল পশ্চিম।")
ADDED = B("You added the walks. The straight line is shorter: use the two net distances.", "তুমি খোজবোৰ যোগ কৰিলা। পোনে পোনে দূৰত্ব কম: দুটা নিকা দূৰত্ব ব্যৱহাৰ কৰা।")
SUNSIDE = B("A shadow falls away from the sun, not towards it.", "ছাঁ সূৰ্যৰ ওলোটা ফালে পৰে, সূৰ্যৰ ফালে নহয়।")


def turns_text(moves):
    en = " then ".join("left" if m == "L" else "right" for m in moves)
    as_ = " তাৰ পিছত ".join("বাওঁফালে" if m == "L" else "সোঁফালে" for m in moves)
    return en, as_


def turn_q(f, moves):
    end = walk(f, moves)[2]
    swapped = walk(f, ["L" if m == "R" else "R" for m in moves])[2]
    en, as_ = turns_text(moves)
    step = {"q": B(f"Face {face_en(f)}, then turn {en}. Turn the walker and stop.", f"{face_as(f)}লৈ মুখ কৰি {as_} ঘূৰা। খোজকাৰীক ঘূৰাই ৰখোৱা।"),
            "widget": {"kind": "walk", "f": f, "turnOnly": True, "ask": "facing"}, "target": end, "answerText": B(f"Facing {face_en(end)}", f"{face_as(end)}লৈ মুখ"),
            "why": B(f"Each turn is measured from where you face now, so you end facing {face_en(end)}.", f"প্ৰতিটো ঘূৰণি এতিয়াৰ মুখৰ পৰা, গতিকে শেষত {face_as(end)}লৈ মুখ।")}
    # Every version sets traps: a version without them would inherit the first version's.
    step["traps"] = [{"val": swapped, "tag": "r-m-leftwest", "why": WEST}] if swapped != end else []
    return step


def two_turns(f, a, b):
    s = "rs9.u1.q4"
    g1, g2 = walk(f, [a])[2], walk(f, [a, b])[2]
    word = lambda m: ("left", "বাওঁফালে") if m == "L" else ("right", "সোঁফালে")
    other = lambda x: [(x + 1) % 4, (x + 2) % 4, (x + 3) % 4]
    fb = lambda x: B(face_en(x).capitalize(), face_as(x))
    return {"q": B(f"Face {face_en(f)}, turn {word(a)[0]}, then turn {word(b)[0]}.", f"{face_as(f)}লৈ মুখ কৰি {word(a)[1]}, তাৰ পিছত {word(b)[1]} ঘূৰা।"), "parts": [
        part(B("After the first turn you face?", "প্ৰথম ঘূৰণিৰ পিছত মুখ কোন ফালে?"), fb(g1), [fb(x) for x in other(g1)[:2]], B("Measure the turn from your own facing.", "নিজৰ মুখৰ পৰা ঘূৰণি জোখা।"), tag="r-m-leftwest", sid=s),
        part(B("After the second turn you face?", "দ্বিতীয় ঘূৰণিৰ পিছত মুখ কোন ফালে?"), fb(g2), [fb(x) for x in other(g2)[:2]], B("Start from the new facing, not the old one.", "নতুন মুখৰ পৰা আৰম্ভ কৰা, পুৰণিটোৰ পৰা নহয়।"), sid=s),
    ], "why": B(f"You end facing {face_en(g2)}.", f"শেষত {face_as(g2)}লৈ মুখ।")}


def route_q(f, route):
    x, y, _ = walk(f, route)
    en, as_ = route_text(f, route)
    mirror = walk(f, ["L" if m == "R" else "R" if m == "L" else m for m in route])
    a, b = spot(x, y)
    step = {"q": B(f"Start at the dot. {en}", f"বিন্দুৰ পৰা আৰম্ভ কৰা। {as_}"), "widget": {"kind": "walk", "f": f, "ask": "place"}, "target": place(x, y), "answerText": B(f"You end {a} of the start", f"আৰম্ভণিৰ পৰা {b}"),
            "why": B(f"Walking it step by step ends {a} of the start.", f"খোজে খোজে গ'লে আৰম্ভণিৰ পৰা {b} ত শেষ হয়।")}
    step["traps"] = [{"val": place(*mirror[:2]), "tag": "r-m-leftwest", "why": WEST}] if mirror[:2] != (x, y) else []
    return step


def end_face(f, route):
    end = walk(f, route)[2]
    en, as_ = route_text(f, route)
    return {"q": B(f"{en} Which way do you face now? Turn the walker to match.", f"{as_} এতিয়া মুখ কোন ফালে? খোজকাৰীক সেইফালে ঘূৰোৱা।"), "widget": {"kind": "walk", "f": f, "turnOnly": True, "ask": "facing"}, "target": end, "answerText": B(f"Facing {face_en(end)}", f"{face_as(end)}লৈ মুখ"),
            "why": B("Walking changes where you are. Only turns change where you face.", "খোজে ঠাই সলায়। কেৱল ঘূৰণিয়ে মুখ সলায়।")}


def net_east(route):
    x, y, _ = walk(0, route)
    en, as_ = route_text(0, route)
    return {"q": B(f"{en} How many squares north of the start are you?", f"{as_} আৰম্ভণিৰ পৰা উত্তৰে কিমান ঘৰ আছা?"), "answer": str(y),
            "why": B("Walks north and south cancel, and walks east and west do not count.", "উত্তৰ আৰু দক্ষিণৰ খোজ কাটে, পূব আৰু পশ্চিমৰ খোজ ইয়াত নাগণে।")}


def route_steps(a, b, c):
    s = "rs9.u2.q3"
    route = [a, "R", b, "R", c]
    x, y, _ = walk(0, route)
    fb = lambda f: B(face_en(f).capitalize(), face_as(f))
    return {"q": B(f"Walk {a} north, turn right and walk {b}, then turn right and walk {c}.", f"উত্তৰলৈ {a} ঘৰ গৈ সোঁফালে ঘূৰি {b} ঘৰ যোৱা, তাৰ পিছত সোঁফালে ঘূৰি {c} ঘৰ যোৱা।"), "parts": [
        part(B("The second walk goes?", "দ্বিতীয় খোজ কোন ফালে?"), fb(1), [fb(3), fb(2)], B("Right of north is east.", "উত্তৰৰ সোঁফালে পূব।"), tag="r-m-leftwest", sid=s),
        part(B("The third walk goes?", "তৃতীয় খোজ কোন ফালে?"), fb(2), [fb(0), fb(3)], B("Right of east is south.", "পূবৰ সোঁফালে দক্ষিণ।"), sid=s),
        part(B("How far north of the start do you finish?", "আৰম্ভণিৰ পৰা উত্তৰে কিমান দূৰত শেষ?"), B(str(y), str(y)), [B(str(a + c), str(a + c)), B(str(b), str(b))], B(f"{a} up and {c} back leaves {y}.", f"{a} ওপৰলৈ আৰু {c} ঘূৰি অহাত {y} থাকে।"), sid=s),
    ], "why": B(f"You finish {y} north and {x} east of the start.", f"আৰম্ভণিৰ পৰা উত্তৰে {y} আৰু পূবে {x} ত শেষ।")}


def straight(a, b, c):
    return {"q": B(f"Walk {a} km north, then {b} km east. How far are you from the start in a straight line?", f"উত্তৰলৈ {a} কি.মি. গৈ পূবলৈ {b} কি.মি. যোৱা। পোনে পোনে আৰম্ভণিৰ পৰা দূৰত্ব কিমান?"), "answer": str(c), "suffix": B("km", "কি.মি."),
            "why": B(f"The two walks form a right angle: {a}² + {b}² = {c}².", f"দুয়োটা খোজে সমকোণ বনায়: {a}² + {b}² = {c}²।"), "traps": [{"ans": str(a + b), "tag": "r-m-addlegs", "why": ADDED}]}


def cancel(n, s_, e, c):
    return {"q": B(f"Walk {n} km north, {s_} km south, then {e} km east. What is the straight distance from the start?", f"উত্তৰলৈ {n} কি.মি., দক্ষিণলৈ {s_} কি.মি., তাৰ পিছত পূবলৈ {e} কি.মি. যোৱা। পোনে পোনে আৰম্ভণিৰ পৰা দূৰত্ব কিমান?"), "answer": str(c), "suffix": B("km", "কি.মি."),
            "why": B(f"North and south leave {n - s_}. With {e} east, the straight line is {c}.", f"উত্তৰ-দক্ষিণত {n - s_} থাকে। পূবে {e} ৰ লগত পোন দূৰত্ব {c}।"), "traps": [{"ans": str(n + s_ + e), "tag": "r-m-addlegs", "why": ADDED}]}


def dist_steps(n, s_, e, w, c):
    s = "rs9.u3.q3"
    ns, ew = n - s_, e - w
    return {"q": B(f"Walk {n} north, {e} east, {s_} south, then {w} west.", f"উত্তৰলৈ {n}, পূবলৈ {e}, দক্ষিণলৈ {s_}, তাৰ পিছত পশ্চিমলৈ {w} যোৱা।"), "parts": [
        part(B("Net north?", "নিকা উত্তৰ?"), B(str(ns), str(ns)), [B(str(n + s_), str(n + s_)), B(str(n), str(n))], B("Opposite walks subtract.", "ওলোটা খোজ বিয়োগ হয়।"), sid=s),
        part(B("Net east?", "নিকা পূব?"), B(str(ew), str(ew)), [B(str(e + w), str(e + w)), B(str(e), str(e))], B("Opposite walks subtract.", "ওলোটা খোজ বিয়োগ হয়।"), sid=s),
        part(B("Straight distance?", "পোন দূৰত্ব?"), B(str(c), str(c)), [B(str(ns + ew), str(ns + ew)), B(str(n + s_ + e + w), str(n + s_ + e + w))], B(f"{ns}² + {ew}² = {c}².", f"{ns}² + {ew}² = {c}²।"), tag="r-m-addlegs", sid=s),
    ], "why": B(f"Reduce to one right angle, {ns} and {ew}, then find {c}.", f"এটা সমকোণলৈ আনা, {ns} আৰু {ew}, তাৰ পিছত {c}।")}


# Morning: sun east, shadow west. Evening: sun west, shadow east.
TIME = {"morning": (3, "ৰাতিপুৱা"), "evening": (1, "সন্ধিয়া")}
SIDE = {"front": (0, "সন্মুখত"), "right": (1, "সোঁফালে"), "behind": (2, "পিছফালে"), "left": (3, "বাওঁফালে")}


def shadow_q(time, side):
    shadow, as_time = TIME[time]
    turn, as_side = SIDE[side]
    f = (shadow - turn) % 4
    wrong = ((shadow + 2) - turn) % 4
    return {"q": B(f"It is {time}. Turn the walker so that its shadow falls {'in front' if side == 'front' else 'behind' if side == 'behind' else 'to its ' + side}.", f"{as_time}ৰ সময়। খোজকাৰীক এনেকৈ ঘূৰোৱা যাতে তাৰ ছাঁ {as_side} পৰে।"),
            "widget": {"kind": "walk", "f": 0 if f else 1, "turnOnly": True, "ask": "facing"}, "target": f, "answerText": B(f"Facing {face_en(f)}", f"{face_as(f)}লৈ মুখ"),
            "traps": [{"val": wrong, "tag": "r-m-shadow", "why": SUNSIDE}],
            "why": B(f"In the {time} the shadow points {face_en(shadow)}, so you must face {face_en(f)}.", f"{as_time} ছাঁ {face_as(shadow)}লৈ পৰে, গতিকে {face_as(f)}লৈ মুখ কৰিব লাগে।")}


def shadow_steps(time, side):
    s = "rs9.u4.q3"
    shadow, as_time = TIME[time]
    turn, as_side = SIDE[side]
    f = (shadow - turn) % 4
    fb = lambda x: B(face_en(x).capitalize(), face_as(x))
    return {"q": B(f"In the {time}, a person's shadow falls to their {side}. Which way do they face?", f"{as_time} এজন ব্যক্তিৰ ছাঁ তেওঁৰ {as_side} পৰিছে। তেওঁৰ মুখ কোন ফালে?"), "parts": [
        part(B("Where is the sun?", "সূৰ্য ক'ত?"), fb((shadow + 2) % 4), [fb(shadow), fb((shadow + 1) % 4)], B("Morning sun is east, evening sun is west.", "ৰাতিপুৱা সূৰ্য পূবে, সন্ধিয়া পশ্চিমে।"), sid=s),
        part(B("Which way does the shadow point?", "ছাঁ কোন ফালে পৰে?"), fb(shadow), [fb((shadow + 2) % 4), fb((shadow + 1) % 4)], B("A shadow points away from the sun.", "ছাঁ সূৰ্যৰ ওলোটা ফালে পৰে।"), tag="r-m-shadow", sid=s),
        part(B(f"So they face?", "তেন্তে মুখ কোন ফালে?"), fb(f), [fb((f + 2) % 4), fb((f + 1) % 4)], B(f"Their {side} must be {face_en(shadow)}.", f"তেওঁৰ {as_side} {face_as(shadow)} হ'ব লাগিব।"), sid=s),
    ], "why": B(f"The shadow points {face_en(shadow)}, so they face {face_en(f)}.", f"ছাঁ {face_as(shadow)}লৈ, গতিকে মুখ {face_as(f)}লৈ।")}


def lesson():
    p = "rs9"
    fb = lambda f: B(face_en(f).capitalize(), face_as(f))
    u1 = unit("u1", B("Your left is not west", "তোমাৰ বাওঁফাল পশ্চিম নহয়"), "star", [
        B("North, east, south and west never move.", "উত্তৰ, পূব, দক্ষিণ আৰু পশ্চিম সলনি নহয়।"),
        B("Left and right turn with you.", "বাওঁ আৰু সোঁ তোমাৰ লগত ঘূৰে।"),
        B("A right turn moves clockwise: N, E, S, W.", "সোঁ ঘূৰণি ঘড়ীৰ কাঁটাৰ দিশে: উ, পূ, দ, প।"),
        B("Two right turns make you face the opposite way.", "দুটা সোঁ ঘূৰণিয়ে ওলোটা মুখ কৰে।"),
    ], [
        lab(f"{p}.u1.s1", B("Left and right travel with you", "বাওঁ-সোঁ তোমাৰ লগত যায়"), B("The map's directions stay still. Your left and right do not. Turn the walker and watch the L and R labels.", "মানচিত্ৰৰ দিশ স্থিৰ। তোমাৰ বাওঁ-সোঁ স্থিৰ নহয়। খোজকাৰীক ঘূৰাই বাওঁ-সোঁ চিন চোৱা।"), {"kind": "walk", "f": 0, "turnOnly": True}, [
            task(B("Turn right once.", "এবাৰ সোঁফালে ঘূৰা।"), {"f": 1}, B("You face east. Your left now points north, not west.", "তুমি পূবলৈ মুখ কৰিলা। তোমাৰ বাওঁফাল এতিয়া উত্তৰ, পশ্চিম নহয়।")),
            task(B("Turn until you face south.", "দক্ষিণলৈ মুখ নোহোৱালৈ ঘূৰা।"), {"f": 2}, B("Facing south, your left is east. It is the opposite of the map.", "দক্ষিণলৈ মুখ কৰিলে বাওঁফাল পূব। মানচিত্ৰৰ ওলোটা।")),
        ]),
        diagram(f"{p}.u1.s2", B("Turning is moving round a clock", "ঘূৰণি মানে ঘড়ীৰ দিশ"), [B("Say the order aloud: north, east, south, west. Right steps forward through it, and left steps back.", "ক্ৰমটো মাতি কোৱা: উত্তৰ, পূব, দক্ষিণ, পশ্চিম। সোঁ আগলৈ, বাওঁ পিছলৈ।")], "flow", [B("North", "উত্তৰ"), B("East", "পূব"), B("South", "দক্ষিণ"), B("West", "পশ্চিম")]),
        with_variants({"id": f"{p}.u1.q1", "type": "explore", "skill": TURN}, turn_q, [(2, ["L"]), (3, ["R"]), (1, ["L", "L"]), (2, ["R", "L", "L"])]),
        tf(f"{p}.u1.q2", TURN, B("A person facing south has east on their left.", "দক্ষিণলৈ মুখ কৰা ব্যক্তিৰ বাওঁফালে পূব।"), True, B("Facing south reverses the map's left and right.", "দক্ষিণলৈ মুখ কৰিলে মানচিত্ৰৰ বাওঁ-সোঁ ওলোটা হয়।"), ("r-m-leftwest", WEST)),
        match(f"{p}.u1.q3", TURN, B("Match the facing to what lies on your right", "মুখৰ দিশক সোঁফালৰ দিশৰ লগত মিলোৱা"), [[fb(f), fb(f + 1)] for f in range(4)], B("Right is the next direction clockwise.", "সোঁফাল মানে ঘড়ীৰ দিশে পিছৰটো।")),
        stepwise(f"{p}.u1.q4", TURN, two_turns, [(2, "R", "R"), (1, "L", "L"), (3, "L", "R"), (0, "R", "R")]),
        order(f"{p}.u1.q5", TURN, B("Start at north and put the directions in clockwise order", "উত্তৰৰ পৰা ঘড়ীৰ দিশে দিশবোৰ সজোৱা"), [fb(0), fb(1), fb(2), fb(3)], B("Clockwise from north: north, east, south, west.", "উত্তৰৰ পৰা ঘড়ীৰ দিশে: উত্তৰ, পূব, দক্ষিণ, পশ্চিম।")),
    ])
    u2 = unit("u2", B("Walk the route", "পথ অনুসৰণ"), "star", [
        B("Follow one instruction at a time.", "এবাৰত এটা নিৰ্দেশ মানা।"),
        B("Mark your facing after every turn.", "প্ৰতিটো ঘূৰণিৰ পিছত মুখ চিন কৰা।"),
        B("Only turns change your facing.", "কেৱল ঘূৰণিয়ে মুখ সলায়।"),
        B("Opposite walks cancel each other.", "ওলোটা খোজে ইটোৱে সিটোক কাটে।"),
    ], [
        lab(f"{p}.u2.s1", B("Draw the route, do not imagine", "কল্পনা নকৰি পথ আঁকা"), B("Direction questions are hard in your head and easy on paper. Walk this one: 2 north, right, then 3.", "দিশৰ প্ৰশ্ন মনতে টান, কাগজত সহজ। খোজ কাঢ়া: উত্তৰলৈ 2, সোঁফালে ঘূৰি 3।"), {"kind": "walk", "f": 0}, [
            task(B("Walk 2 squares north.", "উত্তৰলৈ 2 ঘৰ যোৱা।"), {"x": 0, "y": 2}, B("Two steps. You still face north.", "দুটা খোজ। মুখ এতিয়াও উত্তৰলৈ।")),
            task(B("Turn right and walk 3.", "সোঁফালে ঘূৰি 3 ঘৰ যোৱা।"), {"x": 3, "y": 2}, B("The trail shows the whole answer: 3 east and 2 north of the start.", "ৰেখাই গোটেই উত্তৰ দেখুৱায়: আৰম্ভণিৰ পৰা পূবে 3, উত্তৰে 2।")),
        ]),
        diagram(f"{p}.u2.s2", B("A routine for every route", "সকলো পথৰ এটা নিয়ম"), [B("Draw a small north arrow, then follow the words in order. Never skip to the end.", "সৰু উত্তৰ চিন আঁকি শব্দবোৰ ক্ৰমে অনুসৰণ কৰা। শেষলৈ জঁপিয়াই নাযাবা।")], "flow", [B("Mark north", "উত্তৰ চিন"), B("Follow in order", "ক্ৰমে অনুসৰণ"), B("Read the end", "শেষ পঢ়া")]),
        with_variants({"id": f"{p}.u2.q1", "type": "explore", "skill": ROUTE}, route_q, [(0, [2, "R", 3, "L", 1]), (1, [3, "L", 2]), (2, [1, "L", 3, "L", 4]), (3, [2, "R", 2, "R", 1])]),
        with_variants({"id": f"{p}.u2.q2", "type": "explore", "skill": ROUTE}, end_face, [(0, [3, "R", 2, "L", 1, "L", 2]), (2, [2, "L", 3, "L", 1]), (1, [1, "L", 1, "L", 1, "L", 1])]),
        stepwise(f"{p}.u2.q3", ROUTE, route_steps, [(4, 2, 1), (3, 5, 1), (4, 3, 2)]),
        solve(f"{p}.u2.q4", ROUTE, net_east, [([5, "R", 2, "R", 3],), ([4, "L", 3, "L", 1],), ([3, "R", 3, "R", 2],)]),
        tf(f"{p}.u2.q5", ROUTE, B("Walking forward does not change the way you face.", "আগলৈ খোজ কাঢ়িলে মুখ সলনি নহয়।"), True, B("Only a turn changes your facing.", "কেৱল ঘূৰণিয়ে মুখ সলায়।")),
    ])
    u3 = unit("u3", B("The straight way home", "পোনে পোনে ঘৰলৈ"), "star", [
        B("Cancel opposite walks first.", "প্ৰথমে ওলোটা খোজ কাটা।"),
        B("What is left is one north-south and one east-west distance.", "বাকী থাকে এটা উত্তৰ-দক্ষিণ আৰু এটা পূব-পশ্চিম দূৰত্ব।"),
        B("They meet at a right angle, so use a² + b² = c².", "সিহঁতে সমকোণ বনায়, a² + b² = c² ব্যৱহাৰ কৰা।"),
        B("3, 4, 5 and 6, 8, 10 appear again and again.", "3, 4, 5 আৰু 6, 8, 10 সঘনাই আহে।"),
    ], [
        lab(f"{p}.u3.s1", B("Two walks, one short line", "দুটা খোজ, এডাল চুটি ৰেখা"), B("Walk 3 north and 4 east, then look at the gap back to the dot. It is a straight line of 5.", "উত্তৰলৈ 3 আৰু পূবলৈ 4 গৈ বিন্দুলৈ চোৱা। পোন ৰেখাডাল 5।"), {"kind": "walk", "f": 0}, [
            task(B("End 3 north and 4 east of the dot.", "বিন্দুৰ পৰা উত্তৰে 3 আৰু পূবে 4 ত ৰোৱা।"), {"x": 4, "y": 3}, B("You walked 7, but home is only 5 away: 3² + 4² = 5².", "তুমি 7 খোজ গ'লা, কিন্তু ঘৰ 5 দূৰত: 3² + 4² = 5²।")),
        ]),
        diagram(f"{p}.u3.s2", B("Shrink the route first", "প্ৰথমে পথ চুটি কৰা"), [B("North cancels south, and east cancels west. After that, every route is one right-angled triangle.", "উত্তৰে দক্ষিণক কাটে, পূবে পশ্চিমক কাটে। তাৰ পিছত প্ৰতিটো পথ এটা সমকোণী ত্ৰিভুজ।")], "flow", [B("Cancel opposites", "ওলোটা কাটা"), B("Two sides left", "দুটা বাহু"), B("a² + b² = c²", "a² + b² = c²")]),
        solve(f"{p}.u3.q1", DIST, straight, [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 6, 10)]),
        solve(f"{p}.u3.q2", DIST, cancel, [(7, 3, 3, 5), (9, 3, 8, 10), (10, 2, 6, 10)]),
        stepwise(f"{p}.u3.q3", DIST, dist_steps, [(5, 2, 6, 2, 5), (8, 2, 10, 2, 10), (7, 2, 15, 3, 13)]),
        tf(f"{p}.u3.q4", DIST, B("The straight distance is the sum of all the walks.", "পোন দূৰত্ব সকলো খোজৰ যোগফল।"), False, B("It is the short line between start and end.", "ই আৰম্ভণি আৰু শেষৰ মাজৰ চুটি ৰেখা।"), ("r-m-addlegs", ADDED)),
        match(f"{p}.u3.q5", DIST, B("Match the two sides to the straight line", "দুটা বাহুক পোন ৰেখাৰ লগত মিলোৱা"), [[B("3 and 4", "3 আৰু 4"), B("5", "5")], [B("6 and 8", "6 আৰু 8"), B("10", "10")], [B("5 and 12", "5 আৰু 12"), B("13", "13")]], B("Each pair fits a² + b² = c².", "প্ৰতিটো যোৰ a² + b² = c² ত মিলে।")),
    ])
    u4 = unit("u4", B("Sun and shadow", "সূৰ্য আৰু ছাঁ"), "star", [
        B("The sun is in the east in the morning.", "ৰাতিপুৱা সূৰ্য পূবে থাকে।"),
        B("It is in the west in the evening.", "সন্ধিয়া সূৰ্য পশ্চিমে থাকে।"),
        B("A shadow points away from the sun.", "ছাঁ সূৰ্যৰ ওলোটা ফালে পৰে।"),
        B("Then use left and right as usual.", "তাৰ পিছত বাওঁ-সোঁ সদায়ৰ দৰে।"),
    ], [
        lab(f"{p}.u4.s1", B("The morning shadow points west", "ৰাতিপুৱাৰ ছাঁ পশ্চিমলৈ"), B("At sunrise the sun is in the east, so your shadow stretches west. Face your own shadow.", "সূৰ্যোদয়ত সূৰ্য পূবে, গতিকে ছাঁ পশ্চিমলৈ। নিজৰ ছাঁৰ ফালে মুখ কৰা।"), {"kind": "walk", "f": 0, "turnOnly": True}, [
            task(B("Turn to face the morning shadow.", "ৰাতিপুৱাৰ ছাঁৰ ফালে মুখ কৰা।"), {"f": 3}, B("You face west, and the sun is behind you.", "তুমি পশ্চিমলৈ মুখ কৰিলা, সূৰ্য তোমাৰ পিছফালে।")),
            task(B("Now turn to face the evening shadow.", "এতিয়া সন্ধিয়াৰ ছাঁৰ ফালে মুখ কৰা।"), {"f": 1}, B("In the evening the sun is west, so the shadow points east.", "সন্ধিয়া সূৰ্য পশ্চিমে, গতিকে ছাঁ পূবলৈ।")),
        ]),
        diagram(f"{p}.u4.s2", B("Three steps for any shadow", "যিকোনো ছাঁৰ তিনি খোজ"), [B("Ask where the sun is, flip it for the shadow, then place the person.", "সূৰ্য ক'ত সোধা, ছাঁৰ বাবে ওলোটোৱা, তাৰ পিছত ব্যক্তিজনক ৰখোৱা।")], "flow", [B("Find the sun", "সূৰ্য উলিওৱা"), B("Flip for the shadow", "ছাঁৰ বাবে ওলোটোৱা"), B("Place the person", "ব্যক্তি ৰখোৱা")]),
        with_variants({"id": f"{p}.u4.q1", "type": "explore", "skill": SHADOW}, shadow_q, [("morning", "left"), ("evening", "right"), ("morning", "behind"), ("evening", "front")]),
        tf(f"{p}.u4.q2", SHADOW, B("In the evening, a shadow points east.", "সন্ধিয়া ছাঁ পূবলৈ পৰে।"), True, B("The sun is west, so the shadow is east.", "সূৰ্য পশ্চিমে, গতিকে ছাঁ পূবে।"), ("r-m-shadow", SUNSIDE)),
        stepwise(f"{p}.u4.q3", SHADOW, shadow_steps, [("morning", "right"), ("evening", "left"), ("morning", "left")]),
        match(f"{p}.u4.q4", SHADOW, B("Match the time to the fact", "সময়ক তথ্যৰ লগত মিলোৱা"), [[B("Morning sun", "ৰাতিপুৱাৰ সূৰ্য"), B("East", "পূব")], [B("Morning shadow", "ৰাতিপুৱাৰ ছাঁ"), B("West", "পশ্চিম")], [B("Facing north, morning shadow falls", "উত্তৰমুৱা হ'লে ৰাতিপুৱাৰ ছাঁ"), B("To the left", "বাওঁফালে")], [B("Facing north, evening shadow falls", "উত্তৰমুৱা হ'লে সন্ধিয়াৰ ছাঁ"), B("To the right", "সোঁফালে")]], B("Fix the shadow first, then read left and right.", "প্ৰথমে ছাঁ ঠিক কৰা, তাৰ পিছত বাওঁ-সোঁ পঢ়া।")),
        with_variants({"id": f"{p}.u4.q5", "type": "explore", "skill": SHADOW}, shadow_q, [("evening", "left"), ("morning", "front"), ("evening", "behind")]),
    ])
    test = {"id": "test", "title": B("Direction test", "দিশৰ পৰীক্ষা"), "steps": [
        mcq(f"{p}.t.q1", TURN, lambda f, m: {"q": B(f"You face {face_en(f)} and turn {'left' if m == 'L' else 'right'}. Which way do you face?", f"তুমি {face_as(f)}লৈ মুখ কৰি {'বাওঁফালে' if m == 'L' else 'সোঁফালে'} ঘূৰিলা। এতিয়া মুখ কোন ফালে?"), "right": face_en(walk(f, [m])[2]).capitalize(), "wrong": [(face_en(walk(f, ["L" if m == "R" else "R"])[2]).capitalize(), "r-m-leftwest", WEST)], "fill": [face_en(f).capitalize(), face_en(f + 2).capitalize(), "North", "East"], "why": B(f"You end facing {face_en(walk(f, [m])[2])}.", f"শেষত {face_as(walk(f, [m])[2])}লৈ মুখ।")}, [(2, "L"), (3, "R"), (2, "R")]),
        mcq(f"{p}.t.q2", ROUTE, lambda a, b: {"q": B(f"Walk {a} north, turn right, walk {b}, turn right, walk {a}. Where do you end?", f"উত্তৰলৈ {a} গৈ সোঁফালে ঘূৰি {b} গৈ সোঁফালে ঘূৰি {a} যোৱা। ক'ত শেষ হ'ল?"), "right": f"{b} east", "wrong": [(f"{b} west", "r-m-leftwest", WEST)], "fill": [f"{a} north", f"{a + b} east", "At the start"], "why": B(f"North and south cancel, leaving {b} east.", f"উত্তৰ-দক্ষিণ কাটে, পূবে {b} থাকে।")}, [(4, 2), (3, 5), (5, 3)]),
        solve(f"{p}.t.q3", DIST, straight, [(4, 3, 5), (8, 6, 10), (12, 5, 13)]),
        mcq(f"{p}.t.q4", SHADOW, lambda t, m: {"q": B(f"It is {t}. You face north. Where does your shadow fall?", f"{TIME[t][1]}ৰ সময়। তুমি উত্তৰলৈ মুখ কৰিছা। ছাঁ কোন ফালে পৰিব?"), "right": m, "wrong": [("Right" if m == "Left" else "Left", "r-m-shadow", SUNSIDE)], "fill": ["In front", "Behind", "Nowhere"], "why": B(f"The {t} shadow points {'west' if t == 'morning' else 'east'}, which is your {m.lower()} when you face north.", f"{TIME[t][1]} ছাঁ {'পশ্চিমলৈ' if t == 'morning' else 'পূবলৈ'} পৰে; উত্তৰলৈ মুখ কৰিলে সেয়া {'বাওঁফাল' if m == 'Left' else 'সোঁফাল'}।")}, [("morning", "Left"), ("evening", "Right")]),
        tf(f"{p}.t.q5", TURN, B("Three right turns face the same way as one left turn.", "তিনিটা সোঁ ঘূৰণি আৰু এটা বাওঁ ঘূৰণিত মুখ একে ফালে হয়।"), True, B("Three quarter turns one way equal one quarter turn the other way.", "এফালে তিনি চতুৰ্থাংশ আনফালে এক চতুৰ্থাংশৰ সমান।")),
        solve(f"{p}.t.q6", DIST, cancel, [(8, 2, 8, 10), (6, 3, 4, 5)]),
    ]}
    return {"id": "rs-09-direction", "no": 9, "slug": "direction", "title": B("Direction sense", "দিশ জ্ঞান"), "reign": B("Turns, routes, distance, shadows", "ঘূৰণি, পথ, দূৰত্ব, ছাঁ"), "units": [u1, u2, u3, u4], "test": test}
