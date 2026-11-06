# Images for the 76 formerly CSS-only units

The scope is the 76 units whose story cards all lacked both image and map metadata at the start of this work. Their existing bilingual text, card IDs and source lists are frozen in `css-only-image-plan.json` (in git history; see `docs/CLEANUP.md`). One distinct contextual illustration is planned per unit, shared by its story cards. This keeps each short unit visually coherent without creating a false documentary scene for every claim.

## Source checks and visual constraints

- [IndianOil: Guwahati Refinery](https://iocl.com/guwahati-refinery), read 2026-11-03: confirms the refinery's operation from 1962 and industrial processing context. Generated industrial scenes are contextual; no exact plant layout or inauguration is claimed.
- [ASI Guwahati: Dah-Parbatia](https://asiguwahaticircle.gov.in/mound%20and%20ruins.html), read 2026-11-03: describes the carved doorframe, masonry remains and stylistic dating around the sixth century. Generated archaeological illustrations are interpretations, not photographs or measured reconstructions.
- [Majuli district: Samaguri Satra](https://majuli.assam.gov.in/tourist-place-detail/274), read 2026-11-03: identifies the mask-making tradition and its relationship to bhaona. Craft imagery must emphasize makers, material and performance rather than invented historical dialogue.
- [MEA statement on NRC, 1 September 2019](https://www.hcipretoria.gov.in/section/news/statement-by-mea-on-nrc-september-1-2019/), located 2026-11-03: official statement concerning the 31 August publication. Civic images contain blank documents, no fabricated official text, verdict, individual legal status or current-law claim.

Existing lesson sources remain the basis for the historical teaching text. The art adds no new dates, outcomes, evidence, identities or purported source passages. Legal, census, settlement and autonomy illustrations show contextual civic reading/discussion, with no invented signing ceremony, boundary or readable document. Author units use literary objects and reading settings without invented portraits. Legendary narratives remain identified by the existing teaching text and an artistic-interpretation label. War and violence imagery is non-graphic and avoids invented victims or identifiable leaders.

Generation uses the built-in imagegen tool. Full prompts and saved output paths are recorded in `css-only-generation-progress.json` (in git history; see `docs/CLEANUP.md`); integrated WebP paths and per-card provenance are recorded separately after review. Images must be inspected before integration. Existing exercise and progress IDs remain unchanged. New Assamese caption prefixes retain pending editorial review.

## User direction

On 2026-11-03 the user instructed retaining first drafts and stopping revisions. The generation batch continues with its saved first-draft selections. Correction candidates are excluded from integration. Build, file loading, caption layout and ID-preservation checks remain required; these checks do not claim historical or human Assamese editorial approval.

## Completed local integration

76 first-draft unit images generated with the built-in imagegen tool are saved as WebP in `content/media/generated-unit-art/`. They cover154 story cards across76 units in31 lessons. Full prompts,original generated-file paths,output hashes and card IDs are in `generated-unit-art-assets.json`. No correction candidates were integrated,following the user's instruction.

The build passed for134 lessons and7742 step/question IDs. All152 full-size/thumbnail files decoded in the browser. Eight390px mobile unit runs completed in English and Assamese,including a deliberate wrong answer and successful retry in every run; first-attempt accuracy remained4/5. No horizontal overflow was reported. The existing learning-gate checks passed. A structural comparison confirmed exactly154 story-card changes restricted to image metadata,with narrative,unit and exercise IDs and all other lesson fields preserved.

No unit remains entirely CSS-art-only. There are still83 CSS-art cards in76 mixed units outside this bounded scope. Publication to both existing sites was authorised on2026-11-03;deployed versions are verified separately. New Assamese caption prefixes remain pending editorial review. Technical checks do not constitute historical or human editorial approval of these first drafts.
