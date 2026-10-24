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
| mcq | Standard multiple choice | Exam practice, sparingly |

## Lesson file

`content/lessons/<id>.json`: `sources`, `guide`, `map`, `units` → `steps`. Every text is `{ "en", "as" }`. Every step has a permanent `id`: **never change an id once published**, saved progress, review and mistakes refer to it. Names in text are `[[id]]` or `[[id|shown text]]` and must exist in `content/entities.json`. `map`: a `box` [west, south, east, north], the rivers, ridges and places to `show`, optional `routes`, `texts`, `labels`; positions are [lat, lon]. Images: WebP about 1080 px in `content/media/<id>/` (build makes the `@480` copies).

## Story cards: the one design

Built by the engine; the author writes text and picks a picture.

1. **Kicker** "STORY" with one progress dot per paragraph.
2. **Hero** painting, map or line art; the first year on the card shows as a terra stamp.
3. **Title:** at most 6 words, a hook, not a label ("Blood on the forehead").
4. **Lede:** the first paragraph, larger; it must make sense alone.
5. **Beats:** each further paragraph appears on the next tap.

Limits (build): at most 3 paragraphs, 35 words per paragraph, 55 words per card (English). One idea per paragraph.

Emphasis, never mixed: `<mark>` = the key fact (max 3 per card); `[[entity]]` = a tappable name; years are styled automatically; `<b>` = lists of names and memory-trick letters.

## Learning loop (in `app/engine.js`)

- A missed question in a unit or lesson test returns once at the end. Match does not repeat.
- Test-outs, "Jump here" tests and checkpoints never repeat questions; the 80% pass mark counts first attempts.
- Missed questions go to the lesson's mistakes list and to daily review (1, 3, 7, 15, 30 days; a wrong answer resets to day 1).
- Passing a lesson test (80%+) opens Unit 1 of the next lesson. Add `?all` to unlock everything for review.
- Rewards: XP, daily streak, stars, surprise "Did you know" cards.
