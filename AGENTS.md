# Axomrank working instructions

## Current user objective

Revamp Assam History so short historical missions are enjoyable and facts remain
remembered after a delay. Start with the bounded daily memory mission, then the
three-lesson mission and fact-linked review pilot in `docs/EXPERIENCE-REVAMP.md`.
The user also requested a repository cleanup: remove only verified disposable
artifacts, and preserve user-owned untracked files and historical provenance.
The user chose **one agent** on 2026-11-02. Do not delegate unless they change
that preference.

Read `docs/EXPERIENCE-REVAMP.md`, `docs/HISTORY-COMPLETION.md` and
`docs/history-completion.json` before expanding the revamp. The required
curriculum is implemented locally according to the measured completion record;
Assamese editorial review is deferred and the final browser recheck remains
outstanding. Measure actual files before reporting completion or publication.
A private draft is not a published or reviewed lesson.

Experience changes must keep the history as evidence, not game fiction. A
mission may frame a puzzle, but it may not invent dialogue, sources, dates or
alternative outcomes. Track engagement and delayed recall separately. Treat
reward systems and mission formats as design hypotheses to test with learners.

## Sources and pictures

The user authorised reuse of `/home/angsuman/extra_spac/Assam History`.
Read that library's `AGENTS.md`; filter `INDEX.csv` to find assets. Treat its
research summaries as leads, with their uncertainty intact. Read actual source
passages before making factual claims. Primary editions are also available in
`/home/angsuman/extra_spac/Primary source`. Keep both source folders unchanged.
Copy selected pictures into this project's media tree and record provenance in
`docs/research/`. Generated scenes are artistic interpretations, not evidence.

## Lesson contract

Read `docs/LESSON-DESIGN.md` and the relevant curriculum section. Use the
individual curriculum row's unit budget when it differs from generic tier
ranges. Write English and Assamese together. A unit has one story beat, four
learned points, two or three short visual story cards and five to seven varied
exercises with explanations. Match interaction to the fact; avoid repeated MCQ
drills. Connect prior learning where the connection is meaningful.

Every lesson and exercise id is permanent once published. Existing learners'
completion, mistakes and spaced review depend on these ids. New course copies
need new ids. Keep dates, traditions and disputed identifications distinct.
Never invent exam provenance, source passages, historical dialogue or reviews.
New Assamese prose must retain pending editorial-review status until reviewed.
New fact ids may link existing questions, but must never replace published step
ids. Migrate progress before changing the review data model. A successful retry
must not inflate first-attempt accuracy or a delayed-mastery claim.

## Implementation and verification

This is a static HTML/CSS/JavaScript PWA. Content is JSON; `app/engine.js` owns
the player, `app/home.js` owns navigation, `app/common.js` owns local progress
and spaced review, and `app/sync.js` owns Firebase sync. Source records, maps
and tappable entities are shared. Course entries use `kings` even for topics
that are not rulers. Eras use numeric `from`/`to` ranges.

Run `python3 scripts/build.py` before delivery. It validates references and
assets, creates missing image thumbnails, regenerates the manifest and stamps
the service-worker version. It does not verify historical accuracy or fluent
Assamese. For new units also run `scripts/audit_lessons.py` with their paths.
Use the existing `scripts/autoplay.js` browser helper for meaningful player
checks in English and Assamese, including mistakes/retries and first-attempt
80% gates. Test-outs and checkpoints must not retry questions.

Keep user-owned untracked files, including the pre-existing
`scripts/preview_drafts.py`. Do not run its hard-coded external output path
without inspecting it. Keep previews and browser artifacts out of commits.
`output/` is also user-owned and must be preserved. Disposable ignored browser
and Python caches may be cleaned after confirming they are generated artifacts.
