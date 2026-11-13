# TPDB v0.53: a larger square wheel on the barrow, chosen in whole pictures; all 64 templates through the gate, read a fiftieth time

v0.52 ended with one template under the gate: `square_wheel`, because two readers of the four wheelbarrows did not notice the wheel. Sam's brief for v0.53: "go for v0.53!" It names no part of the drawing, so the work is the list of `vision/flaws_v052.md`, the square wheel first.

Every flagged picture of v0.52 was looked at again at full size before anything was drawn, and each proposal on the list was read against the comments in the code. Three of the list's drawings had been tried in earlier releases and are left; two remarks were measured and are left; and two things went to one bench in whole pictures (`vision/isolation_v053.md`).

The work is in the scene (generator 0.53.0, placement revision 49). The cast is v0.52's, unchanged (builder 0.52.0).
- **The wheelbarrow's square wheel is larger**: 68 units across for 50, the tub, the handles and the legs raised with it (`draw.WHEEL53`). The shape, which earlier benches chose, is kept.
- **A child jumping for joy is never planned into a picture with a game of catch** (`templates.JUMP53`). A gap between them was tried first and read no better.
- **Put to readers and not taken:** the woman in purple with a fuller figure and a cardigan, or a longer skirt (v0.52's O1). In eighteen whole pictures she was called a woman with either, and with v0.52's drawing too.
- **Looked at and left:** the floating box lower with a shadow (R3) and a piece of bread in the thief bird's beak (R4), which earlier releases drew and replaced; the heavy seesaw's man (O2), whose seat measures right; and figures over the pond's near edge (O3), which every reader places on the bank.

The set was regenerated and screened a fiftieth time. Nineteen of its 21 pictures are v0.52's to the pixel: the twelve cells of tiers 1 to 3, the tier-4 park and street and the five isomorphs. The tier-4 garden and playground are new.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What v0.52 drew | v0.53 |
|---|---|
| The wheelbarrow's square wheel, 50 units across and half under its fork. Two readers of v0.52's four barrows did not notice it: "Wheelbarrow, bottom right: grey." | 68 units across. On the bench in whole pictures it is in the description or the inventory of 10 readings of 10, for 4 of 8 with v0.52's wheel: "On the left of the lawn stands an empty grey wheelbarrow, but its wheel is drawn as a square, which would not roll." |
| The same wheel, read by nobody as anything else on the bench | A second reading from two readers of five: "It could alternatively be read as a crate or grate placed in front of the wheelbarrow, but it sits where the wheel should be." On the list for v0.54 |
| A child jumping for joy beside a game of catch, the jump read as a try for the ball | Never planned into one picture. With the jumper 150 units behind the catcher two readers of two still tied them: "he could be trying to catch it too" |
| The woman in purple a girl first in 4 of her 25 screened pictures | **Two drawings benched in whole scenes and not taken.** A woman in 18 readings of 18 with a cardigan, with a longer skirt and with v0.52's drawing. In the screen a girl first in 2 of 25 |
| The legibility gate, 63 of 64 in v0.52 | **64 of 64.** `square_wheel` has 0.938 in its eight pictures: the four wheelbarrows read in full, and a bicycle's square wheels went unnamed in one picture of four. No item of 1,102 was misread, and nothing was mended, swapped or read again after the screen |
| The set, 0.986 over all items in v0.52 | **0.984.** Five of the set's 286 items are under full marks: the clouds in three pictures, and the two items of the bicycle in the new tier-4 playground |

Left as a note for the pilot, as in v0.52: the setting's clouds and trees are left out by some readers and named by others of the same pictures. A person tested will leave them out too, and the scoring rule should say whether they count.

## The bench

Every reader was a fresh subagent given its prompt and its pictures and nothing else. The record is `vision/isolation_v053.md`. One bench asked two questions of nine readers, eight pictures each, with the screen's own prompt: v0.52's pictures built again from their own records with one change, read beside v0.52's own.
- **The wheel.** Three of v0.52's wheelbarrows, as screened and with the larger wheel; a reader had two barrows, both drawn one way. With v0.52's wheel two readers of four named it in the description of both their barrows and two came to it only at the end, among the things they were unsure of. With the larger wheel all five readers have it in the description or in the barrow's own line, in both their pictures.
- **The woman in purple.** Eighteen of v0.52's pictures of her, the four in which the screen's readers called her a girl among them, as screened and with each of two drawings. She is a woman in all 54 readings. A bench whose first arm does not show the fault cannot choose, so her drawing stays. The screen says where the fault lives: v0.52's four girls were three readers' of thirteen.
- **Looked at large and set aside before the bench:** her hair in a low bun (from the front, a boy with short hair), her hair cut to the shoulders (hardly a change), a skirt to the knee (younger, not older).

__DESIGN_TESTS__

## Placement revision 49

Every record stores the placement revision it was made with. v0.53 pictures use revision 49, which adds two rules to revision 48, each behind a switch whose letter O gives revision 48's drawing:
- `draw.WHEEL53` (B): the wheelbarrow's square wheel 34 units from hub to side for 25, and the barrow raised by as much. It costs no place: the barrow alone placed on twelve garden seeds of twelve with either wheel.
- `templates.JUMP53` (X): the jump and the game of catch share an exclusive tag, read when the planner asks, so that revision 48's records keep their plans. The gap of the first rule (B) stays for a forced set; forced together on twelve seeds it cost two places in the garden and one each in the park and the playground.

A v0.52 record rebuilds with the v0.52 package, and a v0.53 record with v0.53's.

The cast is v0.52's, file for file (builder 0.52.0; `assets/cast/out053` is a copy of v0.52's `out052`). Two switches were added to it and left at v0.52's drawing: `TPDB_ANA53`, the woman in purple's benched drawings, and with it a hair style cut to the shoulders (`people.SHOULDER53`).

__INSPECTION__

The planner's difficulty priors are the calibration measured under revision 49 (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.52. __CALIB_NOTE__

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
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg, and from v0.32 `~body` and `~legs` at both legs, for the bench; from v0.46 a family's config can ask for a wider line round the figure's outer edge (`silhouette_px`), a line that takes no light (`unlit`) and cel tones of its own (`cel`); from v0.47 those tones can light a figure's trunk by its normals in the rest pose (`rest`), so the shadow's edge does not break where an arm bends the trunk's skin; from v0.48 a side view of a pose can be drawn with face states of its own (`profile_face` in the pose's config, `expression_states_profile` in the family's), and the scale is read from `TPDB_PPM`) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant; from v0.32 a piece of a split figure is checked by its base pose, and the manifest schema takes the `~` suffix; from v0.46 a record that carries its own cel tones is measured against those tones, and the schema takes the line's and the tones' new fields; from v0.47 the schema takes the manifest's `rest` field |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads, v0.44 sits the reading dog up in reading glasses, redraws the cats' ears, the goat's beard and the dogs' noses, gives props colours of their own and redraws the run, the sand spade, the nozzle's inspection, the call from the seesaw and the content face, v0.45 enlarges the ice cream, redraws the camera, the shoes' soles, the trowel, the paint roller, the carried box and the kite's reel, turns the hose inspector's head to the viewer and hides the swimming duck's legs, v0.46 draws the whole cast again: a heavier outer line and two flat tones, no added neck under the three smaller heads, higher necklines, fuller sleeves, no wrist seam, the vest's bands on the vest, a plain wire for the glasses, a smoother moustache and a line mouth on a dark line of its own, and v0.47 draws the cast's anatomy again: sloped shoulders, tapered arms and legs with their joints, a thumb, a wedge shoe on a sole, a skirt that turns with the thighs, a nose with no line round it, a three-quarter side view, glasses as flat rings, the cardigan's V and buttons, a wider moustache in two halves, the animals' eyes, markings, tails and paws, and the weak actions (the walk, the run, the sit on the ground, the reading dog's pose of its own, the dog on the hose, the peck and the stalk), and v0.48 draws the heads, faces and hair again (an egg head with a jaw and a chin, a smaller and lower face with a plain line for a mouth, hair cut along a curve with a parting, a face of its own for a side view, one flat tone, a tee to the hips, feet turned out) and every animal's body and limbs (the dogs' and cats' bodies, joints, skulls and tails, the cats' eyes, the goat's barrel, legs and face), and v0.49 draws every person's head again (a jaw down to a corner and a rounded chin wider than the neck, a shape for each kind of person in `core.HEAD49_SHAPES`, the neck a part of its own), with a wider moustache and the ice cream at the mouth |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out053/` | The 18 `.blend` families (builder 0.52.0: the cast is v0.52's, unchanged), their render configs and `cast_catalog.json` |
| `assets/cast/lib053/` | Every variant the generated scenes and probes use: v0.52's files for what v0.52's set used, and the rest rendered from `out053` |
| `assets/cast/gallery053/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.53.0, placement revision 49); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.53 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v053.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v053.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v053.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all fifty screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release; from v0.47 `tools/cycle/forced_cell.py` builds a cell from forced template sets and `tools/cycle/yield_set.py` counts how often a forced set places, with a rule's switch at each of its values; new in v0.48, the helper scripts that earlier releases kept in a scratch folder: `probe_angle.py`, `more_probes.py`, `iso_t4_wide.py`, `merge_iso.py`, `gate_yaw.py`, `strict_count.py` and `who_called.py`; and from v0.50 `tools/cycle/age_scenes.py`, which builds pictures of the last screen again with trial casts and counts what their figures are called; and from v0.51 `tools/cycle/extra_probes.py`, which forces probes for a carrier that the counts by template do not see; and from v0.52 `tools/cycle/fig_pairs.py`, which makes the sheets and prompts of a blind bench of two drawings of the same figures, and `tools/cycle/who_build.py`, which builds the last screen's pictures again with a trial cast; and from v0.53 `tools/cycle/bench_build.py`, `bench_prepare.py` and `bench_tally.py`, a bench in whole scenes that asks two questions of one set of readers, `tools/cycle/calib_cmp.py`, which counts what moved between two calibrations, and `tools/cycle/crops.py`, which cuts named elements out of built pictures onto a sheet |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out053                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out053 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
TPDB_TRIP48=O python vision/isolation_bench.py tpdb_work/bench tpwN_1 tpwN_2   # one template alone, cropped (here with revision 44's trip)
python vision/prepare_screen.py scenes,probes vision/v053   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v053 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery053 --old-gallery <v0.52 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.53 --single   # the release as one zip, tpdb_v0.53.zip
```

The release is one zip, `tpdb_v0.53.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.52 record rebuilds with the v0.52 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
