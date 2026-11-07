"""SVG drawing helpers for TPDB settings and scene props (flat color, dark outline).

Everything that stands on the ground is drawn at a ground point (x, y) and a size factor
s = ppm(y) / PPM_FRONT, so it shrinks with depth exactly like the rendered cast.
Sizes in these functions are pixels at the front of the scene.
"""
import math
import sys

W, H = 1600, 1000
PPM_FRONT, Y_FRONT, Y_ZERO = 190.0, 880.0, -402.0
OUT = "#26262e"
OW = 4.5

C = {
    "outline": OUT, "sky": "#a9dcf5", "sky_dull": "#b9c4cc", "grass": "#72c05a", "grass_dark": "#3d8a3a",
    "grass_far": "#9bd384", "hill": "#86c56c", "path": "#e8d9bd", "path_edge": "#c7b08a", "soil": "#7a4e2d",
    "wood": "#a8713e", "wood_light": "#d29a5c", "wall": "#f4ead6", "roof": "#b2473f", "white": "#ffffff",
    "cloud_dark": "#454d60", "water": "#1d6fc0", "water_light": "#6cb8e6", "pond": "#5aa9d8", "hose": "#16677f",
    "sun": "#ffd23f", "red": "#d93f3f", "blue": "#3d63c2", "yellow": "#f2c230", "purple": "#8c55c4",
    "teal": "#22a39a", "orange": "#f08a2c", "pink": "#e8679b", "slate": "#55657d", "gray": "#9aa0a8",
    "charcoal": "#3b3b45", "tan": "#cf9150", "cream": "#f2deb6", "brown": "#6b4329", "paving": "#d9d4cb",
    "paving_line": "#bdb6aa", "wall2": "#e9c9a6", "wall3": "#c9d9c4", "wall4": "#f0d0d0", "glass": "#bfe3f2",
    "green": "#4e9a52", "navy": "#34508a", "khaki": "#c8b27a", "paint": "#3d63c2", "lamp_glass": "#e9eef0",
    "leaf_green": "#8cc04c", "sand": "#ecd9a0", "sand_dark": "#d9bd78", "paper": "#f4f1ea", "skin1": "#f2cba8", "play": "#e9b77e", "leaf_brown": "#a8743e", "hole": "#4a2f1b", "rock": "#a7abb0", "rock_dark": "#80858c",
}


def ppm(y):
    return PPM_FRONT * (y - Y_ZERO) / (Y_FRONT - Y_ZERO)


def sz(y):
    """Size factor at ground depth y (1.0 at the front row, y = 880)."""
    return ppm(y) / PPM_FRONT


# ----------------------------------------------------------------- primitives
def P(x, y):
    return f"{x:.1f},{y:.1f}"


def stroke(d, color, w, ow=OW, extra=""):
    return (f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w + 2 * ow:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w:.1f}" stroke-linecap="round" stroke-linejoin="round" {extra}/>')


def poly_d(pts, close=False):
    return "M " + " L ".join(P(*p) for p in pts) + (" Z" if close else "")


def shape(d, fill, ow=OW):
    return f'<path d="{d}" fill="{fill}" stroke="{OUT}" stroke-width="{ow:.1f}" stroke-linejoin="round" stroke-linecap="round"/>'


def poly(pts, fill, ow=OW):
    return shape(poly_d(pts, True), fill, ow)


def circ(cx, cy, r, fill, ow=OW):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{OUT}" stroke-width="{ow:.1f}"/>'


def ell(cx, cy, rx, ry, fill, ow=OW, rot=0):
    t = f' transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})"' if rot else ""
    return f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" stroke="{OUT}" stroke-width="{ow:.1f}"{t}/>'


def rect(x, y, w, h, fill, rx=0, ow=OW):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx:.1f}" fill="{fill}" stroke="{OUT}" stroke-width="{ow:.1f}" stroke-linejoin="round"/>'


def line(x1, y1, x2, y2, color=OUT, w=OW):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{w:.1f}" stroke-linecap="round"/>'


def flat(d, fill, opacity=None):
    o = f' fill-opacity="{opacity}"' if opacity is not None else ""
    return f'<path d="{d}" fill="{fill}" stroke="none"{o}/>'


def shadow(x, y, w, s=1.0):
    # revision 26: flatter, as the figures' are now (a bicycle's reached well below its wheels)
    ry = w / (11 if getattr(sys.modules.get("scenegen.scene"), "PLACEMENT_REV", 26) >= 26 else 7)
    return f'<ellipse cx="{x:.1f}" cy="{y + 2:.1f}" rx="{w / 2:.1f}" ry="{ry:.1f}" fill="{OUT}" fill-opacity="0.16"/>'


def blob(parts, fill, ow=OW):
    """Union of circles with a single outline (outline pass, then a flat fill pass)."""
    s = "".join(circ(x, y, r, fill, ow) for x, y, r in parts)
    s += "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{max(0.5, r - ow * 0.6):.1f}" fill="{fill}"/>' for x, y, r in parts)
    return s


# ----------------------------------------------------------------- sky
def sun(cx, cy, r=56):
    s = ""
    for i in range(12):
        a = math.radians(30 * i)
        s += line(cx + math.cos(a) * (r + 14), cy + math.sin(a) * (r + 14), cx + math.cos(a) * (r + 39), cy + math.sin(a) * (r + 39), C["orange"], 7)
    return s + circ(cx, cy, r, C["sun"])


def puff(cx, cy, scale, fill):
    parts = [(cx + dx * scale, cy + dy * scale, r * scale) for dx, dy, r in [(-70, 15, 42), (-25, -15, 55), (35, -5, 50), (78, 18, 36), (5, 25, 45)]]
    return blob(parts, fill)


# ----------------------------------------------------------------- plants
def tree(x, base_y, s=1.0, trunk_h=170, canopy=None, col=None, extra_parts=()):
    """Round deciduous tree. Returns (svg, info) with canopy center/radius and branch slots.
    extra_parts: more (x, y, r) lobes merged into the crown's single outline."""
    col = col or C["grass_dark"]
    th = trunk_h * s
    tw = 34 * s
    cy = base_y - th - 40 * s
    R = 100 * s if canopy is None else canopy * s
    svg = rect(x - tw / 2, base_y - th - 30 * s, tw, th + 30 * s, C["wood"], 6 * s)
    parts = [(x - 0.66 * R, cy + 0.55 * R, 0.66 * R), (x + 0.68 * R, cy + 0.52 * R, 0.64 * R), (x, cy, R),
             (x - 0.44 * R, cy - 0.45 * R, 0.6 * R), (x + 0.48 * R, cy - 0.42 * R, 0.62 * R)]
    svg += blob(parts + list(extra_parts), col)
    slots = [(x - 0.45 * R, cy + 0.10 * R), (x + 0.50 * R, cy + 0.05 * R), (x - 0.05 * R, cy - 0.35 * R),
             (x + 0.10 * R, cy + 0.45 * R), (x - 0.60 * R, cy + 0.55 * R), (x + 0.70 * R, cy + 0.55 * R)]
    branch = [(x - 0.95 * R, cy + 0.95 * R), (x + 0.95 * R, cy + 0.92 * R)]
    return svg, {"canopy": (x, cy, R), "slots": slots, "branch_tips": branch, "bbox": (x - 1.35 * R, cy - 1.05 * R, x + 1.35 * R, base_y),
                 "parts": parts + list(extra_parts), "col": col, "trunk_w": tw}


def tree_with_branch(x, base_y, s=1.0, side=1, trunk_h=300, canopy=118, smooth=False):
    """Taller tree with one limb reaching out under the canopy (for things sitting on a branch).

    The limb starts high on the trunk and rises toward a leafy tuft, so it never reads as a bare
    plank, and it sits above a standing adult's head."""
    R0 = canopy * s
    cy0 = base_y - trunk_h * s - 40 * s
    bx0, by0 = x + side * 8 * s, base_y - trunk_h * 0.80 * s
    bx1, by1 = x + side * (R0 * (1.02 if smooth else 1.32)), cy0 + R0 * 0.62
    tuft = [(bx1 + side * 6 * s, by1 - 10 * s, 26 * s), (bx1 + side * 30 * s, by1 - 2 * s, 20 * s), (bx1 - side * 12 * s, by1 - 22 * s, 18 * s),
            # v0.7: lobes bridging the tuft to the crown, so the leafy end of the limb is one outline with
            # the crown (a separate tuft read as a green blob stuck to the tree)
            (x + side * R0 * 0.98, cy0 + R0 * 0.50, 30 * s), (x + side * R0 * 1.16, cy0 + R0 * 0.52, 24 * s)]
    if smooth:
        # v0.8: no leafy end at all: the limb runs up under the crown and out of sight (the round tuft at
        # its end still read as "a lump" or "a small bush sticking out of the canopy")
        tuft = []
    svg, info = tree(x, base_y, s, trunk_h=trunk_h, canopy=canopy, extra_parts=tuft)
    cx, cy, R = info["canopy"]
    limb = stroke(f"M {P(bx0, by0)} Q {P(bx0 + side * R * 0.55, by0 - 6 * s)} {P(bx1, by1)}", C["wood"], 13 * s)
    svg = limb + svg
    t = 0.55
    mx = (1 - t) ** 2 * bx0 + 2 * (1 - t) * t * (bx0 + side * R * 0.55) + t * t * bx1
    my = (1 - t) ** 2 * by0 + 2 * (1 - t) * t * (by0 - 6 * s) + t * t * by1
    info["branch"] = (mx, my - 7 * s)
    info["branch_line"] = ((bx0, by0), (bx1, by1))
    info["bbox"] = (min(info["bbox"][0], bx1 - 40 * s), info["bbox"][1], max(info["bbox"][2], bx1 + 54 * s), info["bbox"][3])
    return svg, info


def bush(cx, cy, scale=1.0):
    return blob([(cx + dx * scale, cy + dy * scale, r * scale) for dx, dy, r in [(-40, 5, 32), (0, -12, 40), (40, 4, 32)]], C["grass_dark"])


def flower(x, y, col, h=60, r=11):
    s = stroke(poly_d([(x, y), (x, y - h)]), "#3f8f3a", 5 * r / 11, OW * 0.6)
    s += ell(x + 9 * r / 11, y - h * 0.45, 9 * r / 11, 4.5 * r / 11, "#3f8f3a", OW * 0.6, rot=-30)
    for i in range(5):
        a = math.radians(72 * i - 90)
        s += circ(x + math.cos(a) * r, y - h + math.sin(a) * r, r * 0.75, col, OW * 0.7)
    s += circ(x, y - h, r * 0.55, C["yellow"] if col != C["yellow"] else C["orange"], OW * 0.7)
    return s


def flowerbed(cx, cy, s=1.0, n=8, rx=125):
    svg = ell(cx, cy, rx * s, 36 * s, C["soil"])
    cols = [C["red"], C["yellow"], C["purple"], C["pink"], C["red"], C["orange"], C["purple"], C["yellow"]]
    for i in range(n):
        t = (i + 0.5) / n
        fx = cx - rx * s * 0.82 + t * rx * s * 1.64
        fy = cy + (8 if i % 2 == 0 else -8) * s
        svg += flower(fx, fy, cols[i % len(cols)], (60 + 18 * ((i * 37) % 3) / 2) * s, 11 * s)
    return svg, (cx - rx * s, cy - 100 * s, cx + rx * s, cy + 36 * s)


def pot(x, y, plant_col, s=1.0):
    svg = poly([(x - 24 * s, y - 40 * s), (x + 24 * s, y - 40 * s), (x + 17 * s, y), (x - 17 * s, y)], "#c0643a")
    svg += rect(x - 28 * s, y - 48 * s, 56 * s, 12 * s, "#c0643a", 3 * s)
    for dx in (-12, 0, 12):
        svg += ell(x + dx * s, y - 64 * s, 10 * s, 18 * s, plant_col, OW * 0.7, rot=dx * 2)
    return svg


def planter(x, y, s=1.0):
    svg = rect(x - 60 * s, y - 46 * s, 120 * s, 46 * s, C["slate"], 4 * s)
    for i, col in enumerate((C["red"], C["yellow"], C["pink"], C["orange"])):
        svg += flower(x - 42 * s + i * 28 * s, y - 40 * s, col, 34 * s, 8 * s)
    return svg


# ----------------------------------------------------------------- furniture & things
def bench(x, base_y, s=1.0, w=200, back=True):
    """Park bench seen from the front. Seat top at base_y - 64 s."""
    w *= s
    seat_y = base_y - 64 * s
    svg = ""
    if back:
        # two slim back slats on posts, set back from the seat (a back as deep as the seat read as a table top)
        svg += rect(x - w / 2 + 14 * s, seat_y - 50 * s, 9 * s, 52 * s, C["wood"], 2 * s) + rect(x + w / 2 - 23 * s, seat_y - 50 * s, 9 * s, 52 * s, C["wood"], 2 * s)
        svg += rect(x - w / 2 + 4 * s, seat_y - 48 * s, w - 8 * s, 9 * s, C["wood_light"], 3 * s)
        svg += rect(x - w / 2 + 4 * s, seat_y - 30 * s, w - 8 * s, 9 * s, C["wood_light"], 3 * s)
    svg += rect(x - w / 2 + 14 * s, seat_y + 10 * s, 14 * s, base_y - seat_y - 10 * s, C["wood"], 2 * s)
    svg += rect(x + w / 2 - 28 * s, seat_y + 10 * s, 14 * s, base_y - seat_y - 10 * s, C["wood"], 2 * s)
    svg += poly([(x - w / 2 + 6 * s, seat_y - 6 * s), (x + w / 2 - 6 * s, seat_y - 6 * s), (x + w / 2, seat_y + 2 * s), (x - w / 2, seat_y + 2 * s)], C["wood"], OW * 0.8)
    svg += rect(x - w / 2, seat_y, w, 14 * s, C["wood_light"], 3 * s)
    return svg, {"seat_y": seat_y + 4 * s, "x0": x - w / 2 + 20 * s, "x1": x + w / 2 - 20 * s, "bbox": (x - w / 2, seat_y - 52 * s, x + w / 2, base_y)}


def lamp(x, base_y, s=1.0, h=300):
    top = base_y - h * s
    svg = rect(x - 7 * s, top + 30 * s, 14 * s, h * s - 30 * s, C["charcoal"], 3 * s)
    svg += rect(x - 16 * s, base_y - 14 * s, 32 * s, 14 * s, C["charcoal"], 3 * s)
    # the lamp is off (pale glass): a lit lamp in daylight reads as an oddity
    svg += poly([(x - 26 * s, top + 34 * s), (x + 26 * s, top + 34 * s), (x + 14 * s, top), (x - 14 * s, top)], C["lamp_glass"])
    svg += rect(x - 30 * s, top + 30 * s, 60 * s, 9 * s, C["charcoal"], 2 * s)
    svg += poly([(x - 18 * s, top + 2 * s), (x + 18 * s, top + 2 * s), (x, top - 16 * s)], C["charcoal"])
    return svg, {"top": (x, top - 16 * s), "bbox": (x - 30 * s, top - 16 * s, x + 30 * s, base_y)}


def bin_(x, y, s=1.0, col=None):
    col = col or C["green"]
    svg = poly([(x - 26 * s, y - 70 * s), (x + 26 * s, y - 70 * s), (x + 22 * s, y), (x - 22 * s, y)], col)
    svg += rect(x - 30 * s, y - 80 * s, 60 * s, 12 * s, col, 3 * s)
    for dx in (-10, 0, 10):
        svg += line(x + dx * s, y - 60 * s, x + dx * s, y - 10 * s, OUT, 2.5)
    return svg


def blanket(cx, cy, s=1.0):
    w, h = 230 * s, 70 * s
    pts = [(cx - w / 2, cy), (cx + w / 2 - 30 * s, cy - h), (cx + w / 2 + 40 * s, cy - h * 0.4), (cx - w / 2 + 70 * s, cy + h * 0.6)]
    svg = poly(pts, C["red"])
    for t in (0.25, 0.5, 0.75):
        a = (pts[0][0] + (pts[1][0] - pts[0][0]) * t, pts[0][1] + (pts[1][1] - pts[0][1]) * t)
        b = (pts[3][0] + (pts[2][0] - pts[3][0]) * t, pts[3][1] + (pts[2][1] - pts[3][1]) * t)
        svg += line(a[0], a[1], b[0], b[1], C["white"], 6 * s)
        a = (pts[0][0] + (pts[3][0] - pts[0][0]) * t, pts[0][1] + (pts[3][1] - pts[0][1]) * t)
        b = (pts[1][0] + (pts[2][0] - pts[1][0]) * t, pts[1][1] + (pts[2][1] - pts[1][1]) * t)
        svg += line(a[0], a[1], b[0], b[1], C["white"], 6 * s)
    svg += shape(poly_d(pts, True), "none")
    return svg, (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))


# v0.22: the barrow's square wheel without anything round inside it (an open square with eight spokes round a round hub read
# twice as "a square dark frame with a spoked wheel inside it"). Three were read on the bench: "A", a solid square wheel, a
# grey plate inside a thick dark tyre, a square hub and four bolts ("a separate metal box or plate" in both readings); "B",
# the open square tyre with a cross of two bars to the middles of its sides ("a small square window frame or grate"); and
# "C", the open square with eight straight spokes from a square hub to its corners and the middles of its sides, which led
# both readings as a wheel ("a dark wheel with a small square hub ... drawn the wrong shape"). C is used
SQUARE_STYLE20 = "C"


WHEEL27 = "B"


def wheel(cx, cy, r, square=False, col=None, v12=None):
    col = col or C["charcoal"]
    if square and v12 == "barrow20":
        t = max(3.5, r * 0.30)
        style = SQUARE_STYLE20
        box_ = f'x="{cx - r + t / 2:.1f}" y="{cy - r + t / 2:.1f}" width="{2 * r - t:.1f}" height="{2 * r - t:.1f}" stroke-linejoin="miter"'
        if style == "A":
            svg = f'<rect {box_} fill="{C["gray"]}" stroke="{OUT}" stroke-width="{t + OW * 1.2:.1f}"/><rect {box_} fill="none" stroke="{col}" stroke-width="{t - OW * 0.2:.1f}"/>'
            h = r * 0.26
            svg += rect(cx - h, cy - h, 2 * h, 2 * h, C["charcoal"], 0, OW * 0.6)
            for ax, ay in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
                svg += circ(cx + ax * (r - t) * 0.55, cy + ay * (r - t) * 0.55, max(1.4, r * 0.06), C["slate"], 0)
            return svg
        if style == "C":
            # eight straight spokes from a square hub to the corners and the middles of the sides
            w = max(1.8, r * 0.085)
            svg = ""
            for ax, ay in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
                svg += line(cx, cy, cx + ax * (r - t * 0.6), cy + ay * (r - t * 0.6), OUT, w)
            svg += f'<rect {box_} fill="none" stroke="{OUT}" stroke-width="{t + OW * 1.2:.1f}"/><rect {box_} fill="none" stroke="{col}" stroke-width="{t - OW * 0.2:.1f}"/>'
            h = r * 0.24
            return svg + rect(cx - h, cy - h, 2 * h, 2 * h, C["charcoal"], 0, OW * 0.6)
        w = max(2.4, r * 0.14)
        svg = ""
        for x0, y0, x1, y1 in ((cx - r + t * 0.6, cy, cx + r - t * 0.6, cy), (cx, cy - r + t * 0.6, cx, cy + r - t * 0.6)):
            svg += line(x0, y0, x1, y1, OUT, w + OW * 1.2) + line(x0, y0, x1, y1, C["slate"], w)
        svg += f'<rect {box_} fill="none" stroke="{OUT}" stroke-width="{t + OW * 1.2:.1f}"/><rect {box_} fill="none" stroke="{col}" stroke-width="{t - OW * 0.2:.1f}"/>'
        h = r * 0.22
        return svg + rect(cx - h, cy - h, 2 * h, 2 * h, C["charcoal"], 0, OW * 0.6)
    if square and v12:
        # v0.12: an open square wheel with sharp corners: eight thin spokes set off the diagonals, the ground
        # showing between them, a thin tyre over their ends and a round hub. Four spokes on the diagonals
        # of a filled square made an X ("a crate", "a square box behind the wheelbarrow"); tread blocks and
        # rounded corners made "a rounded square or octagon", "a round wheel drawn badly"
        t = max(3.0, r * 0.22)
        for k in range(8):
            a = math.radians(22.5 + 45 * k)
            c, sn = math.cos(a), math.sin(a)
            L = (r - t * 0.6) / max(abs(c), abs(sn))
            svg_ = line(cx, cy, cx + c * L, cy + sn * L, OUT, max(1.8, r * 0.085))
            svg = svg_ if k == 0 else svg + svg_
        box_ = f'x="{cx - r + t / 2:.1f}" y="{cy - r + t / 2:.1f}" width="{2 * r - t:.1f}" height="{2 * r - t:.1f}" fill="none" stroke-linejoin="miter"'
        svg += f'<rect {box_} stroke="{OUT}" stroke-width="{t + OW * 1.2:.1f}"/><rect {box_} stroke="{col}" stroke-width="{t - OW * 0.2:.1f}"/>'
        return svg + circ(cx, cy, r * 0.28, C["charcoal"], OW * 0.6) + circ(cx, cy, r * 0.1, C["gray"], 0)
    if square:
        # a square tyre around a square rim, with a round hub and four spokes: plainly a wheel, and
        # plainly square (a filled square read as a box hiding the wheel)
        t = max(3.0, r * 0.26)
        svg = rect(cx - r, cy - r, 2 * r, 2 * r, col, r * 0.12)
        svg += rect(cx - r + t, cy - r + t, 2 * (r - t), 2 * (r - t), C["gray"], r * 0.06, OW * 0.6)
        for ax, ay in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
            svg += line(cx, cy, cx + ax * (r - t) * 0.92, cy + ay * (r - t) * 0.92, OUT, max(2.0, r * 0.09))
        return svg + circ(cx, cy, r * 0.2, C["charcoal"], OW * 0.6)
    if v12 == "bike" and WHEEL27 == "B":
        # v0.27: a tyre round spokes, the ground showing through (solid, the wheels read as "solid black disc wheels")
        t = max(3.0, r * 0.20)
        svg = ""
        for i in range(8):
            a = i * math.pi / 8
            svg += line(cx - math.cos(a) * (r - t), cy - math.sin(a) * (r - t), cx + math.cos(a) * (r - t), cy + math.sin(a) * (r - t), C["slate"], max(1.2, r * 0.05))
        svg += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r - t / 2:.1f}" fill="none" stroke="{OUT}" stroke-width="{t + OW * 1.2:.1f}"/>'
        svg += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r - t / 2:.1f}" fill="none" stroke="{col}" stroke-width="{t - OW * 0.2:.1f}"/>'
        return svg + circ(cx, cy, r * 0.16, C["gray"], OW * 0.6)
    return circ(cx, cy, r, col) + circ(cx, cy, r * 0.3, C["gray"], OW * 0.6)


def wheelbarrow(x, y, s=1.0, square=False, f=1, both=False, bracket=False, low=False, stand=False, v20=False):
    """Ground point x,y under the wheel's center; f = +1 handles to the right. both = also draw the far
    handle and leg (v0.9: with one handle showing it read as "a one-handled wheelbarrow"). stand (v0.20): the tub raised
    on a bigger wheel and two long legs (low on the grass it read as "very flat ... with no visible legs, looks tipped")."""
    if stand and not square:
        return _wheelbarrow_stand(x, y, s, f, both)
    r = (25 if square else 17) * s
    wy = y - r
    tub = [(x - f * 15 * s, y - 58 * s), (x + f * 90 * s, y - 58 * s), (x + f * 75 * s, y - 13 * s), (x + f * 0 * s, y - 13 * s)]
    if square:          # lift the tub so the bigger wheel sits under its front end
        tub = [(px, py - 12 * s) for px, py in tub]
    svg = ""
    lift = 12 if square else 0
    if low:
        # v0.17: the handles run back from under the tub, rising gently to the grips, the far one just behind the near
        # one (from the tub's top rim they stood up "as if tipped forward onto its wheel")
        h0, h1 = (x + f * 30 * s, y - (22 + lift) * s), (x + f * 146 * s, y - (40 + lift) * s)
        far = (-f * 4 * s, -5 * s)
    else:
        h0, h1 = (x + f * 85 * s, y - (64 if square else 52) * s), (x + f * 140 * s, y - (44 if square else 32) * s)
        far = (-f * 5 * s, -10 * s)
    if both:
        dx, dy = far
        svg += stroke(poly_d([(h0[0] + dx, h0[1] + dy), (h1[0] + dx, h1[1] + dy)]), C["wood"], 7 * s)
        svg += stroke(poly_d([(x + f * 70 * s + dx, y - (26 if square else 14) * s + dy), (x + f * 74 * s + dx, y + dy * 0.6)]), C["charcoal"], 5 * s)
    # (low: the near handle drawn before the tub, so it runs on under the tub instead of lying across it)
    svg += stroke(poly_d([h0, h1]), C["wood"], 7 * s)
    svg += stroke(poly_d([(x + f * 70 * s, y - (26 if square else 14) * s), (x + f * 74 * s, y)]), C["charcoal"], 5 * s)
    wx = x - f * (6 if square else 0) * s
    if bracket and square:
        # v0.12: the square wheel mostly out in front of the tub, so its whole square shows (with its top
        # half behind the tub, only an L of it showed: "a square frame")
        wx = x - f * 20 * s
    if bracket:
        # v0.12: a ground shadow like the people's ("the wheelbarrow casts no visible shadow, while the
        # people and the dog do")
        svg = shadow(x + f * 52 * s, y, BARROW_SHADOW25 * s) + svg
    if bracket:
        # v0.12: the wheel tucked under the front of the tub, the tub drawn over its top (drawn in front of
        # the tub, a square wheel read as a crate standing in front of the barrow)
        svg += wheel(wx, wy, r, square, v12="barrow20" if v20 else "barrow")
        svg += poly(tub, C["gray"])
    else:
        svg += poly(tub, C["gray"])
        svg += wheel(wx, wy, r, square)

    if bracket:
        # v0.12: the wheel's fork runs from under the tub down to the hub, drawn over the wheel, with an
        # axle bolt, so the wheel is plainly fixed to the barrow (the square wheel alone read as "a
        # separate box ... the real wheel hidden behind it")
        ty = (y - 13 * s) - (12 * s if square else 0)
        for bx in (x + f * 4 * s, x + f * 26 * s):
            svg += stroke(poly_d([(bx, ty - 2 * s), (wx, wy)]), C["slate"], 6 * s, OW * 0.8)
        if v20 and square:
            # v0.22: a square axle plate, nothing round at the wheel's middle
            a_ = max(4.0, r * 0.26)
            svg += rect(wx - a_, wy - a_, 2 * a_, 2 * a_, C["slate"], 0, OW * 0.7) + rect(wx - a_ * 0.35, wy - a_ * 0.35, a_ * 0.7, a_ * 0.7, OUT, 0, 0)
        else:
            svg += circ(wx, wy, max(4.0, r * 0.26), C["slate"], OW * 0.7) + circ(wx, wy, max(1.6, r * 0.09), OUT, 0)
    # (the wheel end reaches 32 px past x on the side away from the handles, whichever way it faces; 46 px
    # for the square wheel set forward)
    e = (48 if bracket and square else 34) * s
    return svg, (min(x - f * e, x + f * (150 if low else 145) * s), y - 72 * s, max(x - f * e, x + f * (150 if low else 145) * s), y)


# v0.23: the filler wheelbarrow's leg as a thin strut with no foot (see _wheelbarrow_stand; chosen on the bench over a strut
# with a small flat foot, which one reader still saw "a bit like a boot")
LEG23 = "strut"
# v0.24 bench: px (at the front row's scale) a rider sits above the seesaw's seat point, and below the middle of the slide's
# chute. Riders read "slightly in front of" the plank and the chute in seven v0.23 pictures. Chosen (isolation_v024.md): the
# seesaw as it was (raised 10 or 18 px, riders "overlap the plank" or "float slightly above the seat"), the slide at 0 ("looks
# seated on the slide"; at 8 "slightly above or in front of" it, at -8 "hover just above" it).
RIDE24 = {"seesaw": 0, "slide": 0}
# v0.25 bench (isolation_v025.md): the width of the wheelbarrow's shadow, 200 and 210 before ("a large dark oval extending well
# beyond it", four v0.24 probes; at 160 it "looks slightly lifted"); the sandwich bird's size ("about as big as the sandwich", "a
# blue kettle or jug"; at 0.68 "a glove or bag"); and the newspaper dog's paws ("white gloved hands", three pictures): "O" white
# ovals with toes over the paper, "A" ovals in the dog's own colour, "B" with toes (both "stuck onto" the paper, "detached from
# the arms"), "C" no ovals, the paper behind the dog so its own paws rest on it.
BARROW_SHADOW25 = 130
BIRD25 = 0.8
PAW25 = "C"


def _wheelbarrow_stand(x, y, s, f, both):
    """v0.20: the wheelbarrow at rest on its wheel and legs, the tub well off the ground, the handles sloping up to the
    grips; the same footprint as before."""
    r = 21 * s
    wy = y - r
    tb = y - 34 * s                     # the tub's bottom
    tub = [(x - f * 16 * s, tb - 46 * s), (x + f * 92 * s, tb - 46 * s), (x + f * 76 * s, tb), (x + f * 6 * s, tb)]
    h0, h1 = (x + f * 22 * s, tb - 4 * s), (x + f * 150 * s, y - 52 * s)
    leg = lambda dx, dy: stroke(poly_d([(x + f * 84 * s + dx, tb + 2 * s + dy), (x + f * 90 * s + dx, y - 3 * s + dy)]), C["charcoal"], 6 * s)
    foot = lambda dx, dy: stroke(poly_d([(x + f * 84 * s + dx, y - 3 * s + dy), (x + f * 97 * s + dx, y - 3 * s + dy)]), C["charcoal"], 5 * s)
    if LEG23 == "strut":
        # v0.23 bench round 2: the strut alone, no foot
        leg = lambda dx, dy: stroke(poly_d([(x + f * 82 * s + dx, tb - 2 * s + dy), (x + f * 87 * s + dx, y - 1 * s + dy)]), C["slate"], 3.6 * s)
        foot = lambda dx, dy: ""
    elif LEG23:
        # v0.23: a thin metal strut with a small flat foot centred under it (the thick dark leg and the foot running forward
        # from its bottom made an L that two v0.22 readers saw as "a small dark boot")
        leg = lambda dx, dy: stroke(poly_d([(x + f * 82 * s + dx, tb - 2 * s + dy), (x + f * 88 * s + dx, y - 3 * s + dy)]), C["slate"], 3.6 * s)
        foot = lambda dx, dy: stroke(poly_d([(x + f * 83 * s + dx, y - 2 * s + dy), (x + f * 93 * s + dx, y - 2 * s + dy)]), C["slate"], 3.0 * s)
    svg = shadow(x + f * 55 * s, y, BARROW_SHADOW25 * s)
    if both:
        dx, dy = -f * 4 * s, -5 * s
        svg += stroke(poly_d([(h0[0] + dx, h0[1] + dy), (h1[0] + dx, h1[1] + dy)]), C["wood"], 7 * s)
        svg += leg(dx, dy) + foot(dx, dy)
    svg += stroke(poly_d([h0, h1]), C["wood"], 7 * s)
    svg += wheel(x, wy, r, False)
    svg += poly(tub, C["gray"])
    svg += stroke(poly_d([(x + f * 40 * s, tb - 2 * s), (x + f * 66 * s, tb - 2 * s)]), C["slate"], 4 * s)
    for bx in (x + f * 8 * s, x + f * 30 * s):
        svg += stroke(poly_d([(bx, tb - 2 * s), (x, wy)]), C["slate"], 6 * s, OW * 0.8)
    svg += circ(x, wy, max(4.0, r * 0.26), C["slate"], OW * 0.7) + circ(x, wy, max(1.6, r * 0.09), OUT, 0)
    svg += leg(0, 0) + foot(0, 0)
    e = 34 * s
    return svg, (min(x - f * e, x + f * 152 * s), tb - 50 * s, max(x - f * e, x + f * 152 * s), y)


def bicycle(x, y, s=1.0, square=False, col=None, f=1, rack=False, wide=False, heavy_stand=False, front_stand=False, center_stand=False):
    """Parked bicycle seen from the side. x,y = ground point midway between the wheels. wide (v0.12): a
    longer wheelbase and smaller wheels (the wheels nearly touching read as "squashed")."""
    col = col or C["teal"]
    r = (30 if wide else 34) * s
    wb = (64 if wide else 52) * s
    a, b = (x - f * wb, y - r), (x + f * wb, y - r)
    seat = (x - f * (22 if wide else 18) * s, y - 92 * s)
    bars = (x + f * (42 if wide else 34) * s, y - 102 * s)
    crank = (x, y - r)
    svg = wheel(a[0], a[1], r, square, C["charcoal"], v12="bike" if wide else None) + wheel(b[0], b[1], r, square, C["charcoal"], v12="bike" if wide else None)
    frame = f"M {P(*a)} L {P(*crank)} L {P(seat[0], seat[1] + 12 * s)} Z M {P(*crank)} L {P(bars[0] - f * 6 * s, bars[1] + 14 * s)} L {P(seat[0], seat[1] + 12 * s)} M {P(bars[0] - f * 6 * s, bars[1] + 14 * s)} L {P(*b)}"
    svg += stroke(frame, col, 6 * s)
    if wide:
        # v0.12: a saddle on a seat post, and handlebars on a stem sweeping back to a grip (two short dark
        # bars alike, the bars floating above the frame: "I can't tell the seat from the handlebars")
        sx, sy = seat
        svg += stroke(poly_d([(sx, sy + 12 * s), (sx, sy + 2 * s)]), C["slate"], 4 * s, OW * 0.5)
        svg += poly([(sx - f * 13 * s, sy - 4.5 * s), (sx + f * 13 * s, sy - 1 * s), (sx + f * 13 * s, sy + 2 * s), (sx - f * 11 * s, sy + 5 * s)], C["charcoal"], OW * 0.6)
        hx, hy = bars[0] - f * 6 * s, bars[1] + 14 * s
        tx, ty = bars[0] - f * 2 * s, bars[1] - 2 * s
        svg += stroke(poly_d([(hx, hy), (tx, ty)]), C["slate"], 4 * s, OW * 0.5)
        svg += stroke(f"M {P(tx, ty)} Q {P(tx + f * 8 * s, ty - 8 * s)} {P(tx - f * 6 * s, ty - 9 * s)}", C["slate"], 3.6 * s, OW * 0.5)
        svg += stroke(poly_d([(tx - f * 6 * s, ty - 9 * s), (tx - f * 16 * s, ty - 8 * s)]), C["charcoal"], 6 * s, OW * 0.6)
    else:
        svg += stroke(poly_d([(seat[0] - f * 12 * s, seat[1]), (seat[0] + f * 10 * s, seat[1])]), C["charcoal"], 7 * s)
        svg += stroke(poly_d([(bars[0] - f * 10 * s, bars[1]), (bars[0] + f * 8 * s, bars[1] - 4 * s)]), C["charcoal"], 6 * s)
    if wide:
        # v0.12: a chain ring with its chain to the back hub, a short crank with a pedal, and a thin stand
        # off the back of the frame ending in a foot (the stand drawn from the crank read as "a crank or
        # pedal arm ... too long", "through the ground", and "no chain")
        cr = 9 * s
        chain = (f"M {P(crank[0], crank[1] - cr)} L {P(a[0], a[1] - 4 * s)} "
                 f"M {P(crank[0], crank[1] + cr)} L {P(a[0], a[1] + 4 * s)}")
        svg += stroke(chain, C["charcoal"], 2.6 * s, OW * 0.35)
        svg += circ(crank[0], crank[1], cr, C["gray"], OW * 0.6)
        pd = (crank[0] + f * 7 * s, crank[1] + 15 * s)
        svg += stroke(poly_d([crank, pd]), C["slate"], 4 * s, OW * 0.5)
        svg += rect(pd[0] - 7 * s, pd[1] - 2 * s, 14 * s, 4.5 * s, C["charcoal"], 1.5 * s, OW * 0.5)
        svg += circ(crank[0], crank[1], 3 * s, C["slate"], OW * 0.4)
        ks0 = (crank[0] - f * 16 * s, crank[1] + 3 * s)
        ks = (crank[0] - f * 30 * s, y - 1)
        if center_stand:
            # v0.16: a two-legged centre stand under the crank, splayed out to two feet on the open ground between the
            # wheels, dark against the grass (a single stand off the frame, light or dark, still left the bicycle "standing
            # upright with no rider or stand")
            c0 = (crank[0] - f * 6 * s, crank[1] + 6 * s)
            for dxs in (-17, 17):
                ft = (crank[0] + dxs * s, y - 1)
                svg += stroke(poly_d([c0, ft]), C["charcoal"], 5 * s, OW * 0.7)
                svg += ell(ft[0] + (dxs / 17) * 3 * s, ft[1] - 1 * s, 7 * s, 2.8 * s, C["charcoal"], OW * 0.5)
            svg += circ(c0[0], c0[1], 4.5 * s, C["charcoal"], OW * 0.5)
        elif front_stand:
            # v0.14: the stand drawn in front of the wheel, light grey against it, from the chain stay well behind the crank
            # down and back to a broad foot on the ground (from the crank itself it read as "a long pedal arm")
            k0 = (crank[0] - f * 26 * s, crank[1] + 5 * s)
            ks = (crank[0] - f * 46 * s, y)
            svg += stroke(poly_d([k0, ks]), C["gray"], 5.5 * s, OW * 0.7)
            svg += ell(ks[0] - f * 3 * s, ks[1] - 1 * s, 10 * s, 3.4 * s, C["gray"], OW * 0.6)
        elif heavy_stand:
            # v0.13: a heavier stand, darker, splayed out with a broad foot (a square-wheeled bicycle with the
            # thin stand "stands upright on its own with no rider and no stand visible")
            ks = (crank[0] - f * 36 * s, y)
            svg = stroke(poly_d([ks0, ks]), C["charcoal"], 6 * s, OW * 0.7) + svg
            svg += ell(ks[0] - f * 3 * s, ks[1] - 1 * s, 10 * s, 3.4 * s, C["charcoal"], OW * 0.6)
        else:
            svg = stroke(poly_d([ks0, ks]), C["slate"], 3.5 * s, OW * 0.6) + svg
            svg += ell(ks[0] - f * 2 * s, ks[1], 6 * s, 2.2 * s, C["charcoal"], OW * 0.5)
        svg = shadow(x, y, 2 * (wb + r) * 0.95) + svg
    else:
        svg += circ(crank[0], crank[1], 7 * s, C["gray"], OW * 0.7)
        # kickstand: a parked bike stands on its stand, never by itself
        ks = (crank[0] - f * 34 * s, y + 1)
        svg = stroke(poly_d([(crank[0] - f * 4 * s, crank[1] + 4 * s), ks]), C["gray"], 6 * s, OW * 0.8) + svg
        svg += ell(ks[0], ks[1] - 1, 8 * s, 3 * s, C["charcoal"], OW * 0.6)
    if rack:
        # v0.7: parked against a steel rack hoop drawn behind it (on its kickstand alone, a parked bike
        # still read as standing up by itself)
        # (v0.14, rack="narrow": a narrow hoop standing between the wheels, its legs clear of them; the wide hoop's legs
        # came down on square wheels, which then read as "square wheel-holder frames that belong to the rack")
        hw = (70 if wide else 60) * s if rack != "narrow" else 30 * s
        hoop = f"M {P(x - hw, y - 4 * s)} L {P(x - hw, y - 78 * s)} Q {P(x - hw, y - 104 * s)} {P(x - hw + 26 * s, y - 104 * s)} L {P(x + hw - 26 * s, y - 104 * s)} Q {P(x + hw, y - 104 * s)} {P(x + hw, y - 78 * s)} L {P(x + hw, y - 4 * s)}"
        svg = stroke(hoop, C["gray"], 8 * s, OW * 0.9) + svg
    ext = (98 if wide else 90) * s
    return svg, (x - ext, y - 110 * s, x + ext, y)


def floating_crate(x, y, s=1.0, lift=0.0, col=None, tilt=12.0, ground_shadow=True):
    """A wooden box hanging in the air `lift` px above its own shadow at (x, y). Seen from below (its
    underside shows, which a box standing on the ground never does) and tilted, so it cannot be read
    as a box standing further back on the ground; the shadow sits straight under it."""
    col = col or C["wood_light"]
    w, h = 90 * s, 70 * s
    yb = y - lift
    # v0.13: no ground shadow once the box hangs high above it (far below the raised box, its shadow read
    # as "a shadow with nothing above it to cast it")
    svg = f'<ellipse cx="{x:.1f}" cy="{y + 2:.1f}" rx="{w * 0.5:.1f}" ry="{w * 0.13:.1f}" fill="{OUT}" fill-opacity="0.24"/>' if ground_shadow else ""
    g = f'<g transform="rotate({tilt:.1f} {x:.1f} {yb - h / 2:.1f})">'
    g += poly([(x - w / 2, yb), (x - w / 2 + 16 * s, yb + 14 * s), (x + w / 2 + 16 * s, yb + 14 * s), (x + w / 2, yb)], C["wood"])
    g += poly([(x + w / 2, yb - h), (x + w / 2 + 16 * s, yb - h + 14 * s), (x + w / 2 + 16 * s, yb + 14 * s), (x + w / 2, yb)], C["tan"])
    g += rect(x - w / 2, yb - h, w, h, col, 2 * s)
    g += line(x - w / 2 + 6 * s, yb - h / 2, x + w / 2 - 6 * s, yb - h / 2, C["wood"], 4 * s)
    g += "</g>"
    pad = 14 * s
    return svg + g, (x - w / 2 - pad, yb - h - pad, x + w / 2 + 16 * s + pad, yb + 14 * s + pad)


def crate(x, y, s=1.0, lift=0.0, col=None):
    """Wooden box with its ground point at (x, y); lift > 0 floats it that many px above its shadow."""
    col = col or C["wood_light"]
    w, h = 90 * s, 70 * s
    yb = y - lift
    svg = shadow(x, y, w * (1.0 if lift == 0 else 0.8))
    svg += poly([(x - w / 2, yb - h), (x - w / 2 + 16 * s, yb - h - 14 * s), (x + w / 2 + 16 * s, yb - h - 14 * s), (x + w / 2, yb - h)], C["tan"])
    svg += poly([(x + w / 2, yb - h), (x + w / 2 + 16 * s, yb - h - 14 * s), (x + w / 2 + 16 * s, yb - 14 * s), (x + w / 2, yb)], C["wood"])
    svg += rect(x - w / 2, yb - h, w, h, col, 2 * s)
    svg += line(x - w / 2 + 6 * s, yb - h / 2, x + w / 2 - 6 * s, yb - h / 2, C["wood"], 4 * s)
    return svg, (x - w / 2, yb - h - 14 * s, x + w / 2 + 16 * s, yb)


def long_box(x, y, s=1.0, w=62, h=34, dx=30, dy=62, grain=False):
    """v0.29: a long low box or board lying with its length across a walker's way, its ground point the middle of its footprint (a bucket on the line of the stride was "to the side of her
    path rather than directly under her feet")."""
    w, h, dx, dy = w * s, h * s, dx * s, dy * s
    x0, y0 = x - (w + dx) / 2, y + dy / 2
    svg = shadow(x, y + dy / 2 - 4 * s, w + dx * 0.9)
    svg += poly([(x0, y0 - h), (x0 + dx, y0 - h - dy), (x0 + w + dx, y0 - h - dy), (x0 + w, y0 - h)], C["tan"])
    svg += poly([(x0 + w, y0 - h), (x0 + w + dx, y0 - h - dy), (x0 + w + dx, y0 - dy), (x0 + w, y0)], C["wood"])
    svg += rect(x0, y0 - h, w, h, C["wood_light"], 2 * s)
    if grain:
        for k in (0.33, 0.66):
            svg += line(x0 + w * k + 2 * dx * 0.08, y0 - h - dy * 0.12, x0 + w * k + dx * 0.9, y0 - h - dy * 0.9, C["wood"], 2 * s)
    else:
        svg += line(x0 + w * 0.5 + dx * 0.1, y0 - h - dy * 0.1, x0 + w * 0.5 + dx * 0.9, y0 - h - dy * 0.9, C["wood"], 3 * s)
    return svg, (x0, y0 - h - dy, x0 + w + dx, y0)


def package(x, y, s=1.0):
    w, h = 74 * s, 50 * s
    svg = shadow(x, y, w)
    svg += poly([(x - w / 2, y - h), (x - w / 2 + 12 * s, y - h - 12 * s), (x + w / 2 + 12 * s, y - h - 12 * s), (x + w / 2, y - h)], C["tan"])
    svg += poly([(x + w / 2, y - h), (x + w / 2 + 12 * s, y - h - 12 * s), (x + w / 2 + 12 * s, y - 12 * s), (x + w / 2, y)], C["wood"])
    svg += rect(x - w / 2, y - h, w, h, C["khaki"], 2 * s)
    svg += rect(x - 6 * s, y - h, 12 * s, h, C["cream"], 0, OW * 0.6)
    return svg, (x - w / 2, y - h - 12 * s, x + w / 2 + 12 * s, y)


def bucket(x, y, s=1.0, col=None, tipped=False):
    col = col or C["blue"]
    if tipped:
        svg = poly([(x - 34 * s, y - 34 * s), (x + 22 * s, y - 44 * s), (x + 26 * s, y), (x - 30 * s, y - 2 * s)], col)
        svg += ell(x - 33 * s, y - 17 * s, 9 * s, 18 * s, "#2a4a92", OW * 0.8)
        return svg, (x - 44 * s, y - 46 * s, x + 28 * s, y)
    svg = poly([(x - 26 * s, y - 52 * s), (x + 26 * s, y - 52 * s), (x + 20 * s, y), (x - 20 * s, y)], col)
    svg += ell(x, y - 52 * s, 26 * s, 7 * s, "#2a4a92", OW * 0.8)
    svg += f'<path d="M {P(x - 24 * s, y - 50 * s)} Q {P(x, y - 86 * s)} {P(x + 24 * s, y - 50 * s)}" fill="none" stroke="{OUT}" stroke-width="3"/>'
    return svg, (x - 28 * s, y - 86 * s, x + 28 * s, y)


def puddle(x, y, s=1.0, w=160):
    return ell(x, y, w / 2 * s, 18 * s, C["water_light"], OW * 0.7)


def ball(x, y, r, col=None):
    col = col or C["red"]
    svg = circ(x, y, r, col)
    svg += f'<path d="M {P(x - r, y)} Q {P(x, y + r * 0.6)} {P(x + r, y)}" fill="none" stroke="{C["white"]}" stroke-width="{max(2, r * 0.22):.1f}"/>'
    return svg


def beach_ball(x, y, r, col=None):
    """v0.28: a ball of coloured panels meeting at a cap (one white band round a blue ball: "a blue planet-like sphere"; two bands across it were a target)."""
    col = col or C["blue"]
    svg = circ(x, y, r, col)
    px_, py_ = x - 0.22 * r, y - 0.52 * r          # the cap, turned toward the viewer's upper left
    rr = max(0.5, r - OW * 0.5)
    for a0, a1 in ((-35, 15), (65, 115), (165, 215)):
        ax, ay = x + rr * math.cos(math.radians(a0)), y + rr * math.sin(math.radians(a0))
        bx, by = x + rr * math.cos(math.radians(a1)), y + rr * math.sin(math.radians(a1))
        svg += (f'<path d="M {P(px_, py_)} Q {P((px_ + ax) / 2 + 0.10 * r, (py_ + ay) / 2 - 0.10 * r)} {P(ax, ay)} A {rr:.1f} {rr:.1f} 0 0 1 {P(bx, by)} '
                f'Q {P((px_ + bx) / 2 - 0.10 * r, (py_ + by) / 2 + 0.05 * r)} {P(px_, py_)} Z" fill="{C["white"]}"/>')
    svg += ell(px_, py_, 0.17 * r, 0.14 * r, C["yellow"], OW * 0.5)
    svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="none" stroke="{OUT}" stroke-width="{OW}"/>'
    return svg


def kite(x, y, s=1.0, col=None, rot=0, wind=0):
    col = col or C["yellow"]
    pts = [(0, -50), (34, 0), (0, 62), (-34, 0)]
    a = math.radians(rot)
    tp = [(x + (px * math.cos(a) - py * math.sin(a)) * s, y + (px * math.sin(a) + py * math.cos(a)) * s) for px, py in pts]
    svg = poly(tp, col)
    svg += line(tp[0][0], tp[0][1], tp[2][0], tp[2][1], OUT, 3) + line(tp[1][0], tp[1][1], tp[3][0], tp[3][1], OUT, 3)
    tail = tp[2]
    if wind:
        # v0.14: a flying kite's tail streams away downwind in a long wave, the bows along it, and the string is tied
        # at the spars' crossing (the tail hanging straight down beside the string's last stretch: "the string seems
        # to run to the bottom of the kite's tail rather than to the kite itself")
        tpts = [(tail[0] + wind * 52 * s * t + 7 * s * math.sin(t * 2 * math.pi) * (1 - t), tail[1] + 78 * s * t - 10 * s * t * t)
                for t in (i / 16 for i in range(17))]
        svg += f'<path d="{poly_d(tpts)}" fill="none" stroke="{OUT}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
        for i, t in enumerate((0.44, 0.88)):
            bx, by = tpts[round(t * 16)]
            svg += poly([(bx - 9 * s, by - 6 * s), (bx + 9 * s, by + 6 * s), (bx + 9 * s, by - 6 * s), (bx - 9 * s, by + 6 * s)], C["red"] if i == 0 else C["blue"], OW * 0.6)
        xs = [q[0] for q in tp + tpts]
        return svg, {"bridle": (x, y), "bbox": (min(xs) - 10 * s, y - 55 * s, max(xs) + 10 * s, max(q[1] for q in tpts) + 8 * s)}
    d = f"M {P(*tail)} q {12 * s:.1f} {24 * s:.1f} 0 {44 * s:.1f} q {-12 * s:.1f} {20 * s:.1f} {4 * s:.1f} {40 * s:.1f}"
    svg += f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="3"/>'
    for i, t in enumerate((0.33, 0.66)):
        bx, by = tail[0] + 2 * s, tail[1] + 84 * s * t
        svg += poly([(bx - 9 * s, by - 6 * s), (bx + 9 * s, by + 6 * s), (bx + 9 * s, by - 6 * s), (bx - 9 * s, by + 6 * s)], C["red"] if i == 0 else C["blue"], OW * 0.6)
    return svg, {"bridle": (x, y + 8 * s), "bbox": (x - 40 * s, y - 55 * s, x + 40 * s, y + 150 * s)}


def kite_outline(x, y, s=1.0, rot=0, grow=1.0):
    """The kite's diamond as drawn by kite(), scaled about its centre by `grow` (for clipping)."""
    a = math.radians(rot)
    return [(x + (px * math.cos(a) - py * math.sin(a)) * s * grow, y + (px * math.sin(a) + py * math.cos(a)) * s * grow)
            for px, py in [(0, -50), (34, 0), (0, 62), (-34, 0)]]


def balloon(x, y, s=1.0, col=None, string_to=None, string_len=110):
    col = col or C["red"]
    svg = ell(x, y, 28 * s, 34 * s, col)
    svg += poly([(x - 6 * s, y + 38 * s), (x + 6 * s, y + 38 * s), (x, y + 32 * s)], col, OW * 0.6)
    end = string_to or (x + 8 * s, y + 34 * s + string_len * s)
    svg = f'<path d="M {P(x, y + 38 * s)} Q {P(x - 18 * s, (y + end[1]) / 2)} {P(*end)}" fill="none" stroke="{OUT}" stroke-width="2.5"/>' + svg
    svg += ell(x - 10 * s, y - 12 * s, 6 * s, 9 * s, C["white"], 0, rot=20)
    return svg, (x - 30 * s, y - 36 * s, x + 30 * s, max(end[1], y + 40 * s))


def fish(x, y, s=1.0, col=None, f=1):
    col = col or C["orange"]
    svg = poly([(x - f * 34 * s, y), (x - f * 52 * s, y - 16 * s), (x - f * 52 * s, y + 16 * s)], col, OW * 0.8)
    svg += ell(x, y, 36 * s, 18 * s, col)
    svg += circ(x + f * 18 * s, y - 4 * s, 4 * s, OUT, 0)
    svg += f'<path d="M {P(x + f * 4 * s, y - 14 * s)} Q {P(x - f * 2 * s, y)} {P(x + f * 4 * s, y + 14 * s)}" fill="none" stroke="{OUT}" stroke-width="2.5"/>'
    return svg, (x - 54 * s, y - 20 * s, x + 54 * s, y + 20 * s)


def cap(x, y, s=1.0, col=None, rot=-20):
    col = col or C["blue"]
    svg = f'<g transform="rotate({rot:.1f} {x:.1f} {y:.1f})">'
    svg += shape(f"M {P(x - 30 * s, y)} A {30 * s:.1f} {26 * s:.1f} 0 0 1 {P(x + 30 * s, y)} Z", col)
    svg += ell(x + 34 * s, y + 1 * s, 22 * s, 6 * s, col, OW * 0.8)
    svg += circ(x, y - 26 * s, 4 * s, col, OW * 0.6) + "</g>"
    return svg, (x - 36 * s, y - 34 * s, x + 60 * s, y + 12 * s)


def bread_bit(x, y, s=1.0, side=1):
    """A torn piece of bread with crust, held in a beak at (x, y)."""
    s *= 1.1
    d = f"M {P(x - 9 * s, y - 4 * s)} Q {P(x - 2 * s, y - 9 * s)} {P(x + 8 * s, y - 5 * s)} L {P(x + 10 * s, y + 3 * s)} Q {P(x + 1 * s, y + 7 * s)} {P(x - 8 * s, y + 4 * s)} Z"
    return shape(d, C["cream"], OW * 0.7) + f'<path d="M {P(x - 9 * s, y - 4 * s)} Q {P(x - 2 * s, y - 9 * s)} {P(x + 8 * s, y - 5 * s)}" fill="none" stroke="{C["wood"]}" stroke-width="{3 * s:.1f}"/>'


def sandwich(x, y, s=1.0, bitten=0, style=5):
    """A sandwich on its side: crusted bread, a wavy lettuce frill, tomato and a drooping cheese corner.
    (A plain stack read as a pile of books.) bitten = +1/-1 tears a bite out of the right/left end.
    style 6 (v0.8): bolder filling and thin outlines (at scene size the v0.7 outlines swallowed the
    filling and it read as a stack of books or folded cloth)."""
    if bitten:
        sw, bb = sandwich(x, y, s, style=style)
        s2 = s * 1.1
        bx = x + bitten * 30 * s2
        # the bite: a scalloped notch in the bench's colour would hide the bench, so the notch is cut
        # with a clip path
        cid = f"bite{int(x)}_{int(y)}"
        notch = " ".join(f"M {P(bx + bitten * 2 * s2, y - (31 - k * 9) * s2)} m {-7 * s2:.1f} 0 a {7 * s2:.1f} {7 * s2:.1f} 0 1 0 {14 * s2:.1f} 0 a {7 * s2:.1f} {7 * s2:.1f} 0 1 0 {-14 * s2:.1f} 0" for k in range(3))
        clip = (f'<defs><clipPath id="{cid}"><path clip-rule="evenodd" d="M {P(x - 60 * s2, y - 60 * s2)} h {120 * s2:.1f} v {80 * s2:.1f} h {-120 * s2:.1f} Z {notch}"/></clipPath></defs>')
        return clip + f'<g clip-path="url(#{cid})">{sw}</g>', bb
    if style >= 6:
        s *= 1.1
        lw = OW * 0.45
        svg = rect(x - 31 * s, y - 10 * s, 62 * s, 10 * s, C["wood_light"], 4 * s, lw)
        svg += rect(x - 27 * s, y - 7 * s, 54 * s, 3.5 * s, C["cream"], 2 * s, 0)
        frill = " ".join(f"Q {P(x - 35 * s + (k + 0.5) * 7 * s, y - 6 * s)} {P(x - 35 * s + (k + 1) * 7 * s, y - 11 * s)}" for k in range(10))
        svg += shape(f"M {P(x - 35 * s, y - 11 * s)} {frill} L {P(x + 35 * s, y - 17 * s)} L {P(x - 35 * s, y - 17 * s)} Z", C["green"], lw)
        for k in range(4):
            svg += circ(x - 21 * s + k * 14 * s, y - 18 * s, 5.5 * s, C["red"], lw)
        svg += poly([(x - 32 * s, y - 25 * s), (x + 32 * s, y - 25 * s), (x + 33 * s, y - 13 * s), (x + 25 * s, y - 20 * s), (x - 32 * s, y - 20 * s)], C["yellow"], lw)
        svg += shape(f"M {P(x - 32 * s, y - 24 * s)} Q {P(x - 32 * s, y - 40 * s)} {P(x, y - 40 * s)} Q {P(x + 32 * s, y - 40 * s)} {P(x + 32 * s, y - 24 * s)} Z", C["wood_light"], lw)
        svg += f'<path d="M {P(x - 22 * s, y - 31 * s)} Q {P(x, y - 37 * s)} {P(x + 20 * s, y - 32 * s)}" fill="none" stroke="{C["cream"]}" stroke-width="{3 * s:.1f}" stroke-linecap="round"/>'
        return svg, (x - 36 * s, y - 41 * s, x + 36 * s, y + 2 * s)
    s *= 1.1
    crust, bread = C["wood"], C["cream"]
    svg = rect(x - 30 * s, y - 12 * s, 60 * s, 12 * s, crust, 5 * s, OW * 0.8)
    svg += rect(x - 27 * s, y - 10 * s, 54 * s, 7 * s, bread, 3 * s, 0)
    wave = " ".join(f"Q {P(x - 32 * s + (k + 0.5) * 8 * s, y - 12 * s + (5 if k % 2 else -1) * s)} {P(x - 32 * s + (k + 1) * 8 * s, y - 13 * s)}" for k in range(8))
    svg += shape(f"M {P(x - 32 * s, y - 13 * s)} {wave} L {P(x + 32 * s, y - 18 * s)} L {P(x - 32 * s, y - 18 * s)} Z", C["green"], OW * 0.7)
    svg += rect(x - 24 * s, y - 22 * s, 46 * s, 5 * s, C["red"], 2 * s, OW * 0.6)
    svg += poly([(x - 28 * s, y - 23 * s), (x + 28 * s, y - 23 * s), (x + 30 * s, y - 15 * s), (x + 22 * s, y - 21 * s), (x - 28 * s, y - 21 * s)], C["yellow"], OW * 0.6)
    svg += rect(x - 30 * s, y - 36 * s, 60 * s, 13 * s, crust, 6 * s, OW * 0.8)
    svg += rect(x - 27 * s, y - 33 * s, 54 * s, 7 * s, bread, 3 * s, 0)
    return svg, (x - 33 * s, y - 37 * s, x + 33 * s, y + 2 * s)


# v0.28 bench (isolation_v028.md): "O" keeps the scoop in a puddle ("a pink hat or a pink frisbee", "flying saucer"); "A" a flat splat; "B" a splat with a low melted lump
SPLAT28 = "A"


def _splat28(x, y, s, col, lump):
    """v0.28: ice cream that has hit the ground and burst: a lobed splat lying flat, no dome, with flecks thrown clear of it and the sprinkles still on it."""
    rim = ((180, 47), (152, 27), (126, 42), (96, 24), (66, 40), (36, 26), (6, 48), (-24, 29), (-52, 40), (-88, 25), (-122, 39), (-154, 28))
    pts = [(x + r * math.cos(math.radians(a)) * s, y + r * 0.34 * math.sin(math.radians(a)) * s) for a, r in rim]
    mids = [((p[0] + q[0]) / 2, (p[1] + q[1]) / 2) for p, q in zip(pts, pts[1:] + pts[:1])]
    d = f"M {P(*mids[-1])} " + " ".join(f"Q {P(*p)} {P(*m)}" for p, m in zip(pts, mids)) + " Z"
    svg = shape(d, col, OW * 0.8)
    svg += ell(x - 8 * s, y - 2 * s, 21 * s, 5 * s, C["white"], 0).replace("/>", ' fill-opacity="0.28"/>')
    top = y - 2 * s
    if lump:
        top = y - 19 * s
        svg += shape(f"M {P(x - 20 * s, y + 1 * s)} Q {P(x - 24 * s, y - 10 * s)} {P(x - 10 * s, y - 13 * s)} Q {P(x - 3 * s, y - 20 * s)} {P(x + 7 * s, y - 13 * s)} "
                     f"Q {P(x + 22 * s, y - 11 * s)} {P(x + 19 * s, y + 1 * s)} Q {P(x, y + 5 * s)} {P(x - 20 * s, y + 1 * s)} Z", col, OW * 0.7)
        svg += ell(x - 7 * s, y - 10 * s, 4.5 * s, 2.4 * s, C["white"], 0, rot=-15)
    for (dx, dy, a, c) in ((-30, -2, 20, "yellow"), (-13, 3, -35, "blue"), (24, -3, 60, "green"), (31, 2, -20, "white"), (2, 5, 15, "yellow"), (14, -7, -50, "blue"), (-22, 5, 70, "green")):
        px_, py_ = x + dx * s, y + dy * s
        ux, uy = math.cos(math.radians(a)) * 3.2 * s, math.sin(math.radians(a)) * 1.8 * s
        svg += f'<path d="M {P(px_ - ux, py_ - uy)} L {P(px_ + ux, py_ + uy)}" stroke="{C[c]}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round"/>'
    for dx, dy, r in ((-55, -4, 3.0), (-50, 9, 2.2), (56, 6, 3.0), (52, -7, 2.2), (10, 17, 2.6), (-20, -17, 2.2)):
        svg += ell(x + dx * s, y + dy * s, r * s, r * 0.7 * s, col, OW * 0.4)
    return svg, (x - 58 * s, top, x + 59 * s, y + 19 * s)


def dropped_scoop(x, y, s=1.0, col=None, ball=1.0, style="O"):
    """A scoop of ice cream that has fallen on the ground: the round scoop (with the ridge left by the
    scoop and a highlight) sits in a melted puddle with drips. A flat blob read as a pink bag or a shoe.
    ball (v0.14) scales the scoop sitting in the puddle (full size it was "about as big as the dog's head")."""
    if style != "O":
        return _splat28(x, y, s, col or C["pink"], style == "B")
    if ball != 1.0:
        return _dropped_scoop_small(x, y, s, col or C["pink"], ball)
    col = col or C["pink"]
    svg = shape(f"M {P(x - 40 * s, y)} Q {P(x - 46 * s, y - 8 * s)} {P(x - 26 * s, y - 9 * s)} Q {P(x, y - 13 * s)} {P(x + 28 * s, y - 9 * s)} "
                f"Q {P(x + 48 * s, y - 7 * s)} {P(x + 40 * s, y + 1 * s)} Q {P(x + 30 * s, y + 9 * s)} {P(x + 12 * s, y + 6 * s)} "
                f"Q {P(x - 4 * s, y + 12 * s)} {P(x - 18 * s, y + 6 * s)} Q {P(x - 36 * s, y + 9 * s)} {P(x - 40 * s, y)} Z", col, OW * 0.8)
    # the scoop is a ball sitting in the puddle, with rainbow sprinkles (the plainest sign of ice cream)
    svg += ell(x, y - 17 * s, 22 * s, 19 * s, col)
    svg += f'<path d="M {P(x - 21 * s, y - 11 * s)} Q {P(x - 12 * s, y - 5 * s)} {P(x - 4 * s, y - 10 * s)} Q {P(x + 5 * s, y - 4 * s)} {P(x + 13 * s, y - 10 * s)} Q {P(x + 18 * s, y - 6 * s)} {P(x + 21 * s, y - 11 * s)}" fill="none" stroke="{OUT}" stroke-width="{OW * 0.7}"/>'
    svg += ell(x - 8 * s, y - 27 * s, 6 * s, 4 * s, C["white"], 0, rot=-25)
    for (dx, dy, a, c) in ((-10, -18, 30, "yellow"), (2, -29, -40, "blue"), (11, -20, 70, "green"), (-1, -15, -10, "white"), (9, -31, 15, "yellow"), (-14, -27, -60, "blue"), (15, -13, 40, "white")):
        cx, cy = x + dx * s, y + dy * s
        ux, uy = math.cos(math.radians(a)) * 3.2 * s, math.sin(math.radians(a)) * 3.2 * s
        svg += f'<path d="M {P(cx - ux, cy - uy)} L {P(cx + ux, cy + uy)}" stroke="{C[c]}" stroke-width="{2.4 * s:.1f}" stroke-linecap="round"/>'
    for dx, dy in ((-30, 4), (33, 3), (6, 9)):
        svg += circ(x + dx * s, y + dy * s, 2.5 * s, col, OW * 0.4)
    return svg, (x - 46 * s, y - 37 * s, x + 48 * s, y + 12 * s)


def _dropped_scoop_small(x, y, s, col, m):
    """v0.14: the same puddle, with a smaller scoop sitting in it (its offsets from the puddle's middle scaled by m,
    outlines kept at full weight)."""
    svg = shape(f"M {P(x - 40 * s, y)} Q {P(x - 46 * s, y - 8 * s)} {P(x - 26 * s, y - 9 * s)} Q {P(x, y - 13 * s)} {P(x + 28 * s, y - 9 * s)} "
                f"Q {P(x + 48 * s, y - 7 * s)} {P(x + 40 * s, y + 1 * s)} Q {P(x + 30 * s, y + 9 * s)} {P(x + 12 * s, y + 6 * s)} "
                f"Q {P(x - 4 * s, y + 12 * s)} {P(x - 18 * s, y + 6 * s)} Q {P(x - 36 * s, y + 9 * s)} {P(x - 40 * s, y)} Z", col, OW * 0.8)
    by = y - 4 * s                     # the scoop rests in the puddle: offsets measured from here
    q = lambda dx, dy: (x + dx * m * s, by + (dy + 4) * m * s)
    cx, cy = q(0, -17)
    svg += ell(cx, cy, 22 * m * s, 19 * m * s, col)
    r = [q(-21, -11), q(-12, -5), q(-4, -10), q(5, -4), q(13, -10), q(18, -6), q(21, -11)]
    svg += f'<path d="M {P(*r[0])} Q {P(*r[1])} {P(*r[2])} Q {P(*r[3])} {P(*r[4])} Q {P(*r[5])} {P(*r[6])}" fill="none" stroke="{OUT}" stroke-width="{OW * 0.7}"/>'
    hx, hy = q(-8, -27)
    svg += ell(hx, hy, 6 * m * s, 4 * m * s, C["white"], 0, rot=-25)
    for (dx, dy, a, c) in ((-10, -18, 30, "yellow"), (2, -29, -40, "blue"), (11, -20, 70, "green"), (-1, -15, -10, "white"), (9, -31, 15, "yellow"), (-14, -27, -60, "blue"), (15, -13, 40, "white")):
        px, py = q(dx, dy)
        ux, uy = math.cos(math.radians(a)) * 3.2 * m * s, math.sin(math.radians(a)) * 3.2 * m * s
        svg += f'<path d="M {P(px - ux, py - uy)} L {P(px + ux, py + uy)}" stroke="{C[c]}" stroke-width="{2.4 * max(m, 0.85) * s:.1f}" stroke-linecap="round"/>'
    for dx, dy in ((-30, 4), (33, 3), (6, 9)):
        svg += circ(x + dx * s, y + dy * s, 2.5 * s, col, OW * 0.4)
    top = cy - 19 * m * s
    return svg, (x - 46 * s, top, x + 48 * s, y + 12 * s)


def scoop_splat(x, y, s=1.0, col=None):
    col = col or C["pink"]
    svg = shape(f"M {P(x - 30 * s, y)} Q {P(x - 34 * s, y - 14 * s)} {P(x - 14 * s, y - 16 * s)} Q {P(x, y - 30 * s)} {P(x + 16 * s, y - 16 * s)} "
                f"Q {P(x + 38 * s, y - 14 * s)} {P(x + 30 * s, y)} Q {P(x, y + 8 * s)} {P(x - 30 * s, y)} Z", col)
    return svg, (x - 38 * s, y - 30 * s, x + 38 * s, y + 8 * s)


def cone(x, y, s=1.0, rot=0):
    svg = f'<g transform="rotate({rot:.1f} {x:.1f} {y:.1f})">' + poly([(x - 12 * s, y), (x + 12 * s, y), (x, y + 34 * s)], C["wood_light"], OW * 0.8) + "</g>"
    return svg, (x - 14 * s, y - 2 * s, x + 14 * s, y + 36 * s)


def paint_tin(x, y, s=1.0, col=None):
    """A tin of paint standing on the ground at (x, y), lid off, a drip down the side (v0.9: a fence being
    painted with no paint anywhere read as odd)."""
    col = col or C["paint"]
    w, h = 30 * s, 30 * s
    svg = rect(x - w / 2, y - h, w, h, C["gray"], 2 * s)
    svg += ell(x, y - h, w / 2, 5 * s, col)
    svg += shape(f"M {P(x + w / 2 - 7 * s, y - h + 2 * s)} L {P(x + w / 2 - 7 * s, y - h + 13 * s)} Q {P(x + w / 2 - 4 * s, y - h + 16 * s)} {P(x + w / 2 - 1 * s, y - h + 13 * s)} L {P(x + w / 2 - 1 * s, y - h + 2 * s)} Z", col, 0)
    svg += f'<path d="M {P(x - w / 2 + 2 * s, y - h)} Q {P(x, y - h - 22 * s)} {P(x + w / 2 - 2 * s, y - h)}" fill="none" stroke="{OUT}" stroke-width="{2.2 * s + 0.6:.1f}"/>'
    return svg, (x - w / 2 - 2, y - h - 22 * s, x + w / 2 + 2, y)


def paint_tray(x, y, s=1.0, col=None):
    col = col or C["paint"]
    svg = poly([(x - 44 * s, y - 16 * s), (x + 44 * s, y - 16 * s), (x + 38 * s, y), (x - 38 * s, y)], C["gray"])
    svg += ell(x - 8 * s, y - 15 * s, 30 * s, 5 * s, col, OW * 0.6)
    return svg, (x - 46 * s, y - 20 * s, x + 46 * s, y)


def paw_prints(pts, s_fn, col=None):
    col = col or C["paint"]
    svg = ""
    for i, (x, y) in enumerate(pts):
        s = s_fn(y)
        off = (6 if i % 2 else -6) * s
        svg += ell(x + off, y, 7 * s, 4 * s, col, 0)
        for dx in (-6, 0, 6):
            svg += ell(x + off + dx * s, y - 7 * s, 2.6 * s, 2.0 * s, col, 0)
    return svg


def sprinkler(x, y, s=1.0, toward=1, reach=260, land=None, solid=False):
    """land (v0.17): the point the longest arc comes down on (the soaked box's lid); the two shorter arcs fall on the
    grass short of it. solid (v0.19): unbroken arcs, outlined, with drops breaking off them (dashed arcs read as "a
    dotted trajectory rather than water")."""
    svg = ell(x, y - 6 * s, 20 * s, 8 * s, C["slate"]) + rect(x - 4 * s, y - 34 * s, 8 * s, 28 * s, C["charcoal"], 2 * s)
    svg += circ(x, y - 36 * s, 6 * s, C["gray"], OW * 0.6)
    arcs = ""
    for i, (h, d) in enumerate([(150, 0.75), (190, 1.0), (120, 0.55)]):
        ex, ey = x + toward * reach * d * s, y - 6 * s
        if land is not None:
            if d == 1.0:
                ex, ey = land
            else:
                # (the shorter arcs come down on the grass, a few drops bouncing where they land; ending a little above
                # the ground they "stop in mid-air")
                ex, ey = x + (land[0] - x) * d, y + 4 * s
                arcs += drops(ex, ey - 12 * s, s * 0.7, 2, 14)
        if solid:
            q0, q1, q2 = (x, y - 38 * s), ((x + ex) / 2, y - h * s), (ex, ey)
            d_ = f"M {P(*q0)} Q {P(*q1)} {P(*q2)}"
            arcs += f'<path d="{d_}" fill="none" stroke="{OUT}" stroke-width="{4.2 * s + 2.2:.1f}" stroke-linecap="round"/>'
            arcs += f'<path d="{d_}" fill="none" stroke="{C["water_light"]}" stroke-width="{4.2 * s:.1f}" stroke-linecap="round"/>'
            for t in (0.58, 0.76):
                u = 1 - t
                qx = u * u * q0[0] + 2 * u * t * q1[0] + t * t * q2[0]
                qy = u * u * q0[1] + 2 * u * t * q1[1] + t * t * q2[1]
                arcs += circ(qx + toward * 4 * s, qy - 9 * s, 2.4 * s, C["water_light"], OW * 0.4)
            continue
        arcs += f'<path d="M {P(x, y - 38 * s)} Q {P((x + ex) / 2, y - h * s)} {P(ex, ey)}" fill="none" stroke="{C["water"]}" stroke-width="{3.5 * s + 1:.1f}" stroke-dasharray="{10 * s:.1f} {8 * s:.1f}" stroke-linecap="round"/>'
    far = land[0] if land is not None else x + toward * reach * s
    return svg, arcs, (min(x, far) - 10, y - 200 * s, max(x, far) + 10, y)


def wet_marks(x, y, s=1.0, w=74, h=50):
    """v0.17: a cardboard box being soaked: two drips running down its front, a little water
    splashing off the lid's edges and a puddle at its foot (drops drawn above the lid read as "water coming out of the box")."""
    svg = ""      # (the puddle at its foot is drawn under the box by the template)
    # (no darker wet patches: on the bench the blotches made the box "a hay or straw bale", "a crate", "wood grain")
    # (v0.27: short, from the lid's edge: two lines down its whole front read as slats: "a wooden crate")
    for dx, top, bot in ((-0.30, -0.98, -0.66), (0.22, -0.98, -0.52)):
        svg += f'<path d="M {P(x + dx * w * s, y + top * h * s)} L {P(x + dx * w * s, y + bot * h * s)}" stroke="{C["water_light"]}" stroke-width="{3.2 * s:.1f}" stroke-linecap="round"/>'
        svg += circ(x + dx * w * s, y + bot * h * s + 2 * s, 2.6 * s, C["water_light"], 0)
    # water running off the lid's two front corners
    for side in (-1, 1):
        cx = x + side * (w / 2 + (6 if side > 0 else 0)) * s
        svg += f'<path d="M {P(cx, y - (h + 4) * s)} q {side * 9 * s:.1f} {4 * s:.1f} {side * 11 * s:.1f} {16 * s:.1f}" fill="none" stroke="{C["water"]}" stroke-width="{3 * s:.1f}" stroke-linecap="round" stroke-dasharray="{7 * s:.1f} {5 * s:.1f}"/>'
    return svg


def drops(x, y, s=1.0, n=3, spread=18):
    svg = ""
    for i in range(n):
        dx = (i - (n - 1) / 2) * spread * s
        dy = (i % 2) * 14 * s
        svg += shape(f"M {P(x + dx, y + dy - 9 * s)} Q {P(x + dx + 6 * s, y + dy + 2 * s)} {P(x + dx, y + dy + 5 * s)} Q {P(x + dx - 6 * s, y + dy + 2 * s)} {P(x + dx, y + dy - 9 * s)} Z",
                     C["water_light"], OW * 0.5)
    return svg


def water_stream(p0, direction, s=1.0, length=170, upward=False, spread=0.0, splash=False, solid=False, style=None):
    """A stream leaving p0 along `direction`; it falls under gravity unless `upward` (the contradiction).
    v0.16 styles for falling water: "shower" (a fan of droplet lines from a watering can's rose) and "pour" (a stream
    from a pan's lip, wide at the lip and thinning as it falls, drops breaking off at its end)."""
    dx, dy = direction
    n = math.hypot(dx, dy) or 1
    dx, dy = dx / n, dy / n
    L = length * s
    if style in ("shower", "pour") and not upward:
        c1 = (p0[0] + dx * L * 0.45, p0[1] + dy * L * 0.45)
        end = (p0[0] + dx * L * 0.70, p0[1] + L * 0.85)
        c2 = (end[0] - dx * L * 0.05, end[1] - L * 0.35)
        if style == "pour":
            # poured water leaves the lip and falls almost straight down
            c1 = (p0[0] + dx * L * 0.16, p0[1] + max(0.0, dy) * L * 0.16)
            end = (p0[0] + dx * L * 0.30, p0[1] + L * 0.92)
            c2 = (end[0] - dx * L * 0.02, end[1] - L * 0.55)

        def bez(t, a=p0, b=c1, c=c2, d=end):
            u = 1 - t
            return (u ** 3 * a[0] + 3 * u * u * t * b[0] + 3 * u * t * t * c[0] + t ** 3 * d[0],
                    u ** 3 * a[1] + 3 * u * u * t * b[1] + 3 * u * t * t * c[1] + t ** 3 * d[1])
        svg = ""
        xs, ys = [p0[0], end[0]], [p0[1], end[1]]
        if style == "shower":
            # four lines of round drops fanning out from the rose, each falling under gravity
            for i, off in enumerate((-1.5, -0.5, 0.5, 1.5)):
                e = (end[0] + off * 11 * s, end[1] + abs(off) * 3 * s)
                k1 = (c1[0] + off * 3 * s, c1[1] + off * 2 * s)
                k2 = (c2[0] + off * 8 * s, c2[1])
                d = f"M {P(p0[0] + off * 2 * s, p0[1] + off * 1.5 * s)} C {P(*k1)} {P(*k2)} {P(*e)}"
                # (short streaks rather than dots: lines of round drops read as "a beaded chain or dotted line")
                svg += f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{3.2 * s + 1.6:.1f}" stroke-linecap="round" stroke-dasharray="{9 * s:.1f} {7 * s:.1f}" stroke-dashoffset="{i * 5 * s:.1f}"/>'
                svg += f'<path d="{d}" fill="none" stroke="{C["water_light"]}" stroke-width="{3.2 * s:.1f}" stroke-linecap="round" stroke-dasharray="{9 * s:.1f} {7 * s:.1f}" stroke-dashoffset="{i * 5 * s:.1f}"/>'
                xs.append(e[0]); ys.append(e[1])
            svg += drops(end[0], end[1] - 4 * s, s * 1.0, 3, 16)
        else:
            # a ribbon of water, 8 px wide at the lip and 3 px at its end, with a white glint, and drops breaking off below
            left, right = [], []
            N = 24
            for k in range(N + 1):
                t = k / N
                x0, y0 = bez(t)
                x1, y1 = bez(min(1.0, t + 0.01))
                tx_, ty_ = x1 - x0, y1 - y0
                nn = math.hypot(tx_, ty_) or 1
                nx, ny = -ty_ / nn, tx_ / nn
                w = (12.0 - 8.0 * t) * s / 2
                left.append((x0 + nx * w, y0 + ny * w))
                right.append((x0 - nx * w, y0 - ny * w))
            ribbon = "M " + " L ".join(P(*q) for q in left + right[::-1]) + " Z"
            svg += f'<path d="{ribbon}" fill="{C["water_light"]}" stroke="{OUT}" stroke-width="{OW * 0.55:.1f}" stroke-linejoin="round"/>'
            glint = " ".join(P(*bez(k / 20)) for k in range(1, 13))
            svg += f'<path d="M {glint}" fill="none" stroke="{C["white"]}" stroke-width="{1.8 * s:.1f}" stroke-linecap="round" stroke-opacity="0.85"/>'
            svg += drops(end[0], end[1] + 8 * s, s * 1.0, 3, 14)
        return svg, (min(xs) - 22 * s, min(ys) - 22 * s, max(xs) + 22 * s, max(ys) + 26 * s), end
    if style == "jet" and not upward:
        # v0.19 (revision 17): a hose's jet: an unbroken ribbon of water, wide at the nozzle and thinning as it arcs down,
        # with a white glint and drops breaking off its last third (dashed, it read as "a dashed line with gaps (could
        # read as a dotted line)"; one even-width line had read as "a solid bent tube")
        c1 = (p0[0] + dx * L * 0.45, p0[1] + dy * L * 0.45)
        end = (p0[0] + dx * L * 0.70, p0[1] + L * 0.85)
        c2 = (end[0] - dx * L * 0.05, end[1] - L * 0.35)

        def bez(t, a=p0, b=c1, c=c2, d=end):
            u = 1 - t
            return (u ** 3 * a[0] + 3 * u * u * t * b[0] + 3 * u * t * t * c[0] + t ** 3 * d[0],
                    u ** 3 * a[1] + 3 * u * u * t * b[1] + 3 * u * t * t * c[1] + t ** 3 * d[1])
        left, right = [], []
        N = 28
        for k in range(N + 1):
            t = k / N
            x0, y0 = bez(t)
            x1, y1 = bez(min(1.0, t + 0.01))
            tx_, ty_ = x1 - x0, y1 - y0
            nn = math.hypot(tx_, ty_) or 1
            nx, ny = -ty_ / nn, tx_ / nn
            # (widening as it goes, as a jet spreads: one even thin line read as "a thin second tube or wire")
            w = (8.0 + 6.0 * t) * s / 2
            left.append((x0 + nx * w, y0 + ny * w))
            right.append((x0 - nx * w, y0 - ny * w))
        ribbon = "M " + " L ".join(P(*q) for q in left + right[::-1]) + " Z"
        svg = f'<path d="{ribbon}" fill="{C["water_light"]}" stroke="{OUT}" stroke-width="{OW * 0.55:.1f}" stroke-linejoin="round"/>'
        glint = " ".join(P(*bez(k / 24)) for k in range(1, 16))
        svg += f'<path d="M {glint}" fill="none" stroke="{C["white"]}" stroke-width="{1.8 * s:.1f}" stroke-linecap="round" stroke-opacity="0.85"/>'
        # drops spraying off both sides of the arc's second half
        for t, off, side in ((0.48, 11, 1), (0.58, 13, -1), (0.66, 14, 1), (0.76, 15, -1), (0.84, 15, 1), (0.92, 14, -1)):
            x0, y0 = bez(t)
            x1, y1 = bez(t + 0.01)
            nn = math.hypot(x1 - x0, y1 - y0) or 1
            nx, ny = -(y1 - y0) / nn, (x1 - x0) / nn
            if ny > 0:
                nx, ny = -nx, -ny
            svg += circ(x0 + side * nx * off * s, y0 + side * ny * off * s, 2.8 * s, C["water_light"], OW * 0.45)
        svg += drops(end[0], end[1] + (-10 if splash else 12) * s, s * 1.2, 3, 18)
        xs = [p0[0], c1[0], c2[0], end[0]]
        ys = [p0[1], c1[1], c2[1], end[1]]
        return svg, (min(xs) - 16, min(ys) - 22 * s, max(xs) + 16, max(ys) + 22 * s), end
    if upward and solid:
        # v0.10: the water leaves the spout already rising, like a pour turned upside down (starting
        # down toward the flowers and curving up, it read as a spray arcing over them)
        c1 = (p0[0] + dx * L * 0.30, p0[1] - L * 0.08)
        c2 = (p0[0] + dx * L * 0.48, p0[1] - L * 0.42)
        end = (p0[0] + dx * L * 0.50, p0[1] - L * 0.78)
    elif upward:
        c1 = (p0[0] + dx * L * 0.35, p0[1] + dy * L * 0.35)
        end = (p0[0] + dx * L * 0.55, p0[1] - L * 0.75)
        c2 = (end[0] + dx * L * 0.05, end[1] + L * 0.25)
    else:
        c1 = (p0[0] + dx * L * 0.45, p0[1] + dy * L * 0.45)
        end = (p0[0] + dx * L * 0.70, p0[1] + L * 0.85)
        c2 = (end[0] - dx * L * 0.05, end[1] - L * 0.35)
    d = f"M {P(*p0)} C {P(*c1)} {P(*c2)} {P(*end)}"
    if solid:
        # v0.10: one unbroken stream (the dashed upward stream read as "a string of beads")
        svg = f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{9 * s + 4:.1f}" stroke-linecap="round"/>'
        svg += f'<path d="{d}" fill="none" stroke="{C["water_light"]}" stroke-width="{9 * s:.1f}" stroke-linecap="round"/>'
        svg += f'<path d="{d}" fill="none" stroke="{C["white"]}" stroke-width="{2.5 * s:.1f}" stroke-linecap="round" stroke-opacity="0.85"/>'
        svg += drops(end[0], end[1] + (-18 if upward else (-10 if splash else 12)) * s, s * 1.2, 3, 18)
        xs = [p0[0], c1[0], c2[0], end[0]]
        ys = [p0[1], c1[1], c2[1], end[1]]
        return svg, (min(xs) - 12, min(ys) - 22 * s, max(xs) + 12, max(ys) + 22 * s), end
    # broken stream: short outlined dashes with gaps, plus a light core, so it reads as falling water
    svg = f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{9 * s + 4:.1f}" stroke-linecap="round" stroke-dasharray="{20 * s:.1f} {11 * s:.1f}"/>'
    svg += f'<path d="{d}" fill="none" stroke="{C["water_light"]}" stroke-width="{9 * s:.1f}" stroke-linecap="round" stroke-dasharray="{20 * s:.1f} {11 * s:.1f}"/>'
    svg += f'<path d="{d}" fill="none" stroke="{C["white"]}" stroke-width="{2.5 * s:.1f}" stroke-dasharray="{8 * s:.1f} {23 * s:.1f}" stroke-linecap="round" stroke-opacity="0.9"/>'
    svg += drops(end[0], end[1] + (-18 if upward else (-10 if splash else 12)) * s, s * 1.2, 3, 18)
    xs = [p0[0], c1[0], c2[0], end[0]]
    ys = [p0[1], c1[1], c2[1], end[1]]
    return svg, (min(xs) - 12, min(ys) - 22 * s, max(xs) + 12, max(ys) + 22 * s), end


def dirt_heap(x, y, s=1.0, w=50, h=46):
    """v0.27: a lumpy heap of dug soil with clods at its foot (one smooth curve read as "a neat flat-bottomed dome", "a thin brown arch")."""
    W, H_ = w * s, h * s
    d = (f"M {P(x - W, y)} Q {P(x - W * 0.86, y - H_ * 0.42)} {P(x - W * 0.52, y - H_ * 0.52)} Q {P(x - W * 0.40, y - H_ * 1.0)} {P(x - W * 0.02, y - H_ * 0.98)} "
         f"Q {P(x + W * 0.36, y - H_ * 0.96)} {P(x + W * 0.46, y - H_ * 0.56)} Q {P(x + W * 0.86, y - H_ * 0.46)} {P(x + W, y)} Z")
    svg = shape(d, C["soil"])
    svg += f'<path d="M {P(x - W * 0.30, y - H_ * 0.58)} q {W * 0.14:.1f} {-H_ * 0.14:.1f} {W * 0.30:.1f} {-H_ * 0.05:.1f} M {P(x + W * 0.02, y - H_ * 0.28)} q {W * 0.16:.1f} {-H_ * 0.10:.1f} {W * 0.30:.1f} {H_ * 0.02:.1f}" fill="none" stroke="{OUT}" stroke-width="{1.8 * s + 0.4:.1f}" stroke-linecap="round"/>'
    for dx, dy, r in ((-1.04, -0.03, 5.0), (1.06, -0.05, 5.5), (0.70, 0.03, 4.0), (-0.62, 0.04, 3.6)):
        svg += circ(x + dx * W, y + dy * H_, r * s, C["soil"], OW * 0.55)
    return svg


def dustpan(x, y, s=1.0, f=1, col=None):
    """v0.10: a dustpan lying on the ground, its open lip facing -f (toward the swept heap), its short
    handle toward +f."""
    col = col or C["red"]
    lip, back = x - f * 22 * s, x + f * 14 * s
    svg = poly([(lip, y + 2 * s), (lip, y - 5 * s), (back, y - 16 * s), (back, y + 2 * s)], col, OW * 0.8)
    svg += poly([(back, y - 13 * s), (back + f * 30 * s, y - 20 * s), (back + f * 31 * s, y - 15 * s), (back, y - 7 * s)], col, OW * 0.7)
    svg += line(lip + f * 3 * s, y - 1 * s, back - f * 2 * s, y - 1 * s, OUT, 1.6 * s)
    xs = (lip, back + f * 31 * s)
    return svg, (min(xs) - 2, y - 22 * s, max(xs) + 2, y + 4 * s)


def hose_tail(pts, start, s=1.0, col=None):
    """v0.30: the last of a hose_through from point `start` on, to draw over a figure: the same curve, its fill starting a point further back than its edge, so no seam crosses the hose."""
    col = col or C["hose"]

    def d_from(k):
        d = "M " + P(*pts[k])
        for i in range(k, len(pts) - 1):
            p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, len(pts) - 1)]
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            d += f" C {P(*c1)} {P(*c2)} {P(*p2)}"
        return d
    w, ow = 9 * s, OW * 0.8
    return (f'<path d="{d_from(start)}" fill="none" stroke="{OUT}" stroke-width="{w + 2 * ow:.1f}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d_from(start - 1)}" fill="none" stroke="{col}" stroke-width="{w:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')


def hose_through(pts, s=1.0, col=None):
    """v0.29: a hose as a smooth curve through the points (each piece of hose_path bends to a point of its own, so a slack run came out as one tight arc)."""
    col = col or C["hose"]
    d = "M " + P(*pts[0])
    for i in range(len(pts) - 1):
        p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, len(pts) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C {P(*c1)} {P(*c2)} {P(*p2)}"
    return stroke(d, col, 9 * s, OW * 0.8)


def hose_path(pts, s=1.0, col=None):
    col = col or C["hose"]
    d = "M " + P(*pts[0])
    for i in range(1, len(pts) - 1, 2):
        d += f" Q {P(*pts[i])} {P(*pts[i + 1])}"
    return stroke(d, col, 9 * s, OW * 0.8)


def facade(x0, x1, top, base, wall, trim, awning=None, door_at=0.5, windows=2, roof=None):
    """Front of a small two-storey building; no text anywhere."""
    w = x1 - x0
    svg = rect(x0, top, w, base - top, wall, 0)
    svg += rect(x0 - 6, top - 14, w + 12, 18, roof or trim, 2)
    h = base - top
    # upper windows: plain panes (v0.5 simplified the facades so the street is no busier than the park)
    for i in range(windows):
        wx = x0 + w * (i + 0.5) / windows - 34
        wy = top + h * 0.12
        svg += rect(wx, wy, 68, 76, C["glass"], 3)
    # shop window + door
    dx = x0 + w * door_at
    svg += rect(dx - 30, base - 128, 60, 128, trim, 3)
    svg += circ(dx + 18, base - 62, 4.5, C["yellow"], OW * 0.6)
    sw0 = x0 + 18 if door_at > 0.5 else dx + 46
    sw1 = dx - 46 if door_at > 0.5 else x1 - 18
    if sw1 - sw0 > 60:
        svg += rect(sw0, base - 118, sw1 - sw0, 88, C["glass"], 3) + rect(sw0 - 4, base - 30, sw1 - sw0 + 8, 10, trim, 2, OW * 0.8)
    if awning:
        ay = base - 150
        n = max(3, int(w / 84))
        aw = (w + 16) / n
        for i in range(n):
            col = awning if i % 2 == 0 else C["white"]
            svg += poly([(x0 - 8 + i * aw, ay), (x0 - 8 + (i + 1) * aw, ay), (x0 - 8 + (i + 1) * aw + 6, ay + 34), (x0 - 8 + i * aw + 6, ay + 34)], col, OW * 0.8)
    return svg


def fruit_stall(x, base_y, s=1.0):
    w = 260 * s
    top = base_y - 96 * s
    svg = rect(x - w / 2 + 10 * s, base_y - 70 * s, 12 * s, 70 * s, C["wood"], 2 * s) + rect(x + w / 2 - 22 * s, base_y - 70 * s, 12 * s, 70 * s, C["wood"], 2 * s)
    svg += rect(x - w / 2, top, w, 30 * s, C["wood_light"], 3 * s)
    cols = [C["red"], C["orange"], C["yellow"], C["green"]]
    for i in range(4):
        cx = x - w / 2 + (i + 0.5) * w / 4
        svg += rect(cx - 28 * s, top - 22 * s, 56 * s, 24 * s, C["tan"], 2 * s, OW * 0.8)
        for j in range(5):
            svg += circ(cx - 20 * s + j * 10 * s, top - 24 * s - (j % 2) * 7 * s, 8 * s, cols[i], OW * 0.6)
    # awning poles + canopy
    svg += rect(x - w / 2 - 4 * s, top - 140 * s, 8 * s, 140 * s, C["charcoal"], 2 * s) + rect(x + w / 2 - 4 * s, top - 140 * s, 8 * s, 140 * s, C["charcoal"], 2 * s)
    n = 6
    for i in range(n):
        col = C["teal"] if i % 2 == 0 else C["white"]
        svg += poly([(x - w / 2 - 14 * s + i * (w + 28 * s) / n, top - 150 * s), (x - w / 2 - 14 * s + (i + 1) * (w + 28 * s) / n, top - 150 * s),
                     (x - w / 2 - 14 * s + (i + 1) * (w + 28 * s) / n, top - 118 * s), (x - w / 2 - 14 * s + i * (w + 28 * s) / n, top - 118 * s)], col, OW * 0.8)
    return svg, {"counter_y": top - 24 * s, "bbox": (x - w / 2 - 16 * s, top - 152 * s, x + w / 2 + 16 * s, base_y)}


def cafe_chair(x, y, s=1.0, f=1):
    """Bistro chair seen from the side; f = +1 back on the right."""
    svg = stroke(poly_d([(x - f * 18 * s, y), (x - f * 16 * s, y - 44 * s)]), C["charcoal"], 4 * s, OW * 0.7)
    svg += stroke(poly_d([(x + f * 16 * s, y), (x + f * 16 * s, y - 92 * s)]), C["charcoal"], 4 * s, OW * 0.7)
    svg += rect(x - 22 * s, y - 50 * s, 44 * s, 8 * s, C["charcoal"], 2 * s, OW * 0.7)
    svg += rect(x + f * 10 * s - 5 * s, y - 92 * s, 10 * s, 42 * s, C["charcoal"], 2 * s, OW * 0.7)
    return svg


def cafe_table(x, y, s=1.0):
    svg = cafe_chair(x - 62 * s, y + 4 * s, s, -1) + cafe_chair(x + 62 * s, y + 4 * s, s, 1)
    svg += rect(x - 4 * s, y - 70 * s, 8 * s, 70 * s, C["charcoal"], 2 * s) + ell(x, y - 2 * s, 22 * s, 6 * s, C["charcoal"], OW * 0.7)
    svg += ell(x, y - 72 * s, 46 * s, 10 * s, C["white"])
    # v0.7: no cup on the empty table (a cup with nobody there read as someone gone missing)
    return svg, (x - 86 * s, y - 84 * s, x + 86 * s, y + 4 * s)


def tree_planter(x, y, s=1.0):
    """Raised round planter the street tree grows from (not a dark hole in the paving)."""
    svg = rect(x - 64 * s, y - 26 * s, 128 * s, 26 * s, C["slate"], 4 * s)
    svg += ell(x, y - 26 * s, 64 * s, 15 * s, C["soil"])
    return svg


def rock(x, y, s=1.0):
    d = f"M {P(x - 46 * s, y)} Q {P(x - 50 * s, y - 26 * s)} {P(x - 18 * s, y - 40 * s)} Q {P(x + 14 * s, y - 50 * s)} {P(x + 38 * s, y - 28 * s)} Q {P(x + 52 * s, y - 8 * s)} {P(x + 40 * s, y)} Z"
    svg = shape(d, C["rock"])
    svg += f'<path d="M {P(x - 26 * s, y - 28 * s)} Q {P(x - 8 * s, y - 38 * s)} {P(x + 12 * s, y - 34 * s)}" fill="none" stroke="{C["white"]}" stroke-width="{4 * s:.1f}" stroke-linecap="round" stroke-opacity="0.8"/>'
    svg += f'<path d="M {P(x + 6 * s, y)} Q {P(x + 18 * s, y - 14 * s)} {P(x + 36 * s, y - 16 * s)}" fill="none" stroke="{C["rock_dark"]}" stroke-width="{3 * s:.1f}"/>'
    return svg, (x - 52 * s, y - 50 * s, x + 52 * s, y + 2)


def laundry_basket(x, y, s=1.0, cloth=False):
    """Wicker basket with folded clothes heaped in it. cloth (v0.38, the hanger's basket only): a fold drawn in each bundle and a sleeve hanging
    over the front rim (the smooth bundles were "balls or cushions" to three bench readers of six)."""
    svg = ""
    for dx, col in ((-24, C["blue"]), (4, C["white"]), (28, C["pink"])):
        svg += ell(x + dx * s, y - 50 * s, 24 * s, 14 * s, col, OW * 0.8)
        if cloth:
            svg += f'<path d="M {P(x + (dx - 14) * s, y - 52 * s)} Q {P(x + dx * s, y - 58 * s)} {P(x + (dx + 13) * s, y - 50 * s)}" fill="none" stroke="{OUT}" stroke-width="{1.6 * s:.1f}" stroke-linecap="round"/>'
    svg += shape(f"M {P(x - 50 * s, y - 46 * s)} L {P(x + 50 * s, y - 46 * s)} L {P(x + 40 * s, y)} L {P(x - 40 * s, y)} Z", "#c99a5a")
    for k in (1, 2):
        svg += line(x - 48 * s + k * 2, y - 46 * s + k * 15 * s, x + 48 * s - k * 2, y - 46 * s + k * 15 * s, "#a87a3c", 3 * s)
    if cloth:
        # a sleeve of the blue bundle over the rim, its cuff down the basket's front
        svg += shape(f"M {P(x - 30 * s, y - 49 * s)} Q {P(x - 22 * s, y - 40 * s)} {P(x - 25 * s, y - 24 * s)} L {P(x - 13 * s, y - 23 * s)} "
                     f"Q {P(x - 10 * s, y - 40 * s)} {P(x - 16 * s, y - 50 * s)} Z", C["blue"], OW * 0.8)
        svg += line(x - 25.5 * s, y - 28 * s, x - 12.5 * s, y - 27 * s, OUT, 1.4 * s)
        # and a drop forming at its cuff: the washing in the basket is wet too (under the dripping shirt, dry-looking clothes read as "about to get wet")
        svg += drop(x - 19 * s, y - 23.5 * s, s, forming=True)
    return svg, (x - 54 * s, y - 66 * s, x + 54 * s, y)


def drop(x, y, s=1.0, forming=False):
    """v0.38: a water drop under wet washing; forming hangs from the hem or cuff at (x, y), otherwise it falls, centred at (x, y)."""
    if forming:
        return shape(f"M {P(x - 3 * s, y - 1 * s)} Q {P(x - 1.5 * s, y + 5 * s)} {P(x - 4.2 * s, y + 8 * s)} "
                     f"Q {P(x, y + 13 * s)} {P(x + 4.2 * s, y + 8 * s)} Q {P(x + 1.5 * s, y + 5 * s)} {P(x + 3 * s, y - 1 * s)} Z", C["water_light"], OW * 0.5)
    return shape(f"M {P(x, y - 6 * s)} Q {P(x + 4.5 * s, y + 1 * s)} {P(x, y + 4 * s)} Q {P(x - 4.5 * s, y + 1 * s)} {P(x, y - 6 * s)} Z", C["water_light"], OW * 0.5)


def blowing_leaves(x0, y0, x1, y1, s=1.0, n=4):
    """A few leaves tumbling along with the wind lines."""
    svg = ""
    for i in range(n):
        t = (i + 0.5) / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t + (12 if i % 2 else -12) * s
        svg += ell(x, y, 9 * s, 4.5 * s, [C["leaf_green"], C["grass_dark"], C["leaf_brown"]][i % 3], OW * 0.5, rot=30 + 50 * i)
    return svg


def pond(cx, cy, rx, ry):
    svg = ell(cx, cy, rx, ry, C["pond"])
    svg += f'<ellipse cx="{cx - rx * 0.25:.1f}" cy="{cy - ry * 0.25:.1f}" rx="{rx * 0.35:.1f}" ry="{ry * 0.18:.1f}" fill="{C["water_light"]}"/>'
    svg += f'<ellipse cx="{cx + rx * 0.35:.1f}" cy="{cy + ry * 0.25:.1f}" rx="{rx * 0.22:.1f}" ry="{ry * 0.12:.1f}" fill="{C["water_light"]}"/>'
    for i, (dx, h) in enumerate([(-0.92, 50), (-0.86, 38), (0.88, 46), (0.93, 34)]):
        x = cx + dx * rx
        y = cy + ry * 0.25
        svg += stroke(poly_d([(x, y), (x + (i - 1.5) * 3, y - h)]), C["grass_dark"], 5, OW * 0.6)
        svg += ell(x + (i - 1.5) * 3, y - h, 4, 10, C["brown"], OW * 0.6)
    return svg


def hills(y, col=None):
    col = col or C["hill"]
    d = f"M -10 {y + 40} Q 200 {y - 70} 420 {y + 10} Q 640 {y - 60} 900 {y + 15} Q 1150 {y - 80} 1350 {y} Q 1480 {y - 40} 1610 {y + 10} L 1610 {y + 80} L -10 {y + 80} Z"
    return shape(d, col, OW * 0.8)


def tree_line(y, x0=-20, x1=1620, step=70):
    parts = []
    x = x0
    i = 0
    while x < x1:
        r = 46 + (i * 17) % 22
        parts.append((x, y - r * 0.6, r))
        x += step
        i += 1
    return blob(parts, "#5aa35a", OW * 0.8)


# ----------------------------------------------------------------- playground
def railing(y_top, y_base, x0=-10, x1=1610, step=58, col=None, mids=None):
    """Metal railing along the back of the playground (v0.16: `mids` gives the heights of the lower rails as fractions
    of the railing, for the taller railing)."""
    col = col or C["slate"]
    svg = ""
    x = x0 + 20
    while x < x1:
        svg += rect(x - 4, y_top, 8, y_base - y_top, col, 2, OW * 0.7)
        x += step
    svg += rect(x0, y_top - 6, x1 - x0, 11, col, 3, OW * 0.8)
    for f in (mids or (0.55,)):
        svg += rect(x0, y_top + (y_base - y_top) * f, x1 - x0, 8, col, 2, OW * 0.7)
    return svg


def slide(x, base_y, s=1.0, f=1, ladder2=False):
    """Playground slide seen from the side: ladder at x, platform, chute running down toward +f."""
    h = 230 * s              # platform height
    pw = 70 * s              # platform width
    lx0, lx1 = x - f * 46 * s, x
    top = base_y - h
    svg = ""
    # chute (behind the near rail)
    cx0, cx1 = x + f * pw, x + f * (pw + 260 * s)
    chute = [(cx0, top - 4 * s), (cx1, base_y - 26 * s), (cx1 + f * 34 * s, base_y - 22 * s), (cx1 + f * 34 * s, base_y - 10 * s),
             (cx1, base_y - 12 * s), (cx0, top + 14 * s)]
    svg += poly(chute, C["yellow"])
    svg += stroke(poly_d([(cx0, top - 16 * s), (cx1, base_y - 38 * s), (cx1 + f * 30 * s, base_y - 34 * s)]), C["orange"], 7 * s, OW * 0.7)
    # platform posts and deck
    for px in (x, x + f * pw):
        svg += rect(px - 6 * s, top, 12 * s, h, C["red"], 2 * s, OW * 0.8)
    if ladder2:
        # v0.12: one ladder leaning on the platform end, both rails parallel and tucked under the deck,
        # hand-hooks curling over it (the rails crossing the post read as "doubled ... detached")
        b0, b1 = x - f * 64 * s, x - f * 44 * s
        t0, t1 = x - f * 14 * s, x + f * 6 * s
        for (bx, tx) in ((b0, t0), (b1, t1)):
            svg += stroke(poly_d([(bx, base_y), (tx, top + 2 * s)]), C["slate"], 7 * s, OW * 0.7)
        for k in range(1, 6):
            t = k / 6
            ax, ay = b0 + (t0 - b0) * t, base_y + (top + 2 * s - base_y) * t
            svg += line(ax, ay, ax + (b1 - b0), ay, OUT, 4 * s)
        for tx in (t0, t1):
            svg += stroke(f"M {P(tx, top + 2 * s)} Q {P(tx - f * 4 * s, top - 34 * s)} {P(tx + f * 12 * s, top - 30 * s)}", C["slate"], 6 * s, OW * 0.7)
    svg += rect(min(x, x + f * pw) - 8 * s, top - 10 * s, pw + 16 * s, 14 * s, C["blue"], 3 * s)
    # safety rail
    svg += stroke(poly_d([(x, top - 10 * s), (x, top - 58 * s), (x + f * pw, top - 58 * s), (x + f * pw, top - 10 * s)]), C["red"], 7 * s, OW * 0.7)
    # ladder
    if not ladder2:
        svg += stroke(poly_d([(lx0, base_y), (lx1 - f * 4 * s, top)]), C["slate"], 7 * s, OW * 0.7)
        svg += stroke(poly_d([(lx0 + f * 16 * s, base_y), (lx1 + f * 12 * s, top)]), C["slate"], 7 * s, OW * 0.7)
        for k in range(1, 6):
            t = k / 6
            ax, ay = lx0 + (lx1 - f * 4 * s - lx0) * t, base_y - h * t
            svg += line(ax, ay, ax + f * 16 * s, ay, OUT, 4 * s)
    xs = [lx0 - 10 * s, cx1 + f * 40 * s] if not ladder2 else [x - f * 74 * s, cx1 + f * 40 * s]
    info = {"platform": (x + f * pw / 2, top - 10 * s), "bottom": (cx1 + f * 50 * s, base_y), "depth": base_y,
            "chute": ((cx0, top - 4 * s), (cx1, base_y - 26 * s)),
            "bbox": (min(xs), top - 62 * s, max(xs), base_y)}
    return svg, info


# v0.28 bench (isolation_v028.md): riders this far in from the plank's end ("sitting very near the end of the plank, almost past it"), 0 before
SEESAW_IN28 = 22


def seesaw(cx, base_y, s=1.0, tilt=0.0, L=212, inset=0, ground=False, pad=False, up=(0, 0)):
    """Seesaw on a pivot; tilt > 0 lifts the right end. Returns svg and the two seat points.
    inset (v0.28) moves the seats and handles in from the plank's ends; ground (v0.28) casts one shadow under the whole plank, for the riders too.
    up (v0.32): how much taller each end's handle stands, in units (left, right), for a rider raised onto the plank who grips it."""
    ph = 82 * s
    a = math.radians(tilt)
    dx, dy = math.cos(a) * L * s, -math.sin(a) * L * s
    pv = (cx, base_y - ph)
    left, right = (pv[0] - dx, pv[1] - dy), (pv[0] + dx, pv[1] + dy)
    svg = f'<ellipse cx="{cx:.1f}" cy="{base_y + 2:.1f}" rx="{abs(dx) * 1.04:.1f}" ry="{13 * s:.1f}" fill="{OUT}" fill-opacity="0.16"/>' if ground else ""
    svg += poly([(cx - 34 * s, base_y), (cx + 34 * s, base_y), (cx + 8 * s, base_y - ph), (cx - 8 * s, base_y - ph)], C["slate"])
    svg += stroke(poly_d([left, right]), C["red"], 14 * s, OW * 0.8)
    seats = {}
    for name, (x, y), sg in (("left", left, 1), ("right", right, -1)):
        x, y = x + sg * inset * s * math.cos(a), y - sg * inset * s * math.sin(a)
        hx, hy = x + sg * 34 * s * math.cos(a), y - sg * 34 * s * math.sin(a)
        ht = 42 + (up[0] if name == "left" else up[1])
        svg += stroke(poly_d([(hx, hy - 6 * s), (hx, hy - ht * s)]), C["charcoal"], 6 * s, OW * 0.7)
        svg += stroke(poly_d([(hx - 9 * s, hy - ht * s), (hx + 9 * s, hy - ht * s)]), C["charcoal"], 6 * s, OW * 0.7)
        if pad:
            # (v0.31 bench) a seat on the plank, under the rider
            nx_, ny_ = -math.sin(a) * 9 * s, -math.cos(a) * 9 * s
            p0_ = (x - sg * 6 * s * math.cos(a) + nx_, y + sg * 6 * s * math.sin(a) + ny_)
            p1_ = (x + sg * 28 * s * math.cos(a) + nx_, y - sg * 28 * s * math.sin(a) + ny_)
            svg += stroke(poly_d([p0_, p1_]), C["wood"], 9 * s, OW * 0.7)
        seats[name] = (x + sg * 8 * s, y - 6 * s)
        seats[name + "_handle"] = (hx, hy - ht * s)
    svg += circ(pv[0], pv[1], 8 * s, C["gray"], OW * 0.7)
    ys = [left[1], right[1], base_y]
    return svg, {"seats": seats, "bbox": (cx - dx - 20 * s, min(ys) - (50 + max(up)) * s, cx + dx + 20 * s, base_y), "pivot": pv}


def sandbox(cx, cy, s=1.0, w=330, d=88):
    """Wooden sandbox in perspective."""
    w, d = w * s, d * s
    top = [(cx - w / 2 + 40 * s, cy - d), (cx + w / 2 - 40 * s, cy - d), (cx + w / 2, cy), (cx - w / 2, cy)]
    svg = poly(top, C["wood"])
    inner = [(cx - w / 2 + 52 * s, cy - d + 10 * s), (cx + w / 2 - 52 * s, cy - d + 10 * s), (cx + w / 2 - 16 * s, cy - 10 * s), (cx - w / 2 + 16 * s, cy - 10 * s)]
    svg += poly(inner, C["sand"], OW * 0.7)
    svg += rect(cx - w / 2, cy, w, 18 * s, C["wood_light"], 2 * s)
    return svg, {"center": (cx, cy - d / 2), "inner": inner, "bbox": (cx - w / 2, cy - d, cx + w / 2, cy + 18 * s)}


# v0.26 bench: what the sweeper has swept (all four v0.25 pictures of `sweep` had "no visible rubbish or leaf pile for the old man
# to sweep"): "A" a heap of leaves at the broom's head, "B" a heap of dust and grit, "O" nothing. v0.26: A, on the bench
# (isolation_v026.md: "sweeping up leaves"; B was "a dustpan-like shape", "a small rock or mound")
SWEEP26 = "A"
# v0.35 bench: the swing swung out ("O" hanging straight, as v0.34; "S" 8 and "T" 12 degrees, in a wider frame)
SWING35 = "T"           # chosen on the v0.35 bench (vision/isolation_v035.md)


# v0.39 (revision 37, vision/flaws_v038.md O1): the broom's heap for summer. "A" autumn leaves as v0.38 ("a small seasonal inconsistency", seven
# pictures from five readers in v0.38), "S" cut grass, twigs and a few brown leaves, "B" grit and dust as the fork's. By the bench (isolation_v039.md).
HEAP39 = "S"
# v0.40 (revision 38, vision/flaws_v039.md O1): "S" v0.39's heap ("Some of the raked leaves are green rather than brown or autumn-coloured, which looks
# a little odd for raked fallen leaves", five pictures from four readers), "D" dry leaves and twigs, no green, "G" cut grass. By the bench.
HEAP40 = "D"


def leaf(cx, cy, L, W, rot, fill):
    """v0.40: a leaf, pointed at both ends, with a midrib and a short stalk, centred at (cx, cy), length L, width W, turned rot degrees."""
    r = math.radians(rot)
    ux, uy = math.cos(r), math.sin(r)
    vx, vy = -uy, ux
    tip = (cx + ux * L / 2, cy + uy * L / 2)
    base = (cx - ux * L / 2, cy - uy * L / 2)
    c1 = (cx + vx * W * 2, cy + vy * W * 2)      # (a quadratic's control point at 2W gives the leaf a half-width of W)
    c2 = (cx - vx * W * 2, cy - vy * W * 2)
    stalk = (base[0] - ux * L * 0.22, base[1] - uy * L * 0.22)
    svg = (f'<path d="M {P(*base)} Q {P(*c1)} {P(*tip)} Q {P(*c2)} {P(*base)} Z" fill="{fill}" stroke="{OUT}" stroke-width="{OW * 0.45:.1f}" stroke-linejoin="round"/>'
           f'<path d="M {P(*stalk)} L {P(*tip)}" stroke="{OUT}" stroke-width="{OW * 0.35:.1f}" stroke-opacity="0.8" stroke-linecap="round"/>')
    return svg


def sweep_heap(x, y, s=1.0, f=1, style="A"):
    """A small heap ahead of the broom's head, on the ground at y."""
    bb = (x - 40 * s, y - 34 * s, x + 40 * s, y + 6 * s)
    if style == "D":
        # v0.40: dry leaves and twigs, browns and tans with one yellowed leaf, no green; each leaf pointed with a midrib and a stalk (as ovals
        # they were "seeds, nuts, beans", "peanuts", "wood chips" on the bench)
        svg = ""
        cols = (C["leaf_brown"], C["khaki"], C["tan"], C["brown"], C["wood_light"], C["leaf_brown"],
                C["khaki"], C["wood"], C["leaf_brown"], C["tan"], C["khaki"], C["brown"])
        pts = ((-30, 0, 12), (-14, 1, -28), (2, 2, 18), (18, 1, -14), (32, 0, 30), (-22, -8, -20), (-6, -9, 24), (10, -9, -34), (24, -7, 10), (-11, -17, 8), (6, -18, -18), (-2, -26, 30))
        for (dx, dy, rot), c in zip(pts, cols):
            svg += leaf(x + dx * s, y + dy * s, 17 * s, 3.8 * s, rot, c)
        for (ax, ay, bx_, by_) in ((-26, -6, -6, -14), (4, -4, 26, -12), (-10, -20, 8, -22), (-32, 1, -18, -4)):
            svg += stroke(poly_d([(x + ax * s, y + ay * s), (x + bx_ * s, y + by_ * s)]), C["brown"], 2.2 * s, OW * 0.4)
        return svg, bb
    if style == "G":
        # v0.40: cut grass, a low mound of clippings with short blades across it
        svg = (f'<path d="M {P(x - 38 * s, y + 3 * s)} Q {P(x - 30 * s, y - 20 * s)} {P(x - 6 * s, y - 24 * s)} Q {P(x + 20 * s, y - 26 * s)} {P(x + 38 * s, y + 3 * s)} Z" '
               f'fill="{C["leaf_green"]}" stroke="{OUT}" stroke-width="{OW * 0.6:.1f}" stroke-linejoin="round"/>')
        for k, (dx, dy, ang) in enumerate(((-28, -2, 20), (-20, -10, -35), (-12, -4, 60), (-6, -17, 10), (2, -8, -50), (8, -19, 35), (14, -3, -15),
                                           (20, -13, 55), (27, -4, -40), (-16, -16, -70), (12, -12, 80), (-2, -1, 25))):
            r = math.radians(ang)
            ux, uy = math.cos(r) * 6 * s, math.sin(r) * 6 * s
            svg += f'<path d="M {P(x + dx * s - ux, y + dy * s - uy)} L {P(x + dx * s + ux, y + dy * s + uy)}" stroke="{C["grass_dark"] if k % 2 else C["green"]}" stroke-width="{2.0 * s:.1f}" stroke-linecap="round"/>'
        return svg, bb
    if style == "S":
        svg = ""
        cols = (C["leaf_green"], C["grass_dark"], C["khaki"], C["leaf_green"], C["leaf_brown"], C["grass_dark"],
                C["leaf_green"], C["khaki"], C["grass_dark"], C["leaf_green"], C["leaf_brown"], C["grass_dark"])
        pts = ((-30, 0, 12), (-14, 1, -28), (2, 2, 18), (18, 1, -14), (32, 0, 30), (-22, -8, -20), (-6, -9, 24), (10, -9, -34), (24, -7, 10), (-11, -17, 8), (6, -18, -18), (-2, -26, 30))
        for (dx, dy, rot), c in zip(pts, cols):
            svg += f'<ellipse cx="{x + dx * s:.1f}" cy="{y + dy * s:.1f}" rx="{10 * s:.1f}" ry="{4.6 * s:.1f}" fill="{c}" stroke="{OUT}" stroke-width="{OW * 0.45:.1f}" ' \
                   f'transform="rotate({rot} {x + dx * s:.1f} {y + dy * s:.1f})"/>'
        for (ax, ay, bx_, by_) in ((-26, -6, -6, -14), (4, -4, 26, -12), (-10, -20, 8, -22)):
            svg += stroke(poly_d([(x + ax * s, y + ay * s), (x + bx_ * s, y + by_ * s)]), C["brown"], 2.2 * s, OW * 0.4)
        return svg, bb
    if style == "B":
        svg = (f'<path d="M {P(x - 36 * s, y + 3 * s)} q {36 * s:.1f} {-48 * s:.1f} {72 * s:.1f} 0 z" fill="{C["gray"]}" '
               f'stroke="{OUT}" stroke-width="{OW * 0.6:.1f}" stroke-linejoin="round"/>')
        for k, (dx, dy) in enumerate(((-18, -2), (-9, -9), (2, -5), (11, -11), (20, -2), (-1, 0), (9, 1), (-25, 1), (-3, -16), (5, -19))):
            svg += f'<circle cx="{x + dx * s:.1f}" cy="{y + dy * s:.1f}" r="{(1.6 + (k % 3) * 0.6) * s:.1f}" fill="{C["brown"] if k % 2 else C["charcoal"]}"/>'
        return svg, bb
    svg = ""
    cols = (C["orange"], C["brown"], C["yellow"], C["red"], C["wood"], C["orange"], C["yellow"], C["brown"], C["orange"], C["wood"], C["red"], C["yellow"])
    pts = ((-30, 0, 12), (-14, 1, -28), (2, 2, 18), (18, 1, -14), (32, 0, 30), (-22, -8, -20), (-6, -9, 24), (10, -9, -34), (24, -7, 10), (-11, -17, 8), (6, -18, -18), (-2, -26, 30))
    for (dx, dy, rot), c in zip(pts, cols):
        svg += f'<ellipse cx="{x + dx * s:.1f}" cy="{y + dy * s:.1f}" rx="{11 * s:.1f}" ry="{5.5 * s:.1f}" fill="{c}" stroke="{OUT}" stroke-width="{OW * 0.45:.1f}" ' \
               f'transform="rotate({rot} {x + dx * s:.1f} {y + dy * s:.1f})"/>'
    return svg, bb


def sandcastle(x, y, s=1.0, heaped=False):
    if heaped:
        # v0.26 bench: heaped sand with bucket-shaped towers ("very straight, boxy edges ... a cardboard or wooden model")
        sd = C["sand_dark"]
        svg = f'<path d="M {P(x - 42 * s, y)} Q {P(x - 40 * s, y - 26 * s)} {P(x - 22 * s, y - 32 * s)} Q {P(x, y - 38 * s)} {P(x + 22 * s, y - 32 * s)} Q {P(x + 40 * s, y - 26 * s)} {P(x + 42 * s, y)} Z" fill="{sd}" stroke="{OUT}" stroke-width="{OW * 0.8:.1f}" stroke-linejoin="round"/>'
        for tx, ty, th, tw in ((-24, -24, 34, 12), (22, -24, 26, 11), (-1, -32, 44, 13)):
            tp = y + ty * s - th * s
            svg += (f'<path d="M {P(x + (tx - tw) * s, y + ty * s)} L {P(x + (tx - tw * 0.72) * s, tp)} Q {P(x + tx * s, tp - 7 * s)} {P(x + (tx + tw * 0.72) * s, tp)} '
                    f'L {P(x + (tx + tw) * s, y + ty * s)} Q {P(x + tx * s, y + (ty + 5) * s)} {P(x + (tx - tw) * s, y + ty * s)} Z" fill="{sd}" stroke="{OUT}" stroke-width="{OW * 0.7:.1f}" stroke-linejoin="round"/>')
        for dx, dy in ((-30, -7), (-14, -16), (6, -9), (28, -11), (16, -21), (-5, -24), (-34, -14), (33, -5)):
            svg += f'<circle cx="{x + dx * s:.1f}" cy="{y + dy * s:.1f}" r="{1.5 * s:.1f}" fill="{OUT}" fill-opacity="0.35"/>'
        top = y - 83 * s
        svg += stroke(poly_d([(x - 1 * s, top), (x - 1 * s, top - 20 * s)]), OUT, 1.5 * s, 0)
        svg += poly([(x - 1 * s, top - 20 * s), (x + 13 * s, top - 15 * s), (x - 1 * s, top - 10 * s)], C["red"], OW * 0.5)
        return svg, (x - 44 * s, top - 22 * s, x + 44 * s, y)
    svg = rect(x - 34 * s, y - 34 * s, 68 * s, 34 * s, C["sand_dark"], 2 * s)
    for dx in (-22, 0, 22):
        svg += rect(x + dx * s - 9 * s, y - 52 * s, 18 * s, 20 * s, C["sand_dark"], 1 * s, OW * 0.7)
    svg += rect(x - 26 * s, y - 72 * s, 20 * s, 40 * s, C["sand_dark"], 1 * s, OW * 0.7)
    svg += stroke(poly_d([(x - 16 * s, y - 72 * s), (x - 16 * s, y - 92 * s)]), OUT, 1.5 * s, 0)
    svg += poly([(x - 16 * s, y - 92 * s), (x - 2 * s, y - 87 * s), (x - 16 * s, y - 82 * s)], C["red"], OW * 0.5)
    return svg, (x - 36 * s, y - 94 * s, x + 36 * s, y)


def sand_pail(x, y, s=1.0, col=None):
    col = col or C["red"]
    svg = poly([(x - 16 * s, y - 30 * s), (x + 16 * s, y - 30 * s), (x + 12 * s, y), (x - 12 * s, y)], col, OW * 0.8)
    svg += ell(x, y - 30 * s, 16 * s, 4 * s, C["sand"], OW * 0.6)
    svg += f'<path d="M {P(x - 14 * s, y - 29 * s)} Q {P(x, y - 50 * s)} {P(x + 14 * s, y - 29 * s)}" fill="none" stroke="{OUT}" stroke-width="2.5"/>'
    svg += stroke(poly_d([(x + 22 * s, y - 2 * s), (x + 36 * s, y - 44 * s)]), C["blue"], 4 * s, OW * 0.6)
    svg += poly([(x + 16 * s, y), (x + 30 * s, y - 4 * s), (x + 26 * s, y - 14 * s), (x + 14 * s, y - 10 * s)], C["blue"], OW * 0.6)
    return svg, (x - 18 * s, y - 50 * s, x + 38 * s, y)


def stroller(x, y, s=1.0, f=1, grip=None, short=False, face=False):
    """Baby stroller seen from the side, handle toward -f (the pusher stands on that side).
    grip: the pusher's hands; the handle bar is drawn up to them."""
    r = 20 * s
    svg = circ(x - f * 46 * s, y - r, r, C["charcoal"]) + circ(x + f * 40 * s, y - r, r, C["charcoal"])
    svg += circ(x - f * 46 * s, y - r, r * 0.3, C["gray"], OW * 0.6) + circ(x + f * 40 * s, y - r, r * 0.3, C["gray"], OW * 0.6)
    body = [(x - f * 62 * s, y - 50 * s), (x + f * 58 * s, y - 50 * s), (x + f * 50 * s, y - 92 * s), (x - f * 56 * s, y - 92 * s)]
    svg += poly(body, C["teal"])
    hood = f"M {P(x - f * 56 * s, y - 92 * s)} Q {P(x - f * 58 * s, y - 150 * s)} {P(x + f * 10 * s, y - 146 * s)} L {P(x + f * 4 * s, y - 92 * s)} Z"
    svg += shape(hood, C["navy"])
    svg += circ(x - f * 20 * s, y - 102 * s, 13 * s, C["skin1"], OW * 0.7)      # the baby, under the hood
    if face:
        # v0.16: a sleeping baby's face, closed eyes and a small mouth, and a curl of hair (a plain round head "has no face
        # drawn", "could be read as a pillow or ball")
        bx, by = x - f * 20 * s, y - 102 * s
        for ex in (-4.6, 4.6):
            svg += f'<path d="M {P(bx + ex * s - 2.6 * s, by - 1.2 * s)} Q {P(bx + ex * s, by + 1.6 * s)} {P(bx + ex * s + 2.6 * s, by - 1.2 * s)}" fill="none" stroke="{OUT}" stroke-width="{max(1.2, 1.5 * s):.1f}" stroke-linecap="round"/>'
        svg += f'<circle cx="{bx:.1f}" cy="{by + 5.2 * s:.1f}" r="{1.6 * s:.1f}" fill="{C["mouth"] if "mouth" in C else OUT}"/>'
        svg += f'<path d="M {P(bx - 3 * s, by - 11.5 * s)} q {2 * s:.1f} {-4 * s:.1f} {5 * s:.1f} {-1 * s:.1f}" fill="none" stroke="{OUT}" stroke-width="{max(1.2, 1.6 * s):.1f}" stroke-linecap="round"/>'
    if face:
        # v0.16: a quilt over the baby's body, rising over it and hanging down the pram's side in soft folds, with a
        # stitched hem (the flat cream oval on top read as "a flat disc or lid sitting on top", "a tray or a cake")
        q = (f"M {P(x - f * 8 * s, y - 95 * s)} Q {P(x + f * 20 * s, y - 112 * s)} {P(x + f * 52 * s, y - 95 * s)} "
             f"L {P(x + f * 52 * s, y - 77 * s)} Q {P(x + f * 44 * s, y - 72 * s)} {P(x + f * 36 * s, y - 77 * s)} "
             f"Q {P(x + f * 28 * s, y - 72 * s)} {P(x + f * 20 * s, y - 77 * s)} Q {P(x + f * 12 * s, y - 72 * s)} {P(x + f * 4 * s, y - 77 * s)} "
             f"L {P(x + f * 4 * s, y - 92 * s)} Z")
        svg += shape(q, C["pink"], OW * 0.7)
        svg += (f'<path d="M {P(x + f * 6 * s, y - 82 * s)} L {P(x + f * 50 * s, y - 82 * s)}" fill="none" stroke="{C["white"]}" '
                f'stroke-width="{max(1.2, 1.8 * s):.1f}" stroke-dasharray="{4 * s:.1f} {3 * s:.1f}" stroke-linecap="round"/>')
        for dx, dy in ((12, -98), (28, -101), (42, -96), (20, -89), (36, -88)):
            svg += f'<circle cx="{x + f * dx * s:.1f}" cy="{y + dy * s:.1f}" r="{1.8 * s:.1f}" fill="{C["white"]}"/>'
    else:
        svg += ell(x + f * 16 * s, y - 92 * s, 34 * s, 9 * s, C["cream"], OW * 0.7)    # blanket
    handle = grip or (x - f * 96 * s, y - 128 * s)
    # v0.13 (short): the handle rises from the top of the body, behind the hood, to the hands (from low on the
    # body it ran "very long and steeply angled")
    h0 = (x - f * 60 * s, y - 96 * s) if short else (x - f * 56 * s, y - 70 * s)
    svg += stroke(poly_d([h0, handle]), C["charcoal"], 6 * s, OW * 0.7)
    svg += stroke(poly_d([(handle[0] - f * 4 * s, handle[1]), (handle[0] + f * 10 * s, handle[1] + 4 * s)]), C["charcoal"], 9 * s, OW * 0.7)
    xs = [x - f * 100 * s, x + f * 64 * s, handle[0]]
    return svg, {"handle": handle, "bbox": (min(xs), min(y - 152 * s, handle[1] - 6), max(xs), y)}


def ladder(x, y, s=1.0, lean=14, h=300):
    """A step ladder leaning on nothing (the contradiction): feet at (x, y), top leaning toward +x."""
    a = math.radians(lean)
    H = h * s
    tx = x + math.sin(a) * H
    ty = y - math.cos(a) * H
    w = 46 * s
    svg = stroke(poly_d([(x, y), (tx, ty)]), C["wood_light"], 8 * s, OW * 0.8)
    svg += stroke(poly_d([(x + w, y), (tx + w * 0.8, ty)]), C["wood_light"], 8 * s, OW * 0.8)
    for k in range(1, 7):
        t = k / 7
        ax, ay = x + (tx - x) * t, y + (ty - y) * t
        bx = x + w + (tx + w * 0.8 - x - w) * t
        svg += line(ax, ay, bx, ay, OUT, 5 * s)
    return svg, (min(x, tx) - 8 * s, ty - 8 * s, max(x + w, tx + w) + 8 * s, y + 2)


def newspaper(x, y, s=1.0, f=1, style=6):
    """An opened newspaper (ruled lines only, never readable text), held up near (x, y). style 7 (v0.9)
    adds a headline bar on each page, a photo block and narrow columns (with ruled lines alone it read
    as a notebook or a ring binder)."""
    w, h = 74 * s, 58 * s
    pts = [(x - w / 2, y - h / 2), (x, y - h / 2 + f * 6 * s), (x + w / 2, y - h / 2), (x + w / 2, y + h / 2), (x, y + h / 2 + f * 6 * s), (x - w / 2, y + h / 2)]
    svg = poly(pts, C["paper"])
    svg += line(x, y - h / 2 + f * 6 * s, x, y + h / 2 + f * 6 * s, OUT, 2.5)
    if style >= 7:
        for side in (-1, 1):
            xa, xb = (x - w / 2 + 5 * s, x - 5 * s) if side < 0 else (x + 5 * s, x + w / 2 - 5 * s)
            top = y - h / 2 + (6 * s if side * f > 0 else 3 * s) + 4 * s
            svg += rect(xa, top, xb - xa, 7 * s, OUT, 0)                       # headline bar
            if side == -f:
                if style >= 8:
                    # v0.26: a pale photo with no outline (the darker one was "a dark square ... a dark object or something the paw is
                    # holding", three pictures)
                    svg += rect(xa, top + 11 * s, (xb - xa) * 0.55, 17 * s, "#dcdbd2", 1.5, 0)
                else:
                    svg += rect(xa, top + 11 * s, (xb - xa) * 0.55, 17 * s, C["rock"], 1.5)      # photo
                cols = [(xa + (xb - xa) * 0.62, xb)]
                rows = [(top + 12 * s + k * 5 * s) for k in range(4)]
                for (c0, c1) in cols:
                    for yy in rows:
                        svg += line(c0, yy, c1, yy, C["rock_dark"], 1.6 * s)
                for k in range(3):
                    yy = top + 33 * s + k * 5 * s
                    svg += line(xa, yy, xb, yy, C["rock_dark"], 1.6 * s)
            else:
                mid = (xa + xb) / 2
                for (c0, c1) in ((xa, mid - 2 * s), (mid + 2 * s, xb)):
                    for k in range(7):
                        yy = top + 12 * s + k * 5 * s
                        svg += line(c0, yy, c1, yy, C["rock_dark"], 1.6 * s)
        return svg, (x - w / 2 - 3, y - h / 2 - 8 * s, x + w / 2 + 3, y + h / 2 + 8 * s)
    for side in (-1, 1):
        for k in range(5):
            yy = y - h / 2 + 12 * s + k * 9 * s
            x0, x1 = (x - w / 2 + 6 * s, x - 6 * s) if side < 0 else (x + 6 * s, x + w / 2 - 6 * s)
            svg += line(x0, yy, x1 - (10 * s if k == 4 else 0), yy, C["rock_dark"], 2.2 * s)
    return svg, (x - w / 2 - 3, y - h / 2 - 8 * s, x + w / 2 + 3, y + h / 2 + 8 * s)
