"""The rendered asset library: catalog lookup, variant ids, on-demand rendering, placement math.

A variant is (family, pose, expression, yaw). Its PNG, mask and manifest live in the library
directory and are rendered on first use by assets/cast/render_set.py (one Blender process per
family, so a batch of scenes shares the start-up cost).
"""
import base64
import io
import json
import math
import os
import shutil
import subprocess
import sys
import time
from collections import defaultdict

from PIL import Image

from .draw import OUT, ppm

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
CAST_DIR = os.path.join(ROOT, "assets", "cast", "out039")
LIB_DIR = os.path.join(ROOT, "assets", "cast", "lib039")
RENDER_SET = os.path.join(ROOT, "assets", "cast", "render_set.py")
# v0.28 bench (isolation_v028.md): "O" keeps the shadow from the figure's box
SHADOW28 = "B"
# v0.29 bench: "W" a wider shadow, further under the body, for a dog asleep (the old pose's oval went from wide to narrow in v0.28, and the sleeping dog fell under the gate)
SHADOW29 = "O"
SHADOW_FOOT = 0.085                 # a person's shadow past the feet on each side, as a part of the figure's height
ON_THE_GROUND = {"sit_ground", "kneel_plant", "sand_build"}     # poses whose body, not the feet, meets the ground


def _rev():
    return sys.modules["scenegen.scene"].PLACEMENT_REV


def vid(fam, pose, expr, yaw):
    return f"{fam}__{pose}__{expr}__y{int(yaw):03d}"


class Library:
    def __init__(self, cast_dir=CAST_DIR, lib_dir=LIB_DIR, samples=10):
        self.cast_dir, self.lib_dir, self.samples = cast_dir, lib_dir, samples
        self.catalog = json.load(open(os.path.join(cast_dir, "cast_catalog.json")))
        self.families = self.catalog["families"]
        self.actions = self.catalog["actions"]
        self._m = {}
        self._img = {}
        os.makedirs(lib_dir, exist_ok=True)

    # catalog queries ---------------------------------------------------------
    def people(self, kinds=None):
        out = []
        for f, d in self.families.items():
            if d["class"] != "person":
                continue
            if kinds and d["kind"] not in kinds:
                continue
            out.append(f)
        return out

    def kind(self, fam):
        return self.families[fam]["kind"]

    def animals(self, kinds):
        return [f for f, d in self.families.items() if d["class"] == "animal" and d["kind"] in kinds]

    def label(self, fam):
        return self.families[fam]["labels"]

    def has(self, v):
        return os.path.exists(os.path.join(self.lib_dir, v + ".json"))

    def ensure(self, variants, log=print):
        """Render every missing variant (list of (fam, pose, expr, yaw))."""
        todo = [v for v in {tuple(v) for v in variants} if not self.has(vid(*v))]
        if not todo:
            return 0
        tmp = os.path.join(self.lib_dir, f".queue_{os.getpid()}.json")
        json.dump([list(v) for v in sorted(todo)], open(tmp, "w"))
        log(f"rendering {len(todo)} variants ...")
        # v0.27: rendered aside and moved in whole, the manifest last, as has() looks for it (searches side by side read each other's half-written images: "image file is truncated")
        aside = os.path.join(self.lib_dir, f".render_{os.getpid()}")
        os.makedirs(aside, exist_ok=True)
        r = subprocess.run([sys.executable, RENDER_SET, self.cast_dir, aside, tmp, str(self.samples)], capture_output=True, text=True)
        log(r.stdout.strip()[-2000:])
        if r.returncode != 0:
            log(r.stderr[-2000:])
        os.remove(tmp)
        for f in sorted(os.listdir(aside), key=lambda n: (n.endswith(".json") and not n.startswith("."), n)):
            src, dst = os.path.join(aside, f), os.path.join(self.lib_dir, f)
            if os.path.exists(dst):
                os.remove(src)      # (another search got there first; a cast renders the same variant the same way)
                continue
            for k in range(20):
                try:
                    os.replace(src, dst)
                    break
                except OSError:
                    time.sleep(0.5)
        shutil.rmtree(aside, ignore_errors=True)
        missing = [v for v in todo if not self.has(vid(*v))]
        if missing:
            raise RuntimeError(f"render failed for {missing[:5]}")
        return len(todo)

    def manifest(self, v):
        if v not in self._m:
            self._m[v] = json.load(open(os.path.join(self.lib_dir, v + ".json")))
        return self._m[v]

    def image(self, v):
        if v not in self._img:
            m = self.manifest(v)
            self._img[v] = Image.open(os.path.join(self.lib_dir, m["files"]["image"]["path"])).convert("RGBA")
        return self._img[v]


MIRROR_SWAP = [("_L", "_R"), ("FL", "FR"), ("BL", "BR")]


def mirror_name(name):
    for a, b in MIRROR_SWAP:
        if a in name:
            return name.replace(a, "\0").replace(b, a).replace("\0", b)
        if b in name:
            return name.replace(b, "\0").replace(a, b).replace("\0", a)
    return name


class BBox(tuple):
    """A bounding box (x0, y0, x1, y1) that remembers the placed asset it belongs to."""
    asset = None


class Placed:
    """One rendered asset placed in the scene: ground point (X, Y), scale from depth, optional mirror."""

    def __init__(self, lib, v, X, Y, mirror=False, depth_y=None, eid=None, role="scored"):
        self.lib, self.v, self.m = lib, v, lib.manifest(v)
        self.mirror = mirror
        self.depth_y = depth_y if depth_y is not None else Y
        self.k = ppm(self.depth_y) / self.m["render"]["pixels_per_meter"]
        self.s = -1 if mirror else 1
        self.gx, self.gy = self.m["geometry"]["ground_point_px"]
        self.X, self.Y = X, Y
        self.id = eid or v
        self.role = role
        self.z = self.depth_y

    @property
    def family(self):
        return self.m["family_id"]

    def set_depth(self, depth_y, keep="ground"):
        self.depth_y = depth_y
        self.k = ppm(depth_y) / self.m["render"]["pixels_per_meter"]
        self.z = depth_y

    def pt(self, p):
        x, y = (self.X + self.s * self.k * (p[0] - self.gx), self.Y + self.k * (p[1] - self.gy))
        rot = getattr(self, "rot", None)
        if rot:
            # v0.35: a figure turned about a point (the child on a swung seat), as its drawing is
            a, cx, cy = math.radians(rot[0]), rot[1], rot[2]
            x, y = cx + (x - cx) * math.cos(a) - (y - cy) * math.sin(a), cy + (x - cx) * math.sin(a) + (y - cy) * math.cos(a)
        return (x, y)

    def has_anchor(self, name):
        return (mirror_name(name) if self.mirror else name) in self.m["anchors"]

    def anchor(self, name):
        n = mirror_name(name) if self.mirror else name
        return self.pt(self.m["anchors"][n]["px"])

    def bbox(self):
        x0, y0, x1, y1 = self.m["geometry"]["bbox_px"]
        if getattr(self, "rot", None):
            q = [self.pt(c) for c in ((x0, y0), (x1, y0), (x0, y1), (x1, y1))]
            out = BBox((min(c[0] for c in q), min(c[1] for c in q), max(c[0] for c in q), max(c[1] for c in q)))
            out.asset = self
            return out
        a, b = self.pt((x0, y0)), self.pt((x1, y1))
        out = BBox((min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])))
        out.asset = self
        return out

    def color_at(self, name, r=4):
        """The asset's own colour around one of its anchors (median of the opaque pixels nearby)."""
        n = mirror_name(name) if self.mirror else name
        px, py = self.m["anchors"][n]["px"]
        im = self.lib.image(self.v)
        cols = []
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                x, y = int(px + dx), int(py + dy)
                if 0 <= x < im.width and 0 <= y < im.height:
                    c = im.getpixel((x, y))
                    if c[3] > 200 and sum(c[:3]) > 120:      # skip outline ink and transparent pixels
                        cols.append(c[:3])
        if not cols:
            return "#ffffff"
        cols.sort(key=lambda c: sum(c))
        c = cols[(len(cols) * 3) // 4]          # the lit side, not the shading
        return "#%02x%02x%02x" % c

    def move_anchor_to(self, name, target):
        ax, ay = self.anchor(name)
        self.X += target[0] - ax
        self.Y += target[1] - ay

    def facing(self):
        """+1 if the character looks toward image right, -1 toward image left, 0 toward the viewer."""
        A = self.m["anchors"]
        if "gaze_target" not in A:
            return 0
        ex = (A["eye_L"]["px"][0] + A["eye_R"]["px"][0]) / 2 if "eye_L" in A else A["head_top"]["px"][0]
        dx = A["gaze_target"]["px"][0] - ex
        toward = -(A["gaze_target"]["depth_m"] - (A["eye_L"]["depth_m"] + A["eye_R"]["depth_m"]) / 2) if "eye_L" in A else 0
        if abs(dx) < 6 and toward > 0.5:
            return 0
        return (1 if dx > 0 else -1) * self.s

    def toward_viewer(self):
        A = self.m["anchors"]
        if "eye_L" not in A or "gaze_target" not in A:
            return 0.0
        return -(A["gaze_target"]["depth_m"] - (A["eye_L"]["depth_m"] + A["eye_R"]["depth_m"]) / 2)

    def eye_mid(self):
        if self.has_anchor("eye_L"):
            (lx, ly), (rx, ry) = self.anchor("eye_L"), self.anchor("eye_R")
            return ((lx + rx) / 2, (ly + ry) / 2)
        return self.anchor("head_top")

    def area_px(self):
        a = self.m.get("_area")
        if a is None:
            import numpy as np
            mask = Image.open(os.path.join(self.lib.lib_dir, self.m["files"]["mask"]["path"])).convert("L")
            a = int((np.asarray(mask) > 127).sum())
            self.m["_area"] = a
        return a * self.k * self.k

    def image_data(self):
        """The asset scaled (and mirrored) to its scene size, as a PNG data URI plus its top-left corner."""
        key = (round(self.k, 5), self.mirror, round(self.X, 2), round(self.Y, 2))
        if getattr(self, "_img_key", None) == key:
            return self._img_val
        self._img_key = key
        self._img_val = self._image_data()
        return self._img_val

    def _image_data(self):
        im = self.lib.image(getattr(self, "draw_v", None) or self.v)      # (v0.31: a rider draws the figure without its far leg)
        w, h = im.size
        nw, nh = max(1, round(w * self.k)), max(1, round(h * self.k))
        sm = im.resize((nw, nh), Image.LANCZOS)
        if self.mirror:
            sm = sm.transpose(Image.FLIP_LEFT_RIGHT)
        x0 = self.X - self.s * self.k * self.gx if not self.mirror else self.X - self.k * (w - self.gx)
        y0 = self.Y - self.k * self.gy
        buf = io.BytesIO()
        sm.save(buf, "PNG", optimize=True)
        return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode(), x0, y0, nw, nh

    def solid_span(self):
        """Revision 26: the columns the body itself fills, in sprite pixels (columns under a third of the fullest one are a tail, an arm or a tool)."""
        sp = self.m.get("_span")
        if sp is None:
            import numpy as np
            mask = np.asarray(Image.open(os.path.join(self.lib.lib_dir, self.m["files"]["mask"]["path"])).convert("L")) > 127
            cols = mask.sum(axis=0)
            idx = np.nonzero(cols >= max(1, cols.max() / 3))[0]
            rows = np.nonzero(mask[:, idx[0]:idx[-1] + 1].any(axis=1))[0]
            sp = (int(idx[0]), int(idx[-1]) + 1, int(rows[-1]) + 1)
            self.m["_span"] = sp
        return sp

    def own_shadow(self):
        """Revision 26: the shadow from the figure's own footprint (its box took in arms, tools and the depth of the body: "a very wide oval, much wider
        than the puppy", "a large oval ... a bit wide and offset from her feet"). A person on their feet casts it from the feet; anything else from the
        columns the body fills, under its lowest part (a body lying down reaches below its ground point, and hid a shadow drawn there). Returns (cx, cy, rx, ry)."""
        H = self.m["geometry"]["height_m"] * ppm(self.depth_y)
        if self.family.startswith("person.") and self.pose() not in ON_THE_GROUND and self.has_anchor("foot_L") and self.has_anchor("foot_R"):
            a, b = self.anchor("foot_L")[0], self.anchor("foot_R")[0]
            rx = abs(a - b) / 2 + SHADOW_FOOT * H
            return (a + b) / 2, self.Y + 2, rx, rx * 0.26
        u0, u1, v1 = self.solid_span()
        a, b = self.X + self.s * self.k * (u0 - self.gx), self.X + self.s * self.k * (u1 - self.gx)
        rx = abs(b - a) / 2 * 1.06
        ry = rx * 0.2
        if SHADOW29 == "W" and self.pose().startswith("sleep"):
            rx *= 1.22
            ry = rx * 0.3
            return (a + b) / 2, self.Y + self.k * (v1 - self.gy) - 1.1 * ry, rx, ry
        return (a + b) / 2, self.Y + self.k * (v1 - self.gy) - 0.45 * ry, rx, ry

    def pose(self):
        return self.v.split("__")[1]

    def svg(self, shadow=True):
        uri, x0, y0, w, h = self.image_data()
        out = ""
        # a ground shadow only for things standing on the ground (not for a bird on a lamp or fence)
        on_ground = abs(self.Y - self.depth_y) < 30
        if shadow and on_ground and _rev() >= 26 and SHADOW28 != "O":
            # (a rider on the seesaw has none of its own: the seesaw casts one under the whole plank, "the boy has a shadow ... the girl has none of her own")
            if not getattr(self, "no_shadow", False):
                cx, cy, rx, ry = self.own_shadow()
                air = self.m["variant"].get("airborne")
                out += f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{OUT}" fill-opacity="{0.14 if air else 0.16}"/>'
        elif shadow and on_ground and not self.m["variant"].get("airborne"):
            fw = max(self.m["geometry"]["footprint_m"].values()) * ppm(self.depth_y) * 1.25
            # v0.9: a rider seated on a structure gets the shadow under the feet (set by the template)
            cx = getattr(self, "shadow_x", None) or self.X
            out += f'<ellipse cx="{cx:.1f}" cy="{self.Y + 2:.1f}" rx="{fw / 2:.1f}" ry="{fw / 7:.1f}" fill="{OUT}" fill-opacity="0.16"/>'
        elif shadow and on_ground and self.family.startswith("person."):
            # v0.7: a jumper's shadow on the ground below, with a gap up to the feet (with no shadow at all
            # a jump read as kneeling or squatting)
            fw = max(self.m["geometry"]["footprint_m"].values()) * ppm(self.depth_y) * 1.0
            out += f'<ellipse cx="{self.X:.1f}" cy="{self.Y + 2:.1f}" rx="{fw / 2:.1f}" ry="{fw / 8:.1f}" fill="{OUT}" fill-opacity="0.14"/>'
        img = f'<image x="{x0:.2f}" y="{y0:.2f}" width="{w}" height="{h}" href="{uri}"/>'
        rot = getattr(self, "rot", None)
        if rot:
            img = f'<g transform="rotate({rot[0]:.2f} {rot[1]:.2f} {rot[2]:.2f})">{img}</g>'
        out += img
        return out


def looks_at(p, box, max_len=2600):
    """Does the gaze ray from p's eyes (through its gaze_target anchor) cross box?"""
    if p.toward_viewer() > 0.7:
        return False, "faces the viewer"
    ex, ey = p.eye_mid()
    gx, gy = p.anchor("gaze_target")
    dx, dy = gx - ex, gy - ey
    n = math.hypot(dx, dy) or 1.0
    dx, dy = dx / n, dy / n
    for t in range(0, max_len, 2):
        x, y = ex + dx * t, ey + dy * t
        if box[0] <= x <= box[2] and box[1] <= y <= box[3]:
            return True, f"hits after {t}px"
    return False, "misses"


def gaze_angle_to(p, pt):
    """Angle in degrees between p's gaze ray and the direction from its eyes to pt."""
    ex, ey = p.eye_mid()
    gx, gy = p.anchor("gaze_target")
    a = math.atan2(gy - ey, gx - ex)
    b = math.atan2(pt[1] - ey, pt[0] - ex)
    d = abs((a - b + math.pi) % (2 * math.pi) - math.pi)
    return math.degrees(d)
