#!/usr/bin/env python3
"""Lesson 31: The road to 1947."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "lord-wavell": ("person", "Lord Wavell|লৰ্ড ৱেভেল", "Viceroy who proposed the Wavell Plan of 1945|১৯৪৫ৰ ৱেভেল পৰিকল্পনাৰ ভাইচৰয়"),
 "lord-mountbatten": ("person", "Lord Mountbatten|লৰ্ড মাউণ্টবেটেন", "Last Viceroy, author of the plan of 3 June 1947|শেষ ভাইচৰয়, ১৯৪৭ৰ ৩ জুনৰ পৰিকল্পনাৰ লেখক"),
 "muhammad-ali-jinnah": ("person", "Muhammad Ali Jinnah|মহম্মদ আলী জিন্নাহ", "Leader of the Muslim League|মুছলিম লীগৰ নেতা"),
 "simla": ("place", "Simla|চিমলা", "Hill town of the conference of June 1945|১৯৪৫ৰ জুনৰ সন্মিলনৰ পাহাৰীয়া নগৰ", [31.1, 77.17]),
})
sources = [
 src("Wikipedia, Simla Conference", "https://en.wikipedia.org/wiki/Simla_Conference", "Used as a guide: 14 June 1945, terms, 25 June, failure over Muslim representation. Check in review."),
 src("Wikipedia, Royal Indian Navy mutiny", "https://en.wikipedia.org/wiki/Royal_Indian_Navy_mutiny", "Used as a guide: 18 February 1946, HMIS Talwar, Bombay. Check in review."),
 src("Wikipedia, Direct Action Day", "https://en.wikipedia.org/wiki/Direct_Action_Day", "Used as a guide: Cabinet Mission 16 May 1946, League's withdrawal, 16 August 1946, estimated deaths, spread of violence. Responsibility is disputed, so the lesson assigns none. Check in review."),
 src("Wikipedia, Mountbatten Plan", "https://en.wikipedia.org/wiki/Mountbatten_Plan", "Used as a guide: 3 June 1947, Bengal and Punjab divided, Independence Act, 14 and 15 August. Check in review."),
 src("APSC CCE Prelims 2023 GS-I, question 8", "https://apsc.nic.in/cce.html", "Order of Quit India, Wavell Plan, Navy Mutiny and Mountbatten Plan."),
]
u1 = U(1, "court", "Talks after the war|যুদ্ধৰ পিছৰ আলোচনা",
 "Fix the Wavell Plan and why it failed.|ৱেভেল পৰিকল্পনা আৰু ইয়াৰ বিফলতা মনত ৰাখা।", "Finding recorded: Simla, June 1945, failed over Muslim representation.|প্ৰমাণ লিখা হ'ল: চিমলা, ১৯৪৫ৰ জুন, মুছলিম প্ৰতিনিধিত্বৰ বিষয়ত বিফল।",
 ["The Wavell Plan was announced on 14 June 1945|১৯৪৫ৰ ১৪ জুনত ৱেভেল পৰিকল্পনা ঘোষণা", "It proposed an Indian Executive Council|ই ভাৰতীয় কাৰ্যনিৰ্বাহী পৰিষদৰ প্ৰস্তাৱ দিছিল", "The Simla Conference opened on 25 June|২৫ জুনত চিমলা সন্মিলন", "It failed over Muslim representation|মুছলিম প্ৰতিনিধিত্বৰ বিষয়ত ই বিফল হৈছিল"],
 S("An enlarged council|বৃহৎ পৰিষদ", "On 14 June <mark>1945</mark> [[lord-wavell|Lord Wavell]] announced a plan: a reconstituted Executive Council, with Indians in all posts but Viceroy and Commander-in-Chief.|<mark>১৯৪৫ৰ</mark> ১৪ জুনত [[lord-wavell|লৰ্ড ৱেভেলে]] পৰিকল্পনা ঘোষণা কৰিছিল: ভাইচৰয় আৰু প্ৰধান সেনাপতিৰ বাহিৰে সকলো পদত ভাৰতীয় থকা নতুন কাৰ্যনিৰ্বাহী পৰিষদ।", art="court"),
 S("Simla fails|চিমলা বিফল", "The <mark>Simla Conference</mark> opened on 25 June. [[muhammad-ali-jinnah|Jinnah]] insisted the League alone name Muslim members, Wavell could not accept that, and it ended without agreement.|২৫ জুনত <mark>চিমলা সন্মিলন</mark> আৰম্ভ হৈছিল। [[muhammad-ali-jinnah|জিন্নাহে]] কেৱল লীগে মুছলিম সদস্য দিব বুলি জোৰ দিছিল, ৱেভেলে মানিব নোৱাৰিলে, সন্মিলন বিফল হ'ল।", map={"base": "india", "box": [72, 27, 84, 34], "show": ["simla", "delhi"]}),
 IN("The Wavell Plan was announced in|ৱেভেল পৰিকল্পনা ঘোষণা হৈছিল", ".|ত।", ["1942|১৯৪২", "1945|১৯৪৫", "1946|১৯৪৬", "1947|১৯৪৭"], 1, "1945.|১৯৪৫।"),
 TF("The Simla Conference reached full agreement.|চিমলা সন্মিলনত সম্পূৰ্ণ সন্মতি হৈছিল।", False, "It failed over Muslim representation.|মুছলিম প্ৰতিনিধিত্বৰ বিষয়ত বিফল হৈছিল।"),
 MP("Tap Simla.|চিমলা টিপা।", "simla", ["simla", "bombay", "calcutta", "sylhet"], "In the Himalayan foothills.|হিমালয়ৰ পাদদেশত।"),
 WH(["I led the Muslim League.|মই মুছলিম লীগৰ নেতা।", "I insisted on naming all Muslim members.|মই সকলো মুছলিম সদস্য দিয়াৰ জোৰ দিছিলোঁ।"], ["Jinnah|জিন্নাহ", "Wavell|ৱেভেল", "Saadulla|চাদুল্লা", "Azad|আজাদ"], 0, "Jinnah.|জিন্নাহ।"),
 SP("The Wavell Plan was announced by Lord *Curzon.*|ৱেভেল পৰিকল্পনা লৰ্ড *কাৰ্জনে* ঘোষণা কৰিছিল।", "Wavell|ৱেভেলে", "By Wavell.|ৱেভেলে।"),
)
u2 = U(2, "flag", "Mutiny at Bombay|বোম্বেত বিদ্ৰোহ",
 "See why the British felt the ground move.|ব্ৰিটিছে কিয় ভেটি কঁপা অনুভৱ কৰিলে, চোৱা।", "Finding recorded: the naval ratings rose at Bombay in February 1946.|প্ৰমাণ লিখা হ'ল: ১৯৪৬ৰ ফেব্ৰুৱাৰীত বোম্বেত নৌসেনাৰ বিদ্ৰোহ।",
 ["The Navy Mutiny began on 18 February 1946|১৯৪৬ৰ ১৮ ফেব্ৰুৱাৰীত নৌ বিদ্ৰোহ", "It began at HMIS Talwar in Bombay|ই বোম্বেৰ HMIS তলৱাৰত আৰম্ভ হৈছিল", "It spread to 22 ships in a day|এদিনত ই ২২খন জাহাজলৈ বিয়পিছিল", "It came after the Wavell Plan|ই ৱেভেল পৰিকল্পনাৰ পিছত আহিছিল"],
 S("HMIS Talwar|HMIS তলৱাৰ", "On <mark>18 February 1946</mark> ratings at <mark>HMIS Talwar</mark>, a signals school in [[bombay]], refused orders.|<mark>১৯৪৬ৰ ১৮ ফেব্ৰুৱাৰীত</mark> [[bombay|বোম্বেৰ]] সংকেত বিদ্যালয় <mark>HMIS তলৱাৰৰ</mark> নাৱিকসকলে আদেশ অমান্য কৰিছিল।", art="door"),
 S("Twenty-two ships|বাইশখন জাহাজ", "Within a day the revolt reached 22 ships and 12 shore establishments in the harbour.|এদিনৰ ভিতৰতে বিদ্ৰোহ বন্দৰৰ ২২খন জাহাজ আৰু ১২টা স্থলভাগৰ প্ৰতিষ্ঠানলৈ বিয়পিছিল।", art="embassy"),
 TF("The Royal Indian Navy Mutiny began at Bombay.|ৰয়েল ইণ্ডিয়ান নেভী বিদ্ৰোহ বোম্বেত আৰম্ভ হৈছিল।", True, "At HMIS Talwar.|HMIS তলৱাৰত।"),
 IN("The Navy Mutiny took place in|নৌ বিদ্ৰোহ হৈছিল", ".|ত।", ["1942|১৯৪২", "1945|১৯৪৫", "1946|১৯৪৬", "1947|১৯৪৭"], 2, "1946.|১৯৪৬।"),
 OR("Put these in chronological order.|এইবোৰ কালানুক্ৰমে সজোৱা।", ["Quit India|ভাৰত ত্যাগ", "Wavell Plan|ৱেভেল পৰিকল্পনা", "Navy Mutiny|নৌ বিদ্ৰোহ", "Mountbatten Plan|মাউণ্টবেটেন পৰিকল্পনা"], "1942, 1945, 1946, 1947. APSC asked exactly this.|১৯৪২, ১৯৪৫, ১৯৪৬, ১৯৪৭। APSCয়ে ঠিক এইটো সুধিছিল।"),
 MP("Tap the city of the mutiny.|বিদ্ৰোহৰ চহৰখন টিপা।", "bombay", ["bombay", "calcutta", "simla", "sylhet"], "Bombay.|বোম্বে।"),
 SP("The mutiny began on HMIS *Vikrant.*|বিদ্ৰোহ HMIS *বিক্ৰান্তত* আৰম্ভ হৈছিল।", "Talwar|তলৱাৰত", "HMIS Talwar.|HMIS তলৱাৰ।"),
)
u3 = U(3, "hands", "A plan collapses|পৰিকল্পনা ভাঙি পৰে",
 "Follow 1946 from plan to violence.|পৰিকল্পনাৰ পৰা হিংসালৈ ১৯৪৬ অনুসৰণ কৰা।", "Finding recorded: Cabinet Mission in May, League's withdrawal in July, Calcutta in August.|প্ৰমাণ লিখা হ'ল: মে'ত কেবিনেট অভিযান, জুলাইত লীগৰ প্ৰত্যাহাৰ, আগষ্টত কলিকতা।",
 ["The Cabinet Mission plan came on 16 May 1946|১৯৪৬ৰ ১৬ মে'ত কেবিনেট অভিযানৰ পৰিকল্পনা", "It grouped provinces|ই প্ৰদেশৰ গোট কৰিছিল", "The League withdrew its approval in July|জুলাইত লীগে সন্মতি প্ৰত্যাহাৰ কৰিছিল", "Direct Action Day was 16 August 1946|১৯৪৬ৰ ১৬ আগষ্টত প্ৰত্যক্ষ সংগ্ৰাম দিৱস"],
 LINK(S("Groups of provinces|প্ৰদেশৰ গোট", "The <mark>Cabinet Mission</mark> proposed its plan on 16 May 1946, with groups of provinces. Congress and the League at first accepted it.|<mark>কেবিনেট অভিযানে</mark> ১৯৪৬ৰ ১৬ মে'ত প্ৰদেশৰ গোটসহ পৰিকল্পনা দিছিল। কংগ্ৰেছ আৰু লীগে প্ৰথমে ইয়াক গ্ৰহণ কৰিছিল।", "After Nehru said Congress was not bound by it, the League withdrew on 29 July.|কংগ্ৰেছ বান্ধ খাই নাই বুলি নেহৰুৱে কোৱাৰ পিছত ২৯ জুলাইত লীগে প্ৰত্যাহাৰ কৰিছিল।", art="scroll"),
  "british-17", 54, 1, "A constitutional plan arrives|সাংবিধানিক পৰিকল্পনাৰ আগমন", "The Assam History course tells how Grouping touched Assam.|অসমৰ ইতিহাস পাঠ্যক্ৰমত গোটকৰণে অসমক কেনেকৈ স্পৰ্শ কৰিলে, কোৱা হৈছে।"),
 S("Calcutta, August 1946|কলিকতা, ১৯৪৬ৰ আগষ্ট", "The League called <mark>Direct Action Day</mark> for 16 August 1946. Rioting in Calcutta killed an estimated 4,000 to 10,000 people, Hindus and Muslims.|লীগে ১৯৪৬ৰ ১৬ আগষ্টত <mark>প্ৰত্যক্ষ সংগ্ৰাম দিৱস</mark> ঘোষণা কৰিছিল। কলিকতাৰ দাংগাত আনুমানিক ৪,০০০ৰ পৰা ১০,০০০ হিন্দু আৰু মুছলমানৰ মৃত্যু হৈছিল।", "Violence spread to Noakhali and Bihar.|হিংসা নোৱাখালী আৰু বিহাৰলৈ বিয়পিছিল।", art="calendar"),
 IN("Direct Action Day was|প্ৰত্যক্ষ সংগ্ৰাম দিৱস আছিল", ".|।", ["8 August 1942|১৯৪২ৰ ৮ আগষ্ট", "16 August 1946|১৯৪৬ৰ ১৬ আগষ্ট", "3 June 1947|১৯৪৭ৰ ৩ জুন", "15 August 1947|১৯৪৭ৰ ১৫ আগষ্ট"], 1, "16 August 1946.|১৯৪৬ৰ ১৬ আগষ্ট।"),
 TF("The Cabinet Mission plan included groups of provinces.|কেবিনেট অভিযানৰ পৰিকল্পনাত প্ৰদেশৰ গোট আছিল।", True, "Assam was affected by this.|ইয়াৰ প্ৰভাৱ অসমত পৰিছিল।"),
 OR("Put 1946 in order.|১৯৪৬ ক্ৰমে সজোৱা।", ["Navy Mutiny|নৌ বিদ্ৰোহ", "Cabinet Mission plan|কেবিনেট অভিযানৰ পৰিকল্পনা", "League withdraws|লীগৰ প্ৰত্যাহাৰ", "Direct Action Day|প্ৰত্যক্ষ সংগ্ৰাম দিৱস"], "February, May, July, August.|ফেব্ৰুৱাৰী, মে', জুলাই, আগষ্ট।"),
 MP("Tap Calcutta.|কলিকতা টিপা।", "calcutta", ["calcutta", "bombay", "simla", "sylhet"], "Calcutta.|কলিকতা।"),
 SP("Direct Action Day was called by the *Congress.*|প্ৰত্যক্ষ সংগ্ৰাম দিৱস *কংগ্ৰেছে* ঘোষণা কৰিছিল।", "League|লীগে", "The Muslim League called it.|মুছলিম লীগে ঘোষণা কৰিছিল।"),
)
u4 = U(4, "flag", "Partition and freedom|বিভাজন আৰু স্বাধীনতা",
 "Fix the last dates.|শেষৰ তাৰিখবোৰ মনত ৰাখা।", "Finding recorded: plan on 3 June, independence at midnight on 14 to 15 August 1947.|প্ৰমাণ লিখা হ'ল: ৩ জুনত পৰিকল্পনা, ১৯৪৭ৰ ১৪-১৫ আগষ্টৰ মাজনিশা স্বাধীনতা।",
 ["Mountbatten set out his plan on 3 June 1947|১৯৪৭ৰ ৩ জুনত মাউণ্টবেটেনে পৰিকল্পনা দিছিল", "Bengal and Punjab were divided|বংগ আৰু পঞ্জাব বিভক্ত হৈছিল", "The Indian Independence Act ended Crown rule|ভাৰতীয় স্বাধীনতা আইনে ৰাজমুকুটৰ শাসন শেষ কৰিছিল", "India became independent on 15 August 1947|১৯৪৭ৰ ১৫ আগষ্টত ভাৰত স্বাধীন হৈছিল"],
 S("Two dominions|দুখন ডমিনিয়ন", "On <mark>3 June 1947</mark> [[lord-mountbatten|Mountbatten]] proposed partition into two dominions, India and Pakistan. <mark>Bengal and Punjab</mark> were divided.|<mark>১৯৪৭ৰ ৩ জুনত</mark> [[lord-mountbatten|মাউণ্টবেটেনে]] ভাৰত আৰু পাকিস্তান দুখন ডমিনিয়নৰ প্ৰস্তাৱ দিছিল। <mark>বংগ আৰু পঞ্জাব</mark> বিভক্ত হ'ল।", art="seal"),
 LINK(S("Midnight|মাজনিশা", "The Indian Independence Act ended Crown rule. Pakistan came into being on 14 August and India on <mark>15 August 1947</mark>.|ভাৰতীয় স্বাধীনতা আইনে ৰাজমুকুটৰ শাসন শেষ কৰিছিল। ১৪ আগষ্টত পাকিস্তান আৰু <mark>১৯৪৭ৰ ১৫ আগষ্টত</mark> ভাৰত হ'ল।", "In Assam, [[sylhet]] voted in a referendum.|অসমত [[sylhet|শ্ৰীহট্টত]] গণভোট হৈছিল।", art="calendar"),
  "british-18", 55, 1, "A district goes to the polls|এখন জিলাৰ ভোট", "The Assam History course tells the Sylhet referendum.|অসমৰ ইতিহাস পাঠ্যক্ৰমত শ্ৰীহট্ট গণভোটৰ কথা আছে।"),
 IN("The Mountbatten Plan is dated|মাউণ্টবেটেন পৰিকল্পনাৰ তাৰিখ", ".|।", ["3 June 1947|১৯৪৭ৰ ৩ জুন", "15 August 1947|১৯৪৭ৰ ১৫ আগষ্ট", "26 January 1950|১৯৫০ৰ ২৬ জানুৱাৰী", "16 May 1946|১৯৪৬ৰ ১৬ মে'"], 0, "3 June 1947.|১৯৪৭ৰ ৩ জুন।"),
 TF("Bengal and Punjab were divided in 1947.|১৯৪৭ত বংগ আৰু পঞ্জাব বিভক্ত হৈছিল।", True, "Along religious majorities by district.|জিলাৰ ধৰ্মীয় সংখ্যাগৰিষ্ঠতা অনুসৰি।"),
 MA([("Wavell|ৱেভেল", "Simla Conference|চিমলা সন্মিলন"), ("Mountbatten|মাউণ্টবেটেন", "Plan of 3 June|৩ জুনৰ পৰিকল্পনা"), ("Sylhet|শ্ৰীহট্ট", "Referendum|গণভোট")], "Name and event.|নাম আৰু ঘটনা।"),
 MP("Tap Sylhet.|শ্ৰীহট্ট টিপা।", "sylhet", ["sylhet", "bombay", "simla", "calcutta"], "Today in Bangladesh.|আজি বাংলাদেশত।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1945, "Wavell Plan|ৱেভেল পৰিকল্পনা"), (1947, "Independence|স্বাধীনতা")], [("Quit India, 1942|ভাৰত ত্যাগ, ১৯৪২", 0), ("Navy Mutiny, 1946|নৌ বিদ্ৰোহ, ১৯৪৬", 1), ("Constitution in force, 1950|সংবিধান বলবৎ, ১৯৫০", 2)], "1942 → 1945 → 1946 → 1947 → 1950.|১৯৪২ → ১৯৪৫ → ১৯৪৬ → ১৯৪৭ → ১৯৫০।"),
)
test = TEST("Order the last years of British rule.|ব্ৰিটিছ শাসনৰ শেষ বছৰবোৰ সজোৱা।", "Recorded: Wavell, the Mutiny, the Mission and the Plan.|লিখা হ'ল: ৱেভেল, বিদ্ৰোহ, অভিযান আৰু পৰিকল্পনা।",
 OR("Put these in chronological order.|এইবোৰ কালানুক্ৰমে সজোৱা।", ["Quit India|ভাৰত ত্যাগ", "Wavell Plan|ৱেভেল পৰিকল্পনা", "Navy Mutiny|নৌ বিদ্ৰোহ", "Mountbatten Plan|মাউণ্টবেটেন পৰিকল্পনা"], "1942, 1945, 1946, 1947.|১৯৪২, ১৯৪৫, ১৯৪৬, ১৯৪৭।"),
 TF("The Cabinet Mission came before the Mountbatten Plan.|মাউণ্টবেটেন পৰিকল্পনাৰ আগত কেবিনেট অভিযান।", True, "1946, then 1947.|১৯৪৬, তাৰ পিছত ১৯৪৭।"),
 IN("The last Viceroy was|শেষ ভাইচৰয়", ".|।", ["Wavell|ৱেভেল", "Linlithgow|লিনলিথগো", "Mountbatten|মাউণ্টবেটেন", "Irwin|আৰউইন"], 2, "Mountbatten.|মাউণ্টবেটেন।"),
 MP("Tap Simla.|চিমলা টিপা।", "simla", ["simla", "bombay", "calcutta", "sylhet"], "Simla.|চিমলা।"),
 MA([("18 February 1946|১৯৪৬ৰ ১৮ ফেব্ৰুৱাৰী", "Navy Mutiny|নৌ বিদ্ৰোহ"), ("16 August 1946|১৯৪৬ৰ ১৬ আগষ্ট", "Direct Action Day|প্ৰত্যক্ষ সংগ্ৰাম দিৱস"), ("3 June 1947|১৯৪৭ৰ ৩ জুন", "Mountbatten Plan|মাউণ্টবেটেন পৰিকল্পনা")], "Date and event.|তাৰিখ আৰু ঘটনা।"),
 MC("Consider these statements. (1) The Simla Conference opened in June 1945. (2) The Navy Mutiny began at Calcutta. (3) Pakistan came into being on 14 August 1947. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) ১৯৪৫ৰ জুনত চিমলা সন্মিলন। (২) নৌ বিদ্ৰোহ কলিকতাত আৰম্ভ। (৩) ১৯৪৭ৰ ১৪ আগষ্টত পাকিস্তান হ'ল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "It began at Bombay.|ই বোম্বেত আৰম্ভ হৈছিল।"),
)
LESSON(31, "The road to 1947|১৯৪৭লৈ বাট", "1945–1947|১৯৪৫–১৯৪৭", "Mass struggle and freedom|গণ সংগ্ৰাম আৰু স্বাধীনতা", "Evidence file 31|প্ৰমাণ নথি ৩১", "Two years to midnight|মাজনিশালৈ দুবছৰ",
 "Conferences failed, sailors mutinied, cities burned and a line was drawn. Put the last two years in exact order.|সন্মিলন বিফল হ'ল, নাৱিকে বিদ্ৰোহ কৰিলে, চহৰ জ্বলিল, ৰেখা টনা হ'ল। শেষ দুবছৰ সঠিক ক্ৰমত সজোৱা।",
 sources, [u1, u2, u3, u4], test, ["simla", "bombay", "calcutta", "sylhet"], box=[66, 8, 98, 36],
 timeline=[("1945", "Wavell Plan|ৱেভেল পৰিকল্পনা", "u1"), ("1946", "Navy Mutiny|নৌ বিদ্ৰোহ", "u2"), ("1946", "Direct Action Day|প্ৰত্যক্ষ সংগ্ৰাম দিৱস", "u3"), ("1947", "Independence|স্বাধীনতা", "u4")])
