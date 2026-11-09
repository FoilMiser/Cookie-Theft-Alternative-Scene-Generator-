# TPDB v0.43: the reading dog lying down, the two women grown up, the dogs' legs, the goat's horns, beard and rope, read a fortieth time

v0.42 ended with 63 of 64 templates through the gate: `about_to_trip` fell on one reader who saw the box beside a boy reading as he walked, with the reading dog and its paper just behind him. Next on the list came the reading dog itself, whose paper "stands upright on its own", and the two women still called "girl". Sam's notes on the figures (`tpdb_work/figure-fixes-v042.md`) ranked nine things:
- keep the reading dog away from the trip;
- lay the dog down with its paper flat on the ground, or let the paper lean on it;
- give the women an adult head and face;
- the goat's hunched graze, its beard, its segmented horns and the garden goat with no tether;
- the dogs' stiff tube legs;
- the begging dog's nose pointing at the sky;
- the camera and the planting;
- the cat's legs at 45;
- the shoes.

v0.43 benched those in two rounds and took most of them (builder 0.43.0):
- **The reading dog:** lying down like a sphinx, the head bowed over a paper laid open on the ground under its forepaws.
- **The women:** the head smaller and the neck longer, a narrower, taller face with smaller eyes set lower and red lips. The woman in yellow has her bob back and darker shoes.
- **The dogs:** the legs a tenth shorter and tapered, the hind leg's thigh part of the body, a brown patch over the spotted dog's hip, the far legs darker.
- **The goat:** one smooth tapered curve for each horn, a larger grey beard, and the neck forward when it stands.
- **Placement revision 41:**
  - the reading dog kept away from the trip and from anyone reading as they walk;
  - a dog, never a goat, on the stopped hose;
  - the stalking cat in profile only, with a gap before its bird;
  - the begging dog's mouth closed;
  - the goat's rope slack and always drawn.
- **Read and left as they were:**
  - the paper leaning on a sitting dog ("the paper falling");
  - the cat at 135, as tangled as at 45;
  - the goat's graze with lower hips ("cramped").
- **Tried and left before the readers:** the begging dog's head lowered. At 45 the gaze check found it facing the viewer, and it placed on none of 12 seeds.

The set was regenerated and screened a fortieth time. Every dog, goat and woman is drawn anew, so no picture is identical to v0.42's.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.42 readers, or Sam's notes, saw | v0.43 |
|---|---|
| `about_to_trip` under the gate, the reading dog beside the walker | The reading dog kept away (revision 41): the trip reads 1.00 in five pictures |
| The woman in yellow called "girl" in 6 of her 14 pictures | A grown woman's head and face: "a woman" in 15 of her 16, once "a woman or girl" |
| The woman in purple "girl" or "girl or young woman" in about ten of her 23 | "A woman" in 16 of her 18, twice hedged ("woman (or older girl)") |
| The dogs' legs "stiff and tube-like" (Sam's notes, the bench) | Shorter and tapered: no stiff, stilt or tube in 29 pictures with a dog |
| The goat's horns stacked segments, the beard unseen, a garden goat untethered | Smooth horns, a grey beard, the rope slack and always drawn, no goat on the hose: tethered in all six pictures, though unusual in four and twice, from behind, possibly a sheep |
| The stalking cat's legs tangled at 45 | In profile only: stalking in all three pictures |
| The begging dog "howling", its nose straight up | The mouth closed: begging in all four pictures. The lowered head did not place at 45 |
| `photo` and `plant_flowers` under the strict count | Five probes each: 0.90 and 1.00, both passing read strictly |
| The reading dog's paper "stands upright on its own" | Lying down over a paper on the ground: never a person and no paper standing, but "lying on an open newspaper", once tearing it. **Not fixed: under the gate** |

Left as notes for the pilot: the stopped hose's swelling, figures drawn over the pond or the prop beside them, and the goat in a garden.

## The isolation bench

The two lists were benched in two rounds of single cut-outs (`vision/isolation_v043.md`). Round 1 had sixteen readers of 31 cut-outs, two to a reader and never two takes of one thing. It read each thing in v0.42's cast and scene against the cast with every switch on:
- **The reading dog:** v0.42's "kneeling upright on its hind legs like a person". Lying down, reading in three of three, each with "sniffing" or "pawing" beside it, the paper "an open book". Leaning, the paper "balanced on one corner", "falling".
- **The woman in yellow:** "a woman or older girl" and "A woman or girl" for v0.42's; "a woman" in both of the new.
- **The dogs:** v0.42's legs "long, straight posts" and "stiff like stilts"; none of that in the new.
- **The goat:** the new graze "cramped", so v0.42's was kept. The rope was "a J-shaped hook or walking-stick handle".
- **The cat at 135:** "jumbled together under the body", as at 45.

Round 2, six readers of 12 cut-outs, read four things:
- **The reading dog:** a larger paper slanted flat, "an open newspaper lying flat on the grass", though the raised head looked "past the paper".
- **The goat's rope:** the slack rope, with no stiffness.
- **The begging dog:** the closed mouth, "as if begging, possibly for the ice cream", where v0.42's was "happily stretching or sniffing the air".
- **The woman in yellow:** her darker shoes, unremarked.

Before any reader, the bench's own look caught four things:
- the begging head's pitch barely moved the nose;
- the woman in purple's ponytail vanished from the front;
- the cat at 135 was as tangled as at 45;
- the lowered begging head did not place.

__DESIGN_TESTS__

## Placement revision 41

Every record stores the placement revision it was made with. v0.43 pictures use revision 41:
- **The trip's zone:** the reading dog kept out of a zone round the trip's walker and box, and away from anyone reading as they walk (`templates.TRIP43` "B").
- **The reading dog's paper:** laid flat on the ground under the forepaws of a dog lying down (`templates.READ43` "A"; "B", the paper leaning on a sitting dog, read on the bench and not taken).
- **The stopped hose:** a dog on it, never a goat (`templates.HOSE43` "B").
- **The stalking cat:** in profile only, with a gap of 45 units between its front and the bird (`templates.CAT43` "B"; "C", at 135 as well, not taken).
- **The begging dog:** its mouth closed (`templates.BEGX43` "B").
- **The goat's rope:** slack, with room kept for its peg, and the goat never drawn untethered (`templates.TETHER43` "R").

A v0.42 record rebuilds with the v0.42 package. The cast redraws both dogs, the goat and the two women (builder 0.43.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.43 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.42. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, and v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out043/` | The 18 `.blend` families (builder 0.43.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib043/` | Every variant the generated scenes and probes use, carried over from `lib042` or rendered from `out043` (the dogs, the goat and the two women) |
| `assets/cast/gallery043/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.43.0, placement revision 41); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.43 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v043.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v043.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v043.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out043                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out043 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v043   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v043 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery043 --old-gallery <v0.42 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.43 --single   # the release as one zip, tpdb_v0.43.zip
```

The release is one zip, `tpdb_v0.43.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.42 record rebuilds with the v0.42 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
