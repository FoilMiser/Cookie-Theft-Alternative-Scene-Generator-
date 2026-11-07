# TPDB v0.40: one hand for the blown hat, two on the hose, the goat's head out of the grass, the heaps of dry leaves, read a thirty-seventh time

v0.39 ended with all 64 templates through the gate, and its list began with the strict count. Read strictly, the full marks the scorers called hedged left one template under: `windy_hat`, whose reader saw both arms thrown up "in alarm rather than reaching". The list went on to the summer heap's green leaves, "a little odd for raked fallen leaves"; the goat's head lost in the grass tuft; the grandfather's two white sleeves to the nozzle, "one long flat white shape"; the pinched hose read as a puddle; and the ice-cream eater drawn so small at the back that the cone was "something small and pink".

v0.40 benched those in two rounds and changed the cast in three poses (builder 0.40.0) and the placement in one revision:
- **The cast:** the reach for the hat with one hand, the other at the side; the hose held at the nozzle and, with the other hand, lower down; and the goat grazing with its back level and its head ahead of its legs.
- **Placement (revision 38):** draws the heaps of dry leaves, leaf-shaped, the goat's tuft ahead of its muzzle and behind its head, and keeps an ice-cream eater at least 170 px tall.

The set was regenerated and screened a thirty-seventh time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.39 readers saw | v0.40 |
|---|---|
| The blown hat, both arms up: "or as her throwing her hands up in alarm rather than reaching" | One hand up toward the hat, the other at the side. On the bench all three readers of the old reach offered hands thrown up "startled" or "cheering", and all three of the new one had her reaching after the cap. In the screen: "He reaches up with one arm toward an orange cap". 0.933 read strictly, in five pictures |
| "The man's arms are drawn as one long flat white shape stretched out to the nozzle" | The near hand holds the nozzle up to the face, the far hand the hose below it: "One raised hand holds the nozzle up near his face, and the other hand holds the hose lower down" |
| The goat: "The goat's head is small and low against the grass tuft, and at first glance it is hard to tell head from tuft"; on the bench "The goat looks folded or curled up rather than standing level" | The back level on straight legs and the neck reaching forward and down; the tuft ahead of the muzzle, behind the head, with blades running from the mouth into it. No reader of the screen lost the head in the tuft. The hunch at 45 and 135 is still read on the bench, and goes on v0.41's list |
| "Some of the raked leaves are green rather than brown or autumn-coloured, which looks a little odd for raked fallen leaves" | Dry leaves, leaf-shaped (as ovals they were "seeds, nuts, beans" on the bench). No reader finds them green, but five pictures find brown leaves odd under green trees, the third drawing of the heap to draw a remark on the season |
| The ice cream: "something small and pink" | An ice-cream eater at least 170 px tall. Every eater named, in 17 pictures |
| The pinched hose under the dog: "it could also be read as a puddle or a bulge in the hose" | Not seen, in six pictures, with nothing changed |

Left as notes for the pilot: goats in a garden or park, figures drawn over the prop beside them, and wind that moves only the hat.

## The isolation bench

The list was benched in two rounds of single cut-outs, two to a reader and never two takes of one thing (`vision/isolation_v040.md`). Round 1, twenty-one readers of 41 cut-outs, read each thing in v0.39's cast against the new drawings:
- **The reach:** with one hand, the other by the chest (B) or at the side (C).
- **The hose:** in two hands.
- **The goat's graze:** at 90, 45 and 135, in two settings, with the tuft ahead of the muzzle.
- **The walking front foot:** left flat.
- **The heaps:** of dry leaves or of cut grass.

What round 1 found:
- **The reach: C.** It lost the hands thrown up "startled" or "cheering" of all three old readers; the hand by the chest of B was "a thin white object" or "small and blobby".
- **The hose:** the two hands were read apart in both.
- **The goat:** both new grazes lost the old "contorted" and "folded or curled up", and C read cleanest at 90. Its hunch at 45 and 135, and the bite floating apart from the tuft, remained.
- **The walk:** gained nothing, so it is unchanged.
- **The heaps:** the dry leaves read as leaves but, as ovals, also as nuts; cut grass as a green dome or dustpan.

Round 2 read the leaves drawn pointed with a midrib and a stalk, "a small pile of brown, dry leaves" in all four, and the goat's bite run into its tuft, "as if it is pulling up or chewing a blade".

Before any reader, the bench's own look caught two things:
- **The first reach crossed the face.** It used the near arm, which crossed in front of the face like a hand shading the eyes; the far arm reaches now.
- **A part-rebuilt bench cast.** It had kept that first reach for a figure built before the change, so the bench cast was built whole again and its cases run again.

__DESIGN_TESTS__

## Placement revision 38

Every record stores the placement revision it was made with. v0.40 pictures use revision 38, which adds to those of revisions 1 to 37:
- **The heaps:** the broom's heap and the raked pile drawn of dry leaves, leaf-shaped, and twigs (`draw.HEAP40` "D").
- **The goat's tuft:** drawn just ahead of its muzzle and behind its head, a little shorter, with a few blades running from its mouth into it (`templates.TUFT40`).
- **The ice cream:** an ice-cream eater's figure at least 170 px tall (`templates.ICE40`).

All are behind the revision, so v0.39's records rebuild with the v0.39 package. The cast is v0.39's but for the reach for a blown hat, the hose inspected and the goat's graze (builder 0.40.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.40 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.39. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, and v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out040/` | The 18 `.blend` families (builder 0.40.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib040/` | Every variant the generated scenes and probes use, carried over from `lib039` or rendered from `out040` |
| `assets/cast/gallery040/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.40.0, placement revision 38); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.40 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v040.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v040.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v040.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-seven screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out040                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out040 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v040   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v040 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery040 --old-gallery <v0.39 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.40 --single   # the release as one zip, tpdb_v0.40.zip
```

The release is one zip, `tpdb_v0.40.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.39 record rebuilds with the v0.39 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
