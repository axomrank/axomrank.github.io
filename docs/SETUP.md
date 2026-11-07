# Services and deployment

| Service | What it does | Where |
|---|---|---|
| Cloudflare Pages | Main hosting | https://axomrank.pages.dev (project `axomrank`) |
| GitHub Pages | Second copy, built from `main` | https://axomrank.github.io/ |
| Firebase Auth | Google sign-in | Project `axomrank-ahom` |
| Firestore | One progress document per learner, `users/{uid}` (Mumbai, asia-south1) | Project `axomrank-ahom` |

All are on free plans.

## Publishing an update

```bash
python3 scripts/build.py          # check content, write content/manifest.json, stamp sw.js
git add <changed files> && git commit -m "…" && git push   # GitHub Pages
scripts/deploy_cloudflare.sh      # Cloudflare Pages (copies only the website files)
```

The build stamps a new version into `sw.js`, so phones replace old app files on their next visit.

## Firestore security rules

Rules are in `firestore.rules`. Each learner can read and write only their own progress document (`users/{uid}`, with only the fields the app uses, including `game`: badges, feats, daily goal, streak freezes). Community data is separate: `profiles/{uid}` (public card, owner writes), `rooms/{room}/msgs` (group chat), `dms/{a_b}` and its `msgs` (direct messages, readable only by the two learners) and `reports` (write-only; read reports in the Firebase console). Publish the rules **before** deploying an app version that writes new fields, or sync fails. To publish (uses gcloud):

```bash
scripts/deploy_rules.sh
```

## Firebase settings that live in the console

- **Authentication → Sign-in method:** Google is enabled.
- **Authentication → Settings → Authorized domains:** must include `axomrank.pages.dev` (and any custom domain), or Google sign-in fails with `auth/unauthorized-domain`. On 2026-11-07 the list had the old `ahom-lessons.pages.dev` but not `axomrank.pages.dev`. Add domains with `scripts/authorize_domain.sh [domain ...]` (uses gcloud; keeps existing entries).
- **Web app config:** in `app/config.js`. These values are public by design; the rules protect the data.

## Images on Cloudflare R2 (later)

Images are served with the app (about 2 MB for two lessons). When media grows or audio is added:

1. Cloudflare dashboard → R2 → create a bucket with public access and a CORS rule allowing GET from the two site addresses.
2. Upload `content/media/` to it, keeping the same paths.
3. Set `mediaBase` in `app/config.js` to the bucket's public URL (ending with `/`) and publish.

## Android and iOS (next step)

Wrap the web app with Capacitor. Google Play costs $25 once; the Apple developer account costs $99 per year. Google sign-in inside the native apps needs the `@capacitor-firebase/authentication` plugin.
