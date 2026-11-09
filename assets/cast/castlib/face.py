"""Face kit v2: features on an ellipsoid head, and the expressions that toggle and move them.

Every part is built once. An expression is a set of visible parts plus rest-space
transforms (eye glance, brow height and tilt, eye size), stored per object, so the
renderer can switch expressions without rebuilding anything. Glances also move the
ANCHOR_gaze_target empty, so "looks at" checks follow the eyes.
"""
import math

import bpy  # noqa: F401
from mathutils import Matrix, Quaternion, Vector

from .core import capsule_arc, ellipsoid, half_ellipsoid, list_m, nrm, smooth_curve, tube, upd


class Face:
    """Features on the front (-Y) of an ellipsoid head with center c and radii (ax, ay, az)."""

    def __init__(self, rig, bone, c, radii, k=1.0, prefix="F"):
        self.rig, self.bone, self.c, self.k, self.p = rig, bone, Vector(c), k, prefix
        self.ax, self.ay, self.az = radii
        self.objs = {}

    def surf(self, x, z):
        u = 1 - (x / self.ax) ** 2 - (z / self.az) ** 2
        y = -self.ay * math.sqrt(max(1e-4, u))
        return Vector((x, y, z))

    def normal(self, x, z):
        p = self.surf(x, z)
        return nrm(Vector((p.x / self.ax ** 2, p.y / self.ay ** 2, p.z / self.az ** 2)))

    def at(self, x, z, out=0.0):
        return self.c + self.surf(x, z) + self.normal(x, z) * out

    def frame(self, x, z, out, spin=0.0, scale=(1, 1, 1)):
        """World matrix for a feature lying flat on the skin: local -Y = outward normal."""
        n = self.normal(x, z)
        q = Vector((0, -1, 0)).rotation_difference(n)
        q = q @ Quaternion((0, 1, 0), spin)
        sc = Vector((scale[0], scale[1] * 0.55, scale[2]))
        return Matrix.LocRotScale(self.at(x, z, out * 0.6), q, sc)

    def obj(self, key, ob):
        ob.name = f"{self.p}_{key}"
        self.objs[key] = ob
        return ob

    def place(self, key, ob, M):
        ob.matrix_world = M
        upd()
        self.rig.attach(ob, self.bone)
        return self.obj(key, ob)

    def curve_on(self, key, pts2d, radius, matkey, out):
        pts = [self.at(x, z, out) for x, z in pts2d]
        return self.obj(key, tube(key, pts, radius, matkey, self.rig, self.bone))


# Sizes in head units (k = character scale); bigger than v0.3 so faces read at scene size.
EYE_W, EYE_H = 0.0235, 0.0355
BROW_UP = 0.058
MOUTH_DZ = -0.086
MOUTH_W = 0.034
LINE = 0.0072


def build_people_face(face, eye_dx, eye_z, k, glasses=False, blush_key="pink", skin_key="skin1", mouth_col=None):
    for side, s in (("L", 1), ("R", -1)):
        x = s * eye_dx
        face.place(f"eye_{side}", ellipsoid("eye", (0, 0, 0), (1, 1, 1), "outline"),
                   face.frame(x, eye_z, 0.0, scale=(EYE_W * k, 0.010 * k, EYE_H * k)))
        cobj = face.place(f"catch_{side}", ellipsoid("catch", (0, 0, 0), (1, 1, 1), "cream"),
                          face.frame(x + 0.008 * k, eye_z + 0.013 * k, 0.016 * k, scale=(0.0085 * k, 0.004 * k, 0.0110 * k)))
        cobj.lineart.usage = "EXCLUDE"
        face.place(f"half_{side}", half_ellipsoid("half", "outline"),
                   face.frame(x, eye_z + 0.004 * k, 0.0, scale=(EYE_W * 1.08 * k, 0.010 * k, EYE_H * 0.85 * k)))
        face.place(f"white_{side}", ellipsoid("white", (0, 0, 0), (1, 1, 1), "cream"),
                   face.frame(x, eye_z, 0.002 * k, scale=(EYE_W * 1.30 * k, 0.010 * k, EYE_H * 1.12 * k)))
        face.place(f"pupil_{side}", ellipsoid("pupil", (0, 0, 0), (1, 1, 1), "outline"),
                   face.frame(x, eye_z, 0.012 * k, scale=(EYE_W * 0.55 * k, 0.004 * k, EYE_H * 0.52 * k)))
        w = EYE_W * 1.35 * k
        face.curve_on(f"arcup_{side}", smooth_curve([(x - w, eye_z - 0.016 * k), (x, eye_z + 0.017 * k), (x + w, eye_z - 0.016 * k)], 6),
                      LINE * 1.05 * k, "outline", 0.004 * k)
        face.curve_on(f"arcup2_{side}", smooth_curve([(x - w * 1.05, eye_z - 0.020 * k), (x - w * 0.15, eye_z + 0.020 * k), (x + w * 1.05, eye_z - 0.006 * k)], 6),
                      LINE * 1.25 * k, "outline", 0.004 * k)
        face.curve_on(f"arcdn_{side}", smooth_curve([(x - w, eye_z + 0.006 * k), (x, eye_z - 0.014 * k), (x + w, eye_z + 0.006 * k)], 6),
                      LINE * 1.05 * k, "outline", 0.004 * k)
        face.place(f"brow_{side}", capsule_arc("brow", "outline", bend=0.30),
                   face.frame(x, eye_z + BROW_UP * k, 0.004 * k, scale=(0.027 * k, 0.007 * k, 0.0095 * k)))
        # v0.28, TPDB_BLUSH: smaller, nearer the eye ("a pink smudge on the cheek, which could be blush or ice cream")
        bl28 = __import__("os").environ.get("TPDB_BLUSH", "B") == "B"
        face.place(f"blush_{side}", ellipsoid("blush", (0, 0, 0), (1, 1, 1), blush_key),
                   face.frame(s * (eye_dx + (0.022 if bl28 else 0.030) * k), eye_z - (0.036 if bl28 else 0.044) * k, 0.001 * k,
                              scale=((0.015 if bl28 else 0.024) * k, 0.004 * k, (0.008 if bl28 else 0.013) * k)))

    mz = eye_z + MOUTH_DZ * k
    mw = MOUTH_W * k
    # v0.27, chosen on the bench: thinner, in a lip colour (a black line near the edge of the face: "a dark mark around the mouth could be a mouth or a small beard or moustache", four cut-outs)
    m27 = __import__("os").environ.get("TPDB_MOUTH", "B") == "B"
    lw = LINE * k * (0.86 if m27 else 1.0)
    mc = "throat" if m27 else "outline"
    if mouth_col:
        mc, lw = mouth_col, lw * 1.15      # v0.43 (TPDB_ADULT43): lips, a line in a lip colour
    out = 0.003 * k
    face.curve_on("m_smile", smooth_curve([(-mw, mz + 0.009 * k), (0, mz - 0.011 * k), (mw, mz + 0.009 * k)], 8), lw, mc, out)
    face.curve_on("m_frown", smooth_curve([(-mw, mz - 0.011 * k), (0, mz + 0.007 * k), (mw, mz - 0.011 * k)], 8), lw, mc, out)
    # neutral: a short, thin, barely curved line set low (a straight bar under the nose reads as a moustache)
    face.curve_on("m_flat", smooth_curve([(-mw * 0.62, mz - 0.004 * k), (0, mz - 0.008 * k), (mw * 0.62, mz - 0.004 * k)], 6), lw * 0.78, mc, out)
    face.curve_on("m_wobble", smooth_curve([(-mw * 0.72, mz + 0.002 * k), (-mw * 0.36, mz + 0.011 * k), (0, mz), (mw * 0.36, mz - 0.011 * k), (mw * 0.72, mz - 0.002 * k)], 6), lw * 0.72, mc, out)
    face.curve_on("m_slant", [(-mw * 0.20, mz - 0.006 * k), (mw * 0.78, mz + 0.008 * k)], lw * 0.80, mc, out)
    face.curve_on("m_smirk", smooth_curve([(-mw * 0.85, mz - 0.003 * k), (0.1 * mw, mz - 0.006 * k), (mw * 0.95, mz + 0.012 * k)], 8), lw, mc, out)
    face.curve_on("m_disgust", smooth_curve([(-mw * 0.85, mz - 0.012 * k), (-0.25 * mw, mz + 0.006 * k), (0.40 * mw, mz - 0.003 * k), (mw * 0.90, mz + 0.004 * k)], 6), lw * 0.78, mc, out)
    face.place("m_grin", half_ellipsoid("grin", "throat"), face.frame(0, mz + 0.010 * k, 0.0, scale=(mw * 1.30, 0.010 * k, 0.030 * k)))
    face.place("m_laugh", half_ellipsoid("laugh", "throat"), face.frame(0, mz + 0.012 * k, 0.0, scale=(mw * 1.45, 0.010 * k, 0.042 * k)))
    face.place("m_tongue", ellipsoid("tongue", (0, 0, 0), (1, 1, 1), "red"), face.frame(0, mz - 0.020 * k, 0.003 * k, scale=(mw * 0.62, 0.004 * k, 0.012 * k)))
    face.place("m_O", ellipsoid("O", (0, 0, 0), (1, 1, 1), "throat"), face.frame(0, mz - 0.006 * k, 0.0, scale=(0.017 * k, 0.010 * k, 0.022 * k)))
    face.place("m_ooh", ellipsoid("ooh", (0, 0, 0), (1, 1, 1), "throat"), face.frame(0, mz - 0.010 * k, 0.0, scale=(0.015 * k, 0.010 * k, 0.030 * k)))
    face.place("m_o", ellipsoid("o", (0, 0, 0), (1, 1, 1), "outline"), face.frame(0, mz, 0.0, scale=(0.009 * k, 0.008 * k, 0.011 * k)))
    face.place("m_teeth", ellipsoid("teeth", (0, 0, 0), (1, 1, 1), "cream"), face.frame(0, mz - 0.002 * k, 0.001 * k, scale=(mw * 1.05, 0.010 * k, 0.012 * k)))
    face.curve_on("m_teeth_line", [(-mw * 0.92, mz - 0.002 * k), (mw * 0.92, mz - 0.002 * k)], lw * 0.55, "outline", 0.010 * k)

    if glasses:
        for side, s in (("L", 1), ("R", -1)):
            x = s * eye_dx
            ring = [(x + 0.042 * k * math.cos(a), eye_z + 0.038 * k * math.sin(a))
                    for a in [i / 28 * 2 * math.pi for i in range(28)]]
            ob = face.curve_on(f"glass_{side}", ring, 0.0045 * k, "outline", 0.018 * k)
            ob.data.splines[0].use_cyclic_u = True
        face.curve_on("glass_bridge", [(-eye_dx + 0.042 * k, eye_z + 0.008 * k), (eye_dx - 0.042 * k, eye_z + 0.008 * k)],
                      0.004 * k, "outline", 0.020 * k)


MOUTHS = {"m_smile": ["m_smile"], "m_frown": ["m_frown"], "m_flat": ["m_flat"], "m_wobble": ["m_wobble"], "m_slant": ["m_slant"],
          "m_smirk": ["m_smirk"], "m_disgust": ["m_disgust"], "m_grin": ["m_grin"], "m_laugh": ["m_laugh", "m_tongue"],
          "m_O": ["m_O"], "m_ooh": ["m_ooh"], "m_o": ["m_o"], "m_teeth": ["m_teeth", "m_teeth_line"]}

# eyes: bean | half | wide | happy | laugh | closed | narrow
# brow: (raise L, tilt L, raise R, tilt R) in head units / degrees; positive tilt = inner end up
# look: glance (x toward the character's left, z up), each in [-1, 1]
PEOPLE_EXPRESSIONS = {
    "neutral":     dict(eyes="bean",   brow=(0.000, 0, 0.000, 0),     mouth="m_flat"),
    "smile":       dict(eyes="bean",   brow=(0.004, 0, 0.004, 0),     mouth="m_smile"),
    "happy":       dict(eyes="happy",  brow=(0.009, 0, 0.009, 0),     mouth="m_grin", blush=True),
    "laughing":    dict(eyes="laugh",  brow=(0.014, 8, 0.014, 8),     mouth="m_laugh", blush=True),
    "content":     dict(eyes="closed", brow=(0.004, 6, 0.004, 6),     mouth="m_smile", blush=True),
    "surprised":   dict(eyes="wide",   brow=(0.024, 0, 0.024, 0),     mouth="m_O"),
    "scared":      dict(eyes="wide",   brow=(0.018, 26, 0.018, 26),   mouth="m_teeth", pupil=0.6),
    "puzzled":     dict(eyes="bean",   brow=(0.020, -10, -0.004, 14), mouth="m_slant", look=(-0.5, 0.6)),
    "sad":         dict(eyes="bean",   brow=(0.004, 24, 0.004, 24),   mouth="m_frown", eye=0.84, look=(0.0, -0.6)),
    "angry":       dict(eyes="narrow", brow=(-0.012, -30, -0.012, -30), mouth="m_frown"),
    "worried":     dict(eyes="wide",   brow=(0.010, 26, 0.010, 26),   mouth="m_wobble", pupil=0.75),
    "sleepy":      dict(eyes="closed", brow=(-0.004, 6, -0.004, 6),   mouth="m_o"),
    "focused":     dict(eyes="narrow", brow=(-0.006, -10, -0.006, -10), mouth="m_flat"),
    "bored":       dict(eyes="half",   brow=(-0.004, 0, -0.004, 0),   mouth="m_flat", look=(0.55, 0.45)),
    "disgusted":   dict(eyes="half",   brow=(-0.010, -22, 0.004, 10), mouth="m_disgust", look=(-0.6, 0.0)),
    "embarrassed": dict(eyes="bean",   brow=(0.008, 18, 0.008, 18),   mouth="m_wobble", blush=True, look=(0.6, -0.6)),
    "determined":  dict(eyes="narrow", brow=(-0.008, -20, -0.008, -20), mouth="m_smirk"),
    "calling":     dict(eyes="bean",   brow=(0.016, 0, 0.016, 0),     mouth="m_ooh"),
    "suspicious":  dict(eyes="half",   brow=(-0.010, -14, 0.006, 0),  mouth="m_slant", look=(0.75, 0.0)),
}

GLANCE_YAW_DEG, GLANCE_PITCH_DEG = 24.0, 20.0


def gaze_dir(look):
    gx, gz = look
    yaw, pitch = math.radians(gx * GLANCE_YAW_DEG), math.radians(gz * GLANCE_PITCH_DEG)
    return Vector((math.sin(yaw) * math.cos(pitch), -math.cos(yaw) * math.cos(pitch), math.sin(pitch)))


def people_expression_states(face, eye_dx, eye_z, k, gaze_anchor_name="ANCHOR_gaze_target", extra_show=()):
    states = {}
    mid = (face.at(eye_dx, eye_z) + face.at(-eye_dx, eye_z)) / 2
    for name, e in PEOPLE_EXPRESSIONS.items():
        st = {}
        show = set(extra_show)
        eyes = e["eyes"]
        gx, gz = e.get("look", (0.0, 0.0))
        ex, ez = gx * 0.010 * k, gz * 0.009 * k
        if eyes in ("bean", "narrow"):
            show |= {"eye_L", "eye_R", "catch_L", "catch_R"}
        elif eyes == "half":
            show |= {"half_L", "half_R"}
        elif eyes == "wide":
            show |= {"white_L", "white_R", "pupil_L", "pupil_R"}
        elif eyes == "happy":
            show |= {"arcup_L", "arcup_R"}
        elif eyes == "laugh":
            show |= {"arcup2_L", "arcup2_R"}
        elif eyes == "closed":
            show |= {"arcdn_L", "arcdn_R"}
        show |= set(MOUTHS[e["mouth"]])
        # v0.28, TPDB_BROW: no brows over closed eyes, which drew two dark lines to each eye ("dark marks around the eye and mouth area", "a slightly muddled drawing of her features")
        if not (eyes == "closed" and __import__("os").environ.get("TPDB_BROW", "B") == "B"):
            show |= {"brow_L", "brow_R"}
        if e.get("blush"):
            show |= {"blush_L", "blush_R"}
        show |= {key for key in face.objs if key.startswith("glass")}
        # v0.36: the bold moustache in every expression (every face part not named here is hidden, and the thin moustache, named
        # nowhere, has been hidden in every render since it was first built)
        show |= {key for key in face.objs if key.startswith("mustache36")}
        for key, ob in face.objs.items():
            st[ob.name] = {"hide": key not in show}
        f = e.get("eye", 1.0)
        for side, s in (("L", 1), ("R", -1)):
            x = s * eye_dx
            if eyes == "narrow":
                st[face.objs[f"eye_{side}"].name]["basis"] = list_m(face.frame(x + ex, eye_z - 0.005 * k + ez, 0.0, scale=(EYE_W * 1.10 * k, 0.010 * k, EYE_H * 0.42 * k)))
                st[face.objs[f"catch_{side}"].name]["hide"] = True
            else:
                st[face.objs[f"eye_{side}"].name]["basis"] = list_m(face.frame(x + ex, eye_z + ez, 0.0, scale=(EYE_W * f * k, 0.010 * k, EYE_H * f * k)))
                st[face.objs[f"catch_{side}"].name]["basis"] = list_m(face.frame(x + ex + 0.008 * k * f, eye_z + ez + 0.013 * k * f, 0.016 * k, scale=(0.0085 * k * f, 0.004 * k, 0.0110 * k * f)))
            st[face.objs[f"half_{side}"].name]["basis"] = list_m(face.frame(x + ex, eye_z + 0.004 * k + ez * 0.5, 0.0, scale=(EYE_W * 1.08 * k, 0.010 * k, EYE_H * 0.85 * k)))
            pf = e.get("pupil", 1.0)
            st[face.objs[f"pupil_{side}"].name]["basis"] = list_m(face.frame(x + gx * 0.013 * k, eye_z + gz * 0.011 * k, 0.012 * k,
                                                                             scale=(EYE_W * 0.55 * pf * k, 0.004 * k, EYE_H * 0.52 * pf * k)))
            raise_, tilt = (e["brow"][0], e["brow"][1]) if side == "L" else (e["brow"][2], e["brow"][3])
            spin = math.radians(tilt) * (1 if side == "L" else -1)
            st[face.objs[f"brow_{side}"].name]["basis"] = list_m(
                face.frame(x, eye_z + BROW_UP * k + raise_ * k, 0.004 * k, spin=spin, scale=(0.027 * k, 0.007 * k, 0.0095 * k)))
        st[gaze_anchor_name] = {"basis": list_m(Matrix.Translation(mid + gaze_dir((gx, gz))))}
        states[name] = st
    return states
