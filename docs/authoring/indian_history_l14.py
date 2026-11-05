#!/usr/bin/env python3
"""Lesson 14: Babur and Sher Shah."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "babur": ("person", "Babur|বাবৰ", "Founder of the Mughal Empire, winner at Panipat in 1526|মোগল সাম্ৰাজ্যৰ প্ৰতিষ্ঠাপক, ১৫২৬ত পানিপথৰ বিজয়ী"),
 "ibrahim-lodi": ("person", "Ibrahim Lodi|ইব্ৰাহিম লোদী", "Last Sultan of Delhi|দিল্লীৰ শেষ ছুলতান"),
 "rana-sanga": ("person", "Rana Sanga|ৰাণা সংগ", "Ruler of Mewar who fought Babur at Khanwa in 1527|১৫২৭ত খানুৱাত বাবৰৰ সৈতে যুঁজা মেৱাৰৰ শাসক"),
 "humayun": ("person", "Humayun|হুমায়ুন", "Second Mughal emperor, driven out by Sher Shah|দ্বিতীয় মোগল সম্ৰাট, শ্বেৰ শ্বাহে খেদি পঠাইছিল"),
 "sher-shah-suri": ("person", "Sher Shah Suri|শ্বেৰ শ্বাহ সূৰী", "Ruler of Hindustan from 1540 to 1545|১৫৪০ৰ পৰা ১৫৪৫লৈ হিন্দুস্তানৰ শাসক"),
 "sasaram": ("place", "Sasaram|সাসাৰাম", "Bihar town with Sher Shah's tomb|শ্বেৰ শ্বাহৰ সমাধি থকা বিহাৰৰ নগৰ", [24.95, 84.03]),
 "chausa": ("place", "Chausa|চৌসা", "Bihar site of Sher Shah's victory of 1539|১৫৩৯ত শ্বেৰ শ্বাহৰ জয়ৰ বিহাৰৰ স্থান", [25.52, 83.9]),
 "khanwa": ("place", "Khanwa|খানুৱা", "Rajasthan battlefield of 1527|১৫২৭ৰ ৰাজস্থানৰ ৰণক্ষেত্ৰ", [27.03, 77.54]),
})
sources = [
 src("Wikipedia, First Battle of Panipat", "https://en.wikipedia.org/wiki/First_Battle_of_Panipat", "Used as a guide: 21 April 1526, muskets and cannon, Khanwa. Check in review."),
 src("Wikipedia, Sher Shah Suri", "https://en.wikipedia.org/wiki/Sher_Shah_Suri", "Used as a guide: Chausa, Kannauj, rupiya, the older road he rebuilt, Sasaram, 1545. Check in review."),
 src("Babur-nama in English, translated by A. S. Beveridge, 1922", "https://archive.org/details/baburnamainengli02babuuoft", "Located, not read. Check the Panipat account against it in review."),
]
u1 = U(1, "flag", "Panipat, 1526|পানিপথ, ১৫২৬",
 "Find out how a small army took Delhi.|সৰু সৈন্যবাহিনীয়ে দিল্লী কেনেকৈ ল'লে, বিচাৰি উলিওৱা।", "Finding recorded: guns and cannon helped Babur beat Ibrahim Lodi.|প্ৰমাণ লিখা হ'ল: বন্দুক আৰু কামানে বাবৰক ইব্ৰাহিম লোদীক হৰুৱাত সহায় কৰিছিল।",
 ["Babur founded the Mughal Empire|বাবৰে মোগল সাম্ৰাজ্য প্ৰতিষ্ঠা কৰিছিল", "He beat Ibrahim Lodi at Panipat on 21 April 1526|১৫২৬ৰ ২১ এপ্ৰিলত পানিপথত ইব্ৰাহিম লোদীক হৰুৱাইছিল", "He used muskets and cannon|তেওঁ বন্দুক আৰু কামান ব্যৱহাৰ কৰিছিল", "That ended the Delhi Sultanate|ইয়াৰে দিল্লী ছুলতানীৰ অন্ত পৰিল"],
 S("Twelve thousand against many more|বাৰ হাজাৰ বনাম বহু বেছি", "On 21 April <mark>1526</mark> [[babur|Babur]] met [[ibrahim-lodi|Ibrahim Lodi]] at [[panipat]]. Babur's force was about 12,000, far smaller than the Sultan's.|<mark>১৫২৬ৰ</mark> ২১ এপ্ৰিলত [[babur|বাবৰে]] [[panipat|পানিপথত]] [[ibrahim-lodi|ইব্ৰাহিম লোদীক]] সন্মুখীন হৈছিল। বাবৰৰ সৈন্য প্ৰায় ১২,০০০, ছুলতানৰতকৈ বহু কম।", art="embassy"),
 S("Guns behind the wagons|গাড়ীৰ আঁৰত বন্দুক", "Babur used <mark>muskets and cannon</mark> from behind a line of wagons, and the noise panicked Ibrahim's elephants.|বাবৰে গাড়ীৰ শাৰীৰ আঁৰৰ পৰা <mark>বন্দুক আৰু কামান</mark> ব্যৱহাৰ কৰিছিল, শব্দত ইব্ৰাহিমৰ হাতী ত্ৰস্ত হৈছিল।", "Ibrahim was killed, and the <mark>Delhi Sultanate</mark> ended.|ইব্ৰাহিম নিহত হ'ল, <mark>দিল্লী ছুলতানীৰ</mark> অন্ত পৰিল।", art="court"),
 IN("The founder of the Mughal Empire in India was|ভাৰতত মোগল সাম্ৰাজ্যৰ প্ৰতিষ্ঠাপক", ".|।", ["Humayun|হুমায়ুন", "Sher Shah Suri|শ্বেৰ শ্বাহ সূৰী", "Babur|বাবৰ", "Akbar|আকবৰ"], 2, "Babur.|বাবৰ।"),
 TF("Ibrahim Lodi had more soldiers than Babur.|ইব্ৰাহিম লোদীৰ সৈন্য বাবৰতকৈ বেছি আছিল।", True, "Babur won with far fewer men.|বাবৰে বহু কম সৈন্যৰে জয়ী হৈছিল।"),
 MP("Tap Panipat.|পানিপথ টিপা।", "panipat", ["panipat", "sasaram", "khanwa", "surat"], "North of Delhi, in Haryana.|দিল্লীৰ উত্তৰে, হাৰিয়ানাত।"),
 SP("The First Battle of Panipat was fought in *1556.*|পানিপথৰ প্ৰথম যুদ্ধ *১৫৫৬ত* হৈছিল।", "1526|১৫২৬ত", "1556 is the second battle.|১৫৫৬ দ্বিতীয় যুদ্ধ।"),
 WH(["I was the last Sultan of Delhi.|মই দিল্লীৰ শেষ ছুলতান।", "I was a Lodi.|মই লোদী।", "I died at Panipat.|মই পানিপথত মৃত্যুবৰণ কৰিছিলোঁ।"], ["Iltutmish|ইলতুৎমিছ", "Firoz Shah|ফিৰোজ শ্বাহ", "Ibrahim Lodi|ইব্ৰাহিম লোদী", "Hemu|হেমু"], 2, "Ibrahim Lodi.|ইব্ৰাহিম লোদী।"),
)
u2 = U(2, "flag", "Khanwa and Humayun|খানুৱা আৰু হুমায়ুন",
 "See how nearly the Mughals lost India.|মোগলসকলে ভাৰত প্ৰায় কেনেকৈ হেৰুৱাইছিল, চোৱা।", "Finding recorded: Babur won Khanwa, but Humayun lost to Sher Shah.|প্ৰমাণ লিখা হ'ল: বাবৰে খানুৱা জিকিলে, কিন্তু হুমায়ুন শ্বেৰ শ্বাহৰ ওচৰত হাৰিল।",
 ["Babur beat Rana Sanga at Khanwa in 1527|১৫২৭ত খানুৱাত বাবৰে ৰাণা সংগক হৰুৱাইছিল", "Humayun followed Babur|বাবৰৰ পিছত হুমায়ুন", "Sher Shah beat him at Chausa in 1539|১৫৩৯ত চৌসাত শ্বেৰ শ্বাহে তেওঁক হৰুৱাইছিল", "Kannauj in 1540 forced him out|১৫৪০ত কনৌজৰ পৰা তেওঁ খেদা খালে"],
 S("One more battle|আৰু এটা যুদ্ধ", "Panipat was not the end. In 1527 Babur still had to fight [[rana-sanga|Rana Sanga]] of Mewar at <mark>[[khanwa|Khanwa]]</mark>.|পানিপথেই শেষ নাছিল। ১৫২৭ত বাবৰে মেৱাৰৰ [[rana-sanga|ৰাণা সংগৰ]] সৈতে <mark>[[khanwa|খানুৱাত]]</mark> যুঁজিব লগা হৈছিল।", art="embassy"),
 S("An emperor in flight|পলায়নত সম্ৰাট", "[[humayun|Humayun]] lost to [[sher-shah-suri|Sher Shah]] at <mark>[[chausa|Chausa]]</mark> in 1539 and at <mark>[[kannauj|Kannauj]]</mark> in 1540, and had to flee.|[[humayun|হুমায়ুন]] ১৫৩৯ত <mark>[[chausa|চৌসাত]]</mark> আৰু ১৫৪০ত <mark>[[kannauj|কনৌজত]]</mark> [[sher-shah-suri|শ্বেৰ শ্বাহৰ]] ওচৰত হাৰি পলাবলৈ বাধ্য হৈছিল।", map={"base": "india", "box": [75, 23, 87, 30.5], "show": ["chausa", "kannauj", "delhi"]}),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["First Panipat|পানিপথৰ প্ৰথম যুদ্ধ", "Khanwa|খানুৱা", "Chausa|চৌসা", "Kannauj|কনৌজ"], "1526, 1527, 1539, 1540.|১৫২৬, ১৫২৭, ১৫৩৯, ১৫৪০।"),
 MA([("Khanwa|খানুৱা", "Rana Sanga|ৰাণা সংগ"), ("First Panipat|পানিপথৰ প্ৰথম যুদ্ধ", "Ibrahim Lodi|ইব্ৰাহিম লোদী"), ("Chausa|চৌসা", "Humayun loses|হুমায়ুনৰ পৰাজয়")], "Battle and opponent.|যুদ্ধ আৰু প্ৰতিপক্ষ।"),
 TF("Humayun defeated Sher Shah at Chausa.|চৌসাত হুমায়ুনে শ্বেৰ শ্বাহক হৰুৱাইছিল।", False, "Sher Shah won.|শ্বেৰ শ্বাহ জয়ী হৈছিল।"),
 IN("Babur fought Rana Sanga at|বাবৰে ৰাণা সংগৰ সৈতে যুঁজিছিল", ".|ত।", ["Panipat|পানিপথ", "Khanwa|খানুৱা", "Chausa|চৌসা", "Kannauj|কনৌজ"], 1, "Khanwa, 1527.|১৫২৭ত খানুৱা।"),
 SC("Unscramble the second Mughal emperor.|দ্বিতীয় মোগল সম্ৰাটক সজোৱা।", "HUMAYUN", ["হু", "মা", "য়ুন"], "Humayun.|হুমায়ুন।"),
)
u3 = U(3, "walk", "A road and a coin|এটা পথ আৰু এটা মুদ্ৰা",
 "See why a five-year reign is still asked.|পাঁচ বছৰৰ ৰাজত্ব এতিয়াও কিয় সোধা হয়, চোৱা।", "Finding recorded: Sher Shah rebuilt the Grand Trunk Road and issued the rupiya.|প্ৰমাণ লিখা হ'ল: শ্বেৰ শ্বাহে গ্ৰেণ্ড ট্ৰাংক ৰোড পুনৰ গঢ়িছিল আৰু ৰুপিয়া উলিয়াইছিল।",
 ["Sher Shah ruled from 1540 to 1545|শ্বেৰ শ্বাহে ১৫৪০ৰ পৰা ১৫৪৫লৈ শাসন কৰিছিল", "Papers credit him with the Grand Trunk Road|পৰীক্ষাত গ্ৰেণ্ড ট্ৰাংক ৰোডৰ কৃতিত্ব তেওঁক দিয়ে", "He rebuilt an older route|তেওঁ পুৰণি পথ এটা পুনৰ গঢ়িছিল", "His silver rupiya came before the modern rupee|তেওঁৰ ৰূপৰ ৰুপিয়া আধুনিক টকাৰ পূৰ্বসূৰী"],
 S("Road with rest-houses|জিৰণি ঘৰ থকা পথ", "Papers name <mark>[[sher-shah-suri|Sher Shah]]</mark> for the Grand Trunk Road. The route was older, and he greatly rebuilt it.|পৰীক্ষাত গ্ৰেণ্ড ট্ৰাংক ৰোডৰ বাবে <mark>[[sher-shah-suri|শ্বেৰ শ্বাহৰ]]</mark> নাম লোৱা হয়। পথটো পুৰণি, তেওঁ ইয়াক ব্যাপকভাৱে পুনৰ গঢ়িছিল।", "He added rest-houses, wells, shade trees and a relay post.|তেওঁ জিৰণি ঘৰ, নাদ, ছাঁৰ গছ আৰু ডাক ব্যৱস্থা যোগ কৰিছিল।", art="houses"),
 S("The silver rupiya|ৰূপৰ ৰুপিয়া", "His silver <mark>rupiya</mark> of about 178 grains came before the modern rupee.|প্ৰায় ১৭৮ গ্ৰেইনৰ তেওঁৰ ৰূপৰ <mark>ৰুপিয়া</mark> আধুনিক টকাৰ পূৰ্বসূৰী।", "He died at Kalinjar in 1545 and lies at [[sasaram]], in a tomb set in a lake.|১৫৪৫ত কালিঞ্জৰত তেওঁৰ মৃত্যু হয়, [[sasaram|সাসাৰামত]] হ্ৰদৰ মাজৰ সমাধিত আছে।", art="seal"),
 IN("The Grand Trunk Road is credited to|গ্ৰেণ্ড ট্ৰাংক ৰোডৰ কৃতিত্ব দিয়া হয়", ".|ক।", ["Akbar|আকবৰ", "Jahangir|জাহাংগীৰ", "Qutb ud-Din Aibak|কুতুবউদ্দিন আইবক", "Sher Shah Suri|শ্বেৰ শ্বাহ সূৰী"], 3, "Sher Shah, who rebuilt it.|শ্বেৰ শ্বাহ, যি ইয়াক পুনৰ গঢ়িছিল।"),
 TF("Sher Shah built the Grand Trunk Road from nothing.|শ্বেৰ শ্বাহে শূন্যৰ পৰা গ্ৰেণ্ড ট্ৰাংক ৰোড বনাইছিল।", False, "He rebuilt and improved an existing route.|তেওঁ থকা পথ এটা পুনৰ গঢ়ি উন্নত কৰিছিল।"),
 MP("Tap Sher Shah's tomb town.|শ্বেৰ শ্বাহৰ সমাধিৰ নগৰখন টিপা।", "sasaram", ["sasaram", "panipat", "khanwa", "surat"], "Sasaram, in Bihar.|বিহাৰৰ সাসাৰাম।"),
 SP("Sher Shah's coin was the gold *dinar.*|শ্বেৰ শ্বাহৰ মুদ্ৰা সোণৰ *দিনাৰ।*", "rupiya|ৰুপিয়া", "It was the silver rupiya.|ই ৰূপৰ ৰুপিয়া।"),
 OD("Which was NOT added along Sher Shah's road?|শ্বেৰ শ্বাহৰ পথত কোনটো যোগ কৰা হোৱা নাছিল?", ["Rest-houses|জিৰণি ঘৰ", "Wells|নাদ", "Shade trees|ছাঁৰ গছ", "Railway stations|ৰেলৱে ষ্টেচন"], 3, "Railways came in the 19th century.|ৰেল ঊনবিংশ শতিকাত আহিছিল।"),
)
u4 = U(4, "crown", "The return|ঘূৰি অহা",
 "Close the gap between Humayun and Akbar.|হুমায়ুন আৰু আকবৰৰ মাজৰ ফাঁক পূৰণ কৰা।", "Finding recorded: the Mughals returned in 1555, and Akbar took the throne in 1556.|প্ৰমাণ লিখা হ'ল: ১৫৫৫ত মোগল ঘূৰি আহিল, ১৫৫৬ত আকবৰ সিংহাসনত।",
 ["The Sur line followed Sher Shah|শ্বেৰ শ্বাহৰ পিছত সূৰ বংশ", "Humayun regained Delhi in 1555|১৫৫৫ত হুমায়ুনে দিল্লী পুনৰ পাইছিল", "He died soon after|তাৰ অলপ পিছতে তেওঁৰ মৃত্যু হয়", "Akbar followed in 1556|১৫৫৬ত আকবৰ আহিল"],
 S("Weak heirs|দুৰ্বল উত্তৰাধিকাৰী", "After Sher Shah, the Sur line weakened, and in 1555 [[humayun|Humayun]] retook <mark>Delhi</mark>.|শ্বেৰ শ্বাহৰ পিছত সূৰ বংশ দুৰ্বল হ'ল, ১৫৫৫ত [[humayun|হুমায়ুনে]] <mark>দিল্লী</mark> পুনৰ ল'লে।", art="calendar"),
 S("A boy king|বালক ৰজা", "Humayun died in early 1556. His son <mark>[[akbar|Akbar]]</mark>, aged 13, took the throne.|১৫৫৬ৰ আৰম্ভণিতে হুমায়ুনৰ মৃত্যু হয়। তেওঁৰ ১৩ বছৰীয়া পুত্ৰ <mark>[[akbar|আকবৰ]]</mark> সিংহাসনত বহিল।", art="court"),
 OR("Put the Mughal line in order.|মোগল বংশ ক্ৰমে সজোৱা।", ["Babur|বাবৰ", "Humayun|হুমায়ুন", "Akbar|আকবৰ"], "Father to son.|পিতৃৰ পৰা পুত্ৰলৈ।"),
 TF("Akbar was an adult when he took the throne.|আকবৰ সিংহাসনত বহোঁতে প্ৰাপ্তবয়স্ক আছিল।", False, "He was 13.|তেওঁৰ বয়স ১৩ আছিল।"),
 IN("Humayun regained Delhi in|হুমায়ুনে দিল্লী পুনৰ পাইছিল", ".|ত।", ["1540|১৫৪০", "1545|১৫৪৫", "1555|১৫৫৫", "1605|১৬০৫"], 2, "1555.|১৫৫৫।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1526, "First Panipat|পানিপথৰ প্ৰথম যুদ্ধ"), (1556, "Akbar's accession|আকবৰৰ সিংহাসনাৰোহণ")], [("Sher Shah takes power, 1540|শ্বেৰ শ্বাহৰ ক্ষমতা, ১৫৪০", 1), ("Vijayanagara founded, 1336|বিজয়নগৰ প্ৰতিষ্ঠা, ১৩৩৬", 0), ("Talikota, 1565|তালিকোটা, ১৫৬৫", 2)], "1336 → 1526 → 1540 → 1556 → 1565.|১৩৩৬ → ১৫২৬ → ১৫৪০ → ১৫৫৬ → ১৫৬৫।"),
 WH(["I fled in 1540.|মই ১৫৪০ত পলাইছিলোঁ।", "I came back in 1555.|মই ১৫৫৫ত ঘূৰি আহিছিলোঁ।", "My son was Akbar.|মোৰ পুত্ৰ আকবৰ।"], ["Babur|বাবৰ", "Humayun|হুমায়ুন", "Jahangir|জাহাংগীৰ", "Sher Shah Suri|শ্বেৰ শ্বাহ সূৰী"], 1, "Humayun.|হুমায়ুন।"),
)
test = TEST("Tell how the Mughals won, lost and won again.|মোগলে কেনেকৈ জিকিলে, হেৰুৱালে আৰু আকৌ জিকিলে, কোৱা।", "Recorded: Babur, Sher Shah and the return.|লিখা হ'ল: বাবৰ, শ্বেৰ শ্বাহ আৰু প্ৰত্যাৱৰ্তন।",
 IN("The first Mughal emperor was|প্ৰথম মোগল সম্ৰাট", ".|।", ["Humayun|হুমায়ুন", "Aurangzeb|ঔৰংগজেব", "Babur|বাবৰ", "Akbar|আকবৰ"], 2, "Babur.|বাবৰ।"),
 IN("The Grand Trunk Road was built during the rule of|গ্ৰেণ্ড ট্ৰাংক ৰোড নিৰ্মিত হৈছিল", ".|ৰ শাসনত।", ["Sher Shah Suri|শ্বেৰ শ্বাহ সূৰী", "Iltutmish|ইলতুৎমিছ", "Alauddin Khalji|আলাউদ্দিন খিলজী", "Muhammad bin Tughluq|মহম্মদ বিন তুঘলক"], 0, "That is the exam answer; he rebuilt an older route.|এয়া পৰীক্ষাৰ উত্তৰ; তেওঁ পুৰণি পথ পুনৰ গঢ়িছিল।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["First Panipat|পানিপথৰ প্ৰথম যুদ্ধ", "Chausa|চৌসা", "Humayun returns|হুমায়ুনৰ প্ৰত্যাৱৰ্তন"], "1526, 1539, 1555.|১৫২৬, ১৫৩৯, ১৫৫৫।"),
 TF("Babur used cannon at Panipat.|বাবৰে পানিপথত কামান ব্যৱহাৰ কৰিছিল।", True, "With muskets as well.|বন্দুকো ব্যৱহাৰ কৰিছিল।"),
 MP("Tap Panipat.|পানিপথ টিপা।", "panipat", ["panipat", "sasaram", "khanwa", "surat"], "Panipat.|পানিপথ।"),
 MC("Consider these statements. (1) Khanwa was fought in 1527. (2) Sher Shah defeated Humayun at Kannauj. (3) Sher Shah issued the rupiya. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ১৫২৭ত খানুৱাৰ যুদ্ধ হৈছিল। (২) কনৌজত শ্বেৰ শ্বাহে হুমায়ুনক হৰুৱাইছিল। (৩) শ্বেৰ শ্বাহে ৰুপিয়া উলিয়াইছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "2 and 3 only|কেৱল ২ আৰু ৩", "1 and 3 only|কেৱল ১ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 3, "All three are correct.|তিনিওটা শুদ্ধ।"),
)
LESSON(14, "Babur and Sher Shah|বাবৰ আৰু শ্বেৰ শ্বাহ", "1526–1556|১৫২৬–১৫৫৬", "The Mughal age|মোগল যুগ", "Evidence file 14|প্ৰমাণ নথি ১৪", "Won, lost, won again|জয়, পৰাজয়, পুনৰ জয়",
 "Babur took Delhi, his son lost it, and a brilliant rival left a road and a coin. Follow thirty unsteady years.|বাবৰে দিল্লী ল'লে, পুত্ৰই হেৰুৱালে, এজন প্ৰতিদ্বন্দ্বীয়ে পথ আৰু মুদ্ৰা এৰি গ'ল। ত্ৰিশ অস্থিৰ বছৰ অনুসৰণ কৰা।",
 sources, [u1, u2, u3, u4], test, ["panipat", "sasaram", "khanwa", "surat"],
 timeline=[("1526", "First Battle of Panipat|পানিপথৰ প্ৰথম যুদ্ধ", "u1"), ("1540", "Sher Shah takes power|শ্বেৰ শ্বাহৰ ক্ষমতা", "u2"), ("1556", "Akbar's accession|আকবৰৰ সিংহাসনাৰোহণ", "u4")])
