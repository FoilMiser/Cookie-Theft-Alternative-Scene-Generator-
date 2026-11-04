# TPDB v0.27: faces turned to the viewer, a broom that is a broom, read a twenty-fourth time

v0.26 ended with five gate failures: `sweep` at 0.67, with a fan of bristles read as "a long yellow-headed rake", the one misread; `ice_cream` at 0.83 ("looking at or eating it"); `photo` at 0.83 ("binoculars or a camera"); `about_to_trip` at 0.89, its obstacle off the walker's line; and `sprinkler_package` at 0.89 ("a wooden crate standing in a puddle"). Its oddities were led by a seesaw's plank through its sitter, a stiff hose and faces hidden by a tilted head, and the tier-4 playground had taken 89 failed seeds, for a reason not traced.

v0.27 works through those. Looking closely at crops before drawing anything changed the list: the walkers' feet did point the right way, the hose did reach the fist, and in full profile the eye sits on the head's outline, whichever face it is. Each change went to the isolation bench first, drawn two or more ways and read blind on its own, then into whole test scenes among other events. The set was regenerated and screened a twenty-fourth time, on a slightly shorter, thicker cast.

__INTRO_RESULT__

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What was fixed

| What the v0.26 readers saw | v0.27 |
|---|---|
| `sweep`'s fan of bristles: "a long yellow-headed rake", that screen's one misread (0.67) | Bristles dense and nearly parallel, with two bindings at the neck (builder 0.27.0). Read beside a rake on the bench: "a long-handled rake", "a yellow-bristled broom". No reader said rake of it in its three screened pictures: 1.00 |
| Faces in full profile: "the face is mostly turned away and hidden", with the eye on the head's outline | The head turned 35 degrees to the viewer in every pose of a person in full profile, as a twin of the pose; a pose with a hand-held thing at the face keeps its profile. Remarks on a face hidden or hard to read fell from 22 pictures to 10, by keyword |
| `about_to_trip`: "his head and arms face left", "his legs and feet look like they stride towards the right" (0.89) | The back heel lifted, on its toe, with the head turned. The trip was offered unprompted in all four pictures, "he may be about to walk into or trip over it": 0.96. The obstacle's line still draws remarks ("headed roughly past it") |
| `ice_cream`: "looking at or eating it" (0.83) | The scoop at the lips. 1.00 in 13 pictures |
| `sprinkler_package`: "a wooden crate standing in a puddle" (0.89) | Two short drips from the lid in place of long ones. "The box looks like it is getting soaked": 1.00 |
| `photo`: "binoculars or a camera" (0.83) | Not changed. 1.00, so the half mark was probably reader variance |
| The bird at the ground: "a bird toppling forward", its tail "a party hat or a funnel" | The body less tipped, the head in front of it, an eye on its side: "pecking at seeds" |
| The bicycle: "solid black disc wheels" | Spokes, and no remark on its wheels |
| The dress: "two separate yellow shapes" at the waist | A thin belt at the join. A yellow dress in 16 of 18 pictures; both others are the pose sitting on air |
| A mouth near the edge of the face read as "a small beard or moustache" | The line thinner and in a lip colour. No moustache in 67 pictures |
| Narrow figures: "long thin legs" | Legs an eighth shorter and limbs 14% thicker. The bench went from eight remarks to three, on four cut-outs a side. The screen's remarks did not fall |
| The hose: "like a stiff loop standing in the air" | Hanging from the fist in a slack hook. Fewer remarks, but still "almost like a pipe" in one picture |
| The tier-4 playground's 89 failed seeds, not traced | Traced as far as this: the placement rules are not the cause, nor the room, but which sets of events the planner draws (below) |

Left as they were: the seesaw's plank, looked at closely on the bench, as the leg does lie over it; the leaf clumps over a caught kite; water; the roller's head. Left as notes for the pilot: figures overlapping the pond, goats in a garden or park, a wind that reaches only some things.

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (`vision/isolation_v027.md`, two rounds, 51 cut-outs, 20 readers). The bench casts were built from the same cast library with the variants switched on (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`); the release cast builds with the chosen ones. The broom took two rounds: dense flared bristles were still "a long-handled broom or rake with a yellow fanned head", and a yard broom "a broom or a rake-like tool", so round 2 narrowed them to nearly parallel, and all four cut-outs said broom, one of them beside a rake. With the head turned and the heel lifted the trip was offered unprompted in both cut-outs and in neither of the old, though the two changes were not separated. The scoop at the mouth was first "smelling it like a flower", so it went lower. The bench also found what nobody had listed: a hand past the edge of the book, and a mouth read as a beard. The bearded man's beard read as "a dark face covering or mask", and now stops short of the ear.

__DESIGN_TESTS__

## Placement revision 25

Every record stores the placement revision it was made with. v0.27 pictures use revision 25, which adds to those of revisions 1 to 24 the hose's slack hook to the fist, the lumpy heap beside a hole, the sitter on air kept clear of the path, a duck's wake kept on the pond, and a shadow under a ball in a walker's way. The turned heads, the lifted heel, the broom, the scoop, the hand on the book, the mouth, the shorter figure, the belt, the beard and the pecking bird are in the cast (builder 0.27.0), and the spoked wheel and the short drips in `draw.py`.

__INSPECTION__

The planner's difficulty priors are the calibration measured on the v0.27 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.26. __CALIB_NOTE__

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
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.27 turns the heads in profile, lifts the walker's heel, redraws the broom, the mouth, the belt, the beard and the pecking bird, shortens the figure, and keeps the bench variants behind `TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ` and `TPDB_BEARD`, with `TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BAG`, `TPDB_ROLLER` and `TPDB_SLIDE` from earlier releases |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out027/` | The 18 `.blend` families (builder 0.27.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib027/` | Every variant the generated scenes and probes use, carried over from `lib026` where the cast did not change or rendered from `out027` |
| `assets/cast/gallery027/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (__GALLERY_N__, all pass the validator) |
| `scenegen/` | The generator (0.27.0, placement revision 25); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) and the bicycle's two wheels (`WHEEL27`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.27 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v027.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v027.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v027.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all twenty-four screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out027                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out027 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record __REBUILD_EXAMPLE__ --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v027   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v027 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery027 --old-gallery <v0.26 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.27 --single   # the release as one zip, tpdb_v0.27.zip
```

The release is one zip, `tpdb_v0.27.zip`, about __ZIP_MB__ MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.26 record rebuilds with the v0.26 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- __LIMITS__
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
