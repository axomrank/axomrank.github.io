"""Lessons 7 and 8: Symbols and operators, and Number puzzles. Answers are computed."""
from math_kit import B, match, mcq, order, part, solve, stepwise, tf, unit
from math_lessons_c import diagram
from reason_kit import same

SWAP = "r-opswap"; INTER = "r-opinter"; BAL = "r-opbal"; MACH = "r-opmach"
SCAN = "r-dscan"; PAIRS = "r-dpairs"; SORT = "r-dsort"; BUILD = "r-dbuild"; MIDDLE = "r-dmiddle"; CHECK = "r-dcheck"
SKILLS = {SWAP: ("operators", B("Replace symbols", "চিহ্ন সলনি"), []), INTER: ("operators", B("Interchange signs", "চিহ্ন অদল-বদল"), [SWAP]), BAL: ("operators", B("Balance an equation", "সমীকৰণ মিলোৱা"), [SWAP]), MACH: ("operators", B("Follow the steps", "খোজ অনুসৰণ"), []),
          SCAN: ("number-puzzles", B("Scan with a condition", "চৰ্তৰে চকু ফুৰোৱা"), []), PAIRS: ("number-puzzles", B("Count neighbour pairs", "কাষৰ যোৰ গণনা"), [SCAN]), SORT: ("number-puzzles", B("Sort digits and numbers", "অংক আৰু সংখ্যা সজোৱা"), []), BUILD: ("number-puzzles", B("Build numbers from digits", "অংকৰে সংখ্যা বনোৱা"), []), MIDDLE: ("number-puzzles", B("Positions in a line", "শাৰীত স্থান"), []), CHECK: ("number-puzzles", B("Test the options", "বিকল্প পৰীক্ষা"), [])}
TAGS = {"r-m-leftright": (SWAP, B("Calculating left to right", "বাওঁৰ পৰা সোঁলৈ গণনা")), "r-m-halfscan": (SCAN, B("Missing part of a condition", "চৰ্তৰ অংশ এৰা")), "r-m-placeval": (BUILD, B("Forgetting that 0 cannot lead", "আৰম্ভণিত 0 নহয় পাহৰা"))}
LR = B("Replace the symbols, then follow × and ÷ before + and −.", "চিহ্ন সলনি কৰি যোগ-বিয়োগৰ আগতে পূৰণ-হৰণ কৰা।")
HALF = B("Check both parts of the condition for every digit.", "প্ৰতিটো অংকত চৰ্তৰ দুয়োটা অংশ চোৱা।")
ZERO = B("A number cannot begin with 0.", "সংখ্যা 0 ৰে আৰম্ভ নহয়।")
OPS = {"+": lambda a, b: a + b, "−": lambda a, b: a - b, "×": lambda a, b: a * b, "÷": lambda a, b: a // b}


def ev(nums, ops):
    """Standard order: × ÷ first, then + −."""
    ns, os_ = list(nums), list(ops)
    i = 0
    while i < len(os_):
        if os_[i] in "×÷":
            ns[i:i + 2] = [OPS[os_[i]](ns[i], ns[i + 1])]
            os_.pop(i)
        else:
            i += 1
    v = ns[0]
    for o, n in zip(os_, ns[1:]):
        v = OPS[o](v, n)
    return v


def ltr(nums, ops):
    v = nums[0]
    for o, n in zip(ops, nums[1:]):
        v = OPS[o](v, n)
    return v


def line(nums, syms):
    return " ".join(str(x) for pair in zip(nums, syms + [""]) for x in pair).strip()


def replace_q(nums, syms, key):
    real = [key[s] for s in syms]
    legend = ", ".join(f"{k} means {v}" for k, v in key.items())
    legend_as = ", ".join(f"{k} মানে {v}" for k, v in key.items())
    v = ev(nums, real)
    return {"q": B(f"{legend}. Find {line(nums, syms)}.", f"{legend_as}। {line(nums, syms)} উলিওৱা।"), "answer": str(v), "why": B(f"That is {line(nums, real)} = {v}.", f"সেয়া {line(nums, real)} = {v}।"), "traps": [{"ans": str(ltr(nums, real)), "tag": "r-m-leftright", "why": LR}] if ltr(nums, real) != v else []}


def inter_q(nums, ops, a, b):
    swap = {a: b, b: a}
    real = [swap.get(o, o) for o in ops]
    v = ev(nums, real)
    return {"q": B(f"Interchange {a} and {b}. What is {line(nums, ops)}?", f"{a} আৰু {b} অদল-বদল কৰা। {line(nums, ops)} কিমান?"), "answer": str(v), "why": B(f"It becomes {line(nums, real)} = {v}.", f"ই হয় {line(nums, real)} = {v}।"), "traps": [{"ans": str(ev(nums, ops)), "tag": "r-m-leftright", "why": B("You kept the signs unchanged. Swap them first.", "তুমি চিহ্ন সলনি কৰা নাই। প্ৰথমে অদল-বদল কৰা।")}]}


def bal_q(a, b, c, right):
    wrongs = [o for o in "+−×" if o != right]
    res = OPS[right](a, b) + c
    return {"q": B(f"Which sign makes this true: {a} ? {b} + {c} = {res}?", f"কোন চিহ্নই ইয়াক শুদ্ধ কৰে: {a} ? {b} + {c} = {res}?"), "parts": [
        part(B("Take away the + part. What must the left give?", "+ অংশ আঁতৰোৱা। বাওঁফালে কিমান হ'ব লাগিব?"), same(res - c), [same(res), same(res + c)], B(f"{res} − {c}.", f"{res} − {c}।"), sid="rs7.u3.q1"),
        part(B("Which sign?", "কোন চিহ্ন?"), same(right), [same(wrongs[0]), same(wrongs[1])], B(f"{a} {right} {b} = {res - c}.", f"{a} {right} {b} = {res - c}।"), sid="rs7.u3.q1"),
    ], "why": B(f"{a} {right} {b} + {c} = {res}.", f"{a} {right} {b} + {c} = {res}।")}


def mach_q(n, a, b):
    v = (n + a) * b
    return {"q": B(f"Start with {n}. Add {a}. Multiply by {b}. What do you get?", f"{n} ৰ পৰা আৰম্ভ কৰা। {a} যোগ কৰা। {b} ৰে পূৰণ কৰা। কিমান হ'ল?"), "answer": str(v), "why": B(f"({n} + {a}) × {b} = {v}.", f"({n} + {a}) × {b} = {v}।"), "traps": [{"ans": str(n + a * b), "tag": "r-m-leftright", "why": B("Here steps run in the stated order, one at a time.", "ইয়াত খোজবোৰ কোৱা ক্ৰমতে এটা এটাকৈ।")}]}


def back_q(result, a, b):
    return {"q": B(f"A number had {a} added, then was doubled {b} time(s), giving {result * 2 ** b}. What was it, with {a} taken back off?", f"এটা সংখ্যাত {a} যোগ কৰি {b} বাৰ দুগুণ কৰাত {result * 2 ** b} হ'ল। {a} আঁতৰাই মূল সংখ্যাটো কি?"), "answer": str(result - a), "why": B(f"Undo in reverse: halve {b} time(s), then subtract {a}.", f"ওলোটাকৈ: {b} বাৰ আধা কৰি {a} বিয়োগ।")}


def lesson_operators():
    p = "rs7"
    u1 = unit("u1", B("Swap the symbols first", "প্ৰথমে চিহ্ন সলনি"), "star", [B("Write the real signs before calculating.", "গণনাৰ আগতে আচল চিহ্ন লিখা।"), B("Then use normal order.", "তাৰ পিছত সাধাৰণ ক্ৰম।"), B("× and ÷ come before + and −.", "+ আৰু − ৰ আগত × আৰু ÷।"), B("Only then work left to right.", "তাৰ পিছতহে বাওঁৰ পৰা সোঁলৈ।")], [
        diagram(f"{p}.u1.s1", B("Rewrite, then solve", "আকৌ লিখি সমাধান"), [B("The trick is only disguise. Rewrite the line in real signs and it is plain arithmetic.", "কৌশলটো কেৱল ছদ্মবেশ। আচল চিহ্নত লিখিলে সাধাৰণ অংক।")], "flow", [same("8 @ 2 # 3"), B("@ is +, # is ×", "@ +, # ×"), same("8 + 2 × 3")]),
        diagram(f"{p}.u1.s2", B("Order still rules", "ক্ৰম এতিয়াও থাকে"), [B("After rewriting, 8 + 2 × 3 is 14, not 30.", "লিখাৰ পিছত 8 + 2 × 3 = 14, 30 নহয়।")], "flow", [B("× and ÷", "× আৰু ÷"), B("+ and −", "+ আৰু −"), B("Left to right", "বাওঁৰ পৰা সোঁলৈ")]),
        solve(f"{p}.u1.q1", SWAP, replace_q, [([8, 2, 3], ["@", "#"], {"@": "+", "#": "×"}), ([20, 5, 2], ["$", "%"], {"$": "÷", "%": "+"}), ([9, 3, 4], ["#", "@"], {"#": "−", "@": "×"})]),
        solve(f"{p}.u1.q2", SWAP, replace_q, [([12, 4, 5], ["&", "%"], {"&": "÷", "%": "×"}), ([6, 7, 2], ["%", "&"], {"%": "+", "&": "×"}), ([30, 6, 3], ["&", "@"], {"&": "÷", "@": "−"})]),
        tf(f"{p}.u1.q3", SWAP, B("6 + 2 × 5 equals 40.", "6 + 2 × 5 = 40।"), False, B("× first gives 16.", "× আগতে কৰিলে 16।"), ("r-m-leftright", LR)),
        match(f"{p}.u1.q4", SWAP, B("Match the line to its value", "শাৰীক মানৰ লগত মিলোৱা"), [[same("2 + 3 × 4"), same("14")], [same("20 ÷ 5 + 1"), same("5")], [same("10 − 2 × 3"), same("4")]], B("× and ÷ first.", "× আৰু ÷ আগতে।")),
        order(f"{p}.u1.q5", SWAP, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the key", "চাবি পঢ়া"), B("Rewrite the line", "শাৰী লিখা"), B("Do × and ÷", "× আৰু ÷"), B("Do + and −", "+ আৰু −")], B("Rewrite before calculating.", "গণনাৰ আগতে লিখা।")),
    ])
    u2 = unit("u2", B("Signs that trade places", "ঠাই সলোৱা চিহ্ন"), "star", [B("Interchange means both ways.", "অদল-বদল মানে দুয়োফালে।"), B("Write the new line first.", "প্ৰথমে নতুন শাৰী লিখা।"), B("Leave other signs alone.", "আন চিহ্ন সলনি নকৰিবা।"), B("Then use normal order.", "তাৰ পিছত সাধাৰণ ক্ৰম।")], [
        diagram(f"{p}.u2.s1", B("Both signs change", "দুয়োটা চিহ্ন সলনি"), [B("If + and × trade places, every + becomes × and every × becomes +.", "+ আৰু × অদল-বদল হ'লে সকলো + × হয়, সকলো × + হয়।")], "flow", [same("4 + 3 × 2"), B("Trade + and ×", "+ আৰু × অদল-বদল"), same("4 × 3 + 2")]),
        diagram(f"{p}.u2.s2", B("Other signs stay", "আন চিহ্ন থাকে"), [B("Only the named pair changes. Copy everything else as it is.", "কেৱল নাম লোৱা যোৰ সলনি। বাকীখিনি একেদৰে লিখা।")], "flow", [B("Find the pair", "যোৰ উলিওৱা"), B("Swap them", "সলনি"), B("Keep the rest", "বাকী ৰাখা")]),
        solve(f"{p}.u2.q1", INTER, inter_q, [([4, 3, 2], ["+", "×"], "+", "×"), ([18, 3, 2], ["÷", "+"], "÷", "×"), ([10, 2, 3], ["−", "×"], "−", "+")]),
        tf(f"{p}.u2.q2", INTER, B("If + and − interchange, 5 + 3 becomes 5 − 3.", "+ আৰু − অদল-বদল হ'লে 5 + 3 হয় 5 − 3।"), True, B("Each + becomes −.", "প্ৰতিটো + − হয়।")),
        match(f"{p}.u2.q3", INTER, B("Interchange + and ×, then match", "+ আৰু × অদল-বদল কৰি মিলোৱা"), [[same("2 + 3"), same("6")], [same("2 × 3"), same("5")], [same("1 + 9"), same("9")]], B("Change the sign, then calculate.", "চিহ্ন সলাই গণা।")),
        stepwise(f"{p}.u2.q4", INTER, lambda n, a, b, c: {"q": B(f"Interchange {a} and {b}: {line(n, c)}.", f"{a} আৰু {b} অদল-বদল: {line(n, c)}।"), "parts": [
            part(B("The new line?", "নতুন শাৰী?"), same(line(n, [({a: b, b: a}).get(o, o) for o in c])), [same(line(n, c)), same(line(n[::-1], c))], B("Swap only the named signs.", "কেৱল নাম লোৱা চিহ্ন সলনি।"), sid=f"{p}.u2.q4"),
            part(B("Its value?", "ইয়াৰ মান?"), same(ev(n, [({a: b, b: a}).get(o, o) for o in c])), [same(ev(n, [({a: b, b: a}).get(o, o) for o in c]) + 2), same(ev(n, [({a: b, b: a}).get(o, o) for o in c]) - 1)], LR, tag="r-m-leftright", sid=f"{p}.u2.q4"),
        ], "why": B("Rewrite first, then calculate.", "লিখি গণা।")}, [([6, 2, 3], "+", "×", ["+", "×"]), ([7, 4, 2], "−", "+", ["−", "+"]), ([9, 3, 2], "×", "÷", ["÷", "×"])]),
        order(f"{p}.u2.q5", INTER, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the pair", "যোৰ পঢ়া"), B("Rewrite the line", "শাৰী লিখা"), B("Use normal order", "সাধাৰণ ক্ৰম"), B("Check", "পৰীক্ষা")], B("Rewrite first.", "প্ৰথমে লিখা।")),
    ])
    u3 = unit("u3", B("Make it balance", "সমান কৰা"), "star", [B("Work from the known side.", "জনা ফালৰ পৰা আৰম্ভ।"), B("Try the likely sign first.", "সম্ভাব্য চিহ্ন আগতে।"), B("A large result suggests ×.", "ডাঙৰ ফল মানে ×।"), B("Test the full line.", "গোটেই শাৰী চোৱা।")], [
        diagram(f"{p}.u3.s1", B("Options are your friend", "বিকল্পই সহায়ক"), [B("Trying each sign is quicker than reasoning it out.", "প্ৰতিটো চিহ্ন চোৱাই ভাবি থকাতকৈ খৰ।")], "flow", [B("Try a sign", "চিহ্ন চোৱা"), B("Compute", "গণা"), B("Does it match?", "মিলিলনে?")]),
        diagram(f"{p}.u3.s2", B("Size gives a clue", "আকাৰে ইংগিত দিয়ে"), [B("If the result is much larger than the numbers, try × first.", "ফল সংখ্যাতকৈ বহুত ডাঙৰ হ'লে আগতে × চোৱা।")], "flow", [same("6 ? 5 = 30"), B("Large result", "ডাঙৰ ফল"), same("×")]),
        stepwise(f"{p}.u3.q1", BAL, bal_q, [(6, 5, 2, "×"), (9, 4, 3, "+"), (8, 3, 7, "−")]),
        solve(f"{p}.u3.q2", BAL, lambda a, b, c: {"q": B(f"Find the missing number: {a} × ? + {b} = {a * c + b}.", f"নিৰুদ্দিষ্ট সংখ্যা: {a} × ? + {b} = {a * c + b}।"), "answer": str(c), "why": B(f"{a * c + b} − {b} = {a * c}, and {a * c} ÷ {a} = {c}.", f"{a * c + b} − {b} = {a * c}, {a * c} ÷ {a} = {c}।")}, [(3, 2, 5), (4, 5, 6), (7, 1, 3)]),
        tf(f"{p}.u3.q3", BAL, B("7 × 3 + 2 = 23.", "7 × 3 + 2 = 23।"), True, B("21 + 2 = 23.", "21 + 2 = 23।")),
        match(f"{p}.u3.q4", BAL, B("Match the missing sign", "নিৰুদ্দিষ্ট চিহ্ন মিলোৱা"), [[same("9 ? 3 = 27"), same("×")], [same("9 ? 3 = 12"), same("+")], [same("9 ? 3 = 3"), same("÷")]], B("Test each sign.", "প্ৰতিটো চিহ্ন চোৱা।")),
        order(f"{p}.u3.q5", BAL, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the target", "লক্ষ্য পঢ়া"), B("Guess by size", "আকাৰে অনুমান"), B("Compute", "গণা"), B("Confirm", "নিশ্চিত")], B("Size narrows the choice.", "আকাৰে বাছনি কমায়।")),
    ])
    u4 = unit("u4", B("Rules in steps", "খোজে খোজে নিয়ম"), "star", [B("Follow stated steps in order.", "কোৱা খোজ ক্ৰমে মানা।"), B("Here brackets do not apply.", "ইয়াত সাধাৰণ ক্ৰম নাখাটে।"), B("To go backward, undo each step.", "ওলোটাকৈ, প্ৰতিটো খোজ উভতোৱা।"), B("Undo from last to first.", "শেষৰ পৰা প্ৰথমলৈ।")], [
        diagram(f"{p}.u4.s1", B("Stated steps come first", "কোৱা ক্ৰমেই আগ"), [B("Add 2, then multiply by 3 means (n + 2) × 3. The wording sets the order.", "2 যোগ, তাৰ পিছত 3 ৰে পূৰণ মানে (n + 2) × 3। ভাষাই ক্ৰম ঠিক কৰে।")], "flow", [same("n"), same("n + 2"), same("(n + 2) × 3")]),
        diagram(f"{p}.u4.s2", B("Reverse to find the start", "ওলোটাকৈ আৰম্ভণি"), [B("To go back, undo the last step first: × becomes ÷, and + becomes −.", "উভতিবলৈ শেষ খোজ আগতে উভতোৱা: × হয় ÷, + হয় −।")], "flow", [B("Final value", "শেষৰ মান"), B("Undo last", "শেষটো উভতোৱা"), B("Undo first", "প্ৰথমটো উভতোৱা")]),
        solve(f"{p}.u4.q1", MACH, mach_q, [(3, 4, 2), (5, 1, 3), (2, 6, 4)]),
        solve(f"{p}.u4.q2", MACH, lambda r, a, b: {"q": B(f"A number has {a} added, then is multiplied by {b}, giving {(r + a) * b}. Find the number.", f"এটা সংখ্যাত {a} যোগ কৰি {b} ৰে পূৰণ কৰাত {(r + a) * b} হ'ল। সংখ্যাটো উলিওৱা।"), "answer": str(r), "why": B(f"{(r + a) * b} ÷ {b} = {r + a}, then − {a} = {r}.", f"{(r + a) * b} ÷ {b} = {r + a}, তাৰ পিছত − {a} = {r}।")}, [(4, 3, 2), (6, 2, 5), (9, 1, 3)]),
        tf(f"{p}.u4.q3", MACH, B("To undo × 3, you divide by 3.", "× 3 উভতাবলৈ 3 ৰে হৰণ কৰা।"), True, B("Division undoes multiplication.", "হৰণে পূৰণ উভতায়।")),
        match(f"{p}.u4.q4", MACH, B("Match the step to its undo", "খোজক উভতোৱাৰ লগত মিলোৱা"), [[same("+ 4"), same("− 4")], [same("× 2"), same("÷ 2")], [same("− 5"), same("+ 5")]], B("Each has an opposite.", "প্ৰতিটোৰ বিপৰীত আছে।")),
        order(f"{p}.u4.q5", MACH, B("Start 2, add 3, double, take 1: order the values", "2 ৰ পৰা, 3 যোগ, দুগুণ, 1 বিয়োগ: মান ক্ৰমে"), [same(2), same(5), same(10), same(9)], B("Follow each step.", "প্ৰতিটো খোজ মানা।")),
    ])
    test = {"id": "test", "title": B("Operators test", "চিহ্নৰ পৰীক্ষা"), "steps": [
        solve(f"{p}.t.q1", SWAP, replace_q, [([7, 3, 2], ["@", "#"], {"@": "+", "#": "×"}), ([24, 6, 1], ["$", "%"], {"$": "÷", "%": "+"})]),
        solve(f"{p}.t.q2", SWAP, replace_q, [([5, 4, 3], ["#", "@"], {"#": "×", "@": "−"}), ([9, 2, 4], ["%", "$"], {"%": "+", "$": "×"})]),
        solve(f"{p}.t.q3", INTER, inter_q, [([3, 5, 2], ["+", "×"], "+", "×"), ([12, 4, 1], ["÷", "+"], "÷", "×")]),
        solve(f"{p}.t.q4", MACH, mach_q, [(7, 2, 3), (4, 5, 2)]),
        tf(f"{p}.t.q5", BAL, B("8 − 3 × 2 = 2.", "8 − 3 × 2 = 2।"), True, B("× first: 8 − 6 = 2.", "× আগতে: 8 − 6 = 2।")),
        tf(f"{p}.t.q6", SWAP, B("Rewrite symbols before calculating.", "গণনাৰ আগতে চিহ্ন লিখা।"), True, B("It avoids mix-ups.", "ই ভুল ৰোধ কৰে।")),
    ]}
    return {"id": "rs-07-operators", "no": 7, "slug": "operators", "title": B("Symbols and operators", "চিহ্ন আৰু প্ৰক্ৰিয়া"), "reign": B("Replacing, interchanging, balancing", "সলনি, অদল-বদল, সমতা"), "units": [u1, u2, u3, u4], "test": test}


# ---------------------------------------------------------------- number puzzles
def scan_before(s, d, before):
    n = sum(1 for i in range(1, len(s)) if s[i] == d and s[i - 1] == before)
    return {"q": B(f"In {s}, how many {d}s come straight after a {before}?", f"{s} ত {before} ৰ ঠিক পিছত {d} কিমানবাৰ আছে?"), "answer": str(n), "why": B(f"Look at each {d} and the digit before it: {n}.", f"প্ৰতিটো {d} আৰু তাৰ আগৰ অংক চোৱা: {n}।"), "traps": [{"ans": str(s.count(d)), "tag": "r-m-halfscan", "why": HALF}] if s.count(d) != n else []}


def scan_both(s, d, before, after):
    n = sum(1 for i in range(1, len(s) - 1) if s[i] == d and s[i - 1] == before and s[i + 1] == after)
    one = sum(1 for i in range(1, len(s)) if s[i] == d and s[i - 1] == before)
    return {"q": B(f"In {s}, how many {d}s have {before} just before and {after} just after?", f"{s} ত কিমান {d} ৰ ঠিক আগত {before} আৰু ঠিক পিছত {after}?"), "answer": str(n), "why": B(f"Both conditions must hold: {n}.", f"দুয়োটা চৰ্ত লাগিব: {n}।"), "traps": [{"ans": str(one), "tag": "r-m-halfscan", "why": HALF}] if one != n else []}


def even_pairs(s):
    n = sum(1 for a, b in zip(s, s[1:]) if int(a) % 2 == 0 and int(b) % 2 == 0)
    return {"q": B(f"In {s}, how many neighbouring pairs are both even?", f"{s} ত দুয়োটা যুগ্ম এনে কিমান কাষৰ যোৰ?"), "answer": str(n), "why": B(f"Slide along the digits two at a time: {n}.", f"দুটাকৈ অংক আগবাঢ়ি চোৱা: {n}।")}


def sum_pairs(s, t):
    n = sum(1 for a, b in zip(s, s[1:]) if int(a) + int(b) == t)
    return {"q": B(f"In {s}, how many neighbouring pairs add to {t}?", f"{s} ত যোগফল {t} হোৱা কিমান কাষৰ যোৰ?"), "answer": str(n), "why": B(f"Test each pair: {n}.", f"প্ৰতিটো যোৰ চোৱা: {n}।")}


def sorted_mid(nums):
    s = sorted(nums)
    return {"q": B(f"Arrange {', '.join(map(str, nums))} in ascending order. Which number is in the middle?", f"{', '.join(map(str, nums))} উৰ্ধ্বক্ৰমে সজোৱা। মাজত কোন সংখ্যা?"), "answer": str(s[len(s) // 2]), "why": B(f"In order: {', '.join(map(str, s))}.", f"ক্ৰমে: {', '.join(map(str, s))}।")}


def digit_sort(n):
    asc = "".join(sorted(str(n)))
    return {"q": B(f"Arrange the digits of {n} in ascending order. Which digit is 2nd from the left?", f"{n} ৰ অংকবোৰ উৰ্ধ্বক্ৰমে সজোৱা। বাওঁফালৰ পৰা দ্বিতীয় অংক কি?"), "answer": asc[1], "why": B(f"In order: {asc}.", f"ক্ৰমে: {asc}।")}


def largest(ds):
    v = "".join(sorted(ds, reverse=True))
    return {"q": B(f"What is the largest number made from {', '.join(ds)}, using each once?", f"{', '.join(ds)} এবাৰকৈ লৈ আটাইতকৈ ডাঙৰ সংখ্যা কি?"), "answer": v, "why": B("Put the largest digit first.", "ডাঙৰ অংক আগত ৰাখা।")}


def smallest(ds):
    s = sorted(ds)
    if s[0] == "0":
        s[0], s[1] = s[1], s[0]
    v = "".join(s)
    return {"q": B(f"What is the smallest number made from {', '.join(ds)}, using each once?", f"{', '.join(ds)} এবাৰকৈ লৈ আটাইতকৈ সৰু সংখ্যা কি?"), "answer": v, "why": B("Use the smallest allowed leading digit, then ascending order.", "আগত আটাইতকৈ সৰু অনুমোদিত অংক, তাৰ পিছত উৰ্ধ্বক্ৰম।"), "traps": [{"ans": "".join(sorted(ds)).lstrip("0") or "0", "tag": "r-m-placeval", "why": ZERO}] if "0" in ds else []}


def diff_big(ds):
    b = int("".join(sorted(ds, reverse=True)))
    a = "".join(sorted(ds))
    if a[0] == "0":
        z = list(a); z[0], z[1] = z[1], z[0]; a = "".join(z)
    return {"q": B(f"Find the difference between the largest and smallest numbers from {', '.join(ds)}.", f"{', '.join(ds)} ৰ পৰা ডাঙৰ আৰু সৰু সংখ্যাৰ পাৰ্থক্য উলিওৱা।"), "answer": str(b - int(a)), "why": B(f"{b} − {a} = {b - int(a)}.", f"{b} − {a} = {b - int(a)}।")}


def pos_from(n, a):
    return {"q": B(f"A person is {a}th from the left in a line of {n}. What is their place from the right?", f"{n} জনৰ শাৰীত এজন বাওঁফালৰ পৰা {a} নম্বৰ। সোঁফালৰ পৰা স্থান কিমান?"), "answer": str(n - a + 1), "why": B(f"{n} − {a} + 1 = {n - a + 1}.", f"{n} − {a} + 1 = {n - a + 1}।")}


def count_between(a, b, k):
    n = sum(1 for x in range(a, b + 1) if x % k == 0)
    return {"q": B(f"How many multiples of {k} lie from {a} to {b}, including both?", f"{a} ৰ পৰা {b} লৈ (দুয়োটা ধৰি) {k} ৰ গুণিতক কিমান?"), "answer": str(n), "why": B(f"Count from the first to the last multiple: {n}.", f"প্ৰথম গুণিতকৰ পৰা শেষলৈ: {n}।")}


def digit_count(a, b, d):
    n = sum(str(x).count(d) for x in range(a, b + 1))
    return {"q": B(f"How many times is the digit {d} written from {a} to {b}?", f"{a} ৰ পৰা {b} লৈ {d} অংকটো কিমানবাৰ লিখা হয়?"), "answer": str(n), "why": B(f"Count the units and the tens separately: {n}.", f"একক আৰু দহক পৃথককৈ গণা: {n}।")}


def lesson_puzzles():
    p = "rs8"
    u1 = unit("u1", B("Read with a condition", "চৰ্তৰে পঢ়া"), "star", [B("Move through digits one at a time.", "এটা এটাকৈ অংক চোৱা।"), B("Check the digit you want first.", "বিচৰা অংকটো আগতে।"), B("Then check its neighbours.", "তাৰ পিছত কাষৰ অংক।"), B("Mark what you have counted.", "গণাখিনি চিন দিয়া।")], [
        diagram(f"{p}.u1.s1", B("Slow is faster", "লাহে যোৱাই খৰ"), [B("These questions punish skimming. Stop at each target digit and test it.", "এই প্ৰশ্নত আওপকীয়া পঢ়া নচলে। প্ৰতিটো লক্ষ্য অংকত ৰৈ পৰীক্ষা কৰা।")], "flow", [B("Find the digit", "অংক উলিওৱা"), B("Look before", "আগত চোৱা"), B("Look after", "পিছত চোৱা")]),
        diagram(f"{p}.u1.s2", B("Both means both", "দুয়োটা মানে দুয়োটা"), [B("'Before and after' needs two ticks. One tick is not a count.", "'আগত আৰু পিছত' দুটা টিক লাগে। এটাত নহয়।")], "flow", [same("3 5 7 ✓"), same("3 5 2 ✗"), same("4 5 7 ✗")]),
        solve(f"{p}.u1.q1", SCAN, scan_before, [("3523585236753", "5", "3"), ("7274727672147", "7", "2"), ("9149419491493", "4", "1")]),
        solve(f"{p}.u1.q2", SCAN, scan_both, [("3573528357358", "5", "3", "7"), ("6282681826286", "2", "6", "8"), ("1451341451541", "4", "1", "5")]),
        tf(f"{p}.u1.q3", SCAN, B("In 2 5 2 7, one 5 sits straight after a 2.", "2 5 2 7 ত এটা 5, 2 ৰ ঠিক পিছত।"), True, B("Only the first 2 is followed by 5.", "কেৱল প্ৰথম 2 ৰ পিছত 5।"), ("r-m-halfscan", HALF)),
        match(f"{p}.u1.q4", SCAN, B("In 4 1 4 2 4 2, match the question to the count", "4 1 4 2 4 2 ত প্ৰশ্নক সংখ্যাৰ লগত মিলোৱা"), [[B("How many 4s?", "4 কিমান?"), same(3)], [B("How many 2s?", "2 কিমান?"), same(2)], [B("How many 1s?", "1 কিমান?"), same(1)]], B("Test each.", "প্ৰতিটো চোৱা।")),
        order(f"{p}.u1.q5", SCAN, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Read the condition", "চৰ্ত পঢ়া"), B("Find the digit", "অংক উলিওৱা"), B("Test neighbours", "কাষ চোৱা"), B("Add to the count", "গণনাত যোগ")], B("Condition first.", "চৰ্ত আগতে।")),
    ])
    u2 = unit("u2", B("Pairs that slide along", "আগবঢ়া যোৰ"), "star", [B("A pair overlaps the next pair.", "এটা যোৰ পিছৰটোৰ লগত সানিছে।"), B("Move one digit, not two.", "এটা অংক সৰা, দুটা নহয়।"), B("n digits give n − 1 pairs.", "n অংকত n − 1 যোৰ।"), B("Test every pair.", "প্ৰতিটো যোৰ চোৱা।")], [
        diagram(f"{p}.u2.s1", B("Overlapping pairs", "সানমিহলি যোৰ"), [B("In 2 4 6, both 2 4 and 4 6 are pairs. The middle digit is in two.", "2 4 6 ত 2 4 আৰু 4 6 দুয়োটা যোৰ। মাজৰ অংক দুয়োটাত।")], "flow", [same("2 4"), same("4 6"), B("2 pairs", "2 যোৰ")]),
        diagram(f"{p}.u2.s2", B("Slide one step", "এক খোজ সৰা"), [B("Point at two digits, test them, then move one step right.", "দুটা অংক দেখুৱাই চোৱা, এক খোজ সোঁফালে সৰা।")], "flow", [B("Point", "দেখুওৱা"), B("Test", "চোৱা"), B("Slide", "সৰা")]),
        solve(f"{p}.u2.q1", PAIRS, even_pairs, [("246135824",), ("8426315648",), ("1248627935",)]),
        solve(f"{p}.u2.q2", PAIRS, sum_pairs, [("3524614352", 7), ("1827364554", 9), ("2356241342", 5)]),
        tf(f"{p}.u2.q3", PAIRS, B("A line of 10 digits has 9 neighbouring pairs.", "10 অংকৰ শাৰীত 9 কাষৰ যোৰ।"), True, B("n − 1 pairs.", "n − 1 যোৰ।")),
        match(f"{p}.u2.q4", PAIRS, B("Match the digits to the even pairs", "অংকক যুগ্ম যোৰৰ লগত মিলোৱা"), [[same("2 4 6"), same(2)], [same("2 3 4"), same(0)], [same("8 8 1"), same(1)]], B("Slide along each.", "প্ৰতিটোত আগবাঢ়া।")),
        order(f"{p}.u2.q5", PAIRS, B("Put the method in order", "পদ্ধতি ক্ৰমে সজোৱা"), [B("Take the first two", "প্ৰথম দুটা"), B("Test the rule", "নিয়ম চোৱা"), B("Move one digit", "এক অংক সৰা"), B("Repeat to the end", "শেষলৈ")], B("Move by one.", "এক অংক সৰা।")),
    ])
    u3 = unit("u3", B("Putting things in order", "ক্ৰমে সজোৱা"), "star", [B("Ascending runs small to large.", "উৰ্ধ্বক্ৰম সৰুৰ পৰা ডাঙৰ।"), B("Descending runs large to small.", "অধঃক্ৰম ডাঙৰৰ পৰা সৰু।"), B("Write the order first.", "প্ৰথমে ক্ৰম লিখা।"), B("Then read the position asked.", "তাৰ পিছত সোধা স্থান পঢ়া।")], [
        diagram(f"{p}.u3.s1", B("Write it out", "লিখি লোৱা"), [B("Do not sort in your head. Write the new order, then count.", "মনতে নসজাবা। নতুন ক্ৰম লিখি গণা।")], "flow", [same("381"), same("138"), B("2nd: 3", "২য়: 3")]),
        diagram(f"{p}.u3.s2", B("Middle of an odd list", "বিজোৰ তালিকাৰ মাজ"), [B("With five numbers, the third in order is the middle.", "পাঁচটা সংখ্যাত ক্ৰমৰ তৃতীয়টো মাজত।")], "flow", [same("1"), same("2"), B("3 middle", "3 মাজত"), same("4")]),
        solve(f"{p}.u3.q1", SORT, sorted_mid, [([47, 12, 83, 35, 66],), ([92, 18, 54, 27, 71],), ([33, 88, 15, 60, 42],)]),
        solve(f"{p}.u3.q2", SORT, digit_sort, [(5283,), (9416,), (7305,)]),
        tf(f"{p}.u3.q3", SORT, B("In descending order, the largest number comes first.", "অধঃক্ৰমত ডাঙৰ সংখ্যা আগত।"), True, B("Descending goes downward.", "অধঃক্ৰম তললৈ যায়।")),
        match(f"{p}.u3.q4", SORT, B("Match the list to its middle", "তালিকাক মাজৰ লগত মিলোৱা"), [[same("9, 1, 5"), same(5)], [same("2, 8, 7"), same(7)], [same("6, 3, 4"), same(4)]], B("Sort first.", "আগতে সজোৱা।")),
        order(f"{p}.u3.q5", SORT, B("Ascending order", "উৰ্ধ্বক্ৰম"), [same(n) for n in (18, 45, 62, 90)], B("Smallest first.", "সৰুটো আগতে।")),
    ])
    u4 = unit("u4", B("Build a number", "সংখ্যা বনোৱা"), "star", [B("For the largest, put big digits first.", "ডাঙৰৰ বাবে ডাঙৰ অংক আগত।"), B("For the smallest, put small digits first.", "সৰুৰ বাবে সৰু অংক আগত।"), B("A number cannot begin with 0.", "সংখ্যা 0 ৰে আৰম্ভ নহয়।"), B("Use each digit once unless told.", "নকলে প্ৰতিটো অংক এবাৰ।")], [
        diagram(f"{p}.u4.s1", B("Place decides value", "স্থানে মান ঠিক কৰে"), [B("The leftmost place is worth the most, so it gets the biggest digit.", "বাওঁফালৰ স্থানৰ মান বেছি, সেয়ে ডাঙৰ অংক তাত।")], "flow", [same("5, 2, 8"), B("Largest", "ডাঙৰ"), same("852")]),
        diagram(f"{p}.u4.s2", B("The zero rule", "শূন্যৰ নিয়ম"), [B("From 0, 3, 7 the smallest is 307, not 037.", "0, 3, 7 ৰ পৰা সৰু 307, 037 নহয়।")], "flow", [same("0, 3, 7"), B("Not 037", "037 নহয়"), same("307")]),
        solve(f"{p}.u4.q1", BUILD, largest, [(("4", "9", "2", "7"),), (("3", "1", "8", "5"),), (("6", "0", "4", "2"),)]),
        solve(f"{p}.u4.q2", BUILD, smallest, [(("5", "0", "3", "8"),), (("7", "2", "0", "4"),), (("9", "6", "1", "3"),)]),
        solve(f"{p}.u4.q3", BUILD, diff_big, [(("3", "1", "4"),), (("5", "2", "7"),), (("8", "0", "6"),)]),
        tf(f"{p}.u4.q4", BUILD, B("From 0, 2, 5 the smallest three-digit number is 025.", "0, 2, 5 ৰ পৰা সৰু তিনিটা অংকৰ সংখ্যা 025।"), False, B("It is 205.", "ই 205।"), ("r-m-placeval", ZERO)),
        match(f"{p}.u4.q5", BUILD, B("Digits 1, 4, 6: match", "অংক 1, 4, 6: মিলোৱা"), [[B("Largest", "ডাঙৰ"), same(641)], [B("Smallest", "সৰু"), same(146)], [B("Difference", "পাৰ্থক্য"), same(495)]], B("641 − 146 = 495.", "641 − 146 = 495।")),
        order(f"{p}.u4.q6", BUILD, B("Build the largest from 3, 7, 1", "3, 7, 1 ৰে ডাঙৰ সংখ্যা"), [same(7), same(3), same(1)], B("Big digits first.", "ডাঙৰ অংক আগত।")),
    ])
    u5 = unit("u5", B("Places in a line", "শাৰীত স্থান"), "star", [B("From right = total − left + 1.", "সোঁফালৰ স্থান = মুঠ − বাওঁ + 1।"), B("Count both ends in the total.", "দুই মূৰ মুঠত গণা।"), B("Multiples: divide and count.", "গুণিতক: হৰণ কৰি গণা।"), B("Count digits by place.", "স্থান অনুসৰি অংক গণা।")], [
        diagram(f"{p}.u5.s1", B("The plus-one rule", "যোগ এক নিয়ম"), [B("In a line of 10, 3rd from left is 8th from right: 10 − 3 + 1.", "10 জনৰ শাৰীত বাওঁফালৰ 3 নম্বৰ, সোঁফালৰ 8: 10 − 3 + 1।")], "flow", [same("10 total"), same("3 from left"), same("8 from right")]),
        diagram(f"{p}.u5.s2", B("Counting multiples", "গুণিতক গণনা"), [B("From 1 to 50 there are 7 multiples of 7, since 50 ÷ 7 is 7 and a bit.", "1 ৰ পৰা 50 ৰ ভিতৰত 7 ৰ গুণিতক 7 টা, কাৰণ 50 ÷ 7 ৰ ভাগফল 7।")], "flow", [same("50 ÷ 7"), B("Whole part 7", "ভাগফল 7"), B("7 multiples", "7 গুণিতক")]),
        solve(f"{p}.u5.q1", MIDDLE, pos_from, [(20, 7), (35, 12), (42, 18)]),
        solve(f"{p}.u5.q2", MIDDLE, count_between, [(10, 50, 6), (20, 80, 7), (15, 90, 9)]),
        solve(f"{p}.u5.q3", MIDDLE, digit_count, [(1, 30, "3"), (1, 50, "5"), (10, 40, "2")]),
        tf(f"{p}.u5.q4", MIDDLE, B("In a line of 15, the 8th from the left is the middle person.", "15 জনৰ শাৰীত বাওঁফালৰ 8 নম্বৰ মাজৰজন।"), True, B("15 − 8 + 1 = 8 from each end.", "15 − 8 + 1 = 8, দুয়োফালৰ পৰা 8।")),
        order(f"{p}.u5.q6", MIDDLE, B("From the 5th in a line of 9, order the steps", "9 জনৰ শাৰীৰ 5 নম্বৰৰ বাবে খোজ সজোৱা"), [B("Write the total", "মুঠ লিখা"), B("Subtract the place", "স্থান বিয়োগ"), B("Add one", "এক যোগ"), B("Read the answer", "উত্তৰ পঢ়া")], B("Total − place + 1.", "মুঠ − স্থান + 1।")),
        match(f"{p}.u5.q5", MIDDLE, B("In a line of 12, match", "12 জনৰ শাৰীত মিলোৱা"), [[B("1st from left", "বাওঁফালৰ ১ম"), same(12)], [B("5th from left", "বাওঁফালৰ ৫ম"), same(8)], [B("9th from left", "বাওঁফালৰ ৯ম"), same(4)]], B("Total − left + 1.", "মুঠ − বাওঁ + 1।")),
    ])
    u6 = unit("u6", B("Let the options help", "বিকল্পৰ সহায়"), "star", [B("Check the last digit first.", "প্ৰথমে শেষ অংক চোৱা।"), B("Check odd or even.", "অযুগ্ম নে যুগ্ম চোৱা।"), B("Estimate the size.", "আকাৰ অনুমান কৰা।"), B("Then test only what remains.", "বাকীখিনিহে পৰীক্ষা কৰা।")], [
        diagram(f"{p}.u6.s1", B("Cut options fast", "বিকল্প খৰকৈ কমোৱা"), [B("Without solving fully, last digits often rule out two options.", "সম্পূৰ্ণ সমাধান নকৰাকৈ শেষ অংকে প্ৰায়ে দুটা বিকল্প বাদ দিয়ে।")], "flow", [B("Last digit", "শেষ অংক"), B("Odd or even", "অযুগ্ম, যুগ্ম"), B("Size", "আকাৰ")]),
        diagram(f"{p}.u6.s2", B("Reverse the question", "প্ৰশ্ন ওলোটোৱা"), [B("Put an option back into the question. If it fits, you are done.", "বিকল্প প্ৰশ্নত বহুওৱা। মিলিলেই হ'ল।")], "flow", [B("Take an option", "বিকল্প লোৱা"), B("Plug it in", "বহুওৱা"), B("Does it fit?", "মিলিলনে?")]),
        solve(f"{p}.u6.q1", CHECK, lambda a, b: {"q": B(f"What is the last digit of {a} × {b}?", f"{a} × {b} ৰ শেষ অংক কি?"), "answer": str(a * b % 10), "why": B(f"Multiply last digits only: {a % 10} × {b % 10}.", f"কেৱল শেষ অংক পূৰণ কৰা: {a % 10} × {b % 10}।")}, [(47, 36), (123, 58), (89, 74)]),
        tf(f"{p}.u6.q2", CHECK, B("The product of two odd numbers is odd.", "দুটা অযুগ্ম সংখ্যাৰ পূৰণফল অযুগ্ম।"), True, B("Odd × odd stays odd.", "অযুগ্ম × অযুগ্ম অযুগ্মই থাকে।")),
        match(f"{p}.u6.q3", CHECK, B("Match the sum to its kind", "যোগফলক ধৰণৰ লগত মিলোৱা"), [[B("Odd + odd", "অযুগ্ম + অযুগ্ম"), B("Even", "যুগ্ম")], [B("Odd + even", "অযুগ্ম + যুগ্ম"), B("Odd", "অযুগ্ম")], [B("Ends in 0", "শেষত 0"), B("Divides by 10", "10 ৰে হৰণ হয়")]], B("Parity rules.", "যুগ্ম-অযুগ্ম নিয়ম।")),
        stepwise(f"{p}.u6.q4", CHECK, lambda a, b: {"q": B(f"Which is {a} × {b} without full multiplication?", f"সম্পূৰ্ণ পূৰণ নকৰাকৈ {a} × {b} কোনটো?"), "parts": [
            part(B("Last digit?", "শেষ অংক?"), same(a * b % 10), [same((a * b + 2) % 10), same((a * b + 5) % 10)], B("Multiply last digits.", "শেষ অংক পূৰণ কৰা।"), sid=f"{p}.u6.q4"),
            part(B("The answer?", "উত্তৰ?"), same(a * b), [same(a * b + 2), same(a * b + 5)], B("Only one option ends correctly.", "এটাহে শুদ্ধকৈ শেষ হয়।"), sid=f"{p}.u6.q4"),
        ], "why": B("Last digits narrow it at once.", "শেষ অংকে লগে লগে কমায়।")}, [(13, 17), (24, 16), (32, 19)]),
        order(f"{p}.u6.q5", CHECK, B("Elimination in order", "বাদ দিয়া ক্ৰম"), [B("Last digit", "শেষ অংক"), B("Parity", "যুগ্ম-অযুগ্ম"), B("Size", "আকাৰ"), B("Plug in", "বহুওৱা")], B("Cheapest test first.", "সহজ পৰীক্ষা আগতে।")),
    ])
    test = {"id": "test", "title": B("Number puzzle test", "সংখ্যা সাঁথৰৰ পৰীক্ষা"), "steps": [
        solve(f"{p}.t.q1", SCAN, scan_before, [("8428148248128", "8", "4"), ("6356563656365", "5", "6")]),
        solve(f"{p}.t.q2", PAIRS, even_pairs, [("4682139426",), ("2468135792",)]),
        solve(f"{p}.t.q3", SORT, sorted_mid, [([73, 21, 58, 94, 36],), ([14, 67, 29, 81, 50],)]),
        solve(f"{p}.t.q4", BUILD, largest, [(("2", "8", "5", "1"),), (("9", "3", "7", "0"),)]),
        solve(f"{p}.t.q5", MIDDLE, pos_from, [(25, 9), (30, 11)]),
        tf(f"{p}.t.q6", BUILD, B("A number cannot begin with 0.", "সংখ্যা 0 ৰে আৰম্ভ নহয়।"), True, B("That digit would add nothing.", "সেই অংকৰ মূল্য নাথাকে।")),
    ]}
    return {"id": "rs-08-number-puzzles", "no": 8, "slug": "number-puzzles", "title": B("Number puzzles", "সংখ্যাৰ সাঁথৰ"), "reign": B("Scanning, ordering, building numbers", "চকু ফুৰোৱা, ক্ৰম, সংখ্যা বনোৱা"), "units": [u1, u2, u3, u4, u5, u6], "test": test}


class OPERATORS:
    lesson = staticmethod(lesson_operators)


class PUZZLES:
    lesson = staticmethod(lesson_puzzles)
