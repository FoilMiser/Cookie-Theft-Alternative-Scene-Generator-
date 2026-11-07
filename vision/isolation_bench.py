"""python vision/isolation_bench.py OUT [names...] : the isolation bench (v0.40 back to v0.23 cases; earlier cases in isolation_v012.md to v022.md).

BENCH_LIB=<dir> runs it against another variant library (the side-by-side readings swapped a pose in a copy).

Each weak visual is built on its own: one template forced alone into a picture (no other events), then
cropped around that template's own elements (or a setting element), so a reader judges that one thing.
Writes OUT/<name>.png (the crop) and OUT/<name>_full.png (the whole single-event picture)."""
import json, os, sys
_OUT0 = os.path.abspath(sys.argv[1])
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); os.chdir(ROOT)
from PIL import Image
from scenegen.library import Library
from scenegen.generate import build_one
from scenegen.planner import USAGE

OUT = _OUT0
ONLY = set(sys.argv[2:])
os.makedirs(OUT, exist_ok=True)
lib = Library(**({"cast_dir": os.environ["BENCH_CAST"]} if os.environ.get("BENCH_CAST") else {}), **({"lib_dir": os.environ["BENCH_LIB"]} if os.environ.get("BENCH_LIB") else {}))

# name: (setting, seed, forced templates, what to crop: "event", "full", or a setting element id or filler prefix,
#        accept rule or None)
BENCH = {
    # v0.40 (vision/flaws_v039.md): first three letters the thing, the fourth the drawing. O v0.39's cast and scene (BENCH_CAST=assets/cast/out039,
    # its library copied to tpdb_work/bench40/lib_O); N the v0.40 cast with every switch at B (BENCH_CAST=tpdb_work/bench40/out_N): the reach for the
    # blown hat with one hand (wh0), the hose in two hands (hi0), the goat's graze with its tuft ahead of the muzzle (gt0, at 90, 45 and 135), the walking
    # front foot flat (wk0 the boy with an ice cream, wd0 the grandfather and his dog); C the cast with TPDB_REACH40=C and TPDB_GRAZE40=C
    # (BENCH_CAST=tpdb_work/bench40/out_C); the heaps (hp0 the broom's, rk0 the raked pile) O v0.39's summer heap, D dry leaves, G cut grass
    "wh0O_1": ("garden", 40011, {"modules": ["windy_hat"]}, "event", None),
    "wh0O_2": ("park", 40012, {"modules": ["windy_hat"]}, "event", None),
    "wh0O_3": ("street", 40013, {"modules": ["windy_hat"]}, "event", None),
    "wh0N_1": ("garden", 40011, {"modules": ["windy_hat"]}, "event", None),
    "wh0N_2": ("park", 40012, {"modules": ["windy_hat"]}, "event", None),
    "wh0N_3": ("street", 40013, {"modules": ["windy_hat"]}, "event", None),
    "wh0C_1": ("garden", 40011, {"modules": ["windy_hat"]}, "event", None),
    "wh0C_2": ("park", 40012, {"modules": ["windy_hat"]}, "event", None),
    "wh0C_3": ("street", 40013, {"modules": ["windy_hat"]}, "event", None),
    "hi0O_1": ("garden", 40021, {"modules": ["blocked_hose"]}, "event", ("fam", "blocked_hose", ["person.tomas"])),
    "hi0O_2": ("garden", 40022, {"modules": ["blocked_hose"]}, "event", ("fam", "blocked_hose", ["person.tomas"])),
    "hi0N_1": ("garden", 40021, {"modules": ["blocked_hose"]}, "event", ("fam", "blocked_hose", ["person.tomas"])),
    "hi0N_2": ("garden", 40022, {"modules": ["blocked_hose"]}, "event", ("fam", "blocked_hose", ["person.tomas"])),
    "gt0O_1": ("park", 40031, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 90}}, "event", None),
    "gt0O_2": ("park", 40032, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 45}}, "event", None),
    "gt0O_3": ("park", 40033, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 135}}, "event", None),
    "gt0N_1": ("park", 40031, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 90}}, "event", None),
    "gt0N_2": ("park", 40032, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 45}}, "event", None),
    "gt0N_3": ("park", 40033, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 135}}, "event", None),
    "gt0C_1": ("park", 40031, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 90}}, "event", None),
    "gt0C_2": ("park", 40032, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 45}}, "event", None),
    "gt0C_3": ("park", 40033, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 135}}, "event", None),
    "wk0O_1": ("street", 40041, {"events": ["ice_cream"]}, "event", ("pose", "person.leo__walk_ice_cream")),
    "wk0O_2": ("park", 40042, {"events": ["ice_cream"]}, "event", ("pose", "person.leo__walk_ice_cream")),
    "wk0N_1": ("street", 40041, {"events": ["ice_cream"]}, "event", ("pose", "person.leo__walk_ice_cream")),
    "wk0N_2": ("park", 40042, {"events": ["ice_cream"]}, "event", ("pose", "person.leo__walk_ice_cream")),
    "wd0O_1": ("park", 40051, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.tomas"])),
    "wd0O_2": ("garden", 40052, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.tomas"])),
    "wd0N_1": ("park", 40051, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.tomas"])),
    "wd0N_2": ("garden", 40052, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.tomas"])),
    "hp0O_1": ("street", 40061, {"events": ["sweep"]}, "event", None),
    "hp0O_2": ("garden", 40062, {"events": ["sweep"]}, "event", None),
    "hp0D_1": ("street", 40061, {"events": ["sweep"]}, "event", None),
    "hp0D_2": ("garden", 40062, {"events": ["sweep"]}, "event", None),
    "hp0G_1": ("street", 40061, {"events": ["sweep"]}, "event", None),
    "hp0G_2": ("garden", 40062, {"events": ["sweep"]}, "event", None),
    "rk0O_1": ("garden", 40071, {"events": ["rake"]}, "event", None),
    "rk0D_1": ("garden", 40071, {"events": ["rake"]}, "event", None),
    "rk0D_2": ("garden", 40072, {"events": ["rake"]}, "event", None),
    "rk0G_1": ("garden", 40071, {"events": ["rake"]}, "event", None),
    "rk0G_2": ("garden", 40072, {"events": ["rake"]}, "event", None),
    # round 2 (BENCH_CAST=tpdb_work/bench40/out_C, the winners): the dry heap's leaves pointed with a midrib and a stalk, on round 1's seeds; the goat C
    # with its bite joined to the tuft, at the three angles
    "hp0D_3": ("street", 40061, {"events": ["sweep"]}, "event", None),
    "hp0D_4": ("garden", 40062, {"events": ["sweep"]}, "event", None),
    "rk0D_3": ("garden", 40071, {"events": ["rake"]}, "event", None),
    "rk0D_4": ("garden", 40072, {"events": ["rake"]}, "event", None),
    "gt0C_4": ("park", 40031, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 90}}, "event", None),
    "gt0C_5": ("park", 40032, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 45}}, "event", None),
    "gt0C_6": ("park", 40033, {"events": ["goat_grazing"], "yaws": {"goat_grazing": 135}}, "event", None),
    # v0.39 (Sam's figure-fixes-v038.md: the cast's people and animals redrawn, and the animals at revision 37's angles; the swept heap for summer).
    # First three letters the thing, the fourth the drawing: O v0.38's cast with the animals at 90 (BENCH_CAST=assets/cast/out038), N the v0.39 cast
    # with its switches (TPDB_ISECT39=B TPDB_SHOE39=D TPDB_MID39=B TPDB_BELT39=B TPDB_BEN39=C TPDB_QUAD39=B TPDB_ART39=B) at revision 37's angles;
    # the heap hp9 A autumn as v0.38, S summer, B grit, beside the raked pile rk9 S
    # round 3: the goat's coat, D v0.38's white on the redrawn goat, E brown all over with a white muzzle and beard (BENCH_CAST=tpdb_work/bench39/out_GD,
    # out_GE: out039 with the goat rebuilt with TPDB_GOAT39=D or E)
    "gt9D_1": ("park", 39181, {"events": ["goat_grazing"]}, "event", None),
    "gt9D_2": ("park", 39182, {"events": ["goat_grazing"]}, "event", None),
    "gt9D_3": ("park", 39183, {"events": ["goat_grazing"]}, "event", None),
    "gt9E_1": ("park", 39181, {"events": ["goat_grazing"]}, "event", None),
    "gt9E_2": ("park", 39182, {"events": ["goat_grazing"]}, "event", None),
    "gt9E_3": ("park", 39183, {"events": ["goat_grazing"]}, "event", None),
    # round 2: R the round-2 cast (BENCH_CAST=tpdb_work/bench39/out_R2: N with TPDB_MID39=C, no tuck, TPDB_BELT39=O, TPDB_GOAT39=C, the goat's legs
    # brown, and the spotted dog's spots on its flanks), on round 1's seeds of what it changes
    "wk9R_1": ("street", 39111, {"events": ["carry_bag"]}, "event", None),
    "wk9R_2": ("street", 39112, {"events": ["carry_bag"]}, "event", None),
    "hg9R_1": ("garden", 39131, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "hg9R_2": ("garden", 39132, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "hg9R_3": ("garden", 39133, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "dw9R_1": ("park", 39151, {"events": ["walk_dog"]}, "event", None),
    "dw9R_2": ("park", 39152, {"events": ["walk_dog"]}, "event", None),
    "gt9R_1": ("park", 39181, {"events": ["goat_grazing"]}, "event", None),
    "gt9R_2": ("park", 39182, {"events": ["goat_grazing"]}, "event", None),
    "gt9R_3": ("park", 39183, {"events": ["goat_grazing"]}, "event", None),
    "dp9R_1": ("park", 39191, {"events": ["dog_playing"]}, "event", None),
    "wk9O_1": ("street", 39111, {"events": ["carry_bag"]}, "event", None),
    "wk9O_2": ("street", 39112, {"events": ["carry_bag"]}, "event", None),
    "wk9N_1": ("street", 39111, {"events": ["carry_bag"]}, "event", None),
    "wk9N_2": ("street", 39112, {"events": ["carry_bag"]}, "event", None),
    "rd9O_1": ("park", 39121, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "rd9O_2": ("park", 39122, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "rd9N_1": ("park", 39121, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "rd9N_2": ("park", 39122, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "hg9O_1": ("garden", 39131, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "hg9O_2": ("garden", 39132, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "hg9O_3": ("garden", 39133, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "hg9N_1": ("garden", 39131, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "hg9N_2": ("garden", 39132, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "hg9N_3": ("garden", 39133, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.ben"])),
    "kk9O_1": ("park", 39141, {"events": ["kick_ball"]}, "event", None),
    "kk9N_1": ("park", 39141, {"events": ["kick_ball"]}, "event", None),
    "dw9O_1": ("park", 39151, {"events": ["walk_dog"]}, "event", None),
    "dw9O_2": ("park", 39152, {"events": ["walk_dog"]}, "event", None),
    "dw9N_1": ("park", 39151, {"events": ["walk_dog"]}, "event", None),
    "dw9N_2": ("park", 39152, {"events": ["walk_dog"]}, "event", None),
    "db9O_1": ("street", 39161, {"modules": ["dog_begs"]}, "event", None),
    "db9O_2": ("street", 39162, {"modules": ["dog_begs"]}, "event", None),
    "db9N_1": ("street", 39161, {"modules": ["dog_begs"]}, "event", None),
    "db9N_2": ("street", 39162, {"modules": ["dog_begs"]}, "event", None),
    "cs9O_1": ("park", 39171, {"modules": ["cat_stalks_bird"]}, "event", None),
    "cs9O_2": ("park", 39172, {"modules": ["cat_stalks_bird"]}, "event", None),
    "cs9N_1": ("park", 39171, {"modules": ["cat_stalks_bird"]}, "event", None),
    "cs9N_2": ("park", 39172, {"modules": ["cat_stalks_bird"]}, "event", None),
    "gt9O_1": ("park", 39181, {"events": ["goat_grazing"]}, "event", None),
    "gt9O_2": ("park", 39182, {"events": ["goat_grazing"]}, "event", None),
    "gt9O_3": ("park", 39183, {"events": ["goat_grazing"]}, "event", None),
    "gt9N_1": ("park", 39181, {"events": ["goat_grazing"]}, "event", None),
    "gt9N_2": ("park", 39182, {"events": ["goat_grazing"]}, "event", None),
    "gt9N_3": ("park", 39183, {"events": ["goat_grazing"]}, "event", None),
    "dp9O_1": ("park", 39191, {"events": ["dog_playing"]}, "event", None),
    "dp9N_1": ("park", 39191, {"events": ["dog_playing"]}, "event", None),
    "hp9A_1": ("street", 39201, {"events": ["sweep"]}, "event", None),
    "hp9A_2": ("street", 39202, {"events": ["sweep"]}, "event", None),
    "hp9S_1": ("street", 39201, {"events": ["sweep"]}, "event", None),
    "hp9S_2": ("street", 39202, {"events": ["sweep"]}, "event", None),
    "hp9B_1": ("street", 39201, {"events": ["sweep"]}, "event", None),
    "hp9B_2": ("street", 39202, {"events": ["sweep"]}, "event", None),
    "rk9S_1": ("garden", 39211, {"events": ["rake"]}, "event", None),
    "rk9S_2": ("garden", 39212, {"events": ["rake"]}, "event", None),
    # v0.38 (a basket of washing at the hanger's feet, by templates.BASKET38: hngO none as v0.37, hngB the basket, hngW the basket and the shirt dripping)
    "hngO_1": ("garden", 38111, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngO_2": ("garden", 38112, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngO_3": ("garden", 38113, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngB_1": ("garden", 38111, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngB_2": ("garden", 38112, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngB_3": ("garden", 38113, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngW_1": ("garden", 38111, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngW_2": ("garden", 38112, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngW_3": ("garden", 38113, {"events": ["hang_laundry"]}, "event", "laundry"),
    # round 2 (hngC the bundles drawn as cloth, a sleeve over the rim and the first drop forming on the hem; hngD the drops and no basket)
    "hngC_1": ("garden", 38111, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngC_2": ("garden", 38112, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngC_3": ("garden", 38113, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngD_1": ("garden", 38111, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngD_2": ("garden", 38112, {"events": ["hang_laundry"]}, "event", "laundry"),
    "hngD_3": ("garden", 38113, {"events": ["hang_laundry"]}, "event", "laundry"),
    # v0.36 (the grandfather under the bucket; the cast's switches by bench cast: bktM from TPDB_MOUSTACHE36=M, bktR from TPDB_BUCKET36=R, bktB both)
    # round 2: the moustache lying flatter (TPDB_MOUSTACHE36_FLAT=F) under the bucket, and the bold and flat ones in profile, kneeling to plant
    "bktF_1": ("garden", 36121, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktF_2": ("park", 36122, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktF_3": ("street", 36123, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "prfM_1": ("garden", 36131, {"events": ["plant_flowers"]}, "event", ("pose", "person.tomas__kneel_plant")),
    "prfM_2": ("park", 36132, {"events": ["plant_flowers"]}, "event", ("pose", "person.tomas__kneel_plant")),
    "prfM_3": ("garden", 36133, {"events": ["plant_flowers"]}, "event", ("pose", "person.tomas__kneel_plant")),
    "prfF_1": ("garden", 36131, {"events": ["plant_flowers"]}, "event", ("pose", "person.tomas__kneel_plant")),
    "prfF_2": ("park", 36132, {"events": ["plant_flowers"]}, "event", ("pose", "person.tomas__kneel_plant")),
    "prfF_3": ("garden", 36133, {"events": ["plant_flowers"]}, "event", ("pose", "person.tomas__kneel_plant")),
    "bktO_1": ("garden", 36111, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktO_2": ("park", 36112, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktO_3": ("street", 36113, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktM_1": ("garden", 36111, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktM_2": ("park", 36112, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktM_3": ("street", 36113, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktR_1": ("garden", 36111, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktR_2": ("park", 36112, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktR_3": ("street", 36113, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktB_1": ("garden", 36111, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktB_2": ("park", 36112, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    "bktB_3": ("street", 36113, {"contradictions": ["bucket_hat"]}, "event", ("pose", "person.tomas__bucket_hat")),
    # v0.35 (the swing swung out, by D.SWING35: swgO as v0.34, swgS 8 degrees and swgT 12 degrees in a wider frame)
    "swgO_1": ("garden", 35111, {"events": ["swing"]}, "event", None),
    "swgO_2": ("garden", 35112, {"events": ["swing"]}, "event", None),
    "swgO_3": ("garden", 35113, {"events": ["swing"]}, "event", None),
    "swgS_1": ("garden", 35111, {"events": ["swing"]}, "event", None),
    "swgS_2": ("garden", 35112, {"events": ["swing"]}, "event", None),
    "swgS_3": ("garden", 35113, {"events": ["swing"]}, "event", None),
    "swgT_1": ("garden", 35111, {"events": ["swing"]}, "event", None),
    "swgT_2": ("garden", 35112, {"events": ["swing"]}, "event", None),
    "swgT_3": ("garden", 35113, {"events": ["swing"]}, "event", None),
    # v0.34 (the woman in yellow seated reading; the cast's switches by bench cast: seaP from TPDB_SEAT34=P, seaH from TPDB_HAIR34=L, seaB both)
    "seaO_1": ("garden", 34111, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaO_2": ("park", 34112, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaO_3": ("street", 34113, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaP_1": ("garden", 34111, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaP_2": ("park", 34112, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaP_3": ("street", 34113, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaH_1": ("garden", 34111, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaH_2": ("park", 34112, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaH_3": ("street", 34113, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaB_1": ("garden", 34111, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaB_2": ("park", 34112, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    "seaB_3": ("street", 34113, {"events": ["read_bench"]}, "event", ("pose", "person.mei__sit_read")),
    # v0.33 (templates.HOSE33 and KICK33 by name: stp the stopped hose, kik the stuck rider's kick arcs)
    "stpO_1": ("garden", 33111, {"modules": ["blocked_hose"]}, "event", None),
    "stpO_2": ("garden", 33112, {"modules": ["blocked_hose"]}, "event", None),
    "stpO_3": ("garden", 33113, {"modules": ["blocked_hose"]}, "event", None),
    "stpF_1": ("garden", 33111, {"modules": ["blocked_hose"]}, "event", None),
    "stpF_2": ("garden", 33112, {"modules": ["blocked_hose"]}, "event", None),
    "stpF_3": ("garden", 33113, {"modules": ["blocked_hose"]}, "event", None),
    "stpP_1": ("garden", 33111, {"modules": ["blocked_hose"]}, "event", None),
    "stpP_2": ("garden", 33112, {"modules": ["blocked_hose"]}, "event", None),
    "stpP_3": ("garden", 33113, {"modules": ["blocked_hose"]}, "event", None),
    "kikO_1": ("playground", 33121, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikO_2": ("playground", 33122, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikO_3": ("playground", 33123, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikN_1": ("playground", 33121, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikN_2": ("playground", 33122, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikN_3": ("playground", 33123, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikB_1": ("playground", 33121, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikB_2": ("playground", 33122, {"modules": ["seesaw_heavy"]}, "event", None),
    "kikB_3": ("playground", 33123, {"modules": ["seesaw_heavy"]}, "event", None),
    # v0.32 (the cast's switches by bench cast: ridX and boxU from TPDB_LOW=X TPDB_BOX=U, ridF from TPDB_LOW=F)
    "ridO_1": ("playground", 32111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridO_2": ("playground", 32112, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridO_3": ("playground", 32113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridX_1": ("playground", 32111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridX_2": ("playground", 32112, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridX_3": ("playground", 32113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridF_1": ("playground", 32111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridF_2": ("playground", 32112, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridF_3": ("playground", 32113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridG_1": ("playground", 32111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridG_2": ("playground", 32112, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridG_3": ("playground", 32113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridB_1": ("playground", 32111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridB_2": ("playground", 32112, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridB_3": ("playground", 32113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridC_1": ("playground", 32111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridC_2": ("playground", 32112, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridC_3": ("playground", 32113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridH_1": ("playground", 32111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridH_2": ("playground", 32112, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridH_3": ("playground", 32113, {"modules": ["seesaw_heavy"]}, "event", None),
    "boxV_1": ("street", 32121, {"events": ["carry_box"]}, "event", None),
    "boxV_2": ("park", 32122, {"events": ["carry_box"]}, "event", None),
    "boxV_3": ("playground", 32123, {"events": ["carry_box"]}, "event", None),
    "boxO_1": ("street", 32121, {"events": ["carry_box"]}, "event", None),
    "boxO_2": ("park", 32122, {"events": ["carry_box"]}, "event", None),
    "boxO_3": ("playground", 32123, {"events": ["carry_box"]}, "event", None),
    "boxU_1": ("street", 32121, {"events": ["carry_box"]}, "event", None),
    "boxU_2": ("park", 32122, {"events": ["carry_box"]}, "event", None),
    "boxU_3": ("playground", 32123, {"events": ["carry_box"]}, "event", None),
    # v0.31 round 2
    "ridT_1": ("playground", 31111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridT_2": ("playground", 31112, {"events": ["seesaw"]}, "event", None),
    "ridT_3": ("playground", 31113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridT_4": ("playground", 31114, {"events": ["seesaw"]}, "event", None),
    "ridU_1": ("playground", 31111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridU_3": ("playground", 31113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridP_1": ("playground", 31111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridP_2": ("playground", 31112, {"events": ["seesaw"]}, "event", None),
    "ridP_3": ("playground", 31113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridP_4": ("playground", 31114, {"events": ["seesaw"]}, "event", None),
    "relN_1": ("garden", 31151, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    "relN_2": ("garden", 31152, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    # v0.31 (scene drawings by name, see the loop below). v0.31's ridO_1 to _3 (isolation_v031.md) are ridO31_1 to _3 here: v0.32 used the
    # same names for its own cases, and in a dict the later entry wins, so the file as v0.32 left it ran v0.31's cases under v0.32's names
    "ridO31_1": ("playground", 31111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridO31_2": ("playground", 31112, {"events": ["seesaw"]}, "event", None),
    "ridS_1": ("playground", 31111, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridS_2": ("playground", 31112, {"events": ["seesaw"]}, "event", None),
    "ridS_3": ("playground", 31113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridS_4": ("playground", 31114, {"events": ["seesaw"]}, "event", None),
    "ridO31_3": ("playground", 31113, {"modules": ["seesaw_heavy"]}, "event", None),
    "ridO_4": ("playground", 31114, {"events": ["seesaw"]}, "event", None),
    "vstB_1": ("garden", 31121, {"events": ["water_flowers"]}, "event", ("pose", "person.tomas")),
    "vstB_2": ("garden", 31122, {"events": ["rake"]}, "event", ("pose", "person.tomas")),
    "vstB_3": ("park", 31123, {"events": ["fishing"]}, "event", ("pose", "person.tomas")),
    "vstO_1": ("garden", 31121, {"events": ["water_flowers"]}, "event", ("pose", "person.tomas")),
    "vstO_2": ("garden", 31122, {"events": ["rake"]}, "event", ("pose", "person.tomas")),
    "vstO_3": ("park", 31123, {"events": ["fishing"]}, "event", ("pose", "person.tomas")),
    "sanO_1": ("playground", 31131, {"events": ["sandbox"]}, "event", None),
    "sanO_2": ("playground", 31132, {"events": ["sandbox"]}, "event", None),
    "sanM_1": ("playground", 31131, {"events": ["sandbox"]}, "event", None),
    "sanM_2": ("playground", 31132, {"events": ["sandbox"]}, "event", None),
    "sanM_3": ("playground", 31133, {"events": ["sandbox"]}, "event", None),
    "fshE_5": ("garden", 31141, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshE_6": ("park", 31142, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshL_1": ("garden", 31141, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshL_2": ("park", 31142, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshL_3": ("garden", 31143, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "relB_3": ("garden", 31151, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    "relM_1": ("garden", 31151, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    "relM_2": ("garden", 31152, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    "conO_1": ("street", 31161, {"events": ["dog_begs"]}, "event", None),
    "conO_2": ("park", 31162, {"events": ["ice_cream"]}, "event", None),
    "conB_1": ("street", 31161, {"events": ["dog_begs"]}, "event", None),
    "conB_2": ("park", 31162, {"events": ["ice_cream"]}, "event", None),
    "conB_3": ("playground", 31163, {"events": ["dog_begs"]}, "event", None),
    # v0.30 round 2
    "hosV_1": ("garden", 30141, {"events": ["hose_water"]}, "event", None),
    "hosV_2": ("garden", 30142, {"events": ["hose_water"]}, "event", None),
    "hosV_3": ("garden", 30143, {"events": ["hose_water"]}, "event", None),
    "fshF_3": ("garden", 30161, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshF_4": ("park", 30162, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshF_5": ("garden", 30163, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "relC_1": ("garden", 30171, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    "relC_2": ("garden", 30172, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    # v0.30 (scene drawings by name, see the loop below; the cast is v0.29's)
    "hosO_5": ("garden", 30141, {"events": ["hose_water"]}, "event", None),
    "hosO_6": ("garden", 30142, {"events": ["hose_water"]}, "event", None),
    "hosU_1": ("garden", 30141, {"events": ["hose_water"]}, "event", None),
    "hosU_2": ("garden", 30142, {"events": ["hose_water"]}, "event", None),
    "hosU_3": ("garden", 30143, {"events": ["hose_water"]}, "event", None),
    "fshO_3": ("garden", 30161, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshO_4": ("park", 30162, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshG_3": ("garden", 30161, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshG_4": ("park", 30162, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshE_3": ("garden", 30161, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshE_4": ("park", 30162, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "trpA_1": ("garden", 30121, {"modules": ["about_to_trip"]}, "event", None),
    "trpA_2": ("playground", 30122, {"modules": ["about_to_trip"]}, "event", None),
    "trpA_3": ("park", 30123, {"modules": ["about_to_trip"]}, "event", None),
    "trpN_1": ("garden", 30121, {"modules": ["about_to_trip"]}, "event", None),
    "trpN_2": ("playground", 30122, {"modules": ["about_to_trip"]}, "event", None),
    "trpN_3": ("park", 30123, {"modules": ["about_to_trip"]}, "event", None),
    "fedO_3": ("park", 30111, {"modules": ["ducks_bread"]}, "event", None),
    "fedO_4": ("park", 30112, {"modules": ["ducks_bread"]}, "event", None),
    "fedW_1": ("park", 30111, {"modules": ["ducks_bread"]}, "event", None),
    "fedW_2": ("park", 30112, {"modules": ["ducks_bread"]}, "event", None),
    "fedW_3": ("park", 30113, {"modules": ["ducks_bread"]}, "event", None),
    "relO_1": ("garden", 30171, {"events": ["rake"]}, "hose_reel", ("el", "hose_reel")),
    "relB_1": ("garden", 30171, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    "relB_2": ("garden", 30172, {"events": ["rake"]}, "hose_reel", ("el", "hose_tail")),
    # v0.29 round 3
    "hosT_1": ("garden", 29141, {"events": ["hose_water"]}, "event", None),
    "hosT_2": ("garden", 29142, {"events": ["hose_water"]}, "event", None),
    "trpY_1": ("street", 29121, {"modules": ["about_to_trip"]}, "event", None),
    "trpY_2": ("garden", 29122, {"modules": ["about_to_trip"]}, "event", None),
    "trpY_3": ("playground", 29124, {"modules": ["about_to_trip"]}, "event", None),
    "wanD_1": ("garden", 29131, {"modules": ["dog_wants_walk"]}, "waitingdog", None),
    # v0.29 round 2
    "fedE_1": ("park", 29111, {"modules": ["ducks_bread"]}, "event", None),
    "fedE_2": ("park", 29112, {"modules": ["ducks_bread"]}, "event", None),
    "fedL_1": ("park", 29111, {"modules": ["ducks_bread"]}, "event", None),
    "fedL_2": ("park", 29112, {"modules": ["ducks_bread"]}, "event", None),
    "trpX_1": ("street", 29121, {"modules": ["about_to_trip"]}, "event", None),
    "trpX_2": ("garden", 29122, {"modules": ["about_to_trip"]}, "event", None),
    "trpX_3": ("park", 29123, {"modules": ["about_to_trip"]}, "event", None),
    "wanC_1": ("garden", 29131, {"modules": ["dog_wants_walk"]}, "waitingdog", None),
    "wanC_2": ("garden", 29132, {"modules": ["dog_wants_walk"]}, "waitingdog", None),
    "hosS_1": ("garden", 29141, {"events": ["hose_water"]}, "event", None),
    "hosS_2": ("garden", 29142, {"events": ["hose_water"]}, "event", None),
    "hosS_3": ("garden", 29143, {"events": ["hose_water"]}, "event", None),
    "fshC_1": ("park", 29161, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshC_2": ("garden", 29162, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    # v0.29 (out_B = the new sleeping poses and the duck's new pose, on the v0.28 people; out_C = out_B and the back heel lifted less. Scene drawings by name, see the loop below)
    "slpO_1": ("garden", 29101, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_01"])),
    "slpO_2": ("park", 29102, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_02"])),
    "slpW_1": ("garden", 29101, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_01"])),
    "slpW_2": ("park", 29102, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_02"])),
    "slpB_1": ("garden", 29101, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_01"])),
    "slpB_2": ("park", 29102, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_02"])),
    "slpC_1": ("garden", 29101, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_01"])),
    "slpC_2": ("park", 29102, {"events": ["dog_sleeping"]}, "event", ("fam", "dog_sleeping", ["animal.dog_02"])),
    "fedO_1": ("park", 29111, {"modules": ["ducks_bread"]}, "event", None),
    "fedK_1": ("park", 29111, {"modules": ["ducks_bread"]}, "event", None),
    "fedK_2": ("park", 29112, {"modules": ["ducks_bread"]}, "event", None),
    "fedK_3": ("park", 29113, {"modules": ["ducks_bread"]}, "event", None),
    "trpO_3": ("street", 29121, {"modules": ["about_to_trip"]}, "event", None),
    "trpO_4": ("garden", 29122, {"modules": ["about_to_trip"]}, "event", None),
    "trpL_3": ("street", 29121, {"modules": ["about_to_trip"]}, "event", None),
    "trpL_4": ("garden", 29122, {"modules": ["about_to_trip"]}, "event", None),
    "trpW_3": ("street", 29121, {"modules": ["about_to_trip"]}, "event", None),
    "trpW_4": ("garden", 29122, {"modules": ["about_to_trip"]}, "event", None),
    "trpP_3": ("street", 29121, {"modules": ["about_to_trip"]}, "event", None),
    "trpP_4": ("garden", 29122, {"modules": ["about_to_trip"]}, "event", None),
    "wanO_1": ("garden", 29131, {"modules": ["dog_wants_walk"]}, "waitingdog", None),
    "wanB_1": ("garden", 29131, {"modules": ["dog_wants_walk"]}, "waitingdog", None),
    "wanB_2": ("garden", 29132, {"modules": ["dog_wants_walk"]}, "waitingdog", None),
    "hosO_1": ("garden", 29141, {"events": ["hose_water"]}, "event", None),
    "hosK_1": ("garden", 29141, {"events": ["hose_water"]}, "event", None),
    "hosK_2": ("garden", 29142, {"events": ["hose_water"]}, "event", None),
    "blkO_1": ("garden", 29151, {"modules": ["blocked_hose"]}, "event", None),
    "blkB_1": ("garden", 29151, {"modules": ["blocked_hose"]}, "event", None),
    "blkB_2": ("garden", 29152, {"modules": ["blocked_hose"]}, "event", None),
    "fshO_1": ("park", 29161, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshB_1": ("park", 29161, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "fshB_2": ("garden", 29162, {"contradictions": ["fish_in_tree"]}, "treefish", None),
    "heeO_1": ("street", 29171, {"events": ["walk_dog"]}, "event", None),
    "heeO_2": ("park", 29172, {"events": ["carry_bag"]}, "event", None),
    "heeC_1": ("street", 29171, {"events": ["walk_dog"]}, "event", None),
    "heeC_2": ("park", 29172, {"events": ["carry_bag"]}, "event", None),
    # v0.28 (out_O = the v0.27 cast; out_B = no brows over closed eyes, a smaller blush, a fuller beard. Scene drawings by name: splO the old scoop, splA a flat splat, splB a splat with
    # a low lump; shdO the old shadows; ssaO the old seesaw, ssaB riders further in with one shadow under the plank; balO the old ball and branch)
    "splO_1": ("park", 28101, {"modules": ["ice_cream_drop"]}, "event", None),
    "splO_2": ("street", 28102, {"modules": ["ice_cream_drop"]}, "event", None),
    "splA_1": ("park", 28101, {"modules": ["ice_cream_drop"]}, "event", None),
    "splA_2": ("street", 28102, {"modules": ["ice_cream_drop"]}, "event", None),
    "splB_1": ("park", 28101, {"modules": ["ice_cream_drop"]}, "event", None),
    "splB_2": ("street", 28102, {"modules": ["ice_cream_drop"]}, "event", None),
    "shdO_1": ("garden", 28111, {"events": ["dog_sleeping"]}, "event", None),
    "shdO_2": ("park", 28112, {"events": ["dig"]}, "event", None),
    "shdO_3": ("park", 28113, {"events": ["run"]}, "event", None),
    "shdO_4": ("garden", 28114, {"events": ["play_catch"]}, "event", None),
    "shdB_1": ("garden", 28111, {"events": ["dog_sleeping"]}, "event", None),
    "shdB_2": ("park", 28112, {"events": ["dig"]}, "event", None),
    "shdB_3": ("park", 28113, {"events": ["run"]}, "event", None),
    "shdB_4": ("garden", 28114, {"events": ["play_catch"]}, "event", None),
    "shdB_5": ("park", 28115, {"events": ["picnic"]}, "event", None),
    "shdB_6": ("street", 28116, {"events": ["walk_dog"]}, "event", None),
    "shdB_7": ("playground", 28117, {"events": ["jump"]}, "event", None),
    "shdB_8": ("playground", 28118, {"events": ["sandbox"]}, "event", None),
    "shdB_9": ("park", 28119, {"events": ["goat_grazing"]}, "event", None),
    "ssaO_1": ("playground", 28121, {"events": ["seesaw"]}, "event", None),
    "ssaB_1": ("playground", 28121, {"events": ["seesaw"]}, "event", None),
    "ssaB_2": ("playground", 28122, {"events": ["seesaw"]}, "event", None),
    "ssaB_3": ("playground", 28123, {"modules": ["seesaw_heavy"]}, "event", None),
    "balO_1": ("park", 28131, {"modules": ["ball_in_tree"]}, "ballintree", None),
    "balB_1": ("park", 28131, {"modules": ["ball_in_tree"]}, "ballintree", None),
    "balB_2": ("street", 28132, {"modules": ["ball_in_tree"]}, "ballintree", None),
    "brbB_1": ("playground", 28133, {"events": ["bird_perched"]}, "event", ("branchbird",)),
    "facO_1": ("park", 28141, {"events": ["picnic"]}, "event", None),
    "facO_2": ("park", 28142, {"events": ["ice_cream"]}, "event", ("pose", "__eat_ice_cream")),
    "facB_1": ("park", 28141, {"events": ["picnic"]}, "event", None),
    "facB_2": ("park", 28142, {"events": ["ice_cream"]}, "event", ("pose", "__eat_ice_cream")),
    "facB_3": ("street", 28143, {"events": ["ice_cream"]}, "event", ("pose", "__walk_ice_cream")),
    "brdO_1": ("street", 28151, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.dev"])),
    "brdB_1": ("street", 28151, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.dev"])),
    "brdB_2": ("park", 28152, {"events": ["fishing"]}, "event", ("fam", "fishing", ["person.dev"])),
    # v0.28 round 2: the branch on a limb from the trunk, the dog's mouth over the flat splat
    "lmbB_1": ("park", 28131, {"modules": ["ball_in_tree"]}, "ballintree", None),
    "lmbB_2": ("street", 28132, {"modules": ["ball_in_tree"]}, "ballintree", None),
    "lmbB_3": ("garden", 28134, {"modules": ["ball_in_tree"]}, "ballintree", None),
    "lmbB_4": ("playground", 28133, {"events": ["bird_perched"]}, "event", ("branchbird",)),
    "dogB_1": ("park", 28101, {"modules": ["ice_cream_drop"]}, "event", None),
    "dogB_2": ("street", 28102, {"modules": ["ice_cream_drop"]}, "event", None),
    "dogB_3": ("playground", 28103, {"modules": ["ice_cream_drop"]}, "event", None),
    "brdD_1": ("street", 28151, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.dev"])),
    "brdD_2": ("park", 28152, {"events": ["fishing"]}, "event", ("fam", "fishing", ["person.dev"])),
    "brdD_3": ("street", 28153, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.dev"])),
    "brdC_3": ("street", 28153, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.dev"])),
    # v0.27 round 2 (out_D = round 1's winners, a narrower corn broom, the scoop at the lips, the hand under the book, the lip-coloured mouth; out_E = out_D and shorter, thicker legs)
    "brmD_1": ("garden", 27131, {"events": ["sweep"]}, "event", ("fam", "sweep", ["person.tomas"])),
    "brmD_2": ("street", 27132, {"events": ["sweep"]}, "event", None),
    "brmD_3": ("garden", 27134, {"events": ["sweep"]}, "event", ("fam", "sweep", ["person.rosa"])),
    "brmR_2": ("garden", 27135, {"events": ["sweep", "rake"]}, "full", None),
    "icwD_1": ("street", 27201, {"events": ["ice_cream"]}, "event", ("pose", "person.dev__walk_ice_cream")),
    "icwD_2": ("park", 27202, {"events": ["ice_cream"]}, "event", ("pose", "__walk_ice_cream")),
    "trpD_1": ("street", 27111, {"modules": ["about_to_trip"]}, "event", ("fam", "about_to_trip", ["person.leo"])),
    "trpD_2": ("garden", 27112, {"modules": ["about_to_trip"]}, "event", None),
    "hosD_1": ("garden", 27151, {"events": ["hose_water"]}, "event", None),
    "bodD_1": ("street", 26102, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "bodD_2": ("garden", 26171, {"events": ["water_flowers"]}, "event", None),
    "bodD_3": ("playground", 26172, {"events": ["play_catch"]}, "event", None),
    "bodD_4": ("park", 27204, {"events": ["read_bench"]}, "event", None),
    "bodE_1": ("street", 26102, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "bodE_2": ("garden", 26171, {"events": ["water_flowers"]}, "event", None),
    "bodE_3": ("playground", 26172, {"events": ["play_catch"]}, "event", None),
    "bodE_4": ("park", 27204, {"events": ["read_bench"]}, "event", None),
    # v0.27 (out_O = the v0.26 drawings; out_B = the head turned in profile, the back heel lifted, the scoop at the mouth, the corn broom, the pecking bird's head out in front, a belt on the dress,
    # the hose hanging from the fist; out_C = out_B with the yard broom)
    "proO_1": ("park", 27101, {"events": ["fishing"]}, "event", ("fam", "fishing", ["person.tomas"])),
    "proO_2": ("garden", 27102, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.rosa"])),
    "proO_3": ("street", 27103, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.dev"])),
    "proO_4": ("garden", 27104, {"modules": ["kite_in_tree"]}, "event", None),
    "proB_1": ("park", 27101, {"events": ["fishing"]}, "event", ("fam", "fishing", ["person.tomas"])),
    "proB_2": ("garden", 27102, {"events": ["hang_laundry"]}, "event", ("fam", "hang_laundry", ["person.rosa"])),
    "proB_3": ("street", 27103, {"events": ["walk_dog"]}, "event", ("fam", "walk_dog", ["person.dev"])),
    "proB_4": ("garden", 27104, {"modules": ["kite_in_tree"]}, "event", None),
    "trpO_1": ("street", 27111, {"modules": ["about_to_trip"]}, "event", ("fam", "about_to_trip", ["person.leo"])),
    "trpO_2": ("garden", 27112, {"modules": ["about_to_trip"]}, "event", None),
    "trpB_1": ("street", 27111, {"modules": ["about_to_trip"]}, "event", ("fam", "about_to_trip", ["person.leo"])),
    "trpB_2": ("garden", 27112, {"modules": ["about_to_trip"]}, "event", None),
    "icrO_1": ("street", 27121, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.dev"])),
    "icrO_2": ("park", 27122, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.mei"])),
    "icrB_1": ("street", 27121, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.dev"])),
    "icrB_2": ("park", 27122, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.mei"])),
    "brmA_1": ("garden", 27131, {"events": ["sweep"]}, "event", ("fam", "sweep", ["person.tomas"])),
    "brmA_2": ("street", 27132, {"events": ["sweep"]}, "event", None),
    "brmB_1": ("garden", 27131, {"events": ["sweep"]}, "event", ("fam", "sweep", ["person.tomas"])),
    "brmB_2": ("street", 27132, {"events": ["sweep"]}, "event", None),
    "brmC_1": ("garden", 27131, {"events": ["sweep"]}, "event", ("fam", "sweep", ["person.tomas"])),
    "brmC_2": ("street", 27132, {"events": ["sweep"]}, "event", None),
    "brmR_1": ("garden", 27133, {"events": ["sweep", "rake"]}, "full", None),
    "pckO_1": ("playground", 27141, {"modules": ["cat_stalks_bird"]}, "event", None),
    "pckB_1": ("playground", 27141, {"modules": ["cat_stalks_bird"]}, "event", None),
    "pckB_2": ("park", 27142, {"events": ["feed_birds"]}, "event", None),
    "hosB_1": ("garden", 27151, {"events": ["hose_water"]}, "event", None),
    "hosB_2": ("garden", 27152, {"modules": ["blocked_hose"]}, "event", None),
    "pkgB_1": ("garden", 27161, {"modules": ["sprinkler_package"]}, "package", None),
    "pkgB_2": ("park", 27162, {"modules": ["sprinkler_package"]}, "package", None),
    "digB_1": ("park", 27171, {"events": ["dig"]}, "event", None),
    "digB_2": ("garden", 27172, {"events": ["dig"]}, "event", None),
    "drsO_1": ("street", 27191, {"events": ["carry_box"]}, "event", ("fam", "carry_box", ["person.mei"])),
    "drsB_1": ("street", 27191, {"events": ["carry_box"]}, "event", ("fam", "carry_box", ["person.mei"])),
    # v0.26 (BENCH_CAST/BENCH_LIB name the bench cast: out_A = old A, teen C, reading dog A, feed A; out_B = old B, teen D, reading dog B,
    # feed B; out_C = old C)
    "oldA_1": ("park", 26101, {"events": ["fishing"]}, "event", ("fam", "fishing", ["person.tomas"])),
    "oldA_2": ("street", 26102, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "oldB_1": ("park", 26101, {"events": ["fishing"]}, "event", ("fam", "fishing", ["person.tomas"])),
    "oldB_2": ("street", 26102, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "oldC_1": ("park", 26101, {"events": ["fishing"]}, "event", ("fam", "fishing", ["person.tomas"])),
    "oldC_2": ("street", 26102, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "rdgA_1": ("park", 26106, {"contradictions": ["dog_reading"]}, "event", ("fam", "dog_reading", ["animal.dog_01"])),
    "rdgA_2": ("street", 26110, {"modules": ["ice_cream_drop"], "contradictions": ["dog_reading"]}, "dog_reading", ("fam", "dog_reading", ["animal.dog_02"])),
    "rdgB_1": ("park", 26106, {"contradictions": ["dog_reading"]}, "event", ("fam", "dog_reading", ["animal.dog_01"])),
    "rdgB_2": ("street", 26110, {"modules": ["ice_cream_drop"], "contradictions": ["dog_reading"]}, "dog_reading", ("fam", "dog_reading", ["animal.dog_02"])),
    "teeC_1": ("playground", 26121, {"events": ["kick_ball"]}, "event", ("fam", "kick_ball", ["person.leo"])),
    "teeC_2": ("park", 26122, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.leo"])),
    "teeD_1": ("playground", 26121, {"events": ["kick_ball"]}, "event", ("fam", "kick_ball", ["person.leo"])),
    "teeD_2": ("park", 26122, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.leo"])),
    # draw.SWEEP26: A leaves, B dust
    "swpA_1": ("garden", 26131, {"events": ["sweep"]}, "event", None),
    "swpA_2": ("street", 26132, {"events": ["sweep"]}, "event", None),
    "swpB_1": ("garden", 26131, {"events": ["sweep"]}, "event", None),
    "swpB_2": ("street", 26132, {"events": ["sweep"]}, "event", None),
    "wanN_1": ("garden", 26141, {"modules": ["dog_wants_walk"]}, (0, 470, 420, 890), None),
    "wanN_2": ("garden", 26142, {"modules": ["dog_wants_walk"]}, (0, 470, 420, 890), None),
    "fedA_1": ("park", 26151, {"modules": ["ducks_bread"]}, "event", None),
    "fedA_2": ("park", 26152, {"events": ["feed_birds"]}, "event", None),
    "fedB_1": ("park", 26151, {"modules": ["ducks_bread"]}, "event", None),
    "fedB_2": ("park", 26152, {"events": ["feed_birds"]}, "event", None),
    "casA_1": ("playground", 26161, {"events": ["sandbox"]}, "event", None),
    "casA_2": ("playground", 26162, {"events": ["sandbox"]}, "event", None),
    # round 2 (out_E = the winners, a fan broom, the reading dog's tail up; out_F = out_E and fuller bodies)
    "swpC_1": ("garden", 26131, {"events": ["sweep"]}, "event", None),
    "swpC_2": ("street", 26132, {"events": ["sweep"]}, "event", None),
    "rdgC_1": ("park", 26106, {"contradictions": ["dog_reading"]}, "event", ("fam", "dog_reading", ["animal.dog_01"])),
    "rdgC_2": ("street", 26110, {"modules": ["ice_cream_drop"], "contradictions": ["dog_reading"]}, "dog_reading", ("fam", "dog_reading", ["animal.dog_02"])),
    "bodO_1": ("street", 26102, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "bodO_2": ("garden", 26171, {"events": ["water_flowers"]}, "event", None),
    "bodO_3": ("playground", 26172, {"events": ["play_catch"]}, "event", None),
    "bodA_1": ("street", 26102, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "bodA_2": ("garden", 26171, {"events": ["water_flowers"]}, "event", None),
    "bodA_3": ("playground", 26172, {"events": ["play_catch"]}, "event", None),
    # v0.25 (BENCH_CAST/BENCH_LIB name the bench cast: out_A = bag A and roller A, out_B = bag B and roller B)
    "bagA_1": ("park", 25101, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "bagA_2": ("street", 25102, {"events": ["carry_bag"]}, "event", None),
    "bagB_1": ("park", 25101, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "bagB_2": ("street", 25102, {"events": ["carry_bag"]}, "event", None),
    "rolA_1": ("garden", 25103, {"events": ["paint_fence"]}, "event", None),
    "rolA_2": ("garden", 25104, {"events": ["paint_fence"]}, "event", None),
    "rolB_1": ("garden", 25103, {"events": ["paint_fence"]}, "event", None),
    "rolB_2": ("garden", 25104, {"events": ["paint_fence"]}, "event", None),
    # draw.BARROW_SHADOW25: A 130 px wide, B 160 (v0.24: 200)
    "barA_1": ("garden", 25105, {"events": ["rake"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
    "barB_1": ("garden", 25105, {"events": ["rake"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
    # draw.PAW25: the newspaper dog's paws on the tan dog and the white one
    "pawA_1": ("park", 25106, {"contradictions": ["dog_reading"]}, "event", ("fam", "dog_reading", ["animal.dog_01"])),
    "pawA_2": ("street", 25110, {"modules": ["ice_cream_drop"], "contradictions": ["dog_reading"]}, "dog_reading", ("fam", "dog_reading", ["animal.dog_02"])),
    "pawB_1": ("park", 25106, {"contradictions": ["dog_reading"]}, "event", ("fam", "dog_reading", ["animal.dog_01"])),
    "pawB_2": ("street", 25110, {"modules": ["ice_cream_drop"], "contradictions": ["dog_reading"]}, "dog_reading", ("fam", "dog_reading", ["animal.dog_02"])),
    # round 2: the paper behind the dog, its own paws on it
    "pawC_1": ("park", 25106, {"contradictions": ["dog_reading"]}, "event", ("fam", "dog_reading", ["animal.dog_01"])),
    "pawC_2": ("street", 25110, {"modules": ["ice_cream_drop"], "contradictions": ["dog_reading"]}, "dog_reading", ("fam", "dog_reading", ["animal.dog_02"])),
    # draw.BIRD25: A 0.8 of its size, B 0.68
    "birA_1": ("park", 25108, {"modules": ["bird_steals"]}, "event", None),
    "birA_2": ("street", 25109, {"modules": ["bird_steals"]}, "event", None),
    "birB_1": ("park", 25108, {"modules": ["bird_steals"]}, "event", None),
    "birB_2": ("street", 25109, {"modules": ["bird_steals"]}, "event", None),
    # v0.24 (BENCH_CAST/BENCH_LIB name the bench cast: out_tA = cap, out_tB = backpack; none = the v0.23 teenager)
    # the teenager, kicking and with a child at play: never called a teenager in the v0.23 screen
    "teenO_1": ("playground", 24101, {"events": ["kick_ball"]}, "event", ("fam", "kick_ball", ["person.leo"])),
    "teenO_2": ("park", 24102, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.leo"])),
    "teenA_1": ("playground", 24101, {"events": ["kick_ball"]}, "event", ("fam", "kick_ball", ["person.leo"])),
    "teenA_2": ("park", 24102, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.leo"])),
    "teenB_1": ("playground", 24101, {"events": ["kick_ball"]}, "event", ("fam", "kick_ball", ["person.leo"])),
    "teenB_2": ("park", 24102, {"events": ["ice_cream"]}, "event", ("fam", "ice_cream", ["person.leo"])),
    # riders on the seesaw and the slide: O as v0.23; the number is draw.RIDE24 (px up from the seat point; px down from the chute)
    "seeO_1": ("playground", 24111, {"events": ["seesaw"]}, "event", None),
    "seeA_1": ("playground", 24111, {"events": ["seesaw"]}, "event", None),
    "seeB_1": ("playground", 24111, {"events": ["seesaw"]}, "event", None),
    "sliO_1": ("playground", 24121, {"events": ["slide"]}, "event", None),
    "sliA_1": ("playground", 24121, {"events": ["slide"]}, "event", None),
    "sliB_1": ("playground", 24121, {"events": ["slide"]}, "event", None),
    # round 2 (out_sU = arms up and ahead, out_sH = hands holding the chute's sides; both at the round 1 winner, slide 0 px)
    "sliU_1": ("playground", 24131, {"events": ["slide"]}, "event", ("fam", "slide", ["person.kai"])),
    "sliU_2": ("playground", 24132, {"events": ["slide"]}, "event", ("fam", "slide", ["person.nia"])),
    "sliH_1": ("playground", 24131, {"events": ["slide"]}, "event", ("fam", "slide", ["person.kai"])),
    "sliH_2": ("playground", 24132, {"events": ["slide"]}, "event", ("fam", "slide", ["person.nia"])),
    # v0.23 round 1 (BENCH_CAST/BENCH_LIB name the bench cast: out_b1 = pan B, beg A, head A; out_b2 = pan C, head B)
    # the frying pan held out by the end of its handle, over a flower bed: B face toward the viewer, C tipped to pour
    "panB_1": ("garden", 23101, {"contradictions": ["pan_watering"]}, "event", None),
    "panB_2": ("garden", 23102, {"contradictions": ["pan_watering"]}, "event", None),
    "panC_1": ("garden", 23103, {"contradictions": ["pan_watering"]}, "event", None),
    "panC_2": ("garden", 23104, {"contradictions": ["pan_watering"]}, "event", None),
    # the dog begging, sitting up on its haunches with both front paws folded at the chest
    "begA_1": ("street", 23105, {"modules": ["dog_begs"]}, "event", None),
    "begA_2": ("park", 23106, {"modules": ["dog_begs"]}, "event", None),
    # the older man walking in profile: A the grey fringe kept to the back of the head; B also a fuller nose
    "headA_1": ("park", 23107, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "headA_2": ("street", 23108, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "headB_1": ("park", 23109, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    "headB_2": ("street", 23110, {"events": ["carry_bag"]}, "event", ("fam", "carry_bag", ["person.tomas"])),
    # the garden's wheelbarrow on a thin strut with a small flat foot (draw.LEG23)
    "leg_1": ("garden", 23111, {"events": ["rake"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
    "leg_2": ("garden", 23112, {"events": ["sweep"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
    # round 2 (out_b3 = pan D, beg A2; out_b4 = pan E): D the pan seen from above at a slant, deeper, on a handle about as
    # long as the pan is wide; E as the v0.19 pan (face toward the viewer) on that shorter, thicker handle, held out;
    # the beg with the hind legs folded under; the barrow's strut with no foot (draw.LEG23 = "strut")
    "panD_1": ("garden", 23201, {"contradictions": ["pan_watering"]}, "event", None),
    "panD_2": ("garden", 23202, {"contradictions": ["pan_watering"]}, "event", None),
    "panE_1": ("garden", 23203, {"contradictions": ["pan_watering"]}, "event", None),
    "panE_2": ("garden", 23204, {"contradictions": ["pan_watering"]}, "event", None),
    "begA2_1": ("street", 23205, {"modules": ["dog_begs"]}, "event", None),
    "begA2_2": ("park", 23206, {"modules": ["dog_begs"]}, "event", None),
    "strut_1": ("garden", 23207, {"events": ["rake"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
    "strut_2": ("garden", 23208, {"events": ["sweep"]}, "filler_wheelbarrow", ("el", "filler_wheelbarrow")),
}


def crop_box(rec, what, tids=()):
    els = {e["id"]: e for e in rec["elements"]}
    if what == "event":
        ids = {i for it in rec["items"] if it.get("template") in tids for i in it["elements"]}
        # plus everything the event drew (setting-role svgs keyed to it are listed in the record too)
        boxes = [els[i]["bbox"] for i in ids if i in els and els[i].get("bbox")]
        boxes += [e["bbox"] for e in rec["elements"] if e.get("bbox") and e["id"].startswith(("sweepheap", "toyball", "wavelines", "gusts", "seeds", "dustpan", "crownleaves", "speedlines"))]
        if "kite_in_tree" in tids:
            # the whole crown the kite hangs from
            boxes += [e["bbox"] for e in rec["elements"] if e.get("bbox") and e["id"] == "tree"]
    else:
        boxes = [e["bbox"] for e in rec["elements"] if e.get("bbox") and (e["id"] == what or e["id"].startswith(what))]
    x0, y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
    x1, y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    w, h = max(x1 - x0 + 160, 420), max(y1 - y0 + 140, 340)
    return (int(max(0, cx - w / 2)), int(max(0, cy - h / 2)), int(min(1600, cx + w / 2)), int(min(1000, cy + h / 2)))


def fams_of(rec, tid):
    els = {e["id"]: e for e in rec["elements"]}
    return {els[i]["asset"]["variant"].split("__")[0] for it in rec["items"] if it.get("template") == tid
            for i in it["elements"] if i in els and els[i].get("asset")}


def accepted(rec, rule):
    if rule is None:
        return True
    els = {e["id"]: e for e in rec["elements"]}
    if isinstance(rule, tuple):
        if rule[0] == "fam":
            return bool(fams_of(rec, rule[1]) & set(rule[2]))
        if rule[0] == "pose":
            return any(rule[1] in e.get("asset", {}).get("variant", "") for e in rec["elements"])
        if rule[0] == "el":
            return any(e["id"].startswith(rule[1]) for e in rec["elements"])
        if rule[0] == "obj":
            return any(it.get("template") == "about_to_trip" and rule[1] in it["text"] for it in rec["items"])
        if rule[0] == "branchbird":
            return any(it.get("template") == "bird_perched" and "branch" in it["text"] for it in rec["items"])
        if rule[0] == "fencebird":
            return any(it.get("template") == "bird_perched" and "fence" in it["text"] for it in rec["items"]) and \
                any(e["id"] == "clothesline" for e in rec["elements"])
        if rule[0] == "railbird":
            return any(it.get("template") == "bird_perched" and "fence" in it["text"] for it in rec["items"])
        if rule[0] == "noreel":
            return not any(e["id"] == "hose_reel" for e in rec["elements"])
        if rule[0] == "fencecat":
            return any(it.get("template") == "cat_stalks_bird" and "on the fence" in it["text"] for it in rec["items"])
        if rule[0] == "backrow":
            return any(e.get("asset", {}).get("family", "").startswith("person.") and e["bbox"][3] < 700 for e in rec["elements"] if e.get("bbox"))
    if rule == "kidwave":
        return any(it.get("template") == "wave" and any("child" in str(els[i].get("asset", {}).get("labels", {}).get("category", "")) for i in it["elements"] if i in els)
                   for it in rec["items"])
    if rule == "laundry":
        return any(e["id"] == "laundry" for e in rec["elements"])
    return True


import re as _re
from scenegen import draw as _D
import scenegen.library as _L0
import scenegen.settings as _Q0
import scenegen.templates as _T0
# v0.32: the release's value of every versioned switch (NAME23 ... NAME32). The prefix block below sets each switch by name prefix, with defaults that
# were older drawings, so a case that matched no prefix got them (v0.31's new cases took the old obstacle and the old duck; v0.32's would have taken the
# v0.30 seesaw). The v0.32 cases are reset to these, then set by name.
_REL = {(m, k): getattr(m, k) for m in (_D, _L0, _Q0, _T0) for k in dir(m) if _re.fullmatch(r"[A-Z_]+\d\d", k)}
NEW32 = {n for n in BENCH if n[:4] in ("ridO", "ridX", "ridF", "ridG", "ridB", "ridC", "ridH", "boxO", "boxU", "boxV") and BENCH[n][1] // 1000 in (32, 33)}
NEW33 = {n for n in BENCH if n[:3] in ("stp", "kik") and BENCH[n][1] // 1000 == 33}
NEW34 = {n for n in BENCH if n[:3] == "sea" and BENCH[n][1] // 1000 == 34}
NEW35 = {n for n in BENCH if n[:3] == "swg" and BENCH[n][1] // 1000 == 35}
NEW36 = {n for n in BENCH if n[:3] in ("bkt", "prf") and BENCH[n][1] // 1000 == 36}
NEW38 = {n for n in BENCH if n[:3] == "hng" and BENCH[n][1] // 1000 == 38}
NEW39 = {n for n in BENCH if n[2] == "9" and BENCH[n][1] // 1000 == 39}
NEW40 = {n for n in BENCH if n[2] == "0" and BENCH[n][1] // 1000 == 40}
# v0.33: a case name used twice is refused (v0.32's ridO_1 to _3 were silently replaced by v0.31's, written further down)
import ast as _ast
_keys = [k.value for n_ in _ast.walk(_ast.parse(open(os.path.abspath(__file__), encoding="utf-8").read()))
         if isinstance(n_, _ast.Assign) and getattr(n_.targets[0], "id", None) == "BENCH" for k in n_.value.keys]
_dup = sorted({k for k in _keys if _keys.count(k) > 1})
if _dup:
    sys.exit(f"bench case names used twice: {_dup}")
for name, (st, seed, forced, what, rule) in BENCH.items():
    if ONLY and name not in ONLY:
        continue
    for (m, k), v in _REL.items():
        setattr(m, k, v)
    if name.startswith("sq"):
        _D.SQUARE_STYLE20 = name[2]
    _D.LEG23 = "strut" if name.startswith("strut") else name.startswith("leg")
    _D.RIDE24 = {"seesaw": {"seeA": 10, "seeB": 18}.get(name[:4], 0), "slide": {"sliA": 0, "sliB": -8, "sliU": 0, "sliH": 0}.get(name[:4], 8)}
    _D.BARROW_SHADOW25 = {"barA": 130, "barB": 160}.get(name[:4], _D.BARROW_SHADOW25)
    _D.PAW25 = {"pawA": "A", "pawB": "B", "pawC": "C"}.get(name[:4], _D.PAW25)
    _D.BIRD25 = {"birA": 0.8, "birB": 0.68}.get(name[:4], _D.BIRD25)
    _D.SWEEP26 = {"swpA": "A", "swpB": "B"}.get(name[:4], _D.SWEEP26)
    _D.SPLAT28 = {"splO": "O", "splA": "A", "splB": "B"}.get(name[:4], "A")
    _D.SEESAW_IN28 = 0 if name.startswith("ssaO") else 22
    import scenegen.library as _L
    _L.SHADOW28 = "O" if name[:4] in ("shdO", "ssaO") else "B"
    _L.SHADOW29 = "W" if name.startswith("slpW") else "O"
    import scenegen.templates as _T
    _T.SLEEP29 = {"slpO": "O", "slpW": "O", "slpB": "B", "slpC": "C"}.get(name[:4], "B")
    _T.TRIP29 = {"trpL": "L", "trpW": "W", "trpP": "P", "trpX": "W", "trpY": "W", "trpA": "W", "trpN": "W"}.get(name[:4], "O")
    _T.TRIP_OBJ29 = "bucket" if name[:4] in ("trpO", "trpL") else None
    _T.DUCK29 = {"fedO": "O", "fedL": "L", "fedW": "L"}.get(name[:4], "B")
    if name in ("fedO_3", "fedO_4"):
        _T.DUCK29 = "L"
    _T.DOOR29 = "B" if name.startswith(("wanB", "wanC", "wanD")) else "O"
    _T.HOSE29 = "O" if name == "hosO_1" else "B"
    _T.BULGE29 = "O" if name.startswith("blkO") else "B"
    _T.FISH29 = "O" if name in ("fshO_1", "fshO_2") else "B"
    _T.HOSE30 = {"hosU": "U", "hosV": "V"}.get(name[:4], "O")
    _T.FISH30 = {"fshG": "G", "fshE": "E", "fshF": "F", "fshL": "E"}.get(name[:4], "O")
    _T.TRIP_W30 = {"trpN": 60}.get(name[:4], 72)
    _T.CRUMB30 = "W" if name.startswith("fedW") else "O"
    _T.SEESAW31 = {"ridS": "S", "ridT": "T", "ridU": "U", "ridP": "P"}.get(name[:4], "O")
    _T.CASTLE31 = 26 if name.startswith("sanO") else 52
    _T.LIMB31 = "L" if name.startswith("fshL") else "O"
    _Q_ = __import__("scenegen.settings", fromlist=["x"])
    _Q_.REEL31 = {"relM": (24, 0), "relN": (16, 16)}.get(name[:4], (0, 0))
    import scenegen.settings as _Q
    _Q.REEL30 = "B" if name.startswith(("relB", "relC", "relM", "relN")) else "O"
    if name in NEW32:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
        _T0.LOW32 = {"ridF": "F", "ridB": "B", "ridC": "B"}.get(name[:4], "O")
        _T0.LOW_RISE_B32 = 12 if name.startswith("ridC") else 5
        _T0.STUCK32 = 8 if name[:4] in ("ridX", "ridF", "ridG", "ridB", "ridC") else 14
        _T0.HANDLE32 = "H" if name.startswith("ridH") else "O"
    if name in NEW33:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
        _T0.HOSE33 = name[3] if name.startswith("stp") else _T0.HOSE33
        _T0.KICK33 = name[3] if name.startswith("kik") else _T0.KICK33
    if name in NEW34:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
    if name in NEW35:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
        _D.SWING35 = name[3]
    if name in NEW36:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
    if name in NEW38:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
        _T0.BASKET38 = name[3]
    if name in NEW39:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
        _T0.YAW39 = "O" if name[3] == "O" else "B"
        if name[:3] in ("hp9", "rk9"):
            _D.HEAP39 = name[3]
    if name in NEW40:
        for (m, k), v in _REL.items():
            setattr(m, k, v)
        if name[3] == "O":
            # v0.39's scene: its heap, its tuft, no least height for the ice-cream eater
            _D.HEAP40, _T0.TUFT40, _T0.ICE40 = "S", "O", 0
        elif name[:3] in ("hp0", "rk0"):
            _D.HEAP40 = name[3]
    rec = None
    for k in range(40):
        USAGE.clear()
        r_, sc, fin = build_one(lib, 3, st, seed + 1000 * k, os.path.join(OUT, "_scenes"), forced=forced, require_band=False, max_tries=8, log=lambda *a: None)
        if r_ and accepted(r_, rule):
            rec = r_
            break
    if not rec:
        print(name, "FAIL", flush=True)
        continue
    png = os.path.join(OUT, "_scenes", rec["name"] + ".png")
    im = Image.open(png).convert("RGB")
    if what == "full":
        im.save(os.path.join(OUT, name + ".png"))
        print(name, rec["name"], "full", flush=True)
        continue
    try:
        if isinstance(what, tuple):
            box = what
        elif what == "event":
            box = crop_box(rec, "event", [t for v in forced.values() for t in v])
        elif what in ("wave", "dog_reading"):
            box = crop_box(rec, "event", [what])
        else:
            box = crop_box(rec, what)
    except ValueError:
        print(name, "NO ELEMENT", what, flush=True)
        continue
    im.crop(box).save(os.path.join(OUT, name + ".png"))
    im.save(os.path.join(OUT, name + "_full.png"))
    print(name, rec["name"], box, flush=True)
