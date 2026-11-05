#!/usr/bin/env python3
"""Lesson 26: Gandhi and Non-Cooperation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import *  # noqa: F403
PLACES({
 "champaran": ("place", "Champaran|চম্পাৰণ", "District in Bihar, site of Gandhi's satyagraha of 1917|বিহাৰৰ জিলা, ১৯১৭ৰ গান্ধীৰ সত্যাগ্ৰহৰ ঠাই", [26.65, 84.92]),
 "chauri-chaura": ("place", "Chauri Chaura|চৌৰী চৌৰা", "Town in Gorakhpur district, site of the violence of 1922|গোৰখপুৰ জিলাৰ নগৰ, ১৯২২ৰ হিংসাৰ ঠাই", [26.65, 83.58]),
 "porbandar": ("place", "Porbandar|পোৰবন্দৰ", "Gujarat town where Gandhi was born|গান্ধীৰ জন্মস্থান, গুজৰাটৰ নগৰ", [21.64, 69.61]),
 "rajkumar-shukla": ("person", "Raj Kumar Shukla|ৰাজকুমাৰ শুক্লা", "Peasant who invited Gandhi to Champaran|গান্ধীক চম্পাৰণলৈ নিমন্ত্ৰণ কৰা খেতিয়ক"),
 "motilal-nehru": ("person", "Motilal Nehru|মতিলাল নেহৰু", "Founder of the Swaraj Party with C. R. Das|চিত্তৰঞ্জন দাসৰ সৈতে স্বৰাজ দলৰ প্ৰতিষ্ঠাপক"),
 "cr-das": ("person", "C. R. Das|চিত্তৰঞ্জন দাস", "Founder of the Swaraj Party with Motilal Nehru|মতিলাল নেহৰুৰ সৈতে স্বৰাজ দলৰ প্ৰতিষ্ঠাপক"),
})
sources = [
 src("Wikipedia, Mahatma Gandhi", "https://en.wikipedia.org/wiki/Mahatma_Gandhi", "Used as a guide: full name, 1869, Porbandar, South Africa 1893 to 1914, 1915, Gokhale. Check in review."),
 src("Wikipedia, Champaran Satyagraha", "https://en.wikipedia.org/wiki/Champaran_Satyagraha", "Used as a guide: 1917, Teenkathia, Shukla, outcome. Check in review."),
 src("Wikipedia, Non-cooperation movement (1919–1922)", "https://en.wikipedia.org/wiki/Non-cooperation_movement_(1919%E2%80%931922)", "Used as a guide: 1920, Khilafat, boycotts, Chauri Chaura, withdrawal, arrest. Its dates for the withdrawal conflict; the lesson uses 12 February. Check in review."),
 src("Wikipedia, Swaraj Party", "https://en.wikipedia.org/wiki/Swaraj_Party", "Used as a guide: 1 January 1923, founders, council entry. Check in review."),
]
u1 = U(1, "walk", "From South Africa|দক্ষিণ আফ্ৰিকাৰ পৰা",
 "Fix the basic facts of Gandhi's early life.|গান্ধীৰ প্ৰথম জীৱনৰ তথ্য মনত ৰাখা।", "Finding recorded: Mohandas Karamchand Gandhi, South Africa to 1914, India from 1915.|প্ৰমাণ লিখা হ'ল: মোহনদাস কৰমচান্দ গান্ধী, ১৯১৪লৈ দক্ষিণ আফ্ৰিকা, ১৯১৫ৰ পৰা ভাৰত।",
 ["His full name was Mohandas Karamchand Gandhi|তেওঁৰ সম্পূৰ্ণ নাম মোহনদাস কৰমচান্দ গান্ধী", "He was born at Porbandar in 1869|১৮৬৯ত পোৰবন্দৰত জন্ম", "He stayed in South Africa from 1893 to 1914|১৮৯৩ৰ পৰা ১৯১৪লৈ দক্ষিণ আফ্ৰিকাত", "He returned to India in 1915|১৯১৫ত ভাৰতলৈ উভতিছিল"],
 S("Twenty-one years away|একৈশ বছৰ বাহিৰত", "<mark>Mohandas Karamchand Gandhi</mark> was born at [[porbandar]] in 1869. He went to <mark>South Africa</mark> in 1893 and stayed about 21 years.|<mark>মোহনদাস কৰমচান্দ গান্ধীৰ</mark> ১৮৬৯ত [[porbandar|পোৰবন্দৰত]] জন্ম। ১৮৯৩ত তেওঁ <mark>দক্ষিণ আফ্ৰিকালৈ</mark> গৈ প্ৰায় ২১ বছৰ আছিল।", art="embassy"),
 S("Home in 1915|১৯১৫ত ঘৰলৈ", "He returned in <mark>1915</mark>, at Gokhale's request. His book Hind Swaraj, of 1909, had already argued that British rule rested on Indian cooperation.|<mark>১৯১৫ত</mark> গোখলেৰ অনুৰোধত তেওঁ উভতিছিল। ১৯০৯ৰ তেওঁৰ গ্ৰন্থ হিন্দ স্বৰাজত ব্ৰিটিছ শাসন ভাৰতীয়ৰ সহযোগিতাত ৰৈ আছে বুলি কোৱা হৈছিল।", art="scroll"),
 IN("The real name of Mahatma Gandhi was|মহাত্মা গান্ধীৰ প্ৰকৃত নাম", ".|।", ["Mohandas Kumar Gandhi|মোহনদাস কুমাৰ গান্ধী", "Mohansingh Karamchand Gandhi|মোহনসিং কৰমচান্দ গান্ধী", "Mohandas Karamsingh Gandhi|মোহনদাস কৰমসিং গান্ধী", "Mohandas Karamchand Gandhi|মোহনদাস কৰমচান্দ গান্ধী"], 3, "Mohandas Karamchand Gandhi.|মোহনদাস কৰমচান্দ গান্ধী।"),
 IN("Before coming to India, Gandhi stayed in|ভাৰতলৈ অহাৰ আগতে গান্ধী আছিল", ".|ত।", ["South Africa|দক্ষিণ আফ্ৰিকা", "Uganda|উগাণ্ডা", "Egypt|ইজিপ্ত", "Sri Lanka|শ্ৰীলংকা"], 0, "South Africa.|দক্ষিণ আফ্ৰিকা।"),
 MP("Tap Porbandar.|পোৰবন্দৰ টিপা।", "porbandar", ["porbandar", "champaran", "chauri-chaura", "delhi"], "On the Gujarat coast.|গুজৰাটৰ উপকূলত।"),
 TF("Gandhi returned to India in 1915.|১৯১৫ত গান্ধী ভাৰতলৈ উভতিছিল।", True, "At Gokhale's request.|গোখলেৰ অনুৰোধত।"),
 OR("Put his early life in order.|তেওঁৰ প্ৰথম জীৱন ক্ৰমে সজোৱা।", ["Born at Porbandar|পোৰবন্দৰত জন্ম", "Goes to South Africa|দক্ষিণ আফ্ৰিকালৈ", "Hind Swaraj|হিন্দ স্বৰাজ", "Returns to India|ভাৰতলৈ প্ৰত্যাৱৰ্তন"], "1869, 1893, 1909, 1915.|১৮৬৯, ১৮৯৩, ১৯০৯, ১৯১৫।"),
)
u2 = U(2, "hands", "Champaran, 1917|চম্পাৰণ, ১৯১৭",
 "See Gandhi's first campaign in India.|ভাৰতত গান্ধীৰ প্ৰথম অভিযান চোৱা।", "Finding recorded: Gandhi refused to leave Champaran, and the system ended.|প্ৰমাণ লিখা হ'ল: গান্ধীয়ে চম্পাৰণ ত্যাগ নকৰিলে, ব্যৱস্থাটো শেষ হ'ল।",
 ["Champaran came in 1917, in Bihar|১৯১৭ত বিহাৰৰ চম্পাৰণ", "Tenants were forced to grow indigo|ৰায়তক নীল খেতি কৰিবলৈ বাধ্য কৰা হৈছিল", "Raj Kumar Shukla invited Gandhi|ৰাজকুমাৰ শুক্লাই গান্ধীক নিমন্ত্ৰণ কৰিছিল", "It was his first satyagraha on Indian soil|ই ভাৰতত তেওঁৰ প্ৰথম সত্যাগ্ৰহ"],
 S("Indigo again|আকৌ নীল", "In [[champaran]], Bihar, tenants had to grow indigo on part of their land under the Teenkathia system.|বিহাৰৰ [[champaran|চম্পাৰণত]] তিনকঠিয়া ব্যৱস্থাত ৰায়তে মাটিৰ এটা অংশত নীল খেতি কৰিব লাগিছিল।", "A peasant, [[rajkumar-shukla|Raj Kumar Shukla]], invited Gandhi in <mark>1917</mark>.|<mark>১৯১৭ত</mark> খেতিয়ক [[rajkumar-shukla|ৰাজকুমাৰ শুক্লাই]] গান্ধীক নিমন্ত্ৰণ কৰিছিল।", art="houses"),
 S("I will not leave|মই নাযাওঁ", "Ordered to leave, Gandhi refused and accepted the consequences. It was his first <mark>satyagraha</mark> on Indian soil, and the system was dismantled.|যাবলৈ আদেশ দিলে গান্ধীয়ে অস্বীকাৰ কৰি পৰিণতি মানি লৈছিল। ই ভাৰতত তেওঁৰ প্ৰথম <mark>সত্যাগ্ৰহ</mark>, ব্যৱস্থাটো শেষ হ'ল।", art="door"),
 TF("Champaran was in Gujarat.|চম্পাৰণ গুজৰাটত আছিল।", False, "It is in Bihar.|ই বিহাৰত।"),
 MP("Tap Champaran.|চম্পাৰণ টিপা।", "champaran", ["champaran", "porbandar", "delhi", "bombay"], "In Bihar.|বিহাৰত।"),
 IN("Gandhi's first satyagraha on Indian soil was at|ভাৰতত গান্ধীৰ প্ৰথম সত্যাগ্ৰহ", ".|ত।", ["Dandi|ডাণ্ডী", "Bardoli|বাৰদোলী", "Champaran|চম্পাৰণ", "Amritsar|অমৃতসৰ"], 2, "Champaran, 1917.|১৯১৭ত চম্পাৰণ।"),
 WH(["I was a peasant.|মই খেতিয়ক।", "I invited Gandhi to Bihar.|মই গান্ধীক বিহাৰলৈ নিমন্ত্ৰণ কৰিছিলোঁ।"], ["Raj Kumar Shukla|ৰাজকুমাৰ শুক্লা", "Rajendra Prasad|ৰাজেন্দ্ৰ প্ৰসাদ", "Sidhu Murmu|সিধু মুৰ্মু", "Dinabandhu Mitra|দীনবন্ধু মিত্ৰ"], 0, "Raj Kumar Shukla.|ৰাজকুমাৰ শুক্লা।"),
 SC("Unscramble the name of Gandhi's method.|গান্ধীৰ পদ্ধতিৰ নামটো সজোৱা।", "SATYAGRAHA", ["স", "ত্যা", "গ্ৰ", "হ"], "Satyagraha.|সত্যাগ্ৰহ।"),
)
u3 = U(3, "flag", "Non-Cooperation|অসহযোগ",
 "Follow the first mass movement to its sudden end.|প্ৰথম গণ আন্দোলন আকস্মিক অন্তলৈ অনুসৰণ কৰা।", "Finding recorded: launched in 1920, called off after Chauri Chaura in 1922.|প্ৰমাণ লিখা হ'ল: ১৯২০ত আৰম্ভ, ১৯২২ত চৌৰী চৌৰাৰ পিছত প্ৰত্যাহাৰ।",
 ["Non-Cooperation began in 1920|১৯২০ত অসহযোগ আৰম্ভ", "It was linked with the Khilafat movement|ই খিলাফত আন্দোলনৰ সৈতে জড়িত", "Chauri Chaura came on 4 February 1922|১৯২২ৰ ৪ ফেব্ৰুৱাৰীত চৌৰী চৌৰা", "Gandhi then called the movement off|তাৰ পিছত গান্ধীয়ে আন্দোলন প্ৰত্যাহাৰ কৰিছিল"],
 LINK(S("Leave what the Raj offers|ৰাজে দিয়া বস্তু ত্যাগ", "From <mark>1920</mark> Gandhi urged Indians to withdraw cooperation: leave government schools and courts, return honours, boycott British goods, wear khadi.|<mark>১৯২০ৰ</mark> পৰা গান্ধীয়ে সহযোগ প্ৰত্যাহাৰৰ আহ্বান দিছিল: চৰকাৰী বিদ্যালয় আৰু আদালত ত্যাগ, উপাধি ঘূৰোৱা, ব্ৰিটিছ বস্তু বৰ্জন, খাদী পিন্ধা।", "He backed the <mark>Khilafat</mark> movement, which won him Muslim support.|তেওঁ <mark>খিলাফত</mark> আন্দোলন সমৰ্থন কৰিছিল, ইয়াৰ ফলত মুছলমান সমৰ্থন পাইছিল।", art="seal"),
  "british-13", 50, 2, "Gandhi arrives in Assam|অসমত গান্ধী", "The Assam History course tells Gandhi's visit to Assam in 1921.|অসমৰ ইতিহাস পাঠ্যক্ৰমত ১৯২১ত অসমলৈ গান্ধীৰ আগমনৰ কথা আছে।"),
 S("Chauri Chaura|চৌৰী চৌৰা", "On <mark>4 February 1922</mark> a crowd at [[chauri-chaura|Chauri Chaura]] set fire to a police station, killing about 22 policemen.|<mark>১৯২২ৰ ৪ ফেব্ৰুৱাৰীত</mark> [[chauri-chaura|চৌৰী চৌৰাত]] জনতাই আৰক্ষী থানাত জুই দিছিল, প্ৰায় ২২ জন আৰক্ষী নিহত হৈছিল।", "Gandhi saw the movement turning violent and called it off. He was arrested soon after.|আন্দোলন হিংসাত্মক হোৱা দেখি গান্ধীয়ে প্ৰত্যাহাৰ কৰিছিল। অলপ পিছতে তেওঁ গ্ৰেপ্তাৰ হৈছিল।", art="door"),
 IN("Gandhi called off Non-Cooperation after|গান্ধীয়ে অসহযোগ প্ৰত্যাহাৰ কৰিছিল", ".|ৰ পিছত।", ["Jallianwala Bagh|জালিয়ানৱালা বাগ", "Chauri Chaura|চৌৰী চৌৰা", "Dandi|ডাণ্ডী", "Bardoli|বাৰদোলী"], 1, "Chauri Chaura.|চৌৰী চৌৰা।"),
 OD("Which was NOT part of Non-Cooperation?|কোনটো অসহযোগৰ অংশ নহয়?", ["Boycott of British goods|ব্ৰিটিছ বস্তু বৰ্জন", "Leaving government schools|চৰকাৰী বিদ্যালয় ত্যাগ", "Wearing khadi|খাদী পিন্ধা", "Making salt at Dandi|ডাণ্ডীত লৱণ বনোৱা"], 3, "Dandi belongs to 1930.|ডাণ্ডী ১৯৩০ৰ।"),
 MP("Tap Chauri Chaura.|চৌৰী চৌৰা টিপা।", "chauri-chaura", ["chauri-chaura", "porbandar", "bombay", "delhi"], "In Gorakhpur district.|গোৰখপুৰ জিলাত।"),
 TF("Non-Cooperation was linked with the Khilafat movement.|অসহযোগ খিলাফত আন্দোলনৰ সৈতে জড়িত আছিল।", True, "Gandhi backed Khilafat.|গান্ধীয়ে খিলাফত সমৰ্থন কৰিছিল।"),
 SP("Chauri Chaura took place in *1932.*|চৌৰী চৌৰা *১৯৩২ত* হৈছিল।", "1922|১৯২২ত", "1922.|১৯২২।"),
)
u4 = U(4, "court", "The Swaraj Party|স্বৰাজ দল",
 "Fix the party papers keep asking about.|পৰীক্ষাত বাৰে বাৰে সোধা দলটো মনত ৰাখা।", "Finding recorded: Das and Motilal Nehru, 1923, to fight from inside the councils.|প্ৰমাণ লিখা হ'ল: দাস আৰু মতিলাল নেহৰু, ১৯২৩, পৰিষদৰ ভিতৰৰ পৰা যুঁজ।",
 ["The Swaraj Party was founded on 1 January 1923|১৯২৩ৰ ১ জানুৱাৰীত স্বৰাজ দল প্ৰতিষ্ঠিত", "Its founders were C. R. Das and Motilal Nehru|প্ৰতিষ্ঠাপক চিত্তৰঞ্জন দাস আৰু মতিলাল নেহৰু", "It aimed to enter the councils|ইয়াৰ লক্ষ্য পৰিষদত প্ৰৱেশ", "It won 45 of 145 seats in 1923|১৯২৩ত ই ১৪৫ৰ ৪৫টা আসন পাইছিল"],
 S("Into the councils|পৰিষদৰ ভিতৰলৈ", "After the withdrawal some Congress members wanted a new line. [[cr-das|C. R. Das]] and [[motilal-nehru|Motilal Nehru]] founded the <mark>Swaraj Party</mark> on 1 January <mark>1923</mark>.|প্ৰত্যাহাৰৰ পিছত কিছুমান কংগ্ৰেছ সদস্যই নতুন পথ বিচাৰিছিল। <mark>১৯২৩ৰ</mark> ১ জানুৱাৰীত [[cr-das|চিত্তৰঞ্জন দাস]] আৰু [[motilal-nehru|মতিলাল নেহৰুৱে]] <mark>স্বৰাজ দল</mark> গঢ়িছিল।", art="court"),
 S("Obstruct from within|ভিতৰৰ পৰা বাধা", "They contested the councils Gandhi rejected and won 45 of 145 seats. Vithalbhai Patel became president of the Central Assembly.|গান্ধীয়ে অস্বীকাৰ কৰা পৰিষদত তেওঁলোকে প্ৰতিদ্বন্দ্বিতা কৰি ১৪৫ৰ ৪৫টা আসন পাইছিল। বিঠলভাই পেটেল কেন্দ্ৰীয় সভাৰ সভাপতি হৈছিল।", art="houses"),
 IN("The Swaraj Party was founded by|স্বৰাজ দল গঢ়িছিল", ".|এ।", ["Ambedkar and Patel|আম্বেদকাৰ আৰু পেটেল", "Aruna Asaf Ali and Bose|অৰুণা আছফ আলী আৰু বসু", "Bhagat Singh and Rajguru|ভগত সিং আৰু ৰাজগুৰু", "Motilal Nehru and C. R. Das|মতিলাল নেহৰু আৰু চিত্তৰঞ্জন দাস"], 3, "Das and Motilal Nehru.|দাস আৰু মতিলাল নেহৰু।"),
 TF("The Swaraj Party was founded in 1923.|১৯২৩ত স্বৰাজ দল প্ৰতিষ্ঠিত হৈছিল।", True, "On 1 January.|১ জানুৱাৰীত।"),
 OR("Put these in order.|এইবোৰ ক্ৰমে সজোৱা।", ["Champaran|চম্পাৰণ", "Non-Cooperation|অসহযোগ", "Chauri Chaura|চৌৰী চৌৰা", "Swaraj Party|স্বৰাজ দল"], "1917, 1920, 1922, 1923.|১৯১৭, ১৯২০, ১৯২২, ১৯২৩।"),
 SP("The Swarajists chose to *boycott* the councils.|স্বৰাজীসকলে পৰিষদ *বৰ্জন* কৰিছিল।", "enter|প্ৰৱেশ", "They chose to enter them.|তেওঁলোকে প্ৰৱেশ কৰিছিল।"),
 MA([("C. R. Das|চিত্তৰঞ্জন দাস", "Swaraj Party|স্বৰাজ দল"), ("Raj Kumar Shukla|ৰাজকুমাৰ শুক্লা", "Champaran|চম্পাৰণ"), ("Gokhale|গোখলে", "Gandhi's mentor|গান্ধীৰ পথপ্ৰদৰ্শক")], "Name and link.|নাম আৰু সম্পৰ্ক।"),
)
test = TEST("Follow Gandhi's first decade in India.|ভাৰতত গান্ধীৰ প্ৰথম দশক অনুসৰণ কৰা।", "Recorded: Champaran, Non-Cooperation and the Swarajists.|লিখা হ'ল: চম্পাৰণ, অসহযোগ আৰু স্বৰাজী।",
 IN("In 1923 the Swaraj Party was founded by|১৯২৩ত স্বৰাজ দল গঢ়িছিল", ".|এ।", ["Motilal Nehru and C. R. Das|মতিলাল নেহৰু আৰু চিত্তৰঞ্জন দাস", "Gandhi and Jawaharlal Nehru|গান্ধী আৰু জৱাহৰলাল নেহৰু", "Sachin Sanyal and Jogesh Chatterjee|শচীন সান্যাল আৰু যোগেশ চট্টোপাধ্যায়", "Ghaffar Khan and Vithalbhai Patel|গফ্ফাৰ খান আৰু বিঠলভাই পেটেল"], 0, "Das and Motilal Nehru.|দাস আৰু মতিলাল নেহৰু।"),
 TF("Gandhi stayed in South Africa before returning to India.|ভাৰতলৈ উভতি অহাৰ আগতে গান্ধী দক্ষিণ আফ্ৰিকাত আছিল।", True, "From 1893 to 1914.|১৮৯৩ৰ পৰা ১৯১৪লৈ।"),
 OR("Order these.|এইবোৰ সজোৱা।", ["Champaran|চম্পাৰণ", "Rowlatt hartal|ৰাউলাট হৰতাল", "Non-Cooperation|অসহযোগ", "Chauri Chaura|চৌৰী চৌৰা"], "1917, 1919, 1920, 1922.|১৯১৭, ১৯১৯, ১৯২০, ১৯২২।"),
 MP("Tap Champaran.|চম্পাৰণ টিপা।", "champaran", ["champaran", "porbandar", "bombay", "delhi"], "In Bihar.|বিহাৰত।"),
 SP("Non-Cooperation was linked with the *Swadeshi* movement of Muslims.|অসহযোগ মুছলমানৰ *স্বদেশী* আন্দোলনৰ সৈতে জড়িত।", "Khilafat|খিলাফত", "The Khilafat movement.|খিলাফত আন্দোলন।"),
 MC("Consider these statements. (1) Gandhi's full name is Mohandas Karamchand Gandhi. (2) Chauri Chaura came before Champaran. (3) Gandhi withdrew Non-Cooperation in 1922. Which are correct?|এই উক্তিবোৰ বিবেচনা কৰা। (১) গান্ধীৰ সম্পূৰ্ণ নাম মোহনদাস কৰমচান্দ গান্ধী। (২) চম্পাৰণৰ আগতে চৌৰী চৌৰা। (৩) ১৯২২ত গান্ধীয়ে অসহযোগ প্ৰত্যাহাৰ কৰিছিল। কোনবোৰ শুদ্ধ?", ["1 and 2 only|কেৱল ১ আৰু ২", "1 and 3 only|কেৱল ১ আৰু ৩", "2 and 3 only|কেৱল ২ আৰু ৩", "1, 2 and 3|১, ২ আৰু ৩"], 1, "Champaran was first, in 1917.|চম্পাৰণ প্ৰথম, ১৯১৭ত।"),
)
LESSON(26, "Gandhi and Non-Cooperation|গান্ধী আৰু অসহযোগ", "1915–1923|১৯১৫–১৯২৩", "The national movement|ৰাষ্ট্ৰীয় আন্দোলন", "Evidence file 26|প্ৰমাণ নথি ২৬", "A new kind of leader|নতুন ধৰণৰ নেতা",
 "A lawyer back from South Africa turned peasants and students into a mass movement, then stopped it himself.|দক্ষিণ আফ্ৰিকাৰ পৰা উভতি অহা উকীলে খেতিয়ক আৰু ছাত্ৰক গণ আন্দোলনলৈ আনিলে, তাৰ পিছত নিজেই বন্ধ কৰিলে।",
 sources, [u1, u2, u3, u4], test, ["champaran", "porbandar", "chauri-chaura", "bombay", "delhi"],
 timeline=[("1915", "Gandhi returns to India|গান্ধী ভাৰতলৈ", "u1"), ("1917", "Champaran|চম্পাৰণ", "u2"), ("1920", "Non-Cooperation|অসহযোগ", "u3"), ("1922", "Chauri Chaura|চৌৰী চৌৰা", "u3"), ("1923", "Swaraj Party|স্বৰাজ দল", "u4")])
