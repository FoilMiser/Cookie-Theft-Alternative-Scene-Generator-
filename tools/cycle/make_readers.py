import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import glob, os, sys
S = WORK
V = os.path.join(ROOT, "vision", "v" + TAG)
pics = sorted(glob.glob(f"{V}/blind/pic_*.png"))
n = len(pics); k = int(sys.argv[1]) if len(sys.argv) > 1 else 9
sizes = [n // k + (1 if i < n % k else 0) for i in range(k)]
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "prompts", "reader_template.txt")).read().replace("/home/claude/tpdb", ROOT)
head, rest = tpl.split("Images (open each with the Read tool):\n", 1)
tail = rest[rest.index("For each picture"):]
os.makedirs(f"{S}/v{TAG}prompts", exist_ok=True)
i = 0
for r, sz in enumerate(sizes, 1):
    mine = pics[i:i + sz]; i += sz
    h = head.replace("Look at 7 cartoon", f"Look at {sz} cartoon").replace("only the 7 image", f"only the {sz} image")
    t = tail.replace("/v09/", f"/v{TAG}/").replace("just the 7 file", f"just the {sz} file")
    txt = h + "Images (open each with the Read tool):\n" + "\n".join(mine) + "\n\n" + t
    open(f"{S}/v{TAG}prompts/reader_{r}.txt", "w").write(txt)
    print(r, sz, os.path.basename(mine[0]), os.path.basename(mine[-1]))
