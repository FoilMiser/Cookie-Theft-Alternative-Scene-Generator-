"""Copy bench crops into a blind round folder and write reader prompts.

    python iso_round.py <bench_dir> <round_dir> <prompt_dir> <tag> name1 name2 ...

Images are shuffled and numbered iso_01..; map.json keeps the names; each reader gets ISO_PER images (default two) that come
from different bench cases (and different templates where possible)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, WORK, TAG, PREV  # noqa: E402
import json, os, random, shutil, sys

bench, rnd, pdir, tag = sys.argv[1:5]
names = sys.argv[5:]
os.makedirs(rnd, exist_ok=True)
os.makedirs(pdir, exist_ok=True)
rng = random.Random(hash(tag) & 0xffff)
order = names[:]
rng.shuffle(order)
mp = {}
for i, n in enumerate(order, 1):
    k = f"iso_{i:02d}"
    shutil.copy(os.path.join(bench, n + ".png"), os.path.join(rnd, k + ".png"))
    mp[k] = n
json.dump(mp, open(os.path.join(rnd, "map.json"), "w"), indent=1)
keys = list(mp)
# group images whose case names share no prefix (so one reader never sees two takes of the same thing)
PER = int(os.environ.get("ISO_PER", "2"))
pairs, left = [], keys[:]
while left:
    g = [left.pop(0)]
    while len(g) < PER:
        j = next((i for i, b in enumerate(left) if mp[b][:3] not in {mp[x][:3] for x in g}), None)
        if j is None:
            break
        g.append(left.pop(j))
    pairs.append(g)
TEXT = """You are taking part in a picture-legibility check. You will see {n} small cut-out{s}, each taken from a different cartoon picture. You must NOT open, list or search any other file or folder (no Glob, Grep, ls, or reading JSON/code) — only the image files named below, so your reading stays blind. Look at each cut-out as a whole, the way it opens with the Read tool: do not crop, zoom, enlarge or otherwise process the images. Treat each cut-out on its own; they are unrelated.

Images (open each with the Read tool):
{imgs}

For each cut-out, write a file {rnd}/desc_iso_NN.md (NN = the number in its file name), with the Write tool and not from the shell, with:
1. "What I see": 2–5 sentences: who or what is in it, what any person or animal is doing, and what any object is or seems to be for.
2. "Unsure or ambiguous": anything you could not make out or that could be read two ways (say both readings), and anything that looks unintentionally strange (things floating, objects passing through each other, odd shapes or proportions, body parts that look detached or oddly joined).

Be literal about what you actually see; don't guess what a test designer intended. When done, reply with just the file paths: you know their names, so do not list the folder to check them.
"""
for i, p in enumerate(pairs, 1):
    imgs = "\n".join(os.path.join(rnd, k + ".png") for k in p)
    open(os.path.join(pdir, f"{tag}_{i}.txt"), "w").write(TEXT.format(n=len(p), s="s" if len(p) > 1 else "", imgs=imgs, rnd=rnd))
print(len(pairs), "readers;", json.dumps(mp))
