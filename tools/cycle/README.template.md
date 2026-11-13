# TPDB v0.50: grown figures read as grown, measured in whole scenes; the seesaw's children seated; two templates under the gate, read a forty-seventh time

v0.49 ended with all 64 templates through the gate and a list of what read least well. Sam's brief for v0.50: "go for v0.50!" It names nothing in the pictures, so the work list is v0.49's own (`vision/flaws_v049.md`):
- its two oddities of grade A: grown figures read as children, in 20 of their 89 pictures (O1), and riders drawn above their seat on the seesaw and the slide (O2);
- the templates that read least well: the lost balloon (R1), the stopped hose (R2), the game of catch (R3), the dogs (R4) and the heavy seesaw's call (R5);
- the smaller oddities: the painter's roller (O3), the goat's stake (O4), a held balloon's string (O5) and O6 to O8.

The work is in the cast (builder 0.50.0) and in the placement rules (revision 47). Each change is behind a switch whose letter O gives v0.49's drawing, and each was read blind against v0.49's drawing on the same seeds before it went in (`vision/isolation_v050.md`):
- **The grown figures.** Marks of age: the woman in purple as tall as the woman in the yellow dress, and both with a woman's bust; the yellow dress to below the knee; a fuller beard for the man in green, one that stands off the chin. And proportions: every grown figure's head is 0.86 of its v0.49 size on the same body, about five heads tall for four and a third. The teenager and the children are as they were. Each change was measured alone and both together, in whole scenes (below), and the release has both. A sheet of the four casts with the counts on it went to Sam before the cast was built (`vision/isolation_v050/age_candidates.png`), with both named as the one the release goes ahead with.
- **The seesaw's children** are set down until their own drawing rests on the plank. The rise is measured in each sprite, where a constant from v0.31 had been left 4 to 10 units too high by two redrawings of the bodies. The handle is a grab bar that comes down to the plank ahead of the knees, since the seated riders hid the old post in their laps (O2).
- **The lost balloon's string** ends a head's height above the reaching hand in the garden too, where a rule of v0.45 had lifted it onto the hedge, up to 200 units from the hand (R1).
- **The goat's stake** is half as tall again, the rope in two turns round its upper part (O4). **A held balloon's string** hangs in a loose S (O5). **The painter's pole** is dark, where it had the colour of the fence behind it (O3).
- **Put to readers and not taken:** the stopped hose with no swelling before the paw (R2), and three other places for the child on the slide (O2). Each read no better than v0.49's drawing, or worse.
- **Looked at and left:** the game of catch (R3), the dogs (R4), the heavy seesaw's call (R5), the reading dog's glasses (O6) and O7. The game of catch then failed this screen's gate.

The set was regenerated and screened a forty-seventh time. Every grown figure is drawn anew, so no picture is identical to v0.49's. Five of the sixteen cells have v0.49's templates, the three tier-4 cells on v0.49's seeds among them; the other eleven are new sets, drawn by the planner from the new prior.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What v0.49's readers or the bench said | v0.50 |
|---|---|
| Four grown figures called a girl or a boy first in 20 of their 89 pictures: "Girl, centre-front: dark ponytail, purple top, teal trousers; running to the right." | **3 of 79** by the same rule: the woman in purple in 1 of 18, the woman in the yellow dress in none of 18, the man in the red shirt in 2 of 23, the man in green in none of 20. The runner is "Woman 2, right, front: dark hair, purple top, teal trousers; running to the right, speed lines behind her." The bench had counted 1 of 45 for 13 of 45 beforehand, on other pictures and with other readers |
| The beard of the man in green named in none of his 25 pictures | Fuller, and named in **16 of 20**: "short dark hair and beard, green shirt, beige trousers" |
| The moustache of the man in the red shirt named in 13 of his 22 pictures | **7 of 23.** On the smaller head it is a smaller mark, as the bench had shown, and its wearer is the one grown figure still called a boy: "Boy, left front: brown hair, red shirt, blue jeans; sweeping leaves on the path with a broom." Second of the oddities for v0.51 |
| The seesaw's riders: "The girl looks small and perches a little above the plank; she might be slightly floating above the seat, but it mostly reads as sitting." | Seated by measure, with a grab bar. **No rider above the plank in any of the ten pictures with a seesaw,** and the handle held in every one: "sitting on the raised left end of the seesaw, holding the handle." |
| The child on the slide: "The girl seems to sit slightly above the chute surface" | **Not changed.** Four places for the slider read alike on the bench. One screen picture of five: "The boy sits slightly above the chute surface in places, but it reads normally as sliding." |
| `lost_balloon` 0.972: "The red balloon may belong to the girl (she let go) or to someone else; she seems to be reaching for it." | The string's end a head's height above the hand in the garden too. **1.00 in five pictures,** and nobody else's balloon in any. The end is now near other things in three: "although a viewer might wonder whether it is tied to something on the fence" |
| `blocked_hose`: the dog "on the hose, or on its connector" | **Benched without its swelling and left as it was:** without it the stopped water was read by one of three, for two of three. 0.95 in five pictures, two half marks in one: "It is not completely clear whether the dog's paw is actually on the hose or just behind the bulge" |
| "The goat's tether stake looks very short; the goat could be tethered or just standing by a stake." | Half as tall again, the rope round its upper part. No reader calls it short: "The rope from the goat's collar to the stake is clear; it is just tethered, not escaping." |
| "The balloon's string is perfectly straight and stiff, so it could be a balloon on a stick, or a lollipop/ice lolly on a stick; most likely a balloon." | A loose S. No stick in any of its five pictures; once "The balloon string seems to loop around near the girl's head/face rather than run straight to her hand." |
| "The roller looks a little small and oddly held, high above the woman's hand, but it reads as painting." | A dark pole. Painting in all nine pictures and no roller above a hand; one reader of one picture: "The roller's top part looks almost like a separate pale cylinder against the fence" |
| `play_catch` 1.00 by the gate, one reader's doubt: "she could also be the one who threw it" | **Looked at and left, and it fails: 0.80 in five pictures.** A small girl has thrown to a grown woman, and the ball is drawn by the woman's hands: "So the two are playing catch, and the ball is either just leaving the woman or arriving at her." |
| `square_wheel` 1.00 in four pictures, three bicycles and a wheelbarrow | **Not worked, and it fails: 0.875 in four pictures, with the screen's one misread.** The bicycles read at once. The wheelbarrow has the sprinkler's hose on the ground behind its wheel: "There is a square dark-framed object behind/under the wheelbarrow (looks like a hose reel or a fan-like grate), partly hidden; unclear what it is." |
| The legibility gate, 64 of 64 in v0.49 | **62 of 64,** and 18 of the 19 (template, angle) pairs. One item of 992 was misread. Nothing was mended, swapped or read again after the screen. With the 33 full marks that stand beside another reading halved, 52 of the 64 pass, for v0.49's 54 |
| The set, 0.967 over all items in v0.49 | **0.949.** Nine of the set's eighteen items under full marks are the clouds or a tree, left out by a reader, as many as in v0.49; the other nine are the game of catch, the wheelbarrow's wheel, the thief bird and the bread for the ducks, in five pictures |

Left as a note for the pilot, as in v0.49: the setting's clouds and trees are left out by some readers and named by others of the same pictures. A person tested will leave them out too, and the pilot's scoring should say whether setting items count.

## The isolation bench

Every reader was a fresh subagent given its prompt and its pictures and nothing else. The record is `vision/isolation_v050.md`:
- **The age bench, in whole scenes.** v0.49 had built a bench for the grown figures, strips of four small figures cut out and read alone, and that bench could not see the fault: whatever the cast, one figure of fourteen was called young. Readers call a figure young in a scene, where there are children and things to do. So this bench reads whole scenes (`tools/cycle/age_scenes.py`). Thirty-two of v0.49's own screened pictures were built again from their records with three other casts, on the same seeds and with the same forced sets, and all 96 came back with the same templates and the same poses for the same people. Sixteen readers had eight pictures each, two of every cast, and no reader saw a picture twice. The prompt and the count are the screen's own. Called young first, of the four figures' 45 appearances: **13 with v0.49's cast, 3 with the marks of age, 5 with the smaller heads, 1 with both.** The bench finds the screen's fault where it is, 13 of 45 for the screen's 16 of 45 on the same pictures, and each change cuts it by itself. The same picture in two casts: "Girl (left, front-middle): dark hair in a ponytail, purple top, teal trousers; walking beside the path while eating a pink ice-cream cone." and "Woman, left: purple top, teal trousers, dark ponytail. Walking on the path, eating a pink ice-cream cone." No reader of any cast wrote of a head's size, of a bust or of the dress's length: what the changes moved is what the figures were called.
- **Three rounds of cut-outs, the rules in the scene,** forty-four cut-outs and seventeen readers; no reader saw two takes of one thing.
  - The seesaw. v0.49's: "The right child appears to sit slightly above/in front of the plank rather than firmly on it". Seated by measure, no rider was above the plank, and the handle was gone in three of three: "Neither child seems to have handles to hold; their hands are just held in front of their bodies or in their laps." With the grab bar a handle was held in five of five: "Each child holds a dark grip handle in front of them."
  - The slider, in four places: in front of the chute, behind its near wall, sunk until the wall hid the hips, and on top of the far rail. A remark on how the child sits in two, two, three and three cut-outs of three: "The child appears to be sitting slightly above the chute rather than clearly resting on it". Where the slider is put is not what the readers see, and none was taken.
  - The stopped hose with no swelling. No reader named a connector, and one of three went on to the stopped water, for two of three with the swelling: "The hose has a bulge/kink right where the dog's front paw is, so it reads as the dog stepping on the hose (blocking the water) - or it could just be a hose fitting/joint." The swelling is misnamed, and it is also what says that something happens at the paw. It stays.
  - The lost balloon's string. Lifted above the fence, as v0.49 drew it in the garden: "so the link between him and that balloon is implied rather than shown". By the hand, two of three were not sure it had left the hand: "the child is still holding it and the gap is a drawing error". A head's height above the hand, it had escaped from this child in three of three, and that was taken.
  - The goat's stake, one cut-out each way: tethered both ways, and a short stake both ways. Taken because the rope is now tied on the stake where it lay at its foot, and it costs nothing in placement.
- **A fourth round, the cast's two props,** twelve cut-outs and six readers. The straight balloon string was a stick in two of three, "She holds a long stick in one raised hand, with a yellow oval on top of it.", and the loose S a string in three of three. With the wood-coloured pole two readers of three offered something else for the roller's head, "the roller could also be taken for a can or cylinder held against the fence", and with the dark pole none did.

**What the bench leaves open.** The slide: what is untried is the chute's own drawing and the slider's pose. And the lost balloon's cut-outs do not choose between the string lifted over the fence and the string a head above the hand: the second was taken because its end is by the child and no reader of it held the balloon.

__DESIGN_TESTS__

## Placement revision 47

Every record stores the placement revision it was made with. v0.50 pictures use revision 47: the grown figures' new boxes and anchors, and three rules, each behind a switch whose letter O draws revision 46:
- **A child on the seesaw sits on the plank** (`SEAT50` B, `scenegen/templates.py`): the rule measures how far each child's drawing reaches below its seat anchor, at the hips (`_under50`), and sets that edge 1.5 units into the plank's top edge. The handle is a bar that leaves the post's top and comes down to the plank in front of the rider (`draw.seesaw`, `arch`), and an empty seesaw has the same bars (`SEESAW50` B, `scenegen/settings.py`). The grown rider of the heavy seesaw is seated as before.
- **The lost balloon's string** (`LOST50` M) ends a head's height above the reaching hand in the garden as in the other settings; `WOOD45`, which lifted its end onto the hedge above the fence, no longer applies. `LOST50` B ends the string by the hand, which two bench readers of three took for a balloon still held.
- **The goat's stake** (`STAKE50` B) is half as tall again, with the rope in two turns round its upper part and not in a ring at its foot.

Each changed template alone placed on 12 seeds of 12 with its rule on and off (`tools/cycle/yield_set.py`). Two more switches are at O, so the release draws v0.49's: `HOSE50` (B: the stopped hose full and thick from the reel to the paw, with no swelling) and `SLIDE50` (B, A and T: the slider behind the chute's near wall, sunk in it, and on top of the far rail).

A v0.49 record rebuilds with the v0.49 package, and a v0.50 record with v0.50's.

The cast draws every grown figure again (builder 0.50.0), behind switches read when it is built: `TPDB_AGE50` at MP, which is the marks of age (M) with the smaller heads (P), `TPDB_AGE50_HEAD` at 0.86 and `TPDB_BUST50` at 1.0; and `TPDB_STRING50` and `TPDB_ROLLER50` at B, the balloon's string and the painter's pole. These are the code's defaults, and the letter O gives v0.49's drawing. The children, the teenager and the animals are v0.49's. The renderer takes its scale from `TPDB_PPM` (400 px per metre).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.50 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.49. __CALIB_NOTE__

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
| `assets/cast/out050/` | The 18 `.blend` families (builder 0.50.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib050/` | Every variant the generated scenes and probes use, all rendered from `out050`: every person and every animal, nothing carried over |
| `assets/cast/gallery050/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.50.0, placement revision 47); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.50 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v050.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v050.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v050.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty-seven screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release; from v0.47 `tools/cycle/forced_cell.py` builds a cell from forced template sets and `tools/cycle/yield_set.py` counts how often a forced set places, with a rule's switch at each of its values; new in v0.48, the helper scripts that earlier releases kept in a scratch folder: `probe_angle.py`, `more_probes.py`, `iso_t4_wide.py`, `merge_iso.py`, `gate_yaw.py`, `strict_count.py` and `who_called.py`; and from v0.50 `tools/cycle/age_scenes.py`, which builds pictures of the last screen again with trial casts and counts what their figures are called |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out050                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out050 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
TPDB_TRIP48=O python vision/isolation_bench.py tpdb_work/bench tpwN_1 tpwN_2   # one template alone, cropped (here with revision 44's trip)
python vision/prepare_screen.py scenes,probes vision/v050   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v050 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery050 --old-gallery <v0.49 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.50 --single   # the release as one zip, tpdb_v0.50.zip
```

The release is one zip, `tpdb_v0.50.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.49 record rebuilds with the v0.49 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
