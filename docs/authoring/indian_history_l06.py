#!/usr/bin/env python3
"""Lesson 6: After the Mauryas."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "kanishka": ("person", "Kanishka|কনিষ্ক", "Kushan emperor of the 2nd century CE|খ্ৰীষ্টীয় দ্বিতীয় শতিকাৰ কুষাণ সম্ৰাট"),
 "gautamiputra-satakarni": ("person", "Gautamiputra Satakarni|গৌতমীপুত্ৰ সাতকৰ্ণী", "Greatest Satavahana ruler|সাতবাহনৰ শ্ৰেষ্ঠ শাসক"),
 "begram": ("place", "Begram|বেগ্ৰাম", "Site in Afghanistan, famous for its hoard of ivories|আফগানিস্তানৰ স্থল, হাতীদাঁতৰ ভাণ্ডাৰৰ বাবে খ্যাত", [34.96, 69.26]),
 "purushapura": ("place", "Purushapura|পুৰুষপুৰ", "Kushan capital, today's Peshawar|কুষাণ ৰাজধানী, আজিৰ পেশাৱাৰ", [34.01, 71.57]),
 "mathura": ("place", "Mathura|মথুৰা", "City in Uttar Pradesh, a centre of early Indian sculpture|উত্তৰ প্ৰদেশৰ নগৰ, আদি ভাৰতীয় ভাস্কৰ্যৰ কেন্দ্ৰ", [27.49, 77.67]),
})
sources = [
 src("Wikipedia, Kanishka", "https://en.wikipedia.org/wiki/Kanishka", "Used as a guide: c. 127 to 150 CE, Purushapura, Mathura, Fourth Council as tradition, Gandhara, the 78 CE debate. Check in review."),
 src("Wikipedia, Begram ivories", "https://en.wikipedia.org/wiki/Begram_ivories", "Used as a guide: find, 1936 to 1940, 1st or 2nd century CE. The export's key for APSC 2025 Q21 reads differently. Check in review."),
 src("Wikipedia, Satavahana dynasty", "https://en.wikipedia.org/wiki/Satavahana_dynasty", "Used as a guide: region, Prakrit, Gautamiputra Satakarni, the Nashik inscription. Check in review."),
 src("Wikipedia, Sangam literature", "https://en.wikipedia.org/wiki/Sangam_literature", "Used as a guide: Old Tamil, date range, akam and puram, Chola, Chera and Pandya. Check in review."),
]
u1 = U(1, "crown", "The Kushans|কুষাণ",
 "Place Kanishka and the two schools of sculpture.|কনিষ্ক আৰু ভাস্কৰ্যৰ দুটা ধাৰা স্থাপন কৰা।", "Finding recorded: Kanishka ruled from Purushapura, with Gandhara and Mathura art.|প্ৰমাণ লিখা হ'ল: কনিষ্কই পুৰুষপুৰৰ পৰা শাসন কৰিছিল, গান্ধাৰ আৰু মথুৰা শিল্পৰ সৈতে।",
 ["Kanishka was a Kushan emperor|কনিষ্ক কুষাণ সম্ৰাট", "His main capital was Purushapura, today's Peshawar|তেওঁৰ মূল ৰাজধানী পুৰুষপুৰ, আজিৰ পেশাৱাৰ", "Gandhara and Mathura were his two art schools|গান্ধাৰ আৰু মথুৰা তেওঁৰ দিনৰ দুটা শিল্পধাৰা", "Tradition links him to the Fourth Buddhist Council|পৰম্পৰাই তেওঁক চতুৰ্থ বৌদ্ধ সংগীতিৰ সৈতে জড়িত কৰে"],
 S("Rule from Peshawar|পেশাৱাৰৰ পৰা শাসন", "[[kanishka|Kanishka]] led the Kushans at their peak, about 127 to 150 CE. His main capital was <mark>[[purushapura|Purushapura]]</mark>, and [[mathura]] was another centre.|[[kanishka|কনিষ্কই]] প্ৰায় ১২৭ৰ পৰা ১৫০ খ্ৰীষ্টাব্দত কুষাণৰ শীৰ্ষ সময়ত নেতৃত্ব দিছিল। মূল ৰাজধানী <mark>[[purushapura|পুৰুষপুৰ]]</mark>, [[mathura|মথুৰা]] আন এটা কেন্দ্ৰ।", "He was once linked with 78 CE, the start of the Saka era. Historians no longer accept that.|তেওঁক এসময়ত ৭৮ খ্ৰীষ্টাব্দ, শক সম্বতৰ আৰম্ভণিৰ সৈতে জড়িত কৰা হৈছিল। ইতিহাসবিদে এতিয়া সেয়া নামানে।", art="court"),
 S("Two schools of stone|শিলৰ দুটা ধাৰা", "<mark>Gandhara</mark> art mixed Greek and Indian forms. <mark>Mathura</mark> grew as a second school.|<mark>গান্ধাৰ</mark> শিল্পত গ্ৰীক আৰু ভাৰতীয় ৰূপ মিহলি হৈছিল। <mark>মথুৰা</mark> দ্বিতীয় ধাৰা হিচাপে গঢ়ি উঠিল।", "Tradition credits Kanishka with the Fourth Buddhist Council in Kashmir.|পৰম্পৰা মতে কনিষ্কই কাশ্মীৰত চতুৰ্থ বৌদ্ধ সংগীতি পাতিছিল।", art="seal"),
 WH(["I was a Kushan emperor.|মই কুষাণ সম্ৰাট।", "My main capital was Purushapura.|মোৰ মূল ৰাজধানী পুৰুষপুৰ।", "Tradition links me with the Fourth Council.|পৰম্পৰাই মোক চতুৰ্থ সংগীতিৰ সৈতে জড়িত কৰে।"], ["Ashoka|অশোক", "Kanishka|কনিষ্ক", "Harsha|হৰ্ষ", "Samudragupta|সমুদ্ৰগুপ্ত"], 1, "Kanishka.|কনিষ্ক।"),
 TF("Kanishka's main capital was Pataliputra.|কনিষ্কৰ মূল ৰাজধানী পাটলিপুত্ৰ।", False, "It was Purushapura, today's Peshawar.|ই পুৰুষপুৰ, আজিৰ পেশাৱাৰ।"),
 MA([("Gandhara|গান্ধাৰ", "Greek and Indian forms|গ্ৰীক আৰু ভাৰতীয় ৰূপ"), ("Purushapura|পুৰুষপুৰ", "Peshawar|পেশাৱাৰ"), ("Fourth Council|চতুৰ্থ সংগীতি", "Kashmir, by tradition|পৰম্পৰা মতে কাশ্মীৰ")], "Three Kushan facts.|কুষাণৰ তিনিটা তথ্য।"),
 IN("Purushapura is today's|পুৰুষপুৰ হ'ল আজিৰ", ".|।", ["Lahore|লাহোৰ", "Peshawar|পেশাৱাৰ", "Kabul|কাবুল", "Delhi|দিল্লী"], 1, "Peshawar.|পেশাৱাৰ।"),
 SC("Unscramble the art school of the north-west.|উত্তৰ-পশ্চিমৰ শিল্পধাৰাটো সজোৱা।", "GANDHARA", ["গা", "ন্ধা", "ৰ"], "Gandhara art.|গান্ধাৰ শিল্প।"),
)
u2 = U(2, "seal", "The Begram hoard|বেগ্ৰামৰ ভাণ্ডাৰ",
 "See what a sealed room shows about trade.|বন্ধ কোঠা এটাই বাণিজ্যৰ কি দেখুৱায়, চোৱা।", "Finding recorded: Begram's ivories show Kushan art and links with India.|প্ৰমাণ লিখা হ'ল: বেগ্ৰামৰ হাতীদাঁতে কুষাণ শিল্প আৰু ভাৰতৰ সম্পৰ্ক দেখুৱায়।",
 ["The Begram ivories come from Afghanistan|বেগ্ৰামৰ হাতীদাঁত আফগানিস্তানৰ", "They were dug up between 1936 and 1940|১৯৩৬ৰ পৰা ১৯৪০ৰ ভিতৰত উলিওৱা হৈছিল", "They were plaques once fixed to furniture|এইবোৰ আচবাবৰ ফলক আছিল", "They are dated about the 1st to 2nd century CE|এইবোৰ প্ৰায় খ্ৰীষ্টীয় প্ৰথম-দ্বিতীয় শতিকাৰ"],
 S("Two sealed rooms|দুটা বন্ধ কোঠা", "French excavators at <mark>[[begram|Begram]]</mark> in Afghanistan, working from 1936 to 1940, opened two walled-up rooms.|১৯৩৬ৰ পৰা ১৯৪০লৈ আফগানিস্তানৰ <mark>[[begram|বেগ্ৰামত]]</mark> ফৰাচী খননকাৰীয়ে দেৱালে বন্ধ দুটা কোঠা খুলিছিল।", "Inside were more than a thousand <mark>ivory</mark> and bone pieces, once fixed to furniture.|ভিতৰত আচবাবত লগোৱা হাজাৰতকৈ অধিক <mark>হাতীদাঁত</mark> আৰু হাড়ৰ টুকুৰা আছিল।", art="door"),
 S("How old?|কিমান পুৰণি?", "Sources date them to about the <mark>1st to 2nd century CE</mark>, and link them with north-western India.|উৎসবোৰে এইবোৰক প্ৰায় <mark>খ্ৰীষ্টীয় প্ৰথম-দ্বিতীয় শতিকাৰ</mark> বুলি ধৰে, উত্তৰ-পশ্চিম ভাৰতৰ সৈতে জড়িত।", art="calendar"),
 TF("The Begram ivories were found in India.|বেগ্ৰামৰ হাতীদাঁত ভাৰতত পোৱা গৈছিল।", False, "They were found in Afghanistan.|আফগানিস্তানত পোৱা গৈছিল।"),
 IN("The Begram ivories were once fixed to|বেগ্ৰামৰ হাতীদাঁত এসময়ত লগোৱা আছিল", ".|ত।", ["ships|জাহাজ", "furniture|আচবাব", "temple doors|মন্দিৰৰ দুৱাৰ", "armour|কৱচ"], 1, "They were plaques and inlays on furniture.|এইবোৰ আচবাবৰ ফলক আৰু জড়োৱা কাম।"),
 MP("Tap Begram.|বেগ্ৰাম টিপা।", "begram", ["begram", "mathura", "pataliputra", "delhi"], "Begram is in Afghanistan.|বেগ্ৰাম আফগানিস্তানত।"),
 OD("Which does NOT describe the Begram hoard?|কোনটো বেগ্ৰাম ভাণ্ডাৰৰ বৰ্ণনা নহয়?", ["Ivory and bone|হাতীদাঁত আৰু হাড়", "Walled-up rooms|বন্ধ কোঠা", "French excavators|ফৰাচী খননকাৰী", "Found at Lothal|লোথালত পোৱা"], 3, "It was found in Afghanistan.|আফগানিস্তানত পোৱা গৈছিল।"),
 SP("The ivories are dated to the *Gupta* age.|হাতীদাঁতবোৰ *গুপ্ত* যুগৰ।", "Kushan|কুষাণ", "They are Kushan-period finds.|এইবোৰ কুষাণ যুগৰ।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Maurya rule ends|মৌৰ্য শাসনৰ অন্ত", "Begram ivories in use|বেগ্ৰাম হাতীদাঁত ব্যৱহাৰত", "Begram excavated|বেগ্ৰাম খনন"], "About 185 BCE, 1st to 2nd century CE, 1936 to 1940.|প্ৰায় খ্ৰীষ্টপূৰ্ব ১৮৫, খ্ৰীষ্টীয় প্ৰথম-দ্বিতীয় শতিকা, ১৯৩৬–৪০।"),
)
u3 = U(3, "river", "Deccan and Tamil south|দাক্ষিণাত্য আৰু তামিল দক্ষিণ",
 "See who ruled south of the Kushans.|কুষাণৰ দক্ষিণত কোনে শাসন কৰিছিল, চোৱা।", "Finding recorded: Satavahanas in the Deccan; Cholas, Cheras and Pandyas in the Tamil lands.|প্ৰমাণ লিখা হ'ল: দাক্ষিণাত্যত সাতবাহন; তামিল ভূমিত চোল, চেৰ আৰু পাণ্ড্য।",
 ["Satavahanas ruled the Deccan|সাতবাহনে দাক্ষিণাত্য শাসন কৰিছিল", "Gautamiputra Satakarni was their greatest ruler|গৌতমীপুত্ৰ সাতকৰ্ণী শ্ৰেষ্ঠ শাসক", "Sangam poems are in Old Tamil|সংগম কবিতা প্ৰাচীন তামিলত", "Chola, Chera and Pandya ruled the Tamil lands|চোল, চেৰ আৰু পাণ্ড্যই তামিল ভূমি শাসন কৰিছিল"],
 S("Lords of the Deccan|দাক্ষিণাত্যৰ অধিপতি", "The <mark>Satavahanas</mark> held the Deccan from about the late 2nd century BCE. Their court used Prakrit.|<mark>সাতবাহনে</mark> প্ৰায় খ্ৰীষ্টপূৰ্ব দ্বিতীয় শতিকাৰ শেষৰ পৰা দাক্ষিণাত্য ধৰি ৰাখিছিল। ৰাজসভাত প্ৰাকৃত ব্যৱহাৰ হৈছিল।", "[[gautamiputra-satakarni|Gautamiputra Satakarni]] was the greatest. His mother's Nashik inscription praises his wins over Sakas and others.|[[gautamiputra-satakarni|গৌতমীপুত্ৰ সাতকৰ্ণী]] শ্ৰেষ্ঠ। মাতৃৰ নাশিক অভিলেখত শক আদিৰ ওপৰত জয়ৰ প্ৰশংসা আছে।", art="court"),
 S("Poems of the Tamil lands|তামিল ভূমিৰ কবিতা", "<mark>Sangam</mark> poems, in Old Tamil, are the earliest literature of the south, dated about 300 BCE to 300 CE.|প্ৰাচীন তামিলৰ <mark>সংগম</mark> কবিতা দক্ষিণৰ আদিতম সাহিত্য, প্ৰায় খ্ৰীষ্টপূৰ্ব ৩০০ৰ পৰা ৩০০ খ্ৰীষ্টাব্দ।", "They show three lines ruling: <mark>Chola, Chera and Pandya</mark>.|ইয়াত তিনিটা বংশ দেখা যায়: <mark>চোল, চেৰ আৰু পাণ্ড্য</mark>।", art="scroll"),
 MA([("Satavahanas|সাতবাহন", "Deccan|দাক্ষিণাত্য"), ("Sangam poems|সংগম কবিতা", "Old Tamil|প্ৰাচীন তামিল"), ("Kushans|কুষাণ", "North-west|উত্তৰ-পশ্চিম")], "Who, where.|কোন, ক'ত।"),
 OD("Which was NOT one of the three Tamil lines?|কোনটো তিনিটা তামিল বংশৰ এটা নহয়?", ["Chola|চোল", "Chera|চেৰ", "Pandya|পাণ্ড্য", "Shunga|শুংগ"], 3, "The Shungas ruled in the north.|শুংগই উত্তৰত শাসন কৰিছিল।"),
 TF("Sangam poetry is in Old Tamil.|সংগম কবিতা প্ৰাচীন তামিলত।", True, "It is the earliest literature of the south.|ই দক্ষিণৰ আদিতম সাহিত্য।"),
 WH(["I was a Satavahana ruler.|মই সাতবাহন শাসক।", "My mother's inscription is at Nashik.|মোৰ মাতৃৰ অভিলেখ নাশিকত।"], ["Kanishka|কনিষ্ক", "Gautamiputra Satakarni|গৌতমীপুত্ৰ সাতকৰ্ণী", "Harsha|হৰ্ষ", "Ajatashatru|অজাতশত্ৰু"], 1, "Gautamiputra Satakarni.|গৌতমীপুত্ৰ সাতকৰ্ণী।"),
 SP("The Satavahana court mainly used *Tamil.*|সাতবাহন ৰাজসভাত মূলতঃ *তামিল* ব্যৱহাৰ হৈছিল।", "Prakrit|প্ৰাকৃত", "Prakrit was the court language.|প্ৰাকৃত ৰাজসভাৰ ভাষা আছিল।"),
)
test = TEST("Map the powers after the Mauryas.|মৌৰ্যৰ পিছৰ শক্তিবোৰ স্থাপন কৰা।", "Recorded: Kushans, Satavahanas and the Tamil lines.|লিখা হ'ল: কুষাণ, সাতবাহন আৰু তামিল বংশ।",
 MA([("Kanishka|কনিষ্ক", "Kushan|কুষাণ"), ("Gautamiputra Satakarni|গৌতমীপুত্ৰ সাতকৰ্ণী", "Satavahana|সাতবাহন"), ("Pushyamitra|পুষ্যমিত্ৰ", "Shunga|শুংগ")], "Ruler and dynasty.|শাসক আৰু বংশ।"),
 IN("The main Kushan capital under Kanishka was|কনিষ্কৰ অধীনত কুষাণৰ মূল ৰাজধানী", ".|।", ["Purushapura|পুৰুষপুৰ", "Pataliputra|পাটলিপুত্ৰ", "Nashik|নাশিক", "Madurai|মাদুৰাই"], 0, "Purushapura.|পুৰুষপুৰ।"),
 TF("Begram's ivories were dug up in the 1930s.|বেগ্ৰামৰ হাতীদাঁত ১৯৩০ৰ দশকত উলিওৱা হৈছিল।", True, "Between 1936 and 1940.|১৯৩৬ৰ পৰা ১৯৪০ৰ ভিতৰত।"),
 MP("Tap Begram.|বেগ্ৰাম টিপা।", "begram", ["begram", "mathura", "pataliputra", "delhi"], "Afghanistan.|আফগানিস্তান।"),
 SP("Sangam poems are in *Sanskrit.*|সংগম কবিতা *সংস্কৃতত।*", "Old Tamil|প্ৰাচীন তামিল", "They are in Old Tamil.|এইবোৰ প্ৰাচীন তামিলত।"),
 MC("Consider these statements. (1) Gandhara art mixed Greek and Indian forms. (2) Historians now firmly link Kanishka to 78 CE. (3) Chola, Chera and Pandya appear in Sangam poems. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) গান্ধাৰ শিল্পত গ্ৰীক আৰু ভাৰতীয় ৰূপ মিহলি। (২) ইতিহাসবিদে এতিয়া কনিষ্কক ৭৮ খ্ৰীষ্টাব্দৰ সৈতে দৃঢ়ভাৱে জড়িত কৰে। (৩) সংগম কবিতাত চোল, চেৰ আৰু পাণ্ড্য আছে। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "The 78 CE link is no longer accepted.|৭৮ খ্ৰীষ্টাব্দৰ সম্পৰ্ক এতিয়া গ্ৰহণযোগ্য নহয়।"),
)
LESSON(6, "After the Mauryas|মৌৰ্যৰ পিছত", "c. 185 BCE–300 CE|প্ৰায় খ্ৰীষ্টপূৰ্ব ১৮৫–৩০০ খ্ৰীষ্টাব্দ", "Empires of the north|উত্তৰৰ সাম্ৰাজ্য", "Evidence file 6|প্ৰমাণ নথি ৬", "An empire breaks into regions|সাম্ৰাজ্য অঞ্চলত ভাগ হয়",
 "When the Mauryas fell, power moved to the north-west, the Deccan and the Tamil lands. Trace it through coins, ivories and poems.|মৌৰ্য পতনৰ পিছত ক্ষমতা উত্তৰ-পশ্চিম, দাক্ষিণাত্য আৰু তামিল ভূমিলৈ গ'ল। মুদ্ৰা, হাতীদাঁত আৰু কবিতাত অনুসৰণ কৰা।",
 sources, [u1, u2, u3], test, ["begram", "mathura", "pataliputra", "delhi"])
