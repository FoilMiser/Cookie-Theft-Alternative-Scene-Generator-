# TPDB v0.44: the reading dog sitting up in glasses, a lead of its own colour, the goat in the park, the run, the spade, the call and the cat's ears, read a forty-first time

v0.43 ended with 62 of 64 templates through the gate: `dog_reading`, laid down over a paper on the ground, read as "lying on an open newspaper", and `dog_wants_walk` fell on one reader who took its red lead for one on its red collar. Sam sent two notes on the v0.43 figures. The first ranked the screen's findings (`tpdb_work/figure-fixes-v043.md`):
- the reading dog back to sitting up, the paper off the ground, the head bowed, with and without reading glasses;
- the dog by the door's lead in its own colour, its loop off the ground;
- the goat in the park only, not grazing at 135;
- the camera and the begging dog's head, as time allowed.

The second was a review of every v0.43 render (`tpdb_work/figure-review-v043.md`): props the colour of the clothes behind them, the run read as a lunge, the cat with no ears in profile, the lost balloon's string landing on things, the sand spade a floating red cross, the upward water a bent tube, the square wheels and twenty more.

v0.44 benched them in whole pictures, as the first note asked, in two rounds, and took most of them (builder 0.44.0):
- **The reading dog:** sitting up again, its forepaws raised to eye level to hold its paper's top edge, its head bowed to the page, in round reading glasses; always the tan dog.
- **The cats:** the ears turned so their triangles show in profile, the muzzle forward, the whiskers forward as well as out.
- **The people:** props in colours of their own (a bag, a watering can or a balloon near a garment's hue takes another colour); the run off the ground; the sand spade's blade on its handle; the nozzle inspected face up; the call from the stuck seesaw, a hand at the mouth; the content face as the happy arcs.
- **The goat's beard** a short blunt tuft, and **the dog's nose** set into its muzzle.
- **Placement revision 42:**
  - the reading dog's paper hung from its paws by the top edge and tilted, the dog in the front half of the picture, off the path and away from other dogs;
  - the waiting dog's lead yellow, hanging from its mouth to a loop clear of the ground;
  - the goat grazing in the park only, and never at 135;
  - the stalking cat its own length from a tree;
  - the lost balloon high on a long string, its curled end clear of everything;
  - the upward water a tapering ribbon, never in the street.
- **Read and left as they were:** a rounded square wheel ("square-ish", or on a bicycle "buckled or squashed"), and the lead lying on the grass ("possibly a thin yellow hose").
- **Tried and left before the readers:** the throw's follow-through, which looked no better than v0.43's.

The set was regenerated and screened a forty-first time. Every dog, cat, goat and person is drawn anew, so no picture is identical to v0.43's.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.43 readers, or Sam's notes, saw | v0.44 |
|---|---|
| `dog_reading` under the gate, lying "on an open newspaper", one misread | Sitting up in glasses, its paper hung from its paws: 1.00 in five pictures, "as if reading" in all five, the glasses named twice |
| `dog_wants_walk` under the gate, its red lead "attached" to its red collar | A yellow lead hanging to a loop: 1.00 in five pictures, "as if it wants a walk" |
| The goat unusual in gardens, twice a sheep from behind | In the park only, never at 135: tethered in all four pictures, "a little unusual" in all four, never a sheep |
| The cat a plain ball of a head in profile, once against a dark tree | The ears and whiskers show, the cat clear of the trees: stalking in all three pictures |
| The run a lunge, the spade a red cross, the stuck girl "nervous or praying" | Off the ground, a spade, a hand at an open mouth: `run`, `sandbox` and `seesaw_heavy` 1.00 in three pictures each |
| The upward water "a bent tube" before the shop door | A tapering ribbon, never in the street: 1.00 in three pictures |
| The lost balloon's string landing on other things | High on a long string, its end clear: 0.944, one picture read two ways |
| Props the colour of the clothes behind them | The bag, can and balloon in colours of their own. The scoop left the rule after the screen. **Not fixed: `ice_cream` under the gate**, the girl in pink's ice cream too small to read when she walks with it in profile |

Left as notes for the pilot: the goat in a park, the reading dog's paper "floating" beside it twice, figures over the pond's outline, the tall lamp post.

## The isolation bench

v0.43's bench read cut-outs, and the lying reading dog read as reading there and as lying on its paper in the screen. So v0.44's bench read whole pictures: a tier-3 picture with the changed templates forced among the planner's own, built in v0.43's drawing and in v0.44's (`vision/isolation_v044.md`). Round 1 had nine readers of 17 pictures, two to a reader and never two pictures of one scene:
- **The reading dog:** v0.43's lying dog read as reading in three of three, each with "lying on it", "chewing" or "tearing" beside it. Sitting up, it read as reading in all six, with "holding" or "fetching" beside it, and in glasses two readers of three took the dark rings for glasses ("could be a pair of glasses"). But its paper, hung square, "stands upright on its own" or "floats" in four of six.
- **The lead:** green read as "a garden hose (the dog bringing a hose to help with watering)".
- **The square wheel:** rounded, it was "square-ish", and a bicycle's one "buckled or squashed"; v0.43's were plainly square.
- **The spade, the call and the water:** "a red spade" (v0.43's "a stick or a toy"); "calling the man to bounce her or let her down"; the water "ending in drops above the flowers instead of falling onto them".

Round 2, four readers of 8 pictures, read two things:
- **The reading dog** in glasses with its paper tilted, its far side sagging: reading in all four, the paper never standing by itself, the glasses "spectacles".
- **The lead** in yellow: hanging, "as if it wants to go for a walk" and "fetching its own lead to ask for a walk"; on the grass, "a dog lead, or possibly a thin yellow hose" and "a thin yellow garden hose" as the other reading.

Before any reader, the bench's own look caught three things:
- the reading dog's paws at chest height left room for a paper smaller than v0.42's, so they were raised to eye level, and the white dog's, lower, left too little, so the reading dog is the tan dog;
- the green lead hung against the garden's blue door, after a blue one;
- the throw looked no better than v0.43's.

__DESIGN_TESTS__

## Placement revision 42

Every record stores the placement revision it was made with. v0.44 pictures use revision 42:
- **The reading dog:** sitting up, its paper hung from its raised forepaws by the top edge, 1.05 to 1.30 times v0.42's paper as the ground allows, tilted 9 degrees, its far side sagging; the dog in the front half of the picture, off the path and 400 px from any other dog; always the tan dog, so never with the dog by the door (`templates.READ44` "G", in glasses, and `READ44T` "T"; "A", without glasses, read on the bench).
- **The dog by the door:** its lead yellow, hanging from its mouth to a loop clear of the ground (`templates.LEAD44` "B"; "C", the loop on the grass, read on the bench).
- **The goat:** grazing in the park only, never at 135 (`templates.GOAT44` "B").
- **The stalking cat:** its own length clear of a tree (`templates.CAT44` "B").
- **The lost balloon:** high above the reaching hand on a string at least nine-tenths of the child's height, against open sky, its curled end clear of everything for 60 px (`templates.BAL44` "B").
- **The upward water:** a ribbon tapering as it rises, drops breaking off its top, never in the street (`draw.WATER44` "B").

A v0.43 record rebuilds with the v0.43 package. The cast redraws every dog, cat, goat and person (builder 0.44.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.44 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.43. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads, and v0.44 sits the reading dog up in reading glasses, redraws the cats' ears, the goat's beard and the dogs' noses, gives props colours of their own and redraws the run, the sand spade, the nozzle's inspection, the call from the seesaw and the content face |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out044/` | The 18 `.blend` families (builder 0.44.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib044/` | Every variant the generated scenes and probes use, rendered from `out044` (every dog, cat, goat and person) or carried over from `lib043` (the songbirds and the duck) |
| `assets/cast/gallery044/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.44.0, placement revision 42); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.44 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v044.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v044.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v044.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty-one screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out044                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out044 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v044   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v044 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery044 --old-gallery <v0.43 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.44 --single   # the release as one zip, tpdb_v0.44.zip
```

The release is one zip, `tpdb_v0.44.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.43 record rebuilds with the v0.43 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
