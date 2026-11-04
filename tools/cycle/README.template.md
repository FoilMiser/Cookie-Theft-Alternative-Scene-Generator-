# TPDB v0.28: shadows from the feet, a splat, a dog beside the food, read a twenty-fifth time

v0.27 ended with one gate failure, `dog_begs` at 0.89, its readers unsure whose food the dog wanted ("could be hers, begging from her bag"). Its oddities were led by shadows ("a very wide oval, much wider than the puppy"), eyes shut on a walker, and a fallen ice cream read as "a pink hat or a pink frisbee". And it had not been able to place a tier-4 playground at all: 219 free seeds placed nothing, so it forced an old picture's events.

v0.28 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-fifth time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.27 readers saw | v0.28 |
|---|---|
| `dog_begs`: "could be hers, begging from her bag", "or be watching the kite" (0.89) | At the end of the bench the eater sits nearest, its gaze on the food, and nobody else near it, now or later. Not redrawn. "Begging for the ice cream": 1.00 in its three pictures |
| Shadows: "a very wide oval, much wider than the puppy", "a bit wide and offset from her feet" | From the figure's own footprint: a person's from the feet, anything else's from the columns the body fills, under its lowest part. Drawn objects' are flatter too. Pictures remarking on shadows fell from 20 to 11, none calling one wide. The sleeping dog may have paid for this (below) |
| The fallen ice cream: "a pink hat or a pink frisbee", a flying saucer | A flat splat, with flecks thrown clear of it and the sprinkles still on, and the dog's mouth over it. "A pink splat with coloured sprinkles": in full in its three pictures |
| The seesaw: "almost past it", and "the girl has none of her own" | Riders and handles further in from the ends, and one shadow under the whole seesaw. No remark on either. The heavy rider's leg over the plank stays |
| Eyes shut on a walker: "Walking with eyes shut is slightly odd" | No walker has closed eyes, in 70 pictures |
| Marks on a face: "dark marks around her nose and mouth", "a pink smudge on the cheek" | No brows over closed eyes and a smaller blush. Pictures remarking on them fell from 9 to 5 |
| The beard: "a thin dark strap along the jaw" | A fuller one read as "a mask or scarf", so a goatee and moustache: "a small beard". No strap or mask in 70 pictures |
| The ball in the tree: "a blue planet-like sphere", on "a small bare branch drawn on top of the crown" | A beach ball, in all four of its pictures, on a limb from a fork at the top of the trunk. Once now "as if the leaves had been cut away to display the ball" |
| "Two bins so close to each other seem like more bins than the scene needs" | One bin to a picture |
| The tier-4 playground: 219 failed seeds, not explained | Explained, and placing again with events of its own (below) |

Left as they were: `about_to_trip`, as the obstacle is already on the line of the stride by rule and by eye, and its meaning item fell again; the hose in `hose_water`, which drew more remarks; the heavy rider's leg; the narrow figure. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v028.md`, three rounds, 37 cut-outs, 17 readers). The variants are behind `TPDB_BROW`, `TPDB_BLUSH` and `TPDB_BEARD` in the cast, and `draw.SPLAT28`, `draw.SEESAW_IN28` and `library.SHADOW28` in the scene; the release builds with the chosen ones. Shadows took four remarks on four old cut-outs and none on four new. A first new shadow vanished under the sleeping dog, which reaches below its ground point, and two bands across the ball looked like a target: both were looked at and fixed before any reader saw them. The splat without a dome beat the one with a low lump, which was once "some other spilled food or slime". The ball's branch took two rounds: with leaves over both ends it "does not visibly connect to the trunk", three of three, and with a limb to the trunk it was "a single bent pipe", so the top of the trunk became a fork. The beard took three: a fuller one was worse, and the answer was less of it.

__DESIGN_TESTS__

## Placement revision 26

Every record stores the placement revision it was made with. v0.28 pictures use revision 26, which adds to those of revisions 1 to 25 the begging dog's end of the bench, its gaze and the ground kept clear round it; shadows from the figure's own footprint; the seesaw's riders further in on one shadow; the splat and the dog's mouth over it; no closed eyes on a walker; the beach ball on a limb, and a bird's branch the same way; one bin to a picture; and three rules for a tier-4 playground and one for a tier-4 street. The faces and the goatee are in the cast (builder 0.28.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.28 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.27. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.28 takes the brows off closed eyes, shrinks the blush and gives the bearded man a goatee |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out028/` | The 18 `.blend` families (builder 0.28.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib028/` | Every variant the generated scenes and probes use, carried over from `lib027` where the cast did not change or rendered from `out028` |
| `assets/cast/gallery028/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.28.0, placement revision 26); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`) and the seesaw's inset (`SEESAW_IN28`); `library.py` the shadow's two (`SHADOW28`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.28 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v028.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v028.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v028.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-five screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out028                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out028 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v028   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v028 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery028 --old-gallery <v0.27 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.28 --single   # the release as one zip, tpdb_v0.28.zip
```

The release is one zip, `tpdb_v0.28.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.27 record rebuilds with the v0.27 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
