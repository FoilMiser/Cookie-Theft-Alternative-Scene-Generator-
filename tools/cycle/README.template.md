# TPDB v0.29: a dog asleep, a duck at a crumb, a box in the way, read a twenty-sixth time

v0.28 ended with three gate failures: `dog_sleeping` at 0.67 ("sniffing the grass, lying down, or curled up asleep"), `ducks_bread` at 0.83 ("swimming towards those crumbs") and `dog_wants_walk` at 0.83 ("sits with a red lead in its mouth", no more). `about_to_trip` passed but had fallen for two releases ("he is moving past it, not squarely into it"). Its oddities were led by the hose in hand, "like a rigid pipe", and readings that weakened a contradiction, such as a bucket as "a makeshift rain hat" under storm clouds.

v0.29 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-sixth time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.28 readers saw | v0.29 |
|---|---|
| `dog_sleeping`: "sniffing the grass, lying down, or curled up asleep", "could be a puppy or a kitten" (0.67) | Turned three-quarters, its chin on its paws. "Curled up asleep", and a puppy, in all three of its pictures: 1.00. The wider shadow tried on the old pose did little |
| `ducks_bread`: "swimming towards those crumbs" (0.83) | The neck arched, the bill at a crumb. "Bending its head down to peck at the crumbs": 1.00 in its three pictures. Crumbs now sometimes run past the pond's edge |
| `dog_wants_walk`: "sits with a red lead in its mouth" (0.83) | Beside the door and turned to it, not in front of it facing out. "As though asking to be taken for a walk", on the seed that failed: 0.92 |
| `about_to_trip`: "he is moving past it, not squarely into it" (0.92, meaning 0.75) | A long low box across the line of the stride, the same obstacle in every picture without another box, where v0.28 had a bucket, a ball or a box. "So he seems about to trip over it": 1.00 in five street pictures, with four of the five still allowing he may pass. It costs ground (below) |
| The hose in hand: "like a rigid pipe", "with no slack" | Slack, bowed out in front of the figure. No rigid pipe. But the short piece added at the fist has a square end and reads as a sleeve: "seems to stop at about waist height". On the v0.30 list |
| The stopped hose's swelling: "a separate slug-shaped object" | Slimmer, with no highlight. "As if the water is blocked there" |
| The goldfish: "looks pasted onto the leaves" | On a limb, well out from the trunk. "Sitting on a bare curved branch, which is impossible". The pasting moved to the limb: "a little pasted in" |
| A ladder "too far away" from a lamp post; a floating box beside a soaked one; a bucket as "a makeshift rain hat" | Rules: a ladder at least 160 units from a lamp, one kind of box to a picture, no bucket on a head under a dark sky. No such reading this time |

Left as they were: the lifted heel, as the bench found nothing to choose; the heavy rider's leg; the narrow figure. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v029.md`, three rounds, 56 cut-outs, 21 readers). The variants are behind `SLEEP29`, `TRIP29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29` and `FISH29` in `scenegen/templates.py`, `SHADOW29` in `scenegen/library.py` and `TPDB_FOOT` in the cast; the release builds with the chosen ones. The sleeping dog facing out hid its body behind its head ("sitting and looking down, sniffing the ground, or begging"), and turned three-quarters it was asleep to both readers. The duck took two rounds: its neck down along the breast was "lying on its side or collapsed", three of three, and an arched neck kept the head above the body. The trip took three. A plank "stands at a lean, on its narrow end" and was out. A box across the line was "a little skewed", so it went wider, straighter on and less steep on top. On the last two drawings six of six named the walk into it, against three of four on the bucket. The hose bowed toward the body "looks broken up", and bowed in front it "appears to stop or have a gap", where the hose in the fist, which is the figure's, met the one on the ground. That joint got a short piece over it, and was not read on the bench, which is where the screen found it wanting.

__DESIGN_TESTS__

## Placement revision 27

Every record stores the placement revision it was made with. v0.29 pictures use revision 27, which adds to those of revisions 1 to 26 the sleeping dog's new pose at yaw 45; the long box as the trip's obstacle, falling back to a bucket beside a floating, carried or soaked box; the duck's pose and three crumbs at its mouth; the dog beside the door, turned to it, with its lead in a J; the slack hose and its joint; the slimmer swelling; the fish on a limb in the slot furthest from the trunk; and three rules: no lamp within 160 units of the ladder, one kind of box to a picture, no bucket on a head under a dark sky. The dogs' and the duck's new poses are in the cast (builder 0.29.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.29 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.28. __CALIB_NOTE__

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
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 adds the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look` |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out029/` | The 18 `.blend` families (builder 0.29.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib029/` | Every variant the generated scenes and probes use, carried over from `lib028` where the cast did not change or rendered from `out029` |
| `assets/cast/gallery029/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.29.0, placement revision 27); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`), the long box (`long_box`) and the hose through its points (`hose_through`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.29 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v029.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v029.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v029.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-six screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out029                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out029 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v029   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v029 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery029 --old-gallery <v0.28 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.29 --single   # the release as one zip, tpdb_v0.29.zip
```

The release is one zip, `tpdb_v0.29.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.28 record rebuilds with the v0.28 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
