#!/usr/bin/env python3
"""Lesson 22: Indigo, press and schools."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "dinabandhu-mitra": ("person", "Dinabandhu Mitra|দীনবন্ধু মিত্ৰ", "Author of the play Nil Darpan|নীলদৰ্পণ নাটকৰ লেখক"),
 "nil-darpan": ("term", "Nil Darpan|নীলদৰ্পণ", "Play of 1860 on the oppression of indigo cultivators|নীল খেতিয়কৰ ওপৰত অত্যাচাৰৰ ১৮৬০ৰ নাটক"),
 "sidhu-kanhu": ("person", "Sidhu and Kanhu Murmu|সিধু আৰু কানহু মুৰ্মু", "Brothers who led the Santhal rebellion|চাঁওতাল বিদ্ৰোহৰ নেতা ভাতৃদ্বয়"),
 "nadia": ("place", "Nadia|নদীয়া", "Bengal district where the indigo revolt began|নীল বিদ্ৰোহ আৰম্ভ হোৱা বংগৰ জিলা", [23.47, 88.56]),
})
sources = [
 src("Wikipedia, Indigo revolt", "https://en.wikipedia.org/wiki/Indigo_revolt", "Used as a guide: 1859 to about 1862, Nadia, causes, Indigo Commission, Nil Darpan, James Long. Check in review."),
 src("APSC CCE Prelims 2025 GS-I, question 31, page read", "https://apsc.nic.in/cce.html", "Printed statements on Nil Darpan."),
 src("Wikipedia, Wood's despatch", "https://en.wikipedia.org/wiki/Wood%27s_despatch", "Used as a guide: 19 July 1854, recommendations, universities of 1857. Check in review."),
 src("APSC CCE Prelims 2023 GS-I, question 6", "https://apsc.nic.in/cce.html", "The chain of Macaulay, Wood, Raleigh and Sadler. The dates 1902 and 1917 are from general reference, as both Wikipedia pages tried returned errors. Check in review."),
 src("Wikipedia, Santal rebellion", "https://en.wikipedia.org/wiki/Santal_rebellion", "Used as a guide: 30 June 1855, Sidhu and Kanhu, causes. Check in review."),
]
u1 = U(1, "river", "Indigo|নীল",
 "See why peasants turned on the planters.|খেতিয়কে নীলকৰৰ বিৰুদ্ধে কিয় থিয় দিলে, চোৱা।", "Finding recorded: forced indigo and debt led to revolt from 1859.|প্ৰমাণ লিখা হ'ল: বাধ্যতামূলক নীল আৰু ধাৰে ১৮৫৯ৰ পৰা বিদ্ৰোহলৈ নিলে।",
 ["The Indigo Revolt began in Bengal in 1859|১৮৫৯ত বংগত নীল বিদ্ৰোহ আৰম্ভ হৈছিল", "Planters forced peasants to grow indigo|নীলকৰে খেতিয়কক নীল খেতি কৰিবলৈ বাধ্য কৰিছিল", "Sidhu and Kanhu led the Santhals in 1855|১৮৫৫ত সিধু আৰু কানহুৱে চাঁওতালৰ নেতৃত্ব দিছিল", "The Indigo Commission came in 1860|১৮৬০ত নীল কমিচন গঠন হৈছিল"],
 S("Food or indigo|খাদ্য নে নীল", "European planters forced Bengal's peasants to grow <mark>indigo</mark> in place of food, on loans that kept them in debt.|ইউৰোপীয় নীলকৰে বংগৰ খেতিয়কক খাদ্যৰ ঠাইত <mark>নীল</mark> খেতি কৰিবলৈ বাধ্য কৰিছিল, ধাৰৰ জালত ৰাখিছিল।", art="houses"),
 S("Nadia rises|নদীয়াৰ উত্থান", "The revolt began in March <mark>1859</mark> in [[nadia]] and spread. It was aimed at the planters more than at British authority.|১৮৫৯ৰ মাৰ্চত [[nadia|নদীয়াত]] বিদ্ৰোহ আৰম্ভ হৈ বিয়পিল। ই ব্ৰিটিছ শাসনতকৈ নীলকৰৰ বিৰুদ্ধে আছিল।", "The government set up an Indigo Commission in 1860.|১৮৬০ত চৰকাৰে নীল কমিচন গঠন কৰিছিল।", art="door"),
 LINK(S("Other risings|আন বিদ্ৰোহ", "The <mark>Santhals</mark>, led by [[sidhu-kanhu|Sidhu and Kanhu]], rose in 1855 against moneylenders and landlords.|[[sidhu-kanhu|সিধু আৰু কানহুৰ]] নেতৃত্বত <mark>চাঁওতালে</mark> ১৮৫৫ত মহাজন আৰু জমিদাৰৰ বিৰুদ্ধে বিদ্ৰোহ কৰিছিল।", "Assam's peasants rose too, at Phulaguri in 1861.|১৮৬১ত ফুলগুৰিত অসমৰ খেতিয়কেও বিদ্ৰোহ কৰিছিল।", art="door"),
  "british-05", 42, 1, "The village feels the pressure|গাঁৱত হেঁচা", "The Assam History course tells the Phulaguri rising.|অসমৰ ইতিহাস পাঠ্যক্ৰমত ফুলগুৰি বিদ্ৰোহৰ কথা আছে।"),
 TF("The Indigo Revolt began in Bengal.|নীল বিদ্ৰোহ বংগত আৰম্ভ হৈছিল।", True, "In Nadia, in 1859.|১৮৫৯ত নদীয়াত।"),
 IN("The Indigo Revolt began in|নীল বিদ্ৰোহ আৰম্ভ হৈছিল", ".|ত।", ["1857|১৮৫৭", "1859|১৮৫৯", "1885|১৮৮৫", "1905|১৯০৫"], 1, "1859.|১৮৫৯।"),
 MP("Tap Nadia.|নদীয়া টিপা।", "nadia", ["nadia", "delhi", "bombay", "jhansi"], "In Bengal.|বংগত।"),
 SP("Planters forced peasants to grow *cotton* in Bengal.|নীলকৰে বংগৰ খেতিয়কক *কপাহ* খেতি কৰিবলৈ বাধ্য কৰিছিল।", "indigo|নীল", "It was indigo.|ই নীল।"),
 SC("Unscramble the crop.|শস্যটো সজোৱা।", "INDIGO", ["নী", "ল"], "Indigo.|নীল।"),
)
u2 = U(2, "scroll", "A play in the dock|কাঠগড়াত নাটক",
 "Learn the Nil Darpan facts.|নীলদৰ্পণৰ তথ্য শিকা।", "Finding recorded: Dinabandhu Mitra, 1860, on indigo oppression; James Long tried.|প্ৰমাণ লিখা হ'ল: দীনবন্ধু মিত্ৰ, ১৮৬০, নীল অত্যাচাৰ; জেমছ লঙৰ বিচাৰ।",
 ["Nil Darpan was written in 1860|১৮৬০ত নীলদৰ্পণ লিখা হৈছিল", "Its author was Dinabandhu Mitra|ইয়াৰ লেখক দীনবন্ধু মিত্ৰ", "It shows the oppression of Bengal's peasants|ইয়াত বংগৰ খেতিয়কৰ ওপৰত অত্যাচাৰ আছে", "James Long was tried over its English translation|ইংৰাজী অনুবাদৰ বাবে জেমছ লঙৰ বিচাৰ হৈছিল"],
 S("A mirror of indigo|নীলৰ দৰ্পণ", "<mark>[[nil-darpan|Nil Darpan]]</mark> was written in <mark>1860</mark> by [[dinabandhu-mitra|Dinabandhu Mitra]]. It showed European planters oppressing Bengal's peasants.|<mark>[[nil-darpan|নীলদৰ্পণ]]</mark> <mark>১৮৬০ত</mark> [[dinabandhu-mitra|দীনবন্ধু মিত্ৰই]] লিখিছিল। ইয়াত ইউৰোপীয় নীলকৰে বংগৰ খেতিয়কক অত্যাচাৰ কৰা দেখুওৱা হৈছে।", "Papers offer Munshi Premchand as a false author.|পৰীক্ষাত মুন্সী প্ৰেমচান্দক ভুল লেখক হিচাপে দিয়া হয়।", art="scroll"),
 S("The publisher pays|প্ৰকাশকৰ মাচুল", "An English translation led to the publisher, <mark>James Long</mark>, being tried and fined.|ইংৰাজী অনুবাদৰ বাবে প্ৰকাশক <mark>জেমছ লঙৰ</mark> বিচাৰ হৈ জৰিমনা হৈছিল।", art="court"),
 IN("The author of Nil Darpan was|নীলদৰ্পণৰ লেখক", ".|।", ["Munshi Premchand|মুন্সী প্ৰেমচান্দ", "Dinabandhu Mitra|দীনবন্ধু মিত্ৰ", "Bankim Chandra|বংকিমচন্দ্ৰ", "Rabindranath Tagore|ৰবীন্দ্ৰনাথ ঠাকুৰ"], 1, "Dinabandhu Mitra.|দীনবন্ধু মিত্ৰ।"),
 TF("Nil Darpan was written in 1860.|১৮৬০ত নীলদৰ্পণ লিখা হৈছিল।", True, "Yes.|হয়।"),
 WH(["I published a translation.|মই এটা অনুবাদ প্ৰকাশ কৰিছিলোঁ।", "I was tried and fined.|মোৰ বিচাৰ হৈ জৰিমনা হৈছিল।"], ["James Long|জেমছ লং", "Macaulay|মেকলে", "Robert Clive|ৰবাৰ্ট ক্লাইভ", "Hector Munro|হেক্টৰ মুনৰো"], 0, "James Long.|জেমছ লং।"),
 SP("Nil Darpan portrays the oppression of Bengal's *weavers.*|নীলদৰ্পণত বংগৰ *তাঁতীৰ* ওপৰত অত্যাচাৰ আছে।", "peasants|খেতিয়কৰ", "Indigo peasants.|নীল খেতিয়ক।"),
 OD("Which statement about Nil Darpan is FALSE?|নীলদৰ্পণৰ কোনটো উক্তি মিছা?", ["Written in 1860|১৮৬০ত লিখা", "By Dinabandhu Mitra|দীনবন্ধু মিত্ৰৰ", "About indigo planters|নীলকৰৰ বিষয়ে", "By Premchand|প্ৰেমচান্দৰ"], 3, "Premchand did not write it.|প্ৰেমচান্দে লিখা নাছিল।"),
)
u3 = U(3, "calendar", "The education chain|শিক্ষাৰ শৃংখল",
 "Order the education documents, as APSC does.|APSCৰ দৰে শিক্ষা নথিবোৰ ক্ৰমে সজোৱা।", "Finding recorded: Macaulay, Wood, Raleigh, Sadler.|প্ৰমাণ লিখা হ'ল: মেকলে, উড, ৰেলে, চেডলাৰ।",
 ["Macaulay's Minute came in 1835|মেকলেৰ টোকা ১৮৩৫ত", "Wood's Despatch came in 1854|উডৰ ডেচপেচ ১৮৫৪ত", "The Raleigh Commission came in 1902|ৰেলে কমিচন ১৯০২ত", "The Sadler Commission came in 1917|চেডলাৰ কমিচন ১৯১৭ত"],
 S("Wood's Despatch|উডৰ ডেচপেচ", "On 19 July <mark>1854</mark> Sir Charles Wood sent his Despatch. It asked for education departments, universities and grants-in-aid.|<mark>১৮৫৪ৰ</mark> ১৯ জুলাইত ছাৰ চাৰ্লছ উডে তেওঁৰ ডেচপেচ পঠাইছিল। ইয়াত শিক্ষা বিভাগ, বিশ্ববিদ্যালয় আৰু অনুদানৰ কথা আছিল।", "Universities at <b>Calcutta, Bombay and Madras</b> opened in 1857.|১৮৫৭ত <b>কলিকতা, বোম্বে আৰু মাদ্ৰাজত</b> বিশ্ববিদ্যালয় হৈছিল।", art="scroll"),
 S("Four in a row|ক্ৰমে চাৰিটা", "APSC asked for this order: <b>Macaulay's Minute 1835, Wood's Despatch 1854, Raleigh Commission 1902, Sadler Commission 1917</b>.|APSCয়ে এই ক্ৰম সুধিছিল: <b>মেকলেৰ টোকা ১৮৩৫, উডৰ ডেচপেচ ১৮৫৪, ৰেলে কমিচন ১৯০২, চেডলাৰ কমিচন ১৯১৭</b>।", art="calendar"),
 OR("Put these in chronological order.|এইবোৰ কালানুক্ৰমে সজোৱা।", ["Macaulay's Minute|মেকলেৰ টোকা", "Wood's Despatch|উডৰ ডেচপেচ", "Raleigh Commission|ৰেলে কমিচন", "Sadler Commission|চেডলাৰ কমিচন"], "1835, 1854, 1902, 1917.|১৮৩৫, ১৮৫৪, ১৯০২, ১৯১৭।"),
 IN("Wood's Despatch was sent in|উডৰ ডেচপেচ পঠোৱা হৈছিল", ".|ত।", ["1835|১৮৩৫", "1854|১৮৫৪", "1902|১৯০২", "1917|১৯১৭"], 1, "1854.|১৮৫৪।"),
 MA([("1835|১৮৩৫", "Macaulay|মেকলে"), ("1854|১৮৫৪", "Wood|উড"), ("1902|১৯০২", "Raleigh|ৰেলে"), ("1917|১৯১৭", "Sadler|চেডলাৰ")], "Year and name.|বছৰ আৰু নাম।"),
 TF("The first universities came after Wood's Despatch.|উডৰ ডেচপেচৰ পিছত প্ৰথম বিশ্ববিদ্যালয় হৈছিল।", True, "In 1857.|১৮৫৭ত।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1854, "Wood's Despatch|উডৰ ডেচপেচ"), (1902, "Raleigh Commission|ৰেলে কমিচন")], [("Macaulay's Minute, 1835|মেকলেৰ টোকা, ১৮৩৫", 0), ("First universities, 1857|প্ৰথম বিশ্ববিদ্যালয়, ১৮৫৭", 1), ("Sadler Commission, 1917|চেডলাৰ কমিচন, ১৯১৭", 2)], "1835 → 1854 → 1857 → 1902 → 1917.|১৮৩৫ → ১৮৫৪ → ১৮৫৭ → ১৯০২ → ১৯১৭।"),
)
test = TEST("Trace protest and schooling.|প্ৰতিবাদ আৰু শিক্ষা অনুসৰণ কৰা।", "Recorded: indigo, Nil Darpan, Santhals and education.|লিখা হ'ল: নীল, নীলদৰ্পণ, চাঁওতাল আৰু শিক্ষা।",
 IN("Sidhu and Kanhu led the|সিধু আৰু কানহুৱে নেতৃত্ব দিছিল", ".|ৰ।", ["Indigo Revolt|নীল বিদ্ৰোহ", "Santhal rebellion|চাঁওতাল বিদ্ৰোহ", "Salt March|লৱণ যাত্ৰা", "Revolt of 1857|১৮৫৭ৰ বিদ্ৰোহ"], 1, "The Santhal rebellion.|চাঁওতাল বিদ্ৰোহ।"),
 MA([("Indigo Revolt|নীল বিদ্ৰোহ", "1859|১৮৫৯"), ("Santhal rebellion|চাঁওতাল বিদ্ৰোহ", "1855|১৮৫৫"), ("Phulaguri|ফুলগুৰি", "1861|১৮৬১")], "Rising and year.|বিদ্ৰোহ আৰু বছৰ।"),
 TF("Nil Darpan's author was Munshi Premchand.|নীলদৰ্পণৰ লেখক মুন্সী প্ৰেমচান্দ।", False, "It was Dinabandhu Mitra.|দীনবন্ধু মিত্ৰ।"),
 OR("Put in chronological order.|কালানুক্ৰমে সজোৱা।", ["Macaulay's Minute|মেকলেৰ টোকা", "Wood's Despatch|উডৰ ডেচপেচ", "Raleigh Commission|ৰেলে কমিচন", "Sadler Commission|চেডলাৰ কমিচন"], "1835, 1854, 1902, 1917.|১৮৩৫, ১৮৫৪, ১৯০২, ১৯১৭।"),
 MP("Tap Nadia.|নদীয়া টিপা।", "nadia", ["nadia", "delhi", "bombay", "jhansi"], "In Bengal.|বংগত।"),
 MC("Consider these statements on Nil Darpan. (1) It was written in 1860. (2) Its author is Dinabandhu Mitra. (3) It portrays peasants oppressed by indigo planters. Which are correct?|নীলদৰ্পণৰ এই উক্তিবোৰ বিবেচনা কৰা। (১) ১৮৬০ত লিখা। (২) লেখক দীনবন্ধু মিত্ৰ। (৩) নীলকৰে অত্যাচাৰ কৰা খেতিয়কৰ চিত্ৰ। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 3, "All three.|তিনিওটা।"),
)
LESSON(22, "Indigo, press and schools|নীল, প্ৰেছ আৰু বিদ্যালয়", "1835–1919|১৮৩৫–১৯১৯", "Company rule|কোম্পানীৰ শাসন", "Evidence file 22|প্ৰমাণ নথি ২২", "Fields and classrooms|পথাৰ আৰু শ্ৰেণীকোঠা",
 "Peasants fought planters while officials rewrote the schools. Learn the risings, the play and the APSC education chain.|খেতিয়কে নীলকৰৰ সৈতে যুঁজিছিল, বিষয়াই বিদ্যালয় সলাইছিল। বিদ্ৰোহ, নাটক আৰু APSCৰ শিক্ষা শৃংখল শিকা।",
 sources, [u1, u2, u3], test, ["nadia", "delhi", "bombay", "jhansi"],
 timeline=[("1854", "Wood's Despatch|উডৰ ডেচপেচ", "u3"), ("1859", "Indigo Revolt begins|নীল বিদ্ৰোহ আৰম্ভ", "u1"), ("1860", "Nil Darpan|নীলদৰ্পণ", "u2")])
