#!/usr/bin/env python3
"""Lesson 29: How a bill becomes law. Run from the repository root."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from constitution_pilot import *  # noqa: E402,F403

LS, RS = B("Lok Sabha", "লোকসভা"), B("Rajya Sabha", "ৰাজ্যসভা")
TRUE_Q = B("One word is wrong. Tap it.", "এটা শব্দ ভুল। সেইটো টিপা।")

mission = {"label": B("Bill tracker 29", "বিধেয়ক অনুসৰণ ২৯"), "title": B("Track a bill to the end", "বিধেয়ক শেষলৈকে অনুসৰণ কৰা"),
           "hook": B("Every law in India began as a bill. Follow one through both Houses, past a deadlock and onto the President's desk, and see which bills die on the way.",
                     "ভাৰতৰ প্ৰতিখন আইন আৰম্ভ হয় বিধেয়ক হিচাপে। দুয়োখন সদন, অচলাৱস্থা আৰু ৰাষ্ট্ৰপতিৰ টেবুললৈকে এখন বিধেয়ক অনুসৰণ কৰা, আৰু কোনখন বাটতে শেষ হয় চোৱা।")}

sources = [{"title": "The Constitution of India, as on 10 September 2026, Articles 79, 100, 107 to 111, 117, 118 and 368", "url": "https://www.legislative.gov.in/static/uploads/2025/07/95ef471035ee0b5e4e5b1cac3d3584c1.pdf", "local_source": "Constitution sources/constitution-of-india-2026-en.pdf", "used_for": "All procedure in this lesson. Bill examples are hypothetical teaching scenarios."}]

u1 = unit("u1", "walk", B("Both Houses must agree", "দুয়োখন সদনৰ সন্মতি"),
    B("Find the basic rule every ordinary bill follows.", "প্ৰতিখন সাধাৰণ বিধেয়কে মানি চলা মূল নিয়ম বিচাৰি উলিওৱা।"),
    B("Finding recorded: an ordinary bill can start in either House, and both must agree.", "প্ৰমাণ লিখা হ'ল: সাধাৰণ বিধেয়ক যিকোনো সদনত আৰম্ভ হ'ব পাৰে, দুয়োখনে একমত হ'ব লাগে।"),
    [B("A bill may originate in either House", "বিধেয়ক যিকোনো সদনত আৰম্ভ হ'ব পাৰে"), B("Exceptions are Money Bills and other financial Bills", "ব্যতিক্ৰম ধন বিধেয়ক আৰু আন বিত্তীয় বিধেয়ক"),
     B("Both Houses must agree, including on amendments", "সংশোধনীসহ দুয়োখন সদন একমত হ'ব লাগিব"), B("Parliament is the President and the two Houses", "ৰাষ্ট্ৰপতি আৰু দুয়োখন সদন মিলি সংসদ")],
    [story(B("Two Houses, one text", "দুখন সদন, এটা পাঠ"),
           [B("[[art-79|Parliament]] is the President and two Houses. Under [[art-107]], a [[bill|bill]] may begin in <mark>either House</mark>.", "ৰাষ্ট্ৰপতি আৰু দুখন সদন মিলি [[art-79|সংসদ]]। [[art-107]]-ৰ অধীনত [[bill|বিধেয়ক]] <mark>যিকোনো সদনত</mark> আৰম্ভ হ'ব পাৰে।"),
            B("The exceptions are Money Bills and other financial Bills.", "ব্যতিক্ৰম হ'ল ধন বিধেয়ক আৰু আন বিত্তীয় বিধেয়ক।")], art="houses"),
     story(B("Agreement means the same words", "সন্মতি মানে একে শব্দ"),
           [B("A bill passes only if <mark>both Houses agree</mark>, without amendment or with amendments both accept.", "<mark>দুয়োখন সদন একমত</mark> হ'লেহে বিধেয়ক গৃহীত হয়: সংশোধনী নোহোৱাকৈ বা দুয়োখনে মানি লোৱা সংশোধনীৰে।"),
            B("So a change made in one House must go back to the other.", "সেয়ে এখন সদনৰ সলনি আনখন সদনলৈ উভতি যাব লাগিব।")], art="scroll"),
     tf(B("Every bill must begin in the Lok Sabha.", "প্ৰতিখন বিধেয়ক লোকসভাত আৰম্ভ হ'ব লাগিব।"), False, B("Under Article 107(1), a bill may begin in either House, apart from Money and financial Bills.", "অনুচ্ছেদ ১০৭(১) অনুসৰি ধন আৰু বিত্তীয় বিধেয়কৰ বাহিৰে বিধেয়ক যিকোনো সদনত আৰম্ভ হ'ব পাৰে।")),
     order(B("Scenario: put an ordinary bill's route in order.", "কাল্পনিক উদাহৰণ: সাধাৰণ বিধেয়কৰ বাট ক্ৰমত সজোৱা।"),
           [B("Passed by the first House", "প্ৰথম সদনত গৃহীত"), B("Sent to the other House", "আনখন সদনলৈ প্ৰেৰিত"), B("Agreed by the other House", "আনখন সদনত সন্মত"), B("Presented to the President", "ৰাষ্ট্ৰপতিৰ ওচৰত উপস্থাপন")],
           B("Article 111 follows once both Houses have passed the bill.", "দুয়োখন সদনে গ্ৰহণ কৰাৰ পিছত অনুচ্ছেদ ১১১ প্ৰযোজ্য হয়।")),
     inline(B("Parliament consists of the President and", "সংসদত আছে ৰাষ্ট্ৰপতি আৰু"), B(".", "।"), [B("the Lok Sabha alone", "কেৱল লোকসভা"), B("the two Houses", "দুয়োখন সদন"), B("the Cabinet", "কেবিনেট")], 1, B("Article 79 names the President and the two Houses.", "অনুচ্ছেদ ৭৯-এ ৰাষ্ট্ৰপতি আৰু দুয়োখন সদনৰ নাম লৈছে।")),
     odd(B("Which cannot begin in the Rajya Sabha?", "কোনখন ৰাজ্যসভাত আৰম্ভ হ'ব নোৱাৰে?"), [B("An ordinary Bill", "সাধাৰণ বিধেয়ক"), B("A Money Bill", "ধন বিধেয়ক"), B("A Constitution Amendment Bill", "সংবিধান সংশোধনী বিধেয়ক")], 1, B("Article 109(1) bars Money Bills from the Rajya Sabha. Article 368 allows either House for amendments.", "অনুচ্ছেদ ১০৯(১)-এ ধন বিধেয়ক ৰাজ্যসভাত নিষেধ কৰে। সংশোধনীৰ বাবে অনুচ্ছেদ ৩৬৮-এ যিকোনো সদনলৈ অনুমতি দিয়ে।")),
     spot(TRUE_Q, "A bill passes when one House agrees.", "এখন সদন একমত হ'লে বিধেয়ক গৃহীত হয়।", 4, 0, B("→ both Houses", "→ দুয়োখন"), B("one → both", "এখন → দুয়োখন"), B("Article 107(2) requires both Houses.", "অনুচ্ছেদ ১০৭(২)-এ দুয়োখন সদন লাগে।"))])

u2 = unit("u2", "scroll", B("Which bill is this?", "এইখন কি বিধেয়ক?"),
    B("Sort bills by type before tracking them.", "অনুসৰণৰ আগতে বিধেয়কৰ প্ৰকাৰ বাছি উলিওৱা।"),
    B("Finding recorded: the type decides the route, and the Speaker decides what is a Money Bill.", "প্ৰমাণ লিখা হ'ল: প্ৰকাৰে বাট ঠিক কৰে, আৰু ধন বিধেয়ক কি অধ্যক্ষই ঠিক কৰে।"),
    [B("A Money Bill contains only the matters listed in Article 110(1)", "ধন বিধেয়কত কেৱল অনুচ্ছেদ ১১০(১)-ৰ বিষয় থাকে"), B("The Speaker's decision on a Money Bill is final", "ধন বিধেয়ক সম্পৰ্কে অধ্যক্ষৰ সিদ্ধান্ত চূড়ান্ত"),
     B("A fine in a bill does not make it a Money Bill", "জৰিমনা থকাৰ বাবে বিধেয়ক ধন বিধেয়ক নহয়"), B("Financial Bills need the President's recommendation", "বিত্তীয় বিধেয়কৰ বাবে ৰাষ্ট্ৰপতিৰ পৰামৰ্শ লাগে")],
    [story(B("Four kinds of bill", "চাৰি প্ৰকাৰৰ বিধেয়ক"),
           [B("Ordinary Bills follow [[art-107]]. Money Bills follow [[art-109]]. Other financial Bills follow Article 117. Amendment Bills follow [[art-368]].", "সাধাৰণ বিধেয়কে [[art-107]], ধন বিধেয়কে [[art-109]], আন বিত্তীয় বিধেয়কে অনুচ্ছেদ ১১৭ আৰু সংশোধনী বিধেয়কে [[art-368]] মানে।"),
            B("The label matters because it decides the route.", "নামটো গুৰুত্বপূৰ্ণ, কাৰণ ই বাট ঠিক কৰে।")], art="scroll"),
     story(B("The Speaker's certificate", "অধ্যক্ষৰ প্ৰমাণপত্ৰ"),
           [B("[[art-110]] says a Money Bill contains <mark>only</mark> listed matters, such as tax and the Consolidated Fund.", "[[art-110]] অনুসৰি ধন বিধেয়কত <mark>কেৱল</mark> তালিকাভুক্ত বিষয় থাকে, যেনে কৰ আৰু একত্ৰীকৃত নিধি।"),
            B("If there is a dispute, the <mark>Speaker's decision is final</mark>. The Speaker signs a certificate on the bill.", "বিবাদ হ'লে <mark>অধ্যক্ষৰ সিদ্ধান্ত চূড়ান্ত</mark>। অধ্যক্ষে বিধেয়কত প্ৰমাণপত্ৰ স্বাক্ষৰ কৰে।")], art="seal"),
     match([(B("Article 110", "অনুচ্ছেদ ১১০"), B("Defines a Money Bill", "ধন বিধেয়কৰ সংজ্ঞা")), (B("Article 109", "অনুচ্ছেদ ১০৯"), B("Money Bill procedure", "ধন বিধেয়কৰ প্ৰক্ৰিয়া")), (B("Article 117", "অনুচ্ছেদ ১১৭"), B("Financial Bills", "বিত্তীয় বিধেয়ক")), (B("Article 368", "অনুচ্ছেদ ৩৬৮"), B("Amendment Bills", "সংশোধনী বিধেয়ক"))],
           B("Each type has its own article.", "প্ৰতিটো প্ৰকাৰৰ নিজা অনুচ্ছেদ আছে।")),
     inline(B("Whether a bill is a Money Bill is finally decided by the", "বিধেয়ক ধন বিধেয়ক নে নহয়, চূড়ান্তভাৱে ঠিক কৰে"), B(".", "-এ।"), [B("President", "ৰাষ্ট্ৰপতি"), B("Speaker", "অধ্যক্ষ"), B("Finance Minister", "বিত্ত মন্ত্ৰী"), B("Chairman", "সভাপতি")], 1, B("Article 110(3) makes the Speaker's decision final.", "অনুচ্ছেদ ১১০(৩)-এ অধ্যক্ষৰ সিদ্ধান্ত চূড়ান্ত কৰিছে।")),
     tf(B("Scenario: a bill on a local issue includes a small fine. That alone makes it a Money Bill.", "কাল্পনিক উদাহৰণ: স্থানীয় বিষয়ৰ বিধেয়কত সৰু জৰিমনা আছে। সেয়ে ই ধন বিধেয়ক হ'ল।"), False, B("Article 110(2): fines or penalties alone do not make a Money Bill.", "অনুচ্ছেদ ১১০(২): কেৱল জৰিমনা বা দণ্ডৰ বাবে ধন বিধেয়ক নহয়।")),
     odd(B("Which is not a Money Bill matter in Article 110(1)?", "অনুচ্ছেদ ১১০(১)-ৰ ধন বিধেয়কৰ বিষয় কোনটো নহয়?"), [B("Imposing a tax", "কৰ আৰোপ"), B("Withdrawals from the Consolidated Fund", "একত্ৰীকৃত নিধিৰ পৰা উলিওৱা ধন"), B("Forming a new State", "নতুন ৰাজ্য গঠন")], 2, B("Forming a State falls under Article 3, not Article 110.", "ৰাজ্য গঠন অনুচ্ছেদ ৩-ৰ বিষয়, অনুচ্ছেদ ১১০-ৰ নহয়।")),
     scramble(B("Unscramble the officer who certifies.", "প্ৰমাণপত্ৰ দিয়া বিষয়াজন সজাই লিখা।"), "SPEAKER", ["অ", "ধ্য", "ক্ষ"], B("SPEAKER", "অধ্যক্ষ"), B("The Speaker's certificate is endorsed on every Money Bill.", "প্ৰতিখন ধন বিধেয়কত অধ্যক্ষৰ প্ৰমাণপত্ৰ থাকে।"))])

u3 = unit("u3", "moon", B("The fourteen-day clock", "চৈধ্য দিনৰ ঘড়ী"),
    B("Find out how far the Rajya Sabha can go on a Money Bill.", "ধন বিধেয়কত ৰাজ্যসভাই কিমান দূৰ যাব পাৰে, বিচাৰি উলিওৱা।"),
    B("Finding recorded: the Rajya Sabha recommends within 14 days; the Lok Sabha decides.", "প্ৰমাণ লিখা হ'ল: ৰাজ্যসভাই ১৪ দিনৰ ভিতৰত পৰামৰ্শ দিয়ে; লোকসভাই সিদ্ধান্ত লয়।"),
    [B("A Money Bill cannot be introduced in the Rajya Sabha", "ধন বিধেয়ক ৰাজ্যসভাত উত্থাপন কৰিব নোৱাৰি"), B("The Rajya Sabha has 14 days to return it", "ৰাজ্যসভাৰ হাতত ঘূৰাই দিবলৈ ১৪ দিন"),
     B("The Lok Sabha may accept or reject its recommendations", "লোকসভাই পৰামৰ্শ গ্ৰহণ বা নাকচ কৰিব পাৰে"), B("If not returned in 14 days, the bill is deemed passed", "১৪ দিনত নুঘূৰালে গৃহীত বুলি গণ্য হয়")],
    [story(B("Recommend, not refuse", "নাকচ নহয়, পৰামৰ্শ"),
           [B("Under [[art-109]], a Money Bill starts in the <mark>Lok Sabha</mark>. It then goes to the Rajya Sabha for recommendations.", "[[art-109]] অনুসৰি ধন বিধেয়ক <mark>লোকসভাত</mark> আৰম্ভ হয়। তাৰ পিছত পৰামৰ্শৰ বাবে ৰাজ্যসভালৈ যায়।"),
            B("The Rajya Sabha must return it within <mark>14 days</mark>.", "ৰাজ্যসভাই <mark>১৪ দিনৰ</mark> ভিতৰত ঘূৰাই দিব লাগিব।")], art="calendar"),
     story(B("The clock runs out", "সময় শেষ"),
           [B("The Lok Sabha may accept or reject any recommendation. Either way the bill is deemed passed by both Houses.", "লোকসভাই যিকোনো পৰামৰ্শ গ্ৰহণ বা নাকচ কৰিব পাৰে। দুয়োটা ক্ষেত্ৰতে বিধেয়ক দুয়োখন সদনত গৃহীত বুলি গণ্য হয়।"),
            B("If the Rajya Sabha does not return it in time, it is <mark>deemed passed</mark> as the Lok Sabha passed it.", "সময়মতে নুঘূৰালে লোকসভাই গ্ৰহণ কৰা ৰূপতে ই <mark>গৃহীত বুলি গণ্য</mark> হয়।")], art="houses"),
     tf(B("The Rajya Sabha can block a Money Bill for six months.", "ৰাজ্যসভাই ধন বিধেয়ক ছমাহ আটকাই ৰাখিব পাৰে।"), False, B("It has 14 days. After that the bill is deemed passed.", "ইয়াৰ হাতত ১৪ দিন। তাৰ পিছত বিধেয়ক গৃহীত বুলি গণ্য হয়।")),
     order(B("Put the Money Bill route in order.", "ধন বিধেয়কৰ বাট ক্ৰমত সজোৱা।"),
           [B("Introduced in the Lok Sabha", "লোকসভাত উত্থাপন"), B("Passed by the Lok Sabha", "লোকসভাত গৃহীত"), B("Sent to the Rajya Sabha", "ৰাজ্যসভালৈ প্ৰেৰণ"), B("Back to the Lok Sabha within 14 days", "১৪ দিনৰ ভিতৰত লোকসভালৈ ঘূৰি অহা")],
           B("Article 109 sets this route.", "অনুচ্ছেদ ১০৯-এ এই বাট ঠিক কৰে।")),
     inline(B("The Rajya Sabha must return a Money Bill within", "ৰাজ্যসভাই ধন বিধেয়ক ঘূৰাই দিব লাগিব"), B("days.", "দিনৰ ভিতৰত।"), [B("7", "৭"), B("14", "১৪"), B("30", "৩০"), B("180", "১৮০")], 1, B("Article 109(2) gives 14 days.", "অনুচ্ছেদ ১০৯(২)-এ ১৪ দিন দিছে।")),
     tf(B("The Lok Sabha must accept the Rajya Sabha's recommendations on a Money Bill.", "ধন বিধেয়কত ৰাজ্যসভাৰ পৰামৰ্শ লোকসভাই মানিবই লাগিব।"), False, B("It may accept or reject all or any of them.", "ই সকলো বা যিকোনো পৰামৰ্শ গ্ৰহণ বা নাকচ কৰিব পাৰে।")),
     spot(TRUE_Q, "A Money Bill is first introduced in the Rajya Sabha.", "ধন বিধেয়ক প্ৰথমে ৰাজ্যসভাত উত্থাপন কৰা হয়।", 8, 3, B("→ Lok Sabha", "→ লোকসভা"), B("Rajya → Lok", "ৰাজ্যসভা → লোকসভা"), B("Article 109(1) bars introduction in the Rajya Sabha.", "অনুচ্ছেদ ১০৯(১)-এ ৰাজ্যসভাত উত্থাপন নিষেধ কৰে।"))])

u4 = unit("u4", "hands", B("When the Houses disagree", "সদন একমত নহ'লে"),
    B("Find the way out of a deadlock.", "অচলাৱস্থাৰ পৰা ওলোৱাৰ বাট বিচাৰা।"),
    B("Finding recorded: a joint sitting settles ordinary deadlocks, with the Speaker presiding.", "প্ৰমাণ লিখা হ'ল: যুটীয়া বৈঠকে সাধাৰণ অচলাৱস্থা সমাধান কৰে, অধ্যক্ষই সভাপতিত্ব কৰে।"),
    [B("Article 108 provides for a joint sitting", "অনুচ্ছেদ ১০৮-এ যুটীয়া বৈঠকৰ ব্যৱস্থা কৰে"), B("Three triggers: rejection, final disagreement, or six months", "তিনিটা কাৰণ: নাকচ, চূড়ান্ত মতভেদ বা ছমাহ"),
     B("A joint sitting is not available for a Money Bill", "ধন বিধেয়কৰ বাবে যুটীয়া বৈঠক নাই"), B("The Speaker presides at a joint sitting", "যুটীয়া বৈঠকত অধ্যক্ষই সভাপতিত্ব কৰে")],
    [story(B("Three ways to deadlock", "অচলাৱস্থাৰ তিনিটা বাট"),
           [B("[[art-108]] applies if the other House <mark>rejects</mark> a bill, the Houses <mark>finally disagree</mark> on amendments, or <mark>six months</mark> pass without it being passed.", "[[art-108]] প্ৰযোজ্য হয় যদি আনখন সদনে <mark>নাকচ</mark> কৰে, সংশোধনীত <mark>চূড়ান্ত মতভেদ</mark> হয়, বা গ্ৰহণ নকৰাকৈ <mark>ছমাহ</mark> পাৰ হয়।"),
            B("The President may then summon a joint sitting.", "তেতিয়া ৰাষ্ট্ৰপতিয়ে যুটীয়া বৈঠক আহ্বান কৰিব পাৰে।")], art="houses"),
     story(B("One room, one vote", "এটা কোঠা, এটা ভোট"),
           [B("At a joint sitting the <mark>Speaker</mark> presides, under Article 118(4).", "অনুচ্ছেদ ১১৮(৪) অনুসৰি যুটীয়া বৈঠকত <mark>অধ্যক্ষই</mark> সভাপতিত্ব কৰে।"),
            B("Article 108 does not apply to a Money Bill. An Amendment Bill must pass in each House under Article 368.", "ধন বিধেয়কত অনুচ্ছেদ ১০৮ প্ৰযোজ্য নহয়। সংশোধনী বিধেয়ক অনুচ্ছেদ ৩৬৮ অনুসৰি প্ৰতিখন সদনত গৃহীত হ'ব লাগিব।")], art="court"),
     match([(B("Bill rejected", "বিধেয়ক নাকচ"), B("Joint sitting possible", "যুটীয়া বৈঠক সম্ভৱ")), (B("Money Bill stalled", "ধন বিধেয়ক আটক"), B("Deemed passed after 14 days", "১৪ দিনৰ পিছত গৃহীত বুলি গণ্য")), (B("Amendment Bill", "সংশোধনী বিধেয়ক"), B("Must pass in each House", "প্ৰতিখন সদনত গৃহীত হ'ব লাগিব"))],
           B("Different bills escape deadlock differently.", "বেলেগ বিধেয়কৰ বাট বেলেগ।")),
     inline(B("At a joint sitting, the chair is taken by the", "যুটীয়া বৈঠকত সভাপতিত্ব কৰে"), B(".", "-এ।"), [B("Chairman", "সভাপতি"), B("Speaker", "অধ্যক্ষ"), B("President", "ৰাষ্ট্ৰপতি"), B("Prime Minister", "প্ৰধান মন্ত্ৰী")], 1, B("Article 118(4) names the Speaker.", "অনুচ্ছেদ ১১৮(৪)-এ অধ্যক্ষৰ নাম লৈছে।")),
     tf(B("A joint sitting can resolve a deadlock on a Money Bill.", "যুটীয়া বৈঠকে ধন বিধেয়কৰ অচলাৱস্থা সমাধান কৰিব পাৰে।"), False, B("The proviso to Article 108(1) excludes Money Bills.", "অনুচ্ছেদ ১০৮(১)-ৰ ব্যতিক্ৰমে ধন বিধেয়ক বাদ দিয়ে।")),
     odd(B("Which is not a trigger for a joint sitting?", "যুটীয়া বৈঠকৰ কাৰণ কোনটো নহয়?"), [B("The other House rejects the bill", "আনখন সদনে নাকচ কৰে"), B("Six months pass without passage", "গ্ৰহণ নোহোৱাকৈ ছমাহ পাৰ হয়"), B("The Speaker asks for one", "অধ্যক্ষই বিচাৰে"), B("Final disagreement on amendments", "সংশোধনীত চূড়ান্ত মতভেদ")], 2, B("The President notifies the intention, on the three grounds in Article 108(1).", "অনুচ্ছেদ ১০৮(১)-ৰ তিনিটা কাৰণত ৰাষ্ট্ৰপতিয়ে অভিপ্ৰায় জনায়।")),
     spot(TRUE_Q, "A joint sitting needs seven months without passage.", "যুটীয়া বৈঠকৰ বাবে গ্ৰহণ নোহোৱাকৈ সাত মাহ লাগে।", 4, 5, B("→ six", "→ ছয়"), B("seven → six", "সাত → ছয়"), B("Article 108(1)(c) says six months.", "অনুচ্ছেদ ১০৮(১)(গ)-ত ছমাহ বুলি কোৱা আছে।"))])

u5 = unit("u5", "crown", B("The President's desk", "ৰাষ্ট্ৰপতিৰ টেবুল"),
    B("Find the President's three options.", "ৰাষ্ট্ৰপতিৰ তিনিটা বাট বিচাৰি উলিওৱা।"),
    B("Finding recorded: assent, withhold or return, but a re-passed bill cannot be refused.", "প্ৰমাণ লিখা হ'ল: সন্মতি, স্থগিত বা ঘূৰাই দিয়া, কিন্তু পুনৰ গৃহীত বিধেয়ক নাকচ কৰিব নোৱাৰি।"),
    [B("Article 111: the President assents or withholds assent", "অনুচ্ছেদ ১১১: ৰাষ্ট্ৰপতিয়ে সন্মতি দিয়ে বা স্থগিত ৰাখে"), B("The President may return a bill that is not a Money Bill", "ধন বিধেয়কৰ বাহিৰে আনখন ঘূৰাই দিব পাৰে"),
     B("If passed again, assent shall not be withheld", "পুনৰ গৃহীত হ'লে সন্মতি স্থগিত ৰাখিব নোৱাৰি"), B("An Amendment Bill must receive assent", "সংশোধনী বিধেয়কত সন্মতি দিবই লাগিব")],
    [story(B("Assent or withhold", "সন্মতি বা স্থগিত"),
           [B("Under [[art-111]], a passed bill goes to the President, who <mark>assents</mark> or <mark>withholds assent</mark>.", "[[art-111]] অনুসৰি গৃহীত বিধেয়ক ৰাষ্ট্ৰপতিৰ ওচৰলৈ যায়। তেওঁ <mark>সন্মতি দিয়ে</mark> বা <mark>স্থগিত ৰাখে</mark>।"),
            B("The President may also <mark>return</mark> a bill for reconsideration, unless it is a Money Bill.", "ধন বিধেয়কৰ বাহিৰে তেওঁ পুনৰ বিবেচনাৰ বাবে <mark>ঘূৰাই</mark> দিব পাৰে।")], art="seal"),
     story(B("The second time is final", "দ্বিতীয়বাৰ চূড়ান্ত"),
           [B("If the Houses pass the returned bill again, with or without amendment, the President <mark>shall not withhold assent</mark>.", "সংশোধনীসহ বা অবিহনে সদনে পুনৰ গ্ৰহণ কৰিলে ৰাষ্ট্ৰপতিয়ে <mark>সন্মতি স্থগিত ৰাখিব নোৱাৰে</mark>।"),
            B("For an Amendment Bill, Article 368(2) says the President shall give assent.", "সংশোধনী বিধেয়কৰ ক্ষেত্ৰত অনুচ্ছেদ ৩৬৮(২)-এ কয়, ৰাষ্ট্ৰপতিয়ে সন্মতি দিব।")], art="scroll"),
     tf(B("The President can return a Money Bill for reconsideration.", "ৰাষ্ট্ৰপতিয়ে ধন বিধেয়ক পুনৰ বিবেচনাৰ বাবে ঘূৰাই দিব পাৰে।"), False, B("The proviso to Article 111 covers only a bill that is not a Money Bill.", "অনুচ্ছেদ ১১১-ৰ ব্যৱস্থা কেৱল ধন বিধেয়ক নোহোৱা বিধেয়কৰ বাবে।")),
     order(B("Scenario: a returned bill. Put the steps in order.", "কাল্পনিক উদাহৰণ: ঘূৰাই দিয়া বিধেয়ক। ক্ৰমত সজোৱা।"),
           [B("Houses pass the bill", "সদনে বিধেয়ক গ্ৰহণ কৰে"), B("President returns it with a message", "ৰাষ্ট্ৰপতিয়ে বাৰ্তাসহ ঘূৰাই দিয়ে"), B("Houses reconsider and pass it again", "সদনে পুনৰ বিবেচনা কৰি গ্ৰহণ কৰে"), B("President cannot withhold assent", "ৰাষ্ট্ৰপতিয়ে সন্মতি স্থগিত ৰাখিব নোৱাৰে")],
           B("Article 111 allows one return.", "অনুচ্ছেদ ১১১-এ এবাৰ ঘূৰাই দিয়াৰ ব্যৱস্থা কৰে।")),
     match([(B("Ordinary Bill", "সাধাৰণ বিধেয়ক"), B("Assent, withhold or return", "সন্মতি, স্থগিত বা ঘূৰাই দিয়া")), (B("Money Bill", "ধন বিধেয়ক"), B("Assent or withhold", "সন্মতি বা স্থগিত")), (B("Amendment Bill", "সংশোধনী বিধেয়ক"), B("Shall give assent", "সন্মতি দিব লাগিব"))],
           B("The options shrink with the type of bill.", "বিধেয়কৰ প্ৰকাৰ অনুসৰি বাট কমি যায়।")),
     inline(B("Assent to bills is in Article", "বিধেয়কত সন্মতিৰ বিষয়ে আছে অনুচ্ছেদ"), B(".", "-ত।"), [B("72", "৭২"), B("108", "১০৮"), B("111", "১১১"), B("123", "১২৩")], 2, B("Article 111 is Assent to Bills.", "অনুচ্ছেদ ১১১ বিধেয়কত সন্মতি প্ৰদান।")),
     line(B("Place each provision on the line.", "প্ৰতিটো উপবন্ধ ৰেখাত ৰাখা।"), [(107, B("Passing bills", "বিধেয়ক গ্ৰহণ")), (111, B("Assent", "সন্মতি"))],
          [(B("Joint sitting", "যুটীয়া বৈঠক"), 1), (B("Money Bill defined", "ধন বিধেয়কৰ সংজ্ঞা"), 1), (B("Financial Bills", "বিত্তীয় বিধেয়ক"), 2), (B("Ordinances", "অধ্যাদেশ"), 2)],
          B("107 → 108 → 110 → 111 → 117 → 123.", "১০৭ → ১০৮ → ১১০ → ১১১ → ১১৭ → ১২৩।"))])

u6 = unit("u6", "flag", B("Bills that die", "শেষ হোৱা বিধেয়ক"),
    B("Work out which bills survive a dissolution.", "লোকসভা ভংগ হ'লে কোন বিধেয়ক থাকে, উলিওৱা।"),
    B("Finding recorded: prorogation kills nothing; dissolution of the Lok Sabha kills most pending bills.", "প্ৰমাণ লিখা হ'ল: স্থগিতকৰণে একো শেষ নকৰে; লোকসভা ভংগ হ'লে বেছিভাগ বিচাৰাধীন বিধেয়ক শেষ হয়।"),
    [B("Prorogation does not end a pending bill", "স্থগিতকৰণে বিচাৰাধীন বিধেয়ক শেষ নকৰে"), B("A bill pending in the Lok Sabha lapses on dissolution", "লোকসভাত বিচাৰাধীন বিধেয়ক ভংগৰ লগে লগে শেষ হয়"),
     B("A Lok Sabha-passed bill pending in the Rajya Sabha also lapses", "লোকসভাই গ্ৰহণ কৰি ৰাজ্যসভাত থকা বিধেয়কো শেষ হয়"), B("A Rajya Sabha bill not passed by the Lok Sabha survives", "লোকসভাই গ্ৰহণ নকৰা ৰাজ্যসভাৰ বিধেয়ক থাকি যায়")],
    [story(B("The session ends, the bill lives", "অধিৱেশন শেষ, বিধেয়ক জীয়াই"),
           [B("Prorogation ends a session. Under [[art-107]], a pending bill <mark>does not lapse</mark> because of it.", "স্থগিতকৰণে অধিৱেশন শেষ কৰে। [[art-107]] অনুসৰি ইয়াৰ বাবে বিচাৰাধীন বিধেয়ক <mark>শেষ নহয়</mark>।"),
            B("Dissolution is different. It ends the Lok Sabha itself.", "ভংগ বেলেগ কথা। ই লোকসভাকে শেষ কৰে।")], art="calendar"),
     story(B("Who survives dissolution?", "ভংগৰ পিছত কোন থাকে?"),
           [B("A bill pending in the Lok Sabha <mark>lapses</mark>. So does one passed by it and pending in the Rajya Sabha.", "লোকসভাত থকা বিধেয়ক <mark>শেষ</mark> হয়। ই গ্ৰহণ কৰি ৰাজ্যসভাত থকাখনো শেষ হয়।"),
            B("A bill pending in the Rajya Sabha, not passed by the Lok Sabha, <mark>survives</mark>.", "লোকসভাই গ্ৰহণ নকৰা ৰাজ্যসভাৰ বিধেয়ক <mark>থাকি যায়</mark>।"),
            B("A joint sitting already notified can still go ahead.", "ঘোষিত যুটীয়া বৈঠক তথাপি হ'ব পাৰে।")], art="houses"),
     tf(B("A bill pending in Parliament lapses when the Houses are prorogued.", "সদন স্থগিত হ'লে বিচাৰাধীন বিধেয়ক শেষ হয়।"), False, B("Article 107(3) says it shall not lapse.", "অনুচ্ছেদ ১০৭(৩)-এ কয়, ই শেষ নহয়।")),
     match([(B("Pending in the Lok Sabha", "লোকসভাত বিচাৰাধীন"), B("Lapses", "শেষ হয়")), (B("Passed by Lok Sabha, pending in Rajya Sabha", "লোকসভাত গৃহীত, ৰাজ্যসভাত বিচাৰাধীন"), B("Also lapses", "সেইখনো শেষ হয়")), (B("Pending in Rajya Sabha, not passed by Lok Sabha", "ৰাজ্যসভাত বিচাৰাধীন, লোকসভাত অগৃহীত"), B("Survives", "থাকি যায়"))],
           B("Article 107(4) and (5) set these outcomes.", "অনুচ্ছেদ ১০৭(৪) আৰু (৫)-এ এই ফল ঠিক কৰে।")),
     inline(B("Scenario: the Lok Sabha is dissolved. A bill it passed is in the Rajya Sabha. The bill", "কাল্পনিক উদাহৰণ: লোকসভা ভংগ হ'ল। ই গ্ৰহণ কৰা বিধেয়ক ৰাজ্যসভাত আছে। বিধেয়কখন"), B(".", "।"), [B("survives", "থাকি যায়"), B("lapses", "শেষ হয়"), B("becomes law", "আইন হয়")], 1, B("Article 107(5) says it lapses, subject to Article 108.", "অনুচ্ছেদ ১০৮-ৰ অধীনত অনুচ্ছেদ ১০৭(৫)-এ কয়, ই শেষ হয়।")),
     odd(B("Which ends a Lok Sabha itself?", "কিহে লোকসভাকে শেষ কৰে?"), [B("Prorogation", "স্থগিতকৰণ"), B("Adjournment", "মুলতবী"), B("Dissolution", "ভংগ")], 2, B("Dissolution ends the House; the others do not.", "ভংগই সদন শেষ কৰে; আন দুটাই নকৰে।")),
     spot(TRUE_Q, "Dissolution of the Rajya Sabha ends pending bills.", "ৰাজ্যসভা ভংগ হ'লে বিচাৰাধীন বিধেয়ক শেষ হয়।", 3, 0, B("→ Lok Sabha", "→ লোকসভা"), B("Rajya → Lok", "ৰাজ্যসভা → লোকসভা"), B("Article 107 speaks of dissolution of the House of the People.", "অনুচ্ছেদ ১০৭-এ লোকসভা ভংগৰ কথা কৈছে।"))])

test = {"id": "test", "title": B("Lesson test", "পাঠৰ পৰীক্ষা"),
        "mission": {"objective": B("Track any bill from start to finish.", "যিকোনো বিধেয়ক আৰম্ভণিৰ পৰা শেষলৈ অনুসৰণ কৰা।"), "result": B("Tracker complete: you know each route and each dead end.", "অনুসৰণ সম্পূৰ্ণ: প্ৰতিটো বাট আৰু বন্ধ বাট তুমি জানা।")}, "learned": [],
        "steps": [
            match([(B("14 days", "১৪ দিন"), B("Rajya Sabha on a Money Bill", "ধন বিধেয়কত ৰাজ্যসভা")), (B("Six months", "ছমাহ"), B("Joint sitting trigger", "যুটীয়া বৈঠকৰ কাৰণ")), (B("Speaker", "অধ্যক্ষ"), B("Certifies a Money Bill", "ধন বিধেয়ক প্ৰমাণিত কৰে"))], B("Three numbers and names to keep apart.", "পৃথক কৰি মনত ৰাখিবলগীয়া।")),
            tf(B("A Constitution Amendment Bill may be introduced in either House.", "সংবিধান সংশোধনী বিধেয়ক যিকোনো সদনত উত্থাপন কৰিব পাৰি।"), True, B("Article 368(2) says either House.", "অনুচ্ছেদ ৩৬৮(২)-এ যিকোনো সদন বুলি কৈছে।")),
            inline(B("A joint sitting is under Article", "যুটীয়া বৈঠক আছে অনুচ্ছেদ"), B(".", "-ত।"), [B("107", "১০৭"), B("108", "১০৮"), B("110", "১১০"), B("111", "১১১")], 1, B("Article 108 is the joint sitting.", "অনুচ্ছেদ ১০৮ যুটীয়া বৈঠক।")),
            mcq(B("Consider: (i) A Money Bill cannot start in the Rajya Sabha. (ii) The Speaker's decision on a Money Bill is final. (iii) The President may return a Money Bill. Which are correct?", "বিবেচনা কৰা: (i) ধন বিধেয়ক ৰাজ্যসভাত আৰম্ভ হ'ব নোৱাৰে। (ii) ধন বিধেয়কত অধ্যক্ষৰ সিদ্ধান্ত চূড়ান্ত। (iii) ৰাষ্ট্ৰপতিয়ে ধন বিধেয়ক ঘূৰাই দিব পাৰে। কোনবোৰ শুদ্ধ?"),
                [B("(i) only", "কেৱল (i)"), B("(i) and (ii) only", "কেৱল (i) আৰু (ii)"), B("(ii) and (iii) only", "কেৱল (ii) আৰু (iii)"), B("(i), (ii) and (iii)", "(i), (ii) আৰু (iii)")], 1, B("Statement (iii) is wrong: Article 111 excludes Money Bills from return.", "(iii) ভুল: অনুচ্ছেদ ১১১-এ ধন বিধেয়ক ঘূৰাই দিয়া বাদ দিছে।")),
            tf(B("A re-passed bill can still be refused by the President.", "পুনৰ গৃহীত বিধেয়ক ৰাষ্ট্ৰপতিয়ে তথাপি নাকচ কৰিব পাৰে।"), False, B("Article 111: assent shall not be withheld.", "অনুচ্ছেদ ১১১: সন্মতি স্থগিত ৰাখিব নোৱাৰি।")),
            order(B("Put the Money Bill's path in order.", "ধন বিধেয়কৰ বাট ক্ৰমত সজোৱা।"), [B("Speaker's certificate possible", "অধ্যক্ষৰ প্ৰমাণপত্ৰ"), B("Rajya Sabha's 14 days", "ৰাজ্যসভাৰ ১৪ দিন"), B("Deemed passed by both Houses", "দুয়োখন সদনত গৃহীত বুলি গণ্য"), B("President's assent", "ৰাষ্ট্ৰপতিৰ সন্মতি")], B("The certificate is endorsed when the bill goes to the Rajya Sabha.", "বিধেয়ক ৰাজ্যসভালৈ যাওঁতে প্ৰমাণপত্ৰ থাকে।")),
        ]}

write(29, "con-29-how-a-bill-becomes-law", B("How a bill becomes law", "বিধেয়ক কেনেকৈ আইন হয়"), B("Articles 107–111", "অনুচ্ছেদ ১০৭–১১১"), B("The Constitution of India · Parliament", "ভাৰতৰ সংবিধান · সংসদ"), mission, sources, [u1, u2, u3, u4, u5, u6], test)
