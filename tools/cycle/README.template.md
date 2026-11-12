# TPDB v0.49: a head with a jaw and a chin, chosen blind among four shapes, and every template through the gate, read a forty-sixth time

v0.48 ended with 63 of the 64 templates through the gate. Sam's brief for v0.49: "go for v0.49 now! This is an improvement, but I am not sure if I love this head shape either, they look a little like bowling pins since they do not have chins. want to focus on a better head shape first using blender and carefully choosing a good style to go with?" The work list came from two places:
- that brief: a better head shape, worked in Blender first, in a style chosen with care;
- v0.48's list (`vision/flaws_v048.md`): the one template that failed its gate, `rain_coming` (R1); the ice cream that stops short of the mouth (R5); grown figures read young and facial hair unseen (O1); the goat's thin rope (O5); and an animal cut off at the picture's foot (O6).

**What v0.48's head was.** An egg, 0.92 of its radius wide and 1.06 tall, narrowing below the cheeks to a rounded point. At nine tenths of the way down it is 0.31 of its half width across, and the neck under it is 0.43, so the jaw's line ran straight on into the neck's and no chin showed. Reviewers who did not know which drawing was which had it as "a circle sitting on a stalk", "a light-bulb or inverted-pear shape" and "a balloon on a stick".

The work is in the cast (builder 0.49.0) and in two placement rules (revision 46). Each change is behind a switch whose letter O gives v0.48's drawing. Two blind benches of the head, an age bench and two rounds of cut-outs (`vision/isolation_v049.md`) took these:
- **The head.** Below its middle the outline is a superellipse, fuller toward the bottom than a ball's, times a taper: the cheeks come down to a corner and the chin is a rounded shelf wider than the neck. The face's side of the head has the same corner, so a side view has a chin and a jaw under it. A shape is a short list of numbers and a person's spec names one: a man's, a woman's a little narrower in the chin, the teenager's between them, a child's as wide as it is tall. One map still places the head, its hair, its hats and every feature of the face.
- **Four shapes went to reviewers,** of about thirty looked at on my own sheets: a tapered jaw, a round jaw, a small chin and a soft square. The round jaw was chosen (below). A sheet of v0.48's head and the four went to Sam before the cast was built, with the round jaw named as the one the release goes ahead with (`vision/isolation_v049/head_candidates.png`).
- **The neck is a part of its own.** As a piece of the skin's one mesh it drew no line where it met the head, and the chin's line across it came out as stubs or dashes. It now keeps its intersections, so that line is drawn whole. It is narrower at the jaw than v0.48's, and the head is carried a tenth of its radius forward of it, so from the side the jaw stands ahead of the neck.
- **The moustache** is a fifth wider and a quarter thicker (O1).
- **The ice cream** is at the mouth: the scoop's near side a finger from the lips, the head tipped twelve degrees to it (R5).
- **The goat's rope** is half as thick again (O5).
- **Placement revision 46, two rules:** that rope; and an animal's box ends 8 px above the picture's foot (O6), a rule that was written three times (below).
- **Put to readers and not taken:** a storm watcher with a hand held out, palm up, for the first drop of rain (R1). One bench reader of four had the rain first, and one had the watcher "looking and pointing toward the right, roughly at a small café table with two chairs"; both readers of v0.48's pointer on the same seeds went on to the rain. And a smaller head on the grown figures, 0.90 and 0.83 of its size, which changed nothing on the age bench.
- **Not changed:** the rest of v0.48's list. The lost balloon (R2), the stopped hose (R3), the trip's hedge (R4), R6, the figures in front of the pond (O2), the seesaw's riders (O3), the painter's roller (O4) and O7 to O9 were not worked and are carried to `vision/flaws_v049.md`.

The set was regenerated and screened a forty-sixth time. Every person is drawn anew, so no picture is identical to v0.48's; thirteen of the sixteen cells have v0.48's seeds and templates, so most of the set is v0.48's set with the new heads.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What Sam's brief, v0.48's readers or the bench said | v0.49 |
|---|---|
| The brief: "they look a little like bowling pins since they do not have chins". On the bench, of v0.48's row: "a circle sitting on a stalk" | A jaw that comes down full to a corner and a broad, rounded chin wider than the neck. v0.48's head was last or fourth for all four reviewers of a ranked sheet. No reader of the 106 pictures wrote of a jaw, a chin or a head's shape, which is weak evidence: the screen asks what happens in a picture and not how a figure is drawn |
| The brief: "carefully choosing a good style to go with" | Four shapes with a chin, judged blind twice. The ranked sheet did not order them: every reviewer put the sheet's top row last, whatever was in it. Read two at a time, each pairing in both orders, the round jaw was chosen over the tapered jaw and over the small chin: "Row a tapers to a small chin under a wide cranium, which looks boyish, while row b's broader, flatter jaw reads as an adult man." |
| **What the jaw did not do.** v0.48: four grown figures called a girl or a boy in 11 of their 81 pictures | **20 of 89** by the same rule: the woman in purple in 9 of 24, "Girl, centre-front: dark ponytail, purple top, teal trousers; running to the right."; the woman in the yellow dress in 5 of 18; the man in green in 4 of 25; the man in the red shirt in 2 of 22. The age bench had found no difference between the two heads, nor from a smaller head. First of the oddities for v0.50 |
| No reader of v0.48's 87 pictures named a moustache or a beard | The wider moustache is named in 13 of its wearer's 22 pictures: "A man with a moustache, in a red shirt and blue trousers". The beard is named in none of its wearer's 25 |
| `rain_coming` 0.889 in three pictures, failing the gate: the reader had the child "pointing up at the sky, perhaps at the storm clouds" and did not go on to the rain | **1.00 in five pictures,** with v0.48's drawing: "pointing up at the dark clouds as though rain is coming". The hand held out for the rain read worse on the bench and was not used, so this is more pictures and other readers, not a mended visual |
| `ice_cream` 0.95: "he does not seem to be eating at this moment, just holding the cone up" | The scoop at the mouth. **1.00 in fourteen pictures,** eaten or licked in thirteen: "walks along the path eating a pink ice-cream cone". Two of its full marks are a call about the eating, for v0.48's two half marks and eight calls |
| The goat's rope: "The goat's lead is thin and hard to see; it could be read as a rope tying it to a stake, or just a stick/line on the grass." | Half as thick again. A rope or a tether in all five of its pictures; the remark is now the stake: "The goat's tether stake looks very short; the goat could be tethered or just standing by a stake." |
| "The dog is cut off at the bottom edge of the picture slightly; otherwise nothing looks strange." | An animal's box ends 8 px above the picture's foot. No description has a figure cut off |
| `lost_balloon` 0.933 and `blocked_hose` 0.95, each beside another reading | **Not worked.** 0.972 in six pictures and 1.00 in five: "The red balloon may belong to the girl (she let go) or to someone else; she seems to be reaching for it."; the dog "on the hose, or on its connector" |
| The seesaw's riders, a remark in four pictures | **Not worked.** Five pictures, with the slide's: "The girl looks small and perches a little above the plank; she might be slightly floating above the seat, but it mostly reads as sitting." |
| The legibility gate, 63 of 64 in v0.48 | **64 of 64,** and all 19 (template, angle) pairs. No item of 1,144 was misread. Nothing was mended, swapped or read again after the screen. With the 42 full marks that stand beside another reading halved, 54 of the 64 pass, for v0.48's 55 |
| The set, 0.993 over all items in v0.48 | **0.967,** and all of the fall is in the setting: nine of the set's ten items under full marks are the clouds or the sun, left out by a reader. Across the screen seven readers left out 41 such items, for v0.48's two readers and 23 |

Left as a note for the pilot: the setting's clouds, trees and sun are left out by some readers and named by others of the same pictures. A person tested will leave them out too, and the pilot's scoring should say whether setting items count.

## The isolation bench

The bench of this release judged a drawing first and events after. Every reviewer and reader was a fresh subagent given its prompt and its pictures and nothing else. The record is `vision/isolation_v049.md`:
- **Bench 1, a ranking.** Nine heads, the same in every row, drawn five ways: v0.48's and the four shapes, as rows A to E in an order shuffled for each of four reviewers. v0.48's head is last or fourth for all four, and is the only row no reviewer placed above fourth. Beyond that the bench does not order the shapes: every reviewer put the row at the top of the sheet last and the second row fourth, whatever was in them, and three different shapes were somebody's first. One reviewer said as much: "Rows C, D and E differ only a little at this size, so the fine points between them are less certain than the points about A and B."
- **Bench 2, pairs.** The three shapes that had been somebody's first, two at a time and larger, each pairing in both orders so that the place on the sheet cancels: six reviewers. The round jaw was chosen over the tapered jaw and over the small chin, and the tapered jaw over the small chin, each in both orders. Of the small chin: "a narrow, tapering V-shaped lower face that ends in a small pointed chin". The differences are small on the women and the children: "The difference is strongest on the men (front, turned, side and bearded) and slight on the women and the child." One of the six described its two rows the wrong way round and chose the round jaw all the same; its choice is counted and its words are not used.
- **The age bench.** Eight people, each standing and walking: sixteen figures of a cast at 0.45 of the release's size, in strips of four, each strip read by one fresh reader who said what they would call each person and how sure they were. Four casts were read: v0.48's, v0.49's, and v0.49's with a grown figure's head at 0.90 and at 0.83 of its size. Of the 14 grown figures, 1, 1, 1 and 0 were called by a young name first, and a young reading was offered beside the name for 10, 9, 9 and 8. Neither a jaw nor a smaller head makes a figure of this size read older, and what the readers go by is elsewhere: "the face looks fairly young and smooth". The wider moustache was named on all four of its figures, where v0.48's had "There may be a small dark moustache, but it is hard to tell at this size."
- **Two rounds of single events cut out of scenes,** thirteen pictures and eight readers.
  - The storm watcher: four pictures of the hand held out and two of the pointer. Both readers of the pointer went on to the rain: "pointing up at the clouds with a worried or frowning face, as if she has noticed that rain is coming". Of the hand held out, one reader had the rain first, two had it as one of two readings, "as if checking for raindrops or gesturing toward something", and one did not have it. At a picture's size an open hand held level is a finger pointed at whatever stands in front of it.
  - The ice cream: all four readers of round 1 have it eaten, and three add that it is too near: "The ice cream almost looks pressed into his cheek or nose instead of just held at his mouth." Moved a finger further off and lower for round 2, both readers have the eating first, and both still note how near it is.
  - The goat's rope, heavier: "A tan rope runs from the collar down to a short brown stake in the ground, so the goat is tethered."

**What the bench leaves open.** Which of the three paired shapes is best on the women and the children, where the reviewers found little between them. And what would make a grown figure read as grown: the bench rules out the head's outline and its size, and names a mark of age, which the two smooth-faced women do not have.

__DESIGN_TESTS__

## Placement revision 46

Every record stores the placement revision it was made with. v0.49 pictures use revision 46: the people's new boxes and anchors, and two rules, each behind a switch whose letter O draws revision 45:
- **The goat's rope** (`ROPE49` B, `scenegen/templates.py`): its two strokes are 6.6 and 4.2 px wide at full size, for 4.6 and 2.6.
- **An animal clear of the picture's foot** (`EDGE49` B and `EDGE49_PX` 8, `scenegen/scene.py`): an animal's box ends at least 8 px above the picture's foot, where 4 px is the rule for everything else. The rule was written three times, and each of the first two cost a build of the set. For every figure, people too, at 14 px, it took from the people the front strip of the ground, where a crowded picture stands its largest figures: the tier-4 garden failed on 56 seeds, the tier-3 playground went to a forced set and no tier-4 isomorph came in 235 calls. For animals only, still at 14 px, the set came back to v0.48's seeds in 14 cells of 16 and the tier-4 isomorph still would not build in 126 calls: a stalking cat and a bird of v0.48's own isomorph stand 8 and 10 px above the foot. At 8 px that isomorph builds on its seed. Each form was tried in the end with one call of last release's isomorph, the switch on and off, which answered in half a minute what the wider and wider searches had not.

`RAIN49` (`scenegen/templates.py`) is the storm watcher with a hand held out, and it is at O: the release draws v0.48's pointer.

A v0.48 record rebuilds with the v0.48 package, and a v0.49 record with v0.49's.

The cast draws every person's head again (builder 0.49.0), behind switches read when it is built: `TPDB_HEAD49`, `TPDB_NECK49`, `TPDB_MOUSTACHE49` and `TPDB_ICE49` at B, which are the code's defaults; the letter O gives v0.48's drawing. `TPDB_HEAD49_SHAPE` takes a shape as JSON for a family, a kind of person or all of them (the bench's sheets were built with it), `TPDB_HS49` scales a grown figure's head (1.0; the age bench's 0.90 and 0.83), and `TPDB_RAIN49` at B builds the pose of the hand held out. The animals are v0.48's. The renderer takes its scale from `TPDB_PPM` (400 px per metre; the bench's sheets were rendered at 800).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.49 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.48. __CALIB_NOTE__

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
| `assets/cast/out049/` | The 18 `.blend` families (builder 0.49.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib049/` | Every variant the generated scenes and probes use, all rendered from `out049`: every person and every animal, nothing carried over |
| `assets/cast/gallery049/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.49.0, placement revision 46); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.49 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v049.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v049.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v049.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty-six screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release; from v0.47 `tools/cycle/forced_cell.py` builds a cell from forced template sets and `tools/cycle/yield_set.py` counts how often a forced set places, with a rule's switch at each of its values; new in v0.48, the helper scripts that earlier releases kept in a scratch folder: `probe_angle.py`, `more_probes.py`, `iso_t4_wide.py`, `merge_iso.py`, `gate_yaw.py`, `strict_count.py` and `who_called.py` |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out049                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out049 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
TPDB_TRIP48=O python vision/isolation_bench.py tpdb_work/bench tpwN_1 tpwN_2   # one template alone, cropped (here with revision 44's trip)
python vision/prepare_screen.py scenes,probes vision/v049   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v049 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery049 --old-gallery <v0.48 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.49 --single   # the release as one zip, tpdb_v0.49.zip
```

The release is one zip, `tpdb_v0.49.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.48 record rebuilds with the v0.48 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
