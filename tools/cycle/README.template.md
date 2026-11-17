# TPDB v0.56: a list of fifty rows worked on three blind benches; the bicycle with square wheels is held and passes; 63 of 64 templates through the gate, read a fifty-third time

v0.55 ended with 63 of its 64 templates through the gate. After it Sam asked for a quality check, and seven fresh reviewers, three screens read side by side and the records' geometry filled the work list out to fifty rows (`vision/flaws_v055.md`, its second part). Sam's brief for v0.56: "I will compact, go for v0.56, work the whole list".

The list has five rows at the gate or its edge, eleven inferences and contradictions that are read two ways, twelve rows of the cast, ten of placement, eight of grey and four of the keys. Every new drawing was put behind a switch whose other value is v0.55's drawing, and was read blind before it went into scenes; what the readers did not take is not in the release.
- **The cast (builder 0.56.0)** has twelve poses drawn again and three new ones. Drawn again: hanging the washing (the hands apart, a peg in one), the child with the dropped cone (looking at it, a hand at the cheek), the child on the swing (a fist on each rope), the pan (shallow, with a long handle), the feeder's paper bag (held by its neck), kneeling to plant (both knees down, a seedling in the hand), the hose's nozzle (twice the size), the heavy seesaw's two riders and the sleeping dog (curled, chin on its paws). New: a figure that holds a bicycle, one that throws bread, and a bird that pulls.
- **Placement revision 50 (generator 0.56.0)** draws the pond's shore and keeps the figures of other events clear of the pond, keeps every figure's ground line off the picture's bottom edge, lowers the street's sun, gives a walker a deeper lane, keeps a jumper out of a picture with anything else in the air, puts the pram on the path and the picnic's sitter on a larger blanket, turns the photographer to the side and gives the camera a subject, and stands the ladder that leans on nothing against open sky.
- **The scene's drawings:** the bicycle with square wheels is held by its owner; the wheelbarrow's square wheel is the round wheel's size and open on its spokes; the stopped hose has a large nozzle with one drop at its mouth and a seep at the reel; the seesaw's ends rest on stops; the thief bird is half as large again and pulls a slice of bread away; the paint is pink; the sprinkler's box is a taped parcel on the path; the kite lies on a limb; and the pond, the sprinkler's water, the dropped ice cream, the kite, the loose balloon, the barrow's tub and the baskets have colours that stand off in grey.
- **Read and not taken:** the seated skirt as one sheet, lowered eyes, a steeper pointing arm, a crouching cat, a handle on the bucket, a shorter stride, a level paint roller, a long lead for the dog at the door, the bird turned from the cat, the rising water as streaks, a trail only behind the thrown ball, the bicycle leaning on a post and the hose pressed flat.
- **Three benches judged it:** 46 reviews of pairs for the cast's drawings, 268 readings of whole pictures in up to four arms, and 50 more in a second round for what the first left open.

The set was regenerated and screened a fifty-third time. **Every picture is new:** the cast and the rules move every figure, so this screen compares with v0.55's by template and not by picture, and the planner's priors, three of which v0.55 had left, were all taken from the new calibration.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What v0.55 drew, and what its check found | v0.56 |
|---|---|
| The bicycle with square wheels stood on its stand with nobody near it. It was under the gate in v0.52, v0.54 and v0.55: in the busiest picture its wheels were not looked at, and it lay on its side to two readers | **Its owner holds it.** On the bench six readers of six named the wheels as the wrong thing, for four of ten on its stand; leaning on a post, the list's other proposal, none of eight did. In the screen `square_wheel` reads **1.00 in ten pictures**: "At the far left an older man in a flat cap and brown waistcoat stands holding a teal bicycle whose wheels are square, which is impossible." |
| The wheelbarrow's square wheel was a large dark frame beside the tub, a firm sighting in 3 readings of 12 | The round wheel's size and place, open on its spokes: five bench readers of six. The same square drawn solid, as the list proposed, was a block: "A red wheelbarrow stands near the fence, with a black box-shaped thing at its front." In full in all five of the screen's wheelbarrows |
| The stopped hose: another reading beside the dog in 15 readings of 15, a nozzle too small to see, nothing to say the tap is on | A nozzle twice the size, a drop at its mouth, water seeping at the reel, and the swelling kept. The dog was the one cause to eight bench readers of ten, for none of four; pressed flat with no swelling, to one of eight; without the seep, to three of eight. `blocked_hose` reads **1.00** for 0.975 |
| The thief bird, small beside its sandwich, 0.967 | Half as large again, pulling the top slice away. **No likelier to be read as stealing:** with nothing beside it in 12 bench readings of 24, for 12 of 31 of v0.55's bird. It is no longer small. `bird_steals` reads 1.00, with five full marks that rest on a judgement call |
| The ladder that leans on nothing ended at the hedge's line: a support behind it in 9 readings of 9 | Longer, its top third against open sky, in a park with no lamp post: "In the middle of the grass, a tall wooden ladder stands upright on its own, leaning against nothing, which is impossible." `ladder_nothing` reads 1.00 in five pictures and no scorer lists a call |
| Figures over the pond's near edge, 23 readings in 13 pictures | The pond has a shore, and figures of other events keep clear of it: a doubt in 5 bench readings of 13 as it was, 4 of 28 with the shore, none of 10 with the rule. In the screen three pictures are left, each the pond's own figure: "- The man stands on the pond's rim, and his lower body overlaps the water's edge. He could be standing just in front of the pond or partly in it." |
| Nobody knew what the photographer photographs, 9 readings of 9 | A subject near and alone on that side did nothing while the figure stood at three-quarters: "The photographer's camera points out of the picture rather than at any particular person, so it is unclear what she is photographing." From the side all six readers named the subject first. `photo` reads 1.00 in five pictures with no oddity logged |
| The heavy seesaw's man sat on the grass at the plank's end to two readers of three | The plank's ends rest on stops and the child stretches an arm down to him. One bench reader of fourteen doubted his seat; **three screen readers of five do**, and two give no weight as why the child is stuck: "- The old man appears to be sitting on the seesaw end but his feet are on the ground and his body is quite far forward of the seat; he could be read as sitting on the plank or just leaning/perched on it." `seesaw_heavy` 0.933. Not mended |
| The pan was a pot or a saucepan in 6 readings of 9, still the wrong thing to water with | Shallow, with a long handle, a frying pan to eight bench readers of eight. **In the screen it is a watering can first to two readers of five:** "- The boy's watering can looks odd: it is held by a long thin handle out in front like a frying pan or ladle, and the water seems to come from its far side. It could be read as a pan or a scoop rather than a watering can." `pan_watering` 0.900, on the gate's line. Worse than it was |
| The game of catch, 1.00 in five pictures | **Not changed, and under the gate: 0.833 in three pictures.** In two gardens the ball stands at the fence's top above the catcher: "- The ball's direction: it is going up and to the right, well above the girl's hands. Could be read as a throw to the girl that is going too high (over her head / over the fence), or as a throw at the cat on the fence." It is first on the next list |
| The dog at the door with a short strap in its mouth | Not taken: a lead of real length, trailing on the step, was "a yellow garden hose" to eight bench readers of ten |
| The legibility gate, 63 of 64 in v0.55 | **63 of 64.** `square_wheel` passes; `play_catch` fails. Sixty templates read 1.00 |
| The set, 0.972 over all items in v0.55 | **0.975**, on 21 new pictures. Eight of the set's 277 items are under full marks: the clouds in six pictures, a half mark on the man who sits on nothing and a half mark on the girl who catches the ball |

Left as a note for the pilot, as in v0.53 to v0.55: the setting's clouds and trees are left out by some readers and named by others. A person tested will leave them out too, and the scoring rule should say whether they count.

## The benches

Every reviewer and reader was a fresh subagent given its prompt and its pictures and nothing else. The record is `vision/isolation_v056.md`.
- **Pairs, for the cast's drawings.** A sheet shows the same figures drawn two ways, v0.55's and the trial's, large and at a picture's size, with nothing said of which row is which; every set is made twice, one row above and then the other, so that a row's place cancels. Fifteen sets in round 1, seven mended in round 2, one in round 3: 46 reviews. Chosen in both orders: the washing, the cone, the swing, the pan, the sleeping dog, and the feeder's bag once it was one bag and not a sack on a box. Lost in both orders, twice: a level paint roller ("in b the flat roller in its frame could be a tray, a rolling pin or a cart handle"), a crouching cat ("row b turns the body into a long low lump with no readable legs") and a steeper pointing arm ("the vertical arm in b looks more like raising a hand to ask a question"). The seated skirt as one sheet lost its second round in both orders, and nobody had called v0.55's skirt shorts.
- **Whole pictures, round 1.** Sixty of v0.55's pictures were built again on their own records' plans with only the drawings changed, and read as they were (one reader), with the new drawings (two) and with an alternative where there was one (two); the tier-4 playground, where the bicycle failed, was read by eight readers as it was and eight with the bicycle leaning on a post and nothing else changed; and nineteen new pictures were built under revision 50 (two readers each). 268 readings by 34 readers, no reader with a picture twice. Six analysts who never saw a picture counted each row from the readers' own lines.
- **What the list's own proposals did.** About half lost. A lead of real length is a garden hose. The rising water as streaks and drops is a spray: "The water from the watering can arcs in a loop shape back over the flowers with drops rising above them — slightly odd water path, but readable as watering." A trail only behind the ball loses the thrower, in 6 readings of 8 for 1 of 4. A hose with no swelling loses the block. And leaning on a post the bicycle read worse than on its stand: "The bicycle and the wooden post overlap so the post seems to go through the middle of the bike frame; it could be read as the bike being locked/leaning against the post, or as the post passing through the bike."
- **Round 2.** Twelve readers, 50 readings. The thief bird in three scenes, each built three ways and read by four readers: seven of twelve for the bird that pulls, four of twelve for the larger bird that pecks and four of twelve for v0.55's, so round 1's four of four for the pecking bird did not hold. The hose without its seep: three of eight for six of eight with it, and the tap came back ("the woman may simply not have turned it on yet"). And the photographer from the side.
- **A bench is not a screen.** The pan that eight bench readers of eight called a frying pan is a watering can to two screen readers of five, and the seesaw's man is doubted more in the screen than on the bench. Both are on the next list.

__DESIGN_TESTS__

## Placement revision 50

Every record stores the placement revision it was made with. v0.56 pictures use revision 50, the placement rows of v0.55's list and the scene's new drawings, each behind a switch of its own (`scene.sw56(NAME)`, where `O` is v0.55's; the header comment of `scenegen/scene.py` has each rule with what the readers wrote and what it costs):
- the pond's shore, and a figure of another event with at most 0.30 of its height above the pond's near edge (`BANK`, `PONDFIG`);
- no figure's ground line lower than 970 (`EDGE`), and the street's sun 32 units lower (`SUN`);
- a walker's lane 70 units deep behind its line and 30 in front, with no filler in it; a duck 120 units from an angler's float; a child jumping for joy never in a picture with a held or a lost balloon, a hat the wind took or a floating box, and 150 units clear of the swing and the washing (`LANE`, `FLOAT`, `REACH`);
- the sprinkler's hose across no flower bed and no animal on a hose that runs (`HOSEBED`, `HOSERUN`); the pram's wheels on the path (`PRAM`); the picnic's blanket half as large again with the sitter and the basket in its middle (`PICNIC`);
- the photographer drawn from the side, the subject 200 to 430 units away at the same depth and alone on that side (`PHOTO`);
- the ladder 520 long with its top third against open sky, in a park with no lamp post (`LADDER`); the storm pointer's line clear of the bird table (`RAINLINE`); the hand that reaches for the hat clear of the gate (`HATHAND`); no raised hand within 250 units of the floating box (`BOXHAND`);
- nobody's feet near the thief bird's bench, and no thief bird in a garden whose hose reel another template uses (`STEALAT`); the parcel on the path, never with the garden's swing (`PARCEL`).

What the rules cost, in seeds placed of twelve with the rule on and off: a pram alone in the park 7 and 12; a photographer with two events 7 and 10 in the park, 8 and 11 in the playground and 9 and 10 in the street; the jumper with the washing 8 and 9; every other rule the same count on and off. On v0.55's four tier-4 sets, six seeds each: park 4 and 4, street 5 and 5, playground 3 and 3, garden 5 and 4.

**A record says whether it reads in grey.** The build measures every scored thing of 600 square units or more against a ring of the finished picture round it and records whether 35 % of its fill is 20 grey levels or more away (`compose.grey_check`). It fails no picture yet: 121 of the 126 screened records pass, and five are flagged (`vision/flaws_v056.md`, G1).

The cast is v0.55's with twelve poses drawn again and three added (builder 0.56.0; each drawing behind a switch `TPDB_<NAME>56` in `castlib`, where `O` builds v0.55's). v0.55's whole library of 345 variants was rendered again from the new cast and compared: every variant of a pose that was not drawn again came out alike, thirteen of them but for a single pixel. The release's library is the new renders.

A v0.55 record rebuilds with the v0.55 package, and a v0.56 record with v0.56's.

__INSPECTION__

The planner's difficulty priors are taken from the calibration measured under revision 50 with the new cast (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.55. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (79 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads, v0.44 sits the reading dog up in reading glasses, redraws the cats' ears, the goat's beard and the dogs' noses, gives props colours of their own and redraws the run, the sand spade, the nozzle's inspection, the call from the seesaw and the content face, v0.45 enlarges the ice cream, redraws the camera, the shoes' soles, the trowel, the paint roller, the carried box and the kite's reel, turns the hose inspector's head to the viewer and hides the swimming duck's legs, v0.46 draws the whole cast again: a heavier outer line and two flat tones, no added neck under the three smaller heads, higher necklines, fuller sleeves, no wrist seam, the vest's bands on the vest, a plain wire for the glasses, a smoother moustache and a line mouth on a dark line of its own, and v0.47 draws the cast's anatomy again: sloped shoulders, tapered arms and legs with their joints, a thumb, a wedge shoe on a sole, a skirt that turns with the thighs, a nose with no line round it, a three-quarter side view, glasses as flat rings, the cardigan's V and buttons, a wider moustache in two halves, the animals' eyes, markings, tails and paws, and the weak actions (the walk, the run, the sit on the ground, the reading dog's pose of its own, the dog on the hose, the peck and the stalk), and v0.48 draws the heads, faces and hair again (an egg head with a jaw and a chin, a smaller and lower face with a plain line for a mouth, hair cut along a curve with a parting, a face of its own for a side view, one flat tone, a tee to the hips, feet turned out) and every animal's body and limbs (the dogs' and cats' bodies, joints, skulls and tails, the cats' eyes, the goat's barrel, legs and face), and v0.49 draws every person's head again (a jaw down to a corner and a rounded chin wider than the neck, a shape for each kind of person in `core.HEAD49_SHAPES`, the neck a part of its own), with a wider moustache and the ice cream at the mouth; v0.55 draws the lower body of a seated figure in stiff pieces; and v0.56 draws twelve poses again and adds `hold_bike`, `throw_bread` and the songbirds' `tug`, each behind a switch `TPDB_<NAME>56` |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out056/` | The 18 `.blend` families (builder 0.56.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib056/` | Every variant the generated scenes and probes use, all rendered from `out056` |
| `assets/cast/gallery056/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.56.0, placement revision 50; v0.56's switches are `scene.sw56` and `SW56_DEFAULT`); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.56 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v056.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v056.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v056.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all fifty-three screens, the review of v0.55's pictures that v0.56's list comes from (`review_v055/`), `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release; from v0.47 `tools/cycle/forced_cell.py` builds a cell from forced template sets and `tools/cycle/yield_set.py` counts how often a forced set places, with a rule's switch at each of its values; new in v0.48, the helper scripts that earlier releases kept in a scratch folder: `probe_angle.py`, `more_probes.py`, `iso_t4_wide.py`, `merge_iso.py`, `gate_yaw.py`, `strict_count.py` and `who_called.py`; and from v0.50 `tools/cycle/age_scenes.py`, which builds pictures of the last screen again with trial casts and counts what their figures are called; and from v0.51 `tools/cycle/extra_probes.py`, which forces probes for a carrier that the counts by template do not see; and from v0.52 `tools/cycle/fig_pairs.py`, which makes the sheets and prompts of a blind bench of two drawings of the same figures, and `tools/cycle/who_build.py`, which builds the last screen's pictures again with a trial cast; and from v0.53 `tools/cycle/bench_build.py`, `bench_prepare.py` and `bench_tally.py`, a bench in whole scenes that asks two questions of one set of readers, `tools/cycle/calib_cmp.py`, which counts what moved between two calibrations, and `tools/cycle/crops.py`, which cuts named elements out of built pictures onto a sheet; and from v0.54 `tools/cycle/pixcmp.py`, which says which pictures of a folder are another folder's to the pixel, `tools/cycle/who_pose.py`, which counts what a screen's readers called a figure by its pose, and `tools/cycle/retest.py` (v0.53's), which compares the scores of the pictures that came back with the last screen's; and from v0.55 `tools/cycle/sit_screen.py`, which prints what two screens' readers doubted about the seated figures of the same pictures ; and from v0.56 `tools/cycle/bench_round2.py` and `bench_tally2.py`, a bench's second round and its readers' lines (`tools/cycle/fig_pairs.py`, `fig_pairs_tally.py` and the three `bench_*.py` are v0.56's own: four arms of whole pictures, dealt row by row) |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out056                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out056 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
TPDB_TRIP48=O python vision/isolation_bench.py tpdb_work/bench tpwN_1 tpwN_2   # one template alone, cropped (here with revision 44's trip)
python vision/prepare_screen.py scenes,probes vision/v056   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v056 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery056 --old-gallery <v0.55 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.56 --single   # the release as one zip, tpdb_v0.56.zip
```

The release is one zip, `tpdb_v0.56.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.55 record rebuilds with the v0.55 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
