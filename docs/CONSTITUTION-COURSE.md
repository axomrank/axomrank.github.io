# Course plan: the Constitution of India

Status: plan, 2026-11-04. Phases 0, 1 and the writing part of Phase 2 are recorded
below. Three pilot lessons exist as hidden drafts; none is reviewed, and learners
cannot see the course. It defines the course that fills the empty `polity` subject in
`content/catalog.json`.

## Goal

A learner preparing for ADRE, APSC CCE, Assam Police SI or Assam TET should be
able to find any important provision, explain what it does and recall it weeks
later, in English and Assamese. The course covers every Part and Schedule of
the Constitution, weighted by what exams ask, in about **16 hours**
(60 lessons, 236 units, 16 checkpoints).

It follows [LESSON-DESIGN.md](LESSON-DESIGN.md) and the mission and memory
plan in [EXPERIENCE-REVAMP.md](EXPERIENCE-REVAMP.md): one story beat per unit,
four learned points, two or three visual story cards, five to seven varied
exercises with explanations, and an 80% first-attempt gate.

## What exams ask

A hand classification of the 2,398 extracted questions in
`/home/angsuman/extra_spac/PYQ` found 86 constitution and governance questions
(3.6%): ADRE 43, APSC 37, SI 2, DME 2, TET 2. A further 13 belong to Current
Affairs or Assam History. The mapping is in
[constitution-pyq-map.json](research/constitution-pyq-map.json). It is a small
sample, and it only covers questions a keyword filter selected.

| Section | Questions | Share | Units | Share |
|---|---|---:|---:|---:|
| C14 Constitutional and other bodies | 16 | 19% | 20 | 8% |
| C12 Tribal areas, special provisions, languages | 11 | 13% | 18 | 8% |
| C7 Parliament | 10 | 12% | 22 | 9% |
| C9 States and Union Territories | 8 | 9% | 15 | 6% |
| C2 Preamble and features | 7 | 8% | 11 | 5% |
| C1 Making the Constitution | 6 | 7% | 22 | 9% |
| C4 Fundamental Rights | 6 | 7% | 28 | 12% |
| C8 Judiciary | 5 | 6% | 16 | 7% |
| C6 Union executive | 4 | 5% | 16 | 7% |
| C5, C10, C16 | 3 each | 3% each | 10, 14, 7 | 4%, 6%, 3% |
| C15 Amendment | 2 | 2% | 12 | 5% |
| C3, C13 | 1 each | 1% each | 10, 10 | 4% each |
| C11 Emergency | 0 | 0% | 5 | 2% |

This corrects the earlier keyword estimate, which overstated Fundamental
Rights. Elections, Assam's special provisions and telling constitutional bodies
from other bodies are asked far more than their first budgets allowed. Seven
units therefore moved to lessons 47, 48, 52 and 55, keeping the total at 236.
Fundamental Rights, Emergency and amendment keep more units than their question
share because later sections depend on them. Papers set basics at ADRE level
and Assam-specific detail at APSC level, so Assam lessons need both.

## What makes it memorable

1. **The Constitution as a map.** The 25 Parts are districts and articles are
   addresses. Each section opens on the district map, and the learner's
   completed "addresses" fill in. Article numbers, the hardest exam facts, are
   learned as neighbourhoods (14–18 equality, 19–22 freedom, 23–24
   exploitation, 25–28 religion, 29–30 culture and education, 32 remedies),
   not as isolated numbers.
2. **Real case files.** A story card states the real question before the
   court (with case name and year), the learner predicts the article involved,
   and the reveal gives the actual holding. Prediction changes only the clue
   order, never the outcome. Core cases: Shankari Prasad, Golaknath,
   Kesavananda Bharati, Indira Gandhi v. Raj Narain, Maneka Gandhi, Minerva
   Mills, Indra Sawhney, S. R. Bommai, Vishaka, Puttaswamy, Navtej Singh Johar
   and the 2024 Section 6A judgment.
3. **Contrast pairs, mixed on purpose.** Exams test confusions, so units put
   lookalikes side by side and review interleaves them: Article 32 and 226;
   352, 356 and 360; money bill and financial bill; censure and no-confidence
   motions; Speaker and Chairman; Lok Sabha and Rajya Sabha; constitutional
   and statutory bodies; Fifth and Sixth Schedules; rights and directives.
4. **Assam in every section.** Each section has one meaningful Assam anchor,
   linked with `link` to the Assam History course where the stories connect:
   Gopinath Bordoloi's sub-committee and the Sixth Schedule; Muhammad Saadulla
   on the Drafting Committee; the North-East reorganisation of 1963–1987;
   Articles 244A and 371B; the Gauhati High Court; the Assam Legislative
   Assembly; APSC under Part XIV; Assamese and Bodo in the Eighth Schedule;
   the Assam Accord and Section 6A; the 100th Amendment's land boundary.
5. **Memory tricks, labelled as tricks.** For example, the twelve Schedules
   as **TEARS OF OLD PM** (Territory, Emoluments, Affirmations, Rajya Sabha
   seats, Scheduled areas, Other tribal areas, Lists, Languages, Ninth,
   Defection, Panchayats, Municipalities). Tricks use `<b>` and never replace
   the fact.
6. **The illustrated original.** The hand-calligraphed 1950 Constitution has
   artwork at the head of each Part, prepared under Nandalal Bose. Used as the
   section hero, it gives each Part a picture to remember. Confirm the
   reproduction rights and the specific image source before use.
7. **A tappable article index.** Add `article` entities (for example
   `[[art-21]]`) so any mention opens a short bilingual summary, and an
   Explorer page of Parts, articles and Schedules beside the timeline in
   `history.html`.

## Exercise patterns

| Fact | Exercise | Notes |
|---|---|---|
| Article number | `timeline` used as a number line | Anchors are articles, such as 14 Equality and 32 Remedies. The renderer shows numeric anchors; check the build validator accepts non-year anchors. |
| Which list or Part | `match`, `odd` | A bucket-sort type is a possible later addition, only if the pilot shows `match` is not enough. |
| Procedure | `order` | Passage of a bill, impeachment, amendment, election of the President. |
| Office or body | `whoami` | Clues from qualification to powers; an earlier answer earns more XP. |
| Territory | `map` | Reorganisation of states, North East, Sixth Schedule council areas. |
| Exam trap | `tf`, `spot` | One distinct confusion per item, with the reason. |
| Applying a right | Labelled scenario + `mcq` | Hypothetical situations carry a "Scenario" label and are never presented as real cases. |

Plain `mcq` remains rare: at most one "consider the statements" question per
lesson test, matching the APSC format.

## Course outline

Tiers follow LESSON-DESIGN (A 6–8, B 4–6, C 2–3 units). Each section ends with
a checkpoint that never repeats questions.

### C1 · Making the Constitution (6 lessons, 22 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 1 | Rules before the Republic | B | 4 | Regulating Act 1773 to Government of India Act 1935; what 1935 left behind |
| 2 | The demand for an Assembly | C | 3 | The idea of a Constituent Assembly, August Offer, Cabinet Mission Plan 1946 |
| 3 | The Assembly at work | A | 6 | Composition, first sitting 9 December 1946, Objectives Resolution, committees, Drafting Committee and its members |
| 4 | Assam's voices in the Assembly | C | 3 | Bordoloi sub-committee on North-East tribal areas, Saadulla, other members from Assam |
| 5 | Borrowed and built | B | 4 | Features drawn from the 1935 Act, Britain, the USA, Ireland, Canada, Australia, Weimar Germany, the USSR, South Africa, Japan and France |
| 6 | Adoption and the handwritten copy | C | 2 | 26 November 1949, 26 January 1950 and why that date, calligraphy and art |

### C2 · Preamble and salient features (3 lessons, 11 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 7 | The Preamble word by word | B | 5 | Sovereign, socialist, secular, democratic, republic; justice, liberty, equality, fraternity |
| 8 | Is the Preamble part of it? | C | 2 | Berubari (1960), Kesavananda (1973), 42nd Amendment additions |
| 9 | Salient features | B | 4 | Federal with a strong Centre, parliamentary form, rigid and flexible, single citizenship, integrated judiciary |

### C3 · Union, territory and citizenship (3 lessons, 10 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 10 | Union and its territory | B | 4 | Articles 1–4, States Reorganisation 1956, North-East reorganisation (map) |
| 11 | Who is a citizen | B | 4 | Articles 5–11, Citizenship Act 1955, acquisition and loss, OCI |
| 12 | Citizenship and Assam | C | 2 | Assam Accord 1985, Section 6A and its 1971 cut-off, the 2024 Supreme Court ruling, CAA 2019 as enacted |

### C4 · Fundamental Rights, Part III (7 lessons, 28 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 13 | What a right means | C | 3 | Article 12 "State", Article 13 judicial review, enforceability |
| 14 | Right to equality | A | 6 | Articles 14–18, reservation, abolition of untouchability and titles |
| 15 | Right to freedom | A | 6 | Articles 19–22, the growth of Article 21, Article 21A |
| 16 | Exploitation and religion | C | 3 | Articles 23–28 |
| 17 | Culture and education | C | 2 | Articles 29–30, minority institutions |
| 18 | Remedies and writs | B | 5 | Articles 32 and 226, the five writs, Ambedkar on Article 32 (verified CAD wording only) |
| 19 | Rights in court | C | 3 | Maneka Gandhi, Indra Sawhney, Vishaka, Puttaswamy, Navtej Singh Johar |

### C5 · Directives and duties, Parts IV and IVA (3 lessons, 10 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 20 | Directive Principles | B | 4 | Articles 36–51 by socialist, Gandhian and liberal groups; Article 45 |
| 21 | Rights versus directives | C | 3 | Champakam Dorairajan, the 25th and 42nd Amendments, Minerva Mills balance |
| 22 | Fundamental Duties | C | 3 | Article 51A, Swaran Singh Committee, 42nd and 86th Amendments |

### C6 · Union executive, Part V (4 lessons, 16 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 23 | The President | A | 6 | Election, qualification, term, impeachment (Articles 52–62) |
| 24 | What the President can do | B | 4 | Vetoes, ordinances (123), pardons (72), emergency role |
| 25 | The Vice-President | C | 2 | Articles 63–71, Rajya Sabha Chairman |
| 26 | Prime Minister and ministers | B | 4 | Articles 74–78, collective responsibility, Attorney General (76) |

### C7 · Parliament, Part V (5 lessons, 22 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 27 | Two Houses | B | 5 | Composition, qualifications, terms of Lok Sabha and Rajya Sabha |
| 28 | Presiding officers and sessions | B | 4 | Speaker, Chairman, sessions, quorum, joint sitting (108) |
| 29 | How a bill becomes law | A | 6 | Ordinary, money (110), financial and amendment bills |
| 30 | Control of public money | C | 3 | Budget (112), Consolidated and Contingency Funds, cut motions |
| 31 | Tools of accountability | B | 4 | Question Hour, Zero Hour, motions, PAC and other committees |

### C8 · Judiciary (4 lessons, 16 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 32 | The Supreme Court | A | 6 | Articles 124–147, appointment and collegium, jurisdictions |
| 33 | High Courts and Gauhati | B | 4 | Articles 214–231, the Gauhati High Court's jurisdiction across states |
| 34 | Judicial review and PIL | C | 3 | Review, activism, public interest litigation |
| 35 | Courts below and tribunals | C | 3 | Subordinate courts, Part XIVA tribunals, Lok Adalats |

### C9 · States and Union Territories (4 lessons, 15 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 36 | The Governor | B | 5 | Articles 153–167, discretion, assent (200–201) |
| 37 | Chief Minister and ministers | C | 2 | Articles 163–164 |
| 38 | State legislatures | B | 4 | Unicameral and bicameral (169), Assam Legislative Assembly |
| 39 | Union Territories | B | 4 | Part VIII, Delhi (239AA), Jammu and Kashmir after 2019 |

### C10 · Federalism (4 lessons, 14 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 40 | Three lists | B | 5 | Seventh Schedule, Articles 245–255, Parliament in state fields |
| 41 | Working together | C | 3 | Articles 256–263, Inter-State Council, zonal councils and the North Eastern Council |
| 42 | Money between Union and states | B | 4 | Part XII, Finance Commission (280), GST Council (279A) |
| 43 | Trade and rivers | C | 2 | Part XIII, inter-state water disputes (262) |

### C11 · Emergency, Part XVIII (1 lesson, 5 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 44 | Three emergencies | B | 5 | Articles 352, 356 and 360; 1975; 44th Amendment safeguards; Bommai |

### C12 · Tribal areas, special provisions and languages (4 lessons, 18 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 45 | Scheduled areas | C | 3 | Part X, Article 244, Fifth Schedule |
| 46 | The Sixth Schedule | A | 6 | Autonomous councils in Assam (Bodoland, Karbi Anglong, Dima Hasao), Meghalaya, Tripura and Mizoram; Bordoloi link |
| 47 | Special provisions for states | B | 5 | Articles 370 (history and 2019), 371–371J, 244A and 371B for Assam |
| 48 | Languages | B | 4 | Part XVII, Eighth Schedule, Bodo added by the 92nd Amendment |

### C13 · Local government (3 lessons, 10 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 49 | Panchayati Raj | B | 5 | Background committees, 73rd Amendment, Part IX, Eleventh Schedule |
| 50 | Municipalities | C | 3 | 74th Amendment, Part IXA, Twelfth Schedule |
| 51 | Co-operative societies | C | 2 | 97th Amendment, Part IXB, the 2021 Supreme Court ruling |

### C14 · Constitutional and other bodies (4 lessons, 20 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 52 | Election Commission | A | 7 | Part XV, Articles 324–329, the Representation of the People Acts |
| 53 | Public services and APSC | C | 3 | Part XIV, UPSC and state commissions, Article 311, All-India Services |
| 54 | Watchdogs and commissions | B | 4 | CAG, Advocate General, commissions for SCs, STs and backward classes |
| 55 | Constitutional or not? | B | 6 | NITI Aayog, NHRC, CIC, Lokpal and other statutory or executive bodies |

### C15 · Amendment and basic structure, Part XX (3 lessons, 12 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 56 | How it changes | B | 4 | Article 368, three kinds of majority, state ratification |
| 57 | The basic structure | B | 4 | Shankari Prasad to Kesavananda, Raj Narain and Minerva Mills |
| 58 | Amendments that changed India | B | 4 | Selected amendments from the 1st to the latest on a timeline |

### C16 · Democracy and the whole map (2 lessons, 7 units)

| # | Lesson | Tier | Units | Content |
|---|---|---|---|---|
| 59 | Parties and defection | C | 3 | Tenth Schedule, 52nd and 91st Amendments |
| 60 | The complete map | B | 4 | Parts XIX, XXI and XXII, all twelve Schedules, a capstone tour |

## Coverage check

Every Part and Schedule has a home. Part VII was repealed in 1956 and is
taught only as that fact (lesson 10).

| Part | Lessons | Part | Lessons |
|---|---|---|---|
| I | 10 | XII | 42 |
| II | 11, 12 | XIII | 43 |
| III | 13–19 | XIV, XIVA | 53, 35 |
| IV, IVA | 20–22 | XV | 52 |
| V | 23–32 | XVI | 14, 54 |
| VI | 33, 36–38 | XVII | 48 |
| VIII | 39 | XVIII | 44 |
| IX, IXA, IXB | 49–51 | XIX | 60 |
| X | 45 | XX | 56–58 |
| XI | 40, 41 | XXI, XXII | 47, 60 |

Schedules: First 10, Second 23–32, Third 60, Fourth 27, Fifth 45, Sixth 46,
Seventh 40, Eighth 48, Ninth 21, Tenth 59, Eleventh 49, Twelfth 50.

## Sources

Verify each fact against the primary passage before writing it.

- The Constitution of India, Legislative Department edition as on 10 September
  2026, to the 106th Amendment.
- The official Assamese translation of the Constitution, for legal terms. The
  located third edition runs to the 106th Amendment; its PDF text layer is
  damaged, so terms are read from page images.
- Constituent Assembly Debates (Lok Sabha Digital Library). Quote only
  verified wording with volume and date.
- Supreme Court judgments from official reports, cited with name and year.
- The amending Acts themselves for amendment facts.
- NCERT political science and exam-preparation books are leads only and are
  not reproduced.

Located editions are in
[constitution-sources.json](research/constitution-sources.json). Record further
provenance there and terms in
`docs/research/constitution-glossary.json` (English, Assamese, source, review
status).

## Guardrails specific to law

- **The text changes.** Article counts, the latest amendment, seat numbers and
  pending bills are time-sensitive. Keep them in
  `docs/research/constitution-currency.json` with an `asOf` date, and recheck
  before each release. Avoid naming current office-holders; firsts belong
  here, current holders belong in Current Affairs.
- **Contested subjects stay factual.** For citizenship, Article 370, the
  Emergency and reservation, state the provision, the legislative history and
  the court's holding, with attribution. Mark pending cases as pending. Do not
  editorialise.
- **Scenarios are labelled.** Hypothetical situations carry a visible
  "Scenario" label. Real cases always carry their real name and year. No
  invented Assembly dialogue, quotes or judgments.
- **Permanent ids.** Course `indian-constitution` in subject `polity`. Lessons
  `con-NN-slug`, reserved in the course file; steps `con-NN.uU.SS`, matching the
  existing lessons. Ids are permanent once published.
- **Assamese pending review.** All new Assamese copy and glossary terms retain
  pending editorial-review status.

## Phase 0 results

- [constitution-article-register.json](research/constitution-article-register.json)
  lists 506 contents entries (471 in force, 35 omitted) in 26 Part headings, with
  12 Schedules and 3 appendices. Every entry was matched to the body text. These
  are contents entries, not an official article count, so do not teach them as one.
- [constitution-glossary.json](research/constitution-glossary.json) has all Part
  titles and 78 terms in Assamese, read from page images and pending review.
- [constitution-currency.json](research/constitution-currency.json) holds the
  dated facts. Reading the text gave five lesson traps: the 106th Amendment's
  commencement differs from when women's seats take effect; articles 124A to
  124C are printed but struck down; Union territory entries run to 9 for 8
  territories; the Sixth Schedule still says North Cachar Hills; lettered
  articles use Assamese letters in the Assamese text.
- Still to collect when each lesson needs them: Constituent Assembly Debates,
  judgments and amending Acts.

## Phase 1 results

- `content/courses/indian-constitution.json` holds all 60 lessons and 16 sections
  with `draft: true`, an empty question bank and a plain placeholder picture.
  Lesson and section titles are new Assamese, pending review.
- The course is hidden. The `polity` catalog entry is a "soon" row, so the subject
  still shows Coming soon. The draft opens only at
  `index.html?course=indian-constitution`, and every lesson there shows Soon.
- 85 `article` entities (`[[art-21a]]`) come from
  [add_article_entities.py](../scripts/add_article_entities.py). Each is only the
  official heading in both languages. To add one, add its heading to the glossary.
- A `timeline` step with `"scale": "articles"` plays as an article line. Anchors
  must be plain numbers, which the build checks, because a letter would not turn
  into an Assamese letter; lettered articles go in `items`.
- A temporary fixture lesson was played in English and Assamese at 375px, with a
  mistake and retry. The retry did not raise first-attempt accuracy (1 of 2), there
  was no overflow, and the article sheet opened. The fixture was then removed.

### Before release

1. Replace the catalog "soon" row with `{ "course": "indian-constitution" }` and
   remove `draft`.
2. Give the subject page its own intro. It is hard-coded to history wording, with a
   history reference link.
3. Reword "Era checkpoint" for this course, or make the wording course-specific.
4. Replace the placeholder picture.

## Phase 2 results

Lessons 18, 29 and 46 are written in English and Assamese: 17 units, 123 steps and
18 lesson-test questions. Scripts are in `docs/authoring/constitution_l*.py`.

- `audit_lessons.py` and `build.py` pass. The history completion check passes after
  it was scoped to history lessons.
- All units and tests were played by autoplay at 375px, in both languages, with no
  overflow. Mistakes returned once, and retries did not raise first-attempt scores.
  A 3 of 6 lesson test did not pass; a later 6 of 6 did. The `con-tribal` checkpoint
  and new pictures were also opened.
- The player cannot judge law or Assamese. Each fact was read in the sources listed
  in its lesson, but a legal reader and an Assamese reader are still needed.
- Puttaswamy's rejection of the 1976 majority rests on secondary reports. Only the
  first part of the 6 September 1949 debate was read. Check both in review.
- Checkpoints draw three test questions per finished lesson until the question bank
  is written, so pilot checkpoints are short.
- Pictures are simple inline drawings. Better art remains a roll-out task.
- True/false is the most common exercise, 20 of 88 exercises in units. Watch this in
  learner testing.

Phase 3 needs real learners, so it has not started.

## Delivery

| Phase | Work | Gate |
|---|---|---|
| 0. Sources | Collect the primary texts above, classify polity PYQs, build an article register (Part, range, title, amending Act) and the glossary | Register matches the official text; PYQ counts confirm or change unit budgets |
| 1. Skeleton | Course file, `article` entities, number-line check for `timeline`, catalog entry | `python3 scripts/build.py` passes with an empty course |
| 2. Pilot | Three contrasting lessons: 18 Remedies and writs, 29 How a bill becomes law, 46 The Sixth Schedule | Lesson contract, `audit_lessons.py`, English and Assamese autoplay with retries and 80% first-attempt gates; mobile and offline |
| 3. Learner check | Compare pilot completion, enjoyment and 7- and 30-day recall, as in EXPERIENCE-REVAMP | Keep only the patterns that help recall without excessive time |
| 4. Roll-out | Write sections C1 to C16 in order, each with its checkpoint | Each section passes Phase 2 checks before the next starts |
| 5. Exam layer | Link real PYQ ids to lessons and add timed polity practice | Every linked question has documented provenance |

## Decisions for the user

- Is 16 hours the right size, or is a compact path (about 10 hours,
  merging tier-C lessons) preferred, with the rest as a deep dive?
- Should `tet` be added to the `polity` subject's exam list, given that TET
  asks about Articles 21A and 45?
