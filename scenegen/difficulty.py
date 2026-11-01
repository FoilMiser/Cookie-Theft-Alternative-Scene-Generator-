"""Item difficulty and picture difficulty (TPDB Difficulty Model Spec, starting weights).

b = b0 + type + 0.6*h - 0.8*A - 0.5*s - 0.3*r + 1.2*d - 0.3*f + domain + 0.12*L
P(produce | theta) = logistic(theta - b)

  s  z-score of ln(visible area / canvas area) against the item library reference
  r  independent cues - 1 (inference and contradiction items)
  d  cue-effect centroid distance / canvas diagonal (inference items)
  f  Zipf frequency of the item's key word - 4
  L  scored events in the scene (template instances)

The salience reference (mean and SD of ln area fraction) is fixed from the Garden prototype's
item library (house z = +1.90, single drip z = -3.22), so scores are comparable across scenes.
"""
import math

from wordfreq import zipf_frequency

WEIGHTS = {
    "b0": -1.0,
    "type": {"entity": 0.0, "action": 0.3, "inference": 0.6, "contradiction_notice": 0.8, "contradiction_explain": 1.4},
    "chain": 0.6, "animate": -0.8, "salience": -0.5, "redundancy": -0.3, "separation": 1.2, "frequency": -0.3,
    "domain": {None: 0.0, "physical": 0.0, "biological": -0.2, "functional": 0.2},
    "load": 0.12,
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


def zipf(word):
    if word not in _ZIPF:
        parts = word.split()
        _ZIPF[word] = min(zipf_frequency(p, "en") for p in parts) if parts else 4.0
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
