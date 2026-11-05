#!/usr/bin/env python3
"""Lesson 13: Bhakti, Sufis and Sikh Gurus."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "kabir": ("person", "Kabir|কবীৰ", "Devotional poet who rejected outward religious forms|বাহ্যিক ধৰ্মীয় ৰূপ অস্বীকাৰ কৰা ভক্ত কবি"),
 "guru-nanak": ("person", "Guru Nanak|গুৰু নানক", "Founder of Sikhism|শিখ ধৰ্মৰ প্ৰৱৰ্তক"),
 "guru-tegh-bahadur": ("person", "Guru Tegh Bahadur|গুৰু তেগ বাহাদুৰ", "Ninth Sikh Guru, who visited Dhubri|নৱম শিখ গুৰু, ধুবুৰীলৈ আহিছিল"),
 "tulsidas": ("person", "Tulsidas|তুলসীদাস", "Author of the Ramcharitmanas|ৰামচৰিতমানসৰ লেখক"),
 "moinuddin-chishti": ("person", "Moinuddin Chishti|মইনুদ্দিন চিশ্তী", "Chishti Sufi saint of Ajmer|আজমীৰৰ চিশ্তী চুফী সন্ত"),
 "nizamuddin-auliya": ("person", "Nizamuddin Auliya|নিজামুদ্দিন আউলিয়া", "Chishti Sufi saint of Delhi|দিল্লীৰ চিশ্তী চুফী সন্ত"),
 "ajmer": ("place", "Ajmer|আজমীৰ", "City in Rajasthan with the Chishti shrine|চিশ্তী দৰগাহ থকা ৰাজস্থানৰ নগৰ", [26.45, 74.64]),
 "dhubri": ("place", "Dhubri|ধুবুৰী", "Town on the Brahmaputra in Assam|অসমৰ ব্ৰহ্মপুত্ৰ পাৰৰ নগৰ", [26.02, 89.98]),
 "patna": ("place", "Patna|পাটনা", "Capital of Bihar|বিহাৰৰ ৰাজধানী", [25.59, 85.14]),
})
sources = [
 src("Wikipedia, Bhakti movement", "https://en.wikipedia.org/wiki/Bhakti_movement", "Used as a guide: Alvars and Nayanars, spread north, Kabir, Nanak, Mirabai, Tulsidas, Sankardev. Check in review."),
 src("Wikipedia, Guru Tegh Bahadur", "https://en.wikipedia.org/wiki/Guru_Tegh_Bahadur", "Used as a guide: ninth Guru, Dhubri, 1666, 1675, the Dhubri gurdwara. The peace story is from Sikh accounts. Check in review."),
 src("Wikipedia, Chishti Order", "https://en.wikipedia.org/wiki/Chishti_Order", "Used as a guide: Moinuddin at Ajmer, Nizamuddin at Delhi. Check in review."),
]
u1 = U(1, "star", "Devotion from the south|দক্ষিণৰ পৰা ভক্তি",
 "Trace how bhakti spread.|ভক্তি কেনেকৈ বিয়পিল, অনুসৰণ কৰা।", "Finding recorded: Tamil saints first, then regional languages across India.|প্ৰমাণ লিখা হ'ল: প্ৰথমে তামিল সন্ত, তাৰ পিছত সমগ্ৰ ভাৰতৰ আঞ্চলিক ভাষা।",
 ["Bhakti began with Tamil Alvars and Nayanars|ভক্তি তামিল আলবাৰ আৰু নায়নাৰৰ পৰা আৰম্ভ", "Alvars were Vaishnava, Nayanars Shaiva|আলবাৰ বৈষ্ণৱ, নায়নাৰ শৈৱ", "It spread north using local languages|স্থানীয় ভাষাৰে ই উত্তৰলৈ বিয়পিল", "It peaked in the 15th to 17th centuries|পঞ্চদশৰ পৰা সপ্তদশ শতিকাত ই শীৰ্ষত আছিল"],
 S("Hymns in Tamil|তামিল স্তোত্ৰ", "Bhakti, devotion to a personal god, began in the Tamil lands. The <mark>Alvars</mark> sang for Vishnu, the <mark>Nayanars</mark> for Shiva.|ব্যক্তিগত ঈশ্বৰৰ প্ৰতি ভক্তি তামিল ভূমিত আৰম্ভ হৈছিল। <mark>আলবাৰে</mark> বিষ্ণুৰ, <mark>নায়নাৰে</mark> শিৱৰ গীত গাইছিল।", art="scroll"),
 S("Everyday languages|দৈনন্দিন ভাষা", "It moved north through Karnataka and reached Odisha, Bengal, Assam and the north, at its height in the <mark>15th to 17th centuries</mark>.|ই কৰ্ণাটকৰ বাটে উত্তৰলৈ গ'ল, ওড়িশা, বংগ, অসম আৰু উত্তৰ ভাৰত পালে, <mark>পঞ্চদশৰ পৰা সপ্তদশ শতিকাত</mark> শীৰ্ষত।", "Its poets used local languages, so ordinary people could understand.|ইয়াৰ কবিসকলে স্থানীয় ভাষা ব্যৱহাৰ কৰিছিল, যাতে সাধাৰণ মানুহে বুজে।", art="houses"),
 MA([("Alvars|আলবাৰ", "Vishnu|বিষ্ণু"), ("Nayanars|নায়নাৰ", "Shiva|শিৱ")], "Tamil saints and their gods.|তামিল সন্ত আৰু তেওঁলোকৰ দেৱতা।"),
 TF("Bhakti began in the Tamil lands.|ভক্তি তামিল ভূমিত আৰম্ভ হৈছিল।", True, "With the Alvars and Nayanars.|আলবাৰ আৰু নায়নাৰৰ পৰা।"),
 IN("Bhakti poets mainly used|ভক্তি কবিসকলে মূলতঃ ব্যৱহাৰ কৰিছিল", ".|।", ["Greek|গ্ৰীক", "local languages|স্থানীয় ভাষা", "Persian only|কেৱল ফাৰ্চী", "Sanskrit only|কেৱল সংস্কৃত"], 1, "Local languages reached ordinary people.|স্থানীয় ভাষাই সাধাৰণ মানুহক পাইছিল।"),
 SP("Nayanars were devotees of *Vishnu.*|নায়নাৰ *বিষ্ণুৰ* ভক্ত।", "Shiva|শিৱৰ", "Alvars were Vaishnava.|আলবাৰ বৈষ্ণৱ।"),
 OR("Trace bhakti's path.|ভক্তিৰ পথ অনুসৰণ কৰা।", ["Tamil lands|তামিল ভূমি", "Karnataka|কৰ্ণাটক", "Northern India and Assam|উত্তৰ ভাৰত আৰু অসম"], "South to north.|দক্ষিণৰ পৰা উত্তৰলৈ।"),
)
u2 = U(2, "scroll", "Poets of the north|উত্তৰৰ কবি",
 "Match the poets and their works.|কবি আৰু ৰচনা মিলোৱা।", "Finding recorded: Kabir, Nanak, Tulsidas and Sankardev.|প্ৰমাণ লিখা হ'ল: কবীৰ, নানক, তুলসীদাস আৰু শংকৰদেৱ।",
 ["Kabir rejected outward religious forms|কবীৰে বাহ্যিক ধৰ্মীয় ৰূপ অস্বীকাৰ কৰিছিল", "Guru Nanak founded Sikhism|গুৰু নানকে শিখ ধৰ্ম প্ৰৱৰ্তন কৰিছিল", "Tulsidas wrote the Ramcharitmanas|তুলসীদাসে ৰামচৰিতমানস লিখিছিল", "Sankardev carried bhakti into Assam|শংকৰদেৱে অসমত ভক্তি বিয়পাইছিল"],
 S("Beyond ritual|আচাৰৰ বাহিৰত", "[[kabir|Kabir]] favoured inner experience over outward forms. [[guru-nanak|Guru Nanak]] <mark>founded Sikhism</mark>, drawing on both Hindu and Islamic traditions.|[[kabir|কবীৰে]] বাহ্যিক ৰূপতকৈ অন্তৰৰ অনুভৱক গুৰুত্ব দিছিল। [[guru-nanak|গুৰু নানকে]] <mark>শিখ ধৰ্ম প্ৰৱৰ্তন কৰিছিল</mark>।", art="door"),
 LINK(S("Hindi and Assamese|হিন্দী আৰু অসমীয়া", "[[tulsidas|Tulsidas]] wrote the <mark>Ramcharitmanas</mark>, not Kabir or Veda Vyas.|[[tulsidas|তুলসীদাসে]] <mark>ৰামচৰিতমানস</mark> লিখিছিল, কবীৰ বা বেদব্যাসে নহয়।", "In Assam, [[sankardev|Sankardev]] used a language people could follow, and developed Brajavali.|অসমত [[sankardev|শংকৰদেৱে]] মানুহে বুজা ভাষা ব্যৱহাৰ কৰিছিল, ব্ৰজাৱলী গঢ়িছিল।", art="scroll"),
  "assam-culture-01", 67, 3, "One refuge, four anchors|এক শৰণ, চাৰি আধাৰ", "The Assam History course teaches Sankardev in full.|অসমৰ ইতিহাস পাঠ্যক্ৰমত শংকৰদেৱক সম্পূৰ্ণকৈ শিকোৱা হৈছে।"),
 IN("The Ramcharitmanas was written by|ৰামচৰিতমানস লিখিছিল", ".|এ।", ["Kabir|কবীৰ", "Veda Vyas|বেদব্যাস", "Adi Shankaracharya|আদি শংকৰাচাৰ্য", "Tulsidas|তুলসীদাস"], 3, "Tulsidas.|তুলসীদাস।"),
 MA([("Guru Nanak|গুৰু নানক", "Sikhism|শিখ ধৰ্ম"), ("Tulsidas|তুলসীদাস", "Ramcharitmanas|ৰামচৰিতমানস"), ("Sankardev|শংকৰদেৱ", "Assam|অসম")], "Teacher and legacy.|শিক্ষক আৰু উত্তৰাধিকাৰ।"),
 TF("Kabir stressed outward ritual.|কবীৰে বাহ্যিক আচাৰত গুৰুত্ব দিছিল।", False, "He stressed inner experience.|তেওঁ অন্তৰৰ অনুভৱত গুৰুত্ব দিছিল।"),
 WH(["I founded Sikhism.|মই শিখ ধৰ্ম প্ৰৱৰ্তন কৰিছিলোঁ।", "I drew on Hindu and Islamic traditions.|মই হিন্দু আৰু ইছলামী পৰম্পৰাৰ পৰা লৈছিলোঁ।"], ["Kabir|কবীৰ", "Guru Nanak|গুৰু নানক", "Tulsidas|তুলসীদাস", "Mirabai|মীৰাবাই"], 1, "Guru Nanak.|গুৰু নানক।"),
 SC("Unscramble the author of the Ramcharitmanas.|ৰামচৰিতমানসৰ লেখকক সজোৱা।", "TULSIDAS", ["তুল", "সী", "দাস"], "Tulsidas.|তুলসীদাস।"),
)
u3 = U(3, "walk", "Sufis and a Guru at Dhubri|চুফী আৰু ধুবুৰীত গুৰু",
 "Connect the Sufis and the Sikh Gurus to the wider story.|চুফী আৰু শিখ গুৰুক বহল কাহিনীৰ সৈতে জোৰা লগোৱা।", "Finding recorded: Chishti saints at Ajmer and Delhi; Guru Tegh Bahadur at Dhubri.|প্ৰমাণ লিখা হ'ল: আজমীৰ আৰু দিল্লীত চিশ্তী সন্ত; ধুবুৰীত গুৰু তেগ বাহাদুৰ।",
 ["Moinuddin Chishti's shrine is at Ajmer|মইনুদ্দিন চিশ্তীৰ দৰগাহ আজমীৰত", "Nizamuddin Auliya's tomb is in Delhi|নিজামুদ্দিন আউলিয়াৰ সমাধি দিল্লীত", "Guru Tegh Bahadur was the ninth Guru|গুৰু তেগ বাহাদুৰ নৱম গুৰু", "A gurdwara at Dhubri marks his visit|ধুবুৰীৰ গুৰুদ্বাৰাই তেওঁৰ আগমন চিহ্নিত কৰে"],
 S("Shrines of the Chishtis|চিশ্তীৰ দৰগাহ", "The Chishti Sufi order took root in India. [[moinuddin-chishti|Moinuddin Chishti]] lies at <mark>[[ajmer|Ajmer]]</mark>, [[nizamuddin-auliya|Nizamuddin Auliya]] at Delhi.|চিশ্তী চুফী ধাৰা ভাৰতত শিপাইছিল। [[moinuddin-chishti|মইনুদ্দিন চিশ্তীৰ]] সমাধি <mark>[[ajmer|আজমীৰত]]</mark>, [[nizamuddin-auliya|নিজামুদ্দিন আউলিয়াৰ]] দিল্লীত।", art="houses"),
 S("A Guru at Dhubri|ধুবুৰীত গুৰু", "[[guru-tegh-bahadur|Guru Tegh Bahadur]], the <mark>ninth</mark> Sikh Guru, travelled to Assam. He was at [[dhubri]] in 1666, and a gurdwara there marks the visit.|নৱম শিখ গুৰু [[guru-tegh-bahadur|তেগ বাহাদুৰ]] অসমলৈ আহিছিল। ১৬৬৬ত তেওঁ [[dhubri|ধুবুৰীত]] আছিল, তাৰ গুৰুদ্বাৰাই এই আগমন চিহ্নিত কৰে।", "Aurangzeb ordered his execution at Delhi in 1675.|১৬৭৫ত ঔৰংগজেবে দিল্লীত তেওঁৰ প্ৰাণদণ্ডৰ আদেশ দিছিল।", map={"base": "india", "box": [76, 22, 92, 31], "show": ["dhubri", "patna", "delhi"]}),
 IN("The Gurudwara at Dhubri is linked with|ধুবুৰীৰ গুৰুদ্বাৰা জড়িত", ".|ৰ সৈতে।", ["Guru Nanak|গুৰু নানক", "Guru Tegh Bahadur|গুৰু তেগ বাহাদুৰ", "Guru Angad|গুৰু অংগদ", "Guru Arjan|গুৰু অৰ্জুন"], 1, "Guru Tegh Bahadur.|গুৰু তেগ বাহাদুৰ।"),
 MP("Tap Dhubri.|ধুবুৰী টিপা।", "dhubri", ["dhubri", "ajmer", "delhi", "patna"], "On the Brahmaputra in western Assam.|পশ্চিম অসমৰ ব্ৰহ্মপুত্ৰ পাৰত।"),
 MA([("Moinuddin Chishti|মইনুদ্দিন চিশ্তী", "Ajmer|আজমীৰ"), ("Nizamuddin Auliya|নিজামুদ্দিন আউলিয়া", "Delhi|দিল্লী"), ("Guru Tegh Bahadur|গুৰু তেগ বাহাদুৰ", "Dhubri|ধুবুৰী")], "Name and place.|নাম আৰু ঠাই।"),
 TF("Guru Tegh Bahadur was the first Sikh Guru.|গুৰু তেগ বাহাদুৰ প্ৰথম শিখ গুৰু।", False, "He was the ninth.|তেওঁ নৱম।"),
 SP("Moinuddin Chishti's shrine is at *Delhi.*|মইনুদ্দিন চিশ্তীৰ দৰগাহ *দিল্লীত।*", "Ajmer|আজমীৰত", "It is at Ajmer.|ই আজমীৰত।"),
)
test = TEST("Trace devotion across India.|সমগ্ৰ ভাৰতত ভক্তি অনুসৰণ কৰা।", "Recorded: bhakti, Sufis and the Gurus.|লিখা হ'ল: ভক্তি, চুফী আৰু গুৰু।",
 IN("The Ramcharitmanas was written by|ৰামচৰিতমানস লিখিছিল", ".|এ।", ["Kabir|কবীৰ", "Tulsidas|তুলসীদাস", "Veda Vyas|বেদব্যাস", "Adi Shankaracharya|আদি শংকৰাচাৰ্য"], 1, "Tulsidas.|তুলসীদাস।"),
 IN("The Gurudwara at Dhubri is linked with|ধুবুৰীৰ গুৰুদ্বাৰা জড়িত", ".|ৰ সৈতে।", ["Guru Nanak|গুৰু নানক", "Guru Angad|গুৰু অংগদ", "Guru Tegh Bahadur|গুৰু তেগ বাহাদুৰ", "Guru Arjan|গুৰু অৰ্জুন"], 2, "Guru Tegh Bahadur.|গুৰু তেগ বাহাদুৰ।"),
 MP("Tap Ajmer.|আজমীৰ টিপা।", "ajmer", ["ajmer", "dhubri", "delhi", "patna"], "In Rajasthan.|ৰাজস্থানত।"),
 TF("Alvars and Nayanars began bhakti in the Tamil lands.|আলবাৰ আৰু নায়নাৰে তামিল ভূমিত ভক্তি আৰম্ভ কৰিছিল।", True, "Yes.|হয়।"),
 MA([("Kabir|কবীৰ", "Inner experience|অন্তৰৰ অনুভৱ"), ("Guru Nanak|গুৰু নানক", "Sikhism|শিখ ধৰ্ম"), ("Sankardev|শংকৰদেৱ", "Brajavali|ব্ৰজাৱলী")], "Teacher and mark.|শিক্ষক আৰু চিনাকি।"),
 MC("Consider these statements. (1) Bhakti used local languages. (2) Nizamuddin Auliya's tomb is at Ajmer. (3) Sankardev took part in the bhakti movement. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ভক্তিত স্থানীয় ভাষা ব্যৱহাৰ হৈছিল। (২) নিজামুদ্দিন আউলিয়াৰ সমাধি আজমীৰত। (৩) শংকৰদেৱ ভক্তি আন্দোলনৰ অংশ। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "His tomb is in Delhi.|তেওঁৰ সমাধি দিল্লীত।"),
)
LESSON(13, "Bhakti, Sufis and Sikh Gurus|ভক্তি, চুফী আৰু শিখ গুৰু", "Medieval India|মধ্যযুগীয় ভাৰত", "Sultans, Deccan and devotion|ছুলতান, দাক্ষিণাত্য আৰু ভক্তি", "Evidence file 13|প্ৰমাণ নথি ১৩", "Songs across a continent|উপমহাদেশ জোৰা গীত",
 "While kings fought, devotion moved in everyday languages from the Tamil lands to Assam. Follow the songs.|ৰজাই যুঁজোঁতে দৈনন্দিন ভাষাৰে ভক্তি তামিল ভূমিৰ পৰা অসমলৈ আহিছিল। গীত অনুসৰণ কৰা।",
 sources, [u1, u2, u3], test, ["dhubri", "ajmer", "delhi", "patna"])
