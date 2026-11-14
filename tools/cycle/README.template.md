# TPDB v0.54: the man who reads is read as a man; two wheel drawings benched in whole pictures and not taken; 63 of 64 templates through the gate, read a fifty-first time

v0.53 ended with every template through the gate and a list of doubts: a bicycle's square wheels that one reader did not name, a second reading of the wheelbarrow's larger wheel, and the man in the red shirt, a boy to the readers of three pictures. Sam's brief for v0.54: "go for v0.54, go ahead and publish and push and put the computer to sleep when you are done". It names no part of the drawing, so the work is the list of `vision/flaws_v053.md`.

Before anything was drawn the last two screens were counted again, by pose and by where in a description a thing is named, and every flagged picture was looked at at full size. The count found what the list had half seen: the man in the red shirt was a boy in every picture in which he reads, four of four over two screens, and in none of his 27 others. Three drawings then went to one bench in whole pictures, twelve fresh readers of six pictures each (`vision/isolation_v054.md`). One was taken.

The work is in the cast (builder 0.54.0). The placement rules are revision 49, unchanged (generator 0.54.0).
- **A grown man with facial hair reads with his head up**: bent 10 degrees over the book for 26 or 30, his eyes on the page (`castlib.actions.READ54`). It is the man in the red shirt and the man in green. On the bench he is a boy in 1 reading of 12, for 6 of 12 as v0.53 drew him, and he is read as reading in every one.
- **Put to readers and not taken:** the bicycle's square wheels larger (`draw.WHEEL54`), which were named no sooner and which two readers of six took for a rack; and tread on the wheelbarrow's square tyre (`draw.TREAD54`), which no reader named, drawn for a second reading that no reader of either tyre gave.
- **Looked at and left:** the begging dog and the stopped hose (R2), whose drawings earlier releases worked, and the six templates of the strict count (R3).

The set was regenerated and screened a fifty-first time. Ninety-five of the 99 screened pictures are v0.53's to the pixel, nineteen of the set's 21 among them; the four that changed are the four that hold one of the two men reading.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What v0.53 drew | v0.54 |
|---|---|
| The man in the red shirt reading, his head bent 26 or 30 degrees over the book. A boy first in every picture in which he read: "Boy on bench, front right: brown hair, red shirt, blue trousers, reading a red book." | His head bent 10 degrees. On the bench a man in 11 readings of 12, for 4 of 12; in the screen a man in both pictures where he sits reading, his moustache named in both: "- Man, front right: brown hair, moustache, red shirt, blue trousers; sitting on a bench reading a red book." |
| The same man walking with an open book, a boy in the one picture of it | Still a boy there, to the screen's reader and to one bench reader of two with his head up: "- Boy, centre front: brown hair, red T-shirt, blue jeans. He is walking or hurrying (motion lines) while reading an open book." On the list for v0.55 |
| A bicycle's square wheels, named late or not at all in 4 readings of 12 over three screens | **Larger wheels benched in whole pictures and not taken.** In the description or the inventory of 8 readings of 12, for 10 of 12 with v0.53's wheels, and a rack to three readers: "The bicycle's wheels sit inside black square frames: it could be a bike parked in a bike rack, or a bike drawn with square wheels." |
| The wheelbarrow's larger square wheel, to two bench readers of five a crate or a grate | **Tread on the tyre benched in whole pictures and not taken.** No reader of either tyre offered the second reading, and none named the tread |
| The legibility gate, 64 of 64 in v0.53 | **63 of 64.** `square_wheel` has 0.896 in eight pictures that are v0.53's to the pixel, where v0.53's readers gave them 0.938: the tier-4 playground's bicycle was a bicycle and no more to a second reader running, and one wheelbarrow's wheel was named only among the unsure things. No item of 1,102 was misread, and nothing was mended, swapped or read again after the screen |
| The set, 0.984 over all items in v0.53 | **0.974**, on nineteen pictures of 21 that are the same pictures. Eight of the set's 286 items are under full marks: the clouds in five pictures, the two items of the tier-4 playground's bicycle, and a half mark on the stopped hose |

Left as a note for the pilot, as in v0.53: the setting's clouds and trees are left out by some readers and named by others of the same pictures. A person tested will leave them out too, and the scoring rule should say whether they count.

## The bench

Every reader was a fresh subagent given its prompt and its pictures and nothing else. The record is `vision/isolation_v054.md`. One bench asked three questions of twelve readers, six pictures each, with the screen's own prompt: v0.53's pictures built again from their own records with one change, and four pictures built for the bench, read beside the same pictures as v0.53 draws them. A reader had two pictures of each question, both drawn one way, and the arms of the three questions were crossed.
- **The man reading.** Six pictures: on a bench in the garden, the park and the playground, and walking in the garden and the street. As v0.53 draws him he is a boy first in 6 readings of 12, from four readers of six, and twice more not a man: "- Left-centre: young person in red shirt and blue trousers sitting on a bench reading a red book." With his head up he is a man in 11 of 12. All 24 readings have him reading, and where a walker with a book is about to meet a box, all six readings of each arm say so.
- **The bicycle.** Four bicycles, as v0.53 draws them and with the wheels larger. The larger wheels were in the description or the inventory of 8 readings of 12, for 10 of 12, and two readers put both their bicycles in a rack and gave square wheels only as the other reading. v0.14 had found the same of a real rack behind the bicycle: two large dark squares under a bicycle are a stand before they are wheels.
- **The wheelbarrow.** v0.53's four barrows, with the tyre plain and with tread. With the tread the wheel is in every description, 12 of 12 for 8 of 12; but the four are two readers' who named their bicycles late as well, no reader named the tread, and the reading it was drawn for came from nobody. A bench whose question is not answered cannot choose, so the tyre stays plain.
- **One more count from the same readings:** the woman in purple is a woman in twelve readings of twelve of two pictures and a girl in three of four of a third, where she looks down into a hose's nozzle.

__DESIGN_TESTS__

## Placement revision 49

Every record stores the placement revision it was made with. v0.54 pictures use revision 49, as v0.53's do: no rule was added. Two switches were added to the scene and left at v0.53's drawing; turned on, each would act only from the revision named in `templates.WHEEL54_REV`:
- `draw.WHEEL54` (O; B is the bicycle's square wheels 38 units from hub to side for 30, the frame raised and the wheelbase longer by as much);
- `draw.TREAD54` (O; T is tread across the wheelbarrow's square tyre).

The cast is v0.52's, which v0.53 kept, with one pose rule more (builder 0.54.0; `castlib.actions.READ54` B, where O builds v0.53's): the two grown men with facial hair read with the head up, in the four poses that hold a book. Every other variant is v0.53's file. A sprite's box and mask are new in those poses, so the one cell that holds both men reading, the tier-3 garden, placed in another layout under the same rules.

A v0.53 record rebuilds with the v0.53 package, and a v0.54 record with v0.54's.

One line of v0.53's code was wrong and is put right: the header of `scenegen/scene.py` said the woman in purple had been drawn again in v0.53. She was benched and not drawn again, as v0.53's README said.

__INSPECTION__

The planner's difficulty priors are the calibration measured under revision 49 with the new cast (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.53. __CALIB_NOTE__

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
| `assets/cast/out054/` | The 18 `.blend` families (builder 0.54.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib054/` | Every variant the generated scenes and probes use: v0.53's files, and the two men's reading poses rendered from `out054` |
| `assets/cast/gallery054/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.54.0, placement revision 49); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.54 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v054.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v054.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v054.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all fifty-one screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release; from v0.47 `tools/cycle/forced_cell.py` builds a cell from forced template sets and `tools/cycle/yield_set.py` counts how often a forced set places, with a rule's switch at each of its values; new in v0.48, the helper scripts that earlier releases kept in a scratch folder: `probe_angle.py`, `more_probes.py`, `iso_t4_wide.py`, `merge_iso.py`, `gate_yaw.py`, `strict_count.py` and `who_called.py`; and from v0.50 `tools/cycle/age_scenes.py`, which builds pictures of the last screen again with trial casts and counts what their figures are called; and from v0.51 `tools/cycle/extra_probes.py`, which forces probes for a carrier that the counts by template do not see; and from v0.52 `tools/cycle/fig_pairs.py`, which makes the sheets and prompts of a blind bench of two drawings of the same figures, and `tools/cycle/who_build.py`, which builds the last screen's pictures again with a trial cast; and from v0.53 `tools/cycle/bench_build.py`, `bench_prepare.py` and `bench_tally.py`, a bench in whole scenes that asks two questions of one set of readers, `tools/cycle/calib_cmp.py`, which counts what moved between two calibrations, and `tools/cycle/crops.py`, which cuts named elements out of built pictures onto a sheet; and from v0.54 `tools/cycle/pixcmp.py`, which says which pictures of a folder are another folder's to the pixel, `tools/cycle/who_pose.py`, which counts what a screen's readers called a figure by its pose, and `tools/cycle/retest.py` (v0.53's), which compares the scores of the pictures that came back with the last screen's |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out054                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out054 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
TPDB_TRIP48=O python vision/isolation_bench.py tpdb_work/bench tpwN_1 tpwN_2   # one template alone, cropped (here with revision 44's trip)
python vision/prepare_screen.py scenes,probes vision/v054   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v054 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery054 --old-gallery <v0.53 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.54 --single   # the release as one zip, tpdb_v0.54.zip
```

The release is one zip, `tpdb_v0.54.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.53 record rebuilds with the v0.53 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
