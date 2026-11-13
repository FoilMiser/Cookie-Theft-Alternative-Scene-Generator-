"""Fill tools/cycle/README.template.md with the generated set, counts, the forty-nine screens and the gate.

    python vision/fill_readme.py
Text that depends on reading the screen (the introduction's result and the screen narrative) lives in
vision/readme_v052_text.json, written after the screen.
"""
import glob
import json
import os

T = open("tools/cycle/README.template.md", encoding="utf-8").read()
TXT = json.load(open("vision/readme_v052_text.json", encoding="utf-8")) if os.path.exists("vision/readme_v052_text.json") else {}
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
T = T.replace("__GALLERY_N__", str(len(glob.glob("assets/cast/gallery052/*.json"))))

# ------------------------------------------------------------------ the forty-nine screens and the gate
S = json.load(open("vision/screen_summary.json"))
vs = [("v04", "v0.4"), ("v05", "v0.5"), ("v06", "v0.6"), ("v07", "v0.7"), ("v08", "v0.8"), ("v09", "v0.9"), ("v010", "v0.10"), ("v011", "v0.11"), ("v012", "v0.12"), ("v013", "v0.13"), ("v014", "v0.14"), ("v015", "v0.15"), ("v016", "v0.16"), ("v017", "v0.17"), ("v018", "v0.18"), ("v019", "v0.19"), ("v020", "v0.20"), ("v021", "v0.21"), ("v022", "v0.22"), ("v023", "v0.23"), ("v024", "v0.24"), ("v025", "v0.25"), ("v026", "v0.26"), ("v027", "v0.27"), ("v028", "v0.28"), ("v029", "v0.29"), ("v030", "v0.30"), ("v031", "v0.31"), ("v032", "v0.32"), ("v033", "v0.33"), ("v034", "v0.34"), ("v035", "v0.35"), ("v036", "v0.36"), ("v037", "v0.37"), ("v038", "v0.38"), ("v039", "v0.39"), ("v040", "v0.40"), ("v041", "v0.41"), ("v042", "v0.42"), ("v043", "v0.43"), ("v044", "v0.44"), ("v045", "v0.45"), ("v046", "v0.46"), ("v047", "v0.47"), ("v048", "v0.48"), ("v049", "v0.49"), ("v050", "v0.50"), ("v051", "v0.51"), ("v052", "v0.52")]
lab = [("entity", "Things"), ("action", "Actions"), ("inference", "Inferences"), ("contradiction", "Contradictions"), ("overall", "All items")]
tr = ["| | " + " | ".join(f"{n} ({S[k]['pictures']} pictures)" for k, n in vs) + " |", "|---" * (len(vs) + 1) + "|"]
for k, l in lab:
    tr.append(f"| {l}, mean score | " + " | ".join(format(S[v]["mean"].get(k, 0), ".2f") for v, _ in vs) + " |")
tr.append("| Items misread | " + " | ".join(f"{S[v]['misreads']} of {S[v]['items']}" for v, _ in vs) + " |")
tr.append("| Oddities per picture, as logged by the scorers | " + " | ".join(f"{S[v]['oddities'] / S[v]['pictures']:.1f}" for v, _ in vs) + " |")
tr.append("| Readers' remarks per picture (recounted in v0.26) | " + " | ".join(f"{S[v]['remarks']:.1f}" if S[v].get("remarks") else "—" for v, _ in vs) + " |")
pr = S["v052"].get("probes", {})
b6, b7 = S["v051"]["by_template"], S["v052"]["by_template"]
REDRAWN = ["square_wheel", "bird_steals", "ducks_bread", "blocked_hose", "ice_cream", "floating_box", "cat_stalks_bird", "jump",
           "plant_flowers", "seesaw_heavy", "play_catch", "windy_hat", "sweep_fork", "sweep", "read_bench", "wave", "hang_laundry",
           "paint_fence"]
red = ["| Template | v0.51 | v0.52 | v0.52 meaning items |", "|---|---|---|---|"]
for t in REDRAWN:
    a, b = b6.get(t), b7.get(t)
    red.append(f"| `{t}` | " + (f"{a['mean']:.2f} ({n_items(a['items'])})" if a else "—") + " | "
               + (f"{b['mean']:.2f} ({n_items(b['items'])})" if b else "not drawn") + " | "
               + ("—" if not b or b["meaning_mean"] is None else f"{b['meaning_mean']:.2f} ({b['meaning_items']})") + " |")
G = json.load(open("vision/v052/gate.json"))
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
g14 = json.load(open("vision/v018/gate.json")) if os.path.exists("vision/v018/gate.json") else {}
g15 = json.load(open("vision/v019/gate.json")) if os.path.exists("vision/v019/gate.json") else {}
g16 = json.load(open("vision/v020/gate.json")) if os.path.exists("vision/v020/gate.json") else {}
g17 = json.load(open("vision/v021/gate.json")) if os.path.exists("vision/v021/gate.json") else {}
g18 = json.load(open("vision/v022/gate.json")) if os.path.exists("vision/v022/gate.json") else {}
g19 = json.load(open("vision/v023/gate.json")) if os.path.exists("vision/v023/gate.json") else {}
g20 = json.load(open("vision/v024/gate.json")) if os.path.exists("vision/v024/gate.json") else {}
g21 = json.load(open("vision/v025/gate.json")) if os.path.exists("vision/v025/gate.json") else {}
g22 = json.load(open("vision/v026/gate.json")) if os.path.exists("vision/v026/gate.json") else {}
g23 = json.load(open("vision/v027/gate.json")) if os.path.exists("vision/v027/gate.json") else {}
g24 = json.load(open("vision/v028/gate.json")) if os.path.exists("vision/v028/gate.json") else {}
g25 = json.load(open("vision/v029/gate.json")) if os.path.exists("vision/v029/gate.json") else {}
g26 = json.load(open("vision/v030/gate.json")) if os.path.exists("vision/v030/gate.json") else {}
g27 = json.load(open("vision/v031/gate.json")) if os.path.exists("vision/v031/gate.json") else {}
g28 = json.load(open("vision/v032/gate.json")) if os.path.exists("vision/v032/gate.json") else {}
g29 = json.load(open("vision/v033/gate.json")) if os.path.exists("vision/v033/gate.json") else {}
g30 = json.load(open("vision/v034/gate.json")) if os.path.exists("vision/v034/gate.json") else {}
g31 = json.load(open("vision/v035/gate.json")) if os.path.exists("vision/v035/gate.json") else {}
g32 = json.load(open("vision/v036/gate.json")) if os.path.exists("vision/v036/gate.json") else {}
g33 = json.load(open("vision/v037/gate.json")) if os.path.exists("vision/v037/gate.json") else {}
g34 = json.load(open("vision/v038/gate.json")) if os.path.exists("vision/v038/gate.json") else {}
g35 = json.load(open("vision/v039/gate.json")) if os.path.exists("vision/v039/gate.json") else {}
g36 = json.load(open("vision/v040/gate.json")) if os.path.exists("vision/v040/gate.json") else {}
g37 = json.load(open("vision/v041/gate.json")) if os.path.exists("vision/v041/gate.json") else {}
g38 = json.load(open("vision/v042/gate.json")) if os.path.exists("vision/v042/gate.json") else {}
g39 = json.load(open("vision/v043/gate.json")) if os.path.exists("vision/v043/gate.json") else {}
g40 = json.load(open("vision/v044/gate.json")) if os.path.exists("vision/v044/gate.json") else {}
g41 = json.load(open("vision/v045/gate.json")) if os.path.exists("vision/v045/gate.json") else {}
g42 = json.load(open("vision/v046/gate.json")) if os.path.exists("vision/v046/gate.json") else {}
g43 = json.load(open("vision/v047/gate.json")) if os.path.exists("vision/v047/gate.json") else {}
g44 = json.load(open("vision/v048/gate.json")) if os.path.exists("vision/v048/gate.json") else {}
g45 = json.load(open("vision/v049/gate.json")) if os.path.exists("vision/v049/gate.json") else {}
g46 = json.load(open("vision/v050/gate.json")) if os.path.exists("vision/v050/gate.json") else {}
g47 = json.load(open("vision/v051/gate.json")) if os.path.exists("vision/v051/gate.json") else {}
gl = [f"| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 | v0.32 | v0.33 | v0.34 | v0.35 | v0.36 | v0.37 | v0.38 | v0.39 | v0.40 | v0.41 | v0.42 | v0.43 | v0.44 | v0.45 | v0.46 | v0.47 | v0.48 | v0.49 | v0.50 | v0.51 | v0.52 |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for st, l in (("pass", "Pass (mean at least 0.9, at least two pictures, no misread)"), ("too_few", "Read well, but in fewer than two pictures"), ("fail", "Fail")):
    cnt = lambda g: sum(1 for v in g.values() if v['status'] == st) if g else '—'
    gl.append(f"| {l} | {cnt(g5)} | {cnt(gr)} | {cnt(g6)} | {cnt(g7)} | {cnt(g8)} | {cnt(g9)} | {cnt(g10)} | {cnt(g11)} | {cnt(g12)} | {cnt(g13)} | {cnt(g14)} | {cnt(g15)} | {cnt(g16)} | {cnt(g17)} | {cnt(g18)} | {cnt(g19)} | {cnt(g20)} | {cnt(g21)} | {cnt(g22)} | {cnt(g23)} | {cnt(g24)} | {cnt(g25)} | {cnt(g26)} | {cnt(g27)} | {cnt(g28)} | {cnt(g29)} | {cnt(g30)} | {cnt(g31)} | {cnt(g32)} | {cnt(g33)} | {cnt(g34)} | {cnt(g35)} | {cnt(g36)} | {cnt(g37)} | {cnt(g38)} | {cnt(g39)} | {cnt(g40)} | {cnt(g41)} | {cnt(g42)} | {cnt(g43)} | {cnt(g44)} | {cnt(g45)} | {cnt(g46)} | {cnt(g47)} | {len(by[st])} |")
fails = ["| Template | v0.52 mean | Pictures | Misreads |", "|---|---|---|---|"] + [
    f"| `{t}` | {G[t]['mean']:.2f} ({n_items(G[t]['items'])}) | {G[t]['pictures']} | {G[t]['misreads']} |" for t in sorted(by["fail"] + by["too_few"], key=lambda t: G[t]["mean"])]
probes = load("probes")
sec = ["## The forty-ninth blind screen", "",
       f"{TXT.get('readers', 'Fresh')} readers, who had never seen the key, described every picture of the new set and "
       f"{len(probes)} probe pictures; {TXT.get('scorers', 'two')} separate scorers, each given part of the pictures and the same prompt, marked each "
       "scored item against the key, exactly as in the earlier screens. "
       f"The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template "
       "appeared in at least three screened pictures, as in v0.10 to v0.51.", "",
       "\n".join(tr), "", TXT.get("screen", ""), "", "The square wheel, which fell under the gate with nothing of it drawn; the thief bird and the bread for the ducks, the two others under full marks; the stopped hose and the ice cream, which were under full marks in v0.51; the templates that the next list names; and six plain events whose figures raise or reach an arm in the new sleeves (mean of each template's scored items; "
       "inference and contradiction items alone in the last column):", "", "\n".join(red), "", TXT.get("redrawn", ""), "",
       "### The legibility gate", "", "\n".join(gl), "", TXT.get("gate", ""), ""]
if len(fails) > 2:
    sec += ["Templates that did not pass (`vision/flaws_v052.md` gives what the readers saw and the next fix):", "", "\n".join(fails), ""]
T = T.replace("__SCREEN_SECTION__", "\n".join(s for s in sec).rstrip())
DESIGN = TXT.get("design", "")
REBUILD = "scenes/" + sorted(r["name"] for r in recs if r["tier"] == 3 and r["setting"] == "park" and not r.get("isomorph_of"))[0] + ".json"
T = T.replace("__INTRO_RESULT__", TXT.get("intro", ""))
T = T.replace("__LIMITS__", open("vision/limits.txt").read().strip())
T = T.replace("__DESIGN_TESTS__", DESIGN)
T = T.replace("__REBUILD_EXAMPLE__", REBUILD)
T = T.replace("__INSPECTION__", TXT.get("inspection", ""))
T = T.replace("__ZIP_MB__", TXT.get("zip_mb", "150"))
T = T.replace("__CALIB_NOTE__", TXT.get("calib", ""))
open("README_v0.52.md", "w", encoding="utf-8", newline="\n").write(T)
print("README_v0.52.md written")
