# Repository cleanup

The repository keeps what the hosted app, its build and checks, and future
lesson work need. Everything else lives in git history.

## Restoring something

Every file removed here is in commit `6df7725`:

```bash
git checkout 6df7725 -- docs/authoring
```

Replace the path with whatever you need.

## Removed from the repository (2026-11-06)

| Path | What it was |
|---|---|
| `scripts/archive/` | Finished Assam History migrations and helpers |
| `docs/authoring/` | Briefs and scripts that created released lessons, plus pre-unification snapshots. No live script used them, and rerunning them could reset released courses. |
| `docs/GLASS-UI.md` | Verification log for the finished interface change |
| `docs/research/` process logs | `css-only-image-plan.json`, `css-only-generation-progress.json`, `css-art-corrections.json`, `generic-art-library-audit.csv` and `.md`, `choice-normalisation.json`, `history-unification.json`, `integrated-history-index.json` |
| 62 images in `content/media/` (1.8 MB) | Files whose names appear nowhere in shipped content |
| Ignored `.playwright-cli/`, `__pycache__/`, `.wrangler/` | Generated caches |

## Removed with the interface redesign (2026-11-06)

- `content/media/interface/brahmaputra-glass.webp` and its thumbnail: replaced by
  `axom-river.webp`, built from it. See `docs/research/glass-interface-art.md`.
- The exercise-book page styling in `app/math.css`: Mathematics and Reasoning now use
  the glass theme. Their scenes and widgets stayed.
- The dark-mode branches of `app/app.css` and `app/glass.css`: the interface is one
  light theme painted over the river.

## Kept on purpose

- `docs/research/` source and picture registers: the licence and attribution
  record for pictures that still ship. The checks also read the Constitution
  register, and the course documents cite the others.
- Identical images in different lesson folders (3 MB): each is in use, and merging
  them would mean editing published lessons.
- `content/courses/ahom-kings.json`, its bank and optional lessons: saved links and
  learner progress depend on them.
- `private/` and `output/`: user-owned, on neither host, and not recoverable
  from git.
- `scripts/preview_drafts.py`: user-owned draft preview tool.

## Known issue

`scripts/build_india_map.py` cannot run, because `world.json` survives only in
the Trash. `content/maps/india.json` itself is intact.

## 2026-11-06: dropped course plans

The user dropped Economy, Current Affairs and Assamese Language as not required.
`docs/ECONOMY-COURSE.md`, `docs/CURRENT-AFFAIRS-COURSE.md` and
`docs/ASSAMESE-LANGUAGE-COURSE.md` are deleted, along with the Economy subject and the
Current Affairs "coming soon" entry in `content/catalog.json`. Git history keeps them.
