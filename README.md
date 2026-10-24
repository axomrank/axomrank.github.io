# Axomrank · Assam government exam preparation

Short, game-like, bilingual (English and Assamese) lessons for ADRE, Assam TET, APSC and Assam Police SI. It works offline and can be installed from the browser.

**Live:** https://axomrank.pages.dev (also https://axomrank.github.io/)

**Courses:** Ahom Kings (41 reigns, 1228–1838) is the first course. More subjects (Assam geography, polity, economy, culture, current affairs, general studies) follow the same lesson format; see [docs/PLAN.md](docs/PLAN.md) and [docs/CURRICULUM.md](docs/CURRICULUM.md).

## Documentation

| File | What |
|---|---|
| [docs/PLAN.md](docs/PLAN.md) | Project plan and roadmap |
| [docs/CURRICULUM.md](docs/CURRICULUM.md) | All Assam history: courses, eras, build order |
| [docs/LESSON-DESIGN.md](docs/LESSON-DESIGN.md) | How lessons, story cards and exercises are written; the learning loop |
| [docs/SETUP.md](docs/SETUP.md) | Hosting, Firebase, publishing |

## Layout

```
index.html, lesson.html   course home and lesson player
sw.js, manifest.webmanifest   offline support and install (sw.js version is stamped by build.py)
_headers, _redirects      Cloudflare Pages caching and redirects
app/                      config.js (services), common.js, engine.js (player), home.js, sync.js, app.css
content/                  courses/, lessons/, questions/, maps/, media/, entities.json, manifest.json (generated)
icons/                    app icons
scripts/                  build.py (check + manifest), import_kmz.py, deploy_cloudflare.sh, deploy_rules.sh, autoplay.js
docs/                     plan, curriculum, lesson design, setup
firestore.rules           Firestore security rules
private/                  local only, git-ignored (grants, raw map files, drafts)
```

## Adding a lesson

1. Write `content/lessons/<id>.json` (`suteuphaa.json` and `subinphaa.json` are models) following [docs/LESSON-DESIGN.md](docs/LESSON-DESIGN.md). Give every step a unique, permanent `id`.
2. Put images in `content/media/<id>/`; add new names to `content/entities.json`.
3. Add the lesson to its course outline in `content/courses/` and its exam questions to `content/questions/`.
4. `python3 scripts/build.py`, then publish (see [docs/SETUP.md](docs/SETUP.md)).
