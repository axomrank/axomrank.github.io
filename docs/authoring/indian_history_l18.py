#!/usr/bin/env python3
"""Lesson 18: Plassey and Buxar."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "vasco-da-gama": ("person", "Vasco da Gama|ভাস্কো দা গামা", "Portuguese navigator who reached Calicut in 1498|১৪৯৮ত কালিকট পোৱা পৰ্তুগীজ নাৱিক"),
 "robert-clive": ("person", "Robert Clive|ৰবাৰ্ট ক্লাইভ", "Company commander who won at Plassey|পলাশীত জয়ী কোম্পানীৰ সেনাপতি"),
 "siraj-ud-daulah": ("person", "Siraj ud-Daulah|চিৰাজ-উদ-দৌলা", "Last independent Nawab of Bengal|বংগৰ শেষ স্বাধীন নবাব"),
 "mir-jafar": ("person", "Mir Jafar|মীৰ জাফৰ", "Siraj's commander, made Nawab after Plassey|চিৰাজৰ সেনাপতি, পলাশীৰ পিছত নবাব"),
 "mir-qasim": ("person", "Mir Qasim|মীৰ কাছিম", "Nawab of Bengal who fought at Buxar|বক্সাৰত যুঁজা বংগৰ নবাব"),
 "diwani": ("term", "Diwani|দেৱানী", "Right to collect revenue, granted to the Company in 1765|ৰাজহ সংগ্ৰহৰ অধিকাৰ, ১৭৬৫ত কোম্পানীয়ে পাইছিল"),
 "calicut": ("place", "Calicut|কালিকট", "Port on the Malabar coast, today's Kozhikode|মালাবাৰ উপকূলৰ বন্দৰ, আজিৰ কোঝিকোড", [11.25, 75.78]),
 "buxar": ("place", "Buxar|বক্সাৰ", "Bihar town on the Ganga|গংগা পাৰৰ বিহাৰৰ নগৰ", [25.56, 83.98]),
})
sources = [
 src("Wikipedia, Vasco da Gama", "https://en.wikipedia.org/wiki/Vasco_da_Gama", "Used as a guide: 1497, 20 May 1498, Cape route, Malindi pilot. Check in review."),
 src("Wikipedia, Battle of Plassey", "https://en.wikipedia.org/wiki/Battle_of_Plassey", "Used as a guide: 23 June 1757, Clive, Siraj, Mir Jafar. Check in review."),
 src("Wikipedia, Battle of Buxar", "https://en.wikipedia.org/wiki/Battle_of_Buxar", "Used as a guide: October 1764, Munro, three allies, Allahabad 1765, Diwani. Check in review."),
]
u1 = U(1, "river", "The sea route|সাগৰৰ পথ",
 "See how Europeans reached India by sea.|ইউৰোপীয়সকলে সাগৰেৰে কেনেকৈ ভাৰত পালে, চোৱা।", "Finding recorded: Vasco da Gama reached Calicut in 1498.|প্ৰমাণ লিখা হ'ল: ১৪৯৮ত ভাস্কো দা গামাই কালিকট পাইছিল।",
 ["Vasco da Gama found the sea route to India|ভাস্কো দা গামাই ভাৰতলৈ সাগৰৰ পথ বিচাৰি পাইছিল", "He reached Calicut in May 1498|১৪৯৮ৰ মে'ত তেওঁ কালিকট পাইছিল", "He sailed for Portugal round the Cape|তেওঁ পৰ্তুগালৰ হৈ উত্তমাশা অন্তৰীপ ঘূৰি আহিছিল", "A pilot from Malindi guided him across|মালিন্দিৰ এজন পথপ্ৰদৰ্শকে তেওঁক আনিছিল"],
 S("Round the Cape|অন্তৰীপ ঘূৰি", "[[vasco-da-gama|Vasco da Gama]] left Portugal in 1497, rounded the Cape of Good Hope and sailed up East Africa.|[[vasco-da-gama|ভাস্কো দা গামাই]] ১৪৯৭ত পৰ্তুগাল এৰি উত্তমাশা অন্তৰীপ ঘূৰি পূব আফ্ৰিকাৰ উপকূলেদি আহিছিল।", "At Malindi he hired a Gujarati pilot, who guided the fleet across the ocean.|মালিন্দিত তেওঁ এজন গুজৰাটী পথপ্ৰদৰ্শক ল'লে, যিয়ে নৌবহৰক মহাসাগৰ পাৰ কৰাইছিল।", art="embassy"),
 S("Calicut, 1498|কালিকট, ১৪৯৮", "He reached <mark>[[calicut|Calicut]]</mark> in May <mark>1498</mark>. Portuguese, Dutch, English and French traders followed in time.|<mark>১৪৯৮ৰ</mark> মে'ত তেওঁ <mark>[[calicut|কালিকট]]</mark> পাইছিল। সময়ত পৰ্তুগীজ, ডাচ, ইংৰাজ আৰু ফৰাচী বেপাৰী আহিল।", art="calendar"),
 IN("The sea route to India from Europe was found by|ইউৰোপৰ পৰা ভাৰতলৈ সাগৰৰ পথ বিচাৰি পাইছিল", ".|এ।", ["Christopher Columbus|ক্ৰিষ্টোফাৰ কলম্বাছ", "Vasco da Gama|ভাস্কো দা গামা", "Ibn Battuta|ইবন বতুতা", "Thomas Roe|টমাছ ৰ'"], 1, "Vasco da Gama.|ভাস্কো দা গামা।"),
 MP("Tap Calicut.|কালিকট টিপা।", "calicut", ["calicut", "plassey", "buxar", "surat"], "On the Malabar coast.|মালাবাৰ উপকূলত।"),
 TF("Vasco da Gama sailed for England.|ভাস্কো দা গামা ইংলেণ্ডৰ হৈ আহিছিল।", False, "He sailed for Portugal.|তেওঁ পৰ্তুগালৰ হৈ আহিছিল।"),
 OR("Trace his voyage.|তেওঁৰ যাত্ৰা অনুসৰণ কৰা।", ["Lisbon|লিচবন", "Cape of Good Hope|উত্তমাশা অন্তৰীপ", "Malindi|মালিন্দি", "Calicut|কালিকট"], "West to east, round Africa.|আফ্ৰিকা ঘূৰি পশ্চিমৰ পৰা পূবলৈ।"),
 SP("Vasco da Gama reached Calicut in *1598.*|ভাস্কো দা গামাই *১৫৯৮ত* কালিকট পাইছিল।", "1498|১৪৯৮ত", "1498.|১৪৯৮।"),
)
u2 = U(2, "flag", "Plassey, 1757|পলাশী, ১৭৫৭",
 "Find out why the Nawab's large army lost.|নবাবৰ ডাঙৰ সৈন্য কিয় হাৰিল, বিচাৰি উলিওৱা।", "Finding recorded: Mir Jafar stood idle, and Clive won.|প্ৰমাণ লিখা হ'ল: মীৰ জাফৰ নিষ্ক্ৰিয় আছিল, ক্লাইভ জিকিল।",
 ["Plassey was fought on 23 June 1757|১৭৫৭ৰ ২৩ জুনত পলাশীৰ যুদ্ধ", "Robert Clive led the Company's force|ৰবাৰ্ট ক্লাইভে কোম্পানীৰ সৈন্য চলাইছিল", "Siraj ud-Daulah was Nawab of Bengal|চিৰাজ-উদ-দৌলা বংগৰ নবাব", "Mir Jafar held back his troops|মীৰ জাফৰে সৈন্য ৰখি থৈছিল"],
 S("A Nawab and a Company|নবাব আৰু কোম্পানী", "<mark>[[siraj-ud-daulah|Siraj ud-Daulah]]</mark>, Nawab of Bengal, ordered the English to stop fortifying and attacked Calcutta.|বংগৰ নবাব <mark>[[siraj-ud-daulah|চিৰাজ-উদ-দৌলাই]]</mark> ইংৰাজক দুৰ্গ গঢ়া বন্ধ কৰিবলৈ আদেশ দি কলিকতা আক্ৰমণ কৰিছিল।", art="court"),
 S("The bribed commander|উৎকোচ লোৱা সেনাপতি", "On 23 June <mark>1757</mark> [[robert-clive|Robert Clive]] met him at [[plassey]]. Clive had promised his commander, <mark>[[mir-jafar|Mir Jafar]]</mark>, the throne.|<mark>১৭৫৭ৰ</mark> ২৩ জুনত [[robert-clive|ৰবাৰ্ট ক্লাইভে]] [[plassey|পলাশীত]] তেওঁক সন্মুখীন হৈছিল। ক্লাইভে তেওঁৰ সেনাপতি <mark>[[mir-jafar|মীৰ জাফৰক]]</mark> সিংহাসনৰ প্ৰতিশ্ৰুতি দিছিল।", "Mir Jafar kept his troops idle, and the Company won.|মীৰ জাফৰে সৈন্য নিষ্ক্ৰিয় ৰাখিলে, কোম্পানী জিকিল।", map={"base": "india", "box": [80, 21, 92, 28.5], "show": ["plassey", "calcutta", "buxar"]}),
 IN("The Company's armies defeated Siraj ud-Daulah at|কোম্পানীৰ সৈন্যই চিৰাজ-উদ-দৌলাক হৰুৱাইছিল", ".|ত।", ["Battle of Buxar|বক্সাৰৰ যুদ্ধ", "Battle of Plassey|পলাশীৰ যুদ্ধ", "Battle of Nalapani|নালাপানিৰ যুদ্ধ", "Battle of the Jhelum|জিলমৰ যুদ্ধ"], 1, "Plassey, 1757.|১৭৫৭ত পলাশী।"),
 WH(["I was Siraj's commander.|মই চিৰাজৰ সেনাপতি।", "Clive promised me the throne.|ক্লাইভে মোক সিংহাসনৰ প্ৰতিশ্ৰুতি দিছিল।", "I became Nawab after Plassey.|পলাশীৰ পিছত মই নবাব হৈছিলোঁ।"], ["Mir Qasim|মীৰ কাছিম", "Mir Jafar|মীৰ জাফৰ", "Mir Jumla|মীৰজুমলা", "Shuja-ud-Daula|চুজা-উদ-দৌলা"], 1, "Mir Jafar.|মীৰ জাফৰ।"),
 MP("Tap Plassey.|পলাশী টিপা।", "plassey", ["plassey", "calicut", "surat", "buxar"], "In Bengal.|বংগত।"),
 TF("Siraj ud-Daulah lost partly through betrayal.|চিৰাজ-উদ-দৌলা আংশিকভাৱে বিশ্বাসঘাতকতাৰ বাবে হাৰিছিল।", True, "Mir Jafar kept his troops out of the fight.|মীৰ জাফৰে সৈন্য যুদ্ধৰ বাহিৰত ৰাখিছিল।"),
 SP("Plassey was won by Hector *Munro.*|পলাশীত হেক্টৰ *মুনৰো* জয়ী হৈছিল।", "Clive|ক্লাইভ", "Munro won at Buxar.|মুনৰো বক্সাৰত জয়ী হৈছিল।"),
)
u3 = U(3, "flag", "Buxar, 1764|বক্সাৰ, ১৭৬৪",
 "See why Buxar mattered more than Plassey.|বক্সাৰ পলাশীতকৈ কিয় গুৰুত্বপূৰ্ণ, চোৱা।", "Finding recorded: three allies lost at Buxar, and the Company won the Diwani.|প্ৰমাণ লিখা হ'ল: বক্সাৰত তিনি মিত্ৰ হাৰিল, কোম্পানীয়ে দেৱানী পালে।",
 ["Buxar was fought in October 1764|১৭৬৪ৰ অক্টোবৰত বক্সাৰৰ যুদ্ধ", "Hector Munro led the Company's force|হেক্টৰ মুনৰোৱে কোম্পানীৰ সৈন্য চলাইছিল", "Mir Qasim, Shuja-ud-Daula and Shah Alam II lost|মীৰ কাছিম, চুজা-উদ-দৌলা আৰু শ্বাহ আলম দ্বিতীয় হাৰিছিল", "The Treaty of Allahabad gave the Diwani in 1765|১৭৬৫ৰ এলাহাবাদ সন্ধিয়ে দেৱানী দিছিল"],
 S("Three against one|তিনি বনাম এক", "In October <mark>1764</mark> Hector Munro beat three allies at [[buxar]]: <b>Mir Qasim, Shuja-ud-Daula and Shah Alam II</b>.|<mark>১৭৬৪ৰ</mark> অক্টোবৰত হেক্টৰ মুনৰোৱে [[buxar|বক্সাৰত]] তিনি মিত্ৰক হৰুৱাইছিল: <b>মীৰ কাছিম, চুজা-উদ-দৌলা আৰু শ্বাহ আলম দ্বিতীয়</b>।", art="embassy"),
 S("The right to collect|সংগ্ৰহৰ অধিকাৰ", "The <mark>Treaty of Allahabad</mark> of 1765 gave the Company the <mark>[[diwani|Diwani]]</mark>: the right to collect revenue in Bengal, Bihar and Orissa.|১৭৬৫ৰ <mark>এলাহাবাদ সন্ধিয়ে</mark> কোম্পানীক <mark>[[diwani|দেৱানী]]</mark> দিছিল: বংগ, বিহাৰ আৰু উৰিষ্যাৰ ৰাজহ সংগ্ৰহৰ অধিকাৰ।", art="scroll"),
 MA([("Plassey, 1757|পলাশী, ১৭৫৭", "Siraj ud-Daulah|চিৰাজ-উদ-দৌলা"), ("Buxar, 1764|বক্সাৰ, ১৭৬৪", "Mir Qasim and allies|মীৰ কাছিম আৰু মিত্ৰ"), ("Allahabad, 1765|এলাহাবাদ, ১৭৬৫", "Diwani|দেৱানী")], "Keep the three dates apart.|তিনিওটা তাৰিখ পৃথক ৰাখা।"),
 OD("Who did NOT fight the Company at Buxar?|বক্সাৰত কোনে কোম্পানীৰ বিৰুদ্ধে যুঁজা নাছিল?", ["Mir Qasim|মীৰ কাছিম", "Shuja-ud-Daula|চুজা-উদ-দৌলা", "Shah Alam II|শ্বাহ আলম দ্বিতীয়", "Mir Jafar|মীৰ জাফৰ"], 3, "The other three were the allies.|আন তিনিজন মিত্ৰ আছিল।"),
 TF("Diwani means the right to collect revenue.|দেৱানী মানে ৰাজহ সংগ্ৰহৰ অধিকাৰ।", True, "In Bengal, Bihar and Orissa.|বংগ, বিহাৰ আৰু উৰিষ্যাত।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1757, "Plassey|পলাশী"), (1765, "Diwani|দেৱানী")], [("Third Panipat, 1761|তৃতীয় পানিপথ, ১৭৬১", 1), ("Buxar, 1764|বক্সাৰ, ১৭৬৪", 1), ("Regulating Act, 1773|ৰেগুলেটিং আইন, ১৭৭৩", 2)], "1757 → 1761 → 1764 → 1765 → 1773.|১৭৫৭ → ১৭৬১ → ১৭৬৪ → ১৭৬৫ → ১৭৭৩।"),
 SC("Unscramble the revenue right.|ৰাজহৰ অধিকাৰটো সজোৱা।", "DIWANI", ["দে", "ৱা", "নী"], "Diwani.|দেৱানী।"),
)
u4 = U(4, "crown", "From traders to rulers|বেপাৰীৰ পৰা শাসক",
 "State what changed by 1765.|১৭৬৫লৈ কি সলনি হ'ল, কোৱা।", "Finding recorded: a trading company now held revenue and puppet Nawabs.|প্ৰমাণ লিখা হ'ল: এটা বেপাৰী কোম্পানীৰ হাতত এতিয়া ৰাজহ আৰু পুতলা নবাব।",
 ["After Plassey Mir Jafar ruled as a puppet|পলাশীৰ পিছত মীৰ জাফৰ পুতলা শাসক", "Company power began in Bengal|কোম্পানীৰ ক্ষমতা বংগত আৰম্ভ", "Buxar broke Mughal political control further|বক্সাৰে মোগল ৰাজনৈতিক নিয়ন্ত্ৰণ আৰু ভাঙিলে", "The Company took full control of Bengal-Bihar in 1772|১৭৭২ত কোম্পানীয়ে বংগ-বিহাৰৰ সম্পূৰ্ণ নিয়ন্ত্ৰণ ল'লে"],
 S("A Nawab in name|নামতহে নবাব", "After Plassey [[mir-jafar|Mir Jafar]] was Nawab, but as a <mark>puppet</mark>. Bengal fell under the Company in practice.|পলাশীৰ পিছত [[mir-jafar|মীৰ জাফৰ]] নবাব, কিন্তু <mark>পুতলা</mark>। কাৰ্যতঃ বংগ কোম্পানীৰ অধীন হ'ল।", art="court"),
 S("Mughal title, Company power|মোগল উপাধি, কোম্পানীৰ ক্ষমতা", "With the Diwani the emperor's own title legalised Company revenue. In 1772 the Company took full control of Bengal-Bihar.|দেৱানীৰে সম্ৰাটৰ নিজৰ উপাধিয়ে কোম্পানীৰ ৰাজহক বৈধ কৰিলে। ১৭৭২ত কোম্পানীয়ে বংগ-বিহাৰৰ সম্পূৰ্ণ নিয়ন্ত্ৰণ ল'লে।", "The story now moves from battles to laws, starting with the <mark>Regulating Act of 1773</mark>.|কাহিনী এতিয়া যুদ্ধৰ পৰা আইনলৈ যায়, <mark>১৭৭৩ৰ ৰেগুলেটিং আইনৰ</mark> পৰা।", art="scroll"),
 TF("After Plassey, Bengal's Nawab held real independent power.|পলাশীৰ পিছত বংগৰ নবাবৰ প্ৰকৃত স্বাধীন ক্ষমতা আছিল।", False, "Mir Jafar was a puppet.|মীৰ জাফৰ পুতলা আছিল।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Calicut|কালিকট", "Plassey|পলাশী", "Buxar|বক্সাৰ", "Diwani|দেৱানী", "Regulating Act|ৰেগুলেটিং আইন"], "1498, 1757, 1764, 1765, 1773.|১৪৯৮, ১৭৫৭, ১৭৬৪, ১৭৬৫, ১৭৭৩।"),
 IN("The Company's next step after the Diwani was the|দেৱানীৰ পিছত আহিল", " of 1773.|, ১৭৭৩ত।", ["Regulating Act|ৰেগুলেটিং আইন", "Rowlatt Act|ৰাউলাট আইন", "Salt Act|লৱণ আইন", "Charter Act|চাৰ্টাৰ আইন"], 0, "The Regulating Act.|ৰেগুলেটিং আইন।"),
 SP("Bengal fell under the *Dutch* Company.|বংগ *ডাচ* কোম্পানীৰ অধীন হৈছিল।", "English|ইংৰাজ", "The English East India Company.|ইংৰাজ ইষ্ট ইণ্ডিয়া কোম্পানী।"),
 WH(["I was a Mughal emperor.|মই মোগল সম্ৰাট।", "I fought at Buxar.|মই বক্সাৰত যুঁজিছিলোঁ।", "I granted the Diwani.|মই দেৱানী দিছিলোঁ।"], ["Aurangzeb|ঔৰংগজেব", "Shah Alam II|শ্বাহ আলম দ্বিতীয়", "Bahadur Shah II|বাহাদুৰ শ্বাহ দ্বিতীয়", "Shah Jahan|শ্বাহজাহান"], 1, "Shah Alam II.|শ্বাহ আলম দ্বিতীয়।"),
)
test = TEST("Show how a Company took Bengal.|কোম্পানীয়ে বংগ কেনেকৈ ল'লে, দেখুওৱা।", "Recorded: sea route, Plassey, Buxar and the Diwani.|লিখা হ'ল: সাগৰৰ পথ, পলাশী, বক্সাৰ আৰু দেৱানী।",
 IN("The Company's armies defeated Siraj ud-Daulah at|কোম্পানীৰ সৈন্যই চিৰাজ-উদ-দৌলাক হৰুৱাইছিল", ".|ত।", ["Buxar|বক্সাৰ", "Plassey|পলাশী", "Nalapani|নালাপানি", "the Jhelum|জিলম"], 1, "Plassey.|পলাশী।"),
 TF("Vasco da Gama reached India in 1498.|১৪৯৮ত ভাস্কো দা গামাই ভাৰত পাইছিল।", True, "At Calicut.|কালিকটত।"),
 MP("Tap Buxar.|বক্সাৰ টিপা।", "buxar", ["buxar", "calicut", "surat", "plassey"], "In Bihar.|বিহাৰত।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Plassey|পলাশী", "Buxar|বক্সাৰ", "Treaty of Allahabad|এলাহাবাদ সন্ধি"], "1757, 1764, 1765.|১৭৫৭, ১৭৬৪, ১৭৬৫।"),
 MA([("Robert Clive|ৰবাৰ্ট ক্লাইভ", "Plassey|পলাশী"), ("Hector Munro|হেক্টৰ মুনৰো", "Buxar|বক্সাৰ")], "Commander and battle.|সেনাপতি আৰু যুদ্ধ।"),
 MC("Consider these statements. (1) Mir Jafar became Nawab after Plassey. (2) Hector Munro won at Plassey. (3) The Diwani covered Bengal, Bihar and Orissa. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) পলাশীৰ পিছত মীৰ জাফৰ নবাব হৈছিল। (২) পলাশীত হেক্টৰ মুনৰো জয়ী হৈছিল। (৩) দেৱানীয়ে বংগ, বিহাৰ আৰু উৰিষ্যা সামৰিছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Clive won at Plassey.|ক্লাইভ পলাশীত জয়ী হৈছিল।"),
)
LESSON(18, "Plassey and Buxar|পলাশী আৰু বক্সাৰ", "1498–1765|১৪৯৮–১৭৬৫", "Company rule|কোম্পানীৰ শাসন", "Evidence file 18|প্ৰমাণ নথি ১৮", "From traders to rulers|বেপাৰীৰ পৰা শাসক",
 "A trading company won a province through a bribe, a battle and a signature. Follow how it happened.|এটা বেপাৰী কোম্পানীয়ে উৎকোচ, যুদ্ধ আৰু স্বাক্ষৰেৰে এটা প্ৰদেশ জিকিলে। কেনেকৈ হ'ল, অনুসৰণ কৰা।",
 sources, [u1, u2, u3, u4], test, ["calicut", "plassey", "buxar", "surat"],
 timeline=[("1498", "Vasco da Gama at Calicut|কালিকটত ভাস্কো দা গামা", "u1"), ("1757", "Battle of Plassey|পলাশীৰ যুদ্ধ", "u2"), ("1764", "Battle of Buxar|বক্সাৰৰ যুদ্ধ", "u3"), ("1765", "Diwani granted|দেৱানী প্ৰদান", "u3")])
