#!/usr/bin/env python3
"""Lesson 11: The Delhi Sultanate."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "qutb-ud-din-aibak": ("person", "Qutb ud-Din Aibak|কুতুবউদ্দিন আইবক", "Founder of the Mamluk line in 1206|১২০৬ত মামলুক বংশৰ প্ৰতিষ্ঠাপক"),
 "iltutmish": ("person", "Iltutmish|ইলতুৎমিছ", "Sultan who completed the Qutb Minar|কুতুব মিনাৰ সম্পূৰ্ণ কৰা ছুলতান"),
 "razia-sultana": ("person", "Razia Sultana|ৰাজিয়া ছুলতানা", "Woman ruler at Delhi, 1236 to 1240|দিল্লীৰ মহিলা শাসক, ১২৩৬ৰ পৰা ১২৪০"),
 "alauddin-khalji": ("person", "Alauddin Khalji|আলাউদ্দিন খিলজী", "Khalji sultan known for price-controlled markets|মূল্য নিয়ন্ত্ৰিত বজাৰৰ বাবে খ্যাত খিলজী ছুলতান"),
 "muhammad-bin-tughluq": ("person", "Muhammad bin Tughluq|মহম্মদ বিন তুঘলক", "Sultan who moved the capital to Daulatabad|দৌলতাবাদলৈ ৰাজধানী নিয়া ছুলতান"),
 "ibn-battuta": ("person", "Ibn Battuta|ইবন বতুতা", "Moroccan traveller at Muhammad bin Tughluq's court|মহম্মদ বিন তুঘলকৰ সভাত থকা মৰক্কোৰ পৰ্যটক"),
 "daulatabad": ("place", "Daulatabad|দৌলতাবাদ", "Deccan fort, once Devagiri|দাক্ষিণাত্যৰ দুৰ্গ, পূৰ্বৰ দেৱগিৰি", [19.94, 75.21]),
 "panipat": ("place", "Panipat|পানিপথ", "Battlefield north of Delhi|দিল্লীৰ উত্তৰৰ ৰণক্ষেত্ৰ", [29.39, 76.97]),
})
sources = [
 src("Wikipedia, Delhi Sultanate", "https://en.wikipedia.org/wiki/Delhi_Sultanate", "Used as a guide: five dynasties and dates, Iltutmish, Razia, Alauddin, Muhammad bin Tughluq, Firoz Shah, Timur, 1526. Check in review."),
 src("Wikipedia, Nalanda mahavihara", "https://en.wikipedia.org/wiki/Nalanda_mahavihara", "Used as a guide for Bakhtiyar Khalji's attributed role. Check in review."),
]
u1 = U(1, "crown", "Five dynasties|পাঁচটা বংশ",
 "Learn the five dynasties in order.|পাঁচটা বংশ ক্ৰমে শিকা।", "Finding recorded: Mamluk, Khalji, Tughlaq, Sayyid, Lodi.|প্ৰমাণ লিখা হ'ল: মামলুক, খিলজী, তুঘলক, চৈয়দ, লোদী।",
 ["The Sultanate began in 1206|ছুলতানী ১২০৬ত আৰম্ভ হৈছিল", "The order is Mamluk, Khalji, Tughlaq, Sayyid, Lodi|ক্ৰম মামলুক, খিলজী, তুঘলক, চৈয়দ, লোদী", "Qutb ud-Din Aibak founded the first line|কুতুবউদ্দিন আইবকে প্ৰথম বংশ গঢ়িছিল", "It ended at Panipat in 1526|১৫২৬ত পানিপথত ই শেষ হৈছিল"],
 S("From slave to sultan|দাসৰ পৰা ছুলতান", "[[qutb-ud-din-aibak|Qutb ud-Din Aibak]], once a slave of Muhammad of Ghor, began the <mark>Mamluk</mark> line in <mark>1206</mark>.|মহম্মদ ঘোৰীৰ দাস [[qutb-ud-din-aibak|কুতুবউদ্দিন আইবকে]] <mark>১২০৬ত</mark> <mark>মামলুক</mark> বংশ আৰম্ভ কৰিছিল।", art="court"),
 S("A memory line|মনত ৰখাৰ ক্ৰম", "Five dynasties ruled at [[delhi]]: <b>Mamluk, Khalji, Tughlaq, Sayyid, Lodi</b>.|[[delhi|দিল্লীত]] পাঁচটা বংশই শাসন কৰিছিল: <b>মামলুক, খিলজী, তুঘলক, চৈয়দ, লোদী</b>।", "The last, Ibrahim Lodi, fell to Babur at [[panipat]] in <mark>1526</mark>.|শেষ জন ইব্ৰাহিম লোদী <mark>১৫২৬ত</mark> [[panipat|পানিপথত]] বাবৰৰ হাতত পৰাস্ত হৈছিল।", art="calendar"),
 OR("Put the five dynasties in order.|পাঁচটা বংশ ক্ৰমে সজোৱা।", ["Mamluk|মামলুক", "Khalji|খিলজী", "Tughlaq|তুঘলক", "Sayyid|চৈয়দ", "Lodi|লোদী"], "1206 to 1526.|১২০৬ৰ পৰা ১৫২৬।"),
 IN("The Delhi Sultanate began in|দিল্লী ছুলতানী আৰম্ভ হৈছিল", ".|ত।", ["1192|১১৯২", "1206|১২০৬", "1290|১২৯০", "1526|১৫২৬"], 1, "1206.|১২০৬।"),
 TF("The Lodis were the last Sultanate dynasty.|লোদী ছুলতানীৰ শেষ বংশ।", True, "Babur ended their rule in 1526.|১৫২৬ত বাবৰে তেওঁলোকৰ শাসন শেষ কৰিছিল।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1206, "Sultanate begins|ছুলতানী আৰম্ভ"), (1526, "First Panipat|পানিপথৰ প্ৰথম যুদ্ধ")], [("Razia on the throne, 1236|সিংহাসনত ৰাজিয়া, ১২৩৬", 1), ("Timur sacks Delhi, 1398|তিমুৰৰ দিল্লী লুণ্ঠন, ১৩৯৮", 1), ("Chola raids on Srivijaya, 1025|শ্ৰীবিজয়ত চোল অভিযান, ১০২৫", 0)], "1025 → 1206 → 1236 → 1398 → 1526.|১০২৫ → ১২০৬ → ১২৩৬ → ১৩৯৮ → ১৫২৬।"),
 SP("The first dynasty was the *Lodi* line.|প্ৰথম বংশ *লোদী।*", "Mamluk|মামলুক", "The Mamluks came first.|মামলুক প্ৰথম।"),
)
u2 = U(2, "star", "Razia and Iltutmish|ৰাজিয়া আৰু ইলতুৎমিছ",
 "Meet the woman on Delhi's throne.|দিল্লীৰ সিংহাসনৰ মহিলাগৰাকীক চিনি পোৱা।", "Finding recorded: Razia ruled from 1236 to 1240.|প্ৰমাণ লিখা হ'ল: ৰাজিয়াই ১২৩৬ৰ পৰা ১২৪০লৈ শাসন কৰিছিল।",
 ["Iltutmish was Aibak's son-in-law|ইলতুৎমিছ আইবকৰ জোঁৱাই", "He completed the Qutb Minar|তেওঁ কুতুব মিনাৰ সম্পূৰ্ণ কৰিছিল", "Razia Sultana ascended the throne at Delhi|ৰাজিয়া ছুলতানা দিল্লীৰ সিংহাসনত বহিছিল", "She ruled from 1236 to 1240|তেওঁ ১২৩৬ৰ পৰা ১২৪০লৈ শাসন কৰিছিল"],
 S("Finishing the Minar|মিনাৰ সম্পূৰ্ণ", "<mark>[[iltutmish|Iltutmish]]</mark>, Aibak's son-in-law, ruled from 1211 to 1236 and completed the <mark>Qutb Minar</mark>.|আইবকৰ জোঁৱাই <mark>[[iltutmish|ইলতুৎমিছে]]</mark> ১২১১ৰ পৰা ১২৩৬লৈ শাসন কৰি <mark>কুতুব মিনাৰ</mark> সম্পূৰ্ণ কৰিছিল।", art="houses"),
 S("A woman on the throne|সিংহাসনত মহিলা", "<mark>[[razia-sultana|Razia Sultana]]</mark> ruled at Delhi from 1236 to 1240, one of few women rulers in Islamic history.|<mark>[[razia-sultana|ৰাজিয়া ছুলতানাই]]</mark> ১২৩৬ৰ পৰা ১২৪০লৈ দিল্লীত শাসন কৰিছিল, ইছলামী ইতিহাসৰ অলপ মহিলা শাসকৰ এগৰাকী।", "Papers set her beside Chand Bibi, Ahilya Bai and Lakshmi Bai. Only Razia ruled at Delhi.|পৰীক্ষাত তেওঁক চান্দ বিবি, অহল্যা বাই আৰু লক্ষ্মীবাইৰ লগত দিয়ে। কেৱল ৰাজিয়াই দিল্লীত শাসন কৰিছিল।", art="court"),
 IN("The woman who ascended the throne at Delhi was|দিল্লীৰ সিংহাসনত বহা মহিলাগৰাকী", ".|।", ["Chand Bibi|চান্দ বিবি", "Rani Ahilya Bai|ৰাণী অহল্যা বাই", "Razia Sultana|ৰাজিয়া ছুলতানা", "Rani Laxmi Bai|ৰাণী লক্ষ্মীবাই"], 2, "Razia Sultana.|ৰাজিয়া ছুলতানা।"),
 WH(["I was Aibak's son-in-law.|মই আইবকৰ জোঁৱাই।", "I completed the Qutb Minar.|মই কুতুব মিনাৰ সম্পূৰ্ণ কৰিছিলোঁ।"], ["Iltutmish|ইলতুৎমিছ", "Balban|বলবন", "Firoz Shah|ফিৰোজ শ্বাহ", "Sikandar Lodi|চিকন্দৰ লোদী"], 0, "Iltutmish.|ইলতুৎমিছ।"),
 TF("Razia Sultana belonged to the Lodi dynasty.|ৰাজিয়া ছুলতানা লোদী বংশৰ।", False, "She belonged to the Mamluk line.|তেওঁ মামলুক বংশৰ।"),
 SC("Unscramble the sultan who finished the Minar.|মিনাৰ সম্পূৰ্ণ কৰা ছুলতানক সজোৱা।", "ILTUTMISH", ["ইল", "তুৎ", "মিছ"], "Iltutmish.|ইলতুৎমিছ।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Aibak|আইবক", "Iltutmish|ইলতুৎমিছ", "Razia|ৰাজিয়া"], "1206, 1211, 1236.|১২০৬, ১২১১, ১২৩৬।"),
)
u3 = U(3, "star", "Markets and a moved capital|বজাৰ আৰু স্থানান্তৰিত ৰাজধানী",
 "Contrast Alauddin's and Tughluq's experiments.|আলাউদ্দিন আৰু তুঘলকৰ পৰীক্ষা তুলনা কৰা।", "Finding recorded: Alauddin fixed prices; Tughluq moved the capital and issued token coins.|প্ৰমাণ লিখা হ'ল: আলাউদ্দিনে মূল্য বান্ধিলে; তুঘলকে ৰাজধানী সলালে আৰু প্ৰতীকী মুদ্ৰা উলিয়ালে।",
 ["Alauddin Khalji ran price-controlled markets|আলাউদ্দিন খিলজীয়ে মূল্য নিয়ন্ত্ৰিত বজাৰ চলাইছিল", "He raised farm taxes to half the produce|তেওঁ কৃষি কৰ উৎপাদনৰ আধালৈ বঢ়াইছিল", "Muhammad bin Tughluq moved the capital to Daulatabad|মহম্মদ বিন তুঘলকে দৌলতাবাদলৈ ৰাজধানী নিছিল", "His token coins failed through counterfeiting|তেওঁৰ প্ৰতীকী মুদ্ৰা জাল হৈ বিফল হৈছিল"],
 S("Fixed prices|বান্ধি দিয়া মূল্য", "[[alauddin-khalji|Alauddin Khalji]] set up government-run <mark>markets</mark> with controlled prices, and raised farm taxes to half the produce.|[[alauddin-khalji|আলাউদ্দিন খিলজীয়ে]] চৰকাৰী <mark>বজাৰ</mark> আৰু নিয়ন্ত্ৰিত মূল্য চলাইছিল, কৃষি কৰ আধালৈ বঢ়াইছিল।", "He also faced repeated Mongol raids.|তেওঁ বাৰে বাৰে মোংগল আক্ৰমণৰ সন্মুখীন হৈছিল।", art="houses"),
 S("A capital on the move|স্থানান্তৰিত ৰাজধানী", "[[muhammad-bin-tughluq|Muhammad bin Tughluq]] moved the capital to <mark>[[daulatabad|Daulatabad]]</mark>, forcing Delhi's elite to go.|[[muhammad-bin-tughluq|মহম্মদ বিন তুঘলকে]] <mark>[[daulatabad|দৌলতাবাদলৈ]]</mark> ৰাজধানী নিছিল, দিল্লীৰ অভিজাতক যাবলৈ বাধ্য কৰিছিল।", "His base-metal <mark>token coins</mark> failed when people forged them. [[ibn-battuta|Ibn Battuta]] served at his court.|তেওঁৰ ধাতুৰ <mark>প্ৰতীকী মুদ্ৰা</mark> মানুহে জাল কৰাত বিফল হৈছিল। [[ibn-battuta|ইবন বতুতাই]] তেওঁৰ সভাত সেৱা আগবঢ়াইছিল।", map={"base": "india", "box": [66, 18, 85, 30.5], "show": ["delhi", "daulatabad"]}),
 IN("The explorer who visited India during Muhammad bin Tughluq's reign was|মহম্মদ বিন তুঘলকৰ ৰাজত্বত ভাৰতলৈ অহা পৰ্যটক", ".|।", ["Faxian|ফা-হিয়েন", "Xuanzang|হিউৱেন চাঙ", "Vasco da Gama|ভাস্কো দা গামা", "Ibn Battuta|ইবন বতুতা"], 3, "Ibn Battuta.|ইবন বতুতা।"),
 MA([("Alauddin Khalji|আলাউদ্দিন খিলজী", "Price-controlled markets|মূল্য নিয়ন্ত্ৰিত বজাৰ"), ("Muhammad bin Tughluq|মহম্মদ বিন তুঘলক", "Token coins|প্ৰতীকী মুদ্ৰা"), ("Firoz Shah Tughlaq|ফিৰোজ শ্বাহ তুঘলক", "Yamuna canal|যমুনা খাল")], "Ruler and policy.|শাসক আৰু নীতি।"),
 MP("Tap Daulatabad.|দৌলতাবাদ টিপা।", "daulatabad", ["daulatabad", "delhi", "bodh-gaya", "panipat"], "In the Deccan.|দাক্ষিণাত্যত।") ,
 TF("Muhammad bin Tughluq's token coins were a lasting success.|মহম্মদ বিন তুঘলকৰ প্ৰতীকী মুদ্ৰা স্থায়ী সফলতা আছিল।", False, "They failed through counterfeiting.|জাল হৈ বিফল হৈছিল।"),
 SP("Ibn Battuta came from *Persia.*|ইবন বতুতা *পাৰস্যৰ* পৰা আহিছিল।", "Morocco|মৰক্কোৰ", "He came from Morocco.|তেওঁ মৰক্কোৰ পৰা আহিছিল।"),
)
u4 = U(4, "moon", "The Sultanate and Kamarupa|ছুলতানী আৰু কামৰূপ",
 "Connect Delhi's politics with the east.|দিল্লীৰ ৰাজনীতি পূবৰ সৈতে জোৰা লগোৱা।", "Finding recorded: armies from the west turned back in Assam, and Timur broke Delhi in 1398.|প্ৰমাণ লিখা হ'ল: পশ্চিমৰ সৈন্য অসমৰ পৰা ঘূৰি গৈছিল, ১৩৯৮ত তিমুৰে দিল্লী ভাঙিছিল।",
 ["Bakhtiyar Khalji led a march towards Tibet through Kamarupa|বখতিয়াৰ খিলজীয়ে কামৰূপৰ বাটে তিব্বতলৈ অভিযান কৰিছিল", "That march failed|সেই অভিযান বিফল হৈছিল", "Timur plundered Delhi in 1398|১৩৯৮ত তিমুৰে দিল্লী লুণ্ঠন কৰিছিল", "The Sultanate never recovered its old reach|ছুলতানীয়ে পুৰণি বিস্তাৰ পুনৰ নাপালে"],
 LINK(S("A march that failed|বিফল অভিযান", "Early in the 13th century Bakhtiyar Khalji marched through Kamarupa towards Tibet, and his force was destroyed on the way back.|ত্ৰয়োদশ শতিকাৰ আৰম্ভণিতে বখতিয়াৰ খিলজীয়ে কামৰূপৰ বাটে তিব্বতলৈ অভিযান কৰিছিল, উভতি অহাৰ পথত তেওঁৰ সৈন্য ধ্বংস হৈছিল।", "Later armies from Bengal also struggled against the rivers and rains of the Brahmaputra valley.|পিছৰ বংগৰ সৈন্যইও ব্ৰহ্মপুত্ৰ উপত্যকাৰ নদী আৰু বৰষুণৰ সন্মুখত সংগ্ৰাম কৰিছিল।", art="embassy"),
  "medieval-01", 14, 1, "A march that failed|বিফল অভিযান", "The Assam History course tells these raids from Kamarupa's side.|অসমৰ ইতিহাস পাঠ্যক্ৰমত এই অভিযান কামৰূপৰ ফালৰ পৰা কোৱা হৈছে।"),
 S("Timur at Delhi|দিল্লীত তিমুৰ", "In <mark>1398</mark> Timur's army plundered Delhi. The Sultanate was left in chaos, and the Sayyids began as vassals of the Timurids.|<mark>১৩৯৮ত</mark> তিমুৰৰ সৈন্যই দিল্লী লুণ্ঠন কৰিছিল। ছুলতানী বিশৃংখল হ'ল, আৰু চৈয়দ বংশ তিমুৰীয় অধীনত আৰম্ভ হৈছিল।", art="calendar"),
 TF("Bakhtiyar Khalji's march through Kamarupa succeeded.|কামৰূপৰ বাটে বখতিয়াৰ খিলজীৰ অভিযান সফল হৈছিল।", False, "It failed.|ই বিফল হৈছিল।"),
 IN("Timur plundered Delhi in|তিমুৰে দিল্লী লুণ্ঠন কৰিছিল", ".|ত।", ["1206|১২০৬", "1320|১৩২০", "1398|১৩৯৮", "1526|১৫২৬"], 2, "1398.|১৩৯৮।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Sultanate begins|ছুলতানী আৰম্ভ", "Timur at Delhi|দিল্লীত তিমুৰ", "First Panipat|পানিপথৰ প্ৰথম যুদ্ধ"], "1206, 1398, 1526.|১২০৬, ১৩৯৮, ১৫২৬।"),
 OD("Which was NOT a Sultanate dynasty?|কোনটো ছুলতানীৰ বংশ নহয়?", ["Khalji|খিলজী", "Tughlaq|তুঘলক", "Mughal|মোগল", "Lodi|লোদী"], 2, "The Mughals followed the Sultanate.|ছুলতানীৰ পিছত মোগল আহিল।"),
 WH(["I came after the Tughlaqs.|মই তুঘলকৰ পিছত আহিলোঁ।", "I began as a vassal of the Timurids.|মই তিমুৰীয়ৰ অধীনত আৰম্ভ কৰিছিলোঁ।", "The Lodis followed me.|মোৰ পিছত লোদী আহিল।"], ["Mamluk|মামলুক", "Khalji|খিলজী", "Sayyid|চৈয়দ", "Mughal|মোগল"], 2, "The Sayyids.|চৈয়দ।"),
)
test = TEST("Rule Delhi for three centuries in six questions.|ছটা প্ৰশ্নত তিনি শতিকা দিল্লী শাসন কৰা।", "Recorded: dynasties, rulers and policies.|লিখা হ'ল: বংশ, শাসক আৰু নীতি।",
 OR("Order the dynasties.|বংশবোৰ সজোৱা।", ["Mamluk|মামলুক", "Khalji|খিলজী", "Tughlaq|তুঘলক", "Sayyid|চৈয়দ", "Lodi|লোদী"], "That order.|এই ক্ৰমত।"),
 IN("The ruler who ascended the throne at Delhi was|দিল্লীৰ সিংহাসনত বহা শাসক আছিল", ".|।", ["Chand Bibi|চান্দ বিবি", "Rezia Sultana|ৰাজিয়া ছুলতানা", "Rani Ahilya Bai|ৰাণী অহল্যা বাই", "Rani Laxmi Bai|ৰাণী লক্ষ্মীবাই"], 1, "Razia.|ৰাজিয়া।"),
 MA([("Ibn Battuta|ইবন বতুতা", "Muhammad bin Tughluq|মহম্মদ বিন তুঘলক"), ("Xuanzang|হিউৱেন চাঙ", "Harsha|হৰ্ষ"), ("Faxian|ফা-হিয়েন", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়")], "The traveller table grows.|পৰ্যটকৰ তালিকা বাঢ়ে।"),
 TF("Alauddin Khalji set up controlled markets.|আলাউদ্দিন খিলজীয়ে নিয়ন্ত্ৰিত বজাৰ পাতিছিল।", True, "Yes.|হয়।"),
 MP("Tap the Deccan capital of Muhammad bin Tughluq.|মহম্মদ বিন তুঘলকৰ দাক্ষিণাত্যৰ ৰাজধানী টিপা।", "daulatabad", ["daulatabad", "delhi", "bodh-gaya", "panipat"], "Daulatabad.|দৌলতাবাদ।"),
 MC("Consider these statements. (1) Qutb ud-Din Aibak began the Mamluk line. (2) Iltutmish completed the Qutb Minar. (3) The Sayyids ended at Panipat in 1526. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) কুতুবউদ্দিন আইবকে মামলুক বংশ আৰম্ভ কৰিছিল। (২) ইলতুৎমিছে কুতুব মিনাৰ সম্পূৰ্ণ কৰিছিল। (৩) ১৫২৬ত পানিপথত চৈয়দ বংশ শেষ হৈছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 0, "The Lodis fell at Panipat.|পানিপথত লোদী পৰাস্ত হৈছিল।"),
)
LESSON(11, "The Delhi Sultanate|দিল্লী ছুলতানী", "1206–1526|১২০৬–১৫২৬", "Sultans, Deccan and devotion|ছুলতান, দাক্ষিণাত্য আৰু ভক্তি", "Evidence file 11|প্ৰমাণ নথি ১১", "Five dynasties, one throne|পাঁচটা বংশ, এখন সিংহাসন",
 "Five dynasties held Delhi for three centuries. Learn their order, their experiments and why armies from the west failed in the east.|পাঁচটা বংশই তিনি শতিকা দিল্লী ধৰি ৰাখিছিল। ক্ৰম, পৰীক্ষা আৰু পশ্চিমৰ সৈন্য পূবত কিয় বিফল হৈছিল, শিকা।",
 sources, [u1, u2, u3, u4], test, ["delhi", "daulatabad", "panipat", "bodh-gaya"],
 timeline=[("1206", "Delhi Sultanate begins|দিল্লী ছুলতানী আৰম্ভ", "u1"), ("1236", "Razia Sultana takes the throne|ৰাজিয়া ছুলতানা সিংহাসনত", "u2"), ("1398", "Timur plunders Delhi|তিমুৰৰ দিল্লী লুণ্ঠন", "u4"), ("1526", "First Battle of Panipat|পানিপথৰ প্ৰথম যুদ্ধ", "u1")])
