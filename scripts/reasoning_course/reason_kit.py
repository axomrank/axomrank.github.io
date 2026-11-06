"""Helpers for the Reasoning generator (scripts/build_reasoning_course.py).

Puzzles compute their answers here, so text and answer cannot drift apart.
A step's id is permanent; its variants may grow. Past papers set the patterns only:
never copy their wording, words or numbers.
"""
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def enc(word, k):
    return "".join(AZ[(AZ.index(c) + k) % 26] for c in word)


def enc_steps(word, gaps):
    """Each letter moves by its own gap: gaps repeat if the word is longer."""
    return "".join(AZ[(AZ.index(c) + gaps[i % len(gaps)]) % 26] for i, c in enumerate(word))


def pos(c):
    return AZ.index(c) + 1


def rev_pos(c):
    return 27 - pos(c)


def word_sum(word):
    return sum(pos(c) for c in word)


def signed(n):
    return f"+{n}" if n > 0 else f"−{-n}" if n < 0 else "0"


def pair_swap(word):
    out = list(word)
    for i in range(0, len(out) - 1, 2):
        out[i], out[i + 1] = out[i + 1], out[i]
    return "".join(out)


def half_swap(word):
    h = len(word) // 2
    return word[-h:] + word[h:-h] + word[:h]


# ---------------------------------------------------------------- directions
FACE = [("north", "উত্তৰ"), ("east", "পূব"), ("south", "দক্ষিণ"), ("west", "পশ্চিম")]
STEP = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def face_en(f):
    return FACE[f % 4][0]


def face_as(f):
    return FACE[f % 4][1]


def walk(f, route):
    """route: ints walk forward, 'L' and 'R' turn. Returns x, y, facing, starting at the origin."""
    x = y = 0
    for move in route:
        if move == "L":
            f = (f + 3) % 4
        elif move == "R":
            f = (f + 1) % 4
        else:
            x += STEP[f][0] * move
            y += STEP[f][1] * move
    return x, y, f


def place(x, y):
    """The value the walk scene reports in place mode."""
    return (x + 50) * 100 + y + 50


def route_text(f, route):
    en, as_ = [f"Face {face_en(f)}."], [f"{face_as(f)}লৈ মুখ কৰা।"]
    for move in route:
        if move == "L":
            en.append("Turn left."), as_.append("বাওঁফালে ঘূৰা।")
        elif move == "R":
            en.append("Turn right."), as_.append("সোঁফালে ঘূৰা।")
        else:
            en.append(f"Walk {move}."), as_.append(f"{move} ঘৰ যোৱা।")
    return " ".join(en), " ".join(as_)


def spot(x, y):
    """Where a point lies from the start, in both languages."""
    en, as_ = [], []
    if y:
        en.append(f"{abs(y)} {'north' if y > 0 else 'south'}"), as_.append(f"{'উত্তৰে' if y > 0 else 'দক্ষিণে'} {abs(y)}")
    if x:
        en.append(f"{abs(x)} {'east' if x > 0 else 'west'}"), as_.append(f"{'পূবে' if x > 0 else 'পশ্চিমে'} {abs(x)}")
    return (", ".join(en) or "the start"), (", ".join(as_) or "আৰম্ভণিৰ ঠাই")


# ---------------------------------------------------------------- Venn regions
def bits(*regions):
    """The value the venn scene reports: one bit per shaded region."""
    return sum(1 << r for r in set(regions))
