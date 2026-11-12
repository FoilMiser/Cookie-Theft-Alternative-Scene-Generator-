"""who_cmp.py : what the screens' readers called the four grown figures that are read young, this release's screen beside the last one's, by
one rule: the first inventory line that names the figure's clothes; young-first = the first person word in it is girl, boy, teenager, teen,
child or kid. (who_called.py prints every line for one figure; this is the count the flaws file and the README quote, from v0.49.) Run it after
the folders are swapped, when `scenes` and `probes` are this release's and `scenes_v<PREV>` and `probes_v<PREV>` the last one's. The clothes
patterns are tight on purpose: "red" alone matches the teenager's cap and "yellow" a child's shirt."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, TAG, PREV  # noqa: E402
import collections, json, re
os.chdir(ROOT)
PAT = {"person.ana": r"purple (top|t-?shirt|shirt|tee|blouse|sweater|jumper)", "person.mei": r"yellow (sun)?dress",
       "person.ben": r"red (t-?shirt|shirt|top|tee)", "person.dev": r"green (t-?shirt|shirt|top|tee)"}
WORD = re.compile(r"\b(young woman|woman|lady|girl|teenager|teen|boy|young man|man|child|kid|person|adult)\b")
YOUNG = {"girl", "boy", "teenager", "teen", "child", "kid"}
for tag, sdir, pdir in ((PREV, f"scenes_v{PREV}", f"probes_v{PREV}"), (TAG, "scenes", "probes")):
    if not os.path.exists(f"vision/v{tag}/key_map.json"):
        continue
    km = json.load(open(f"vision/v{tag}/key_map.json"))
    tot = collections.Counter(); young = collections.Counter(); none = collections.Counter()
    for pic, name in sorted(km.items()):
        f = next((p for p in (f"{sdir}/{name}.json", f"{pdir}/{name}.json") if os.path.exists(p)), None)
        if f is None:
            continue
        r = json.load(open(f))
        fams = {(e.get("asset") or {}).get("family") for e in r["elements"]}
        s = open(f"vision/v{tag}/desc_{pic}.md", encoding="utf-8").read()
        inv = s[s.lower().find("inventory"):]
        for fam, pat in PAT.items():
            if fam not in fams:
                continue
            tot[fam] += 1
            lines = [l.strip() for l in inv.splitlines() if re.search(pat, l, re.I)]
            if not lines:
                none[fam] += 1
                continue
            w = WORD.findall(lines[0].lower())
            if w and w[0] in YOUNG:
                young[fam] += 1
    print(tag, {f.split(".")[1]: "%d of %d (no line %d)" % (young[f], tot[f], none[f]) for f in PAT}, "| all four:", sum(young.values()), "of", sum(tot.values()))
