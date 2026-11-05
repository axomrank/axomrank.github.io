#!/usr/bin/env python3
"""Lesson 3: Buddha and Mahavira."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403

PLACES({
 "buddha": ("person", "Gautama Buddha|গৌতম বুদ্ধ", "Founder of Buddhism, of the Shakya clan|বৌদ্ধ ধৰ্মৰ প্ৰৱৰ্তক, শাক্য বংশৰ"),
 "mahavira": ("person", "Mahavira|মহাবীৰ", "24th and last Tirthankara of Jainism|জৈন ধৰ্মৰ চতুৰ্বিংশ আৰু শেষ তীৰ্থংকৰ"),
 "tirthankara": ("term", "Tirthankara|তীৰ্থংকৰ", "A teacher of the Jain path|জৈন পথৰ শিক্ষক"),
 "pawapuri": ("place", "Pawapuri|পাৱাপুৰী", "Place in Bihar where Mahavira died|বিহাৰৰ ঠাই, য'ত মহাবীৰৰ মৃত্যু হৈছিল", [25.09, 85.54]),
})
sources = [
 src("Wikipedia, The Buddha", "https://en.wikipedia.org/wiki/The_Buddha", "Used as a guide: uncertain dates, four places, Lumbini pillar, Four Noble Truths, Middle Way. Check in review."),
 src("The Edicts of King Ashoka, English rendering by Ven. S. Dhammika", "https://www.accesstoinsight.org/lib/authors/dhammika/wheel386.html", "Used for the wider edict context; the Lumbini inscription is cited through the Wikipedia article."),
 src("Wikipedia, Mahavira", "https://en.wikipedia.org/wiki/Mahavira", "Used as a guide: 24th Tirthankara, Parshvanatha, Vaishali, Pawapuri, five vows, the two Jain traditions and their dates. Check in review."),
 src("APSC CCE Prelims 2025 GS-I, question 33, page read", "https://apsc.nic.in/cce.html", "Mahavira as the 24th Tirthankara; printed options read from the paper."),
]
BOX4 = {"base": "india", "box": [81, 24, 87.5, 28.2], "show": ["lumbini", "bodh-gaya", "sarnath", "kushinagar"]}
u1 = U(1, "walk", "Four places, one life|চাৰি ঠাই, এটা জীৱন",
 "Fix the four places of the Buddha's life.|বুদ্ধৰ জীৱনৰ চাৰিখন ঠাই মনত ৰাখা।",
 "Finding recorded: Lumbini, Bodh Gaya, Sarnath, Kushinagar.|প্ৰমাণ লিখা হ'ল: লুম্বিনী, বোধগয়া, সাৰনাথ, কুশীনগৰ।",
 ["Lumbini: birth|লুম্বিনী: জন্ম", "Bodh Gaya: enlightenment|বোধগয়া: জ্ঞানলাভ", "Sarnath: first sermon|সাৰনাথ: প্ৰথম উপদেশ", "Kushinagar: parinirvana|কুশীনগৰ: পৰিনিৰ্বাণ"],
 S("Born at Lumbini|লুম্বিনীত জন্ম",
   "Tradition places the birth of the [[buddha|Buddha]] at <mark>[[lumbini]]</mark>, in today's Nepal. He was of the Shakya clan.|পৰম্পৰা মতে [[buddha|বুদ্ধৰ]] জন্ম আজিৰ নেপালৰ <mark>[[lumbini|লুম্বিনীত]]</mark>। তেওঁ শাক্য বংশৰ।",
   "An Ashokan pillar there marks the site, about two centuries later. His own dates are uncertain.|তাত থকা অশোকৰ স্তম্ভে প্ৰায় দুশ বছৰ পিছত ঠাইখন চিনাক্ত কৰে। তেওঁৰ নিজৰ তাৰিখ অনিশ্চিত।", map=BOX4),
 S("Awakening and first sermon|জ্ঞানলাভ আৰু প্ৰথম উপদেশ",
   "He reached awakening at <mark>[[bodh-gaya|Bodh Gaya]]</mark> and gave his first sermon at <mark>[[sarnath]]</mark>, the Dharmachakrapravartana.|তেওঁ <mark>[[bodh-gaya|বোধগয়াত]]</mark> জ্ঞান লাভ কৰিছিল আৰু <mark>[[sarnath|সাৰনাথত]]</mark> প্ৰথম উপদেশ দিছিল, ধৰ্মচক্ৰপ্ৰৱৰ্তন।",
   "He died at <mark>[[kushinagar]]</mark>. Buddhists call this his parinirvana.|<mark>[[kushinagar|কুশীনগৰত]]</mark> তেওঁৰ মৃত্যু হয়। বৌদ্ধসকলে ইয়াক পৰিনিৰ্বাণ বোলে।", map=BOX4),
 MA([("Lumbini|লুম্বিনী", "Birth|জন্ম"), ("Bodh Gaya|বোধগয়া", "Enlightenment|জ্ঞানলাভ"), ("Sarnath|সাৰনাথ", "First sermon|প্ৰথম উপদেশ"), ("Kushinagar|কুশীনগৰ", "Parinirvana|পৰিনিৰ্বাণ")], "APSC swaps these pairs to test you.|APSCয়ে এই মিলবোৰ সলাই পৰীক্ষা কৰে।"),
 MP("Tap Kushinagar.|কুশীনগৰ টিপা।", "kushinagar", ["kushinagar", "bodh-gaya", "lumbini", "sarnath"], "Kushinagar is in Uttar Pradesh.|কুশীনগৰ উত্তৰ প্ৰদেশত।"),
 SP("The Buddha gained enlightenment at *Kushinagar.*|বুদ্ধই *কুশীনগৰত* জ্ঞান লাভ কৰিছিল।", "Bodh Gaya|বোধগয়াত", "Kushinagar is the place of his parinirvana.|কুশীনগৰ তেওঁৰ পৰিনিৰ্বাণৰ স্থান।"),
 OR("Put his life in order.|তেওঁৰ জীৱন ক্ৰমে সজোৱা।", ["Lumbini|লুম্বিনী", "Bodh Gaya|বোধগয়া", "Sarnath|সাৰনাথ", "Kushinagar|কুশীনগৰ"], "Birth, awakening, first sermon, parinirvana.|জন্ম, জ্ঞানলাভ, প্ৰথম উপদেশ, পৰিনিৰ্বাণ।"),
 TF("Lumbini is in today's Nepal.|লুম্বিনী আজিৰ নেপালত।", True, "It lies just across the Indian border.|ই ভাৰতীয় সীমাৰ সিপাৰে।"),
)
u2 = U(2, "star", "The Middle Way|মধ্যপথ",
 "State what the Buddha taught.|বুদ্ধই কি শিকাইছিল, কোৱা।",
 "Finding recorded: Four Noble Truths, Eightfold Path, Middle Way, Sangha.|প্ৰমাণ লিখা হ'ল: চাৰি আৰ্য সত্য, অষ্টাংগিক মাৰ্গ, মধ্যপথ, সংঘ।",
 ["The Four Noble Truths sum up his teaching|চাৰি আৰ্য সত্যত তেওঁৰ শিক্ষাৰ সাৰ", "The Noble Eightfold Path is the way of practice|অষ্টাংগিক মাৰ্গ অভ্যাসৰ পথ", "The Middle Way avoids indulgence and severe austerity|মধ্যপথে ভোগ আৰু কঠোৰ তপস্যা দুয়োটা এৰায়", "He founded the monastic Sangha|তেওঁ ভিক্ষুৰ সংঘ গঢ়িছিল"],
 S("Between two extremes|দুই চৰমৰ মাজত",
   "After years of severe austerity he taught a <mark>Middle Way</mark> between indulgence and self-punishment.|বছৰ বছৰ কঠোৰ তপস্যাৰ পিছত তেওঁ ভোগ আৰু আত্মপীড়নৰ মাজৰ <mark>মধ্যপথ</mark> শিকালে।", art="door"),
 S("Truths, Path and Sangha|সত্য, মাৰ্গ আৰু সংঘ",
   "His teaching is summed up in the <mark>Four Noble Truths</mark> and the <mark>Noble Eightfold Path</mark>.|তেওঁৰ শিক্ষাৰ সাৰ <mark>চাৰি আৰ্য সত্য</mark> আৰু <mark>অষ্টাংগিক মাৰ্গ</mark>।",
   "He built a monastic order, the Sangha, and taught across the Ganga plain.|তেওঁ ভিক্ষুৰ সংঘ গঢ়িছিল আৰু গংগা সমভূমিত শিক্ষা দিছিল।", art="houses"),
 IN("The Noble Path of the Buddha has|বুদ্ধৰ আৰ্য মাৰ্গৰ", " parts.|টা অংগ আছে।", ["four|চাৰি", "five|পাঁচ", "eight|আঠ", "twelve|বাৰ"], 2, "It is the Eightfold Path.|ই অষ্টাংগিক মাৰ্গ।"),
 TF("The Buddha taught that severe self-punishment is the only way.|বুদ্ধই কঠোৰ আত্মপীড়নেই একমাত্ৰ পথ বুলি শিকাইছিল।", False, "He taught a Middle Way.|তেওঁ মধ্যপথ শিকাইছিল।"),
 SC("Unscramble the Buddhist monastic order.|বৌদ্ধ ভিক্ষুৰ সংঘটো সজোৱা।", "SANGHA", ["সং", "ঘ"], "The Sangha is the order of monks.|সংঘ ভিক্ষুৰ সমাজ।"),
 WH(["I come in fours.|মই চাৰিটা।", "I sum up the Buddha's teaching.|মই বুদ্ধৰ শিক্ষাৰ সাৰ।"], ["Four Vedas|চাৰি বেদ", "Four Noble Truths|চাৰি আৰ্য সত্য", "Four varnas|চাৰি বৰ্ণ", "Four Tirthankaras|চাৰি তীৰ্থংকৰ"], 1, "The Four Noble Truths.|চাৰি আৰ্য সত্য।"),
 OD("Which term does NOT belong to Buddhism?|কোনটো শব্দ বৌদ্ধ ধৰ্মৰ নহয়?", ["Sangha|সংঘ", "Middle Way|মধ্যপথ", "Parinirvana|পৰিনিৰ্বাণ", "Tirthankara|তীৰ্থংকৰ"], 3, "Tirthankara is a Jain term.|তীৰ্থংকৰ জৈন শব্দ।"),
)
u3 = U(3, "star", "The 24th Tirthankara|চতুৰ্বিংশ তীৰ্থংকৰ",
 "Fix Mahavira's place in the Jain line.|জৈন পৰম্পৰাত মহাবীৰৰ স্থান মনত ৰাখা।",
 "Finding recorded: Mahavira was the 24th Tirthankara, after Parshvanatha.|প্ৰমাণ লিখা হ'ল: মহাবীৰ পাৰ্শ্বনাথৰ পিছৰ চতুৰ্বিংশ তীৰ্থংকৰ।",
 ["Tirthankara is a Jain term|তীৰ্থংকৰ জৈন শব্দ", "Mahavira was the 24th and last|মহাবীৰ চতুৰ্বিংশ আৰু শেষ", "Parshvanatha was the 23rd|পাৰ্শ্বনাথ ত্ৰয়োবিংশ", "He died at Pawapuri in Bihar|বিহাৰৰ পাৱাপুৰীত তেওঁৰ মৃত্যু হয়"],
 S("The ford-makers|তীৰ্থ গঢ়া জন",
   "Jains revere a line of <mark>[[tirthankara|Tirthankaras]]</mark>, teachers of the path. [[mahavira|Mahavira]], born Vardhamana, is the <mark>24th and last</mark>.|জৈনসকলে পথৰ শিক্ষক <mark>[[tirthankara|তীৰ্থংকৰসকলক]]</mark> শ্ৰদ্ধা কৰে। বৰ্ধমান নামে জন্মা [[mahavira|মহাবীৰ]] <mark>চতুৰ্বিংশ আৰু শেষ</mark>।",
   "Parshvanatha came before him as the 23rd.|তেওঁৰ আগতে পাৰ্শ্বনাথ ত্ৰয়োবিংশ।", art="seal"),
 S("A life in Bihar|বিহাৰত এটা জীৱন",
   "Tradition places his birth near Vaishali in Bihar. He left home at about 30, and died at [[pawapuri]].|পৰম্পৰা মতে তেওঁৰ জন্ম বিহাৰৰ বৈশালীৰ ওচৰত। প্ৰায় ৩০ বছৰত ঘৰ এৰে, [[pawapuri|পাৱাপুৰীত]] মৃত্যু হয়।",
   "Traditions disagree on his dates: Shvetambaras give 527 BCE for his death and Digambaras 510 BCE.|তেওঁৰ তাৰিখত মতভেদ আছে: শ্বেতাম্বৰ মতে মৃত্যু খ্ৰীষ্টপূৰ্ব ৫২৭, দিগম্বৰ মতে ৫১০।", art="calendar"),
 IN("Mahavira was the|মহাবীৰ আছিল", " Tirthankara.|তম তীৰ্থংকৰ।", ["21st|২১", "22nd|২২", "23rd|২৩", "24th|২৪"], 3, "He was the 24th and last.|তেওঁ চতুৰ্বিংশ আৰু শেষ।"),
 WH(["The term Tirthankara is linked to me.|তীৰ্থংকৰ শব্দ মোৰ সৈতে জড়িত।", "I was shaped by Mahavira and Parshvanatha.|মহাবীৰ আৰু পাৰ্শ্বনাথে মোক গঢ়িছিল।", "I have Shvetambara and Digambara traditions.|মোৰ শ্বেতাম্বৰ আৰু দিগম্বৰ পৰম্পৰা আছে।"], ["Buddhism|বৌদ্ধ ধৰ্ম", "Jainism|জৈন ধৰ্ম", "Sikhism|শিখ ধৰ্ম", "Hinduism|হিন্দু ধৰ্ম"], 1, "Jainism.|জৈন ধৰ্ম।"),
 TF("Parshvanatha came before Mahavira.|পাৰ্শ্বনাথ মহাবীৰৰ আগত।", True, "He was the 23rd Tirthankara.|তেওঁ ত্ৰয়োবিংশ তীৰ্থংকৰ।"),
 SP("Mahavira's birth name was *Siddhartha.*|মহাবীৰৰ জন্মনাম *সিদ্ধাৰ্থ।*", "Vardhamana|বৰ্ধমান", "Siddhartha is the Buddha's name.|সিদ্ধাৰ্থ বুদ্ধৰ নাম।"),
 MA([("Birth region|জন্মস্থান অঞ্চল", "Near Vaishali|বৈশালীৰ ওচৰত"), ("Death|মৃত্যু", "Pawapuri|পাৱাপুৰী"), ("Birth name|জন্মনাম", "Vardhamana|বৰ্ধমান")], "Three facts of one life.|এটা জীৱনৰ তিনিটা তথ্য।"),
)
u4 = U(4, "hands", "Two paths compared|দুটা পথৰ তুলনা",
 "Keep Jain and Buddhist teaching apart.|জৈন আৰু বৌদ্ধ শিক্ষা পৃথক ৰাখা।",
 "Finding recorded: five vows for Jains, the Eightfold Path for Buddhists.|প্ৰমাণ লিখা হ'ল: জৈনৰ পঞ্চ ব্ৰত, বৌদ্ধৰ অষ্টাংগিক মাৰ্গ।",
 ["Jainism teaches five vows|জৈন ধৰ্মত পঞ্চ ব্ৰত", "Ahimsa is the first of them|অহিংসা ইয়াৰ প্ৰথম", "Svetambara and Digambara are the two Jain traditions|শ্বেতাম্বৰ আৰু দিগম্বৰ দুটা জৈন পৰম্পৰা", "Both teachers worked in the Ganga plain|দুয়ো শিক্ষকে গংগা সমভূমিত কাম কৰিছিল"],
 S("Five vows|পঞ্চ ব্ৰত",
   "Mahavira's <mark>five vows</mark> are non-violence, truthfulness, non-stealing, chastity and non-attachment.|মহাবীৰৰ <mark>পঞ্চ ব্ৰত</mark>: অহিংসা, সত্য, অস্তেয়, ব্ৰহ্মচৰ্য আৰু অপৰিগ্ৰহ।", art="seal"),
 S("Same region, different answers|একে অঞ্চল, বেলেগ উত্তৰ",
   "The Buddha and Mahavira both taught in the eastern Ganga plain, and both questioned Vedic ritual as the path to release.|বুদ্ধ আৰু মহাবীৰে দুয়ো পূব গংগা সমভূমিত শিক্ষা দিছিল, দুয়ো মুক্তিৰ পথ হিচাপে বৈদিক যজ্ঞক প্ৰশ্ন কৰিছিল।",
   "Later Jains divided into <mark>Svetambara</mark> and <mark>Digambara</mark> traditions.|পিছত জৈনসকল <mark>শ্বেতাম্বৰ</mark> আৰু <mark>দিগম্বৰ</mark> পৰম্পৰাত বিভক্ত হয়।", art="houses"),
 MA([("Eightfold Path|অষ্টাংগিক মাৰ্গ", "Buddhism|বৌদ্ধ ধৰ্ম"), ("Five vows|পঞ্চ ব্ৰত", "Jainism|জৈন ধৰ্ম"), ("Sangha|সংঘ", "Buddhism|বৌদ্ধ ধৰ্ম"), ("Tirthankara|তীৰ্থংকৰ", "Jainism|জৈন ধৰ্ম")], "Exams test this confusion.|পৰীক্ষাত এই বিভ্ৰান্তি সোধা হয়।"),
 OD("Which is NOT one of Mahavira's five vows?|কোনটো মহাবীৰৰ পঞ্চ ব্ৰতৰ এটা নহয়?", ["Non-violence|অহিংসা", "Truthfulness|সত্য", "Non-stealing|অস্তেয়", "Pilgrimage|তীৰ্থযাত্ৰা"], 3, "The vows are about conduct.|ব্ৰতবোৰ আচৰণৰ বিষয়ে।"),
 TF("Svetambara and Digambara are Buddhist schools.|শ্বেতাম্বৰ আৰু দিগম্বৰ বৌদ্ধ সম্প্ৰদায়।", False, "They are Jain traditions.|এইবোৰ জৈন পৰম্পৰা।"),
 IN("The first Jain vow is|প্ৰথম জৈন ব্ৰত", ".|।", ["ahimsa|অহিংসা", "dhamma|ধম্ম", "sangha|সংঘ", "moksha|মোক্ষ"], 0, "Ahimsa means non-violence.|অহিংসা মানে হিংসা নকৰা।"),
 WH(["I taught the Eightfold Path.|মই অষ্টাংগিক মাৰ্গ শিকাইছিলোঁ।", "I gave my first sermon at Sarnath.|মই সাৰনাথত প্ৰথম উপদেশ দিছিলোঁ।"], ["Mahavira|মহাবীৰ", "Parshvanatha|পাৰ্শ্বনাথ", "Gautama Buddha|গৌতম বুদ্ধ", "Ashoka|অশোক"], 2, "The Buddha.|বুদ্ধ।"),
)
test = TEST("Keep two great teachers apart.|দুজন মহান শিক্ষকক পৃথক ৰাখা।", "Recorded: places, teachings and the Jain line.|লিখা হ'ল: স্থান, শিক্ষা আৰু জৈন পৰম্পৰা।",
 MC("Consider these pairs. (1) Lumbini: birth. (2) Sarnath: first sermon. (3) Kushinagar: enlightenment. Which are correctly matched?|এই মিলবোৰ বিবেচনা কৰা। (১) লুম্বিনী: জন্ম। (২) সাৰনাথ: প্ৰথম উপদেশ। (৩) কুশীনগৰ: জ্ঞানলাভ। কোনবোৰ শুদ্ধ?", ["1 only|কেৱল ১", "1 and 2 only|কেৱল ১ আৰু ২", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Enlightenment was at Bodh Gaya.|জ্ঞানলাভ বোধগয়াত।"),
 MP("Tap Bodh Gaya.|বোধগয়া টিপা।", "bodh-gaya", ["bodh-gaya", "kushinagar", "lumbini", "sarnath"], "Bodh Gaya is in Bihar.|বোধগয়া বিহাৰত।"),
 IN("The term Tirthankara is associated with|তীৰ্থংকৰ শব্দ জড়িত", ".|ৰ সৈতে।", ["Buddhism|বৌদ্ধ ধৰ্ম", "Jainism|জৈন ধৰ্ম", "Sikhism|শিখ ধৰ্ম", "Hinduism|হিন্দু ধৰ্ম"], 1, "Jainism.|জৈন ধৰ্ম।"),
 TF("Buddhists believe Gautama Buddha attained parinirvana at Kushinagar.|বৌদ্ধসকলৰ মতে গৌতম বুদ্ধই কুশীনগৰত পৰিনিৰ্বাণ লাভ কৰিছিল।", True, "Yes, at Kushinagar.|হয়, কুশীনগৰত।"),
 SP("Mahavira was the *23rd* Tirthankara.|মহাবীৰ *২৩তম* তীৰ্থংকৰ।", "24th|২৪তম", "Parshvanatha was the 23rd.|পাৰ্শ্বনাথ ২৩তম।"),
 MA([("Middle Way|মধ্যপথ", "Buddha|বুদ্ধ"), ("Five vows|পঞ্চ ব্ৰত", "Mahavira|মহাবীৰ")], "Teaching and teacher.|শিক্ষা আৰু শিক্ষক।"),
)
LESSON(3, "Buddha and Mahavira|বুদ্ধ আৰু মহাবীৰ", "6th–5th c. BCE|খ্ৰীষ্টপূৰ্ব ষষ্ঠ–পঞ্চম শতিকা", "Beginnings|আৰম্ভণি", "Evidence file 3|প্ৰমাণ নথি ৩", "Two teachers, one plain|দুজন শিক্ষক, এখন সমভূমি",
 "Papers love to swap the places of the Buddha's life and the terms of Jainism. Learn which belongs where.|পৰীক্ষাত বুদ্ধৰ জীৱনৰ ঠাই আৰু জৈন শব্দ সলাই সোধা হয়। কোনটো ক'ত, শিকা।",
 sources, [u1, u2, u3, u4], test, ["lumbini", "bodh-gaya", "sarnath", "kushinagar", "pawapuri"], box=[81.5, 24, 86.5, 28])
