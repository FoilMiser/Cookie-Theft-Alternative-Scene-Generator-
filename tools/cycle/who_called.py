"""who_called.py FAMILY 'regex of the clothes' [full] : what the screen's readers called a figure. For every screened picture the family is in,
the first inventory line that names its clothes, and a tally of the words for a person in it (woman, girl, man, boy ...). A rough count: check
the lines with `full` when a clothes word fits two figures. Run after the swap, e.g. who_called.py person.ana purple"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, os, re, sys, collections
os.chdir(ROOT)
fam, pat = sys.argv[1], re.compile(sys.argv[2], re.I)
full = len(sys.argv) > 3
km = json.load(open(f"vision/v{TAG}/key_map.json"))
cnt = collections.Counter(); n = 0
for pic, name in sorted(km.items()):
    f = next(p for p in (f"scenes/{name}.json", f"probes/{name}.json") if os.path.exists(p))
    r = json.load(open(f))
    if not any((e.get("asset") or {}).get("family") == fam for e in r["elements"]):
        continue
    n += 1
    s = open(f"vision/v{TAG}/desc_{pic}.md", encoding="utf-8").read()
    inv = s[s.lower().find("inventory"):]
    lines = [l.strip() for l in inv.splitlines() if pat.search(l)]
    l = lines[0] if lines else "(no line)"
    w = re.findall(r"\b(young woman|woman|lady|girl|teenager|teen|boy|young man|man|child|kid|person|adult)\b", l.lower())
    cnt[" / ".join(dict.fromkeys(w[:3])) or "?"] += 1
    if full:
        print(pic, "|", l[:170])
print(fam, n, "pictures:", dict(cnt.most_common()))
