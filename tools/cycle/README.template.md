# TPDB v0.42: the goat, the dogs, the trousers, the shoes and the woman in yellow redrawn, the goat tethered, the birds turned, read a thirty-ninth time

v0.41 ended with all 64 templates through the gate, and read strictly with two under it: `blocked_hose`, its cause given with "it could also simply be turned off", and `rain_coming`. The list went on to a second ice cream near the begging dog, the dog's body in profile, "upright", "kneeling", "human-like", the woman in yellow called "girl", and the goat out of place. Sam's notes on the figures (`tpdb_work/figure-fixes-v041.md`) ranked nine more things by what they cost a reader. First the goat, a sphere head on a hunched body. Then the belt, a ring at the waist, and the trousers' V across the front, a "briefs" look. Then the dog's chest patch, "like a bib or nappy", the begging and reading dogs' human poses, front-view shoes and bare legs, the cat, the woman in yellow, and the birds always in profile.

v0.42 benched those in two rounds and took most of them (builder 0.42.0):
- **The goat:** a wedge head on a neck, the back a fifth longer and level on shorter legs, split hooves, a pointed beard and a red collar; tethered to a peg when it grazes.
- **The dogs:** the tan dog's patch a narrow blaze down the chest, the far legs a step darker, a brown patch on the spotted dog's near foreleg, and a longer muzzle with a level top. The begging dog sits on its haunches with a shorter trunk, and the reading dog's hind legs fold beside it.
- **The people:** no hip node in the trousers, so no V; no belt under an untucked tee; shoes with a longer toe and a sole; bare legs with a calf. The woman in yellow has a low bun.
- **The birds:** the songbirds and the duck at 45 as well as 90.
- **Placement revision 40:** the goat's tether and the birds' angle; no one else with an ice cream near the begging dog; after the screen, the square-wheeled bicycle off the stall and the bench.
- **Read and left as they were:** the cat (its legs tangled either way) and a crimp in the stopped hose. The knees were priced and not changed.

The set was regenerated and screened a thirty-ninth time. Every person, dog and goat is drawn anew, so no picture is identical to v0.41's.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.41 readers, or Sam's notes, saw | v0.42 |
|---|---|
| The goat out of place in seven pictures, once "a sheep"; its sphere head, an ear like an eye socket, a hunched body | Redrawn and tethered. Tied to a stake in six descriptions, out of place twice, both softened ("a little unusual, but it is tethered and calm"); no sheep |
| The begging dog at 90 "upright", "kneeling", "human-like" | On its haunches with a shorter trunk: kneeling or a person in none of its five pictures (three of three of v0.41's on the bench) |
| A second ice cream near the begging dog: "I can't tell who the dog is begging from" | Nobody else with an ice cream near it (revision 40); in both pictures with another eater in view, the reader gave the one on the bench |
| The belt a ring at the waist, and a V across the trousers, a "briefs" look (Sam's notes) | No belt under a tee, no hip node: no description mentions a belt, briefs or a waistband (v0.41's mentioned a belt in six) |
| The dog's chest "like a bib or nappy"; white legs like stilts | A narrow blaze, darker far legs: no bib or stilts in 30 pictures with a dog |
| The reading dog's hind legs stretched out "like a person sitting" | Folded, the trunk shorter: no reader called it a person. But its paper "stands upright on its own" three times (once in v0.41) |
| Birds and the duck only in profile | At 45 too: every (template, angle) pair of the four bird templates reads 1.00 |
| The woman in yellow called "girl" | A low bun, read as "a ponytail": "girl" in 6 of her 14 pictures, five hedged (8 of 24 in v0.41). Not fixed |

Left as notes for the pilot: the cat's legs at 45, the stopped hose's swelling, and figures drawn over the prop beside them.

## The isolation bench

The two lists were benched in two rounds of single cut-outs (`vision/isolation_v042.md`). Round 1, twenty-five readers of 50 cut-outs, two to a reader and never two takes of one thing, read each thing in v0.41's cast and scene against the cast with every switch on:
- **The goat:** tethered in all three cut-outs, and the disc head gone; the hunch at 45 and 135 stayed.
- **The begging dog:** kneeling or a person in three of v0.41's three cut-outs, in none of the new three.
- **The trousers, belt and shoes:** nothing said of them; v0.41's belt once "a belt, or ... the gap".
- **The woman in yellow:** a woman in all six whole pictures on both sides.
- **The cat:** tangled on both sides, and the smaller head drew "a rat or weasel".
- **The crimp at the paw:** once "a separate stray bit".
- **The birds at 45:** each read.

Round 2, nine readers of one cut-out each, read the goat's graze sloped to the rump (no better, and once "kneeling or bowing", so the level back stayed), the reading dog with the shorter trunk (the person in one of two), and the dogs cut out close at 45, where nothing chose between them.

Before any reader, the bench's own look caught five things: the goat's first collar a scarf and its beard a beak; nostrils in front of the muzzle; a leaning beg that stretched into a tube; a set-back hip node that left the V; and cream soles that read as white discs.

__DESIGN_TESTS__

## Placement revision 40

Every record stores the placement revision it was made with. v0.42 pictures use revision 40:
- **The goat's tether:** a rope from its collar to a peg in the ground when it grazes (`templates.GOAT42` "T").
- **The birds' angle:** the songbirds and the duck at 45 as well as 90 where they need no direction (`templates.BIRD42` "B", `ANIMAL_YAWS40`).
- **The begging dog's zone:** no one else with an ice cream near it, in front of the bench as well (`templates.BEG40` "B").
- **The square wheel:** the bicycle or barrow clear of the stall and the bench, added after the screen (in front of a stall's legs, the bicycle was "parked against the stall").
- **The stopped hose's crimp:** read on the bench and not taken (`templates.KINK42` "O").

A v0.41 record rebuilds with the v0.41 package. The cast redraws every person, both dogs and the goat (builder 0.42.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.42 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.41. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, and v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out042/` | The 18 `.blend` families (builder 0.42.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib042/` | Every variant the generated scenes and probes use, carried over from `lib041` (the cats, songbirds and duck) or rendered from `out042` |
| `assets/cast/gallery042/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.42.0, placement revision 40); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.42 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v042.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v042.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v042.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-nine screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out042                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out042 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v042   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v042 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery042 --old-gallery <v0.41 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.42 --single   # the release as one zip, tpdb_v0.42.zip
```

The release is one zip, `tpdb_v0.42.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.41 record rebuilds with the v0.41 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
