#!/usr/bin/env python3
"""Lesson 30: Bose and the INA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "rangoon": ("place", "Rangoon|ৰেংগুন", "Today's Yangon, given in papers as the INA's headquarters|আজিৰ য়াংগুন, পৰীক্ষাত আজাদ হিন্দ ফৌজৰ কেন্দ্ৰ", [16.87, 96.2]),
 "singapore": ("place", "Singapore|ছিংগাপুৰ", "City where Bose took charge in 1943|১৯৪৩ত বসুৱে দায়িত্ব লোৱা চহৰ", [1.35, 103.82]),
 "kohima": ("place", "Kohima|কোহিমা", "Nagaland town, a battlefield of 1944|নাগালেণ্ডৰ নগৰ, ১৯৪৪ৰ ৰণক্ষেত্ৰ", [25.67, 94.11]),
 "imphal": ("place", "Imphal|ইম্ফল", "Capital of Manipur, a battlefield of 1944|মণিপুৰৰ ৰাজধানী, ১৯৪৪ৰ ৰণক্ষেত্ৰ", [24.82, 93.94]),
 "mohan-singh": ("person", "Mohan Singh|মোহন সিং", "Formed the first INA in 1942|১৯৪২ত প্ৰথম আজাদ হিন্দ ফৌজ গঢ়িছিল"),
 "rash-behari-bose": ("person", "Rash Behari Bose|ৰাসবিহাৰী বসু", "Handed the organisation to Subhas Bose in 1943|১৯৪৩ত সুভাষ বসুক দায়িত্ব দিছিল"),
})
sources = [
 src("Wikipedia, Subhas Chandra Bose", "https://en.wikipedia.org/wiki/Subhas_Chandra_Bose", "Used as a guide: Congress president 1938 and 1939, resignation, Forward Bloc 22 June 1939, 1941 escape, 18 August 1945. The venues Haripura and Tripuri were not confirmed and are left out. Check in review."),
 src("Wikipedia, Indian National Army", "https://en.wikipedia.org/wiki/Indian_National_Army", "Used as a guide: Mohan Singh, Bose in Singapore, Azad Hind, Imphal and Kohima, Red Fort trials. The Rangoon headquarters rests on the DME 2025 paper and was not confirmed. Check in review."),
]
u1 = U(1, "star", "A break with Congress|কংগ্ৰেছৰ সৈতে বিচ্ছেদ",
 "See why Bose left and what he founded.|বসুৱে কিয় এৰিলে আৰু কি গঢ়িলে, চোৱা।", "Finding recorded: re-elected in 1939, he resigned and formed the Forward Bloc.|প্ৰমাণ লিখা হ'ল: ১৯৩৯ত পুনৰ নিৰ্বাচিত হৈ পদত্যাগ কৰি ফৰৱাৰ্ড ব্লক গঢ়িলে।",
 ["Bose became Congress president in 1938|১৯৩৮ত বসু কংগ্ৰেছ সভাপতি হৈছিল", "He was re-elected in 1939 against Gandhi's choice|১৯৩৯ত গান্ধীৰ প্ৰাৰ্থীৰ বিৰুদ্ধে পুনৰ নিৰ্বাচিত", "He then resigned|তাৰ পিছত তেওঁ পদত্যাগ কৰিছিল", "He formed the Forward Bloc in 1939|১৯৩৯ত তেওঁ ফৰৱাৰ্ড ব্লক গঢ়িছিল"],
 S("President twice|দুবাৰ সভাপতি", "[[subhas-chandra-bose|Subhas Chandra Bose]] became Congress president in 1938. In 1939 he won again, beating Pattabhi Sitaramayya, Gandhi's preferred candidate.|[[subhas-chandra-bose|সুভাষচন্দ্ৰ বসু]] ১৯৩৮ত কংগ্ৰেছ সভাপতি হৈছিল। ১৯৩৯ত গান্ধীৰ পছন্দৰ পট্টভি সীতাৰামাইয়াক হৰুৱাই তেওঁ পুনৰ জয়ী হৈছিল।", art="court"),
 S("A new bloc|নতুন ব্লক", "The Working Committee resigned in protest, and Bose resigned the presidency. On 22 June <mark>1939</mark> he organised the <mark>Forward Bloc</mark>.|কাৰ্যনিৰ্বাহী সমিতিয়ে প্ৰতিবাদত পদত্যাগ কৰিলে, বসুৱেও সভাপতি পদ এৰিলে। <mark>১৯৩৯ৰ</mark> ২২ জুনত তেওঁ <mark>ফৰৱাৰ্ড ব্লক</mark> সংগঠিত কৰিছিল।", art="seal"),
 IN("After leaving the Congress, Bose set up the|কংগ্ৰেছ এৰি বসুৱে গঢ়িছিল", ".|।", ["Republican Party|ৰিপাব্লিকান পাৰ্টি", "Socialist Party|ছচিয়েলিষ্ট পাৰ্টি", "Forward Bloc|ফৰৱাৰ্ড ব্লক", "Swaraj Party|স্বৰাজ দল"], 2, "The Forward Bloc.|ফৰৱাৰ্ড ব্লক।"),
 TF("Bose lost the Congress presidential election of 1939.|১৯৩৯ৰ কংগ্ৰেছ সভাপতি নিৰ্বাচনত বসু হাৰিছিল।", False, "He won, then resigned.|তেওঁ জিকিছিল, তাৰ পিছত পদত্যাগ কৰিছিল।"),
 MA([("Swaraj Party|স্বৰাজ দল", "Das and Motilal Nehru|দাস আৰু মতিলাল নেহৰু"), ("Forward Bloc|ফৰৱাৰ্ড ব্লক", "Subhas Bose|সুভাষ বসু"), ("Labour Swaraj Party|লেবাৰ স্বৰাজ দল", "Nazrul|নজৰুল")], "Keep the parties apart.|দলবোৰ পৃথক ৰাখা।"),
 SP("Bose founded the Forward Bloc in *1949.*|বসুৱে *১৯৪৯ত* ফৰৱাৰ্ড ব্লক গঢ়িছিল।", "1939|১৯৩৯ত", "1939.|১৯৩৯।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["President|সভাপতি", "Re-elected|পুনৰ নিৰ্বাচিত", "Forward Bloc|ফৰৱাৰ্ড ব্লক"], "1938, early 1939, June 1939.|১৯৩৮, ১৯৩৯ৰ আৰম্ভণি, ১৯৩৯ৰ জুন।"),
)
u2 = U(2, "flag", "Azad Hind|আজাদ হিন্দ",
 "Trace the army from 1942 to 1943.|১৯৪২ৰ পৰা ১৯৪৩লৈ সৈন্যবাহিনী অনুসৰণ কৰা।", "Finding recorded: Mohan Singh began it, and Bose revived it in 1943.|প্ৰমাণ লিখা হ'ল: মোহন সিঙে আৰম্ভ কৰিছিল, ১৯৪৩ত বসুৱে পুনৰ জীৱিত কৰিছিল।",
 ["Bose escaped from Calcutta in January 1941|১৯৪১ৰ জানুৱাৰীত বসু কলিকতাৰ পৰা পলাইছিল", "Mohan Singh formed the first INA in 1942|১৯৪২ত মোহন সিঙে প্ৰথম আজাদ হিন্দ ফৌজ গঢ়িছিল", "Bose took charge at Singapore in July 1943|১৯৪৩ৰ জুলাইত ছিংগাপুৰত বসুৱে দায়িত্ব লৈছিল", "A Provisional Government of Azad Hind followed|তাৰ পিছত আজাদ হিন্দৰ অস্থায়ী চৰকাৰ"],
 S("Out of Calcutta|কলিকতাৰ পৰা বাহিৰলৈ", "Bose escaped from his Calcutta home in January <mark>1941</mark>.|<mark>১৯৪১ৰ</mark> জানুৱাৰীত বসু কলিকতাৰ ঘৰৰ পৰা পলাইছিল।", "In South-East Asia, [[mohan-singh|Mohan Singh]] had formed the first <mark>Indian National Army</mark> in 1942, mostly from captured soldiers. It was disbanded that December.|দক্ষিণ-পূব এছিয়াত [[mohan-singh|মোহন সিঙে]] ১৯৪২ত বেছিভাগ বন্দী সৈন্যৰে প্ৰথম <mark>আজাদ হিন্দ ফৌজ</mark> গঢ়িছিল। সেই ডিচেম্বৰত ই ভাঙি দিয়া হৈছিল।", art="embassy"),
 S("Singapore, 1943|ছিংগাপুৰ, ১৯৪৩", "In July <mark>1943</mark> [[rash-behari-bose|Rash Behari Bose]] handed over at [[singapore]]. The INA became the army of the Provisional Government of Azad Hind.|<mark>১৯৪৩ৰ</mark> জুলাইত ছিংগাপুৰত [[rash-behari-bose|ৰাসবিহাৰী বসুৱে]] দায়িত্ব দিছিল। ফৌজটো আজাদ হিন্দৰ অস্থায়ী চৰকাৰৰ সেনা হ'ল।", "In early 1944 its headquarters moved to <mark>[[rangoon|Rangoon]]</mark>, the answer papers want.|১৯৪৪ৰ আৰম্ভণিতে ইয়াৰ মুখ্য কাৰ্যালয় <mark>[[rangoon|ৰেংগুনলৈ]]</mark> গৈছিল, পৰীক্ষাত এইটোৱে উত্তৰ।", art="seal"),
 IN("The head office of the INA was at|আজাদ হিন্দ ফৌজৰ মুখ্য কাৰ্যালয় আছিল", ".|।", ["Tokyo|টকিঅ'", "Berlin|বাৰ্লিন", "Rangoon|ৰেংগুন", "Kuala Lumpur|কুৱালালামপুৰ"], 2, "Rangoon, from early 1944.|১৯৪৪ৰ আৰম্ভণিৰ পৰা ৰেংগুন।"),
 WH(["I formed the first INA.|মই প্ৰথম আজাদ হিন্দ ফৌজ গঢ়িছিলোঁ।", "It was disbanded in December 1942.|১৯৪২ৰ ডিচেম্বৰত ই ভাঙি দিয়া হৈছিল।"], ["Subhas Bose|সুভাষ বসু", "Mohan Singh|মোহন সিং", "Rash Behari Bose|ৰাসবিহাৰী বসু", "Bhagat Singh|ভগত সিং"], 1, "Mohan Singh.|মোহন সিং।"),
 TF("Bose founded the very first INA in 1942.|বসুৱে ১৯৪২ত প্ৰথম আজাদ হিন্দ ফৌজ গঢ়িছিল।", False, "Mohan Singh did. Bose revived it in 1943.|মোহন সিঙে গঢ়িছিল। ১৯৪৩ত বসুৱে পুনৰ জীৱিত কৰিছিল।"),
 MP("Tap Rangoon.|ৰেংগুন টিপা।", "rangoon", ["rangoon", "kohima", "calcutta", "delhi"], "Today's Yangon.|আজিৰ য়াংগুন।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Bose escapes Calcutta|বসু কলিকতাৰ পৰা পলায়", "First INA disbanded|প্ৰথম ফৌজ ভঙা", "Bose takes charge|বসুৱে দায়িত্ব লয়"], "1941, 1942, 1943.|১৯৪১, ১৯৪২, ১৯৪৩।"),
)
u3 = U(3, "moon", "Imphal to the Red Fort|ইম্ফলৰ পৰা লালকিল্লালৈ",
 "Follow the INA to its end and its effect.|আজাদ হিন্দ ফৌজৰ অন্ত আৰু প্ৰভাৱ অনুসৰণ কৰা।", "Finding recorded: defeat in 1944, then public trials that stirred India.|প্ৰমাণ লিখা হ'ল: ১৯৪৪ত পৰাজয়, তাৰ পিছত ভাৰত আলোড়িত কৰা ৰাজহুৱা বিচাৰ।",
 ["The INA joined the 1944 offensive into India|১৯৪৪ৰ ভাৰত অভিযানত ফৌজে ভাগ লৈছিল", "It failed at Imphal and Kohima|ইম্ফল আৰু কোহিমাত ই বিফল হৈছিল", "Bose died in Taihoku on 18 August 1945|১৯৪৫ৰ ১৮ আগষ্টত তাইহোকুত বসুৰ মৃত্যু", "The Red Fort trials ran from November 1945|১৯৪৫ৰ নৱেম্বৰৰ পৰা লালকিল্লাৰ বিচাৰ"],
 LINK(S("War at India's door|ভাৰতৰ দুৱাৰত যুদ্ধ", "In 1944 the INA joined the Japanese offensive into India. It failed at <mark>[[imphal]]</mark> and <mark>[[kohima]]</mark>, and the retreat brought heavy losses.|১৯৪৪ত ফৌজে জাপানৰ ভাৰত অভিযানত ভাগ লৈছিল। <mark>[[imphal|ইম্ফল]]</mark> আৰু <mark>[[kohima|কোহিমাত]]</mark> ই বিফল হৈছিল, পিছহোঁহকাত ডাঙৰ ক্ষতি হৈছিল।", map={"base": "india", "box": [88, 21, 98, 27.5], "show": ["imphal", "kohima"]}),
  "british-16", 53, 2, "Imphal and Kohima|ইম্ফল আৰু কোহিমা", "The Assam History course tells this war from the North-East.|অসমৰ ইতিহাস পাঠ্যক্ৰমত উত্তৰ-পূবৰ পৰা এই যুদ্ধৰ কথা আছে।"),
 S("Trials that backfired|ওলোটা ফল দিয়া বিচাৰ", "Bose died on 18 August 1945 at Taihoku, after a plane crash. Public trials of INA men at the <mark>Red Fort</mark> from November 1945 sparked wide protest across religious lines.|১৯৪৫ৰ ১৮ আগষ্টত তাইহোকুত বিমান দুৰ্ঘটনাৰ পিছত বসুৰ মৃত্যু হয়। ১৯৪৫ৰ নৱেম্বৰৰ পৰা <mark>লালকিল্লাত</mark> ফৌজৰ বিচাৰে ধৰ্ম নিৰ্বিশেষে ব্যাপক প্ৰতিবাদ জগাইছিল।", art="court"),
 MP("Tap Kohima.|কোহিমা টিপা।", "kohima", ["kohima", "rangoon", "calcutta", "delhi"], "In Nagaland.|নাগালেণ্ডত।"),
 TF("The INA offensive of 1944 succeeded at Imphal.|১৯৪৪ত ইম্ফলত ফৌজৰ অভিযান সফল হৈছিল।", False, "It failed.|ই বিফল হৈছিল।"),
 IN("INA men were tried in public at the|ফৌজৰ সদস্যৰ ৰাজহুৱা বিচাৰ হৈছিল", ".|ত।", ["Red Fort|লালকিল্লা", "Agra Fort|আগ্ৰা দুৰ্গ", "Ahmednagar Fort|আহমেদনগৰ দুৰ্গ", "Golconda|গোলকোণ্ডা"], 0, "The Red Fort.|লালকিল্লা।"),
 SC("Unscramble the Manipur battlefield.|মণিপুৰৰ ৰণক্ষেত্ৰখন সজোৱা।", "IMPHAL", ["ই", "ম্ফ", "ল"], "Imphal.|ইম্ফল।"),
 MA([("Imphal and Kohima|ইম্ফল আৰু কোহিমা", "1944|১৯৪৪"), ("Red Fort trials|লালকিল্লাৰ বিচাৰ", "1945|১৯৪৫"), ("Forward Bloc|ফৰৱাৰ্ড ব্লক", "1939|১৯৩৯")], "Event and year.|ঘটনা আৰু বছৰ।"),
)
test = TEST("Trace Bose's road from Congress to Azad Hind.|কংগ্ৰেছৰ পৰা আজাদ হিন্দলৈ বসুৰ পথ অনুসৰণ কৰা।", "Recorded: Forward Bloc, INA, Imphal and the Red Fort.|লিখা হ'ল: ফৰৱাৰ্ড ব্লক, ফৌজ, ইম্ফল আৰু লালকিল্লা।",
 IN("The party Bose founded after leaving the Congress was the|কংগ্ৰেছ এৰি বসুৱে গঢ়া দল", ".|।", ["Republican Party|ৰিপাব্লিকান পাৰ্টি", "Socialist Party|ছচিয়েলিষ্ট পাৰ্টি", "Forward Bloc|ফৰৱাৰ্ড ব্লক", "Indian National Army|আজাদ হিন্দ ফৌজ"], 2, "The Forward Bloc; the INA was an army.|ফৰৱাৰ্ড ব্লক; ফৌজ এটা সৈন্যবাহিনী।"),
 IN("The INA's head office was at|ফৌজৰ মুখ্য কাৰ্যালয় আছিল", ".|।", ["Tokyo|টকিঅ'", "Berlin|বাৰ্লিন", "Rangoon|ৰেংগুন", "Kuala Lumpur|কুৱালালামপুৰ"], 2, "Rangoon.|ৰেংগুন।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Forward Bloc|ফৰৱাৰ্ড ব্লক", "Bose reaches Singapore|বসু ছিংগাপুৰত", "Imphal and Kohima|ইম্ফল আৰু কোহিমা", "Red Fort trials|লালকিল্লাৰ বিচাৰ"], "1939, 1943, 1944, 1945.|১৯৩৯, ১৯৪৩, ১৯৪৪, ১৯৪৫।"),
 MP("Tap Imphal.|ইম্ফল টিপা।", "imphal", ["imphal", "rangoon", "calcutta", "delhi"], "In Manipur.|মণিপুৰত।"),
 TF("Mohan Singh formed the first INA.|মোহন সিঙে প্ৰথম ফৌজ গঢ়িছিল।", True, "In 1942.|১৯৪২ত।"),
 MC("Consider these statements. (1) Bose won the 1939 Congress election. (2) Rash Behari Bose handed over to him in 1943. (3) The trials of INA men were held at Rangoon. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ১৯৩৯ৰ কংগ্ৰেছ নিৰ্বাচনত বসু জয়ী। (২) ১৯৪৩ত ৰাসবিহাৰী বসুৱে তেওঁক দায়িত্ব দিছিল। (৩) ফৌজৰ বিচাৰ ৰেংগুনত হৈছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 0, "The trials were at the Red Fort.|বিচাৰ লালকিল্লাত হৈছিল।"),
)
LESSON(30, "Bose and the INA|বসু আৰু আজাদ হিন্দ ফৌজ", "1938–1945|১৯৩৮–১৯৪৫", "Mass struggle and freedom|গণ সংগ্ৰাম আৰু স্বাধীনতা", "Evidence file 30|প্ৰমাণ নথি ৩০", "Another road to freedom|স্বাধীনতাৰ আন এক পথ",
 "Bose won the Congress vote, lost the party and raised an army abroad. Its defeat stirred India more than its campaign did.|বসুৱে কংগ্ৰেছৰ ভোট জিকিলে, দল হেৰুৱালে, বিদেশত সৈন্য গঢ়িলে। অভিযানতকৈ ইয়াৰ পৰাজয়েহে ভাৰতক বেছি আলোড়িত কৰিলে।",
 sources, [u1, u2, u3], test, ["rangoon", "kohima", "imphal", "calcutta", "delhi"], box=[80, 8, 106, 30],
 timeline=[("1939", "Forward Bloc|ফৰৱাৰ্ড ব্লক", "u1"), ("1943", "Bose takes charge at Singapore|ছিংগাপুৰত বসুৰ দায়িত্ব", "u2"), ("1944", "Imphal and Kohima|ইম্ফল আৰু কোহিমা", "u3")])
