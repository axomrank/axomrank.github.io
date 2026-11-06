# Mathematics course

The learner should find out what they cannot yet do, repair it on the spot, and see
that repair last. Everything here serves that loop. Lesson format and permanent-id
rules in [LESSON-DESIGN.md](LESSON-DESIGN.md) still apply.

## State of the course

| | Measured |
|---|---|
| Lessons published | All 16 topics |
| Exercises linked to a skill | 492, in 1318 versions counting number variants |
| Skills in the graph | 71, covering all 16 topics |
| Mistake patterns | 79 |
| Units, counting tests | 82 |
| Placement questions | 28, covering every topic |

Assamese text is pending independent editorial review (`review_notes` in each lesson).

## Verified on the finished course

Every lesson played start to finish in English and Assamese with no errors. Checked for a
new learner without `?all`: lesson locks, a passed test opening the next lesson, a failed
test staying failed even with correct retries, checkpoints and jump tests without retries,
test-outs, placement, drills walking back to a prerequisite, daily review on interactive
steps, and the offline app shell.

Not yet checked: pinch zoom on a real phone, real learners, and Assamese by a fluent reader.
The slides also list Algebra, Co-ordinate Geometry and Data Interpretation, which have no
decks and are not in this course. Cube roots had no deck either, but are taught in lesson 4.

## Syllabus source

Topic order comes from the 51 lecture decks the course owner supplied (Kamaleswar Baro,
KSK Educare, for ADRE Grade III and IV and DME). They are third-party teaching material:
**use them for the syllabus and question patterns only**. Do not copy their wording or
numbers, and do not label a question with an exam unless its provenance is verified.
Every question in this course is meant to be original. A comparison of deck questions with
our versions found about 40 that had kept a deck's numbers, and those were replaced. It
catches only text the PDFs expose, so numbers in image-only slides were compared by eye.
Small common values such as 10% on ₹1000 can still coincide. Many Assamese slides use a legacy font and
do not extract cleanly; read the page image if a passage matters.

| Topic | Decks | Questions in decks | Tagged ADRE 2022 |
|---|---|---:|---:|
| Number system | 1–2 | 16 | 0 |
| LCM and HCF | 3–4 | 22 | 0 |
| Simplification, squares, roots | 5–7 | 32 | 0 |
| Average | 8–10 | 35 | 0 |
| Ratio and proportion | 11–13 | 33 | 0 |
| Percentage | 14–17 | 32 | 0 |
| Profit, loss, discount | 18–23 | 47 | 0 |
| SI and CI | 24–28 | 35 | 0 |
| Time and work | 29–31 | 29 | 0 |
| Speed, distance, trains | 32–35 | 27 | 1 |
| Ages | 36 | 5 | 1 |
| Pipes and cisterns | 37 | 4 | 0 |
| Trigonometry, height and distance | 38–41 | 32 | 2 |
| AP and GP | 42–44 | 24 | 2 |
| Plane figures | 45–48 | 39 | 13 |
| Solid figures | 49–51 | 20 | 2 |

Counts come from text extraction, so treat them as rough. Tags appear only on some
decks, so a zero does not mean a topic is absent from the exam. These are planning
signals, not a measured exam distribution.

## Open-source choices

No Brilliant-style project could be dropped in, so the layer is written for this app.

| Project | Licence | Decision |
|---|---|---|
| [KaTeX](https://github.com/KaTeX/KaTeX) | MIT | **Used.** Vendored in `app/vendor/katex/` for offline use |
| [Mathigon textbooks](https://github.com/mathigon/textbooks) | No open licence found | Not usable. Studied as an idea only; no code copied |
| [Khan Perseus](https://github.com/Khan/perseus) | MIT | Rejected: its form-based exercises do not suit direct manipulation. Hint ladders and answer types inspired `solve` |
| [Numbas](https://github.com/numbas/Numbas) | Apache-2.0 | Rejected as a dependency. Randomised questions inspired `variants` |
| [JSXGraph](https://github.com/jsxgraph/jsxgraph) | LGPL-3.0 | Kept for later: a candidate for trigonometry and geometry widgets |
| [Oppia](https://github.com/oppia/oppia) | Apache-2.0 | Rejected: a full server platform |

Mastery uses Bayesian knowledge tracing, a published method (Corbett and Anderson,
1995), implemented in `app/common.js` with no dependency.

## How the learning loop works

1. **Placement** (`lesson.html?diagnostic=mathematics`). Foundations first. A miss drops
   later questions that depend on that skill. No retries, and nothing enters review.
2. **Lesson.** Story cards are playable widgets. A wrong answer in a teaching unit shows
   the likely mistake, then the idea returns at once with new numbers. Lesson tests
   retry at the end as before; placement and checkpoints never retry.
3. **My map** (course tab). Every skill with its state, the next thing to fix and the
   mistakes the learner repeats.
4. **Repair** (`lesson.html?drill=<skill>&course=mathematics`). If a prerequisite is
   the real gap, the round starts there.
5. **Delayed recall.** Daily review shows new numbers under the same permanent step id.

### What may count as evidence

These rules protect the claim that a skill is known. `scripts/check_skill_model.cjs`
tests them.

- Only first attempts update mastery. A retry never does.
- A right answer after a hint earns 5 XP and no mastery.
- "Ready" needs high probability and at least three independent successes.
- "Strong" needs a success at least three days after an earlier success.
- Engagement (XP, streak) and mastery stay separate.
- A widget must never show the answer before the learner acts. Marking both number
  lists on the LCM grid would colour the answer, so question grids mark only one.
- A skill's states are a working estimate. Test them with learners before trusting them.

## Writing more lessons

Add a lesson function to `scripts/math_lessons_*.py` and register it in
`scripts/build_math_course.py`. The topic and skills are already listed there.

```bash
python3 scripts/build_math_course.py
```
```bash
python3 scripts/check_math.py
```
```bash
python3 scripts/build.py
```
```bash
python3 scripts/audit_lessons.py content/lessons/math-*.json
```
```bash
node scripts/check_skill_model.cjs
```

- Compute every answer from the variant's numbers. Never type a result by hand.
- A numeric step needs at least two variants, and three or four is better.
- Tag a wrong answer only when it reveals a real, nameable mistake, and say what happened.
- Use `stepwise` for word problems so the map shows which step failed.
- Keep plain `mcq` for lesson tests, in the exam's four-option form.
- Write `<` in maths as `\lt`, and avoid `$...$` in titles and labels.
- `scripts/autoplay.js` plays the new step types in the browser.
- Run `python3 scripts/audit_math_division.py`: a right answer must never appear in its list, because `//` drops remainders silently.

| Step | Needs | Use for |
|---|---|---|
| `solve` | `q`, `answer`, `why`; optional `traps`, `hints`, `exact`, `prefix`, `suffix` | Typed answers on the keypad |
| `explore` | `q`, `widget`, `target`, `answerText`, `why` | Reaching a value on a widget |
| `stepwise` | `q`, `parts`, `why` | Multi-step problems |

Widgets, usable in `explore` and as a story card's `widget`: `line`, `array`, `gears`,
`tiles`, `dial`, `cuts`, `area`, `dual`, `ray`, `level`, `seesaw`, `chain`, `order`, `square`, `diffsq`, `pairs`, `ladder`, `twosale`, `growth`, `tank`, `mandays`, `track`, `journey`, `ages`, `stairs`, `triangle`, `quarter`, `tower`, `scaleup`, `shear`, `sticks`, `kite`, `roll`, `sectors`, `stack`, `net`, `pour`, `fracbar`, `grid100`, `peel`, `hops`, `blocks`.
Read [MATHEMATICS-VISUALS.md](MATHEMATICS-VISUALS.md) before adding or using one. Do-to-discover
cards are listed in `scripts/math_labs.py`.

## Before release

Deploy `firestore.rules` **before** a release that writes mastery data: it now allows
`skills` and `miscon`. Until then a learner who uses these features would have their
account sync rejected. Learners who have not used them are unaffected, because the two
fields are sent only once they hold data.
