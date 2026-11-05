# TPDB v0.31: riders astride the seesaw, a spade at the castle, read a twenty-eighth time

v0.30 ended with 63 of 64 templates through the gate, the one failure a half mark on washing hung under storm clouds. Its list began with the seesaw, on the list since v0.27 and the largest thing left that was plainly a drawing fault: "the man's legs appear to go through or around the plank". The bearded man's vest had "a jagged edge against the white shirt", a child's hand and the castle "merge a little", and a reel stood "partly overlapping the edge of the flower bed".

v0.31 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-eighth time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.30 readers saw | v0.31 |
|---|---|
| The seesaw: "the man's legs appear to go through or around the plank" | Each rider drawn in two pieces, the leg further from the viewer behind the plank and the rest in front, and raised so the hips rest on it. Plank remarks in 2 of 6 seesaw pictures, against 5 of 6, both of them the man on the low end, and none in the three pictures of two children |
| The vest: "a jagged edge against the white shirt" | Wider than the shirt, so the shirt cannot come through. The man is in 13 pictures, and no reader remarks on his vest |
| The castle: "the hand and castle merge a little" | Further from the spade, so the hand and the spade show: "probably a toy spade, next to the castle" |
| The reel: "partly overlapping the edge of the flower bed" | Moved down and to the left, clear of the bed and the step. No remark in its 10 pictures |
| Washing under storm clouds: "taking it down because of the coming storm" | No washing hung under a dark sky. 1.00 in three pictures, though one reader still offers that he may be taking it down, under a clear sky |

Left as they were: the fish's limb, which a redraw on the bench made worse, and which comes off the list; the cone, where the bench found nothing to choose; the walker's book and the feed bag. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v031.md`, two rounds, 42 cut-outs, 19 readers). The variants are behind `SEESAW31`, `RIDE31`, `CASTLE31` and `LIMB31` in `scenegen/templates.py`, `REEL31` in `scenegen/settings.py`, and `TPDB_VEST` and `TPDB_CONE` in the cast; the release builds with the chosen ones. The seesaw needed the renderer to cut a rider in two (`split_leg` in `assets/render_assets.py`): a pose name with `~near` draws the figure without the leg further from the camera, and `~far` that leg alone, in the same frame. The far leg behind the plank read no better on its own, because the hips still lay over the plank; raised as well, the children sat on it. A seat on the plank added a thing to explain and read no better. The vest needed only its size, and the castle only a step further from the spade, which had been drawn all along behind it.

__DESIGN_TESTS__

## Placement revision 29

Every record stores the placement revision it was made with. v0.31 pictures use revision 29, which adds to those of revisions 1 to 28 riders astride the seesaw, in two pieces and raised onto the plank; the castle further from the spade; the reel down and to the left; and washing hung only under a clear sky. The cast is v0.30's with the vest widened (builder 0.31.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.31 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.30. __CALIB_NOTE__

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
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, and v0.31 widens the vest |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out031/` | The 18 `.blend` families (builder 0.31.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib031/` | Every variant the generated scenes and probes use, carried over from `lib030` or rendered from `out031` |
| `assets/cast/gallery031/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.31.0, placement revision 29); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.31 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v031.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v031.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v031.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-eight screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out031                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out031 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v031   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v031 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery031 --old-gallery <v0.30 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.31 --single   # the release as one zip, tpdb_v0.31.zip
```

The release is one zip, `tpdb_v0.31.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.30 record rebuilds with the v0.30 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
