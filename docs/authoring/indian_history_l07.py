#!/usr/bin/env python3
"""Lesson 7: The Guptas."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "samudragupta": ("person", "Samudragupta|সমুদ্ৰগুপ্ত", "Gupta emperor praised on the Allahabad Pillar|এলাহাবাদ স্তম্ভত প্ৰশংসিত গুপ্ত সম্ৰাট"),
 "chandragupta-i": ("person", "Chandragupta I|চন্দ্ৰগুপ্ত প্ৰথম", "Gupta king who married the Licchavi princess Kumaradevi|লিচ্ছৱি ৰাজকুমাৰী কুমাৰদেৱীক বিয়া কৰোৱা গুপ্ত ৰজা"),
 "chandragupta-ii": ("person", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়", "Gupta emperor known as Vikramaditya|বিক্ৰমাদিত্য নামে জনাজাত গুপ্ত সম্ৰাট"),
 "harisena": ("person", "Harisena|হৰিষেণ", "Court poet who composed the Allahabad praise of Samudragupta|সমুদ্ৰগুপ্তৰ এলাহাবাদ প্ৰশস্তি ৰচোৱা ৰাজকবি"),
 "faxian": ("person", "Faxian (Fahien)|ফা-হিয়েন", "Chinese Buddhist monk in India about 405 to 411|প্ৰায় ৪০৫ৰ পৰা ৪১১লৈ ভাৰতত থকা চীনা বৌদ্ধ ভিক্ষু"),
 "kalidasa": ("person", "Kalidasa|কালিদাস", "Sanskrit poet and playwright of the Gupta era|গুপ্ত যুগৰ সংস্কৃত কবি আৰু নাট্যকাৰ"),
 "allahabad": ("place", "Prayagraj (Allahabad)|প্ৰয়াগৰাজ (এলাহাবাদ)", "City in Uttar Pradesh with the pillar of Samudragupta's praise|উত্তৰ প্ৰদেশৰ নগৰ, সমুদ্ৰগুপ্তৰ প্ৰশস্তি থকা স্তম্ভৰ ঠাই", [25.43, 81.88]),
 "ujjain": ("place", "Ujjain|উজ্জয়িনী", "City in Malwa|মালৱৰ নগৰ", [23.18, 75.78]),
})
sources = [
 src("Wikipedia, Samudragupta", "https://en.wikipedia.org/wiki/Samudragupta", "Used as a guide: dates, Chandragupta I and Kumaradevi, Harisena, frontier list with Kamarupa. Check in review."),
 src("Wikipedia, Gupta Empire", "https://en.wikipedia.org/wiki/Gupta_Empire", "Used as a guide: dates, Chandragupta II, Faxian 405 to 411, Huns, end of the line. Check in review."),
 src("Wikipedia, Kalidasa", "https://en.wikipedia.org/wiki/Kalidasa", "Used as a guide: three plays, poems, uncertain date, the contested link to Vikramaditya. Check in review."),
 src("J. F. Fleet, Inscriptions of the Early Gupta Kings, 1888", "https://archive.org/details/india.history.resource.107736", "Located, not read. Check the Allahabad text against it in review."),
]
u1 = U(1, "crown", "A marriage and a dynasty|বিয়া আৰু বংশ",
 "See how the Guptas rose.|গুপ্তসকলৰ উত্থান চোৱা।", "Finding recorded: Chandragupta I, then Samudragupta, then Chandragupta II.|প্ৰমাণ লিখা হ'ল: চন্দ্ৰগুপ্ত প্ৰথম, সমুদ্ৰগুপ্ত, চন্দ্ৰগুপ্ত দ্বিতীয়।",
 ["Chandragupta I took the title Maharajadhiraja|চন্দ্ৰগুপ্ত প্ৰথমে মহাৰাজাধিৰাজ উপাধি লৈছিল", "He married the Licchavi princess Kumaradevi|তেওঁ লিচ্ছৱি ৰাজকুমাৰী কুমাৰদেৱীক বিয়া কৰাইছিল", "Samudragupta followed him|তেওঁৰ পিছত সমুদ্ৰগুপ্ত", "Chandragupta II took the empire to its widest|চন্দ্ৰগুপ্ত দ্বিতীয়ে সাম্ৰাজ্য আটাইতকৈ বহল কৰিছিল"],
 S("King of kings|ৰজাৰ ৰজা", "[[chandragupta-i|Chandragupta I]] ruled from about 319. He married the <mark>Licchavi</mark> princess Kumaradevi and took the title Maharajadhiraja.|[[chandragupta-i|চন্দ্ৰগুপ্ত প্ৰথমে]] প্ৰায় ৩১৯ৰ পৰা শাসন কৰিছিল। তেওঁ <mark>লিচ্ছৱি</mark> ৰাজকুমাৰী কুমাৰদেৱীক বিয়া কৰাই মহাৰাজাধিৰাজ উপাধি লৈছিল।", art="court"),
 S("Father, son, grandson|পিতৃ, পুত্ৰ, নাতি", "[[samudragupta|Samudragupta]], their son, ruled from about 335, though scholars differ. [[chandragupta-ii|Chandragupta II]], known as <mark>Vikramaditya</mark>, took the empire to its widest.|তেওঁলোকৰ পুত্ৰ [[samudragupta|সমুদ্ৰগুপ্তই]] প্ৰায় ৩৩৫ৰ পৰা শাসন কৰিছিল, যদিও মতভেদ আছে। <mark>বিক্ৰমাদিত্য</mark> নামে জনাজাত [[chandragupta-ii|চন্দ্ৰগুপ্ত দ্বিতীয়ে]] সাম্ৰাজ্য আটাইতকৈ বহল কৰিছিল।", art="houses"),
 OR("Put the Gupta rulers in order.|গুপ্ত শাসকসকলক ক্ৰমে সজোৱা।", ["Chandragupta I|চন্দ্ৰগুপ্ত প্ৰথম", "Samudragupta|সমুদ্ৰগুপ্ত", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়"], "Three strong reigns.|তিনিটা শক্তিশালী ৰাজত্ব।"),
 TF("Chandragupta I of the Guptas is the same man as Chandragupta Maurya.|গুপ্ত বংশৰ চন্দ্ৰগুপ্ত প্ৰথম আৰু চন্দ্ৰগুপ্ত মৌৰ্য একেজন।", False, "They are centuries apart. Papers test this confusion.|তেওঁলোকৰ মাজত বহু শতিকাৰ ব্যৱধান। পৰীক্ষাত এই বিভ্ৰান্তি সোধা হয়।"),
 IN("Chandragupta II is known as|চন্দ্ৰগুপ্ত দ্বিতীয় জনাজাত", ".|নামে।", ["Vikramaditya|বিক্ৰমাদিত্য", "Devanampiya|দেৱানাম্পিয়", "Maharana|মহাৰাণা", "Shiladitya|শিলাদিত্য"], 0, "Vikramaditya.|বিক্ৰমাদিত্য।"),
 SP("Kumaradevi was a *Maurya* princess.|কুমাৰদেৱী *মৌৰ্য* ৰাজকুমাৰী আছিল।", "Licchavi|লিচ্ছৱি", "She was a Licchavi princess.|তেওঁ লিচ্ছৱি ৰাজকুমাৰী।"),
 WH(["My father took the title Maharajadhiraja.|মোৰ পিতৃয়ে মহাৰাজাধিৰাজ উপাধি লৈছিল।", "Harisena praised me.|হৰিষেণে মোৰ প্ৰশংসা কৰিছিল।"], ["Kanishka|কনিষ্ক", "Harsha|হৰ্ষ", "Samudragupta|সমুদ্ৰগুপ্ত", "Ashoka|অশোক"], 2, "Samudragupta.|সমুদ্ৰগুপ্ত।"),
)
u2 = U(2, "seal", "A pillar that praises|প্ৰশংসা কৰা স্তম্ভ",
 "Read the Allahabad Pillar, and find Kamarupa on it.|এলাহাবাদ স্তম্ভ পঢ়া, তাত কামৰূপ বিচাৰি উলিওৱা।", "Finding recorded: Harisena's praise names Kamarupa as a frontier state.|প্ৰমাণ লিখা হ'ল: হৰিষেণৰ প্ৰশস্তিত কামৰূপ সীমান্ত ৰাজ্য হিচাপে আছে।",
 ["Harisena composed the Allahabad praise|হৰিষেণে এলাহাবাদ প্ৰশস্তি ৰচিছিল", "He was Samudragupta's court poet|তেওঁ সমুদ্ৰগুপ্তৰ ৰাজকবি", "It lists conquests in north and south|ইয়াত উত্তৰ আৰু দক্ষিণৰ জয়ৰ তালিকা আছে", "Kamarupa is named as a frontier kingdom|কামৰূপক সীমান্ত ৰাজ্য বুলি উল্লেখ কৰা হৈছে"],
 S("Words added to an old pillar|পুৰণি স্তম্ভত নতুন শব্দ", "A Maurya pillar now at [[allahabad|Prayagraj]] carries a Gupta inscription too. It is a <mark>prashasti</mark>, a poem of praise.|[[allahabad|প্ৰয়াগৰাজত]] থকা মৌৰ্য স্তম্ভত গুপ্ত অভিলেখো আছে। ই এটা <mark>প্ৰশস্তি</mark>, প্ৰশংসাৰ কাব্য।", "Its author was the court poet <mark>[[harisena|Harisena]]</mark>.|ইয়াৰ লেখক ৰাজকবি <mark>[[harisena|হৰিষেণ]]</mark>।", art="seal"),
 LINK(S("Kamarupa on the frontier|সীমান্তত কামৰূপ", "The text claims wins across north and south, and lists frontier states that paid tribute. One of them is <mark>Kamarupa</mark>.|অভিলেখত উত্তৰ আৰু দক্ষিণৰ জয়ৰ দাবী আছে, কৰ দিয়া সীমান্ত ৰাজ্যৰ তালিকাও আছে। ইয়াৰ এটা <mark>কামৰূপ</mark>।", "It is praise written for a king, so read it as his claim.|ই ৰজাৰ বাবে লিখা প্ৰশংসা, সেয়ে ইয়াক তেওঁৰ দাবী বুলি পঢ়া।", art="scroll"),
  "varman-founders", 4, 1, "The pillar that named Kamarupa|কামৰূপৰ নাম লিখা স্তম্ভ", "The Assam History course starts Kamarupa's story from this same inscription.|অসমৰ ইতিহাস পাঠ্যক্ৰমত এই অভিলেখৰ পৰাই কামৰূপৰ কাহিনী আৰম্ভ।"),
 IN("The court poet of Samudragupta was|সমুদ্ৰগুপ্তৰ ৰাজকবি আছিল", ".|।", ["Banabhatta|বাণভট্ট", "Harisena|হৰিষেণ", "Chand Bardai|চান্দ বৰদাই", "Bhavabhuti|ভৱভূতি"], 1, "Harisena. Banabhatta served Harsha.|হৰিষেণ। বাণভট্ট হৰ্ষৰ সভাত আছিল।"),
 MP("Tap the city with the pillar.|স্তম্ভ থকা চহৰখন টিপা।", "allahabad", ["allahabad", "ujjain", "pataliputra", "girnar"], "Prayagraj, once Allahabad.|প্ৰয়াগৰাজ, পূৰ্বৰ এলাহাবাদ।"),
 TF("The Allahabad inscription names Kamarupa.|এলাহাবাদ অভিলেখত কামৰূপৰ নাম আছে।", True, "It is listed among the frontier states.|ই সীমান্ত ৰাজ্যৰ তালিকাত আছে।"),
 SC("Unscramble the word for a poem of praise.|প্ৰশংসাৰ কাব্যৰ শব্দটো সজোৱা।", "PRASHASTI", ["প্ৰ", "শ", "স্তি"], "A prashasti is a royal eulogy.|প্ৰশস্তি ৰজাৰ স্তুতি।"),
 OD("Who is NOT a court poet?|কোনজন ৰাজকবি নহয়?", ["Harisena|হৰিষেণ", "Banabhatta|বাণভট্ট", "Kalidasa|কালিদাস", "Faxian|ফা-হিয়েন"], 3, "Faxian was a Chinese monk.|ফা-হিয়েন চীনা ভিক্ষু।"),
)
u3 = U(3, "scroll", "Faxian and Kalidasa|ফা-হিয়েন আৰু কালিদাস",
 "Fix the traveller and the poet of the age.|যুগটোৰ পৰ্যটক আৰু কবি মনত ৰাখা।", "Finding recorded: Faxian came about 405; Kalidasa wrote three plays.|প্ৰমাণ লিখা হ'ল: ফা-হিয়েন প্ৰায় ৪০৫ত আহিছিল; কালিদাসে তিনিখন নাটক লিখিছিল।",
 ["Faxian visited under Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়ৰ সময়ত ফা-হিয়েন আহিছিল", "Kalidasa's plays are three|কালিদাসৰ নাটক তিনিখন", "Abhijnana Shakuntalam is his most famous|অভিজ্ঞান শকুন্তলম তেওঁৰ আটাইতকৈ বিখ্যাত", "His date and court are not certain|তেওঁৰ সময় আৰু ৰাজসভা নিশ্চিত নহয়"],
 S("A monk walks in|এজন ভিক্ষুৰ আগমন", "The Chinese monk <mark>[[faxian|Faxian]]</mark>, spelled Fahien in papers, was in India from about 405 to 411, in Chandragupta II's time.|চীনা ভিক্ষু <mark>[[faxian|ফা-হিয়েন]]</mark> প্ৰায় ৪০৫ৰ পৰা ৪১১লৈ চন্দ্ৰগুপ্ত দ্বিতীয়ৰ সময়ত ভাৰতত আছিল।", "His account describes a prosperous land with mild punishments.|তেওঁৰ বিৱৰণত সমৃদ্ধ দেশ আৰু কোমল শাস্তিৰ কথা আছে।", art="embassy"),
 S("Three plays|তিনিখন নাটক", "[[kalidasa|Kalidasa]] wrote in Sanskrit. His plays are <b>Abhijnana Shakuntalam, Malavikagnimitram, Vikramorvashiyam</b>.|[[kalidasa|কালিদাসে]] সংস্কৃতত লিখিছিল। তেওঁৰ নাটক <b>অভিজ্ঞান শকুন্তলম, মালৱিকাগ্নিমিত্ৰম, বিক্ৰমোৰ্বশীয়ম</b>।", "Tradition puts him at Vikramaditya's court, but his date is uncertain. His poems include the Meghaduta.|পৰম্পৰাই তেওঁক বিক্ৰমাদিত্যৰ সভাত ৰাখে, কিন্তু সময় অনিশ্চিত। মেঘদূত তেওঁৰ কাব্য।", art="scroll"),
 MA([("Abhijnana Shakuntalam|অভিজ্ঞান শকুন্তলম", "Kalidasa|কালিদাস"), ("Allahabad praise|এলাহাবাদ প্ৰশস্তি", "Harisena|হৰিষেণ"), ("Indica|ইণ্ডিকা", "Megasthenes|মেগাস্থিনিছ")], "Work and author.|ৰচনা আৰু লেখক।"),
 OD("Which play was NOT written by Kalidasa?|কোনখন নাটক কালিদাসে লিখা নাছিল?", ["Abhijnana Shakuntalam|অভিজ্ঞান শকুন্তলম", "Malavikagnimitram|মালৱিকাগ্নিমিত্ৰম", "Vikramorvashiyam|বিক্ৰমোৰ্বশীয়ম", "Mudrarakshasa|মুদ্ৰাৰাক্ষস"], 3, "Mudrarakshasa is by Vishakhadatta.|মুদ্ৰাৰাক্ষস বিশাখদত্তৰ ৰচনা।"),
 WH(["I was a Chinese Buddhist monk.|মই চীনা বৌদ্ধ ভিক্ষু।", "I came about 405.|মই প্ৰায় ৪০৫ত আহিছিলোঁ।", "Chandragupta II ruled then.|তেতিয়া চন্দ্ৰগুপ্ত দ্বিতীয়ে শাসন কৰিছিল।"], ["Xuanzang|হিউৱেন চাঙ", "Faxian|ফা-হিয়েন", "Ibn Battuta|ইবন বতুতা", "Megasthenes|মেগাস্থিনিছ"], 1, "Faxian. Xuanzang came in Harsha's time.|ফা-হিয়েন। হিউৱেন চাঙ হৰ্ষৰ সময়ত আহিছিল।"),
 TF("Kalidasa's date is firmly fixed by inscriptions.|অভিলেখে কালিদাসৰ সময় দৃঢ়ভাৱে নিৰ্ধাৰণ কৰে।", False, "His works cannot be dated precisely.|তেওঁৰ ৰচনাৰ সঠিক সময় ক'ব নোৱাৰি।"),
 SP("Faxian came during the reign of *Harsha.*|ফা-হিয়েন *হৰ্ষৰ* ৰাজত্বত আহিছিল।", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়ৰ", "He came about 405.|তেওঁ প্ৰায় ৪০৫ত আহিছিল।"),
)
u4 = U(4, "moon", "Huns and the end|হূণ আৰু অন্ত",
 "See what weakened the Guptas.|গুপ্তসকলক কিহে দুৰ্বল কৰিলে, চোৱা।", "Finding recorded: Hun attacks from the late 5th century, and a main line that faded by the 6th.|প্ৰমাণ লিখা হ'ল: পঞ্চম শতিকাৰ শেষৰ পৰা হূণ আক্ৰমণ, ষষ্ঠ শতিকালৈ মূল বংশ ক্ষীণ।",
 ["Huns attacked from the late 5th century|পঞ্চম শতিকাৰ শেষৰ পৰা হূণ আক্ৰমণ", "Toramana and Mihirakula were Hun leaders|তোৰমাণ আৰু মিহিৰকুল হূণ নেতা", "The last known main-line record is about 543|মূল বংশৰ শেষ জ্ঞাত অভিলেখ প্ৰায় ৫৪৩", "Regional powers rose afterwards|পিছত আঞ্চলিক শক্তিৰ উত্থান"],
 S("Riders from the north-west|উত্তৰ-পশ্চিমৰ অশ্বাৰোহী", "From the late 5th century <mark>Huns</mark> attacked the empire. Their leaders included <mark>Toramana</mark> and <mark>Mihirakula</mark>.|পঞ্চম শতিকাৰ শেষৰ পৰা <mark>হূণে</mark> সাম্ৰাজ্য আক্ৰমণ কৰিছিল। তেওঁলোকৰ নেতা <mark>তোৰমাণ</mark> আৰু <mark>মিহিৰকুল</mark>।", art="embassy"),
 S("A slow fade|লাহে লাহে ক্ষীণ", "The main Gupta line faded. Its last known inscription dates to about 543, and regional kings took over.|গুপ্তৰ মূল বংশ ক্ষীণ হৈ পৰিল। ইয়াৰ শেষ জ্ঞাত অভিলেখ প্ৰায় ৫৪৩ৰ, আঞ্চলিক ৰজাই ঠাই ল'লে।", "In Kamarupa, the Varmans were already rising.|কামৰূপত বৰ্মন বংশ ইতিমধ্যে উঠি আহিছিল।", art="calendar"),
 IN("From the late 5th century the Guptas were attacked by the|পঞ্চম শতিকাৰ শেষৰ পৰা গুপ্তসকলক আক্ৰমণ কৰিছিল", ".|এ।", ["Greeks|গ্ৰীক", "Huns|হূণ", "Mughals|মোগল", "Cholas|চোল"], 1, "The Huns.|হূণ।"),
 TF("Mihirakula was a Hun leader.|মিহিৰকুল হূণ নেতা আছিল।", True, "With Toramana, he led the Alchon Huns.|তোৰমাণৰ সৈতে তেওঁ আলচন হূণৰ নেতা।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Faxian in India|ভাৰতত ফা-হিয়েন", "Hun attacks|হূণ আক্ৰমণ", "Last Gupta record|শেষ গুপ্ত অভিলেখ"], "About 405, late 5th century, about 543.|প্ৰায় ৪০৫, পঞ্চম শতিকাৰ শেষ, প্ৰায় ৫৪৩।"),
 WH(["I was a Hun leader.|মই হূণ নেতা।", "My name is paired with Mihirakula.|মিহিৰকুলৰ সৈতে মোৰ নাম জড়িত।"], ["Toramana|তোৰমাণ", "Porus|পুৰু", "Kanishka|কনিষ্ক", "Seleucus I|চেলুকাছ প্ৰথম"], 0, "Toramana.|তোৰমাণ।"),
 SP("The last known Gupta record dates to about *1543.*|শেষ জ্ঞাত গুপ্ত অভিলেখ প্ৰায় *১৫৪৩ৰ।*", "543|৫৪৩ৰ", "About 543.|প্ৰায় ৫৪৩।"),
)
test = TEST("Tell the Gupta story from its sources.|উৎসৰ পৰা গুপ্ত কাহিনী কোৱা।", "Recorded: rulers, the pillar, the traveller and the end.|লিখা হ'ল: শাসক, স্তম্ভ, পৰ্যটক আৰু অন্ত।",
 IN("The court poet of Samudragupta was|সমুদ্ৰগুপ্তৰ ৰাজকবি আছিল", ".|।", ["Banabhatta|বাণভট্ট", "Harisena|হৰিষেণ", "Chand Bardai|চান্দ বৰদাই", "Bhavabhuti|ভৱভূতি"], 1, "Harisena.|হৰিষেণ।"),
 OR("Order the Gupta rulers.|গুপ্ত শাসকসকলক সজোৱা।", ["Chandragupta I|চন্দ্ৰগুপ্ত প্ৰথম", "Samudragupta|সমুদ্ৰগুপ্ত", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়"], "That order.|এই ক্ৰমত।"),
 TF("Abhijnana Shakuntalam was written by Kalidasa.|অভিজ্ঞান শকুন্তলম কালিদাসে লিখিছিল।", True, "It is his best-known play.|ই তেওঁৰ আটাইতকৈ বিখ্যাত নাটক।"),
 MP("Tap Prayagraj.|প্ৰয়াগৰাজ টিপা।", "allahabad", ["allahabad", "ujjain", "pataliputra", "girnar"], "It holds the pillar.|ইয়াত স্তম্ভটো আছে।"),
 MA([("Faxian|ফা-হিয়েন", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়"), ("Megasthenes|মেগাস্থিনিছ", "Chandragupta Maurya|চন্দ্ৰগুপ্ত মৌৰ্য")], "Two Chandraguptas, two visitors.|দুজন চন্দ্ৰগুপ্ত, দুজন অভ্যাগত।"),
 MC("Consider these statements. (1) Kumaradevi was a Licchavi princess. (2) Kamarupa is named on the Allahabad Pillar. (3) Kalidasa wrote the Mudrarakshasa. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) কুমাৰদেৱী লিচ্ছৱি ৰাজকুমাৰী। (২) এলাহাবাদ স্তম্ভত কামৰূপৰ নাম আছে। (৩) কালিদাসে মুদ্ৰাৰাক্ষস লিখিছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 0, "Mudrarakshasa is by Vishakhadatta.|মুদ্ৰাৰাক্ষস বিশাখদত্তৰ।"),
)
LESSON(7, "The Guptas|গুপ্ত সকল", "c. 319–550 CE|প্ৰায় ৩১৯–৫৫০ খ্ৰীষ্টাব্দ", "Empires of the north|উত্তৰৰ সাম্ৰাজ্য", "Evidence file 7|প্ৰমাণ নথি ৭", "Written by the king's poet|ৰজাৰ কবিৰ লেখা",
 "Most of what we know about Samudragupta was written by his own poet. Learn the facts, and learn to read praise as praise.|সমুদ্ৰগুপ্তৰ বিষয়ে জনা বেছিভাগ কথা তেওঁৰ নিজৰ কবিৰ লেখা। তথ্য শিকা, প্ৰশংসাক প্ৰশংসা বুলি পঢ়িবলৈও শিকা।",
 sources, [u1, u2, u3, u4], test, ["allahabad", "ujjain", "pataliputra", "girnar"])
