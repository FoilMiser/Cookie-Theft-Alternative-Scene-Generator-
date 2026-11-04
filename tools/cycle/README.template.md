# TPDB v0.30: a hose that hangs, crumbs on the water, the trip off the street, read a twenty-seventh time

v0.29 ended with all 64 templates through the gate, and three things that needed saying about that. Its trip had only been read in street pictures. Its new hose had a fault of its own, a short piece at the fist that "seems to stop at about waist height". And the fish's new limb was "a little pasted in", with a tuft that "looks detached". Crumbs lay "on the grass past the pond edge", and a reel with nobody at it had "only a short stub of hose joined to nothing".

v0.30 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-seventh time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.29 readers saw | v0.30 |
|---|---|
| The hose at the fist: "seems to stop at about waist height, then the part at her hands starts again" | The hose runs on in front of the figure and up to the fist, and hangs from it as a rope hangs. Nobody has it stop or break. "Stiff" stays, as it has of every way of drawing it since v0.25: "rises to her hand in a stiff curve" |
| The fish's limb: "drawn on top of the leafy crown", a tuft that "looks detached" | The fork's other arm and its tuft gone. What it cost: "it sits on what looks like the tree's bent trunk". All three of its pictures read the fish as impossible |
| Crumbs: "several crumbs lie on the grass past the pond edge" | Only those on the water, clear of its edge. No remark in three pictures, and the duck reads as eating in all three |
| The reel: "only a short stub of hose joined to nothing", "a short second stub of hose curls by the reel" | The end of the hose lying on the grass with its nozzle on, and gone when somebody has the hose. "A yellow nozzle lying on the grass", in all four of its pictures |
| The trip, read only in street pictures | Not redrawn. Probes put it in two gardens, two parks and two playgrounds: all eleven of its pictures read in full |

Left as they were: the box's width, as 60 units read a little less firmly than 72; the reading dog, as no reader called it a kangaroo this time, with nothing changed; the heavy rider's leg, now first on the next list; the narrow figure. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v030.md`, two rounds, 33 cut-outs, 12 readers). The variants are behind `HOSE30`, `FISH30`, `TRIP_W30` and `CRUMB30` in `scenegen/templates.py` and `REEL30` in `scenegen/settings.py`; the release builds with the chosen ones. The cast did not change. The hose took two rounds. Run on to the fist, the square end and the gap went, and with it hanging as a rope hangs its S-bend over the bed went too. Six of six still found it stiff, and there this release stopped. The fish took two: leaves on the crown read as "bushes floating in the foliage", and a limb running on past the fish gave a fish "floating just above" it and a blunt stub, so it has one limb that ends under the fish. Looking at the first crops stopped three things before any reader saw them, among them a bench whose flags had left the old obstacle and the old duck on the new cases.

__DESIGN_TESTS__

## Placement revision 28

Every record stores the placement revision it was made with. v0.30 pictures use revision 28, which adds to those of revisions 1 to 27 the hose hanging from the fist and running on up to it in front of the figure; the fish's limb with no other arm; the thrown crumbs only on the water; and the end of the hose on the grass with its nozzle on when nobody has the hose, and none when somebody has. The cast is v0.29's (builder 0.30.0, nothing redrawn).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.30 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.29. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, and v0.30 draws nothing new |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out030/` | The 18 `.blend` families (builder 0.30.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib030/` | Every variant the generated scenes and probes use, carried over from `lib029` or rendered from `out030` |
| `assets/cast/gallery030/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.30.0, placement revision 28); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.30 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v030.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v030.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v030.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-seven screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out030                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out030 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v030   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v030 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery030 --old-gallery <v0.29 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.30 --single   # the release as one zip, tpdb_v0.30.zip
```

The release is one zip, `tpdb_v0.30.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.29 record rebuilds with the v0.29 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
