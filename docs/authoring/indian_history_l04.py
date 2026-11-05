#!/usr/bin/env python3
"""Lesson 4: Magadha and Alexander."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "magadha": ("place", "Magadha|মগধ", "Ancient kingdom in today's Bihar|আজিৰ বিহাৰৰ প্ৰাচীন ৰাজ্য", [25.0, 85.4]),
 "rajagriha": ("place", "Rajagriha|ৰাজগৃহ", "Early capital of Magadha, today's Rajgir|মগধৰ আদি ৰাজধানী, আজিৰ ৰাজগীৰ", [25.03, 85.42]),
 "mahajanapada": ("term", "Mahajanapada|মহাজনপদ", "One of sixteen great states of the 6th to 4th centuries BCE|খ্ৰীষ্টপূৰ্ব ষষ্ঠৰ পৰা চতুৰ্থ শতিকাৰ ষোল্লটা ডাঙৰ ৰাজ্যৰ এটা"),
 "bimbisara": ("person", "Bimbisara|বিম্বিসাৰ", "Haryanka king of Magadha who annexed Anga|অংগ দখল কৰা মগধৰ হৰ্যংক ৰজা"),
 "ajatashatru": ("person", "Ajatashatru|অজাতশত্ৰু", "Haryanka king who fought for supremacy with Kosala|কোশলৰ সৈতে যুঁজা হৰ্যংক ৰজা"),
 "alexander": ("person", "Alexander of Macedon|মেচিডনৰ আলেকজেণ্ডাৰ", "King of Macedonia who invaded the north-west in 326 BCE|খ্ৰীষ্টপূৰ্ব ৩২৬ত উত্তৰ-পশ্চিম আক্ৰমণ কৰা মেচিডনৰ ৰজা"),
 "porus": ("person", "Porus|পুৰু", "King who fought Alexander at the Jhelum|জিলম নদীত আলেকজেণ্ডাৰৰ সৈতে যুঁজা ৰজা"),
 "jhelum": ("place", "Jhelum|জিলম", "River in Punjab, the ancient Hydaspes|পঞ্জাবৰ নদী, প্ৰাচীন হাইডাস্পিছ", [32.9, 73.7]),
 "beas": ("place", "Beas|বিপাশা", "River in Punjab, the ancient Hyphasis|পঞ্জাবৰ নদী, প্ৰাচীন হাইফেছিছ", [31.5, 75.3]),
})
sources = [
 src("Wikipedia, Mahajanapadas", "https://en.wikipedia.org/wiki/Mahajanapadas", "Used as a guide: sixteen, Anguttara Nikaya list, Magadha's capitals and dynasties. Check in review."),
 src("Wikipedia, Battle of the Hydaspes", "https://en.wikipedia.org/wiki/Battle_of_the_Hydaspes", "Used as a guide: May 326 BCE, Jhelum, outcome, Porus kept as ruler, Beas limit. Porus's reply is reported by Greek-language writers, so it is not taught as his words. Check in review."),
]
u1 = U(1, "houses", "Sixteen great states|ষোল্লটা ডাঙৰ ৰাজ্য",
 "Find out what the Mahajanapadas were.|মহাজনপদ কি আছিল, বিচাৰি উলিওৱা।", "Finding recorded: sixteen states, listed in a Buddhist text.|প্ৰমাণ লিখা হ'ল: ষোল্লটা ৰাজ্য, বৌদ্ধ গ্ৰন্থত তালিকাভুক্ত।",
 ["There were sixteen Mahajanapadas|মহাজনপদ ষোল্লটা আছিল", "They date to about the 6th to 4th centuries BCE|এইবোৰ প্ৰায় খ্ৰীষ্টপূৰ্ব ষষ্ঠৰ পৰা চতুৰ্থ শতিকাৰ", "The Anguttara Nikaya gives the standard list|অংগুত্তৰ নিকায়ত মানক তালিকা আছে", "They included kingdoms and republics|ইয়াত ৰাজ্য আৰু গণৰাজ্য দুয়োটা আছিল"],
 S("A map of sixteen|ষোল্লৰ মানচিত্ৰ", "From about the 6th century BCE, northern India held <mark>sixteen</mark> great states, the [[mahajanapada|Mahajanapadas]].|প্ৰায় খ্ৰীষ্টপূৰ্ব ষষ্ঠ শতিকাৰ পৰা উত্তৰ ভাৰতত <mark>ষোল্লটা</mark> ডাঙৰ ৰাজ্য আছিল, [[mahajanapada|মহাজনপদ]]।", "Some were kingdoms and some were aristocratic republics.|কিছুমান ৰাজ্য, কিছুমান অভিজাত গণৰাজ্য আছিল।", art="houses"),
 S("Who wrote the list?|তালিকা কোনে লিখিলে?", "The standard list comes from a Buddhist text, the <mark>Anguttara Nikaya</mark>. A Jain text gives a different sixteen.|মানক তালিকা বৌদ্ধ গ্ৰন্থ <mark>অংগুত্তৰ নিকায়ৰ</mark>। এখন জৈন গ্ৰন্থত বেলেগ ষোল্লটা আছে।", art="scroll"),
 IN("The number of Mahajanapadas was|মহাজনপদৰ সংখ্যা আছিল", ".|।", ["four|চাৰি", "eight|আঠ", "twelve|বাৰ", "sixteen|ষোল্ল"], 3, "There were sixteen.|ষোল্লটা আছিল।"),
 TF("All Mahajanapadas were monarchies.|সকলো মহাজনপদ ৰাজতন্ত্ৰ আছিল।", False, "Some were aristocratic republics.|কিছুমান অভিজাত গণৰাজ্য আছিল।"),
 SP("The standard list is in the *Rigveda.*|মানক তালিকা *ঋগ্বেদত* আছে।", "Anguttara Nikaya|অংগুত্তৰ নিকায়ত", "It is in a Buddhist text.|ই বৌদ্ধ গ্ৰন্থত আছে।"),
 SC("Unscramble the kingdom that rose highest.|আটাইতকৈ ওপৰলৈ উঠা ৰাজ্যখন সজোৱা।", "MAGADHA", ["ম", "গ", "ধ"], "Magadha came to dominate.|মগধে প্ৰাধান্য লাভ কৰিছিল।"),
 WH(["I am a Buddhist text.|মই বৌদ্ধ গ্ৰন্থ।", "I list sixteen states.|মোত ষোল্লটা ৰাজ্যৰ তালিকা আছে।"], ["Arthashastra|অৰ্থশাস্ত্ৰ", "Anguttara Nikaya|অংগুত্তৰ নিকায়", "Rigveda|ঋগ্বেদ", "Indica|ইণ্ডিকা"], 1, "The Anguttara Nikaya.|অংগুত্তৰ নিকায়।"),
)
u2 = U(2, "crown", "Magadha rises|মগধৰ উত্থান",
 "Order the dynasties of Magadha.|মগধৰ বংশবোৰ ক্ৰমে সজোৱা।", "Finding recorded: Haryanka, Shishunaga, Nanda, then Maurya.|প্ৰমাণ লিখা হ'ল: হৰ্যংক, শিশুনাগ, নন্দ, তাৰ পিছত মৌৰ্য।",
 ["Magadha lay in today's Bihar|মগধ আজিৰ বিহাৰত", "Rajagriha came first, Pataliputra later|প্ৰথমে ৰাজগৃহ, পিছত পাটলিপুত্ৰ", "Bimbisara annexed Anga|বিম্বিসাৰে অংগ দখল কৰিছিল", "The order is Haryanka, Shishunaga, Nanda|ক্ৰম হৰ্যংক, শিশুনাগ, নন্দ"],
 S("From Rajagriha to Pataliputra|ৰাজগৃহৰ পৰা পাটলিপুত্ৰলৈ", "[[magadha]] lay in today's Bihar. Its first capital was [[rajagriha]], and [[pataliputra]] came later.|[[magadha|মগধ]] আজিৰ বিহাৰত আছিল। ইয়াৰ প্ৰথম ৰাজধানী [[rajagriha|ৰাজগৃহ]], পিছত [[pataliputra|পাটলিপুত্ৰ]]।", art="houses"),
 S("Three dynasties|তিনিটা বংশ", "The <mark>Haryankas</mark> came first: [[bimbisara|Bimbisara]] annexed Anga, and [[ajatashatru|Ajatashatru]] fought Kosala.|প্ৰথমে <mark>হৰ্যংক</mark>: [[bimbisara|বিম্বিসাৰে]] অংগ দখল কৰিছিল, [[ajatashatru|অজাতশত্ৰুৱে]] কোশলৰ সৈতে যুঁজিছিল।", "The <mark>Shishunagas</mark> followed, then the <mark>Nandas</mark>. Chandragupta Maurya overthrew the Nandas.|তাৰ পিছত <mark>শিশুনাগ</mark>, তাৰ পিছত <mark>নন্দ</mark>। চন্দ্ৰগুপ্ত মৌৰ্যই নন্দ বংশক উৎখাত কৰিছিল।", art="court"),
 OR("Put the dynasties of Magadha in order.|মগধৰ বংশবোৰ ক্ৰমে সজোৱা।", ["Haryanka|হৰ্যংক", "Shishunaga|শিশুনাগ", "Nanda|নন্দ", "Maurya|মৌৰ্য"], "Haryanka, Shishunaga, Nanda, Maurya.|হৰ্যংক, শিশুনাগ, নন্দ, মৌৰ্য।"),
 MA([("Bimbisara|বিম্বিসাৰ", "Annexed Anga|অংগ দখল"), ("Ajatashatru|অজাতশত্ৰু", "Fought Kosala|কোশলৰ সৈতে যুঁজ"), ("Chandragupta Maurya|চন্দ্ৰগুপ্ত মৌৰ্য", "Overthrew the Nandas|নন্দ উৎখাত")], "King and deed.|ৰজা আৰু কাম।"),
 TF("Magadha's first capital was Pataliputra.|মগধৰ প্ৰথম ৰাজধানী পাটলিপুত্ৰ।", False, "Rajagriha came first.|ৰাজগৃহ প্ৰথম।"),
 MP("Tap Magadha's later capital.|মগধৰ পিছৰ ৰাজধানী টিপা।", "pataliputra", ["pataliputra", "jhelum", "beas", "delhi"], "Pataliputra, near Patna.|পাটনাৰ ওচৰৰ পাটলিপুত্ৰ।"),
 IN("Bimbisara belonged to the|বিম্বিসাৰ আছিল", " dynasty.|বংশৰ।", ["Nanda|নন্দ", "Haryanka|হৰ্যংক", "Maurya|মৌৰ্য", "Shunga|শুংগ"], 1, "He was a Haryanka king.|তেওঁ হৰ্যংক ৰজা।"),
)
u3 = U(3, "flag", "Alexander at the Jhelum|জিলমত আলেকজেণ্ডাৰ",
 "Fix the facts of the 326 BCE invasion.|খ্ৰীষ্টপূৰ্ব ৩২৬ৰ আক্ৰমণৰ তথ্য মনত ৰাখা।", "Finding recorded: Alexander beat Porus on the Jhelum in 326 BCE.|প্ৰমাণ লিখা হ'ল: খ্ৰীষ্টপূৰ্ব ৩২৬ত জিলমত আলেকজেণ্ডাৰে পুৰুক হৰুৱাইছিল।",
 ["Alexander came from Macedonia|আলেকজেণ্ডাৰ মেচিডনৰ", "He invaded the north-west in 326 BCE|খ্ৰীষ্টপূৰ্ব ৩২৬ত উত্তৰ-পশ্চিম আক্ৰমণ কৰিছিল", "He fought Porus on the Jhelum, the Hydaspes|তেওঁ জিলম বা হাইডাস্পিছত পুৰুৰ সৈতে যুঁজিছিল", "Porus kept his rule under Alexander|পুৰুৱে আলেকজেণ্ডাৰৰ অধীনত শাসন ৰাখিছিল"],
 S("A king from Macedonia|মেচিডনৰ ৰজা", "[[alexander|Alexander]] came from the kingdom of <mark>Macedonia</mark>, not Persia. He reached India's north-west in <mark>326 BCE</mark>.|[[alexander|আলেকজেণ্ডাৰ]] পাৰস্যৰ নহয়, <mark>মেচিডন</mark> ৰাজ্যৰ। তেওঁ <mark>খ্ৰীষ্টপূৰ্ব ৩২৬ত</mark> ভাৰতৰ উত্তৰ-পশ্চিম পালে।", art="embassy"),
 S("Battle on the Hydaspes|হাইডাস্পিছৰ যুদ্ধ", "In May 326 BCE he met [[porus|Porus]] on the <mark>[[jhelum|Jhelum]]</mark>, which Greek writers called the Hydaspes. Porus lost but kept his kingdom under Alexander.|খ্ৰীষ্টপূৰ্ব ৩২৬ৰ মে'ত তেওঁ <mark>[[jhelum|জিলমত]]</mark> [[porus|পুৰুৰ]] সৈতে যুঁজিল, গ্ৰীক লেখকে ইয়াক হাইডাস্পিছ বোলে। পুৰু হাৰিল, কিন্তু আলেকজেণ্ডাৰৰ অধীনত ৰাজ্য ৰাখিলে।", "His advance stopped at the [[beas|Beas]].|তেওঁৰ অগ্ৰগতি [[beas|বিপাশাত]] ৰৈ গ'ল।", map={"base": "india", "box": [66, 26, 82, 36], "show": ["jhelum", "beas", "taxila"]}),
 IN("Alexander invaded India in|আলেকজেণ্ডাৰে ভাৰত আক্ৰমণ কৰিছিল", ".|ত।", ["316 BCE|খ্ৰীষ্টপূৰ্ব ৩১৬", "326 BCE|খ্ৰীষ্টপূৰ্ব ৩২৬", "346 BCE|খ্ৰীষ্টপূৰ্ব ৩৪৬", "356 BCE|খ্ৰীষ্টপূৰ্ব ৩৫৬"], 1, "326 BCE.|খ্ৰীষ্টপূৰ্ব ৩২৬।"),
 SP("Alexander came from the kingdom of *Persia.*|আলেকজেণ্ডাৰ *পাৰস্য* ৰাজ্যৰ।", "Macedonia|মেচিডন", "He was king of Macedonia.|তেওঁ মেচিডনৰ ৰজা।"),
 MP("Tap the river of the battle with Porus.|পুৰুৰ সৈতে যুদ্ধৰ নদীখন টিপা।", "jhelum", ["jhelum", "delhi", "pataliputra", "beas"], "The Jhelum.|জিলম।"),
 TF("Alexander spared Porus and left him as ruler.|আলেকজেণ্ডাৰে পুৰুক এৰি শাসক হিচাপে ৰাখিছিল।", True, "Porus stayed on as his ruler in the region.|পুৰু তেওঁৰ অধীনত অঞ্চলৰ শাসক হৈ থাকিল।"),
 MA([("Hydaspes|হাইডাস্পিছ", "Jhelum|জিলম"), ("Hyphasis|হাইফেছিছ", "Beas|বিপাশা")], "Greek names and modern rivers.|গ্ৰীক নাম আৰু আধুনিক নদী।"),
 WH(["I fought on the Jhelum.|মই জিলমত যুঁজিছিলোঁ।", "I lost to Alexander.|মই আলেকজেণ্ডাৰৰ ওচৰত হাৰিছিলোঁ।", "I kept my kingdom.|মই ৰাজ্য ৰাখিছিলোঁ।"], ["Porus|পুৰু", "Bimbisara|বিম্বিসাৰ", "Seleucus I|চেলুকাছ প্ৰথম", "Ambhi|অম্ভি"], 0, "Porus.|পুৰু।"),
)
test = TEST("Trace the road from sixteen states to one empire.|ষোল্ল ৰাজ্যৰ পৰা এটা সাম্ৰাজ্যলৈ বাট অনুসৰণ কৰা।", "Recorded: Mahajanapadas, Magadha and Alexander.|লিখা হ'ল: মহাজনপদ, মগধ আৰু আলেকজেণ্ডাৰ।",
 IN("Alexander was from the ancient kingdom of|আলেকজেণ্ডাৰ আছিল প্ৰাচীন", ".|ৰ।", ["Persia|পাৰস্য", "Byzantium|বাইজান্টিয়াম", "Macedonia|মেচিডন", "the Ottomans|অটোমান"], 2, "Macedonia.|মেচিডন।"),
 MP("Tap the river where Alexander fought Porus.|আলেকজেণ্ডাৰে পুৰুৰ সৈতে যুঁজা নদীখন টিপা।", "jhelum", ["jhelum", "beas", "delhi", "pataliputra"], "The Jhelum.|জিলম।"),
 OR("Order these.|এইবোৰ ক্ৰমে সজোৱা।", ["Bimbisara annexes Anga|বিম্বিসাৰে অংগ দখল কৰে", "Nandas take power|নন্দ ক্ষমতাত", "Alexander at the Jhelum|জিলমত আলেকজেণ্ডাৰ", "Chandragupta takes Pataliputra|চন্দ্ৰগুপ্তই পাটলিপুত্ৰ লয়"], "Magadha's rise, then Alexander, then the Mauryas.|মগধৰ উত্থান, আলেকজেণ্ডাৰ, তাৰ পিছত মৌৰ্য।"),
 TF("There were sixteen Mahajanapadas in the standard list.|মানক তালিকাত ষোল্লটা মহাজনপদ আছিল।", True, "Yes, in the Anguttara Nikaya.|হয়, অংগুত্তৰ নিকায়ত।"),
 SP("Magadha lay in today's *Gujarat.*|মগধ আজিৰ *গুজৰাটত* আছিল।", "Bihar|বিহাৰত", "It lay in Bihar.|ই বিহাৰত আছিল।"),
 MC("Consider these statements. (1) Rajagriha was an early capital of Magadha. (2) The Nandas ruled before the Haryankas. (3) The Hydaspes is the Jhelum. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ৰাজগৃহ মগধৰ আদি ৰাজধানী। (২) হৰ্যংকৰ আগত নন্দ ৰজা আছিল। (৩) হাইডাস্পিছ হ'ল জিলম। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "The Nandas came after the Haryankas.|নন্দ হৰ্যংকৰ পিছৰ।"),
)
LESSON(4, "Magadha and Alexander|মগধ আৰু আলেকজেণ্ডাৰ", "to 326 BCE|খ্ৰীষ্টপূৰ্ব ৩২৬লৈ", "Empires of the north|উত্তৰৰ সাম্ৰাজ্য", "Evidence file 4|প্ৰমাণ নথি ৪", "From sixteen to one|ষোল্লৰ পৰা এক",
 "Sixteen states competed in the north while an invader reached the Punjab. Find out who was left standing.|উত্তৰত ষোল্লটা ৰাজ্যৰ প্ৰতিযোগিতা, পঞ্জাবত আক্ৰমণকাৰী। শেষত কোন থিয় হৈ থাকিল, উলিওৱা।",
 sources, [u1, u2, u3], test, ["jhelum", "beas", "pataliputra", "delhi"])
