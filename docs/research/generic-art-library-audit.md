# Generic story art: Assam History library audit

Date: 2026-11-03. This is a candidate inventory, not approval to publish images.

## Results

| Classification | Cards |
|---|---:|
| Strong catalogue topic match | 122 |
| Contextual illustration candidate | 139 |
| No defensible candidate established in this pass | 237 |
| Total generic story cards | 498 |

Strong candidates cover 103 units in 66 lessons. Both candidate groups together cover 182 units in 96 lessons, proposing 147 distinct image files. Reuse of an image across cards is allowed in these counts. These counts cover all 134 local lesson JSON files, including course versions with overlapping historical content; they are not limited to the 93 core Assam History lessons.

## Method

A generic card is a unit story step without a truthy `img` or `map`, following the renderer's precedence in app/engine.js. Read the source library AGENTS.md and image library guide. Filtered INDEX.csv, then resolved opaque scene IDs through data/assam_history.csv. Compared all 498 card titles and English texts against 672 existing catalogue scene and generated scene/object records. Used text similarity to propose candidates, then reviewed topic correspondence and rejected obvious false positives and period mismatches. Manually corrected some suggestions to a more relevant catalogue record. Checked every proposed path exists. Visually sampled 20 strong candidate images in a contact sheet.

The earlier estimate of 20–30 was incomplete because it searched descriptive filenames without resolving the published scene IDs.

The companion CSV records every card's lesson, unit, permanent step ID, text, classification and proposed library image. Blank paths mean no defensible candidate was established, not proof that the library has none. Character sheets and licensed photo alternatives have not been exhaustively assessed, so this is not a maximum coverage count.

## Interpretation

122/498 (24.5%) have a strong subject or event match in catalogue metadata. Another 139/498 (27.9%) could use an image of a relevant person, object, community or related event, but require an editorial decision: the picture does not depict every claim in the card. Combined candidate coverage is 261/498 (52.4%). The remaining 237 cards (47.6%) need further asset research or another visual approach.

All candidates remain provisional. Full visual inspection, era and source checks, caption suitability, aspect-ratio/crop checks, and provenance review must precede implementation. Catalogue summaries are finding aids, not historical evidence. Generated scenes remain artistic interpretations. A modern community illustration cannot establish a historical event or stand in for a political agreement. Reference photographs with unclear rights were not counted.

## Implementation (2026-11-03)

All 261 selected cards now use library images: 122 from the strong-match group and 139 from the contextual group, across 182 units / 96 lessons. Several initial suggestions were replaced during implementation with more relevant subjects. The CSV reflects those corrected source paths; `generic-art-library-assets.json` records the actual project paths, hashes and per-card captions.

146 unique source assets are used: 33 byte-identical existing project images were reused and 113 new WebP assets were imported. The source library remains unchanged. Its content licence is retained as `assam-history-library-LICENSE-CONTENT.txt`. The build creates the smaller image variants and adds all images to the offline manifest.

Cards have bilingual image captions identifying the illustration. Contextual cards explicitly say “Context illustration”; the image does not establish every claim in the card. Original artistic-reconstruction labels remain visible. New Assamese captions remain pending editorial review. Scene frames use a wider layout; object and character sheets use contain sizing to retain the full sheet. Lesson, unit and step IDs, narrative, exercises and learning gates are preserved.

237 generic story cards remain. Full historical and Assamese editorial review is not claimed. Contact sheets of all selected images were visually inspected; the checks below assess implementation.

Build passed for 134 lessons and 7,742 step/question IDs. The existing learning-gate check passed for retries, first-attempt 80% gates, test-outs and checkpoints. A comparison against the pre-import lesson files confirmed exactly 261 step changes, restricted to image metadata.

Browser verification: all 146 selected full-size images and 146 thumbnails decoded successfully (292/292). At 390px, the existing autoplay helper completed three representative units in both English and Assamese (six runs), covering scene, object and community-sheet imagery. Each run included a deliberate wrong true/false answer followed by its retry; first-attempt accuracy remained 4/5. No horizontal overflow was reported. Historical source review and human Assamese review remain separate.

Captioned library images do not receive an automatic story-year stamp: a year in the paragraph must not be presented as the date of a contextual illustration.
