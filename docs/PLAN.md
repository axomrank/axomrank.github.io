# Axomrank project plan

Axomrank is a bilingual Assamese and English exam-preparation PWA for ADRE,
Assam TET, APSC CSE Prelims and Assam Police SI. It is installable and works
offline. The live sites are [Cloudflare Pages](https://axomrank.pages.dev/)
and [GitHub Pages](https://axomrank.github.io/); local changes are not live
until independently deployed and verified.

## Current state

- Assam History is one chronological core course: 93 lessons, 382 units and
  27 era checkpoints. An optional 41-lesson Ahom deep dive remains for saved
  links. The timeline and people/place index are in `history.html`.
- The player offers story cards, 13 practice types, explanations, an 80%
  first-attempt lesson gate, XP, streaks and spaced review. Progress is local
  and can sync through Firebase when configured.
- Curriculum implementation is measured in [HISTORY-COMPLETION.md](HISTORY-COMPLETION.md).
  Assamese editorial review is deferred. The final browser recheck noted there
  remains a verification item.
- The experience revamp is active. [EXPERIENCE-REVAMP.md](EXPERIENCE-REVAMP.md)
  owns its phases, evidence, pilot lessons, acceptance gates and measures.

## Product principles

1. **Remembered facts:** judge learning by first-attempt and delayed recall,
   including new question variants and time spent.
2. **A reason to act:** short historical missions give each interaction a
   visible purpose. Game framing never changes or invents historical evidence.
3. **Choice and competence:** show what is remembered, offer a manageable next
   action and reward return after a delay. XP and streaks are supporting cues.
4. **Assamese and English together:** write and test both languages in the same
   change. Never claim editorial review that has not occurred.
5. **Trust and access:** named sources, honest uncertainty, clear artistic
   labels, offline use and good performance on modest Android phones.

## Near-term work

1. Finish and verify the bounded daily memory mission. Preserve all due
   records, existing question ids and review progress.
2. Add fact links and a parallel mastery record. Migrate saved state before
   replacing any existing review field.
3. Pilot mission framing and distinct delayed recall in three contrasting
   Assam History lessons. Inspect actual source passages for any changed facts.
4. Compare completion, enjoyment and 7/30-day recall with the current flow.
   Widen the rollout only after the pilot shows a useful result.
5. Recheck the final reference and player UI in a browser, including offline,
   English and Assamese, as the completion record requires.

## Later work

- Extend successful mission patterns through the course, with an earned
  collection of sourced people, places, events and objects.
- Build verified previous-year papers, OMR-style mocks, exam-specific plans,
  weak-topic support and current-affairs workflows. Any real exam provenance
  must be documented.
- Expand to geography, polity, economy, culture and other subjects after the
  History experience is measured and maintained. The Constitution course plan
  is in [CONSTITUTION-COURSE.md](CONSTITUTION-COURSE.md). The Indian History plan is
  in [INDIAN-HISTORY-COURSE.md](INDIAN-HISTORY-COURSE.md).
- Consider optional collaboration, official-notice updates and Android/iOS
  wrappers after the learning loop works. A public leaderboard is a later
  experiment, not a requirement for the core learning journey.

## Operations

Content changes follow source inspection, bilingual writing, factual and
editorial review, build checks, player checks and deployment verification.
Private material lives in `private/`. User-owned untracked files and local
`output/` are preserved. The repository cleanup log is in
[CLEANUP.md](CLEANUP.md).
