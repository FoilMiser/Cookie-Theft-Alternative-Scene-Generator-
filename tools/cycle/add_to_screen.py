"""(v0.57's own script: its two pictures and paths are written in. Edit them.)
add_to_screen.py : pictures added to a screen that has begun. The tier-4 park and its isomorph, found after the screen of the other 134 pictures had begun, added to vision/v057 as
pic_135 and pic_136 (blind copies, key_map, keys with the same fields as vision/prepare_screen.py writes), with keys_f.json, the sixth
scorer's prompt and the eighteenth reader's."""
import json, os, shutil
ROOT = "E:/Cognitive_Test_Scene_Creator"
os.chdir(ROOT)
V = "vision/v057"
km = json.load(open(V + "/key_map.json")); keys = json.load(open(V + "/keys.json"))
ANGLE = {0: "facing the viewer", 45: "three-quarter front", 90: "profile", 135: "three-quarter back"}
add = {"pic_135": "T4_park_s938959", "pic_136": "T4_garden_s9111_iso"}
sub = {}
for k, n in add.items():
    assert k not in km and n not in km.values()
    shutil.copy(f"scenes057/{n}.png", f"{V}/blind/{k}.png")
    r = json.load(open(f"scenes057/{n}.json"))
    e = {"items": [{"id": it["id"], "type": it["type"], "text": it["text"],
                    "accepted": (it["accepted"] if isinstance(it["accepted"], list) else it["accepted"].get("what", []))[:8],
                    **({"names": it["accepted"]["who"]} if isinstance(it["accepted"], dict) and it["accepted"].get("who") else {})}
                   for it in r["items"]]}
    an = []
    for el in r.get("elements", []):
        a = el.get("asset") or {}
        if a.get("family", "").startswith("animal.") and "__y" in a.get("variant", ""):
            x = {"animal": a.get("labels", {}).get("everyday_name", a["family"][7:]), "angle": ANGLE.get(int(a["variant"].rsplit("__y", 1)[1]), "?")}
            if x not in an:
                an.append(x)
    if an:
        e["animals"] = an
    km[k] = n; keys[k] = e; sub[k] = e
json.dump(km, open(V + "/key_map.json", "w"), indent=1)
json.dump(keys, open(V + "/keys.json", "w"), indent=1)
json.dump(sub, open(V + "/keys_f.json", "w"), indent=1)
Vw = os.path.join(ROOT, "vision", "v057")
tpl = open("tools/cycle/prompts/scorer_template.txt").read()
open("tpdb_work/v057prompts/scorer_f.txt", "w").write(tpl.replace("@V@", Vw).replace("@A@", "135").replace("@B@", "136").replace("@N@", "2").replace("@T@", "f"))
r17 = open("tpdb_work/v057prompts/reader_17.txt").read()
head, rest = r17.split("Images (open each with the Read tool):\n", 1)
tail = rest[rest.index("For each picture"):]
pics = [os.path.join(Vw, "blind", k + ".png") for k in add]
txt = head.replace("Look at 7 cartoon", "Look at 2 cartoon").replace("only the 7 image", "only the 2 image") + "Images (open each with the Read tool):\n" + "\n".join(pics) + "\n\n" + tail.replace("just the 7 file", "just the 2 file")
assert " 7 " not in txt
open("tpdb_work/v057prompts/reader_18.txt", "w").write(txt)
print(len(km), "pictures,", sum(len(v["items"]) for v in keys.values()), "items; pic_135", len(sub["pic_135"]["items"]), "pic_136", len(sub["pic_136"]["items"]))
print(txt[:700])
