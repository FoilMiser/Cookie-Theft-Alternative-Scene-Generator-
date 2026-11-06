# TPDB v0.34: long hair for the woman in yellow, the wind asked for exactly, read a thirty-first time

v0.33 ended with 63 of 64 templates through the gate, the one failure a woman in a yellow dress, seated reading, taken for "a child with short dark hair, in a yellow top, yellow shorts and red shoes". Its list went on to washing on a line offered as what a storm pointer points at, "roughly between the two", and water poured from a frying pan in the wind that falls "fairly straight".

v0.34 works through those. Each drawing went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a thirty-first time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.33 readers saw | v0.34 |
|---|---|
| The woman in yellow, seated reading: "a child with short dark hair, in a yellow top, yellow shorts and red shoes" | Long hair, tied back. On the bench every reader of her with it had her a woman or a girl; a dress drawn across her lap changed nothing ("yellow shorts" again). In the design tests she is "the woman" in all three pictures |
| The storm pointer: "at the storm clouds, or at the washing on the line (or both)" | The washing on the line is kept out of the pointing cone, as a scored thing is |
| "Despite the strong wind, the water from the pan falls fairly straight" | No can, pan or sprinkler in a windy picture, as no hose since v0.33. And the wind is asked for exactly: v0.33's rule also kept a hose out of pictures with a kite, a thing stuck in a tree or a floating box, which claim the wind's tag only to keep away from it |

Left as it was: the roller, at the top of the painted patch because the painting pose holds it overhead. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, autumn leaves under summer trees.

## The isolation bench

The woman in yellow seated reading was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v034.md`, one round, 12 cut-outs, 12 readers, one each). The variants are behind `TPDB_SEAT34` and `TPDB_HAIR34` in the cast; the release builds with the chosen one. With her bob she was "a child or young person", "a boy" and "a person"; with long hair, "a woman", "a girl or young woman" and "a girl". A dress across the lap, one cloth from thigh to thigh where the two lobes had looked like shorts, read no better, and with the hair as well read no better than the hair alone, so it stays off. Its first drawing, rungs from thigh to thigh, was set aside on looking: they drew seams, a stack of yellow rolls on her knees.

__DESIGN_TESTS__

## Placement revision 32

Every record stores the placement revision it was made with. v0.34 pictures use revision 32, which adds to those of revisions 1 to 31 no can, pan or sprinkler in a windy picture, the wind asked for as the wind template itself; and the washing on the line kept out of a storm pointer's cone. Revision 31's test of the wind is kept as it was, so v0.33's records rebuild. The cast is v0.33's with long hair for the woman in yellow (builder 0.34.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.34 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.33. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, and v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated) |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out034/` | The 18 `.blend` families (builder 0.34.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib034/` | Every variant the generated scenes and probes use, carried over from `lib033` or rendered from `out034` |
| `assets/cast/gallery034/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.34.0, placement revision 32); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`); `library.py` the shadow's two (`SHADOW28`) and the sleeper's wider one (`SHADOW29`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.34 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v034.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v034.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v034.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-one screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out034                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out034 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v034   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v034 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery034 --old-gallery <v0.33 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.34 --single   # the release as one zip, tpdb_v0.34.zip
```

The release is one zip, `tpdb_v0.34.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.33 record rebuilds with the v0.33 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
