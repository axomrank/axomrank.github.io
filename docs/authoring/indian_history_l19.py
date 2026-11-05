#!/usr/bin/env python3
"""Lesson 19: The Governors-General."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "warren-hastings": ("person", "Warren Hastings|ৱাৰেন হেষ্টিংছ", "First Governor-General of Bengal, 1773|বংগৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল, ১৭৭৩"),
 "lord-cornwallis": ("person", "Lord Cornwallis|লৰ্ড কৰ্ণৱালিছ", "Governor-General behind the Permanent Settlement of 1793|১৭৯৩ৰ চিৰস্থায়ী বন্দোবস্তৰ গৱৰ্ণৰ জেনেৰেল"),
 "lord-bentinck": ("person", "Lord William Bentinck|লৰ্ড উইলিয়াম বেণ্টিংক", "First Governor-General of India|ভাৰতৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল"),
 "lord-dalhousie": ("person", "Lord Dalhousie|লৰ্ড ডালহৌচী", "Governor-General, 1848 to 1856, linked with the doctrine of lapse|গৱৰ্ণৰ জেনেৰেল, ১৮৪৮ৰ পৰা ১৮৫৬, স্বত্ববিলোপ নীতিৰ সৈতে জড়িত"),
 "lord-canning": ("person", "Lord Canning|লৰ্ড কেনিং", "First Viceroy of India, 1858|ভাৰতৰ প্ৰথম ভাইচৰয়, ১৮৫৮"),
 "macaulay": ("person", "Thomas Babington Macaulay|টমাছ বেবিংটন মেকলে", "Law Member whose Minute of 1835 shaped education policy|১৮৩৫ৰ টোকাৰে শিক্ষা নীতি গঢ়া আইন সদস্য"),
 "permanent-settlement": ("term", "Permanent Settlement|চিৰস্থায়ী বন্দোবস্ত", "1793 agreement fixing land revenue with Bengal zamindars|বংগৰ জমিদাৰৰ সৈতে ভূমি ৰাজহ বান্ধি দিয়া ১৭৯৩ৰ বন্দোবস্ত"),
 "doctrine-of-lapse": ("term", "Doctrine of Lapse|স্বত্ববিলোপ নীতি", "Annexing a state whose ruler died without a male heir|পুৰুষ উত্তৰাধিকাৰী নথকা ৰজাৰ ৰাজ্য দখলৰ নীতি"),
 "jhansi": ("place", "Jhansi|ঝাঁচী", "State in central India, annexed under Dalhousie|মধ্য ভাৰতৰ ৰাজ্য, ডালহৌচীৰ দিনত দখল", [25.45, 78.57]),
 "satara": ("place", "Satara|সাতাৰা", "Maratha state annexed in 1848|১৮৪৮ত দখল কৰা মাৰাঠা ৰাজ্য", [17.68, 74.0]),
})
sources = [
 src("Wikipedia, Governor-General of India", "https://en.wikipedia.org/wiki/Governor-General_of_India", "Used as a guide: 1773, Hastings, 1833, Bentinck, 1858, Canning. The article's Bentinck dates conflict, so the lesson uses the 1833 Act. Check in review."),
 src("Wikipedia, Permanent settlement", "https://en.wikipedia.org/wiki/Permanent_settlement", "Used as a guide: 1793, Cornwallis, zamindars. Check in review."),
 src("Wikipedia, Sati (practice)", "https://en.wikipedia.org/wiki/Sati_(practice)", "Used as a guide: Regulation XVII of 4 December 1829. Check in review."),
 src("Wikipedia, Thomas Babington Macaulay", "https://en.wikipedia.org/wiki/Thomas_Babington_Macaulay", "Used as a guide: Law Member, Minute of 2 February 1835, peerage in 1857. The Minute itself was not read. Check in review."),
 src("Wikipedia, Doctrine of lapse", "https://en.wikipedia.org/wiki/Doctrine_of_lapse", "Used as a guide: Dalhousie, Satara, Jhansi, Nagpur, and Awadh on another pretext. Its dates for Jhansi and Nagpur conflict, so the lesson gives none. Check in review."),
]
u1 = U(1, "court", "Three titles|তিনিটা উপাধি",
 "Keep the three firsts apart.|তিনিওটা 'প্ৰথম' পৃথক ৰাখা।", "Finding recorded: Hastings of Bengal, Bentinck of India, Canning as Viceroy.|প্ৰমাণ লিখা হ'ল: বংগৰ হেষ্টিংছ, ভাৰতৰ বেণ্টিংক, ভাইচৰয় কেনিং।",
 ["Warren Hastings was first Governor-General of Bengal|ৱাৰেন হেষ্টিংছ বংগৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল", "Bentinck was first Governor-General of India|বেণ্টিংক ভাৰতৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল", "The Charter Act of 1833 made that change|১৮৩৩ৰ চাৰ্টাৰ আইনে এই সলনি কৰিছিল", "Canning became the first Viceroy in 1858|১৮৫৮ত কেনিং প্ৰথম ভাইচৰয় হৈছিল"],
 LINK(S("One office, three names|এটা পদ, তিনিটা নাম", "The Regulating Act of 1773 made [[warren-hastings|Warren Hastings]] Governor-General of <mark>Bengal</mark>.|১৭৭৩ৰ ৰেগুলেটিং আইনে [[warren-hastings|ৱাৰেন হেষ্টিংছক]] <mark>বংগৰ</mark> গৱৰ্ণৰ জেনেৰেল কৰিছিল।", "The Charter Act of 1833 made [[lord-bentinck|Bentinck]] Governor-General of <mark>India</mark>. In 1858 [[lord-canning|Canning]] became the first <mark>Viceroy</mark>.|১৮৩৩ৰ চাৰ্টাৰ আইনে [[lord-bentinck|বেণ্টিংকক]] <mark>ভাৰতৰ</mark> গৱৰ্ণৰ জেনেৰেল কৰিছিল। ১৮৫৮ত [[lord-canning|কেনিং]] প্ৰথম <mark>ভাইচৰয়</mark> হৈছিল।", art="court"),
  "con-01-rules-before-republic", 1, 1, "From Company to Crown|কোম্পানীৰ পৰা ৰাজমুকুটলৈ", "The Constitution course teaches these Acts in full.|সংবিধান পাঠ্যক্ৰমত এই আইনবোৰ সম্পূৰ্ণকৈ শিকোৱা হৈছে।"),
 S("The trap|ফান্দ", "A paper asks who was the first Governor-General of India. The answer is <mark>Bentinck</mark>, not Hastings, Cornwallis or Dalhousie.|এখন প্ৰশ্নকাকতত ভাৰতৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল সোধা হৈছিল। উত্তৰ <mark>বেণ্টিংক</mark>, হেষ্টিংছ, কৰ্ণৱালিছ বা ডালহৌচী নহয়।", art="seal"),
 IN("The first Governor-General of India was|ভাৰতৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল আছিল", ".|।", ["Lord Dalhousie|লৰ্ড ডালহৌচী", "Lord Cornwallis|লৰ্ড কৰ্ণৱালিছ", "Lord William Bentinck|লৰ্ড উইলিয়াম বেণ্টিংক", "Warren Hastings|ৱাৰেন হেষ্টিংছ"], 2, "Bentinck, under the 1833 Act.|১৮৩৩ৰ আইনৰ অধীনত বেণ্টিংক।"),
 MA([("1773|১৭৭৩", "Governor-General of Bengal|বংগৰ গৱৰ্ণৰ জেনেৰেল"), ("1833|১৮৩৩", "Governor-General of India|ভাৰতৰ গৱৰ্ণৰ জেনেৰেল"), ("1858|১৮৫৮", "Viceroy|ভাইচৰয়")], "Year and title.|বছৰ আৰু উপাধি।"),
 TF("The title Viceroy was first used in 1858.|১৮৫৮ত ভাইচৰয় উপাধি প্ৰথম ব্যৱহাৰ হৈছিল।", True, "With Canning.|কেনিঙৰ সৈতে।"),
 SP("Warren Hastings was Governor-General of *India.*|ৱাৰেন হেষ্টিংছ *ভাৰতৰ* গৱৰ্ণৰ জেনেৰেল আছিল।", "Bengal|বংগৰ", "Of Bengal.|বংগৰ।"),
 OR("Put the titles in order.|উপাধিবোৰ ক্ৰমে সজোৱা।", ["Hastings|হেষ্টিংছ", "Bentinck|বেণ্টিংক", "Canning|কেনিং"], "1773, 1833, 1858.|১৭৭৩, ১৮৩৩, ১৮৫৮।"),
)
u2 = U(2, "houses", "Land and a ban|ভূমি আৰু এক নিষেধাজ্ঞা",
 "Match each Governor-General to his measure.|প্ৰতিজন গৱৰ্ণৰ জেনেৰেলক তেওঁৰ ব্যৱস্থাৰ সৈতে মিলোৱা।", "Finding recorded: Permanent Settlement 1793, sati banned 1829.|প্ৰমাণ লিখা হ'ল: ১৭৯৩ৰ চিৰস্থায়ী বন্দোবস্ত, ১৮২৯ত সতীদাহ নিষিদ্ধ।",
 ["Cornwallis's Permanent Settlement came in 1793|কৰ্ণৱালিছৰ চিৰস্থায়ী বন্দোবস্ত ১৭৯৩ত", "It fixed revenue with Bengal's zamindars|ই বংগৰ জমিদাৰৰ সৈতে ৰাজহ বান্ধি দিছিল", "Bentinck banned sati in 1829|১৮২৯ত বেণ্টিংকে সতীদাহ নিষিদ্ধ কৰিছিল", "Ram Mohan Roy campaigned against sati|ৰামমোহন ৰায়ে সতীদাহৰ বিৰুদ্ধে অভিযান চলাইছিল"],
 S("Revenue fixed for ever|চিৰদিনৰ বাবে বন্ধা ৰাজহ", "In <mark>1793</mark> [[lord-cornwallis|Cornwallis]] fixed Bengal's land revenue with the zamindars in the <mark>[[permanent-settlement|Permanent Settlement]]</mark>.|<mark>১৭৯৩ত</mark> [[lord-cornwallis|কৰ্ণৱালিছে]] <mark>[[permanent-settlement|চিৰস্থায়ী বন্দোবস্তত]]</mark> জমিদাৰৰ সৈতে বংগৰ ভূমি ৰাজহ বান্ধি দিছিল।", "High fixed demands ruined many zamindars, and their lands were auctioned.|উচ্চ নিৰ্দিষ্ট দাবীয়ে বহু জমিদাৰক ধ্বংস কৰিছিল, মাটি নিলাম হৈছিল।", art="scroll"),
 S("Regulation XVII|সপ্তদশ বিধি", "On 4 December <mark>1829</mark> [[lord-bentinck|Bentinck]] made sati illegal. [[ram-mohan-roy|Ram Mohan Roy]] had campaigned against it.|<mark>১৮২৯ৰ</mark> ৪ ডিচেম্বৰত [[lord-bentinck|বেণ্টিংকে]] সতীদাহ অবৈধ কৰিছিল। [[ram-mohan-roy|ৰামমোহন ৰায়ে]] ইয়াৰ বিৰুদ্ধে অভিযান চলাইছিল।", art="seal"),
 MA([("Cornwallis|কৰ্ণৱালিছ", "Permanent Settlement|চিৰস্থায়ী বন্দোবস্ত"), ("Bentinck|বেণ্টিংক", "Sati banned|সতীদাহ নিষিদ্ধ"), ("Dalhousie|ডালহৌচী", "Doctrine of Lapse|স্বত্ববিলোপ নীতি")], "Name and measure.|নাম আৰু ব্যৱস্থা।"),
 IN("The Permanent Settlement dates from|চিৰস্থায়ী বন্দোবস্তৰ তাৰিখ", ".|।", ["1765|১৭৬৫", "1793|১৭৯৩", "1829|১৮২৯", "1858|১৮৫৮"], 1, "1793.|১৭৯৩।"),
 TF("The Permanent Settlement was made with Bengal's zamindars.|চিৰস্থায়ী বন্দোবস্ত বংগৰ জমিদাৰৰ সৈতে হৈছিল।", True, "They collected revenue from cultivators.|তেওঁলোকে খেতিয়কৰ পৰা ৰাজহ তুলিছিল।"),
 WH(["I made sati illegal.|মই সতীদাহ অবৈধ কৰিছিলোঁ।", "The 1833 Act made me Governor-General of India.|১৮৩৩ৰ আইনে মোক ভাৰতৰ গৱৰ্ণৰ জেনেৰেল কৰিছিল।"], ["Cornwallis|কৰ্ণৱালিছ", "Bentinck|বেণ্টিংক", "Dalhousie|ডালহৌচী", "Canning|কেনিং"], 1, "Bentinck.|বেণ্টিংক।"),
 SP("Sati was banned in *1929.*|সতীদাহ *১৯২৯ত* নিষিদ্ধ হৈছিল।", "1829|১৮২৯ত", "1829.|১৮২৯।"),
)
u3 = U(3, "scroll", "English in schools|বিদ্যালয়ত ইংৰাজী",
 "Get Macaulay right.|মেকলেৰ তথ্য ঠিককৈ শিকা।", "Finding recorded: Macaulay's Minute of 1835, under Bentinck.|প্ৰমাণ লিখা হ'ল: বেণ্টিংকৰ দিনত মেকলেৰ ১৮৩৫ৰ টোকা।",
 ["Macaulay's Minute dates from 2 February 1835|মেকলেৰ টোকাৰ তাৰিখ ১৮৩৫ৰ ২ ফেব্ৰুৱাৰী", "It pressed for English education|ই ইংৰাজী শিক্ষাৰ বাবে হেঁচা দিছিল", "He was Law Member, not Governor-General|তেওঁ আইন সদস্য, গৱৰ্ণৰ জেনেৰেল নহয়", "He became a Lord only in 1857|তেওঁ ১৮৫৭তহে লৰ্ড হৈছিল"],
 S("A Minute that changed schools|বিদ্যালয় সলোৱা টোকা", "[[macaulay|Thomas Macaulay]] wrote his <mark>Minute on Indian Education</mark> on 2 February 1835. The English Education Act of 1835 under Bentinck closely followed it.|[[macaulay|টমাছ মেকলেয়ে]] ১৮৩৫ৰ ২ ফেব্ৰুৱাৰীত <mark>ভাৰতীয় শিক্ষা সম্পৰ্কীয় টোকা</mark> লিখিছিল। বেণ্টিংকৰ ১৮৩৫ৰ ইংৰাজী শিক্ষা আইনে ইয়াক অনুসৰণ কৰিছিল।", art="scroll"),
 S("Not a Governor-General|গৱৰ্ণৰ জেনেৰেল নহয়", "Papers call him Lord Macaulay. In India he was <mark>Law Member</mark> of the Council, 1834 to 1838, and became a baron only in 1857.|পৰীক্ষাত তেওঁক লৰ্ড মেকলে বোলা হয়। ভাৰতত তেওঁ ১৮৩৪ৰ পৰা ১৮৩৮লৈ পৰিষদৰ <mark>আইন সদস্য</mark>, ১৮৫৭তহে বেৰন হৈছিল।", art="court"),
 IN("The man known for reforming India's education system is|ভাৰতৰ শিক্ষা ব্যৱস্থাৰ সংস্কাৰৰ বাবে খ্যাত", ".|।", ["Lord Dalhousie|লৰ্ড ডালহৌচী", "Lord Cornwallis|লৰ্ড কৰ্ণৱালিছ", "Lord Mountbatten|লৰ্ড মাউণ্টবেটেন", "Lord Macaulay|লৰ্ড মেকলে"], 3, "Macaulay.|মেকলে।"),
 TF("Macaulay served as Governor-General.|মেকলে গৱৰ্ণৰ জেনেৰেল আছিল।", False, "He was Law Member of the Council.|তেওঁ পৰিষদৰ আইন সদস্য আছিল।"),
 SP("Macaulay's Minute dates from *1935.*|মেকলেৰ টোকাৰ তাৰিখ *১৯৩৫।*", "1835|১৮৩৫", "1835.|১৮৩৫।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Sati banned|সতীদাহ নিষিদ্ধ", "Charter Act|চাৰ্টাৰ আইন", "Macaulay's Minute|মেকলেৰ টোকা"], "1829, 1833, 1835.|১৮২৯, ১৮৩৩, ১৮৩৫।"),
 SC("Unscramble the author of the 1835 Minute.|১৮৩৫ৰ টোকাৰ লেখকক সজোৱা।", "MACAULAY", ["মে", "ক", "লে"], "Macaulay.|মেকলে।"),
)
u4 = U(4, "crown", "Dalhousie's annexations|ডালহৌচীৰ দখল",
 "Separate lapse from Awadh.|স্বত্ববিলোপ আৰু অযোধ্যা পৃথক কৰা।", "Finding recorded: Satara, Jhansi and Nagpur by lapse; Awadh on misrule.|প্ৰমাণ লিখা হ'ল: স্বত্ববিলোপত সাতাৰা, ঝাঁচী আৰু নাগপুৰ; কুশাসনৰ অজুহাতত অযোধ্যা।",
 ["Dalhousie was Governor-General from 1848 to 1856|ডালহৌচী ১৮৪৮ৰ পৰা ১৮৫৬লৈ গৱৰ্ণৰ জেনেৰেল", "Lapse applied when a ruler died without a male heir|পুৰুষ উত্তৰাধিকাৰী নথকাকৈ ৰজাৰ মৃত্যু হ'লে স্বত্ববিলোপ", "Satara, Jhansi and Nagpur were annexed this way|সাতাৰা, ঝাঁচী আৰু নাগপুৰ এইদৰে দখল হৈছিল", "Awadh was taken on the pretext of misrule|কুশাসনৰ অজুহাতত অযোধ্যা লোৱা হৈছিল"],
 S("No male heir, no state|পুৰুষ উত্তৰাধিকাৰী নাই, ৰাজ্য নাই", "[[lord-dalhousie|Dalhousie]] applied the <mark>[[doctrine-of-lapse|Doctrine of Lapse]]</mark>: a state could be annexed if its ruler died without a male heir.|[[lord-dalhousie|ডালহৌচীয়ে]] <mark>[[doctrine-of-lapse|স্বত্ববিলোপ নীতি]]</mark> প্ৰয়োগ কৰিছিল: পুৰুষ উত্তৰাধিকাৰী নথকাকৈ ৰজাৰ মৃত্যু হ'লে ৰাজ্য দখল কৰিব পাৰি।", "[[satara]], [[jhansi]] and Nagpur went this way.|[[satara|সাতাৰা]], [[jhansi|ঝাঁচী]] আৰু নাগপুৰ এইদৰে গ'ল।", art="seal"),
 S("Awadh is different|অযোধ্যা বেলেগ", "<mark>Awadh</mark> was annexed in 1856 on the pretext of misrule, not by lapse. Papers often blur the two.|<mark>অযোধ্যা</mark> ১৮৫৬ত স্বত্ববিলোপত নহয়, কুশাসনৰ অজুহাতত দখল হৈছিল। পৰীক্ষাত দুয়োটা প্ৰায়ে মিহলি কৰা হয়।", "These annexations fed the anger of 1857.|এই দখলে ১৮৫৭ৰ ক্ষোভ বঢ়াইছিল।", art="door"),
 OD("Which was NOT annexed by the Doctrine of Lapse?|কোনটো স্বত্ববিলোপত দখল হোৱা নাছিল?", ["Satara|সাতাৰা", "Jhansi|ঝাঁচী", "Nagpur|নাগপুৰ", "Awadh|অযোধ্যা"], 3, "Awadh was taken on the pretext of misrule.|অযোধ্যা কুশাসনৰ অজুহাতত লোৱা হৈছিল।"),
 MP("Tap Jhansi.|ঝাঁচী টিপা।", "jhansi", ["jhansi", "satara", "plassey", "calicut"], "In central India.|মধ্য ভাৰতত।"),
 TF("The Doctrine of Lapse is linked with Dalhousie.|স্বত্ববিলোপ নীতি ডালহৌচীৰ সৈতে জড়িত।", True, "He applied it most widely.|তেওঁ ইয়াক ব্যাপকভাৱে প্ৰয়োগ কৰিছিল।"),
 IN("Under lapse, a state could be annexed if its ruler had no|স্বত্ববিলোপত ৰাজ্য দখল হ'ব পাৰিছিল যদি ৰজাৰ", ".|নাথাকে।", ["army|সৈন্য", "male heir|পুৰুষ উত্তৰাধিকাৰী", "treaty|সন্ধি", "capital|ৰাজধানী"], 1, "No male heir.|পুৰুষ উত্তৰাধিকাৰী নাই।"),
 WH(["I was Governor-General until 1856.|মই ১৮৫৬লৈ গৱৰ্ণৰ জেনেৰেল আছিলোঁ।", "I annexed Awadh.|মই অযোধ্যা দখল কৰিছিলোঁ।"], ["Bentinck|বেণ্টিংক", "Dalhousie|ডালহৌচী", "Canning|কেনিং", "Curzon|কাৰ্জন"], 1, "Dalhousie.|ডালহৌচী।"),
)
test = TEST("Rank the men who ran Company India.|কোম্পানীৰ ভাৰত চলোৱা মানুহখিনিক ক্ৰমে সজোৱা।", "Recorded: titles, land, law and lapse.|লিখা হ'ল: উপাধি, ভূমি, আইন আৰু স্বত্ববিলোপ।",
 IN("The first Governor-General of India was|ভাৰতৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল", ".|।", ["Warren Hastings|ৱাৰেন হেষ্টিংছ", "Lord Dalhousie|লৰ্ড ডালহৌচী", "Lord William Bentinck|লৰ্ড উইলিয়াম বেণ্টিংক", "Lord Cornwallis|লৰ্ড কৰ্ণৱালিছ"], 2, "Bentinck.|বেণ্টিংক।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Regulating Act|ৰেগুলেটিং আইন", "Permanent Settlement|চিৰস্থায়ী বন্দোবস্ত", "Sati banned|সতীদাহ নিষিদ্ধ", "Macaulay's Minute|মেকলেৰ টোকা"], "1773, 1793, 1829, 1835.|১৭৭৩, ১৭৯৩, ১৮২৯, ১৮৩৫।"),
 MA([("Hastings|হেষ্টিংছ", "Governor-General of Bengal|বংগৰ গৱৰ্ণৰ জেনেৰেল"), ("Canning|কেনিং", "First Viceroy|প্ৰথম ভাইচৰয়"), ("Macaulay|মেকলে", "Law Member|আইন সদস্য")], "Person and post.|ব্যক্তি আৰু পদ।"),
 TF("Awadh was annexed by the Doctrine of Lapse.|স্বত্ববিলোপ নীতিত অযোধ্যা দখল হৈছিল।", False, "The pretext was misrule.|অজুহাত কুশাসন।"),
 MP("Tap Satara.|সাতাৰা টিপা।", "satara", ["satara", "jhansi", "plassey", "calicut"], "In Maharashtra.|মহাৰাষ্ট্ৰত।"),
 MC("Consider these statements. (1) Cornwallis made the Permanent Settlement. (2) Bentinck banned sati. (3) Macaulay was Viceroy. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) কৰ্ণৱালিছে চিৰস্থায়ী বন্দোবস্ত কৰিছিল। (২) বেণ্টিংকে সতীদাহ নিষিদ্ধ কৰিছিল। (৩) মেকলে ভাইচৰয় আছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 0, "Macaulay was Law Member.|মেকলে আইন সদস্য।"),
)
LESSON(19, "The Governors-General|গৱৰ্ণৰ জেনেৰেল সকল", "1773–1856|১৭৭৩–১৮৫৬", "Company rule|কোম্পানীৰ শাসন", "Evidence file 19|প্ৰমাণ নথি ১৯", "Who ran the Company's India?|কোম্পানীৰ ভাৰত কোনে চলাইছিল?",
 "Papers swap these names on purpose. Fix who held which title and what each man did.|পৰীক্ষাত এই নামবোৰ ইচ্ছাকৃতভাৱে সলোৱা হয়। কোনে কি উপাধি ধৰিছিল আৰু কি কৰিছিল, ঠিক কৰা।",
 sources, [u1, u2, u3, u4], test, ["jhansi", "satara", "plassey", "calicut"],
 timeline=[("1773", "Regulating Act|ৰেগুলেটিং আইন", "u1"), ("1793", "Permanent Settlement|চিৰস্থায়ী বন্দোবস্ত", "u2"), ("1829", "Sati banned|সতীদাহ নিষিদ্ধ", "u2"), ("1835", "Macaulay's Minute|মেকলেৰ টোকা", "u3")])
