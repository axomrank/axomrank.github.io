#!/usr/bin/env python3
"""Lesson 16: Jahangir to Aurangzeb."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "jahangir": ("person", "Jahangir|জাহাংগীৰ", "Mughal emperor, 1605 to 1627|মোগল সম্ৰাট, ১৬০৫ৰ পৰা ১৬২৭"),
 "shah-jahan": ("person", "Shah Jahan|শ্বাহজাহান", "Mughal emperor who built the Taj Mahal|তাজমহল নিৰ্মাণ কৰা মোগল সম্ৰাট"),
 "thomas-roe": ("person", "Sir Thomas Roe|ছাৰ টমাছ ৰ'", "English envoy to Jahangir from 1615|১৬১৫ৰ পৰা জাহাংগীৰৰ ওচৰত ইংৰাজ দূত"),
 "dara-shikoh": ("person", "Dara Shikoh|দাৰা চিকো", "Eldest son of Shah Jahan, defeated by Aurangzeb|শ্বাহজাহানৰ জ্যেষ্ঠ পুত্ৰ, ঔৰংগজেবে হৰুৱাইছিল"),
 "golconda": ("place", "Golconda|গোলকোণ্ডা", "Deccan fort near Hyderabad|হায়দৰাবাদৰ ওচৰৰ দাক্ষিণাত্যৰ দুৰ্গ", [17.38, 78.40]),
})
sources = [
 src("Wikipedia, Thomas Roe", "https://en.wikipedia.org/wiki/Thomas_Roe", "Used as a guide: embassy from 1615, Surat factory. Check in review."),
 src("Wikipedia, Taj Mahal", "https://en.wikipedia.org/wiki/Taj_Mahal", "Used as a guide: Shah Jahan, Mumtaz Mahal, Ustad Ahmad Lahori, 1632, 1648, 1653, UNESCO 1983. Check in review."),
 src("Wikipedia, Aurangzeb", "https://en.wikipedia.org/wiki/Aurangzeb", "Used as a guide: 1658 to 1707, succession, 1679 jizya, extent, the historians' debate. Check in review."),
 src("Wikipedia, Guru Tegh Bahadur", "https://en.wikipedia.org/wiki/Guru_Tegh_Bahadur", "Used as a guide: execution in 1675. Check in review."),
]
u1 = U(1, "walk", "Trade at the door|দুৱাৰমুখত বাণিজ্য",
 "See how the English got a foothold.|ইংৰাজে কেনেকৈ ভেটি পালে, চোৱা।", "Finding recorded: Roe won a factory at Surat from Jahangir.|প্ৰমাণ লিখা হ'ল: ৰ'য়ে জাহাংগীৰৰ পৰা চুৰাটত কুঠি পাইছিল।",
 ["Jahangir ruled from 1605 to 1627|জাহাংগীৰে ১৬০৫ৰ পৰা ১৬২৭লৈ শাসন কৰিছিল", "Sir Thomas Roe came as royal envoy in 1615|১৬১৫ত ছাৰ টমাছ ৰ' ৰাজকীয় দূত হিচাপে আহিছিল", "His mission won a factory at Surat|তেওঁৰ অভিযানে চুৰাটত কুঠি পাইছিল", "Jahangir gave no major trade privileges|জাহাংগীৰে ডাঙৰ বাণিজ্য সুবিধা দিয়া নাছিল"],
 S("An envoy from a king|ৰজাৰ দূত", "In <mark>1615</mark> <mark>[[thomas-roe|Sir Thomas Roe]]</mark> reached [[jahangir|Jahangir]] as the envoy of King James, sent at the East India Company's request.|<mark>১৬১৫ত</mark> ইষ্ট ইণ্ডিয়া কোম্পানীৰ অনুৰোধত ৰজা জেমছৰ দূত হিচাপে <mark>[[thomas-roe|ছাৰ টমাছ ৰ']]</mark> [[jahangir|জাহাংগীৰৰ]] ওচৰলৈ আহিছিল।", art="embassy"),
 S("A small win|সৰু জয়", "He won protection for a Company factory at <mark>[[surat]]</mark>. Jahangir gave no major privileges, yet this began a long relationship.|তেওঁ <mark>[[surat|চুৰাটত]]</mark> কোম্পানীৰ কুঠিৰ সুৰক্ষা পাইছিল। জাহাংগীৰে ডাঙৰ সুবিধা দিয়া নাছিল, তথাপি এক দীঘলীয়া সম্পৰ্ক আৰম্ভ হ'ল।", art="houses"),
 IN("Sir Thomas Roe came to the court of|ছাৰ টমাছ ৰ' আহিছিল", ".|ৰ সভালৈ।", ["Akbar|আকবৰ", "Jahangir|জাহাংগীৰ", "Shah Jahan|শ্বাহজাহান", "Aurangzeb|ঔৰংগজেব"], 1, "Jahangir.|জাহাংগীৰ।"),
 MP("Tap Surat.|চুৰাট টিপা।", "surat", ["surat", "agra", "golconda", "delhi"], "On the Gujarat coast.|গুজৰাটৰ উপকূলত।"),
 TF("Roe won sweeping trade rights from Jahangir.|ৰ'য়ে জাহাংগীৰৰ পৰা ব্যাপক বাণিজ্য অধিকাৰ পাইছিল।", False, "He won a factory at Surat, little more.|তেওঁ চুৰাটত কুঠি পাইছিল, তাতকৈ বেছি নহয়।"),
 OR("Order the emperors.|সম্ৰাটসকলক সজোৱা।", ["Akbar|আকবৰ", "Jahangir|জাহাংগীৰ", "Shah Jahan|শ্বাহজাহান", "Aurangzeb|ঔৰংগজেব"], "Father to son.|পিতৃৰ পৰা পুত্ৰলৈ।"),
 SP("Roe's mission won a factory at *Madras.*|ৰ'ৰ অভিযানে *মাদ্ৰাজত* কুঠি পাইছিল।", "Surat|চুৰাটত", "It was Surat.|ই চুৰাট।"),
)
u2 = U(2, "houses", "A tomb and a succession|এটা সমাধি আৰু উত্তৰাধিকাৰ",
 "Fix the Taj Mahal and the war of the sons.|তাজমহল আৰু পুত্ৰসকলৰ যুদ্ধ মনত ৰাখা।", "Finding recorded: Shah Jahan built the Taj; Aurangzeb took the throne in 1658.|প্ৰমাণ লিখা হ'ল: শ্বাহজাহানে তাজমহল বনাইছিল; ১৬৫৮ত ঔৰংগজেব সিংহাসনত।",
 ["Shah Jahan built the Taj Mahal for Mumtaz Mahal|শ্বাহজাহানে মমতাজ মহলৰ বাবে তাজমহল বনাইছিল", "It stands at Agra on the Yamuna|ই যমুনা পাৰৰ আগ্ৰাত", "Work began in 1632|১৬৩২ত কাম আৰম্ভ হৈছিল", "Aurangzeb defeated Dara Shikoh in 1658|১৬৫৮ত ঔৰংগজেবে দাৰা চিকোক হৰুৱাইছিল"],
 S("A tomb on the Yamuna|যমুনা পাৰৰ সমাধি", "<mark>[[shah-jahan|Shah Jahan]]</mark> built the <mark>Taj Mahal</mark> at [[agra]] for his wife Mumtaz Mahal, who died in 1631. Work began in 1632.|<mark>[[shah-jahan|শ্বাহজাহানে]]</mark> ১৬৩১ত মৃত্যু হোৱা পত্নী মমতাজ মহলৰ বাবে [[agra|আগ্ৰাত]] <mark>তাজমহল</mark> বনাইছিল। ১৬৩২ত কাম আৰম্ভ হৈছিল।", art="houses"),
 S("Four sons, one throne|চাৰি পুত্ৰ, এখন সিংহাসন", "When Shah Jahan fell ill in 1657 his sons fought for the throne. <mark>[[aurangzeb|Aurangzeb]]</mark> beat [[dara-shikoh|Dara Shikoh]] in 1658 and confined his father at Agra Fort.|১৬৫৭ত শ্বাহজাহান অসুস্থ হোৱাত পুত্ৰসকলে সিংহাসনৰ বাবে যুঁজিছিল। ১৬৫৮ত <mark>[[aurangzeb|ঔৰংগজেবে]]</mark> [[dara-shikoh|দাৰা চিকোক]] হৰুৱাই পিতৃক আগ্ৰা দুৰ্গত আবদ্ধ কৰিছিল।", art="court"),
 MA([("Shah Jahan|শ্বাহজাহান", "Taj Mahal|তাজমহল"), ("Akbar|আকবৰ", "Fatehpur Sikri|ফতেহপুৰ চিক্ৰী"), ("Sher Shah Suri|শ্বেৰ শ্বাহ সূৰী", "Tomb at Sasaram|সাসাৰামৰ সমাধি")], "Ruler and building.|শাসক আৰু নিৰ্মাণ।"),
 TF("The Taj Mahal is at Delhi.|তাজমহল দিল্লীত।", False, "It is at Agra.|ই আগ্ৰাত।"),
 IN("Aurangzeb's main rival for the throne was|সিংহাসনৰ বাবে ঔৰংগজেবৰ মূল প্ৰতিদ্বন্দ্বী", ".|।", ["Dara Shikoh|দাৰা চিকো", "Bairam Khan|বৈৰাম খান", "Hemu|হেমু", "Mir Jumla|মীৰজুমলা"], 0, "His brother Dara Shikoh.|তেওঁৰ ভায়েক দাৰা চিকো।"),
 SC("Unscramble the builder of the Taj Mahal.|তাজমহলৰ নিৰ্মাতাক সজোৱা।", "SHAHJAHAN", ["শ্বাহ", "জা", "হান"], "Shah Jahan.|শ্বাহজাহান।"),
 WH(["I was Shah Jahan's son.|মই শ্বাহজাহানৰ পুত্ৰ।", "I won the war of succession.|মই উত্তৰাধিকাৰৰ যুদ্ধ জিকিছিলোঁ।", "I ruled until 1707.|মই ১৭০৭লৈ শাসন কৰিছিলোঁ।"], ["Dara Shikoh|দাৰা চিকো", "Jahangir|জাহাংগীৰ", "Aurangzeb|ঔৰংগজেব", "Akbar|আকবৰ"], 2, "Aurangzeb.|ঔৰংগজেব।"),
)
u3 = U(3, "flag", "Aurangzeb's long reign|ঔৰংগজেবৰ দীঘলীয়া ৰাজত্ব",
 "Separate the record from the debate.|নথি আৰু বিতৰ্ক পৃথক কৰা।", "Finding recorded: widest extent, the jizya of 1679, and defeat at Saraighat in 1671.|প্ৰমাণ লিখা হ'ল: সৰ্বাধিক বিস্তাৰ, ১৬৭৯ৰ জিজিয়া, আৰু ১৬৭১ত শৰাইঘাটত পৰাজয়।",
 ["Aurangzeb ruled from 1658 to 1707|ঔৰংগজেবে ১৬৫৮ৰ পৰা ১৭০৭লৈ শাসন কৰিছিল", "The empire reached its widest under him|তেওঁৰ দিনত সাম্ৰাজ্য আটাইতকৈ বহল", "He restored the jizya in 1679|১৬৭৯ত তেওঁ জিজিয়া পুনৰ আনিছিল", "His forces were stopped in Assam at Saraighat|শৰাইঘাটত অসমত তেওঁৰ সৈন্য ৰোধ হৈছিল"],
 S("The widest empire|আটাইতকৈ বহল সাম্ৰাজ্য", "Under Aurangzeb the Mughal Empire reached its <mark>greatest extent</mark>. He restored the <mark>jizya</mark> in 1679.|ঔৰংগজেবৰ দিনত মোগল সাম্ৰাজ্য <mark>সৰ্বাধিক বিস্তৃত</mark> হৈছিল। ১৬৭৯ত তেওঁ <mark>জিজিয়া</mark> পুনৰ আনিছিল।", "Historians still debate how far his policies were religious and how far political, so give the facts and name the debate.|তেওঁৰ নীতি কিমান ধৰ্মীয় আৰু কিমান ৰাজনৈতিক, ইতিহাসবিদৰ মাজত এতিয়াও বিতৰ্ক আছে; তথ্য দিয়া, বিতৰ্কৰ কথা কোৱা।", art="scroll"),
 LINK(S("The war in Assam|অসমৰ যুদ্ধ", "His general [[mir-jumla|Mir Jumla]] took Garhgaon, the Ahom capital. Later, [[lachit|Lachit Borphukan]] and the Ahoms held the Mughals at <mark>Saraighat in 1671</mark>.|তেওঁৰ সেনাপতি [[mir-jumla|মীৰজুমলাই]] আহোম ৰাজধানী গড়গাঁও লৈছিল। পিছত <mark>১৬৭১ত শৰাইঘাটত</mark> [[lachit|লাচিত বৰফুকন]] আৰু আহোমে মোগলক ৰোধ কৰিছিল।", art="embassy"),
  "ahom-07-saraighat", 29, 5, "Saraighat, 1671|শৰাইঘাট, ১৬৭১", "The Assam History course tells this war in full.|অসমৰ ইতিহাস পাঠ্যক্ৰমত এই যুদ্ধ সম্পূৰ্ণকৈ কোৱা হৈছে।"),
 TF("Aurangzeb's empire was the widest of the Mughal age.|ঔৰংগজেবৰ সাম্ৰাজ্য মোগল যুগৰ আটাইতকৈ বহল আছিল।", True, "It covered nearly all the subcontinent.|ই প্ৰায় গোটেই উপমহাদেশ সামৰিছিল।"),
 IN("Aurangzeb restored the jizya in|ঔৰংগজেবে জিজিয়া পুনৰ আনিছিল", ".|ত।", ["1579|১৫৭৯", "1658|১৬৫৮", "1679|১৬৭৯", "1707|১৭০৭"], 2, "1679.|১৬৭৯।"),
 WH(["I was Aurangzeb's general.|মই ঔৰংগজেবৰ সেনাপতি।", "I took Garhgaon.|মই গড়গাঁও লৈছিলোঁ।"], ["Ram Singh|ৰাম সিং", "Mir Jumla|মীৰজুমলা", "Bairam Khan|বৈৰাম খান", "Lachit Borphukan|লাচিত বৰফুকন"], 1, "Mir Jumla. Ram Singh led the later force.|মীৰজুমলা। পিছৰ সৈন্যৰ নেতৃত্ব ৰাম সিঙে দিছিল।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Aurangzeb's accession|ঔৰংগজেবৰ সিংহাসনাৰোহণ", "Saraighat|শৰাইঘাট", "Execution of Guru Tegh Bahadur|গুৰু তেগ বাহাদুৰৰ প্ৰাণদণ্ড", "Jizya restored|জিজিয়া পুনৰ"], "1658, 1671, 1675, 1679.|১৬৫৮, ১৬৭১, ১৬৭৫, ১৬৭৯।"),
 SP("Saraighat was fought in *1771.*|শৰাইঘাটৰ যুদ্ধ *১৭৭১ত* হৈছিল।", "1671|১৬৭১ত", "1671.|১৬৭১।"),
)
test = TEST("Trace a century of Mughal power.|মোগল শক্তিৰ এটা শতিকা অনুসৰণ কৰা।", "Recorded: Jahangir to Aurangzeb.|লিখা হ'ল: জাহাংগীৰৰ পৰা ঔৰংগজেবলৈ।",
 OR("Order the emperors.|সম্ৰাটসকলক সজোৱা।", ["Jahangir|জাহাংগীৰ", "Shah Jahan|শ্বাহজাহান", "Aurangzeb|ঔৰংগজেব"], "That order.|এই ক্ৰমত।"),
 MA([("Sir Thomas Roe|ছাৰ টমাছ ৰ'", "Jahangir|জাহাংগীৰ"), ("Taj Mahal|তাজমহল", "Shah Jahan|শ্বাহজাহান"), ("Jizya restored|জিজিয়া পুনৰ", "Aurangzeb|ঔৰংগজেব")], "Fact and emperor.|তথ্য আৰু সম্ৰাট।"),
 TF("Saraighat was an Ahom victory over Mughal forces.|শৰাইঘাট মোগল সৈন্যৰ ওপৰত আহোমৰ জয়।", True, "In 1671.|১৬৭১ত।"),
 MP("Tap Agra, home of the Taj Mahal.|তাজমহলৰ চহৰ আগ্ৰা টিপা।", "agra", ["agra", "surat", "golconda", "delhi"], "Agra.|আগ্ৰা।"),
 IN("Mumtaz Mahal was the wife of|মমতাজ মহল আছিল", ".|ৰ পত্নী।", ["Jahangir|জাহাংগীৰ", "Akbar|আকবৰ", "Shah Jahan|শ্বাহজাহান", "Aurangzeb|ঔৰংগজেব"], 2, "Shah Jahan.|শ্বাহজাহান।"),
 MC("Consider these statements. (1) Roe won a factory at Surat. (2) Aurangzeb built the Taj Mahal. (3) Aurangzeb defeated Dara Shikoh. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ৰ'য়ে চুৰাটত কুঠি পাইছিল। (২) ঔৰংগজেবে তাজমহল বনাইছিল। (৩) ঔৰংগজেবে দাৰা চিকোক হৰুৱাইছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Shah Jahan built the Taj Mahal.|শ্বাহজাহানে তাজমহল বনাইছিল।"),
)
LESSON(16, "Jahangir to Aurangzeb|জাহাংগীৰৰ পৰা ঔৰংগজেবলৈ", "1605–1707|১৬০৫–১৭০৭", "The Mughal age|মোগল যুগ", "Evidence file 16|প্ৰমাণ নথি ১৬", "Peak and overreach|শিখৰ আৰু অতি বিস্তাৰ",
 "A century of marble, trade and war, from a factory at Surat to a defeat on the Brahmaputra.|মাৰ্বল, বাণিজ্য আৰু যুদ্ধৰ এটা শতিকা, চুৰাটৰ কুঠিৰ পৰা ব্ৰহ্মপুত্ৰৰ পৰাজয়লৈ।",
 sources, [u1, u2, u3], test, ["agra", "surat", "golconda", "delhi"],
 timeline=[("1615", "Roe reaches Jahangir|ৰ' জাহাংগীৰৰ ওচৰত", "u1"), ("1658", "Aurangzeb takes the throne|ঔৰংগজেব সিংহাসনত", "u2"), ("1671", "Saraighat|শৰাইঘাট", "u3")])
