#!/usr/bin/env python3
"""Lesson 32: Building the nation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "pingali-venkayya": ("person", "Pingali Venkayya|পিংগলি ভেংকায়া", "Credited as designer of the National Flag|ৰাষ্ট্ৰীয় পতাকাৰ ৰূপকাৰ বুলি জনাজাত"),
 "maulana-azad": ("person", "Maulana Abul Kalam Azad|মৌলানা আবুল কালাম আজাদ", "First Education Minister of India|ভাৰতৰ প্ৰথম শিক্ষামন্ত্ৰী"),
 "amrit-kaur": ("person", "Amrit Kaur|অমৃত কৌৰ", "Health Minister, the only woman in the first cabinet|স্বাস্থ্য মন্ত্ৰী, প্ৰথম কেবিনেটৰ একমাত্ৰ মহিলা"),
 "goa": ("place", "Goa|গোৱা", "Portuguese territory taken in Operation Vijay, 1961|১৯৬১ত অপাৰেচন বিজয়ত লোৱা পৰ্তুগীজ অঞ্চল", [15.3, 74.0]),
 "pokhran": ("place", "Pokhran|পোখৰাণ", "Rajasthan test range|ৰাজস্থানৰ পৰীক্ষা ক্ষেত্ৰ", [27.1, 71.75]),
 "junagadh": ("place", "Junagadh|জুনাগড়", "Princely state in Gujarat|গুজৰাটৰ দেশীয় ৰাজ্য", [21.52, 70.46]),
})
sources = [
 src("Wikipedia, First Nehru ministry", "https://en.wikipedia.org/wiki/First_Nehru_ministry", "Used as a guide: 15 August 1947, Patel, Ambedkar, Azad, Prasad, Amrit Kaur. Check in review."),
 src("Wikipedia, Vallabhbhai Patel", "https://en.wikipedia.org/wiki/Vallabhbhai_Patel", "Used as a guide: Deputy PM, Home, about 565 states, Junagadh, Hyderabad, Iron Man, Statue of Unity. Check in review."),
 src("Wikipedia, List of Bharat Ratna recipients", "https://en.wikipedia.org/wiki/List_of_Bharat_Ratna_recipients", "Used as a guide: Patel, 1991. Check in review."),
 src("Wikipedia, Assassination of Mahatma Gandhi", "https://en.wikipedia.org/wiki/Assassination_of_Mahatma_Gandhi", "Used as a guide: 30 January 1948, Birla House, Godse. Check in review."),
 src("Wikipedia, Flag of India", "https://en.wikipedia.org/wiki/Flag_of_India", "Used as a guide: Venkayya, 22 July 1947, 24 spokes. Check in review."),
 src("Wikipedia, Annexation of Goa", "https://en.wikipedia.org/wiki/Annexation_of_Goa", "Used as a guide: Operation Vijay, 17 to 19 December 1961. Check in review."),
 src("Wikipedia, Smiling Buddha", "https://en.wikipedia.org/wiki/Smiling_Buddha", "Used as a guide: 18 May 1974, Pokhran. Check in review."),
 src("Wikipedia, Operation Meghdoot", "https://en.wikipedia.org/wiki/Operation_Meghdoot", "Used as a guide: 13 April 1984, Siachen. Check in review."),
 src("Wikipedia, 2020–2021 China–India skirmishes", "https://en.wikipedia.org/wiki/2020%E2%80%932021_China%E2%80%93India_skirmishes", "Used as a guide: Galwan, May and June 2020. Check in review."),
 src("Wikipedia, Bangladesh Liberation War", "https://en.wikipedia.org/wiki/Bangladesh_Liberation_War", "Used as a guide: 26 March to 16 December 1971. Check in review."),
]
u1 = U(1, "court", "The first cabinet|প্ৰথম কেবিনেট",
 "Match ministers to portfolios.|মন্ত্ৰীক বিভাগৰ সৈতে মিলোৱা।", "Finding recorded: Nehru, Patel, Ambedkar, Azad and Amrit Kaur.|প্ৰমাণ লিখা হ'ল: নেহৰু, পেটেল, আম্বেদকাৰ, আজাদ আৰু অমৃত কৌৰ।",
 ["Nehru became Prime Minister on 15 August 1947|১৯৪৭ৰ ১৫ আগষ্টত নেহৰু প্ৰধানমন্ত্ৰী", "Patel was Deputy Prime Minister and Home Minister|পেটেল উপ-প্ৰধানমন্ত্ৰী আৰু গৃহমন্ত্ৰী", "B. R. Ambedkar was the first Law Minister|বি. আৰ. আম্বেদকাৰ প্ৰথম আইন মন্ত্ৰী", "Gandhi was killed on 30 January 1948|১৯৪৮ৰ ৩০ জানুৱাৰীত গান্ধীক হত্যা কৰা হৈছিল"],
 S("Fifteen ministers|পোন্ধৰজন মন্ত্ৰী", "[[jawaharlal-nehru|Nehru]] took office on 15 August 1947. [[vallabhbhai-patel|Patel]] was Deputy PM and Home Minister. <mark>[[br-ambedkar|B. R. Ambedkar]]</mark> held Law, [[maulana-azad|Azad]] Education.|১৯৪৭ৰ ১৫ আগষ্টত [[jawaharlal-nehru|নেহৰু]] প্ৰধানমন্ত্ৰী হৈছিল। [[vallabhbhai-patel|পেটেল]] উপ-প্ৰধানমন্ত্ৰী আৰু গৃহমন্ত্ৰী। <mark>[[br-ambedkar|বি. আৰ. আম্বেদকাৰ]]</mark> আইন, [[maulana-azad|আজাদ]] শিক্ষা।", "[[amrit-kaur|Amrit Kaur]], Health Minister, was the only woman.|স্বাস্থ্য মন্ত্ৰী [[amrit-kaur|অমৃত কৌৰ]] একমাত্ৰ মহিলা।", art="court"),
 S("Birla House|বিড়লা ভৱন", "On <mark>30 January 1948</mark> Nathuram Godse shot [[mahatma-gandhi|Gandhi]] at Birla House, Delhi, during an evening prayer meeting.|<mark>১৯৪৮ৰ ৩০ জানুৱাৰীত</mark> দিল্লীৰ বিড়লা ভৱনত সন্ধিয়াৰ প্ৰাৰ্থনা সভাত নাথুৰাম গডছেই [[mahatma-gandhi|গান্ধীক]] গুলীয়াইছিল।", art="calendar"),
 IN("The first Law and Justice Minister of independent India was|স্বাধীন ভাৰতৰ প্ৰথম আইন আৰু ন্যায় মন্ত্ৰী", ".|।", ["Vallabhbhai Patel|বল্লভভাই পেটেল", "Maulana Azad|মৌলানা আজাদ", "C. Rajagopalachari|চি. ৰাজাগোপালাচাৰী", "B. R. Ambedkar|বি. আৰ. আম্বেদকাৰ"], 3, "Ambedkar.|আম্বেদকাৰ।"),
 MA([("Patel|পেটেল", "Home|গৃহ"), ("Ambedkar|আম্বেদকাৰ", "Law|আইন"), ("Azad|আজাদ", "Education|শিক্ষা"), ("Amrit Kaur|অমৃত কৌৰ", "Health|স্বাস্থ্য")], "Minister and portfolio.|মন্ত্ৰী আৰু বিভাগ।"),
 TF("Vallabhbhai Patel was India's first Deputy Prime Minister.|বল্লভভাই পেটেল ভাৰতৰ প্ৰথম উপ-প্ৰধানমন্ত্ৰী।", True, "APSC tests this.|APSCয়ে এইটো সোধে।"),
 SP("Gandhi was killed in *Bombay.*|গান্ধীক *বোম্বেত* হত্যা কৰা হৈছিল।", "Delhi|দিল্লীত", "At Birla House, Delhi.|দিল্লীৰ বিড়লা ভৱনত।"),
 WH(["I was Health Minister.|মই স্বাস্থ্য মন্ত্ৰী।", "I was the only woman in the first cabinet.|প্ৰথম কেবিনেটৰ মই একমাত্ৰ মহিলা।"], ["Sarojini Naidu|চৰোজিনী নাইডু", "Amrit Kaur|অমৃত কৌৰ", "Aruna Asaf Ali|অৰুণা আছফ আলী", "Annie Besant|এনি বেচান্ত"], 1, "Amrit Kaur.|অমৃত কৌৰ।"),
)
u2 = U(2, "crown", "The Iron Man|লৌহ পুৰুষ",
 "See how the map of India was joined.|ভাৰতৰ মানচিত্ৰ কেনেকৈ যোৰা লাগিল, চোৱা।", "Finding recorded: Patel brought in most of about 565 princely states.|প্ৰমাণ লিখা হ'ল: পেটেলে প্ৰায় ৫৬৫ দেশীয় ৰাজ্যৰ বেছিভাগ আনিছিল।",
 ["Patel is the Iron Man of India|পেটেল ভাৰতৰ লৌহ পুৰুষ", "There were about 565 princely states|প্ৰায় ৫৬৫ দেশীয় ৰাজ্য আছিল", "Junagadh and Hyderabad came in by military action|জুনাগড় আৰু হায়দৰাবাদ সামৰিক কাৰ্যৰে আহিছিল", "He received the Bharat Ratna in 1991, posthumously|১৯৯১ত মৰণোত্তৰ ভাৰতৰত্ন"],
 S("565 states|৫৬৫ ৰাজ্য", "<mark>[[vallabhbhai-patel|Patel]]</mark> persuaded most of the roughly <mark>565</mark> princely states to join India. Papers call him the <mark>Iron Man of India</mark>.|<mark>[[vallabhbhai-patel|পেটেলে]]</mark> প্ৰায় <mark>৫৬৫</mark> দেশীয় ৰাজ্যৰ বেছিভাগক ভাৰতত যোগ দিবলৈ সন্মত কৰাইছিল। পৰীক্ষাত তেওঁক <mark>ভাৰতৰ লৌহ পুৰুষ</mark> বোলে।", art="houses"),
 S("Force and honours|বল আৰু সন্মান", "[[junagadh]] and [[hyderabad]] came in through military action. Patel died in 1950.|[[junagadh|জুনাগড়]] আৰু [[hyderabad|হায়দৰাবাদ]] সামৰিক কাৰ্যৰে আহিছিল। ১৯৫০ত পেটেলৰ মৃত্যু হয়।", "He got the Bharat Ratna only in <mark>1991</mark>, not 1989. The Statue of Unity, about 182 metres tall, honours him.|তেওঁ ভাৰতৰত্ন ১৯৮৯ত নহয়, <mark>১৯৯১ত</mark> পাইছিল। প্ৰায় ১৮২ মিটাৰ ওখ ঐক্যৰ মূৰ্তি তেওঁৰ সন্মানত।", art="seal"),
 IN("The Iron Man of India is|ভাৰতৰ লৌহ পুৰুষ", ".|।", ["Mahatma Gandhi|মহাত্মা গান্ধী", "Subhas Chandra Bose|সুভাষচন্দ্ৰ বসু", "B. R. Ambedkar|বি. আৰ. আম্বেদকাৰ", "Vallabhbhai Patel|বল্লভভাই পেটেল"], 3, "Patel.|পেটেল।"),
 TF("Patel received the Bharat Ratna in 1989.|পেটেলে ১৯৮৯ত ভাৰতৰত্ন পাইছিল।", False, "It was 1991. APSC used this as a trap.|ই ১৯৯১। APSCয়ে ইয়াক ফান্দ হিচাপে ব্যৱহাৰ কৰিছিল।"),
 MP("Tap Junagadh.|জুনাগড় টিপা।", "junagadh", ["junagadh", "goa", "pokhran", "delhi"], "In Gujarat.|গুজৰাটত।"),
 OD("Which state came in through military action?|কোনখন ৰাজ্য সামৰিক কাৰ্যৰে আহিছিল?", ["Mysore|মহীশূৰ", "Travancore|ত্ৰিবাংকুৰ", "Hyderabad|হায়দৰাবাদ", "Baroda|বৰোদা"], 2, "Hyderabad, with Junagadh.|জুনাগড়ৰ সৈতে হায়দৰাবাদ।"),
 SP("Patel is called the *Steel* Man of India.|পেটেলক ভাৰতৰ *ইস্পাত* পুৰুষ বোলে।", "Iron|লৌহ", "The Iron Man of India.|ভাৰতৰ লৌহ পুৰুষ।"),
)
u3 = U(3, "flag", "The flag|পতাকা",
 "Fix the flag's facts.|পতাকাৰ তথ্য মনত ৰাখা।", "Finding recorded: Venkayya, adopted on 22 July 1947, with 24 spokes.|প্ৰমাণ লিখা হ'ল: ভেংকায়া, ১৯৪৭ৰ ২২ জুলাইত গৃহীত, ২৪টা অৰ।",
 ["Pingali Venkayya is credited as designer|পিংগলি ভেংকায়াক ৰূপকাৰ বোলা হয়", "The Constituent Assembly adopted it on 22 July 1947|১৯৪৭ৰ ২২ জুলাইত গণপৰিষদে গ্ৰহণ কৰিছিল", "The wheel has 24 spokes|চক্ৰত ২৪টা অৰ", "The Ashoka Chakra replaced the spinning wheel|অশোক চক্ৰই চৰখাৰ ঠাই ল'লে"],
 S("From charkha to chakra|চৰখাৰ পৰা চক্ৰলৈ", "<mark>[[pingali-venkayya|Pingali Venkayya]]</mark> is credited with the design, though today's flag adapts his. The Assembly adopted it on <mark>22 July 1947</mark>.|<mark>[[pingali-venkayya|পিংগলি ভেংকায়াক]]</mark> ৰূপকাৰ বোলা হয়, যদিও আজিৰ পতাকা তেওঁৰ নক্সাৰ ৰূপান্তৰ। <mark>১৯৪৭ৰ ২২ জুলাইত</mark> গণপৰিষদে গ্ৰহণ কৰিছিল।", "The Congress flag's charkha gave way to the Ashoka Chakra.|কংগ্ৰেছৰ পতাকাৰ চৰখাৰ ঠাইত অশোক চক্ৰ আহিল।", art="seal"),
 S("Twenty-four spokes|চৌবিশটা অৰ", "The navy blue wheel has <mark>24</mark> spokes. You met it on Ashoka's Lion Capital at Sarnath.|নীলা চক্ৰত <mark>২৪টা</mark> অৰ আছে। ইয়াক সাৰনাথৰ অশোকৰ সিংহশীৰ্ষত দেখিছিলা।", art="calendar"),
 IN("The National Flag of India was designed by|ভাৰতৰ ৰাষ্ট্ৰীয় পতাকাৰ ৰূপকাৰ", ".|।", ["Mahatma Gandhi|মহাত্মা গান্ধী", "Pingali Venkayya|পিংগলি ভেংকায়া", "Sarojini Naidu|চৰোজিনী নাইডু", "Rabindranath Tagore|ৰবীন্দ্ৰনাথ ঠাকুৰ"], 1, "Venkayya.|ভেংকায়া।"),
 IN("The number of spokes in the flag's Chakra is|পতাকাৰ চক্ৰৰ অৰৰ সংখ্যা", ".|।", ["16|১৬", "22|২২", "24|২৪", "32|৩২"], 2, "24.|২৪।"),
 TF("The flag was adopted on 22 July 1947.|১৯৪৭ৰ ২২ জুলাইত পতাকা গৃহীত হৈছিল।", True, "By the Constituent Assembly.|গণপৰিষদে।"),
 SC("Unscramble the wheel on the flag.|পতাকাৰ চক্ৰটো সজোৱা।", "CHAKRA", ["চ", "ক্ৰ"], "Chakra.|চক্ৰ।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Flag adopted|পতাকা গৃহীত", "Independence|স্বাধীনতা", "Republic|গণৰাজ্য"], "July 1947, August 1947, January 1950.|১৯৪৭ জুলাই, ১৯৪৭ আগষ্ট, ১৯৫০ জানুৱাৰী।"),
)
u4 = U(4, "calendar", "After 1950|১৯৫০ৰ পিছত",
 "Order the events papers mix up.|পৰীক্ষাত মিহলি কৰা ঘটনা সজোৱা।", "Finding recorded: 1961, 1971, 1974, 1984, 2020.|প্ৰমাণ লিখা হ'ল: ১৯৬১, ১৯৭১, ১৯৭৪, ১৯৮৪, ২০২০।",
 ["Operation Vijay of 1961 took Goa|১৯৬১ৰ অপাৰেচন বিজয়ে গোৱা লৈছিল", "Bangladesh was created in 1971|১৯৭১ত বাংলাদেশৰ সৃষ্টি", "Smiling Buddha was the 1974 test at Pokhran|১৯৭৪ত পোখৰাণত স্মাইলিং বুদ্ধ পৰীক্ষা", "Operation Meghdoot of 1984 was at Siachen|১৯৮৪ৰ অপাৰেচন মেঘদূত চিয়াচেনত"],
 S("Which Operation Vijay?|কোনটো অপাৰেচন বিজয়?", "Two operations carry this name. APSC's answer only works with <mark>1961</mark>: the operation that took [[goa]]. The Kargil one came in 1999.|এই নামত দুটা অভিযান আছে। APSCৰ উত্তৰ <mark>১৯৬১ৰ</mark> ক্ষেত্ৰতহে মিলে: [[goa|গোৱা]] লোৱা অভিযান। কাৰ্গিলৰটো ১৯৯৯ত।", art="embassy"),
 S("A line of dates|তাৰিখৰ শাৰী", "<b>Goa 1961. Bangladesh 16 December 1971. Smiling Buddha at Pokhran, 18 May 1974. Meghdoot at Siachen, 13 April 1984. Galwan, 2020.</b>|<b>গোৱা ১৯৬১। বাংলাদেশ ১৯৭১ৰ ১৬ ডিচেম্বৰ। পোখৰাণত স্মাইলিং বুদ্ধ, ১৯৭৪ৰ ১৮ মে'। চিয়াচেনত মেঘদূত, ১৯৮৪ৰ ১৩ এপ্ৰিল। গালৱান, ২০২০।</b>", art="calendar"),
 IN("Bangladesh was created in|বাংলাদেশৰ সৃষ্টি হৈছিল", ".|ত।", ["1947|১৯৪৭", "1951|১৯৫১", "1962|১৯৬২", "1971|১৯৭১"], 3, "1971.|১৯৭১।"),
 OR("Put these in ascending order.|এইবোৰ ক্ৰমে সজোৱা।", ["Operation Vijay|অপাৰেচন বিজয়", "Smiling Buddha|স্মাইলিং বুদ্ধ", "Operation Meghdoot|অপাৰেচন মেঘদূত", "Galwan standoff|গালৱান সংঘাত"], "1961, 1974, 1984, 2020.|১৯৬১, ১৯৭৪, ১৯৮৪, ২০২০।"),
 MA([("Operation Vijay, 1961|অপাৰেচন বিজয়, ১৯৬১", "Goa|গোৱা"), ("Smiling Buddha|স্মাইলিং বুদ্ধ", "Pokhran|পোখৰাণ"), ("Operation Meghdoot|অপাৰেচন মেঘদূত", "Siachen|চিয়াচেন")], "Operation and place.|অভিযান আৰু ঠাই।"),
 MP("Tap Pokhran.|পোখৰাণ টিপা।", "pokhran", ["pokhran", "goa", "junagadh", "delhi"], "In Rajasthan.|ৰাজস্থানত।"),
 TF("Smiling Buddha was India's first nuclear test.|স্মাইলিং বুদ্ধ ভাৰতৰ প্ৰথম পাৰমাণৱিক পৰীক্ষা।", True, "On 18 May 1974.|১৯৭৪ৰ ১৮ মে'ত।"),
)
test = TEST("Close the course on the Republic.|গণৰাজ্যত পাঠ্যক্ৰম সামৰা।", "Recorded: cabinet, Patel, flag and later events.|লিখা হ'ল: কেবিনেট, পেটেল, পতাকা আৰু পিছৰ ঘটনা।",
 IN("The first Law and Justice Minister was|প্ৰথম আইন আৰু ন্যায় মন্ত্ৰী", ".|।", ["Vallabhbhai Patel|বল্লভভাই পেটেল", "B. R. Ambedkar|বি. আৰ. আম্বেদকাৰ", "Maulana Azad|মৌলানা আজাদ", "C. Rajagopalachari|চি. ৰাজাগোপালাচাৰী"], 1, "Ambedkar.|আম্বেদকাৰ।"),
 OR("Put these in ascending order.|এইবোৰ ক্ৰমে সজোৱা।", ["Operation Vijay|অপাৰেচন বিজয়", "Smiling Buddha|স্মাইলিং বুদ্ধ", "Operation Meghdoot|অপাৰেচন মেঘদূত", "Galwan standoff|গালৱান সংঘাত"], "1961, 1974, 1984, 2020.|১৯৬১, ১৯৭৪, ১৯৮৪, ২০২০।"),
 MP("Tap Goa.|গোৱা টিপা।", "goa", ["goa", "pokhran", "junagadh", "delhi"], "On the west coast.|পশ্চিম উপকূলত।"),
 TF("The Iron Man of India is Vallabhbhai Patel.|ভাৰতৰ লৌহ পুৰুষ বল্লভভাই পেটেল।", True, "Yes.|হয়।"),
 MA([("Pingali Venkayya|পিংগলি ভেংকায়া", "Flag|পতাকা"), ("Amrit Kaur|অমৃত কৌৰ", "Health|স্বাস্থ্য"), ("Patel|পেটেল", "Princely states|দেশীয় ৰাজ্য")], "Name and link.|নাম আৰু সম্পৰ্ক।"),
 MC("Consider these statements about Patel. (1) He was first Deputy Prime Minister. (2) He received the Bharat Ratna in 1989. (3) Papers link his title Sardar with Bardoli. Which are correct?|পেটেল সম্পৰ্কে এই উক্তিবোৰ বিবেচনা কৰা। (১) তেওঁ প্ৰথম উপ-প্ৰধানমন্ত্ৰী। (২) ১৯৮৯ত তেওঁ ভাৰতৰত্ন পাইছিল। (৩) পৰীক্ষাত তেওঁৰ চৰ্দাৰ উপাধি বাৰদোলীৰ সৈতে জড়িত। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "It was 1991.|ই ১৯৯১।"),
)
LESSON(32, "Building the nation|ৰাষ্ট্ৰ গঢ়", "1947–2020|১৯৪৭–২০২০", "Mass struggle and freedom|গণ সংগ্ৰাম আৰু স্বাধীনতা", "Evidence file 32|প্ৰমাণ নথি ৩২", "After midnight|মাজনিশাৰ পিছত",
 "Independence left a cabinet to form, hundreds of states to join and a flag to fly. Finish the course on the facts papers ask most.|স্বাধীনতাৰ পিছত কেবিনেট গঢ়া, শ শ ৰাজ্য জোৰা আৰু পতাকা উৰুওৱাৰ কাম আছিল। পৰীক্ষাত সততে সোধা তথ্যৰে পাঠ্যক্ৰম শেষ কৰা।",
 sources, [u1, u2, u3, u4], test, ["junagadh", "goa", "pokhran", "delhi"],
 timeline=[("1947", "First cabinet|প্ৰথম কেবিনেট", "u1"), ("1961", "Operation Vijay|অপাৰেচন বিজয়", "u4"), ("1971", "Bangladesh created|বাংলাদেশৰ সৃষ্টি", "u4")])
