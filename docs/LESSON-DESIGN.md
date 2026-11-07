# Lesson design standard

How every Axomrank lesson, in every course, is written and how the player behaves. `scripts/build.py` enforces the rules marked (build).

## Never boring

The app must feel like a game, not a textbook: short units, a story first, a different kind of exercise every time, instant feedback with the reason, and visible progress on one path through the whole course. Anything repetitive or dull is a bug.

- **Unit:** one story beat. 2–3 short story cards (with a painting, map or art), then 5–7 exercises. 3–5 minutes.
- **Lesson size by tier:** A = 6–8 units, B = 4–6, C = 2–3 (a lesson = one king, one movement, one event, one topic).
- **Every unit:** 4 `learned` points; `link` to earlier units or lessons where the story really connects.
- **Exercise mix:** prefer whoami, map, timeline, picture, tf, unscramble, spot, fill, match, order, odd. Plain `mcq` is rare: at most one exam-style "consider the statements" question in a lesson test. Match the type to the fact: place → map, date → timeline, person → whoami, scene → picture, trap → tf or spot.

| Type | Plays as | Use for |
|---|---|---|
| story | Short cards with a picture | The narrative |
| whoami | Clues appear one by one; earlier guess = more XP | People, peoples, offices |
| map | Tap the right spot or river | Places, borders, routes |
| timeline | Drop events before, between or after anchor years | Dates and sequence |
| picture | Pick the right painting or photo | Scenes, monuments |
| tf | One statement, two big buttons, then the reason | Exam traps |
| unscramble | Rearrange letters or syllables | Names and terms |
| spot | Tap the wrong word | Common confusions |
| fill / inline | Type or pick the missing word | Key words |
| match | Tap matching pairs | Who did what |
| order | Tap events in order | Sequences |
| odd | Pick the one that does not belong | Groups |
| figtap | Tap the right numbered pin on a drawn figure (`kind`, `answer`, `answerText`) | Parts of a process or place |
| mcq | Standard multiple choice | Exam practice, sparingly |

## Lesson file

`content/lessons/<id>.json`: `sources`, `guide`, `map`, `units` → `steps`. Every text is `{ "en", "as" }`. Every step has a permanent `id`: **never change an id once published**, saved progress, review and mistakes refer to it. Names in text are `[[id]]` or `[[id|shown text]]` and must exist in `content/entities.json`. `map`: a `box` [west, south, east, north], the rivers, ridges and places to `show`, optional `routes`, `texts`, `labels`; positions are [lat, lon]. Images: WebP about 1080 px in `content/media/<id>/` (build makes the `@480` copies).

A story card may use `figure: {kind, spots}` from `app/geofigure.js`: a drawn scene with numbered pins, one `spot` label per pin. Prefer it to a `diagram` chip grid.

## Story cards: the one design

Built by the engine; the author writes text and picks a picture.

1. **Hero** painting or line art runs edge to edge above a glass card. A map, diagram, widget or captioned document sits inside the card instead; the first year on the card shows as a red stamp.
2. **Kicker** "UNIT 3 · STORY" with one progress dot per paragraph.
3. **Title:** at most 6 words, a hook, not a label ("Blood on the forehead").
4. **Lede:** the first paragraph, larger; it must make sense alone.
5. **Beats:** each further paragraph appears on the next tap. A last paragraph ending in a question becomes the green "Think about it" card.

Limits (build): at most 3 paragraphs, 35 words per paragraph, 55 words per card (English). One idea per paragraph.

Emphasis, never mixed: `<mark>` = the key fact (max 3 per card); `[[entity]]` = a tappable name; years are styled automatically; `<b>` = lists of names and memory-trick letters.

## Constitution course additions

`[[art-21a]]` opens an article's official heading. A `timeline` step with `"scale": "articles"` plays as an article line: anchors are plain article numbers and `items` hold the provisions, including lettered ones. A course entry's `reign` may be bilingual. A course with `"draft": true` needs no catalog place, stays off the home page and opens only by its direct link.

## Indian History additions

A lesson or story `map` may set `"base": "india"`; the default is `"assam"`. See the map authoring rules in [INDIAN-HISTORY-COURSE.md](INDIAN-HISTORY-COURSE.md).

## Mathematics additions

`solve`, `explore` and `stepwise` steps, story-card widgets, number `variants`, `skill` and `traps` fields and `$...$` maths come from `app/math.js`. See [MATHEMATICS-COURSE.md](MATHEMATICS-COURSE.md). A step with `variants` keeps one permanent id across all its versions.

## Reasoning additions

The Reasoning course adds the scenes in `app/reasonstage.js`, listed in `WIDGET_KINDS` in `scripts/build.py`, and `"input": "letters"` on a `solve` step. See [REASONING-COURSE.md](REASONING-COURSE.md).

## Learning loop (in `app/engine.js`)

- A missed question in a unit or lesson test returns once at the end. Match does not repeat.
- Test-outs, "Jump here" tests and checkpoints never repeat questions; the 80% pass mark counts first attempts.
- Missed questions go to the lesson's mistakes list and to daily review (1, 3, 7, 15, 30 days; a wrong answer resets to day 1).
- Passing a lesson test (80%+) opens Unit 1 of the next lesson. Add `?all` to unlock everything for review.
- Rewards: XP, daily streak, stars, surprise "Did you know" cards.

## Experience revamp in progress

The product-level mission and memory plan lives in
[EXPERIENCE-REVAMP.md](EXPERIENCE-REVAMP.md). Keep the contract above while
piloting it. A mission has a visible historical puzzle and result; its actions
must help answer that puzzle. Review is now presented as a bounded memory
mission of up to eight questions, with the remaining queue preserved and an
optional next round. This first slice still schedules individual step ids.
Fact-linked variants and delayed-mastery states are planned, not yet shipped.

The Lesson 1 pilot uses optional `mission` metadata: the lesson supplies a
bilingual `label`, `title` and `hook`; each unit and the lesson test supply a
bilingual `objective` and `result`. The player shows a progress board on the
path, an objective during play and a recorded finding on completion. These
fields frame existing sourced material; they do not replace story cards,
exercises or permanent ids. The build checks both languages when a mission is
present.

## Library image captions

A story may add bilingual `imageCaption` metadata to identify its illustration, especially when it is contextual rather than a depiction of every claim. `imageLayout` is `wide` for scenes or `contain` for objects and character sheets. The caption sits below the image, while the artistic-reconstruction label stays on the frame. New Assamese captions retain pending editorial-review status. Library origins, hashes, licence and card uses are recorded in `docs/research/generic-art-library-assets.json`.
