# TPDB v0.46: the cast drawn again in the settings' own line and two flat tones, with shorter necks, read a forty-third time

v0.45 ended with all 64 templates through the gate. Sam's brief for v0.46 was the drawing itself: "make moves to improve the art style for v.046 and clean up issues like the woman in the yellow dress having a neck that is too long". The work list came from three places:
- Sam's remark on the neck;
- an item of v0.45's set review (`tpdb_work/review45/review_set.md`, item 26), "Two outline systems in one picture": "people and animals have soft shading and thin outlines in a darker shade of their own colour; props and set have bold black outlines and flat fills". It asked for "a dark outline of constant width on the cast";
- a look at v0.45's cast at full size, figure by figure, which found a seam line at every wrist, the safety vest's bands standing off the chest, sleeves that stood off the arm like shoulder pads and a moustache with a notched edge.

All of the work is in the cast (builder 0.46.0). The bench read it in whole pictures and then in enlarged figure cut-outs, v0.45's drawing beside v0.46's, in five rounds, and took these:
- **The line:** a figure's outer edge is 9.5 px wide at render size, about 4.5 px in a picture, which is the settings' own line, and the lines inside it are 5.5 px (v0.45 had one 5 px line, about half the weight of the settings'). The line takes no light, so it is the palette's outline colour; lit, it had come out darker than its ink in every earlier release.
- **The shading:** two flat tones, the colour and a shadow at 0.86 of it, with no pool of light (v0.45 had three soft tones against the settings' flat fills).
- **The necks** of the three figures with a scaled-down head (the woman in the yellow dress, the woman in purple and the man in the red shirt): the chin sits where a full-size head's does, no neck is added and the neck keeps its full width. Every grown figure's neckline is 1.4 cm higher and its neck a little fuller. On the model the neck that shows on the woman in the yellow dress went from 8.2 cm to 3.9 cm.
- **The figure:** her waist is wider (0.94 of the standard figure's for 0.86); a tee's sleeve ends nearer the arm's width, the shoulder is lower and smaller, and the resting arm hangs nearer the body.
- **Clean-ups:** no seam line at the wrist; the safety vest's two bands lie on the vest all the way round; the glasses are a plain dark wire, a fifth thicker; the moustache is a smooth curve rounded at its ends.
- **The mouth** drawn as a line: the lip-coloured line at v0.45's width, riding on a wider dark line of its own. It took three drawings: the first closed to a dark mark under the heavier line, and the second, a plain red line, was read by one bench reviewer as "a cut or blood".
- **Placement revision 43 is unchanged.** No scene rule was changed.
- **Looked at and left before the readers:** one line weight for the edge and the inner lines alike; the new line over v0.45's soft tones; flat colour with no shadow tone at all; a higher neckline still; glasses half as thick again.
- **Not worked:** the scene items of v0.45's list (the thief bird, the square wheels, the stalked bird and the oddities), carried to `vision/flaws_v046.md`.

The set was regenerated and screened a forty-third time. Every person and every animal is drawn anew, so no picture is identical to v0.45's.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What Sam, v0.45's reviewers or the bench saw | v0.46 |
|---|---|
| "Two outline systems in one picture": the figures in thin lines and soft shading, the settings in bold lines and flat fills | An outer edge as heavy as the settings' line, and two flat tones. In enlarged cut-outs beside v0.45's it was the better drawn in six pairs of eight and the nearer to the background's drawing in seven: "match the scene and read more clearly". In whole pictures the pair reviewers did not see it: "No difference" in sixteen pairs of sixteen |
| The neck of the woman in the yellow dress, too long (Sam) | 8.2 cm to 3.9 cm on the model. Seated on the bench: "neck about right; head size suits the body". With the ice cream, her head tipped back, a reviewer still wrote "neck too long and too thin, same as a", where a is v0.45's. No reader of the 98 screened pictures named a neck, and she is a woman in 29 descriptions of 30 |
| A seam line at the wrist, v0.45's "stray ring at the raised wrist" | Gone |
| The vest's bands, which in v0.45's drawing "look torn and spill past the outline" | They "are clean and stay inside the vest"; an "orange hi-vis vest with reflective stripes" in whole pictures |
| The glasses, in profile the far lens a black disc past the face | A plain dark wire. No gain shown: in both drawings they "look as if they are floating off the face" |
| The moustache's notched edge, "a dark brown blob around his mouth that reads more like a smudge than a moustache or mouth" | **Worse in the screen.** Smoothed and rounded at its ends, it "could also be a smear of something (for example chocolate) on his face" and "looks a little like a smudge"; four of its wearer's eleven descriptions name a moustache. First of the oddities for v0.47 |
| A line mouth under the heavier line | Drawn three times; the release's is v0.45's mouth made as geometry. No reader wrote of blood, a cut or a wound at a mouth. On a face in profile it is still "a red blob stuck on the cheek rather than a mouth", as v0.45's was |
| v0.45's soft tones, "shiny" and "plastic" in the cut-outs | Two flat tones. The shadow's hard edge was read once as a fault, "her arm drawn faintly through her body", and on the bench as "a fold or stain" on a lap. On the v0.47 list |
| The legibility gate, 64 of 64 in v0.45 | **60 of 64.** `dog_reading`, `about_to_trip` and `sweep_fork` each fell on one misread, and `blocked_hose` on one reader's hedges. No placement rule had changed, and nothing was mended, swapped or read again after the screen |
| v0.45's list: `bird_steals` 0.933, `square_wheel` 0.933, `cat_stalks_bird` 0.958 | Not worked: 0.972, 1.00 and 1.00 |

Left as notes for the pilot: the goat in a park "a little unusual", "a bottle that looks like wine sits beside a child at the picnic", and "the two women look identical (same face and hair), only their clothes differ".

## The isolation bench

The bench is eight tier-3 pictures, two each of the street, the park, the playground and the garden, with events forced among the planner's own so that all ten people of the cast and both dogs stand in at least one. Each was built on revision 43's rules in v0.45's cast and in v0.46's on the same seed, so only the cast differs (`vision/isolation_v046.md`). Three forced sets were swapped before any reading for ones the planner could place. There were five rounds and 41 fresh readers and reviewers:
- **Rounds 1 and 2, whole pictures.** Sixteen readers read every scene and every forced event as built, in both casts. Eight pair reviewers had the two pictures of a scene side by side, which is which drawn at random, and were asked how the people and animals are drawn and whether they belong to the drawing round them. On belonging they said "No difference" in sixteen pairs of sixteen: "I could not tell the two drawing styles apart at this size, so the choice should rest on other grounds". What they named, they named in both casts: thin necks, and the kneeling man's moustache, "a dark brown smudge at his mouth or chin that reads as a moustache or as dirt". One thing went against the new cast, the glasses ("her glasses are thin, light lines on a small face"), and the wire was thickened. A bench of whole pictures could not judge this release's changes, so round 3 enlarged the figures.
- **Round 3, twelve figures cut out of the bench pictures and enlarged to 640 px**, v0.45's beside the new, the order drawn at random. The new drawing was the better in eight pairs, v0.45's in two, with no difference in two; its outline and colours were the nearer to the background's in eight, with no difference in four. "Its bold outlines and flat colours match the scene, so the figure sits in it more naturally." "The vest stripes are clean and sit within the body, while in a they look scratchy and stick out like loose straps." The two pairs that went to v0.45 named two faults of the new drawing. Under the heavier line the mouth's own outline closed over its colour, "only a small dark mark"; and the shadow tone, one hard-edged band at 0.72 of the colour, was "a darker, dull yellow band that looks like a stain or a shadow pasted on". The mouth became a plain line with no outline, and the shadow was lightened to 0.86.
- **The line's colour.** The validator, run on the release's renders before round 4, put 374 of the library's 386 records under its palette share. Line Art's strokes were lit like any surface and came out at (28, 28, 34), where the palette's outline colour, which the settings are drawn in, is (38, 38, 46). It had been so in every release since Line Art came in, and a thin line hid it. The line now takes no light.
- **Round 4, the release's cast, sixteen pairs.** Beside round 3's drawing it was the better in three pairs of twelve, on the mouth alone, with no difference in nine: no reviewer saw the lighter shadow or the line's colour. Beside v0.45's, in four pairs, it was the nearer to the background's drawing in all four and the better drawn in two, v0.45's in two. And one reviewer wrote of the plain mouth: "a red smudge on the cheek beside the nose, too large and off to the side, which can read as a cut or blood rather than a mouth." A mouth that one reader in a handful can take for blood cannot go into a picture for patients, so it was drawn again: v0.45's coloured line, riding on a wider dark line sunk into the face.
- **Round 5, fourteen pairs.** Between the two mouths, in six pairs, one went to each and four were no difference; on the figure where the plain mouth had been a cut it was again "a red smear or wound on the cheek", and the new one "a smaller red mark that reads as a mouth". Beside v0.45's, in eight pairs, the release's drawing was the better in six, v0.45's in one, with no difference in one; it was the nearer to the background's drawing in seven, with no difference in one. Its "flat fills and firmer outlines match the scene and read more clearly", where v0.45's shading "looks like it belongs to a different picture". The one pair to v0.45 was given for the form its shading shows: "the shading gives the top, legs and shoes some shape".
- **The neck Sam named.** Seated on the bench, the release's is "neck about right; head size suits the body", where v0.45's is "neck about right, perhaps slightly long". Standing with the ice cream, her head tipped back, the reviewer with v0.45's beside it wrote "neck too long and too thin, same as a" of the release's, a being v0.45's, and another wrote "a little too thick (about as wide as the lower face) and slightly long". It was not shortened again: reviewers asked about the neck in that pose called it a little long in both drawings, and round 3's reviewer had called the seated one "a little short". The pose is on the watch list.
- **What the bench left open.** The mouth of a face in profile lies at the edge of the outline and is "a red blob stuck on the cheek rather than a mouth" in both mouths. Under the moustache the release's mouth is darker than the plain one was: "You cannot make out a mouth." Hands have no fingers and legs no knees, in both casts. And a crop changed a thing: both reviewers of the woman walking her dog read the lead, which the crop cut off from the dog, as "a thin red stick (a cane)".

The release's cast as it stands was read on the bench in cut-outs only; whole pictures in it were the design tests' and the screen's to read. Some readers and reviewers listed their round's folder when their files were written and so saw the names of the other files in it; none opened one, and from round 4 the maps lay outside the folders (`vision/isolation_v046.md`, The blind rule).

__DESIGN_TESTS__

## Placement revision 43

Every record stores the placement revision it was made with. v0.46 pictures use revision 43, as v0.45's did: no placement rule changed in this release. The revision's rules, new in v0.45:
- **The lost balloon:** its string's end 62 to 80 px above the reaching hand at full size (`templates.BAL45`), the string a slow wave that grows toward its free end, with no curl (`CURL45`). On a playground the end lies nowhere on the railing (`RAIL45`). In the garden it lies above the wooden fence's pickets, 34 to 48 px at full size, and a child whose hand would be more than 200 px below it is not stood there (`WOOD45`).
- **The fence painter:** the wet paint on the board under the roller begins below the roller, so the roller lies on bare wood at the paint's edge; the painter stands a step further forward until the roller lies well below the boards' tops, the tin with them (`templates.PAINT45`).
- **The planter:** kneels at the bed's end and digs in the bed, a hole under the trowel's point, a few clods beyond it, the pot in front of the bed (`templates.PLANT45`).
- **The picnic:** a loaf and a bottle stand out of the basket, and where the blanket has room a plate with a slice of watermelon lies on it (`templates.PICNIC45`).
- **The goat:** its stake never drawn in front of a standing structure (`templates.TETHER45`).
- **A swimming animal:** cut along a waterline with a ripple round it, with no ground shadow (`library.SWIM45`).
- **The slide's ladder:** the frame's own end, in the frame's red: two rails to the ground with slate rungs between them, the near rail running on up into the hand rail over the deck (`settings.SLIDE45`).
- **The bird table:** its post stands in a tuft of grass (`settings.FOOT45`).
- **The reading dog:** its paper drawn 12 px toward the dog and 6 px higher, at the dog's scale, so the forelegs cross the near page and the paws lie on it (`templates.READ45`).

Each switch is "B"; any other value gives the rule's v0.44 form. The rules are v0.45's and the renders are not: a v0.45 record rebuilds with the v0.45 package, and a v0.46 record with v0.46's.

The cast draws every person and every animal again (builder 0.46.0), behind eleven switches read when it is built: `TPDB_STYLE46`, `TPDB_NECK46`, `TPDB_ARM46`, `TPDB_MEI46`, `TPDB_CLEAN46`, `TPDB_COLLAR46`, `TPDB_GLASSW46`, `TPDB_SHADE46` and `TPDB_INK46` at B, `TPDB_MOUSTACHE46` at C and `TPDB_MOUTH46` at D, which are the code's defaults. The letter O gives the drawing before the switch.

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.46 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.45. __CALIB_NOTE__

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
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg, and from v0.32 `~body` and `~legs` at both legs, for the bench; from v0.46 a family's config can ask for a wider line round the figure's outer edge (`silhouette_px`), a line that takes no light (`unlit`) and cel tones of its own (`cel`)) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant; from v0.32 a piece of a split figure is checked by its base pose, and the manifest schema takes the `~` suffix; from v0.46 a record that carries its own cel tones is measured against those tones, and the schema takes the line's and the tones' new fields |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads, v0.44 sits the reading dog up in reading glasses, redraws the cats' ears, the goat's beard and the dogs' noses, gives props colours of their own and redraws the run, the sand spade, the nozzle's inspection, the call from the seesaw and the content face, v0.45 enlarges the ice cream, redraws the camera, the shoes' soles, the trowel, the paint roller, the carried box and the kite's reel, turns the hose inspector's head to the viewer and hides the swimming duck's legs, and v0.46 draws the whole cast again: a heavier outer line and two flat tones, no added neck under the three smaller heads, higher necklines, fuller sleeves, no wrist seam, the vest's bands on the vest, a plain wire for the glasses, a smoother moustache and a line mouth on a dark line of its own |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out046/` | The 18 `.blend` families (builder 0.46.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib046/` | Every variant the generated scenes and probes use, all rendered from `out046`: every person and every animal, nothing carried over |
| `assets/cast/gallery046/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.46.0, placement revision 43); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.46 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v046.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v046.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v046.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty-three screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out046                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out046 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v046   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v046 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery046 --old-gallery <v0.45 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.46 --single   # the release as one zip, tpdb_v0.46.zip
```

The release is one zip, `tpdb_v0.46.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.45 record rebuilds with the v0.45 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
