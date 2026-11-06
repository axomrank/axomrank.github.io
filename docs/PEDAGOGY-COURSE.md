# Child Development and Pedagogy course plan

Status: listed and published on 2026-11-06 at the user's request, with a pending-review notice.
All 10 lessons exist. English only, at the user's request: each
`as` field repeats the English, as in the English course, and no Assamese is planned. Lesson format and permanent-id rules in
[LESSON-DESIGN.md](LESSON-DESIGN.md) apply.

A future teacher should be able to apply an idea to a classroom situation, not just name a
theorist.

## Why this course

55 past questions, all from TET: 35 in the Special Paper I and 20 in Paper I. That is 17% of
the TET sample, and none appear in Paper II. Other exams ask nothing here, so this course is
worth building for TET candidates alone. Only the 2021 papers are in the sample, so check
newer papers and the current syllabus before fixing the list. The earlier official notice link
returned a 404 error when it was tried, so that syllabus has not been read. A 2026-11-06 search also
found only secondary guides.

| Group | Past questions |
|---|---:|
| Teaching methods | 30 |
| Child development | 20 |
| Inclusive education | 5 |

## Scope

- **Course id:** `pedagogy`, with lesson ids `pd-NN-slug`, in the existing `pedagogy` subject,
  tagged `tet`.
- **Out of scope:** teaching methods for each school subject, until the syllabus is read.

## Course map

10 lessons and about 34 units, roughly 200 exercises. The sample is thin, so use 3 or 4 units
each and let the syllabus set coverage.

| # | Lesson id | Group | Core content |
|---:|---|---|---|
| 1 | `pd-01-development` | Child development | Stages, tasks, adolescence, research methods |
| 2 | `pd-02-learning` | Child development | Thorndike, Pavlov, insight learning |
| 3 | `pd-03-thinking` | Child development | Cognitive development and its major theories |
| 4 | `pd-04-differences` | Child development | Intelligence, creativity, individual differences |
| 5 | `pd-05-motivation` | Child development | Motivation, attention, behaviour |
| 6 | `pd-06-inclusion` | Inclusive education | Special needs, gifted learners, hearing impairment |
| 7 | `pd-07-methods` | Teaching methods | Heuristic, project, deductive, lecture methods |
| 8 | `pd-08-planning` | Teaching methods | Objectives, lesson plans, questioning, micro-teaching |
| 9 | `pd-09-classroom` | Teaching methods | Guidance, child-centred practice, the learning environment |
| 10 | `pd-10-thinkers` | Teaching methods | Tagore, Dewey, Rousseau, and current policy |

## How questions are made

- **Lesson JSON, written by hand.** TET often asks what a teacher should do, so use short
  classroom scenarios with a clear best answer, as Decision Making does in Reasoning.
- **Sources:** NCERT, the National Curriculum Framework, the National Education Policy 2020,
  the Right to Education Act and the theorists' own work where available. Record them in
  `docs/research/`.
- **Keep ideas distinct:** attribute each theory to its author, and label anything disputed.
- **Simplify carefully:** popular summaries of these theories are often wrong. Read the source
  before stating what a theorist claimed.
- **Do not invent:** classroom examples are illustrations. Never present one as a real case.

## Engine work

Nothing is required. `inline`, `match`, `order` and `whoami` cover it. A `classroom` scenario
scene is an idea to test, not a need.

## Build order

1. Read the current TET syllabus and any newer papers.
2. Pilot lessons 2, 6 and 8 as a hidden draft.
3. Test with trainee teachers if possible.
4. Finish the rest, then add placement and list the course.

## Release gates

Build checks pass. Theories were checked against sources. A teacher-educator has reviewed the
scenarios.
