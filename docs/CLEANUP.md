# Repository cleanup audit

Audited 2026-11-02 for the experience revamp. Deletion is limited to files
whose purpose and ownership are clear.

## Removed

- Ignored `.playwright-cli/` snapshots and console logs from earlier browser
  runs. They are generated verification artifacts, not site content.
- Ignored Python `__pycache__/` files under `scripts/` and `docs/authoring/`.
  Python recreates these on demand.

## Preserved intentionally

- Untracked `output/`, including `output/practice-audit/`, and untracked
  `scripts/preview_drafts.py`: user-owned material. `output/` is ignored so
  future reports do not enter commits accidentally.
- `private/`: user-owned local source material and drafts.
- `docs/authoring/pre-unification/`: archived course and question-bank
  snapshots used to trace the unification and permanent ids.
- One-time authoring/import scripts: not loaded by the PWA, but kept for
  provenance and reproducibility until a separate dependency audit proves
  they can be archived or removed safely.
- `content/courses/ahom-kings.json`, its question bank and optional lessons:
  saved-link and learner-progress compatibility still use them.

No published lesson, exercise, source register, image or user file was removed.
