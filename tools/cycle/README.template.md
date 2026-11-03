# TPDB v0.25: a shopping bag that looks like one, a roller that touches the fence, a dog with its own paws, read a twenty-second time

v0.24 ended with its screen's one gate failure, the older man's shopping bag at 0.75 ("carrying something yellow", "very long and thin ... could be a tag, folded paper"), and a list of oddities led by a wheelbarrow's oversized shadow, a bird as big as the sandwich it stole ("a blue kettle or jug"), a newspaper dog's "white gloved hands" and a paint roller that "hardly seems to touch the fence".

v0.25 works through those. Each went to the isolation bench first, drawn two or more ways and read blind on its own, and most turned out to have a plain cause: the bag and the roller both showed their narrow edge to a viewer looking at a figure in profile. All of them were then read blind in whole test scenes among other events, the set was regenerated, and it was screened a twenty-second time. Oddities now come in two rows, as v0.24 showed that scorers differ in how much they log.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.24 readers saw | v0.25 |
|---|---|
| The older man's shopping bag: "carrying something yellow", "very long and thin ... could be a tag, folded paper" (0.75, the gate's one failure) | Redrawn on the bench (builder 0.25.0): its broad face along the walker's line, so a profile shows it, as tall as it is wide, with dark handles rising to the hand. Bench readers: "a plain yellow shopping bag with dark handles" |
| A paint roller that "hardly seems to touch the fence", "a small pale oval" | Redrawn on the bench: upright, its side to the viewer, a T on the end of the pole. Its axis had run along the line of sight, so only its round end showed. "A long-handled paint roller up against the fence" |
| The wheelbarrow's shadow: "a large dark oval extending well beyond it" (four probes) | 130 px wide, was 210: "a soft dark shadow beneath it" |
| The bird at the sandwich "about as big as the sandwich", "a blue kettle or jug" | 0.8 of its size, and the sandwich 0.72 of its drawn size (was 0.8). At 0.68 the bird was "a glove or a bag" |
| The newspaper dog's "white gloved hands" | The paper drawn behind the dog with no paws painted over it, so its own paws rest on it, at different heights so both show. Ovals in its own colour read as "stuck onto" the paper |

Left as they were, as notes for the pilot: figures overlapping the pond, goats in a garden or park, the older ones (wind under a clear sky, a stall with nobody at it, sweeping a path with nothing on it). Feet at the edge of a path were looked at and left: only about three of the remarks that seemed to be about them really were.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v025.md`, two rounds, 20 cut-outs, seven readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_BAG`, `TPDB_ROLLER`); the release cast builds with the chosen ones. The bag as tall as it is wide was "a plain yellow shopping bag with dark handles" twice, where a wider one also drew "a briefcase" and "more like a box". The upright roller was "a long-handled paint roller" twice, where a fatter one was once "or wide brush". The barrow's shadow at 130 px lay "beneath it", and at 160 the barrow "looks slightly lifted". The bird at 0.8 still pecked, and at 0.68 it was "a glove or a bag". The dog's paws took a second round: ovals in its own colour, with or without toes, stayed "stuck onto" the paper, so the ovals went, and with its own paws on the paper it "holds an open newspaper ... as if reading it". The sandwich's smaller size and the paws at different heights were first read in whole scenes.

__DESIGN_TESTS__

## Placement revision 23

Every record stores the placement revision it was made with. v0.25 pictures use revision 23, which adds to those of revisions 1 to 22 the bird's and the sandwich's sizes and the newspaper drawn behind the dog. The bag, the roller and the dog's paws are in the cast (builder 0.25.0), and the barrow's shadow in `scenegen/draw.py`.

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.25 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.24. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.25 redraws the bag and the roller, and keeps the bench variants behind `TPDB_BAG` and `TPDB_ROLLER`, with `TPDB_TEEN` and `TPDB_SLIDE` from v0.24 |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out025/` | The 18 `.blend` families (builder 0.25.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib025/` | Every variant the generated scenes and probes use, carried over from `lib024` where the cast did not change or rendered from `out025` |
| `assets/cast/gallery025/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.25.0, placement revision 23); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`) and the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`; `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.25 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v025.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v025.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v025.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all twenty-two screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out025                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out025 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_BAG=A> python vision/isolation_bench.py tpdb_work/bench bagA_1 bagA_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v025   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v025 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery025 --old-gallery <v0.24 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.25 --single   # the release as one zip, tpdb_v0.25.zip
```

The release is one zip, `tpdb_v0.25.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.24 record rebuilds with the v0.24 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
