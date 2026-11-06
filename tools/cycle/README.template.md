# TPDB v0.32: a handle raised with the rider, a box on the forearm, read a twenty-ninth time

v0.31 ended with 63 of 64 templates through the gate, the one failure a half mark on a boy jumping for joy near a ball stuck in a tree: he "could be trying to reach the ball or just cheering". Its list began with the man on the seesaw's low end, still "sitting on the plank end or sitting just beside it", and went on to watering under storm clouds, which "could be read as ironic or pointless", the girl stuck up high, who "may look like she is hovering slightly", and a box held at the side "as if it is half floating".

v0.32 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-ninth time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.31 readers saw | v0.32 |
|---|---|
| The girl stuck up high "may look like she is hovering slightly" | The bench found the readers' words were about her hands, "a little above the handle rather than clearly around it", in 7 of 15 readings, and the handle now rises with her. "Holding the handle" in all three of her pictures, and nothing of her hands; one reader still saw her hover, from the kick arcs under her feet |
| A box held at the side "as if it is half floating" | Carried on the whole forearm, the hand at its far corner. "Carrying a cardboard box in both arms", and no box carried floats in its three pictures |
| Watering under storm clouds: it "could be read as ironic or pointless" | Watering by hose or can under a clear sky only. In the 12 pictures with watering, no reader remarks on the sky |
| `jump`, the gate's one failure: "could be trying to reach the ball or just cheering" | The jumper kept 200 units from a ball or kite stuck in a tree. 1.00 in three pictures: "he is not under the tree, so I read it as jumping for joy" |

Left as it was: the man on the seesaw's low end. The bench turned him away from the plank and put both his legs behind it, and every reader of each still doubted his seat; on the list since v0.27, and 1.00 in every screen since, he comes off it. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, autumn leaves under summer trees.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v032.md`, three rounds, 24 cut-outs, 15 readers). The variants are behind `LOW32`, `LOW_IN32`, `LOW_RISE32`, `LOW_RISE_B32`, `STUCK32` and `HANDLE32` in `scenegen/templates.py`, and `TPDB_BOX` and `TPDB_LOW` in the cast; the release builds with the chosen ones. The man on the low end was drawn turned away from the plank, and with both legs behind it, a new cut in the renderer (`~body` and `~legs`); every reader of each still doubted his seat, and the turned man placed less often. Lowering the stuck girl found nothing either. What her readers said, again and again, was that her fists sat above the handle, which the v0.31 raise had left where it was; with the handle raised as much, none of three said anything about her hands. The box, pressed to its sides or held higher on the hands, floated for every reader; on the whole forearm, for none.

__DESIGN_TESTS__

## Placement revision 30

Every record stores the placement revision it was made with. v0.32 pictures use revision 30, which adds to those of revisions 1 to 29 the seesaw's handle raised as far as a rider who grips it sits; watering by hose or can under a clear sky only; and a jumper kept 200 units from a ball or kite stuck in a tree. The cast is v0.31's with a box carried on the whole forearm (builder 0.32.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.32 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.31. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, and v0.32 carries a box on the whole forearm |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out032/` | The 18 `.blend` families (builder 0.32.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib032/` | Every variant the generated scenes and probes use, carried over from `lib031` or rendered from `out032` |
| `assets/cast/gallery032/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.32.0, placement revision 30); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.32 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v032.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v032.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v032.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-nine screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out032                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out032 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v032   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v032 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery032 --old-gallery <v0.31 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.32 --single   # the release as one zip, tpdb_v0.32.zip
```

The release is one zip, `tpdb_v0.32.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.31 record rebuilds with the v0.31 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
