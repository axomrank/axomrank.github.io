#!/usr/bin/env python3
"""Lesson 1: The Indus cities."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403

PLACES({
 "kalibangan": ("place", "Kalibangan|কালিবংগান", "Harappan site in Rajasthan with a ploughed field|ৰাজস্থানৰ হৰপ্পীয় স্থল, ইয়াত হাল বোৱা পথাৰ পোৱা গৈছে", [29.47, 74.13]),
 "dholavira": ("place", "Dholavira|ধোলাভিৰা", "Harappan city in Kutch, Gujarat, known for water reservoirs|গুজৰাটৰ কচ্ছৰ হৰপ্পীয় নগৰ, পানীৰ জলাশয়ৰ বাবে খ্যাত", [23.89, 70.21]),
 "daya-ram-sahni": ("person", "Daya Ram Sahni|দয়াৰাম চাহনি", "Archaeologist who excavated Harappa in 1921|১৯২১ত হৰপ্পা খনন কৰা পুৰাতত্ত্ববিদ"),
 "rd-banerji": ("person", "R. D. Banerji|ৰাখালদাস বন্দ্যোপাধ্যায়", "Archaeologist linked with Mohenjo-daro in 1922|১৯২২ত মহেঞ্জোদাৰোৰ সৈতে জড়িত পুৰাতত্ত্ববিদ"),
})
sources = [
 src("Wikipedia, Indus Valley Civilisation", "https://en.wikipedia.org/wiki/Indus_Valley_Civilisation", "Used as a guide: mature phase, sites, Great Bath, drains, seals, undeciphered script, decline. Check in review."),
 src("John Marshall, ed., Mohenjo-daro and the Indus Civilization, 1931", "https://archive.org/details/mohenjodaroandtheinduscivilizationvol1jmarshalled1931_84_N", "Located, not read. The excavation dates and site findings need checking against it and later reports in review."),
]
BOX = [64, 20, 80, 33]
u1 = U(1, "home", "Cities found by accident of time|সময়ে লুকুৱাই ৰখা নগৰ",
 "Place the Indus cities in time and space.|সিন্ধু নগৰবোৰ সময় আৰু ঠাইত স্থাপন কৰা।",
 "Finding recorded: the mature phase ran from about 2600 to 1900 BCE.|প্ৰমাণ লিখা হ'ল: পূৰ্ণ পৰ্যায় প্ৰায় খ্ৰীষ্টপূৰ্ব ২৬০০ৰ পৰা ১৯০০লৈ।",
 ["The mature Harappan phase ran about 2600 to 1900 BCE|পূৰ্ণ হৰপ্পীয় পৰ্যায় প্ৰায় খ্ৰীষ্টপূৰ্ব ২৬০০–১৯০০", "Harappa was excavated first, in 1921|প্ৰথমে ১৯২১ত হৰপ্পা খনন কৰা হৈছিল", "Mohenjo-daro followed in 1922|১৯২২ত মহেঞ্জোদাৰো আহিল", "Both great cities are in today's Pakistan|দুয়োখন ডাঙৰ নগৰ আজিৰ পাকিস্তানত"],
 S("Two cities, one surprise|দুখন নগৰ, এটা বিস্ময়",
   "[[daya-ram-sahni|Daya Ram Sahni]] dug at [[harappa]] in <mark>1921</mark>. [[rd-banerji|R. D. Banerji]] followed at [[mohenjo-daro]] in 1922.|১৯২১ত [[daya-ram-sahni|দয়াৰাম চাহনিয়ে]] [[harappa|হৰপ্পাত]] খনন কৰিছিল। ১৯২২ত [[rd-banerji|ৰাখালদাস বন্দ্যোপাধ্যায়ে]] [[mohenjo-daro|মহেঞ্জোদাৰোত]] কাম কৰিছিল।",
   "The finds showed planned cities far older than anyone had expected.|আৱিষ্কাৰে দেখুৱালে যে পৰিকল্পিত নগৰবোৰ কোনেও ভবাতকৈ বহু পুৰণি।", map={"base": "india", "box": [62, 22, 81, 33], "show": ["harappa", "mohenjo-daro"]}),
 S("How old?|কিমান পুৰণি?",
   "The mature Harappan phase ran from about <mark>2600 to 1900 BCE</mark>. The wider civilisation is dated from about 3300 to 1300 BCE.|পূৰ্ণ হৰপ্পীয় পৰ্যায় প্ৰায় <mark>খ্ৰীষ্টপূৰ্ব ২৬০০ৰ পৰা ১৯০০লৈ</mark>। বিস্তৃত সভ্যতাটো প্ৰায় খ্ৰীষ্টপূৰ্ব ৩৩০০ৰ পৰা ১৩০০লৈ ধৰা হয়।",
   "Harappa and Mohenjo-daro lie in today's Pakistan, but many sites lie in India.|হৰপ্পা আৰু মহেঞ্জোদাৰো আজিৰ পাকিস্তানত, কিন্তু বহু স্থল ভাৰতত আছে।", art="calendar"),
 MP("Tap Mohenjo-daro.|মহেঞ্জোদাৰো টিপা।", "mohenjo-daro", ["mohenjo-daro", "harappa", "lothal", "kalibangan"], "Mohenjo-daro is in Sindh, Pakistan.|মহেঞ্জোদাৰো পাকিস্তানৰ সিন্ধত।"),
 OD("Which was NOT part of the Indus Valley Civilisation?|কোনখন সিন্ধু সভ্যতাৰ অংশ নাছিল?", ["Mohenjo-daro|মহেঞ্জোদাৰো", "Harappa|হৰপ্পা", "Lothal|লোথাল", "Machilipatnam|মছলিপট্টনম"], 3, "Machilipatnam is a later port on the Andhra coast.|মছলিপট্টনম অন্ধ্ৰ উপকূলৰ পিছৰ বন্দৰ।"),
 MA([("Harappa, 1921|হৰপ্পা, ১৯২১", "Daya Ram Sahni|দয়াৰাম চাহনি"), ("Mohenjo-daro, 1922|মহেঞ্জোদাৰো, ১৯২২", "R. D. Banerji|ৰাখালদাস বন্দ্যোপাধ্যায়")], "Keep site, year and name together.|স্থল, বছৰ আৰু নাম একেলগে মনত ৰাখা।"),
 TF("Harappa is in today's Pakistan.|হৰপ্পা আজিৰ পাকিস্তানত।", True, "It is in Punjab, Pakistan.|ই পাকিস্তানৰ পঞ্জাবত।"),
 SC("Unscramble the site dug in 1921.|১৯২১ত খনন কৰা স্থলটো সজোৱা।", "HARAPPA", ["হ", "ৰ", "প্পা"], "Harappa gave the culture its name.|হৰপ্পাৰ নামেৰে এই সংস্কৃতিৰ নাম।"),
)
u2 = U(2, "houses", "A city built on a plan|পৰিকল্পনাৰে গঢ়া নগৰ",
 "See what the planners built.|পৰিকল্পনাকাৰীসকলে কি গঢ়িছিল, চোৱা।",
 "Finding recorded: covered drains and the Great Bath mark Harappan planning.|প্ৰমাণ লিখা হ'ল: ঢকা নলা আৰু বৃহৎ স্নানাগাৰ হৰপ্পীয় পৰিকল্পনাৰ চিন।",
 ["Streets had covered drains|ৰাস্তাত ঢকা নলা আছিল", "The Great Bath is at Mohenjo-daro|বৃহৎ স্নানাগাৰ মহেঞ্জোদাৰোত", "Houses had water and drainage|ঘৰত পানী আৰু নলাৰ ব্যৱস্থা আছিল", "Dholavira is known for water reservoirs|ধোলাভিৰা পানীৰ জলাশয়ৰ বাবে খ্যাত"],
 S("Drains under the street|ৰাস্তাৰ তলৰ নলা",
   "Harappan cities had <mark>covered drains</mark> along main streets, and houses had water and drainage.|হৰপ্পীয় নগৰৰ মূল ৰাস্তাত <mark>ঢকা নলা</mark> আছিল, ঘৰত পানী আৰু নলাৰ ব্যৱস্থা আছিল।",
   "This is the feature exam papers love: planning, not palaces.|পৰীক্ষাত এই বৈশিষ্ট্য প্ৰায়ে আহে: ৰাজপ্ৰাসাদ নহয়, পৰিকল্পনা।", art="houses"),
 S("The Great Bath|বৃহৎ স্নানাগাৰ",
   "At [[mohenjo-daro]] stands the <mark>Great Bath</mark>, a large brick tank. Its exact use is not known.|[[mohenjo-daro|মহেঞ্জোদাৰোত]] <mark>বৃহৎ স্নানাগাৰ</mark> আছে, ইটাৰ ডাঙৰ চৌবাচ্চা। ইয়াৰ সঠিক ব্যৱহাৰ জনা নাযায়।",
   "At [[dholavira]] in Kutch, builders stored water in reservoirs.|কচ্ছৰ [[dholavira|ধোলাভিৰাত]] নিৰ্মাতাসকলে জলাশয়ত পানী জমা কৰিছিল।", art="door"),
 TF("The Great Bath is at Harappa.|বৃহৎ স্নানাগাৰ হৰপ্পাত।", False, "It is at Mohenjo-daro.|ই মহেঞ্জোদাৰোত।"),
 IN("Harappan streets are known for covered|হৰপ্পীয় ৰাস্তাবোৰ ঢকা", ".|ৰ বাবে খ্যাত।", ["temples|মন্দিৰ", "drains|নলা", "markets|বজাৰ", "gates|দুৱাৰ"], 1, "Covered drains are a mark of their planning.|ঢকা নলা তেওঁলোকৰ পৰিকল্পনাৰ চিন।"),
 MA([("Mohenjo-daro|মহেঞ্জোদাৰো", "Great Bath|বৃহৎ স্নানাগাৰ"), ("Dholavira|ধোলাভিৰা", "Water reservoirs|পানীৰ জলাশয়"), ("Lothal|লোথাল", "Dock|ডক"), ("Kalibangan|কালিবংগান", "Ploughed field|হাল বোৱা পথাৰ")], "One site, one famous find.|এটা স্থল, এটা খ্যাত আৱিষ্কাৰ।"),
 SP("The Great Bath was built of *marble* brick work.|বৃহৎ স্নানাগাৰ *মাৰ্বল* ইটাৰ কাম আছিল।", "fired|পোৰা", "It is built of fired brick.|ই পোৰা ইটাৰে নিৰ্মিত।"),
 WH(["I am a Harappan city in Kutch.|মই কচ্ছৰ হৰপ্পীয় নগৰ।", "I am in Gujarat.|মই গুজৰাটত আছোঁ।", "I stored water in reservoirs.|মই জলাশয়ত পানী জমা কৰিছিলোঁ।"], ["Lothal|লোথাল", "Dholavira|ধোলাভিৰা", "Kalibangan|কালিবংগান", "Harappa|হৰপ্পা"], 1, "Dholavira, in Kutch.|কচ্ছৰ ধোলাভিৰা।"),
)
u3 = U(3, "star", "Sites and their finds|স্থল আৰু আৱিষ্কাৰ",
 "Pair each site with its find, as APSC does.|APSCৰ দৰে প্ৰতিটো স্থলক আৱিষ্কাৰৰ সৈতে মিলোৱা।",
 "Finding recorded: seals, a dock and a ploughed field.|প্ৰমাণ লিখা হ'ল: মোহৰ, ডক আৰু হাল বোৱা পথাৰ।",
 ["Steatite seals carry animals and signs|ষ্টিয়াটাইট মোহৰত জন্তু আৰু চিহ্ন আছে", "The unicorn is the most common seal animal|মোহৰত আটাইতকৈ বেছি দেখা জন্তু একশৃংগ", "Lothal is known for its dock|লোথাল ডকৰ বাবে খ্যাত", "Kalibangan shows a ploughed field|কালিবংগানত হাল বোৱা পথাৰ আছে"],
 S("A seal in the hand|হাতত এটা মোহৰ",
   "Traders stamped goods with small steatite <mark>seals</mark>. The most common animal on them is the <mark>unicorn</mark>.|বেপাৰীয়ে ষ্টিয়াটাইটৰ সৰু <mark>মোহৰেৰে</mark> বস্তুত চিন দিছিল। ইয়াত আটাইতকৈ বেছি দেখা জন্তু <mark>একশৃংগ</mark>।", art="seal"),
 S("Dock and furrow|ডক আৰু হালৰ ৰেখা",
   "[[lothal]] in Gujarat is known for a brick basin read as a <mark>dock</mark>.|গুজৰাটৰ [[lothal|লোথাল]] ডক বুলি ধৰা ইটাৰ অৱবাহিকাৰ বাবে খ্যাত।",
   "[[kalibangan]] in Rajasthan shows a <mark>ploughed field</mark>.|ৰাজস্থানৰ [[kalibangan|কালিবংগানত]] <mark>হাল বোৱা পথাৰ</mark> আছে।",
   "[[dholavira]] has ten large signs of the script, and Banawali a terracotta plough.|[[dholavira|ধোলাভিৰাত]] লিপিৰ দহটা ডাঙৰ চিহ্ন আছে, বনাৱালীত মাটিৰ নাঙল।", map={"base": "india", "box": [64, 20, 81, 31], "show": ["lothal", "kalibangan"]}),
 IN("The most common animal on Harappan seals is the|হৰপ্পীয় মোহৰত আটাইতকৈ বেছি দেখা জন্তু", ".|।", ["cow|গৰু", "unicorn|একশৃংগ", "elephant|হাতী", "tiger|বাঘ"], 1, "The unicorn appears most often.|একশৃংগ আটাইতকৈ বেছি দেখা যায়।"),
 MP("Tap Lothal.|লোথাল টিপা।", "lothal", ["lothal", "kalibangan", "harappa", "mohenjo-daro"], "Lothal is in Gujarat.|লোথাল গুজৰাটত।"),
 SP("Kalibangan is known for its *dock* field.|কালিবংগান ইয়াৰ *ডক* পথাৰৰ বাবে খ্যাত।", "ploughed|হাল বোৱা", "Lothal has the dock; Kalibangan the ploughed field.|লোথালত ডক; কালিবংগানত হাল বোৱা পথাৰ।"),
 TF("Harappan seals carry signs as well as animals.|হৰপ্পীয় মোহৰত জন্তুৰ লগতে চিহ্নও আছে।", True, "They carry images and short inscriptions.|ইয়াত ছবি আৰু চুটি লেখ আছে।"),
 OD("Which find does NOT fit a Harappan site?|কোনটো আৱিষ্কাৰ হৰপ্পীয় স্থলৰ সৈতে নিমিলে?", ["Dock|ডক", "Steatite seal|ষ্টিয়াটাইট মোহৰ", "Covered drain|ঢকা নলা", "Iron plough|লোহাৰ নাঙল"], 3, "Harappan cities are Bronze Age.|হৰপ্পীয় নগৰ ব্ৰঞ্জ যুগৰ।"),
)
u4 = U(4, "moon", "A script nobody reads|কোনেও পঢ়িব নোৱৰা লিপি",
 "Separate what is known from what is not.|কি জনা আৰু কি নজনা, পৃথক কৰা।",
 "Finding recorded: the script is undeciphered and the decline was gradual.|প্ৰমাণ লিখা হ'ল: লিপি অপঠিত আৰু পতন ক্ৰমান্বয়ে।",
 ["The Indus script is still undeciphered|সিন্ধু লিপি এতিয়াও অপঠিত", "The decline was gradual, not one event|পতন ক্ৰমান্বয়ে হৈছিল, এটা ঘটনাত নহয়", "A drying climate is one explanation|শুকান জলবায়ু এটা ব্যাখ্যা", "People moved east and south|মানুহ পূব আৰু দক্ষিণলৈ গৈছিল"],
 S("The silent signs|নীৰৱ চিহ্ন",
   "The Indus signs have <mark>not been deciphered</mark>. So we know these people from objects, not from their own words.|সিন্ধু চিহ্নবোৰ <mark>পাঠোদ্ধাৰ হোৱা নাই</mark>। সেয়ে তেওঁলোকক নিজৰ কথাৰে নহয়, বস্তুৰ পৰাহে জনা যায়।", art="scroll"),
 S("A slow ending|লাহে লাহে অন্ত",
   "After about 1900 BCE the great cities declined. A drying climate and reduced water are one leading explanation.|প্ৰায় খ্ৰীষ্টপূৰ্ব ১৯০০ৰ পিছত ডাঙৰ নগৰবোৰৰ অৱনতি হয়। শুকান জলবায়ু আৰু পানীৰ অভাৱ এটা মুখ্য ব্যাখ্যা।",
   "It was a <mark>gradual</mark> change, and people moved to other regions.|ই <mark>ক্ৰমান্বয়ে</mark> হোৱা পৰিৱৰ্তন, মানুহ আন অঞ্চললৈ গৈছিল।", art="calendar"),
 TF("Scholars can now read the Indus script fluently.|পণ্ডিতে এতিয়া সিন্ধু লিপি সহজে পঢ়িব পাৰে।", False, "It remains undeciphered.|ই এতিয়াও অপঠিত।"),
 IN("The Indus decline is best described as|সিন্ধু সভ্যতাৰ পতন আটাইতকৈ ভালকৈ কোৱা যায়", ".|।", ["sudden|হঠাৎ", "gradual|ক্ৰমান্বয়ে", "unknown to scholars|পণ্ডিতৰ অজ্ঞাত", "a single war|এটা যুদ্ধ"], 1, "It happened over a long time.|ই দীঘলীয়া সময়ত হৈছিল।"),
 WH(["I was written on seals.|মোক মোহৰত লিখা হৈছিল।", "Nobody has deciphered me.|কোনেও মোক পাঠোদ্ধাৰ কৰা নাই।"], ["Brahmi|ব্ৰাহ্মী", "Indus script|সিন্ধু লিপি", "Kharosthi|খৰোষ্ঠী", "Greek|গ্ৰীক"], 1, "Brahmi was read in 1837; the Indus script has not been.|১৮৩৭ত ব্ৰাহ্মী পঢ়া হ'ল; সিন্ধু লিপি হোৱা নাই।"),
 SC("Unscramble the animal most common on the seals.|মোহৰত আটাইতকৈ বেছি দেখা জন্তুটো সজোৱা।", "UNICORN", ["এক", "শৃং", "গ"], "The unicorn is the commonest seal animal.|মোহৰত একশৃংগ আটাইতকৈ বেছি দেখা যায়।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Mature Harappan cities|পূৰ্ণ হৰপ্পীয় নগৰ", "Decline of the cities|নগৰৰ অৱনতি", "Harappa excavated|হৰপ্পা খনন"], "About 2600 BCE, about 1900 BCE, then 1921.|প্ৰায় খ্ৰীষ্টপূৰ্ব ২৬০০, প্ৰায় খ্ৰীষ্টপূৰ্ব ১৯০০, তাৰ পিছত ১৯২১।"),
)
test = TEST("Rebuild the Indus world from its finds.|আৱিষ্কাৰৰ পৰা সিন্ধু জগত পুনৰ গঢ়া।", "Recorded: sites, finds and limits of evidence.|লিখা হ'ল: স্থল, আৱিষ্কাৰ আৰু প্ৰমাণৰ সীমা।",
 MP("Tap Harappa.|হৰপ্পা টিপা।", "harappa", ["harappa", "mohenjo-daro", "lothal", "kalibangan"], "Harappa is in Punjab, Pakistan.|হৰপ্পা পাকিস্তানৰ পঞ্জাবত।"),
 MA([("Lothal|লোথাল", "Dock|ডক"), ("Kalibangan|কালিবংগান", "Ploughed field|হাল বোৱা পথাৰ"), ("Dholavira|ধোলাভিৰা", "Ten large signs|দহটা ডাঙৰ চিহ্ন"), ("Banawali|বনাৱালী", "Terracotta plough|মাটিৰ নাঙল")], "This is the pairing APSC asked in 2025.|২০২৫ত APSCয়ে এই মিলটো সুধিছিল।"),
 IN("The commonest animal on the seals is the|মোহৰত আটাইতকৈ বেছি দেখা জন্তু", ".|।", ["unicorn|একশৃংগ", "cow|গৰু", "tiger|বাঘ", "elephant|হাতী"], 0, "The unicorn.|একশৃংগ।"),
 TF("The Indus script has been fully deciphered.|সিন্ধু লিপি সম্পূৰ্ণ পাঠোদ্ধাৰ হৈছে।", False, "It has not.|হোৱা নাই।"),
 OR("Put the digs in order.|খনন ক্ৰমে সজোৱা।", ["Harappa|হৰপ্পা", "Mohenjo-daro|মহেঞ্জোদাৰো"], "1921, then 1922.|১৯২১, তাৰ পিছত ১৯২২।"),
 MC("Consider these statements. (1) The Great Bath is at Mohenjo-daro. (2) Lothal is in Rajasthan. (3) Harappan streets had covered drains. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) বৃহৎ স্নানাগাৰ মহেঞ্জোদাৰোত। (২) লোথাল ৰাজস্থানত। (৩) হৰপ্পীয় ৰাস্তাত ঢকা নলা আছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Lothal is in Gujarat.|লোথাল গুজৰাটত।"),
)
LESSON(1, "The Indus cities|সিন্ধু উপত্যকাৰ নগৰ", "c. 2600–1900 BCE|প্ৰায় খ্ৰীষ্টপূৰ্ব ২৬০০–১৯০০", "Beginnings|আৰম্ভণি", "Evidence file 1|প্ৰমাণ নথি ১", "A city without a voice|মাত নোহোৱা নগৰ",
 "These planned cities left drains, seals and a dock, but no words anyone can read. Work out what they can still tell you.|এই পৰিকল্পিত নগৰবোৰে নলা, মোহৰ আৰু ডক এৰি গ'ল, কিন্তু কোনেও পঢ়িব পৰা শব্দ নহয়। সিহঁতে কি ক'ব পাৰে, উলিওৱা।",
 sources, [u1, u2, u3, u4], test, ["harappa", "mohenjo-daro", "lothal", "kalibangan", "dholavira"], box=BOX)
