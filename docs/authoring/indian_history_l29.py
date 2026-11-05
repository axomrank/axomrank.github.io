#!/usr/bin/env python3
"""Lesson 29: Quit India."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "stafford-cripps": ("person", "Stafford Cripps|ষ্টেফৰ্ড ক্ৰিপছ", "Led the failed Mission of March 1942|১৯৪২ৰ মাৰ্চৰ বিফল অভিযানৰ নেতা"),
 "aruna-asaf-ali": ("person", "Aruna Asaf Ali|অৰুণা আছফ আলী", "Hoisted the flag at Bombay on 9 August 1942|১৯৪২ৰ ৯ আগষ্টত বোম্বেত পতাকা উত্তোলন কৰিছিল"),
 "lord-linlithgow": ("person", "Lord Linlithgow|লৰ্ড লিনলিথগো", "Viceroy in 1942|১৯৪২ত ভাইচৰয়"),
 "ahmednagar": ("place", "Ahmednagar|আহমেদনগৰ", "Maharashtra fort where Nehru was held from 1942 to 1945|১৯৪২ৰ পৰা ১৯৪৫লৈ নেহৰু বন্দী থকা মহাৰাষ্ট্ৰৰ দুৰ্গ", [19.09, 74.74]),
 "midnapore": ("place", "Midnapore|মেদিনীপুৰ", "Bengal district with a parallel government, in Tamluk and Contai|সমান্তৰাল চৰকাৰ থকা বংগৰ জিলা, তমলুক আৰু কাঁথিত", [22.3, 87.92]),
})
sources = [
 src("Wikipedia, Quit India Movement", "https://en.wikipedia.org/wiki/Quit_India_Movement", "Used as a guide: Cripps, 8 August 1942, Gowalia Tank, Do or Die, arrests, Aruna Asaf Ali, Tamluk, Linlithgow's phrase. Check in review."),
 src("Wikipedia, The Discovery of India", "https://en.wikipedia.org/wiki/The_Discovery_of_India", "Used as a guide: written at Ahmednagar Fort, 1942 to 1945. Check in review."),
]
u1 = U(1, "court", "A failed offer|বিফল প্ৰস্তাৱ",
 "See why 1942 came to a head.|১৯৪২ত কিয় সংকট চৰম হ'ল, চোৱা।", "Finding recorded: the Cripps Mission offered no timetable and failed.|প্ৰমাণ লিখা হ'ল: ক্ৰিপছ অভিযানে কোনো সময়সূচী দিয়া নাছিল, বিফল হৈছিল।",
 ["The Cripps Mission came in March 1942|১৯৪২ৰ মাৰ্চত ক্ৰিপছ অভিযান", "It offered no timetable for self-government|ই স্বায়ত্ত শাসনৰ সময়সূচী দিয়া নাছিল", "The war was reaching India's east|যুদ্ধ ভাৰতৰ পূবলৈ আহিছিল", "Gandhi rejected the offer|গান্ধীয়ে প্ৰস্তাৱ অস্বীকাৰ কৰিছিল"],
 S("A mission from London|লণ্ডনৰ অভিযান", "In March <mark>1942</mark>, with war close to India, [[stafford-cripps|Stafford Cripps]] came with an offer. It gave no timetable for self-government.|<mark>১৯৪২ৰ</mark> মাৰ্চত, যুদ্ধ ভাৰতৰ ওচৰ হওঁতে, [[stafford-cripps|ষ্টেফৰ্ড ক্ৰিপছ]] এটা প্ৰস্তাৱ লৈ আহিছিল। ইয়াত স্বায়ত্ত শাসনৰ সময়সূচী নাছিল।", art="embassy"),
 S("A cheque nobody wanted|কোনেও নিবিচৰা চেক", "Gandhi's remark called it a post-dated cheque on a crashing bank. The <mark>Cripps Mission</mark> failed, and Congress turned to a final demand.|গান্ধীয়ে ইয়াক ভাঙি পৰা বেংকৰ পিছৰ তাৰিখৰ চেক বুলিছিল। <mark>ক্ৰিপছ অভিযান</mark> বিফল হ'ল, কংগ্ৰেছে চূড়ান্ত দাবীৰ ফালে গ'ল।", art="seal"),
 IN("The Cripps Mission came in|ক্ৰিপছ অভিযান আহিছিল", ".|ত।", ["1927|১৯২৭", "1935|১৯৩৫", "1942|১৯৪২", "1946|১৯৪৬"], 2, "March 1942.|১৯৪২ৰ মাৰ্চ।"),
 TF("The Cripps Mission gave a timetable for independence.|ক্ৰিপছ অভিযানে স্বাধীনতাৰ সময়সূচী দিছিল।", False, "It gave none.|ই নিদিলে।"),
 WH(["I came from London in 1942.|মই ১৯৪২ত লণ্ডনৰ পৰা আহিছিলোঁ।", "My offer failed.|মোৰ প্ৰস্তাৱ বিফল হৈছিল।"], ["John Simon|জন চাইমন", "Stafford Cripps|ষ্টেফৰ্ড ক্ৰিপছ", "Thomas Roe|টমাছ ৰ'", "Edwin Montagu|এডৱিন মণ্টেগু"], 1, "Cripps.|ক্ৰিপছ।"),
 OR("Order the British missions.|ব্ৰিটিছ অভিযানবোৰ সজোৱা।", ["Simon Commission|চাইমন কমিছন", "Cripps Mission|ক্ৰিপছ অভিযান", "Cabinet Mission|কেবিনেট অভিযান"], "1927, 1942, 1946.|১৯২৭, ১৯৪২, ১৯৪৬।"),
 SP("The Cripps Mission came in *1924.*|ক্ৰিপছ অভিযান *১৯২৪ত* আহিছিল।", "1942|১৯৪২ত", "1942.|১৯৪২।"),
)
u2 = U(2, "flag", "Do or Die|কৰো বা মৰো",
 "Fix the place, date and slogan.|ঠাই, তাৰিখ আৰু শ্লোগান মনত ৰাখা।", "Finding recorded: 8 August 1942 at Gowalia Tank, today's August Kranti Maidan.|প্ৰমাণ লিখা হ'ল: ১৯৪২ৰ ৮ আগষ্ট, গোৱালিয়া টেংক, আজিৰ আগষ্ট ক্ৰান্তি ময়দান।",
 ["Quit India began on 8 August 1942 at Bombay|১৯৪২ৰ ৮ আগষ্টত বোম্বেত ভাৰত ত্যাগ আৰম্ভ", "Gandhi spoke at Gowalia Tank|গান্ধীয়ে গোৱালিয়া টেংকত কৈছিল", "It is now August Kranti Maidan|ইয়াক এতিয়া আগষ্ট ক্ৰান্তি ময়দান বোলে", "The slogan was Do or Die|শ্লোগান কৰো বা মৰো"],
 S("Gowalia Tank|গোৱালিয়া টেংক", "On <mark>8 August 1942</mark> the Congress launched the movement at [[bombay]]. Gandhi gave his <mark>Do or Die</mark> speech at Gowalia Tank.|<mark>১৯৪২ৰ ৮ আগষ্টত</mark> [[bombay|বোম্বেত]] কংগ্ৰেছে আন্দোলন আৰম্ভ কৰিছিল। গান্ধীয়ে গোৱালিয়া টেংকত <mark>কৰো বা মৰো</mark> ভাষণ দিছিল।", "That ground is now <mark>August Kranti Maidan</mark>.|সেই ঠাই এতিয়া <mark>আগষ্ট ক্ৰান্তি ময়দান</mark>।", art="door"),
 S("Leaders vanish overnight|নিশাতে নেতা নাইকিয়া", "Almost the whole Congress leadership was jailed within hours. [[aruna-asaf-ali|Aruna Asaf Ali]], then little known, hoisted the flag on 9 August.|প্ৰায় গোটেই কংগ্ৰেছ নেতৃত্ব কেইঘণ্টামানৰ ভিতৰতে বন্দী হ'ল। তেতিয়াৰ অচিনাকি [[aruna-asaf-ali|অৰুণা আছফ আলীয়ে]] ৯ আগষ্টত পতাকা উত্তোলন কৰিছিল।", art="calendar"),
 IN("Gandhi launched Quit India in 1942 at|গান্ধীয়ে ১৯৪২ত ভাৰত ত্যাগ আৰম্ভ কৰিছিল", ".|ত।", ["Shivaji Park|শিৱাজী পাৰ্ক", "Brabourne Stadium|ব্ৰেবৰ্ণ ষ্টেডিয়াম", "August Kranti Maidan|আগষ্ট ক্ৰান্তি ময়দান", "Pragati Maidan|প্ৰগতি ময়দান"], 2, "Then called Gowalia Tank.|তেতিয়া গোৱালিয়া টেংক।"),
 IN("'Karenge Ya Marenge' belongs to the|'কৰেংগে য়া মৰেংগে' জড়িত", ".|ৰ সৈতে।", ["Non-Cooperation Movement|অসহযোগ আন্দোলন", "Quit India Movement|ভাৰত ত্যাগ আন্দোলন", "Khilafat Movement|খিলাফত আন্দোলন", "Revolt of 1857|১৮৫৭ৰ বিদ্ৰোহ"], 1, "Quit India, 1942.|ভাৰত ত্যাগ, ১৯৪২।"),
 MP("Tap the city where Quit India began.|ভাৰত ত্যাগ আৰম্ভ হোৱা চহৰখন টিপা।", "bombay", ["bombay", "delhi", "calcutta", "ahmednagar"], "Bombay.|বোম্বে।"),
 TF("Aruna Asaf Ali hoisted the flag after the leaders' arrests.|নেতাসকলৰ গ্ৰেপ্তাৰৰ পিছত অৰুণা আছফ আলীয়ে পতাকা উত্তোলন কৰিছিল।", True, "On 9 August.|৯ আগষ্টত।"),
 SC("Unscramble the month of 1942.|১৯৪২ৰ মাহটো সজোৱা।", "AUGUST", ["আ", "গ", "ষ্ট"], "August.|আগষ্ট।"),
)
u3 = U(3, "moon", "A leaderless rising|নেতৃত্বহীন বিদ্ৰোহ",
 "See what happened with the leaders in jail.|নেতা জেলত থাকোঁতে কি হ'ল, চোৱা।", "Finding recorded: sabotage, over 100,000 arrests and parallel governments.|প্ৰমাণ লিখা হ'ল: ধ্বংসাত্মক কাম, ১,০০,০০০ৰ অধিক গ্ৰেপ্তাৰ আৰু সমান্তৰাল চৰকাৰ।",
 ["Over 100,000 people were arrested|১,০০,০০০ৰ অধিক লোক গ্ৰেপ্তাৰ", "Crowds attacked railways and post offices|জনতাই ৰেল আৰু ডাকঘৰ আক্ৰমণ কৰিছিল", "Tamluk ran a parallel government|তমলুকত সমান্তৰাল চৰকাৰ", "Kanaklata Barua was shot at Gohpur|গহপুৰত কনকলতা বৰুৱাক গুলীয়াইছিল"],
 S("Rails and post offices|ৰেল আৰু ডাকঘৰ", "With leaders jailed, crowds attacked post offices, railways and police stations. Over <mark>100,000</mark> were arrested.|নেতা বন্দী হোৱাত জনতাই ডাকঘৰ, ৰেল আৰু আৰক্ষী থানা আক্ৰমণ কৰিছিল। <mark>১,০০,০০০ৰো</mark> অধিক লোক গ্ৰেপ্তাৰ হৈছিল।", "Viceroy [[lord-linlithgow|Linlithgow]] called it the most serious rebellion since 1857.|ভাইচৰয় [[lord-linlithgow|লিনলিথগোৱে]] ইয়াক ১৮৫৭ৰ পিছৰ আটাইতকৈ গুৰুতৰ বিদ্ৰোহ বুলিছিল।", art="door"),
 LINK(S("Parallel governments, and Gohpur|সমান্তৰাল চৰকাৰ আৰু গহপুৰ", "In Tamluk and Contai, in [[midnapore]], people ran a <mark>parallel government</mark> until 1944.|[[midnapore|মেদিনীপুৰৰ]] তমলুক আৰু কাঁথিত মানুহে ১৯৪৪লৈ <mark>সমান্তৰাল চৰকাৰ</mark> চলাইছিল।", "In Assam, police shot <mark>[[kanaklata-barua|Kanaklata Barua]]</mark> and Mukunda Kakati at Gohpur.|অসমৰ গহপুৰত আৰক্ষীয়ে <mark>[[kanaklata-barua|কনকলতা বৰুৱা]]</mark> আৰু মুকুন্দ কাকতিক গুলীয়াইছিল।", map={"base": "india", "box": [84, 21, 96, 29], "show": ["midnapore", "calcutta"]}),
  "british-15", 52, 2, "The flag at Gohpur|গহপুৰত পতাকা", "The Assam History course tells Gohpur in full.|অসমৰ ইতিহাস পাঠ্যক্ৰমত গহপুৰৰ কথা সম্পূৰ্ণকৈ আছে।"),
 IN("Kanaklata Barua was martyred in the|কনকলতা বৰুৱা শ্বহীদ হৈছিল", ".|ত।", ["Non-Cooperation movement|অসহযোগ আন্দোলন", "Quit India movement|ভাৰত ত্যাগ আন্দোলন", "Sepoy Mutiny|চিপাহী বিদ্ৰোহ", "Civil Disobedience|আইন অমান্য"], 1, "Quit India.|ভাৰত ত্যাগ।"),
 TF("All of Quit India stayed non-violent.|ভাৰত ত্যাগ সম্পূৰ্ণ অহিংস আছিল।", False, "There was sabotage and violence.|ধ্বংসাত্মক কাম আৰু হিংসা হৈছিল।"),
 MP("Tap Midnapore.|মেদিনীপুৰ টিপা।", "midnapore", ["midnapore", "bombay", "delhi", "ahmednagar"], "In Bengal.|বংগত।"),
 MA([("Tamluk|তমলুক", "Parallel government|সমান্তৰাল চৰকাৰ"), ("Gohpur|গহপুৰ", "Kanaklata Barua|কনকলতা বৰুৱা"), ("Gowalia Tank|গোৱালিয়া টেংক", "Do or Die|কৰো বা মৰো")], "Place and link.|ঠাই আৰু সম্পৰ্ক।"),
 SP("Kanaklata Barua was shot at *Tezpur.*|কনকলতা বৰুৱাক *তেজপুৰত* গুলীয়াইছিল।", "Gohpur|গহপুৰত", "At Gohpur.|গহপুৰত।"),
)
u4 = U(4, "scroll", "Prison and a book|কাৰাগাৰ আৰু গ্ৰন্থ",
 "Fix the Discovery of India question.|ডিছকভাৰী অৱ ইণ্ডিয়াৰ প্ৰশ্ন মনত ৰাখা।", "Finding recorded: Nehru wrote it at Ahmednagar Fort between 1942 and 1945.|প্ৰমাণ লিখা হ'ল: ১৯৪২–৪৫ত আহমেদনগৰ দুৰ্গত নেহৰুৱে লিখিছিল।",
 ["Nehru was held at Ahmednagar Fort|নেহৰু আহমেদনগৰ দুৰ্গত বন্দী আছিল", "He wrote The Discovery of India there|তাত তেওঁ ডিছকভাৰী অৱ ইণ্ডিয়া লিখিছিল", "It came out in 1946|ই ১৯৪৬ত প্ৰকাশ হৈছিল", "Leaders were released in 1945|১৯৪৫ত নেতাসকল মুক্তি পাইছিল"],
 S("A fort in Maharashtra|মহাৰাষ্ট্ৰৰ এটা দুৰ্গ", "[[jawaharlal-nehru|Jawaharlal Nehru]] was jailed at <mark>[[ahmednagar|Ahmednagar Fort]]</mark> from 1942 to 1945. There he wrote <mark>The Discovery of India</mark>, published in 1946.|[[jawaharlal-nehru|জৱাহৰলাল নেহৰু]] ১৯৪২ৰ পৰা ১৯৪৫লৈ <mark>[[ahmednagar|আহমেদনগৰ দুৰ্গত]]</mark> বন্দী আছিল। তাত তেওঁ <mark>ডিছকভাৰী অৱ ইণ্ডিয়া</mark> লিখিছিল, ১৯৪৬ত প্ৰকাশ।", art="scroll"),
 S("Three mass movements|তিনিটা গণ আন্দোলন", "Keep them apart: <b>Non-Cooperation 1920, Civil Disobedience 1930, Quit India 1942</b>. Each has its own place, slogan and ending.|এইবোৰ পৃথক ৰাখা: <b>অসহযোগ ১৯২০, আইন অমান্য ১৯৩০, ভাৰত ত্যাগ ১৯৪২</b>। প্ৰত্যেকৰে নিজা ঠাই, শ্লোগান আৰু অন্ত আছে।", art="calendar"),
 IN("Nehru wrote The Discovery of India at|নেহৰুৱে ডিছকভাৰী অৱ ইণ্ডিয়া লিখিছিল", ".|ত।", ["Pune Central Jail|পুণে কেন্দ্ৰীয় কাৰাগাৰ", "Yerwada Jail|য়েৰৱদা কাৰাগাৰ", "Thane Jail|থানে কাৰাগাৰ", "Ahmednagar Fort|আহমেদনগৰ দুৰ্গ"], 3, "Ahmednagar Fort.|আহমেদনগৰ দুৰ্গ।"),
 MA([("Non-Cooperation|অসহযোগ", "Chauri Chaura|চৌৰী চৌৰা"), ("Civil Disobedience|আইন অমান্য", "Dandi|ডাণ্ডী"), ("Quit India|ভাৰত ত্যাগ", "Do or Die|কৰো বা মৰো")], "Movement and mark.|আন্দোলন আৰু চিন।"),
 OR("Order the mass movements.|গণ আন্দোলনবোৰ সজোৱা।", ["Non-Cooperation|অসহযোগ", "Civil Disobedience|আইন অমান্য", "Quit India|ভাৰত ত্যাগ"], "1920, 1930, 1942.|১৯২০, ১৯৩০, ১৯৪২।"),
 MP("Tap Ahmednagar.|আহমেদনগৰ টিপা।", "ahmednagar", ["ahmednagar", "calcutta", "delhi", "midnapore"], "In Maharashtra.|মহাৰাষ্ট্ৰত।"),
 TF("The Discovery of India was written in prison.|ডিছকভাৰী অৱ ইণ্ডিয়া কাৰাগাৰত লিখা।", True, "At Ahmednagar Fort.|আহমেদনগৰ দুৰ্গত।"),
)
test = TEST("Tell 1942 from offer to prison.|প্ৰস্তাৱৰ পৰা কাৰাগাৰলৈ ১৯৪২ কোৱা।", "Recorded: Cripps, Gowalia Tank, Gohpur and Ahmednagar.|লিখা হ'ল: ক্ৰিপছ, গোৱালিয়া টেংক, গহপুৰ আৰু আহমেদনগৰ।",
 IN("August Kranti and 'Karenge Ya Marenge' belong to the|আগষ্ট ক্ৰান্তি আৰু 'কৰেংগে য়া মৰেংগে' জড়িত", ".|ৰ সৈতে।", ["Non-Cooperation Movement|অসহযোগ আন্দোলন", "Quit India Movement|ভাৰত ত্যাগ আন্দোলন", "Khilafat Movement|খিলাফত আন্দোলন", "Revolt of 1857|১৮৫৭ৰ বিদ্ৰোহ"], 1, "Quit India.|ভাৰত ত্যাগ।"),
 TF("Kanaklata Barua and Mukunda Kakati were shot at Gohpur.|গহপুৰত কনকলতা আৰু মুকুন্দ কাকতিক গুলীয়াইছিল।", True, "In 1942.|১৯৪২ত।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Cripps Mission|ক্ৰিপছ অভিযান", "Do or Die speech|কৰো বা মৰো ভাষণ", "Discovery of India published|ডিছকভাৰী অৱ ইণ্ডিয়া প্ৰকাশ"], "March 1942, August 1942, 1946.|১৯৪২ মাৰ্চ, ১৯৪২ আগষ্ট, ১৯৪৬।"),
 MP("Tap Ahmednagar.|আহমেদনগৰ টিপা।", "ahmednagar", ["ahmednagar", "calcutta", "delhi", "midnapore"], "Ahmednagar.|আহমেদনগৰ।"),
 MA([("Aruna Asaf Ali|অৰুণা আছফ আলী", "Hoisted the flag|পতাকা উত্তোলন"), ("Lord Linlithgow|লৰ্ড লিনলিথগো", "Viceroy|ভাইচৰয়")], "Name and role.|নাম আৰু ভূমিকা।"),
 MC("Consider these statements. (1) Quit India began in August 1942. (2) Gandhi led the movement in the streets throughout. (3) Tamluk had a parallel government. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ১৯৪২ৰ আগষ্টত ভাৰত ত্যাগ আৰম্ভ। (২) গান্ধীয়ে গোটেই সময় ৰাজপথত নেতৃত্ব দিছিল। (৩) তমলুকত সমান্তৰাল চৰকাৰ আছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Gandhi was jailed within hours.|গান্ধী কেইঘণ্টামানৰ ভিতৰতে বন্দী হৈছিল।"),
)
LESSON(29, "Quit India|ভাৰত ত্যাগ", "1942–1945|১৯৪২–১৯৪৫", "Mass struggle and freedom|গণ সংগ্ৰাম আৰু স্বাধীনতা", "Evidence file 29|প্ৰমাণ নথি ২৯", "A movement without its leaders|নেতা নোহোৱা আন্দোলন",
 "Every leader was jailed within hours of the call, and the movement went on without them. Find out how.|আহ্বানৰ কেইঘণ্টামানৰ ভিতৰতে সকলো নেতা বন্দী হ'ল, আন্দোলন তথাপি চলিল। কেনেকৈ, উলিওৱা।",
 sources, [u1, u2, u3, u4], test, ["bombay", "delhi", "calcutta", "ahmednagar", "midnapore"],
 timeline=[("1942", "March: Cripps Mission|মাৰ্চ: ক্ৰিপছ অভিযান", "u1"), ("1942", "8 August: Do or Die|৮ আগষ্ট: কৰো বা মৰো", "u2"), ("1946", "The Discovery of India published|ডিছকভাৰী অৱ ইণ্ডিয়া প্ৰকাশ", "u4")])
