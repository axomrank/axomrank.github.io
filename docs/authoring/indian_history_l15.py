#!/usr/bin/env python3
"""Lesson 15: Akbar."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "akbar": ("person", "Akbar|আকবৰ", "Mughal emperor, 1556 to 1605|মোগল সম্ৰাট, ১৫৫৬ৰ পৰা ১৬০৫"),
 "hemu": ("person", "Hemu|হেমু", "Commander who fought Akbar's forces at Panipat in 1556|১৫৫৬ত পানিপথত আকবৰৰ সৈন্যৰ সৈতে যুঁজা সেনাপতি"),
 "bairam-khan": ("person", "Bairam Khan|বৈৰাম খান", "Guardian of the young Akbar|ডেকা আকবৰৰ অভিভাৱক"),
 "abul-fazl": ("person", "Abu'l Fazl|আবুল ফজল", "Akbar's minister and historian|আকবৰৰ মন্ত্ৰী আৰু ইতিহাসকাৰ"),
 "din-i-ilahi": ("term", "Din-i-Ilahi|দীন-ই-ইলাহী", "Akbar's syncretic creed|আকবৰৰ সমন্বয়ী মত"),
 "mansabdari": ("term", "Mansabdari|মনচবদাৰী", "Mughal system of ranks for officers|বিষয়াৰ পদমৰ্যাদাৰ মোগল ব্যৱস্থা"),
 "john-mildenhall": ("person", "John Mildenhall|জন মিলডেনহল", "English traveller who reached Akbar's court in 1603|১৬০৩ত আকবৰৰ সভা পোৱা ইংৰাজ পৰ্যটক"),
 "fatehpur-sikri": ("place", "Fatehpur Sikri|ফতেহপুৰ চিক্ৰী", "Akbar's walled capital near Agra|আগ্ৰাৰ ওচৰৰ আকবৰৰ দেৱালে ঘেৰা ৰাজধানী", [27.09, 77.66]),
 "agra": ("place", "Agra|আগ্ৰা", "Mughal city on the Yamuna|যমুনা পাৰৰ মোগল নগৰ", [27.18, 78.01]),
 "lahore": ("place", "Lahore|লাহোৰ", "City in today's Pakistan|আজিৰ পাকিস্তানৰ নগৰ", [31.55, 74.34]),
})
sources = [
 src("Wikipedia, Second Battle of Panipat", "https://en.wikipedia.org/wiki/Second_Battle_of_Panipat", "Used as a guide: 5 November 1556, Bairam Khan, Hemu. Check in review."),
 src("Wikipedia, Akbar", "https://en.wikipedia.org/wiki/Akbar", "Used as a guide: reign, Din-i-Ilahi, mansabdari, jizya abolished, Fatehpur Sikri. The part on the Akbarnama was not read. Check in review."),
 src("Wikipedia, John Mildenhall", "https://en.wikipedia.org/wiki/John_Mildenhall", "Used as a guide: 1603, self-styled ambassador, never recognised by the Company. Check in review."),
 src("Ain-i-Akbari, translated by Blochmann and Jarrett", "https://archive.org/details/in.ernet.dli.2015.484850", "Located, not read. Check mansabdari against it in review."),
]
u1 = U(1, "flag", "Panipat, 1556|পানিপথ, ১৫৫৬",
 "Fix the second battle of Panipat.|পানিপথৰ দ্বিতীয় যুদ্ধ মনত ৰাখা।", "Finding recorded: 5 November 1556, Akbar's side against Hemu.|প্ৰমাণ লিখা হ'ল: ১৫৫৬ৰ ৫ নৱেম্বৰ, আকবৰৰ পক্ষ বনাম হেমু।",
 ["The Second Battle of Panipat was in 1556|পানিপথৰ দ্বিতীয় যুদ্ধ ১৫৫৬ত", "Akbar's side fought Hemu|আকবৰৰ পক্ষই হেমুৰ সৈতে যুঁজিছিল", "Bairam Khan was Akbar's guardian|বৈৰাম খান আকবৰৰ অভিভাৱক", "An arrow struck Hemu and his army fled|কাঁড়ে হেমুক আঘাত কৰিলে, সৈন্য পলাল"],
 S("The second Panipat|দ্বিতীয় পানিপথ", "On <mark>5 November 1556</mark> Mughal forces met [[hemu|Hemu]], who had taken Delhi and Agra. Akbar was 13, and [[bairam-khan|Bairam Khan]] was his guardian.|<mark>১৫৫৬ৰ ৫ নৱেম্বৰত</mark> মোগল সৈন্যই দিল্লী আৰু আগ্ৰা লোৱা [[hemu|হেমুৰ]] সন্মুখীন হৈছিল। আকবৰ ১৩ বছৰীয়া, [[bairam-khan|বৈৰাম খান]] অভিভাৱক।", art="embassy"),
 S("An arrow turns a battle|কাঁড়ে সলোৱা যুদ্ধ", "Hemu led from an elephant. An arrow struck his eye, and his army panicked. The Mughals recovered Delhi and Agra.|হেমুৱে হাতীৰ পৰা নেতৃত্ব দিছিল। কাঁড় তেওঁৰ চকুত লাগিল, সৈন্য ত্ৰস্ত হ'ল। মোগলে দিল্লী আৰু আগ্ৰা পুনৰ পালে।", "Remember three Panipats: <b>1526, 1556, 1761</b>.|তিনিটা পানিপথ মনত ৰাখা: <b>১৫২৬, ১৫৫৬, ১৭৬১</b>।", art="calendar"),
 IN("The Second Battle of Panipat was in|পানিপথৰ দ্বিতীয় যুদ্ধ হৈছিল", ".|ত।", ["1526|১৫২৬", "1536|১৫৩৬", "1556|১৫৫৬", "1576|১৫৭৬"], 2, "1556.|১৫৫৬।"),
 MA([("1526|১৫২৬", "Babur beats Ibrahim Lodi|বাবৰে ইব্ৰাহিম লোদীক হৰুৱায়"), ("1556|১৫৫৬", "Mughals beat Hemu|মোগলে হেমুক হৰুৱায়"), ("1761|১৭৬১", "Durrani beats Marathas|দুৰানীয়ে মাৰাঠাক হৰুৱায়")], "The three Panipats.|তিনিটা পানিপথ।"),
 TF("Bairam Khan was Akbar's guardian.|বৈৰাম খান আকবৰৰ অভিভাৱক আছিল।", True, "Akbar was only 13.|আকবৰৰ বয়স মাত্ৰ ১৩ আছিল।"),
 WH(["I had taken Delhi and Agra.|মই দিল্লী আৰু আগ্ৰা লৈছিলোঁ।", "I fought from an elephant.|মই হাতীৰ পৰা যুঁজিছিলোঁ।", "An arrow struck my eye.|কাঁড় মোৰ চকুত লাগিছিল।"], ["Hemu|হেমু", "Rana Sanga|ৰাণা সংগ", "Ibrahim Lodi|ইব্ৰাহিম লোদী", "Porus|পুৰু"], 0, "Hemu.|হেমু।"),
 SP("Hemu fought at the Second Battle of *Khanwa.*|হেমুৱে *খানুৱাৰ* দ্বিতীয় যুদ্ধত যুঁজিছিল।", "Panipat|পানিপথৰ", "It was Panipat.|ই পানিপথ।"),
)
u2 = U(2, "star", "Ranks for an empire|সাম্ৰাজ্যৰ পদমৰ্যাদা",
 "Learn how Akbar organised officers and taxes.|আকবৰে বিষয়া আৰু কৰ কেনেকৈ সজাইছিল, শিকা।", "Finding recorded: mansabdari ranks, and the jizya abolished.|প্ৰমাণ লিখা হ'ল: মনচবদাৰী পদ, আৰু জিজিয়া বিলোপ।",
 ["Akbar ruled from 1556 to 1605|আকবৰে ১৫৫৬ৰ পৰা ১৬০৫লৈ শাসন কৰিছিল", "Mansabdari gave each officer a rank|মনচবদাৰীয়ে প্ৰতিজন বিষয়াক পদ দিছিল", "Each rank supplied a set number of cavalry|প্ৰতিটো পদে নিৰ্দিষ্ট অশ্বাৰোহী যোগান ধৰিছিল", "Akbar abolished the jizya|আকবৰে জিজিয়া বিলোপ কৰিছিল"],
 S("A number for every officer|প্ৰতিজন বিষয়াৰ এটা সংখ্যা", "Under <mark>[[mansabdari|mansabdari]]</mark> each officer held a rank and supplied a set number of cavalry.|<mark>[[mansabdari|মনচবদাৰীত]]</mark> প্ৰতিজন বিষয়াৰ এটা পদ আছিল আৰু নিৰ্দিষ্ট অশ্বাৰোহী যোগান ধৰিব লাগিছিল।", art="court"),
 S("The tax removed|কৰ বিলোপ", "[[akbar|Akbar]] abolished the <mark>jizya</mark>, the tax on non-Muslims. It is one reason historians speak of his policy of tolerance.|[[akbar|আকবৰে]] অমুছলমানৰ ওপৰত থকা কৰ <mark>জিজিয়া</mark> বিলোপ কৰিছিল। ইতিহাসবিদে তেওঁৰ সহনশীলতাৰ নীতিৰ কথা কোৱাৰ এইটো এটা কাৰণ।", "He founded <mark>[[fatehpur-sikri|Fatehpur Sikri]]</mark> as a walled capital in 1569.|১৫৬৯ত তেওঁ দেৱালে ঘেৰা ৰাজধানী হিচাপে <mark>[[fatehpur-sikri|ফতেহপুৰ চিক্ৰী]]</mark> গঢ়িছিল।", art="houses"),
 IN("Akbar's system of ranks was|আকবৰৰ পদমৰ্যাদাৰ ব্যৱস্থা আছিল", ".|।", ["paik|পাইক", "mansabdari|মনচবদাৰী", "iqta|ইক্তা", "ryotwari|ৰায়তৱাৰী"], 1, "Mansabdari.|মনচবদাৰী।"),
 TF("Akbar introduced the jizya.|আকবৰে জিজিয়া প্ৰৱৰ্তন কৰিছিল।", False, "He abolished it.|তেওঁ ইয়াক বিলোপ কৰিছিল।"),
 MP("Tap Fatehpur Sikri's region, Agra.|ফতেহপুৰ চিক্ৰীৰ অঞ্চল আগ্ৰা টিপা।", "agra", ["agra", "surat", "lahore", "kashmir"], "Fatehpur Sikri is near Agra.|ফতেহপুৰ চিক্ৰী আগ্ৰাৰ ওচৰত।"),
 SC("Unscramble Akbar's rank system.|আকবৰৰ পদ ব্যৱস্থাটো সজোৱা।", "MANSABDARI", ["মন", "চব", "দা", "ৰী"], "Mansabdari.|মনচবদাৰী।"),
 SP("Fatehpur Sikri was founded by *Babur.*|ফতেহপুৰ চিক্ৰী *বাবৰে* গঢ়িছিল।", "Akbar|আকবৰে", "Akbar founded it in 1569.|১৫৬৯ত আকবৰে গঢ়িছিল।"),
)
u3 = U(3, "star", "One creed, few followers|এক মত, অলপ অনুগামী",
 "Pin down what Din-i-Ilahi was.|দীন-ই-ইলাহী কি আছিল, নিৰ্দিষ্ট কৰা।", "Finding recorded: Akbar's syncretic creed, drawing on several faiths.|প্ৰমাণ লিখা হ'ল: কেইবাটাও ধৰ্মৰ পৰা লোৱা আকবৰৰ সমন্বয়ী মত।",
 ["Akbar initiated Din-i-Ilahi|আকবৰে দীন-ই-ইলাহী আৰম্ভ কৰিছিল", "It was a syncretic creed|ই এক সমন্বয়ী মত", "It drew on Islam, Hinduism and others|ই ইছলাম, হিন্দু আৰু আন ধৰ্মৰ পৰা লৈছিল", "Abu'l Fazl was his minister and historian|আবুল ফজল তেওঁৰ মন্ত্ৰী আৰু ইতিহাসকাৰ"],
 S("A creed of the court|ৰাজসভাৰ মত", "Akbar's <mark>[[din-i-ilahi|Din-i-Ilahi]]</mark> drew mainly on Islam and Hinduism, with Zoroastrian and Christian elements.|আকবৰৰ <mark>[[din-i-ilahi|দীন-ই-ইলাহীয়ে]]</mark> মূলতঃ ইছলাম আৰু হিন্দু ধৰ্মৰ পৰা লৈছিল, জৰথুষ্ট্ৰীয় আৰু খ্ৰীষ্টীয় উপাদানো আছিল।", "Historians differ on how far to call it a religion. Papers simply ask who began it.|ইয়াক ধৰ্ম বুলি কিমান ক'ব পাৰি, ইতিহাসবিদৰ মতভেদ আছে। পৰীক্ষাত কেৱল কোনে আৰম্ভ কৰিছিল সোধে।", art="seal"),
 S("The emperor's historian|সম্ৰাটৰ ইতিহাসকাৰ", "[[abul-fazl|Abu'l Fazl]], his minister, wrote the <mark>Akbarnama</mark>, the Book of Akbar, and the Ain-i-Akbari.|তেওঁৰ মন্ত্ৰী [[abul-fazl|আবুল ফজলে]] <mark>আকবৰনামা</mark> আৰু আইন-ই-আকবৰী লিখিছিল।", "Like Bana and Harisena, he wrote for his king.|বাণ আৰু হৰিষেণৰ দৰে তেওঁ নিজৰ ৰজাৰ বাবে লিখিছিল।", art="scroll"),
 IN("Din-i-Ilahi was initiated by|দীন-ই-ইলাহী আৰম্ভ কৰিছিল", ".|এ।", ["Aurangzeb|ঔৰংগজেব", "Babur|বাবৰ", "Shah Jahan|শ্বাহজাহান", "Akbar|আকবৰ"], 3, "Akbar.|আকবৰ।"),
 MA([("Akbarnama|আকবৰনামা", "Abu'l Fazl|আবুল ফজল"), ("Harshacharita|হৰ্ষচৰিত", "Banabhatta|বাণভট্ট"), ("Rajatarangini|ৰাজতৰংগিণী", "Kalhana|কলহণ")], "Work and writer.|ৰচনা আৰু লেখক।"),
 TF("Din-i-Ilahi drew on more than one religion.|দীন-ই-ইলাহীয়ে এটাতকৈ অধিক ধৰ্মৰ পৰা লৈছিল।", True, "It was syncretic.|ই সমন্বয়ী আছিল।"),
 WH(["I was Akbar's minister.|মই আকবৰৰ মন্ত্ৰী।", "I wrote the Akbarnama.|মই আকবৰনামা লিখিছিলোঁ।"], ["Bairam Khan|বৈৰাম খান", "Abu'l Fazl|আবুল ফজল", "Banabhatta|বাণভট্ট", "Mir Jumla|মীৰজুমলা"], 1, "Abu'l Fazl.|আবুল ফজল।"),
 OD("Which is NOT linked with Akbar?|কোনটো আকবৰৰ সৈতে জড়িত নহয়?", ["Din-i-Ilahi|দীন-ই-ইলাহী", "Mansabdari|মনচবদাৰী", "Fatehpur Sikri|ফতেহপুৰ চিক্ৰী", "Taj Mahal|তাজমহল"], 3, "Shah Jahan built the Taj Mahal.|শ্বাহজাহানে তাজমহল বনাইছিল।"),
)
u4 = U(4, "walk", "An Englishman at court|ৰাজসভাত এজন ইংৰাজ",
 "Handle the Mildenhall question carefully.|মিলডেনহলৰ প্ৰশ্ন সাৱধানে চোৱা।", "Finding recorded: Mildenhall reached Akbar in 1603, but his standing was self-claimed.|প্ৰমাণ লিখা হ'ল: ১৬০৩ত মিলডেনহলে আকবৰক পাইছিল, কিন্তু তেওঁৰ মৰ্যাদা নিজেই দাবী কৰা।",
 ["John Mildenhall reached Akbar's court in 1603|১৬০৩ত জন মিলডেনহলে আকবৰৰ সভা পাইছিল", "He sought trade privileges|তেওঁ বাণিজ্যৰ সুবিধা বিচাৰিছিল", "The Company never recognised him|কোম্পানীয়ে তেওঁক কেতিয়াও স্বীকৃতি দিয়া নাছিল", "Roe came later, to Jahangir|ৰ' পিছত জাহাংগীৰৰ ওচৰলৈ আহিছিল"],
 S("A self-styled envoy|নিজেই ঘোষিত দূত", "<mark>[[john-mildenhall|John Mildenhall]]</mark> travelled overland and reached Akbar's court in <mark>1603</mark>, seeking trade privileges.|<mark>[[john-mildenhall|জন মিলডেনহলে]]</mark> স্থলপথেৰে আহি <mark>১৬০৩ত</mark> বাণিজ্য সুবিধা বিচাৰি আকবৰৰ সভা পাইছিল।", "One paper calls him Queen Elizabeth's ambassador. Sources call him self-styled, and the Company never recognised him.|এখন প্ৰশ্নকাকতত তেওঁক ৰাণী এলিজাবেথৰ দূত বোলা হৈছে। উৎসত তেওঁ নিজেই ঘোষিত, কোম্পানীয়ে স্বীকৃতি দিয়া নাছিল।", art="embassy"),
 S("Three names to separate|পৃথক কৰিবলগীয়া তিনিটা নাম", "Mildenhall came to <mark>Akbar</mark>. William Hawkins and Sir Thomas Roe came to <mark>Jahangir</mark>, and Roe won permission for a factory at Surat.|মিলডেনহল <mark>আকবৰৰ</mark> ওচৰলৈ আহিছিল। উইলিয়াম হকিন্স আৰু ছাৰ টমাছ ৰ' <mark>জাহাংগীৰৰ</mark> ওচৰলৈ, ৰ'য়ে চুৰাটত কুঠিৰ অনুমতি পাইছিল।", art="court"),
 IN("The Englishman who reached Akbar's court in 1603 was|১৬০৩ত আকবৰৰ সভা পোৱা ইংৰাজ", ".|।", ["Sir Thomas Roe|ছাৰ টমাছ ৰ'", "William Hawkins|উইলিয়াম হকিন্স", "John Mildenhall|জন মিলডেনহল", "Robert Clive|ৰবাৰ্ট ক্লাইভ"], 2, "Mildenhall.|মিলডেনহল।"),
 MA([("John Mildenhall|জন মিলডেনহল", "Akbar|আকবৰ"), ("Sir Thomas Roe|ছাৰ টমাছ ৰ'", "Jahangir|জাহাংগীৰ")], "Visitor and emperor.|অভ্যাগত আৰু সম্ৰাট।"),
 TF("The East India Company officially recognised Mildenhall.|ইষ্ট ইণ্ডিয়া কোম্পানীয়ে মিলডেনহলক আনুষ্ঠানিক স্বীকৃতি দিছিল।", False, "It never did.|কেতিয়াও দিয়া নাছিল।"),
 OR("Put the English visitors in order.|ইংৰাজ অভ্যাগতসকলক ক্ৰমে সজোৱা।", ["John Mildenhall|জন মিলডেনহল", "Sir Thomas Roe|ছাৰ টমাছ ৰ'"], "1603, then 1615.|১৬০৩, তাৰ পিছত ১৬১৫।"),
 SP("Mildenhall reached the court of *Aurangzeb.*|মিলডেনহলে *ঔৰংগজেবৰ* সভা পাইছিল।", "Akbar|আকবৰৰ", "He reached Akbar.|তেওঁ আকবৰক পাইছিল।"),
)
test = TEST("Sum up Akbar's reign.|আকবৰৰ ৰাজত্বৰ সাৰাংশ দিয়া।", "Recorded: Panipat, ranks, creed and visitors.|লিখা হ'ল: পানিপথ, পদ, মত আৰু অভ্যাগত।",
 IN("Din-i-Ilahi was initiated by|দীন-ই-ইলাহী আৰম্ভ কৰিছিল", ".|এ।", ["Aurangzeb|ঔৰংগজেব", "Akbar|আকবৰ", "Shah Jahan|শ্বাহজাহান", "Babur|বাবৰ"], 1, "Akbar.|আকবৰ।"),
 IN("The Second Battle of Panipat between Akbar's side and Hemu was in|আকবৰৰ পক্ষ আৰু হেমুৰ পানিপথৰ দ্বিতীয় যুদ্ধ", ".|ত।", ["1526|১৫২৬", "1536|১৫৩৬", "1556|১৫৫৬", "1576|১৫৭৬"], 2, "1556.|১৫৫৬।"),
 TF("Mansabdari gave officers ranks.|মনচবদাৰীয়ে বিষয়াক পদ দিছিল।", True, "Yes.|হয়।"),
 MA([("Akbarnama|আকবৰনামা", "Abu'l Fazl|আবুল ফজল"), ("Regent of young Akbar|ডেকা আকবৰৰ অভিভাৱক", "Bairam Khan|বৈৰাম খান"), ("1603 visitor|১৬০৩ৰ অভ্যাগত", "John Mildenhall|জন মিলডেনহল")], "Facts of the reign.|ৰাজত্বৰ তথ্য।"),
 MP("Tap Agra.|আগ্ৰা টিপা।", "agra", ["agra", "surat", "lahore", "kashmir"], "On the Yamuna.|যমুনা পাৰত।"),
 MC("Consider these statements. (1) Akbar abolished the jizya. (2) Akbar built the Taj Mahal. (3) Akbar founded Fatehpur Sikri. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) আকবৰে জিজিয়া বিলোপ কৰিছিল। (২) আকবৰে তাজমহল বনাইছিল। (৩) আকবৰে ফতেহপুৰ চিক্ৰী গঢ়িছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Shah Jahan built the Taj Mahal.|শ্বাহজাহানে তাজমহল বনাইছিল।"),
)
LESSON(15, "Akbar|আকবৰ", "1556–1605|১৫৫৬–১৬০৫", "The Mughal age|মোগল যুগ", "Evidence file 15|প্ৰমাণ নথি ১৫", "A boy on the throne|সিংহাসনত এজন বালক",
 "A 13-year-old inherited a shaky throne and left an empire with ranks, taxes and a creed of his own. Find out how.|১৩ বছৰীয়া বালকে অস্থিৰ সিংহাসন পালে আৰু পদ, কৰ আৰু নিজৰ মত থকা সাম্ৰাজ্য এৰি গ'ল। কেনেকৈ, উলিওৱা।",
 sources, [u1, u2, u3, u4], test, ["agra", "surat", "lahore", "kashmir"],
 timeline=[("1556", "Second Battle of Panipat|পানিপথৰ দ্বিতীয় যুদ্ধ", "u1"), ("1569", "Fatehpur Sikri founded|ফতেহপুৰ চিক্ৰী প্ৰতিষ্ঠা", "u2"), ("1603", "Mildenhall at court|সভাত মিলডেনহল", "u4")])
