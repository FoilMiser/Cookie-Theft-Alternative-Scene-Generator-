# TPDB v0.24: a teenager who looks like one, a slide with the face in view, sleepers clear of walkers' feet, read a twenty-first time

v0.23 ended with the twentieth blind screen at its ceiling: every one of 729 scored items had full marks and all 64 templates passed the gate, so what its readers still reported were oddities, and `vision/flaws_v023.md` listed them for v0.24. Above all, a sleeping cat on the path 50 px behind a walking man's back foot, "right by his feet, so he could trip over it or step on it". Going through the scorers' notes, two more stood out, both credited in full and both left as notes for the pilot in v0.23: no reader called the teenager a teenager ("a woman with a brown ponytail", 13 items), and figures at the back were "drawn as large as foreground people ... as if walking on the hilltop" (four pictures, each with the feet within 75 px of the horizon).

v0.24 works through those. The ones about how things look went to the isolation bench first, in two rounds, each drawn two or more ways and read blind on its own; the bench also found one nobody had listed, the raised arms of a child on the slide lying across the face. The rest are placement rules (revision 22). All of them were then read blind in whole test scenes among other events, the set was regenerated, and it was screened a twenty-first time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.23 readers saw | v0.24 |
|---|---|
| A sleeping cat 50 px behind a walking man's back foot: "right by his feet, so he could trip over it or step on it" | A sleeping animal kept clear of any walker's feet on both sides and in depth, not only ahead of a reading walker |
| The teenager never called a teenager: "a woman with a brown ponytail" (13 items, credited) | Redrawn on the bench (builder 0.24.0): shorter, a larger head, short hair and a red cap worn backwards. Bench readers: "a boy or young man", "a teenager or a slim adult" |
| A child on the slide with the arms raised across the face: "holding her head or hair" (and on the bench "covering the face or eyes ... upset, scared") | Redrawn on the bench: both arms up and ahead, the near one passing under the chin, the hands open toward the viewer: "sitting and sliding ... with both arms stretched up and forward" |
| A child "slightly in front of" the chute, "hovering a little above the slide" | The seat 8 px higher, on the chute's middle: "looks seated on the slide" |
| A figure at the back "drawn as large as foreground people ... as if walking on the hilltop" (four pictures) | In the park and on the playground, nobody on the ground in the 90 px of open ground before the horizon. No reader remarked on size in either setting in the design tests |

Tried and left as it was: the seesaw's riders, "perched rather than seated" in v0.23, read worse raised than where they were (bench, below). Left as they were, as notes for the pilot: water from a blocked hose that might spray the woman holding it (she is peering into the nozzle, and the reading fits), a figure at the back of the street against the shop fronts, goats in a garden or park, and the older ones (wind under a clear sky, a stall with nobody at it, sweeping a path with nothing on it).

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v024.md`, two rounds, 16 cut-outs, eight readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_TEEN`, `TPDB_SLIDE`); the release cast builds with the chosen ones. The teenager with a cap worn backwards was "a boy or young man" and "a teenager or a slim adult"; with the old ponytail and an orange school backpack "a girl or young woman", the pack "a second ball", "a disc" or "shield-like". The seesaw's riders, raised 10 or 18 px, were said to "overlap the plank" or "float slightly above the seat", and where they were drew no remark, so they stayed; the 18 px drawing had looked best by eye before it was read. On the slide, the seat on the chute's middle "looks seated", 8 px below it "slightly above or in front of" and 8 px above it "hover just above". All three slide readers then said the raised arm merges with the face, which nobody had listed: arms raised out to the sides lie across the head in profile. With the arms up and ahead the child was "going down it ... as if waving or cheering", with the hands holding the chute "just sitting still". Two further candidates were dropped by eye before any reader saw them (a mop of hair; a backpack whose straps sank into the hoodie), and one refinement of the arms, which lay across the face again. The final arms were read first in the whole scenes.

__DESIGN_TESTS__

## Placement revision 22

Every record stores the placement revision it was made with. v0.24 pictures use revision 22, which adds the rules above to those of revisions 1 to 21: a sleeping animal clear of the ground round any other event's walker's feet, 170 px either side of them and in depth; and in the park and on the playground, nobody on the ground within 90 px of the horizon. The seat on the slide and the teenager's cap (kept out of the windy-hat picture, which casts someone bareheaded) are also gated on it. The cast is builder 0.24.0.

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.24 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.23. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.24 redraws the teenager and the slide's arms, and keeps the bench variants behind `TPDB_TEEN` and `TPDB_SLIDE` |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out024/` | The 18 `.blend` families (builder 0.24.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib024/` | Every variant the generated scenes and probes use, carried over from `lib023` where the cast did not change or rendered from `out024` |
| `assets/cast/gallery024/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.24.0, placement revision 22); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`) and the riders' bench offsets (`RIDE24`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.24 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v024.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v024.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v024.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all twenty-one screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out024                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out024 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_TEEN=A> python vision/isolation_bench.py tpdb_work/bench teenA_1 teenA_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v024   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v024 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery024 --old-gallery <v0.23 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.24 --single   # the release as one zip, tpdb_v0.24.zip
```

The release is one zip, `tpdb_v0.24.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.23 record rebuilds with the v0.23 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. All 21 v0.23 records rebuilt on Windows with identical SVGs: 18 were identical to the pixel, and the other three differed by one level on at most 96 of 1.6 million pixels, the rounding of a newer cairo. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so `lib024` mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
