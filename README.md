# TPDB v0.23: a frying pan that looks like one, a dog that begs, an older man who faces his way, read a twentieth time

v0.22 ended with a nineteenth blind legibility screen: no item of the set was misread, 285 of its 287 scored items had full
marks, and 63 of 64 templates passed the gate. The one that fell short was the frying pan, for the second screen running:
out of the street, it read as a frying pan in two of its three garden probes and as "a grey, round watering can" in the
third, held close in front of the flowers with its handle hidden ("I could not clearly see a spout or handle"). Two
inferences in the tier-4 street took a half point each: a dog with a paw raised in front of a man eating ice cream,
"perhaps hoping for some ... or just walking by", and a reading walker whose box lay "to the side of / slightly ahead of"
her. The readers also reported oddities, none of them misreadings: the older man's grey ring of hair, seen in profile, read
as "a beard" or "a face mask", so that he seemed to walk the other way, in the tier-4 park toward a sleeping cat on the
path behind him; a runner and a woman with a pram heading toward each other; a duck at an angler's float that "might go for
the bait"; and a wheelbarrow's stand "like a boot".

v0.23 works through that list. The four that are about how things look (the pan, the begging dog, the older man's profile
and the barrow's leg) went to the isolation bench first, in two rounds, where each was drawn two or more ways and read blind
on its own; the rest are placement rules (revision 21). All of them were then read blind in whole test scenes among other
events, the set was regenerated, and it was screened a twentieth time.

The twentieth screen is the first in which every scored item had full marks: all 729 items of the 65 pictures, the set's 283 and the probes' 446, and no misread. All 64 templates pass the gate (63 in v0.22). The frying pan, redrawn on the bench, read as a frying pan in all three of its pictures after misreads in v0.21 and v0.22; the begging dog, sitting up with its paws at its chest, as begging in all three; and the reading walker's obstacle, now a full step ahead, as a trip in all three. No runner and walker were about to collide, no duck went for an angler's float, and no reader saw a boot under a wheelbarrow. The screen is now at its ceiling and no longer separates the templates; what the readers still reported are oddities, and `vision/flaws_v023.md` lists them for v0.24: above all a sleeping cat on the path just behind a walking man's back foot, again read as something he "could trip over".

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Python
`bpy`, Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`.

## What was fixed

| What the v0.22 readers saw | v0.23 |
|---|---|
| The frying pan held close in front of the flowers, its short handle under the hand: "a grey, round watering can ... a watering can, a bucket or even a stone" (the misread) | Redrawn on the bench (builder 0.23.0): the pan held out from the body, seen from above at a slant so that its depth shows, on a thicker handle about as long as the pan is wide. Both bench readers called it "a frying pan or saucepan"; face-on on a long handle, two other drawings read as "the sprinkler head (rose) of a watering can" or a hose wand |
| A dog with one paw raised, its body sloping down to a tail laid along the ground: "perhaps hoping for some ... or just walking by", "as if it were half-lying" | Redrawn on the bench: sitting up on its haunches, both front paws folded at the chest, the head tipped up to the food, the tail curled round the haunch. All four bench readers: "sits up ... begging" |
| The older man in profile, his grey ring of hair behind the ear read as "a beard" or "a face mask", so he seemed to face the other way | Redrawn on the bench: the grey kept to the back of the head and a fuller nose standing out from the face. Both bench readers had him walking the right way |
| The wheelbarrow's thick dark leg and the foot running forward from it: "a small dark boot" | A thin strut with no foot; no bench reader saw a boot |
| A reading walker's box 25 px ahead of her leading foot, "to the side of / slightly ahead of" her | The obstacle a full step ahead (45 to 85 px) of her leading toe, squarely on her line |
| A runner and a woman with a pram heading toward each other, "might bump into each other" | No runner and other mover facing each other on one line (within 90 px in depth), and a runner 50 px clear of any mover beside her |
| A duck "swimming close to the float, so the duck might go for the bait or get tangled in the line" | No duck within 60 px of an angler's float or line, and none facing a float |

Left as they were, as notes for the pilot: hoses that are hard to follow at a glance, an angler's upper body over the pond
with his feet on the bank, a dog's red bandana read as a hat or a bow, sizes at the back, goats in a garden or park, and
the older ones (wind under a clear sky, a stall with nobody at it, sweeping a path with nothing on it).

## The isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers
(`vision/isolation_v023.md`, two rounds, 20 cut-outs, ten readers). The bench casts were built from the same cast library
with the variants switched on (`TPDB_PAN`, `TPDB_BEG`, `TPDB_HEAD`); the release cast builds with the chosen ones. Four
frying pans were read twice each: held out by a long handle face-on (B) or tipped to pour (C), they were offered as "the
sprinkler head of a watering can with a very long spout" or "a hose watering wand"; the v0.19 face-on pan on a shorter
handle (E) as "the sprinkler head (rose) of a watering can ... or even a frying pan"; seen from above at a slant, deeper,
on a thicker handle about as long as the pan is wide (D), it led both readings as "a frying pan or saucepan". D is the v0.23
pan. The begging dog sitting up with its paws raised read as begging in all four of its cut-outs, though two readers saw
its lower body "stretched long and flat"; the tail laid behind it is now curled round the haunch. The older man with the
grey kept to the back of his head and a fuller nose was read walking the right way twice; with the grey alone narrowed,
once. The barrow's strut with a small foot was still "a bit like a boot" once; with no foot, "a short gray support leg".

## Design tests

After the bench, the new drawings and the rules of revision 21 were read blind in whole test scenes among other events (`vision/design_tests_v023.md`, two rounds, eight pictures): a garden with the new frying pan beside a dig and a dog walker; a tier-4 park with the older man and his bag, the reading walker, the begging dog, a sleeping cat and the duck feeding; a tier-4 street with the begging dog, the reading walker, a runner, a pram and the square-wheeled bicycle; a playground with a runner and a pram; a park with an angler and a duck; and a garden with the barrow on its strut beside the blocked hose. The pan read as "a frying pan or saucepan rather than a watering can, which seems odd"; the dog "sits up on its hind legs ... begging for the ice cream" in both its pictures; both reading walkers looked "about to trip over" their boxes; and the older man was seen facing the way he walked. Two pictures told stories they were not meant to: a runner whose lane ended just short of a cat stalking a bird behind her line seemed to run "toward the cat and bird, perhaps to stop the cat", and a duck facing the angler's float "may be about to swim over to it". Revision 21 therefore also deepens a runner's lane behind her line and turns every duck away from a float; rebuilt, the runner was no longer tied to the cat and the duck to the float. In the rebuilt playground the runner passed "almost touching" a man with a pram, so a runner also keeps clear of any mover beside her; that last rule was not read again before the set was built.

## Placement revision 21

Every record stores the placement revision it was made with. v0.23 pictures use revision 21, which adds the rules above
to those of revisions 1 to 20: the reading walker's obstacle a full step ahead of her leading toe; no runner and other
mover heading straight at each other on one line, and a runner clear of any mover beside her; a runner's lane deeper
behind her line (220 px, was 150); and no duck at an angler's float or line, nor facing a float. The cast is builder
0.23.0 (the pan, the begging dog and the older man's head); the barrow's leg is drawn by the scene composer.

Building and inspecting the set and the probes found nothing more to fix. The tier-4 garden, park and playground placed again on their v0.22 seeds with the same events, the older man's new profile in two of them, and the tier-4 street came from the showcase pass (attempt 21 of its seed), where in v0.22 it had needed 33 failed seeds. The tier-3 park and playground made no isomorph under revision 21 in 41 tries over ten seeds, so the set's isomorphs are three at tier 2, one at tier 3 and one at tier 4.

The planner's difficulty priors are the calibration measured on the v0.23 templates (`calibration.json`), with f = 0 and
a = 4.47 for every inference and contradiction, as in v0.20 to v0.22. The begging dog's cue salience moved by -0.06 with its new pose; every other template's by at most 0.012.

## The twentieth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 44 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.22.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 |

Across all 65 pictures every scored item had full marks (751 of 755 in v0.22), and none was misread. The three scorers credited between six and twelve items each in full whose description also offered a second reading or left out part of the key's wording ("calling out", "upset", "can't roll"), and listed them; a stricter scorer would have given some of them half points. Unintended oddities fell from 25 to 21 in the set and from 54 to 42 in the probes. What the readers noticed: in the tier-4 park a sleeping cat on the path about 50 px behind a walking man's back foot, "right by his feet, so he could trip over it or step on it"; a small girl on playground equipment "slightly in front of" the slide chute or the seesaw plank (six probes); water from the blocked hose about to spray "into the woman's face"; figures at the back drawn large; and the older ones (goats, wind lines with nothing blowing, a hole in the middle of the lawn, the teenager read as a woman).

The v0.22 failure and half points, and the templates whose drawing or placement v0.23 changed (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.22 | v0.23 | v0.23 meaning items |
|---|---|---|---|
| `pan_watering` | 0.78 (9 items) | 1.00 (9 items) | 1.00 (6) |
| `dog_begs` | 0.94 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `about_to_trip` | 0.96 (12 items) | 1.00 (9 items) | 1.00 (3) |
| `carry_bag` | 1.00 (3 items) | 1.00 (3 items) | — |
| `run` | 1.00 (3 items) | 1.00 (3 items) | — |
| `fishing` | 1.00 (3 items) | 1.00 (3 items) | — |
| `ducks_swimming` | 1.00 (3 items) | 1.00 (3 items) | — |
| `ducks_bread` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |

Every template in the table read in full. The frying pan rose from 0.78 to 1.00 over nine items, its contradiction items read in all three pictures ("a frying pan is a strange thing to water with"); the begging dog from 0.94 to 1.00; and the reading walker from 0.96 to 1.00. The older man carrying a bag was read as an older man in a cap walking the way he faced; one reader gave him "grey hair and beard" for his moustache, none a mask. The runner, the angler and the ducks, whose placement revision 21 changed, read in full with no extra story about them.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 |

Every template was screened in at least three pictures (56 in three, 4 in four, 3 in five, 1 in six), and all 64 pass, as in v0.20. With every item at full marks, the gate no longer separates the templates: the v0.9 retest put its reader variance at about five templates between screens, and the pilot with people is the test of difficulty that can.

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.778 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 5 | 0 (0) | 3 | 0.767 | — | 18 | 0.027 | goat grazing, feed birds, jump |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.779 | — | 15 | 0.047 | photo, read bench |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.771 | — | 14 | 0.032 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_garden_s16118_iso (isomorph of T2_playground_s042) | 9 | 1 (0) | 4 | 0.712 | 0.393 | 18 | 0.042 | sprinkler package, carry box, plant flowers, play catch |
| T2_park_s3022 | 8 | 1 (0) | 4 | 0.710 | 0.364 | 22 | 0.029 | lost balloon, dog sleeping, water flowers, run |
| T2_park_s7109_iso (isomorph of T2_street_s1032) | 8 | 1 (0) | 4 | 0.716 | 0.380 | 19 | 0.032 | sprinkler package, carry box, drink bench, walk dog |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.713 | 0.368 | 18 | 0.048 | lost balloon, push stroller, balloon, wave |
| T2_street_s7109_iso (isomorph of T2_park_s3022) | 8 | 1 (0) | 4 | 0.711 | 0.356 | 20 | 0.052 | ball in tree, water flowers, wave, ice cream |
| T2_playground_s042 | 9 | 1 (0) | 4 | 0.711 | 0.397 | 17 | 0.031 | kite in tree, dog playing, wave, play catch |
| T3_garden_s4013 | 12 | 3 (0) | 5 | 0.641 | 0.305 | 23 | 0.037 | cat stalks bird, paint tracks, kite in tree, birds flying, plant flowers |
| T3_garden_s17102_iso (isomorph of T3_street_s3133) | 12 | 2 (1) | 5 | 0.662 | 0.325 | 20 | 0.041 | kite in tree, bucket hat, kick ball, bird perched, paint fence |
| T3_park_s3023 | 12 | 3 (0) | 6 | 0.638 | 0.282 | 24 | 0.032 | ducks bread, ice cream drop, ball in tree, carry box, walk dog, carry bag |
| T3_street_s3133 | 12 | 2 (1) | 5 | 0.656 | 0.332 | 20 | 0.053 | about to trip, sweep fork, bird perched, ice cream, carry box |
| T3_playground_s2043 | 12 | 2 (1) | 6 | 0.670 | 0.307 | 22 | 0.041 | dog begs, sitting on air, fly kite, sandbox, photo, walk dog |
| T4_garden_s327962 | 18 | 5 (2) | 8 | 0.569 | 0.236 | 29 | 0.044 | paint tracks, lost balloon, cat stalks bird, dog reading, fish in tree, read bench, birds flying, cat sleeping |
| T4_park_s242971 | 18 | 5 (1) | 8 | 0.584 | 0.238 | 29 | 0.035 | ball in tree, lost balloon, bird steals, ducks bread, dog reading, ice cream, carry bag, cat sleeping |
| T4_park_s11111_iso (isomorph of T4_street_s21034) | 18 | 5 (2) | 8 | 0.588 | 0.213 | 33 | 0.039 | windy hat, ice cream drop, bird steals, dog reading, pan watering, bird perched, carry box, picnic |
| T4_street_s21034 | 18 | 5 (2) | 8 | 0.576 | 0.215 | 27 | 0.056 | windy hat, ice cream drop, bird steals, dog reading, bucket hat, carry bag, jump, birds flying |
| T4_playground_s391818 | 18 | 5 (2) | 9 | 0.559 | 0.227 | 27 | 0.043 | ball in tree, bird steals, lost balloon, dog reading, sitting on air, jump, dog sleeping, birds flying, ice cream |

Isomorph pairs differ by at most 0.012 in content and 0.012 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.4 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.4 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.6 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.1 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^23.0 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 440,799 | 220 | 70,459 | 10^17.2 |
| street | 4 | 7,157,106 | 330 | 947,071 | 10^22.3 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.9 |
| playground | 4 | 10,690,061 | 232 | 1,352,842 | 10^21.9 |

In all 440,902,571 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

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
| `assets/validate_assets.py` | Checks for every rendered variant |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.23 redraws the frying pan, the begging dog and the older man's head, and keeps the bench variants behind `TPDB_PAN`, `TPDB_BEG` and `TPDB_HEAD` |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out023/` | The 18 `.blend` families (builder 0.23.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib023/` | Every variant the generated scenes and probes use, carried over from `lib022` where the cast did not change or rendered from `out023` |
| `assets/cast/gallery023/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.23.0, placement revision 21); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`) and the barrow's two bench legs (`LEG23`); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.23 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v023.md` and their rounds; none in v0.21), flaw lists (`flaws_v04.md` to `flaws_v023.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v023.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all twenty screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/cycle/` | How each release is made, step by step, and the scripts that build, search, verify, prune and screen a release (new in v0.23, so that a fresh session can make the next one) |

## How to run

```bash
pip install bpy==5.2.3 cairosvg pillow numpy scipy wordfreq==3.1.1 jsonschema --break-system-packages

cd assets/cast && python build_cast.py out023 && cd ../..           # build the cast (about a minute)
cd assets/cast && python gapcheck.py out023 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s3023.json --out /tmp/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PAN=D> python vision/isolation_bench.py /tmp/bench panD_1 begA_1 strut_1   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v023   # then describe and score: vision/screen_prompts.md
python vision/summarize_screen.py vision/v04:<v0.4 scenes> vision/v05:<v0.5 scenes> vision/v06:<v0.6 scenes,probes> \
    vision/v07:<v0.7 scenes,probes> vision/v08:<v0.8 scenes,probes> vision/v09:<v0.9 scenes,probes> \
    vision/v010:<v0.10 scenes,probes> vision/v011:<v0.11 scenes,probes> vision/v012:<v0.12 scenes,probes> \
    vision/v013:<v0.13 scenes,probes> vision/v014:<v0.14 scenes,probes> vision/v015:<v0.15 scenes,probes> \
    vision/v016:<v0.16 scenes,probes> vision/v017:<v0.17 scenes,probes> vision/v018:<v0.18 scenes,probes> \
    vision/v019:<v0.19 scenes,probes> vision/v020:<v0.20 scenes,probes> vision/v021:<v0.21 scenes,probes> \
    vision/v022:<v0.22 scenes,probes> vision/v023:scenes,probes
python vision/gate.py vision/v023 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery023 --old-gallery <v0.22 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.23 --single   # the release as one zip, tpdb_v0.23.zip
```

The release is one zip, `tpdb_v0.23.zip`, about 157 MB. Google Drive does not virus-scan a file over 100 MB, so it asks
to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that.
`package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the
same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.22 record rebuilds with the v0.22 package.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- No template falls under the legibility gate after the v0.23 screen, and no item of the 65 pictures fell short of full
  marks: 64 of 64 pass, as in v0.20. The screen is at its ceiling and no longer separates the templates. `vision/flaws_v023.md`
  lists the oddities the readers reported for v0.24.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are at the ceiling: across 65 pictures all 729 scored items had full marks (4 of 755 fell short in v0.22). AI readers describe exhaustively, so the screen cannot rank templates by difficulty;
  that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, and v0.23 scorers six to twelve, enough to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 20 make them harder (walkers' and runners'
  lanes, pointing lines, feet off benches and off other events' things, the photographer's line of sight, the waver's
  clear hand, body gaps, the gap from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear
  past a reading walker's obstacle, jumpers in the front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float). The
  tier-4 garden, park and playground came again on their v0.22 seeds, with the same events, and the tier-4 street from
  the showcase pass (attempt 21 of its seed; in v0.22 the street needed 33 failed seeds before one placed).
  Their records rebuild them exactly.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures.
- The stuck girl on the seesaw always calls out, but no reader mentioned it: the tilt, the man's weight and
  the motion lines at her feet carry the reading.
- The body check (`assets/cast/gapcheck.py`) finds parts that come apart, not parts that pass through one
  another: a hand inside a hip or a lobe of skirt inside the bell is allowed, and only the outline drawn
  in the render shows whether the join looks right.
- The wind reaches the hat, the washing, an empty swing, the tree and the sky, but not hair or clothes, nor the
  bushes and flowers (three v0.19 probe readers noticed): the cast is posed and rendered in 3D, and a blowing
  fringe or skirt would be a new rig.
- The isolation bench reads one template cut out of its picture. A visual that reads alone can still be
  misread among other events, so the bench comes before the test scenes and the screen, never instead of them.
- The planner's priors come from the v0.23 calibration, with f = 0 and a at its centre for every inference and
  contradiction, as in v0.20 to v0.22: the begging dog's cue salience moved by -0.06 (its new pose), every other
  template's by at most 0.012.
- Exact rebuilds hold within a release: the v0.23 cast (builder 0.23.0) and placement rules (revision 21) change how the
  pan, the begging dog and the older man look and where events go, so a v0.22 record rebuilds with the v0.22 package.
- Every variant comes from the v0.23 cast (builder 0.23.0, `out023`): the variants of the families and poses v0.23 did
  not change were carried over from `lib022`, the rest rendered anew; the library keeps only the 390 variants the v0.23
  set and probes use. The bench variants (`TPDB_PAN`, `TPDB_BEG`, `TPDB_HEAD`) stay in the cast library, off by default.
- Age of acquisition is recorded at weight 0, so it moves nothing until the pilot's pre-registered test says it
  should. The bundled ratings are a verbatim excerpt of Kuperman et al. (2012) under CC BY-NC-ND 3.0, taken from a
  copy in the lftk package; they have not yet been checked against the original file at crr.ugent.be.
- Key words follow one rule (the word the first accepted answer names: an action's verb, or the thing that names
  it), applied by hand in v0.20 and unchanged since; a key that is itself an accepted answer was left alone.
- The sleeping cat, 1.4 times its v0.17 size, read as "small" in one v0.18 probe and drew no remark in its four
  v0.19 pictures; drawn larger, the standing and stalking cats would come out as big as the small white dog.
- Twenty-seven actions in the cast are used by no template; they are kept for later templates and left
  out of the gallery and the screen, so they have never been read blind.
- Edge density is not part of the isomorph rule. Street pictures stay the busiest, so a street
  isomorph of a park or playground picture carries more visual detail at the same object count.
- The top third of park and playground pictures is still mostly sky.
- A filler closer than 24 px to the picture's side edge is now moved 30 px inside it, and no reader said one
  was cut off; the sun can still sit partly off the top edge, where the backdrop draws it.
- The tier-3 park and playground made no isomorph under revision 21 (41 tries over ten seeds), so the v0.23 isomorphs are three at tier 2,
  one at tier 3 and one at tier 4.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
