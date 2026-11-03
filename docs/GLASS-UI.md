# Maroon glass interface

Implemented locally on 2026-11-03 from the approved glass concept. Shared styling is in `app/glass.css`, loaded after the existing player stylesheet on home, lesson and reference pages. The primary accent is `#792e49`. River art provenance is in `docs/research/glass-interface-art.md`.

The interface uses translucent ivory panels, backdrop blur, light borders, maroon actions, green success feedback and rose error feedback. Story reading uses a stronger frost for contrast. Existing content, permanent ids, saved progress, learning gates and interaction handlers were not changed. Dark mode, keyboard focus, reduced motion, reduced transparency and a solid fallback without backdrop-filter are included.

Verified with the existing player and autoplay helper:

- Build passes: 134 lessons, 7,742 combined step/question ids; service-worker version `591fd29977`.
- 390×844 home, lesson path, story, exercises and completion inspected; desktop 1280×900 inspected. Dark-mode story inspected.
- `early-assam-01` unit 1 completes in English and Assamese with deliberate true/false and inline mistakes, followed by successful retries. No autoplay horizontal-overflow issues.
- Lesson test: English retains 4/6 first-attempt accuracy after successful retries; Assamese scores 6/6. `scripts/check_learning_gates.cjs` passes the 80% rule, retries, test-outs and checkpoints.
- Home reloads offline with the new stylesheet and backdrop confirmed in the current service-worker shell cache.
- `git diff --check` passes. Browser artifacts stay in ignored `output/playwright/` and `.playwright-cli/`.

These checks cover the visual change and a representative bilingual lesson, not a new full-curriculum browser audit or learner study. No new units or Assamese prose were authored. Not deployed by this task.
