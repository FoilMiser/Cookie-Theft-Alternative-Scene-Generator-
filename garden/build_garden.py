"""
TPDB scene family 1: "Garden" — master SVG generator.

Every drawable element is an SVG <g> tagged with:
  data-tier-min / data-tier-max  tiers in which it is visible (1..4)
  data-role                      background | setting | filler | scored
  data-concepts                  main-concept / inference ids it carries
Rendering tier N = keep elements with tier_min <= N <= tier_max.
Checklists, region maps and visual-load counts are derived from the tags.
"""
import math, json, io, os, sys
import cairosvg
import numpy as np
from PIL import Image

W, H = 1600, 1000
OUT = "#26262e"
OW = 4.5

PAL = {
    "outline": OUT, "sky": "#a9dcf5", "grass": "#72c05a", "grass_dark": "#3d8a3a",
    "path": "#e8d9bd", "soil": "#7a4e2d", "wood": "#a8713e", "wood_light": "#d29a5c",
    "wall": "#f4ead6", "roof": "#b2473f", "white": "#ffffff", "cloud_dark": "#454d60",
    "water": "#1d6fc0", "hose": "#16677f", "sun": "#ffd23f",
    "red": "#d93f3f", "blue": "#3d63c2", "yellow": "#f2c230", "purple": "#8c55c4",
    "teal": "#22a39a", "orange": "#f08a2c", "pink": "#e8679b", "slate": "#55657d",
    "gray": "#9aa0a8", "charcoal": "#3b3b45", "tan": "#cf9150", "cream": "#f2deb6", "brown": "#6b4329",
    "skin1": "#f2cba8", "skin2": "#c98b5e", "skin3": "#8a5536", "hair_gray": "#c9c9cf",
    "street": "#8f939c", "grass_far": "#9bd384",
}
C = PAL


# ----------------------------------------------------------------- primitives
def P(x, y):
    return f"{x:.1f},{y:.1f}"


def stroke(d, color, w, ow=OW, extra=""):
    """Thick line with a dark outline (draw outline wider, then colour)."""
    return (f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w + 2 * ow:.1f}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w:.1f}" '
            f'stroke-linecap="round" stroke-linejoin="round" {extra}/>')


def poly_d(pts, close=False):
    return "M " + " L ".join(P(*p) for p in pts) + (" Z" if close else "")


def shape(d, fill, ow=OW):
    return (f'<path d="{d}" fill="{fill}" stroke="{OUT}" stroke-width="{ow:.1f}" '
            f'stroke-linejoin="round" stroke-linecap="round"/>')


def poly(pts, fill, ow=OW):
    return shape(poly_d(pts, True), fill, ow)


def circ(cx, cy, r, fill, ow=OW):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{OUT}" stroke-width="{ow:.1f}"/>'


def ell(cx, cy, rx, ry, fill, ow=OW, rot=0):
    t = f' transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})"' if rot else ""
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" '
            f'stroke="{OUT}" stroke-width="{ow:.1f}"{t}/>')


def rect(x, y, w, h, fill, rx=0, ow=OW):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" '
            f'fill="{fill}" stroke="{OUT}" stroke-width="{ow:.1f}" stroke-linejoin="round"/>')


def line(x1, y1, x2, y2, color=OUT, w=OW):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
            f'stroke-width="{w:.1f}" stroke-linecap="round"/>')


def flat(d, fill):
    return f'<path d="{d}" fill="{fill}" stroke="none"/>'


# ------------------------------------------------------------------ figure rig
def _dir(a, f):
    """Angle in degrees: 0 = straight down, +90 = forward (facing f)."""
    r = math.radians(a)
    return math.sin(r) * f, math.cos(r)


def _limb(root, a1, l1, a2, l2, f):
    d1 = _dir(a1, f)
    j = (root[0] + d1[0] * l1, root[1] + d1[1] * l1)
    d2 = _dir(a2, f)
    e = (j[0] + d2[0] * l2, j[1] + d2[1] * l2)
    return j, e


def ik(root, target, l1, l2, f, bend=1):
    """Two-bone IK returning absolute angles (a1, a2). Clamps if out of reach."""
    dx = (target[0] - root[0]) * f
    dy = target[1] - root[1]
    d = max(1e-6, min(math.hypot(dx, dy), l1 + l2 - 0.5))
    base = math.atan2(dx, dy)
    cosA = (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d)
    alpha = math.acos(max(-1, min(1, cosA)))
    a1 = base + bend * alpha
    jx, jy = math.sin(a1) * l1, math.cos(a1) * l1
    a2 = math.atan2(dx - jx, dy - jy) if math.hypot(dx, dy) <= l1 + l2 else base
    return math.degrees(a1), math.degrees(a2)


def person(cx, fy, h, f, skin, shirt, pants, hair, style="short",
           legs=((-4, -2), (4, 2)), arms=(("a", -8, -4), ("a", 8, 4)),
           lean=0, expr="neutral", gaze=(0, 0), brows=None, child=False,
           hip=None, hat=None, shoes=None, sleeves="short", head_tilt=0):
    """Return (svg, info). f = +1 faces right, -1 faces left."""
    s = []
    k = 1.0
    leg_len = (0.42 if child else 0.46) * h
    torso = (0.27 if child else 0.30) * h
    head_r = (0.125 if child else 0.09) * h
    ua, fa = (0.15 if child else 0.165) * h, (0.14 if child else 0.15) * h
    lw, aw = (0.09 if child else 0.08) * h, (0.065 if child else 0.055) * h
    sw, hw = (0.11 if child else 0.12) * h, (0.10 if child else 0.10) * h
    shoes = shoes or C["charcoal"]

    hipp = hip if hip else (cx, fy - leg_len)
    up = _dir(180 + lean, f)  # torso axis pointing up
    shoulder = (hipp[0] + up[0] * torso, hipp[1] + up[1] * torso)
    ux, uy = up
    nx, ny = -uy, ux
    arm_root = (shoulder[0] + up[0] * -0.03 * h, shoulder[1] + up[1] * -0.03 * h)
    hc = (shoulder[0] + up[0] * head_r * 1.08 + f * 0.01 * h, shoulder[1] + up[1] * head_r * 1.08)

    # legs
    leg_pts = []
    for i, (t, sh) in enumerate(legs):
        root = (hipp[0] + f * (-0.02 + 0.04 * i) * h, hipp[1])
        knee, foot = _limb(root, t, leg_len / 2, sh, leg_len / 2, f)
        leg_pts.append((root, knee, foot))

    # arms
    arm_pts = []
    for i, spec in enumerate(arms):
        root = (arm_root[0] + f * (-0.035 + 0.07 * i) * h, arm_root[1])
        if spec[0] == "a":
            a1, a2 = spec[1], spec[2]
        else:
            a1, a2 = ik(root, spec[1], ua, fa, f, spec[2] if len(spec) > 2 else 1)
        el, hand = _limb(root, a1, ua, a2, fa, f)
        arm_pts.append((root, el, hand))

    def draw_leg(lp):
        root, knee, foot = lp
        out = stroke(poly_d([root, knee, foot]), pants, lw)
        out += ell(foot[0] + f * 0.03 * h, foot[1] + 0.005 * h, 0.05 * h, 0.026 * h, shoes)
        return out

    def draw_arm(ap):
        root, el, hand = ap
        out = (f'<path d="{poly_d([root, el, hand])}" fill="none" stroke="{OUT}" '
               f'stroke-width="{aw + 2 * OW:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')
        out += (f'<path d="{poly_d([root, el])}" fill="none" stroke="{shirt}" stroke-width="{aw:.1f}" '
                f'stroke-linecap="round"/>')
        fore_col = shirt if sleeves == "long" else skin
        out += (f'<path d="{poly_d([el, hand])}" fill="none" stroke="{fore_col}" stroke-width="{aw * 0.92:.1f}" '
                f'stroke-linecap="round"/>')
        if sleeves != "long":
            # re-cover elbow with sleeve end
            mid = ((root[0] + el[0] * 2) / 3, (root[1] + el[1] * 2) / 3)
            out += (f'<path d="{poly_d([root, mid])}" fill="none" stroke="{shirt}" stroke-width="{aw:.1f}" '
                    f'stroke-linecap="round"/>')
        out += circ(hand[0], hand[1], aw * 0.62, skin, OW * 0.8)
        return out

    s.append(draw_arm(arm_pts[0]))
    s.append(draw_leg(leg_pts[0]))
    s.append(draw_leg(leg_pts[1]))
    # torso
    tp = [(shoulder[0] + nx * sw, shoulder[1] + ny * sw), (shoulder[0] - nx * sw, shoulder[1] - ny * sw),
          (hipp[0] - nx * hw, hipp[1] - ny * hw), (hipp[0] + nx * hw, hipp[1] + ny * hw)]
    s.append(shape(poly_d(tp, True), shirt))
    band = [(hipp[0] + nx * hw, hipp[1] + ny * hw), (hipp[0] - nx * hw, hipp[1] - ny * hw),
            (hipp[0] - nx * hw + ux * 0.05 * h, hipp[1] - ny * hw + uy * 0.05 * h),
            (hipp[0] + nx * hw + ux * 0.05 * h, hipp[1] + ny * hw + uy * 0.05 * h)]
    s.append(shape(poly_d(band, True), pants))
    # head
    r = head_r
    x, y = hc
    hs = f'<g transform="rotate({head_tilt * f:.1f} {x:.1f} {y:.1f})">'
    if style == "long":
        hs += ell(x - f * 0.35 * r, y + 0.55 * r, 0.8 * r, 1.05 * r, hair)
    if style == "bun":
        hs += circ(x - f * 0.6 * r, y - 0.85 * r, 0.42 * r, hair)
    if style in ("short", "long", "bun", "curly"):
        if style == "curly":
            for dx_, dy_ in [(-0.6, -0.5), (-0.1, -0.85), (0.45, -0.7), (-0.85, 0.05), (0.75, -0.25)]:
                hs += circ(x + f * dx_ * r, y + dy_ * r, 0.42 * r, hair, OW * 0.8)
        else:
            hs += circ(x - f * 0.12 * r, y - 0.14 * r, 1.04 * r, hair)
    hs += circ(x, y, r, skin)
    if style != "long" and hat is None:
        hs += circ(x - f * 0.18 * r, y + 0.08 * r, 0.2 * r, skin, OW * 0.8)  # ear
    if hat:
        hs += shape(f"M {P(x - 1.02 * r, y - 0.18 * r)} A {r:.1f} {r:.1f} 0 0 1 {P(x + 1.02 * r, y - 0.18 * r)} Z", hat)
        hs += ell(x + f * 0.75 * r, y - 0.2 * r, 0.62 * r, 0.14 * r, hat, OW * 0.8)
    gx, gy = gaze
    ex1, ex2 = x + f * 0.18 * r + gx * 0.1 * r, x + f * 0.6 * r + gx * 0.1 * r
    ey = y - 0.05 * r + gy * 0.14 * r
    eyes = ""
    if expr == "sleep":
        for ex in (ex1, ex2):
            eyes += f'<path d="M {P(ex - 0.12 * r, ey)} Q {P(ex, ey + 0.1 * r)} {P(ex + 0.12 * r, ey)}" fill="none" stroke="{OUT}" stroke-width="{OW * 0.8:.1f}" stroke-linecap="round"/>'
    else:
        eyes += circ(ex1, ey, 0.1 * r, OUT, 0) + circ(ex2, ey, 0.1 * r, OUT, 0)
    hs += eyes
    if brows == "puzzled":
        hs += line(ex1 - 0.13 * r * f, ey - 0.28 * r, ex1 + 0.13 * r * f, ey - 0.22 * r, OUT, OW * 0.8)
        hs += line(ex2 - 0.13 * r * f, ey - 0.42 * r, ex2 + 0.13 * r * f, ey - 0.5 * r, OUT, OW * 0.8)
    if brows == "focus":
        hs += line(ex1 - 0.13 * r * f, ey - 0.3 * r, ex1 + 0.15 * r * f, ey - 0.22 * r, OUT, OW * 0.8)
        hs += line(ex2 - 0.13 * r * f, ey - 0.24 * r, ex2 + 0.15 * r * f, ey - 0.3 * r, OUT, OW * 0.8)
    mx, my = x + f * 0.42 * r, y + 0.45 * r
    if expr in ("smile",):
        hs += f'<path d="M {P(mx - 0.22 * r, my - 0.04 * r)} Q {P(mx, my + 0.2 * r)} {P(mx + 0.22 * r, my - 0.04 * r)}" fill="none" stroke="{OUT}" stroke-width="{OW * 0.8:.1f}" stroke-linecap="round"/>'
    elif expr == "frown":
        hs += f'<path d="M {P(mx - 0.2 * r, my + 0.08 * r)} Q {P(mx, my - 0.12 * r)} {P(mx + 0.2 * r, my + 0.08 * r)}" fill="none" stroke="{OUT}" stroke-width="{OW * 0.8:.1f}" stroke-linecap="round"/>'
    elif expr == "open":
        hs += ell(mx, my + 0.02 * r, 0.12 * r, 0.15 * r, OUT, 0)
    elif expr in ("neutral", "sleep"):
        hs += line(mx - 0.15 * r, my, mx + 0.15 * r, my, OUT, OW * 0.8)
    hs += "</g>"
    s.append(hs)
    s.append(draw_arm(arm_pts[1]))
    info = {"head": hc, "head_r": r, "hands": [a[2] for a in arm_pts], "feet": [l[2] for l in leg_pts],
            "hip": hipp, "shoulder": shoulder}
    return "".join(s), info


# --------------------------------------------------------------- scene objects
def dog(cx, ground, f, pose="stand", col=None):
    col = col or C["cream"]
    dark = C["brown"]
    s = []
    if pose == "stand":
        by = ground - 58
        # far legs
        for lx in (cx + f * 30, cx - f * 32):
            s.append(stroke(poly_d([(lx - 6 * f, by + 8), (lx - 6 * f, ground - 4)]), "#d9bf8f", 13))
        s.append(stroke(f"M {P(cx - f * 48, by - 6)} Q {P(cx - f * 70, by - 40)} {P(cx - f * 60, by - 52)}", col, 10))
        s.append(ell(cx, by, 58, 26, col))
        for lx in (cx + f * 38, cx - f * 26):
            s.append(stroke(poly_d([(lx, by + 10), (lx, ground - 4)]), col, 14))
            s.append(ell(lx + f * 5, ground - 3, 11, 6, col, OW * 0.8))
        hx, hy = cx + f * 62, by - 28
        s.append(circ(hx, hy, 25, col))
        s.append(ell(hx + f * 26, hy + 8, 17, 12, col))
        s.append(circ(hx + f * 40, hy + 4, 5.5, OUT, 0))
        s.append(ell(hx - f * 10, hy + 4, 9, 18, dark, OW * 0.8, rot=-15 * f))
        s.append(circ(hx + f * 9, hy - 6, 3.6, OUT, 0))
        s.append(f'<path d="M {P(hx + f * 22, hy + 16)} q {f * 8:.1f},5 {f * 16:.1f},0" fill="none" stroke="{OUT}" stroke-width="3"/>')
    else:  # lying, asleep
        by = ground - 22
        s.append(stroke(f"M {P(cx - f * 55, by + 6)} Q {P(cx - f * 85, by + 16)} {P(cx - f * 95, by + 12)}", col, 10))
        s.append(ell(cx, by, 62, 22, col))
        s.append(ell(cx + f * 52, ground - 6, 26, 7, col, OW * 0.8))
        hx, hy = cx + f * 66, by - 14
        s.append(circ(hx, hy, 23, col))
        s.append(ell(hx + f * 24, hy + 8, 16, 11, col))
        s.append(circ(hx + f * 37, hy + 5, 5, OUT, 0))
        s.append(ell(hx - f * 8, hy + 6, 9, 17, dark, OW * 0.8, rot=-30 * f))
        s.append(f'<path d="M {P(hx + f * 3, hy - 4)} q {f * 6:.1f},5 {f * 12:.1f},0" fill="none" stroke="{OUT}" stroke-width="3" stroke-linecap="round"/>')
    return "".join(s)


def flower(x, y, col, h=60, r=11):
    s = stroke(poly_d([(x, y), (x, y - h)]), "#3f8f3a", 5, OW * 0.6)
    s += ell(x + 9, y - h * 0.45, 9, 4.5, "#3f8f3a", OW * 0.6, rot=-30)
    for i in range(5):
        a = math.radians(72 * i - 90)
        s += circ(x + math.cos(a) * r, y - h + math.sin(a) * r, r * 0.75, col, OW * 0.7)
    s += circ(x, y - h, r * 0.55, C["yellow"] if col != C["yellow"] else C["orange"], OW * 0.7)
    return s


def puff(cx, cy, scale, fill):
    s = ""
    for dx, dy, r in [(-70, 15, 42), (-25, -15, 55), (35, -5, 50), (78, 18, 36), (5, 25, 45)]:
        s += circ(cx + dx * scale, cy + dy * scale, r * scale, fill)
    # erase inner outlines with a flat fill pass
    for dx, dy, r in [(-70, 15, 42), (-25, -15, 55), (35, -5, 50), (78, 18, 36), (5, 25, 45)]:
        s += f'<circle cx="{cx + dx * scale:.1f}" cy="{cy + dy * scale:.1f}" r="{r * scale - OW * 0.6:.1f}" fill="{fill}"/>'
    return s


def tree(cx):
    s = rect(cx - 16, 290, 32, 160, C["wood"], 6)
    for dx, dy, r in [(-62, 300, 62), (64, 296, 60), (0, 240, 92), (-40, 200, 55), (45, 205, 58)]:
        s += circ(cx + dx, dy, r, C["grass_dark"])
    for dx, dy, r in [(-62, 300, 62), (64, 296, 60), (0, 240, 92), (-40, 200, 55), (45, 205, 58)]:
        s += f'<circle cx="{cx + dx:.1f}" cy="{dy:.1f}" r="{r - OW * 0.6:.1f}" fill="{C["grass_dark"]}"/>'
    return s


def bush(cx, cy, scale=1.0):
    s = ""
    pts = [(-40, 5, 32), (0, -12, 40), (40, 4, 32)]
    for dx, dy, r in pts:
        s += circ(cx + dx * scale, cy + dy * scale, r * scale, C["grass_dark"])
    for dx, dy, r in pts:
        s += f'<circle cx="{cx + dx * scale:.1f}" cy="{cy + dy * scale:.1f}" r="{r * scale - OW * 0.6:.1f}" fill="{C["grass_dark"]}"/>'
    return s


def pot(x, y, plant_col):
    s = poly([(x - 24, y - 40), (x + 24, y - 40), (x + 17, y), (x - 17, y)], "#c0643a")
    s += rect(x - 28, y - 48, 56, 12, "#c0643a", 3)
    for dx in (-12, 0, 12):
        s += ell(x + dx, y - 64, 10, 18, plant_col, OW * 0.7, rot=dx * 2)
    return s


# ----------------------------------------------------------------- scene build
ELEMENTS = []
CONCEPTS = {}


def concept(cid, text, kind, tmin, tmax, sub=None):
    CONCEPTS[cid] = {"id": cid, "text": text, "kind": kind, "tier_min": tmin, "tier_max": tmax,
                     "inference_type": sub}


def el(eid, label, svg, z, tmin=1, tmax=4, role="setting", concepts=()):
    ELEMENTS.append({"id": eid, "label": label, "svg": svg, "z": z, "tier_min": tmin, "tier_max": tmax,
                     "role": role, "concepts": list(concepts)})


# ---- concepts (healthy-speaker targets; pilot data decides the final list)
concept("C01", "A man is in the garden holding a hose", "mc", 1, 4)
concept("C02", "There is a flower bed / flowers", "mc", 1, 4)
concept("C03", "It is a sunny day", "mc", 1, 4)
concept("C04", "It is the backyard of a house", "mc", 1, 4)
concept("C05", "Water is spraying onto the flowers", "mc", 1, 1)
concept("C06", "A dog is lying asleep on the grass", "mc", 1, 1)
concept("C07", "The dog is standing on the hose", "mc", 2, 4)
concept("C08", "No water is coming out of the hose", "mc", 2, 4)
concept("C09", "The man is looking at the nozzle, puzzled", "mc", 2, 4)
concept("C10", "A woman is hanging up laundry", "mc", 2, 4)
concept("C11", "Clothes are hanging on the clothesline", "mc", 2, 4)
concept("C12", "A child is on the swing", "mc", 2, 4)
concept("C13", "Dark clouds are coming", "mc", 3, 4)
concept("C14", "A cat is crouched on the fence", "mc", 3, 4)
concept("C15", "A bird is at the bird feeder", "mc", 3, 4)
concept("C16", "A neighbor is handing a ball over the fence", "mc", 3, 4)
concept("C17", "The child is reaching out to catch the ball", "mc", 3, 4)
concept("C18", "A delivery person is leaving through the gate", "mc", 4, 4)
concept("C19", "A package was left on the path", "mc", 4, 4)
concept("C20", "A sprinkler is running", "mc", 4, 4)
concept("C21", "A child is building / patting a snowman", "mc", 4, 4)
concept("C22", "There is a snowman", "mc", 4, 4)
concept("I01", "The dog is blocking the water by standing on the hose", "inf", 2, 4, "cause")
concept("I02", "It is going to rain and the laundry will get wet", "inf", 3, 4, "prediction")
concept("I03", "The cat is about to pounce on the bird", "inf", 3, 4, "intent (gaze/pose)")
concept("I05", "The sprinkler is soaking the package", "inf", 4, 4, "prediction")
concept("I06", "A snowman cannot be there on a hot sunny day", "inf", 4, 4, "contradiction")

GROUND = 600

# ---- background / setting
el("sky", "Sky", rect(-10, -10, W + 20, GROUND + 20, C["sky"], 0, 0), 0, role="background")
el("ground", "Lawn", rect(-10, GROUND, W + 20, H - GROUND + 10, C["grass"], 0, 0), 1, role="background")

sun = ""
for i in range(12):
    a = math.radians(30 * i)
    sun += line(1450 + math.cos(a) * 70, 120 + math.sin(a) * 70, 1450 + math.cos(a) * 95,
                120 + math.sin(a) * 95, C["orange"], 7)
sun += circ(1450, 120, 56, C["sun"])
el("sun", "Sun", sun, 2, concepts=["C03"], role="scored")

el("clouds_white", "Small white clouds (slot for storm clouds)",
   puff(640, 120, 0.7, C["white"]) + puff(900, 160, 0.55, C["white"]), 3, 1, 2, role="filler")
el("clouds_dark", "Dark storm clouds rolling in",
   puff(600, 115, 1.05, C["cloud_dark"]) + puff(850, 90, 1.0, C["cloud_dark"]) + puff(1035, 150, 0.75, C["cloud_dark"]),
   3, 3, 4, role="scored", concepts=["C13", "I02"])

el("tree", "Tree behind fence", tree(420), 4, role="filler")

# bird feeder on a pole behind fence
feeder = stroke(poly_d([(1245, 440), (1245, 352)]), C["wood"], 8)
feeder += rect(1218, 330, 54, 26, C["wood_light"], 3)
feeder += poly([(1210, 332), (1245, 305), (1280, 332)], C["roof"])
feeder += line(1222, 360, 1268, 360, OUT, 4)
el("feeder", "Bird feeder on a pole", feeder, 5, role="filler")

# neighbor behind fence handing a ball (T3+)
nb_svg, nb = person(1395, 600, 300, -1, C["skin1"], C["orange"], C["slate"], C["hair_gray"], "short",
                    arms=(("t", (1418, 470), -1), ("t", (1318, 392), 1)), expr="smile", gaze=(0, -0.2))
ball_x, ball_y = nb["hands"][1][0] - 18, nb["hands"][1][1] - 12
ball = circ(ball_x, ball_y, 21, C["red"]) + f'<path d="M {P(ball_x - 21, ball_y)} Q {P(ball_x, ball_y + 12)} {P(ball_x + 21, ball_y)}" fill="none" stroke="{C["white"]}" stroke-width="5"/>'
ball += circ(nb["hands"][1][0], nb["hands"][1][1], 8.5, C["skin1"], OW * 0.8)
el("neighbor", "Neighbor over the fence holding out a ball", nb_svg + ball, 6, 3, 4, role="scored", concepts=["C16"])

# fence
fence = ""
x = 310
while x < W + 10:
    if not (1440 <= x < 1560):
        fence += poly([(x, 440), (x + 22, 428), (x + 44, 440), (x + 44, 615), (x, 615)], C["wood_light"], OW * 0.8)
    x += 46
fence += poly([(1562, 440), (1584, 428), (1606, 440), (1606, 615), (1562, 615)], C["wood_light"], OW * 0.8)
fence += rect(300, 480, 1140, 16, C["wood"], 2, OW * 0.8) + rect(300, 565, 1140, 16, C["wood"], 2, OW * 0.8)
fence += rect(1560, 480, 60, 16, C["wood"], 2, OW * 0.8) + rect(1560, 565, 60, 16, C["wood"], 2, OW * 0.8)
el("fence", "Wooden fence", fence, 7, role="setting", concepts=["C04"])

gate_closed = rect(1442, 432, 116, 183, C["wood"], 4) + line(1442, 432, 1558, 615, OUT, 4) + circ(1540, 525, 7, C["charcoal"])
el("gate_closed", "Closed gate", gate_closed, 8, 1, 3, role="filler")
gate_open = rect(1442, 432, 116, 183, C["street"], 0, OW * 0.8)
gate_open += rect(1442, 432, 116, 120, C["sky"], 0, 0) + rect(1442, 552, 116, 63, C["grass_far"], 0, 0)
gate_open += poly([(1442, 425), (1478, 445), (1478, 640), (1442, 615)], C["wood"])
el("gate_open", "Gate standing open", gate_open, 8, 4, 4, role="scored", concepts=["C18"])

# cat crouched on fence top, eyes on the bird (T3+)
cat = stroke(f"M {P(1080, 415)} Q {P(1046, 400)} {P(1050, 352)}", C["charcoal"], 10)
cat += ell(1110, 414, 38, 17, C["charcoal"])
cat += ell(1135, 430, 12, 6, C["charcoal"], OW * 0.8) + ell(1095, 430, 12, 6, C["charcoal"], OW * 0.8)
cat += poly([(1140, 384), (1146, 360), (1158, 380)], C["charcoal"]) + poly([(1160, 384), (1172, 362), (1176, 388)], C["charcoal"])
cat += circ(1158, 398, 19, C["charcoal"])
cat += ell(1166, 406, 8, 6, C["white"], 0)
cat += circ(1160, 393, 4.5, C["yellow"], 0) + circ(1172, 391, 4.5, C["yellow"], 0)
cat += circ(1161, 392, 2, OUT, 0) + circ(1173, 390, 2, OUT, 0)
el("cat", "Cat crouched on fence, staring at the bird", cat, 9, 3, 4, role="scored", concepts=["C14", "I03"])

bird = ell(1255, 342, 15, 11, C["red"]) + circ(1243, 333, 9, C["red"])
bird += poly([(1234, 332), (1224, 336), (1234, 338)], C["yellow"], OW * 0.6)
bird += ell(1262, 340, 9, 5, "#a52c2c", OW * 0.6, rot=-15) + circ(1241, 330, 2, OUT, 0)
bird += line(1256, 352, 1256, 360, OUT, 3)
el("bird", "Bird eating at the feeder", '<g transform="translate(1250,342) scale(1.35) translate(-1250,-342)">' + bird + "</g>", 9, 3, 4, role="scored", concepts=["C15", "I03"])

# house at left
house = rect(-10, 230, 320, 545, C["wall"], 0)
house += poly([(-20, 238), (340, 238), (250, 120), (-20, 120)], C["roof"])
house += rect(40, 320, 100, 110, C["sky"], 4) + line(90, 320, 90, 430) + line(40, 375, 140, 375)
house += rect(175, 560, 90, 215, C["blue"], 4) + circ(250, 670, 6, C["yellow"])
house += rect(160, 765, 120, 16, C["gray"], 2)
el("house", "Back of the house", house, 10, role="scored", concepts=["C04"])

path = flat(poly_d([(1448, 615), (1556, 615), (1560, 1010), (1250, 1010)], True), C["path"])
path += f'<path d="M 1448 615 L 1250 1010 M 1556 615 L 1560 1010" fill="none" stroke="{OUT}" stroke-width="{OW * 0.8}"/>'
for (sx, sy, rx) in [(1500, 660, 26), (1470, 740, 32), (1440, 830, 38), (1405, 935, 44)]:
    path += ell(sx, sy, rx, rx * 0.35, "#c7b08a", OW * 0.6)
el("path", "Stone path to the gate", path, 11, role="setting")

el("bush_left", "Bush", bush(360, 615, 0.9), 12, role="filler")
el("bush_mid", "Bush", bush(1010, 612, 0.85), 12, role="filler")

# clothesline posts + line
cl = rect(624, 390, 13, 315, C["wood"], 3) + rect(944, 390, 13, 315, C["wood"], 3)
cl += rect(608, 384, 45, 11, C["wood"], 3) + rect(928, 384, 45, 11, C["wood"], 3)
cl += f'<path d="M 630 396 Q 790 440 950 396" fill="none" stroke="{OUT}" stroke-width="3.5"/>'
el("clothesline", "Clothesline", cl, 13, role="filler")


def line_y(x):  # quadratic sag of the clothesline
    t = (x - 630) / 320
    return (1 - t) ** 2 * 396 + 2 * (1 - t) * t * 440 + t * t * 396


laundry = ""
# trousers
x0 = 652
laundry += poly([(x0, line_y(x0)), (x0 + 58, line_y(x0 + 58)), (x0 + 60, line_y(x0) + 120), (x0 + 36, line_y(x0) + 120),
                 (x0 + 29, line_y(x0) + 40), (x0 + 22, line_y(x0) + 120), (x0 - 2, line_y(x0) + 120)], C["blue"])
# striped towel
x0 = 724
laundry += rect(x0, line_y(x0 + 25) - 2, 52, 92, C["yellow"], 3)
for k_ in range(3):
    laundry += line(x0 + 4, line_y(x0 + 25) + 20 + k_ * 24, x0 + 48, line_y(x0 + 25) + 20 + k_ * 24, C["red"], 6)
# socks
for x0 in (900, 922):
    yy = line_y(x0)
    laundry += poly([(x0, yy), (x0 + 15, yy), (x0 + 15, yy + 40), (x0 + 26, yy + 52), (x0 + 18, yy + 60), (x0, yy + 46)], C["pink"], OW * 0.8)
for px in (656, 704, 728, 772, 905, 927):
    laundry += rect(px - 3, line_y(px) - 9, 7, 16, C["wood_light"], 1, OW * 0.6)
el("laundry", "Clothes hanging on the line", laundry, 14, 2, 4, role="scored", concepts=["C11", "I02"])

# swing frame + ropes + seat
sw = stroke(poly_d([(1098, 845), (1140, 468)]), C["slate"], 12) + stroke(poly_d([(1176, 845), (1140, 468)]), C["slate"], 12)
sw += stroke(poly_d([(1292, 845), (1330, 468)]), C["slate"], 12) + stroke(poly_d([(1368, 845), (1330, 468)]), C["slate"], 12)
sw += stroke(poly_d([(1130, 470), (1340, 470)]), C["slate"], 13)
el("swing_frame", "Swing set", sw, 15, role="filler")

seat_y = 772
ropes = line(1205, 476, 1205, seat_y, OUT, 4) + line(1262, 476, 1262, seat_y, OUT, 4)
seat_empty = ropes + rect(1192, seat_y - 4, 84, 13, C["red"], 3)
el("swing_empty", "Empty swing seat", seat_empty, 16, 1, 1, role="filler")

# woman hanging laundry (T2+)
wm_svg, wm = person(770, 705, 300, 1, C["skin3"], C["purple"], C["teal"], C["charcoal"], "long",
                    arms=(("t", (842, 426), -1), ("t", (896, 420), 1)), gaze=(0.6, -1.0), expr="neutral", lean=-6)
shirt_held = '<g transform="translate(12,44)">' + poly([(812, 378), (874, 378), (888, 400), (874, 410), (870, 470), (818, 470), (816, 410), (800, 400)], C["white"])
shirt_held += rect(816, 370, 7, 14, C["wood_light"], 1, OW * 0.6) + rect(864, 372, 7, 14, C["wood_light"], 1, OW * 0.6) + "</g>"
basket = shape(f"M 840 662 L 940 662 L 930 708 L 850 708 Z", "#c99a5a")
basket += ell(890, 662, 52, 9, "#a87a3c", OW * 0.8) + ell(872, 654, 22, 9, C["teal"], OW * 0.7) + ell(905, 652, 20, 8, C["orange"], OW * 0.7)
el("woman", "Woman pinning a shirt to the line", shirt_held + wm_svg, 17, 2, 4, role="scored", concepts=["C10"])
el("basket", "Laundry basket", basket, 17, 2, 4, role="filler")

# child on swing — T2 holds ropes, T3+ reaches for the ball
def swing_child(reach):
    hip = (1234, seat_y - 6)
    if reach:
        arms = (("t", (1207, 740), -1), ("t", (1318, 668), -1))
        gaze, expr = (0.6, -1.2), "open"
    else:
        arms = (("t", (1207, 740), -1), ("t", (1262, 736), -1))
        gaze, expr = (0.3, 0), "smile"
    svg_, info_ = person(1234, 0, 205, 1, C["skin2"], C["yellow"], C["orange"], C["charcoal"], "curly",
                         legs=((84, 14), (80, 4)), arms=arms, child=True, hip=hip, gaze=gaze, expr=expr, lean=-14 if reach else 0)
    rope2 = line(1262, 476, 1262, seat_y, OUT, 4) if reach else ""
    return ropes + rect(1192, seat_y - 4, 84, 13, C["red"], 3) + svg_ + rope2


el("child_swing", "Child sitting on the swing", swing_child(False), 18, 2, 2, role="scored", concepts=["C12"])
el("child_swing_reach", "Child on the swing reaching out to catch the ball", swing_child(True), 18, 3, 4,
   role="scored", concepts=["C12", "C17"])

# delivery driver walking out through the gate (T4)
dv_svg, dv = person(1500, 668, 300, 1, C["skin2"], C["slate"], C["charcoal"], C["charcoal"], "short",
                    legs=((-24, -8), (20, 6)), arms=(("a", 24, 40), ("a", -26, -14)), hat=C["slate"],
                    expr="neutral", sleeves="short")
el("driver", "Delivery person walking out of the gate", dv_svg, 19, 4, 4, role="scored", concepts=["C18"])

# flower bed
fb = ell(445, 800, 125, 36, C["soil"])
cols = [C["red"], C["yellow"], C["purple"], C["pink"], C["red"], C["orange"], C["purple"], C["yellow"]]
for i, (fx, fy, fh) in enumerate([(345, 802, 58), (375, 790, 75), (410, 812, 62), (440, 788, 80),
                                  (470, 810, 60), (500, 792, 74), (530, 806, 58), (548, 795, 66)]):
    fb += flower(fx, fy, cols[i], fh)
el("flowers", "Flower bed", fb, 20, role="scored", concepts=["C02"])

reel = rect(282, 800, 40, 70, C["charcoal"], 4) + circ(302, 820, 28, C["hose"]) + circ(302, 820, 10, C["gray"])
el("hose_reel", "Hose reel", reel, 21, role="filler")

bench = rect(40, 858, 200, 18, C["wood_light"], 3) + rect(40, 820, 200, 16, C["wood_light"], 3)
bench += rect(55, 876, 14, 52, C["wood"], 2) + rect(212, 876, 14, 52, C["wood"], 2)
el("bench", "Garden bench", bench, 21, role="filler")

pots = pot(1350, 925, C["grass_dark"]) + pot(1410, 905, "#4fae4a")
el("pots", "Flower pots (slot for package)", pots, 21, 1, 3, role="filler")

wb = poly([(905, 900), (1010, 900), (995, 945), (920, 945)], C["gray"])
wb += circ(920, 958, 17, C["charcoal"]) + stroke(poly_d([(1005, 905), (1060, 925)]), C["wood"], 7)
el("wheelbarrow", "Wheelbarrow (slot for snowman)", wb, 21, 1, 3, role="filler")

can = poly([(1185, 905), (1235, 905), (1230, 960), (1190, 960)], C["teal"])
can += stroke(poly_d([(1188, 925), (1150, 900)]), C["teal"], 8) + stroke(f"M 1195 905 Q 1210 878 1228 905", C["teal"], 6)
el("watering_can", "Watering can (slot for sprinkler)", can, 21, 1, 3, role="filler")

bowl = ell(1100, 968, 30, 11, C["red"]) + ell(1100, 962, 24, 6, "#8a2a2a", OW * 0.6)
el("dog_bowl", "Dog bowl", bowl, 21, role="filler")

# snowman (T4) + child building it
sm = circ(985, 920, 52, C["white"]) + circ(985, 840, 38, C["white"]) + circ(985, 780, 28, C["white"])
sm += circ(976, 774, 4, OUT, 0) + circ(992, 774, 4, OUT, 0)
sm += poly([(990, 784), (1022, 790), (990, 792)], C["orange"], OW * 0.6)
sm += rect(958, 738, 54, 12, C["charcoal"], 2) + rect(966, 706, 38, 36, C["charcoal"], 3)
sm += stroke(poly_d([(1020, 840), (1058, 808), (1068, 798)]), C["brown"], 5, OW * 0.6)
sm += stroke(poly_d([(950, 840), (915, 818)]), C["brown"], 5, OW * 0.6)
sm += rect(955, 806, 60, 13, C["blue"], 5)
for yy in (835, 855):
    sm += circ(985, yy, 4.5, OUT, 0)
el("snowman", "Snowman on the lawn", sm, 22, 4, 4, role="scored", concepts=["C22", "I06"])

ch2_svg, ch2 = person(880, 0, 190, 1, C["skin1"], C["pink"], C["blue"], "#a8662e", "bun",
                      legs=((-2, -95), (70, 2)), arms=(("t", (935, 860), 1), ("t", (944, 900), 1)),
                      child=True, hip=(872, 925), lean=18, gaze=(0.5, 0.3), expr="smile")
el("child_snowman", "Child patting the snowman", ch2_svg, 23, 4, 4, role="scored", concepts=["C21", "I06"])

pkg = poly([(1318, 930), (1398, 930), (1398, 985), (1318, 985)], "#c8955a")
pkg += poly([(1318, 930), (1338, 912), (1418, 912), (1398, 930)], "#ddb07a")
pkg += poly([(1398, 930), (1418, 912), (1418, 967), (1398, 985)], "#a8743f")
pkg += line(1358, 930, 1358, 985, "#f3e3c3", 7) + rect(1330, 945, 20, 13, C["white"], 1, OW * 0.6)
el("package", "Package left on the path", pkg, 22, 4, 4, role="scored", concepts=["C19", "I05"])

spr = rect(1195, 945, 34, 18, C["gray"], 4) + stroke(poly_d([(1212, 945), (1212, 922)]), C["gray"], 7)
for i, (cx2, cy2) in enumerate([(1260, 840), (1310, 830), (1360, 850)]):
    spr += (f'<path d="M 1214 920 Q {cx2} {cy2 - 70} {cx2 + 70} {cy2 + 75}" fill="none" stroke="{C["water"]}" '
            f'stroke-width="5" stroke-dasharray="14 10" stroke-linecap="round"/>')
for dx, dy in [(1340, 905), (1372, 896), (1395, 904), (1356, 892)]:
    spr += ell(dx, dy, 4, 6, C["water"], OW * 0.4)
el("sprinkler", "Sprinkler spraying toward the package", spr, 24, 4, 4, role="scored", concepts=["C20", "I05"])

# man: T1 watering, T2+ peering into a dry nozzle
def man(dry):
    if dry:
        arms = (("a", -12, 10), ("t", (566, 618), -1))
        gaze, expr, brows, tilt = (-0.2, -0.2), "frown", "puzzled", 8
    else:
        arms = (("t", (606, 728), -1), ("t", (566, 694), -1))
        gaze, expr, brows, tilt = (0.4, 0.5), "smile", None, 0
    svg_, info_ = person(640, 880, 320, -1, C["skin1"], C["red"], C["charcoal"], "#7a4a28", "short",
                         arms=arms, gaze=gaze, expr=expr, brows=brows, head_tilt=tilt)
    hx, hy = info_["hands"][1]
    if dry:  # nozzle pointing back at his face
        noz = poly([(hx - 4, hy - 8), (hx + 26, hy - 18), (hx + 30, hy - 8), (hx, hy + 6)], C["charcoal"], OW * 0.8)
        tip = (hx + 30, hy - 13)
    else:
        noz = poly([(hx + 4, hy - 7), (hx - 30, hy - 1), (hx - 30, hy + 9), (hx + 4, hy + 9)], C["charcoal"], OW * 0.8)
        tip = (hx - 30, hy + 4)
    return svg_ + noz, info_, tip


man_wet_svg, man_wet, tip_wet = man(False)
man_dry_svg, man_dry, tip_dry = man(True)

S = (470, 962)  # where the dog stands on the hose


def hose(hand, pinched):
    a = f"M 302 848 C 300 930 380 968 {P(*S)}"
    b = f"M {P(*S)} C 560 958 640 960 690 905 C 730 860 {P(hand[0] + 60, hand[1] + 90)} {P(*hand)}"
    if pinched:
        out = stroke(a, C["hose"], 14) + stroke(b, C["hose"], 7)
    else:
        out = stroke(a, C["hose"], 10) + stroke(b, C["hose"], 10)
    return out


el("hose_t1", "Garden hose", hose(man_wet["hands"][1], False), 25, 1, 1, role="scored", concepts=["C01"])
el("hose_t2", "Garden hose, pinched under the dog's paw", hose(man_dry["hands"][1], True), 25, 2, 4,
   role="scored", concepts=["C01", "C07", "I01"])

el("dog_lying", "Dog asleep on the grass", dog(760, 962, 1, "lie"), 26, 1, 1, role="scored", concepts=["C06"])
el("dog_on_hose", "Dog standing on the hose", dog(S[0] + 46, S[1] + 3, -1, "stand"), 26, 2, 4,
   role="scored", concepts=["C07", "I01"])

el("man_watering", "Man watering the flowers", man_wet_svg, 27, 1, 1, role="scored", concepts=["C01"])
el("man_puzzled", "Man peering into the dry nozzle", man_dry_svg, 27, 2, 4, role="scored", concepts=["C01", "C09"])

spray = ""
tx, ty = tip_wet
for ex, ey, cy in [(420, 770, -60), (470, 760, -90), (515, 772, -40)]:
    spray += (f'<path d="M {P(tx, ty)} Q {P((tx + ex) / 2, ty + cy)} {P(ex, ey)}" fill="none" stroke="{C["water"]}" '
              f'stroke-width="6" stroke-dasharray="16 9" stroke-linecap="round"/>')
for dx, dy in [(430, 752), (455, 744), (490, 748), (505, 760), (440, 766)]:
    spray += ell(dx, dy, 4, 6, C["water"], OW * 0.4)
el("water_spray", "Water spraying onto the flowers", spray, 28, 1, 1, role="scored", concepts=["C05"])

tx, ty = tip_dry
drip = ell(tx + 6, ty + 26, 5, 8, C["water"], OW * 0.5)
el("dry_nozzle", "Single drip from the empty nozzle", drip, 28, 2, 4, role="scored", concepts=["C08", "I01"])


# ------------------------------------------------------------------- outputs
def svg_doc(elements, title):
    body = []
    for e in sorted(elements, key=lambda e: e["z"]):
        body.append(f'<g id="{e["id"]}" data-tier-min="{e["tier_min"]}" data-tier-max="{e["tier_max"]}" '
                    f'data-role="{e["role"]}" data-concepts="{" ".join(e["concepts"])}" data-label="{e["label"]}">'
                    f'{e["svg"]}</g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<title>{title}</title>' + "".join(body) + "</svg>")


def visible(t):
    return [e for e in ELEMENTS if e["tier_min"] <= t <= e["tier_max"]]


def render(svg, w=W):
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=w)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def to_gray(img):
    a = np.asarray(img.convert("RGB")).astype(float)
    L = 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]  # Rec.709 luma
    return Image.fromarray(np.clip(L, 0, 255).astype(np.uint8), "L")


def luma(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    master = svg_doc(ELEMENTS, "TPDB Garden — master (all tiers)")
    open(os.path.join(outdir, "garden_master.svg"), "w").write(master)

    # per-element masks at half resolution -> bbox, area, 3x3 cells
    MW, MH = W // 2, H // 2
    for e in ELEMENTS:
        if e["role"] == "background":
            e["bbox"] = [0, 0, W, H]
            continue
        im = render(svg_doc([e], e["id"]), MW)
        alpha = np.asarray(im)[..., 3] > 20
        ys, xs = np.nonzero(alpha)
        if len(xs) == 0:
            e["bbox"] = None
            continue
        x0, x1, y0, y1 = xs.min() * 2, xs.max() * 2, ys.min() * 2, ys.max() * 2
        e["bbox"] = [int(x0), int(y0), int(x1), int(y1)]
        e["area_frac"] = round(float(alpha.mean()), 4)
        e["width_frac"] = round((x1 - x0) / W, 3)
        cells = set()
        for cy in range(3):
            for cx in range(3):
                sub = alpha[cy * MH // 3:(cy + 1) * MH // 3, cx * MW // 3:(cx + 1) * MW // 3]
                if sub.mean() > 0.01:
                    cells.add(f"{'TMB'[cy]}{'LCR'[cx]}")
        if not cells:
            cx_, cy_ = xs.mean() / MW, ys.mean() / MH
            cells.add(f"{'TMB'[min(2, int(cy_ * 3))]}{'LCR'[min(2, int(cx_ * 3))]}")
        e["cells"] = sorted(cells)

    metrics = []
    for t in (1, 2, 3, 4):
        els = visible(t)
        svg = svg_doc(els, f"TPDB Garden — Tier {t}")
        open(os.path.join(outdir, f"garden_T{t}.svg"), "w").write(svg)
        col = render(svg)
        col.convert("RGB").save(os.path.join(outdir, f"garden_T{t}_color.png"), optimize=True)
        g = to_gray(col)
        g.save(os.path.join(outdir, f"garden_T{t}_gray.png"), optimize=True)
        ga = np.asarray(g).astype(float)
        gx = np.abs(np.diff(ga, axis=1))[:-1, :]
        gy = np.abs(np.diff(ga, axis=0))[:, :-1]
        edge = float(((gx + gy) > 40).mean())
        mcs = sorted(c for c, v in CONCEPTS.items() if v["kind"] == "mc" and v["tier_min"] <= t <= v["tier_max"])
        infs = sorted(c for c, v in CONCEPTS.items() if v["kind"] == "inf" and v["tier_min"] <= t <= v["tier_max"])
        objs = [e for e in els if e["role"] != "background"]
        scored_cells = set()
        for e in objs:
            if e["role"] == "scored":
                scored_cells.update(e.get("cells", []))
        buf = io.BytesIO()
        g.save(buf, "PNG", optimize=True)
        metrics.append({
            "tier": t, "main_concepts": len(mcs), "inferences": len(infs),
            "objects": len(objs), "scored_objects": sum(e["role"] == "scored" for e in objs),
            "filler_objects": sum(e["role"] == "filler" for e in objs),
            "edge_density": round(edge, 4), "gray_png_kb": round(len(buf.getvalue()) / 1024, 1),
            "scored_cells": len(scored_cells), "mc_ids": mcs, "inf_ids": infs,
        })

    # concept -> elements / regions
    for cid, c in CONCEPTS.items():
        carriers = [e for e in ELEMENTS if cid in e["concepts"]]
        c["elements"] = [e["id"] for e in carriers]
        c["cells"] = sorted(set(sum((e.get("cells", []) for e in carriers), [])))
        widths = [e.get("width_frac", 0) for e in carriers if e["role"] == "scored"]
        c["min_width_frac"] = min(widths) if widths else None

    # grayscale separation for adjacent colour pairs
    pairs = [("grass", "cream"), ("grass", "charcoal"), ("red", "charcoal"), ("sky", "wood_light"), ("sky", "cloud_dark"), ("sky", "white"), ("grass", "hose"),
             ("grass", "path"), ("grass", "grass_dark"), ("sky", "grass_dark"),
             ("sky", "charcoal"), ("wood_light", "charcoal"), ("grass", "white"), ("grass", "water"),
             ("soil", "water"), ("sky", "red"), ("purple", "teal"), ("slate", "charcoal"),
             ("yellow", "orange"), ("sky", "orange")]
    gray_pairs = [{"a": a, "b": b, "delta_L": round(abs(luma(C[a]) - luma(C[b])), 1)} for a, b in pairs]

    tags = {"family": "garden", "canvas": [W, H], "palette": PAL, "concepts": CONCEPTS,
            "elements": [{k: v for k, v in e.items() if k != "svg"} for e in ELEMENTS],
            "tiers": metrics, "gray_pairs": gray_pairs}
    json.dump(tags, open(os.path.join(outdir, "garden_tags.json"), "w"), indent=1)
    return tags


if __name__ == "__main__":
    tags = main(sys.argv[1] if len(sys.argv) > 1 else "out")
    for m in tags["tiers"]:
        print({k: v for k, v in m.items() if not k.endswith("_ids")})
    for gp in tags["gray_pairs"]:
        flag = "  <-- low" if gp["delta_L"] < 30 else ""
        print(f'{gp["a"]:>11} vs {gp["b"]:<11} dL={gp["delta_L"]}{flag}')
    for cid, c in tags["concepts"].items():
        print(cid, c["cells"], c["min_width_frac"])
