# Current Affairs plan

Status: planned on 2026-11-06. Nothing is built. This is a publishing process more than a
course, so it needs an owner before anything is built.

The catalog promises "Assam and India, with a daily quiz". The stable half of the subject is
in [General Awareness](GENERAL-AWARENESS-COURSE.md).

## The decision to make first

**Who writes and checks each pack?** Every other course is written once. This one stops being
useful the moment nobody updates it, and a stale or wrong answer is worse than none. If nobody
can own it, drop the promise from the catalog. This needs the course owner's decision.

## What the data says

Only 7 of the 2,398 questions are tagged Current Affairs, but that undercounts it: many
General Awareness questions on awards, sports results and office holders are recent events,
and 80 of those 173 questions are from 2024 papers. The papers cannot show how far back
examiners reach, so the window below is an assumption to check.

## Design

- **Monthly packs,** not a lesson path: 15 to 25 facts in each, `ca-YYYY-MM`.
- **Daily quiz:** a few facts a day drawn from the current pack, reusing the bounded daily
  mission rather than adding a second daily habit.
- **Rolling window:** keep the last 12 months active. Older packs retire from review, but
  their ids stay, because learners' progress refers to them.
- **Sections:** Assam, India, world, sports, awards, science and appointments.
- **Links:** a fact links to the course that explains it. Budget facts link to Economy, and
  office holders link to the Constitution lesson on that office, whose plan leaves current
  holders to this course.

## Rules

- Every fact names its source and date. Prefer official releases: the Press Information
  Bureau, the Assam government and the bodies concerned.
- Keep dates and claims distinct, and do not include disputed political claims as facts.
- Never present a fact as an exam question without verified provenance.
- A corrected fact keeps its id and gets a new version.
- Assamese stays pending review, which is harder here because of the pace.

## Engine work

| Item | Need |
|---|---|
| Packs | A new `content/current/` folder, listed in the manifest. New |
| Expiry | Review must skip retired facts without losing progress. New, and it touches `app/common.js`, so migrate carefully |
| Daily quiz | Reuse the daily mission |
| Offline | Add the current pack to the service worker's cached files |
| Check | `scripts/check_current.py`: every fact has a source, a date and two languages |

## Build order

1. Settle ownership.
2. Write one pack by hand and time it. That shows whether monthly is realistic.
3. Build expiry and the pack format, and test progress migration.
4. Publish three packs to a hidden draft and test with learners.
5. List it only when the third pack came out on time.

## Release gates

An owner is named. Three packs were published on schedule. Expiry was tested with saved
progress. Every fact has a source and a date.
