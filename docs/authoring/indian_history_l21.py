#!/usr/bin/env python3
"""Lesson 21: The Revolt of 1857."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "mangal-pandey": ("person", "Mangal Pandey|মংগল পাণ্ডে", "Sepoy whose protest at Barrackpore came in March 1857|১৮৫৭ৰ মাৰ্চত বেৰাকপুৰত প্ৰতিবাদ কৰা চিপাহী"),
 "bahadur-shah-ii": ("person", "Bahadur Shah II|বাহাদুৰ শ্বাহ দ্বিতীয়", "Last Mughal emperor, figurehead of the rebels at Delhi|শেষ মোগল সম্ৰাট, দিল্লীত বিদ্ৰোহীৰ নামমাত্ৰ নেতা"),
 "rani-lakshmibai": ("person", "Rani Lakshmibai|ৰাণী লক্ষ্মীবাই", "Rani of Jhansi who led forces in 1857 and 1858|১৮৫৭–৫৮ত সৈন্যৰ নেতৃত্ব দিয়া ঝাঁচীৰ ৰাণী"),
 "nana-sahib": ("person", "Nana Sahib|নানা চাহেব", "Rebel leader at Kanpur|কানপুৰৰ বিদ্ৰোহী নেতা"),
 "begum-hazrat-mahal": ("person", "Begum Hazrat Mahal|বেগম হজৰত মহল", "Rebel leader at Lucknow|লক্ষ্ণৌৰ বিদ্ৰোহী নেতা"),
 "kunwar-singh": ("person", "Kunwar Singh|কুঁৱৰ সিং", "Rebel leader in Bihar|বিহাৰৰ বিদ্ৰোহী নেতা"),
 "meerut": ("place", "Meerut|মীৰাট", "Cantonment near Delhi where the rising began|দিল্লীৰ ওচৰৰ সেনানিবাস, য'ত বিদ্ৰোহ আৰম্ভ হৈছিল", [28.98, 77.71]),
 "barrackpore": ("place", "Barrackpore|বেৰাকপুৰ", "Cantonment near Calcutta|কলিকতাৰ ওচৰৰ সেনানিবাস", [22.76, 88.37]),
 "kanpur": ("place", "Kanpur|কানপুৰ", "City on the Ganga, a centre of 1857|গংগা পাৰৰ নগৰ, ১৮৫৭ৰ এটা কেন্দ্ৰ", [26.45, 80.33]),
 "lucknow": ("place", "Lucknow|লক্ষ্ণৌ", "Capital of Awadh|অযোধ্যাৰ ৰাজধানী", [26.85, 80.95]),
 "gwalior": ("place", "Gwalior|গোৱালিয়ৰ", "Place of the rebels' final defeat in June 1858|১৮৫৮ৰ জুনত বিদ্ৰোহীৰ শেষ পৰাজয়ৰ ঠাই", [26.22, 78.18]),
})
sources = [
 src("Wikipedia, Indian Rebellion of 1857", "https://en.wikipedia.org/wiki/Indian_Rebellion_of_1857", "Used as a guide: 10 May at Meerut, causes, Mangal Pandey, Bahadur Shah II, Gwalior, the 1858 Act, the three names. Leaders by centre need checking against a standard history. Check in review."),
 src("Wikipedia, Governor-General of India", "https://en.wikipedia.org/wiki/Governor-General_of_India", "Used as a guide: 1858, Canning, Viceroy. Check in review."),
]
BOX = {"base": "india", "box": [74, 22, 90, 31]}
u1 = U(1, "flag", "Why it broke out|কিয় বিদ্ৰোহ হ'ল",
 "Separate the spark from the fuel.|জুইকুৰা আৰু ইন্ধন পৃথক কৰা।", "Finding recorded: cartridges were the spark; annexations, taxes and fears were the fuel.|প্ৰমাণ লিখা হ'ল: কাৰ্তুজ জুইকুৰা; দখল, কৰ আৰু ভয় ইন্ধন।",
 ["Rumours of greased cartridges angered sepoys|চৰ্বি লগোৱা কাৰ্তুজৰ গুজৱে চিপাহীক ক্ষুব্ধ কৰিছিল", "Belief mattered more than proof|প্ৰমাণতকৈ বিশ্বাস ডাঙৰ আছিল", "Lapse and Awadh's annexation were grievances|স্বত্ববিলোপ আৰু অযোধ্যা দখল ক্ষোভৰ কাৰণ", "Mangal Pandey's protest came in March 1857|১৮৫৭ৰ মাৰ্চত মংগল পাণ্ডেৰ প্ৰতিবাদ"],
 S("The cartridge rumour|কাৰ্তুজৰ গুজৱ", "Sepoys believed the new Enfield cartridges were greased in ways that offended their faith. Historians stress that the <mark>belief</mark> mattered more than proof.|চিপাহীসকলে বিশ্বাস কৰিছিল যে নতুন এনফিল্ড কাৰ্তুজত তেওঁলোকৰ ধৰ্মত আঘাত দিয়া চৰ্বি লগোৱা হৈছে। ইতিহাসবিদৰ মতে প্ৰমাণতকৈ <mark>বিশ্বাস</mark> ডাঙৰ আছিল।", art="seal"),
 S("Older anger|পুৰণি ক্ষোভ", "There was fuel already: the Doctrine of Lapse, the annexation of Awadh, heavy land taxes and slow promotions.|ইন্ধন আগতেই আছিল: স্বত্ববিলোপ, অযোধ্যা দখল, গধুৰ ভূমি কৰ আৰু লেহেমীয়া পদোন্নতি।", "In March 1857 [[mangal-pandey|Mangal Pandey]] made his protest at <mark>[[barrackpore|Barrackpore]]</mark>.|১৮৫৭ৰ মাৰ্চত [[mangal-pandey|মংগল পাণ্ডেয়ে]] <mark>[[barrackpore|বেৰাকপুৰত]]</mark> প্ৰতিবাদ কৰিছিল।", art="court"),
 TF("The revolt had only one cause.|বিদ্ৰোহৰ এটাই কাৰণ আছিল।", False, "The cartridges were a spark on older grievances.|পুৰণি ক্ষোভত কাৰ্তুজ এটা জুইকুৰা আছিল।"),
 MP("Tap Barrackpore.|বেৰাকপুৰ টিপা।", "barrackpore", ["barrackpore", "meerut", "jhansi", "bombay"], "Near Calcutta.|কলিকতাৰ ওচৰত।"),
 OD("Which was NOT a grievance before 1857?|১৮৫৭ৰ আগৰ ক্ষোভৰ কোনটো নহয়?", ["Annexation of Awadh|অযোধ্যা দখল", "Doctrine of Lapse|স্বত্ববিলোপ নীতি", "Heavy land taxes|গধুৰ ভূমি কৰ", "Rowlatt Act|ৰাউলাট আইন"], 3, "The Rowlatt Act came in 1919.|ৰাউলাট আইন ১৯১৯ত আহিছিল।"),
 IN("The rifle at the centre of the rumour was the|গুজৱৰ কেন্দ্ৰত থকা ৰাইফল", ".|।", ["Enfield|এনফিল্ড", "Maxim|মেক্সিম", "Sten|ষ্টেন", "Bren|ব্ৰেন"], 0, "The Enfield.|এনফিল্ড।"),
 WH(["I was a sepoy.|মই চিপাহী।", "My protest came at Barrackpore.|বেৰাকপুৰত মোৰ প্ৰতিবাদ।", "It was March 1857.|সেয়া ১৮৫৭ৰ মাৰ্চ।"], ["Nana Sahib|নানা চাহেব", "Mangal Pandey|মংগল পাণ্ডে", "Kunwar Singh|কুঁৱৰ সিং", "Tantia Tope|তাঁতিয়া টোপে"], 1, "Mangal Pandey.|মংগল পাণ্ডে।"),
)
u2 = U(2, "walk", "From Meerut to Delhi|মীৰাটৰ পৰা দিল্লীলৈ",
 "Trace how the rising spread.|বিদ্ৰোহ কেনেকৈ বিয়পিল, অনুসৰণ কৰা।", "Finding recorded: Meerut on 10 May, then Delhi and Bahadur Shah II.|প্ৰমাণ লিখা হ'ল: ১০ মে'ত মীৰাট, তাৰ পিছত দিল্লী আৰু বাহাদুৰ শ্বাহ দ্বিতীয়।",
 ["The rising began at Meerut on 10 May 1857|১৮৫৭ৰ ১০ মে'ত মীৰাটত বিদ্ৰোহ আৰম্ভ হৈছিল", "Rebels went to Delhi|বিদ্ৰোহী দিল্লীলৈ গৈছিল", "They proclaimed Bahadur Shah II as their leader|তেওঁলোকে বাহাদুৰ শ্বাহ দ্বিতীয়ক নেতা ঘোষণা কৰিছিল", "It spread across the upper Ganga plain and central India|ই ওপৰ গংগা সমভূমি আৰু মধ্য ভাৰতত বিয়পিল"],
 S("10 May|১০ মে'", "On <mark>10 May 1857</mark> sepoys rose at [[meerut]], about 40 miles from Delhi, and the revolt spread fast.|<mark>১৮৫৭ৰ ১০ মে'ত</mark> দিল্লীৰ প্ৰায় ৪০ মাইল দূৰৰ [[meerut|মীৰাটত]] চিপাহীসকলে বিদ্ৰোহ কৰিলে, ই দ্ৰুতগতিত বিয়পিল।", map={**BOX, "show": ["meerut", "delhi", "barrackpore"]}),
 S("An old emperor|বৃদ্ধ সম্ৰাট", "Rebels proclaimed the aged Mughal emperor, <mark>[[bahadur-shah-ii|Bahadur Shah II]]</mark>, as their figurehead at Delhi.|বিদ্ৰোহীসকলে বৃদ্ধ মোগল সম্ৰাট <mark>[[bahadur-shah-ii|বাহাদুৰ শ্বাহ দ্বিতীয়ক]]</mark> দিল্লীত নামমাত্ৰ নেতা ঘোষণা কৰিছিল।", "The British retook Delhi by late September.|ছেপ্টেম্বৰৰ শেষলৈ ব্ৰিটিছে দিল্লী পুনৰ ল'লে।", art="court"),
 IN("The Revolt of 1857 began at|১৮৫৭ৰ বিদ্ৰোহ আৰম্ভ হৈছিল", ".|ত।", ["Delhi|দিল্লী", "Meerut|মীৰাট", "Kanpur|কানপুৰ", "Jhansi|ঝাঁচী"], 1, "Meerut, 10 May.|১০ মে'ত মীৰাট।"),
 MP("Tap Meerut.|মীৰাট টিপা।", "meerut", ["meerut", "barrackpore", "bombay", "jhansi"], "Near Delhi.|দিল্লীৰ ওচৰত।"),
 TF("Bahadur Shah II was the rebels' figurehead.|বাহাদুৰ শ্বাহ দ্বিতীয় বিদ্ৰোহীৰ নামমাত্ৰ নেতা আছিল।", True, "They proclaimed him at Delhi.|তেওঁলোকে দিল্লীত তেওঁক ঘোষণা কৰিছিল।"),
 OR("Put 1857 in order.|১৮৫৭ ক্ৰমে সজোৱা।", ["Mangal Pandey's protest|মংগল পাণ্ডেৰ প্ৰতিবাদ", "Rising at Meerut|মীৰাটত বিদ্ৰোহ", "British retake Delhi|ব্ৰিটিছে দিল্লী পুনৰ লয়"], "March, May, September.|মাৰ্চ, মে', ছেপ্টেম্বৰ।"),
 SP("The rising began at Meerut in *1847.*|*১৮৪৭ত* মীৰাটত বিদ্ৰোহ আৰম্ভ হৈছিল।", "1857|১৮৫৭ত", "1857.|১৮৫৭।"),
)
u3 = U(3, "star", "Leaders by centre|কেন্দ্ৰ অনুসৰি নেতা",
 "Pair each centre with its leader.|প্ৰতিটো কেন্দ্ৰ নেতাৰ সৈতে মিলোৱা।", "Finding recorded: Lakshmibai at Jhansi, with others elsewhere; Gwalior ended it.|প্ৰমাণ লিখা হ'ল: ঝাঁচীত লক্ষ্মীবাই, আন ঠাইত আন নেতা; গোৱালিয়ৰত শেষ।",
 ["Rani Lakshmibai led at Jhansi|ৰাণী লক্ষ্মীবাইয়ে ঝাঁচীত নেতৃত্ব দিছিল", "Nana Sahib led at Kanpur|নানা চাহেবে কানপুৰত নেতৃত্ব দিছিল", "Begum Hazrat Mahal led at Lucknow|বেগম হজৰত মহলে লক্ষ্ণৌত নেতৃত্ব দিছিল", "Rebels were defeated at Gwalior in June 1858|১৮৫৮ৰ জুনত গোৱালিয়ৰত বিদ্ৰোহী পৰাস্ত হৈছিল"],
 S("Many centres|বহু কেন্দ্ৰ", "The rising had no single head. <b>Jhansi: Rani Lakshmibai. Kanpur: Nana Sahib. Lucknow: Begum Hazrat Mahal. Bihar: Kunwar Singh.</b>|বিদ্ৰোহৰ এজন মূৰব্বী নাছিল। <b>ঝাঁচী: ৰাণী লক্ষ্মীবাই। কানপুৰ: নানা চাহেব। লক্ষ্ণৌ: বেগম হজৰত মহল। বিহাৰ: কুঁৱৰ সিং।</b>", map={**BOX, "show": ["jhansi", "kanpur", "lucknow", "gwalior"]}),
 LINK(S("The end, and Assam|অন্ত আৰু অসম", "Fighting ran into 1858, and the rebels were finally defeated at <mark>[[gwalior|Gwalior]]</mark> in June.|যুদ্ধ ১৮৫৮লৈ চলিল, জুনত <mark>[[gwalior|গোৱালিয়ৰত]]</mark> বিদ্ৰোহী শেষত পৰাস্ত হ'ল।", "Sikh princes, Punjab and several large states backed the British. In Assam, Maniram Dewan was caught up in a plot.|শিখ ৰজা, পঞ্জাব আৰু কেইবাখনো ডাঙৰ ৰাজ্যই ব্ৰিটিছক সমৰ্থন কৰিছিল। অসমত মণিৰাম দেৱান এটা ষড়যন্ত্ৰত জড়িত হৈছিল।", art="door"),
  "british-03-maniram-1857", 40, 4, "The plot of 1857|১৮৫৭ৰ ষড়যন্ত্ৰ", "The Assam History course tells Maniram Dewan's story.|অসমৰ ইতিহাস পাঠ্যক্ৰমত মণিৰাম দেৱানৰ কাহিনী আছে।"),
 MA([("Jhansi|ঝাঁচী", "Rani Lakshmibai|ৰাণী লক্ষ্মীবাই"), ("Kanpur|কানপুৰ", "Nana Sahib|নানা চাহেব"), ("Lucknow|লক্ষ্ণৌ", "Begum Hazrat Mahal|বেগম হজৰত মহল"), ("Bihar|বিহাৰ", "Kunwar Singh|কুঁৱৰ সিং")], "Centre and leader.|কেন্দ্ৰ আৰু নেতা।"),
 IN("Among these, the leader of the 1857 rebellion was|এইবোৰৰ ভিতৰত ১৮৫৭ৰ বিদ্ৰোহৰ নেতা", ".|।", ["Rani Ahilya Bai|ৰাণী অহল্যা বাই", "Rani Laxmi Bai|ৰাণী লক্ষ্মীবাই", "Chand Bibi|চান্দ বিবি", "Rezia Sultana|ৰাজিয়া ছুলতানা"], 1, "Rani Laxmi Bai of Jhansi.|ঝাঁচীৰ ৰাণী লক্ষ্মীবাই।"),
 MP("Tap Lucknow.|লক্ষ্ণৌ টিপা।", "lucknow", ["lucknow", "bombay", "barrackpore", "meerut"], "Capital of Awadh.|অযোধ্যাৰ ৰাজধানী।"),
 TF("All Indian rulers joined the revolt.|সকলো ভাৰতীয় শাসক বিদ্ৰোহত যোগ দিছিল।", False, "Sikh princes and several states backed the British.|শিখ ৰজা আৰু কেইবাখনো ৰাজ্যই ব্ৰিটিছক সমৰ্থন কৰিছিল।"),
 SP("Maniram Dewan was involved in the *1942* rising.|মণিৰাম দেৱান *১৯৪২ৰ* বিদ্ৰোহত জড়িত আছিল।", "1857|১৮৫৭ৰ", "He was linked to 1857.|তেওঁ ১৮৫৭ৰ সৈতে জড়িত।"),
)
u4 = U(4, "court", "A new government|নতুন চৰকাৰ",
 "State what changed after 1858.|১৮৫৮ৰ পিছত কি সলনি হ'ল, কোৱা।", "Finding recorded: the Crown replaced the Company, and Canning became Viceroy.|প্ৰমাণ লিখা হ'ল: কোম্পানীৰ ঠাইত ৰাজমুকুট, কেনিং ভাইচৰয়।",
 ["The Government of India Act 1858 ended Company rule|১৮৫৮ৰ ভাৰত চৰকাৰ আইনে কোম্পানীৰ শাসন শেষ কৰিছিল", "The title Viceroy began in 1858|১৮৫৮ত ভাইচৰয় উপাধি আৰম্ভ", "Canning was the first Viceroy|কেনিং প্ৰথম ভাইচৰয়", "The revolt has several names|বিদ্ৰোহৰ কেইবাটাও নাম আছে"],
 S("Crown for Company|কোম্পানীৰ ঠাইত ৰাজমুকুট", "The <mark>Government of India Act 1858</mark> dissolved Company rule and placed India under the Crown. [[lord-canning|Canning]] became the first <mark>Viceroy</mark>.|<mark>১৮৫৮ৰ ভাৰত চৰকাৰ আইনে</mark> কোম্পানীৰ শাসন শেষ কৰি ভাৰতক ৰাজমুকুটৰ অধীন কৰিছিল। [[lord-canning|কেনিং]] প্ৰথম <mark>ভাইচৰয়</mark> হৈছিল।", art="court"),
 S("What to call it|ইয়াক কি বোলা হ'ব", "It is called the Sepoy Mutiny, the Revolt of 1857 and the First War of Independence. Each name carries a view of what it was.|ইয়াক চিপাহী বিদ্ৰোহ, ১৮৫৭ৰ বিদ্ৰোহ আৰু প্ৰথম স্বাধীনতা যুদ্ধ বোলা হয়। প্ৰতিটো নামত এটা দৃষ্টিভংগী আছে।", art="scroll"),
 IN("The title Viceroy was given in|ভাইচৰয় উপাধি দিয়া হৈছিল", ".|ত।", ["1867|১৮৬৭", "1858|১৮৫৮", "1876|১৮৭৬", "1905|১৯০৫"], 1, "1858.|১৮৫৮।"),
 TF("The East India Company kept ruling India after 1858.|১৮৫৮ৰ পিছতো ইষ্ট ইণ্ডিয়া কোম্পানীয়ে ভাৰত শাসন কৰিছিল।", False, "The Crown took over.|ৰাজমুকুটে দায়িত্ব ল'লে।"),
 YR("Place each event on the line.|প্ৰতিটো ঘটনা ৰেখাত ৰাখা।", [(1857, "Rising at Meerut|মীৰাটত বিদ্ৰোহ"), (1885, "Congress founded|কংগ্ৰেছ প্ৰতিষ্ঠা")], [("Sati banned, 1829|সতীদাহ নিষিদ্ধ, ১৮২৯", 0), ("Viceroy title, 1858|ভাইচৰয় উপাধি, ১৮৫৮", 1), ("Arya Samaj, 1875|আৰ্য সমাজ, ১৮৭৫", 1)], "1829 → 1857 → 1858 → 1875 → 1885.|১৮২৯ → ১৮৫৭ → ১৮৫৮ → ১৮৭৫ → ১৮৮৫।"),
 WH(["I was Governor-General in 1857.|১৮৫৭ত মই গৱৰ্ণৰ জেনেৰেল আছিলোঁ।", "I became the first Viceroy.|মই প্ৰথম ভাইচৰয় হৈছিলোঁ।"], ["Dalhousie|ডালহৌচী", "Canning|কেনিং", "Curzon|কাৰ্জন", "Bentinck|বেণ্টিংক"], 1, "Canning.|কেনিং।"),
 OD("Which is NOT a name for the events of 1857?|কোনটো ১৮৫৭ৰ ঘটনাৰ নাম নহয়?", ["Sepoy Mutiny|চিপাহী বিদ্ৰোহ", "First War of Independence|প্ৰথম স্বাধীনতা যুদ্ধ", "Revolt of 1857|১৮৫৭ৰ বিদ্ৰোহ", "Quit India|ভাৰত ত্যাগ"], 3, "Quit India was in 1942.|ভাৰত ত্যাগ ১৯৪২ত।"),
)
test = TEST("Tell 1857 from spark to settlement.|জুইকুৰাৰ পৰা নিষ্পত্তিলৈ ১৮৫৭ কোৱা।", "Recorded: causes, centres, leaders and the Crown.|লিখা হ'ল: কাৰণ, কেন্দ্ৰ, নেতা আৰু ৰাজমুকুট।",
 IN("A leader of the 1857 rebellion was|১৮৫৭ৰ বিদ্ৰোহৰ এগৰাকী নেতা আছিল", ".|।", ["Rani Ahilya Bai|ৰাণী অহল্যা বাই", "Rani Laxmi Bai|ৰাণী লক্ষ্মীবাই", "Chand Bibi|চান্দ বিবি", "Rezia Sultana|ৰাজিয়া ছুলতানা"], 1, "Rani Laxmi Bai, among others.|ৰাণী লক্ষ্মীবাই, আন নেতাৰ সৈতে।"),
 MA([("Meerut|মীৰাট", "Rising begins|বিদ্ৰোহ আৰম্ভ"), ("Gwalior|গোৱালিয়ৰ", "Final defeat|শেষ পৰাজয়"), ("Delhi|দিল্লী", "Bahadur Shah II|বাহাদুৰ শ্বাহ দ্বিতীয়")], "Place and role.|ঠাই আৰু ভূমিকা।"),
 TF("The title Viceroy dates from 1858.|ভাইচৰয় উপাধি ১৮৫৮ৰ পৰা।", True, "With Canning.|কেনিঙৰ সৈতে।"),
 MP("Tap Jhansi.|ঝাঁচী টিপা।", "jhansi", ["jhansi", "barrackpore", "bombay", "meerut"], "Jhansi.|ঝাঁচী।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Doctrine of Lapse under Dalhousie|ডালহৌচীৰ স্বত্ববিলোপ", "Rising at Meerut|মীৰাটত বিদ্ৰোহ", "Government of India Act|ভাৰত চৰকাৰ আইন"], "Before 1856, 1857, 1858.|১৮৫৬ৰ আগত, ১৮৫৭, ১৮৫৮।"),
 MC("Consider these statements. (1) The revolt began at Meerut. (2) Nana Sahib led at Lucknow. (3) The 1858 Act ended Company rule. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) বিদ্ৰোহ মীৰাটত আৰম্ভ হৈছিল। (২) নানা চাহেবে লক্ষ্ণৌত নেতৃত্ব দিছিল। (৩) ১৮৫৮ৰ আইনে কোম্পানীৰ শাসন শেষ কৰিছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Nana Sahib led at Kanpur.|নানা চাহেবে কানপুৰত নেতৃত্ব দিছিল।"),
)
LESSON(21, "The Revolt of 1857|১৮৫৭ৰ বিদ্ৰোহ", "1857–1858|১৮৫৭–১৮৫৮", "Company rule|কোম্পানীৰ শাসন", "Evidence file 21|প্ৰমাণ নথি ২১", "One year, many risings|এটা বছৰ, বহু বিদ্ৰোহ",
 "It began with a rumour and ended a Company. Follow the spark, the centres and what changed.|ই গুজৱৰে আৰম্ভ হৈছিল আৰু এটা কোম্পানীৰ অন্ত পেলাইছিল। জুইকুৰা, কেন্দ্ৰ আৰু পৰিৱৰ্তন অনুসৰণ কৰা।",
 sources, [u1, u2, u3, u4], test, ["meerut", "barrackpore", "jhansi", "bombay", "lucknow"],
 timeline=[("1857", "10 May: rising at Meerut|১০ মে': মীৰাটত বিদ্ৰোহ", "u2"), ("1858", "June: defeat at Gwalior|জুন: গোৱালিয়ৰত পৰাজয়", "u3"), ("1858", "Government of India Act|ভাৰত চৰকাৰ আইন", "u4")])
