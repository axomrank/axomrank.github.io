#!/usr/bin/env python3
"""Lesson 24: Swadeshi to Lucknow."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "bal-gangadhar-tilak": ("person", "Bal Gangadhar Tilak|বাল গংগাধৰ তিলক", "Radical leader of the slogan on Swaraj|স্বৰাজৰ শ্লোগানৰ চৰমপন্থী নেতা"),
 "lala-lajpat-rai": ("person", "Lala Lajpat Rai|লালা লাজপত ৰায়", "Punjab leader, one of Lal Bal Pal|পঞ্জাবৰ নেতা, লাল-বাল-পালৰ এজন"),
 "bipin-chandra-pal": ("person", "Bipin Chandra Pal|বিপিনচন্দ্ৰ পাল", "Bengal leader, one of Lal Bal Pal|বংগৰ নেতা, লাল-বাল-পালৰ এজন"),
 "aurobindo-ghosh": ("person", "Aurobindo Ghosh|অৰবিন্দ ঘোষ", "Radical leader who wrote on passive resistance|নিষ্ক্ৰিয় প্ৰতিৰোধৰ বিষয়ে লিখা চৰমপন্থী নেতা"),
 "annie-besant": ("person", "Annie Besant|এনি বেচান্ত", "Leader of the Home Rule movement|হোম ৰুল আন্দোলনৰ নেত্ৰী"),
 "madan-mohan-malaviya": ("person", "Madan Mohan Malaviya|মদন মোহন মালৱীয়", "Founder of the Hindu Mahasabha and Banaras Hindu University|হিন্দু মহাসভা আৰু কাশী হিন্দু বিশ্ববিদ্যালয়ৰ প্ৰতিষ্ঠাপক"),
 "dhaka": ("place", "Dacca|ঢাকা", "City where the Muslim League was founded in 1906|১৯০৬ত মুছলিম লীগ প্ৰতিষ্ঠিত হোৱা চহৰ", [23.81, 90.41]),
 "haridwar": ("place", "Haridwar|হৰিদ্বাৰ", "City on the Ganga, linked with the Hindu Mahasabha of 1915|গংগা পাৰৰ নগৰ, ১৯১৫ৰ হিন্দু মহাসভাৰ সৈতে জড়িত", [29.95, 78.16]),
})
sources = [
 src("Wikipedia, Partition of Bengal (1905)", "https://en.wikipedia.org/wiki/Partition_of_Bengal_(1905)", "Used as a guide: 16 October 1905, Curzon, Swadeshi, Eastern Bengal and Assam, annulment. Check in review."),
 src("Wikipedia, Bal Gangadhar Tilak", "https://en.wikipedia.org/wiki/Bal_Gangadhar_Tilak", "Used as a guide: the slogan and its reported origin with Baptista, Kesari, Lal Bal Pal, Surat, Mandalay, Home Rule League. Check in review."),
 src("Wikipedia, All-India Muslim League", "https://en.wikipedia.org/wiki/All-India_Muslim_League", "Used as a guide: 30 December 1906, Dacca, 1909, 1916. Lucknow Pact terms were not read. Check in review."),
 src("Wikipedia, Akhil Bharat Hindu Mahasabha", "https://en.wikipedia.org/wiki/Akhil_Bharat_Hindu_Mahasabha", "Used as a guide: 1915, Haridwar, Malaviya. Check in review."),
 src("Wikipedia, Delhi Durbar", "https://en.wikipedia.org/wiki/Delhi_Durbar", "Used as a guide: 12 December 1911, capital moved, partition annulled. Check in review."),
 src("Wikipedia, Lala Lajpat Rai", "https://en.wikipedia.org/wiki/Lala_Lajpat_Rai", "Used as a guide: associated with Punjab National Bank's management in 1894. Check in review."),
 src("APSC CCE Prelims 2025 GS-I, question 32, page read", "https://apsc.nic.in/cce.html", "Options on 'passive resistance'; key B is Aurobindo Ghosh. The Wikipedia page on him did not cover the 1907 articles. Check in review."),
]
u1 = U(1, "flag", "A province cut in two|দুভাগ হোৱা প্ৰদেশ",
 "See why Bengal's partition lit a movement.|বংগ বিভাজনে কিয় আন্দোলন জ্বলালে, চোৱা।", "Finding recorded: 1905 partition, Swadeshi boycott, 1911 annulment.|প্ৰমাণ লিখা হ'ল: ১৯০৫ৰ বিভাজন, স্বদেশী বৰ্জন, ১৯১১ত বাতিল।",
 ["Curzon partitioned Bengal on 16 October 1905|১৯০৫ৰ ১৬ অক্টোবৰত কাৰ্জনে বংগ বিভাজন কৰিছিল", "Assam joined Eastern Bengal and Assam|অসম পূব বংগ আৰু অসমৰ অংশ হৈছিল", "Swadeshi and boycott were the response|স্বদেশী আৰু বৰ্জন প্ৰতিক্ৰিয়া আছিল", "It was annulled in 1911|১৯১১ত ই বাতিল হৈছিল"],
 LINK(S("Curzon's line|কাৰ্জনৰ ৰেখা", "[[lord-curzon|Lord Curzon]] partitioned Bengal on <mark>16 October 1905</mark>. Officials called it administrative, and many Bengalis called it divide and rule.|[[lord-curzon|লৰ্ড কাৰ্জনে]] <mark>১৯০৫ৰ ১৬ অক্টোবৰত</mark> বংগ বিভাজন কৰিছিল। বিষয়াই ইয়াক প্ৰশাসনিক বুলিছিল, বহু বঙালীয়ে বিভাজন আৰু শাসনৰ নীতি বুলিছিল।", "Assam went into the new province of Eastern Bengal and Assam.|অসম নতুন পূব বংগ আৰু অসম প্ৰদেশত গ'ল।", art="seal"),
  "british-12", 49, 1, "An enlarged province|বৃহৎ প্ৰদেশ", "The Assam History course tells what this meant for Assam.|অসমৰ ইতিহাস পাঠ্যক্ৰমত অসমৰ বাবে ইয়াৰ অৰ্থ কোৱা হৈছে।"),
 S("Own goods only|কেৱল নিজৰ বস্তু", "The answer was <mark>Swadeshi</mark>: buy Indian goods and boycott British ones. Protests spread beyond Bengal.|উত্তৰ আছিল <mark>স্বদেশী</mark>: ভাৰতীয় বস্তু কিনা, ব্ৰিটিছ বস্তু বৰ্জন কৰা। প্ৰতিবাদ বংগৰ বাহিৰলৈ বিয়পিল।", "At the Delhi Durbar on 12 December <mark>1911</mark> the partition was annulled and the capital moved to Delhi.|<mark>১৯১১ৰ</mark> ১২ ডিচেম্বৰত দিল্লী দৰবাৰত বিভাজন বাতিল হ'ল, ৰাজধানী দিল্লীলৈ গ'ল।", art="calendar"),
 IN("Bengal was partitioned in|বংগ বিভাজন হৈছিল", ".|ত।", ["1885|১৮৮৫", "1905|১৯০৫", "1911|১৯১১", "1919|১৯১৯"], 1, "1905.|১৯০৫।"),
 IN("The British moved India's capital from Calcutta to Delhi in|ব্ৰিটিছে কলিকতাৰ পৰা দিল্লীলৈ ৰাজধানী নিছিল", ".|ত।", ["1907|১৯০৭", "1910|১৯১০", "1911|১৯১১", "1913|১৯১৩"], 2, "It was announced in 1911.|১৯১১ত ঘোষণা কৰা হৈছিল।"),
 TF("Swadeshi meant boycotting British goods.|স্বদেশী মানে ব্ৰিটিছ বস্তু বৰ্জন।", True, "And buying Indian goods.|আৰু ভাৰতীয় বস্তু কিনা।"),
 WH(["I was Viceroy in 1905.|মই ১৯০৫ত ভাইচৰয় আছিলোঁ।", "I partitioned Bengal.|মই বংগ বিভাজন কৰিছিলোঁ।"], ["Curzon|কাৰ্জন", "Chelmsford|চেমছফৰ্ড", "Irwin|আৰউইন", "Canning|কেনিং"], 0, "Lord Curzon.|লৰ্ড কাৰ্জন।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Partition of Bengal|বংগ বিভাজন", "Delhi Durbar|দিল্লী দৰবাৰ", "Rowlatt Act|ৰাউলাট আইন"], "1905, 1911, 1919.|১৯০৫, ১৯১১, ১৯১৯।"),
)
u2 = U(2, "star", "Lal, Bal and Pal|লাল, বাল আৰু পাল",
 "Name the radicals and their slogan.|চৰমপন্থী আৰু তেওঁলোকৰ শ্লোগান জানা।", "Finding recorded: Tilak's slogan, Lal Bal Pal, the Surat split.|প্ৰমাণ লিখা হ'ল: তিলকৰ শ্লোগান, লাল-বাল-পাল, চুৰাট বিভাজন।",
 ["Lal Bal Pal were Lajpat Rai, Tilak and Bipin Chandra Pal|লাল-বাল-পাল হ'ল লাজপত ৰায়, তিলক আৰু বিপিনচন্দ্ৰ পাল", "Papers link the Swaraj birthright slogan with Tilak|পৰীক্ষাত স্বৰাজৰ জন্মসিদ্ধ অধিকাৰৰ শ্লোগান তিলকৰ সৈতে", "Papers name Aurobindo for passive resistance|পৰীক্ষাত নিষ্ক্ৰিয় প্ৰতিৰোধৰ বাবে অৰবিন্দ", "Tilak was jailed at Mandalay from 1908 to 1914|১৯০৮ৰ পৰা ১৯১৪লৈ তিলক মাণ্ডালয়ত বন্দী"],
 S("Three radicals|তিনিজন চৰমপন্থী", "<b>Lal</b>a Lajpat Rai, <b>Bal</b> Gangadhar Tilak and Bipin Chandra <b>Pal</b> pressed for self-rule. They split from the moderates at Surat in 1907.|<b>লালা</b> লাজপত ৰায়, <b>বাল</b> গংগাধৰ তিলক আৰু বিপিনচন্দ্ৰ <b>পালে</b> স্বৰাজৰ বাবে হেঁচা দিছিল। ১৯০৭ত চুৰাটত তেওঁলোক মধ্যপন্থীৰ পৰা পৃথক হৈছিল।", art="door"),
 S("A slogan and a theory|শ্লোগান আৰু তত্ত্ব", "Papers give <mark>Tilak</mark> the slogan that Swaraj is a birthright, though one account credits an associate with coining it.|পৰীক্ষাত স্বৰাজ জন্মসিদ্ধ অধিকাৰৰ শ্লোগান <mark>তিলকক</mark> দিয়ে, যদিও এটা বিৱৰণ মতে তেওঁৰ সহযোগীয়ে ইয়াক গঢ়িছিল।", "<mark>Aurobindo Ghosh</mark> set out the Doctrine of Passive Resistance in the paper Bande Mataram in April 1907.|<mark>অৰবিন্দ ঘোষে</mark> ১৯০৭ৰ এপ্ৰিলত বন্দে মাতৰম কাকতত নিষ্ক্ৰিয় প্ৰতিৰোধৰ মতবাদ লিখিছিল।", art="seal"),
 IN("Papers link 'Freedom is my birthright' with|পৰীক্ষাত 'স্বাধীনতা মোৰ জন্মসিদ্ধ অধিকাৰ' জড়িত", ".|ৰ সৈতে।", ["Chandra Sekhar Azad|চন্দ্ৰশেখৰ আজাদ", "Bal Gangadhar Tilak|বাল গংগাধৰ তিলক", "Gopal Krishna Gokhale|গোপাল কৃষ্ণ গোখলে", "Bhagat Singh|ভগত সিং"], 1, "Tilak.|তিলক।"),
 IN("APSC names the first propounder of 'passive resistance' as|APSCয়ে নিষ্ক্ৰিয় প্ৰতিৰোধৰ প্ৰথম প্ৰৱক্তা বুলিছে", ".|ক।", ["Tilak|তিলক", "Aurobindo Ghosh|অৰবিন্দ ঘোষ", "Gokhale|গোখলে", "Gandhi|গান্ধী"], 1, "Aurobindo Ghosh, by the APSC key.|APSCৰ উত্তৰ মতে অৰবিন্দ ঘোষ।"),
 MA([("Lal|লাল", "Lajpat Rai|লাজপত ৰায়"), ("Bal|বাল", "Tilak|তিলক"), ("Pal|পাল", "Bipin Chandra Pal|বিপিনচন্দ্ৰ পাল")], "The trio.|তিনিজন।"),
 TF("Gandhi was one of Lal Bal Pal.|গান্ধী লাল-বাল-পালৰ এজন আছিল।", False, "The three are Lajpat Rai, Tilak and Pal.|তিনিজন লাজপত ৰায়, তিলক আৰু পাল।"),
 SP("Tilak was jailed at *Andaman* from 1908.|১৯০৮ৰ পৰা তিলক *আন্দামানত* বন্দী আছিল।", "Mandalay|মাণ্ডালয়ত", "At Mandalay.|মাণ্ডালয়ত।"),
)
u3 = U(3, "houses", "New organisations|নতুন সংগঠন",
 "Place the League, the Mahasabha and the 1909 Act.|লীগ, মহাসভা আৰু ১৯০৯ৰ আইন স্থাপন কৰা।", "Finding recorded: League 1906, separate electorates 1909, Mahasabha 1915.|প্ৰমাণ লিখা হ'ল: ১৯০৬ত লীগ, ১৯০৯ত পৃথক নিৰ্বাচন, ১৯১৫ত মহাসভা।",
 ["The Muslim League was founded at Dacca in 1906|১৯০৬ত ঢাকাত মুছলিম লীগ প্ৰতিষ্ঠিত", "The 1909 Act brought separate electorates|১৯০৯ৰ আইনে পৃথক নিৰ্বাচন আনিছিল", "The Hindu Mahasabha dates from 1915 at Haridwar|হিন্দু মহাসভা ১৯১৫ত হৰিদ্বাৰত", "Malaviya led its founding|মালৱীয়ে ইয়াৰ প্ৰতিষ্ঠাত নেতৃত্ব দিছিল"],
 S("Dacca, 1906|ঢাকা, ১৯০৬", "The <mark>Muslim League</mark> was formed at [[dhaka|Dacca]] on 30 December 1906. It pressed for separate electorates, which the <mark>Act of 1909</mark> granted.|১৯০৬ৰ ৩০ ডিচেম্বৰত [[dhaka|ঢাকাত]] <mark>মুছলিম লীগ</mark> গঠিত হৈছিল। ই পৃথক নিৰ্বাচন বিচাৰিছিল, <mark>১৯০৯ৰ আইনে</mark> সেয়া দিছিল।", art="court"),
 S("Haridwar, 1915|হৰিদ্বাৰ, ১৯১৫", "The <mark>Hindu Mahasabha</mark> was organised at [[haridwar]] in 1915, with [[madan-mohan-malaviya|Madan Mohan Malaviya]] at its head.|১৯১৫ত [[haridwar|হৰিদ্বাৰত]] <mark>হিন্দু মহাসভা</mark> সংগঠিত হৈছিল, মূৰত [[madan-mohan-malaviya|মদন মোহন মালৱীয়]] আছিল।", art="houses"),
 IN("The Hindu Mahasabha was first organised in 1915 at|১৯১৫ত হিন্দু মহাসভা প্ৰথম সংগঠিত হৈছিল", ".|ত।", ["Haridwar|হৰিদ্বাৰ", "Allahabad|এলাহাবাদ", "Varanasi|বাৰাণসী", "Delhi|দিল্লী"], 0, "Haridwar.|হৰিদ্বাৰ।"),
 MP("Tap Dacca.|ঢাকা টিপা।", "dhaka", ["dhaka", "haridwar", "bombay", "lahore"], "In today's Bangladesh.|আজিৰ বাংলাদেশত।"),
 MA([("1906|১৯০৬", "Muslim League|মুছলিম লীগ"), ("1909|১৯০৯", "Separate electorates|পৃথক নিৰ্বাচন"), ("1915|১৯১৫", "Hindu Mahasabha|হিন্দু মহাসভা")], "Year and event.|বছৰ আৰু ঘটনা।"),
 TF("The Act of 1909 granted separate electorates.|১৯০৯ৰ আইনে পৃথক নিৰ্বাচন দিছিল।", True, "Under Morley and Minto.|মৰ্লে আৰু মিণ্টোৰ দিনত।"),
 SP("The Muslim League was founded at *Lahore.*|মুছলিম লীগ *লাহোৰত* প্ৰতিষ্ঠিত হৈছিল।", "Dacca|ঢাকাত", "At Dacca.|ঢাকাত।"),
)
u4 = U(4, "hands", "Home Rule and Lucknow|হোম ৰুল আৰু লক্ষ্ণৌ",
 "See the two wings close ranks.|দুয়ো পক্ষ কেনেকৈ ওচৰ চাপিল, চোৱা।", "Finding recorded: Home Rule Leagues and the Lucknow Pact in 1916.|প্ৰমাণ লিখা হ'ল: ১৯১৬ত হোম ৰুল লীগ আৰু লক্ষ্ণৌ চুক্তি।",
 ["Tilak was released in 1914|১৯১৪ত তিলক মুক্তি পাইছিল", "Tilak and Annie Besant led Home Rule in 1916|১৯১৬ত তিলক আৰু এনি বেচান্তে হোম ৰুলৰ নেতৃত্ব দিছিল", "The Lucknow Pact came in 1916|১৯১৬ত লক্ষ্ণৌ চুক্তি", "Papers name Lajpat Rai with Punjab National Bank|পৰীক্ষাত পঞ্জাব নেচনেল বেংকৰ সৈতে লাজপত ৰায়"],
 S("Home Rule|হোম ৰুল", "Released in 1914, [[bal-gangadhar-tilak|Tilak]] worked with [[annie-besant|Annie Besant]] on the <mark>Home Rule</mark> campaign from 1916.|১৯১৪ত মুক্তি পোৱাৰ পিছত [[bal-gangadhar-tilak|তিলকে]] ১৯১৬ৰ পৰা [[annie-besant|এনি বেচান্তৰ]] সৈতে <mark>হোম ৰুল</mark> অভিযান চলাইছিল।", art="scroll"),
 S("Lucknow, 1916|লক্ষ্ণৌ, ১৯১৬", "In 1916 the Congress and the League came together in the <mark>Lucknow Pact</mark>.|১৯১৬ত <mark>লক্ষ্ণৌ চুক্তিত</mark> কংগ্ৰেছ আৰু লীগ একত্ৰিত হৈছিল।", "A TET paper names [[lala-lajpat-rai|Lala Lajpat Rai]] as founder of Punjab National Bank. Sources say he was linked with its early management in 1894.|এখন TET প্ৰশ্নকাকতত [[lala-lajpat-rai|লালা লাজপত ৰায়ক]] পঞ্জাব নেচনেল বেংকৰ প্ৰতিষ্ঠাপক বোলা হৈছে। উৎস মতে তেওঁ ১৮৯৪ত ইয়াৰ আদি পৰিচালনাৰ সৈতে জড়িত।", art="seal"),
 IN("The Congress and the League joined in the|কংগ্ৰেছ আৰু লীগ একত্ৰিত হৈছিল", " of 1916.|ত, ১৯১৬।", ["Surat split|চুৰাট বিভাজন", "Lucknow Pact|লক্ষ্ণৌ চুক্তি", "Poona Pact|পুণা চুক্তি", "Gandhi-Irwin Pact|গান্ধী-আৰউইন চুক্তি"], 1, "The Lucknow Pact.|লক্ষ্ণৌ চুক্তি।"),
 WH(["I led Home Rule with Tilak.|মই তিলকৰ সৈতে হোম ৰুলৰ নেতৃত্ব দিছিলোঁ।"], ["Annie Besant|এনি বেচান্ত", "Sarojini Naidu|চৰোজিনী নাইডু", "Razia Sultana|ৰাজিয়া ছুলতানা", "Rani Lakshmibai|ৰাণী লক্ষ্মীবাই"], 0, "Annie Besant.|এনি বেচান্ত।"),
 TF("Papers link Punjab National Bank with Lala Lajpat Rai.|পৰীক্ষাত পঞ্জাব নেচনেল বেংক লালা লাজপত ৰায়ৰ সৈতে জড়িত।", True, "He was linked with its early management.|তেওঁ ইয়াৰ আদি পৰিচালনাৰ সৈতে জড়িত আছিল।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1905, "Partition of Bengal|বংগ বিভাজন"), (1916, "Lucknow Pact|লক্ষ্ণৌ চুক্তি")], [("Surat split, 1907|চুৰাট বিভাজন, ১৯০৭", 1), ("Capital to Delhi, 1911|দিল্লীলৈ ৰাজধানী, ১৯১১", 1), ("Rowlatt Act, 1919|ৰাউলাট আইন, ১৯১৯", 2)], "1905 → 1907 → 1911 → 1916 → 1919.|১৯০৫ → ১৯০৭ → ১৯১১ → ১৯১৬ → ১৯১৯।"),
 SP("The Lucknow Pact joined the Congress and the *Mahasabha.*|লক্ষ্ণৌ চুক্তিয়ে কংগ্ৰেছ আৰু *মহাসভাক* একত্ৰিত কৰিছিল।", "League|লীগক", "It was the Muslim League.|ই মুছলিম লীগ।"),
)
test = TEST("Trace eleven crowded years.|এঘাৰ ব্যস্ত বছৰ অনুসৰণ কৰা।", "Recorded: Swadeshi, radicals, League and Lucknow.|লিখা হ'ল: স্বদেশী, চৰমপন্থী, লীগ আৰু লক্ষ্ণৌ।",
 OR("Order these.|এইবোৰ সজোৱা।", ["Partition of Bengal|বংগ বিভাজন", "Muslim League|মুছলিম লীগ", "Surat split|চুৰাট বিভাজন", "Lucknow Pact|লক্ষ্ণৌ চুক্তি"], "1905, 1906, 1907, 1916.|১৯০৫, ১৯০৬, ১৯০৭, ১৯১৬।"),
 IN("The word that means own-country goods is|নিজ দেশৰ বস্তু বুজোৱা শব্দ", ".|।", ["Swadeshi|স্বদেশী", "Swaraj|স্বৰাজ", "Satyagraha|সত্যাগ্ৰহ", "Hartal|হৰতাল"], 0, "Swadeshi.|স্বদেশী।"),
 MA([("Curzon|কাৰ্জন", "Partition of Bengal|বংগ বিভাজন"), ("Tilak|তিলক", "Home Rule|হোম ৰুল"), ("Malaviya|মালৱীয়", "Hindu Mahasabha|হিন্দু মহাসভা")], "Name and event.|নাম আৰু ঘটনা।"),
 TF("The Partition of Bengal was annulled in 1911.|১৯১১ত বংগ বিভাজন বাতিল হৈছিল।", True, "At the Delhi Durbar.|দিল্লী দৰবাৰত।"),
 MP("Tap Haridwar.|হৰিদ্বাৰ টিপা।", "haridwar", ["haridwar", "dhaka", "bombay", "lahore"], "On the Ganga.|গংগা পাৰত।"),
 MC("Consider these statements. (1) Assam joined Eastern Bengal and Assam in 1905. (2) The League was founded at Dacca. (3) The capital moved to Delhi in 1905. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ১৯০৫ত অসম পূব বংগ আৰু অসমৰ অংশ হৈছিল। (২) লীগ ঢাকাত প্ৰতিষ্ঠিত। (৩) ১৯০৫ত ৰাজধানী দিল্লীলৈ গৈছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 0, "The move was announced in 1911.|১৯১১ত ঘোষণা কৰা হৈছিল।"),
)
LESSON(24, "Swadeshi to Lucknow|স্বদেশীৰ পৰা লক্ষ্ণৌলৈ", "1905–1916|১৯০৫–১৯১৬", "The national movement|ৰাষ্ট্ৰীয় আন্দোলন", "Evidence file 24|প্ৰমাণ নথি ২৪", "A line on a map|মানচিত্ৰত এডাল ৰেখা",
 "One line across Bengal set off boycotts, slogans, new parties and a change of capital.|বংগৰ মাজৰ এডাল ৰেখাই বৰ্জন, শ্লোগান, নতুন দল আৰু ৰাজধানী সলনি আনিলে।",
 sources, [u1, u2, u3, u4], test, ["dhaka", "haridwar", "bombay", "lahore"],
 timeline=[("1905", "Partition of Bengal|বংগ বিভাজন", "u1"), ("1906", "Muslim League|মুছলিম লীগ", "u3"), ("1911", "Partition annulled|বিভাজন বাতিল", "u1"), ("1916", "Lucknow Pact|লক্ষ্ণৌ চুক্তি", "u4")])
