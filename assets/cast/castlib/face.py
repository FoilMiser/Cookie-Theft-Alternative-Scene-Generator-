"""Face kit v2: features on an ellipsoid head, and the expressions that toggle and move them.

Every part is built once. An expression is a set of visible parts plus rest-space
transforms (eye glance, brow height and tilt, eye size), stored per object, so the
renderer can switch expressions without rebuilding anything. Glances also move the
ANCHOR_gaze_target empty, so "looks at" checks follow the eyes.
"""
import math

import bpy  # noqa: F401
from mathutils import Matrix, Quaternion, Vector

from .core import HEAD48, capsule_arc, ellipsoid, half_ellipsoid, head_f, head_fy, head_g, list_m, nrm, smooth_curve, tube, upd


class Face:
    """Features on the front (-Y) of an ellipsoid head with center c and radii (ax, ay, az)."""

    def __init__(self, rig, bone, c, radii, k=1.0, prefix="F", n=2.0):
        self.rig, self.bone, self.c, self.k, self.p = rig, bone, Vector(c), k, prefix
        self.ax, self.ay, self.az = radii
        self.n = n          # v0.47: the head's level sections |x|^n + |y|^n = r^n (core.squircle); 2 is the ellipsoid
        self.objs = {}
        self.xoff = 0.0     # v0.48 (PROF48): features built while this is set lie that far round the face

    def surf(self, x, z):
        if HEAD48 == "B":
            # v0.48: the head's own surface (core.head_pt): narrower and carried forward below the cheeks
            n = self.n
            zs = max(-0.999, min(0.999, z / self.az))
            f = head_f(zs)
            u = max(1e-4, 1 - zs * zs) ** (n / 2) - abs(x / (self.ax * f)) ** n
            return Vector((x, -self.ay * (head_fy(zs) * max(1e-4, u) ** (1.0 / n) + head_g(zs)), z))
        if self.n != 2.0:
            n = self.n
            u = max(1e-4, 1 - (z / self.az) ** 2) ** (n / 2) - abs(x / self.ax) ** n
            return Vector((x, -self.ay * max(1e-4, u) ** (1.0 / n), z))
        u = 1 - (x / self.ax) ** 2 - (z / self.az) ** 2
        y = -self.ay * math.sqrt(max(1e-4, u))
        return Vector((x, y, z))

    def normal(self, x, z):
        if HEAD48 == "B":
            e = 2e-4
            return nrm((self.surf(x + e, z) - self.surf(x - e, z)).cross(self.surf(x, z + e) - self.surf(x, z - e)))
        p = self.surf(x, z)
        if self.n != 2.0:
            n = self.n
            xs, ys, zs = p.x / self.ax, p.y / self.ay, p.z / self.az
            return nrm(Vector((math.copysign(abs(xs) ** (n - 1), xs) / self.ax, math.copysign(abs(ys) ** (n - 1), ys) / self.ay,
                               zs * max(1e-4, 1 - zs * zs) ** (n / 2 - 1) / self.az)))
        return nrm(Vector((p.x / self.ax ** 2, p.y / self.ay ** 2, p.z / self.az ** 2)))

    def at(self, x, z, out=0.0):
        x = x + self.xoff
        return self.c + self.surf(x, z) + self.normal(x, z) * out

    def frame(self, x, z, out, spin=0.0, scale=(1, 1, 1)):
        """World matrix for a feature lying flat on the skin: local -Y = outward normal."""
        n = self.normal(x + self.xoff, z)
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

    def side(self, s, y, z, out=0.0):
        """v0.48: a point on the side of the head (s: 1 the figure's left, -1 its right) at depth y and height z, `out` off the skin."""
        n = self.n
        zs = max(-0.999, min(0.999, z / self.az))
        f = head_f(zs)
        yy = y + self.ay * head_g(zs)
        u = max(1e-4, 1 - zs * zs) ** (n / 2) - abs(yy / (self.ay * head_fy(zs, yy > 0))) ** n
        return self.c + Vector((s * (self.ax * f * max(1e-4, u) ** (1.0 / n) + out), y, z))

    def curve_on(self, key, pts2d, radius, matkey, out):
        pts = [self.at(x, z, out) for x, z in pts2d]
        return self.obj(key, tube(key, pts, radius, matkey, self.rig, self.bone))


# Sizes in head units (k = character scale); bigger than v0.3 so faces read at scene size.
EYE_W, EYE_H = 0.0235, 0.0355
BROW_UP = 0.058
MOUTH_DZ = -0.086
MOUTH_W = 0.034
LINE = 0.0072
BROW_SC = (0.027, 0.007, 0.0095)
# v0.48 (TPDB_FACE48; vision/isolation_v048.md): the face on the egg head (core.HEAD48). "B": the features spread down the taller face, the
# eyes just under the middle of the head and a little smaller, the brows longer and heavier with a clear gap over the eyes, the nose lower,
# and the mouth lower and wider, one plain line in the lip colour with no dark edge under it (v0.46's edged line drew a smile as an angular
# red shape: lipstick on every face). "O": v0.47's face
FACE48 = __import__("os").environ.get("TPDB_FACE48", "B")
# v0.48 (TPDB_PROF48 "B"; pair bench 2, vision/isolation_v048.md): a side view has a face of its own. The eyes and the mouth lie on the front
# of the head, so in a side view they are seen edge on: turned 15 degrees toward the viewer the reviewers had "the single eye sits on the
# very front edge of the face outline, partly cut off", "no eye is visible, so the face looks empty and could be read as the back of the
# head", "no mouth drawn; the face is mostly ear and glasses". As a draughtsman does in a profile, the near eye and its brow are set further
# round the cheek (PROF48_EYE, in head units), the mouth likewise (PROF48_MOUTH), and the far eye and brow are left out. render_assets uses
# these states (`expression_states_profile`) for a side view whose pose has the side view's twin. "O": one face for every view
PROF48 = __import__("os").environ.get("TPDB_PROF48", "B") if FACE48 == "B" and HEAD48 == "B" else "O"
PROF48_EYE = float(__import__("os").environ.get("TPDB_PROF48_EYE", "0.034"))
PROF48_MOUTH = float(__import__("os").environ.get("TPDB_PROF48_MOUTH", "0.024"))
if FACE48 == "B":
    EYE_W, EYE_H = 0.0205, 0.0290
    BROW_UP = 0.054
    MOUTH_DZ = -0.099
    MOUTH_W = 0.038
    BROW_SC = (0.029, 0.007, 0.0098)


# v0.46 bench (TPDB_CLEAN46 "B"; vision/isolation_v046.md): the glasses a plain dark wire of the line's own weight with no outline of
# its own (a thin wire outlined on both sides: in profile the far lens stood past the face as a black disc)
GLASS46 = __import__("os").environ.get("TPDB_CLEAN46", "B")
# (second round, TPDB_GLASSW46 "B": the wire a fifth thicker. At the inner lines' weight the frames were "thin, light lines on a small
# face" beside v0.45's, the one pair a reviewer gave to the old cast. "C", half as thick again, closed the far lens to a black disc
# in a three-quarter view, the fault the plain wire was drawn to end; "O" keeps the first round's wire)
GLASSW46 = {"O": (0.0072, 0.0065), "B": (0.0086, 0.0076), "C": (0.0105, 0.0090)}[__import__("os").environ.get("TPDB_GLASSW46", "B")]
# (after round 3, TPDB_MOUTH46: a mouth drawn as a line is a plain line in its own colour, thicker, with no outline of its own. The
# heavier line closed over the lip colour, and near the edge of a face in profile the outer line ran into it: beside v0.45's "open red
# smiling mouth" the new one was "a small dark mark with dots around the chin that look like dirt or stubble", one of the two cut-outs a
# reviewer gave to the old cast. The value is the line's thickness against v0.45's ("B" was a trial, thinner than the old line with its
# outline); "O" keeps the outlined line, and so does the darkest skin, where the lip colour alone is too near the skin's own grey)
# (after round 4, "D": the plain line read as a mouth where round 3's had been "a dark smudge", three cut-outs of twelve, but beside
# v0.45's it was "a red smudge on the cheek beside the nose, too large and off to the side, which can read as a cut or blood", "a bit
# like lipstick on a man", "partly outside the outline": a thick mark of one flat colour in a drawing where every other shape has a
# dark edge. "D" is v0.45's mouth again, a thin line in the lip colour with a thin dark edge, but the edge is a second, wider line
# under it and not Line Art, so neither of the two line weights can close over it or thicken it at the edge of a face. Every skin.)
MOUTH46 = {"O": None, "B": 1.45, "C": 1.8, "D": "rim"}[__import__("os").environ.get("TPDB_MOUTH46", "D")]
# v0.47 (TPDB_GLASS47): on the squarer head (people.HEAD47) a rim laid point by point on the skin wrapped round the head's corner, its
# outer half spread wide and the eye against its inner side: in a three-quarter view the near lens was mostly dark, a pair of dark
# glasses at scene size. Each rim is now a flat ring centred on its eye: (half-width, half-height, degrees the lens's plane is turned
# outward from the skin's own at the eye, distance off the skin), in head units. "O" keeps the rim laid on the skin. Benches glB to glF
# (person.rosa at 0, 45 and 90 degrees and her head-down poses): B, C and D, the ring alone, changed little, because the eye was as large
# as the lens's opening; E and F also draw the eyes smaller, and F is the one in which skin shows round each eye in every view.
GLASS47 = __import__("os").environ.get("TPDB_GLASS47", "F")
GLASS47_GEOM = {"B": (0.045, 0.041, 0.0, 0.013), "C": (0.045, 0.041, 10.0, 0.013), "D": (0.049, 0.044, 6.0, 0.013),
                "E": (0.049, 0.044, 6.0, 0.013), "F": (0.046, 0.043, 6.0, 0.013)}
# (and the eyes behind them drawn smaller by this factor, so that skin shows between eye and rim: an eye as large as its lens is a dark lens)
GLASS47_EYE = {"E": 0.84, "F": 0.76}
if FACE48 == "B":
    # v0.48: the glasses' wire lighter and the rims a little smaller (at v0.46's weight on the smaller face the two rims were the face)
    GLASSW46 = (0.0062, 0.0056)
    GLASS47_GEOM = dict(GLASS47_GEOM, F=(0.043, 0.040, 6.0, 0.013))
    GLASS47_EYE = dict(GLASS47_EYE, F=0.84)


def build_people_face(face, eye_dx, eye_z, k, glasses=False, blush_key="pink", skin_key="skin1", mouth_col=None):
    ek = face.ek = GLASS47_EYE.get(GLASS47, 1.0) if glasses else 1.0      # v0.47 (TPDB_GLASS47): smaller eyes behind glasses
    bsc = face.bsc = tuple(a * b for a, b in zip(BROW_SC, getattr(face, "brow_k", (1.0, 1.0, 1.0))))      # v0.48: a face's own brows
    EW, EH = EYE_W * ek, EYE_H * ek
    for side, s in (("L", 1), ("R", -1)):
        x = s * eye_dx
        face.place(f"eye_{side}", ellipsoid("eye", (0, 0, 0), (1, 1, 1), "outline"),
                   face.frame(x, eye_z, 0.0, scale=(EW * k, 0.010 * k, EH * k)))
        cobj = face.place(f"catch_{side}", ellipsoid("catch", (0, 0, 0), (1, 1, 1), "cream"),
                          face.frame(x + 0.008 * k * ek, eye_z + 0.013 * k * ek, 0.016 * k, scale=(0.0085 * k * ek, 0.004 * k, 0.0110 * k * ek)))
        cobj.lineart.usage = "EXCLUDE"
        face.place(f"half_{side}", half_ellipsoid("half", "outline"),
                   face.frame(x, eye_z + 0.004 * k, 0.0, scale=(EW * 1.08 * k, 0.010 * k, EH * 0.85 * k)))
        face.place(f"white_{side}", ellipsoid("white", (0, 0, 0), (1, 1, 1), "cream"),
                   face.frame(x, eye_z, 0.002 * k, scale=(EW * 1.30 * k, 0.010 * k, EH * 1.12 * k)))
        face.place(f"pupil_{side}", ellipsoid("pupil", (0, 0, 0), (1, 1, 1), "outline"),
                   face.frame(x, eye_z, 0.012 * k, scale=(EW * 0.55 * k, 0.004 * k, EH * 0.52 * k)))
        w = EW * 1.35 * k
        face.curve_on(f"arcup_{side}", smooth_curve([(x - w, eye_z - 0.016 * k), (x, eye_z + 0.017 * k), (x + w, eye_z - 0.016 * k)], 6),
                      LINE * 1.05 * k, "outline", 0.004 * k)
        face.curve_on(f"arcup2_{side}", smooth_curve([(x - w * 1.05, eye_z - 0.020 * k), (x - w * 0.15, eye_z + 0.020 * k), (x + w * 1.05, eye_z - 0.006 * k)], 6),
                      LINE * 1.25 * k, "outline", 0.004 * k)
        face.curve_on(f"arcdn_{side}", smooth_curve([(x - w, eye_z + 0.006 * k), (x, eye_z - 0.014 * k), (x + w, eye_z + 0.006 * k)], 6),
                      LINE * 1.05 * k, "outline", 0.004 * k)
        if PROF48 == "B" and side == "R":
            # the side view's own arcs for the near eye (the eye's other shapes are moved by the states)
            face.xoff = s * PROF48_EYE * k
            face.curve_on(f"p_arcup_{side}", smooth_curve([(x - w, eye_z - 0.016 * k), (x, eye_z + 0.017 * k), (x + w, eye_z - 0.016 * k)], 6),
                          LINE * 1.05 * k, "outline", 0.004 * k)
            face.curve_on(f"p_arcup2_{side}", smooth_curve([(x - w * 1.05, eye_z - 0.020 * k), (x - w * 0.15, eye_z + 0.020 * k), (x + w * 1.05, eye_z - 0.006 * k)], 6),
                          LINE * 1.25 * k, "outline", 0.004 * k)
            face.curve_on(f"p_arcdn_{side}", smooth_curve([(x - w, eye_z + 0.006 * k), (x, eye_z - 0.014 * k), (x + w, eye_z + 0.006 * k)], 6),
                          LINE * 1.05 * k, "outline", 0.004 * k)
            face.xoff = 0.0
        face.place(f"brow_{side}", capsule_arc("brow", "outline", bend=0.30),
                   face.frame(x, eye_z + BROW_UP * k, 0.004 * k, scale=tuple(a * k for a in bsc)))
        # v0.28, TPDB_BLUSH: smaller, nearer the eye ("a pink smudge on the cheek, which could be blush or ice cream")
        bl28 = __import__("os").environ.get("TPDB_BLUSH", "B") == "B"
        face.place(f"blush_{side}", ellipsoid("blush", (0, 0, 0), (1, 1, 1), blush_key),
                   face.frame(s * (eye_dx + (0.022 if bl28 else 0.030) * k), eye_z - (0.036 if bl28 else 0.044) * k, 0.001 * k,
                              scale=((0.015 if bl28 else 0.024) * k, 0.004 * k, (0.008 if bl28 else 0.013) * k)))

    def mouths(pre):
        mz = eye_z + MOUTH_DZ * k
        mw = MOUTH_W * k
        # v0.27, chosen on the bench: thinner, in a lip colour (a black line near the edge of the face: "a dark mark around the mouth could be a mouth or a small beard or moustache", four cut-outs)
        m27 = __import__("os").environ.get("TPDB_MOUTH", "B") == "B"
        lw = LINE * k * (0.86 if m27 else 1.0)
        mc = "throat" if m27 else "outline"
        if mouth_col:
            mc, lw = mouth_col, lw * 1.15      # v0.43 (TPDB_ADULT43): lips, a line in a lip colour
        out = 0.003 * k

        rim = MOUTH46 == "rim"
        plain = MOUTH46 if skin_key != "skin3" and not rim else None

        def mline(key, pts, r):
            if FACE48 == "B":
                # v0.48: one plain line, in the lip colour (the outline's on the darkest skin, where the lip colour is too near the skin's grey)
                # (pair bench 1: in the lip colour a turned face's mouth was "a small red mark", "a smear"; a dark brown line is a mouth)
                ob = face.curve_on(key, pts, r * 1.12, "outline" if skin_key == "skin3" else "hair_brown_dark", 0.004 * k)
                ob.lineart.usage = "EXCLUDE"
                return ob
            if rim:
                # the dark edge: a wider line sunk into the face by half its radius, a little longer than the lip-coloured line at both
                # ends, so that about 2.5 px of it show round the lip colour at render size, half the weight of the lines inside the
                # figure, as v0.45's edge was (the head's surface lies about 0.003 above the ellipsoid the features are set on; 0.6 sunk
                # and no longer than the lip line, the first two trials, drew a finer and shorter mark than v0.45's). The lip-coloured
                # line rides on its top.
                rr = r + 0.0108 * k
                ext = 0.006 * k

                def beyond(p, q):
                    dx, dz = p[0] - q[0], p[1] - q[1]
                    n = (dx * dx + dz * dz) ** 0.5 or 1.0
                    return (p[0] + dx / n * ext, p[1] + dz / n * ext)

                p2 = [(q[0], q[1]) for q in pts]
                ob = face.curve_on(key + "_rim", [beyond(p2[0], p2[1])] + p2 + [beyond(p2[-1], p2[-2])], rr, "outline", -0.5 * rr)
                ob.lineart.usage = "EXCLUDE"
                ob = face.curve_on(key, pts, r, mc, 0.5 * rr - 0.3 * r)
                ob.lineart.usage = "EXCLUDE"
                return ob
            ob = face.curve_on(key, pts, r * (plain or 1.0), mc, out)
            if plain:
                ob.lineart.usage = "EXCLUDE"
            return ob

        if FACE48 == "B":
            mline(pre + "m_smile", smooth_curve([(-mw, mz + 0.011 * k), (-mw * 0.55, mz - 0.004 * k), (0, mz - 0.010 * k), (mw * 0.55, mz - 0.004 * k),
                                           (mw, mz + 0.011 * k)], 6), lw)
        else:
            mline(pre + "m_smile", smooth_curve([(-mw, mz + 0.009 * k), (0, mz - 0.011 * k), (mw, mz + 0.009 * k)], 8), lw)
        mline(pre + "m_frown", smooth_curve([(-mw, mz - 0.011 * k), (0, mz + 0.007 * k), (mw, mz - 0.011 * k)], 8), lw)
        # neutral: a short, thin, barely curved line set low (a straight bar under the nose reads as a moustache)
        mline(pre + "m_flat", smooth_curve([(-mw * 0.62, mz - 0.004 * k), (0, mz - 0.008 * k), (mw * 0.62, mz - 0.004 * k)], 6), lw * 0.78)
        mline(pre + "m_wobble", smooth_curve([(-mw * 0.72, mz + 0.002 * k), (-mw * 0.36, mz + 0.011 * k), (0, mz), (mw * 0.36, mz - 0.011 * k), (mw * 0.72, mz - 0.002 * k)], 6), lw * 0.72)
        mline(pre + "m_slant", [(-mw * 0.20, mz - 0.006 * k), (mw * 0.78, mz + 0.008 * k)], lw * 0.80)
        mline(pre + "m_smirk", smooth_curve([(-mw * 0.85, mz - 0.003 * k), (0.1 * mw, mz - 0.006 * k), (mw * 0.95, mz + 0.012 * k)], 8), lw)
        mline(pre + "m_disgust", smooth_curve([(-mw * 0.85, mz - 0.012 * k), (-0.25 * mw, mz + 0.006 * k), (0.40 * mw, mz - 0.003 * k), (mw * 0.90, mz + 0.004 * k)], 6), lw * 0.78)
        face.place(pre + "m_grin", half_ellipsoid("grin", "throat"), face.frame(0, mz + 0.010 * k, 0.0, scale=(mw * 1.30, 0.010 * k, 0.030 * k)))
        face.place(pre + "m_laugh", half_ellipsoid("laugh", "throat"), face.frame(0, mz + 0.012 * k, 0.0, scale=(mw * 1.45, 0.010 * k, 0.042 * k)))
        face.place(pre + "m_tongue", ellipsoid("tongue", (0, 0, 0), (1, 1, 1), "red"), face.frame(0, mz - 0.020 * k, 0.003 * k, scale=(mw * 0.62, 0.004 * k, 0.012 * k)))
        face.place(pre + "m_O", ellipsoid("O", (0, 0, 0), (1, 1, 1), "throat"), face.frame(0, mz - 0.006 * k, 0.0, scale=(0.017 * k, 0.010 * k, 0.022 * k)))
        if __import__("os").environ.get("TPDB_CALL44", "A") == "A":     # v0.44 bench (vision/isolation_v044.md): A
            # v0.44 (TPDB_CALL44): wider open, so the call shows at scene size ("a 4 px o")
            face.place(pre + "m_ooh", ellipsoid("ooh", (0, 0, 0), (1, 1, 1), "throat"), face.frame(0, mz - 0.012 * k, 0.0, scale=(0.021 * k, 0.010 * k, 0.037 * k)))
        else:
            face.place(pre + "m_ooh", ellipsoid("ooh", (0, 0, 0), (1, 1, 1), "throat"), face.frame(0, mz - 0.010 * k, 0.0, scale=(0.015 * k, 0.010 * k, 0.030 * k)))
        face.place(pre + "m_o", ellipsoid("o", (0, 0, 0), (1, 1, 1), "outline"), face.frame(0, mz, 0.0, scale=(0.009 * k, 0.008 * k, 0.011 * k)))
        face.place(pre + "m_teeth", ellipsoid("teeth", (0, 0, 0), (1, 1, 1), "cream"), face.frame(0, mz - 0.002 * k, 0.001 * k, scale=(mw * 1.05, 0.010 * k, 0.012 * k)))
        face.curve_on(pre + "m_teeth_line", [(-mw * 0.92, mz - 0.002 * k), (mw * 0.92, mz - 0.002 * k)], lw * 0.55, "outline", 0.010 * k)

    mouths("")
    if PROF48 == "B":
        # the side view's own mouths, the same shapes set round toward the near cheek (the figure's right)
        face.xoff = -PROF48_MOUTH * k
        mouths("p_")
        face.xoff = 0.0

    if glasses and GLASS47 != "O":
        # v0.47 (TPDB_GLASS47): each rim a flat ring, centred on its eye, in a plane that stands off the face as a lens does
        rx, rz, wrap, off = GLASS47_GEOM[GLASS47]
        inner = {}
        for side, s in (("L", 1), ("R", -1)):
            x = s * eye_dx
            q = Vector((0, -1, 0)).rotation_difference(face.normal(x, eye_z))
            q = Quaternion((0, 0, 1), s * math.radians(wrap)) @ q
            ex, ez, nn = q @ Vector((1, 0, 0)), q @ Vector((0, 0, 1)), q @ Vector((0, -1, 0))
            P0 = face.c + face.surf(x, eye_z) + nn * off * k
            ring = [P0 + ex * (rx * k * math.cos(a)) + ez * (rz * k * math.sin(a)) for a in [i / 32 * 2 * math.pi for i in range(32)]]
            ob = face.obj(f"glass_{side}", tube(f"glass_{side}", ring, GLASSW46[0] * k, "outline", face.rig, face.bone, closed=True))
            ob.lineart.usage = "EXCLUDE"
            inner[side] = P0 - ex * (s * rx * k) + ez * (0.008 * k)
            if FACE48 == "B" and HEAD48 == "B":
                # v0.48: an arm from each rim back along the temple to the ear: seen from the side, what says glasses is the arm
                outer = P0 + ex * (s * rx * k) + ez * (0.006 * k)
                arm = [outer, face.side(s, -0.045 * k, eye_z + 0.010 * k, 0.010 * k), face.side(s, 0.0, eye_z + 0.012 * k, 0.008 * k),
                       face.side(s, 0.030 * k, eye_z + 0.006 * k, 0.006 * k)]
                ob = face.obj(f"glass_arm_{side}", tube(f"glass_arm_{side}", smooth_curve(arm, 5), GLASSW46[1] * 0.9 * k, "outline", face.rig, face.bone))
                ob.lineart.usage = "EXCLUDE"
        ob = face.obj("glass_bridge", tube("glass_bridge", [inner["R"], (inner["R"] + inner["L"]) / 2 + Vector((0, -0.003 * k, 0.003 * k)), inner["L"]],
                                           GLASSW46[1] * k, "outline", face.rig, face.bone))
        ob.lineart.usage = "EXCLUDE"
        if PROF48 == "B":
            # v0.48: the side view's own near rim, centred on the near eye where the side view's face has it, and its arm
            s = -1
            x = s * (eye_dx + PROF48_EYE * k)
            q = Vector((0, -1, 0)).rotation_difference(face.normal(x, eye_z))
            ex, ez, nn = q @ Vector((1, 0, 0)), q @ Vector((0, 0, 1)), q @ Vector((0, -1, 0))
            P0 = face.c + face.surf(x, eye_z) + nn * off * k
            ring = [P0 + ex * (rx * k * math.cos(a)) + ez * (rz * k * math.sin(a)) for a in [i / 32 * 2 * math.pi for i in range(32)]]
            ob = face.obj("p_glass_R", tube("p_glass_R", ring, GLASSW46[0] * k, "outline", face.rig, face.bone, closed=True))
            ob.lineart.usage = "EXCLUDE"
            outer = P0 + ex * (s * rx * k) + ez * (0.006 * k)
            arm = [outer, face.side(s, -0.020 * k, eye_z + 0.011 * k, 0.009 * k), face.side(s, 0.012 * k, eye_z + 0.010 * k, 0.007 * k),
                   face.side(s, 0.034 * k, eye_z + 0.005 * k, 0.006 * k)]
            ob = face.obj("p_glass_arm_R", tube("p_glass_arm_R", smooth_curve(arm, 5), GLASSW46[1] * 0.9 * k, "outline", face.rig, face.bone))
            ob.lineart.usage = "EXCLUDE"
    elif glasses:
        for side, s in (("L", 1), ("R", -1)):
            x = s * eye_dx
            ring = [(x + 0.042 * k * math.cos(a), eye_z + 0.038 * k * math.sin(a))
                    for a in [i / 28 * 2 * math.pi for i in range(28)]]
            ob = face.curve_on(f"glass_{side}", ring, (GLASSW46[0] if GLASS46 == "B" else 0.0045) * k, "outline", 0.018 * k)
            ob.data.splines[0].use_cyclic_u = True
            if GLASS46 == "B":
                ob.lineart.usage = "EXCLUDE"
        ob = face.curve_on("glass_bridge", [(-eye_dx + 0.042 * k, eye_z + 0.008 * k), (eye_dx - 0.042 * k, eye_z + 0.008 * k)],
                           (GLASSW46[1] if GLASS46 == "B" else 0.004) * k, "outline", 0.020 * k)
        if GLASS46 == "B":
            ob.lineart.usage = "EXCLUDE"


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

# v0.44 bench (figure-review-v043.md item 18, TPDB_CONTENT44): the "content" face's closed lids under low brows merge into "><", brain freeze or
# crying, in all nine content renders (mostly eating ice cream). "A": the happy face's upward arcs, the brows a little raised and level. "O": v0.43
CONTENT44 = __import__("os").environ.get("TPDB_CONTENT44", "A")  # v0.44 (vision/isolation_v044.md; read in the design tests): A
if CONTENT44 == "A":
    PEOPLE_EXPRESSIONS["content"] = dict(eyes="happy", brow=(0.006, 0, 0.006, 0), mouth="m_smile", blush=True)

GLANCE_YAW_DEG, GLANCE_PITCH_DEG = 24.0, 20.0


def gaze_dir(look):
    gx, gz = look
    yaw, pitch = math.radians(gx * GLANCE_YAW_DEG), math.radians(gz * GLANCE_PITCH_DEG)
    return Vector((math.sin(yaw) * math.cos(pitch), -math.cos(yaw) * math.cos(pitch), math.sin(pitch)))


def people_expression_states(face, eye_dx, eye_z, k, gaze_anchor_name="ANCHOR_gaze_target", extra_show=(), profile=False):
    """profile (v0.48, PROF48): the states of a side view's face: the near eye and brow set round the cheek, the side view's own mouths,
    and nothing of the far eye."""
    states = {}
    pshift = PROF48_EYE * k if profile and "p_arcup_R" in face.objs else 0.0
    arc = "p_arc" if pshift else "arc"
    ek = getattr(face, "ek", 1.0)
    EW, EH = EYE_W * ek, EYE_H * ek
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
            show |= {"arcup_L", arc + "up_R"}
        elif eyes == "laugh":
            show |= {"arcup2_L", arc + "up2_R"}
        elif eyes == "closed":
            show |= {"arcdn_L", arc + "dn_R"}
        show |= {("p_" if profile else "") + key for key in MOUTHS[e["mouth"]]}
        show |= {key + "_rim" for key in MOUTHS[e["mouth"]] if key + "_rim" in face.objs}      # v0.46, TPDB_MOUTH46 "D": the line's dark edge
        # v0.28, TPDB_BROW: no brows over closed eyes, which drew two dark lines to each eye ("dark marks around the eye and mouth area", "a slightly muddled drawing of her features")
        if not (eyes == "closed" and __import__("os").environ.get("TPDB_BROW", "B") == "B"):
            show |= {"brow_L", "brow_R"}
        if e.get("blush"):
            show |= {"blush_L", "blush_R"}
        if profile and "p_glass_R" in face.objs:
            # (pair bench 3, of the glasses in a side view: "the glasses hang at the very edge of the head and look partly off the face")
            # the side view's own near rim, round the cheek with its eye, and its arm; nothing of the far rim or the bridge
            show |= {"p_glass_R", "p_glass_arm_R"}
        else:
            show |= {key for key in face.objs if key.startswith("glass")}
        # v0.36: the bold moustache in every expression (every face part not named here is hidden, and the thin moustache, named
        # nowhere, has been hidden in every render since it was first built)
        show |= {key for key in face.objs if key.startswith("p_mustache36" if profile and "p_mustache36" in face.objs else "mustache36")}
        if profile:
            # nothing of the far eye: its edge showed past the bridge of the nose as a sliver
            show -= {key for key in show if key.endswith("_L") and not key.startswith("glass")}
        for key, ob in face.objs.items():
            st[ob.name] = {"hide": key not in show}
        f = e.get("eye", 1.0)
        for side, s in (("L", 1), ("R", -1)):
            x = s * eye_dx + (s * pshift if side == "R" else 0.0)
            if eyes == "narrow":
                st[face.objs[f"eye_{side}"].name]["basis"] = list_m(face.frame(x + ex, eye_z - 0.005 * k + ez, 0.0, scale=(EW * 1.10 * k, 0.010 * k, EH * 0.42 * k)))
                st[face.objs[f"catch_{side}"].name]["hide"] = True
            else:
                st[face.objs[f"eye_{side}"].name]["basis"] = list_m(face.frame(x + ex, eye_z + ez, 0.0, scale=(EW * f * k, 0.010 * k, EH * f * k)))
                st[face.objs[f"catch_{side}"].name]["basis"] = list_m(face.frame(x + ex + 0.008 * k * f * ek, eye_z + ez + 0.013 * k * f * ek, 0.016 * k, scale=(0.0085 * k * f * ek, 0.004 * k, 0.0110 * k * f * ek)))
            st[face.objs[f"half_{side}"].name]["basis"] = list_m(face.frame(x + ex, eye_z + 0.004 * k + ez * 0.5, 0.0, scale=(EW * 1.08 * k, 0.010 * k, EH * 0.85 * k)))
            pf = e.get("pupil", 1.0)
            st[face.objs[f"pupil_{side}"].name]["basis"] = list_m(face.frame(x + gx * 0.013 * k, eye_z + gz * 0.011 * k, 0.012 * k,
                                                                             scale=(EW * 0.55 * pf * k, 0.004 * k, EH * 0.52 * pf * k)))
            raise_, tilt = (e["brow"][0], e["brow"][1]) if side == "L" else (e["brow"][2], e["brow"][3])
            spin = math.radians(tilt) * (1 if side == "L" else -1)
            st[face.objs[f"brow_{side}"].name]["basis"] = list_m(
                face.frame(x, eye_z + BROW_UP * k + raise_ * k, 0.004 * k, spin=spin, scale=tuple(a * k for a in getattr(face, "bsc", BROW_SC))))
        st[gaze_anchor_name] = {"basis": list_m(Matrix.Translation(mid + gaze_dir((gx, gz))))}
        states[name] = st
    return states
