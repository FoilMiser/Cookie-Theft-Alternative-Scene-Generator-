# TPDB v0.33: no kick arcs on the seesaw, the storm pointer clear of the cat, read a thirtieth time

v0.32 ended with 63 of 64 templates through the gate, the one failure the dog on the stopped hose, on a picture unchanged since v0.31: "Only a single drop is shown, so it is unclear whether water is flowing. The dog's back foot looks as if it may be standing on the hose". Its list went on to a woman pointing at the storm from right under a cat on the fence, read as "pointing upward at the cat", the girl stuck up high, whom the motion arcs under her feet made look "as though she is hovering slightly above the plank", and a hose spraying straight through a gust that blew a cap off.

v0.33 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a thirtieth time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.32 readers saw | v0.33 |
|---|---|
| The girl stuck up high: the arcs under her feet "make her look as though she is hovering slightly above the plank" | No arcs. Added in v0.16, when readers of her without them saw nothing wrong, they are no longer needed: she calls out and holds a raised handle, and on the bench every reader of her without them had her stuck |
| The storm pointer "pointing upward at the cat with a surprised face", a cat on the fence at her fingertip | Anything up high is kept 100 units from the pointer's fingertip, whichever way the arm points. The line to the clouds had been clear; the cat sat at the end of the finger |
| "The wind is strong enough to blow a cap off, but the hose water is not bent by it" | No hose sprays in a windy picture |

Left as it was: the stopped hose. Led in front of the dog's front feet, and flattened wider under the back one, it read no better on the bench and drew remarks on its path, and the swelling still reads as a bulge or a puddle. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, autumn leaves under summer trees.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v033.md`, one round, 18 cut-outs, 9 readers). The variants are behind `HOSE33` and `KICK33` in `scenegen/templates.py`; the release builds with the chosen ones. Without the kick arcs no reader saw the girl hover, and all three had her stuck ("the light girl is stuck up in the air"); with them behind her heels instead, two of three saw her "hovering slightly above" the plank or "perched just above or behind" it. Two drawings were set aside on looking: a hose led in front of the dog's feet that rose straight to the hand, as one that read as "a pole" had in v0.11, and arcs in front of the toes, which lay on the plank. The bench file had given three v0.32 cases the names of three v0.31 cases, and the later entries had won without a word; v0.31's are renamed, and the bench now refuses a name used twice.

__DESIGN_TESTS__

## Placement revision 31

Every record stores the placement revision it was made with. v0.33 pictures use revision 31, which adds to those of revisions 1 to 30 no kick arcs by the stuck rider's feet; anything scored above a storm pointer's fingertip kept 100 units from it; and no hose spraying in a windy picture. The last two are rules in each template's placement, not in its class, so earlier records rebuild as they were. The cast is v0.32's (builder 0.33.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.33 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.32. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, and v0.33 draws nothing new |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out033/` | The 18 `.blend` families (builder 0.33.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib033/` | Every variant the generated scenes and probes use, carried over from `lib032` or rendered from `out033` |
| `assets/cast/gallery033/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.33.0, placement revision 31); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.33 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v033.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v033.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v033.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out033                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out033 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v033   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v033 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery033 --old-gallery <v0.32 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.33 --single   # the release as one zip, tpdb_v0.33.zip
```

The release is one zip, `tpdb_v0.33.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.32 record rebuilds with the v0.32 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
