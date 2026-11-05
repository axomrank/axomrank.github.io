#!/usr/bin/env python3
"""Indian History, Phase 0 and 1: hand PYQ map and the hidden course skeleton.

Run from the repository root:  python3 docs/authoring/indian_history_outline.py
Writes content/courses/indian-history.json, content/questions/indian-history.json,
content/media/indian-history/era-tile.webp and docs/research/indian-history-pyq-map.json,
then prints the tables used in docs/INDIAN-HISTORY-COURSE.md.
Lesson ids are reserved here and become permanent once published.
"""
import collections, csv, json, os
from PIL import Image, ImageDraw

PYQ = "/home/angsuman/extra_spac/PYQ/questions.csv"

SECTIONS = [
    ("ih-beginnings", 1, 3, "Beginnings", "আৰম্ভণি"),
    ("ih-empires", 4, 8, "Empires of the north", "উত্তৰৰ সাম্ৰাজ্য"),
    ("ih-wider", 9, 10, "South, Kashmir and learning", "দক্ষিণ, কাশ্মীৰ আৰু জ্ঞানচৰ্চা"),
    ("ih-sultans", 11, 13, "Sultans, Deccan and devotion", "ছুলতান, দাক্ষিণাত্য আৰু ভক্তি"),
    ("ih-mughals", 14, 17, "The Mughal age", "মোগল যুগ"),
    ("ih-company", 18, 22, "Company rule", "কোম্পানীৰ শাসন"),
    ("ih-national", 23, 27, "The national movement", "ৰাষ্ট্ৰীয় আন্দোলন"),
    ("ih-freedom", 28, 32, "Mass struggle and freedom", "গণ সংগ্ৰাম আৰু স্বাধীনতা"),
]

# n, slug, English, Assamese (new, pending review), period, tier, units, content
L = [
 (1, "indus-cities", "The Indus cities", "সিন্ধু উপত্যকাৰ নগৰ", "Indus", "B", 4, "Harappa, Mohenjo-daro and Lothal; seals and the unicorn; site and finding pairs"),
 (2, "vedic-age", "The Vedic age", "বৈদিক যুগ", "Vedic", "C", 3, "The four Vedas, the Rigveda first; the Saraswati question; early and later Vedic life"),
 (3, "buddha-and-mahavira", "Buddha and Mahavira", "বুদ্ধ আৰু মহাবীৰ", "6th–5th c. BCE", "B", 4, "Four places of the Buddha's life; Tirthankaras and Mahavira as the 24th; contrast of the two teachings"),
 (4, "alexander-and-magadha", "Magadha and Alexander", "মগধ আৰু আলেকজেণ্ডাৰ", "to 326 BCE", "C", 3, "Mahajanapadas, the rise of Magadha, Macedonia, 326 BCE and Porus on the Jhelum"),
 (5, "mauryas", "The Mauryas", "মৌৰ্য সকল", "Maurya", "B", 5, "Chandragupta and Chanakya, the Arthashastra, Megasthenes, Ashoka, Kalinga and the edicts"),
 (6, "after-the-mauryas", "After the Mauryas", "মৌৰ্যৰ পিছত", "Post-Maurya", "C", 3, "Kushans and Kanishka, Gandhara and Mathura, Satavahanas, Sangam, the Begram ivories"),
 (7, "guptas", "The Guptas", "গুপ্ত সকল", "Gupta", "B", 4, "Samudragupta and Harisena's Allahabad praise, Chandragupta II, Faxian, Kalidasa's plays"),
 (8, "harsha", "Harsha and Xuanzang", "হৰ্ষ আৰু হিউৱেন চাঙ", "7th c.", "C", 3, "Prabhakaravardhana's son, Banabhatta, Banskhera, Xuanzang; link to Bhaskaravarman of Kamarupa"),
 (9, "south-and-kashmir", "Cholas, Deccan and Kashmir", "চোল, দাক্ষিণাত্য আৰু কাশ্মীৰ", "6th–13th c.", "C", 3, "Pallavas and Chalukyas, the Chola reach into Southeast Asia, Lalitaditya, Kalhana's Rajatarangini"),
 (10, "learning-and-art", "Knowledge and stone", "জ্ঞান আৰু শিলৰ কলা", "Ancient", "B", 4, "Charaka, Sushruta, Aryabhata and the zero question, Nalanda, Ajanta, Elephanta, Khajuraho"),
 (11, "delhi-sultanate", "The Delhi Sultanate", "দিল্লী ছুলতানী", "1206–1526", "B", 4, "Five dynasties in order, Iltutmish, Razia, Alauddin, Tughluq and Ibn Battuta; link to raids on Kamarupa"),
 (12, "vijayanagara-and-deccan", "Vijayanagara and the Deccan", "বিজয়নগৰ আৰু দাক্ষিণাত্য", "1336–1600s", "C", 3, "Harihara and Bukka, Krishnadeva Raya, Bahmani successors, Gol Gumbaz and Charminar"),
 (13, "bhakti-and-sufi", "Bhakti, Sufis and Sikh Gurus", "ভক্তি, চুফী আৰু শিখ গুৰু", "Medieval", "C", 3, "Kabir, Nanak, Tulsidas, Chishti Sufis, Guru Tegh Bahadur at Dhubri; link to Sankardev"),
 (14, "babur-and-sher-shah", "Babur and Sher Shah", "বাবৰ আৰু শ্বেৰ শ্বাহ", "1526–1556", "B", 4, "Panipat 1526, Humayun, Sher Shah, the Grand Trunk Road and the rupee"),
 (15, "akbar", "Akbar", "আকবৰ", "1556–1605", "B", 4, "Panipat 1556 and Hemu, mansabdari, Din-i-Ilahi, Abu'l Fazl, Mildenhall at court"),
 (16, "jahangir-to-aurangzeb", "Jahangir to Aurangzeb", "জাহাংগীৰৰ পৰা ঔৰংগজেবলৈ", "1605–1707", "C", 3, "Hawkins and Roe, Shah Jahan's buildings, Aurangzeb and the Deccan; link to Mir Jumla and Saraighat"),
 (17, "marathas-and-mysore", "Marathas and Mysore", "মাৰাঠা আৰু মহীশূৰ", "1674–1799", "C", 3, "Shivaji, Panipat 1761, Hyder Ali and Tipu Sultan"),
 (18, "europeans-and-plassey", "Plassey and Buxar", "পলাশী আৰু বক্সাৰ", "1498–1765", "B", 4, "Vasco da Gama, the European companies, Plassey 1757, Buxar 1764, Diwani 1765"),
 (19, "governors-general", "The Governors-General", "গৱৰ্ণৰ জেনেৰেল সকল", "1773–1856", "B", 4, "Hastings, Cornwallis, Bentinck as first Governor-General of India, Dalhousie, Macaulay's Minute; link to the Regulating Act lesson"),
 (20, "reformers", "Reformers", "সমাজ সংস্কাৰক", "19th c.", "C", 3, "Ram Mohan Roy, Vidyasagar, Arya Samaj, Vivekananda; link to Anandaram Dhekial Phukan"),
 (21, "revolt-of-1857", "The Revolt of 1857", "১৮৫৭ৰ বিদ্ৰোহ", "1857–1858", "B", 4, "Causes, Mangal Pandey, leaders by centre, Lakshmibai, 1858 and the Viceroy; link to Maniram Dewan"),
 (22, "indigo-and-education", "Indigo, press and schools", "নীল, প্ৰেছ আৰু বিদ্যালয়", "1835–1919", "C", 3, "Indigo Revolt and Nil Darpan, the education chain from Macaulay to Sadler, peasant risings"),
 (23, "early-congress", "The early Congress", "প্ৰাৰম্ভিক কংগ্ৰেছ", "1885–1905", "B", 4, "1885, moderates, Naoroji and the drain, Calcutta 1906 and Swaraj"),
 (24, "swadeshi-and-home-rule", "Swadeshi to Lucknow", "স্বদেশীৰ পৰা লক্ষ্ণৌলৈ", "1905–1916", "B", 4, "Partition of Bengal, Tilak, Surat 1907, League, Hindu Mahasabha, Delhi 1911, Lucknow 1916; link to Swadeshi in Assam"),
 (25, "year-1919", "The year 1919", "১৯১৯ চন", "1919", "B", 4, "Rowlatt Act, Jallianwala Bagh, Tagore's knighthood, Montagu-Chelmsford; what did not happen in 1919"),
 (26, "gandhi-and-noncooperation", "Gandhi and Non-Cooperation", "গান্ধী আৰু অসহযোগ", "1915–1923", "B", 4, "South Africa, Champaran, Khilafat, Non-Cooperation, Chauri Chaura, the Swaraj Party; link to Gandhi in Assam"),
 (27, "simon-and-revolutionaries", "Simon and the revolutionaries", "চাইমন আৰু বিপ্লৱী সকল", "1925–1931", "C", 3, "Labour Swaraj Party, Simon Commission, Bhagat Singh, Bardoli, Lahore 1929"),
 (28, "salt-march", "The Salt March", "লৱণ যাত্ৰা", "1930–1932", "B", 4, "Dandi, Civil Disobedience, Gandhi-Irwin Pact, Round Tables; link to Civil Disobedience in Assam"),
 (29, "quit-india", "Quit India", "ভাৰত ত্যাগ", "1942", "B", 4, "Cripps, August Kranti Maidan, Do or Die, Discovery of India in Ahmednagar; link to Kanaklata and Gohpur"),
 (30, "bose-and-ina", "Bose and the INA", "বসু আৰু আজাদ হিন্দ ফৌজ", "1939–1945", "C", 3, "Forward Bloc, Azad Hind, Rangoon, the Red Fort trials; link to Kohima and the war in the North-East"),
 (31, "road-to-1947", "The road to 1947", "১৯৪৭লৈ বাট", "1945–1947", "B", 4, "Wavell Plan, Navy Mutiny, Cabinet Mission, Mountbatten Plan, Partition; link to Sylhet and Grouping"),
 (32, "building-the-republic", "Building the nation", "ৰাষ্ট্ৰ গঢ়", "1947–1971", "B", 4, "First cabinet, Patel and integration, the flag, 1971 and Bangladesh, the order of later operations"),
]

# Hand classification. Every id below was read. Tagged History items, then items
# the export files under other subjects.
M = {
 1: "ADRE-2022-G3-P4-Degree-Q020 ADRE-2024-G3-P3-HSSLC-Q042 APSC-CCE-Prelims-2025-GS-I-Q026",
 2: "ADRE-2024-G3-P3-HSSLC-Q041 APSC-CCE-Prelims-2025-GS-I-Q024 Assam-Police-SI-2025-CWT-P1-SetA-Q098",
 3: "ADRE-2022-G3-P4-Degree-Q001 APSC-CCE-Prelims-2023-GS-I-Q011 APSC-CCE-Prelims-2025-GS-I-Q033 Assam-Police-SI-2025-CWT-P1-SetA-Q072",
 4: "ADRE-2024-G4-P1-HSLC-Q015 Assam-Police-SI-2025-CWT-P1-SetA-Q094 DME-2025-G3-NonTechnical-Q014",
 5: "ADRE-2022-G4-P1-HSLC-Q044 ADRE-2024-G3-P4-Degree-Q091 ADRE-2024-G4-P2-ClassVIII-Q042 ADRE-2024-G3-P5-Driver-Q025",
 6: "APSC-CCE-Prelims-2025-GS-I-Q021",
 7: "Assam-Police-SI-2025-CWT-P1-SetA-Q073 ADRE-2022-G3-P5-Driver-Q024 DME-2025-G3-NonTechnical-Q015",
 8: "ADRE-2022-G3-P3-HSSLC-Q037 APSC-CCE-Prelims-2025-GS-I-Q023 Assam-Police-SI-2025-CWT-P1-SetA-Q086",
 9: "ADRE-2024-G3-P4-Degree-Q028 ADRE-2024-G4-P1-HSLC-Q011 ADRE-2022-G3-P5-Driver-Q018",
 10: "ADRE-2022-G3-P5-Driver-Q028 ADRE-2024-G4-P2-ClassVIII-Q002 Assam-Police-SI-2025-CWT-P1-SetA-Q095 APSC-CCE-Prelims-2023-GS-I-Q007",
 11: "ADRE-2022-G4-P1-HSLC-Q045 ADRE-2024-G4-P1-HSLC-Q034",
 12: "ADRE-2022-G3-P3-HSSLC-Q023 ADRE-2024-G4-P1-HSLC-Q088 ADRE-2024-G4-P2-ClassVIII-Q062",
 13: "ADRE-2022-G3-P4-Degree-Q049 ADRE-2024-G4-P1-HSLC-Q065",
 14: "ADRE-2022-G4-P2-ClassVIII-Q039 ADRE-2022-G4-P2-ClassVIII-Q051 ADRE-2024-G4-P2-ClassVIII-Q043 DME-2025-G3-NonTechnical-Q016",
 15: "ADRE-2022-G3-P4-Degree-Q009 ADRE-2022-G3-P5-Driver-Q021 Assam-Police-SI-2025-CWT-P1-SetA-Q090",
 17: "ADRE-2024-G3-P3-HSSLC-Q003",
 18: "ADRE-2024-G3-P5-Driver-Q140 ADRE-2024-G3-P5-Driver-Q108",
 19: "ADRE-2022-G4-P2-ClassVIII-Q045 Assam-Police-SI-2025-CWT-P1-SetA-Q083",
 20: "DME-2025-G3-NonTechnical-Q018",
 21: "ADRE-2022-G3-P4-Degree-Q017 ADRE-2024-G3-P5-Driver-Q126",
 22: "APSC-CCE-Prelims-2023-GS-I-Q006 APSC-CCE-Prelims-2025-GS-I-Q031",
 23: "Assam-Police-SI-2025-CWT-P1-SetA-Q085",
 24: "ADRE-2022-G3-P4-Degree-Q008 ADRE-2022-G3-P4-Degree-Q015 APSC-CCE-Prelims-2025-GS-I-Q032 Assam-Police-SI-2025-CWT-P1-SetA-Q087 TET-2021-Paper-II-Q087",
 25: "ADRE-2022-G3-P3-HSSLC-Q032 ADRE-2022-G3-P4-Degree-Q012 ADRE-2022-G4-P2-ClassVIII-Q057 ADRE-2024-G3-P3-HSSLC-Q004 Assam-Police-SI-2025-CWT-P1-SetA-Q077",
 26: "ADRE-2022-G3-P3-HSSLC-Q021 ADRE-2024-G3-P5-Driver-Q135 ADRE-2024-G4-P2-ClassVIII-Q041 Assam-Police-SI-2025-CWT-P1-SetA-Q075",
 27: "Assam-Police-SI-2025-CWT-P1-SetA-Q079",
 28: "ADRE-2024-G4-P2-ClassVIII-Q034 Assam-Police-SI-2025-CWT-P1-SetA-Q097 DME-2025-G3-NonTechnical-Q019",
 29: "ADRE-2022-G3-P3-HSSLC-Q040 ADRE-2024-G4-P1-HSLC-Q074 ADRE-2022-G4-P2-ClassVIII-Q043",
 30: "Assam-Police-SI-2025-CWT-P1-SetA-Q100 DME-2025-G3-NonTechnical-Q017",
 31: "APSC-CCE-Prelims-2023-GS-I-Q008",
 32: "ADRE-2022-G4-P1-HSLC-Q046 ADRE-2024-G4-P2-ClassVIII-Q044 APSC-CCE-Prelims-2023-GS-I-Q080 APSC-CCE-Prelims-2025-GS-I-Q058 ADRE-2022-G3-P5-Driver-Q013 ADRE-2024-G4-P2-ClassVIII-Q012 ADRE-2022-G4-P2-ClassVIII-Q023",
}
ROUTED = {
 "assam-history": "ADRE-2022-G4-P1-HSLC-Q025 ADRE-2022-G4-P2-ClassVIII-Q013 ADRE-2024-G4-P2-ClassVIII-Q023 ADRE-2022-G3-P4-Degree-Q005",
 "world-history": "ADRE-2022-G3-P5-Driver-Q031 ADRE-2024-G3-P3-HSSLC-Q005 ADRE-2024-G3-P3-HSSLC-Q043 ADRE-2024-G3-P4-Degree-Q084",
}
# Answers not to teach from until the source page is read (see the course plan).
HOLD = {
 "APSC-CCE-Prelims-2025-GS-I-Q021": "Export key C reads 3rd to 1st century BCE; sources read give the 1st or 2nd century CE, and neighbouring keys in this export do not fit their pages. Taught as 1st to 2nd century CE. Check the printed options.",
 "APSC-CCE-Prelims-2025-GS-I-Q023": "Page read: options are Ashoka, Kanishka, Harshavardhana, Dharmapala. The export's key A does not fit; Banskhera belongs to Harshavardhana (C). Taught as Harsha.",
 "APSC-CCE-Prelims-2025-GS-I-Q024": "Page read: options are Ganga, Yamuna, Sutlej, Ghaggar-Hakra. The export's key C gives Sutlej; the expected answer is Ghaggar-Hakra (D). Taught as a disputed identification.",
 "ADRE-2024-G3-P3-HSSLC-Q003": "Key gives Tipu Sultan for 'Lion of Mysore'; he is usually styled Tiger of Mysore. Check before quoting the epithet.",
 "ADRE-2024-G4-P2-ClassVIII-Q002": "'Father of zero' is an exam label; the history of zero is not that simple. Teach the label as a label.",
}

rows = {r["id"]: r for r in csv.DictReader(open(PYQ, encoding="utf-8"))}
slug = {x[0]: f"ih-{x[0]:02d}-{x[1]}" for x in L}
qs, seen = [], set()
def add(q, **k):
    assert q in rows, q
    assert q not in seen, q
    seen.add(q)
    r = rows[q]
    qs.append({"pyq": q, "exam": r["exam"], "year": r["year"], **k, "tagged": r["subject"] + " > " + r["topic"],
               "question": " ".join(r["question"].split())[:150], **({"hold": HOLD[q]} if q in HOLD else {})})
for n, ids in M.items():
    for q in ids.split(): add(q, lesson=n, lessonId=slug[n])
for route, ids in ROUTED.items():
    for q in ids.split(): add(q, lesson=None, route=route)

# Every tagged Indian or World History record must be accounted for.
tagged = {i for i, r in rows.items() if r["subject"] == "History" and r["topic"] != "Assam History"}
missing = tagged - seen
assert not missing, missing

mapped = [q for q in qs if q["lesson"]]
sec = lambda n: next(s for s in SECTIONS if s[1] <= n <= s[2])
period = lambda n: "Ancient" if n <= 10 else "Medieval" if n <= 17 else "Modern"
out = {
 "status": "First-pass hand classification, 2026-11-05. Lesson numbers refer to docs/INDIAN-HISTORY-COURSE.md.",
 "method": "Every record the export tags History, other than Assam History, was read and mapped or routed. A keyword filter then swept subjects other than English, Mathematics, Reasoning, Commerce, Driving, Computer and Aptitude, and hits were read; General Awareness people, books and miscellany were read in full. Questions the sweep missed are not counted. Records filed under Assam History stay with that course, even where they touch national events.",
 "counts": {"records_in_export": len(rows), "mapped_to_lessons": len(mapped), "routed": len(qs) - len(mapped), "held_for_source_check": len(HOLD)},
 "questions": qs,
}
json.dump(out, open("docs/research/indian-history-pyq-map.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

os.makedirs("content/media/indian-history", exist_ok=True)
im = Image.new("RGB", (540, 540), (246, 238, 226)); d = ImageDraw.Draw(im)
d.ellipse((150, 150, 390, 390), outline=(176, 86, 52), width=14)
for a, b in (((270, 150), (270, 390)), ((150, 270), (390, 270))): d.line((a, b), fill=(176, 86, 52), width=8)
im.save("content/media/indian-history/era-tile.webp", quality=80)

units = sum(x[6] for x in L)
AS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
course = {
 "id": "indian-history", "order": 3, "draft": True,
 "title": {"en": "Indian History", "as": "ভাৰতৰ ইতিহাস"},
 "eyebrow": {"en": "Being written", "as": "লিখি থকা হৈছে"},
 "subtitle": {"en": f"Planned: {len(L)} lessons · {units} units · {len(SECTIONS)} checkpoints",
              "as": f"পৰিকল্পনা: {len(L)}টা পাঠ · {units}টা অধ্যায় · {len(SECTIONS)}টা পৰীক্ষা".translate(AS)},
 "tabs": ["lessons", "profile"], "bank": "content/questions/indian-history.json",
 "kings": [{"n": x[0], "id": slug[x[0]], "name": {"en": x[2], "as": x[3]}, "reign": x[4],
            "face": "indian-history/era-tile.webp", "tier": x[5], "lesson": slug[x[0]] if os.path.exists(f"content/lessons/{slug[x[0]]}.json") else None} for x in L],
 "eras": [{"id": s[0], "from": s[1], "to": s[2], "title": {"en": s[3], "as": s[4]}} for s in SECTIONS],
 "eraWord": {"en": "section", "as": "খণ্ড"},
}
json.dump(course, open("content/courses/indian-history.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

by = collections.Counter(q["lesson"] for q in mapped)
print("records", len(rows), "mapped", len(mapped), f"{len(mapped)/len(rows):.1%}", "routed", len(qs) - len(mapped), "| lessons", len(L), "units", units, f"hours@4min {units*4/60:.1f}")
print("by exam", collections.Counter(q["exam"] for q in mapped).most_common())
print("by year", sorted(collections.Counter((q["exam"], q["year"]) for q in mapped).items()))
print("by period", collections.Counter(period(q["lesson"]) for q in mapped).most_common(), "units", {p: sum(x[6] for x in L if period(x[0]) == p) for p in ("Ancient", "Medieval", "Modern")})
print("hidden outside History tag", sum(1 for q in mapped if not q["tagged"].startswith("History")))
for s in SECTIONS:
    ls = [x for x in L if s[1] <= x[0] <= s[2]]; c = sum(by[x[0]] for x in ls); u = sum(x[6] for x in ls)
    print(f"| {s[0]} {s[3]} | {c} | {c/len(mapped):.0%} | {u} | {u/units:.0%} | {len(ls)}")
print("lessons with no question:", [x[0] for x in L if not by[x[0]]])
print("TABLE")
for s in SECTIONS:
    print(f"\n### {s[3]} (lessons {s[1]}–{s[2]})\n\n| # | Lesson | Tier | Units | Asked | Content |\n|---|---|---|---:|---:|---|")
    for x in L:
        if s[1] <= x[0] <= s[2]: print(f"| {x[0]} | {x[2]} | {x[5]} | {x[6]} | {by[x[0]]} | {x[7]} |")
