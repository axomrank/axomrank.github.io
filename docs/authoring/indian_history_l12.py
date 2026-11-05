#!/usr/bin/env python3
"""Lesson 12: Vijayanagara and the Deccan."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "hampi": ("place", "Hampi|হাম্পি", "Ruins of Vijayanagara in Karnataka|কৰ্ণাটকত বিজয়নগৰৰ ধ্বংসাৱশেষ", [15.34, 76.46]),
 "bijapur": ("place", "Bijapur|বিজাপুৰ", "Karnataka city of the Adil Shahi sultans, today's Vijayapura|কৰ্ণাটকৰ আদিল শ্বাহী ছুলতানৰ নগৰ, আজিৰ বিজয়পুৰা", [16.83, 75.71]),
 "hyderabad": ("place", "Hyderabad|হায়দৰাবাদ", "City of the Qutb Shahi rulers|কুতুব শ্বাহী শাসকৰ নগৰ", [17.36, 78.47]),
 "talikota": ("place", "Talikota|তালিকোটা", "Deccan town that names the battle of 1565|১৫৬৫ৰ যুদ্ধৰ নামৰ দাক্ষিণাত্যৰ নগৰ", [16.47, 76.31]),
 "krishnadevaraya": ("person", "Krishnadeva Raya|কৃষ্ণদেৱ ৰায়", "Vijayanagara emperor, 1509 to 1529|বিজয়নগৰৰ সম্ৰাট, ১৫০৯ৰ পৰা ১৫২৯"),
 "harihara-bukka": ("person", "Harihara and Bukka|হৰিহৰ আৰু বুক্ক", "Brothers who founded Vijayanagara in 1336|১৩৩৬ত বিজয়নগৰ প্ৰতিষ্ঠা কৰা ভাতৃদ্বয়"),
})
sources = [
 src("Wikipedia, Vijayanagara Empire", "https://en.wikipedia.org/wiki/Vijayanagara_Empire", "Used as a guide: 1336, Harihara and Bukka, Sangama, Hampi, Krishnadevaraya, Talikota. Check in review."),
 src("Wikipedia, Gol Gumbaz", "https://en.wikipedia.org/wiki/Gol_Gumbaz", "Used as a guide: Bijapur, Mohammed Adil Shah, died 1656, whispering gallery. Check in review."),
 src("Wikipedia, Charminar", "https://en.wikipedia.org/wiki/Charminar", "Used as a guide: 1591, Muhammad Quli Qutb Shah, Hyderabad. Check in review."),
]
MAPD = {"base": "india", "box": [71, 13.5, 82, 20], "show": ["hampi", "bijapur", "hyderabad", "talikota"]}
u1 = U(1, "crown", "Two brothers found an empire|দুই ভায়েকৰ সাম্ৰাজ্য",
 "Fix the founders of Vijayanagara.|বিজয়নগৰৰ প্ৰতিষ্ঠাপক মনত ৰাখা।", "Finding recorded: Harihara and Bukka, 1336.|প্ৰমাণ লিখা হ'ল: হৰিহৰ আৰু বুক্ক, ১৩৩৬।",
 ["Harihara and Bukka founded Vijayanagara in 1336|১৩৩৬ত হৰিহৰ আৰু বুক্কই বিজয়নগৰ প্ৰতিষ্ঠা কৰিছিল", "They were of the Sangama dynasty|তেওঁলোক সংগম বংশৰ", "Its ruins are near Hampi|ইয়াৰ ধ্বংসাৱশেষ হাম্পিৰ ওচৰত", "Krishnadeva Raya ruled at its peak|কৃষ্ণদেৱ ৰায়ে ইয়াৰ শীৰ্ষ সময়ত শাসন কৰিছিল"],
 S("A city of victory|বিজয়ৰ নগৰ", "In <mark>1336</mark> [[harihara-bukka|Harihara and Bukka]], of the Sangama dynasty, founded the empire named after its capital, <mark>Vijayanagara</mark>.|<mark>১৩৩৬ত</mark> সংগম বংশৰ [[harihara-bukka|হৰিহৰ আৰু বুক্কই]] ৰাজধানীৰ নামেৰে <mark>বিজয়নগৰ</mark> সাম্ৰাজ্য প্ৰতিষ্ঠা কৰিছিল।", "Its ruins near [[hampi]] are a World Heritage Site.|[[hampi|হাম্পিৰ]] ওচৰৰ ইয়াৰ ধ্বংসাৱশেষ বিশ্ব ঐতিহ্য স্থল।", map=MAPD),
 S("The peak|শীৰ্ষ সময়", "[[krishnadevaraya|Krishnadeva Raya]] ruled from <mark>1509 to 1529</mark>, the height of the empire.|[[krishnadevaraya|কৃষ্ণদেৱ ৰায়ে]] <mark>১৫০৯ৰ পৰা ১৫২৯লৈ</mark> শাসন কৰিছিল, সাম্ৰাজ্যৰ শীৰ্ষ সময়।", art="court"),
 IN("Harihara and Bukka founded the|হৰিহৰ আৰু বুক্কই প্ৰতিষ্ঠা কৰিছিল", ".|।", ["Chalukya Empire|চালুক্য সাম্ৰাজ্য", "Vijayanagara Empire|বিজয়নগৰ সাম্ৰাজ্য", "Chola Empire|চোল সাম্ৰাজ্য", "Hoysala Empire|হয়শালা সাম্ৰাজ্য"], 1, "Vijayanagara, in 1336.|১৩৩৬ত বিজয়নগৰ।"),
 MP("Tap Hampi.|হাম্পি টিপা।", "hampi", ["hampi", "delhi", "panipat", "bodh-gaya"], "In Karnataka.|কৰ্ণাটকত।"),
 TF("Krishnadeva Raya ruled Vijayanagara at its height.|কৃষ্ণদেৱ ৰায়ে শীৰ্ষ সময়ত বিজয়নগৰ শাসন কৰিছিল।", True, "From 1509 to 1529.|১৫০৯ৰ পৰা ১৫২৯লৈ।"),
 SP("Vijayanagara was founded in *1526.*|বিজয়নগৰ *১৫২৬ত* প্ৰতিষ্ঠিত হৈছিল।", "1336|১৩৩৬ত", "It began in 1336.|১৩৩৬ত আৰম্ভ হৈছিল।"),
 WH(["I was a Vijayanagara ruler.|মই বিজয়নগৰৰ শাসক।", "My reign began in 1509.|মোৰ ৰাজত্ব ১৫০৯ত আৰম্ভ হৈছিল।"], ["Harihara|হৰিহৰ", "Krishnadeva Raya|কৃষ্ণদেৱ ৰায়", "Rama Raya|ৰাম ৰায়", "Bukka|বুক্ক"], 1, "Krishnadeva Raya.|কৃষ্ণদেৱ ৰায়।"),
)
u2 = U(2, "flag", "Talikota, 1565|তালিকোটা, ১৫৬৫",
 "See why the empire fell.|সাম্ৰাজ্য কিয় পতন হ'ল, চোৱা।", "Finding recorded: the Deccan sultanates beat Vijayanagara at Talikota in 1565.|প্ৰমাণ লিখা হ'ল: ১৫৬৫ত তালিকোটাত দাক্ষিণাত্যৰ ছুলতানীয়ে বিজয়নগৰক হৰুৱাইছিল।",
 ["The Bahmani Sultanate was Vijayanagara's rival|বাহমনী ছুলতানী বিজয়নগৰৰ প্ৰতিদ্বন্দ্বী", "Deccan sultanates later stood in its place|পিছত দাক্ষিণাত্যৰ ছুলতানী ইয়াৰ ঠাই ল'লে", "They defeated Rama Raya's army in 1565|১৫৬৫ত ৰাম ৰায়ৰ সৈন্যক হৰুৱাইছিল", "The battle is named after Talikota|যুদ্ধৰ নাম তালিকোটা"],
 S("Rival to the north|উত্তৰৰ প্ৰতিদ্বন্দ্বী", "Vijayanagara fought the <mark>Bahmani Sultanate</mark> to its north. In time that split into Deccan sultanates, including Bijapur.|বিজয়নগৰে উত্তৰৰ <mark>বাহমনী ছুলতানীৰ</mark> সৈতে যুঁজিছিল। পিছত সেয়া বিজাপুৰকে ধৰি দাক্ষিণাত্যৰ ছুলতানীত ভাগ হ'ল।", art="houses"),
 S("One day in January|জানুৱাৰীৰ এটা দিন", "On 23 January <mark>1565</mark> the Deccan sultanates defeated Rama Raya's army in the battle of <mark>Talikota</mark>.|<mark>১৫৬৫ৰ</mark> ২৩ জানুৱাৰীত <mark>তালিকোটাৰ</mark> যুদ্ধত দাক্ষিণাত্যৰ ছুলতানীয়ে ৰাম ৰায়ৰ সৈন্যক হৰুৱাইছিল।", map=MAPD),
 IN("The Battle of Talikota was fought in|তালিকোটাৰ যুদ্ধ হৈছিল", ".|ত।", ["1336|১৩৩৬", "1509|১৫০৯", "1526|১৫২৬", "1565|১৫৬৫"], 3, "1565.|১৫৬৫।"),
 TF("Vijayanagara won at Talikota.|তালিকোটাত বিজয়নগৰ জয়ী হৈছিল।", False, "The Deccan sultanates won.|দাক্ষিণাত্যৰ ছুলতানী জয়ী হৈছিল।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Vijayanagara founded|বিজয়নগৰ প্ৰতিষ্ঠা", "Krishnadeva Raya's reign|কৃষ্ণদেৱ ৰায়ৰ ৰাজত্ব", "Talikota|তালিকোটা"], "1336, 1509, 1565.|১৩৩৬, ১৫০৯, ১৫৬৫।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1336, "Vijayanagara founded|বিজয়নগৰ প্ৰতিষ্ঠা"), (1565, "Talikota|তালিকোটা")], [("Timur at Delhi, 1398|দিল্লীত তিমুৰ, ১৩৯৮", 1), ("First Panipat, 1526|পানিপথৰ প্ৰথম যুদ্ধ, ১৫২৬", 1), ("Charminar built, 1591|চাৰমিনাৰ নিৰ্মাণ, ১৫৯১", 2)], "1336 → 1398 → 1526 → 1565 → 1591.|১৩৩৬ → ১৩৯৮ → ১৫২৬ → ১৫৬৫ → ১৫৯১।"),
 SC("Unscramble the battle of 1565.|১৫৬৫ৰ যুদ্ধটো সজোৱা।", "TALIKOTA", ["তা", "লি", "কো", "টা"], "Talikota.|তালিকোটা।"),
)
u3 = U(3, "houses", "Domes and minarets|গম্বুজ আৰু মিনাৰ",
 "Match the Deccan's great buildings.|দাক্ষিণাত্যৰ মহান নিৰ্মাণ মিলোৱা।", "Finding recorded: Gol Gumbaz at Bijapur, Charminar at Hyderabad.|প্ৰমাণ লিখা হ'ল: বিজাপুৰত গোল গম্বুজ, হায়দৰাবাদত চাৰমিনাৰ।",
 ["Gol Gumbaz is at Bijapur|গোল গম্বুজ বিজাপুৰত", "It is the tomb of Mohammed Adil Shah|ই মহম্মদ আদিল শ্বাহৰ সমাধি", "Charminar is at Hyderabad|চাৰমিনাৰ হায়দৰাবাদত", "Muhammad Quli Qutb Shah built it in 1591|১৫৯১ত মহম্মদ কুলি কুতুব শ্বাহে নিৰ্মাণ কৰিছিল"],
 S("A dome that whispers|ফুচফুচোৱা গম্বুজ", "The <mark>Gol Gumbaz</mark> at [[bijapur]] is the mausoleum of Mohammed Adil Shah. It was left unfinished at his death in 1656.|[[bijapur|বিজাপুৰৰ]] <mark>গোল গম্বুজ</mark> মহম্মদ আদিল শ্বাহৰ সমাধি। ১৬৫৬ত তেওঁৰ মৃত্যুত ই অসম্পূৰ্ণ হৈ ৰ'ল।", "A whispering gallery runs around its dome.|ইয়াৰ গম্বুজৰ চাৰিওফালে ফুচফুচনি গেলেৰী আছে।", art="door"),
 S("Four minarets|চাৰিটা মিনাৰ", "<mark>Charminar</mark> stands in [[hyderabad]]. Muhammad Quli Qutb Shah built it in <mark>1591</mark> after moving his capital from Golconda.|<mark>চাৰমিনাৰ</mark> [[hyderabad|হায়দৰাবাদত]] আছে। গোলকোণ্ডাৰ পৰা ৰাজধানী সলোৱাৰ পিছত <mark>১৫৯১ত</mark> মহম্মদ কুলি কুতুব শ্বাহে ইয়াক নিৰ্মাণ কৰিছিল।", art="houses"),
 IN("The Gol Gumbaz is located in|গোল গম্বুজ অৱস্থিত", ".|ত।", ["Bijapur|বিজাপুৰ", "Delhi|দিল্লী", "Hyderabad|হায়দৰাবাদ", "Bhopal|ভোপাল"], 0, "Bijapur.|বিজাপুৰ।"),
 MP("Tap the city of the Charminar.|চাৰমিনাৰৰ নগৰখন টিপা।", "hyderabad", ["hyderabad", "delhi", "panipat", "bodh-gaya"], "Hyderabad.|হায়দৰাবাদ।"),
 MA([("Gol Gumbaz|গোল গম্বুজ", "Bijapur|বিজাপুৰ"), ("Charminar|চাৰমিনাৰ", "Hyderabad|হায়দৰাবাদ"), ("Qutb Minar|কুতুব মিনাৰ", "Delhi|দিল্লী")], "Monument and city.|স্মাৰক আৰু নগৰ।"),
 TF("The Gol Gumbaz is the tomb of Muhammad Quli Qutb Shah.|গোল গম্বুজ মহম্মদ কুলি কুতুব শ্বাহৰ সমাধি।", False, "It is Mohammed Adil Shah's.|ই মহম্মদ আদিল শ্বাহৰ।"),
 SP("Charminar was built in *1691.*|চাৰমিনাৰ *১৬৯১ত* নিৰ্মিত।", "1591|১৫৯১ত", "1591.|১৫৯১।"),
)
test = TEST("Sort the south after 1336.|১৩৩৬ৰ পিছৰ দক্ষিণ পৃথক কৰা।", "Recorded: Vijayanagara and the Deccan sultanates.|লিখা হ'ল: বিজয়নগৰ আৰু দাক্ষিণাত্যৰ ছুলতানী।",
 IN("Harihara and Bukka founded|হৰিহৰ আৰু বুক্কই প্ৰতিষ্ঠা কৰিছিল", ".|।", ["Vijayanagara|বিজয়নগৰ", "Bijapur|বিজাপুৰ", "Golconda|গোলকোণ্ডা", "Hampi Sultanate|হাম্পি ছুলতানী"], 0, "Vijayanagara.|বিজয়নগৰ।"),
 MA([("Gol Gumbaz|গোল গম্বুজ", "Adil Shahi|আদিল শ্বাহী"), ("Charminar|চাৰমিনাৰ", "Qutb Shahi|কুতুব শ্বাহী")], "Monument and dynasty.|স্মাৰক আৰু বংশ।"),
 TF("Charminar is in Hyderabad.|চাৰমিনাৰ হায়দৰাবাদত।", True, "Yes.|হয়।"),
 MP("Tap Hampi.|হাম্পি টিপা।", "hampi", ["hampi", "delhi", "panipat", "bodh-gaya"], "Hampi.|হাম্পি।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Talikota|তালিকোটা", "Charminar|চাৰমিনাৰ", "Gol Gumbaz left unfinished|গোল গম্বুজ অসম্পূৰ্ণ"], "1565, 1591, 1656.|১৫৬৫, ১৫৯১, ১৬৫৬।"),
 MC("Consider these statements. (1) Vijayanagara was founded in 1336. (2) Krishnadeva Raya lost at Talikota. (3) Hampi holds Vijayanagara's ruins. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) বিজয়নগৰ ১৩৩৬ত প্ৰতিষ্ঠিত। (২) তালিকোটাত কৃষ্ণদেৱ ৰায় পৰাস্ত হৈছিল। (৩) হাম্পিত বিজয়নগৰৰ ধ্বংসাৱশেষ আছে। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Rama Raya's army lost, after Krishnadeva Raya's death.|কৃষ্ণদেৱ ৰায়ৰ মৃত্যুৰ পিছত ৰাম ৰায়ৰ সৈন্য পৰাস্ত হৈছিল।"),
)
LESSON(12, "Vijayanagara and the Deccan|বিজয়নগৰ আৰু দাক্ষিণাত্য", "1336–1656|১৩৩৬–১৬৫৬", "Sultans, Deccan and devotion|ছুলতান, দাক্ষিণাত্য আৰু ভক্তি", "Evidence file 12|প্ৰমাণ নথি ১২", "City of victory|বিজয়ৰ নগৰ",
 "South of Delhi, two brothers built an empire and rival sultans built great domes. Follow the Deccan from Hampi to Hyderabad.|দিল্লীৰ দক্ষিণত দুই ভায়েকে সাম্ৰাজ্য গঢ়িলে, ছুলতানে গম্বুজ বনালে। হাম্পিৰ পৰা হায়দৰাবাদলৈ দাক্ষিণাত্য অনুসৰণ কৰা।",
 sources, [u1, u2, u3], test, ["hampi", "delhi", "panipat", "bodh-gaya", "hyderabad"], timeline=[("1336", "Vijayanagara founded|বিজয়নগৰ প্ৰতিষ্ঠা", "u1"), ("1565", "Battle of Talikota|তালিকোটাৰ যুদ্ধ", "u2"), ("1591", "Charminar built|চাৰমিনাৰ নিৰ্মাণ", "u3")])
