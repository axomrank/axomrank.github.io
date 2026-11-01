# Which old steps make up each compact lesson. Learned refs are lesson/unit/index.
EYEBROW = {"en": "The Ahom Kingdom", "as": "আহোম ৰাজ্য"}
def B(en, as_): return {"en": en, "as": as_}

LESSONS = [
 {"no": 1, "id": "ahom-01-sukaphaa", "title": B("Sukaphaa founds a kingdom", "চুকাফাৰ ৰাজ্য স্থাপন"), "reign": B("1228–1281 · Sukaphaa and Suteuphaa", "১২২৮–১২৮১ · চুকাফা আৰু চুতেউফা"),
  "portrait": "sukaphaa/sukaphaa-portrait.webp", "map_from": "sukaphaa",
  "units": [
   {"title": B("The journey", "যাত্ৰা"), "learned": ["sukaphaa/u1/0", "sukaphaa/u1/1", "sukaphaa/u1/2", "sukaphaa/u1/3"],
    "steps": ["suk.u1.01", "suk.u1.02", "suk.u1.03", "suk.u1.04", "suk.u1.05", "suk.u1.07", "suk.u1.08", "suk.u1.09"]},
   {"title": B("Friends, not enemies", "শত্ৰু নহয়, বন্ধু"), "learned": ["sukaphaa/u2/0", "sukaphaa/u3/0", "sukaphaa/u3/1", "sukaphaa/u3/2"],
    "steps": ["suk.u2.01", "suk.u2.02", "suk.d1", "suk.u3.01", "suk.u3.02", "suk.u3.04", "suk.u3.05", "suk.u3.06", "suk.u3.07"]},
   {"title": B("Charaideo and the Gohains", "চৰাইদেউ আৰু গোহাঁইসকল"), "learned": ["sukaphaa/u5/0", "sukaphaa/u4/0", "sukaphaa/u4/2", "sukaphaa/u4/3"],
    "steps": ["suk.u5.01", "suk.u5.02", "suk.u5.04", "suk.u4.01", "suk.u4.02", "suk.u4.03", "suk.u4.04", "suk.u4.06"]},
   {"title": B("The Dikhou border", "দিখৌৰ সীমা"), "learned": ["sukaphaa/u5/2", "suteuphaa/u1/0", "suteuphaa/u3/2", "suteuphaa/u4/1"],
    "steps": ["suk.u5.05", "sut.u2.01", "sut.u2.03", "sut.u2.07", "sut.u3.01", "sut.u3.02", "sut.u2.05", "sut.u3.06", "sut.u3.07"]},
   {"title": B("Moidams and Asom Divas", "মৈদাম আৰু অসম দিৱস"), "learned": ["sukaphaa/u6/0", "sukaphaa/u6/1", "sukaphaa/u6/2", "sukaphaa/u6/3"],
    "steps": ["suk.u6.01", "suk.u6.02", "suk.u6.03", "suk.u6.04", "suk.u6.05", "suk.u6.06", "suk.u6.07", "suk.u5.06"]},
  ],
  "test": ["suk.test.01", "suk.test.02", "suk.test.03", "suk.test.04", "suk.test.06", "suk.test.08", "suk.test.09", "sut.test.03", "sut.test.06", "sut.test.01"]},

 {"no": 2, "id": "ahom-02-early-kings", "title": B("Two centuries of early kings", "আদি ৰজাসকলৰ দুশ বছৰ"), "reign": B("1281–1497 · eleven reigns", "১২৮১–১৪৯৭ · এঘাৰটা ৰাজত্ব"),
  "portrait": "sudangphaa/sudangphaa-portrait.webp", "map_from": "sudangphaa",
  "units": [
   {"title": B("The seven houses", "সাতঘৰীয়া"), "learned": ["subinphaa/u1/0", "subinphaa/u2/0", "subinphaa/u3/1", "subinphaa/u3/2"],
    "steps": ["sbn.u1.01", "sbn.u1.10", "sbn.u1.03", "sbn2.u2.04", "sbn2.u2.05", "sbn.u1.05", "sbn.u1.06", "sbn.u1.07", "sbn3.u2.08"]},
   {"title": B("A Kamata bride", "কামতাৰ কইনা"), "learned": ["sukhaangphaa/u1/0", "sukhaangphaa/u2/0", "sukhaangphaa/u2/2", "sukhaangphaa/u3/2"],
    "steps": ["skg.u1.01", "skg.u1.04", "skg.u1.06", "skg.u1.07", "skg.u2.02", "skg.u2.05", "skg.u2.06"]},
   {"title": B("Murder on the Safrai", "চাফ্ৰাইত হত্যা"), "learned": ["sutuphaa/u2/1", "sutuphaa/u2/3", "sutuphaa/u3/2", "sutuphaa/u3/3"],
    "steps": ["stu.u1.02", "stu.u1.03", "stu.d1", "stu.u1.04", "stu.u1.05", "stu3.u2.01", "stu2.u3.03", "stu.u1.09", "stu2.u3.06"]},
   {"title": B("The raft-born prince", "ভুৰত ভাহি অহা কোঁৱৰ"), "learned": ["tyao-khamti/u1/0", "tyao-khamti/u2/3", "sudangphaa/u1/0", "sudangphaa/u1/3"],
    "steps": ["tyk.u1.01", "tyk.u1.05", "tyk3.u2.02", "sdg.u1.01", "sdg.u1.08", "sdg.u1.05", "sdg3.u1.02"]},
   {"title": B("Bamuni Konwar and the Patkai", "বামুণী কোঁৱৰ আৰু পাটকাই"), "learned": ["sudangphaa/u2/0", "sudangphaa/u2/1", "sudangphaa/u2/3", "sudangphaa/u4/2"],
    "steps": ["sdg.u2.01", "sdg3.u2.01", "sdg.u2.07", "sdg.u2.05", "sdg3.u2.03", "sdg.u4.04", "sdg.u4.07", "sdg.u4.06", "sdg.u2.06"]},
   {"title": B("Long reigns, hard neighbours", "দীঘলীয়া ৰাজত্ব, কঠিন চুবুৰীয়া"), "learned": ["susenphaa/u1/1", "susenphaa/u4/0", "suhenphaa/u2/1", "supimphaa/u3/0"],
    "steps": ["ssn.u1.01", "spk2.u2.05", "ssn2.u4.01", "ssn3.u4.03", "shn.u1.04", "shn.u1.05", "shn2.u2.06", "spm2.u3.01", "spm3.u3.01"]},
  ],
  "test": ["sbn2.test.07", "skg.test.01", "skg2.test.09", "stu.test.01", "stu.test.04", "tyk.test.03", "sdg.test.01", "sdg.test.07", "sdg.test.04", "ssn.test.06", "shn.test.01"]},

 {"no": 3, "id": "ahom-03-suhungmung", "title": B("Suhungmung, the Dihingia Raja", "দিহিঙীয়া ৰজা চুহুংমুং"), "reign": B("1497–1539", "১৪৯৭–১৫৩৯"),
  "portrait": "suhungmung/suhungmung-portrait.webp", "map_from": "suhungmung",
  "units": [
   {"title": B("Swarganarayan", "স্বৰ্গনাৰায়ণ"), "learned": ["suhungmung/u1/1", "suhungmung/u1/3", "suhungmung/u2/1", "suhungmung/u2/2"],
    "steps": ["shm.u1.01", "shm3.u1.01", "shm.u1.04", "shm.u1.05", "shm.u1.06", "shm.u1.07", "shm.u2.01", "shm.u2.04", "shm.u2.05"]},
   {"title": B("The fall of the Chutias", "চুতীয়াৰ পতন"), "learned": ["suhungmung/u3/0", "suhungmung/u3/1", "suhungmung/u3/2", "suhungmung/u3/3"],
    "steps": ["shm.u3.01", "shm.g1", "shm.u3.03", "shm.u3.04", "shm.u3.05", "shm.u3.06", "shm.u3.07", "shm.u3.08"]},
   {"title": B("The third Gohain and Dimapur", "তৃতীয় গোহাঁই আৰু ডিমাপুৰ"), "learned": ["suhungmung/u4/1", "suhungmung/u4/2", "suhungmung/u5/1", "suhungmung/u5/2"],
    "steps": ["shm.u4.01", "shm.u4.03", "shm.u4.07", "shm.u4.08", "shm.u5.01", "shm.u5.03", "shm.u5.04", "shm.u5.05", "shm3.u5.01"]},
   {"title": B("Turbak", "তুৰবক"), "learned": ["suhungmung/u6/0", "suhungmung/u6/1", "suhungmung/u6/2", "suhungmung/u6/3"],
    "steps": ["shm.u6.01", "shm.d1", "shm.u6.03", "shm.u6.04", "shm.u6.05", "shm.u6.06", "shm.u6.07", "shm.u6.08"]},
   {"title": B("Murder in the night", "ৰাতিৰ হত্যা"), "learned": ["suhungmung/u7/0", "suhungmung/u7/1", "suhungmung/u7/2", "suhungmung/u7/3"],
    "steps": ["shm.u7.01", "shm.u7.02", "shm.u7.06", "shm.u7.07", "shm.u7.08", "shm4.u7.02", "shm4.u7.03"]},
  ],
  "test": ["shm.test.01", "shm.test.02", "shm.test.03", "shm.test.04", "shm.test.05", "shm3.test.01", "shm.test.07", "shm3.test.02", "shm.test.09", "shm.test.10"]},

 {"no": 4, "id": "ahom-04-koch-wars", "title": B("Garhgaon and the Koch wars", "গড়গাঁও আৰু কোচ যুদ্ধ"), "reign": B("1539–1603 · Suklenmung and Sukhaamphaa", "১৫৩৯–১৬০৩ · চুক্লেনমুং আৰু চুখাম্ফা"),
  "portrait": "suklenmung/suklenmung-portrait.webp", "map_from": "sukhaamphaa",
  "units": [
   {"title": B("Garhgaon and the first coins", "গড়গাঁও আৰু প্ৰথম মুদ্ৰা"), "learned": ["suklenmung/u1/0", "suklenmung/u1/1", "suklenmung/u1/2", "suklenmung/u1/3"],
    "steps": ["skl.u1.01", "skl.u1.02", "skl.u1.05", "skl3.u1.02", "skl.u1.07", "skl3.u1.03", "skl.u1.06", "skl.u1.09"]},
   {"title": B("Chilarai and Sankardev", "চিলাৰায় আৰু শংকৰদেৱ"), "learned": ["suklenmung/u2/1", "suklenmung/u2/2", "suklenmung/u3/0", "suklenmung/u3/3"],
    "steps": ["skl.u2.01", "skl.u2.02", "skl.u2.03", "skl.u2.06", "skl.u2.05", "skl.u3.01", "skl.u3.03", "skl.u3.04", "skl.u3.08"]},
   {"title": B("The Khora Roja and Majuli", "খোৰা ৰজা আৰু মাজুলী"), "learned": ["sukhaamphaa/u1/1", "sukhaamphaa/u1/3", "sukhaamphaa/u2/2", "sukhaamphaa/u3/2"],
    "steps": ["skp.u1.01", "skp3.u1.01", "skp.u2.01", "skp.u2.02", "skp.u2.03", "skp.u2.06", "skp.u3.01", "skp.u3.03", "skp.u3.04", "skp.u3.08"]},
  ],
  "test": ["skl3.test.01", "skl.test.02", "skl.test.03", "skl.test.04", "skl.test.07", "skp.test.01", "skp.test.03", "skp.test.04", "skp.test.07", "skp.test.05"]},
]
