# TPDB v0.55: a seated figure has a knee and a flat seat, and its feet are under its knees; 63 of 64 templates through the gate, read a fifty-second time

v0.54 ended with 63 of its 64 templates through the gate and a list of doubts. Sam's brief for v0.55: "go for v0.55 now, and fix up how the legs of the characters work when they are sitting like this:", with v0.54's own sheet of the man in the red shirt seated at two angles and squatting on the seesaw's low end. The brief names one part of the drawing, so that is the release: the list of `vision/flaws_v054.md` was not worked and stands as it was.

Before anything was drawn, all ten people were rendered from v0.54's cast at twice the release's size, in eight seated views each. The sheets show three things. A seated leg had no knee: the trousers are one hull with a ring at the hip, the knee and the cuff, the knee's ring is carried half by the thigh and half by the shin, and bent a right angle it shrinks, so the leg was a hose that thinned to its bend. The seat was a sack that hung under the thigh, with nothing flat where the figure sits. And the feet were set well ahead of the knees, so the shins sloped forward, a child's by twenty degrees, and the thighs ran off the front of a bench. Thirty-three of v0.54's 99 screened pictures hold a seated figure.

The work is in the cast (builder 0.55.0). The placement rules are revision 49, unchanged (generator 0.55.0).
- **The lower body of a seated figure is drawn in stiff pieces** (`castlib.people.SEAT55`). On a seat, a swing, the seesaw and the slide the standing trousers, skirt and bare legs are hidden and another set of objects is shown: the hips as a block that is flat underneath, at the level of the thighs' underside; a thigh and a shin that keep their thickness and each end in a dome just short of the knee joint, the two domes being the knee; a trouser cuff that rides up to the ankle so the shoe shows whole; bare legs in the same way under a short sleeve of the shorts or a skirt's wrap of the two thighs.
- **The feet are under the knees** (`castlib.actions.SIT55`). On a seat the thigh is level and the shin upright, the far foot a little ahead so that both shins show. The reader on the seesaw's low end sits with the legs out and the book held higher, the knee showing under the forearm.
- **Standing figures are v0.54's.** The standing objects are not touched, and every variant that is not seated is v0.54's file.
- **Judged blind before it was built into scenes:** four benches of pairs, 42 reviewers, chose the new drawing in 36 reviews, and a bench in eighteen whole pictures found every event read as before.
- **Not worked:** the square wheel (R1), the stopped hose (R2) and the strict count's templates (R3) of v0.54's list.

The set was regenerated and screened a fifty-second time. Sixty-nine of the 99 screened pictures are v0.54's to the pixel, thirteen of the set's 21 among them; the thirty that changed are the thirty that hold a figure on a seat, a swing, a seesaw or a slide, and each has v0.54's templates and v0.54's people in v0.54's places.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What v0.54 drew | v0.55 |
|---|---|
| A seated leg with no knee. Of v0.54's row, from reviewers who did not know which it was: "- All four: the legs are soft, uniform tubes with weak knee definition. At the small size the knees almost vanish and the legs look rubbery." | A thigh and a shin that keep their thickness, with a rounded knee. The reason most reviewers gave for choosing it: "It reads clearly as sitting at both sizes, with a level lap, a clear knee and upright shins." |
| A seat that hung under the thigh: "- All four figures: the seat sags below the line of the thigh, as a rounded pouch, with no flat underside, so nothing suggests a seat surface." | The hips a block, flat underneath and no further back than the back. The first trial's seat stood out behind the back, which nine reviewers of twelve named, and was drawn again |
| The feet ahead of the knees: "- All four: the thigh slopes clearly downward from hip to knee, so the knee sits well below the hip and the pose reads as perching, leaning, or sliding off the edge." | The feet under the knees, the thigh level and the shin upright. In whole pictures a doubt about a sitter's legs, feet or seat is in 6 readings of 36, for 10 of 36 of v0.54's pictures read by the same twelve readers |
| The reader on the seesaw's low end squatting, the knee thin under the forearm | The legs out and the book higher. His template reads 1.00; two readers of his three pictures now have him on the grass at the plank's end: "- The man seems to sit almost on the grass at the end of the seesaw rather than clearly on the seat; could be read as sitting on the ground holding the end down." It is on the next list |
| The seven templates that draw a figure on a seat, each 1.00 in v0.54 | **Each 1.00**, and each of their 37 items has the score it had: "- Man, right front: brown hair, moustache, red shirt, blue trousers; sitting on a bench reading a red book." |
| The legibility gate, 63 of 64 in v0.54 | **63 of 64.** `square_wheel` has 0.938 in eight pictures and one misread, which fails it: the tier-4 playground's bicycle, whose part of the picture did not change, was "lying on its side" to a second reader running. No other template is under 0.96 |
| The set, 0.974 over all items in v0.54 | **0.972**, on thirteen pictures of 21 that are the same pictures and eight with a sitter drawn again. Ten of the set's 286 items are under full marks: the clouds or a tree in five pictures, the two items of the tier-4 playground's bicycle, two half marks in the tier-4 street and a half mark on the stopped hose |

Left as a note for the pilot, as in v0.53 and v0.54: the setting's clouds and trees are left out by some readers and named by others of the same pictures. A person tested will leave them out too, and the scoring rule should say whether they count.

## The benches

Every reviewer and reader was a fresh subagent given its prompt and its pictures and nothing else. The record is `vision/isolation_v055.md`.
- **Pairs.** A sheet shows four seated figures drawn two ways, v0.54's and the trial's, with nothing said of which row is which; every set of four is made twice, v0.54's row above and below, so that a row's place cancels. Six sets: trousers and bare legs at three-quarters and from the side, the seesaw's riders, and the swing and the slide. Four rounds, each against the trial as it then stood: the new drawing was chosen by 12 reviewers of 12, 10 of 12, 10 of 12 and 4 of 6. A sitter seen from the side, in trousers or with bare legs, and one with bare legs at three-quarters went to it in both orders in every round, twenty reviewers of twenty. The swing and the slide went to whichever row was drawn below in three rounds of four, and trousers at three-quarters in the last two: there the drawings are a toss-up.
- **What each round changed.** The reviewers named the new drawing's faults as well, and each round mended what the last named: the seat behind the back; a knee that was "a hard square corner"; two shins that lay one on the other at three-quarters; a strip of trouser under a child's tee; trouser shins thinner than standing ones; a slider bent like a chair-sitter. The release's drawing has two small changes that no round of pairs saw, the cuff that rides up and the slider's reach; they were read in whole pictures.
- **Whole pictures.** Eighteen of v0.54's pictures with a seated figure, built again from their own records with the release's cast, each read both ways by twelve readers with the screen's own prompt, six pictures a reader and no picture twice. The figure sits in 36 readings of 36 both ways; the reader reads, the eater eats, the seat that is missing is missed and the child on the heavy seesaw is up in the air, in every reading both ways. Of v0.54's pictures: "- The woman's legs go in front of the bench seat edge so she seems to sit on the very front of it; nothing clearly wrong though." Of the new cast's, a figure that sits on nothing: "- The woman in yellow is drawn sitting but there is nothing under her: she appears to be sitting on thin air. This could be intended as sitting on the grass, but her knees are bent at chair height and her feet are on the ground, so it looks like a missing chair."
- **What stands at the end.** The grown figures' thigh is 30 cm for a shin of 37 (v0.27 shortened the thigh so that a sitter's feet reach the ground), and a level thigh shows it: "- All four: the shins are very long compared with the thighs and torso, so every figure looks like it sits on a high bar stool. This is worst for the teenager and the woman."

__DESIGN_TESTS__

## Placement revision 49

Every record stores the placement revision it was made with. v0.55 pictures use revision 49, as v0.53's and v0.54's do: no rule was added. The two switches that v0.54 added to the scene and left off are still off (`draw.WHEEL54`, `draw.TREAD54`).

The cast is v0.54's with the lower body of a seated figure drawn again (builder 0.55.0; `castlib.people.SEAT55` B and `castlib.actions.SIT55` B, where O builds v0.54's). The seated objects are shown in the postures on a seat, a swing, the seesaw and the slide (`build_cast.SEATED55`) and the standing ones in the rest; sitting on the ground, with the legs out straight, is v0.54's drawing. Every variant that is not seated is v0.54's file. A seated sprite's box and mask are new, and every one of the 99 pictures still placed every figure where v0.54 had it.

A v0.54 record rebuilds with the v0.54 package, and a v0.55 record with v0.55's.

__INSPECTION__

The planner's difficulty priors are v0.54's, and each record's predicted difficulty is computed from the calibration measured under revision 49 with the new cast (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.54. __CALIB_NOTE__

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
| `assets/cast/out055/` | The 18 `.blend` families (builder 0.55.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib055/` | Every variant the generated scenes and probes use: v0.54's files, and the people's seated poses rendered from `out055` |
| `assets/cast/gallery055/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.55.0, placement revision 49); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.55 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v055.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v055.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v055.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all fifty-two screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release; from v0.47 `tools/cycle/forced_cell.py` builds a cell from forced template sets and `tools/cycle/yield_set.py` counts how often a forced set places, with a rule's switch at each of its values; new in v0.48, the helper scripts that earlier releases kept in a scratch folder: `probe_angle.py`, `more_probes.py`, `iso_t4_wide.py`, `merge_iso.py`, `gate_yaw.py`, `strict_count.py` and `who_called.py`; and from v0.50 `tools/cycle/age_scenes.py`, which builds pictures of the last screen again with trial casts and counts what their figures are called; and from v0.51 `tools/cycle/extra_probes.py`, which forces probes for a carrier that the counts by template do not see; and from v0.52 `tools/cycle/fig_pairs.py`, which makes the sheets and prompts of a blind bench of two drawings of the same figures, and `tools/cycle/who_build.py`, which builds the last screen's pictures again with a trial cast; and from v0.53 `tools/cycle/bench_build.py`, `bench_prepare.py` and `bench_tally.py`, a bench in whole scenes that asks two questions of one set of readers, `tools/cycle/calib_cmp.py`, which counts what moved between two calibrations, and `tools/cycle/crops.py`, which cuts named elements out of built pictures onto a sheet; and from v0.54 `tools/cycle/pixcmp.py`, which says which pictures of a folder are another folder's to the pixel, `tools/cycle/who_pose.py`, which counts what a screen's readers called a figure by its pose, and `tools/cycle/retest.py` (v0.53's), which compares the scores of the pictures that came back with the last screen's; and from v0.55 `tools/cycle/sit_screen.py`, which prints what two screens' readers doubted about the seated figures of the same pictures (`tools/cycle/fig_pairs.py` and the three `bench_*.py` are v0.55's own) |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out055                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out055 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
TPDB_TRIP48=O python vision/isolation_bench.py tpdb_work/bench tpwN_1 tpwN_2   # one template alone, cropped (here with revision 44's trip)
python vision/prepare_screen.py scenes,probes vision/v055   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v055 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery055 --old-gallery <v0.54 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.55 --single   # the release as one zip, tpdb_v0.55.zip
```

The release is one zip, `tpdb_v0.55.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.54 record rebuilds with the v0.54 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
