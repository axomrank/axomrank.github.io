#!/usr/bin/env python3
"""Lesson 2: The Vedic age."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403

PLACES({
 "rigveda": ("term", "Rigveda|ঋগ্বেদ", "Oldest of the four Vedas|চাৰি বেদৰ ভিতৰত আটাইতকৈ পুৰণি"),
 "sabha-samiti": ("term", "Sabha and Samiti|সভা আৰু সমিতি", "Assemblies that checked the early Vedic rajan|প্ৰাৰম্ভিক বৈদিক ৰাজনক নিয়ন্ত্ৰণ কৰা সভা"),
})
sources = [
 src("Wikipedia, Vedic period", "https://en.wikipedia.org/wiki/Vedic_period", "Used as a guide: early and later Vedic dates, Rigveda as the oldest, geography, sabha and samiti, varna, iron, migration view. Check in review."),
 src("Wikipedia, Sarasvati River", "https://en.wikipedia.org/wiki/Sarasvati_River", "Used as a guide: Ghaggar-Hakra identification and objections. Check in review."),
 src("APSC CCE Prelims 2025 GS-I, question 24, page read", "https://apsc.nic.in/cce.html", "Exam wording of the Saraswati question. The export's answer key does not fit the printed options."),
]
u1 = U(1, "scroll", "Four Vedas|চাৰি বেদ",
 "Learn the Vedas and which came first.|বেদসমূহ আৰু আটাইতকৈ পুৰণিখন শিকা।",
 "Finding recorded: the Rigveda is the earliest compilation.|প্ৰমাণ লিখা হ'ল: ঋগ্বেদ আটাইতকৈ পুৰণি সংকলন।",
 ["There are four Vedas|বেদ চাৰিখন", "The Rigveda is the earliest|ঋগ্বেদ আটাইতকৈ পুৰণি", "The Rigveda is our main source for the earliest Vedic age|আদি বৈদিক যুগৰ মূল উৎস ঋগ্বেদ", "The Vedas were passed on orally|বেদ মুখে মুখে প্ৰচলিত আছিল"],
 S("Words, not cities|নগৰ নহয়, শব্দ",
   "For the Indus cities we have objects and no readable words. For the Vedic age it is nearly the reverse: we have <mark>texts</mark>.|সিন্ধু নগৰৰ বাবে বস্তু আছে, পঢ়িব পৰা শব্দ নাই। বৈদিক যুগৰ বাবে প্ৰায় ওলোটা: <mark>গ্ৰন্থ</mark> আছে।",
   "The Vedas were composed roughly 1500 to 900 BCE and passed on orally.|বেদ প্ৰায় খ্ৰীষ্টপূৰ্ব ১৫০০ৰ পৰা ৯০০ৰ ভিতৰত ৰচিত, মুখে মুখে প্ৰচলিত আছিল।", art="scroll"),
 S("Four books, one oldest|চাৰিখন গ্ৰন্থ, এখন পুৰণি",
   "The four Vedas are <b>Rigveda, Samaveda, Yajurveda, Atharvaveda</b>.|চাৰি বেদ হ'ল <b>ঋগ্বেদ, সামবেদ, যজুৰ্বেদ, অথৰ্ববেদ</b>।",
   "The <mark>[[rigveda|Rigveda]]</mark> is the earliest, and the main source for the earliest Vedic culture.|<mark>[[rigveda|ঋগ্বেদ]]</mark> আটাইতকৈ পুৰণি, আৰু আদি বৈদিক সংস্কৃতিৰ মূল উৎস।", art="seal"),
 IN("The earliest compilation among the Vedas is the|বেদৰ ভিতৰত আটাইতকৈ পুৰণি সংকলন", ".|।", ["Yajurveda|যজুৰ্বেদ", "Atharvaveda|অথৰ্ববেদ", "Rigveda|ঋগ্বেদ", "Samaveda|সামবেদ"], 2, "The Rigveda is the oldest layer.|ঋগ্বেদ আটাইতকৈ পুৰণি স্তৰ।"),
 OD("Which is NOT one of the four Vedas?|কোনখন চাৰি বেদৰ এখন নহয়?", ["Samaveda|সামবেদ", "Atharvaveda|অথৰ্ববেদ", "Yajurveda|যজুৰ্বেদ", "Arthashastra|অৰ্থশাস্ত্ৰ"], 3, "The Arthashastra is a treatise on statecraft.|অৰ্থশাস্ত্ৰ ৰাজ্য পৰিচালনাৰ গ্ৰন্থ।"),
 TF("The Vedas were first spread as printed books.|বেদ প্ৰথমে ছপা কিতাপ হিচাপে প্ৰচলিত হৈছিল।", False, "They were passed on orally.|সেইবোৰ মুখে মুখে প্ৰচলিত আছিল।"),
 SC("Unscramble the oldest Veda.|আটাইতকৈ পুৰণি বেদখন সজোৱা।", "RIGVEDA", ["ঋ", "গ্বে", "দ"], "The Rigveda came first.|ঋগ্বেদ প্ৰথম।"),
 WH(["I am a Veda.|মই এখন বেদ।", "I am the oldest of the four.|মই চাৰিখনৰ ভিতৰত আটাইতকৈ পুৰণি।", "I tell of the earliest Vedic culture.|মই আদি বৈদিক সংস্কৃতিৰ কথা কওঁ।"], ["Samaveda|সামবেদ", "Rigveda|ঋগ্বেদ", "Atharvaveda|অথৰ্ববেদ", "Yajurveda|যজুৰ্বেদ"], 1, "The Rigveda.|ঋগ্বেদ।"),
)
u2 = U(2, "river", "The Saraswati question|সৰস্বতীৰ প্ৰশ্ন",
 "Know the exam answer and why scholars still argue.|পৰীক্ষাৰ উত্তৰ আৰু পণ্ডিতৰ বিতৰ্কৰ কাৰণ জানা।",
 "Finding recorded: the Ghaggar-Hakra is the usual answer, and the identification is disputed.|প্ৰমাণ লিখা হ'ল: ঘগ্গৰ-হাক্ৰা সাধাৰণ উত্তৰ, কিন্তু ইয়াৰ পৰিচয় বিতৰ্কিত।",
 ["Early Vedic life centred on Punjab and the north-west|আদি বৈদিক জীৱনৰ কেন্দ্ৰ পঞ্জাব আৰু উত্তৰ-পশ্চিম", "Later Vedic culture spread to the Ganga-Yamuna plain|পৰৱৰ্তী বৈদিক সংস্কৃতি গংগা-যমুনা সমভূমিলৈ বিয়পিল", "Many scholars identify the Saraswati with the Ghaggar-Hakra|বহু পণ্ডিতে সৰস্বতীক ঘগ্গৰ-হাক্ৰা বুলি ধৰে", "Others dispute it, and some point to Afghanistan|আনে ইয়াত সন্মত নহয়, কোনোৱে আফগানিস্তানলৈ আঙুলিয়ায়"],
 S("Moving east|পূৱলৈ গতি",
   "Early Vedic life centred on <mark>Punjab</mark> and the north-west. Later it spread east to the Ganga-Yamuna plain.|আদি বৈদিক জীৱনৰ কেন্দ্ৰ আছিল <mark>পঞ্জাব</mark> আৰু উত্তৰ-পশ্চিম। পিছত ই পূবৰ গংগা-যমুনা সমভূমিলৈ বিয়পিল।", art="houses"),
 S("A river in dispute|বিতৰ্কিত নদী",
   "The Rigveda praises a river called the Saraswati. Papers expect the <mark>Ghaggar-Hakra</mark> system, the identification many scholars since the 19th century have made.|ঋগ্বেদত সৰস্বতী নদীৰ প্ৰশংসা আছে। পৰীক্ষাত <mark>ঘগ্গৰ-হাক্ৰা</mark> ব্যৱস্থাৰ উত্তৰ বিচাৰে, ঊনবিংশ শতিকাৰ পৰা বহু পণ্ডিতে তেনেকৈ ধৰিছে।",
   "Others object from geology and the text, and some suggest the Helmand in Afghanistan. Treat it as an identification, not a settled fact.|আনে ভূতত্ত্ব আৰু গ্ৰন্থৰ পৰা আপত্তি কৰে, কোনোৱে আফগানিস্তানৰ হেলমন্দৰ কথা কয়। ইয়াক নিশ্চিত তথ্য নহয়, পৰিচয় বুলি ধৰা।", art="scroll"),
 IN("Papers identify the Rigvedic Saraswati with the|পৰীক্ষাত ঋগ্বেদৰ সৰস্বতীক ধৰা হয়", ".|।", ["Ganga|গংগা", "Yamuna|যমুনা", "Sutlej|শতদ্ৰু", "Ghaggar-Hakra|ঘগ্গৰ-হাক্ৰা"], 3, "That is the expected answer, though disputed.|এয়া প্ৰত্যাশিত উত্তৰ, যদিও বিতৰ্কিত।"),
 TF("All scholars agree on which river the Saraswati was.|সৰস্বতী কোন নদী, সকলো পণ্ডিত একমত।", False, "The identification is disputed.|এই পৰিচয় বিতৰ্কিত।"),
 OR("Put the spread of Vedic culture in order.|বৈদিক সংস্কৃতিৰ বিস্তাৰ ক্ৰমে সজোৱা।", ["Punjab and the north-west|পঞ্জাব আৰু উত্তৰ-পশ্চিম", "Ganga-Yamuna plain|গংগা-যমুনা সমভূমি"], "It moved east over time.|সময়ত ই পূবলৈ গ'ল।"),
 SP("Early Vedic life centred on *Bengal* and the north-west.|আদি বৈদিক জীৱনৰ কেন্দ্ৰ *বংগ* আৰু উত্তৰ-পশ্চিম।", "Punjab|পঞ্জাব", "It centred on Punjab.|কেন্দ্ৰ পঞ্জাব।"),
 MA([("Papers' answer|পৰীক্ষাৰ উত্তৰ", "Ghaggar-Hakra|ঘগ্গৰ-হাক্ৰা"), ("Another proposal|আন এটা প্ৰস্তাৱ", "Helmand, Afghanistan|হেলমন্দ, আফগানিস্তান")], "Know both, and answer the paper.|দুয়োটা জানা, পৰীক্ষাৰ উত্তৰ দিয়া।"),
)
u3 = U(3, "hands", "From tribe to kingdom|জনগোষ্ঠীৰ পৰা ৰাজ্যলৈ",
 "Contrast early and later Vedic society.|আদি আৰু পৰৱৰ্তী বৈদিক সমাজ তুলনা কৰা।",
 "Finding recorded: assemblies weakened, kings and varna hardened, iron spread.|প্ৰমাণ লিখা হ'ল: সভা দুৰ্বল হ'ল, ৰজা আৰু বৰ্ণ কঠোৰ হ'ল, লোহা বিয়পিল।",
 ["The early rajan was checked by sabha and samiti|আদি ৰাজনক সভা আৰু সমিতিয়ে নিয়ন্ত্ৰণ কৰিছিল", "Later, tribes became small kingdoms|পিছত জনগোষ্ঠী সৰু ৰাজ্য হ'ল", "The four-part varna order rose in the later period|পৰৱৰ্তী যুগত চতুৰ্বৰ্ণ ব্যৱস্থা গঢ় ল'লে", "Iron helped clear forests for farming|লোহাই খেতিৰ বাবে হাবি পৰিষ্কাৰত সহায় কৰিছিল"],
 S("A rajan and his assemblies|ৰাজন আৰু সভা",
   "Early Vedic groups were tribes led by a <mark>rajan</mark>, whose power was checked by the [[sabha-samiti|sabha and samiti]].|আদি বৈদিক গোষ্ঠী <mark>ৰাজনৰ</mark> নেতৃত্বত জনগোষ্ঠী আছিল, [[sabha-samiti|সভা আৰু সমিতিয়ে]] তেওঁৰ ক্ষমতা নিয়ন্ত্ৰণ কৰিছিল।", art="court"),
 S("Later changes|পিছৰ পৰিৱৰ্তন",
   "Later, tribes merged into small kingdoms and the assemblies lost influence. The four-part <mark>varna</mark> order took shape.|পিছত জনগোষ্ঠী সৰু ৰাজ্যত মিলিল আৰু সভাৰ প্ৰভাৱ কমিল। চতুৰ্বৰ্ণ <mark>ব্যৱস্থা</mark> গঢ় ল'লে।",
   "<mark>Iron</mark> spread, helping people clear forest and settle to farm.|<mark>লোহা</mark> বিয়পিল, হাবি পৰিষ্কাৰ কৰি খেতিত থিতাপি লোৱাত সহায় কৰিলে।", art="houses"),
 MA([("Early Vedic|আদি বৈদিক", "Tribes under a rajan|ৰাজনৰ অধীনত জনগোষ্ঠী"), ("Later Vedic|পৰৱৰ্তী বৈদিক", "Small kingdoms|সৰু ৰাজ্য")], "The political unit grew.|ৰাজনৈতিক একক ডাঙৰ হ'ল।"),
 TF("Assemblies grew stronger in the later Vedic period.|পৰৱৰ্তী বৈদিক যুগত সভা শক্তিশালী হৈছিল।", False, "They lost influence as kings grew stronger.|ৰজা শক্তিশালী হোৱাৰ লগে লগে সভাৰ প্ৰভাৱ কমিল।"),
 IN("Early Vedic assemblies were the sabha and the|আদি বৈদিক সভা আছিল সভা আৰু", ".|।", ["mahajanapada|মহাজনপদ", "samiti|সমিতি", "sangha|সংঘ", "varna|বৰ্ণ"], 1, "Sabha and samiti.|সভা আৰু সমিতি।"),
 OD("Which belongs to the later Vedic age, not the early one?|কোনটো আদি নহয়, পৰৱৰ্তী বৈদিক যুগৰ?", ["Rajan with assemblies|সভাসহ ৰাজন", "Tribal groups|জনগোষ্ঠী", "Spread of iron|লোহাৰ বিস্তাৰ", "Focus on Punjab|পঞ্জাবত কেন্দ্ৰ"], 2, "Iron spread in the later period.|পৰৱৰ্তী যুগত লোহা বিয়পিল।"),
 SP("Iron helped clear forests for *fishing.*|লোহাই *মাছৰ* বাবে হাবি পৰিষ্কাৰত সহায় কৰিছিল।", "farming|খেতিৰ বাবে", "Iron tools helped farming.|লোহাৰ সঁজুলিয়ে খেতিত সহায় কৰিছিল।"),
)
test = TEST("Show you can read the Vedic age from its texts.|গ্ৰন্থৰ পৰা বৈদিক যুগ পঢ়িব পাৰা বুলি দেখুওৱা।", "Recorded: the Vedas, the river question and social change.|লিখা হ'ল: বেদ, নদীৰ প্ৰশ্ন আৰু সামাজিক পৰিৱৰ্তন।",
 IN("The Veda that depicts the most ancient Vedic culture is the|আটাইতকৈ পুৰণি বৈদিক সংস্কৃতিৰ বৰ্ণনা থকা বেদ", ".|।", ["Rigveda|ঋগ্বেদ", "Yajurveda|যজুৰ্বেদ", "Atharvaveda|অথৰ্ববেদ", "Samaveda|সামবেদ"], 0, "The Rigveda.|ঋগ্বেদ।"),
 OD("Which is NOT a Veda?|কোনখন বেদ নহয়?", ["Rigveda|ঋগ্বেদ", "Samaveda|সামবেদ", "Yajurveda|যজুৰ্বেদ", "Rajatarangini|ৰাজতৰংগিণী"], 3, "The Rajatarangini is Kalhana's history of Kashmir.|ৰাজতৰংগিণী কলহণৰ কাশ্মীৰ ইতিহাস।"),
 TF("The Ghaggar-Hakra identification of the Saraswati is disputed.|সৰস্বতীক ঘগ্গৰ-হাক্ৰা বুলি ধৰাটো বিতৰ্কিত।", True, "Yes, though papers expect it.|হয়, যদিও পৰীক্ষাত এইটোৱে বিচাৰে।"),
 MA([("Sabha and samiti|সভা আৰু সমিতি", "Early assemblies|আদি সভা"), ("Iron|লোহা", "Forest clearing|হাবি পৰিষ্কাৰ"), ("Varna|বৰ্ণ", "Four-part order|চতুৰ্বিধ ব্যৱস্থা")], "Terms and meanings.|শব্দ আৰু অৰ্থ।"),
 OR("Order the sources of Indian history.|ভাৰতীয় ইতিহাসৰ উৎস ক্ৰমে সজোৱা।", ["Indus seals|সিন্ধু মোহৰ", "Rigveda|ঋগ্বেদ", "Ashokan edicts|অশোকৰ অনুশাসন"], "About 2600 BCE, about 1400 BCE, about 250 BCE.|প্ৰায় খ্ৰীষ্টপূৰ্ব ২৬০০, ১৪০০, ২৫০।"),
 MC("Consider these statements. (1) The Rigveda is the oldest Veda. (2) Sabha and samiti gained power in the later Vedic age. (3) Iron spread in the later Vedic age. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ঋগ্বেদ আটাইতকৈ পুৰণি। (২) পৰৱৰ্তী বৈদিক যুগত সভা আৰু সমিতিৰ ক্ষমতা বাঢ়িছিল। (৩) পৰৱৰ্তী বৈদিক যুগত লোহা বিয়পিছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "The assemblies lost influence.|সভাৰ প্ৰভাৱ কমিছিল।"),
)
LESSON(2, "The Vedic age|বৈদিক যুগ", "c. 1500–600 BCE|প্ৰায় খ্ৰীষ্টপূৰ্ব ১৫০০–৬০০", "Beginnings|আৰম্ভণি", "Evidence file 2|প্ৰমাণ নথি ২", "A history made of hymns|স্তোত্ৰৰে গঢ়া ইতিহাস",
 "No Vedic city has been dug up as Harappa was. So how do we know this age? Read it from its texts, and mark where scholars disagree.|হৰপ্পাৰ দৰে বৈদিক নগৰ খনন হোৱা নাই। তেন্তে এই যুগ কেনেকৈ জানো? গ্ৰন্থৰ পৰা পঢ়া, পণ্ডিতৰ মতভেদ চিনাক্ত কৰা।",
 sources, [u1, u2, u3], test, [])
