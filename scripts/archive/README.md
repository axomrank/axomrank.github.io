# Archived scripts

**Do not run these.** They are finished one-time migrations for Assam History,
kept as provenance for how the released content and permanent ids were made.
Released lessons are edited in `content/`, so a rerun could regenerate ids or
overwrite later editorial changes.

They moved here on 2026-11-06 and had no other users apart from the older
`docs/authoring/` briefs. Their paths were updated for this folder. In a
throwaway copy, `unify_assam_history.py`, `integrate_british_course.py` and
`integrate_medieval_course.py` refuse to run against the released content.

| File | What it did |
|---|---|
| `compact_ahom.py`, `compact_ahom_spec.py` | Built the compact Ahom lessons from the reign lessons |
| `unify_assam_history.py` | Merged the separate courses into `assam-history` |
| `integrate_british_course.py`, `integrate_medieval_course.py` | Imported those authored courses |
| `import_curated_course.py` | Imported the curated courses listed in `docs/authoring/*_course.json` |
| `compile_history_units.py`, `lesson_authoring.py` | Helpers for these imports and the older briefs |
| `expand_history_banks.py` | Added exam-format questions from keyed exercises |
| `enrich_history_reference.py` | Enriched the glossary and guides from authored unit facts |
