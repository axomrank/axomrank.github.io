# English course plan

Status: planned on 2026-11-06. Nothing is built. Lesson format and permanent-id rules in
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
- **Language rule:** the English being tested stays in English in both modes. Instructions
  and explanations are in Assamese in Assamese mode. This is a deliberate exception to
  writing all prose in both languages.
- **Out of scope:** literature, essay writing, speaking and listening.

## Course map

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
  words, meanings and Assamese glosses produce variants, so review tests a different word.
- **Every word and rule is written by hand.** Grammar answers cannot be computed, so
  `check_english.py` can only test structure, not correctness.
- **All passages are original.** 72 past questions come from about 11 passages, so reading
  is worth more than its count suggests. Write 12 short passages of varied kinds.
- Word lists must be chosen from a named reference, recorded in `docs/research/`.

## Engine work

| Item | Need |
|---|---|
| Reading | A `passage` step that keeps the text visible across several questions. This is new |
| Prepositions and blanks | The existing `inline` and `fill` steps suit these |
| Error spotting | The existing `spot` step taps the wrong word |
| Sentence arrangement | The existing `order` step works |
| Word review | Daily review already covers steps, and variants give new words |
| Look | Decide whether it uses the exercise-book look through `AXOM.notebook` |

## Assamese

Glosses and grammar explanations need a fluent reader who also knows English grammar. Much
of the value is explaining mistakes that come from Assamese habits, such as prepositions.
Those notes must come from a real teacher's experience, not from guesswork.

## Build order

1. Choose the word reference and write the word tables for lesson 1.
2. Build the `passage` step.
3. Pilot lessons 1, 6 and 15 as a hidden draft: one word, one grammar and one reading lesson.
4. Try it with learners, comparing 7-day recall of words.
5. Finish Parts 1, 2 and 3, then add placement and list the course.

## Release gates

`scripts/verify.sh` and `audit_lessons.py` pass. Every lesson plays in both modes. A person
checks every grammar answer, because code cannot. A fluent reader reviews the explanations.
