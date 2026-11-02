# TPDB v0.21: the worker out of the garden, the bowl by the dog, heads clear of the washing and the cattails, read an eighteenth time

v0.20 ended with a seventeenth blind legibility screen: no item in 65 pictures was misread, 744 of 746 scored items had
full marks, and all 64 templates passed the gate for the first time. Two items took a half point, each in one picture: a
girl crying beside the dropped ice cream without being said to have dropped it, and the square wheel offered as "a normal
round wheel inside a square frame". The readers also reported small oddities, none of them misreadings: a worker in a hi-vis
vest painting or pointing in a home garden; a dog bowl far from any dog; a yellow shirt on the washing line read as part
of the clothes of the woman in front of it, and washing hung in front of a fence being painted; a spare hose reel beside a
watering can and a can's water landing at the front edge of the bed; a man at the pond's rim with the cattails at his hip;
a reading man and a dog walker overlapping in the busy street; and a kicked ball heading for the sandcastle.

v0.21 works through that list. Nothing in it is a drawing that reads poorly, so no visual was redrawn and there was no
isolation bench this time: every change is a placement rule (revision 19), read blind in whole test scenes among other
events, then the set was regenerated and screened an eighteenth time.

None of the v0.20 oddities that revision 19 addressed came back in the eighteenth screen: no worker's vest in a garden, no dog bowl away from a dog, no head among the washing, no spare hose reel or can beside someone watering, no figure in the cattails, no walkers on each other's shoulders, no kick at the sandpit. 738 of 744 scored items had full marks, and the probes' unintended oddities fell by half (68 to 34). But one item of the set was misread, the first since v0.11: in the tier-4 street a woman watering a planter box with a frying pan, the pan held up against a grey shop door, read as "a grey watering can", so its contradiction was missed; in the same picture a teenager jumping for joy read as standing with his arms up. With a ladder that one probe reader could not tell standing from lying flat, three templates fall short of the gate, each of them read in full in v0.20 and in two of its three pictures here: 61 of 64 pass (64 in v0.20). The set scored 0.989 over all items (0.998 in v0.20); its inferences rose to 1.00 and its oddities fell from 1.2 to 1.1 per picture. `vision/flaws_v021.md` lists the three, and the square wheel's second "round wheel inside a square frame", for v0.22.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Python
`bpy`, Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`.

## The oddities fixed

| What the v0.20 readers saw | v0.21 |
|---|---|
| A worker in a hi-vis vest and cap painting the fence or pointing at the sky in a home garden, "out of place" (three probes) | Nobody in the worker's hi-vis vest and cap in a home garden (he still works in the street and the park) |
| "A full food bowl with no pet near it" (one set picture, four probes) | The dog bowl only with a dog or cat standing near it |
| A yellow shirt on the line behind a woman's head read as part of her clothes; jeans on the line "in front of the freshly painted fence" | No head of anyone in front of the hanging washing; beside someone pinning up a shirt, only the jeans already on the line; no washing on the line while the fence is being painted |
| A spare hose reel beside a watering can; a can's water landing "at the front edge of the bed" | No hose reel in a picture with someone watering by can or by the pan, and no spare can beside a hose; the can's stream ends well inside the bed, not at its front edge |
| A man "overlaps the right edge of the pond", the cattails at his hip; a cattail behind a head; a runner "very close to the pond edge" | People and animals clear of the cattails, and their feet clear of the pond's rim |
| In the busy street a reading man and a dog walker "overlap closely" (60 px apart in depth); a goat behind a man "attached to his shoulder" | A figure's head and shoulders kept clear of anyone of another event up to 80 px apart in depth (was 40) |
| A kicked ball "heading for the sandcastle" | The kick's line clear of the sandpit and of anyone else on the ground |

Left as they were, as notes for the pilot: the dropped ice cream's owner (read in full in three of four pictures), the
square wheel (read in full in two of three and noticed as odd in all three), motion read oddly (a seesaw "almost level",
swing lines with straight chains), extra stories readers told, gaze and facing (the cast is turned three-quarters by
design), sizes at the back, and the older ones (a stall with nobody at it, goats, a pram on the grass, the square-wheeled
bicycle standing on its own).

## Design tests

The rules were read blind in seven whole test scenes among other events (`vision/design_tests_v021.md`): a garden with the fence being painted, someone watering by can and a dog playing; a garden with the washing being hung, a dig and a kick; a busy park by the pond with the duck feeding, a runner, the bird feeding, a dog walker and a photographer; a park with someone fishing; a playground with a kick beside the sandpit; a busy street; and a busy garden with the blocked hose. Every rule read as meant. No reader saw a worker's vest in the garden, a hose reel or a spare can beside someone watering, a bowl away from a dog, a head among the hung washing ("a man ... stretching up to peg a white T-shirt onto a washing line, where a pair of blue jeans already hangs"), a figure in the cattails, walkers on each other's shoulders, or a kick at the sandpit ("heading off to the right, away from the other children"). The can's water fell "onto the middle of the flower bed". Two readers said people at the pond's front edge overlap its outline, each adding that their feet are on the grass, "so they read as standing at the bank". Nothing in the test scenes called for another change; one test scene had to be split, since duck feeding and fishing together in a tier-4 park placed in none of four seeds.

## Placement revision 19

Every record stores the placement revision it was made with. v0.21 pictures use revision 19, which adds the rules above
to those of revisions 1 to 18: no one in the worker's hi-vis vest in the garden; the dog bowl only by a dog or cat; heads clear of
the hanging washing, the short line of jeans beside someone hanging a shirt, and no washing while the fence is painted; no
hose reel beside watering by can or pan, no watering can beside a hose, and the can's stream well inside the bed;
people and animals off the cattails and the pond's rim; heads and shoulders clear of figures of other events up to 80 px
apart in depth; and the kick's line clear of the sandpit and of anyone on the ground. Building the set added four more
(below): no watering by can in a picture with any hose, nobody in front of a sprinkler's spray or its box, no hose reel or
spare can beside the sprinkler, and no washing line beside someone hosing the flowers, whose hose is now drawn in front of
the bed.

Building and inspecting the set and the probes found four more things, all fixed before the screen. The first build stopped on a garden that paired watering by can with the blocked hose: dropping the reel from beside the can had left the hose with no reel, so watering by can now never shares a picture with a hose. The first tier-4 park had a goat grazing just in front of a sprinkler's arcs, as if in the spray; nobody may now stand in front of the spray or its box, and the park was searched again. Two garden probes had a hose reel and a spare watering can beside the sprinkler, whose own hose runs off the picture; they were rebuilt without either. And hosing the flowers had stopped placing at all: its hose was a fifth hidden behind the flower bed, and with heads kept clear of the washing there was nowhere else for the waterer to stand, so the hose is now drawn in front of the bed and no washing hangs beside it. Hosing and fishing were then in no screened picture, so each went into three probes beside the templates of the probes they replaced, keeping the screen at 65 pictures.

The planner's difficulty priors are the calibration measured on the v0.21 templates (`calibration.json`), with f = 0 and
a = 4.47 for every inference and contradiction, as in v0.20. The duck feeding's cue salience moved by +0.026 and the frying pan's by +0.02 (measured in 15 scenes instead of 12); every other template's by at most 0.01.

## The eighteenth blind screen

Nine fresh readers, who had never seen the key, described every picture of the new set and 44 probe pictures; three separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.20.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 |
| Unintended oddities per picture | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 |

Across all 65 pictures 6 of 744 scored items fell short of full marks (2 of 746 in v0.20): four half points, and a zero and a misread on the same frying pan. In the set, all in the tier-4 street: the pan, held up face-on at a raised planter box against the slate-grey shop door, read as "a grey watering can" ("a grey can or pot", "nothing looks physically impossible"), its stream "running down the side of the planter"; and a teenager jumping for joy in front of the fruit stall, his feet about 40 px above his shadow, read as standing "with both arms up, smiling", "cheering, celebrating, stretching or dancing". In the probes, a ladder on the open grass, its top just below the foot of a lamp post, was "standing up at a lean ... or lying flat" (two half points), and the square-wheeled wheelbarrow was once more "a square dark frame with a spoked wheel inside it". One scorer gave no half point at all and listed nine hedged items it credited in full. Unintended oddities fell from 26 to 24 in the set and from 68 to 34 in the probes. What the readers noticed: a sprinkler's hose rising "straight up out of the bottom edge like a stiff pipe" (two probes); hoses hard to follow near the hand or under a dog's paws (three probes); extra trip stories (a boy with an ice cream by a wheelbarrow's handles, a reading walker by a sleeping cat or a bicycle, a runner heading for the flower bed); slide chutes ending above the grass; and the older ones (goats, leaves under no tree, the tilted empty swing, a runner in a dress).

The two templates with a v0.20 half point and the templates whose placement revision 19 changed for its oddities (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.20 | v0.21 | v0.21 meaning items |
|---|---|---|---|
| `ice_cream_drop` | 0.97 (16 items) | 1.00 (12 items) | 1.00 (3) |
| `square_wheel` | 0.94 (9 items) | 0.97 (15 items) | 0.95 (10) |
| `paint_fence` | 1.00 (6 items) | 1.00 (6 items) | — |
| `rain_coming` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `dog_playing` | 1.00 (3 items) | 1.00 (3 items) | — |
| `hang_laundry` | 1.00 (3 items) | 1.00 (3 items) | — |
| `water_flowers` | 1.00 (4 items) | 1.00 (3 items) | — |
| `blocked_hose` | 1.00 (12 items) | 1.00 (12 items) | 1.00 (3) |
| `hose_water` | 1.00 (3 items) | 1.00 (3 items) | — |
| `sprinkler_package` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `ducks_bread` | 1.00 (9 items) | 1.00 (9 items) | 1.00 (3) |
| `fishing` | 1.00 (3 items) | 1.00 (3 items) | — |
| `walk_dog` | 1.00 (4 items) | 1.00 (3 items) | — |
| `read_bench` | 1.00 (3 items) | 1.00 (3 items) | — |
| `kick_ball` | 1.00 (3 items) | 1.00 (3 items) | — |

The two v0.20 half points read better: the dropped ice cream at 1.00 over 12 items in three pictures (0.969 in v0.20), the square wheel at 0.967 over 15 items in five (0.944), its one half point the same "round wheel inside a square frame" reading as in v0.20. Every template whose placement revision 19 changed read with full marks: the painter with no worker's vest and no washing behind the boards, the washing being hung beside the jeans alone, the watering can with no reel beside it, the hose drawn in front of the flower bed, the blocked hose with no spare can, the sprinkler with nobody in front of its spray, the duck feeding and the fishing off the cattails, the dog walker and the reader off other figures' shoulders, and the kick clear of the sandpit.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 |

Every template was screened in at least three pictures (54 in three, 4 in four, 4 in five, 1 in six, 1 in seven), and 61 of 64 pass. The three that fall short each read in full in v0.20 and in two of their three pictures here: the frying pan (one misread), the jumper (one half point) and the ladder leaning on nothing (two half points in one probe). About five templates of the gate's movement between screens is reader variance (the v0.9 retest); two of the three, though, have a cause in their picture to fix (the pan against a grey door, the jumper's small gap above his shadow in front of the stall), and the ladder's open-grass probe gives the bench a case to try.

Templates that did not pass (`vision/flaws_v021.md` gives what the readers saw and the next fix):

| Template | v0.21 mean | Pictures | Misreads |
|---|---|---|---|
| `pan_watering` | 0.78 (9 items) | 3 | 1 |
| `jump` | 0.83 (3 items) | 3 | 0 |
| `ladder_nothing` | 0.89 (9 items) | 3 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 6 | 0 (0) | 3 | 0.778 | — | 14 | 0.038 | cat sleeping, drink bench, rake |
| T1_park_s021 | 6 | 0 (0) | 3 | 0.766 | — | 16 | 0.026 | goat grazing, feed birds, jump |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.779 | — | 15 | 0.047 | photo, read bench |
| T1_playground_s041 | 4 | 0 (0) | 2 | 0.771 | — | 14 | 0.032 | sandbox, kick ball |
| T2_garden_s012 | 8 | 1 (0) | 4 | 0.711 | 0.393 | 18 | 0.039 | dog wants walk, dog playing, sweep, play catch |
| T2_park_s3022 | 8 | 1 (0) | 4 | 0.710 | 0.364 | 22 | 0.029 | lost balloon, dog sleeping, water flowers, run |
| T2_park_s12118_iso (isomorph of T2_playground_s4042) | 8 | 1 (0) | 3 | 0.720 | 0.401 | 17 | 0.026 | dog begs, feed birds, balloon |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.713 | 0.368 | 18 | 0.048 | lost balloon, push stroller, balloon, wave |
| T2_street_s7109_iso (isomorph of T2_park_s3022) | 8 | 1 (0) | 4 | 0.711 | 0.356 | 20 | 0.052 | ball in tree, water flowers, wave, ice cream |
| T2_playground_s4042 | 8 | 1 (0) | 3 | 0.710 | 0.403 | 17 | 0.034 | cat stalks bird, push stroller, bird perched |
| T3_garden_s4013 | 12 | 3 (0) | 5 | 0.641 | 0.305 | 23 | 0.037 | cat stalks bird, paint tracks, kite in tree, birds flying, plant flowers |
| T3_garden_s12102_iso (isomorph of T3_street_s133) | 12 | 3 (1) | 6 | 0.642 | 0.326 | 22 | 0.043 | cat stalks bird, kite in tree, square wheel, walk dog, plant flowers, goat grazing |
| T3_park_s3023 | 12 | 3 (0) | 6 | 0.638 | 0.282 | 24 | 0.032 | ducks bread, ice cream drop, ball in tree, carry box, walk dog, carry bag |
| T3_street_s133 | 12 | 3 (1) | 6 | 0.641 | 0.329 | 20 | 0.054 | dog begs, rain coming, square wheel, ice cream, bird perched, balloon |
| T3_street_s8104_iso (isomorph of T3_playground_s11043) | 12 | 2 (0) | 5 | 0.658 | 0.337 | 21 | 0.052 | dog begs, ball in tree, ice cream, bird perched, birds flying |
| T3_playground_s11043 | 12 | 2 (0) | 5 | 0.657 | 0.354 | 21 | 0.039 | seesaw heavy, about to trip, fly kite, birds flying, cat sleeping |
| T4_garden_s230971 | 18 | 5 (1) | 8 | 0.569 | 0.236 | 28 | 0.046 | cat stalks bird, lost balloon, ball in tree, blocked hose, sitting on air, hang laundry, birds flying, goat grazing |
| T4_garden_s13111_iso (isomorph of T4_park_s242971) | 18 | 5 (1) | 8 | 0.568 | 0.227 | 27 | 0.050 | cat stalks bird, sprinkler package, ball in tree, bird steals, square wheel, swing, rake, goat grazing |
| T4_park_s242971 | 18 | 5 (1) | 8 | 0.570 | 0.233 | 27 | 0.034 | ducks bread, ball in tree, about to trip, bird steals, square wheel, ice cream, carry bag, cat sleeping |
| T4_street_s4034 | 18 | 5 (1) | 8 | 0.599 | 0.232 | 26 | 0.056 | ice cream drop, about to trip, ball in tree, bird steals, pan watering, feed birds, carry bag, jump |
| T4_playground_s117095 | 18 | 5 (2) | 9 | 0.550 | 0.248 | 26 | 0.043 | bird steals, about to trip, kite in tree, dog reading, square wheel, dog sleeping, birds flying, balloon, carry box |

Isomorph pairs differ by at most 0.010 in content and 0.017 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,447 | 9 | 1,905 | 10^10.0 |
| garden | 2 | 26,666 | 27 | 11,977 | 10^12.7 |
| garden | 3 | 2,497,856 | 296 | 338,691 | 10^18.3 |
| garden | 4 | 78,307,591 | 565 | 6,485,763 | 10^23.4 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 46,656 | 24 | 20,579 | 10^11.6 |
| park | 3 | 5,825,387 | 236 | 1,027,898 | 10^17.4 |
| park | 4 | 335,129,874 | 376 | 44,950,328 | 10^22.8 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,433 | 24 | 2,952 | 10^11.8 |
| street | 3 | 480,097 | 220 | 78,700 | 10^17.4 |
| street | 4 | 8,526,054 | 330 | 1,143,561 | 10^22.4 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.5 |
| playground | 3 | 749,671 | 183 | 113,624 | 10^17.9 |
| playground | 4 | 10,690,061 | 232 | 1,352,842 | 10^21.9 |

In all 442,310,817 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

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
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; unchanged since v0.20 |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out021/` | The 18 `.blend` families (builder 0.20.0, unchanged), their render configs and `cast_catalog.json` |
| `assets/cast/lib021/` | Every variant the generated scenes and probes use, carried over from `lib020` or rendered from `out021` where first needed |
| `assets/cast/gallery021/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (170, all pass the validator) |
| `scenegen/` | The generator (0.21.0, placement revision 19); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.21 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v020.md` and their rounds), flaw lists (`flaws_v04.md` to `flaws_v021.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v021.md`), screen tools and prompts (`screen_prompts.md`), the keys, descriptions and scores of all eighteen screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |

## How to run

```bash
pip install bpy==5.2.3 cairosvg pillow numpy scipy wordfreq==3.1.1 jsonschema --break-system-packages

cd assets/cast && python build_cast.py out021 && cd ../..           # build the cast (about a minute)
cd assets/cast && python gapcheck.py out021 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s3023.json --out /tmp/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
python vision/isolation_bench.py /tmp/bench pail_d drink_c swing_b   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v021   # then describe and score: vision/screen_prompts.md
python vision/summarize_screen.py vision/v04:<v0.4 scenes> vision/v05:<v0.5 scenes> vision/v06:<v0.6 scenes,probes> \
    vision/v07:<v0.7 scenes,probes> vision/v08:<v0.8 scenes,probes> vision/v09:<v0.9 scenes,probes> \
    vision/v010:<v0.10 scenes,probes> vision/v011:<v0.11 scenes,probes> vision/v012:<v0.12 scenes,probes> \
    vision/v013:<v0.13 scenes,probes> vision/v014:<v0.14 scenes,probes> vision/v015:<v0.15 scenes,probes> \
    vision/v016:<v0.16 scenes,probes> vision/v017:<v0.17 scenes,probes> vision/v018:<v0.18 scenes,probes> \
    vision/v019:<v0.19 scenes,probes> vision/v020:<v0.20 scenes,probes> vision/v021:scenes,probes
python vision/gate.py vision/v021 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery021 --old-gallery <v0.20 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.21 --single   # the release as one zip, tpdb_v0.21.zip
```

The release is one zip, `tpdb_v0.21.zip`, about 144 MB. Google Drive does not virus-scan a file over 100 MB, so it asks
to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that.
`package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the
same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.20 record rebuilds with the v0.20 package.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Three templates fall under the legibility gate after the v0.21 screen, each of them read in full in v0.20 and in two of its
  three v0.21 pictures: the frying pan, misread once as "a grey watering can" in the tier-4 street (held up against a
  grey shop door at a raised planter), the jumper, read as standing with arms up in front of the fruit stall, and the
  ladder leaning on nothing, "standing ... or lying flat" in one probe. 61 of 64 pass. `vision/flaws_v021.md` gives what
  the readers saw and the list for v0.22.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are at the ceiling: across 65 pictures only 6 of 744 scored items fell short of full marks (four half points,
  and one zero and one misread on the same frying pan). AI readers describe exhaustively, so the screen cannot rank templates by difficulty;
  that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven and a v0.21 scorer nine, enough to move a template across the gate.
- Tier-4 pictures are the hardest to place, and revisions 14 to 19 make them harder (walkers' and runners'
  lanes, pointing lines, feet off benches, the photographer's line of sight, the waver's clear hand, body gaps, the
  gap from thin parts, heads clear of figures up to 80 px apart in depth). The tier-4 garden, park and playground
  pictures came from wide seed searches with no template-variety steering, as in v0.15 to v0.20: the garden on the
  fourth seed of up to 40 casts each, the park on the third seed of a second search (searched again after inspection: in
  the first, a goat grazed in front of the sprinkler's arcs), and the playground on the v0.20 seed, which placed again;
  the tier-4 street came from the showcase pass. Their records rebuild them exactly. Some pairs got harder in revision 19: duck feeding and fishing
  together in a tier-4 park placed in none of four seeds (one of four under revision 18).
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
- The planner's priors come from the v0.21 calibration, with f = 0 and a at its centre for every inference and
  contradiction, as in v0.20: the duck feeding's cue salience moved by +0.026, the frying pan's by +0.02 (measured in 15
  scenes instead of 12), every other template's by at most 0.01.
- Exact rebuilds hold within a release: the v0.21 placement rules (revision 19) and the hose drawn in front of the flower
  bed change where events go and what the planner picks, so a v0.20 record rebuilds with the v0.20 package.
- Every variant comes from the v0.20 cast unchanged (builder 0.20.0, copied to `out021`); the library keeps only the
  328 variants the v0.21 set and probes use.
- Age of acquisition is recorded at weight 0, so it moves nothing until the pilot's pre-registered test says it
  should. The bundled ratings are a verbatim excerpt of Kuperman et al. (2012) under CC BY-NC-ND 3.0, taken from a
  copy in the lftk package; they have not yet been checked against the original file at crr.ugent.be.
- Key words follow one rule (the word the first accepted answer names: an action's verb, or the thing that names
  it), applied by hand in v0.20 and unchanged in v0.21; a key that is itself an accepted answer was left alone.
- The sleeping cat, 1.4 times its v0.17 size, read as "small" in one v0.18 probe and drew no remark in its four
  v0.19 pictures; drawn larger, the standing and stalking cats would come out as big as the small white dog.
- Twenty-seven actions in the cast are used by no template; they are kept for later templates and left
  out of the gallery and the screen, so they have never been read blind.
- Edge density is not part of the isomorph rule. Street pictures stay the busiest, so a street
  isomorph of a park or playground picture carries more visual detail at the same object count.
- The top third of park and playground pictures is still mostly sky.
- A filler closer than 24 px to the picture's side edge is now moved 30 px inside it, and no reader said one
  was cut off; the sun can still sit partly off the top edge, where the backdrop draws it.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
