# Glass interface backdrop

- Assets: `content/media/interface/axom-river.webp` (lesson backdrop) and `axom-river-wide.webp` (out-of-focus desktop surround), plus build thumbnails.
- Built 2026-11-06 for the user-supplied four-screen interface mockup. Decorative composite, not historical evidence or a geographic map: Rang Ghar does not stand on the river as shown.
- Base: `brahmaputra-glass.webp`, a watercolor landscape generated on 2026-11-03 for the first glass interface. It is no longer shipped; restore it from git history (`git show 28927b6:content/media/interface/brahmaputra-glass.webp`) to rebuild the scene.
- Changes to the base: brighter tone curve, stronger saturation, sky graded to blue, a low red sun added, cropped to 1000 x 1265.
- Inset: the building from `content/media/library-story/c18-rang-ghar-pavilion-and-field-0d5367e7.webp`, whose record stays in the library-story register. Crowd and sky removed, softened to a painted finish, scaled to 178 px wide, seated with trees cloned from the same painting.
- Used only as CSS backgrounds. Lesson pictures, source records, interpretation labels and learning content stay separate.
- Interface accent is gamosa red (`#d8202b`), with green for correct answers. The woven gamosa motif is an inline SVG in `app/glass.css`, drawn for this app. The seal on the complete screen is an inline SVG in `app/engine.js`.
