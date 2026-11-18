# Working on the AxomRank home page

- This repository serves https://axomrank.github.io/ (the GitHub user site). It holds only the public home page and the redirect page.
- **Never add the AxomRank app's code here.** The app is private (`axomrank/axomrank-app`) and deploys to Cloudflare Pages.
- Keep `index.html` as plain HTML on a white background with a small inline style block. No frameworks, build step or tracking scripts.
- Every number on the page must match its source repository (app course counts, the 2,398 questions in assam-exam-pyq, and so on). Do not invent features, results or testimonials.
- `404.html` handles old URLs. When a public repository is renamed, add the old name to the `moved` map.
- Commit as the `axomrank` account.
