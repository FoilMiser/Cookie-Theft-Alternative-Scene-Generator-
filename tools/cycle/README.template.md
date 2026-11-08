# TPDB v0.41: the begging dog's forelegs folded, four more drawings read and left as they were, read a thirty-eighth time

v0.40 ended with all 64 templates through the gate, and read strictly with five under it: `floating_box`, its box in the air read as "falling or thrown in", and `play_catch` at 0.833, with `ladder_nothing`, `sweep_fork` and `water_upward` at 0.889. The list went on to the heaps' brown leaves under green trees, the third drawing of the heap to draw a remark on the season; the begging dog in profile, "stiff and human-like"; the stalking cat's legs at 45, "bunched up and a bit tangled"; the woman in yellow called "girl"; and the goat's body.

v0.41 benched those in two rounds and took one drawing (builder 0.41.0):
- **The cast:** the begging dog's forelegs folded at the elbows, the paws tipped down at the chest. Every beg on the bench, v0.40's too, had its forelegs held out level, "like stiff rods".
- **Read and left as they were:** the stalking cat's legs apart, the woman in yellow taller with a fuller figure, the floating box hung level, and the trees turning over a heap of dry leaves. None read better than v0.40's drawing, and two read worse. Placement revision 39 keeps the two scene changes behind switches at the old drawing, so it draws nothing new.

The set was regenerated and screened a thirty-eighth time. Twenty of its 21 pictures came back identical to the pixel, so the screen is mostly a retest.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.40 readers saw | v0.41 |
|---|---|
| The begging dog in profile: "upright sitting pose looks a little stiff and human-like" | The forelegs folded, the elbows forward and the paws tipped down at the chest. On the bench v0.40's forelegs were "like stiff rods" or "like human arms" in three of six cut-outs, and the folded ones in none of six. In the screen the dog begs in all four pictures |
| The floating box "falling or thrown in" | Not changed: hung level on the bench, it still read as falling or thrown, and in the park as a box standing far off on the ground. 0.967 read strictly, in five pictures |
| The catcher "ready to catch the ball or just having thrown it" | Not changed: the half mark came back in full on the identical picture. 1.00 in five pictures |
| The heaps' brown leaves under green trees | Not changed: trees turning over the heap read as fruit on the bench. No reader remarked on the season in 93 pictures |
| The stalking cat at 45: "legs are bunched up and a bit tangled under its body" | Not changed: every spread of the legs drew "bunched" or "tangled" on the bench, v0.40's too. No remark in the screen |
| The woman in yellow called "girl" | Not changed: on the bench v0.40's was "a woman" in four cut-outs of four, and neither the taller figure nor the longer dress did better |

Left as notes for the pilot: goats in a garden or park, figures drawn over the prop beside them, and the goat's body at 45 and 135, priced in `vision/isolation_v041.md`.

## The isolation bench

The list was benched in two rounds of single cut-outs (`vision/isolation_v041.md`). Round 1, twenty-three readers of 45 cut-outs, two to a reader and never two takes of one thing, read each thing in v0.40's cast and scene against the new drawings:
- **The begging dog:** leaning forward from the haunches, the head tipped up less.
- **The stalking cat:** at 45 and 90, the paws apart.
- **The woman in yellow:** taller, with a smaller head and a fuller figure, and that in a dress below the knee.
- **The floating box:** hung level.
- **The heaps' season:** the setting's trees turning, in clusters or the whole crown.

What round 1 found:
- **Nothing better, and two things worse.** The level box in the park read as a box on the ground far off, and the turning trees as fruit.
- **The forelegs.** Every beg, v0.40's included, had its forelegs held out level, "like stiff rods", "like a human arm reaching out".

Round 2, nine readers of one cut-out each, read the forelegs folded beside v0.40's on six seeds: rods or arms in three of v0.40's six and none of the folded six, and kneeling in four against two.

Before any reader, the bench's own look caught three things:
- **The leaning dog placed nowhere at 45.** With its head tipped up 18 or 20 degrees, its gaze passed under the eater's food, and the template placed on none of 40 seeds; at 30 it placed again.
- **A first figure too like the old one.** The woman in yellow's first figure barely differed from v0.40's, and her hair in a bun stood on top like a topknot.
- **Fruit in the trees.** The first turning trees looked like fruit close up, so a whole crown turned was added before any reader saw them.

__DESIGN_TESTS__

## Placement revision 39

Every record stores the placement revision it was made with. v0.41 pictures use revision 39, which draws as revision 38:
- **The floating box:** hung level (`templates.BOX41` "L"), read on the bench and not taken (`BOX41` "O").
- **The heaps' season:** with a heap of dry leaves drawn, the setting's trees turning (`templates.SEASON41` "A" or "B"), read on the bench and not taken (`SEASON41` "O").

Both stay behind their switches so that the bench's cases rebuild, and a v0.40 record rebuilds with the v0.40 package. The cast is v0.40's but for the begging dog's forelegs (builder 0.41.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.41 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.40. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, and v0.41 folds the begging dog's forelegs |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out041/` | The 18 `.blend` families (builder 0.41.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib041/` | Every variant the generated scenes and probes use, carried over from `lib040` or rendered from `out041` |
| `assets/cast/gallery041/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.41.0, placement revision 39); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.41 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v041.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v041.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v041.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-eight screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out041                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out041 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v041   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v041 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery041 --old-gallery <v0.40 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.41 --single   # the release as one zip, tpdb_v0.41.zip
```

The release is one zip, `tpdb_v0.41.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.40 record rebuilds with the v0.40 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
