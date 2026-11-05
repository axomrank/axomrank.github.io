#!/usr/bin/env python3
"""Lesson 8: Harsha and Xuanzang."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "banabhatta": ("person", "Banabhatta|বাণভট্ট", "Court poet of Harsha, author of the Harshacharita|হৰ্ষৰ ৰাজকবি, হৰ্ষচৰিতৰ লেখক"),
 "pulakeshin-ii": ("person", "Pulakeshin II|দ্বিতীয় পুলকেশী", "Chalukya king who stopped Harsha at the Narmada|নৰ্মদাত হৰ্ষক ৰোধ কৰা চালুক্য ৰজা"),
 "thanesar": ("place", "Thanesar|থানেশ্বৰ", "Town in Haryana, home of Harsha's family|হাৰিয়ানাৰ নগৰ, হৰ্ষৰ বংশৰ ঘৰ", [29.97, 76.83]),
 "kannauj": ("place", "Kanyakubja (Kannauj)|কান্যকুব্জ (কনৌজ)", "Harsha's capital, in Uttar Pradesh|উত্তৰ প্ৰদেশত হৰ্ষৰ ৰাজধানী", [27.05, 79.91]),
})
sources = [
 src("Bana, The Harsa-carita, translated by Cowell and Thomas, 1897", "https://archive.org/details/harsacaritaofban00banaiala", "Local copy read in part: Prabhakaravardhana of Thanesar and Bhaskaravarman of Pragjyotisa, from the translators' introduction. Local copy in Indian history sources; the URL is the catalogue record."),
 src("Si-Yu-Ki, Xuanzang, translated by Samuel Beal, volume 2, 1884", "https://archive.org/details/siyukibuddhistre02hsua", "Local copy located by search: the Kamarupa section and Siladitya-raja. Passages not read in full; check in review. The URL is the catalogue record."),
 src("Wikipedia, Harsha", "https://en.wikipedia.org/wiki/Harsha", "Used as a guide: 606 to 647, Rajyavardhana, Kanyakubja, Narmada, Banabhatta, the plays, Shaivite grants and Buddhist portrayal. Check in review."),
 src("APSC CCE Prelims 2025 GS-I, question 23, page read", "https://apsc.nic.in/cce.html", "Banskhera inscription with Harshavardhana as the option. The export's answer key does not fit the printed options."),
]
u1 = U(1, "crown", "A young king at Thanesar|থানেশ্বৰৰ ডেকা ৰজা",
 "Trace how Harsha came to the throne.|হৰ্ষ কেনেকৈ সিংহাসনলৈ আহিল, অনুসৰণ কৰা।", "Finding recorded: Harsha followed his murdered brother in 606.|প্ৰমাণ লিখা হ'ল: নিহত ভায়েকৰ পিছত ৬০৬ত হৰ্ষ ৰজা হ'ল।",
 ["Prabhakaravardhana was Harsha's father|প্ৰভাকৰবৰ্ধন হৰ্ষৰ পিতৃ", "Rajyavardhana, his brother, was murdered|তেওঁৰ ককায়েক ৰাজ্যবৰ্ধন নিহত হৈছিল", "Harsha ruled from 606 to 647|হৰ্ষই ৬০৬ৰ পৰা ৬৪৭লৈ শাসন কৰিছিল", "He made Kanyakubja his capital|তেওঁ কান্যকুব্জক ৰাজধানী কৰিছিল"],
 S("A family at Thanesar|থানেশ্বৰৰ এটা পৰিয়াল", "<mark>Prabhakaravardhana</mark> ruled at [[thanesar]]. His sons were Rajyavardhana and [[harsha|Harsha]].|<mark>প্ৰভাকৰবৰ্ধনে</mark> [[thanesar|থানেশ্বৰত]] শাসন কৰিছিল। তেওঁৰ পুত্ৰ ৰাজ্যবৰ্ধন আৰু [[harsha|হৰ্ষ]]।", "When Rajyavardhana was murdered, Harsha took the throne in <mark>606</mark>.|ৰাজ্যবৰ্ধন নিহত হোৱাত <mark>৬০৬ত</mark> হৰ্ষ ৰজা হ'ল।", art="court"),
 S("A capital on the Ganga|গংগাৰ পাৰৰ ৰাজধানী", "Harsha made <mark>[[kannauj|Kanyakubja]]</mark> his capital and ruled until 647. His realm did not cover all of the north.|হৰ্ষই <mark>[[kannauj|কান্যকুব্জক]]</mark> ৰাজধানী কৰি ৬৪৭লৈ শাসন কৰিছিল। তেওঁৰ ৰাজ্য গোটেই উত্তৰ নহয়।", map={"base": "india", "box": [72, 24, 86, 33], "show": ["thanesar", "kannauj"]}),
 IN("The father of King Harshavardhana was|হৰ্ষবৰ্ধনৰ পিতৃ আছিল", ".|।", ["Prabhakaravardhana|প্ৰভাকৰবৰ্ধন", "Bhaskaravardhana|ভাস্কৰবৰ্ধন", "Jaivardhana|জয়বৰ্ধন", "Mahavardhana|মহাবৰ্ধন"], 0, "Prabhakaravardhana of Thanesar.|থানেশ্বৰৰ প্ৰভাকৰবৰ্ধন।"),
 MP("Tap Harsha's capital.|হৰ্ষৰ ৰাজধানী টিপা।", "kannauj", ["kannauj", "thanesar", "pataliputra", "ujjain"], "Kanyakubja, today's Kannauj.|কান্যকুব্জ, আজিৰ কনৌজ।"),
 TF("Harsha's reign began in 606.|হৰ্ষৰ ৰাজত্ব ৬০৬ত আৰম্ভ হৈছিল।", True, "He ruled from 606 to 647.|তেওঁ ৬০৬ৰ পৰা ৬৪৭লৈ শাসন কৰিছিল।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Prabhakaravardhana rules|প্ৰভাকৰবৰ্ধনৰ শাসন", "Rajyavardhana murdered|ৰাজ্যবৰ্ধন নিহত", "Harsha takes the throne|হৰ্ষ সিংহাসনত"], "Father, brother, Harsha.|পিতৃ, ককায়েক, হৰ্ষ।"),
 SC("Unscramble Harsha's capital.|হৰ্ষৰ ৰাজধানীখন সজোৱা।", "KANNAUJ", ["ক", "নৌ", "জ"], "Kannauj.|কনৌজ।"),
)
u2 = U(2, "scroll", "The king's biographer|ৰজাৰ জীৱনীকাৰ",
 "Name Harsha's writers, and his limits.|হৰ্ষৰ লেখক আৰু তেওঁৰ সীমা জানা।", "Finding recorded: Banabhatta wrote the Harshacharita; Pulakeshin II held the Narmada.|প্ৰমাণ লিখা হ'ল: বাণভট্টে হৰ্ষচৰিত লিখিছিল; দ্বিতীয় পুলকেশীয়ে নৰ্মদা ৰাখিছিল।",
 ["Banabhatta wrote the Harshacharita|বাণভট্টে হৰ্ষচৰিত লিখিছিল", "Harsha is credited with three plays|হৰ্ষক তিনিখন নাটকৰ লেখক বোলা হয়", "Pulakeshin II stopped him at the Narmada|দ্বিতীয় পুলকেশীয়ে তেওঁক নৰ্মদাত ৰোধ কৰিছিল", "The Banskhera inscription is Harsha's|বাঁশখেৰা অভিলেখ হৰ্ষৰ"],
 S("A poet at court|ৰাজসভাত কবি", "<mark>[[banabhatta|Banabhatta]]</mark> wrote the <mark>[[harshacharita|Harshacharita]]</mark>, a life of his king. Like Harisena's pillar, it is praise, so read it with care.|<mark>[[banabhatta|বাণভট্টে]]</mark> ৰজাৰ জীৱনী <mark>[[harshacharita|হৰ্ষচৰিত]]</mark> লিখিছিল। হৰিষেণৰ স্তম্ভৰ দৰে এয়াও প্ৰশংসা, সাৱধানে পঢ়া।", "Harsha is widely credited with the plays Ratnavali, Nagananda and Priyadarsika, though this is debated.|ৰত্নাৱলী, নাগানন্দ আৰু প্ৰিয়দৰ্শিকা নাটক হৰ্ষৰ বুলি ধৰা হয়, যদিও বিতৰ্ক আছে।", art="scroll"),
 S("Stopped at the Narmada|নৰ্মদাত ৰোধ", "[[pulakeshin-ii|Pulakeshin II]], the Chalukya king, repelled Harsha at the <mark>Narmada</mark>, which became the border.|চালুক্য ৰজা [[pulakeshin-ii|দ্বিতীয় পুলকেশীয়ে]] <mark>নৰ্মদাত</mark> হৰ্ষক ৰোধ কৰিছিল, নদীখন সীমা হ'ল।", "The <mark>Banskhera</mark> inscription belongs to Harsha. Papers ask this directly.|<mark>বাঁশখেৰা</mark> অভিলেখ হৰ্ষৰ। পৰীক্ষাত এইটো পোনপটীয়াকৈ সোধা হয়।", art="seal"),
 MA([("Harshacharita|হৰ্ষচৰিত", "Banabhatta|বাণভট্ট"), ("Allahabad praise|এলাহাবাদ প্ৰশস্তি", "Harisena|হৰিষেণ"), ("Ratnavali|ৰত্নাৱলী", "Attributed to Harsha|হৰ্ষৰ বুলি ধৰা")], "Work and author.|ৰচনা আৰু লেখক।"),
 WH(["I was a Chalukya king.|মই চালুক্য ৰজা।", "I held the Narmada.|মই নৰ্মদা ৰাখিছিলোঁ।", "Harsha could not pass me.|হৰ্ষই মোক অতিক্ৰম কৰিব নোৱাৰিলে।"], ["Pulakeshin II|দ্বিতীয় পুলকেশী", "Samudragupta|সমুদ্ৰগুপ্ত", "Gautamiputra Satakarni|গৌতমীপুত্ৰ সাতকৰ্ণী", "Bhaskaravarman|ভাস্কৰবৰ্মন"], 0, "Pulakeshin II.|দ্বিতীয় পুলকেশী।"),
 IN("The Banskhera inscription is associated with|বাঁশখেৰা অভিলেখ জড়িত", ".|ৰ সৈতে।", ["Ashoka|অশোক", "Kanishka|কনিষ্ক", "Harshavardhana|হৰ্ষবৰ্ধন", "Dharmapala|ধৰ্মপাল"], 2, "Harshavardhana.|হৰ্ষবৰ্ধন।"),
 SP("Harsha's biography was written by *Harisena.*|হৰ্ষৰ জীৱনী *হৰিষেণে* লিখিছিল।", "Banabhatta|বাণভট্টে", "Harisena served Samudragupta.|হৰিষেণ সমুদ্ৰগুপ্তৰ সভাত আছিল।"),
 TF("Harsha ruled all of India.|হৰ্ষই গোটেই ভাৰত শাসন কৰিছিল।", False, "The Narmada was his southern limit.|নৰ্মদা তেওঁৰ দক্ষিণ সীমা আছিল।"),
)
u3 = U(3, "walk", "The pilgrim who wrote it down|লিখি থোৱা তীৰ্থযাত্ৰী",
 "Link Xuanzang to Harsha and to Kamarupa.|হিউৱেন চাঙক হৰ্ষ আৰু কামৰূপৰ সৈতে জোৰা লগোৱা।", "Finding recorded: Xuanzang visited Harsha's India and also Kamarupa.|প্ৰমাণ লিখা হ'ল: হিউৱেন চাঙ হৰ্ষৰ ভাৰত আৰু কামৰূপলৈ গৈছিল।",
 ["Xuanzang visited in Harsha's reign|হিউৱেন চাঙ হৰ্ষৰ ৰাজত্বত আহিছিল", "Papers spell him Hiuen Tsang|পৰীক্ষাত তেওঁৰ নাম Hiuen Tsang", "He studied Buddhism in India|তেওঁ ভাৰতত বৌদ্ধ ধৰ্ম অধ্যয়ন কৰিছিল", "Bhaskaravarman of Kamarupa was Harsha's ally|কামৰূপৰ ভাস্কৰবৰ্মন হৰ্ষৰ মিত্ৰ"],
 S("One man, many spellings|এজন মানুহ, বহু বানান", "The Chinese pilgrim <mark>[[xuanzang|Xuanzang]]</mark> came in Harsha's time. Papers write Hiuen Tsang, so know both.|চীনা তীৰ্থযাত্ৰী <mark>[[xuanzang|হিউৱেন চাঙ]]</mark> হৰ্ষৰ সময়ত আহিছিল। ইংৰাজীত Xuanzang আৰু Hiuen Tsang দুয়োটা বানান পোৱা যায়।", "His account, the Si-Yu-Ki, is a major source. It shows Harsha as a Buddhist patron, though his own grants call him a Shaivite.|তেওঁৰ বিৱৰণ চি-য়ু-কি এটা ডাঙৰ উৎস। ইয়াত হৰ্ষ বৌদ্ধ পৃষ্ঠপোষক, যদিও তেওঁৰ নিজৰ দানপত্ৰত শৈৱ।", art="scroll"),
 LINK(S("A visit to Kamarupa|কামৰূপলৈ যাত্ৰা", "Xuanzang also visited <mark>Kamarupa</mark>, where [[bhaskaravarman|Bhaskaravarman]] ruled. Bana's Harshacharita names this king as Harsha's ally.|হিউৱেন চাঙ <mark>কামৰূপলৈও</mark> গৈছিল, য'ত [[bhaskaravarman|ভাস্কৰবৰ্মনে]] শাসন কৰিছিল। বাণৰ হৰ্ষচৰিতত এই ৰজা হৰ্ষৰ মিত্ৰ।", art="embassy"),
  "varman-bhaskaravarman", 6, 4, "Xuanzang in Kamarupa|কামৰূপত হিউৱেন চাঙ", "The Assam History course tells this visit from Kamarupa's side.|অসমৰ ইতিহাস পাঠ্যক্ৰমত এই যাত্ৰা কামৰূপৰ ফালৰ পৰা কোৱা হৈছে।"),
 IN("Hiuen Tsang visited India during the reign of|হিউৱেন চাঙ ভাৰতলৈ আহিছিল", ".|ৰ ৰাজত্বত।", ["Harshavardhana|হৰ্ষবৰ্ধন", "Ashoka|অশোক", "Vishnugupta|বিষ্ণুগুপ্ত", "Samudragupta|সমুদ্ৰগুপ্ত"], 0, "Harshavardhana.|হৰ্ষবৰ্ধন।"),
 MA([("Megasthenes|মেগাস্থিনিছ", "Chandragupta Maurya|চন্দ্ৰগুপ্ত মৌৰ্য"), ("Faxian|ফা-হিয়েন", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়"), ("Xuanzang|হিউৱেন চাঙ", "Harsha|হৰ্ষ")], "Traveller and reign. Keep this table.|পৰ্যটক আৰু ৰাজত্ব। এই তালিকা মনত ৰাখা।"),
 TF("Xuanzang visited Kamarupa.|হিউৱেন চাঙ কামৰূপলৈ গৈছিল।", True, "Bhaskaravarman ruled there.|তাত ভাস্কৰবৰ্মনে শাসন কৰিছিল।"),
 WH(["I ruled Kamarupa.|মই কামৰূপ শাসন কৰিছিলোঁ।", "I was Harsha's ally.|মই হৰ্ষৰ মিত্ৰ।", "Xuanzang visited me.|হিউৱেন চাঙ মোৰ ওচৰলৈ আহিছিল।"], ["Pulakeshin II|দ্বিতীয় পুলকেশী", "Bhaskaravarman|ভাস্কৰবৰ্মন", "Sasanka|শশাংক", "Kanishka|কনিষ্ক"], 1, "Bhaskaravarman.|ভাস্কৰবৰ্মন।"),
 SP("Hiuen Tsang came from *Greece.*|হিউৱেন চাঙ *গ্ৰীচৰ* পৰা আহিছিল।", "China|চীনৰ", "He was a Chinese pilgrim.|তেওঁ চীনা তীৰ্থযাত্ৰী।"),
)
test = TEST("Cross-check three kinds of source.|তিনি ধৰণৰ উৎস মিলাই চোৱা।", "Recorded: Harsha through his poet, his pilgrim and his plates.|লিখা হ'ল: কবি, তীৰ্থযাত্ৰী আৰু তাম্ৰফলকৰ জৰিয়তে হৰ্ষ।",
 IN("The father of King Harshavardhana was|হৰ্ষবৰ্ধনৰ পিতৃ আছিল", ".|।", ["Prabhakaravardhana|প্ৰভাকৰবৰ্ধন", "Bhaskaravardhana|ভাস্কৰবৰ্ধন", "Jaivardhana|জয়বৰ্ধন", "Mahavardhana|মহাবৰ্ধন"], 0, "Prabhakaravardhana.|প্ৰভাকৰবৰ্ধন।"),
 TF("Banabhatta wrote the Harshacharita.|বাণভট্টে হৰ্ষচৰিত লিখিছিল।", True, "Yes.|হয়।"),
 MP("Tap Thanesar.|থানেশ্বৰ টিপা।", "thanesar", ["thanesar", "kannauj", "pataliputra", "ujjain"], "In Haryana.|হাৰিয়ানাত।"),
 MA([("Xuanzang|হিউৱেন চাঙ", "Harsha|হৰ্ষ"), ("Faxian|ফা-হিয়েন", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়")], "Traveller and reign.|পৰ্যটক আৰু ৰাজত্ব।"),
 SP("Harsha was stopped at the *Ganga* by Pulakeshin II.|দ্বিতীয় পুলকেশীয়ে হৰ্ষক *গংগাত* ৰোধ কৰিছিল।", "Narmada|নৰ্মদাত", "At the Narmada.|নৰ্মদাত।"),
 MC("Consider these statements. (1) Harsha's capital was Kanyakubja. (2) Harsha's land grants call him a Shaivite. (3) Bhaskaravarman ruled Magadha. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) হৰ্ষৰ ৰাজধানী কান্যকুব্জ। (২) হৰ্ষৰ দানপত্ৰত তেওঁ শৈৱ। (৩) ভাস্কৰবৰ্মনে মগধ শাসন কৰিছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 0, "He ruled Kamarupa.|তেওঁ কামৰূপ শাসন কৰিছিল।"),
)
LESSON(8, "Harsha and Xuanzang|হৰ্ষ আৰু হিউৱেন চাঙ", "606–647 CE|৬০৬–৬৪৭ খ্ৰীষ্টাব্দ", "Empires of the north|উত্তৰৰ সাম্ৰাজ্য", "Evidence file 8|প্ৰমাণ নথি ৮", "One king, three witnesses|এজন ৰজা, তিনিজন সাক্ষী",
 "A court poet, a Chinese pilgrim and a set of land grants all describe Harsha, and they do not fully agree. Compare them.|ৰাজকবি, চীনা তীৰ্থযাত্ৰী আৰু দানপত্ৰই হৰ্ষৰ বৰ্ণনা দিয়ে, সম্পূৰ্ণ একমত নহয়। তুলনা কৰা।",
 sources, [u1, u2, u3], test, ["thanesar", "kannauj", "pataliputra", "ujjain"])
