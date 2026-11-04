"""The readers' remarks by what they are about: how many pictures of a screen remark on each topic, for two screens side by side.

    python vision/remark_topics.py vision/v026 vision/v027

A keyword count over the "unsure" sections, so a rough sort and not a reading: a hit may be a hedge, a remark may use other words, and a
topic can rise because a picture carries more of the thing. It says where to read, and whether a named complaint moved.
"""
import glob
import os
import re
import sys

TOPICS = {
    "face hidden or hard to read": r"(face|head|expression|eyes)[^.]{0,60}(hidden|turned away|hard to read|hard to see|unclear|away from|backwards|upside)",
    "marks on a face": r"(mark|marks|dots|smudge|spots|shape)[^.]{0,40}(face|mouth|eye|cheek|chin)|(face|mouth|cheek|chin)[^.]{0,40}(mark|marks|dots|smudge|spots)",
    "beard as a strap or mask": r"beard[^.]{0,80}(mask|strap|merge|join|covering)|chin strap|face mask",
    "thin or long body or legs": r"(long|thin|stretched|lanky|skinny|narrow)[^.]{0,30}(legs|body|torso|figure)|(legs|body|torso|figure)[^.]{0,30}(long|thin|stretched|lanky|skinny|narrow)",
    "stiff or awkward pose": r"\b(stiff|awkward|oddly bent|twisted|rubbery|contorted)\b",
    "feet overlapping": r"(feet|shoes)[^.]{0,40}(overlap|tangled|merge|together)",
    "shadows": r"\bshadows?\b",
    "scale": r"\b(oversized|too (big|large|small)|very (large|big|small)|out of scale|tiny|scale)\b",
    "the seesaw's plank": r"plank",
    "the hose stiff or jointed": r"hose[^.]{0,80}(stiff|pole|pipe|rigid|joint|not (quite )?(joined|connected))|(stiff|rigid)[^.]{0,40}hose",
    "the hose's bulge": r"bulge|pad\b|fat fitting",
    "water drawn solid": r"(solid|curtain|tube|rigid|beaded|straight)[^.]{0,40}(water|stream|spray|jet)|(water|stream|spray|jet)[^.]{0,60}(solid|curtain|tube|rigid|beaded)",
    "pasted on, sticker, clump": r"sticker|pasted|planet|separate (leaf|clump)|clump",
    "a branch to hold it": r"branch",
    "the roller": r"roller|brush",
    "the bicycle's wheels": r"(disc|solid|black)[^.]{0,20}wheel|wheel[^.]{0,30}(solid|disc|black)|\brack\b",
    "a figure over the pond": r"pond[^.]{0,80}(standing in|in the water|overlap|in front of the)|(standing in|overlap)[^.]{0,40}(pond|water)",
    "goat as something else": r"(sheep|lamb|white dog|ram\b)",
    "legs walking another way": r"(feet|legs|stride)[^.]{0,60}(toward|towards|opposite|other way|different direction)",
}


def unsure(t):
    m = re.search(r"(?im)^#*\s*\**\s*(3\.\s*)?\"?unsure.*$", t)
    return t[m.end():] if m else ""


def count(d):
    texts = {f[-5:-3]: unsure(open(f, encoding="utf-8").read()) for f in sorted(glob.glob(os.path.join(d, "desc_pic_*.md")))}
    return {k: sorted(p for p, t in texts.items() if re.search(pat, t, re.I)) for k, pat in TOPICS.items()}


a, b = sys.argv[1], sys.argv[2]
ca, cb = count(a), count(b)
print(f"{'':30s} {os.path.basename(a):>6s} {os.path.basename(b):>6s}  pictures of the second")
for k in TOPICS:
    print(f"{k:30s} {len(ca[k]):6d} {len(cb[k]):6d}  {' '.join(cb[k]) if len(cb[k]) <= 12 else ''}")
