"""Fill README_v0.18.template.md with the generated set, counts, the fifteen screens and the gate.

    python vision/fill_readme.py
Text that depends on reading the screen (the introduction's result and the screen narrative) lives in
vision/readme_v018_text.json, written after the screen.
"""
import glob
import json
import os

T = open("README_v0.18.template.md").read()
TXT = json.load(open("vision/readme_v018_text.json")) if os.path.exists("vision/readme_v018_text.json") else {}
order = {"garden": 0, "park": 1, "street": 2, "playground": 3}


def load(d):
    return [json.load(open(f)) for f in sorted(glob.glob(os.path.join(d, "T*.json")))]


def n_items(k):
    return f"{k} item" + ("" if k == 1 else "s")


recs = load("scenes")
recs.sort(key=lambda r: (r["tier"], order[r["setting"]], bool(r.get("isomorph_of"))))
rows = ["| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |",
        "|---|---|---|---|---|---|---|---|---|"]
for r in recs:
    p = r["predicted"]["theta_0"]
    name = r["name"] + (f" (isomorph of {r['isomorph_of']})" if r.get("isomorph_of") else "")
    inf = "—" if p["inference"] is None else f"{p['inference']:.3f}"
    rows.append(f"| {name} | {r['counts']['content']} | {r['counts']['inference_units']} ({r['counts']['contradictions']}) | {r['scene_load']} | "
                f"{p['content']:.3f} | {inf} | {r['clutter']['objects']} | "
                f"{r['clutter']['edge_density']:.3f} | {', '.join(t['id'].replace('_', ' ') for t in r['templates'])} |")
main = [r for r in recs if not r.get("isomorph_of")]
intier = sum(1 for r in recs if r["in_tier"])
T = T.replace("__SCENES_TABLE__", f"{len(main)} showcase pictures (one per setting and tier) and {len(recs) - len(main)} isomorphs. "
              f"{intier} of {len(recs)} meet every row of their tier's band and every placement and legibility rule.\n\n" + "\n".join(rows))
isos = [r for r in recs if r.get("isomorph_of")]
if isos:
    dc = max(r["isomorph_check"]["content_diff"] for r in isos)
    di = max(r["isomorph_check"]["inference_diff"] for r in isos)
    T = T.replace("__ISO_TEXT__", f"Isomorph pairs differ by at most {dc:.3f} in content and {di:.3f} in inference completeness, with identical item signatures.")
else:
    T = T.replace("__ISO_TEXT__", "")
C = json.load(open("combos.json"))
C = list(C.values()) if isinstance(C, dict) else C
crow = ["| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |", "|---|---|---|---|---|---|"]
for c in sorted(C, key=lambda c: (order[c["setting"]], c["tier"])):
    crow.append(f"| {c['setting']} | {c['tier']} | {c['structures']:,} | {c['signatures']} | {c['largest_isomorph_pool']:,} | 10^{c['log10_scenes']} |")
tot = sum(c["structures"] for c in C)
T = T.replace("__COMBOS_TABLE__", "\n".join(crow) + f"\n\nIn all {tot:,} structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.")
T = T.replace("__GALLERY_N__", str(len(glob.glob("assets/cast/gallery018/*.json"))))

# ------------------------------------------------------------------ the fifteen screens and the gate
S = json.load(open("vision/screen_summary.json"))
vs = [("v04", "v0.4"), ("v05", "v0.5"), ("v06", "v0.6"), ("v07", "v0.7"), ("v08", "v0.8"), ("v09", "v0.9"), ("v010", "v0.10"), ("v011", "v0.11"), ("v012", "v0.12"), ("v013", "v0.13"), ("v014", "v0.14"), ("v015", "v0.15"), ("v016", "v0.16"), ("v017", "v0.17"), ("v018", "v0.18")]
lab = [("entity", "Things"), ("action", "Actions"), ("inference", "Inferences"), ("contradiction", "Contradictions"), ("overall", "All items")]
tr = ["| | " + " | ".join(f"{n} ({S[k]['pictures']} pictures)" for k, n in vs) + " |", "|---" * (len(vs) + 1) + "|"]
for k, l in lab:
    tr.append(f"| {l}, mean score | " + " | ".join(format(S[v]["mean"].get(k, 0), ".2f") for v, _ in vs) + " |")
tr.append("| Items misread | " + " | ".join(f"{S[v]['misreads']} of {S[v]['items']}" for v, _ in vs) + " |")
tr.append("| Unintended oddities per picture | " + " | ".join(f"{S[v]['oddities'] / S[v]['pictures']:.1f}" for v, _ in vs) + " |")
pr = S["v018"].get("probes", {})
b6, b7 = S["v017"]["by_template"], S["v018"]["by_template"]
REDRAWN = ["wave", "play_catch", "about_to_trip", "cat_sleeping", "cat_stalks_bird", "ducks_bread"]
red = ["| Template | v0.17 | v0.18 | v0.18 meaning items |", "|---|---|---|---|"]
for t in REDRAWN:
    a, b = b6.get(t), b7.get(t)
    red.append(f"| `{t}` | " + (f"{a['mean']:.2f} ({n_items(a['items'])})" if a else "—") + " | "
               + (f"{b['mean']:.2f} ({n_items(b['items'])})" if b else "not drawn") + " | "
               + ("—" if not b or b["meaning_mean"] is None else f"{b['meaning_mean']:.2f} ({b['meaning_items']})") + " |")
G = json.load(open("vision/v018/gate.json"))
by = {st: sorted(t for t, v in G.items() if v["status"] == st) for st in ("pass", "too_few", "fail")}
g6 = json.load(open("vision/v010/gate.json")) if os.path.exists("vision/v010/gate.json") else {}
g7 = json.load(open("vision/v011/gate.json")) if os.path.exists("vision/v011/gate.json") else {}
g8 = json.load(open("vision/v012/gate.json")) if os.path.exists("vision/v012/gate.json") else {}
g5 = json.load(open("vision/v09/gate.json")) if os.path.exists("vision/v09/gate.json") else {}
g9 = json.load(open("vision/v013/gate.json")) if os.path.exists("vision/v013/gate.json") else {}
gr = json.load(open("vision/v09_retest/gate.json")) if os.path.exists("vision/v09_retest/gate.json") else {}
g10 = json.load(open("vision/v014/gate.json")) if os.path.exists("vision/v014/gate.json") else {}
g11 = json.load(open("vision/v015/gate.json")) if os.path.exists("vision/v015/gate.json") else {}
g12 = json.load(open("vision/v016/gate.json")) if os.path.exists("vision/v016/gate.json") else {}
g13 = json.load(open("vision/v017/gate.json")) if os.path.exists("vision/v017/gate.json") else {}
gl = [f"| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for st, l in (("pass", "Pass (mean at least 0.9, at least two pictures, no misread)"), ("too_few", "Read well, but in fewer than two pictures"), ("fail", "Fail")):
    cnt = lambda g: sum(1 for v in g.values() if v['status'] == st) if g else '—'
    gl.append(f"| {l} | {cnt(g5)} | {cnt(gr)} | {cnt(g6)} | {cnt(g7)} | {cnt(g8)} | {cnt(g9)} | {cnt(g10)} | {cnt(g11)} | {cnt(g12)} | {cnt(g13)} | {len(by[st])} |")
fails = ["| Template | v0.18 mean | Pictures | Misreads |", "|---|---|---|---|"] + [
    f"| `{t}` | {G[t]['mean']:.2f} ({n_items(G[t]['items'])}) | {G[t]['pictures']} | {G[t]['misreads']} |" for t in sorted(by["fail"] + by["too_few"], key=lambda t: G[t]["mean"])]
probes = load("probes")
sec = ["## The fifteenth blind screen", "",
       f"{TXT.get('readers', 'Fresh')} readers, who had never seen the key, described every picture of the new set and "
       f"{len(probes)} probe pictures; {TXT.get('scorers', 'two')} separate scorers, each given part of the pictures and the same prompt, marked each "
       "scored item against the key, exactly as in the earlier screens. "
       f"The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template "
       "appeared in at least three screened pictures, as in v0.10 to v0.17.", "",
       "\n".join(tr), "", TXT.get("screen", ""), "", "The template that failed the v0.17 gate and the templates whose visuals or placement were refined for its oddities (mean of each template's scored items; "
       "inference and contradiction items alone in the last column):", "", "\n".join(red), "", TXT.get("redrawn", ""), "",
       "### The legibility gate", "", "\n".join(gl), "", TXT.get("gate", ""), ""]
if len(fails) > 2:
    sec += ["Templates that did not pass (`vision/flaws_v018.md` gives what the readers saw and the next fix):", "", "\n".join(fails), ""]
T = T.replace("__SCREEN_SECTION__", "\n".join(s for s in sec).rstrip())
DESIGN = TXT.get("design", "")
REBUILD = "scenes/" + sorted(r["name"] for r in recs if r["tier"] == 3 and r["setting"] == "park" and not r.get("isomorph_of"))[0] + ".json"
T = T.replace("__INTRO_RESULT__", TXT.get("intro", ""))
T = T.replace("__LIMITS__", open("vision/limits.txt").read().strip())
T = T.replace("__DESIGN_TESTS__", DESIGN)
T = T.replace("__REBUILD_EXAMPLE__", REBUILD)
open("README_v0.18.md", "w").write(T)
print("README_v0.18.md written")
