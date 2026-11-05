#!/usr/bin/env python3
"""Lesson 10: Knowledge and stone."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "sushruta": ("person", "Sushruta|সুশ্ৰুত", "Name attached to the Sushruta Samhita, known for surgery|সুশ্ৰুত সংহিতাৰ সৈতে জড়িত নাম, শল্যচিকিৎসাৰ বাবে খ্যাত"),
 "charaka": ("person", "Charaka|চৰক", "Name attached to the Charaka Samhita, a medical treatise|চিকিৎসা গ্ৰন্থ চৰক সংহিতাৰ সৈতে জড়িত নাম"),
 "aryabhata": ("person", "Aryabhata|আৰ্যভট্ট", "Astronomer and mathematician, born 476 CE|জ্যোতিৰ্বিদ আৰু গণিতজ্ঞ, জন্ম ৪৭৬ খ্ৰীষ্টাব্দ"),
 "ajanta": ("place", "Ajanta|অজন্তা", "Buddhist rock-cut caves in Maharashtra|মহাৰাষ্ট্ৰৰ বৌদ্ধ শিলকটা গুহা", [20.55, 75.70]),
 "elephanta": ("place", "Elephanta|এলিফেণ্টা", "Island caves in Mumbai Harbour|মুম্বাই বন্দৰৰ দ্বীপৰ গুহা", [18.96, 72.93]),
 "khajuraho": ("place", "Khajuraho|খাজুৰাহো", "Temple group in Chhatarpur, Madhya Pradesh|মধ্য প্ৰদেশৰ ছত্ৰপুৰৰ মন্দিৰ সমূহ", [24.85, 79.92]),
})
sources = [
 src("Wikipedia, Sushruta", "https://en.wikipedia.org/wiki/Sushruta", "Used as a guide: composite text, surgery chapters not its main focus, 'father of surgery' as a label. Check in review."),
 src("Wikipedia, Aryabhata", "https://en.wikipedia.org/wiki/Aryabhata", "Used as a guide: 476, Aryabhatiya, Kusumapura, rotation, place value without a symbol for zero. Check in review."),
 src("Wikipedia, Nalanda mahavihara", "https://en.wikipedia.org/wiki/Nalanda_mahavihara", "Used as a guide: Kumaragupta I, about 427, Xuanzang, about 1200 and its uncertainty, UNESCO 2016. Check in review."),
 src("Wikipedia, Ajanta Caves", "https://en.wikipedia.org/wiki/Ajanta_Caves", "Used as a guide: two phases, Jataka murals, Padmapani, UNESCO 1983. Check in review."),
 src("Wikipedia, Elephanta Caves", "https://en.wikipedia.org/wiki/Elephanta_Caves", "Used as a guide: Mumbai Harbour, Trimurti Sadashiva, Shiva, UNESCO 1987. Check in review."),
 src("Wikipedia, Khajuraho Group of Monuments", "https://en.wikipedia.org/wiki/Khajuraho_Group_of_Monuments", "Used as a guide: Chandela, Hindu and Jain, Nagara style, Chhatarpur, UNESCO 1986. Check in review."),
]
u1 = U(1, "star", "Medicine|চিকিৎসা",
 "Keep Charaka and Sushruta apart.|চৰক আৰু সুশ্ৰুত পৃথক ৰাখা।", "Finding recorded: papers call Sushruta the father of surgery; the texts are composite.|প্ৰমাণ লিখা হ'ল: পৰীক্ষাত সুশ্ৰুতক শল্যচিকিৎসাৰ জনক বোলে; গ্ৰন্থবোৰ বহুজনৰ।",
 ["Papers call Sushruta the Father of Surgery|পৰীক্ষাত সুশ্ৰুতক শল্যচিকিৎসাৰ জনক বোলে", "The Sushruta Samhita is a medical treatise|সুশ্ৰুত সংহিতা চিকিৎসা গ্ৰন্থ", "Charaka's name goes with the Charaka Samhita|চৰকৰ নাম চৰক সংহিতাৰ সৈতে", "Both texts were revised over time|দুয়োখন গ্ৰন্থ সময়ত সংশোধিত হৈছিল"],
 S("A surgeon's name|শল্যবিদৰ নাম", "Exam papers call <mark>[[sushruta|Sushruta]]</mark> the Father of Surgery. That is a modern label for the name behind the Sushruta Samhita.|পৰীক্ষাত <mark>[[sushruta|সুশ্ৰুতক]]</mark> শল্যচিকিৎসাৰ জনক বোলে। ই সুশ্ৰুত সংহিতাৰ নামৰ আধুনিক উপাধি।", "The book covers wider medicine too, and its surgery, including nose repair, made it famous.|গ্ৰন্থখনত বহল চিকিৎসাও আছে, নাক মেৰামতিৰ দৰে শল্যচিকিৎসাই ইয়াক বিখ্যাত কৰিছে।", art="scroll"),
 S("Books with many hands|বহুজনৰ হাতৰ গ্ৰন্থ", "The <mark>Charaka Samhita</mark> goes with [[charaka|Charaka]]. Texts like these were revised by later hands, so a single author and date are hard to fix.|<mark>চৰক সংহিতা</mark> [[charaka|চৰকৰ]] সৈতে জড়িত। এনে গ্ৰন্থ পিছৰ লেখকে সংশোধন কৰিছিল, সেয়ে এজন লেখক আৰু তাৰিখ ঠিক কৰা কঠিন।", art="seal"),
 IN("The ancient Indian physician called the Father of Surgery is|শল্যচিকিৎসাৰ জনক বুলি কোৱা প্ৰাচীন ভাৰতীয় চিকিৎসক", ".|।", ["Charaka|চৰক", "Sushruta|সুশ্ৰুত", "Vagbhata|বাগ্ভট", "Vinayaka|বিনায়ক"], 1, "Sushruta.|সুশ্ৰুত।"),
 MA([("Sushruta|সুশ্ৰুত", "Surgery|শল্যচিকিৎসা"), ("Charaka|চৰক", "Charaka Samhita|চৰক সংহিতা"), ("Aryabhata|আৰ্যভট্ট", "Astronomy|জ্যোতিৰ্বিদ্যা")], "Name and field.|নাম আৰু ক্ষেত্ৰ।"),
 TF("The Sushruta Samhita deals only with surgery.|সুশ্ৰুত সংহিতাত কেৱল শল্যচিকিৎসা আছে।", False, "It covers general medicine too.|ইয়াত সাধাৰণ চিকিৎসাও আছে।"),
 SP("Papers call *Charaka* the Father of Surgery.|পৰীক্ষাত *চৰকক* শল্যচিকিৎসাৰ জনক বোলে।", "Sushruta|সুশ্ৰুতক", "That label goes to Sushruta.|এই উপাধি সুশ্ৰুতৰ।"),
 SC("Unscramble the name linked with surgery.|শল্যচিকিৎসাৰ সৈতে জড়িত নামটো সজোৱা।", "SUSHRUTA", ["সু", "শ্ৰু", "ত"], "Sushruta.|সুশ্ৰুত।"),
)
u2 = U(2, "star", "Numbers and stars|সংখ্যা আৰু নক্ষত্ৰ",
 "Answer the zero question, then say what is really known.|শূন্যৰ প্ৰশ্নৰ উত্তৰ দিয়া, তাৰ পিছত সঁচাকৈ কি জনা কোৱা।", "Finding recorded: Aryabhata is the exam answer, but he used no symbol for zero.|প্ৰমাণ লিখা হ'ল: আৰ্যভট্ট পৰীক্ষাৰ উত্তৰ, কিন্তু তেওঁ শূন্যৰ চিহ্ন ব্যৱহাৰ কৰা নাছিল।",
 ["Aryabhata was born in 476 CE|আৰ্যভট্টৰ জন্ম ৪৭৬ খ্ৰীষ্টাব্দত", "His surviving work is the Aryabhatiya|তেওঁৰ থকা ৰচনা আৰ্যভটীয়", "He said the Earth rotates on its axis|তেওঁ পৃথিৱীয়ে অক্ষত ঘূৰে বুলি কৈছিল", "'Father of zero' is an exam label|'শূন্যৰ জনক' পৰীক্ষাৰ উপাধি"],
 S("The man from Kusumapura|কুসুমপুৰৰ মানুহ", "<mark>[[aryabhata|Aryabhata]]</mark>, born in 476, wrote the <mark>Aryabhatiya</mark> and linked himself with Kusumapura, Pataliputra.|<mark>[[aryabhata|আৰ্যভট্টই]]</mark>, ৪৭৬ত জন্ম, <mark>আৰ্যভটীয়</mark> লিখিছিল আৰু নিজকে কুসুমপুৰ বা পাটলিপুত্ৰৰ সৈতে জড়িত কৰিছিল।", "He said the Earth is round and rotates daily on its axis.|তেওঁ কৈছিল পৃথিৱী গোল আৰু দৈনিক অক্ষত ঘূৰে।", art="calendar"),
 S("The zero question|শূন্যৰ প্ৰশ্ন", "A paper asked who is the father of zero, and the expected answer is <mark>Aryabhata</mark>.|এখন প্ৰশ্নকাকতত শূন্যৰ জনক কোন সোধা হৈছিল, প্ৰত্যাশিত উত্তৰ <mark>আৰ্যভট্ট</mark>।", "The full story is less simple. His place-value system needed zero, yet he had <mark>no symbol</mark> for it. Treat the title as a label.|সম্পূৰ্ণ কাহিনী ইমান সহজ নহয়। তেওঁৰ স্থানীয় মানৰ পদ্ধতিত শূন্য লাগিছিল, কিন্তু তেওঁৰ <mark>চিহ্ন নাছিল</mark>। উপাধিটো উপাধি বুলিয়েই ধৰা।", art="scroll"),
 IN("Papers call the father of zero|পৰীক্ষাত শূন্যৰ জনক বোলা হয়", ".|ক।", ["Chitragupta|চিত্ৰগুপ্ত", "Brahmadutta|ব্ৰহ্মদত্ত", "Varahamihira|বৰাহমিহিৰ", "Aryabhata|আৰ্যভট্ট"], 3, "That is the expected answer.|এয়া প্ৰত্যাশিত উত্তৰ।"),
 TF("Aryabhata used a written symbol for zero.|আৰ্যভট্টই শূন্যৰ লিখিত চিহ্ন ব্যৱহাৰ কৰিছিল।", False, "His system implied zero, without a symbol.|তেওঁৰ পদ্ধতিত চিহ্ন নোহোৱাকৈ শূন্য নিহিত আছিল।"),
 WH(["I was born in 476.|মোৰ জন্ম ৪৭৬ত।", "I said the Earth rotates.|মই পৃথিৱী ঘূৰে বুলিছিলোঁ।", "My book carries my name.|মোৰ গ্ৰন্থত মোৰ নাম।"], ["Sushruta|সুশ্ৰুত", "Aryabhata|আৰ্যভট্ট", "Kalhana|কলহণ", "Kalidasa|কালিদাস"], 1, "Aryabhata.|আৰ্যভট্ট।"),
 SP("Aryabhata linked himself with *Kashmir.*|আৰ্যভট্টই নিজকে *কাশ্মীৰৰ* সৈতে জড়িত কৰিছিল।", "Kusumapura|কুসুমপুৰৰ", "Kusumapura is Pataliputra.|কুসুমপুৰ পাটলিপুত্ৰ।"),
 OD("Which is NOT linked with Aryabhata?|কোনটো আৰ্যভট্টৰ সৈতে জড়িত নহয়?", ["Aryabhatiya|আৰ্যভটীয়", "Earth's rotation|পৃথিৱীৰ ঘূৰ্ণন", "Place value|স্থানীয় মান", "Nose surgery|নাকৰ শল্যচিকিৎসা"], 3, "That is Sushruta's text.|সেয়া সুশ্ৰুতৰ গ্ৰন্থৰ।"),
)
u3 = U(3, "houses", "Nalanda|নালন্দা",
 "Follow a great monastery from start to end.|এখন মহান বিহাৰৰ আৰম্ভণিৰ পৰা অন্তলৈ অনুসৰণ কৰা।", "Finding recorded: founded about 427, with Xuanzang as a student, damaged about 1200.|প্ৰমাণ লিখা হ'ল: প্ৰায় ৪২৭ত প্ৰতিষ্ঠিত, হিউৱেন চাঙ ছাত্ৰ, প্ৰায় ১২০০ত ক্ষতিগ্ৰস্ত।",
 ["Nalanda is in Bihar|নালন্দা বিহাৰত", "Kumaragupta I founded it about 427|প্ৰায় ৪২৭ত কুমাৰগুপ্ত প্ৰথমে প্ৰতিষ্ঠা কৰিছিল", "Xuanzang studied there|হিউৱেন চাঙে তাত অধ্যয়ন কৰিছিল", "It became a World Heritage Site in 2016|২০১৬ত বিশ্ব ঐতিহ্য স্থল হৈছিল"],
 S("A monastery in Bihar|বিহাৰৰ এখন মহাবিহাৰ", "<mark>[[nalanda|Nalanda]]</mark> was founded about 427 under the Gupta king Kumaragupta I. [[xuanzang|Xuanzang]] studied there in the 7th century.|<mark>[[nalanda|নালন্দা]]</mark> প্ৰায় ৪২৭ত গুপ্ত ৰজা কুমাৰগুপ্ত প্ৰথমৰ অধীনত প্ৰতিষ্ঠিত হৈছিল। সপ্তম শতিকাত [[xuanzang|হিউৱেন চাঙে]] তাত অধ্যয়ন কৰিছিল।", art="houses"),
 S("The end, and its limits|অন্ত আৰু তাৰ সীমা", "About 1200 it was likely sacked by Muhammad Bakhtiyar Khalji. The evidence is debated, and it may have lingered until about 1400.|প্ৰায় ১২০০ত মহম্মদ বখতিয়াৰ খিলজীয়ে সম্ভৱতঃ ইয়াক লুণ্ঠন কৰিছিল। প্ৰমাণ বিতৰ্কিত, ই প্ৰায় ১৪০০লৈ কোনোমতে চলিব পাৰে।", "UNESCO listed the site in <mark>2016</mark>.|২০১৬ত ইউনেস্কোৱে স্থলটো তালিকাভুক্ত কৰে।", art="calendar"),
 TF("Nalanda is in Maharashtra.|নালন্দা মহাৰাষ্ট্ৰত।", False, "It is in Bihar.|ই বিহাৰত।"),
 IN("Nalanda was founded under the|নালন্দা প্ৰতিষ্ঠিত হৈছিল", " dynasty.|বংশৰ অধীনত।", ["Maurya|মৌৰ্য", "Gupta|গুপ্ত", "Chola|চোল", "Kushan|কুষাণ"], 1, "Under Kumaragupta I.|কুমাৰগুপ্ত প্ৰথমৰ অধীনত।"),
 OR("Put Nalanda's story in order.|নালন্দাৰ কাহিনী ক্ৰমে সজোৱা।", ["Founded|প্ৰতিষ্ঠা", "Xuanzang studies there|হিউৱেন চাঙৰ অধ্যয়ন", "Likely sacked|সম্ভৱতঃ লুণ্ঠন", "UNESCO listing|ইউনেস্কো তালিকা"], "About 427, 7th century, about 1200, 2016.|প্ৰায় ৪২৭, সপ্তম শতিকা, প্ৰায় ১২০০, ২০১৬।"),
 SP("Nalanda was likely sacked by Mahmud of *Ghazni.*|নালন্দা সম্ভৱতঃ মাহমুদ *গজনীয়ে* লুণ্ঠন কৰিছিল।", "Bakhtiyar Khalji|বখতিয়াৰ খিলজীয়ে", "The usual attribution is Bakhtiyar Khalji.|সাধাৰণতে বখতিয়াৰ খিলজীৰ নাম লোৱা হয়।"),
 WH(["I was a Chinese pilgrim.|মই চীনা তীৰ্থযাত্ৰী।", "I studied at Nalanda.|মই নালন্দাত পঢ়িছিলোঁ।", "I also visited Kamarupa.|মই কামৰূপলৈও গৈছিলোঁ।"], ["Faxian|ফা-হিয়েন", "Xuanzang|হিউৱেন চাঙ", "Megasthenes|মেগাস্থিনিছ", "Ibn Battuta|ইবন বতুতা"], 1, "Xuanzang.|হিউৱেন চাঙ।"),
)
u4 = U(4, "seal", "Three monuments|তিনিটা স্মাৰক",
 "Tie each monument to its faith, place and fact.|প্ৰতিটো স্মাৰক ধৰ্ম, ঠাই আৰু তথ্যৰ সৈতে মিলোৱা।", "Finding recorded: Ajanta is Buddhist, Elephanta for Shiva, Khajuraho Hindu and Jain.|প্ৰমাণ লিখা হ'ল: অজন্তা বৌদ্ধ, এলিফেণ্টা শিৱৰ, খাজুৰাহো হিন্দু আৰু জৈন।",
 ["Ajanta has Buddhist caves and murals|অজন্তাত বৌদ্ধ গুহা আৰু চিত্ৰ", "The Trimurti Sadashiva is at Elephanta|ত্ৰিমূৰ্তি সদাশিৱ এলিফেণ্টাত", "Khajuraho was built under the Chandelas|খাজুৰাহো চান্দেলৰ অধীনত নিৰ্মিত", "Khajuraho has Hindu and Jain temples in Nagara style|খাজুৰাহোত নাগৰ শৈলীৰ হিন্দু আৰু জৈন মন্দিৰ"],
 S("Caves|গুহা", "[[ajanta]] in Maharashtra is <mark>Buddhist</mark>: rock-cut halls with Jataka murals.|মহাৰাষ্ট্ৰৰ [[ajanta|অজন্তা]] <mark>বৌদ্ধ</mark>: জাতক চিত্ৰসহ শিলকটা গুহা।", "[[elephanta]], in Mumbai Harbour, holds the <mark>Trimurti Sadashiva</mark>, a three-headed form of Shiva.|মুম্বাই বন্দৰৰ [[elephanta|এলিফেণ্টাত]] শিৱৰ তিনিমূৰীয়া ৰূপ <mark>ত্ৰিমূৰ্তি সদাশিৱ</mark> আছে।", map={"base": "india", "box": [67, 16, 84, 25.5], "show": ["ajanta", "elephanta", "khajuraho"]}),
 S("Khajuraho|খাজুৰাহো", "[[khajuraho]] in Chhatarpur, Madhya Pradesh, was built under the <mark>Chandela</mark> dynasty.|মধ্য প্ৰদেশৰ ছত্ৰপুৰৰ [[khajuraho|খাজুৰাহো]] <mark>চান্দেল</mark> বংশৰ অধীনত নিৰ্মিত।", "It has Hindu and Jain temples in the northern <mark>Nagara</mark> style, not the Dravidian style.|ইয়াত দ্ৰাৱিড় নহয়, উত্তৰৰ <mark>নাগৰ</mark> শৈলীৰ হিন্দু আৰু জৈন মন্দিৰ আছে।", art="houses"),
 IN("The famous Trimurti Sadashiva is part of the caves at|বিখ্যাত ত্ৰিমূৰ্তি সদাশিৱ আছে", ".|ৰ গুহাত।", ["Ajanta|অজন্তা", "Ellora|ইলোৰা", "Elephanta|এলিফেণ্টা", "Bagh|বাঘ"], 2, "Elephanta, Mumbai Harbour.|এলিফেণ্টা, মুম্বাই বন্দৰ।"),
 MP("Tap Khajuraho.|খাজুৰাহো টিপা।", "khajuraho", ["khajuraho", "elephanta", "nalanda", "pataliputra"], "It is in Madhya Pradesh.|ই মধ্য প্ৰদেশত।"),
 MA([("Ajanta|অজন্তা", "Buddhist murals|বৌদ্ধ চিত্ৰ"), ("Elephanta|এলিফেণ্টা", "Trimurti Sadashiva|ত্ৰিমূৰ্তি সদাশিৱ"), ("Khajuraho|খাজুৰাহো", "Chandelas|চান্দেল")], "Monument and fact.|স্মাৰক আৰু তথ্য।"),
 TF("Khajuraho's temples are in the Dravidian style.|খাজুৰাহোৰ মন্দিৰ দ্ৰাৱিড় শৈলীৰ।", False, "They are Nagara.|এইবোৰ নাগৰ।"),
 SP("Khajuraho is in Chhatarpur district of *Maharashtra.*|খাজুৰাহো *মহাৰাষ্ট্ৰৰ* ছত্ৰপুৰ জিলাত।", "Madhya Pradesh|মধ্য প্ৰদেশৰ", "It is in Madhya Pradesh.|ই মধ্য প্ৰদেশত।"),
)
test = TEST("Sort knowledge and stone.|জ্ঞান আৰু শিল পৃথক কৰা।", "Recorded: scholars, a monastery and three monuments.|লিখা হ'ল: পণ্ডিত, মহাবিহাৰ আৰু তিনিটা স্মাৰক।",
 IN("The Trimurti Sadashiva is at|ত্ৰিমূৰ্তি সদাশিৱ আছে", ".|ত।", ["Ajanta|অজন্তা", "Ellora|ইলোৰা", "Elephanta|এলিফেণ্টা", "Bagh|বাঘ"], 2, "Elephanta.|এলিফেণ্টা।"),
 MA([("Sushruta|সুশ্ৰুত", "Father of Surgery, in papers|পৰীক্ষাত শল্যচিকিৎসাৰ জনক"), ("Aryabhata|আৰ্যভট্ট", "Father of zero, in papers|পৰীক্ষাত শূন্যৰ জনক"), ("Kumaragupta I|কুমাৰগুপ্ত প্ৰথম", "Nalanda|নালন্দা")], "Name and association.|নাম আৰু সম্পৰ্ক।"),
 MP("Tap Elephanta.|এলিফেণ্টা টিপা।", "elephanta", ["elephanta", "khajuraho", "nalanda", "pataliputra"], "In Mumbai Harbour.|মুম্বাই বন্দৰত।"),
 TF("Ajanta's caves are Jain.|অজন্তাৰ গুহা জৈন।", False, "They are Buddhist.|এইবোৰ বৌদ্ধ।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Aryabhata born|আৰ্যভট্টৰ জন্ম", "Xuanzang at Nalanda|নালন্দাত হিউৱেন চাঙ", "Kandariya Mahadeva finished|কন্দৰীয়া মহাদেৱ সম্পূৰ্ণ"], "476, 7th century, about 1029.|৪৭৬, সপ্তম শতিকা, প্ৰায় ১০২৯।"),
 MC("Consider these statements about Khajuraho. (1) It was built during the Chandela dynasty. (2) It has Hindu and Jain temples. (3) It is in the Dravidian style. Which are correct?|খাজুৰাহো সম্পৰ্কে এই উক্তিবোৰ বিবেচনা কৰা। (১) ই চান্দেল বংশৰ সময়ত নিৰ্মিত। (২) ইয়াত হিন্দু আৰু জৈন মন্দিৰ আছে। (৩) ই দ্ৰাৱিড় শৈলীৰ। কোনবোৰ শুদ্ধ?", ["1 only|কেৱল ১", "1 and 2 only|কেৱল ১ আৰু ২", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "It is in the Nagara style.|ই নাগৰ শৈলীৰ।"),
)
LESSON(10, "Knowledge and stone|জ্ঞান আৰু শিলৰ কলা", "Ancient India|প্ৰাচীন ভাৰত", "South, Kashmir and learning|দক্ষিণ, কাশ্মীৰ আৰু জ্ঞানচৰ্চা", "Evidence file 10|প্ৰমাণ নথি ১০", "Titles and truths|উপাধি আৰু সত্য",
 "Papers love titles like Father of Surgery. Learn the answer they want, and what the evidence really shows.|পৰীক্ষাত শল্যচিকিৎসাৰ জনকৰ দৰে উপাধি প্ৰায়ে আহে। প্ৰত্যাশিত উত্তৰ শিকা, প্ৰমাণে সঁচাকৈ কি দেখুৱায়, সেয়াও শিকা।",
 sources, [u1, u2, u3, u4], test, ["elephanta", "khajuraho", "nalanda", "pataliputra", "ajanta"])
