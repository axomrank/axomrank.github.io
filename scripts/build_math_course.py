#!/usr/bin/env python3
"""Generate the Mathematics course: lessons, course file, skill graph and placement probes.

Run: python3 scripts/build_math_course.py && python3 scripts/check_math.py && python3 scripts/build.py

Topic order follows the lecture decks supplied by the course owner (docs/MATHEMATICS-COURSE.md).
Every question here is original: the decks set the syllabus, not the wording or the numbers.
Step ids are permanent. Add variants freely; never rename an id.
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from math_kit import B, fr, mcq  # noqa: E402
from math_lessons_a import l1, l2  # noqa: E402
from math_lessons_b import l3, l5  # noqa: E402
from math_labs import apply  # noqa: E402
from math_lessons_c import l6, l7  # noqa: E402
from math_lessons_d import l4, l8  # noqa: E402
from math_lessons_e import l9, l10  # noqa: E402
from math_lessons_f import l11, l12  # noqa: E402
from math_lessons_g import l13, l14  # noqa: E402
from math_lessons_h import l15, l16  # noqa: E402

COURSE = "mathematics"
SOURCE = {
    "title": "Axomrank original worked examples",
    "url": "",
    "used_for": "All questions and numbers are original. Topic order follows lecture decks supplied by the course owner; no question text was copied.",
}
REVIEW = "Answers computed by scripts/build_math_course.py and rechecked by scripts/check_math.py. Independent Assamese editorial review pending."

# id, title, tier, era, lesson number (position), cover
TOPICS = [
    ("numbers", B("Numbers that talk", "কথা কোৱা সংখ্যা"), B("Types, divisibility, unit digits", "প্ৰকাৰ, বিভাজ্যতা, একক অংক"), "B", "foundations"),
    ("lcm", B("LCM and HCF", "ল.সা.গু. আৰু গ.সা.গু."), B("Factors, multiples, the product rule", "গুণনীয়ক, গুণিতক, পূৰণফলৰ নিয়ম"), "A", "foundations"),
    ("fractions", B("Fractions you can see", "দেখিব পৰা ভগ্নাংশ"), B("Meaning, adding, decimals", "অৰ্থ, যোগ, দশমিক"), "A", "foundations"),
    ("simplify", B("Simplification and roots", "সৰলীকৰণ আৰু মূল"), B("BODMAS, squares, square roots", "BODMAS, বৰ্গ, বৰ্গমূল"), "A", "foundations"),
    ("percentage", B("Percentage", "শতাংশ"), B("Out of 100, change, successive change", "এশৰ ভিতৰত, পৰিৱৰ্তন, ক্ৰমিক পৰিৱৰ্তন"), "A", "money"),
    ("ratio", B("Ratio and proportion", "অনুপাত আৰু সমানুপাত"), B("Sharing, combining, proportion", "ভাগ, যোগ, সমানুপাত"), "A", "money"),
    ("average", B("Average", "গড়"), B("Mean, replacement, weighted average", "গড়, সলনি, ভাৰিত গড়"), "A", "money"),
    ("profit", B("Profit, loss and discount", "লাভ, লোকচান আৰু ৰেহাই"), B("Cost, marked price, discount", "ক্ৰয় মূল্য, চিহ্নিত মূল্য, ৰেহাই"), "A", "money"),
    ("interest", B("Simple and compound interest", "সৰল আৰু চক্ৰবৃদ্ধি সুত"), B("Rate, time, growth", "হাৰ, সময়, বৃদ্ধি"), "A", "money"),
    ("work", B("Time and work", "সময় আৰু কাম"), B("Rates, pipes and tanks", "হাৰ, পাইপ আৰু টেংকী"), "A", "motion"),
    ("speed", B("Speed, distance and trains", "গতি, দূৰত্ব আৰু ৰেল"), B("Average speed, relative speed", "গড় গতি, আপেক্ষিক গতি"), "A", "motion"),
    ("age", B("Age problems", "বয়সৰ সমস্যা"), B("Ratios across the years", "বছৰে বছৰে অনুপাত"), "C", "motion"),
    ("sequence", B("AP and GP", "সমান্তৰ আৰু গুণোত্তৰ শ্ৰেণী"), B("Terms and sums", "পদ আৰু যোগফল"), "B", "shape"),
    ("trig", B("Trigonometry", "ত্ৰিকোণমিতি"), B("Ratios, values, height and distance", "অনুপাত, মান, উচ্চতা আৰু দূৰত্ব"), "B", "shape"),
    ("geometry", B("Plane figures", "সমতল আকৃতি"), B("Triangle, quadrilateral, circle", "ত্ৰিভুজ, চতুৰ্ভুজ, বৃত্ত"), "A", "shape"),
    ("solids", B("Solid figures", "ঘন আকৃতি"), B("Surface area and volume", "পৃষ্ঠকালি আৰু আয়তন"), "B", "shape"),
]
ERAS = [
    ("foundations", B("Number foundations", "সংখ্যাৰ ভেটি"), 1, 4),
    ("money", B("Percent and money", "শতাংশ আৰু ধন"), 5, 9),
    ("motion", B("Rates in motion", "গতিৰ হাৰ"), 10, 12),
    ("shape", B("Patterns and shapes", "শ্ৰেণী আৰু আকৃতি"), 13, 16),
]
# skill id: (topic, title, prerequisites). The order is the order the placement round tests them.
SKILLS = {
    "n-line": ("numbers", B("The number line", "সংখ্যা ৰেখা"), []),
    "n-decimal": ("numbers", B("Decimals on the line", "ৰেখাত দশমিক"), ["n-line"]),
    "n-types": ("numbers", B("Number types", "সংখ্যাৰ প্ৰকাৰ"), []),
    "n-factor": ("numbers", B("Prime factors", "মৌলিক গুণনীয়ক"), ["n-types"]),
    "n-div": ("numbers", B("Divisibility", "বিভাজ্যতা"), ["n-types"]),
    "n-unit": ("numbers", B("Unit digits", "একক অংক"), []),
    "l-hcf": ("lcm", B("HCF", "গ.সা.গু."), ["n-factor"]),
    "l-lcm": ("lcm", B("LCM", "ল.সা.গু."), ["n-factor"]),
    "l-apply": ("lcm", B("LCM and HCF problems", "ল.সা.গু. আৰু গ.সা.গু.ৰ সমস্যা"), ["l-hcf", "l-lcm"]),
    "f-meaning": ("fractions", B("Fraction meaning", "ভগ্নাংশৰ অৰ্থ"), []),
    "f-equiv": ("fractions", B("Equal fractions", "সমান ভগ্নাংশ"), ["f-meaning", "l-hcf"]),
    "f-compare": ("fractions", B("Comparing fractions", "ভগ্নাংশৰ তুলনা"), ["f-equiv"]),
    "f-add": ("fractions", B("Adding fractions", "ভগ্নাংশ যোগ"), ["f-equiv", "l-lcm"]),
    "f-of": ("fractions", B("Fraction of a quantity", "পৰিমাণৰ ভগ্নাংশ"), ["f-meaning"]),
    "f-dec": ("fractions", B("Fractions and decimals", "ভগ্নাংশ আৰু দশমিক"), ["f-equiv", "n-decimal"]),
    "s-bodmas": ("simplify", B("Order of operations", "গণনাৰ ক্ৰম"), ["f-add"]),
    "s-roots": ("simplify", B("Squares and roots", "বৰ্গ আৰু বৰ্গমূল"), ["n-factor"]),
    "s-perfect": ("simplify", B("Perfect squares", "পূৰ্ণবৰ্গ"), ["s-roots", "n-factor"]),
    "s-ident": ("simplify", B("Square patterns", "বৰ্গৰ আৰ্হি"), ["s-roots"]),
    "p-meaning": ("percentage", B("Percent meaning", "শতাংশৰ অৰ্থ"), ["f-dec"]),
    "p-of": ("percentage", B("Percent of a quantity", "পৰিমাণৰ শতাংশ"), ["p-meaning", "f-of"]),
    "p-change": ("percentage", B("Percent change", "শতাংশ পৰিৱৰ্তন"), ["p-of"]),
    "p-succ": ("percentage", B("Successive change", "ক্ৰমিক পৰিৱৰ্তন"), ["p-change"]),
    "p-compare": ("percentage", B("More than, less than", "বেছি আৰু কম"), ["p-change"]),
    "r-share": ("ratio", B("Sharing in a ratio", "অনুপাতত ভাগ"), ["f-of"]),
    "r-prop": ("ratio", B("Proportion", "সমানুপাত"), ["r-share", "f-equiv"]),
    "r-combine": ("ratio", B("Linked ratios", "সংযুক্ত অনুপাত"), ["r-prop", "l-lcm"]),
    "a-mean": ("average", B("Average", "গড়"), ["s-bodmas"]),
    "a-change": ("average", B("When one value changes", "এটা মান সলনি হ'লে"), ["a-mean"]),
    "a-weight": ("average", B("Group averages", "গোটৰ গড়"), ["a-mean", "r-share"]),
    "pl-basic": ("profit", B("Profit and loss", "লাভ আৰু লোকচান"), ["p-change"]),
    "pl-discount": ("profit", B("Discount", "ৰেহাই"), ["pl-basic", "p-succ"]),
    "pl-deals": ("profit", B("Tricky deals", "কৌশলী লেনদেন"), ["pl-basic", "r-share"]),
    "i-si": ("interest", B("Simple interest", "সৰল সুত"), ["p-of"]),
    "i-solve": ("interest", B("Finding rate and time", "হাৰ আৰু সময় উলিওৱা"), ["i-si"]),
    "i-ci": ("interest", B("Compound interest", "চক্ৰবৃদ্ধি সুত"), ["i-si", "p-succ"]),
    "i-diff": ("interest", B("Compound against simple", "চক্ৰবৃদ্ধি বনাম সৰল"), ["i-ci"]),
    "w-rate": ("work", B("Work rates", "কামৰ হাৰ"), ["f-add", "l-lcm"]),
    "w-men": ("work", B("People and days", "মানুহ আৰু দিন"), ["r-prop"]),
    "w-pipes": ("work", B("Pipes and tanks", "পাইপ আৰু টেংকী"), ["w-rate"]),
    "sp-basic": ("speed", B("Speed and distance", "গতি আৰু দূৰত্ব"), ["r-share"]),
    "sp-avg": ("speed", B("Average speed", "গড় গতি"), ["sp-basic", "a-weight"]),
    "sp-rel": ("speed", B("Trains and relative speed", "ৰেল আৰু আপেক্ষিক গতি"), ["sp-basic"]),
    "age-gap": ("age", B("The fixed age gap", "বয়সৰ স্থিৰ ব্যৱধান"), ["n-line"]),
    "age-ratio": ("age", B("Age problems", "বয়সৰ সমস্যা"), ["r-share", "age-gap"]),
    "ap": ("sequence", B("Arithmetic progression", "সমান্তৰ শ্ৰেণী"), []),
    "ap-sum": ("sequence", B("Sum of an AP", "সমান্তৰ শ্ৰেণীৰ যোগফল"), ["ap"]),
    "gp": ("sequence", B("Geometric progression", "গুণোত্তৰ শ্ৰেণী"), ["n-unit"]),
    "tr-ratio": ("trig", B("Trig ratios", "ত্ৰিকোণমিতিক অনুপাত"), ["s-roots"]),
    "tr-values": ("trig", B("Standard values", "প্ৰমাণ মান"), ["tr-ratio"]),
    "tr-height": ("trig", B("Heights and distances", "উচ্চতা আৰু দূৰত্ব"), ["tr-values"]),
    "g-rect": ("geometry", B("Squares and rectangles", "বৰ্গ আৰু আয়ত"), ["s-roots", "l-hcf"]),
    "g-sides": ("geometry", B("Triangle side rule", "ত্ৰিভুজৰ বাহুৰ নিয়ম"), ["n-line"]),
    "g-tri": ("geometry", B("Triangles", "ত্ৰিভুজ"), ["s-roots"]),
    "g-quad": ("geometry", B("Rhombus and trapezium", "ৰম্বাছ আৰু ট্ৰেপিজিয়াম"), ["g-tri"]),
    "g-circle": ("geometry", B("Circles", "বৃত্ত"), ["f-of"]),
    "g-solid": ("solids", B("Volume and surface", "আয়তন আৰু পৃষ্ঠকালি"), ["g-rect"]),
    "g-round": ("solids", B("Cylinders and cones", "চুঙা আৰু শংকু"), ["g-solid", "g-circle"]),
    "g-sphere": ("solids", B("Spheres and recasting", "গোলক আৰু নতুন ৰূপ"), ["g-round"]),
}
MISCONCEPTIONS = {
    "m-neg-order": ("n-line", B("Thinking a bigger-looking negative is bigger", "ডাঙৰ দেখা ঋণাত্মক সংখ্যাক ডাঙৰ ধৰা")),
    "m-dec-long": ("n-decimal", B("Thinking more decimal digits means bigger", "বেছি দশমিক অংক মানে ডাঙৰ বুলি ধৰা")),
    "m-one-prime": ("n-types", B("Calling 1 a prime", "1ক মৌলিক ধৰা")),
    "m-odd-prime": ("n-types", B("Treating every odd number as prime", "প্ৰতিটো অযুগ্ম সংখ্যাক মৌলিক ধৰা")),
    "m-div-last": ("n-div", B("Using the last digit to test 3 or 9", "3 বা 9ৰ বাবে শেষৰ অংক চোৱা")),
    "m-unit-cycle": ("n-unit", B("Multiplying base by power for the unit digit", "একক অংকৰ বাবে ভূমি আৰু ঘাত পূৰণ কৰা")),
    "m-lcm-hcf-swap": ("l-apply", B("Swapping LCM and HCF", "ল.সা.গু. আৰু গ.সা.গু. সলনি কৰা")),
    "m-lcm-product": ("l-lcm", B("Taking the product as the LCM", "পূৰণফলকে ল.সা.গু. ধৰা")),
    "m-hcf-remainder": ("l-apply", B("Forgetting the remainder in LCM or HCF problems", "ল.সা.গু. বা গ.সা.গু.ৰ সমস্যাত ভাগশেষ পাহৰা")),
    "m-hcf-divide": ("l-apply", B("Multiplying instead of dividing by the HCF", "গ.সা.গু.ৰে হৰণৰ ঠাইত পূৰণ কৰা")),
    "m-add-tops": ("f-add", B("Adding tops and bottoms", "লব আৰু হৰ যোগ কৰা")),
    "m-cmp-denom": ("f-compare", B("Thinking a bigger denominator means a bigger fraction", "ডাঙৰ হৰ মানে ডাঙৰ ভগ্নাংশ বুলি ধৰা")),
    "m-simplify-partial": ("f-equiv", B("Stopping before simplest form", "সৰলতম ৰূপৰ আগতে ৰখা")),
    "m-frac-of": ("f-of", B("Dividing by the numerator", "লবেৰে হৰণ কৰা")),
    "m-pct-base": ("p-change", B("Using the wrong base for a percentage", "শতাংশৰ ভুল ভিত্তি লোৱা")),
    "m-pct-add": ("p-succ", B("Adding successive percentages", "ক্ৰমিক শতাংশ যোগ কৰা")),
    "m-pct-undo": ("p-change", B("Expecting the same percent to undo a change", "একে শতাংশই পৰিৱৰ্তন ওভতাব বুলি ধৰা")),
    "m-pct-more-less": ("p-compare", B("Treating more-than and less-than as equal", "বেছি আৰু কম একে বুলি ধৰা")),
    "m-bodmas-lr": ("s-bodmas", B("Working left to right, ignoring order", "ক্ৰম নামানি বাওঁৰ পৰা সোঁলৈ কৰা")),
    "m-root-add": ("s-roots", B("Splitting a root across addition", "যোগৰ ওপৰত মূল ভাঙি দিয়া")),
    "m-ratio-part": ("r-share", B("Using ratio numbers as the amounts", "অনুপাতৰ সংখ্যাকে পৰিমাণ ধৰা")),
    "m-avg-add": ("a-mean", B("Averaging without weighting by count", "সংখ্যা নোচোৱাকৈ গড় কৰা")),
    "m-bodmas-div": ("s-bodmas", B("Putting × ahead of ÷", "÷ৰ আগত × ৰখা")),
    "m-pair-all": ("s-perfect", B("Multiplying by the whole number for a square", "বৰ্গৰ বাবে গোটা সংখ্যাৰে পূৰণ কৰা")),
    "m-square-spread": ("s-ident", B("Dropping the middle term of a square", "বৰ্গৰ মাজৰ পদ এৰা")),
    "m-disc-base": ("pl-discount", B("Taking discount on the wrong price", "ভুল দামৰ ওপৰত ৰেহাই ধৰা")),
    "m-articles-base": ("pl-deals", B("Measuring on the wrong number of items", "ভুল সংখ্যাৰ ওপৰত জোখা")),
    "m-two-items": ("pl-deals", B("Expecting equal profit and loss to cancel", "সমান লাভ আৰু লোকচান কাটিব বুলি ধৰা")),
    "m-si-once": ("i-si", B("Stopping at one year's interest", "এবছৰৰ সুততে ৰখা")),
    "m-si-amount": ("i-si", B("Mixing up interest and amount", "সুত আৰু সমূল ধন সলনি কৰা")),
    "m-work-inverse": ("w-men", B("Treating people and days as rising together", "মানুহ আৰু দিন একেলগে বাঢ়ে বুলি ধৰা")),
    "m-pipe-sign": ("w-pipes", B("Adding an outlet instead of subtracting", "নিৰ্গম বিয়োগৰ ঠাইত যোগ কৰা")),
    "m-unit-convert": ("sp-basic", B("Converting km/h and m/s the wrong way", "km/h আৰু m/s ওলোটাকৈ সলনি কৰা")),
    "m-time-inverse": ("sp-avg", B("Treating time as rising with speed", "গতিৰ লগে লগে সময় বাঢ়ে বুলি ধৰা")),
    "m-rel-sign": ("sp-rel", B("Adding speeds when they should subtract", "বিয়োগৰ ঠাইত গতি যোগ কৰা")),
    "m-age-both": ("age-ratio", B("Moving only one age forward", "কেৱল এটা বয়স আগুৱাই নিয়া")),
    "m-sum-half": ("ap-sum", B("Forgetting to halve the sum", "যোগফল আধা কৰিবলৈ পাহৰা")),
    "m-gp-add": ("gp", B("Adding the ratio in a GP", "গুণোত্তৰ শ্ৰেণীত অনুপাত যোগ কৰা")),
    "m-trig-flip": ("tr-ratio", B("Pairing the wrong reciprocal", "ভুল ওলোটা যোৰা কৰা")),
    "m-height-eye": ("tr-height", B("Forgetting the observer's height", "পৰ্যবেক্ষকৰ উচ্চতা পাহৰা")),
    "m-scale-linear": ("g-rect", B("Thinking area scales like length", "কালি দৈৰ্ঘ্যৰ দৰে বাঢ়ে বুলি ধৰা")),
    "m-perim-half": ("g-rect", B("Giving half the perimeter", "পৰিসীমাৰ আধা দিয়া")),
    "m-angle-sum": ("g-tri", B("Using 360° for a triangle", "ত্ৰিভুজত 360° লোৱা")),
    "m-tri-ineq": ("g-sides", B("Ignoring the triangle side rule", "ত্ৰিভুজৰ বাহুৰ নিয়ম নমনা")),
    "m-circle-formula": ("g-circle", B("Mixing area and circumference", "কালি আৰু পৰিধি সলনি কৰা")),
    "m-litre": ("g-solid", B("Forgetting 1000 cubic cm in a litre", "লিটাৰত 1000 ঘন ছেমি পাহৰা")),
    "m-cone-third": ("g-round", B("Dropping the third in a cone", "শংকুত এক-তৃতীয়াংশ এৰা")),
    "m-sphere-hemi": ("g-sphere", B("Mixing sphere and hemisphere", "গোলক আৰু অৰ্ধগোলক সলনি কৰা")),
    "m-ratio-add": ("r-prop", B("Adding the same number to both sides of a ratio", "অনুপাতৰ দুয়োফালে একে সংখ্যা যোগ কৰা")),
    "m-ratio-flip": ("r-combine", B("Keeping the numbers in place in 2A = 5B", "2A = 5Bত সংখ্যা সলনি নকৰা")),
    "m-chain-common": ("r-combine", B("Linking ratios before matching the middle", "মাজৰ পদ নিমিলোৱাকৈ অনুপাত জোৰা")),
    "m-avg-count": ("a-mean", B("Taking half the count as the middle", "সংখ্যাৰ আধাকে মাজ ধৰা")),
    "m-avg-newcomer": ("a-change", B("Changing the average without using the total", "মুঠ নোলোৱাকৈ গড় সলনি কৰা")),
    "m-cp-base": ("pl-basic", B("Taking profit on selling price", "বিক্ৰী মূল্যৰ ওপৰত লাভ ধৰা")),
    "m-discount-add": ("pl-discount", B("Adding two discounts", "দুটা ৰেহাই যোগ কৰা")),
    "m-si-ci": ("i-ci", B("Using simple interest for compound", "চক্ৰবৃদ্ধিৰ ঠাইত সৰল সুত ধৰা")),
    "m-work-days": ("w-rate", B("Adding days instead of rates", "হাৰৰ ঠাইত দিন যোগ কৰা")),
    "m-speed-avg": ("sp-basic", B("Averaging two speeds directly", "দুটা গতিৰ পোনপটীয়া গড় লোৱা")),
    "m-train-length": ("sp-rel", B("Leaving out the train's own length", "ৰেলৰ নিজৰ দৈৰ্ঘ্য বাদ দিয়া")),
    "m-age-gap": ("age-ratio", B("Letting the age gap change", "বয়সৰ পাৰ্থক্য সলনি কৰা")),
    "m-ap-n": ("ap", B("Using n instead of n − 1", "n − 1ৰ ঠাইত n লোৱা")),
    "m-gp-power": ("gp", B("Using the wrong power in a GP", "গুণোত্তৰ শ্ৰেণীত ভুল ঘাত লোৱা")),
    "m-trig-swap": ("tr-ratio", B("Swapping sine and cosine", "ছাইন আৰু কছাইন সলনি কৰা")),
    "m-tri-area": ("g-tri", B("Forgetting the half in triangle area", "ত্ৰিভুজৰ কালিত আধা পাহৰা")),
    "m-radius-dia": ("g-circle", B("Mixing radius and diameter", "ব্যাসাৰ্ধ আৰু ব্যাস সলনি কৰা")),
    "m-area-volume": ("g-solid", B("Confusing surface area and volume", "পৃষ্ঠকালি আৰু আয়তন সলনি কৰা")),
}


def minus(n):
    return str(n).replace("-", "−")


def probes():
    """One placement question per key skill. Options carry the mistake each one reveals."""
    P = []
    add = lambda sid, skill, fn, params: P.append(mcq(f"bank.math.{sid}", skill, fn, params))  # noqa: E731
    add("line", "n-line", lambda a, b: {"q": B(f"Which is the greatest: {minus(a)}, {minus(b)}, {minus(a - 4)} or {minus(b - 6)}?", f"কোনটো আটাইতকৈ ডাঙৰ: {minus(a)}, {minus(b)}, {minus(a - 4)} নে {minus(b - 6)}?"), "right": minus(max(a, b)), "wrong": [(minus(min(a - 4, b - 6)), "m-neg-order", B("Further left is smaller, even if the digits look bigger.", "যিমান বাওঁফালে সিমান সৰু, অংক ডাঙৰ দেখিলেও।"))], "fill": [minus(a), minus(b), minus(a - 4), minus(b - 6)], "why": B("The greatest is furthest right.", "সোঁফালে আটাইতকৈ আঁতৰত থকাটোৱেই ডাঙৰ।")}, [(-2, -3), (-1, -4), (-3, -5)])
    add("types", "n-types", lambda a, n: {"q": B(f"How many primes lie between {a} and {a + 20}?", f"{a} আৰু {a + 20}ৰ মাজত কেইটা মৌলিক সংখ্যা আছে?"), "right": n, "wrong": [(n + 1, "m-odd-prime", B("Not every odd number is prime.", "প্ৰতিটো অযুগ্ম সংখ্যা মৌলিক নহয়।"))], "fill": [n - 1, n + 2, n + 3], "why": B("Remove the multiples of 3, 5 and 7.", "3, 5 আৰু 7ৰ গুণিতক বাদ দিয়া।")}, [(10, 6), (20, 4), (30, 5)])
    add("unit", "n-unit", lambda b, e: {"q": B(f"The unit digit of ${b}^{{{e}}}$ is", f"${b}^{{{e}}}$ৰ একক অংক"), "right": pow(b, e, 10), "wrong": [(b * e % 10, "m-unit-cycle", B("Unit digits follow a cycle.", "একক অংকই চক্ৰ মানে।"))], "fill": [1, 3, 7, 9, 2], "why": B("Use the cycle of last digits.", "শেষৰ অংকৰ চক্ৰ ব্যৱহাৰ কৰা।")}, [(3, 22), (7, 35), (2, 45)])
    add("hcf", "l-hcf", lambda a, b, h, l: {"q": B(f"The HCF of {a} and {b} is", f"{a} আৰু {b}ৰ গ.সা.গু."), "right": h, "wrong": [(l, "m-lcm-hcf-swap", B("That is the LCM.", "সেয়া ল.সা.গু.।"))], "fill": [h * 2, h + 1, h * 3], "why": B("It is the largest number dividing both.", "দুয়োটাকে হৰণ কৰা সৰ্ববৃহৎ সংখ্যা।")}, [(48, 84, 12, 336), (36, 90, 18, 180), (42, 70, 14, 210)])
    add("lcm", "l-lcm", lambda a, b, l, h: {"q": B(f"The LCM of {a} and {b} is", f"{a} আৰু {b}ৰ ল.সা.গু."), "right": l, "wrong": [(a * b, "m-lcm-product", B("The product is a common multiple, but may not be the lowest.", "পূৰণফল সৰুতম নহ'বও পাৰে।")), (h, "m-lcm-hcf-swap", B("That is the HCF.", "সেয়া গ.সা.গু.।"))], "fill": [l * 2, l + a], "why": B("Take each prime at its highest power.", "প্ৰতিটো মৌলিক ডাঙৰ ঘাতত লোৱা।")}, [(12, 18, 36, 6), (15, 20, 60, 5), (16, 24, 48, 8)])
    add("fadd", "f-add", lambda a, b, c, d: {"q": B(f"${fr(a, b)} + {fr(c, d)}$ equals", f"${fr(a, b)} + {fr(c, d)}$ৰ মান"), "right": F(a, b) + F(c, d), "wrong": [(F(a + c, b + d), "m-add-tops", B("Tops and bottoms do not add directly.", "লব আৰু হৰ পোনে পোনে যোগ নহয়।"))], "fill": [F(a * c, b * d), F(a + c, b * d), F(1, 2)], "why": B("Make the denominators equal first.", "প্ৰথমে হৰ সমান কৰা।")}, [(1, 3, 1, 4), (2, 5, 1, 3), (1, 6, 1, 4)])
    add("fof", "f-of", lambda t, d, a: {"q": B(f"${fr(a, d)}$ of {d * t} is", f"{d * t}ৰ ${fr(a, d)}$ অংশ"), "right": a * t, "wrong": [(F(d * t, a), "m-frac-of", B("Divide by the bottom, multiply by the top.", "তলৰ সংখ্যাৰে হৰণ, ওপৰৰ সংখ্যাৰে পূৰণ।"))], "fill": [t, a * t + t, d * t - a], "why": B("Divide, then multiply.", "হৰণ কৰি পূৰণ কৰা।")}, [(7, 4, 3), (9, 5, 2), (6, 7, 3)])
    add("bodmas", "s-bodmas", lambda a, b, c: {"q": B(f"${a} + {b} \\times {c}$ equals", f"${a} + {b} \\times {c}$ৰ মান"), "right": a + b * c, "wrong": [((a + b) * c, "m-bodmas-lr", B("Multiply before you add.", "যোগৰ আগতে পূৰণ কৰা।"))], "fill": [a * b + c, a + b + c, a + b * c + 1], "why": B("Multiplication comes before addition.", "যোগৰ আগতে পূৰণ।")}, [(6, 4, 5), (8, 3, 7), (5, 6, 4)])
    add("roots", "s-roots", lambda a, b: {"q": B(f"$\\sqrt{{{a * a + b * b}}}$ equals", f"$\\sqrt{{{a * a + b * b}}}$ৰ মান"), "right": int((a * a + b * b) ** 0.5), "wrong": [(a + b, "m-root-add", B("A root does not split across addition.", "যোগৰ ওপৰত মূল নাভাঙে।"))], "fill": [int((a * a + b * b) ** 0.5) + 2, int((a * a + b * b) ** 0.5) - 1, a * b], "why": B("Add first, then take the root.", "প্ৰথমে যোগ কৰি মূল লোৱা।")}, [(3, 4), (6, 8), (5, 12)])
    add("pof", "p-of", lambda k, n: {"q": B(f"{k}% of {n} is", f"{n}ৰ {k}%"), "right": F(k * n, 100), "wrong": [], "fill": [F(k * n, 10), F(k * n, 100) + 10, F(k * n, 100) + 5], "why": B("Build it from 10%.", "10%ৰ পৰা গঢ়া।")}, [(15, 240), (35, 600), (45, 80)])
    add("pchange", "p-change", lambda o, n: {"q": B(f"A price rises from ₹{o} to ₹{n}. The rise is", f"দাম ₹{o}ৰ পৰা ₹{n} হ'ল। বৃদ্ধি"), "right": F((n - o) * 100, o), "wrong": [(F((n - o) * 100, n), "m-pct-base", B("The base is the original price.", "মূল দামেই ভিত্তি।"))], "fill": [n - o, F((n - o) * 100, o) + 5, F((n - o) * 100, o) + 10], "unit": "%", "why": B("Change ÷ original × 100.", "পৰিৱৰ্তন ÷ মূল × 100।")}, [(40, 50), (60, 75), (80, 100)])
    add("psucc", "p-succ", lambda a, b: {"q": B(f"A rise of {a}% followed by {b}% is a total rise of", f"{a}%ৰ পিছত {b}% বৃদ্ধি মুঠ কিমান?"), "right": F(a + b) + F(a * b, 100), "wrong": [(a + b, "m-pct-add", B("The second change acts on the new value.", "দ্বিতীয় পৰিৱৰ্তন নতুন মানৰ ওপৰত।"))], "fill": [a + b - 2, a * b, a + b + 1], "unit": "%", "why": B("$a + b + \\frac{ab}{100}$.", "$a + b + \\frac{ab}{100}$।")}, [(10, 20), (20, 30), (25, 20)])
    add("ratio", "r-share", lambda t, a, b: {"q": B(f"₹{t} is shared in the ratio {a}:{b}. The larger share is", f"₹{t} {a}:{b} অনুপাতত ভাগ কৰা হ'ল। ডাঙৰ ভাগটো"), "right": t * b // (a + b), "unit": "", "wrong": [(t // 2, "m-ratio-part", B("Shares follow the ratio, not an even split.", "ভাগ অনুপাত মানে, সমান নহয়।"))], "fill": [t * a // (a + b), t - b, t // (a + b)], "why": B("One part is the total ÷ the sum of the ratio.", "এটা ভাগ = মুঠ ÷ অনুপাতৰ যোগফল।")}, [(600, 2, 3), (720, 1, 3), (900, 4, 5)])
    add("avg", "a-mean", lambda n1, a1, n2, a2: {"q": B(f"{n1} students average {a1} and {n2} students average {a2}. The overall average is", f"{n1} জন ছাত্ৰৰ গড় {a1} আৰু {n2} জনৰ গড় {a2}। মুঠ গড়"), "right": F(n1 * a1 + n2 * a2, n1 + n2), "wrong": [(F(a1 + a2, 2), "m-avg-add", B("Weight each average by its count.", "প্ৰতিটো গড়ক সংখ্যাৰে ভাৰিত কৰা।"))], "fill": [a2 + 1, a1 - 1, a1 + a2], "why": B("Find both totals, then divide by everyone.", "দুয়োটা মুঠ উলিয়াই সকলোৰে হৰণ কৰা।")}, [(10, 60, 30, 80), (20, 50, 30, 60), (10, 40, 40, 50)])
    add("profit", "pl-basic", lambda c, s_: {"q": B(f"Bought for ₹{c}, sold for ₹{s_}. The profit is", f"₹{c}ত কিনি ₹{s_}ত বিক্ৰী কৰা হ'ল। লাভ"), "right": F((s_ - c) * 100, c), "wrong": [(F((s_ - c) * 100, s_), "m-cp-base", B("Profit is measured on the cost price.", "লাভ ক্ৰয় মূল্যৰ ওপৰত জোখা হয়।"))], "fill": [s_ - c, F((s_ - c) * 100, c) + 10, F((s_ - c) * 100, c) + 5], "unit": "%", "why": B("Profit ÷ cost × 100.", "লাভ ÷ ক্ৰয় মূল্য × 100।")}, [(400, 500), (200, 250), (600, 750)])
    add("discount", "pl-discount", lambda a, b: {"q": B(f"Successive discounts of {a}% and {b}% equal a single discount of", f"{a}% আৰু {b}% ক্ৰমিক ৰেহাই একক কিমান?"), "right": F(a + b) - F(a * b, 100), "wrong": [(a + b, "m-discount-add", B("The second discount acts on the reduced price.", "দ্বিতীয় ৰেহাই কমা দামৰ ওপৰত।"))], "fill": [a + b - 1, a + b + 2, a + b - 8], "unit": "%", "why": B("$a + b - \\frac{ab}{100}$.", "$a + b - \\frac{ab}{100}$।")}, [(10, 20), (20, 25), (10, 30)])
    add("si", "i-si", lambda p, r, t: {"q": B(f"Simple interest on ₹{p} at {r}% a year for {t} years is", f"₹{p}ৰ ওপৰত বছৰি {r}% হাৰত {t} বছৰৰ সৰল সুত"), "right": p * r * t // 100, "unit": "", "wrong": [], "fill": [p * r // 100, p + p * r * t // 100, p * r * t // 10], "why": B("$\\frac{P \\times R \\times T}{100}$.", "$\\frac{P \\times R \\times T}{100}$।")}, [(2000, 5, 3), (1500, 8, 2), (4000, 6, 2)])
    add("ci", "i-ci", lambda p, r: {"q": B(f"Compound interest on ₹{p} at {r}% a year for 2 years is", f"₹{p}ৰ ওপৰত বছৰি {r}% হাৰত 2 বছৰৰ চক্ৰবৃদ্ধি সুত"), "right": p * (100 + r) ** 2 // 10000 - p, "wrong": [(2 * p * r // 100, "m-si-ci", B("That is simple interest. Compound interest earns on interest too.", "সেয়া সৰল সুত। চক্ৰবৃদ্ধিত সুতৰো সুত হয়।"))], "fill": [p * (100 + r) ** 2 // 10000, p * r // 100, 3 * p * r // 100], "why": B("Grow by the multiplier twice, then remove the principal.", "গুণকেৰে দুবাৰ বঢ়াই মূলধন বাদ দিয়া।")}, [(1000, 10), (2000, 5), (5000, 20)])
    add("work", "w-rate", lambda a, b: {"q": B(f"A does a job in {a} days and B in {b} days. Together they need", f"Aই এটা কাম {a} দিনত, Bই {b} দিনত কৰে। একেলগে লাগিব"), "right": F(a * b, a + b), "wrong": [(a + b, "m-work-days", B("Rates add, not days.", "হাৰ যোগ হয়, দিন নহয়।")), (F(a + b, 2), "m-work-days", B("Rates add; days do not average.", "হাৰ যোগ হয়; দিনৰ গড় নহয়।"))], "fill": [F(a * b, a + b) + 2, abs(b - a), F(a * b, a + b) + 5], "unit": " days", "why": B("Add the daily rates, then flip.", "দৈনিক হাৰ যোগ কৰি ওলোটা কৰা।")}, [(12, 24), (10, 15), (20, 30)])
    add("speed", "sp-basic", lambda u, v: {"q": B(f"A car goes out at {u} km/h and returns on the same road at {v} km/h. Its average speed is", f"গাড়ী এখন {u} কিমি/ঘণ্টাত গৈ একে বাটেৰে {v} কিমি/ঘণ্টাত উভতে। গড় গতি"), "right": F(2 * u * v, u + v), "wrong": [(F(u + v, 2), "m-speed-avg", B("Time differs on each leg, so use $\\frac{2uv}{u + v}$.", "প্ৰতিটো অংশৰ সময় বেলেগ, সেয়ে $\\frac{2uv}{u + v}$।"))], "fill": [u + v, v - u, F(2 * u * v, u + v) + 5], "unit": " km/h", "why": B("Total distance ÷ total time.", "মুঠ দূৰত্ব ÷ মুঠ সময়।")}, [(30, 60), (40, 60), (20, 30)])
    add("train", "sp-rel", lambda l, p, v, t: {"q": B(f"A {l} m train at {v} m/s crosses a {p} m platform in", f"{v} মি/ছে গতিৰ {l} মি দীঘল ৰেলে {p} মি প্লেটফৰ্ম পাৰ হ'বলৈ লয়"), "right": t, "wrong": [(F(p, v), "m-train-length", B("The train must cover its own length as well.", "ৰেলে নিজৰ দৈৰ্ঘ্যও পাৰ হ'ব লাগিব।"))], "fill": [F(l, v), t + 5, t * 2], "unit": " s", "why": B("Distance is train plus platform.", "দূৰত্ব = ৰেল + প্লেটফৰ্ম।")}, [(120, 180, 15, 20), (150, 250, 20, 20), (100, 200, 10, 30)])
    add("age", "age-ratio", lambda a, b, y, x: {"q": B(f"Ages are in the ratio {a}:{b}. In {y} years the difference between them will be {x * (b - a)} years. The younger is now", f"বয়সৰ অনুপাত {a}:{b}। {y} বছৰৰ পিছত পাৰ্থক্য {x * (b - a)} বছৰ হ'ব। সৰুজনৰ এতিয়াৰ বয়স"), "right": a * x, "wrong": [(a * x + y, "m-age-gap", B("That is the age in the future. The gap stays fixed, so work from today.", "সেয়া ভৱিষ্যতৰ বয়স। পাৰ্থক্য একে থাকে, সেয়ে আজিৰ পৰা কৰা।"))], "fill": [b * x, a * x - 2, a + b], "unit": " years", "why": B("The gap never changes, so one ratio part is known.", "পাৰ্থক্য নসলনি হয়, সেয়ে এটা অনুপাত ভাগ জনা যায়।")}, [(2, 3, 5, 6), (3, 5, 4, 7), (4, 7, 6, 5)])
    add("ap", "ap", lambda a, d, n: {"q": B(f"The {n}th term of {a}, {a + d}, {a + 2 * d}, … is", f"{a}, {a + d}, {a + 2 * d}, … শ্ৰেণীৰ {n}তম পদ"), "right": a + (n - 1) * d, "wrong": [(a + n * d, "m-ap-n", B("The first term has no steps added, so use $n - 1$.", "প্ৰথম পদত কোনো খোজ নাই, সেয়ে $n - 1$ লোৱা।"))], "fill": [a + (n - 2) * d, a * n, a + (n + 1) * d], "why": B("$a + (n - 1)d$.", "$a + (n - 1)d$।")}, [(1, 3, 15), (4, 5, 20), (7, 2, 31)])
    add("gp", "gp", lambda a, r, n: {"q": B(f"The {n}th term of {a}, {a * r}, {a * r * r}, … is", f"{a}, {a * r}, {a * r * r}, … শ্ৰেণীৰ {n}তম পদ"), "right": a * r ** (n - 1), "wrong": [(a * r ** n, "m-gp-power", B("The power is $n - 1$.", "ঘাত $n - 1$।"))], "fill": [a * r ** (n - 2), a * r * n, a + r ** n], "why": B("$ar^{n-1}$.", "$ar^{n-1}$।")}, [(3, 2, 6), (2, 3, 5), (7, 2, 6)])
    add("trig", "tr-ratio", lambda o, a, h: {"q": B(f"In a right triangle, the side opposite A is {o}, the side next to A is {a} and the hypotenuse is {h}. Sin A is", f"সমকোণী ত্ৰিভুজত Aৰ বিপৰীত বাহু {o}, সংলগ্ন বাহু {a}, অতিভুজ {h}। Sin A"), "right": F(o, h), "wrong": [(F(a, h), "m-trig-swap", B("That is cos A.", "সেয়া cos A।"))], "fill": [F(o, a), F(h, o), F(a, o)], "why": B("Sin is opposite over hypotenuse.", "Sin = বিপৰীত ÷ অতিভুজ।")}, [(3, 4, 5), (5, 12, 13), (8, 15, 17)])
    add("tri", "g-tri", lambda b, h: {"q": B(f"A triangle has base {b} cm and height {h} cm. Its area is", f"ত্ৰিভুজৰ ভূমি {b} ছেমি, উচ্চতা {h} ছেমি। কালি"), "right": b * h // 2, "wrong": [(b * h, "m-tri-area", B("Triangle area is half of base × height.", "ত্ৰিভুজৰ কালি ভূমি × উচ্চতাৰ আধা।"))], "fill": [b + h, 2 * (b + h), b * h // 4], "unit": " sq cm", "why": B("$\\frac{1}{2} \\times$ base $\\times$ height.", "$\\frac{1}{2} \\times$ ভূমি $\\times$ উচ্চতা।")}, [(12, 8), (10, 6), (14, 10)])
    add("circle", "g-circle", lambda d: {"q": B(f"Taking $\\pi = \\frac{{22}}{{7}}$, a circle of diameter {d} cm has circumference", f"$\\pi = \\frac{{22}}{{7}}$ ধৰিলে {d} ছেমি ব্যাসৰ বৃত্তৰ পৰিধি"), "right": 22 * d // 7, "wrong": [(44 * d // 7, "m-radius-dia", B("The formula $2\\pi r$ uses the radius, half the diameter.", "$2\\pi r$ত ব্যাসাৰ্ধ লাগে, ব্যাসৰ আধা।"))], "fill": [11 * d // 7, 22 * d // 7 + 8, d * d], "unit": " cm", "why": B("Circumference is $\\pi d$.", "পৰিধি $\\pi d$।")}, [(14,), (28,), (21,)])
    add("solid", "g-solid", lambda a: {"q": B(f"A cube has edge {a} cm. Its volume is", f"ঘনকৰ বাহু {a} ছেমি। আয়তন"), "right": a ** 3, "wrong": [(6 * a * a, "m-area-volume", B("That is the surface area.", "সেয়া পৃষ্ঠকালি।"))], "fill": [a * a, 3 * a, 12 * a], "unit": " cu cm", "why": B("Volume is edge cubed.", "আয়তন = বাহুৰ ঘন।")}, [(4,), (5,), (7,)])
    return P


def write(path, data):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main():
    lessons = apply([l1(), l2(), l3(), l4(), l5(), l6(), l7(), l8(), l9(), l10(), l11(), l12(), l13(), l14(), l15(), l16()])
    by_no = {L["no"]: L for L in lessons}
    for L in lessons:
        write(f"content/lessons/{L['id']}.json", {
            "id": L["id"], "course": COURSE, "no": L["no"], "version": 1, "eyebrow": B("Mathematics", "গণিত"),
            "king": L["title"], "reign": L["reign"], "portrait": f"math/{TOPICS[L['no'] - 1][0]}.webp",
            "sources": [SOURCE], "review_notes": REVIEW, "map": {"box": [89.5, 24, 96.5, 28.2], "show": []},
            "units": L["units"], "test": L["test"],
        })
    kings = []
    for n, (slug, title, reign, tier, _) in enumerate(TOPICS, 1):
        k = {"n": n, "id": f"math-{slug}", "name": title, "reign": reign, "face": f"math/{slug}.webp", "tier": tier}
        if n in by_no:
            k["lesson"] = by_no[n]["id"]
        kings.append(k)
    write(f"content/courses/{COURSE}.json", {
        "id": COURSE, "order": 0, "title": B("Mathematics", "গণিত"),
        "eyebrow": B("Learn by doing", "কৰি শিকা"),
        "subtitle": B("Find your weak points, fix them and build up", "দুৰ্বলতা বিচাৰি উলিয়াই ঠিক কৰা আৰু আগবাঢ়া"),
        "tabs": ["lessons", "skills", "profile"], "bank": f"content/questions/{COURSE}.json", "skills": f"content/skills/{COURSE}.json",
        "kings": kings, "eras": [{"id": f"math-{e}", "title": t, "from": a, "to": b} for e, t, a, b in ERAS],
        "eraWord": B("section", "খণ্ড"),
    })
    write(f"content/questions/{COURSE}.json", {"questions": []})
    steps = {}
    for L in lessons:
        for u in L["units"] + [L["test"]]:
            for s in u["steps"]:
                for skill in {s.get("skill")} | {p.get("skill") for p in s.get("parts", [])}:
                    if skill and skill in SKILLS and s.get("skill") == skill:
                        steps.setdefault(skill, []).append({"l": L["id"], "id": s["id"]})
    write(f"content/skills/{COURSE}.json", {
        "topics": [{"id": slug, "t": title} for slug, title, *_ in TOPICS],
        "skills": [{"id": i, "topic": v[0], "t": v[1], "pre": v[2], "steps": steps.get(i, [])} for i, v in SKILLS.items()],
        "misconceptions": {k: {"skill": v[0], "t": v[1]} for k, v in MISCONCEPTIONS.items()},
        "probes": probes(),
    })
    print(f"math course: {len(lessons)} lessons, {sum(len(v) for v in steps.values())} skill-linked exercises, {len(probes())} probes")


if __name__ == "__main__":
    main()
