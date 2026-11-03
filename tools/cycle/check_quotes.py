"""Every quotation in the release's prose must be found in what the readers or scorers wrote. A miss is a question, not always an error:
a phrase in quotation marks that nobody wrote, or apostrophes taken for quotation marks in the site's notes."""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT as _R, TAG, PREV  # noqa: E402
ROOT = str(_R).rstrip("/\\") + "/"


def norm(t):
    t = t.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", " ").replace("*", "")
    return re.sub(r"\s+", " ", t).lower()


corpus = {}
for pat in (f"vision/v{TAG}/desc_*", f"vision/v{TAG}/scores*", f"vision/isolation_v{TAG}.md", f"vision/isolation_v{TAG}/**/*", f"vision/design_tests_v{TAG}.md", f"vision/design_tests_v{TAG}/**/*",
            f"vision/flaws_v{PREV}.md", f"vision/v{PREV}/desc_*", f"vision/v{PREV}/scores*"):
    for f in glob.glob(ROOT + pat, recursive=True):
        if f.endswith((".md", ".json", ".txt")):
            corpus[f[len(ROOT):]] = norm(open(f, encoding="utf-8", errors="replace").read())

T = json.load(open(ROOT + f"vision/readme_v{TAG}_text.json", encoding="utf-8"))
tpl = open(ROOT + "tools/cycle/README.template.md", encoding="utf-8").read().split("## Folders")[0]
site = open(ROOT + "scenegen/site.py", encoding="utf-8").read()
site_q = "\n".join(re.findall(r"'([^'\n]{6,})'", site[site.index("REDRAWN_NOTES"):site.index("def webp(src, dst")]))
tmpl = open(ROOT + "scenegen/site_template.html", encoding="utf-8").read()
a = tmpl.index('Fresh readers, who never saw')
srcs = {"template": tpl, "text.json": "\n".join(T.values()), "flaws": open(ROOT + f"vision/flaws_v{TAG}.md", encoding="utf-8").read(), "limits": open(ROOT + "vision/limits.txt", encoding="utf-8").read(),
        "site.py": "\n".join('"%s"' % q for q in site_q.split("\n")), "site tmpl": tmpl[a:tmpl.index("</p>", a)]}
bad = 0
for name, s in srcs.items():
    for q in re.findall(r'"([^"\n]{4,}?)"', s):
        for frag in re.split(r"\s*\.\.\.\s*", q):
            n = norm(frag).strip(" ,.;:")
            if not n or len(n) < 4:
                continue
            hits = [k for k, v in corpus.items() if n in v]
            if not hits:
                bad += 1
                print(f"NOT FOUND [{name}]: {frag!r}   (in: {q[:80]!r})")
print("not found:", bad, "corpus files", len(corpus))
