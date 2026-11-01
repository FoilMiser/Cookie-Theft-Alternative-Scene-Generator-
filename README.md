# TPDB v0.18: a wave clear of the backdrop, figures kept apart, a face in profile, and the v0.17 oddities refined, read a fifteenth time

v0.17 ended with a fourteenth blind legibility screen: for the third screen running no item was misread, set or probes,
744 of 748 scored items had full marks, every inference and contradiction was read in full, and 63 of 64 templates passed
the gate. The one that fell short was the waver, on a single hedge in the tier-4 park: a small girl far back on the path,
her raised hand on the dark outline of the hedge line behind her, was "holding a string ... or just a wave". The readers
also reported seven kinds of unintended oddity: two figures of different events drawn into each other ("squashed together,
one partly inside the other"), a dark-haired woman in profile with "no visible face", sizes off for their depth (a sleeping
cat "very small compared with the people", a bird "fairly large compared with the cat"), a rubbish bin 6 px inside the
frame read as "partly cut off", goats out of place in a garden or park, drawing quirks (a duck's wake running "to just
above the man's head") and the older ones noted for the pilot.

v0.18 works through that list as v0.12 to v0.17 did: each weak visual is taken to the isolation bench (forced alone into a
picture, cut out, read blind, redrawn and read again until it reads as intended), each placement rule is read blind in
whole test scenes among other events, and only then does it all go back into the set, which is regenerated and screened
a fifteenth time.

The waver, the one template that failed the v0.17 gate, passes the fifteenth screen: read as a wave in all four of its pictures, and no reader saw a string at the hand. The refined visuals read as meant: the dark-haired woman was in 16 pictures, ten in profile, and no reader said her face was missing; the larger cats read as asleep and as stalking on the grass; catches kept their bodies apart. But the set scored 0.986 over all items (0.995 in v0.17), with 1.9 unintended oddities per picture (1.3), and 60 of 64 templates pass the gate. Four that passed in full in v0.17 fall short, each in a single picture: the reading walker in the windy tier-4 park, read as "holding an open newspaper" and not seen as about to trip; the stalking cat on the tier-4 garden's fence, read as walking; the frying pan in a probe beside a hose reel, read as "a hose nozzle or watering wand", the first misread anywhere in four screens; and a runner read as "striding or jogging". `vision/flaws_v018.md` lists them with their fixes for v0.19.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Python
`bpy`, Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`.

## The v0.17 failure

| Template | What the v0.17 readers saw | v0.18 |
|---|---|---|
| `wave` | In the tier-4 park, a small girl far back on the path, one arm up, her hand right on the dark outline of the hedge line behind her: "a thin curly line near her raised hand. It could be (a) a string she is holding ... or (b) just a wave with a motion line. I could not tell which." Read in full in its two other pictures, and in all its pictures in v0.15 and v0.16 | The waving hand and its two motion arcs are placed only against plain ground, wall or sky: no outline of the backdrop (hill and hedge lines, the ground's edge, fence tops, roofs, awnings, windows, the path's edges) may run through the box round the hand. And no waver stands at the far back (feet above y = 650), where the hand is a few pixels across. In six test scenes the wave read as a wave every time, "with motion lines" |

## The oddities fixed

| What the v0.17 readers saw | v0.18 |
|---|---|
| A man reading as he walks and a man catching beside him "drawn overlapping, 'squashed together', one partly inside the other"; the ball "could hit the reading old man instead of reaching the catcher" | Figures of different events at the same depth (within 40 px, scaled) stand apart, their boxes at least 6 px apart, not only their feet; and the ground just behind a catcher, where a missed ball would go, is kept clear of anyone else |
| "Woman in yellow has no visible face; head is a round dark shape": the dark-haired woman in profile, her bob covering the cheek | Her bob's side hair runs only behind the ear and her hairline is higher, so a profile shows the face; every reading walker's head is bent 20 degrees instead of 30, which bent further had hidden her face over the book ("only a skin-coloured profile edge under dark hair") |
| A sleeping cat in front "very small compared with the people"; a pecking bird "fairly large compared with the cat" | Both cats 1.4 times their v0.17 size (the bird went from "close to half the cat's body length" to "a third" on the bench) |
| A rubbish bin "partly cut off by the edge", though 6 px inside the frame | A filler closer than 24 px to a side edge is moved 30 px inside the picture |
| A duck's wake lines running "to just above the man's head" of a picnicker on the shore | The wake and the water just past it are kept clear of every figure, placed before or after the duck |

Left as they were: the goat in a garden or park, which two readers called unusual (it read as a goat in all its pictures;
a note for the pilot, as since v0.11); the size of a man walking at the back of the park, "a little too large for how far
back he is" (the depth scale is the same for everyone); the older ones (a stall with nobody at it, a dog with no owner,
walkers on the grass beside a path, watering before a storm, the square-wheeled bicycle standing on its own).

## The isolation bench

Two rounds, 14 cut-outs, each read blind by fresh readers two at a time with the isolation prompt (`vision/isolation_v018.md`
gives every reading). The catching woman's face read at the first try; reading as she walked it took the raised hairline,
the side hair behind the ear, and the head bent less; the cats were enlarged twice and still read as "small" asleep, which
stays a note (in the test scenes nobody called the sleeping cat small).

## Design tests

The refined visuals and the new placement rules were then read blind in six whole test scenes among other events (`vision/design_tests_v018.md`), the waver, the one template the v0.17 gate failed, put in all six, so each could only stand where its hand is clear of the backdrop's lines and not at the far back. The wave read as a wave in all six, every time "with motion lines", and no reader saw a string or a held object at the raised hand. No reader saw two figures drawn into each other, a ball heading for someone other than the catcher, a duck's wake reaching anyone or a thing cut off by the picture's edge. The sleeping cat read as asleep in all four scenes it was in, and no reader there called it small; the dark-haired woman read as reading as she walks, though her "facial features are minimal".

Nothing in the test scenes led to a further change before the set was built.

## Placement revision 16

Every record stores the placement revision it was made with. v0.18 pictures use revision 16, which adds the rules above
to those of revisions 1 to 15: the waving hand clear of the backdrop's outlines and no waver at the far back; a body gap
between figures of different events at the same depth; the ground behind a catcher kept clear; fillers kept at least
24 px inside the side edges; and a duck's wake kept off figures. Inspecting the built set added one more: the planner chooses
each inference template under its own sky, so a sprinkler soaking a box (which needs a clear sky) could be chosen with a
rain warning's storm clouds, and the first tier-3 park picture had both; now a clear-sky template is dropped from a set
whose storm clouds another template brings. Its replacement had a man feeding the ducks with an angler's float at his
hand (as a test-scene reader had put it, "the fishing float lands right beside the man and near the crumbs"), so a fishing
line and its float are now kept clear of every other figure too; and the next one put the sprinkler's soaked box right
beside a picnic basket, where it could pass for the picnic's own (and the picnic seem about to be soaked), so a picnic and
the soaked box are no longer chosen for the same picture. The tier-3 park picture was remade a third time.

The planner's difficulty priors are the calibration measured on the v0.18 templates (`calibration.json`); only the stalking cat's moved, its larger cat now more salient.

## The fifteenth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 39 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.17.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 |

Across all 60 pictures only 10 of 720 scored items fell short of full marks (4 of 748 in v0.17), and one, in a probe, was misread: the frying pan, held nearly edge-on beside a hose reel, read as a hose nozzle. In the set nearly every shortfall came from two tier-4 pictures: in the garden a cat on the fence top read as walking and a boy's raised arms under a ball in a tree as "cheering, stretching or waving"; in the park a teenager reading as she walks, her book held wide in a windy picture, read as "holding an open newspaper", and the bucket ahead of her as having "no obvious owner or purpose". Unintended oddities rose from 27 to 40 in the set and from 35 to 41 in the probes (39 probe pictures, 44 in v0.17). None of the v0.17 oddities came back as reported then: no figures of different events drawn into each other, no face hidden by hair, no filler cut off by the edge, no duck's wake reaching anyone. What the readers noticed instead: figures drawn tight against tall things (a photographer "inside the swing frame", a woman "tightly overlapping the lamp post", a begging dog against a woman's legs); children reaching for a ball in a tree who stand "beside the trunk, not under the stuck ball"; kicks that look like a miss and painters whose painted boards are beside them; water drawn as dashes, "readable as a dotted trajectory"; and, again, goats out of place and market stalls with nobody at them.

The template that failed the v0.17 gate and the templates whose visuals or placement were refined for its oddities (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.17 | v0.18 | v0.18 meaning items |
|---|---|---|---|
| `wave` | 0.83 (3 items) | 1.00 (4 items) | — |
| `play_catch` | 1.00 (8 items) | 1.00 (8 items) | — |
| `about_to_trip` | 1.00 (18 items) | 0.88 (12 items) | 0.75 (4) |
| `cat_sleeping` | 1.00 (4 items) | 1.00 (3 items) | — |
| `cat_stalks_bird` | 1.00 (9 items) | 0.89 (9 items) | 0.83 (3) |
| `ducks_bread` | 1.00 (9 items) | 0.94 (9 items) | 0.83 (3) |

The waver passes at 1.00 over four pictures, its hand clear of the backdrop's lines. Catches (four pictures) and the larger sleeping cat (three) read with full marks, the cat "curled up asleep" each time, though one probe reader still found it "small"; the duck feeding missed half a point only where its reader did not say the duck wanted the bread. The stalking cat read in full on the grass and as walking on the fence, and the reading walker, read in full in three pictures, fell short in the windy tier-4 park (below).

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 |

Every template was screened in at least three pictures (50 in three, 11 in four, 1 in five, 1 in six, 1 in seven). Four fail, each in a single picture, and all four read in full in v0.17: the reading walker in the windy tier-4 park, the stalking cat on the tier-4 garden's fence, the frying pan beside a hose reel in a probe (one misread) and a runner read as "striding or jogging". About five templates of the gate's movement between screens is reader variance (the v0.9 retest), but each of these has a cause in its picture that can be fixed. The v0.19 fixes: no reading walker in a windy picture or at the far back, the stalking cat on a fence closer to its bird, no hose reel beside the pan waterer and the pan turned to show its inside, and motion lines behind a runner.

Templates that did not pass (`vision/flaws_v018.md` gives what the readers saw and the next fix):

| Template | v0.18 mean | Pictures | Misreads |
|---|---|---|---|
| `pan_watering` | 0.83 (9 items) | 3 | 1 |
| `run` | 0.83 (3 items) | 3 | 0 |
| `about_to_trip` | 0.88 (12 items) | 4 | 0 |
| `cat_stalks_bird` | 0.89 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 5 | 0 (0) | 3 | 0.780 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 4 | 0 (0) | 3 | 0.773 | — | 18 | 0.027 | goat grazing, plant flowers, feed birds |
| T1_street_s1031 | 4 | 0 (0) | 3 | 0.779 | — | 15 | 0.045 | birds flying, jump, run |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.772 | — | 15 | 0.033 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 3 | 0.730 | 0.413 | 16 | 0.038 | cat stalks bird, dog playing, sweep |
| T2_garden_s8118_iso (isomorph of T2_playground_s1042) | 8 | 1 (0) | 3 | 0.712 | 0.378 | 18 | 0.041 | ball in tree, swing, rake |
| T2_park_s2022 | 8 | 1 (0) | 4 | 0.696 | 0.410 | 18 | 0.024 | lost balloon, balloon, ducks swimming, ice cream |
| T2_street_s2032 | 8 | 1 (0) | 4 | 0.706 | 0.372 | 17 | 0.046 | ice cream drop, wave, bird perched, water flowers |
| T2_playground_s1042 | 8 | 1 (0) | 3 | 0.703 | 0.397 | 16 | 0.032 | kite in tree, birds flying, slide |
| T2_playground_s6109_iso (isomorph of T2_park_s2022) | 8 | 1 (0) | 4 | 0.684 | 0.393 | 19 | 0.037 | kite in tree, dog sleeping, push stroller, sandbox |
| T3_garden_s6013 | 12 | 3 (1) | 6 | 0.640 | 0.312 | 22 | 0.047 | dog begs, about to trip, square wheel, swing, dog sleeping, play catch |
| T3_garden_s7102_iso (isomorph of T3_street_s8133) | 12 | 2 (0) | 5 | 0.654 | 0.344 | 20 | 0.038 | lost balloon, sprinkler package, birds flying, bird perched, play catch |
| T3_park_s14123 | 12 | 3 (0) | 5 | 0.638 | 0.316 | 22 | 0.030 | ducks bread, sprinkler package, kite in tree, dig, fishing |
| T3_street_s8133 | 12 | 2 (0) | 5 | 0.670 | 0.349 | 20 | 0.051 | ball in tree, lost balloon, push stroller, photo, play catch |
| T3_street_s6104_iso (isomorph of T3_park_s14123) | 12 | 3 (0) | 5 | 0.639 | 0.325 | 21 | 0.052 | dog begs, ball in tree, lost balloon, bird perched, birds flying |
| T3_playground_s16343 | 12 | 3 (1) | 6 | 0.653 | 0.301 | 21 | 0.040 | rain coming, seesaw heavy, bucket hat, walk dog, dog sleeping, slide |
| T4_garden_s212414 | 18 | 5 (1) | 9 | 0.569 | 0.220 | 26 | 0.045 | dog begs, ball in tree, sprinkler package, cat stalks bird, dog reading, play catch, carry box, cat sleeping, birds flying |
| T4_park_s32624 | 18 | 5 (1) | 8 | 0.574 | 0.206 | 31 | 0.036 | bird steals, about to trip, windy hat, ducks bread, sitting on air, jump, rake, bird perched |
| T4_park_s13111_iso (isomorph of T4_street_s54034) | 18 | 4 (1) | 7 | 0.597 | 0.232 | 26 | 0.036 | sprinkler package, ice cream drop, windy hat, pan watering, photo, carry box, fishing |
| T4_street_s54034 | 18 | 4 (1) | 7 | 0.587 | 0.238 | 26 | 0.055 | about to trip, ice cream drop, windy hat, bucket hat, carry bag, birds flying, sweep |
| T4_playground_s303559 | 18 | 5 (2) | 9 | 0.565 | 0.243 | 26 | 0.045 | about to trip, ice cream drop, ball in tree, square wheel, dog reading, carry box, read bench, birds flying, photo |

Isomorph pairs differ by at most 0.016 in content and 0.019 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,471 | 9 | 1,927 | 10^10.0 |
| garden | 2 | 28,489 | 27 | 13,003 | 10^12.8 |
| garden | 3 | 3,134,337 | 296 | 387,320 | 10^18.4 |
| garden | 4 | 147,136,991 | 571 | 9,554,664 | 10^23.5 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 47,870 | 24 | 20,959 | 10^11.7 |
| park | 3 | 6,410,537 | 240 | 1,095,206 | 10^17.4 |
| park | 4 | 442,485,244 | 393 | 54,909,608 | 10^23.4 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,720 | 24 | 2,983 | 10^11.8 |
| street | 3 | 545,151 | 236 | 82,853 | 10^17.4 |
| street | 4 | 12,069,908 | 362 | 1,388,400 | 10^22.7 |
| playground | 1 | 1,740 | 11 | 1,152 | 10^9.6 |
| playground | 2 | 15,247 | 27 | 6,005 | 10^12.5 |
| playground | 3 | 925,793 | 199 | 125,120 | 10^17.8 |
| playground | 4 | 17,417,338 | 254 | 1,784,957 | 10^22.3 |

In all 630,234,190 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

## Folders

| Folder | What it holds |
|---|---|
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts) |
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions; v0.18: the reading walker's head bent less), `people.py` (v0.18: the bob that leaves a profile's face open), `animals.py`, `specs.py` (v0.18: the larger cats) |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out018/` | The 18 `.blend` families (builder 0.18.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib018/` | Every variant the generated scenes and probes use: those of unchanged families and poses carried over from `lib017`; the dark-haired woman, the cats, every reading walker and every variant first needed in v0.18 rendered from `out018` |
| `assets/cast/gallery018/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.18.0, placement revision 16); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.18 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v018.md` and their rounds), flaw lists (`flaws_v04.md` to `flaws_v018.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v018.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all fifteen screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |

## How to run

```bash
pip install bpy==5.2.3 cairosvg pillow numpy scipy wordfreq jsonschema --break-system-packages

cd assets/cast && python build_cast.py out018 && cd ../..           # build the cast (about a minute)
cd assets/cast && python gapcheck.py out018 person.mei && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s14123.json --out /tmp/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.combos --out combos.json
python vision/isolation_bench.py /tmp/bench catch_a readwalk_a stalk_a   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v018   # then describe and score: vision/screen_prompts.md
python vision/summarize_screen.py vision/v04:<v0.4 scenes> vision/v05:<v0.5 scenes> vision/v06:<v0.6 scenes,probes> \
    vision/v07:<v0.7 scenes,probes> vision/v08:<v0.8 scenes,probes> vision/v09:<v0.9 scenes,probes> \
    vision/v010:<v0.10 scenes,probes> vision/v011:<v0.11 scenes,probes> vision/v012:<v0.12 scenes,probes> \
    vision/v013:<v0.13 scenes,probes> vision/v014:<v0.14 scenes,probes> vision/v015:<v0.15 scenes,probes> \
    vision/v016:<v0.16 scenes,probes> vision/v017:<v0.17 scenes,probes> vision/v018:scenes,probes
python vision/gate.py vision/v018 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery018 --old-gallery <v0.17 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.18 --single   # the release as one zip, tpdb_v0.18.zip
```

The release is one zip, `tpdb_v0.18.zip`, about 150 MB. Google Drive does not virus-scan a file over 100 MB, so it asks
to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that.
`package_release.py` replaces the `package_v0XX.sh` scripts and checks, file by file, that the zip holds every file of
the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's
pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.17 record rebuilds with the v0.17 package.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Four templates fall under the legibility gate after the v0.18 screen, each in a single picture, all four
  read in full in v0.17: the reading walker in the windy tier-4 park ("reading or holding an open newspaper",
  no trip predicted), the stalking cat on the tier-4 garden's fence (read as walking), the frying pan in a
  probe beside a hose reel (misread as "a hose nozzle or watering wand") and a runner in a probe ("striding
  or jogging"). `vision/flaws_v018.md` gives what the readers saw and the next fixes.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are at the ceiling: across 60 pictures only 10 of 720 scored items fell short of full marks, and
  one was misread. AI readers describe exhaustively, so the screen cannot rank templates by difficulty;
  that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full and a v0.18 scorer listed seven judgment calls, enough
  to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 16 make them harder (walkers' lanes,
  pointing lines, feet off benches, the photographer's line of sight, the waver's clear hand, body gaps).
  The tier-4 garden, playground and street pictures came from wider seed searches with no template-variety
  steering, as in v0.15 to v0.17; the tier-4 park came from the batch's own seed search past the showcase
  seed. Their records rebuild them exactly. Two of the four gate failures were in tier-4 set pictures, where
  many events meet, and a third beside the garden's hose reel.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures.
- The stuck girl on the seesaw always calls out, but no reader mentioned it: the tilt, the man's weight and
  the motion lines at her feet carry the reading.
- The body check (`assets/cast/gapcheck.py`) finds parts that come apart, not parts that pass through one
  another: a hand inside a hip or a lobe of skirt inside the bell is allowed, and only the outline drawn
  in the render shows whether the join looks right.
- The wind reaches the hat, the washing, an empty swing, the tree and the sky, but not hair or clothes: the
  cast is posed and rendered in 3D, and a blowing fringe or skirt would be a new rig.
- The isolation bench reads one template cut out of its picture. A visual that reads alone can still be
  misread among other events, so the bench comes before the test scenes and the screen, never instead of them.
- The planner's priors come from the v0.18 calibration, which differs from v0.17's only in the stalking cat's
  inference (the cat redrawn larger) and by at most 0.002 on every other template.
- Exact rebuilds hold within a release: the v0.18 placement rules (revision 16), the larger cats and the
  dark-haired woman's new hair change where events go and how they look, so a v0.17 record rebuilds with the
  v0.17 package.
- Variants whose pose did not change are carried over from the v0.17 library; rendered again from the
  v0.18 cast they come out the same, or within a few levels of grey at anti-aliased edges.
- The sleeping cat, 1.4 times its v0.17 size, still read as "small" in one probe; drawn larger, the standing
  and stalking cats would come out as big as the small white dog. Its size is a note for the pilot.
- Twenty-seven actions in the cast are used by no template; they are kept for later templates and left
  out of the gallery and the screen, so they have never been read blind.
- Edge density is not part of the isomorph rule. Street pictures stay the busiest, so a street
  isomorph of a park or playground picture carries more visual detail at the same object count.
- The top third of park and playground pictures is still mostly sky.
- A filler closer than 24 px to the picture's side edge is now moved 30 px inside it, and no reader said one
  was cut off; the sun can still sit partly off the top edge, where the backdrop draws it.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
