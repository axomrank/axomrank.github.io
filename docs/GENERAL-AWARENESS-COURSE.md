# General Awareness course plan

Status: planned on 2026-11-06. Nothing is built. Lesson format and permanent-id rules in
[LESSON-DESIGN.md](LESSON-DESIGN.md) apply.

This course holds stable general knowledge. Anything that changes monthly belongs in
[Current Affairs](CURRENT-AFFAIRS-COURSE.md).

## Why this course

173 past questions, of which 7 are tagged Current Affairs and go to that plan. By exam: ADRE
120 (9% of its sample), APSC 32 (6%), Constable 8, SI 6, DME 4 and TET 3.

Memory is the whole of this subject, so it suits daily review well, and it is easy to make
dull. The plan uses collections and clusters rather than lists.

## Scope

- **Course id:** `general-awareness`, with lesson ids `gk-NN-slug`, in the `current-affairs`
  subject beside the monthly packs.
- **Out of scope:** holders of offices who change, recent winners, and anything needing a
  monthly update. Those go to Current Affairs.

## Course map

7 lessons and 34 units, roughly 200 exercises.

| # | Lesson id | Past questions | Units | Content |
|---:|---|---:|---:|---|
| 1 | `gk-01-sports` | 54 | 6 | Olympics, cricket, tennis, football, hockey: rules and history |
| 2 | `gk-02-assam-sports` | 9 | 3 | Sportspersons of Assam, its facilities and commemorations |
| 3 | `gk-03-people` | 30 | 6 | Scientists, explorers, painters, titles of persons |
| 4 | `gk-04-symbols-days` | 28 | 6 | Important days, flags, state and national symbols |
| 5 | `gk-05-awards` | 23 | 6 | How major awards work, with Assam's own awards |
| 6 | `gk-06-books` | 13 | 4 | Books and authors, with Assam's writers |
| 7 | `gk-07-organisations` | 9 | 3 | International and Indian bodies |

## How questions are made

- **Lesson JSON, written by hand,** with a source for every fact.
- **Teach structure first:** how the Olympics are organised, or what each award is for,
  before names. Names attach to a structure and are remembered longer.
- **Assam first:** many questions are local, and local facts are the hardest to find
  elsewhere, so they are the most useful.
- **People are shown as evidence:** use the shared entity system, so a name is tappable and
  links to the history lessons. Do not duplicate Assam History's material.
- **Living people:** use only what reliable sources state. Do not describe anyone beyond
  sourced public facts.

## Engine work

Nothing is required. `whoami`, `match`, `picture` and `map` steps suit this well. An earned
collection of people and awards is a hypothesis to test, as `EXPERIENCE-REVAMP.md` says.

## Build order

1. Agree the boundary with Current Affairs, lesson by lesson.
2. Pilot lessons 2 and 5 as a hidden draft.
3. Finish the rest in order, then add placement and list the course.

## Release gates

Build checks pass. Every fact has a read source. Each lesson states the date it was last
checked. Nothing in it should need a monthly update; if it does, it moves to Current Affairs.
