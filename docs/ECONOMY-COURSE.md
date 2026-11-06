# Economy course plan

Status: planned on 2026-11-06. Nothing is built. Lesson format and permanent-id rules in
[LESSON-DESIGN.md](LESSON-DESIGN.md) apply.

A learner should understand how money moves through banks, government and Assam's own
economy, so that a budget headline makes sense.

## Why this course

78 past questions: APSC 31 (6% of its sample), ADRE 25 (2%), TET 16 (5%), Constable 5 and SI
1. It is the smallest shared subject, but 21 questions are specifically about Assam, which
is where general books help least.

| Group | Past questions |
|---|---:|
| Banking and finance | 23 |
| Indian economy | 22 |
| Assam economy | 21 |
| Economic concepts | 12 |

## Scope

- **Course id:** `economy`, with lesson ids `ec-NN-slug`, in the existing `economy` subject.
- **Boundaries:** interest sums stay in Mathematics. How Parliament passes a budget stays in
  the Constitution course, in "Control of public money" and "Money between Union and states".
  Link to those lessons rather than repeat them.
- **Out of scope:** this year's budget figures, which go to Current Affairs.

## Course map

8 lessons and about 32 units, 4 each, roughly 190 exercises.

| # | Lesson id | Group | Core content |
|---:|---|---|---|
| 1 | `ec-01-basics` | Concepts | Demand, supply, inflation, GDP, economic systems |
| 2 | `ec-02-development` | Concepts | Development, poverty and inequality measures, global indices |
| 3 | `ec-03-money` | Banking | Money, RBI, monetary policy, currency |
| 4 | `ec-04-banks` | Banking | Banks, payments, RTGS and UPI, regulation, bad loans |
| 5 | `ec-05-markets` | Banking | Stock exchanges, bonds, foreign exchange, international banks |
| 6 | `ec-06-budget` | Indian economy | Budget terms, taxes, GST, Economic Survey |
| 7 | `ec-07-assam-land` | Assam | Agriculture, tea, silk, GI tags |
| 8 | `ec-08-assam-industry` | Assam | Oil, refineries, banking in Assam |

Lessons 7 and 8 come first in build order. Assam History's "Oil, industry and the refinery
movement" tells that story, so lesson 8 links to it and covers today's economy.

## How questions are made

- **Lesson JSON, written by hand.** Concepts can be taught with a small scene.
- **Sources:** RBI, the Finance Ministry, the Economic Survey, Assam's Economic Survey and
  the Tea Board. Treat textbooks as leads. Record them in `docs/research/`.
- **Stale facts:** rates, tax slabs and scheme details change, so each has an `asOf` date.
  Teach what a repo rate does, and mention the current value only as dated context.
- **Scenes:** a `moneyflow` showing a loan creating deposits, a `demand` curve to drag, and a
  budget `pie` reusing the Reasoning `bars` idea.

## Engine work

Nothing is required. It shares the `asOf` check proposed in the Science plan.

## Build order

1. Read the official syllabi and confirm the list.
2. Pilot lessons 3, 6 and 8 as a hidden draft: concept, national and Assam.
3. Finish the Assam lessons, then the rest.
4. Add placement and list the course.

## Release gates

Build checks pass. Every changing figure has an `asOf` date. Sources are read. A subject
reviewer and a fluent reader of Assamese economic terms have checked it.
