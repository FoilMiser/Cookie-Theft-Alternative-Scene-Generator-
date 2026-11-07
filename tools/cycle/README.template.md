# TPDB v0.38: a basket at the washing line, the washing wet, no cat on the storm's fence, read a thirty-fifth time

v0.37 ended with 63 of 64 templates through the gate. The one failure was `hang_laundry`, on a picture identical to v0.36's, where it had had full marks: "I can't tell whether the boy is hanging the T-shirt up or taking it down", as readers had said in v0.30 and v0.31, and as readers of three screens had said what was missing: "there is no laundry basket to show which". Its list went on to a storm pointer offered "the cat or something on the fence", three screens running on one picture, and to the broom's autumn leaves under green trees.

v0.38 benched the washing in two rounds: the garden's own laundry basket set at the hanger's feet, and the shirt dripping. The design tests found that the basket under the dripping shirt told a story of its own, dry washing about to get wet, and the rest of the washing now drips too. Placement rules keep the cat off the fence, and a perched bird out of the garden, in a storm pointer's picture. The set was regenerated and screened a thirty-fifth time.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.37 readers saw | v0.38 |
|---|---|
| "I can't tell whether the boy is hanging the T-shirt up or taking it down" | A basket of washing on the grass at the hanger's feet, the garden's laundry basket with its bundles drawn as cloth and a sleeve over the rim, and the shirt dripping. On the bench, with neither, three readers of three could not tell up from down, and all nine who saw the drops leaned to hanging out. In the screen all three readers have the shirt pegged up: "He is reaching up and pegging a white T-shirt onto the line" |
| A design test, the basket under the dripping shirt: "the dry laundry may be about to get wet" | All the washing drips, the jeans beside the shirt and the sleeve over the basket's rim too. Kept from under the shirt instead, the basket had room only where the planter kneels, and the washing and a planter placed 3 of 12 together where they had placed 12 |
| "The man in green could be pointing at the storm clouds, or up at the cat or something on the fence" | No cat walking the fence in a storm pointer's picture, the stalking cat on the ground under her, and in the garden no bird perched up high either. "The clouds are the only thing up there" |

Left as notes for the pilot: goats in a garden or park, the seesaw man's legs over the plank, and hair and clothes that the wind does not move. The autumn leaves, remarked on in seven pictures this time, head v0.39's list.

## The isolation bench

The washing was benched in two rounds of single cut-outs, fifteen readers in all (`vision/isolation_v038.md`): the hanger as in v0.37; with the basket; with the basket and the shirt dripping; then with the bundles drawn as cloth and the first drop forming on the hem; and with the drops and no basket. With neither cue, all three readers were unsure which way the shirt went; the basket alone moved one of three ("The full basket fits either reading"); with the drops, every reader leaned to hanging out. The cloth won, for its second cue and because it took the bundles from "balls or cushions" to clothes. The basket and the drops are drawn in SVG by the template, so the cast is v0.37's (builder 0.38.0). v0.37's washing probes were rebuilt on their own seeds and looked at first (`tpdb_work/rb38.py`), and so was its picture 57, whose seed no longer places a tier-3 garden under the cat rule.

__DESIGN_TESTS__

## Placement revision 36

Every record stores the placement revision it was made with. v0.38 pictures use revision 36, which adds to those of revisions 1 to 35 a basket of washing on the grass at the hanger's feet, measured from her drawing, on the side she faces or else behind her heels, between the line's posts, clear of others' feet and kept as a thing on the ground, with no filler basket beside it; the shirt she pins up, the jeans beside it and the basket's sleeve dripping; no cat walking the fence in a storm pointer's picture, and the stalking cat on the ground under her; and in the garden no bird perched up high with her, the bird dropped from the plan. All are behind the revision, so v0.37's records rebuild. The cast is v0.37's (builder 0.38.0).

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.38 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.37. __CALIB_NOTE__

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, and v0.37 and v0.38 draw nothing new in the cast |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out038/` | The 18 `.blend` families (builder 0.38.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib038/` | Every variant the generated scenes and probes use, carried over from `lib037` or rendered from `out038` |
| `assets/cast/gallery038/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.38.0, placement revision 36); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.38 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v038.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v038.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v038.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all thirty-five screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out038                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out038 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v038   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v038 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery038 --old-gallery <v0.37 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.38 --single   # the release as one zip, tpdb_v0.38.zip
```

The release is one zip, `tpdb_v0.38.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.37 record rebuilds with the v0.37 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
