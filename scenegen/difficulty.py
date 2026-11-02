"""Item difficulty and picture difficulty (TPDB Difficulty Model Spec, starting weights).

b = b0 + type + 0.6*h - 0.8*A - 0.5*s - 0.3*r + 1.2*d - 0.3*f + domain + 0.12*L
P(produce | theta) = logistic(theta - b)

  s  z-score of ln(visible area / canvas area) against the item library reference
  r  independent cues - 1 (inference and contradiction items)
  d  cue-effect centroid distance / canvas diagonal (inference items)
  f  Zipf frequency of the item's key word - 4
  a  age of acquisition of the key word (Kuperman et al. 2012 lemma ratings, years), weight 0 until the pilot
  L  scored events in the scene (template instances)

The salience reference (mean and SD of ln area fraction) is fixed from the Garden prototype's
item library (house z = +1.90, single drip z = -3.22), so scores are comparable across scenes.
"""
import csv
import hashlib
import math
import os
from importlib.metadata import version as _pkg_version

from wordfreq import zipf_frequency

WORDFREQ_VERSION = _pkg_version("wordfreq")

WEIGHTS = {
    "b0": -1.0,
    # v0.20: the key word's frequency (and age of acquisition) apply only to entities and actions; inference and
    # contradiction items are scored on meaning, so their type weights are re-centred by -0.3 x the mean f those items had
    # in the v0.19 set (0.709 for inferences, 0.737 for contradictions), which keeps the set's predictions where they were
    "type": {"entity": 0.0, "action": 0.3, "inference": 0.39, "contradiction_notice": 0.58, "contradiction_explain": 1.18},
    "chain": 0.6, "animate": -0.8, "salience": -0.5, "redundancy": -0.3, "separation": 1.2, "frequency": -0.3,
    "domain": {None: 0.0, "physical": 0.0, "biological": -0.2, "functional": 0.2},
    "load": 0.12,
    "aoa": 0.0,     # recorded on every item so the pilot can test it; no effect on any picture until then
}
SALIENCE_REF = {"mu": -4.65, "sd": 1.41, "source": "Garden prototype item library (house +1.90, drip -3.22)"}

TIERS = {
    1: {"content": (4, 6), "inference": (0, 0), "contradictions": 0, "pc": (0.75, 0.81), "pi": None, "objects": (12, 18)},
    2: {"content": (8, 10), "inference": (1, 1), "contradictions": 1, "pc": (0.68, 0.74), "pi": (0.35, 0.45), "objects": (16, 24)},
    3: {"content": (12, 15), "inference": (2, 3), "contradictions": 1, "pc": (0.61, 0.67), "pi": (0.28, 0.38), "objects": (20, 30)},
    4: {"content": (18, 22), "inference": (4, 5), "contradictions": 2, "pc": (0.54, 0.60), "pi": (0.20, 0.30), "objects": (26, 38)},
}
CENTER = {t: ((v["pc"][0] + v["pc"][1]) / 2, (v["pi"][0] + v["pi"][1]) / 2 if v["pi"] else None) for t, v in TIERS.items()}

CONTENT_TYPES = ("entity", "action")
INFERENCE_TYPES = ("inference", "contradiction_notice", "contradiction_explain")
_ZIPF = {}


# Age of acquisition: a verbatim excerpt of the Kuperman et al. (2012) ratings (norms/aoa_kuperman2012.tsv). A key
# word is looked up as itself when it is rated, else as its lemma (the expanded list's Lemma_highest_PoS convention);
# compounds through an override; the largest value over the words of a multiword key, mirroring the smallest Zipf.
AOA_FILE = os.path.join(os.path.dirname(__file__), "norms", "aoa_kuperman2012.tsv")
AOA_SHA256 = hashlib.sha256(open(AOA_FILE, "rb").read()).hexdigest()
AOA_CENTER = 4.47       # mean over the item key words in use (v0.19), so the intercept stays comparable if the weight is set
AOA_LEMMA = {"birds": "bird", "hills": "hill", "clouds": "cloud", "flowers": "flower", "footprints": "footprint", "shops": "shop",
             "leaves": "leaf", "begging": "beg", "dropped": "drop", "floating": "float", "jumping": "jump", "running": "run",
             "sitting": "sit", "standing": "stand", "stealing": "steal", "sweeping": "sweep", "waving": "wave",
             "drinking": "drink", "reading": "read", "pointing": "point", "planting": "plant", "lost": "lose", "stuck": "stick",
             "eating": "eat", "watering": "water", "feeding": "feed", "carrying": "carry", "kicking": "kick",
             "throwing": "throw", "flying": "fly", "hanging": "hang", "digging": "dig", "raking": "rake", "reaching": "reach"}
AOA_OVERRIDE = {"ice cream": "icecream"}
_AOA = None


def _aoa_table():
    global _AOA
    if _AOA is None:
        with open(AOA_FILE, encoding="utf-8") as fh:
            rows = csv.DictReader((ln for ln in fh if not ln.startswith("#")), delimiter="\t")
            _AOA = {r["Word"]: float(r["Rating.Mean"]) for r in rows}
    return _AOA


def aoa(word):
    """Age of acquisition (years) of an item's key word; an error for a word the norms do not cover."""
    t = _aoa_table()
    w = AOA_OVERRIDE.get(word, word)
    vals = []
    for part in w.split():
        lw = part if part in t else AOA_LEMMA.get(part, part)
        if lw not in t:
            raise ValueError(f"no age-of-acquisition rating for key word {word!r} (looked up {lw!r})")
        vals.append(t[lw])
    return max(vals)


def lexical_versions():
    return {"wordfreq": WORDFREQ_VERSION, "aoa_norms": "scenegen/norms/aoa_kuperman2012.tsv", "aoa_sha256": AOA_SHA256,
            "aoa_center": AOA_CENTER, "zipf_lookup": dict(ZIPF_LOOKUP), "zipf_override": dict(ZIPF_OVERRIDE),
            "lexical_types": list(CONTENT_TYPES), "weights": {k: v for k, v in WEIGHTS.items()}}


# v0.20: a key word is looked up in its everyday sense ("leaves" as the plural of leaf, not the verb); a multiword or
# hyphenated key needs an explicit value (split, it took the frequency of a common part: "see-saw" 5.27 via "see"),
# and a word wordfreq does not know is an error rather than a Zipf of 0 (f = -4)
ZIPF_LOOKUP = {"leaves": "leaf"}
ZIPF_OVERRIDE = {"ice cream": 4.47}     # wordfreq's estimate for the phrase (min of its words gave 4.62, "cream")


def zipf(word):
    if word not in _ZIPF:
        w = ZIPF_LOOKUP.get(word, word)
        if w in ZIPF_OVERRIDE:
            z = ZIPF_OVERRIDE[w]
        elif " " in w or "-" in w:
            raise ValueError(f"multiword key {word!r} needs an entry in ZIPF_OVERRIDE")
        else:
            z = zipf_frequency(w, "en")
            if z <= 0:
                raise ValueError(f"wordfreq has no frequency for key word {word!r}")
        _ZIPF[word] = z
    return _ZIPF[word]


def logistic(x):
    return 1.0 / (1.0 + math.exp(-x))


def salience_z(area_px, canvas_px):
    a = max(area_px, 1.0) / canvas_px
    return (math.log(a) - SALIENCE_REF["mu"]) / SALIENCE_REF["sd"]


def item_b(feat, L, w=WEIGHTS):
    b = w["b0"] + w["type"][feat["type"]]
    b += w["chain"] * feat["chain"]
    b += w["animate"] * (1 if feat["animate"] else 0)
    b += w["salience"] * feat["s"]
    b += w["redundancy"] * feat["r"]
    b += w["separation"] * feat["d"]
    b += w["frequency"] * feat["f"]
    b += w.get("aoa", 0.0) * (feat.get("a", AOA_CENTER) - AOA_CENTER)
    if feat["type"].startswith("contradiction"):
        b += w["domain"].get(feat.get("domain"), 0.0)
    b += w["load"] * L
    return b


def completeness(items, theta=0.0):
    c = [logistic(theta - it["b"]) for it in items if it["type"] in CONTENT_TYPES]
    i = [logistic(theta - it["b"]) for it in items if it["type"] in INFERENCE_TYPES]
    return (sum(c) / len(c) if c else None), (sum(i) / len(i) if i else None)


def in_band(tier, pc, pi, n_content, n_units, n_contra):
    T = TIERS[tier]
    ok = {"content_count": T["content"][0] <= n_content <= T["content"][1],
          "inference_units": T["inference"][0] <= n_units <= T["inference"][1],
          "contradictions": n_contra <= T["contradictions"],
          "content_completeness": pc is not None and T["pc"][0] <= pc <= T["pc"][1]}
    ok["inference_completeness"] = (pi is None and T["pi"] is None) or (pi is not None and T["pi"] is not None and T["pi"][0] <= pi <= T["pi"][1])
    return ok


def check_aoa(path):
    """Compare the bundled excerpt with a copy of the original norms: the BRM list (Word, Rating.Mean) or the expanded
    51,715-word list (Word, AoA_Kup_lem), as .xlsx, .csv or .tsv. Prints every word that differs or is missing."""
    if path.endswith(".xlsx"):
        import openpyxl
        ws = openpyxl.load_workbook(path, read_only=True, data_only=True).active
        it = ws.iter_rows(values_only=True)
        head = [str(h) for h in next(it)]
        rows = [dict(zip(head, r)) for r in it]
    else:
        with open(path, encoding="utf-8-sig") as fh:
            rows = list(csv.DictReader(fh, delimiter="\t" if path.endswith(".tsv") else ","))
    col = "AoA_Kup_lem" if rows and "AoA_Kup_lem" in rows[0] else "Rating.Mean"
    ref = {str(r["Word"]): r[col] for r in rows if r.get(col) not in (None, "", "NA")}
    bad = 0
    for w, v in sorted(_aoa_table().items()):
        o = ref.get(w)
        if o is None or abs(float(o) - v) > 0.005:
            bad += 1
            print(f"{w}: bundled {v}, {os.path.basename(path)} {o}")
    print(f"{len(_aoa_table()) - bad} of {len(_aoa_table())} bundled ratings match {os.path.basename(path)} ({col})")
    return bad == 0


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "--check-aoa":
        sys.exit(0 if check_aoa(sys.argv[2]) else 1)
    print("usage: python -m scenegen.difficulty --check-aoa <AoA_ratings_Kuperman_et_al_BRM.xlsx | AoA_51715_words.xlsx>")
