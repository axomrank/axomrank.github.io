# Indian History image generation agent

## Objective and authority

The user requested on 2026-11-07: write this file to generate all planned images and start executing. Generate artistic interpretations of the concrete image subjects in `docs/INDIAN-HISTORY-IMAGES.md`. This updates the earlier plan's generation scope; it does not turn synthetic pictures into evidence. Keep the original image plan intact. Work with one agent; do not delegate.

## Inventory and resume

Use `docs/research/indian-history-generation-queue.json` as the per-card ledger. Read it at the start of each session, measure files before reporting progress, and resume pending entries. Work in lesson order, A then B then concrete C subjects within each lesson. Rows explicitly saying keep icon/chips remain unchanged. The source plan stops at lesson 32 despite describing 33 lessons; record that gap rather than inventing a lesson-33 brief. Covers reuse a suitable completed A image per lesson and need a recorded crop, not another unnecessary generation.

## Required workflow

1. Read root `AGENTS.md`, the imagegen skill, the source plan and the relevant lesson's story text. Preserve permanent lesson/exercise ids. Keep the Assam History library unchanged.
2. Read authoritative museum, archaeological or archival descriptions for each subject. Record supporting URLs and which details they support. View any reference image before using it. Do not rely on research summaries alone or silently infer disputed details.
3. Generate one distinct asset per built-in ImageGen call. Use coherent painted educational illustrations, wide 16:9 compositions, uncluttered phone-readable framing and restrained colours. Do not impersonate a period photograph, museum scan or historical document.
4. Artefacts and monuments require reference checking of shape and diagnostic features. Manuscripts, inscriptions, coins, proclamations and letters must not contain invented readable passages: use a contextual illustration with obscured writing or obtain an authentic licensed scan. Never treat generated signs or lettering as evidence for a reading, attribution or date. Record any contextual substitution explicitly.
5. Historical scenes may illustrate supported circumstances, but cannot invent dialogue, sources, dates, events or alternative outcomes. Avoid fabricated eyewitness specificity. Sensitive events use places or contextual objects, never victims. Portraits are interpretive likenesses, not authenticated contemporary portraits.
6. Save PNG masters non-destructively under `output/imagegen/indian-history/<lesson-id>/<card>-vN.png`. Save 1080px-wide WebP drafts alongside them. Preserve all user-owned output. Do not overwrite earlier versions.
7. Inspect each generated output for subject, geometry, period, unwanted text and misleading detail. Update its ledger entry with exact prompt, paths, generation tool, supporting sources, QA findings and status `generated-draft` or `needs-revision`. Generated draft does not mean historically approved, integrated or published. Keep rejected versions distinct.
   If generation rejects an archaeological object, record the rejection without bypass retries. A verified openly licensed photograph may fulfil that image entry instead: preserve the original bytes, author, licence and source URL, label it `source-image-draft`, and distinguish it from generated art in all counts. Wikimedia downloads require an identifying user-agent.
8. Every generated image requires the visible credit “AI-generated artist’s interpretation; not historical evidence.” Track English and Assamese captions together before integration; Assamese remains pending editorial review. Never label synthetic art as a source photograph, period painting or document. Check renderer support before choosing an imageKind for generated art.
9. This generation task produces drafts and the ledger. Integration requires preserving story/exercise text and ids, adding appropriate credits, checking covers and service-worker assets, running `scripts/verify.sh`, and meaningful English/Assamese phone-width browser checks. Do not deploy merely because the older plan lists publishing as a step.

## Progress and delivery

After each completed image save the prompt and ledger immediately. Report measured generated/revision/pending counts, exact saved paths and remaining scope. Keep going through requested batches without asking routine permissions. Do not claim all images are finished until every concrete image row has a verified file or an explicit documented unresolved issue. Run `scripts/verify.sh` before delivery.
