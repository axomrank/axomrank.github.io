# General Science and Environment course plan

Status: private draft since 2026-11-06. Lessons 7, 8, 10, 11 and 12 exist; open
`index.html?course=general-science` on the local server. Lesson format and permanent-id rules in
[LESSON-DESIGN.md](LESSON-DESIGN.md) apply.

A learner should be able to explain everyday things, not just recall terms.

## Why this course

| Exam | Science | Environment | Total | Share of its sample |
|---|---:|---:|---:|---:|
| APSC CCE Prelims | 29 | 31 | 60 | 11% |
| DME | 13 | 1 | 14 | 24% |
| Assam Police SI | 7 | 1 | 8 | 8% |
| Assam TET | 3 | 11 | 14 | 4% |
| Assam Police Constable | 3 | 1 | 4 | 4% |
| ADRE | 32 | 5 | 37 | 3% |

The sample is thin and scattered: most subtopics appear once. It shows the style of question
but cannot set coverage, so the **syllabus sets the coverage** and past papers only set the
weight between parts. Read the official syllabus before fixing the lesson list.

## Scope

- **Course id:** `general-science`, with lesson ids `sc-NN-slug`, in the existing `science`
  subject. Add `environment` coverage to its blurb.
- **Level:** school science for everyday life, as the catalog already says.
- **Out of scope:** numerical physics and chemistry drills. Mathematics covers arithmetic.

## Course map

12 lessons and about 48 units, 4 each, roughly 290 exercises.

| # | Lesson id | Group (past questions) | Core content |
|---:|---|---|---|
| 1 | `sc-01-motion` | Physics (21) | Measurement, motion, force, gravity, levers |
| 2 | `sc-02-energy` | Physics | Heat, light, sound, electricity |
| 3 | `sc-03-matter` | Chemistry (17) | Elements, compounds, symbols, acids and bases |
| 4 | `sc-04-everyday-chemistry` | Chemistry | Fuels, metals, reactions at home |
| 5 | `sc-05-living-things` | Biology (18) | Cells, micro-organisms, classification |
| 6 | `sc-06-plants-farming` | Biology | Photosynthesis, fertilisers, sericulture |
| 7 | `sc-07-human-body` | Health (11) | Body systems, vitamins, disease, immunity |
| 8 | `sc-08-space` | Science and technology (20) | Solar system, satellites, ISRO |
| 9 | `sc-09-technology` | Science and technology | Defence, nuclear, AI, nanotechnology |
| 10 | `sc-10-ecology` | Environment (50) | Ecosystems, biodiversity, pollution, waste |
| 11 | `sc-11-climate` | Environment | Greenhouse gases, climate action, energy |
| 12 | `sc-12-conservation` | Environment | Assam wildlife, Ramsar sites, laws, institutions |

Assam wildlife questions count: lesson 12 should use local cases. Link it to Assam Geography
lesson 4, which already places conservation sites, rather than repeating it.

## How questions are made

- **Lesson JSON, written by hand** as in Assam History, because these are facts.
- **Sources:** primary or official wherever possible, such as NCERT texts, ISRO, the
  Ministry of Environment, the Ramsar list and Assam Forest Department reports. Books are
  leads until the passage is read. Record them in `docs/research/`.
- **Stale facts:** population counts, forest cover and missions all change, so each carries
  an `asOf` date. Lesson 9 needs a yearly check.
- **Scenes** are worth building only where the act is the concept: `lever`, a ray of light
  through `refraction`, and a `foodchain`. Build them when a lesson needs them.

## Engine work

Nothing is required for a first version. Add a check that lists facts whose `asOf` is older
than 12 months. That check also serves General Awareness.

## Build order

1. Read the official syllabi and confirm the lesson list.
2. Collect sources for lessons 7, 8 and 12.
3. Pilot those three as a hidden draft: one body, one technology and one Assam lesson.
4. Finish Environment first, because APSC weights it, then the rest.
5. Add placement and list the course.

## Release gates

Build checks pass. Sources are read and recorded. Every changing figure has an `asOf` date.
A subject reviewer checks facts, and a fluent reader checks technical Assamese terms.
