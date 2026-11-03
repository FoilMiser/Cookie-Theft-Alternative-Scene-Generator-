"""make_scorers.py : write the three scorer prompts (three equal parts of the pictures by default) and split keys.json into keys_a/b/c.

    python make_scorers.py [A-B,C-D,E-F]
Writes <WORK>/v<TAG>prompts/scorer_<a|b|c>.txt and <ROOT>/vision/v<TAG>/keys_<a|b|c>.json."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG  # noqa: E402

V = os.path.join(ROOT, "vision", "v" + TAG)
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", "scorer_template.txt")).read()
keys = json.load(open(os.path.join(V, "keys.json")))
n = len(keys)
cuts = [0, n // 3, 2 * n // 3, n]
spans = [tuple(int(x) for x in p.split("-")) for p in sys.argv[1].split(",")] if len(sys.argv) > 1 else [(cuts[i] + 1, cuts[i + 1]) for i in range(3)]
out = os.path.join(WORK, f"v{TAG}prompts")
os.makedirs(out, exist_ok=True)
for t, (a, b) in zip("abcdef", spans):
    sub = {p: v for p, v in keys.items() if a <= int(p.split("_")[1]) <= b}
    json.dump(sub, open(os.path.join(V, f"keys_{t}.json"), "w"), indent=1)
    txt = tpl.replace("@V@", V).replace("@A@", f"{a:02d}").replace("@B@", f"{b:02d}").replace("@N@", str(b - a + 1)).replace("@T@", t)
    open(os.path.join(out, f"scorer_{t}.txt"), "w").write(txt)
    print(t, a, b, len(sub), "pictures", sum(len(v["items"]) for v in sub.values()), "items")
