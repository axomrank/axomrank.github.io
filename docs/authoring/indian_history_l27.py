#!/usr/bin/env python3
"""Lesson 27: Simon and the revolutionaries."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "bhagat-singh": ("person", "Bhagat Singh|ভগত সিং", "Revolutionary hanged at Lahore in 1931|১৯৩১ত লাহোৰত ফাঁচী হোৱা বিপ্লৱী"),
 "kazi-nazrul-islam": ("person", "Kazi Nazrul Islam|কাজী নজৰুল ইছলাম", "Poet and a founding leader of the Labour Swaraj Party|কবি, লেবাৰ স্বৰাজ দলৰ এজন প্ৰতিষ্ঠাপক নেতা"),
 "john-simon": ("person", "John Simon|জন চাইমন", "Chair of the all-British Commission of 1927|১৯২৭ৰ সম্পূৰ্ণ ব্ৰিটিছ কমিছনৰ অধ্যক্ষ"),
 "vallabhbhai-patel": ("person", "Vallabhbhai Patel|বল্লভভাই পেটেল", "Leader of the Bardoli Satyagraha of 1928|১৯২৮ৰ বাৰদোলী সত্যাগ্ৰহৰ নেতা"),
 "bardoli": ("place", "Bardoli|বাৰদোলী", "Taluka in Surat district, Gujarat|গুজৰাটৰ চুৰাট জিলাৰ তালুক", [21.12, 73.11]),
})
sources = [
 src("Wikipedia, Labour Swaraj Party", "https://en.wikipedia.org/wiki/Labour_Swaraj_Party", "Used as a guide: 1 November 1925, Nazrul, Langal. Check in review."),
 src("Wikipedia, Simon Commission", "https://en.wikipedia.org/wiki/Simon_Commission", "Used as a guide: November 1927, 3 February 1928, no Indians, boycott, Lajpat Rai, Nehru Report. Check in review."),
 src("Wikipedia, Bhagat Singh", "https://en.wikipedia.org/wiki/Bhagat_Singh", "Used as a guide: HSRA, Saunders, April 1929, 23 March 1931. Check in review."),
 src("Wikipedia, Bardoli Satyagraha", "https://en.wikipedia.org/wiki/Bardoli_Satyagraha", "Used as a guide: 1928, Patel, tactics, outcome. The origin of 'Sardar' is tagged as uncited there, though APSC treats it as fact. Check in review."),
]
u1 = U(1, "flag", "Simon Go Back|চাইমন ঘূৰি যোৱা",
 "See why a commission met black flags.|এখন কমিছনে কিয় প্ৰতিবাদৰ সন্মুখীন হ'ল, চোৱা।", "Finding recorded: seven British MPs, no Indians, and a national boycott.|প্ৰমাণ লিখা হ'ল: সাতজন ব্ৰিটিছ সাংসদ, কোনো ভাৰতীয় নাই, ৰাষ্ট্ৰীয় বৰ্জন।",
 ["The Simon Commission was appointed in November 1927|১৯২৭ৰ নৱেম্বৰত চাইমন কমিছন নিযুক্ত হৈছিল", "It reached Bombay on 3 February 1928|১৯২৮ৰ ৩ ফেব্ৰুৱাৰীত বোম্বে পাইছিল", "It had no Indian members|ইয়াত কোনো ভাৰতীয় সদস্য নাছিল", "Lala Lajpat Rai was beaten at Lahore|লাহোৰত লালা লাজপত ৰায়ক প্ৰহাৰ কৰা হৈছিল"],
 S("No Indians at the table|টেবুলত কোনো ভাৰতীয় নাই", "The <mark>Simon Commission</mark> of seven British MPs, under [[john-simon|John Simon]], was appointed in 1927 to review the Act of 1919. It had <mark>no Indian</mark> member.|[[john-simon|জন চাইমনৰ]] অধীনৰ সাতজন ব্ৰিটিছ সাংসদৰ <mark>চাইমন কমিছন</mark> ১৯১৯ৰ আইন পৰ্যালোচনাৰ বাবে ১৯২৭ত নিযুক্ত হৈছিল। ইয়াত <mark>কোনো ভাৰতীয়</mark> নাছিল।", art="court"),
 S("Blows at Lahore|লাহোৰত আঘাত", "The Congress boycotted it. At [[lahore]] on 30 October 1928 police beat [[lala-lajpat-rai|Lala Lajpat Rai]], who died on 17 November.|কংগ্ৰেছে ইয়াক বৰ্জন কৰিছিল। ১৯২৮ৰ ৩০ অক্টোবৰত [[lahore|লাহোৰত]] আৰক্ষীয়ে [[lala-lajpat-rai|লালা লাজপত ৰায়ক]] প্ৰহাৰ কৰিছিল, ১৭ নৱেম্বৰত তেওঁৰ মৃত্যু হয়।", art="door"),
 TF("The Simon Commission had Indian members.|চাইমন কমিছনত ভাৰতীয় সদস্য আছিল।", False, "All seven were British MPs.|সাতোজন ব্ৰিটিছ সাংসদ।"),
 IN("The Simon Commission was appointed in|চাইমন কমিছন নিযুক্ত হৈছিল", ".|ত।", ["1919|১৯১৯", "1927|১৯২৭", "1930|১৯৩০", "1942|১৯৪২"], 1, "1927.|১৯২৭।"),
 MP("Tap Lahore.|লাহোৰ টিপা।", "lahore", ["lahore", "bardoli", "bombay", "delhi"], "In today's Pakistan.|আজিৰ পাকিস্তানত।"),
 WH(["I led the march at Lahore.|মই লাহোৰত শোভাযাত্ৰাৰ নেতৃত্ব দিছিলোঁ।", "Police beat me in 1928.|১৯২৮ত আৰক্ষীয়ে মোক প্ৰহাৰ কৰিছিল।"], ["Bhagat Singh|ভগত সিং", "Lala Lajpat Rai|লালা লাজপত ৰায়", "Motilal Nehru|মতিলাল নেহৰু", "Tilak|তিলক"], 1, "Lala Lajpat Rai.|লালা লাজপত ৰায়।"),
 SP("The Commission reviewed the Act of *1858.*|কমিছনে *১৮৫৮ৰ* আইন পৰ্যালোচনা কৰিছিল।", "1919|১৯১৯ৰ", "The Act of 1919.|১৯১৯ৰ আইন।"),
)
u2 = U(2, "star", "Revolutionaries|বিপ্লৱী",
 "Fix the dates of Bhagat Singh's actions.|ভগত সিঙৰ কামৰ তাৰিখ মনত ৰাখা।", "Finding recorded: Saunders 1928, Assembly 1929, hanged 1931.|প্ৰমাণ লিখা হ'ল: ১৯২৮ত চণ্ডাৰ্ছ, ১৯২৯ত সভা, ১৯৩১ত ফাঁচী।",
 ["Bhagat Singh belonged to the HSRA|ভগত সিং HSRAৰ সদস্য", "Saunders was shot in December 1928|১৯২৮ৰ ডিচেম্বৰত চণ্ডাৰ্ছক গুলীয়াইছিল", "The Assembly bombs came in April 1929|১৯২৯ৰ এপ্ৰিলত সভাত বোমা", "He was hanged on 23 March 1931|১৯৩১ৰ ২৩ মাৰ্চত তেওঁক ফাঁচী দিয়া হৈছিল"],
 S("Lahore, December 1928|লাহোৰ, ১৯২৮ৰ ডিচেম্বৰ", "[[bhagat-singh|Bhagat Singh]] and others in the HSRA shot the officer John Saunders. They had meant to kill James Scott, blamed for Lajpat Rai's death.|[[bhagat-singh|ভগত সিং]] আৰু HSRAৰ আনে বিষয়া জন চণ্ডাৰ্ছক গুলীয়াইছিল। তেওঁলোকৰ লক্ষ্য আছিল লাজপত ৰায়ৰ মৃত্যুৰ বাবে দায়ী কৰা জেমছ স্কট।", art="door"),
 S("Bombs meant to be heard|শুনাবলৈ বোমা", "In <mark>April 1929</mark>, with Batukeshwar Dutt, he threw low-intensity bombs in the Central Assembly, to draw attention, not to kill.|<mark>১৯২৯ৰ এপ্ৰিলত</mark> বটুকেশ্বৰ দত্তৰ সৈতে তেওঁ কেন্দ্ৰীয় সভাত কম শক্তিৰ বোমা পেলাইছিল, হত্যাৰ বাবে নহয়, দৃষ্টি আকৰ্ষণৰ বাবে।", "He was hanged at Lahore with Rajguru and Sukhdev on <mark>23 March 1931</mark>.|<mark>১৯৩১ৰ ২৩ মাৰ্চত</mark> ৰাজগুৰু আৰু সুখদেৱৰ সৈতে লাহোৰত তেওঁক ফাঁচী দিয়া হৈছিল।", art="calendar"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Lajpat Rai beaten|লাজপত ৰায়ক প্ৰহাৰ", "Saunders shot|চণ্ডাৰ্ছক গুলীয়াব", "Assembly bombs|সভাত বোমা", "Bhagat Singh hanged|ভগত সিঙৰ ফাঁচী"], "October 1928, December 1928, April 1929, March 1931.|১৯২৮ অক্টোবৰ, ডিচেম্বৰ, ১৯২৯ এপ্ৰিল, ১৯৩১ মাৰ্চ।"),
 IN("Bhagat Singh threw bombs in the Assembly with|ভগত সিঙে সভাত বোমা পেলাইছিল", ".|ৰ সৈতে।", ["Rajguru|ৰাজগুৰু", "Sukhdev|সুখদেৱ", "Batukeshwar Dutt|বটুকেশ্বৰ দত্ত", "Chandra Shekhar Azad|চন্দ্ৰশেখৰ আজাদ"], 2, "Batukeshwar Dutt.|বটুকেশ্বৰ দত্ত।"),
 TF("The Assembly bombs were meant to kill members.|সভাৰ বোমাৰ লক্ষ্য সদস্যক হত্যা আছিল।", False, "They were meant to draw attention.|এইবোৰ দৃষ্টি আকৰ্ষণৰ বাবে আছিল।"),
 SC("Unscramble the revolutionary's first name.|বিপ্লৱীজনৰ প্ৰথম নামটো সজোৱা।", "BHAGAT", ["ভ", "গ", "ত"], "Bhagat Singh.|ভগত সিং।"),
 MA([("Rajguru|ৰাজগুৰু", "Hanged with him|তেওঁৰ সৈতে ফাঁচী"), ("Batukeshwar Dutt|বটুকেশ্বৰ দত্ত", "Assembly bombs|সভাত বোমা"), ("James Scott|জেমছ স্কট", "Intended target|লক্ষ্য")], "Name and link.|নাম আৰু সম্পৰ্ক।"),
)
u3 = U(3, "houses", "Bardoli and Lahore|বাৰদোলী আৰু লাহোৰ",
 "Close the decade with a peasant win and a new goal.|খেতিয়কৰ জয় আৰু নতুন লক্ষ্যৰে দশকটো শেষ কৰা।", "Finding recorded: Patel at Bardoli in 1928, and Purna Swaraj at Lahore in 1929.|প্ৰমাণ লিখা হ'ল: ১৯২৮ত বাৰদোলীত পেটেল, ১৯২৯ত লাহোৰত পূৰ্ণ স্বৰাজ।",
 ["Kazi Nazrul Islam helped set up the Labour Swaraj Party in 1925|১৯২৫ত কাজী নজৰুল ইছলামে লেবাৰ স্বৰাজ দল গঢ়াত সহায় কৰিছিল", "Patel led the Bardoli Satyagraha in 1928|১৯২৮ত পেটেলে বাৰদোলী সত্যাগ্ৰহ চলাইছিল", "APSC links the title Sardar with Bardoli|APSCয়ে চৰ্দাৰ উপাধি বাৰদোলীৰ সৈতে জড়িত কৰে", "The Lahore Congress of 1929 set Purna Swaraj as the goal|১৯২৯ৰ লাহোৰ কংগ্ৰেছে পূৰ্ণ স্বৰাজৰ লক্ষ্য লৈছিল"],
 S("A poet's party|কবিৰ দল", "The <mark>Labour Swaraj Party</mark> began in Bengal on 1 November <mark>1925</mark>, and the poet [[kazi-nazrul-islam|Kazi Nazrul Islam]] was a founding leader.|<mark>১৯২৫ৰ</mark> ১ নৱেম্বৰত বংগত <mark>লেবাৰ স্বৰাজ দল</mark> আৰম্ভ হৈছিল, কবি [[kazi-nazrul-islam|কাজী নজৰুল ইছলাম]] এজন প্ৰতিষ্ঠাপক নেতা।", art="scroll"),
 S("Farmers who would not pay|কৰ নিদিয়া খেতিয়ক", "In <mark>1928</mark> [[vallabhbhai-patel|Vallabhbhai Patel]] led the farmers of [[bardoli]] against a steep land-tax rise. Officials found whole villages empty, and the farmers won.|<mark>১৯২৮ত</mark> [[vallabhbhai-patel|বল্লভভাই পেটেলে]] [[bardoli|বাৰদোলীৰ]] খেতিয়কক ভূমি কৰ বৃদ্ধিৰ বিৰুদ্ধে নেতৃত্ব দিছিল। বিষয়াই গোটেই গাঁও খালী পাইছিল, খেতিয়ক জয়ী হৈছিল।", "APSC links his title Sardar with this campaign.|APSCয়ে তেওঁৰ চৰ্দাৰ উপাধি এই অভিযানৰ সৈতে জড়িত কৰে।", map={"base": "india", "box": [69, 18, 79, 24], "show": ["bardoli", "bombay"]}),
 S("Complete independence|সম্পূৰ্ণ স্বাধীনতা", "The decade closed at the <mark>Lahore Congress of 1929</mark>, which set <mark>[[purna-swaraj|Purna Swaraj]]</mark>, complete independence, as the goal. Your next stop is the Salt March.|দশকটো <mark>১৯২৯ৰ লাহোৰ কংগ্ৰেছত</mark> শেষ হৈছিল, যিয়ে <mark>[[purna-swaraj|পূৰ্ণ স্বৰাজ]]</mark>, অৰ্থাৎ সম্পূৰ্ণ স্বাধীনতাৰ লক্ষ্য লৈছিল। ইয়াৰ পিছত লৱণ যাত্ৰা।", art="calendar"),
 IN("The Labour Swaraj Party of 1925 was set up by|১৯২৫ৰ লেবাৰ স্বৰাজ দল গঢ়িছিল", ".|এ।", ["Abdul Ghaffar Khan|আব্দুল গফ্ফাৰ খান", "Kazi Nazrul Islam|কাজী নজৰুল ইছলাম", "Joseph Baptista|জোচেফ বেপটিষ্টা", "C. R. Das|চিত্তৰঞ্জন দাস"], 1, "Nazrul, among its founding leaders.|প্ৰতিষ্ঠাপক নেতাসকলৰ মাজত নজৰুল।"),
 MP("Tap Bardoli.|বাৰদোলী টিপা।", "bardoli", ["bardoli", "lahore", "delhi", "calcutta"], "In Gujarat.|গুজৰাটত।"),
 MA([("Swaraj Party|স্বৰাজ দল", "Das and Motilal Nehru, 1923|দাস আৰু মতিলাল নেহৰু, ১৯২৩"), ("Labour Swaraj Party|লেবাৰ স্বৰাজ দল", "Nazrul, 1925|নজৰুল, ১৯২৫"), ("Bardoli|বাৰদোলী", "Patel, 1928|পেটেল, ১৯২৮")], "Keep these apart.|এইবোৰ পৃথক ৰাখা।"),
 TF("The Bardoli farmers won their campaign.|বাৰদোলীৰ খেতিয়ক জয়ী হৈছিল।", True, "The government suspended the increase.|চৰকাৰে বৃদ্ধি স্থগিত ৰাখিছিল।"),
 SP("Bardoli was a campaign against a rise in the *salt* tax.|বাৰদোলী *লৱণ* কৰ বৃদ্ধিৰ বিৰুদ্ধে অভিযান।", "land|ভূমি", "It was the land tax.|ই ভূমি কৰ।"),
)
test = TEST("Sort a restless decade.|অস্থিৰ দশকটো পৃথক কৰা।", "Recorded: Simon, Bhagat Singh, Bardoli and Lahore.|লিখা হ'ল: চাইমন, ভগত সিং, বাৰদোলী আৰু লাহোৰ।",
 IN("The Labour Swaraj Party was set up in 1925 by|১৯২৫ত লেবাৰ স্বৰাজ দল গঢ়িছিল", ".|এ।", ["Abdul Ghaffar Khan|আব্দুল গফ্ফাৰ খান", "Kazi Nazrul Islam|কাজী নজৰুল ইছলাম", "Joseph Baptista|জোচেফ বেপটিষ্টা", "C. R. Das|চিত্তৰঞ্জন দাস"], 1, "Nazrul.|নজৰুল।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Labour Swaraj Party|লেবাৰ স্বৰাজ দল", "Simon Commission appointed|চাইমন কমিছন নিযুক্ত", "Bardoli|বাৰদোলী", "Lahore Congress|লাহোৰ কংগ্ৰেছ"], "1925, 1927, 1928, 1929.|১৯২৫, ১৯২৭, ১৯২৮, ১৯২৯।"),
 TF("Bhagat Singh was hanged in 1931.|১৯৩১ত ভগত সিঙক ফাঁচী দিয়া হৈছিল।", True, "On 23 March.|২৩ মাৰ্চত।"),
 MP("Tap Lahore.|লাহোৰ টিপা।", "lahore", ["lahore", "bardoli", "delhi", "calcutta"], "Lahore.|লাহোৰ।"),
 MA([("Vallabhbhai Patel|বল্লভভাই পেটেল", "Bardoli|বাৰদোলী"), ("John Simon|জন চাইমন", "Commission of 1927|১৯২৭ৰ কমিছন")], "Name and link.|নাম আৰু সম্পৰ্ক।"),
 MC("Consider these statements. (1) The Simon Commission had no Indian member. (2) Bhagat Singh's Assembly bombs were meant to kill. (3) The Lahore Congress set Purna Swaraj as the goal. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) চাইমন কমিছনত ভাৰতীয় সদস্য নাছিল। (২) ভগত সিঙৰ বোমা হত্যাৰ বাবে আছিল। (৩) লাহোৰ কংগ্ৰেছে পূৰ্ণ স্বৰাজৰ লক্ষ্য লৈছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "They were meant to draw attention.|এইবোৰ দৃষ্টি আকৰ্ষণৰ বাবে আছিল।"),
)
LESSON(27, "Simon and the revolutionaries|চাইমন আৰু বিপ্লৱী সকল", "1925–1931|১৯২৫–১৯৩১", "The national movement|ৰাষ্ট্ৰীয় আন্দোলন", "Evidence file 27|প্ৰমাণ নথি ২৭", "A restless decade|অস্থিৰ দশক",
 "After Non-Cooperation ended, protest did not stop. It moved to commissions, courts, farms and the Assembly floor.|অসহযোগ শেষ হোৱাৰ পিছতো প্ৰতিবাদ নৰ'ল। ই কমিছন, আদালত, পথাৰ আৰু সভাগৃহলৈ গ'ল।",
 sources, [u1, u2, u3], test, ["lahore", "bardoli", "delhi", "calcutta", "bombay"],
 timeline=[("1927", "Simon Commission appointed|চাইমন কমিছন নিযুক্ত", "u1"), ("1928", "Bardoli Satyagraha|বাৰদোলী সত্যাগ্ৰহ", "u3"), ("1931", "Bhagat Singh hanged|ভগত সিঙৰ ফাঁচী", "u2")])
