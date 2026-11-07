# Indian History generated illustrations

## All queued subjects — draft production finished, 2026-11-07

- Actual measured total: **199 saved image entries** — **189 generated illustrations** and **10 licensed source assets**. The 22 explicit retain-icon/chips rows keep their existing visuals. No unsaved entries remain.
- This pass saved 43 previously missing entries and revised the 1916 meeting to remove the flagged cap. Two newly generated variants (an invented meeting and a Chakra teaching scene) were rejected and replaced with licensed source assets; discarded versions remain preserved.
- All 32 planned lesson covers now have a reusable draft candidate recorded in the queue. These are selections, not changes to lesson portraits or course faces.
- Complete gallery: `output/imagegen/indian-history/all-images.html`. Filter by lesson, card, title or subject; click images for masters and expand notes for exact prompts and metadata.
- Built-in ImageGen used for generated assets; no API/CLI fallback. Current-pass assets were visually inspected. All 199 active master/preview pairs decode; SHA-256 hashes, 1080px preview widths and metadata sidecars checked.
- Some planned documentary subjects have contextual substitutes: Gandhi writing in 1940 is **not** the 1930 letter; the East Champaran museum memorial is modern; the Forward Bloc flag is a modern vector, **not** verified as its 1939 design. The Dandi photo's source date conflicts with the planned day and remains qualified. See the source register and individual QA notes.
- Decorative maps, generated portrait likenesses, buildings and equipment remain interpretive; never use them as geographic or historical evidence. Exact event photographs/facsimiles are not claimed where a contextual substitute is supplied.
- `scripts/verify.sh` passed after this pass; all complete-gallery local links and all 199 bilingual draft titles passed checks. Browser check loaded all 199 previews with zero broken images and confirmed 32 cover candidates; filtering to `ih-32` returned seven entries.
- Historical fidelity and Assamese editorial review remain pending. This completes draft asset production only; images are not integrated into lessons or published.

## First 100 image subjects — draft production finished, 2026-11-07

The request to “complete 100” was executed as 100 total entries: the first 50 plus the next 50 concrete subjects in original table order. The batch ends at `ih-17.u2.02` (Kala Amb memorial).

- Measured output: 100 saved entries — 98 generated illustrations and the same 2 licensed photographs. There are 99 concrete subjects remaining; the 22 explicit retain-icon/chips rows are excluded.
- Review gallery: `output/imagegen/indian-history/first-100.html`. Each entry has a saved master, 1080px-wide WebP, bilingual draft title, credit, prompt/source record and visual inspection notes.
- Manuscripts and coins are contextual studies with unreadable writing. Battle and court scenes are new interpretations, not copies of period miniatures. The namghar and Lachit commemorative sculpture are conceptual types, not exact portraits of named existing monuments. Individual substitutions and limitations are recorded in the ledger and gallery.
- Corrected invented manuscript lettering, an unsupported coin backdrop, trade-ledger writing and an anachronistic Taj Mahal backdrop. Superseded image versions remain preserved.
- All 100 active entries visually inspected. File decoding, preview widths, hashes, critical metadata fields, bilingual titles and every gallery local link passed. `scripts/verify.sh` passed.
- Draft production only: historical fidelity and Assamese editorial review remain pending. No lessons integrated or published; no deployment performed.

## First 50 image subjects — generation pass finished, 2026-11-07

The user requested completion of the first 50 concrete subjects in the original plan's table order, excluding explicit retain-icon/chips rows. The batch ends at `ih-09.u2.01` (Brihadisvara temple).

- Measured output: 50 saved entries — 48 generated illustrations and 2 licensed photographs. Every entry has a master, 1080px-wide WebP preview and metadata sidecar.
- The Dancing Girl and Didarganj Yakshi generation requests were rejected by ImageGen. Authentic openly licensed photographs fulfil those entries; their rights and provenance are in `indian-history-images.md`.
- Built-in ImageGen was used; no API/CLI fallback. Exact prompts and sources are in `indian-history-generation-queue.json` and per-master sidecars. Initial and revised versions of the pillar and lyrist coin are preserved.
- Review gallery: `output/imagegen/indian-history/first-50.html`. Generated images carry interpretation credits; source photos carry their actual photographers' credits.
- Contextual manuscript/inscription studies are not facsimiles. New literary and later portrait illustrations must not inherit dates or attribution from the source artworks proposed in the original plan. Object and architecture details remain interpretive.
- All 50 images visually inspected; file decoding, master hashes, preview widths, metadata and gallery local links checked. `scripts/verify.sh` passed.
- This completes the draft asset production pass only. Historical fidelity and Assamese editorial review remain pending. No lesson integration, publication, commit, push or deployment performed.

## Xuanzang — first draft, 2026-11-07

- File: `output/imagegen/indian-history/xuanzang-interpretation-v1.png`
- Candidate: `ih-08.u3.02`, generated-interpretation option in `docs/INDIAN-HISTORY-IMAGES.md`.
- Tool: built-in ImageGen; no reference image supplied.
- Status: draft; not wired into the lesson, published or historically reviewed.
- Required credit: **AI-generated artist’s interpretation; not historical evidence.**
- Face, clothing and generic landscape are imaginative. No named river or specific encounter is depicted.
- Visual inspection: one monk, wide painted composition, no text, modern objects, palace or invented meeting visible.
- Does not fulfil entries requiring real artefacts, photographs or manuscripts. Existing untracked plan preserved unchanged.

### Generation prompt

```text
Use case: historical-scene.
Asset type: draft educational story-card illustration for Indian History, lesson ih-08-harsha, proposed card ih-08.u3.02. 
Primary request: a respectful artistic interpretation of Xuanzang, the Chinese Buddhist pilgrim, as a travelling monk. A single adult Chinese monk with a shaved head, plain layered ochre and muted brown robes, carrying a modest cloth travel bundle, standing quietly in a softly suggested green river-valley landscape. This is an imaginative illustration, not a portrait likeness or a reconstruction of a documented encounter.
Style: finely painted editorial illustration, natural textures, restrained warm earth tones and greens, readable on a phone, no fantasy embellishment.
Composition: wide 16:9 landscape, waist-up or three-quarter figure, uncluttered background, calm daylight.
Constraints: no king, court, palace, specific monument, map, named river, dates, invented dialogue, inscriptions, manuscript text, modern items, halo, weapons or watermark. No text in the image. Do not imitate a historical photograph or ancient manuscript. Clothing, face and scenery are interpretive and must not imply authenticated details.
```

