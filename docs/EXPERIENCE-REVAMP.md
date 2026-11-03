# Assam History experience revamp

Status: active plan, 2026-11-02. This is the product plan for the next release,
not a claim that the full experience revamp is implemented or learner-tested.

## Goal and evidence

Players should want to finish a short historical mission and be able to recall
its important facts days later. Measure enjoyment, completion and delayed
recall separately. No design can promise that nobody will be bored.

The current course has 93 core lessons, 382 units and 27 era checkpoints.
Each core unit already has visual story cards, varied exercises and feedback.
The player has XP, streaks and step-level review at 1, 3, 7, 15 and 30 days.
In the current 1,934 unit exercise interactions, true/false, inline choice,
matching and fill account for 1,373 (71%). This is a potential rhythm problem,
not measured user boredom. The full review queue used to open a 15-question
round while the home card displayed the entire due count.

Research supports retrieval practice, spaced practice and corrective feedback
for durable recall. Gamification has positive average learning effects, but
motivational effects vary by design and study quality. Mission framing, a
collection and precise pacing therefore need a pilot rather than a promise.

- [Classroom quizzing meta-analysis](https://pubmed.ncbi.nlm.nih.gov/33683913/)
- [Distributed practice synthesis](https://pubmed.ncbi.nlm.nih.gov/16719566/)
- [Feedback and spacing in a learning app](https://pubmed.ncbi.nlm.nih.gov/34867656/)
- [Gamification meta-analysis](https://link.springer.com/article/10.1007/s10648-019-09498-w)
- [Retrieval question-format experiments](https://pubmed.ncbi.nlm.nih.gov/24059563/)
- [Interleaving and discrimination study](https://pubmed.ncbi.nlm.nih.gov/30877483/)

## Player journey

Course: explore Assam through time. Era: enter a historical setting. Lesson:
complete a mission. Unit: solve one small objective. Checkpoint: use evidence
from several missions. Daily return: recover older facts in a short memory
mission. The unit loop is **question or mystery → visual discovery → action →
reasoned feedback → independent recall → later return**.

Puzzle frames may ask a player to restore a chronology, identify a figure,
trace a route, distinguish two records or curate a sourced exhibit. Player
choices may change task order or clues, but not historical outcomes. Existing
artistic reconstructions must stay labelled as such.

## Delivery sequence

| Phase | Work | Acceptance gate |
|---|---|---|
| 1. Short return mission | Cap a round at eight, prioritize mistakes, vary lessons, show total waiting and offer another optional round. Preserve all due records. | English and Assamese rounds finish with correct counts; repeated rounds advance through the backlog; no lost progress. |
| 2. Fact model | Introduce stable fact ids linked to existing step ids. Record first attempt, hint use, retrieval format and delayed success without replacing current SRS. Migrate saved data before retiring any step-level field. | One fact can be tested by two different prompts; published ids and old progress still work. |
| 3. Mission pilot | Redesign three contrasting lessons: `ahom-07-saraighat` (narrative), `early-assam-01` (place and evidence), `assam-culture-05` (manuscripts). Use their actual source passages; write English and Assamese together. | Each mission has a visible objective and result; lesson contract, sources, accessibility, offline play and 80% first-attempt gates pass. |
| 4. Feedback and variety | Add correction after false answers, distinguish common confusions, and use a different recall format on delayed review. Keep spelling puzzles rare. | Error recovery improves without increasing false mastery; no repeated format merely to fill a quota. |
| 5. Journey and collection | Show completed missions, remembered facts and sourced person/place/object cards; allow choice between next story and memory mission. | Cards can become retrieval prompts; completion and delayed recall remain visibly distinct. |
| 6. Rollout | Apply successful patterns across the remaining course, then consider cooperative features and exam tools. | Delayed recall and completion improve in the pilot at a reasonable time cost before wider rollout. |

Phase 1 is implemented locally. The browser check used a 12-question due
fixture: the first round showed eight, a later round continued from the
remaining backlog, and both English and Assamese completed through the
existing autoplay helper. A deliberate English mistake was retried without
inflating first-attempt accuracy. At 390px, the Assamese completion screen
had no horizontal overflow. `scripts/check_daily_review.cjs` checks the
selection and preservation rules. These checks do not measure real learner
enjoyment or delayed retention. Phases 2–6 remain planned.

Lesson 1 (`early-assam-01`) is the first Phase 3 visual preview. It has a
bilingual evidence-file objective across three existing units, stage progress,
a result after each unit, and an interpretive archaeology illustration. It
retains every published lesson and step id, question and pass rule. Its new
Assamese mission copy remains pending educator review. At 390px, the player
completed all three units in English/Assamese with no overflow. A 4/6
first-attempt lesson test failed despite successful retries; a later 6/6
Assamese test passed. The other two pilot lessons and learner outcome study
remain planned.

## Pilot measures

Compare existing and mission versions on equivalent facts. Record first-attempt
accuracy immediately, after 7 days and after 30 days; unfamiliar question
variants; unit exits; completion; voluntary return; mistakes corrected later;
and minutes spent. Collect a short optional enjoyment response. Review results
by language and mobile viewport. Do not use XP, time spent or immediate scores
alone as evidence of learning. Collect only data needed for these measures.

## Guardrails

- Keep published lesson and step ids. New fact ids are additional metadata.
- Verify factual wording in actual source passages; research summaries are leads.
- Preserve source provenance, uncertainty and the artistic-interpretation label.
- Keep new Assamese copy pending editorial review until a human review occurs.
- Run the build, design audit for new units, English/Assamese player runs,
  mistake/retry tests, first-attempt gates and mobile/offline checks.
- Preserve user-owned `output/`, `scripts/preview_drafts.py` and `private/`.
