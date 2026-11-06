# Course plan: Indian History

Status: live on Cloudflare Pages since 2026-11-05 (build 4a89d0483b): 32 lessons, unreviewed.
Assamese and historian review have not happened, and each lesson keeps its pending-review
note. GitHub Pages does not have it yet, because it builds from `main`. Lesson and step ids
are now permanent: add new steps only at the end of a unit, and migrate progress before any
change to ids.

## Goal

A learner preparing for ADRE, APSC CCE or Assam Police SI should be able to answer
what these papers ask about India's past and still recall it weeks later, in
English and Assamese, in about **8 hours** (32 lessons, 116 units, 8 checkpoints).

This is a medium-depth course: about half the size of the Constitution course. It
teaches what the papers ask, not the whole of Indian history. It follows
[LESSON-DESIGN.md](LESSON-DESIGN.md) and
[EXPERIENCE-REVAMP.md](EXPERIENCE-REVAMP.md).

## What exams ask

A hand classification of the 2,398 questions in `/home/angsuman/extra_spac/PYQ`
found **87 Indian history questions (3.6%)**: ADRE 52, Police SI 15, APSC 13, DME 6,
TET 1. Every id is in
[indian-history-pyq-map.json](research/indian-history-pyq-map.json). A further 8 were
routed elsewhere: 4 to Assam History and 4 to World History. 16 of the 87 are filed
outside History in the export (for example Elephanta under Art & Culture and Iron
Man of India under General Awareness), so the History tag alone undercounts.

| Section | Questions | Share | Units | Share |
|---|---:|---:|---:|---:|
| The national movement | 16 | 18% | 19 | 16% |
| Mass struggle and freedom | 16 | 18% | 19 | 16% |
| Empires of the north | 14 | 16% | 18 | 16% |
| Beginnings | 10 | 11% | 11 | 9% |
| Company rule | 9 | 10% | 18 | 16% |
| The Mughal age | 8 | 9% | 14 | 12% |
| South, Kashmir and learning | 7 | 8% | 7 | 6% |
| Sultans, Deccan and devotion | 7 | 8% | 10 | 9% |

By period: Modern 41 (47%), Ancient 31 (36%), Medieval 15 (17%); units 56, 36 and 24.
Company rule keeps more units than its share because the movement that follows
depends on it. Lesson 16 was never asked and stays at three units for continuity
and the Assam link; lesson 32, asked seven times, has four.

### What the papers are like

- **ADRE** asks one plain fact: who, where, when. Modern and Ancient lead, and the
  same facts return: Chanakya and the Arthashastra three times across papers (lesson
  5), the Grand Trunk Road, Babur, the Swaraj Party, Jallianwala Bagh, Dandi.
- **Police SI** asks the same kind of question one level harder: Harisena, the
  Labour Swaraj Party, the Hindu Mahasabha at Haridwar, Mildenhall at Akbar's court.
  It spends 15% of the paper here, the highest share of any exam in the sample.
- **APSC** asks fewer questions, in harder forms: chronological order, pairs and
  statements. Examples are the order of Macaulay, Wood, Raleigh and Sadler; Lothal
  site pairs; Nil Darpan; Begram ivories; Banskhera. It swings by year (5 in 2023, 0
  in 2024, 8 in 2025), and Assam History holds the bigger share.
- **TET** is not measured. The sample has one item because extracted Paper II has no
  Social Studies questions (85 of its 100 are Commerce). It is a gap in the data,
  not evidence of low demand.

### Limits of this evidence

- It is a small sample: 23 papers, and ADRE supplies 60% of the mapped questions.
- The sweep covered keyword hits plus the General Awareness people, books and
  miscellany lists. Questions it missed are not counted.
- APSC's official syllabus is read: History of India and Indian National Movement,
  with 30–35% of GS-I about Assam. ADRE Grade IV names Indian history in a hosted
  2024 copy. The hosted ADRE Grade III copy lists only Assam history, yet Grade III
  papers asked 29 of these questions, 11 of them in 2024. That copy says 100
  questions where the 2024 papers have 150, so it may be superseded; the papers
  decide scope until the final notification is read. SI is a coaching-site copy and
  TET is still unread. See
  [indian-history-sources.json](research/indian-history-sources.json).
- Worked answers in the export are not official keys, and ADRE 2022 has none.

## Depth line

**In:** every topic asked, plus what a learner needs to place it. Dynasties in order,
but only named rulers with an exam reason. Every national-movement stage, with date,
place and leader. One APSC-style order, pairs or statements item in most lesson tests.

**Out:** minor dynasties as lists; administrative detail beyond mansabdari; art
history beyond named monuments; economic history beyond the drain and Diwani;
historiography; World History (6 tagged questions, 4 routed out; Alexander and Bangladesh stay).

## Course outline

Tiers follow LESSON-DESIGN (B 4–6, C 2–3 units); no lesson is tier A at this depth.
"Asked" counts mapped questions. Each section ends with a checkpoint.


### Beginnings (lessons 1–3)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 1 | The Indus cities | B | 4 | 3 | Harappa, Mohenjo-daro and Lothal; seals and the unicorn; site and finding pairs |
| 2 | The Vedic age | C | 3 | 3 | The four Vedas, the Rigveda first; the Saraswati question; early and later Vedic life |
| 3 | Buddha and Mahavira | B | 4 | 4 | Four places of the Buddha's life; Tirthankaras and Mahavira as the 24th; contrast of the two teachings |

### Empires of the north (lessons 4–8)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 4 | Magadha and Alexander | C | 3 | 3 | Mahajanapadas, the rise of Magadha, Macedonia, 326 BCE and Porus on the Jhelum |
| 5 | The Mauryas | B | 5 | 4 | Chandragupta and Chanakya, the Arthashastra, Megasthenes, Ashoka, Kalinga and the edicts |
| 6 | After the Mauryas | C | 3 | 1 | Kushans and Kanishka, Gandhara and Mathura, Satavahanas, Sangam, the Begram ivories |
| 7 | The Guptas | B | 4 | 3 | Samudragupta and Harisena's Allahabad praise, Chandragupta II, Faxian, Kalidasa's plays |
| 8 | Harsha and Xuanzang | C | 3 | 3 | Prabhakaravardhana's son, Banabhatta, Banskhera, Xuanzang; link to Bhaskaravarman of Kamarupa |

### South, Kashmir and learning (lessons 9–10)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 9 | Cholas, Deccan and Kashmir | C | 3 | 3 | Pallavas and Chalukyas, the Chola reach into Southeast Asia, Lalitaditya, Kalhana's Rajatarangini |
| 10 | Knowledge and stone | B | 4 | 4 | Charaka, Sushruta, Aryabhata and the zero question, Nalanda, Ajanta, Elephanta, Khajuraho |

### Sultans, Deccan and devotion (lessons 11–13)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 11 | The Delhi Sultanate | B | 4 | 2 | Five dynasties in order, Iltutmish, Razia, Alauddin, Tughluq and Ibn Battuta; link to raids on Kamarupa |
| 12 | Vijayanagara and the Deccan | C | 3 | 3 | Harihara and Bukka, Krishnadeva Raya, Bahmani successors, Gol Gumbaz and Charminar |
| 13 | Bhakti, Sufis and Sikh Gurus | C | 3 | 2 | Kabir, Nanak, Tulsidas, Chishti Sufis, Guru Tegh Bahadur at Dhubri; link to Sankardev |

### The Mughal age (lessons 14–17)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 14 | Babur and Sher Shah | B | 4 | 4 | Panipat 1526, Humayun, Sher Shah, the Grand Trunk Road and the rupee |
| 15 | Akbar | B | 4 | 3 | Panipat 1556 and Hemu, mansabdari, Din-i-Ilahi, Abu'l Fazl, Mildenhall at court |
| 16 | Jahangir to Aurangzeb | C | 3 | 0 | Hawkins and Roe, Shah Jahan's buildings, Aurangzeb and the Deccan; link to Mir Jumla and Saraighat |
| 17 | Marathas and Mysore | C | 3 | 1 | Shivaji, Panipat 1761, Hyder Ali and Tipu Sultan |

### Company rule (lessons 18–22)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 18 | Plassey and Buxar | B | 4 | 2 | Vasco da Gama, the European companies, Plassey 1757, Buxar 1764, Diwani 1765 |
| 19 | The Governors-General | B | 4 | 2 | Hastings, Cornwallis, Bentinck as first Governor-General of India, Dalhousie, Macaulay's Minute; link to the Regulating Act lesson |
| 20 | Reformers | C | 3 | 1 | Ram Mohan Roy, Vidyasagar, Arya Samaj, Vivekananda; link to Anandaram Dhekial Phukan |
| 21 | The Revolt of 1857 | B | 4 | 2 | Causes, Mangal Pandey, leaders by centre, Lakshmibai, 1858 and the Viceroy; link to Maniram Dewan |
| 22 | Indigo, press and schools | C | 3 | 2 | Indigo Revolt and Nil Darpan, the education chain from Macaulay to Sadler, peasant risings |

### The national movement (lessons 23–27)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 23 | The early Congress | B | 4 | 1 | 1885, moderates, Naoroji and the drain, Calcutta 1906 and Swaraj |
| 24 | Swadeshi to Lucknow | B | 4 | 5 | Partition of Bengal, Tilak, Surat 1907, League, Hindu Mahasabha, Delhi 1911, Lucknow 1916; link to Swadeshi in Assam |
| 25 | The year 1919 | B | 4 | 5 | Rowlatt Act, Jallianwala Bagh, Tagore's knighthood, Montagu-Chelmsford; what did not happen in 1919 |
| 26 | Gandhi and Non-Cooperation | B | 4 | 4 | South Africa, Champaran, Khilafat, Non-Cooperation, Chauri Chaura, the Swaraj Party; link to Gandhi in Assam |
| 27 | Simon and the revolutionaries | C | 3 | 1 | Labour Swaraj Party, Simon Commission, Bhagat Singh, Bardoli, Lahore 1929 |

### Mass struggle and freedom (lessons 28–32)

| # | Lesson | Tier | Units | Asked | Content |
|---|---|---|---:|---:|---|
| 28 | The Salt March | B | 4 | 3 | Dandi, Civil Disobedience, Gandhi-Irwin Pact, Round Tables; link to Civil Disobedience in Assam |
| 29 | Quit India | B | 4 | 3 | Cripps, August Kranti Maidan, Do or Die, Discovery of India in Ahmednagar; link to Kanaklata and Gohpur |
| 30 | Bose and the INA | C | 3 | 2 | Forward Bloc, Azad Hind, Rangoon, the Red Fort trials; link to Kohima and the war in the North-East |
| 31 | The road to 1947 | B | 4 | 1 | Wavell Plan, Navy Mutiny, Cabinet Mission, Mountbatten Plan, Partition; link to Sylhet and Grouping |
| 32 | Building the nation | B | 4 | 7 | First cabinet, Patel and integration, the flag, 1971 and Bangladesh, the order of later operations |

## What makes it memorable

These are design hypotheses to test with learners, as in EXPERIENCE-REVAMP.

1. **Repeaters first.** Facts asked in several papers get their own memory items and
   return in review. The PYQ map shows which ones.
2. **Contrast sets, mixed on purpose.** Exams test confusions: the three battles of
   Panipat; Faxian, Xuanzang and Ibn Battuta with their reigns; Non-Cooperation,
   Civil Disobedience and Quit India; Swaraj Party, Labour Swaraj Party and Forward
   Bloc; Governor-General and Viceroy; "not in 1919".
3. **One spine of anchor dates.** `timeline` steps reuse a few anchors (326 BCE,
   1206, 1526, 1757, 1857, 1885, 1919, 1930, 1942, 1947), and the APSC order questions
   become practice on that line.
4. **Seen from Assam.** Where the history truly connects, a unit links to the Assam
   course. It teaches the national event and leaves the Assam story to its lesson.

## Overlap with existing courses

Link, do not repeat. Existing lessons already teach these from Assam's side.

| Lesson here | Link to |
|---|---|
| 8 Harsha | `varman-bhaskaravarman` |
| 11 Delhi Sultanate | Raids from Bengal, Assam History lesson 14 |
| 13 Bhakti | Sankardev, Assam History lesson 67 |
| 16 Aurangzeb | `ahom-06-mir-jumla` |
| 19 Governors-General | `con-01-rules-before-republic` |
| 21 Revolt of 1857 | `british-03-maniram-1857` |
| 24, 26, 28, 29, 30, 31 | `british-12` to `british-18`, the freedom movement in Assam |
| 31 Road to 1947 | `con-02-demand-for-assembly` |

837 entities already exist, including `mahatma-gandhi`, `harsha`, `xuanzang`,
`aurangzeb`, `mir-jumla`, `lord-curzon`, `jawaharlal-nehru` and `subhas-chandra-bose`.
Reuse them. Their `lessons` lists gain the new ids.

## Exercise patterns

| Fact | Exercise |
|---|---|
| Who | `whoami` with clues, such as a traveller's reign |
| Date and order | `timeline` on the anchor spine; `order` for APSC chains |
| Place | `map` |
| Text, author, reign | `match`, `odd` |
| Trap | `tf`, `spot`, one confusion per item |
| APSC format | At most one `mcq` "consider the statements" per lesson test |

## Guardrails specific to history

- **Exam labels stay labels.** "Father of zero" and similar titles are taught as what
  a paper calls someone, with the fuller history beside them.
- **Dates carry their certainty.** Before about 300 CE, mark dates approximate. The
  Buddha's dates, the Indus and Vedic ranges are spans, not facts to one year.
- **Disputed matters stay disputed.** The Saraswati and Ghaggar-Hakra identification,
  the Vedic migration debate, "Sepoy Mutiny" or "First War of Independence", Din-i-Ilahi
  as a religion, and the identity of Chanakya and Kautilya are stated with attribution.
- **Religion and Partition are told factually.** Conflict between communities and rulers
  is described from sources, with no modern judgement and no blame placed on any
  community today. Keep post-1947 lessons free of current party politics.
- **Spellings are taught.** Papers use Hiuen Tsang, Xuanzang, Fahien and Faxian. A
  unit must show the variant the papers use.
- **No invented dialogue or sources.** Famous sayings appear only in verified wording.
- **Permanent ids.** Course `indian-history` in subject `indian-history`. Lessons
  `ih-NN-slug`, as used in `content/lessons/`;
  steps `ih-NN.uU.SS`. Ids are permanent once published.
- **Assamese pending review.** All 32 lesson titles and 8 section titles are new
  Assamese, as is every later line of copy.

## Answers held for a source check

The APSC 2025 GS-I pages for questions 23, 24, 32 and 33 were read as images. Question
32 is Aurobindo Ghosh and question 33 is the 24th, both matching the export's key
letters. Lesson 24 must teach Aurobindo for 'passive resistance'.

Three export answers look wrong and need correcting in the PYQ repository, which was
not changed here:

- APSC 2025 GS-I Q23: key A is Ashoka; the expected answer is Harshavardhana, C.
- APSC 2025 GS-I Q24: key C is Sutlej; the expected answer is Ghaggar-Hakra, D.
- APSC 2025 GS-I Q21: key C reads 3rd to 1st century BCE; sources read give the 1st to
  2nd century CE. The printed options still need reading.

Two more stay on hold: ADRE 2024 HSSLC Q003, where the key names Tipu Sultan as 'Lion
of Mysore' (for lesson 17), and the 'father of zero' label, taught as a label in lesson 10.

## Prerequisites (Phase 1b)

Done on 2026-11-05 unless marked open.

1. **Sources.** The four titles this course uses were copied, with their text files,
   to `/home/angsuman/extra_spac/Indian history sources`, which was moved to the Trash on
   2026-11-05 after release. The trashed `Primary source`
   folder was not restored or changed. **Open:**
   Stein's Rajatarangini volume 1 (Lalitaditya), and the items under `to_locate`.
2. **India map.** A lesson or card `map` takes `"base": "india"`.
   [build_india_map.py](../scripts/build_india_map.py) writes `content/maps/india.json`
   (142 KB, in the offline shell). India's outline comes only from the DataMeet
   Survey of India-derived file and is drawn over Natural Earth neighbours, so a de
   facto line cannot show inside it. Twelve pilot places were added as entities; their
   Assamese is pending review. **Open:** no river lines exist locally, so lessons show
   rivers such as the Jhelum as labelled places for now. The outline is CC BY-SA, and
   the map note carries the credit.
3. **Pictures.** [indian-history-picture-inventory.json](research/indian-history-picture-inventory.json)
   lists 127 candidates for 50 subjects: 45 free, 6 attribution, 76 share-alike.
   **Open:** none is viewed or downloaded; see its gaps and rules.
4. **Syllabi.** See "Limits of this evidence". **Open:** SI and TET official text, and
   ADRE's final notification.
5. **History checks.** `check_history_completion.py` now names the history courses, so
   new subjects cannot break it, and `build_history_reference.py` already did.
   `check_learning_gates.cjs` had crashed since the Constitution release because its
   stub lacked `L.word`; the stub is fixed and the gates pass.

### Map authoring rules

- Tested at 375px with a temporary lesson, in English and Assamese, with a mistake
  and a retry. Existing Assam maps are unchanged.
- At full-India zoom, labels collide in the Buddhist circuit, and Lothal and Dandi
  are about 17px apart while tap rings are 31px wide. Use a zoomed `box` for a
  cluster, as `[81, 23.5, 87, 28.5]` does for the Buddha's places, and never offer
  neighbours as choices at full zoom.
- `box` is `[west, south, east, north]`. Story maps should be wider than they are tall,
  about 240px high, so that the text stays above Continue.
- The map note is built in. Do not state any border as historical.

## Phase 2 results

Lessons 5, 25 and 28 are written in English and Assamese: 13 units, 115 unit steps
and 18 lesson-test questions.

- `audit_lessons.py`, `build.py`, `check_history_completion.py`, `check_constitution.py`,
  `check_learning_gates.cjs` and `check_daily_review.cjs` pass.
- All 13 units and all 3 tests were played by autoplay at 375px, across English and
  Assamese, with deliberate mistakes. Each mistake returned once, retries did not raise
  first-attempt scores, and there was no overflow or console error. A 3 of 6 lesson
  test did not pass; a later 6 of 6 did. The `ih-empires` checkpoint played 6 of 6 with
  no repeats. Unit 1 of lesson 5 was also replayed in Assamese after the map crops, but
  the other units were not replayed after that change.
- The first version of the map cards pushed text behind Continue, which autoplay cannot
  see. Story maps now use cropped boxes. Keep a story map's height near 240px.
- The player cannot judge history or Assamese. Lesson 5's Kalinga figures and edict
  facts were read in a translation of the edicts, and Tagore's letter in a transcription.
  Most other facts rest on Wikipedia as a guide to scholarly positions, marked "check in
  review" in each lesson's sources, because Britannica refused automated access and the
  Hunter report pages could not be reached. A historian should check these before release.
- Facts that sources disagree on are worded to match: reign dates as approximate; the
  end of the Mauryas as about 185 BCE; marchers as "the usual count"; distance as about
  385 km; the Pact without a place. Tagore's letter uses the 30 May date line, and other
  accounts give 29 or 31 May. Chanakya is taught as the exam answer and as tradition.
- These lessons use inline art and maps, not photographs. No picture was downloaded, so
  the candidates remain unviewed. There is no `picture` exercise yet.
- Entity `lessons` lists were left empty on purpose, so that live Assam lessons do not
  link to a hidden course. Fill them at release.
- Exercises: tf 12, inline 10, match 9, whoami 8, order 8, spot 8, map 6, unscramble 5, odd 5, timeline 5. Watch `tf` and `order` in
  learner testing.

## Roll-out results

Measured 2026-11-05: 32 lessons, 116 units, 841 unit steps, 192 lesson-test questions, 8
checkpoints and a bank of 212 questions built by
[build_indian_history_bank.py](../scripts/build_indian_history_bank.py). The bank reuses
lesson steps, so it adds no new questions and claims no exam provenance.

- `audit_lessons.py`, `build.py`, `check_history_completion.py`, `check_constitution.py`,
  `check_learning_gates.cjs` and `check_daily_review.cjs` pass.
- Every lesson was played by autoplay at 375px, with units alternating English and
  Assamese and a deliberate mistake in the first unit. No unit was played in both
  languages. There was no overflow or console error. All eight checkpoints ran with no
  repeats. `ih-beginnings` and `ih-wider` ran with the bank at 15 of 15; the other six ran
  before the bank was added.
- Lessons edited after their play-through were not replayed: 1, 3, 5, 10, 11, 12 and 27
  (map crops only). Lesson 22's restructure and lesson 27's new card came before play.
- Story maps were measured by calculation, and none is over about 255px. Only the cards
  for lessons 5, 25 and 28 were looked at. Assamese layout on these cards was not looked at.
- Every story map and map exercise uses modern India as reference. Places are approximate.
- Sourcing is the main weakness. Wikipedia is the guide for almost every fact, marked
  "check in review". Primary texts were read only for the edicts, Tagore's letter and
  parts of the Harsha sources. Found editions in the sources register are unread.
- Claims resting on an exam paper alone, unconfirmed in sources read: Swaraj at Calcutta
  in 1906 (lesson 23), Aurobindo on passive resistance (24), the Rangoon headquarters (30),
  and Sardar from Bardoli (27, tagged uncited). The Raleigh and Sadler dates (22) are from
  general reference, and the leaders by centre in 1857 (21) need checking.
- These exam answers are taught with their nuance: Chanakya and Kautilya (5), Saraswati (2),
  father of zero (10), Sher Shah's road (14), Mildenhall (15), Lion of Mysore (17), Lajpat
  Rai and the bank (24), Operation Vijay (32).
- Story art is the shared inline set, used on 221 cards against 26 map cards.
  No photograph is in the course, so there is no `picture` exercise.
- Exercises: tf 115, inline 113, spot 72, match 58, whoami 56, map 54, order 50, unscramble 32, odd 30, timeline 14.
- Entity `lessons` lists stay empty until release, so live lessons do not link to a hidden course.

## Content pass

Added in a final pass over the lesson JSON. After editing lesson steps, run
`build_indian_history_bank.py`, then `build.py`.

- 32 predictions, one a lesson, each just before the card that answers it. They are not
  scored, and the bank skips them.
- 32 diagrams on sequences and sets, 9 labelled memory tricks, 32 "Exam traps" cards in
  the lesson guides and 10 links between lessons.
- Eight section tiles, and real date labels on the course rows.
- [check_indian_history.py](../scripts/check_indian_history.py) compares years and large
  figures across English and Assamese, and checks answers, options and ids: 0 problems.
- After this pass, autoplay finished all 116 units and 32 tests at 375px with no overflow
  or console error, but the final rerun changed only labels, art and links, and was not
  replayed. Six checkpoints have still not been run with the bank.

## Publishing

Deployed to Cloudflare Pages on 2026-11-05 with `scripts/deploy_cloudflare.sh`, at the
user's request, from the `constitution-course` branch. The geography courses were already
published on `main`, in matching copies. GitHub Pages builds from `main`, so it needs this
branch merged. Expect conflicts in `app/engine.js`, `content/entities.json`,
`content/manifest.json` and `sw.js`; rebuild the last two with `scripts/build.py`.

Still open: Assamese and historian review, pictures, river data, the TET tag, and the
PYQ keys listed above.

## Delivery

| Phase | Work | Gate |
|---|---|---|
| 0. Evidence | PYQ map, syllabus wording, sources register | Done, with the limits above |
| 1. Skeleton | Hidden course, reserved ids, empty bank, placeholder picture | Done: `build.py` passes, no catalog place |
| 1b. Prerequisites | The five items above | Done, with open items listed |
| 2. Pilot | Three contrasting lessons: 5 The Mauryas, 25 The year 1919, 28 The Salt March | Done, pending historian and Assamese review |
| 3. Learner check | Completion, enjoyment, 7- and 30-day recall | Keep what helps recall |
| 4. Roll-out | Sections in order, each with its checkpoint | Done, unreviewed |
| 5. Exam layer | Link PYQ ids, original bank, timed practice | Every linked question has provenance |

## Decisions for the user

- Should the course stay tagged for `tet` while Paper II Social Studies is unmeasured?
- May a public-domain river dataset be downloaded for the India map?
- Are share-alike pictures acceptable for this project, or should it use free ones only?
