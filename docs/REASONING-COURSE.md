# Reasoning course plan

Status: all 23 lessons built on 2026-11-06 on the `reasoning-course` branch and listed in
the catalog. Not deployed. Learners have not tried it. Lesson format and permanent-id rules
in [LESSON-DESIGN.md](LESSON-DESIGN.md) still apply.

## Course state

| | Measured |
|---|---|
| Lessons | 23 of 23 |
| Units, not counting tests | 109 |
| Skill-linked exercises | 689, with 1,506 versions counting variants and placement |
| Skills, mistake patterns, placement questions | 109, 41, 28 |
| Answers recomputed by `check_reasoning.py` from the question text | 64 versions |

**Played in the browser at 375px:** all 109 units and all 23 lesson tests, alternating
English and Assamese, with deliberate mistakes and retries: no stuck steps, errors or
horizontal overflow. Placement ran 28 questions without retries. Every scene was viewed
on screen. A Coding test scoring 3 of 6 stayed unpassed after correct retries.

**Not checked yet:** real learners, enjoyment or 7-day recall, a fluent Assamese reader,
and touch input on a real phone. Browser play drove the scenes through test hooks, so a
real drag still needs a person. Only 64 answers are recomputed independently; the others depend
on the generator or on hand-written keys. Hand-checking already found one wrong logic
puzzle and two wrong kinship words, so a person should sample the rest, especially
the hand-written lessons 4, 5, 10, 15, 16, 22 and 23. The learner pilot in the build order
was skipped at the owner's direction.

## Why this course

Measured from the 2,398 questions in the sibling `PYQ` folder, 423 are tagged Reasoning
or Aptitude.

| Exam | Questions | Share of its sample |
|---|---:|---:|
| APSC CCE Prelims GS-II (CSAT) | 137 of 234 | 59% |
| Assam Police Constable | 20 of 100 | 20% |
| ADRE | 240 of 1,290 | 19% |
| Assam Police SI | 17 of 100 | 17% |
| Assam TET | 8 of 320 | 3% |
| DME | 1 of 59 | 2% |

These are planning signals, not an official exam weighting. ADRE is over half the whole
sample. 105 of the 423 questions carry a review flag, and 124 use a worked or editorial
answer rather than a board key. The lesson map is in
[research/reasoning-pyq-map.json](research/reasoning-pyq-map.json).

## Scope

- **Course id:** `reasoning`. Lesson ids are `rs-NN-slug` and are permanent once published.
- **Home:** the existing `aptitude` subject in `content/catalog.json`, whose course list
  is empty. Change its blurb, because "Arithmetic" belongs to Mathematics.
- **Exam tags:** keep `adre`, `apsc` and `si`. The catalog has no Constable exam id, and
  8 TET questions do not justify a `tet` tag.
- **In scope:** all 354 Reasoning questions, plus the 69 Aptitude questions in Part 5.
- **Left to Mathematics:** the one ages question.
- **Out of scope:** timed mock papers. See "Later".

## Course map

Units follow the tiers in the lesson standard: 20 or more past questions gives 6 units,
10 to 19 gives 4, and fewer gives 3. That is 23 lessons and about 109 units, or roughly
650 exercises. Mathematics has 82 units and 492 skill-linked exercises.

### Part 1: Patterns (193 questions, 46 units)

| # | Lesson id | Past questions | The real idea | Main trap to catch |
|---:|---|---:|---|---|
| 1 | `rs-01-alphabet` | 28 | Letters are positions; opposite pairs add to 27 | Counting from the wrong end |
| 2 | `rs-02-number-series` | 24 | Look at the gaps, then the gaps of the gaps | Stopping at the first difference |
| 3 | `rs-03-letter-series` | 20 | A series can be several series interleaved | Reading it as one sequence |
| 4 | `rs-04-analogy` | 33 | Name the relation first, then apply it | Matching the topic, not the relation |
| 5 | `rs-05-odd-one-out` | 31 | Find the property shared by the others | Picking a surface difference |
| 6 | `rs-06-coding` | 24 | A code is a rule you can recover and reverse | Applying the rule forwards when decoding |
| 7 | `rs-07-operators` | 11 | Replace the symbols, then use normal order | Calculating left to right |
| 8 | `rs-08-number-puzzles` | 22 | Scan with a stated condition, one digit at a time | Losing count, or ignoring position |

### Part 2: Position (71 questions, 20 units)

| # | Lesson id | Past questions | The real idea | Main trap to catch |
|---:|---|---:|---|---|
| 9 | `rs-09-direction` | 18 | Left and right depend on the way you face | Treating left as west |
| 10 | `rs-10-blood-relations` | 19 | Draw generations; gender is a separate fact | Assuming gender from a name |
| 11 | `rs-11-ranking` | 13 | Left rank + right rank − 1 = total | Forgetting the person is counted twice |
| 12 | `rs-12-arrangement` | 11 | Fixed facts first, then branch | Treating a possibility as a fact |
| 13 | `rs-13-calendar-clock` | 10 | Odd days are a remainder after 7; hands have rates | Ignoring leap years, or the hour hand's movement |

### Part 3: Logic (39 questions, 11 units)

| # | Lesson id | Past questions | The real idea | Main trap to catch |
|---:|---|---:|---|---|
| 14 | `rs-14-venn` | 15 | Each region is one combination of memberships | Counting an overlap twice |
| 15 | `rs-15-syllogism` | 8 | A conclusion must hold in every possible diagram | "Could be" taken for "must be" |
| 16 | `rs-16-statements` | 16 | Use only what is stated | Using outside knowledge |

### Part 4: Figures (50 questions, 16 units)

| # | Lesson id | Past questions | The real idea | Main trap to catch |
|---:|---|---:|---|---|
| 17 | `rs-17-figure-patterns` | 14 | One feature changes by a rule | Watching everything at once |
| 18 | `rs-18-mirror-fold` | 10 | Reflection flips one axis; unfolding doubles | Rotating instead of reflecting |
| 19 | `rs-19-cube-count` | 13 | Opposite faces never touch; count by layer | Treating adjacent faces as opposite |
| 20 | `rs-20-number-figures` | 13 | The same rule works in every figure | A rule that fits one figure only |

### Part 5: APSC aptitude (69 questions, 16 units)

| # | Lesson id | Past questions | The real idea | Note |
|---:|---|---:|---|---|
| 21 | `rs-21-data` | 13 | Read the question's unit before the numbers | Generated from original data sets |
| 22 | `rs-22-communication` | 34 | Listening, feedback and context | APSC only, and written by hand |
| 23 | `rs-23-decisions` | 22 | Weigh duty, safety and fairness | APSC only, and written by hand |

## How questions are made

- **Parts 1 to 4 are mostly generated.** Most puzzles can be computed, so a Python
  generator builds each step with several variants and computes every answer. A retry or
  review shows a new puzzle under the same permanent step id, which is a real test of
  delayed recall. This is the Mathematics method.
- **Word lessons are written by hand.** Analogy, odd one out, statements, communication
  and decisions depend on meaning. Each English and Assamese pair must keep the relation.
  A pair that only works in one language is dropped.
- **Judgement questions need care.** Lessons 22 and 23 have no official reasoning in the
  sample, and these answers can be arguable. Teach the principle, explain the keyed
  answer, and avoid questions with no clear best choice.
- **Past papers set the pattern only.** Never copy their wording, numbers, figures or
  option sets, and never label a question with an exam unless its provenance is verified.
- **Figures are drawn by code as original SVG.** Past-paper images are never reused.

## Scenes

Reasoning has no history to frame, so the action must be the reasoning itself. The
[scene rules](MATHEMATICS-VISUALS.md) apply: no answer before action, and do, then discover.

| Scene | Lessons | The act |
|---|---|---|
| `alpha` | 1, 3, 6 | Fold the alphabet in half; opposite letters meet |
| `gaps` | 2, 3 | Tap between terms to open each level of differences |
| `shift` | 6 | Slide one alphabet against another until the code lines up |
| `walk` | 9 | Turn and step; the compass follows the walker's facing |
| `tree` | 10 | Place people by generation and mark gender only when it is stated |
| `queue` | 11 | Slide a person and watch both ranks change together |
| `seats` | 12 | Place fixed people, then test what is left |
| `oddday` | 13 | Step through months on a seven-point wheel |
| `hands` | 13 | Run the clock and see the minute hand gain on the hour hand |
| `venn` | 14, 15 | Tap regions; for logic, try every diagram the premises allow |
| `reflect` | 18 | Flip a figure across an axis, or fold and unfold a sheet |
| `die` | 19 | Roll a die and unfold it to find the opposite faces |

Also built during the course: `seats`, `figpick`, `dicenet`, `numgrid` and `bars`. In place
of the planned `reflect` and `die` scenes, figures use `figpick` and `dicenet`.

## Engine work

Findings from reading the code:

| Item | Finding | Work |
|---|---|---|
| Skills, placement, drills, `variants` | The `skills`, `diagnostic` and `drill` paths already take a course id | Reuse. Check each one with a second course |
| Typed answers | The `solve` keypad and its check accepted numbers only | **Done:** `input: "letters"` on a `solve` step |
| Exercise-book look | Was hard-coded for Mathematics | **Done:** `AXOM.notebook(cid)` in `app/common.js`. No course field was needed, so Mathematics JSON stayed unchanged |
| "Paintings" footer | Was hidden for Mathematics only | **Done:** uses `AXOM.notebook` |
| New scenes | All scenes are built | **Done**, in `app/reasonstage.js` |
| Widget list | `WIDGET_KINDS` is fixed in `scripts/build.py` | **Done.** Add each new scene |
| Checks | `scripts/check_math.py` covers Mathematics files only | **Done:** `scripts/check_reasoning.py`, called by `scripts/verify.sh` |
| Browser helper | `scripts/autoplay.js` plays known step types | **Done** |

After each engine change, `python3 scripts/build_math_course.py` must leave the
Mathematics content unchanged.

Traps found while building the pilot:

- `T()` writes HTML spans, so it cannot go in an SVG attribute or SVG text. Use `ST()` in
  `app/reasonstage.js`. Build checks cannot see this; look at each new scene.
- A variant inherits any field it omits. Set `traps` on every variant, even if empty.
- An `unscramble` word is a list of tiles, not a string.

Generator files: `scripts/build_reasoning_course.py`, with modules in
`scripts/reasoning_course/`. It reuses helpers from `scripts/math_course/`, so changing
those can affect this course. As with Mathematics, edit the generator, not
the generated JSON. Skill ids take the prefix `r-` so they cannot collide with Mathematics
in saved progress. `scripts/check_reasoning.py` should recheck each generated answer
independently, require variants on generated steps, and reject duplicate options.

## Assamese

- Assamese numerals follow the app's existing number display.
- Letter puzzles keep the Latin alphabet in both languages, because the alphabet is the
  content. Instructions and explanations are in Assamese. The 2022 ADRE Grade IV paper
  supports this: page 80 prints a letter-coding question once, in English, while the word
  questions beside it appear in Assamese, Bengali, Hindi and English. That is one page, so
  look again if a later paper differs.
- New Assamese stays pending editorial review.

## Build order

1. **Check.** Done: see "Assamese".
2. **Prepare the engine.** Done, with Mathematics content unchanged.
3. **Pilot in draft.** Done: `rs-06-coding`, `rs-09-direction` and `rs-14-venn`, using
   `draft: true` with the catalog entry left as coming soon.
4. **Check the pilot.** Browser play is done. Learner testing was skipped at the owner's
   direction. **Still worth doing:** compare completion, enjoyment and 7-day recall.
5. **Finish Parts 1 to 3.** Done. These cover 303 of the 423 past questions.
6. **Add Part 4.** Done.
7. **Add Part 5.** Done.
8. **Add placement and release.** Placement and the catalog entry are done. Release is not.

## Release gates

- Mathematics is already merged to `main` on GitHub, and this course depends on its skill
  system. Confirm `firestore.rules` is deployed before releasing either.
- `scripts/verify.sh` and `scripts/audit_lessons.py` pass.
- Every lesson plays in English and Assamese, including mistakes, retries and the 80%
  first-attempt gate.
- Test-outs, checkpoints and placement never retry questions.
- A generated-answer sample has been checked by a person, because a generator can be
  consistently wrong.
- Completion and recall are tracked separately. The skill states stay a working estimate
  until tested with learners.

## Later

**Speed rounds.** Exams are timed, and this course does not train speed yet. An optional
timed round could open once a skill is strong. Its time should be stored separately and
never update mastery. Design it after learner testing shows how long people take.

**Revisit after learner testing:** whether Parts 4 and 5 deserve their size.
