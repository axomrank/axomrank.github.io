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

## 2026-11-06 audit

Goal: make the repository easier for future agents to edit safely. Every shipped
file stayed byte-identical.

### Removed

- Ignored `.playwright-cli/` logs, `scripts/__pycache__/` and an empty
  `.wrangler/` folder. All are recreated on demand.

### Reorganised

- Ten finished Assam History migrations and their helpers moved to
  `scripts/archive/`, with paths updated. This completes the dependency audit
  noted above: nothing in the app or current pipeline uses them.
- Math lesson modules moved to `scripts/math_course/`. `build_math_course.py` and
  `audit_math_division.py` stayed in `scripts/`, because generated lesson data and
  the documents cite the generator's path.
- Added `scripts/verify.sh`, `scripts/README.md` and `scripts/archive/README.md`.

### Measured and left in place

- 62 media files (1.8 MB of 138 MB) have no literal reference in shipped content.
  Some are provenance records or pre-unification images. Removing them saves
  little and risks a missing picture.
- 24 groups of identical images (3 MB) sit in different lesson folders. Merging
  them means changing published lesson JSON, which is not worth the saving.
- `docs/authoring/` stayed in place. Its code and archived snapshots are provenance,
  and its filename prefixes already group it by course.
- `docs/research/` stayed in place, including the large image-plan and progress
  logs, because it records picture provenance.
- The four document changes already uncommitted at the start were left for the
  user, apart from removing one stale sentence about `AGENTS.md` in
  `docs/INDIAN-HISTORY-COURSE.md`.

### Known issue

`scripts/build_india_map.py` cannot run, because `world.json` survives only in
the Trash. `content/maps/india.json` itself is intact.
