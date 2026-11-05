#!/usr/bin/env python3
"""Lesson 23: The early Congress."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "ao-hume": ("person", "A. O. Hume|এ. অ'. হিউম", "Retired civil servant who helped organise the first Congress|প্ৰথম কংগ্ৰেছ আয়োজনত সহায় কৰা অৱসৰপ্ৰাপ্ত বিষয়া"),
 "wc-bonnerjee": ("person", "W. C. Bonnerjee|উমেশচন্দ্ৰ বন্দ্যোপাধ্যায়", "First president of the Indian National Congress|ভাৰতীয় ৰাষ্ট্ৰীয় কংগ্ৰেছৰ প্ৰথম সভাপতি"),
 "dadabhai-naoroji": ("person", "Dadabhai Naoroji|দাদাভাই নৌৰজী", "Grand Old Man of India, author of the drain theory|ভাৰতৰ বৃদ্ধ পিতামহ, ধন নিষ্কাশন তত্ত্বৰ লেখক"),
 "gopal-krishna-gokhale": ("person", "Gopal Krishna Gokhale|গোপাল কৃষ্ণ গোখলে", "Moderate leader and mentor of Gandhi|মধ্যপন্থী নেতা, গান্ধীৰ পথপ্ৰদৰ্শক"),
 "indian-national-congress": ("term", "Indian National Congress|ভাৰতীয় ৰাষ্ট্ৰীয় কংগ্ৰেছ", "Founded at Bombay in December 1885|১৮৮৫ৰ ডিচেম্বৰত বোম্বেত প্ৰতিষ্ঠিত"),
})
sources = [
 src("Wikipedia, Indian National Congress", "https://en.wikipedia.org/wiki/Indian_National_Congress", "Used as a guide: 28 December 1885, Bombay, Hume, Bonnerjee, 72 delegates. Check in review."),
 src("Wikipedia, Dadabhai Naoroji", "https://en.wikipedia.org/wiki/Dadabhai_Naoroji", "Used as a guide: Grand Old Man, drain, 1892, 1901, president in 1886, 1893 and 1906. The Swaraj line of 1906 rests on the SI 2025 paper and was not confirmed in this page. Check in review."),
]
u1 = U(1, "court", "Bombay, 1885|বোম্বে, ১৮৮৫",
 "Fix the founding facts of the Congress.|কংগ্ৰেছৰ প্ৰতিষ্ঠাৰ তথ্য মনত ৰাখা।", "Finding recorded: 28 December 1885, Bombay, Bonnerjee presiding.|প্ৰমাণ লিখা হ'ল: ১৮৮৫ৰ ২৮ ডিচেম্বৰ, বোম্বে, সভাপতি বন্দ্যোপাধ্যায়।",
 ["The Congress was founded on 28 December 1885|১৮৮৫ৰ ২৮ ডিচেম্বৰত কংগ্ৰেছ প্ৰতিষ্ঠিত", "The first session met at Bombay|প্ৰথম অধিৱেশন বোম্বেত", "A. O. Hume helped organise it|এ. অ'. হিউমে আয়োজনত সহায় কৰিছিল", "W. C. Bonnerjee was first president|উমেশচন্দ্ৰ বন্দ্যোপাধ্যায় প্ৰথম সভাপতি"],
 S("Seventy-two delegates|বাসত্তৰজন প্ৰতিনিধি", "The [[indian-national-congress|Indian National Congress]] first met at [[bombay]] on 28 December <mark>1885</mark>, with 72 delegates, mostly lawyers.|[[indian-national-congress|ভাৰতীয় ৰাষ্ট্ৰীয় কংগ্ৰেছ]] <mark>১৮৮৫ৰ</mark> ২৮ ডিচেম্বৰত [[bombay|বোম্বেত]] প্ৰথমবাৰ বহিছিল, ৭২ জন প্ৰতিনিধি, বেছিভাগ উকীল।", art="court"),
 S("Who did what|কোনে কি কৰিলে", "[[ao-hume|A. O. Hume]], a retired civil servant, helped organise it. <mark>[[wc-bonnerjee|W. C. Bonnerjee]]</mark> was its first president.|অৱসৰপ্ৰাপ্ত বিষয়া [[ao-hume|এ. অ'. হিউমে]] আয়োজনত সহায় কৰিছিল। <mark>[[wc-bonnerjee|উমেশচন্দ্ৰ বন্দ্যোপাধ্যায়]]</mark> প্ৰথম সভাপতি।", art="seal"),
 IN("The Indian National Congress was founded in|ভাৰতীয় ৰাষ্ট্ৰীয় কংগ্ৰেছ প্ৰতিষ্ঠিত হৈছিল", ".|ত।", ["1857|১৮৫৭", "1885|১৮৮৫", "1905|১৯০৫", "1906|১৯০৬"], 1, "1885.|১৮৮৫।"),
 MP("Tap the city of the first session.|প্ৰথম অধিৱেশনৰ চহৰখন টিপা।", "bombay", ["bombay", "calcutta", "delhi", "lahore"], "Bombay.|বোম্বে।"),
 MA([("A. O. Hume|এ. অ'. হিউম", "Helped organise|আয়োজনত সহায়"), ("W. C. Bonnerjee|উমেশচন্দ্ৰ বন্দ্যোপাধ্যায়", "First president|প্ৰথম সভাপতি")], "Two founding roles.|প্ৰতিষ্ঠাৰ দুটা ভূমিকা।"),
 TF("Hume was the first Congress president.|হিউম কংগ্ৰেছৰ প্ৰথম সভাপতি আছিল।", False, "Bonnerjee was.|বন্দ্যোপাধ্যায় আছিল।"),
 SP("The first session met at *Calcutta.*|প্ৰথম অধিৱেশন *কলিকতাত* বহিছিল।", "Bombay|বোম্বেত", "Bombay.|বোম্বে।"),
)
u2 = U(2, "scroll", "The moderates' case|মধ্যপন্থীৰ যুক্তি",
 "See what the early Congress asked for.|প্ৰাৰম্ভিক কংগ্ৰেছে কি বিচাৰিছিল, চোৱা।", "Finding recorded: moderates sought reform within the Empire.|প্ৰমাণ লিখা হ'ল: মধ্যপন্থীয়ে সাম্ৰাজ্যৰ ভিতৰত সংস্কাৰ বিচাৰিছিল।",
 ["Early leaders were moderates|প্ৰাৰম্ভিক নেতা মধ্যপন্থী", "They sought constitutional reform|তেওঁলোকে সাংবিধানিক সংস্কাৰ বিচাৰিছিল", "They worked through petitions and argument|তেওঁলোকে আবেদন আৰু যুক্তিৰে কাম কৰিছিল", "Gokhale was a leading moderate|গোখলে এজন মুখ্য মধ্যপন্থী"],
 S("Reform, not revolt|বিদ্ৰোহ নহয়, সংস্কাৰ", "Early Congress leaders were <mark>moderates</mark> who sought constitutional reform inside the British Empire.|প্ৰাৰম্ভিক কংগ্ৰেছ নেতা <mark>মধ্যপন্থী</mark> আছিল, তেওঁলোকে ব্ৰিটিছ সাম্ৰাজ্যৰ ভিতৰত সাংবিধানিক সংস্কাৰ বিচাৰিছিল।", art="court"),
 S("A mentor|পথপ্ৰদৰ্শক", "[[gopal-krishna-gokhale|Gopal Krishna Gokhale]] was a leading moderate. He later introduced Gandhi to Indian politics.|[[gopal-krishna-gokhale|গোপাল কৃষ্ণ গোখলে]] এজন মুখ্য মধ্যপন্থী। পিছত তেওঁ গান্ধীক ভাৰতীয় ৰাজনীতিৰ সৈতে চিনাকি কৰাইছিল।", art="door"),
 TF("The early Congress demanded full independence.|প্ৰাৰম্ভিক কংগ্ৰেছে সম্পূৰ্ণ স্বাধীনতা বিচাৰিছিল।", False, "It sought reform inside the Empire.|ই সাম্ৰাজ্যৰ ভিতৰত সংস্কাৰ বিচাৰিছিল।"),
 IN("Gandhi's political mentor was|গান্ধীৰ ৰাজনৈতিক পথপ্ৰদৰ্শক", ".|।", ["Gopal Krishna Gokhale|গোপাল কৃষ্ণ গোখলে", "A. O. Hume|এ. অ'. হিউম", "Bal Gangadhar Tilak|বাল গংগাধৰ তিলক", "Motilal Nehru|মতিলাল নেহৰু"], 0, "Gokhale.|গোখলে।"),
 OD("Which method fits the early moderates?|কোনটো পদ্ধতি প্ৰাৰম্ভিক মধ্যপন্থীৰ?", ["Petitions|আবেদন", "Bomb attacks|বোমা আক্ৰমণ", "Salt marches|লৱণ যাত্ৰা", "Quit India|ভাৰত ত্যাগ"], 0, "They used petitions and argument.|তেওঁলোকে আবেদন আৰু যুক্তি ব্যৱহাৰ কৰিছিল।"),
 SC("Unscramble the moderate leader.|মধ্যপন্থী নেতাক সজোৱা।", "GOKHALE", ["গো", "খ", "লে"], "Gokhale.|গোখলে।"),
 WH(["I was a moderate.|মই মধ্যপন্থী।", "I guided Gandhi into Indian politics.|মই গান্ধীক ভাৰতীয় ৰাজনীতিত আনিছিলোঁ।"], ["Tilak|তিলক", "Gokhale|গোখলে", "Hume|হিউম", "Naoroji|নৌৰজী"], 1, "Gokhale.|গোখলে।"),
)
u3 = U(3, "star", "The drain|ধন নিষ্কাশন",
 "State the economic case against British rule.|ব্ৰিটিছ শাসনৰ বিৰুদ্ধে অৰ্থনৈতিক যুক্তি কোৱা।", "Finding recorded: Naoroji argued British rule drained India's wealth.|প্ৰমাণ লিখা হ'ল: নৌৰজীয়ে ব্ৰিটিছ শাসনে ভাৰতৰ ধন নিষ্কাশন কৰে বুলি কৈছিল।",
 ["Naoroji is the Grand Old Man of India|নৌৰজী ভাৰতৰ বৃদ্ধ পিতামহ", "He wrote Poverty and Un-British Rule in India|তেওঁ পভাৰ্টি এণ্ড আন-ব্ৰিটিছ ৰুল ইন ইণ্ডিয়া লিখিছিল", "He argued that wealth drained to Britain|তেওঁ ধন ব্ৰিটেইনলৈ যায় বুলি যুক্তি দিছিল", "He became a British MP in 1892|১৮৯২ত তেওঁ ব্ৰিটিছ সাংসদ হৈছিল"],
 S("Wealth leaving India|ভাৰতৰ পৰা ওলাই যোৱা ধন", "<mark>[[dadabhai-naoroji|Dadabhai Naoroji]]</mark>, the Grand Old Man of India, argued in <mark>Poverty and Un-British Rule in India</mark> that British rule drained wealth to Britain.|ভাৰতৰ বৃদ্ধ পিতামহ <mark>[[dadabhai-naoroji|দাদাভাই নৌৰজীয়ে]]</mark> <mark>পভাৰ্টি এণ্ড আন-ব্ৰিটিছ ৰুল ইন ইণ্ডিয়াত</mark> ব্ৰিটিছ শাসনে ধন ব্ৰিটেইনলৈ নিয়ে বুলি যুক্তি দিছিল।", art="scroll"),
 S("An MP in London|লণ্ডনত সাংসদ", "In 1892 he won a seat for Finsbury Central, the first British Indian MP. He was Congress president three times.|১৮৯২ত তেওঁ ফিনচবাৰি চেণ্ট্ৰেলৰ পৰা জিকি প্ৰথম ব্ৰিটিছ ভাৰতীয় সাংসদ হৈছিল। তেওঁ তিনিবাৰ কংগ্ৰেছ সভাপতি।", art="embassy"),
 WH(["I am the Grand Old Man of India.|মই ভাৰতৰ বৃদ্ধ পিতামহ।", "I argued the drain theory.|মই ধন নিষ্কাশন তত্ত্ব দিছিলোঁ।", "I sat in the British Parliament.|মই ব্ৰিটিছ সংসদত আছিলোঁ।"], ["Naoroji|নৌৰজী", "Gokhale|গোখলে", "Bonnerjee|বন্দ্যোপাধ্যায়", "Hume|হিউম"], 0, "Dadabhai Naoroji.|দাদাভাই নৌৰজী।"),
 IN("The drain theory is linked with|ধন নিষ্কাশন তত্ত্ব জড়িত", ".|ৰ সৈতে।", ["Macaulay|মেকলে", "Dadabhai Naoroji|দাদাভাই নৌৰজী", "Curzon|কাৰ্জন", "Gandhi|গান্ধী"], 1, "Naoroji.|নৌৰজী।"),
 TF("Naoroji was elected to the British Parliament.|নৌৰজী ব্ৰিটিছ সংসদলৈ নিৰ্বাচিত হৈছিল।", True, "In 1892.|১৮৯২ত।"),
 SP("Naoroji wrote on the drain of wealth to *France.*|নৌৰজীয়ে *ফ্ৰান্সলৈ* ধন নিষ্কাশনৰ বিষয়ে লিখিছিল।", "Britain|ব্ৰিটেইনলৈ", "To Britain.|ব্ৰিটেইনলৈ।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["First Congress|প্ৰথম কংগ্ৰেছ", "Naoroji becomes an MP|নৌৰজী সাংসদ", "Poverty and Un-British Rule|পভাৰ্টি এণ্ড আন-ব্ৰিটিছ ৰুল"], "1885, 1892, 1901.|১৮৮৫, ১৮৯২, ১৯০১।"),
)
u4 = U(4, "flag", "Swaraj at Calcutta|কলিকতাত স্বৰাজ",
 "Fix the first use of Swaraj in Congress.|কংগ্ৰেছত স্বৰাজৰ প্ৰথম ব্যৱহাৰ মনত ৰাখা।", "Finding recorded: papers link Swaraj to Naoroji at Calcutta in 1906.|প্ৰমাণ লিখা হ'ল: পৰীক্ষাত স্বৰাজক ১৯০৬ত কলিকতাত নৌৰজীৰ সৈতে জড়িত কৰা হয়।",
 ["Papers link Swaraj with Calcutta, 1906|পৰীক্ষাত স্বৰাজক ১৯০৬ৰ কলিকতাৰ সৈতে জড়িত কৰে", "Naoroji presided at that session|নৌৰজীয়ে সেই অধিৱেশনত সভাপতিত্ব কৰিছিল", "Moderates and extremists were dividing|মধ্যপন্থী আৰু চৰমপন্থী বিভক্ত হৈছিল", "The split came at Surat in 1907|১৯০৭ত চুৰাটত বিভাজন হৈছিল"],
 S("A new word|নতুন শব্দ", "At <mark>Calcutta in 1906</mark> Naoroji named <mark>[[swaraj|Swaraj]]</mark> as the goal. Gokhale had spoken of self-rule in 1905, but papers want Naoroji.|<mark>১৯০৬ত কলিকতাত</mark> নৌৰজীয়ে <mark>[[swaraj|স্বৰাজক]]</mark> লক্ষ্য বুলি ঘোষণা কৰিছিল। ১৯০৫ত গোখলেয়েও স্বায়ত্ত শাসনৰ কথা কৈছিল, কিন্তু পৰীক্ষাত নৌৰজীৰ নাম বিচাৰে।", art="seal"),
 S("Pressure inside|ভিতৰৰ হেঁচা", "Younger radicals wanted more than petitions. The quarrel broke open at <mark>[[surat|Surat]] in 1907</mark>, your next lesson.|ডেকা চৰমপন্থীয়ে আবেদনতকৈ বেছি বিচাৰিছিল। বিবাদ <mark>১৯০৭ত [[surat|চুৰাটত]]</mark> ফুটি উঠিল, পৰৱৰ্তী পাঠ।", art="door"),
 IN("Papers say Swaraj was first used in Congress by Naoroji at|পৰীক্ষাত নৌৰজীয়ে স্বৰাজ প্ৰথম ব্যৱহাৰ কৰা ঠাই", ".|ত।", ["1904, Bombay|১৯০৪, বোম্বে", "1906, Calcutta|১৯০৬, কলিকতা", "1907, Surat|১৯০৭, চুৰাট", "1916, Lucknow|১৯১৬, লক্ষ্ণৌ"], 1, "1906, Calcutta.|১৯০৬, কলিকতা।"),
 MA([("Bombay, 1885|বোম্বে, ১৮৮৫", "First session|প্ৰথম অধিৱেশন"), ("Calcutta, 1906|কলিকতা, ১৯০৬", "Swaraj|স্বৰাজ"), ("Surat, 1907|চুৰাট, ১৯০৭", "Split|বিভাজন")], "Session and event.|অধিৱেশন আৰু ঘটনা।"),
 TF("The Congress split at Surat in 1907.|১৯০৭ত চুৰাটত কংগ্ৰেছ বিভক্ত হৈছিল।", True, "Moderates and extremists parted.|মধ্যপন্থী আৰু চৰমপন্থী পৃথক হৈছিল।"),
 MP("Tap Calcutta.|কলিকতা টিপা।", "calcutta", ["calcutta", "bombay", "delhi", "lahore"], "Calcutta.|কলিকতা।"),
 OR("Order the sessions.|অধিৱেশনবোৰ সজোৱা।", ["Bombay|বোম্বে", "Calcutta|কলিকতা", "Surat|চুৰাট"], "1885, 1906, 1907.|১৮৮৫, ১৯০৬, ১৯০৭।"),
)
test = TEST("Sum up the early Congress.|প্ৰাৰম্ভিক কংগ্ৰেছৰ সাৰাংশ দিয়া।", "Recorded: founding, moderates, drain and Swaraj.|লিখা হ'ল: প্ৰতিষ্ঠা, মধ্যপন্থী, ধন নিষ্কাশন আৰু স্বৰাজ।",
 IN("The first president of the Congress was|কংগ্ৰেছৰ প্ৰথম সভাপতি", ".|।", ["W. C. Bonnerjee|উমেশচন্দ্ৰ বন্দ্যোপাধ্যায়", "A. O. Hume|এ. অ'. হিউম", "Dadabhai Naoroji|দাদাভাই নৌৰজী", "Gokhale|গোখলে"], 0, "Bonnerjee.|বন্দ্যোপাধ্যায়।"),
 TF("The Congress began at Bombay.|কংগ্ৰেছ বোম্বেত আৰম্ভ হৈছিল।", True, "In 1885.|১৮৮৫ত।"),
 MP("Tap Bombay.|বোম্বে টিপা।", "bombay", ["bombay", "calcutta", "delhi", "lahore"], "Bombay.|বোম্বে।"),
 MA([("Grand Old Man|বৃদ্ধ পিতামহ", "Naoroji|নৌৰজী"), ("Gandhi's mentor|গান্ধীৰ পথপ্ৰদৰ্শক", "Gokhale|গোখলে"), ("Organiser|আয়োজক", "Hume|হিউম")], "Label and name.|পৰিচয় আৰু নাম।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Revolt of 1857|১৮৫৭ৰ বিদ্ৰোহ", "First Congress|প্ৰথম কংগ্ৰেছ", "Surat split|চুৰাট বিভাজন"], "1857, 1885, 1907.|১৮৫৭, ১৮৮৫, ১৯০৭।"),
 MC("Consider these statements. (1) Naoroji argued the drain theory. (2) The early moderates demanded full independence. (3) The Congress split at Surat. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) নৌৰজীয়ে ধন নিষ্কাশন তত্ত্ব দিছিল। (২) প্ৰাৰম্ভিক মধ্যপন্থীয়ে সম্পূৰ্ণ স্বাধীনতা বিচাৰিছিল। (৩) চুৰাটত কংগ্ৰেছ বিভক্ত হৈছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "They sought reform within the Empire.|তেওঁলোকে সাম্ৰাজ্যৰ ভিতৰত সংস্কাৰ বিচাৰিছিল।"),
)
LESSON(23, "The early Congress|প্ৰাৰম্ভিক কংগ্ৰেছ", "1885–1907|১৮৮৫–১৯০৭", "The national movement|ৰাষ্ট্ৰীয় আন্দোলন", "Evidence file 23|প্ৰমাণ নথি ২৩", "Lawyers against an empire|সাম্ৰাজ্যৰ বিৰুদ্ধে উকীল",
 "The national movement began with 72 delegates, petitions and an argument about money. See how far that went.|৭২ জন প্ৰতিনিধি, আবেদন আৰু ধনৰ যুক্তিৰে ৰাষ্ট্ৰীয় আন্দোলন আৰম্ভ হৈছিল। ই কিমান দূৰ গ'ল, চোৱা।",
 sources, [u1, u2, u3, u4], test, ["bombay", "calcutta", "delhi", "lahore"],
 timeline=[("1885", "Congress founded|কংগ্ৰেছ প্ৰতিষ্ঠা", "u1"), ("1892", "Naoroji becomes an MP|নৌৰজী সাংসদ", "u3"), ("1906", "Calcutta session|কলিকতা অধিৱেশন", "u4")])
