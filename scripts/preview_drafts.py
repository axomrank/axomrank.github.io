#!/usr/bin/env python3
"""Check and preview draft courses without publishing them.

Drafts live in private/drafts/<course>/ (never committed or deployed):
  course.json, questions.json, entities.json, lessons/<id>.json
This copies the site to a temporary folder, merges the drafts in (with placeholder
pictures where real ones are missing), runs scripts/build.py there, and writes
REVIEW.md next to each draft so it can be read and corrected.

Usage:  python3 scripts/preview_drafts.py            check + write REVIEW.md
        python3 scripts/preview_drafts.py --serve    also serve the preview at http://localhost:8771
"""
import json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS = os.path.join(ROOT, "private", "drafts")
OUT = "/home/angsuman/extra_spac/tmp/axom-preview"
PLACEHOLDER = os.path.join(ROOT, "content", "media", "shared", "gohains.webp")
load = lambda p: json.load(open(p, encoding="utf-8"))
save = lambda o, p: json.dump(o, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

shutil.rmtree(OUT, ignore_errors=True)
shutil.copytree(ROOT, OUT, ignore=shutil.ignore_patterns(".git", "private", "node_modules", ".wrangler"))
ent = load(f"{OUT}/content/entities.json")
cat = load(f"{OUT}/content/catalog.json")
missing, drafted = [], {}   # drafted: names added by drafts (two drafts may add the same name, if identical)
def placeholder(path):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True); shutil.copy(PLACEHOLDER, path); missing.append(os.path.relpath(path, OUT))

for name in sorted(os.listdir(DRAFTS)) if os.path.isdir(DRAFTS) else []:
    d = os.path.join(DRAFTS, name)
    if not os.path.exists(f"{d}/course.json"): continue
    C = load(f"{d}/course.json")
    save(C, f"{OUT}/content/courses/{C['id']}.json")
    shutil.copy(f"{d}/questions.json", f"{OUT}/{C['bank']}")
    for k, v in (load(f"{d}/entities.json") if os.path.exists(f"{d}/entities.json") else {}).items():
        if k in drafted and drafted[k] != v: sys.exit(f"{name}/entities.json: '{k}' differs from the same name in another draft")
        if k in ent and k not in drafted: sys.exit(f"{name}/entities.json: '{k}' already exists in content/entities.json")
        ent[k] = drafted[k] = v
    for k in C["kings"]: placeholder(f"{OUT}/content/media/{k['face']}")
    lessons = []
    for f in sorted(os.listdir(f"{d}/lessons")):
        L = load(f"{d}/lessons/{f}"); lessons.append(L)
        shutil.copy(f"{d}/lessons/{f}", f"{OUT}/content/lessons/{f}")
        imgs = [L["portrait"]] + [s["img"] for u in L["units"] + [L["test"]] for s in u["steps"] if s.get("img")]
        for i in imgs:
            p = f"{OUT}/content/media/{i if '/' in i else L['id'] + '/' + i}"
            placeholder(p); placeholder(p.replace(".webp", "@480.webp"))
    # put the course on the subject page, in place of its "coming soon" row
    S = next(s for s in cat["subjects"] if s["id"] == "assam-history")
    row = next((i for i, e in enumerate(S["courses"]) if e.get("soon") and e["title"]["en"].lower().startswith(C["title"]["en"].split()[0].lower())), None)
    if row is None: S["courses"].append({"course": C["id"]})
    else: S["courses"][row] = {"course": C["id"]}

    # REVIEW.md: everything a reviewer needs, in reading order
    strip = lambda t: re.sub(r"<[^>]+>", "", re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", re.sub(r"\[\[([^\]|]+)\]\]", lambda m: ent.get(m.group(1), {}).get("name", {}).get("en", m.group(1)), t)))
    strip_as = lambda t: re.sub(r"<[^>]+>", "", re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", re.sub(r"\[\[([^\]|]+)\]\]", lambda m: ent.get(m.group(1), {}).get("name", {}).get("as", m.group(1)), t)))
    both = lambda v: f"{strip(v['en'])}  \n  _{strip_as(v['as'])}_"
    out = [f"# Review: {C['title']['en']}\n", "Drafts written by Claude from the sources listed in each lesson. Check every fact and the Assamese before publishing.\n"]
    for L in lessons:
        out.append(f"\n## Lesson {L['no']}: {L['king']['en']} ({L['reign']['en']})\n")
        out.append(f"**To check:** {L.get('review_notes', '')}\n")
        out.append("**Sources:** " + "; ".join(f"[{s['title']}]({s['url']}) ({s['used_for']})" for s in L["sources"]) + "\n")
        for u in L["units"] + [L["test"]]:
            out.append(f"\n### {u['title']['en']}\n")
            for s in u["steps"]:
                t = s["type"]
                if t == "story":
                    out.append(f"- **Card: {strip(s['title']['en'])}** / _{s['title']['as']}_")
                    out += [f"  - {both(p)}" for p in s["text"]]
                    continue
                q = s.get("q") or s.get("s") or (s.get("clues") or [None])[0]
                if t in ("inline", "fill"): q = {k: f"{s['before'][k]} ___ {s['after'][k]}" for k in ("en", "as")}
                if t == "spot": q = {k: " ".join(s["tokens"][k]) for k in ("en", "as")}
                out.append(f"- **{t}** `{s['id']}`: {both(q)}")
                if t == "whoami": out += [f"  - clue: {both(c)}" for c in s["clues"][1:]]
                if "options" in s and isinstance(s["answer"], int): out.append(f"  - options: " + " · ".join(("**" + o["en"] + "**") if i == s["answer"] else o["en"] for i, o in enumerate(s["options"])))
                if t == "tf": out.append(f"  - answer: **{'True' if s['answer'] else 'False'}**")
                if t == "fill": out.append(f"  - answer: **{s['answer']}** / {s['asOptions'][s['asAnswer']]}")
                if t == "map": out.append(f"  - answer: **{s['target']}** (choices: {', '.join(s['choices'])})")
                if t == "match": out.append("  - pairs: " + " · ".join(f"{a['en']} = {b['en']}" for a, b in s["pairs"]))
                if t == "order": out.append("  - order: " + " → ".join(i["en"] for i in s["items"]))
                if t == "timeline": out.append("  - anchors: " + ", ".join(f"{a['y']} {a['l']['en']}" for a in s["anchors"]) + "; items (slot): " + ", ".join(f"{i['t']['en']} ({i['slot']})" for i in s["items"]))
                if t == "spot": out.append(f"  - wrong word: **{s['tokens']['en'][s['wrong']['en']]}** / {s['tokens']['as'][s['wrong']['as']]}")
                out.append(f"  - why: {both(s['why'])}")
    open(f"{d}/REVIEW.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"{name}: {len(lessons)} draft lessons, review sheet at private/drafts/{name}/REVIEW.md")

save(ent, f"{OUT}/content/entities.json"); save(cat, f"{OUT}/content/catalog.json")
if missing: print(f"placeholder pictures for {len(missing)} files (real pictures still needed), e.g. {missing[0]}")
r = subprocess.run([sys.executable, f"{OUT}/scripts/build.py"], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr.strip())
if r.returncode: sys.exit(1)
if "--serve" in sys.argv:
    print("preview: http://localhost:8771  (Ctrl+C to stop)")
    subprocess.run([sys.executable, "-m", "http.server", "8771", "--directory", OUT])
