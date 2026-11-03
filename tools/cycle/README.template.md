# TPDB v0.26: an older man's head that reads, a dog at the door with its eyes open, leaves to sweep, read a twenty-third time

v0.25 ended with three gate failures, `dog_wants_walk` at 0.83 ("with its eyes shut"), `sweep` at 0.88 ("no visible rubbish or leaf pile for the old man to sweep") and `ducks_bread` at 0.89, and a list of oddities led by the older man's face, "hard to read" in ten of his 21 pictures, a newspaper dog that "could be taken for a monkey, an otter, or a person in a costume", and a cap worn backwards that twice read as a head "the wrong way round".

v0.26 works through those, and it sorted all 428 of the v0.25 readers' remarks by what they were about, which added the feeder's bag and the sandcastle. Each went to the isolation bench first, drawn two or more ways and read blind on its own. All of them were then read blind in whole test scenes among other events, the set was regenerated, and it was screened a twenty-third time. One drawing chosen on the bench, the broom, did not survive the screen.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.25 readers saw | v0.26 |
|---|---|
| The older man's head: "the older man's face is hard to read", a grey patch (ten of his 21 pictures) | His cap kept, with a shorter peak tipped up and short white hair running round under it (builder 0.26.0). Bench: "an older man with grey hair and a blue-grey flat cap". One remark on his face in his 12 screened pictures |
| The newspaper dog's head: "a monkey, an otter, or a person in a costume", "a person in a spacesuit or a small robot" | Its head up and turned a little to the viewer, its tail up behind it. "A brown-and-tan cartoon dog", and no other animal in its five screened pictures |
| The teenager's cap worn backwards, twice a head "the wrong way round" | Worn forwards. "A cartoon boy or young man", and no head on the wrong way round in his 20 pictures. Two readers still took the cap for sideways or backwards |
| The dog at the door "with its eyes shut", its wish for a walk never stated (0.83) | The neutral face only, as the happy one closes its eyes. "As if it is asking to go for a walk": 1.00 |
| `sweep` with nothing to sweep: "no visible rubbish or leaf pile for the old man to sweep" (0.88) | A heap of leaves at the broom, which worked: "sweeping up a pile of autumn leaves". And a fan of seven bristles for its head, as the old wedge read as "a dustpan or scraper" on the bench, which did not: "a long yellow-headed rake", this screen's one misread (0.67). First on the v0.27 list |
| The feeder's "a paper bag, a cup or a carton" | A brown paper bag: "a brown paper bag" or "a paper bag" for all six feeders in five pictures. The crumbs at the pond are bread-coloured |
| The sandcastle: "very straight, boxy edges ... a cardboard or wooden model" | Heaped sand with bucket-shaped towers: "a sandcastle with three towers and a small red flag". The child and the castle stay back from the sandbox's front rim |
| A lamp post merging with a figure | A placement rule keeps a person's box off the post. No reader had a figure growing out of it or about to walk into it |
| Two probes nearly the same picture, both `seesaw` alone | A template's second solo probe now gets a companion event |

Left as they were, as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things, swing ropes behind a rider's head. Tried and left: fuller bodies, as a figure 22% deeper with limbs 12% thicker did not move the readers' words, and the bearded man's bowed head over the birds, which a rule from revision 5 needs.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v026.md`, two rounds, 36 cut-outs, 15 readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BROOM`, `TPDB_BODY`); the release cast builds with the chosen ones. For the older man the eye and the readers disagreed: no cap and short white hair looked best, but read as "a smooth grey cap or hat", and "the face is hard to read", while the cap kept, its peak shorter, was "an older man with grey hair and a blue-grey flat cap". The newspaper dog with its head up in profile could still be "a weasel or an otter"; turned a little to the viewer it was only a dog, and a flat shape at its rear went when the tail went up. A red beanie named the teenager less firmly than the cap worn forwards. A heap of dust and grit was "a small rock or mound", where leaves were "sweeping up leaves". A slice of bread for the feeder was "a couple of sheets of paper". The broom's yellow wedge was "a dustpan or scraper", so round 2 tried the fan, and one reader there said "broom or rake", which the screen bore out.

__DESIGN_TESTS__

## Placement revision 24

Every record stores the placement revision it was made with. v0.26 pictures use revision 24, which adds to those of revisions 1 to 23 the leaf heap at a sweeper's broom, the neutral face for the dog at the door, the heaped sandcastle with the sandbox's child and castle back from its front rim, the newspaper's pale photo (its photo block had kept a dark outline), the bread-coloured crumbs, and a person's box kept off the lamp post. The older man, the teenager, the newspaper dog's head and tail, the feeder's bag and the broom are in the cast (builder 0.26.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.26 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.25. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.26 redraws the older man's and the teenager's caps, the newspaper dog's head and tail, the feeder's bag and the broom, and keeps the bench variants behind `TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BROOM` and `TPDB_BODY`, with `TPDB_BAG`, `TPDB_ROLLER` and `TPDB_SLIDE` from earlier releases |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out026/` | The 18 `.blend` families (builder 0.26.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib026/` | Every variant the generated scenes and probes use, carried over from `lib025` where the cast did not change or rendered from `out026` |
| `assets/cast/gallery026/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.26.0, placement revision 24); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, and the swept heap's two drawings (`SWEEP26`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.26 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v026.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v026.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v026.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all twenty-three screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out026                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out026 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_OLD=A> python vision/isolation_bench.py tpdb_work/bench oldA_1 oldA_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v026   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v026 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery026 --old-gallery <v0.25 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.26 --single   # the release as one zip, tpdb_v0.26.zip
```

The release is one zip, `tpdb_v0.26.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.25 record rebuilds with the v0.25 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
