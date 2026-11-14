"""(v0.55's own script: its two screens are written in.)
sit_screen.py [TAG ...] : the screened pictures that hold a seated figure (a person whose pose has a lower posture of build_cast.SEATED55), and
for each screen (default v054 v055) the lines of each description's unsure section that name legs, knees, feet, a seat, a bench or a sitter.
The lines are printed to be read: a count of them is a hand count."""
import json, os, re, sys
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
tags = sys.argv[1:] or ["v054", "v055"]
cat = json.load(open("assets/cast/out055/cast_catalog.json"))["actions"]
SEATED = {"sit", "sit_swing", "sit_dangle", "sit_hang", "sit_low", "sit_slide"}
LEG = re.compile(r"\b(legs?|knees?|feet|foot|thighs?|shins?|seat|seated|sits?|sitting|bench|lap|perch\w*|dangl\w*|squat\w*|crouch\w*|seesaw|see-saw|swing|slide)\b", re.I)
km = json.load(open("vision/v055/key_map.json"))
pics = []
for pic, name in sorted(km.items()):
    f = next(p for p in (f"scenes/{name}.json", f"probes/{name}.json") if os.path.exists(p))
    r = json.load(open(f, encoding="utf-8"))
    poses = sorted({(e["asset"]["variant"].split("__")[0].split(".")[1], e["asset"]["variant"].split("__")[1].split("~")[0]) for e in r["elements"]
                    if e.get("asset") and e["asset"].get("variant", "").startswith("person.") and cat.get(e["asset"]["variant"].split("__")[1].split("~")[0], {}).get("lower") in SEATED})
    if poses:
        pics.append((pic, name, poses))
print(len(pics), "pictures with a seated figure")
for pic, name, poses in pics:
    print("==", pic, name, poses)
    for tag in tags:
        t = open(f"vision/{tag}/desc_{pic}.md", encoding="utf-8").read()
        m = re.search(r"(?im)^#*\s*\W*\d?\W*\s*\**unsure", t)
        uns = t[m.end():] if m else ""
        for l in uns.splitlines():
            if LEG.search(l) and l.strip().startswith(("-", "*")):
                print("   %s U: %s" % (tag, l.strip()[:300]))
