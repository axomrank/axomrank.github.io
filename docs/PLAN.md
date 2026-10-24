# Axomrank: project plan

Axomrank is a bilingual (Assamese + English), game-like exam-preparation app for Assam government exams: **ADRE, Assam TET, APSC CSE Prelims, Assam Police SI**. It runs on the web (installable, offline), with Android/iOS wrappers later.

Live: https://axomrank.pages.dev · Code: https://github.com/axomrank/axomrank.github.io

## 1. Principles
1. **Never boring, always "one more":** short units, story first, varied exercises, instant feedback, visible progress, streaks and review. See [LESSON-DESIGN.md](LESSON-DESIGN.md).
2. **Assam depth and Assamese first:** state GK, state current affairs, state papers; Assamese is written alongside English, not translated later.
3. **Trust:** human-written, reviewed content with sources and verified answer keys. No AI-generated content.
4. **Real exam feel:** OMR-style mocks and an Assam-wide rank.
5. **Small and fast:** runs on 2 GB Android phones; content loads on demand; works offline.

## 2. Where we are
- Web app: lesson player (14 exercise types), maps, guidebook, name cards, daily review, checkpoints, XP/streak, Google sign-in and sync (Firebase), offline service worker.
- Content: **Ahom Kings**, 41 lessons / 1,647 steps, bilingual, with maps and paintings.
- Hosting: Cloudflare Pages + GitHub Pages. Free plans.
- Still single-course: code and content paths assume one course (`ahom-kings`).

## 3. Roadmap

### Phase 1: platform for many courses (next)
1. **Content layout** changes from one course to many subjects:
   ```
   content/
     catalog.json                 subjects → courses (title, exams, status)
     shared/entities.json         names shared by all courses
     shared/maps/                 base maps (districts, rivers, historic boundaries)
     history/<course>/course.json  eras, lessons
     history/<course>/lessons/<id>.json
     history/<course>/questions.json
     media/<course>/…
   ```
   `scripts/build.py` validates every course and writes the manifest; lesson ids become unique per course; saved progress is keyed by course so Ahom progress is kept (migration step).
2. **Home becomes a hub:** subject cards (History, Geography, Polity, Economy, Culture, Current Affairs, General Studies), then courses, then the path. Exam filter (ADRE / TET / APSC / SI).
3. **Exam tags** on lessons and questions; "My exam" in onboarding.
4. Rename Ahom-specific wording in the player; keep Ahom as course H3.

### Phase 2: Assam History complete
Build courses H1–H9 in [CURRICULUM.md](CURRICULUM.md). Pilot, then core exam topics, then thematic revision courses. Add the master **timeline** and a **people & places** index that spans all courses.

### Phase 3: more subjects
Assam geography (rivers, districts, national parks, climate, resources), polity (Sixth Schedule, councils, Assam Assembly, governance), economy (tea, oil, agriculture, budget, schemes such as Orunodoi), culture (festivals, dance, crafts), general studies and TET pedagogy; each as courses in the same format.

### Phase 4: exam tools
Previous-year papers with verified keys; **OMR-sheet mock tests** with negative marking, section timers, review; weekly free **All Assam Mock** with state leaderboard; pre-written 90/60/30-day plans; daily Assam current affairs and 10-question quiz; weak-topic detection (<50% weak, 50–75% needs work); bookmarks; one-week offline downloads.

### Phase 5: growth and operations
Admin panel (upload, tagging, translation, review, error reports), "Report an error" button, doubt forum, notifications for official notices (ADRE, SEBA/TET, APSC, SLPRB), shareable rank cards, referrals, coaching-centre white-label, Capacitor Android app, Bodo and Bengali later.

## 4. Content quality process
Author → reviewer → translator → final check → publish. Named educators; a public page on how content is reviewed. Every lesson lists its sources. Errors reported in-app go to a review queue.

## 5. Business model
Free core: lessons, notes, daily quiz, previous-year papers, current affairs. Paid: test series and exam passes at low one-time prices (about ₹99–₹499 per exam), not subscriptions. Growth: Assamese YouTube/Instagram shorts, Telegram/WhatsApp channels, referrals, weekly All Assam Mock.

## 6. Metrics
D7 and D30 retention; lessons and mocks per user per week; weekly All Assam Mock participation; revision items completed; free→paid conversion; referral rate.

## 7. Biggest risk
Content operations, not code: thousands of verified bilingual questions, written explanations, study plans and current affairs need subject experts, reviewers and translators. Plan the team and budget first. The first goal is the whole of Assam History at quality, then breadth.

## 8. Working notes
- Private material (grant applications, raw KMZ, drafts) lives in `private/`, never published.
- Every publish: `python3 scripts/build.py`, commit, push (GitHub Pages), `scripts/deploy_cloudflare.sh`. See [SETUP.md](SETUP.md).
