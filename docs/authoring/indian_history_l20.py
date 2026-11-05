#!/usr/bin/env python3
"""Lesson 20: Reformers."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "ram-mohan-roy": ("person", "Ram Mohan Roy|ৰামমোহন ৰায়", "Reformer who founded the Brahmo Samaj in 1828|১৮২৮ত ব্ৰাহ্ম সমাজ প্ৰতিষ্ঠা কৰা সংস্কাৰক"),
 "vidyasagar": ("person", "Ishwar Chandra Vidyasagar|ঈশ্বৰচন্দ্ৰ বিদ্যাসাগৰ", "Main campaigner for widow remarriage|বিধৱা বিবাহৰ মূল প্ৰচাৰক"),
 "dayananda-saraswati": ("person", "Dayananda Saraswati|দয়ানন্দ সৰস্বতী", "Founder of the Arya Samaj in 1875|১৮৭৫ত আৰ্য সমাজৰ প্ৰতিষ্ঠাপক"),
 "vivekananda": ("person", "Swami Vivekananda|স্বামী বিবেকানন্দ", "Born Narendranath Datta; spoke at Chicago in 1893|নৰেন্দ্ৰনাথ দত্ত নামে জন্ম; ১৮৯৩ত চিকাগোত বক্তৃতা"),
 "ramakrishna": ("person", "Ramakrishna|ৰামকৃষ্ণ", "Mystic and guru of Vivekananda|ৰহস্যবাদী, বিবেকানন্দৰ গুৰু"),
})
sources = [
 src("Wikipedia, Brahmo Samaj", "https://en.wikipedia.org/wiki/Brahmo_Samaj", "Used as a guide: 20 August 1828, Calcutta, beliefs. The article lacks inline citations. Check in review."),
 src("Wikipedia, Hindu Widows' Remarriage Act, 1856", "https://en.wikipedia.org/wiki/Hindu_Widows%27_Remarriage_Act,_1856", "Used as a guide: Act XV of 1856, Vidyasagar. Check in review."),
 src("Wikipedia, Arya Samaj", "https://en.wikipedia.org/wiki/Arya_Samaj", "Used as a guide: Dayananda, Bombay, 1875, Vedas. Check in review."),
 src("Wikipedia, Swami Vivekananda", "https://en.wikipedia.org/wiki/Swami_Vivekananda", "Used as a guide: Narendranath Datta, Chicago 1893, Ramakrishna Mission 1897. Check in review."),
]
u1 = U(1, "seal", "Bengal's reformers|বংগৰ সংস্কাৰক",
 "Match Bengal's reformers to their causes.|বংগৰ সংস্কাৰকক তেওঁলোকৰ কামৰ সৈতে মিলোৱা।", "Finding recorded: Roy's Brahmo Samaj and Vidyasagar's widow remarriage.|প্ৰমাণ লিখা হ'ল: ৰায়ৰ ব্ৰাহ্ম সমাজ আৰু বিদ্যাসাগৰৰ বিধৱা বিবাহ।",
 ["Ram Mohan Roy founded the Brahmo Samaj in 1828|১৮২৮ত ৰামমোহন ৰায়ে ব্ৰাহ্ম সমাজ প্ৰতিষ্ঠা কৰিছিল", "It opposed idol worship and caste|ই মূৰ্তিপূজা আৰু জাতিভেদৰ বিৰোধিতা কৰিছিল", "Vidyasagar campaigned for widow remarriage|বিদ্যাসাগৰে বিধৱা বিবাহৰ বাবে অভিযান চলাইছিল", "The Widow Remarriage Act came in 1856|১৮৫৬ত বিধৱা বিবাহ আইন আহিছিল"],
 S("The Brahmo Samaj|ব্ৰাহ্ম সমাজ", "[[ram-mohan-roy|Ram Mohan Roy]] started the <mark>Brahmo Samaj</mark> in Calcutta in <mark>1828</mark>. It opposed idol worship, caste and sati.|[[ram-mohan-roy|ৰামমোহন ৰায়ে]] <mark>১৮২৮ত</mark> কলিকতাত <mark>ব্ৰাহ্ম সমাজ</mark> আৰম্ভ কৰিছিল। ই মূৰ্তিপূজা, জাতিভেদ আৰু সতীদাহৰ বিৰোধিতা কৰিছিল।", art="houses"),
 S("A law for widows|বিধৱাৰ বাবে আইন", "[[vidyasagar|Ishwar Chandra Vidyasagar]] led the campaign for widow remarriage. The Act passed in <mark>1856</mark>, despite a much larger counter-petition.|[[vidyasagar|ঈশ্বৰচন্দ্ৰ বিদ্যাসাগৰে]] বিধৱা বিবাহৰ অভিযান চলাইছিল। বহু ডাঙৰ বিৰোধী আবেদন সত্ত্বেও <mark>১৮৫৬ত</mark> আইন গৃহীত হৈছিল।", art="scroll"),
 MA([("Ram Mohan Roy|ৰামমোহন ৰায়", "Brahmo Samaj|ব্ৰাহ্ম সমাজ"), ("Vidyasagar|বিদ্যাসাগৰ", "Widow remarriage|বিধৱা বিবাহ"), ("Dayananda Saraswati|দয়ানন্দ সৰস্বতী", "Arya Samaj|আৰ্য সমাজ")], "Reformer and cause.|সংস্কাৰক আৰু কাম।"),
 IN("The Brahmo Samaj began in|ব্ৰাহ্ম সমাজ আৰম্ভ হৈছিল", ".|ত।", ["1828|১৮২৮", "1857|১৮৫৭", "1875|১৮৭৫", "1897|১৮৯৭"], 0, "1828.|১৮২৮।"),
 TF("Vidyasagar opposed widow remarriage.|বিদ্যাসাগৰে বিধৱা বিবাহৰ বিৰোধিতা কৰিছিল।", False, "He was its leading campaigner.|তেওঁ ইয়াৰ মূল প্ৰচাৰক আছিল।"),
 WH(["I worked in Calcutta.|মই কলিকতাত কাম কৰিছিলোঁ।", "I campaigned against sati.|মই সতীদাহৰ বিৰুদ্ধে অভিযান চলাইছিলোঁ।", "I began the Brahmo Samaj.|মই ব্ৰাহ্ম সমাজ আৰম্ভ কৰিছিলোঁ।"], ["Ram Mohan Roy|ৰামমোহন ৰায়", "Vivekananda|বিবেকানন্দ", "Vidyasagar|বিদ্যাসাগৰ", "Dayananda Saraswati|দয়ানন্দ সৰস্বতী"], 0, "Ram Mohan Roy.|ৰামমোহন ৰায়।"),
 SP("The Brahmo Samaj began in *Bombay.*|ব্ৰাহ্ম সমাজ *বোম্বেত* আৰম্ভ হৈছিল।", "Calcutta|কলিকতাত", "Calcutta.|কলিকতা।"),
)
u2 = U(2, "star", "Back to the Vedas|বেদলৈ ঘূৰি",
 "Place the Arya Samaj.|আৰ্য সমাজ স্থাপন কৰা।", "Finding recorded: Dayananda Saraswati, Bombay, 1875.|প্ৰমাণ লিখা হ'ল: দয়ানন্দ সৰস্বতী, বোম্বে, ১৮৭৫।",
 ["Dayananda Saraswati founded the Arya Samaj|দয়ানন্দ সৰস্বতীয়ে আৰ্য সমাজ প্ৰতিষ্ঠা কৰিছিল", "It began at Bombay in 1875|১৮৭৫ত বোম্বেত আৰম্ভ হৈছিল", "It treated the Vedas as infallible|ই বেদক অভ্ৰান্ত বুলি ধৰিছিল", "It rejected idol worship|ই মূৰ্তিপূজা অস্বীকাৰ কৰিছিল"],
 S("A return to the Vedas|বেদলৈ প্ৰত্যাৱৰ্তন", "[[dayananda-saraswati|Dayananda Saraswati]] founded the <mark>Arya Samaj</mark> at [[bombay]] in <mark>1875</mark>. It treated the Vedas as infallible.|[[dayananda-saraswati|দয়ানন্দ সৰস্বতীয়ে]] <mark>১৮৭৫ত</mark> [[bombay|বোম্বেত]] <mark>আৰ্য সমাজ</mark> প্ৰতিষ্ঠা কৰিছিল। ই বেদক অভ্ৰান্ত বুলি ধৰিছিল।", art="scroll"),
 S("Schools and reform|বিদ্যালয় আৰু সংস্কাৰ", "It rejected idol worship, ran schools, and campaigned against caste discrimination and for women's education. Lala Lajpat Rai was among its nationalists.|ই মূৰ্তিপূজা অস্বীকাৰ কৰিছিল, বিদ্যালয় চলাইছিল, জাতিভেদৰ বিৰুদ্ধে আৰু নাৰী শিক্ষাৰ বাবে অভিযান চলাইছিল। লালা লাজপত ৰায় ইয়াৰ জাতীয়তাবাদীসকলৰ এজন।", art="houses"),
 IN("The Arya Samaj was founded by|আৰ্য সমাজ প্ৰতিষ্ঠা কৰিছিল", ".|এ।", ["Keshub Chandra Sen|কেশৱচন্দ্ৰ সেন", "Dayananda Saraswati|দয়ানন্দ সৰস্বতী", "Ramakrishna|ৰামকৃষ্ণ", "Ram Mohan Roy|ৰামমোহন ৰায়"], 1, "Dayananda Saraswati.|দয়ানন্দ সৰস্বতী।"),
 TF("The Arya Samaj treated the Vedas as its authority.|আৰ্য সমাজে বেদক কৰ্তৃত্ব বুলি ধৰিছিল।", True, "It regarded them as infallible.|ই সেইবোৰক অভ্ৰান্ত বুলি ধৰিছিল।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Brahmo Samaj|ব্ৰাহ্ম সমাজ", "Arya Samaj|আৰ্য সমাজ", "Ramakrishna Mission|ৰামকৃষ্ণ মিছন"], "1828, 1875, 1897.|১৮২৮, ১৮৭৫, ১৮৯৭।"),
 SP("The Arya Samaj began at Bombay in *1975.*|আৰ্য সমাজ *১৯৭৫ত* বোম্বেত আৰম্ভ হৈছিল।", "1875|১৮৭৫ত", "1875.|১৮৭৫।"),
 OD("Which belongs to the Arya Samaj's programme?|কোনটো আৰ্য সমাজৰ কাৰ্যসূচীৰ?", ["Idol worship|মূৰ্তিপূজা", "Sati|সতীদাহ", "Women's education|নাৰী শিক্ষা", "Caste rank|জাতিৰ স্থান"], 2, "It campaigned for women's education.|ই নাৰী শিক্ষাৰ বাবে অভিযান চলাইছিল।"),
)
u3 = U(3, "walk", "Chicago, 1893|চিকাগো, ১৮৯৩",
 "Fix Vivekananda's name and mission.|বিবেকানন্দৰ নাম আৰু মিছন মনত ৰাখা।", "Finding recorded: Narendranath Datta, Chicago 1893, Mission 1897.|প্ৰমাণ লিখা হ'ল: নৰেন্দ্ৰনাথ দত্ত, ১৮৯৩ত চিকাগো, ১৮৯৭ত মিছন।",
 ["Vivekananda was born Narendranath Datta|বিবেকানন্দৰ জন্মনাম নৰেন্দ্ৰনাথ দত্ত", "His guru was Ramakrishna|তেওঁৰ গুৰু ৰামকৃষ্ণ", "He spoke at Chicago in 1893|১৮৯৩ত তেওঁ চিকাগোত বক্তৃতা দিছিল", "He founded the Ramakrishna Mission in 1897|১৮৯৭ত তেওঁ ৰামকৃষ্ণ মিছন গঢ়িছিল"],
 S("A student from Calcutta|কলিকতাৰ এজন ছাত্ৰ", "[[vivekananda|Swami Vivekananda]] was born <mark>Narendranath Datta</mark> in 1863. The mystic [[ramakrishna|Ramakrishna]] became his guru.|[[vivekananda|স্বামী বিবেকানন্দৰ]] জন্মনাম <mark>নৰেন্দ্ৰনাথ দত্ত</mark>, ১৮৬৩ত জন্ম। ৰহস্যবাদী [[ramakrishna|ৰামকৃষ্ণ]] তেওঁৰ গুৰু।", art="door"),
 LINK(S("A voice in Chicago|চিকাগোত এটা মাত", "In <mark>1893</mark> he spoke at the Parliament of the World's Religions in Chicago. On 1 May <mark>1897</mark> he founded the Ramakrishna Mission.|<mark>১৮৯৩ত</mark> তেওঁ চিকাগোৰ বিশ্ব ধৰ্ম মহাসভাত বক্তৃতা দিছিল। <mark>১৮৯৭ৰ</mark> ১ মে'ত ৰামকৃষ্ণ মিছন গঢ়িছিল।", "Assam had its own awakening too, with Anandaram Dhekial Phukan.|অসমতো নিজা জাগৰণ আছিল, আনন্দৰাম ঢেকিয়াল ফুকনৰ সৈতে।", art="embassy"),
  "british-09", 46, 4, "A language returns|ভাষাৰ প্ৰত্যাৱৰ্তন", "The Assam History course tells Assam's awakening.|অসমৰ ইতিহাস পাঠ্যক্ৰমত অসমৰ জাগৰণৰ কথা আছে।"),
 IN("The original name of Swami Vivekananda was|স্বামী বিবেকানন্দৰ মূল নাম", ".|।", ["Bankim Chandra Chattopadhyay|বংকিমচন্দ্ৰ চট্টোপাধ্যায়", "Narendranath Datta|নৰেন্দ্ৰনাথ দত্ত", "Chittaranjan Das|চিত্তৰঞ্জন দাস", "Rash Behari Bose|ৰাসবিহাৰী বসু"], 1, "Narendranath Datta.|নৰেন্দ্ৰনাথ দত্ত।"),
 TF("Vivekananda spoke at Chicago in 1893.|১৮৯৩ত বিবেকানন্দই চিকাগোত বক্তৃতা দিছিল।", True, "At the Parliament of the World's Religions.|বিশ্ব ধৰ্ম মহাসভাত।"),
 MA([("Chicago|চিকাগো", "1893|১৮৯৩"), ("Ramakrishna Mission|ৰামকৃষ্ণ মিছন", "1897|১৮৯৭"), ("Arya Samaj|আৰ্য সমাজ", "1875|১৮৭৫")], "Event and year.|ঘটনা আৰু বছৰ।"),
 WH(["I was a mystic.|মই ৰহস্যবাদী।", "Narendranath Datta was my disciple.|নৰেন্দ্ৰনাথ দত্ত মোৰ শিষ্য।"], ["Ramakrishna|ৰামকৃষ্ণ", "Dayananda Saraswati|দয়ানন্দ সৰস্বতী", "Ram Mohan Roy|ৰামমোহন ৰায়", "Kabir|কবীৰ"], 0, "Ramakrishna.|ৰামকৃষ্ণ।"),
 SC("Unscramble the city of 1893.|১৮৯৩ৰ চহৰখন সজোৱা।", "CHICAGO", ["চি", "কা", "গো"], "Chicago.|চিকাগো।"),
)
test = TEST("Sort the reformers.|সংস্কাৰকসকলক পৃথক কৰা।", "Recorded: Brahmo, Arya, Vidyasagar and Vivekananda.|লিখা হ'ল: ব্ৰাহ্ম, আৰ্য, বিদ্যাসাগৰ আৰু বিবেকানন্দ।",
 MA([("Ram Mohan Roy|ৰামমোহন ৰায়", "Brahmo Samaj|ব্ৰাহ্ম সমাজ"), ("Dayananda Saraswati|দয়ানন্দ সৰস্বতী", "Arya Samaj|আৰ্য সমাজ"), ("Vivekananda|বিবেকানন্দ", "Ramakrishna Mission|ৰামকৃষ্ণ মিছন")], "Founder and body.|প্ৰতিষ্ঠাপক আৰু সংগঠন।"),
 IN("Vivekananda's birth name was|বিবেকানন্দৰ জন্মনাম", ".|।", ["Narendranath Datta|নৰেন্দ্ৰনাথ দত্ত", "Chittaranjan Das|চিত্তৰঞ্জন দাস", "Rash Behari Bose|ৰাসবিহাৰী বসু", "Ishwar Chandra|ঈশ্বৰচন্দ্ৰ"], 0, "Narendranath Datta.|নৰেন্দ্ৰনাথ দত্ত।"),
 TF("The Widow Remarriage Act passed in 1856.|১৮৫৬ত বিধৱা বিবাহ আইন গৃহীত হৈছিল।", True, "Vidyasagar led the campaign.|বিদ্যাসাগৰে অভিযান চলাইছিল।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Brahmo Samaj|ব্ৰাহ্ম সমাজ", "Widow Remarriage Act|বিধৱা বিবাহ আইন", "Arya Samaj|আৰ্য সমাজ", "Chicago speech|চিকাগো বক্তৃতা"], "1828, 1856, 1875, 1893.|১৮২৮, ১৮৫৬, ১৮৭৫, ১৮৯৩।"),
 SP("*Vidyasagar* founded the Arya Samaj.|*বিদ্যাসাগৰে* আৰ্য সমাজ গঢ়িছিল।", "Dayananda|দয়ানন্দই", "Dayananda Saraswati founded it. Vidyasagar's cause was widow remarriage.|দয়ানন্দ সৰস্বতীয়ে গঢ়িছিল। বিদ্যাসাগৰৰ কাম বিধৱা বিবাহ।"),
 MC("Consider these statements. (1) The Arya Samaj began at Bombay. (2) Ramakrishna founded the Brahmo Samaj. (3) Vivekananda founded the Ramakrishna Mission. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) আৰ্য সমাজ বোম্বেত আৰম্ভ হৈছিল। (২) ৰামকৃষ্ণই ব্ৰাহ্ম সমাজ গঢ়িছিল। (৩) বিবেকানন্দই ৰামকৃষ্ণ মিছন গঢ়িছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Ram Mohan Roy founded the Brahmo Samaj.|ৰামমোহন ৰায়ে ব্ৰাহ্ম সমাজ গঢ়িছিল।"),
)
LESSON(20, "Reformers|সমাজ সংস্কাৰক", "1828–1897|১৮২৮–১৮৯৭", "Company rule|কোম্পানীৰ শাসন", "Evidence file 20|প্ৰমাণ নথি ২০", "Change from within|ভিতৰৰ পৰা পৰিৱৰ্তন",
 "While officials wrote laws, reformers argued over sati, widows, scripture and caste. Match each to their cause.|বিষয়াই আইন লিখোঁতে সংস্কাৰকে সতীদাহ, বিধৱা, শাস্ত্ৰ আৰু জাতিভেদৰ বিতৰ্ক কৰিছিল। প্ৰত্যেকক তেওঁৰ কামৰ সৈতে মিলোৱা।",
 sources, [u1, u2, u3], test, [],
 timeline=[("1828", "Brahmo Samaj|ব্ৰাহ্ম সমাজ", "u1"), ("1875", "Arya Samaj|আৰ্য সমাজ", "u2"), ("1893", "Vivekananda at Chicago|চিকাগোত বিবেকানন্দ", "u3")])
