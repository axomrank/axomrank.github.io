# AxomRank home page

> The public home page of AxomRank: free, bilingual (English and Assamese) preparation for Assam government exams (ADRE, APSC CCE, Assam TET, Assam Police).

**[Live site](https://axomrank.github.io/)** · **[Open the app](https://axomrank.pages.dev)** · [All AxomRank repositories](https://github.com/axomrank)

## What is here

| File | Purpose |
|---|---|
| `index.html` | The home page: what AxomRank is, who it is for, the app's courses, the history sites, the free resources and contact details. Plain HTML with a small inline style, and no JavaScript |
| `404.html` | Sends old links to their new homes: old app URLs (for example `/lesson.html?id=…`) to axomrank.pages.dev, and renamed project paths (for example `/AHOM/`) to their new names |
| `robots.txt`, `sitemap.xml` | Search engine files |
| `icon-192.png` | AxomRank logo |

The AxomRank app itself is **not** in this repository. It is private and is deployed to Cloudflare Pages at https://axomrank.pages.dev.

This repository's name makes it GitHub's *user site* for the account, so it serves `https://axomrank.github.io/`. Each other public repository with GitHub Pages is served under it, for example `/axomrank-blog/` and `/ahom-kingdom-history/`.

## Editing

Edit `index.html` directly and push to `main`; GitHub Pages publishes it within a minute or two. Keep it simple: white background, readable on phones, no build step. Check facts (course and question counts) against the source repositories before changing numbers.

## Roadmap: future improvements

- [ ] Add an Assamese version of the page (`as/index.html`) with `hreflang` links
- [ ] Move to the custom domain axomrank.org and point the old URLs here
- [ ] Add a short "how to start" section with screenshots of the app
- [ ] Add testimonials from real learners (with their permission)
- [ ] Update the sitemap when new pages are added

## For AI agents and contributors

Read [AGENTS.md](AGENTS.md). Commit as the `axomrank` account.

## License and contact

No license file, so all rights are reserved by default. AxomRank is run by Angsuman Das (sole proprietor): angsuman.das@rgu.ac.in, +91 78965 05109.
