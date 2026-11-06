# English course plan

Status: all 15 lessons and 75 units are playable as a local draft.
Open `index.html?course=english` on a local server for the lesson list.
Editorial review, placement, catalog release and delayed-recall evaluation are pending. Lesson format and permanent-id rules in
[LESSON-DESIGN.md](LESSON-DESIGN.md) apply.

An Assamese-medium learner should understand why an English answer is right, and retain the
vocabulary after a delay. This is the largest subject with no course.

## Why this course

| Exam | Questions | Share of its sample |
|---|---:|---:|
| DME | 19 of 59 | 32% |
| Assam TET | 70 of 320 | 22% |
| APSC CCE Prelims GS-II | 49 of 234 | 21% |
| Assam Police Constable | 20 of 100 | 20% |
| ADRE | 215 of 1,290 | 17% |
| Assam Police SI | 6 of 100 | 6% |

54 of the 379 questions carry a review flag. The whole subject is 15.8% of the sample.

## Scope

- **Course id:** `english`, with lesson ids `en-NN-slug`. Add a new `english` subject to
  `content/catalog.json`, with exams `adre`, `tet`, `apsc` and `si`.
- **Language rule:** All course-authored text is in English, including catalog copy,
  directions, passages, choices, feedback and review prompts. The course shows the same
  English text regardless of the app language. Shared navigation follows the learner's app
  setting. This course is an explicit exception to the bilingual lesson contract.
- **Reading level:** Use short directions, familiar examples and plain-English definitions.
  Introduce grammar terms with an example before asking learners to apply them.
- **Out of scope:** literature, essay writing, speaking and listening.

## Course map
See the [75-unit authoring map](ENGLISH-UNIT-MAP.md) for the teaching order and unit briefs.

15 lessons and about 75 units, roughly 450 exercises.

| # | Lesson id | Past questions | Units | The real idea | Main trap |
|---:|---|---:|---:|---|---|
| | **Part 1: Words** | | | | |
| 1 | `en-01-synonyms` | 56 | 6 | Learn words in families | Picking a word that only sounds related |
| 2 | `en-02-idioms` | 27 | 6 | An idiom's meaning is not its words | Reading it literally |
| 3 | `en-03-spelling` | 24 | 6 | Spelling follows patterns and exceptions | Confusing look-alike words |
| 4 | `en-04-one-word` | 31 | 6 | One word for a phrase, and group nouns | Near-miss terms |
| 5 | `en-05-context` | 12 | 4 | Context decides the meaning | Using the commonest meaning |
| | **Part 2: Grammar** | | | | |
| 6 | `en-06-prepositions` | 24 | 6 | Fixed pairs must be learned | Translating from Assamese |
| 7 | `en-07-articles` | 12 | 4 | A, an and the follow sound and meaning | Following the spelling |
| 8 | `en-08-agreement` | 12 | 4 | The verb agrees with the true subject | Matching the nearest noun |
| 9 | `en-09-verbs` | 19 | 4 | Tense shows time and completion | Mixing tenses in one sentence |
| 10 | `en-10-comparison` | 18 | 4 | Degrees, adjectives and adverbs | Double comparatives |
| 11 | `en-11-sentences` | 18 | 4 | Tags, reported speech and voice | Keeping the original tense |
| 12 | `en-12-blanks` | 21 | 6 | Mixed blanks and punctuation | Checking only one rule |
| | **Part 3: Use** | | | | |
| 13 | `en-13-correction` | 24 | 6 | Scan for one error type at a time | Rewriting the whole sentence |
| 14 | `en-14-arrangement` | 9 | 3 | Find the opening and the links | Starting from the middle |
| 15 | `en-15-reading` | 72 | 6 | Answer from the passage only | Using outside knowledge |

## How questions are made

- **Generator with word tables,** following `scripts/build_reasoning_course.py`. Tables of
  words, senses and English definitions produce variants. Review can change the sentence or
  distractors while still testing the taught word and sense.
- **Every word and rule is written by hand.** Grammar answers cannot be computed, so
  `check_english.py` can only test structure, not correctness.
- **All passages are original.** 72 past questions come from about 11 passages, so reading
  is worth more than its count suggests. Write 12 short passages of varied kinds.
- Word lists must be chosen from a named reference, recorded in `docs/research/`.

## Engine work

| Item | Need |
|---|---|
| Reading | Questions carry an optional `passage` panel that stays available in lesson checks and daily review |
| Prepositions and blanks | The existing `inline` and `fill` steps suit these |
| Error spotting | The existing `spot` step taps the wrong word |
| Sentence arrangement | The existing `order` step works |
| Word review | Daily review already covers steps, and variants give new words |
| Look | Decide whether it uses the exercise-book look through `AXOM.notebook` |

## English-only content contract

The draft mirrors English text in both locale fields to fit the existing player and audit.
Use plain English strings where the shared text renderer already accepts them when
expanding the course. Before
authoring the first unit, trace catalog, lesson, checkpoint and review rendering for direct
language lookups and fields that require bilingual objects. Add course-scoped support where
needed and preserve existing bilingual validation for other courses. Check that opening
and leaving English never changes the saved app language.

## Build order

1. Start with one hidden unit in `en-01-synonyms`. Teach near-synonyms in context, with
   four learning points, two or three short story cards and five to seven varied exercises.
   Include one transfer question that uses a fresh sentence. Record the dictionary entries
   used for each sense and write original examples and distractors.
2. Make the unit playable from a direct draft link. Verify it in both app language
   settings, including a wrong answer, retry and review of the same word in a new context.
3. Expand lesson 1 to six units, then pilot `en-06-prepositions` and `en-15-reading`.
   Add persistent passage display when building reading, with evidence-based explanations
   and a check that the passage stays accessible during review.
4. Compare immediate accuracy with seven-day recall before expanding the word pilot.
   Finish the remaining lessons, add placement and list the course after review.

## Release gates

- Run `scripts/verify.sh` and audit new lessons with `scripts/audit_lessons.py`.
- Check the English catalog card, player, checkpoint and review under both app language
  settings. Course text should be identical and readable in both.
- Have an English reviewer check word senses, acceptable grammar variants, answer keys
  and passage evidence. Record the sources and review status before listing the course.
- Keep first-attempt accuracy separate from retry success and seven-day recall.
