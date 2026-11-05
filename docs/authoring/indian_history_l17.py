#!/usr/bin/env python3
"""Lesson 17: Marathas and Mysore."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "shivaji": ("person", "Shivaji|শিৱাজী", "Founder of the Maratha kingdom, crowned in 1674|মাৰাঠা ৰাজ্যৰ প্ৰতিষ্ঠাপক, ১৬৭৪ত অভিষিক্ত"),
 "ahmad-shah-durrani": ("person", "Ahmad Shah Durrani|আহমদ শ্বাহ দুৰানী", "Afghan ruler who won at Panipat in 1761|১৭৬১ত পানিপথত জয়ী আফগান শাসক"),
 "hyder-ali": ("person", "Hyder Ali|হায়দৰ আলী", "De facto ruler of Mysore from 1761|১৭৬১ৰ পৰা মহীশূৰৰ প্ৰকৃত শাসক"),
 "tipu-sultan": ("person", "Tipu Sultan|টিপু ছুলতান", "Ruler of Mysore, known as Sher-e-Mysore|মহীশূৰৰ শাসক, শ্বেৰ-ই-মহীশূৰ নামে খ্যাত"),
 "raigad": ("place", "Raigad|ৰায়গড়", "Fort in Maharashtra where Shivaji was crowned|মহাৰাষ্ট্ৰৰ দুৰ্গ, য'ত শিৱাজীৰ অভিষেক হৈছিল", [18.23, 73.44]),
 "srirangapatna": ("place", "Srirangapatna|শ্ৰীৰংগপট্টনম", "Tipu Sultan's capital in Karnataka|কৰ্ণাটকত টিপু ছুলতানৰ ৰাজধানী", [12.42, 76.69]),
})
sources = [
 src("Wikipedia, Shivaji", "https://en.wikipedia.org/wiki/Shivaji", "Used as a guide: 1674, Raigad, Ashta Pradhan, 1659, 1666 and doubts on the basket story, 1680, chauth. Check in review."),
 src("Wikipedia, Third Battle of Panipat", "https://en.wikipedia.org/wiki/Third_Battle_of_Panipat", "Used as a guide: 14 January 1761, Sadashivrao Bhau, Ahmad Shah Durrani. Check in review."),
 src("Wikipedia, Tipu Sultan", "https://en.wikipedia.org/wiki/Tipu_Sultan", "Used as a guide: Sher-e-Mysore, Hyder Ali, four wars, Srirangapatna, 4 May 1799, rockets. Check in review."),
]
u1 = U(1, "crown", "A crown at Raigad|ৰায়গড়ত মুকুট",
 "Fix the facts of Shivaji's kingdom.|শিৱাজীৰ ৰাজ্যৰ তথ্য মনত ৰাখা।", "Finding recorded: crowned Chhatrapati at Raigad in 1674.|প্ৰমাণ লিখা হ'ল: ১৬৭৪ত ৰায়গড়ত ছত্ৰপতি অভিষেক।",
 ["Shivaji founded the Maratha kingdom|শিৱাজীয়ে মাৰাঠা ৰাজ্য গঢ়িছিল", "He was crowned Chhatrapati at Raigad in 1674|১৬৭৪ত ৰায়গড়ত ছত্ৰপতি হিচাপে অভিষিক্ত", "His council was the Ashta Pradhan|তেওঁৰ পৰিষদ অষ্টপ্ৰধান", "He collected chauth and sardeshmukhi|তেওঁ চৌথ আৰু সৰদেশমুখী লৈছিল"],
 S("Crowned at Raigad|ৰায়গড়ত অভিষেক", "[[shivaji|Shivaji]] was crowned <mark>Chhatrapati</mark> at [[raigad]] on 6 June <mark>1674</mark>.|১৬৭৪ৰ ৬ জুনত [[raigad|ৰায়গড়ত]] [[shivaji|শিৱাজী]] <mark>ছত্ৰপতি</mark> হিচাপে অভিষিক্ত হৈছিল।", "A council of eight ministers, the <mark>Ashta Pradhan</mark>, advised him.|আঠজন মন্ত্ৰীৰ পৰিষদ <mark>অষ্টপ্ৰধানে</mark> তেওঁক পৰামৰ্শ দিছিল।", art="court"),
 S("Agra and after|আগ্ৰা আৰু তাৰ পিছত", "In 1666 Aurangzeb held him under house arrest at Agra, and he escaped. The famous basket story has no contemporary support, according to one historian.|১৬৬৬ত ঔৰংগজেবে আগ্ৰাত তেওঁক গৃহবন্দী কৰিছিল, তেওঁ পলাই গৈছিল। বিখ্যাত টোপোলাৰ কাহিনীৰ সমসাময়িক প্ৰমাণ নাই বুলি এজন ইতিহাসবিদে কৈছে।", "He died at Raigad in 1680.|১৬৮০ত ৰায়গড়ত তেওঁৰ মৃত্যু হয়।", art="door"),
 IN("Shivaji was crowned at|শিৱাজীৰ অভিষেক হৈছিল", ".|ত।", ["Raigad|ৰায়গড়", "Agra|আগ্ৰা", "Pune|পুণে", "Satara|সাতাৰা"], 0, "Raigad, in 1674.|১৬৭৪ত ৰায়গড়।"),
 MP("Tap Raigad.|ৰায়গড় টিপা।", "raigad", ["raigad", "srirangapatna", "panipat", "delhi"], "In Maharashtra.|মহাৰাষ্ট্ৰত।"),
 TF("The Ashta Pradhan was a council of eight ministers.|অষ্টপ্ৰধান আঠজন মন্ত্ৰীৰ পৰিষদ।", True, "Most also held military commands.|বেছিভাগেই সামৰিক দায়িত্বও পালন কৰিছিল।"),
 MA([("Chhatrapati|ছত্ৰপতি", "Shivaji's title|শিৱাজীৰ উপাধি"), ("Ashta Pradhan|অষ্টপ্ৰধান", "Eight ministers|আঠজন মন্ত্ৰী"), ("Chauth|চৌথ", "A revenue right|ৰাজহৰ অধিকাৰ")], "Maratha terms.|মাৰাঠা শব্দ।"),
 SP("Shivaji was crowned in *1774.*|শিৱাজীৰ অভিষেক *১৭৭৪ত* হৈছিল।", "1674|১৬৭৪ত", "1674.|১৬৭৪।"),
 SC("Unscramble Shivaji's title.|শিৱাজীৰ উপাধিটো সজোৱা।", "CHHATRAPATI", ["ছ", "ত্ৰ", "প", "তি"], "Chhatrapati.|ছত্ৰপতি।"),
)
u2 = U(2, "flag", "The third Panipat|তৃতীয় পানিপথ",
 "Close the set of three Panipats.|তিনিটা পানিপথৰ তালিকা সম্পূৰ্ণ কৰা।", "Finding recorded: Durrani beat the Marathas on 14 January 1761.|প্ৰমাণ লিখা হ'ল: ১৭৬১ৰ ১৪ জানুৱাৰীত দুৰানীয়ে মাৰাঠাক হৰুৱাইছিল।",
 ["The Third Battle of Panipat was in 1761|পানিপথৰ তৃতীয় যুদ্ধ ১৭৬১ত", "Ahmad Shah Durrani beat the Marathas|আহমদ শ্বাহ দুৰানীয়ে মাৰাঠাক হৰুৱাইছিল", "Sadashivrao Bhau led the Marathas and was killed|সদাশিৱৰাও ভাউৱে মাৰাঠাক নেতৃত্ব দিছিল, নিহত হৈছিল", "Rohillas and Awadh backed Durrani|ৰোহিলা আৰু অযোধ্যাই দুৰানীক সমৰ্থন কৰিছিল"],
 S("January 1761|১৭৬১ৰ জানুৱাৰী", "On 14 January <mark>1761</mark> the Marathas under Sadashivrao Bhau fought [[ahmad-shah-durrani|Ahmad Shah Durrani]] at [[panipat]].|<mark>১৭৬১ৰ</mark> ১৪ জানুৱাৰীত সদাশিৱৰাও ভাউৰ নেতৃত্বত মাৰাঠাই [[panipat|পানিপথত]] [[ahmad-shah-durrani|আহমদ শ্বাহ দুৰানীৰ]] সৈতে যুঁজিছিল।", art="embassy"),
 S("A decisive defeat|চূড়ান্ত পৰাজয়", "Durrani won, helped by the Rohillas and the Nawab of Awadh. Bhau was killed, and losses were huge.|ৰোহিলা আৰু অযোধ্যাৰ নবাবৰ সহায়ত দুৰানী জয়ী হৈছিল। ভাউ নিহত হ'ল, ক্ষতি বিশাল।", "Now you have all three: <b>1526, 1556, 1761</b>.|এতিয়া তিনিওটা হ'ল: <b>১৫২৬, ১৫৫৬, ১৭৬১</b>।", art="calendar"),
 OR("Put the three Panipats in order.|তিনিটা পানিপথ ক্ৰমে সজোৱা।", ["Babur and Ibrahim Lodi|বাবৰ আৰু ইব্ৰাহিম লোদী", "Mughals and Hemu|মোগল আৰু হেমু", "Durrani and the Marathas|দুৰানী আৰু মাৰাঠা"], "1526, 1556, 1761.|১৫২৬, ১৫৫৬, ১৭৬১।"),
 IN("The Marathas lost the Third Battle of Panipat to|মাৰাঠাই পানিপথৰ তৃতীয় যুদ্ধত হাৰিছিল", ".|ৰ ওচৰত।", ["Akbar|আকবৰ", "Robert Clive|ৰবাৰ্ট ক্লাইভ", "Ahmad Shah Durrani|আহমদ শ্বাহ দুৰানী", "Tipu Sultan|টিপু ছুলতান"], 2, "Ahmad Shah Durrani.|আহমদ শ্বাহ দুৰানী।"),
 TF("The Marathas won at Panipat in 1761.|১৭৬১ত পানিপথত মাৰাঠা জয়ী হৈছিল।", False, "They suffered a decisive defeat.|তেওঁলোক চূড়ান্তভাৱে পৰাস্ত হৈছিল।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1674, "Shivaji crowned|শিৱাজীৰ অভিষেক"), (1761, "Third Panipat|তৃতীয় পানিপথ")], [("Aurangzeb dies, 1707|ঔৰংগজেবৰ মৃত্যু, ১৭০৭", 1), ("Plassey, 1757|পলাশী, ১৭৫৭", 1), ("Tipu dies, 1799|টিপুৰ মৃত্যু, ১৭৯৯", 2)], "1674 → 1707 → 1757 → 1761 → 1799.|১৬৭৪ → ১৭০৭ → ১৭৫৭ → ১৭৬১ → ১৭৯৯।"),
 WH(["I led the Marathas in 1761.|মই ১৭৬১ত মাৰাঠাৰ নেতৃত্ব দিছিলোঁ।", "I was killed at Panipat.|মই পানিপথত নিহত হৈছিলোঁ।"], ["Shivaji|শিৱাজী", "Sadashivrao Bhau|সদাশিৱৰাও ভাউ", "Hyder Ali|হায়দৰ আলী", "Ahmad Shah Durrani|আহমদ শ্বাহ দুৰানী"], 1, "Sadashivrao Bhau.|সদাশিৱৰাও ভাউ।"),
)
u3 = U(3, "star", "Tiger of Mysore|মহীশূৰৰ বাঘ",
 "Keep Hyder Ali and Tipu Sultan apart.|হায়দৰ আলী আৰু টিপু ছুলতান পৃথক ৰাখা।", "Finding recorded: Tipu, Sher-e-Mysore, fell at Srirangapatna in 1799.|প্ৰমাণ লিখা হ'ল: শ্বেৰ-ই-মহীশূৰ টিপু ১৭৯৯ত শ্ৰীৰংগপট্টনমত নিহত হৈছিল।",
 ["Hyder Ali ruled Mysore in practice from 1761|হায়দৰ আলীয়ে ১৭৬১ৰ পৰা কাৰ্যতঃ মহীশূৰ শাসন কৰিছিল", "Tipu Sultan was his son|টিপু ছুলতান তেওঁৰ পুত্ৰ", "Tipu is called Sher-e-Mysore|টিপুক শ্বেৰ-ই-মহীশূৰ বোলা হয়", "He died at Srirangapatna on 4 May 1799|১৭৯৯ৰ ৪ মে'ত শ্ৰীৰংগপট্টনমত তেওঁৰ মৃত্যু হয়"],
 S("Father and son|পিতৃ আৰু পুত্ৰ", "[[hyder-ali|Hyder Ali]] held real power in Mysore from 1761. His son <mark>[[tipu-sultan|Tipu Sultan]]</mark> fought the East India Company in all four Anglo-Mysore wars.|১৭৬১ৰ পৰা মহীশূৰত [[hyder-ali|হায়দৰ আলীৰ]] প্ৰকৃত ক্ষমতা আছিল। তেওঁৰ পুত্ৰ <mark>[[tipu-sultan|টিপু ছুলতানে]]</mark> চাৰিওটা ইংৰাজ-মহীশূৰ যুদ্ধত কোম্পানীৰ সৈতে যুঁজিছিল।", art="court"),
 S("Tiger or lion?|বাঘ নে সিংহ?", "Tipu is <mark>Sher-e-Mysore</mark>. Sher can mean tiger or lion. English usually says Tiger of Mysore, but one ADRE paper said Lion. Either way the answer is <mark>Tipu</mark>.|টিপু <mark>শ্বেৰ-ই-মহীশূৰ</mark>। শ্বেৰ মানে বাঘ বা সিংহ। ইংৰাজীত সাধাৰণতে মহীশূৰৰ বাঘ বোলে, কিন্তু এখন ADRE প্ৰশ্নকাকতত সিংহ আছিল। দুয়োটাতে উত্তৰ <mark>টিপু</mark>।", "He died defending [[srirangapatna|Srirangapatna]] in 1799.|১৭৯৯ত [[srirangapatna|শ্ৰীৰংগপট্টনম]] ৰক্ষা কৰোঁতে তেওঁৰ মৃত্যু হয়।", art="seal"),
 IN("The ruler called the Lion of Mysore in an ADRE paper is|ADRE প্ৰশ্নকাকতত মহীশূৰৰ সিংহ বোলা শাসক", ".|।", ["Adil Shah|আদিল শ্বাহ", "Hyder Ali|হায়দৰ আলী", "Krishnaraja Wodeyar|কৃষ্ণৰাজ ৱদিয়াৰ", "Tipu Sultan|টিপু ছুলতান"], 3, "Tipu Sultan, Sher-e-Mysore.|টিপু ছুলতান, শ্বেৰ-ই-মহীশূৰ।"),
 MP("Tap Tipu's capital.|টিপুৰ ৰাজধানী টিপা।", "srirangapatna", ["srirangapatna", "raigad", "panipat", "delhi"], "Srirangapatna.|শ্ৰীৰংগপট্টনম।"),
 TF("Tipu Sultan was the son of Hyder Ali.|টিপু ছুলতান হায়দৰ আলীৰ পুত্ৰ।", True, "Yes.|হয়।"),
 SP("Tipu died defending Srirangapatna in *1857.*|টিপুৰ মৃত্যু *১৮৫৭ত* শ্ৰীৰংগপট্টনম ৰক্ষা কৰোঁতে হৈছিল।", "1799|১৭৯৯ত", "4 May 1799.|১৭৯৯ৰ ৪ মে'।"),
 OD("Which was NOT a Mysore name?|কোনটো মহীশূৰৰ নাম নহয়?", ["Hyder Ali|হায়দৰ আলী", "Tipu Sultan|টিপু ছুলতান", "Sher-e-Mysore|শ্বেৰ-ই-মহীশূৰ", "Sadashivrao Bhau|সদাশিৱৰাও ভাউ"], 3, "Bhau was a Maratha commander.|ভাউ মাৰাঠা সেনাপতি।"),
)
test = TEST("Name who filled the space Aurangzeb left.|ঔৰংগজেবৰ শূন্যস্থান কোনে পূৰণ কৰিলে, কোৱা।", "Recorded: Marathas, Durrani and Mysore.|লিখা হ'ল: মাৰাঠা, দুৰানী আৰু মহীশূৰ।",
 IN("The Ashta Pradhan served|অষ্টপ্ৰধানে সেৱা কৰিছিল", ".|ক।", ["Akbar|আকবৰ", "Shivaji|শিৱাজী", "Tipu Sultan|টিপু ছুলতান", "Aurangzeb|ঔৰংগজেব"], 1, "Shivaji.|শিৱাজী।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Shivaji crowned|শিৱাজীৰ অভিষেক", "Third Panipat|তৃতীয় পানিপথ", "Tipu dies|টিপুৰ মৃত্যু"], "1674, 1761, 1799.|১৬৭৪, ১৭৬১, ১৭৯৯।"),
 MA([("1526|১৫২৬", "Babur|বাবৰ"), ("1556|১৫৫৬", "Akbar's side|আকবৰৰ পক্ষ"), ("1761|১৭৬১", "Ahmad Shah Durrani|আহমদ শ্বাহ দুৰানী")], "Panipat and its winner.|পানিপথ আৰু বিজয়ী।"),
 MP("Tap Raigad.|ৰায়গড় টিপা।", "raigad", ["raigad", "srirangapatna", "panipat", "delhi"], "Raigad.|ৰায়গড়।"),
 TF("Tipu Sultan fought the East India Company.|টিপু ছুলতানে ইষ্ট ইণ্ডিয়া কোম্পানীৰ সৈতে যুঁজিছিল।", True, "In the Anglo-Mysore wars.|ইংৰাজ-মহীশূৰ যুদ্ধত।"),
 MC("Consider these statements. (1) Shivaji was crowned at Raigad. (2) Hyder Ali was the son of Tipu Sultan. (3) Sadashivrao Bhau led the Marathas in 1761. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) শিৱাজীৰ অভিষেক ৰায়গড়ত। (২) হায়দৰ আলী টিপু ছুলতানৰ পুত্ৰ। (৩) ১৭৬১ত সদাশিৱৰাও ভাউৱে মাৰাঠাৰ নেতৃত্ব দিছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Tipu was Hyder Ali's son.|টিপু হায়দৰ আলীৰ পুত্ৰ।"),
)
LESSON(17, "Marathas and Mysore|মাৰাঠা আৰু মহীশূৰ", "1674–1799|১৬৭৪–১৭৯৯", "The Mughal age|মোগল যুগ", "Evidence file 17|প্ৰমাণ নথি ১৭", "After the Mughals, who?|মোগলৰ পিছত কোন?",
 "As Mughal power thinned, new rulers rose in the Deccan and Mysore, and an Afghan army broke the Marathas at Panipat.|মোগল শক্তি ক্ষীণ হোৱাৰ লগে লগে দাক্ষিণাত্য আৰু মহীশূৰত নতুন শাসকৰ উত্থান হ'ল, আফগান সৈন্যই পানিপথত মাৰাঠাক ভাঙিলে।",
 sources, [u1, u2, u3], test, ["raigad", "srirangapatna", "panipat", "delhi"],
 timeline=[("1674", "Shivaji crowned|শিৱাজীৰ অভিষেক", "u1"), ("1761", "Third Battle of Panipat|পানিপথৰ তৃতীয় যুদ্ধ", "u2"), ("1799", "Tipu Sultan dies|টিপু ছুলতানৰ মৃত্যু", "u3")])
