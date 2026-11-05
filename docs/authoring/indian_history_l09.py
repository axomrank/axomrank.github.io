#!/usr/bin/env python3
"""Lesson 9: Cholas, Deccan and Kashmir."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "kanchipuram": ("place", "Kanchipuram|কাঞ্চীপুৰম", "Pallava capital in Tamil Nadu|তামিলনাডুত পল্লৱ ৰাজধানী", [12.84, 79.70]),
 "mamallapuram": ("place", "Mamallapuram|মামল্লপুৰম", "Pallava port town with rock-cut temples|শিল কাটি নিৰ্মিত মন্দিৰ থকা পল্লৱ বন্দৰ", [12.62, 80.19]),
 "vatapi": ("place", "Vatapi (Badami)|বাতাপি (বাদামী)", "Chalukya capital in Karnataka|কৰ্ণাটকত চালুক্য ৰাজধানী", [15.92, 75.68]),
 "thanjavur": ("place", "Thanjavur|তঞ্জাৱুৰ", "Chola city with the Brihadisvara temple|বৃহদীশ্বৰ মন্দিৰ থকা চোল নগৰ", [10.78, 79.13]),
 "rajaraja-i": ("person", "Rajaraja I|ৰাজৰাজ প্ৰথম", "Chola king, 985 to 1014|চোল ৰজা, ৯৮৫ৰ পৰা ১০১৪"),
 "rajendra-i": ("person", "Rajendra I|ৰাজেন্দ্ৰ প্ৰথম", "Chola king who sent naval raids to Srivijaya in 1025|১০২৫ত শ্ৰীবিজয়লৈ নৌ অভিযান পঠোৱা চোল ৰজা"),
 "lalitaditya": ("person", "Lalitaditya Muktapida|ললিতাদিত্য মুক্তাপীড়", "Karkota king of Kashmir, about 724 to 760|কাৰ্কোট বংশৰ কাশ্মীৰৰ ৰজা, প্ৰায় ৭২৪–৭৬০"),
 "kalhana": ("person", "Kalhana|কলহণ", "12th-century Kashmiri author of the Rajatarangini|ৰাজতৰংগিণীৰ দ্বাদশ শতিকাৰ কাশ্মীৰী লেখক"),
 "rajatarangini": ("term", "Rajatarangini|ৰাজতৰংগিণী", "Kalhana's Sanskrit chronicle of the kings of Kashmir|কাশ্মীৰৰ ৰজাসকলৰ বিষয়ে কলহণৰ সংস্কৃত ইতিবৃত্ত"),
 "kashmir": ("place", "Kashmir|কাশ্মীৰ", "Valley in the far north|উত্তৰৰ উপত্যকা", [34.08, 74.8]),
})
sources = [
 src("Wikipedia, Pallava dynasty", "https://en.wikipedia.org/wiki/Pallava_dynasty", "Used as a guide: Kanchipuram, Mahendravarman, Mamallapuram, Shore Temple, Chalukya wars, 897. Check in review."),
 src("Wikipedia, Chola dynasty", "https://en.wikipedia.org/wiki/Chola_dynasty", "Used as a guide: Rajaraja I, Rajendra I, Thanjavur, 1025 raids on Srivijaya, Gangaikonda Cholapuram. Check in review."),
 src("Wikipedia, Lalitaditya Muktapida", "https://en.wikipedia.org/wiki/Lalitaditya_Muktapida", "Used as a guide: Karkota, dates, the doubted conquests, Martand. Check in review."),
 src("Wikipedia, Rajatarangini", "https://en.wikipedia.org/wiki/Rajatarangini", "Used as a guide: Kalhana, 12th century, Sanskrit, Stein 1900. Stein's volume 2 is in Indian history sources; volume 1, with Lalitaditya, was not available. Check in review."),
]
u1 = U(1, "houses", "Pallavas and Chalukyas|পল্লৱ আৰু চালুক্য",
 "Set the two rival powers of the south.|দক্ষিণৰ দুই প্ৰতিদ্বন্দ্বী শক্তি স্থাপন কৰা।", "Finding recorded: Kanchipuram against Vatapi.|প্ৰমাণ লিখা হ'ল: কাঞ্চীপুৰম বনাম বাতাপি।",
 ["The Pallava capital was Kanchipuram|পল্লৱ ৰাজধানী কাঞ্চীপুৰম", "Mamallapuram has rock-cut rathas and the Shore Temple|মামল্লপুৰমত শিল কটা ৰথ আৰু সাগৰতীৰৰ মন্দিৰ", "The Chalukyas ruled from Vatapi|চালুক্যই বাতাপিৰ পৰা শাসন কৰিছিল", "The two powers fought repeatedly|দুয়ো শক্তিৰ বাৰে বাৰে যুদ্ধ হৈছিল"],
 S("Temples cut from rock|শিল কাটি নিৰ্মিত মন্দিৰ", "The <mark>Pallavas</mark> ruled from [[kanchipuram]]. At [[mamallapuram]] they cut temples from single rocks, the <mark>rathas</mark>.|<mark>পল্লৱসকলে</mark> [[kanchipuram|কাঞ্চীপুৰমৰ]] পৰা শাসন কৰিছিল। [[mamallapuram|মামল্লপুৰমত]] তেওঁলোকে একোটা শিল কাটি মন্দিৰ বনাইছিল, <mark>ৰথ</mark>।", "Narasimhavarman II built the Shore Temple there.|নৰসিংহবৰ্মন দ্বিতীয়ে তাত সাগৰতীৰৰ মন্দিৰ বনাইছিল।", map={"base": "india", "box": [72, 9, 84, 17.5], "show": ["kanchipuram", "vatapi", "thanjavur"]}),
 S("Rivals to the north|উত্তৰৰ প্ৰতিদ্বন্দ্বী", "The <mark>Chalukyas</mark> of [[vatapi|Vatapi]] fought the Pallavas again and again. You met one of them, Pulakeshin II, stopping Harsha.|[[vatapi|বাতাপিৰ]] <mark>চালুক্যই</mark> পল্লৱৰ সৈতে বাৰে বাৰে যুঁজিছিল। তেওঁলোকৰ এজন, দ্বিতীয় পুলকেশী, হৰ্ষক ৰোধ কৰিছিল।", art="court"),
 MA([("Pallavas|পল্লৱ", "Kanchipuram|কাঞ্চীপুৰম"), ("Chalukyas|চালুক্য", "Vatapi|বাতাপি"), ("Cholas|চোল", "Thanjavur|তঞ্জাৱুৰ")], "Dynasty and centre.|বংশ আৰু কেন্দ্ৰ।"),
 MP("Tap Kanchipuram.|কাঞ্চীপুৰম টিপা।", "kanchipuram", ["kanchipuram", "vatapi", "kashmir", "pataliputra"], "It is in Tamil Nadu.|ই তামিলনাডুত।"),
 TF("Mamallapuram's rathas are Pallava work.|মামল্লপুৰমৰ ৰথ পল্লৱৰ কাম।", True, "They are cut from single rocks.|এইবোৰ একোটা শিলৰ পৰা কটা।"),
 SP("The Pallava capital was *Vatapi.*|পল্লৱ ৰাজধানী *বাতাপি।*", "Kanchipuram|কাঞ্চীপুৰম", "Vatapi was the Chalukya capital.|বাতাপি চালুক্য ৰাজধানী।"),
 IN("Pulakeshin II belonged to the|দ্বিতীয় পুলকেশী আছিল", " dynasty.|বংশৰ।", ["Pallava|পল্লৱ", "Chalukya|চালুক্য", "Chola|চোল", "Gupta|গুপ্ত"], 1, "Chalukya.|চালুক্য।"),
)
u2 = U(2, "river", "Cholas across the sea|সাগৰ পাৰ হোৱা চোল",
 "See how far Chola power reached.|চোল শক্তি কিমান দূৰলৈ গৈছিল, চোৱা।", "Finding recorded: Rajendra I's fleet raided Srivijaya in 1025.|প্ৰমাণ লিখা হ'ল: ১০২৫ত ৰাজেন্দ্ৰ প্ৰথমৰ নৌবাহিনীয়ে শ্ৰীবিজয় আক্ৰমণ কৰিছিল।",
 ["The Chola heartland was the Kaveri valley|চোলৰ কেন্দ্ৰভূমি কাবেৰী উপত্যকা", "Rajaraja I ruled from 985 to 1014|ৰাজৰাজ প্ৰথমে ৯৮৫ৰ পৰা ১০১৪লৈ শাসন কৰিছিল", "The Brihadisvara temple is at Thanjavur|বৃহদীশ্বৰ মন্দিৰ তঞ্জাৱুৰত", "Rajendra I raided Srivijaya in 1025|১০২৫ত ৰাজেন্দ্ৰ প্ৰথমে শ্ৰীবিজয় আক্ৰমণ কৰিছিল"],
 S("The temple at Thanjavur|তঞ্জাৱুৰৰ মন্দিৰ", "The Cholas grew from the <mark>Kaveri</mark> valley. [[rajaraja-i|Rajaraja I]] built the great Brihadisvara temple at [[thanjavur]].|চোলসকল <mark>কাবেৰী</mark> উপত্যকাৰ পৰা বাঢ়িছিল। [[rajaraja-i|ৰাজৰাজ প্ৰথমে]] [[thanjavur|তঞ্জাৱুৰত]] বৃহদীশ্বৰ মন্দিৰ বনাইছিল।", art="houses"),
 S("A fleet to Southeast Asia|দক্ষিণ-পূব এছিয়ালৈ নৌবহৰ", "[[rajendra-i|Rajendra I]] sent naval raids against the ports of <mark>Srivijaya</mark> in 1025. Papers ask this as the kingdom whose reach extended to Southeast Asia.|[[rajendra-i|ৰাজেন্দ্ৰ প্ৰথমে]] ১০২৫ত <mark>শ্ৰীবিজয়ৰ</mark> বন্দৰলৈ নৌ অভিযান পঠাইছিল। দক্ষিণ-পূব এছিয়ালৈ প্ৰভাৱ বিস্তাৰ কৰা ৰাজ্য হিচাপে পৰীক্ষাত ইয়াক সোধা হয়।", "He also founded a new capital, Gangaikonda Cholapuram, after reaching the Ganga.|গংগা পোৱাৰ পিছত তেওঁ গংগাইকোণ্ড চোলপুৰম নতুন ৰাজধানী গঢ়িছিল।", art="embassy"),
 IN("The kingdom whose influence extended to Southeast Asia was the|দক্ষিণ-পূব এছিয়ালৈ প্ৰভাৱ বিস্তাৰ কৰা ৰাজ্য", ".|।", ["Chauhan|চৌহান", "Rajput|ৰাজপুত", "Gupta|গুপ্ত", "Chola|চোল"], 3, "The Cholas.|চোল।"),
 WH(["I was a Chola king.|মই চোল ৰজা।", "My fleet raided Srivijaya.|মোৰ নৌবহৰে শ্ৰীবিজয় আক্ৰমণ কৰিছিল।", "I founded Gangaikonda Cholapuram.|মই গংগাইকোণ্ড চোলপুৰম গঢ়িছিলোঁ।"], ["Rajaraja I|ৰাজৰাজ প্ৰথম", "Rajendra I|ৰাজেন্দ্ৰ প্ৰথম", "Mahendravarman I|মহেন্দ্ৰবৰ্মন প্ৰথম", "Pulakeshin II|দ্বিতীয় পুলকেশী"], 1, "Rajendra I.|ৰাজেন্দ্ৰ প্ৰথম।"),
 MP("Tap Thanjavur.|তঞ্জাৱুৰ টিপা।", "thanjavur", ["thanjavur", "vatapi", "kashmir", "pataliputra"], "In the Kaveri valley.|কাবেৰী উপত্যকাত।"),
 OR("Order the Chola kings.|চোল ৰজাসকলক সজোৱা।", ["Rajaraja I|ৰাজৰাজ প্ৰথম", "Rajendra I|ৰাজেন্দ্ৰ প্ৰথম"], "Father, then son.|পিতৃ, তাৰ পিছত পুত্ৰ।"),
 TF("The Brihadisvara temple is at Mamallapuram.|বৃহদীশ্বৰ মন্দিৰ মামল্লপুৰমত।", False, "It is at Thanjavur.|ই তঞ্জাৱুৰত।"),
)
u3 = U(3, "scroll", "Kashmir's chronicler|কাশ্মীৰৰ ইতিহাসকাৰ",
 "Weigh a king's fame against his chronicler.|ৰজাৰ খ্যাতি আৰু ইতিবৃত্ত তুলনা কৰা।", "Finding recorded: Lalitaditya ruled Kashmir; Kalhana's account of his conquests is doubted.|প্ৰমাণ লিখা হ'ল: ললিতাদিত্যই কাশ্মীৰ শাসন কৰিছিল; কলহণৰ জয়ৰ বিৱৰণ সন্দেহজনক।",
 ["Kalhana wrote the Rajatarangini|কলহণে ৰাজতৰংগিণী লিখিছিল", "It is a 12th-century Sanskrit chronicle|ই দ্বাদশ শতিকাৰ সংস্কৃত ইতিবৃত্ত", "Lalitaditya ruled the Kashmir region|ললিতাদিত্যই কাশ্মীৰ অঞ্চল শাসন কৰিছিল", "Historians doubt most of his claimed conquests|ইতিহাসবিদে তেওঁৰ বেছিভাগ জয়ত সন্দেহ কৰে"],
 S("A history of kings|ৰজাৰ ইতিহাস", "[[kalhana|Kalhana]] wrote the <mark>[[rajatarangini|Rajatarangini]]</mark> in 12th-century Kashmir, a Sanskrit chronicle of its kings.|[[kalhana|কলহণে]] দ্বাদশ শতিকাৰ কাশ্মীৰত <mark>[[rajatarangini|ৰাজতৰংগিণী]]</mark> লিখিছিল, ৰজাসকলৰ সংস্কৃত ইতিবৃত্ত।", art="scroll"),
 S("The world conqueror?|বিশ্ববিজয়ী?", "Kalhana calls [[lalitaditya|Lalitaditya]], of the Karkota line, a world conqueror. He wrote about four centuries later.|কলহণে কাৰ্কোট বংশৰ [[lalitaditya|ললিতাদিত্যক]] বিশ্ববিজয়ী বোলে। তেওঁ প্ৰায় চাৰি শতিকা পিছত লিখিছিল।", "Other records support little of this. Lalitaditya's empire in papers means the <mark>Kashmir region</mark>. He built the Martand Sun Temple.|আন নথিয়ে ইয়াৰ কমেই সমৰ্থন কৰে। পৰীক্ষাত ললিতাদিত্যৰ সাম্ৰাজ্য মানে <mark>কাশ্মীৰ অঞ্চল</mark>। তেওঁ মাৰ্তণ্ড সূৰ্য মন্দিৰ বনাইছিল।", art="seal"),
 IN("Rajatarangini was written by|ৰাজতৰংগিণী লিখিছিল", ".|এ।", ["Bilhana|বিলহণ", "Kalhana|কলহণ", "Kalidasa|কালিদাস", "Banabhatta|বাণভট্ট"], 1, "Kalhana.|কলহণ।"),
 MP("Tap the region of Lalitaditya's empire.|ললিতাদিত্যৰ সাম্ৰাজ্যৰ অঞ্চল টিপা।", "kashmir", ["kashmir", "vatapi", "thanjavur", "pataliputra"], "Kashmir.|কাশ্মীৰ।"),
 TF("Kalhana was a contemporary of Lalitaditya.|কলহণ ললিতাদিত্যৰ সমসাময়িক আছিল।", False, "He wrote about four centuries later.|তেওঁ প্ৰায় চাৰি শতিকা পিছত লিখিছিল।"),
 SC("Unscramble the author of the Rajatarangini.|ৰাজতৰংগিণীৰ লেখকক সজোৱা।", "KALHANA", ["ক", "ল", "হ", "ণ"], "Kalhana.|কলহণ।"),
 OD("Which work is NOT a history or life of a ruler?|কোনখন শাসকৰ ইতিহাস বা জীৱনী নহয়?", ["Rajatarangini|ৰাজতৰংগিণী", "Harshacharita|হৰ্ষচৰিত", "Allahabad praise|এলাহাবাদ প্ৰশস্তি", "Meghaduta|মেঘদূত"], 3, "The Meghaduta is Kalidasa's poem.|মেঘদূত কালিদাসৰ কাব্য।"),
)
test = TEST("Place the powers beyond the Ganga.|গংগাৰ বাহিৰৰ শক্তিবোৰ স্থাপন কৰা।", "Recorded: Pallavas, Chalukyas, Cholas and Kashmir.|লিখা হ'ল: পল্লৱ, চালুক্য, চোল আৰু কাশ্মীৰ।",
 IN("Rajatarangini was written by|ৰাজতৰংগিণী লিখিছিল", ".|এ।", ["Kalhana|কলহণ", "Kalidasa|কালিদাস", "Bana|বাণ", "Harisena|হৰিষেণ"], 0, "Kalhana.|কলহণ।"),
 MP("Tap the Chola temple city.|চোল মন্দিৰ নগৰখন টিপা।", "thanjavur", ["thanjavur", "kashmir", "vatapi", "pataliputra"], "Thanjavur.|তঞ্জাৱুৰ।"),
 TF("Lalitaditya's empire lay in the Kashmir region.|ললিতাদিত্যৰ সাম্ৰাজ্য কাশ্মীৰ অঞ্চলত আছিল।", True, "He was a Karkota king.|তেওঁ কাৰ্কোট ৰজা।"),
 MA([("Rajendra I|ৰাজেন্দ্ৰ প্ৰথম", "Srivijaya raids|শ্ৰীবিজয় অভিযান"), ("Narasimhavarman II|নৰসিংহবৰ্মন দ্বিতীয়", "Shore Temple|সাগৰতীৰৰ মন্দিৰ"), ("Rajaraja I|ৰাজৰাজ প্ৰথম", "Brihadisvara temple|বৃহদীশ্বৰ মন্দিৰ")], "King and work.|ৰজা আৰু কাম।"),
 SP("Chola power reached *Central* Asia by sea.|চোল শক্তি সাগৰেৰে *মধ্য* এছিয়া পাইছিল।", "Southeast|দক্ষিণ-পূব", "It reached Southeast Asia.|ই দক্ষিণ-পূব এছিয়া পাইছিল।"),
 MC("Consider these statements. (1) Kanchipuram was the Pallava capital. (2) Kalhana wrote in the 12th century. (3) Rajendra I built the Shore Temple. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) কাঞ্চীপুৰম পল্লৱ ৰাজধানী। (২) কলহণে দ্বাদশ শতিকাত লিখিছিল। (৩) ৰাজেন্দ্ৰ প্ৰথমে সাগৰতীৰৰ মন্দিৰ বনাইছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 0, "The Shore Temple is Pallava.|সাগৰতীৰৰ মন্দিৰ পল্লৱৰ।"),
)
LESSON(9, "Cholas, Deccan and Kashmir|চোল, দাক্ষিণাত্য আৰু কাশ্মীৰ", "6th–13th c.|ষষ্ঠ–ত্ৰয়োদশ শতিকা", "South, Kashmir and learning|দক্ষিণ, কাশ্মীৰ আৰু জ্ঞানচৰ্চা", "Evidence file 9|প্ৰমাণ নথি ৯", "Beyond the Ganga|গংগাৰ সিপাৰে",
 "Indian history was never only the Ganga plain. Follow rock temples, a fleet to Southeast Asia and a chronicle of Kashmir.|ভাৰতৰ ইতিহাস কেৱল গংগা সমভূমি নহয়। শিলৰ মন্দিৰ, দক্ষিণ-পূব এছিয়ালৈ নৌবহৰ আৰু কাশ্মীৰৰ ইতিবৃত্ত অনুসৰণ কৰা।",
 sources, [u1, u2, u3], test, ["kanchipuram", "vatapi", "thanjavur", "kashmir", "pataliputra"])
