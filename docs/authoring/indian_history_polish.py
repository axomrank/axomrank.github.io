#!/usr/bin/env python3
"""Second pass over the Indian History lessons: predictions, diagrams, tricks,
exam-trap cards, links between lessons and section art.

Order: lesson scripts, indian_history_outline.py, this file, then
scripts/build_indian_history_bank.py and scripts/build.py. This pass also releases
the course, so it must run last. Tricks are labelled as tricks.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from indian_history_kit import ROOT, t, many

Y = lambda *a: list(a)
# lesson, unit, position, stem, options, answer, why. A prediction opens the card that answers it.
GUESS = [
 (1, "u3", 1, "Lothal was a Harappan town near the sea. I expect digs there found|লোথাল সাগৰৰ ওচৰৰ হৰপ্পীয় নগৰ। মোৰ অনুমান খননত ওলাইছিল", ["a dock|ডক", "a royal palace|ৰাজপ্ৰাসাদ", "iron ploughs|লোহাৰ নাঙল"], 0, "A brick basin at Lothal is read as a dock.|লোথালৰ ইটাৰ অৱবাহিকাক ডক বুলি ধৰা হয়।"),
 (2, "u2", 1, "The Rigveda praises the Saraswati. Today, naming that river is|ঋগ্বেদত সৰস্বতীৰ প্ৰশংসা আছে। আজি সেই নদী চিনাক্ত কৰাটো", ["settled|নিশ্চিত", "disputed|বিতৰ্কিত", "impossible|অসম্ভৱ"], 1, "The usual answer is the Ghaggar-Hakra, but scholars dispute it.|সাধাৰণ উত্তৰ ঘগ্গৰ-হাক্ৰা, কিন্তু পণ্ডিতৰ মাজত বিতৰ্ক আছে।"),
 (3, "u4", 1, "The Buddha and Mahavira lived at about the same time. I expect they taught in|বুদ্ধ আৰু মহাবীৰ প্ৰায় একে সময়ৰ। মোৰ অনুমান তেওঁলোকে শিক্ষা দিছিল", ["the same region|একে অঞ্চলত", "opposite ends of India|ভাৰতৰ দুই মূৰত", "different countries overseas|সাগৰপাৰৰ দেশত"], 0, "Both taught in the eastern Ganga plain.|দুয়োজনে পূব গংগা সমভূমিত শিক্ষা দিছিল।"),
 (4, "u3", 1, "Porus lost to Alexander. I expect Alexander|পুৰু আলেকজেণ্ডাৰৰ ওচৰত হাৰিল। মোৰ অনুমান আলেকজেণ্ডাৰে", ["killed him|তেওঁক হত্যা কৰিলে", "kept him as ruler|তেওঁক শাসক ৰাখিলে", "took him to Macedonia|তেওঁক মেচিডনলৈ নিলে"], 1, "Porus stayed on as ruler under Alexander.|পুৰু আলেকজেণ্ডাৰৰ অধীনত শাসক হৈ থাকিল।"),
 (5, "u3", 2, "Ashoka had just won a great war. In his own edict I expect him to record|অশোকে ডাঙৰ যুদ্ধ জিকিছে। তেওঁৰ নিজৰ অনুশাসনত মোৰ অনুমান লিখা থাকিব", ["pride in victory|জয়ৰ গৌৰৱ", "deep remorse|গভীৰ অনুতাপ", "plans for the next war|পিছৰ যুদ্ধৰ পৰিকল্পনা"], 1, "Rock Edict 13 records his remorse.|ত্ৰয়োদশ শিলানুশাসনত তেওঁৰ অনুতাপ আছে।"),
 (6, "u1", 1, "Kushan sculpture from Gandhara mixed Indian forms with those of|গান্ধাৰৰ কুষাণ ভাস্কৰ্যত ভাৰতীয় ৰূপৰ লগত মিহলি হৈছিল", ["Greece|গ্ৰীচ", "China|চীন", "Japan|জাপান"], 0, "Gandhara art mixed Greek and Indian forms.|গান্ধাৰ শিল্পত গ্ৰীক আৰু ভাৰতীয় ৰূপ মিহলি হৈছিল।"),
 (7, "u2", 1, "Samudragupta's pillar stands far away at Prayagraj. Does it name Assam's land?|সমুদ্ৰগুপ্তৰ স্তম্ভ দূৰৈৰ প্ৰয়াগৰাজত। ইয়াত অসমৰ ভূমিৰ নাম আছে নে?", ["Yes, as Kamarupa|আছে, কামৰূপ নামে", "No, Assam was unknown|নাই, অসম অজ্ঞাত আছিল", "Only as a river|কেৱল নদী হিচাপে"], 0, "Kamarupa is listed among the frontier states.|কামৰূপ সীমান্ত ৰাজ্যৰ তালিকাত আছে।"),
 (8, "u2", 1, "Harsha marched south. I expect he|হৰ্ষই দক্ষিণলৈ অভিযান কৰিলে। মোৰ অনুমান তেওঁ", ["reached the far south|সুদূৰ দক্ষিণ পালে", "was stopped at a river|এখন নদীত ৰোধ খালে", "never fought there|তাত কেতিয়াও যুঁজা নাছিল"], 1, "Pulakeshin II stopped him at the Narmada.|দ্বিতীয় পুলকেশীয়ে তেওঁক নৰ্মদাত ৰোধ কৰিছিল।"),
 (9, "u2", 1, "The Cholas held a rich delta. To reach beyond India, I expect they used|চোলৰ হাতত উৰ্বৰ ব-দ্বীপ আছিল। ভাৰতৰ বাহিৰলৈ যাবলৈ মোৰ অনুমান তেওঁলোকে ব্যৱহাৰ কৰিছিল", ["a fleet|নৌবহৰ", "mountain passes|গিৰিপথ", "camel caravans|উটৰ দল"], 0, "Rajendra I's fleet raided Srivijaya's ports.|ৰাজেন্দ্ৰ প্ৰথমৰ নৌবহৰে শ্ৰীবিজয়ৰ বন্দৰ আক্ৰমণ কৰিছিল।"),
 (10, "u2", 1, "Papers call Aryabhata the father of zero. Did he write a symbol for it?|পৰীক্ষাত আৰ্যভট্টক শূন্যৰ জনক বোলে। তেওঁ ইয়াৰ চিহ্ন লিখিছিল নে?", ["Yes|লিখিছিল", "No|লিখা নাছিল"], 1, "His place-value system needed zero, but he had no symbol for it.|তেওঁৰ পদ্ধতিত শূন্য লাগিছিল, কিন্তু চিহ্ন নাছিল।"),
 (11, "u3", 1, "Muhammad bin Tughluq wanted a hold on the south. I expect he|মহম্মদ বিন তুঘলকে দক্ষিণত ভেটি বিচাৰিছিল। মোৰ অনুমান তেওঁ", ["moved his capital there|তালৈ ৰাজধানী নিলে", "gave up the south|দক্ষিণ এৰি দিলে", "sent only envoys|কেৱল দূত পঠালে"], 0, "He moved the capital to Daulatabad.|তেওঁ দৌলতাবাদলৈ ৰাজধানী নিছিল।"),
 (12, "u2", 1, "Vijayanagara faced several sultanates together in 1565. I expect|১৫৬৫ত বিজয়নগৰে কেইবাখনো ছুলতানীৰ সন্মুখীন হৈছিল। মোৰ অনুমান", ["Vijayanagara won|বিজয়নগৰ জিকিল", "the sultanates won|ছুলতানীবোৰ জিকিল", "no battle happened|যুদ্ধ নহ'ল"], 1, "The sultanates won at Talikota.|তালিকোটাত ছুলতানীবোৰ জিকিছিল।"),
 (13, "u3", 1, "A Sikh Guru travelled east. How far did he come?|এজন শিখ গুৰু পূবলৈ আহিছিল। তেওঁ কিমান দূৰলৈ আহিছিল?", ["Only to Delhi|দিল্লীলৈকে", "As far as Assam|অসমলৈকে", "Only to Punjab's edge|পঞ্জাবৰ সীমালৈকে"], 1, "Guru Tegh Bahadur reached Dhubri in Assam.|গুৰু তেগ বাহাদুৰ অসমৰ ধুবুৰী পাইছিল।"),
 (14, "u1", 1, "Babur was far outnumbered at Panipat. His edge came from|পানিপথত বাবৰৰ সৈন্য বহু কম আছিল। তেওঁৰ সুবিধা আছিল", ["more elephants|বেছি হাতী", "guns and cannon|বন্দুক আৰু কামান", "a naval fleet|নৌবহৰ"], 1, "Ibrahim's army lacked gunpowder arms.|ইব্ৰাহিমৰ সৈন্যৰ বাৰুদৰ অস্ত্ৰ নাছিল।"),
 (15, "u1", 1, "Hemu was winning with his elephants. What turned the battle?|হেমুৱে হাতীৰে জিকি আছিল। যুদ্ধ কিহে সলালে?", ["An arrow struck him|তেওঁক কাঁড় লাগিল", "Rain stopped it|বৰষুণে ৰখালে", "His elephants ran away first|হাতী আগতে পলাল"], 0, "An arrow hit his eye, and his army panicked.|কাঁড় তেওঁৰ চকুত লাগিল, সৈন্য ত্ৰস্ত হ'ল।"),
 (16, "u2", 1, "Shah Jahan fell ill in 1657 with four grown sons. I expect|১৬৫৭ত চাৰি পুত্ৰ থকা শ্বাহজাহান অসুস্থ হ'ল। মোৰ অনুমান", ["a peaceful handover|শান্তিপূৰ্ণ হস্তান্তৰ", "a war between the sons|পুত্ৰসকলৰ যুদ্ধ", "the Company took over|কোম্পানীয়ে দখল কৰিলে"], 1, "Aurangzeb won the war of succession.|ঔৰংগজেবে উত্তৰাধিকাৰৰ যুদ্ধ জিকিছিল।"),
 (17, "u2", 1, "In 1761 the Marathas, then the strongest power, met an Afghan army. I expect|১৭৬১ত তেতিয়াৰ শক্তিশালী মাৰাঠাই আফগান সৈন্যৰ সন্মুখীন হ'ল। মোৰ অনুমান", ["the Marathas won|মাৰাঠা জিকিল", "the Afghans won|আফগান জিকিল", "both signed a treaty first|যুদ্ধৰ আগতে সন্ধি হ'ল"], 1, "Durrani won decisively.|দুৰানীয়ে চূড়ান্তভাৱে জিকিছিল।"),
 (18, "u2", 1, "The Nawab's army was far larger than Clive's. Yet it lost because|নবাবৰ সৈন্য ক্লাইভতকৈ বহু বেছি আছিল। তথাপি হাৰিল কাৰণ", ["his commander held back|তেওঁৰ সেনাপতিয়ে সৈন্য ৰখিলে", "it had no guns|বন্দুক নাছিল", "it fought at sea|সাগৰত যুঁজিছিল"], 0, "Mir Jafar kept his troops idle.|মীৰ জাফৰে সৈন্য নিষ্ক্ৰিয় ৰাখিছিল।"),
 (19, "u4", 1, "Awadh's ruler had heirs. Could lapse be used there?|অযোধ্যাৰ ৰজাৰ উত্তৰাধিকাৰী আছিল। তাত স্বত্ববিলোপ প্ৰয়োগ হ'ব পাৰিছিল নে?", ["Yes, lapse was used|হয়, প্ৰয়োগ হৈছিল", "No, another pretext was used|নহয়, আন অজুহাত লোৱা হৈছিল"], 1, "The pretext was misrule.|অজুহাত কুশাসন আছিল।"),
 (20, "u1", 1, "Vidyasagar petitioned for widow remarriage. I expect the public response was|বিদ্যাসাগৰে বিধৱা বিবাহৰ আবেদন কৰিলে। মোৰ অনুমান ৰাজহুৱা সঁহাৰি আছিল", ["unanimous support|একমত সমৰ্থন", "a far bigger petition against|বহু ডাঙৰ বিৰোধী আবেদন", "complete silence|সম্পূৰ্ণ নীৰৱতা"], 1, "A counter-petition had far more signatures, yet the Act passed.|বিৰোধী আবেদনত বহু বেছি স্বাক্ষৰ আছিল, তথাপি আইন গৃহীত হৈছিল।"),
 (21, "u2", 1, "The sepoys marched to Delhi. To lead them, I expect they proclaimed|চিপাহীসকল দিল্লীলৈ গ'ল। নেতৃত্বৰ বাবে মোৰ অনুমান তেওঁলোকে ঘোষণা কৰিলে", ["the old Mughal emperor|বৃদ্ধ মোগল সম্ৰাটক", "a British general|ব্ৰিটিছ সেনাপতিক", "the Nawab of Bengal|বংগৰ নবাবক"], 0, "They proclaimed Bahadur Shah II.|তেওঁলোকে বাহাদুৰ শ্বাহ দ্বিতীয়ক ঘোষণা কৰিছিল।"),
 (22, "u2", 1, "Nil Darpan attacked the planters and was translated into English. For its publisher, I expect|নীলদৰ্পণে নীলকৰক আক্ৰমণ কৰিছিল, ইংৰাজীত অনুবাদ হ'ল। প্ৰকাশকৰ বাবে মোৰ অনুমান", ["a reward|বঁটা", "a trial and fine|বিচাৰ আৰু জৰিমনা", "nothing at all|একো নহ'ল"], 1, "James Long was tried and fined.|জেমছ লঙৰ বিচাৰ হৈ জৰিমনা হৈছিল।"),
 (23, "u3", 1, "Naoroji wanted Britain itself to hear the case. I expect he went to|নৌৰজীয়ে ব্ৰিটেইনক যুক্তি শুনাব বিচাৰিছিল। মোৰ অনুমান তেওঁ গ'ল", ["the British Parliament|ব্ৰিটিছ সংসদলৈ", "the Mughal court|মোগল ৰাজসভালৈ", "the Paris press|পেৰিছৰ সংবাদলৈ"], 0, "He became an MP in 1892.|১৮৯২ত তেওঁ সাংসদ হৈছিল।"),
 (24, "u1", 1, "Bengal has been cut in two. How would you answer? History's answer was to|বংগ দুভাগ হ'ল। ইতিহাসৰ উত্তৰ আছিল", ["boycott British goods|ব্ৰিটিছ বস্তু বৰ্জন", "move to Assam|অসমলৈ যোৱা", "accept it quietly|নীৰৱে মানি লোৱা"], 0, "Swadeshi and boycott were the answer.|স্বদেশী আৰু বৰ্জন উত্তৰ আছিল।"),
 (25, "u4", 1, "Under dyarchy Indian ministers got some subjects. The Governor, I expect, kept|দ্বৈত শাসনত ভাৰতীয় মন্ত্ৰীয়ে কিছু বিষয় পালে। মোৰ অনুমান গৱৰ্ণৰে ৰাখিলে", ["law and order|আইন-শৃংখলা", "education|শিক্ষা", "health|স্বাস্থ্য"], 0, "Law and order stayed reserved.|আইন-শৃংখলা সংৰক্ষিত আছিল।"),
 (26, "u2", 1, "Officials ordered Gandhi to leave Champaran. I expect he|বিষয়াই গান্ধীক চম্পাৰণ এৰিবলৈ আদেশ দিলে। মোৰ অনুমান তেওঁ", ["left quietly|নীৰৱে গুচি গ'ল", "refused and took the consequences|অস্বীকাৰ কৰি পৰিণতি মানিলে", "called for armed revolt|সশস্ত্ৰ বিদ্ৰোহ কৰিলে"], 1, "It was his first satyagraha on Indian soil.|ই ভাৰতত তেওঁৰ প্ৰথম সত্যাগ্ৰহ।"),
 (27, "u1", 1, "A commission on India's future had no Indians. I expect the Congress|ভাৰতৰ ভৱিষ্যৎৰ কমিছনত কোনো ভাৰতীয় নাছিল। মোৰ অনুমান কংগ্ৰেছে", ["joined it|যোগ দিলে", "boycotted it|বৰ্জন কৰিলে", "ignored it silently|নীৰৱে এৰাই চলিল"], 1, "The Congress boycotted it.|কংগ্ৰেছে ইয়াক বৰ্জন কৰিছিল।"),
 (28, "u3", 1, "Police beat the volunteers at the Dharasana salt works. I expect the volunteers|ধৰাসনাত আৰক্ষীয়ে স্বেচ্ছাসেৱকক প্ৰহাৰ কৰিলে। মোৰ অনুমান স্বেচ্ছাসেৱকে", ["struck back|উভতি আঘাত কৰিলে", "did not strike back|উভতি আঘাত নকৰিলে", "ran to Bombay|বোম্বেলৈ পলাল"], 1, "They did not strike back, and the story reached the world.|তেওঁলোকে আঘাত নকৰিলে, খবৰ বিশ্বলৈ গ'ল।"),
 (29, "u2", 1, "Gandhi said Do or Die in August 1942, in the middle of a world war. I expect the government|১৯৪২ৰ আগষ্টত বিশ্বযুদ্ধৰ মাজত গান্ধীয়ে কৰো বা মৰো ক'লে। মোৰ অনুমান চৰকাৰে", ["opened talks|আলোচনা আৰম্ভ কৰিলে", "jailed the leaders within hours|কেইঘণ্টামানতে নেতাক বন্দী কৰিলে", "left India|ভাৰত এৰিলে"], 1, "Almost the whole leadership was jailed.|প্ৰায় গোটেই নেতৃত্ব বন্দী হৈছিল।"),
 (30, "u3", 1, "The British put INA men on public trial. I expect the public|ব্ৰিটিছে ফৌজৰ সদস্যৰ ৰাজহুৱা বিচাৰ কৰিলে। মোৰ অনুমান ৰাইজে", ["backed the British|ব্ৰিটিছক সমৰ্থন কৰিলে", "protested widely|ব্যাপক প্ৰতিবাদ কৰিলে", "took no notice|গুৰুত্ব নিদিলে"], 1, "The trials sparked protest across religious lines.|বিচাৰে ধৰ্ম নিৰ্বিশেষে প্ৰতিবাদ জগাইছিল।"),
 (31, "u1", 1, "Wavell called Indian leaders to Simla in 1945. The talks broke on|১৯৪৫ত ৱেভেলে ভাৰতীয় নেতাক চিমলালৈ মাতিলে। আলোচনা ভাঙিল", ["who would name Muslim members|মুছলিম সদস্য কোনে দিব, তাত", "the salt tax|লৱণ কৰত", "the capital's location|ৰাজধানীৰ ঠাইত"], 0, "Jinnah insisted that only the League could name them.|জিন্নাহে কেৱল লীগে দিব বুলি জোৰ দিছিল।"),
 (32, "u2", 1, "Most princely states joined by agreement. Junagadh and Hyderabad joined by|বেছিভাগ দেশীয় ৰাজ্য সন্মতিৰে আহিছিল। জুনাগড় আৰু হায়দৰাবাদ আহিছিল", ["agreement too|সন্মতিৰেই", "military action|সামৰিক কাৰ্যৰে", "a vote in London|লণ্ডনৰ ভোটেৰে"], 1, "Both came in through military action.|দুয়োখন সামৰিক কাৰ্যৰে আহিছিল।"),
]
# lesson, unit, story title (English), layout, items
DIAGRAMS = [
 (2, "u1", "Four books, one oldest", "grid", ["Rigveda|ঋগ্বেদ", "Samaveda|সামবেদ", "Yajurveda|যজুৰ্বেদ", "Atharvaveda|অথৰ্ববেদ"]),
 (3, "u2", "Truths, Path and Sangha", "grid", ["Four Noble Truths|চাৰি আৰ্য সত্য", "Eightfold Path|অষ্টাংগিক মাৰ্গ", "Sangha|সংঘ"]),
 (4, "u2", "Three dynasties", "flow", ["Haryanka|হৰ্যংক", "Shishunaga|শিশুনাগ", "Nanda|নন্দ", "Maurya|মৌৰ্য"]),
 (5, "u3", "Son and grandson", "flow", ["Chandragupta|চন্দ্ৰগুপ্ত", "Bindusara|বিন্দুসাৰ", "Ashoka|অশোক"]),
 (5, "u5", "Stone or legend?", "grid", ["Edicts: Kalinga, remorse|অনুশাসন: কলিংগ, অনুতাপ", "Later texts: Third Council, Mahinda|পিছৰ গ্ৰন্থ: তৃতীয় সংগীতি, মহিন্দ"]),
 (6, "u3", "Poems of the Tamil lands", "grid", ["Chola|চোল", "Chera|চেৰ", "Pandya|পাণ্ড্য"]),
 (7, "u1", "Father, son, grandson", "flow", ["Chandragupta I|চন্দ্ৰগুপ্ত প্ৰথম", "Samudragupta|সমুদ্ৰগুপ্ত", "Chandragupta II|চন্দ্ৰগুপ্ত দ্বিতীয়"]),
 (7, "u3", "Three plays", "grid", ["Abhijnana Shakuntalam|অভিজ্ঞান শকুন্তলম", "Malavikagnimitram|মালৱিকাগ্নিমিত্ৰম", "Vikramorvashiyam|বিক্ৰমোৰ্বশীয়ম"]),
 (8, "u3", "One man, many spellings", "grid", ["Megasthenes: Maurya|মেগাস্থিনিছ: মৌৰ্য", "Faxian: Gupta|ফা-হিয়েন: গুপ্ত", "Xuanzang: Harsha|হিউৱেন চাঙ: হৰ্ষ"]),
 (10, "u1", "Books with many hands", "grid", ["Sushruta: surgery|সুশ্ৰুত: শল্যচিকিৎসা", "Charaka: medicine|চৰক: চিকিৎসা", "Aryabhata: astronomy|আৰ্যভট্ট: জ্যোতিৰ্বিদ্যা"]),
 (12, "u3", "Four minarets", "grid", ["Gol Gumbaz: Bijapur|গোল গম্বুজ: বিজাপুৰ", "Charminar: Hyderabad|চাৰমিনাৰ: হায়দৰাবাদ", "Qutb Minar: Delhi|কুতুব মিনাৰ: দিল্লী"]),
 (13, "u1", "Everyday languages", "flow", ["Tamil lands|তামিল ভূমি", "Karnataka|কৰ্ণাটক", "North India and Assam|উত্তৰ ভাৰত আৰু অসম"]),
 (14, "u4", "A boy king", "flow", ["Babur|বাবৰ", "Humayun|হুমায়ুন", "Sur interval|সূৰ অন্তৰাল", "Akbar|আকবৰ"]),
 (15, "u1", "An arrow turns a battle", "flow", ["1526: Babur wins|১৫২৬: বাবৰৰ জয়", "1556: Mughals beat Hemu|১৫৫৬: মোগলৰ জয়", "1761: Durrani wins|১৭৬১: দুৰানীৰ জয়"]),
 (16, "u2", "Four sons, one throne", "flow", ["Akbar|আকবৰ", "Jahangir|জাহাংগীৰ", "Shah Jahan|শ্বাহজাহান", "Aurangzeb|ঔৰংগজেব"]),
 (17, "u1", "Crowned at Raigad", "grid", ["Chhatrapati|ছত্ৰপতি", "Ashta Pradhan|অষ্টপ্ৰধান", "Chauth|চৌথ"]),
 (18, "u4", "Mughal title, Company power", "flow", ["Plassey, 1757|পলাশী, ১৭৫৭", "Buxar, 1764|বক্সাৰ, ১৭৬৪", "Diwani, 1765|দেৱানী, ১৭৬৫", "Regulating Act, 1773|ৰেগুলেটিং আইন, ১৭৭৩"]),
 (19, "u1", "One office, three names", "flow", ["Hastings: Bengal, 1773|হেষ্টিংছ: বংগ, ১৭৭৩", "Bentinck: India, 1833|বেণ্টিংক: ভাৰত, ১৮৩৩", "Canning: Viceroy, 1858|কেনিং: ভাইচৰয়, ১৮৫৮"]),
 (20, "u2", "Schools and reform", "flow", ["Brahmo Samaj, 1828|ব্ৰাহ্ম সমাজ, ১৮২৮", "Arya Samaj, 1875|আৰ্য সমাজ, ১৮৭৫", "Ramakrishna Mission, 1897|ৰামকৃষ্ণ মিছন, ১৮৯৭"]),
 (21, "u4", "Crown for Company", "flow", ["Company rule|কোম্পানীৰ শাসন", "Revolt, 1857|বিদ্ৰোহ, ১৮৫৭", "Crown rule, 1858|ৰাজমুকুটৰ শাসন, ১৮৫৮"]),
 (22, "u3", "Four in a row", "flow", ["Macaulay, 1835|মেকলে, ১৮৩৫", "Wood, 1854|উড, ১৮৫৪", "Raleigh, 1902|ৰেলে, ১৯০২", "Sadler, 1917|চেডলাৰ, ১৯১৭"]),
 (23, "u4", "Pressure inside", "flow", ["Bombay, 1885|বোম্বে, ১৮৮৫", "Calcutta, 1906|কলিকতা, ১৯০৬", "Surat, 1907|চুৰাট, ১৯০৭"]),
 (24, "u2", "Three radicals", "grid", ["Lal: Lajpat Rai|লাল: লাজপত ৰায়", "Bal: Tilak|বাল: তিলক", "Pal: Bipin Chandra Pal|পাল: বিপিনচন্দ্ৰ পাল"]),
 (25, "u4", "Reserved or transferred?", "grid", ["Reserved: law, finance, land revenue|সংৰক্ষিত: আইন, বিত্ত, ভূমি ৰাজহ", "Transferred: education, health, farming|হস্তান্তৰিত: শিক্ষা, স্বাস্থ্য, কৃষি"]),
 (25, "u2", "Counting the dead", "grid", ["Hunter Committee: 379|হাণ্টাৰ সমিতি: ৩৭৯", "Congress inquiry: about 1,000|কংগ্ৰেছৰ তদন্ত: প্ৰায় ১,০০০"]),
 (26, "u4", "Into the councils", "flow", ["Champaran, 1917|চম্পাৰণ, ১৯১৭", "Non-Cooperation, 1920|অসহযোগ, ১৯২০", "Chauri Chaura, 1922|চৌৰী চৌৰা, ১৯২২", "Swaraj Party, 1923|স্বৰাজ দল, ১৯২৩"]),
 (27, "u2", "Bombs meant to be heard", "flow", ["Saunders, 1928|চণ্ডাৰ্ছ, ১৯২৮", "Assembly, 1929|সভা, ১৯২৯", "Hanged, 1931|ফাঁচী, ১৯৩১"]),
 (28, "u4", "Three Tables, one Congress visit", "grid", ["First, 1930: absent|প্ৰথম, ১৯৩০: অনুপস্থিত", "Second, 1931: Gandhi|দ্বিতীয়, ১৯৩১: গান্ধী", "Third, 1932: absent|তৃতীয়, ১৯৩২: অনুপস্থিত"]),
 (29, "u4", "Three mass movements", "flow", ["Non-Cooperation, 1920|অসহযোগ, ১৯২০", "Civil Disobedience, 1930|আইন অমান্য, ১৯৩০", "Quit India, 1942|ভাৰত ত্যাগ, ১৯৪২"]),
 (30, "u2", "Singapore, 1943", "flow", ["Mohan Singh, 1942|মোহন সিং, ১৯৪২", "Bose at Singapore, 1943|ছিংগাপুৰত বসু, ১৯৪৩", "Rangoon, 1944|ৰেংগুন, ১৯৪৪"]),
 (31, "u3", "Calcutta, August 1946", "flow", ["Mutiny, February|বিদ্ৰোহ, ফেব্ৰুৱাৰী", "Cabinet Mission, May|কেবিনেট অভিযান, মে'", "League withdraws, July|লীগৰ প্ৰত্যাহাৰ, জুলাই", "Direct Action, August|প্ৰত্যক্ষ সংগ্ৰাম, আগষ্ট"]),
 (32, "u4", "A line of dates", "flow", ["Goa, 1961|গোৱা, ১৯৬১", "Smiling Buddha, 1974|স্মাইলিং বুদ্ধ, ১৯৭৪", "Meghdoot, 1984|মেঘদূত, ১৯৮৪", "Galwan, 2020|গালৱান, ২০২০"]),
]
# lesson, unit, story title, a labelled trick added as the card's last beat
TRICKS = [
 (2, "u1", "Words, not cities", "Memory trick: <b>R-S-Y-A</b>, and R comes first.|মনত ৰখাৰ কৌশল: <b>ঋ-সা-য-অ</b>, ঋ প্ৰথম।"),
 (3, "u1", "Awakening and first sermon", "Memory trick: <b>Lumbini Life, Bodh Bright, Sarnath Speech.</b>|মনত ৰখাৰ কৌশল: <b>লুম্বিনী জন্ম, বোধগয়া বোধ, সাৰনাথ সম্ভাষণ।</b>"),
 (11, "u1", "From slave to sultan", "Memory trick for the five: <b>My Kind Teacher Sells Lemons.</b>|পাঁচটা বংশৰ কৌশল: <b>মা-খি-তু-চৈ-লো</b>।"),
 (15, "u1", "The second Panipat", "Memory trick: <b>'26 Lodi falls, '56 Hemu falls, '61 Marathas fall.</b>|মনত ৰখাৰ কৌশল: <b>'২৬ত লোদী, '৫৬ত হেমু, '৬১ত মাৰাঠা।</b>"),
 (19, "u1", "The trap", "Memory trick: <b>Hastings Bengal, Bentinck Bharat, Canning Crown.</b>|মনত ৰখাৰ কৌশল: <b>হেষ্টিংছ বংগ, বেণ্টিংক ভাৰত, কেনিং ৰাজমুকুট।</b>"),
 (22, "u3", "Wood's Despatch", "Memory trick for the chain: <b>My Wise Rector Smiles</b>: Macaulay, Wood, Raleigh, Sadler.|শৃংখলৰ কৌশল: <b>মে-উ-ৰে-চে</b>: মেকলে, উড, ৰেলে, চেডলাৰ।"),
 (25, "u1", "A nation stops work", "Memory trick for 1919: <b>March law, April Bagh, May letter, October inquiry, December Act.</b>|১৯১৯ৰ কৌশল: <b>মাৰ্চত আইন, এপ্ৰিলত বাগ, মে'ত চিঠি, অক্টোবৰত তদন্ত, ডিচেম্বৰত আইন।</b>"),
 (28, "u4", "Talks without the Congress", "Memory trick: <b>Out, In, Out.</b> The Congress attended only the middle Table.|মনত ৰখাৰ কৌশল: <b>নাই, আছে, নাই।</b> কেৱল মাজৰখনত কংগ্ৰেছ আছিল।"),
 (31, "u2", "Twenty-two ships", "Memory trick for APSC's order: <b>Quit, Wavell, Mutiny, Mountbatten: 42, 45, 46, 47.</b>|APSCৰ ক্ৰমৰ কৌশল: <b>ভাৰত ত্যাগ, ৱেভেল, বিদ্ৰোহ, মাউণ্টবেটেন: ৪২, ৪৫, ৪৬, ৪৭।</b>"),
]
# lesson: (trap title, up to two lines). Shown in the lesson guide as a revision card.
TRAPS = {
 1: ("Lothal has the dock, Kalibangan the field. Dholavira has the signboard, Banawali the clay plough.|লোথালত ডক, কালিবংগানত পথাৰ। ধোলাভিৰাত চিহ্ন ফলক, বনাৱালীত মাটিৰ নাঙল।", "The Great Bath is at Mohenjo-daro, never Harappa.|বৃহৎ স্নানাগাৰ মহেঞ্জোদাৰোত, হৰপ্পাত নহয়।"),
 2: ("The Rigveda is the oldest Veda.|ঋগ্বেদ আটাইতকৈ পুৰণি বেদ।", "The Arthashastra and the Rajatarangini are not Vedas, however old they sound.|অৰ্থশাস্ত্ৰ আৰু ৰাজতৰংগিণী বেদ নহয়।"),
 3: ("Enlightenment is Bodh Gaya, not Kushinagar. Kushinagar is parinirvana.|জ্ঞানলাভ বোধগয়াত, কুশীনগৰত নহয়। কুশীনগৰত পৰিনিৰ্বাণ।", "Mahavira is the 24th Tirthankara. Parshvanatha is the 23rd.|মহাবীৰ ২৪তম তীৰ্থংকৰ। পাৰ্শ্বনাথ ২৩তম।"),
 4: ("Alexander was from Macedonia, not Persia.|আলেকজেণ্ডাৰ মেচিডনৰ, পাৰস্যৰ নহয়।", "Jhelum is the Hydaspes. Beas is where he stopped.|জিলম হ'ল হাইডাস্পিছ। বিপাশাত তেওঁ ৰৈছিল।"),
 5: ("Chanakya goes with Chandragupta, not Ashoka.|চাণক্য চন্দ্ৰগুপ্তৰ সৈতে, অশোকৰ সৈতে নহয়।", "Kalinga is Ashoka's war, not Bindusara's.|কলিংগ অশোকৰ যুদ্ধ, বিন্দুসাৰৰ নহয়।"),
 6: ("Kanishka's main capital was Purushapura, not Pataliputra.|কনিষ্কৰ মূল ৰাজধানী পুৰুষপুৰ, পাটলিপুত্ৰ নহয়।", "Sangam poems are in Old Tamil.|সংগম কবিতা প্ৰাচীন তামিলত।"),
 7: ("Chandragupta Maurya and Chandragupta I are six centuries apart.|চন্দ্ৰগুপ্ত মৌৰ্য আৰু চন্দ্ৰগুপ্ত প্ৰথমৰ মাজত ছয় শতিকাৰ ব্যৱধান।", "Harisena served Samudragupta. Banabhatta served Harsha.|হৰিষেণ সমুদ্ৰগুপ্তৰ। বাণভট্ট হৰ্ষৰ।"),
 8: ("Hiuen Tsang and Xuanzang are the same man.|Hiuen Tsang আৰু Xuanzang একেজন।", "Harsha's limit was the Narmada, not the far south.|হৰ্ষৰ সীমা নৰ্মদা, সুদূৰ দক্ষিণ নহয়।"),
 9: ("Vatapi is Chalukya. Kanchipuram is Pallava. Thanjavur is Chola.|বাতাপি চালুক্য। কাঞ্চীপুৰম পল্লৱ। তঞ্জাৱুৰ চোল।", "Kalhana wrote the Rajatarangini, not Kalidasa.|ৰাজতৰংগিণী কলহণৰ, কালিদাসৰ নহয়।"),
 10: ("Sushruta for surgery, Charaka for the Samhita of medicine.|শল্যচিকিৎসাৰ বাবে সুশ্ৰুত, চিকিৎসা সংহিতাৰ বাবে চৰক।", "Trimurti Sadashiva is at Elephanta, not Ajanta.|ত্ৰিমূৰ্তি সদাশিৱ এলিফেণ্টাত, অজন্তাত নহয়।"),
 11: ("Razia ruled at Delhi. Chand Bibi, Ahilya Bai and Lakshmibai did not.|ৰাজিয়াই দিল্লীত শাসন কৰিছিল। চান্দ বিবি, অহল্যা বাই, লক্ষ্মীবাইয়ে নহয়।", "Ibn Battuta goes with Muhammad bin Tughluq.|ইবন বতুতা মহম্মদ বিন তুঘলকৰ সৈতে।"),
 12: ("Harihara and Bukka founded Vijayanagara, not the Hoysalas.|হৰিহৰ আৰু বুক্কই বিজয়নগৰ গঢ়িছিল, হয়শালা নহয়।", "Gol Gumbaz is at Bijapur, Charminar at Hyderabad.|গোল গম্বুজ বিজাপুৰত, চাৰমিনাৰ হায়দৰাবাদত।"),
 13: ("Tulsidas wrote the Ramcharitmanas, not Kabir.|ৰামচৰিতমানস তুলসীদাসৰ, কবীৰৰ নহয়।", "The Dhubri gurdwara marks Guru Tegh Bahadur, not Guru Nanak.|ধুবুৰীৰ গুৰুদ্বাৰা গুৰু তেগ বাহাদুৰৰ, গুৰু নানকৰ নহয়।"),
 14: ("Babur is first Mughal. Sher Shah is not a Mughal at all.|বাবৰ প্ৰথম মোগল। শ্বেৰ শ্বাহ মোগলেই নহয়।", "Khanwa came a year after Panipat.|পানিপথৰ এবছৰ পিছত খানুৱা।"),
 15: ("Din-i-Ilahi is Akbar's, never Aurangzeb's.|দীন-ই-ইলাহী আকবৰৰ, ঔৰংগজেবৰ নহয়।", "Akbar abolished the jizya. Aurangzeb restored it.|আকবৰে জিজিয়া বিলোপ কৰিছিল। ঔৰংগজেবে পুনৰ আনিছিল।"),
 16: ("Roe came to Jahangir, Mildenhall to Akbar.|ৰ' জাহাংগীৰৰ ওচৰলৈ, মিলডেনহল আকবৰৰ ওচৰলৈ।", "Saraighat is 1671, under Aurangzeb, and a Mughal defeat.|শৰাইঘাট ১৬৭১, ঔৰংগজেবৰ দিনত, মোগলৰ পৰাজয়।"),
 17: ("Tipu is Hyder Ali's son, and Sher-e-Mysore is Tipu.|টিপু হায়দৰ আলীৰ পুত্ৰ, শ্বেৰ-ই-মহীশূৰ টিপু।", "Third Panipat was Marathas against Durrani, not the British.|তৃতীয় পানিপথ মাৰাঠা বনাম দুৰানী, ব্ৰিটিছ নহয়।"),
 18: ("Plassey is Clive. Buxar is Munro.|পলাশী ক্লাইভ। বক্সাৰ মুনৰো।", "Mir Jafar is Plassey. Mir Qasim is Buxar.|মীৰ জাফৰ পলাশী। মীৰ কাছিম বক্সাৰ।"),
 19: ("First Governor-General of India is Bentinck, not Hastings.|ভাৰতৰ প্ৰথম গৱৰ্ণৰ জেনেৰেল বেণ্টিংক, হেষ্টিংছ নহয়।", "Macaulay was Law Member, not Governor-General.|মেকলে আইন সদস্য, গৱৰ্ণৰ জেনেৰেল নহয়।"),
 20: ("Brahmo Samaj is Calcutta. Arya Samaj is Bombay.|ব্ৰাহ্ম সমাজ কলিকতা। আৰ্য সমাজ বোম্বে।", "Vivekananda founded the Mission. Ramakrishna was his guru.|বিবেকানন্দই মিছন গঢ়িছিল। ৰামকৃষ্ণ তেওঁৰ গুৰু।"),
 21: ("Mangal Pandey is Barrackpore. The rising began at Meerut.|মংগল পাণ্ডে বেৰাকপুৰ। বিদ্ৰোহ মীৰাটত আৰম্ভ।", "Nana Sahib is Kanpur. Begum Hazrat Mahal is Lucknow.|নানা চাহেব কানপুৰ। বেগম হজৰত মহল লক্ষ্ণৌ।"),
 22: ("Nil Darpan is Dinabandhu Mitra, not Premchand.|নীলদৰ্পণ দীনবন্ধু মিত্ৰৰ, প্ৰেমচান্দৰ নহয়।", "Santhals come before Indigo: 1855, then 1859.|চাঁওতাল নীলৰ আগত: ১৮৫৫, তাৰ পিছত ১৮৫৯।"),
 23: ("Hume organised. Bonnerjee presided.|হিউমে আয়োজন কৰিছিল। বন্দ্যোপাধ্যায় সভাপতি।", "Swaraj is Calcutta 1906. The split is Surat 1907.|স্বৰাজ কলিকতা ১৯০৬। বিভাজন চুৰাট ১৯০৭।"),
 24: ("Partition is 1905. Its annulment and the capital's move are 1911.|বিভাজন ১৯০৫। বাতিল আৰু ৰাজধানী সলনি ১৯১১।", "The League began at Dacca, the Mahasabha at Haridwar.|লীগ ঢাকাত, মহাসভা হৰিদ্বাৰত।"),
 25: ("Tagore gave up his knighthood, not the Nobel.|ঠাকুৰে নাইটহুড ত্যাগ কৰিছিল, ন'বেল নহয়।", "Partition of Bengal did not happen in 1919.|বংগ বিভাজন ১৯১৯ত হোৱা নাছিল।"),
 26: ("Gandhi's first Indian satyagraha is Champaran, not Dandi.|গান্ধীৰ প্ৰথম ভাৰতীয় সত্যাগ্ৰহ চম্পাৰণ, ডাণ্ডী নহয়।", "Swaraj Party is Das and Motilal Nehru, 1923.|স্বৰাজ দল দাস আৰু মতিলাল নেহৰু, ১৯২৩।"),
 27: ("Labour Swaraj is not the Swaraj Party: 1925 against 1923.|লেবাৰ স্বৰাজ আৰু স্বৰাজ দল বেলেগ: ১৯২৫ আৰু ১৯২৩।", "Saunders was shot by mistake for Scott.|স্কটৰ ভুলত চণ্ডাৰ্ছক গুলীওৱা হৈছিল।"),
 28: ("12 March is the start. 6 April is the salt.|১২ মাৰ্চ আৰম্ভণি। ৬ এপ্ৰিল লৱণ।", "Dandi belongs to Civil Disobedience, not Non-Cooperation.|ডাণ্ডী আইন অমান্যৰ, অসহযোগৰ নহয়।"),
 29: ("Gowalia Tank and August Kranti Maidan are the same place.|গোৱালিয়া টেংক আৰু আগষ্ট ক্ৰান্তি ময়দান একে ঠাই।", "Ahmednagar Fort, not Yerwada, is the Discovery of India.|ডিছকভাৰী অৱ ইণ্ডিয়া আহমেদনগৰ দুৰ্গত, য়েৰৱদাত নহয়।"),
 30: ("Forward Bloc is a party. The INA is an army.|ফৰৱাৰ্ড ব্লক দল। আজাদ হিন্দ ফৌজ সৈন্যবাহিনী।", "Mohan Singh formed the first INA, not Bose.|প্ৰথম ফৌজ মোহন সিঙে গঢ়িছিল, বসুৱে নহয়।"),
 31: ("Wavell is 1945. Cabinet Mission is 1946. Mountbatten is 1947.|ৱেভেল ১৯৪৫। কেবিনেট অভিযান ১৯৪৬। মাউণ্টবেটেন ১৯৪৭।", "The Navy Mutiny began at Bombay, HMIS Talwar.|নৌ বিদ্ৰোহ বোম্বেৰ HMIS তলৱাৰত আৰম্ভ।"),
 32: ("In APSC's list Operation Vijay is Goa 1961, not Kargil 1999.|APSCৰ তালিকাত অপাৰেচন বিজয় ১৯৬১ৰ গোৱা, ১৯৯৯ৰ কাৰ্গিল নহয়।", "Patel's Bharat Ratna is 1991, not 1989.|পেটেলৰ ভাৰতৰত্ন ১৯৯১, ১৯৮৯ নহয়।"),
}
# from lesson, unit, story title, to lesson, unit number, note
LINKS = [
 (7, "u1", "King of kings", 5, 1, "Do not confuse him with Chandragupta Maurya.|চন্দ্ৰগুপ্ত মৌৰ্যৰ সৈতে পাহৰি নাযাবা।"),
 (8, "u3", "One man, many spellings", 7, 3, "Faxian came two centuries earlier, under the Guptas.|ফা-হিয়েন দুশতিকা আগতে গুপ্তৰ দিনত আহিছিল।"),
 (11, "u3", "A capital on the move", 8, 3, "Add Ibn Battuta to your table of travellers.|পৰ্যটকৰ তালিকাত ইবন বতুতাক যোগ কৰা।"),
 (14, "u1", "Twelve thousand against many more", 11, 1, "This battle ended the Lodi line.|এই যুদ্ধে লোদী বংশৰ অন্ত পেলাইছিল।"),
 (17, "u2", "January 1761", 15, 1, "This is the third of the three Panipats.|এয়া তিনিটা পানিপথৰ তৃতীয়টো।"),
 (21, "u1", "Older anger", 19, 4, "Lapse and Awadh fed the anger of 1857.|স্বত্ববিলোপ আৰু অযোধ্যাই ১৮৫৭ৰ ক্ষোভ বঢ়াইছিল।"),
 (26, "u3", "Chauri Chaura", 25, 2, "Jallianwala Bagh helped turn Gandhi against British rule.|জালিয়ানৱালা বাগে গান্ধীক ব্ৰিটিছ শাসনৰ বিৰুদ্ধে নিয়াত ভূমিকা লৈছিল।"),
 (28, "u1", "A pledge at Lahore", 27, 3, "The Lahore goal closed the 1920s.|লাহোৰৰ লক্ষ্যই বিশৰ দশক সামৰিছিল।"),
 (29, "u4", "Three mass movements", 28, 2, "Compare the Salt March with Quit India.|লৱণ যাত্ৰা আৰু ভাৰত ত্যাগ তুলনা কৰা।"),
 (32, "u3", "Twenty-four spokes", 5, 5, "The wheel comes from the Sarnath capital.|চক্ৰটো সাৰনাথৰ শীৰ্ষৰ পৰা লোৱা।"),
]

course = json.loads((ROOT / "content/courses/indian-history.json").read_text(encoding="utf-8"))
ids = {k["n"]: k["lesson"] for k in course["kings"]}
lessons = {n: json.loads((ROOT / f"content/lessons/{i}.json").read_text(encoding="utf-8")) for n, i in ids.items()}
unit = lambda n, u: next(x for x in lessons[n]["units"] if x["id"] == u)
def card(n, u, title):
    return next(s for s in unit(n, u)["steps"] if s["type"] == "story" and s["title"]["en"] == title)

for n, u, title, layout, items in DIAGRAMS:
    s = card(n, u, title)
    assert not s.get("map"), (n, title)
    s["diagram"] = {"layout": layout, "items": many(items)}
for n, u, title, trick in TRICKS:
    card(n, u, title)["text"].append(t(trick))
for frm, u, title, to, un, note in LINKS:
    s = card(frm, u, title)
    if s.get("link"):
        continue
    target = lessons[to]["units"][un - 1]
    s["link"] = {"lessonId": ids[to], "lesson": to, "unitNo": un, "unitTitle": target["title"], "note": t(note)}
for n, u, at, stem, options, answer, why in GUESS:
    steps = unit(n, u)["steps"]
    assert steps[at]["type"] == "story", (n, u, at)
    before = t(stem)
    last = stem.split("|")[0].rstrip()[-1]
    after = {"en": "Pick one.", "as": "এটা বাছি লোৱা।"} if last == "?" else {"en": ".", "as": "।"}
    steps.insert(at, {"id": f"ih-{n:02d}.{u}.g1", "type": "inline", "guess": True, "before": before, "after": after, "options": many(options), "answer": answer, "why": t(why)})
for n, lines in TRAPS.items():
    lessons[n]["guide"]["extra_stories"] = [{"id": f"ih-{n:02d}.guide.traps", "type": "story", "art": "seal", "title": {"en": "Exam traps", "as": "পৰীক্ষাৰ ফান্দ"}, "text": many(lines)}]

# Release. The authoring scripts rebuild the course as a draft, so this pass runs last.
course.pop("draft", None)
course["eyebrow"] = {"en": "Indian History", "as": "ভাৰতৰ ইতিহাস"}
units = sum(len(L["units"]) for L in lessons.values())
AS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
course["subtitle"] = {"en": f"{len(lessons)} lessons · {units} units · {len(course['eras'])} checkpoints",
                      "as": f"{len(lessons)}টা পাঠ · {units}টা অধ্যায় · {len(course['eras'])}টা পৰীক্ষা".translate(AS)}
for k in course["kings"]:
    k["reign"] = lessons[k["n"]]["reign"]

ERA = {k["n"]: e["id"].removeprefix("ih-") for e in course["eras"] for k in course["kings"] if e["from"] <= k["n"] <= e["to"]}
for k in course["kings"]:
    k["face"] = f"indian-history/{ERA[k['n']]}.webp"
    lessons[k["n"]]["portrait"] = k["face"]
(ROOT / "content/courses/indian-history.json").write_text(json.dumps(course, ensure_ascii=False, indent=1), encoding="utf-8")
path = ROOT / "content/catalog.json"
catalog = json.loads(path.read_text(encoding="utf-8"))
subject = next(x for x in catalog["subjects"] if x["id"] == "indian-history")
subject["courses"] = [{"course": "indian-history"}]
subject["intro"] = {"en": "Work through the sections in order, then pass each section's checkpoint.", "as": "খণ্ডবোৰ ক্ৰমে পঢ়া, তাৰ পিছত প্ৰতিটো খণ্ডৰ পৰীক্ষাত উত্তীৰ্ণ হোৱা।"}
path.write_text(json.dumps(catalog, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
path = ROOT / "content/entities.json"
entities = json.loads(path.read_text(encoding="utf-8"))
for n, L in lessons.items():
    for name in set(re.findall(r"\[\[([a-z0-9-]+)", json.dumps(L, ensure_ascii=False))):
        if name in entities and ids[n] not in entities[name].setdefault("lessons", []):
            entities[name]["lessons"].append(ids[n])
path.write_text(json.dumps(entities, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for n, L in lessons.items():
    (ROOT / f"content/lessons/{ids[n]}.json").write_text(json.dumps(L, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"polished: {len(GUESS)} predictions, {len(DIAGRAMS)} diagrams, {len(TRICKS)} tricks, {len(TRAPS)} trap cards, {len(LINKS)} links")
