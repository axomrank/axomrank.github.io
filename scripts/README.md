# Scripts

Run everything from the repository root. Before delivery, run:

```bash
scripts/verify.sh
```

It runs `build.py` and all `check_*` scripts, and stops at the first failure.
Nothing in `scripts/` is deployed or loaded by the app.

## Build and checks

| Script | Purpose |
|---|---|
| `verify.sh` | Build plus every check below |
| `build.py` | Validates content, makes `@480` thumbnails, writes `content/manifest.json` and `content/history-reference.json`, stamps `sw.js` |
| `build_history_reference.py` | Called by `build.py`; do not run it separately |
| `audit_lessons.py <paths>` | Lesson-design audit for new units |
| `format_story_beats.py <paths>` | Splits an overlong bilingual story paragraph at aligned sentences |
| `check_math.py`, `check_skill_model.cjs` | Mathematics content and mastery rules |
| `check_reasoning.py` | Reasoning content, and answers recomputed from question text |
| `audit_math_division.py` | Lists `//` divisions that drop a remainder, for a person to check |
| `check_constitution.py`, `check_indian_history.py`, `check_history_completion.py` | Course scope and content |
| `check_daily_review.cjs`, `check_learning_gates.cjs` | Review queue, retries, 80% gates, test-outs, checkpoints |
| `check_asof.py` | Lists lesson facts whose `asOf` date is over 12 months old; never fails |
| `autoplay.js` | Browser helper for player checks, loaded into a running page |

## Generators

Each was rerun on 2026-11-06 unless noted. "No change" means the output matched
the committed files exactly.

| Script | Writes | Rerun result |
|---|---|---|
| `geo_stills/render.sh` | Re-draws the Geography Foundations diagram images (`content/media/gf-*/…webp`) from `geo_stills/stills.js` with headless Chrome; needs the local server on port 8770. `geo_stills/gallery.html` and `still.html` preview every figure | Overwrites those images with the same drawing |
| `build_math_course.py` | `math-*` lessons, Mathematics course, bank and skills | No change |
| `build_reasoning_course.py` | `rs-*` lessons, Reasoning course, bank and skills | No change; course tiles are made only if missing |
| `build_constitution_bank.py` | Constitution bank | No change |
| `build_indian_history_bank.py` | Indian History bank | No change |
| `add_article_entities.py` | `art-*` entries in `content/entities.json` | No change |
| `import_kmz.py <kmz>` | `content/maps/assam.json` | No change, using the KMZ in `private/` |
| `build_india_map.py` | `content/maps/india.json` | **Cannot run.** Its input folder has moved, and `boundaries.json` is now in `../MAP/data/maps/`, but `world.json` survives only in the Trash. The shipped map is fine. |

`build_math_course.py` overwrites the Mathematics files, so change the generator
and never the JSON. Its lesson modules are in `math_course/`: add new lesson
functions there and register them in `build_math_course.py`. `math_kit.py` holds
the shared step helpers. Reasoning lessons are in `reasoning_course/`, and reuse
`math_kit.py`.

## Deployment

`deploy_cloudflare.sh` publishes the site and `deploy_rules.sh` publishes
`firestore.rules`. `authorize_domain.sh` adds domains to Firebase Auth's
authorized domains (Google sign-in). All three change live services, so run
them only when asked; publish rules before the site when the data model changes.
`deploy_cloudflare.sh` uses `$TMPDIR`, falling back to `/tmp`.

## Other folders and files

- `preview_drafts.py`: user-owned. Read it before running it,
  because it replaces its hard-coded output folder.
