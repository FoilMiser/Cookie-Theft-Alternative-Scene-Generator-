# TPDB v0.39: the cast redrawn, the animals turned from profile, the heaps for summer, read a thirty-sixth time

v0.38 ended with all 64 templates through the gate. Its list began with the broom's and the rake's autumn leaves under green trees, seen in seven pictures, and went on to the dog beside a dropped ice cream and the ball's trail in a game of catch, which could be read from either end. Beside it, Sam's notes on the figures and the animals asked for one cast round: the lines where limbs cross, feet and ankles, the man in red's age, the waist and the belt, the quadrupeds' legs and paws and each animal's own build, and the animals turned from profile (Sam: "overly profile to the camera"). A second note asked for hanging the washing, the sleeping cat and planting flowers in five screened pictures each.

v0.39 does all of that as one cast round (builder 0.39.0), benched in three rounds, and one placement revision. The animals of eight templates are drawn at 45 or 135 as well as 90, an isomorph's at its partner's angle, the catch's ball stops short of the catcher's hands, and the heaps are drawn for summer. The probes were stratified by angle, every (template, angle) in two screened pictures, and the scorers tag an oddity about an animal with its angle. The set was regenerated and screened a thirty-sixth time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What was asked for | v0.39 |
|---|---|
| The broom's and the rake's autumn leaves under green trees, seven v0.38 pictures | The heaps drawn for summer, green and brown. No reader set the season against the trees, but five pictures from four readers found the green odd for fallen leaves, so it heads v0.40's list |
| The ball's trail in a game of catch could run from either end; "the ball sits right at the woman's hands" | The ball short of the catcher's hands. All three readers name the thrower: "so he appears to have just thrown the ball" |
| The man in red read as a boy or a young man in 5 of his 19 v0.38 pictures | A little taller and broader, a smaller head, sideburns and a moustache: a man in all 17 of his pictures, mostly "a man with brown hair and a moustache" |
| Feet: a back foot that "seems to point backward" | One flat shoe, toe forward, an ankle, the cuff over the shoe, planted feet level. Mei's flats were read as pads three times on the bench and never in the screen |
| The waist: shirt and trousers as separate pieces, a skirt or dress in parts | The dresses and the skirt in one piece with a hem, a hoodie or cardigan over the waistband, a seat and a filled hip. The tucked tee and a flat belt band read as "a hoop or rubber ring" on the bench and were left out |
| Lines where overlapping parts meet: shoes, belt, buckle, hands, paws | Drawn without the seam |
| The quadrupeds' stick legs and blob paws, each animal built from the same parts | Wider stances, jointed legs and paws, a dog's head with a stop, the cat lying and sleeping redrawn, the spotted dog's spots on its flanks, the goat rebuilt in v0.38's white. No remark on a dog's or cat's legs at any angle |
| Animals "overly profile to the camera" (Sam) | Revision 37: eight templates' animals at 45 or 135 as well as 90. Each (template, angle) read at 1.00 in two or more pictures. The dog walked on a lead stays at 90: at 45 its lead crossed its back at every spot tried |
| hang_laundry, cat_sleeping and plant_flowers in five pictures each | Each at 1.00 in five. Of the washing: "the drips and the full basket suggest he is hanging it up" |

Left as notes for the pilot: goats in a garden or park, figures drawn over the prop beside them, and wind that moves only the hat.

## The isolation bench

The cast round was benched in three rounds of single cut-outs, two to a reader and never two takes of one thing (`vision/isolation_v039.md`). Round 1, twenty-two readers of 44 cut-outs, read each thing in v0.38's cast with every animal in profile against the v0.39 cast with all its switches on and the animals at revision 37's angles. The heap for summer read as "green and brown leaves" where the autumn one was "autumn leaves", and grit read as dust, a rock or a dustpan. The man in red's beard took away the question of which way his shirt went. The single shoe made a foot's direction clear. Two things lost: the tucked tee with a flat belt band read as a ring or hoop at the waist in five cut-outs of eight, and the goat's brown coat on white legs as "a lumpy blob, sack or saddle blanket". Round 2 took the tuck and the band back and gave the goat brown legs: no ring at any waist, but the goat's white head now read as "a separate white ball or egg with horns". Round 3 read the redrawn goat in v0.38's white and all brown. White was the only coat named "a goat" by every reader with nothing taken for a cover or a separate head. Before any reader, the bench's own look caught the hoodie's hem clamp cutting every long sleeve at the hem's height in the rest pose, and the clamp now spares the arms.

__DESIGN_TESTS__

## Placement revision 37

Every record stores the placement revision it was made with. v0.39 pictures use revision 37, which adds to those of revisions 1 to 36 the animals of eight templates drawn at an angle drawn by the seed from `templates.ANIMAL_YAWS` (the dog walked, begging, playing and leaving paint tracks, the dog at the dropped ice cream, the goat grazing, the cat stalking a bird and the animal on the hose, at 45, and at 135 where no direction is needed, beside 90), with the dog walked on a lead drawn at 90 when it draws 45 (`templates.UNPLACED`); an isomorph's animals at its partner's angle; a forced set's angles kept in the record; the catch's ball drawn short of the catcher's hands; and the broom's heap and the raked pile drawn for summer. All are behind the revision, so v0.38's records rebuild with the v0.38 package. The cast is redrawn (builder 0.39.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.39 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.38. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, and v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out039/` | The 18 `.blend` families (builder 0.39.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib039/` | Every variant the generated scenes and probes use, rendered from `out039` (the birds and duck carried over from `lib038`) |
| `assets/cast/gallery039/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.39.0, placement revision 37); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.39 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v039.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v039.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v039.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-six screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out039                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out039 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v039   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v039 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery039 --old-gallery <v0.38 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.39 --single   # the release as one zip, tpdb_v0.39.zip
```

The release is one zip, `tpdb_v0.39.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.38 record rebuilds with the v0.38 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
