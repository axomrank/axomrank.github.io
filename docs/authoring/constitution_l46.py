#!/usr/bin/env python3
"""Lesson 46: The Sixth Schedule. Run from the repository root."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from constitution_pilot import *  # noqa: E402,F403

ONE = B("One word is wrong. Tap it.", "এটা শব্দ ভুল। সেইটো টিপা।")

add_entities({
    "nichols-roy": {"type": "person", "name": B("J. J. M. Nichols-Roy", "জে. জে. এম. নিকলছ-ৰয়"), "meaning": B("Assembly member who spoke for District Councils on 6 September 1949", "১৯৪৯ চনৰ ৬ ছেপ্টেম্বৰত জিলা পৰিষদৰ সপক্ষে কোৱা গণপৰিষদৰ সদস্য")},
    "kuladhar-chaliha": {"type": "person", "name": B("Kuladhar Chaliha", "কুলধৰ চলিহা"), "meaning": B("Assembly member from Assam who objected to the councils' powers in the 1949 debate", "১৯৪৯ চনৰ বিতৰ্কত পৰিষদৰ ক্ষমতাৰ বিৰোধিতা কৰা অসমৰ গণপৰিষদ সদস্য")},
    "autonomous-district": {"type": "term", "name": B("Autonomous district", "স্বায়ত্ত শাসিত জিলা"), "meaning": B("A tribal area listed in the table to paragraph 20 of the Sixth Schedule", "ষষ্ঠ অনুসূচীৰ পেৰেগ্ৰাফ ২০-ৰ তালিকাত থকা জনজাতীয় ক্ষেত্ৰ")},
    "district-council": {"type": "term", "name": B("District Council", "জিলা পৰিষদ"), "meaning": B("The body that administers an autonomous district", "স্বায়ত্ত শাসিত জিলা প্ৰশাসন চলোৱা সংস্থা")},
    "bodoland-territorial-council": {"type": "term", "name": B("Bodoland Territorial Council", "বড়োলেণ্ড টেৰিটৰিয়েল কাউন্সিল"), "meaning": B("The District Council for the Bodoland Territorial Areas District", "বড়োলেণ্ড টেৰিটৰিয়েল এৰিয়াছ ডিষ্ট্ৰিক্টৰ জিলা পৰিষদ")},
})

mission = {"label": B("Council map 46", "পৰিষদৰ মানচিত্ৰ ৪৬"), "title": B("Map self-rule in the hills", "পাহাৰৰ স্বশাসন বুজা"),
           "hook": B("Why does part of Assam run some of its own affairs under a Schedule of the Constitution? Follow the debate, the map and the limits.",
                     "সংবিধানৰ এখন অনুসূচীৰ অধীনত অসমৰ এটা অংশই কিয় নিজৰ কিছুমান কাম নিজে চলায়? বিতৰ্ক, মানচিত্ৰ আৰু সীমা অনুসৰণ কৰা।")}

sources = [
    {"title": "The Constitution of India, as on 10 September 2026, Articles 244, 244A, 332, 371B and the Sixth Schedule with its Assam footnotes", "url": "https://www.legislative.gov.in/static/uploads/2025/07/95ef471035ee0b5e4e5b1cac3d3584c1.pdf", "local_source": "Constitution sources/constitution-of-india-2026-en.pdf", "used_for": "All provisions, paragraph numbers and the Bodoland Territorial Council composition."},
    {"title": "Constituent Assembly Debates, 5 and 6 September 1949", "url": "https://www.constitutionofindia.net/debates/06-sep-1949/", "used_for": "Bordoloi, Nichols-Roy and Chaliha in the debate; the Assam tribal sub-committee and its chairman. Only the first part of the 6 September record was read."},
    {"title": "Axomrank Assam History lessons modern-assam-08 and peoples-councils-movements-06", "url": "", "used_for": "North Cachar Hills and Dima Hasao names; statutory councils under Assam Acts. These repeat earlier lesson research, not fresh sources."},
]

COUNCIL_MAP = {"box": [89.6, 24.7, 94.3, 27.1], "districts": ["kokrajhar", "chirang", "baksa", "udalguri", "karbi-anglong", "west-karbi-anglong", "dima-hasao"],
               "texts": [{"t": B("BODOLAND", "বড়োলেণ্ড"), "at": [26.75, 90.9]}, {"t": B("KARBI ANGLONG", "কাৰ্বি আংলং"), "at": [26.15, 93.2]}, {"t": B("DIMA HASAO", "ডিমা হাছাও"), "at": [25.25, 93.0]}]}

u1 = unit("u1", "hands", B("The 1949 argument", "১৯৪৯ চনৰ তৰ্ক"),
    B("Hear both sides of the debate.", "বিতৰ্কৰ দুয়োটা পক্ষ শুনা।"),
    B("Finding recorded: the Schedule answered a real argument about self-government and unity.", "প্ৰমাণ লিখা হ'ল: অনুসূচীখন স্বশাসন আৰু ঐক্যৰ এক বাস্তৱ তৰ্কৰ উত্তৰ আছিল।"),
    [B("Article 244(2) applies the Sixth Schedule to four States", "অনুচ্ছেদ ২৪৪(২)-এ চাৰিখন ৰাজ্যত ষষ্ঠ অনুসূচী প্ৰযোজ্য কৰে"), B("The four are Assam, Meghalaya, Tripura and Mizoram", "চাৰিখন হ'ল অসম, মেঘালয়, ত্ৰিপুৰা আৰু মিজোৰাম"),
     B("Gopinath Bordoloi chaired the Assam tribal sub-committee", "গোপীনাথ বৰদলৈ অসমৰ জনজাতীয় উপ-সমিতিৰ অধ্যক্ষ আছিল"), B("The Assembly debated the Schedule in September 1949", "১৯৪৯ চনৰ ছেপ্টেম্বৰত গণপৰিষদে অনুসূচীখন আলোচনা কৰিছিল")],
    [story(B("A Schedule for four States", "চাৰিখন ৰাজ্যৰ অনুসূচী"),
           [B("[[art-244]] applies the [[sixth-schedule|Sixth Schedule]] to tribal areas in <mark>Assam, Meghalaya, Tripura and Mizoram</mark>.", "[[art-244]]-এ [[sixth-schedule|ষষ্ঠ অনুসূচী]] <mark>অসম, মেঘালয়, ত্ৰিপুৰা আৰু মিজোৰামৰ</mark> জনজাতীয় ক্ষেত্ৰত প্ৰযোজ্য কৰে।"),
            B("The Assembly had before it recommendations from the Assam tribal sub-committee chaired by [[gopinath-bordoloi|Gopinath Bordoloi]].", "গণপৰিষদৰ সন্মুখত [[gopinath-bordoloi|গোপীনাথ বৰদলৈৰ]] অধ্যক্ষতাৰ অসম জনজাতীয় উপ-সমিতিৰ পৰামৰ্শ আছিল।")], art="scroll"),
     story(B("Two voices, 6 September 1949", "দুটা মাত, ৬ ছেপ্টেম্বৰ ১৯৪৯"),
           [B("[[nichols-roy|Rev. J. J. M. Nichols-Roy]] spoke of giving hill peoples “a certain measure of self-government”.", "[[nichols-roy|ৰেভাৰেণ্ড জে. জে. এম. নিকলছ-ৰয়ে]] পাহাৰীয়া লোকক “কিছু পৰিমাণৰ স্বশাসন” দিয়াৰ কথা কৈছিল (অনুবাদ)।"),
            B("[[kuladhar-chaliha|Kuladhar Chaliha]] objected. Letting councils run the administration, he said, would be “a negation of justice or administration”.", "[[kuladhar-chaliha|কুলধৰ চলিহাই]] বিৰোধিতা কৰিছিল। পৰিষদক প্ৰশাসন চলাবলৈ দিলে সি “ন্যায় বা প্ৰশাসনৰ অস্বীকাৰ” হ'ব বুলি তেওঁ কৈছিল (অনুবাদ)।")], art="court"),
     odd(B("Which State is not under the Sixth Schedule?", "কোনখন ৰাজ্য ষষ্ঠ অনুসূচীৰ অধীনত নহয়?"), [B("Assam", "অসম"), B("Tripura", "ত্ৰিপুৰা"), B("Manipur", "মণিপুৰ"), B("Mizoram", "মিজোৰাম")], 2, B("Article 244(2) names Assam, Meghalaya, Tripura and Mizoram.", "অনুচ্ছেদ ২৪৪(২)-এ অসম, মেঘালয়, ত্ৰিপুৰা আৰু মিজোৰামৰ নাম লৈছে।")),
     match([(B("Nichols-Roy", "নিকলছ-ৰয়"), B("“A certain measure of self-government”", "“কিছু পৰিমাণৰ স্বশাসন”")), (B("Kuladhar Chaliha", "কুলধৰ চলিহা"), B("Objected to councils running administration", "পৰিষদৰ প্ৰশাসনৰ বিৰোধিতা")), (B("Gopinath Bordoloi", "গোপীনাথ বৰদলৈ"), B("Chaired the sub-committee", "উপ-সমিতিৰ অধ্যক্ষ"))], B("Three Assam voices, three roles.", "অসমৰ তিনিটা মাত, তিনিটা ভূমিকা।")),
     who([B("I led Assam's government in the 1940s.", "১৯৪০ৰ দশকত মই অসমৰ চৰকাৰৰ নেতৃত্ব দিছিলোঁ।"), B("I chaired the Assam tribal sub-committee.", "মই অসম জনজাতীয় উপ-সমিতিৰ অধ্যক্ষ আছিলোঁ।"), B("I defended the Sixth Schedule in the Assembly.", "গণপৰিষদত মই ষষ্ঠ অনুসূচীৰ সপক্ষে কৈছিলোঁ।")],
         [B("Gopinath Bordoloi", "গোপীনাথ বৰদলৈ"), B("Kuladhar Chaliha", "কুলধৰ চলিহা"), B("B. R. Ambedkar", "বি. আৰ. আম্বেদকাৰ")], 0, B("Bordoloi defended it on 6 September 1949.", "১৯৪৯ চনৰ ৬ ছেপ্টেম্বৰত বৰদলৈয়ে ইয়াৰ সপক্ষে কৈছিল।")),
     tf(B("Everyone from Assam in the Assembly agreed with the Schedule.", "গণপৰিষদত অসমৰ সকলোৱে অনুসূচীখন সমৰ্থন কৰিছিল।"), False, B("Kuladhar Chaliha objected in the debate.", "কুলধৰ চলিহাই বিতৰ্কত বিৰোধিতা কৰিছিল।")),
     spot(ONE, "The Sixth Schedule applies under Article 356.", "ষষ্ঠ অনুসূচী অনুচ্ছেদ ৩৫৬-ৰ অধীনত প্ৰযোজ্য।", 6, 3, B("→ 244", "→ ২৪৪"), B("356 → 244", "৩৫৬ → ২৪৪"), B("Article 244(2) applies the Sixth Schedule.", "অনুচ্ছেদ ২৪৪(২)-এ ষষ্ঠ অনুসূচী প্ৰযোজ্য কৰে।"))])

u2 = unit("u2", "home", B("District, region, council", "জিলা, অঞ্চল, পৰিষদ"),
    B("Learn the building blocks of the Schedule.", "অনুসূচীৰ মূল গঠন শিকা।"),
    B("Finding recorded: autonomous districts have District Councils of up to thirty members.", "প্ৰমাণ লিখা হ'ল: স্বায়ত্ত শাসিত জিলাত সৰ্বাধিক ত্ৰিশজন সদস্যৰ জিলা পৰিষদ থাকে।"),
    [B("Each listed tribal area is an autonomous district", "তালিকাভুক্ত প্ৰতিটো জনজাতীয় ক্ষেত্ৰ স্বায়ত্ত শাসিত জিলা"), B("The Governor may divide it into autonomous regions", "ৰাজ্যপালে ইয়াক স্বায়ত্ত শাসিত অঞ্চলত ভাগ কৰিব পাৰে"),
     B("A District Council has at most thirty members", "জিলা পৰিষদত সৰ্বাধিক ত্ৰিশজন সদস্য"), B("At most four are nominated by the Governor", "সৰ্বাধিক চাৰিজন ৰাজ্যপালে মনোনীত কৰে")],
    [story(B("From table to district", "তালিকাৰ পৰা জিলা"),
           [B("Each item in the table to paragraph 20 is an [[autonomous-district|autonomous district]].", "পেৰেগ্ৰাফ ২০-ৰ তালিকাৰ প্ৰতিটো বিষয় এখন [[autonomous-district|স্বায়ত্ত শাসিত জিলা]]।"),
            B("If different Scheduled Tribes live there, the Governor may divide it into <mark>autonomous regions</mark>.", "তাত বিভিন্ন অনুসূচিত জনজাতি থাকিলে ৰাজ্যপালে ইয়াক <mark>স্বায়ত্ত শাসিত অঞ্চলত</mark> ভাগ কৰিব পাৰে।")], art="scroll"),
     story(B("Thirty seats, four nominated", "ত্ৰিশটা আসন, চাৰিজন মনোনীত"),
           [B("Each district has a [[district-council|District Council]] of <mark>not more than thirty</mark> members.", "প্ৰতিখন জিলাত <mark>ত্ৰিশজনৰ অনধিক</mark> সদস্যৰ [[district-council|জিলা পৰিষদ]] থাকে।"),
            B("Not more than <mark>four</mark> are nominated by the Governor. The rest are elected by adult suffrage. Elected members serve <mark>five years</mark>.", "<mark>চাৰিজনৰ</mark> অনধিক সদস্য ৰাজ্যপালে মনোনীত কৰে। বাকীসকল প্ৰাপ্তবয়স্ক ভোটাধিকাৰেৰে নিৰ্বাচিত। নিৰ্বাচিত সদস্যৰ কাৰ্যকাল <mark>পাঁচ বছৰ</mark>।")], art="houses"),
     inline(B("A District Council has not more than", "জিলা পৰিষদৰ সদস্য সংখ্যা"), B("members.", "জনৰ অনধিক।"), [B("20", "২০"), B("30", "৩০"), B("46", "৪৬"), B("60", "৬০")], 1, B("Paragraph 2(1) sets thirty.", "পেৰেগ্ৰাফ ২(১)-এ ত্ৰিশজন ঠিক কৰিছে।")),
     tf(B("All members of a District Council are nominated.", "জিলা পৰিষদৰ সকলো সদস্য মনোনীত।"), False, B("At most four are nominated; the rest are elected by adult suffrage.", "সৰ্বাধিক চাৰিজন মনোনীত; বাকীসকল প্ৰাপ্তবয়স্ক ভোটাধিকাৰেৰে নিৰ্বাচিত।")),
     match([(B("Paragraph 1", "পেৰেগ্ৰাফ ১"), B("Autonomous districts and regions", "স্বায়ত্ত শাসিত জিলা আৰু অঞ্চল")), (B("Paragraph 2", "পেৰেগ্ৰাফ ২"), B("Councils", "পৰিষদ")), (B("Paragraph 20", "পেৰেগ্ৰাফ ২০"), B("The table of tribal areas", "জনজাতীয় ক্ষেত্ৰৰ তালিকা"))], B("Three paragraphs to remember.", "মনত ৰাখিবলগীয়া তিনিটা পেৰেগ্ৰাফ।")),
     order(B("Build it from smallest rule to body.", "ক্ৰমত সজোৱা।"), [B("Area listed in the table", "তালিকাত থকা ক্ষেত্ৰ"), B("Becomes an autonomous district", "স্বায়ত্ত শাসিত জিলা হয়"), B("Gets a District Council", "জিলা পৰিষদ পায়")], B("The table creates the district; the district has the council.", "তালিকাই জিলা সৃষ্টি কৰে; জিলাত পৰিষদ থাকে।")),
     spot(ONE, "Elected council members serve for six years.", "পৰিষদৰ নিৰ্বাচিত সদস্যৰ কাৰ্যকাল ছয় বছৰ।", 5, 4, B("→ five", "→ পাঁচ"), B("six → five", "ছয় → পাঁচ"), B("Paragraph 2(6A) gives five years.", "পেৰেগ্ৰাফ ২(৬ক)-এ পাঁচ বছৰ দিছে।"))])

u3 = unit("u3", "hill", B("Assam's three", "অসমৰ তিনিটা"),
    B("Put Assam's Part I areas on the map.", "অসমৰ প্ৰথম অংশৰ ক্ষেত্ৰ মানচিত্ৰত চিনাক্ত কৰা।"),
    B("Finding recorded: Assam has three listed areas, and Bodoland has its own larger council.", "প্ৰমাণ লিখা হ'ল: অসমৰ তালিকাত তিনিটা ক্ষেত্ৰ আছে, আৰু বড়োলেণ্ডৰ নিজা ডাঙৰ পৰিষদ আছে।"),
    [B("Part I of the table lists three Assam areas", "তালিকাৰ প্ৰথম অংশত অসমৰ তিনিটা ক্ষেত্ৰ আছে"), B("They are North Cachar Hills, Karbi Anglong and Bodoland Territorial Areas", "সেইকেইটা উত্তৰ কাছাৰ পাহাৰ, কাৰ্বি আংলং আৰু বড়োলেণ্ড টেৰিটৰিয়েল এৰিয়াছ"),
     B("The text still says North Cachar Hills, now Dima Hasao", "পাঠত এতিয়াও উত্তৰ কাছাৰ পাহাৰ আছে, এতিয়া ডিমা হাছাও"), B("The Bodoland Territorial Council has up to 46 members", "বড়োলেণ্ড টেৰিটৰিয়েল কাউন্সিলত সৰ্বাধিক ৪৬ জন সদস্য")],
    [story(B("Three names in Part I", "প্ৰথম অংশৰ তিনিটা নাম"),
           [B("Part I of the table lists <b>North Cachar Hills, Karbi Anglong and the Bodoland Territorial Areas</b>.", "তালিকাৰ প্ৰথম অংশত আছে <b>উত্তৰ কাছাৰ পাহাৰ, কাৰ্বি আংলং আৰু বড়োলেণ্ড টেৰিটৰিয়েল এৰিয়াছ</b>।"),
            B("The Constitution's table still prints North Cachar Hills. The district is now Dima Hasao. Shading on this map is approximate.", "সংবিধানৰ তালিকাত এতিয়াও উত্তৰ কাছাৰ পাহাৰ ছপা আছে। জিলাখন এতিয়া ডিমা হাছাও। মানচিত্ৰৰ ৰং আনুমানিক।")], map=COUNCIL_MAP),
     dict(story(B("A larger council", "ডাঙৰ পৰিষদ"),
           [B("The [[bodoland-territorial-council|Bodoland Territorial Council]] follows a special rule from 2003: <mark>not more than 46</mark> members.", "[[bodoland-territorial-council|বড়োলেণ্ড টেৰিটৰিয়েল কাউন্সিলত]] ২০০৩ চনৰ বিশেষ নিয়ম খাটে: <mark>৪৬ জনৰ অনধিক</mark> সদস্য।"),
            B("Forty are elected: thirty seats for Scheduled Tribes, five for non-tribal communities, five open. Six are nominated, at least two of them women.", "চল্লিশজন নিৰ্বাচিত: ত্ৰিশটা অনুসূচিত জনজাতিৰ, পাঁচটা অ-জনজাতীয়ৰ, পাঁচটা মুকলি। ছয়জন মনোনীত, তাৰে অন্ততঃ দুজন মহিলা।")], art="houses"),
          link={"lesson": 63, "lessonId": "modern-assam-08", "unitNo": 2, "unitTitle": B("The hills around Haflong", "হাফলঙৰ চাৰিওফালৰ পাহাৰ"), "note": B("Assam History covers how these councils grew.", "এই পৰিষদবোৰ কেনেকৈ গঢ় লৈছে, অসমৰ ইতিহাসত আছে।")}),
     inline(B("The Bodoland Territorial Council has not more than", "বড়োলেণ্ড টেৰিটৰিয়েল কাউন্সিলৰ সদস্য"), B("members.", "জনৰ অনধিক।"), [B("30", "৩০"), B("40", "৪০"), B("46", "৪৬"), B("60", "৬০")], 2, B("Forty elected plus six nominated.", "চল্লিশজন নিৰ্বাচিত আৰু ছয়জন মনোনীত।")),
     odd(B("Which is not in Part I of the table?", "তালিকাৰ প্ৰথম অংশত কোনটো নাই?"), [B("Karbi Anglong", "কাৰ্বি আংলং"), B("Garo Hills", "গাৰো পাহাৰ"), B("North Cachar Hills", "উত্তৰ কাছাৰ পাহাৰ"), B("Bodoland Territorial Areas", "বড়োলেণ্ড টেৰিটৰিয়েল এৰিয়াছ")], 1, B("Garo Hills is in Part II, for Meghalaya.", "গাৰো পাহাৰ মেঘালয়ৰ, দ্বিতীয় অংশত।")),
     match([(B("Elected, reserved for Scheduled Tribes", "নিৰ্বাচিত, অনুসূচিত জনজাতিৰ বাবে সংৰক্ষিত"), B("30", "৩০")), (B("Elected, non-tribal communities", "নিৰ্বাচিত, অ-জনজাতীয়"), B("5", "৫")), (B("Nominated by the Governor", "ৰাজ্যপালৰ দ্বাৰা মনোনীত"), B("6", "৬"))], B("30 + 5 + 5 open + 6 nominated = 46.", "৩০ + ৫ + ৫ মুকলি + ৬ মনোনীত = ৪৬।")),
     tf(B("A question naming North Cachar Hills cannot be about Dima Hasao.", "উত্তৰ কাছাৰ পাহাৰৰ নাম থকা প্ৰশ্ন ডিমা হাছাওৰ বিষয়ে হ'ব নোৱাৰে।"), False, B("Dima Hasao was formerly called North Cachar Hills, and the Constitution's table keeps the old name.", "ডিমা হাছাওৰ পূৰ্বৰ নাম উত্তৰ কাছাৰ পাহাৰ, আৰু সংবিধানৰ তালিকাত পুৰণি নামেই আছে।")),
     spot(ONE, "Bodoland's council has forty seats reserved for Scheduled Tribes.", "বড়োলেণ্ডৰ পৰিষদত অনুসূচিত জনজাতিৰ বাবে চল্লিশটা আসন সংৰক্ষিত।", 3, 5, B("→ thirty", "→ ত্ৰিশ"), B("forty → thirty", "চল্লিশ → ত্ৰিশ"), B("Forty is the elected total; thirty are reserved for Scheduled Tribes.", "চল্লিশ মুঠ নিৰ্বাচিত; ত্ৰিশটা অনুসূচিত জনজাতিৰ বাবে সংৰক্ষিত।"))])

u4 = unit("u4", "star", B("What a council can do", "পৰিষদে কি কৰিব পাৰে"),
    B("List what a council may decide.", "পৰিষদে কি ঠিক কৰিব পাৰে, তালিকা কৰা।"),
    B("Finding recorded: councils make laws on local life, but those laws need the Governor's assent.", "প্ৰমাণ লিখা হ'ল: পৰিষদে স্থানীয় জীৱনৰ বিধি প্ৰণয়ন কৰে, কিন্তু ৰাজ্যপালৰ সন্মতি লাগে।"),
    [B("Paragraph 3 lists subjects such as land, jhum and social customs", "পেৰেগ্ৰাফ ৩-ত মাটি, ঝুম আৰু সামাজিক ৰীতি আদি বিষয় আছে"), B("Council laws need the Governor's assent", "পৰিষদৰ বিধিৰ বাবে ৰাজ্যপালৰ সন্মতি লাগে"),
     B("Councils may set up primary schools and choose the language", "পৰিষদে প্ৰাথমিক বিদ্যালয় স্থাপন আৰু ভাষা ঠিক কৰিব পাৰে"), B("Paragraphs 3A and 3B add subjects for Assam's councils", "পেৰেগ্ৰাফ ৩ক আৰু ৩খ-ই অসমৰ পৰিষদৰ বিষয় বঢ়ায়")],
    [story(B("Laws on local life", "স্থানীয় জীৱনৰ বিধি"),
           [B("Paragraph 3 lets councils make laws on land, forests that are not reserved, jhum, village administration, inheritance, marriage and social customs.", "পেৰেগ্ৰাফ ৩-এ পৰিষদক মাটি, সংৰক্ষিত নোহোৱা বনাঞ্চল, ঝুম, গাঁৱৰ প্ৰশাসন, উত্তৰাধিকাৰ, বিবাহ আৰু সামাজিক ৰীতিৰ বিধি প্ৰণয়নৰ ক্ষমতা দিয়ে।"),
            B("These laws have no effect until the <mark>Governor assents</mark>.", "<mark>ৰাজ্যপালৰ সন্মতি</mark> নোপোৱালৈকে এই বিধি কাৰ্যকৰী নহয়।")], art="scroll"),
     story(B("Schools, language and land revenue", "বিদ্যালয়, ভাষা আৰু ভূমি ৰাজহ"),
           [B("Under paragraph 6, a District Council may set up primary schools and prescribe the <mark>language</mark> of primary education, with the Governor's prior approval for regulations.", "পেৰেগ্ৰাফ ৬ অনুসৰি জিলা পৰিষদে প্ৰাথমিক বিদ্যালয় স্থাপন কৰিব আৰু প্ৰাথমিক শিক্ষাৰ <mark>ভাষা</mark> ঠিক কৰিব পাৰে। ইয়াৰ নিয়মৰ বাবে ৰাজ্যপালৰ অনুমোদন লাগে।"),
            B("Paragraph 8 lets it assess and collect <mark>land revenue</mark>. For Assam, paragraphs 3A and 3B add more subjects.", "পেৰেগ্ৰাফ ৮-এ ইয়াক <mark>ভূমি ৰাজহ</mark> নিৰ্ধাৰণ আৰু সংগ্ৰহৰ ক্ষমতা দিয়ে। অসমৰ বাবে পেৰেগ্ৰাফ ৩ক আৰু ৩খ-ই আৰু বিষয় যোগ কৰে।")], art="calendar"),
     tf(B("A council's law takes effect the day it is passed.", "পৰিষদৰ বিধি গৃহীত হোৱা দিনৰে পৰা কাৰ্যকৰী হয়।"), False, B("Under paragraph 3(3), it has no effect until the Governor assents.", "পেৰেগ্ৰাফ ৩(৩) অনুসৰি ৰাজ্যপালৰ সন্মতি নোপোৱালৈকে ই কাৰ্যকৰী নহয়।")),
     odd(B("Which is not a paragraph 3 subject?", "পেৰেগ্ৰাফ ৩-ৰ বিষয় কোনটো নহয়?"), [B("Jhum cultivation", "ঝুম খেতি"), B("Inheritance of property", "সম্পত্তিৰ উত্তৰাধিকাৰ"), B("Defence of India", "ভাৰতৰ প্ৰতিৰক্ষা"), B("Social customs", "সামাজিক ৰীতি")], 2, B("Defence is not on the paragraph 3 list.", "প্ৰতিৰক্ষা পেৰেগ্ৰাফ ৩-ৰ তালিকাত নাই।")),
     match([(B("Paragraph 3", "পেৰেগ্ৰাফ ৩"), B("Law-making powers", "বিধি প্ৰণয়নৰ ক্ষমতা")), (B("Paragraph 6", "পেৰেগ্ৰাফ ৬"), B("Primary schools", "প্ৰাথমিক বিদ্যালয়")), (B("Paragraph 8", "পেৰেগ্ৰাফ ৮"), B("Land revenue and taxes", "ভূমি ৰাজহ আৰু কৰ"))], B("Each power has its paragraph.", "প্ৰতিটো ক্ষমতাৰ নিজা পেৰেগ্ৰাফ আছে।")),
     inline(B("Council laws need the assent of the", "পৰিষদৰ বিধিৰ বাবে সন্মতি লাগে"), B(".", "-ৰ।"), [B("President", "ৰাষ্ট্ৰপতি"), B("Governor", "ৰাজ্যপাল"), B("Speaker", "অধ্যক্ষ"), B("Chief Minister", "মুখ্যমন্ত্ৰী")], 1, B("Paragraph 3(3) names the Governor.", "পেৰেগ্ৰাফ ৩(৩)-এ ৰাজ্যপালৰ নাম লৈছে।")),
     scramble(B("Unscramble the farming word in paragraph 3.", "পেৰেগ্ৰাফ ৩-ৰ খেতিৰ শব্দটো সজাই লিখা।"), "JHUM", ["ঝু", "ম"], B("JHUM", "ঝুম"), B("Paragraph 3 lets councils regulate jhum.", "পেৰেগ্ৰাফ ৩-এ পৰিষদক ঝুম নিয়ন্ত্ৰণৰ ক্ষমতা দিয়ে।")),
     order(B("Put a council law's path in order.", "পৰিষদৰ বিধিৰ বাট ক্ৰমত সজোৱা।"), [B("Council passes the law", "পৰিষদে বিধি গ্ৰহণ কৰে"), B("Sent to the Governor", "ৰাজ্যপাললৈ প্ৰেৰিত"), B("Governor assents", "ৰাজ্যপালে সন্মতি দিয়ে"), B("Law takes effect", "বিধি কাৰ্যকৰী হয়")], B("No assent, no effect.", "সন্মতি নহ'লে কাৰ্যকৰী নহয়।"))])

u5 = unit("u5", "crown", B("Who holds the brakes", "ব্ৰেক কাৰ হাতত"),
    B("Find the limits on council power.", "পৰিষদৰ ক্ষমতাৰ সীমা বিচাৰি উলিওৱা।"),
    B("Finding recorded: the council can keep out some Assam laws, and the Governor can dissolve a council on a Commission's advice.", "প্ৰমাণ লিখা হ'ল: পৰিষদে অসমৰ কিছুমান আইন ৰোধ কৰিব পাৰে, আৰু আয়োগৰ পৰামৰ্শত ৰাজ্যপালে পৰিষদ ভংগ কৰিব পাৰে।"),
    [B("Assam Acts on paragraph 3 matters apply only if the council directs", "পেৰেগ্ৰাফ ৩-ৰ বিষয়ৰ অসমৰ আইন পৰিষদে নিৰ্দেশ দিলেহে প্ৰযোজ্য"), B("Councils may set up village councils or courts for Scheduled Tribe cases", "পৰিষদে অনুসূচিত জনজাতিৰ গোচৰৰ বাবে গাঁও পৰিষদ বা ন্যায়ালয় গঠন কৰিব পাৰে"),
     B("The Governor may appoint a Commission under paragraph 14", "পেৰেগ্ৰাফ ১৪-ৰ অধীনত ৰাজ্যপালে আয়োগ নিযুক্ত কৰিব পাৰে"), B("Dissolution under paragraph 16 needs a Commission's recommendation", "পেৰেগ্ৰাফ ১৬-ৰ ভংগৰ বাবে আয়োগৰ পৰামৰ্শ লাগে")],
    [story(B("A shield against State laws", "ৰাজ্যিক আইনৰ পৰা ঢাল"),
           [B("Under paragraph 12, an Assam Act on a paragraph 3 matter applies to a council area <mark>only if the council directs</mark>.", "পেৰেগ্ৰাফ ১২ অনুসৰি পেৰেগ্ৰাফ ৩-ৰ বিষয়ৰ অসমৰ আইন <mark>পৰিষদে নিৰ্দেশ দিলেহে</mark> পৰিষদ ক্ষেত্ৰত প্ৰযোজ্য হয়।"),
            B("Under paragraph 4, councils may set up village councils or courts for cases where all parties belong to Scheduled Tribes.", "পেৰেগ্ৰাফ ৪ অনুসৰি সকলো পক্ষ অনুসূচিত জনজাতিৰ হোৱা গোচৰৰ বাবে পৰিষদে গাঁও পৰিষদ বা ন্যায়ালয় গঠন কৰিব পাৰে।")], art="court"),
     story(B("The Governor's hand", "ৰাজ্যপালৰ হাত"),
           [B("Under paragraph 14, the Governor may appoint a Commission to report on administration.", "পেৰেগ্ৰাফ ১৪ অনুসৰি ৰাজ্যপালে প্ৰশাসনৰ প্ৰতিবেদন দিবলৈ আয়োগ নিযুক্ত কৰিব পাৰে।"),
            B("Under paragraph 16, the Governor may dissolve a council <mark>on that Commission's recommendation</mark>, then order fresh elections or, with the Legislature's prior approval, take over for up to twelve months.", "পেৰেগ্ৰাফ ১৬ অনুসৰি <mark>সেই আয়োগৰ পৰামৰ্শত</mark> ৰাজ্যপালে পৰিষদ ভংগ কৰিব পাৰে। তাৰ পিছত নতুন নিৰ্বাচন, বা বিধানমণ্ডলৰ অনুমোদনেৰে বাৰ মাহলৈকে প্ৰশাসন।")], art="seal"),
     tf(B("Every Assam Act applies automatically in council areas.", "অসমৰ প্ৰতিখন আইন পৰিষদ ক্ষেত্ৰত আপোনা-আপুনি প্ৰযোজ্য হয়।"), False, B("Paragraph 12 protects paragraph 3 matters unless the council directs otherwise.", "পৰিষদে নিৰ্দেশ নিদিলে পেৰেগ্ৰাফ ১২-এ পেৰেগ্ৰাফ ৩-ৰ বিষয় সুৰক্ষিত ৰাখে।")),
     order(B("Put the dissolution steps in order.", "ভংগৰ পদক্ষেপ ক্ৰমত সজোৱা।"), [B("Governor appoints a Commission", "ৰাজ্যপালে আয়োগ নিযুক্ত কৰে"), B("Commission recommends dissolution", "আয়োগে ভংগৰ পৰামৰ্শ দিয়ে"), B("Governor issues a public notification", "ৰাজ্যপালে ৰাজহুৱা অধিসূচনা দিয়ে"), B("Fresh election, or temporary administration", "নতুন নিৰ্বাচন বা অস্থায়ী প্ৰশাসন")], B("Paragraph 16 starts from a Commission's recommendation.", "পেৰেগ্ৰাফ ১৬ আয়োগৰ পৰামৰ্শৰ পৰা আৰম্ভ হয়।")),
     inline(B("Dissolving a council needs the recommendation of a", "পৰিষদ ভংগৰ বাবে পৰামৰ্শ লাগে"), B(".", "-ৰ।"), [B("Commission", "আয়োগ"), B("High Court", "উচ্চ ন্যায়ালয়"), B("Gram Sabha", "গাঁও সভা")], 0, B("Paragraph 16(1) refers to a Commission under paragraph 14.", "পেৰেগ্ৰাফ ১৬(১)-এ পেৰেগ্ৰাফ ১৪-ৰ আয়োগৰ কথা কৈছে।")),
     match([(B("Paragraph 4", "পেৰেগ্ৰাফ ৪"), B("Village councils or courts", "গাঁও পৰিষদ বা ন্যায়ালয়")), (B("Paragraph 12", "পেৰেগ্ৰাফ ১২"), B("Application of Assam Acts", "অসমৰ আইনৰ প্ৰয়োগ")), (B("Paragraph 16", "পেৰেগ্ৰাফ ১৬"), B("Dissolution", "ভংগ"))], B("Courts, laws and dissolution have separate paragraphs.", "ন্যায়ালয়, আইন আৰু ভংগৰ পৃথক পেৰেগ্ৰাফ আছে।")),
     spot(ONE, "A temporary takeover may last twenty-four months.", "অস্থায়ী প্ৰশাসন চৌবিশ মাহলৈকে চলিব পাৰে।", 5, 2, B("→ twelve", "→ বাৰ"), B("twenty-four → twelve", "চৌবিশ → বাৰ"), B("Paragraph 16(1)(b) says not exceeding twelve months.", "পেৰেগ্ৰাফ ১৬(১)(খ)-ত বাৰ মাহৰ অনধিক বুলি আছে।"))])

u6 = unit("u6", "flag", B("Assam's special clauses", "অসমৰ বিশেষ অনুচ্ছেদ"),
    B("Separate the Sixth Schedule from its lookalikes.", "ষষ্ঠ অনুসূচীক ইয়াৰ সদৃশ ব্যৱস্থাৰ পৰা পৃথক কৰা।"),
    B("Finding recorded: Sixth Schedule, Fifth Schedule, Articles 244A and 371B, and Assam's statutory councils are different things.", "প্ৰমাণ লিখা হ'ল: ষষ্ঠ অনুসূচী, পঞ্চম অনুসূচী, অনুচ্ছেদ ২৪৪ক আৰু ৩৭১খ, আৰু অসমৰ আইনী পৰিষদ বেলেগ বেলেগ।"),
    [B("The Fifth Schedule does not apply to the four Sixth Schedule States", "চাৰিখন ষষ্ঠ অনুসূচীৰ ৰাজ্যত পঞ্চম অনুসূচী প্ৰযোজ্য নহয়"), B("Article 244A lets Parliament form an autonomous State within Assam", "অনুচ্ছেদ ২৪৪ক-এ সংসদক অসমৰ ভিতৰত স্বায়ত্তশাসিত ৰাজ্য গঠনৰ ক্ষমতা দিয়ে"),
     B("Article 371B allows a committee of the Assam Assembly", "অনুচ্ছেদ ৩৭১খ-এ অসম বিধানসভাৰ সমিতিৰ ব্যৱস্থা কৰে"), B("Mising, Rabha Hasong and Tiwa councils rest on Assam Acts", "মিচিং, ৰাভা হাছং আৰু তিৱা পৰিষদ অসমৰ আইনৰ অধীন")],
    [story(B("Same year, two clauses", "একে বছৰ, দুটা অনুচ্ছেদ"),
           [B("The 22nd Amendment of 1969 added two Assam provisions. [[art-244a]] lets Parliament form an <mark>autonomous State</mark> within Assam.", "১৯৬৯ চনৰ ২২তম সংশোধনীয়ে অসমৰ দুটা ব্যৱস্থা যোগ কৰিলে। [[art-244a]]-এ সংসদক অসমৰ ভিতৰত <mark>স্বায়ত্তশাসিত ৰাজ্য</mark> গঠনৰ ক্ষমতা দিয়ে।"),
            B("[[art-371b]] lets the President provide for a <mark>committee</mark> of the Assam Assembly, including members from the Part I tribal areas.", "[[art-371b]]-এ ৰাষ্ট্ৰপতিক অসম বিধানসভাৰ <mark>সমিতিৰ</mark> ব্যৱস্থা কৰাৰ ক্ষমতা দিয়ে। ইয়াত প্ৰথম অংশৰ জনজাতীয় ক্ষেত্ৰৰ সদস্য থাকে।")], art="scroll"),
     dict(story(B("Fifth, Sixth, or an Act?", "পঞ্চম, ষষ্ঠ নে আইন?"),
           [B("The Fifth Schedule covers Scheduled Areas in States <mark>other than</mark> the four Sixth Schedule States.", "পঞ্চম অনুসূচী চাৰিখন ষষ্ঠ অনুসূচীৰ ৰাজ্যৰ <mark>বাহিৰৰ</mark> অনুসূচিত ক্ষেত্ৰৰ বাবে।"),
            B("Assam's Mising, Rabha Hasong and Tiwa councils rest on <mark>Assam Acts</mark> of 1995, not on the Sixth Schedule.", "অসমৰ মিচিং, ৰাভা হাছং আৰু তিৱা পৰিষদ ষষ্ঠ অনুসূচীৰ অধীন নহয়, ১৯৯৫ চনৰ <mark>অসমৰ আইনৰ</mark> অধীন।")], art="houses"),
          link={"lesson": 91, "lessonId": "peoples-councils-movements-06", "unitNo": 1, "unitTitle": B("Read the instrument first", "প্ৰথমে মূল বিধান পঢ়া"), "note": B("Assam History separates these legal foundations.", "অসমৰ ইতিহাসত এই আইনী ভেটিবোৰ পৃথক কৰা হৈছে।")}),
     match([(B("Sixth Schedule", "ষষ্ঠ অনুসূচী"), B("Karbi Anglong council", "কাৰ্বি আংলং পৰিষদ")), (B("Assam Act of 1995", "১৯৯৫ চনৰ অসমৰ আইন"), B("Mising council", "মিচিং পৰিষদ")), (B("Article 371B", "অনুচ্ছেদ ৩৭১খ"), B("Assembly committee", "বিধানসভাৰ সমিতি")), (B("Article 244A", "অনুচ্ছেদ ২৪৪ক"), B("Autonomous State within Assam", "অসমৰ ভিতৰত স্বায়ত্তশাসিত ৰাজ্য"))], B("Four instruments, four results.", "চাৰিটা ব্যৱস্থা, চাৰিটা ফল।")),
     tf(B("The Mising Autonomous Council is a Sixth Schedule council.", "মিচিং স্বায়ত্তশাসিত পৰিষদ ষষ্ঠ অনুসূচীৰ পৰিষদ।"), False, B("It rests on an Assam Act of 1995.", "ই ১৯৯৫ চনৰ অসমৰ আইনৰ অধীন।")),
     inline(B("Articles 244A and 371B were added by the", "অনুচ্ছেদ ২৪৪ক আৰু ৩৭১খ যোগ কৰিছিল"), B("Amendment.", "সংশোধনীয়ে।"), [B("7th", "৭ম"), B("22nd", "২২তম"), B("42nd", "৪২তম"), B("73rd", "৭৩তম")], 1, B("Both came from the 22nd Amendment, 1969.", "দুয়োটা ১৯৬৯ চনৰ ২২তম সংশোধনীৰ পৰা।")),
     line(B("Place each provision on the line.", "প্ৰতিটো উপবন্ধ ৰেখাত ৰাখা।"), [(244, B("Scheduled and tribal areas", "অনুসূচিত আৰু জনজাতীয় ক্ষেত্ৰ")), (371, B("Special provisions begin", "বিশেষ ব্যৱস্থাৰ আৰম্ভণি"))], [(B("Article 244A", "অনুচ্ছেদ ২৪৪ক"), 1), (B("Article 371B", "অনুচ্ছেদ ৩৭১খ"), 2), (B("Article 32", "অনুচ্ছেদ ৩২"), 0)], B("32 → 244 → 244A → 371 → 371B.", "৩২ → ২৪৪ → ২৪৪ক → ৩৭১ → ৩৭১খ।")),
     tf(B("The Fifth Schedule applies to Assam's tribal areas.", "অসমৰ জনজাতীয় ক্ষেত্ৰত পঞ্চম অনুসূচী প্ৰযোজ্য।"), False, B("Article 244(1) excludes Assam, Meghalaya, Tripura and Mizoram.", "অনুচ্ছেদ ২৪৪(১)-এ অসম, মেঘালয়, ত্ৰিপুৰা আৰু মিজোৰাম বাদ দিছে।"))])

test = {"id": "test", "title": B("Lesson test", "পাঠৰ পৰীক্ষা"),
        "mission": {"objective": B("Complete the council map.", "পৰিষদৰ মানচিত্ৰ সম্পূৰ্ণ কৰা।"), "result": B("Map complete: you can tell who governs what, and under which clause.", "মানচিত্ৰ সম্পূৰ্ণ: কোনে কি চলায় আৰু কোন ব্যৱস্থাৰে, তুমি ক'ব পাৰা।")}, "learned": [],
        "steps": [
            match([(B("Article 244(2)", "অনুচ্ছেদ ২৪৪(২)"), B("Applies the Sixth Schedule", "ষষ্ঠ অনুসূচী প্ৰযোজ্য কৰে")), (B("Article 371B", "অনুচ্ছেদ ৩৭১খ"), B("Assam Assembly committee", "অসম বিধানসভাৰ সমিতি")), (B("Paragraph 3", "পেৰেগ্ৰাফ ৩"), B("Council law-making", "পৰিষদৰ বিধি প্ৰণয়ন"))], B("Keep each clause with its job.", "প্ৰতিটো ব্যৱস্থা ইয়াৰ কামৰ সৈতে মনত ৰাখা।")),
            tf(B("The Bodoland Territorial Council can have 46 members.", "বড়োলেণ্ড টেৰিটৰিয়েল কাউন্সিলত ৪৬ জন সদস্য থাকিব পাৰে।"), True, B("Forty elected and six nominated.", "চল্লিশজন নিৰ্বাচিত আৰু ছয়জন মনোনীত।")),
            inline(B("A District Council normally has not more than", "জিলা পৰিষদত সাধাৰণতে সদস্য থাকে"), B("nominated members.", "জনৰ অনধিক মনোনীত।"), [B("two", "দুই"), B("four", "চাৰি"), B("six", "ছয়"), B("ten", "দহ")], 1, B("Paragraph 2(1) allows four. Six is the Bodoland rule.", "পেৰেগ্ৰাফ ২(১)-এ চাৰিজন দিয়ে। ছয়জন বড়োলেণ্ডৰ নিয়ম।")),
            mcq(B("Which councils in Assam are under the Sixth Schedule? (i) Bodoland Territorial Council (ii) Karbi Anglong Autonomous Council (iii) North Cachar Hills Autonomous Council (iv) Mising Autonomous Council", "অসমৰ কোনবোৰ পৰিষদ ষষ্ঠ অনুসূচীৰ অধীন? (i) বড়োলেণ্ড টেৰিটৰিয়েল কাউন্সিল (ii) কাৰ্বি আংলং স্বায়ত্তশাসিত পৰিষদ (iii) উত্তৰ কাছাৰ পাহাৰ স্বায়ত্তশাসিত পৰিষদ (iv) মিচিং স্বায়ত্তশাসিত পৰিষদ"),
                [B("(i) only", "কেৱল (i)"), B("(i) and (ii) only", "কেৱল (i) আৰু (ii)"), B("(i), (ii) and (iii) only", "কেৱল (i), (ii) আৰু (iii)"), B("(i), (ii), (iii) and (iv)", "(i), (ii), (iii) আৰু (iv)")], 2, B("Part I lists three. The Mising council rests on an Assam Act.", "প্ৰথম অংশত তিনিটা আছে। মিচিং পৰিষদ অসমৰ আইনৰ অধীন।")),
            tf(B("A council's law needs the President's assent to take effect.", "পৰিষদৰ বিধি কাৰ্যকৰী হ'বলৈ ৰাষ্ট্ৰপতিৰ সন্মতি লাগে।"), False, B("Paragraph 3(3) names the Governor.", "পেৰেগ্ৰাফ ৩(৩)-এ ৰাজ্যপালৰ নাম লৈছে।")),
            order(B("Put the Schedule's story in order.", "অনুসূচীৰ কাহিনী ক্ৰমত সজোৱা।"), [B("Assembly debate, 1949", "গণপৰিষদৰ বিতৰ্ক, ১৯৪৯"), B("22nd Amendment, 1969", "২২তম সংশোধনী, ১৯৬৯"), B("Karbi Anglong and North Cachar powers widened, 1995", "কাৰ্বি আংলং আৰু উত্তৰ কাছাৰৰ ক্ষমতা বৃদ্ধি, ১৯৯৫"), B("Bodoland added, 2003", "বড়োলেণ্ড যোগ, ২০০৩")], B("1949 → 1969 → 1995 → 2003.", "১৯৪৯ → ১৯৬৯ → ১৯৯৫ → ২০০৩।")),
        ]}

timeline = [{"y": "1949", "t": B("Assembly debates the Sixth Schedule", "গণপৰিষদত ষষ্ঠ অনুসূচীৰ বিতৰ্ক"), "unit": "u1"}, {"y": "1969", "t": B("22nd Amendment: Articles 244A and 371B", "২২তম সংশোধনী: অনুচ্ছেদ ২৪৪ক আৰু ৩৭১খ"), "unit": "u6"},
            {"y": "2003", "t": B("Bodoland added to Part I", "প্ৰথম অংশত বড়োলেণ্ড যোগ"), "unit": "u3"}]

write(46, "con-46-sixth-schedule", B("The Sixth Schedule", "ষষ্ঠ অনুসূচী"), B("Sixth Schedule", "ষষ্ঠ অনুসূচী"), B("The Constitution of India · Tribal areas", "ভাৰতৰ সংবিধান · জনজাতি ক্ষেত্ৰ"), mission, sources, [u1, u2, u3, u4, u5, u6], test, timeline=timeline)
