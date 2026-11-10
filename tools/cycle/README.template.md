# TPDB v0.45: a larger ice cream, a camera on a strap, a trowel, a roller, a kite's reel, a picnic with its food, a duck in the water and a balloon let go, read a forty-second time

v0.44 ended with 63 of 64 templates through the gate: `ice_cream` fell at 0.85 in 13 pictures, on the girl in pink's cone when she walks with it in profile, "a small pink thing", "a tiny pink dot". Sam's brief for v0.45 was the drawings: improve the visuals, find the flaws and fix them. The work list came from two places:
- `vision/flaws_v044.md`: the ice cream (R1), the camera "or binoculars" (R2), the lost balloon held "by its very tip" (R3), the thief bird (R4) and a walker's "black ice skates" (O2);
- a fresh look at v0.44's pictures and cut-outs by four reviewers, each with a share of the set or the library (`tpdb_work/review45/`). They named what the readers had not: a duck standing on the water, a picnic with no food, a hose inspector looking away from the viewer, a trowel that was a grey line, a roller that was "a paddle", a carried box the fence's colour.

What two or more of the reviewers named, or a reviewer and the flaws list, was drawn. v0.45 benched the changes in whole pictures, v0.44's drawing beside v0.45's on the same seed, in two rounds, and took all of them (builder 0.45.0):
- **The ice cream:** cone and scoop half as big again in a child's hand, a third in a teenager's and a fifth in an adult's, the cone the wood's brown and longer above the fist, the scoop below and in front of the mouth; the empty cone larger in a child's and a teenager's hand too.
- **The camera:** a fifth larger, with a prism hump, a longer lens in a wide silver ring and a bright strap hanging in a loop under it.
- **The shoes:** the sole plate no longer than the shoe's flat underside and no wider than the shoe, dark under every shoe (under a walker's tipped foot it stood clear of the toe and the heel like a blade).
- **The hose inspector's head** toward the viewer and a little down at the nozzle (v0.44's turned it away, a sign error).
- **The props:** the trowel a broad pointed blade seen from its side on a bright handle; the paint roller a blue sleeve with a cream cap at each end on a cranked wire frame; the carried box khaki with a brown tape; the kite's reel two bright flanges with the cream of the wound string between them.
- **The swimming duck:** its legs are not drawn.
- **Placement revision 43:**
  - the lost balloon's string ends 62 to 80 px above the reaching hand and hangs in a slow wave with no curl, off a playground's railing and, in the garden, above the wooden fence's pickets;
  - the wet paint begins below the roller, which lies on bare wood at the paint's edge, the painter a step closer and the tin with them;
  - the planter kneels at the bed's end and digs in the bed, a hole under the trowel's point, the pot in front;
  - the picnic's loaf and bottle stand out of the basket, and a plate with a slice of watermelon lies on the blanket where it has room;
  - the goat's stake is clear of every standing structure;
  - a swimming animal is cut at a waterline with a ripple round it, and has no ground shadow;
  - the slide's ladder is the frame's own end, in the frame's red, and the bird table's post stands in a tuft of grass;
  - after the screen, the reading dog's paper lies on its paws.
- **Looked at and left before the readers:** a grey remix (every picture's grey twin would move for a cosmetic gain), the leash, the goat's profile, the throw and the tucked jump.
- **Not worked:** the thief bird (R4), first on the v0.46 list.

The set was regenerated and screened a forty-second time. Every person and the duck is drawn anew, so no picture is identical to v0.44's.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.44 readers, or the reviewers, saw | v0.45 |
|---|---|
| `ice_cream` under the gate at 0.85, the girl in pink's "a small pink thing", "a tiny pink dot" | Cone and scoop larger in a child's hand: 1.00 in 14 pictures, "a pink ice-cream cone"; a sweet or a lollipop in no description |
| `photo` at 0.90, "a camera (or binoculars)" | Larger, on a strap: 1.00 in five pictures, "holding a camera up to his eye, taking a photo, with a red strap hanging from it"; binoculars in no description |
| `lost_balloon` at 0.944, "holding the string by its very tip, or has just let go" | The string's end well above the hand, in a slow wave: 1.00 in five pictures, "has escaped and is floating up into the sky, its string dangling" |
| "black ice skates" under a walker's dark shoes | The sole plate inside the shoe's underside: no skates in 93 descriptions |
| The hose inspector's head turned away from the viewer | Toward the viewer and down at the nozzle: `blocked_hose` 1.00 in seven pictures |
| The roller "a paddle", blue on a blue board; the trowel a grey line | `paint_fence` 1.00 in nine pictures, "painting the fence blue with a paint roller on a long handle"; `plant_flowers` 1.00 in five, "digging with a small trowel next to a pink flower in a terracotta pot, about to plant it" |
| The duck standing on the water; the carried box the fence's colour | `ducks_swimming` 1.00 in four pictures; `carry_box` 1.00 in three |
| A picnic with no food in sight | `picnic` 1.00 in three pictures: "a plate with a slice of watermelon, and beside him a wicker picnic basket with a bottle and a baguette" |
| The goat's stake standing on a bench's rail | Clear of every structure: "a peg in the ground", "a short wooden stake", tethered in all four pictures |
| The kite flier with no spool; the slide's ladder apart from its frame | "a kite reel" or "a kite spool" in the hand in six of the seven pictures with a kite on its string; `slide` 1.00 in three, no remark on the ladder |
| The reading dog's paper "floating" beside it (v0.44's watch list) | Left as it was, and it failed the gate's first count on a paper "up in the air". Drawn onto the paws after the screen and read again: 1.00 in three pictures |
| `bird_steals` at 0.967, the bird beside the sandwich | **Not worked, and 0.933:** "about to steal the sandwich, or just be perched next to it". First on the v0.46 list |

Left as notes for the pilot: the goat in a park "a little unusual", the crying child who "covers their eyes instead of looking at the dropped ice cream", and a second cardboard box that "has no obvious purpose".

## The isolation bench

As in v0.44 the bench read whole pictures: a tier-3 picture with the changed templates forced among the planner's own, built once in v0.44's drawing and once in v0.45's on the same seed (`vision/isolation_v045.md`). Round 1 had fifteen readers of 30 pictures, two to a reader; the ten new pictures were read twice, by different readers, and the ten old ones once:
- **A child's ice cream:** "holding a pink ice-cream cone" in both readings; v0.44's was "very small and could be read as a lollipop or a pink sweet rather than an ice-cream cone".
- **The planting:** "digging with a trowel" in all four readings, the pot "apparently waiting to be planted"; v0.44's had no trowel in either reading ("tending the colourful flowers").
- **The picnic:** the baguette and the bottle named in all six readings, and the plate with the watermelon slice in both readings of the picture that has it; v0.44's was "a wicker basket beside it", with no food named.
- **The kite's reel:** named in all four readings ("holding a kite spool up in one hand"); v0.44's was "I cannot see whether he has a spool".
- **The lost balloon:** "its string dangling free", and it "dangles well above his hand, so it seems he has just let go of it and can't reach it". But on the playground the end lay at the railing's top line: "caught on/attached to the fence rather than floating free".
- **The roller:** "painting the wooden fence blue with a paint roller on a long handle", but it "hovers slightly above the fence top line on its left edge".
- **The slide's ladder**, v0.44's own: "drawn in front of/ beside the red frame", in the old drawing and the new alike.
- **The camera, the shoes, the hose inspector, the box and the duck** read as well as they had. The camera's and the shoes' misreadings were the screen's, one in ten and one in eighty, and a bench of four pictures does not show them either way.

Round 2, two readers of the three pictures that changed, read the three fixes:
- **The painter** a step further forward: "painting the fence blue with a roller on a handle; a few boards next to her are already blue". Nothing hovers.
- **The balloon's string** clear of the railing's top line: "The yellow balloon's string ends in mid-air well above the girl's hand; she seems to have just let go."
- **The slide's ladder** as the frame's own end: "Slide with red ladder (left)", and no remark on it in four readings.

Before any reader, the bench's own look caught the planting: its first drawing, a dug patch on the lawn, lay under the planter's shoe, and it was redrawn twice. The goat's stake stood clear of every bench on the bench's seeds, so its rule was seen at work afterwards, on the seed of the v0.44 probe that had shown the flaw (design test 6, below).

__DESIGN_TESTS__

## Placement revision 43

Every record stores the placement revision it was made with. v0.45 pictures use revision 43:
- **The lost balloon:** its string's end 62 to 80 px above the reaching hand at full size (`templates.BAL45`), the string a slow wave that grows toward its free end, with no curl (`CURL45`). On a playground the end lies nowhere on the railing (`RAIL45`). In the garden it lies above the wooden fence's pickets, 34 to 48 px at full size, and a child whose hand would be more than 200 px below it is not stood there (`WOOD45`).
- **The fence painter:** the wet paint on the board under the roller begins below the roller, so the roller lies on bare wood at the paint's edge; the painter stands a step further forward until the roller lies well below the boards' tops, the tin with them (`templates.PAINT45`).
- **The planter:** kneels at the bed's end and digs in the bed, a hole under the trowel's point, a few clods beyond it, the pot in front of the bed (`templates.PLANT45`).
- **The picnic:** a loaf and a bottle stand out of the basket, and where the blanket has room a plate with a slice of watermelon lies on it (`templates.PICNIC45`).
- **The goat:** its stake never drawn in front of a standing structure (`templates.TETHER45`).
- **A swimming animal:** cut along a waterline with a ripple round it, with no ground shadow (`library.SWIM45`).
- **The slide's ladder:** the frame's own end, in the frame's red: two rails to the ground with slate rungs between them, the near rail running on up into the hand rail over the deck (`settings.SLIDE45`).
- **The bird table:** its post stands in a tuft of grass (`settings.FOOT45`).
- **The reading dog** (after the screen): its paper drawn 12 px toward the dog and 6 px higher, at the dog's scale, so the forelegs cross the near page and the paws lie on it (`templates.READ45`).

Each switch is "B"; any other value gives the rule's v0.44 form. A v0.44 record rebuilds with the v0.44 package. The cast redraws every person and the duck (builder 0.45.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.45 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.44. __CALIB_NOTE__

__SCREEN_SECTION__

## The generated set

__SCENES_TABLE__

__ISO_TEXT__

## How many pictures the generator can make

__COMBOS_TABLE__

## Key words, frequency and age of acquisition


Unchanged from v0.20: every item record carries its key word's Zipf frequency (f, for things and actions only) and its
age of acquisition (a, from the bundled excerpt of Kuperman, Stadthagen-Gonzalez and Brysbaert, 2012) at weight 0;
`scenegen/norms/aoa_kuperman2012.tsv` keeps the citation and source in its header and every record stores its sha256.
The licence note and what the pilot should test are in the v0.20 README section of the same name (the CC BY-NC-ND 3.0
question about shipping an excerpt; the model with AoA against the model without, pre-registered; AoA kept varying apart
from frequency when choosing the pilot's pictures). Before the pilot, check the bundled rows against the original file
(`python -m scenegen.difficulty --check-aoa <the original .xlsx or .csv>`).

## Folders

| Folder | What it holds |
|---|---|
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg, and from v0.32 `~body` and `~legs` at both legs, for the bench) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant; from v0.32 a piece of a split figure is checked by its base pose, and the manifest schema takes the `~` suffix |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads, v0.44 sits the reading dog up in reading glasses, redraws the cats' ears, the goat's beard and the dogs' noses, gives props colours of their own and redraws the run, the sand spade, the nozzle's inspection, the call from the seesaw and the content face, and v0.45 enlarges the ice cream, redraws the camera, the shoes' soles, the trowel, the paint roller, the carried box and the kite's reel, turns the hose inspector's head to the viewer and hides the swimming duck's legs |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out045/` | The 18 `.blend` families (builder 0.45.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib045/` | Every variant the generated scenes and probes use, rendered from `out045` (every person and the duck) or carried over from `lib044` (the songbirds, the cats, the dogs and the goat) |
| `assets/cast/gallery045/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.45.0, placement revision 43); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.45 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v045.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v045.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v045.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty-two screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out045                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out045 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v045   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v045 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery045 --old-gallery <v0.44 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.45 --single   # the release as one zip, tpdb_v0.45.zip
```

The release is one zip, `tpdb_v0.45.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.44 record rebuilds with the v0.44 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
