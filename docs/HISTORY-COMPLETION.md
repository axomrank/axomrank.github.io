# Assam History implementation complete locally

Measured 2026-11-02. The user requested one agent and explicitly deferred Assamese editorial review. Publication to both existing sites was requested after the local review. Release files pass the checks below;verify deployment against `content/manifest.json` on each host.

- **93 core lessons / 380 units**, covering every required curriculum row.
- **41 optional Ahom deep-dive lessons / 152 units** retained.
- **134 lessons / 532 units / 2,651 practice questions** in total; 2,575 questions belong to core courses.
- Assam History is one visible course: 93 lessons and 27 checkpoints. Former core course definitions and banks are in git history (see `docs/CLEANUP.md`). Old course-home links redirect;original lesson and exercise ids retain progress.
- `history.html` provides the searchable cross-course timeline and people/place index: **573 dated entries and 697 linked names**.
- Source and image-provenance registers are under `docs/research/`. Historical reconstructions are labelled as artistic interpretations. No invented PYQ or human-review provenance.

## Learning loops and compatibility

All 93 core lessons meet the design audit: four bilingual learned points, two or three story cards, five to seven exercises, at least four exercise types, story before retrieval. Older compact lessons were completed to the same standard. Longer original narratives moved into the guidebook’s “More context” section; their ids and text remain available. All previously tracked lesson/exercise ids were preserved.

The player accepts spaces and dates in typed answers. Lesson tests require 80% on first attempts; successful retries cannot inflate the score. Test-outs, jumps and checkpoints do not retry. Bank-only question ids are not written into lesson-only review queues. The service-worker installation includes every integrated course and its bank, so offline home loading does not depend on only the four original courses.

## Verification

Passed: full build, all 93 core lesson-design audits, curriculum counts, question source-step references, exam tags, duplicate-choice checks, permanent-id preservation, JavaScript syntax, and player state-transition checks for pass gates and retry behaviour. Before the final glossary, reference and legacy-loop edits, **544 bilingual unit runs** completed without stuck exercises or horizontal overflow.

**Final browser recheck not executed:** automatic approval review could not complete because the account usage limit was reached. This affected the new reference UI and final legacy-loop/glossary changes. They passed local structural and state checks, but a final live-browser/offline recheck is still outstanding. This is a verification limitation, not missing curriculum content.

Assamese educator review remains deferred as instructed. Existing optional deep-dive content keeps its original narrative structure; the stricter design audit is enforced on the 93 core lessons. The user-owned `scripts/preview_drafts.py` is preserved.

## Reproduce checks

```sh
python3 scripts/build.py
python3 scripts/check_history_completion.py
node scripts/check_learning_gates.cjs
node --check app/engine.js
node --check app/history.js
node --check sw.js
```

## Single-course consolidation

The unified course has 2,575 core practice questions and a continuous global lesson order. Foundations precede the three dynasties;the end-of-Kamarupa transition follows them. Checkpoint era ids and their lesson membership are retained. Original optional deep-dive endpoints remain hidden for compatibility with saved links.

The build regenerates `content/history-reference.json`, the manifest and service-worker version. One-time import/enrichment scripts must not be rerun over published ids. Subsequent editorial changes belong in the integrated JSON files.

Unified-course browser checks passed: 390px mobile layout, 27 sections, transitions from foundations to Varman and from modern Assam to culture, English/Assamese lesson tests, a 15-question checkpoint, and old-course redirects. No overflow or JavaScript errors appeared in these checks. Local preview: http://127.0.0.1:8773/index.html?course=assam-history&all .

## Chapter2 expansion,2026-11-03

The current local scope is93 core lessons /382 units,plus41 optional lessons /152 units:134 lessons /534 units total. Chapter2 retains its original four units and published IDs,and appends two researched extension units on Naraka’s origins and the Kamakhya building challenge. New Assamese editorial review remains pending. See `docs/research/early-assam-02-legends-research.md` for sources,variants and emblem checks. Earlier counts above describe the2026-11-02 baseline.
