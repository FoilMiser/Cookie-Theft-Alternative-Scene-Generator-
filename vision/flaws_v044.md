# v0.44 blind screen: what it found (the work list for v0.45)

The v0.44 screen read the set's 21 pictures and 61 probes with the prompts of v0.39 (`screen_prompts.md`). There were eleven readers of seven or eight pictures and four scorers of 20 or 21. After the screen, three probes were rebuilt and read again by a fresh reader and scorer each (below). The oddity tally is by angle, as in v0.39. Keys, descriptions and scores are in `v044/`; the three pictures' first descriptions are in `v044/first/`.

v0.44 worked three lists: `flaws_v043.md` and Sam's two notes on the v0.43 figures (`tpdb_work/figure-fixes-v043.md`, the screen's findings ranked, and `tpdb_work/figure-review-v043.md`, a review of every v0.43 render). The bench, in whole pictures this time (`isolation_v044.md`), took these into the cast (builder 0.44.0):
- **the reading dog** sitting up again, its forepaws raised to eye level to hold its paper's top edge, its head bowed about 25 degrees to the page, in round reading glasses;
- **the cat's** ears turned so their triangles show in profile, its muzzle further forward, its whiskers forward as well as out;
- **the goat's** beard a short blunt tuft; **the dog's** nose set into its muzzle;
- **props** in colours of their own: a bag, a watering can or a balloon whose hue is within 20 degrees of a saturated garment its holder wears takes another colour;
- **the run** off the ground, **the sand spade's** blade on its handle, **the nozzle** inspected face up, **the call** from the stuck seesaw with a hand at the mouth, **the content face** as the happy arcs.

Placement revision 42 adds six rules:
- the reading dog's paper hangs from its paws by the top edge, tilted, its far side sagging, clear of the ground; the dog is in the front half of the picture, off the path, 400 px from any other dog, and always the tan dog, so never with the dog by the door;
- the waiting dog's lead is yellow and hangs from its mouth to a loop clear of the ground;
- the goat grazes in the park only, and never at 135;
- the stalking cat keeps its own length from a tree;
- the lost balloon floats high on a long string, its curled end clear of everything;
- the upward water tapers as it rises, and is never in the street.

Every dog, cat, goat and person is drawn anew, so no picture is identical to v0.43's, and there is no retest this time.

## Headline (the 21 pictures of the set)

| | v0.40 (21) | v0.41 (21) | v0.42 (21) | v0.43 (21) | v0.44 (21) |
|---|---|---|---|---|---|
| Things | 0.991 | 1.00 | 0.991 | 0.952 | 0.991 |
| Actions | 0.996 | 1.00 | 1.00 | 0.996 | 0.996 |
| Inferences | 0.986 | 0.958 | 0.939 | 1.00 | 0.971 |
| Contradictions | 1.00 | 1.00 | 0.942 | 0.712 | 1.00 |
| All items | 0.993 | 0.995 | 0.984 | 0.955 | 0.991 |
| Misread items | 0 of 287 | 0 of 287 | 0 of 290 | 1 of 290 | 0 of 286 |
| Readers' remarks per picture (all screened pictures) | 3.04 | 3.17 | 3.05 | 3.12 | 3.27 |
| Oddities per picture, as logged by the scorers | 0.5 (at most 3) | 0.4 (at most 3) | 0.7 (at most 3) | 1.1 (at most 3) | 0.7 (at most 3) |

The set's contradictions are back to 1.00 from 0.712: the reading dog, in five of the set's pictures, read in full.

Across all 82 pictures, 920 of the 927 scored items had full marks, and one was misread. The 7 under full marks:
- **Three on the ice cream, one in each of three probes of the girl in pink walking with one in profile.** At first her scoop was cream (the colour rule, against her pink dress): "something small and white" at her mouth, "a sweet or snack she is eating, a dandelion clock she is about to blow" (6, 32, 49), three half marks. After the screen the scoop was put back to pink, as in v0.43, the three pictures were rebuilt, and fresh readers read them again: "a small pink thing up near her mouth or chin, as if she is eating a sweet or smelling something" (6), "something small and pink up to her mouth or nose", a flower or a lollipop (32, the misread), "a small pink object in it, as if she is eating a sweet, smelling a small flower or blowing a kiss" (49). The colour was not the cause: at her size, walking in profile, the cone is too small to be one.
- **The thief bird (23):** "could be read as about to steal it or just perching".
- **The camera (23):** "a camera (or binoculars)".
- **The lost balloon (44):** "holding the string by its very tip, or has just let go and is reaching for it".
- **The clouds (48):** not mentioned.

The scorers gave one, three, three and no items under full marks, of 250, 225, 232 and 220; the three re-reads one each, of 10, 11 and 10.

**What the full marks rest on.** The scorers' notes mark 7 items they credited in full where the free description commits and the unsure section adds another reading (7 in v0.43). Halved, they take no other template under the gate (`tpdb_work/strict44.py`).

## The v0.43 list and Sam's notes

| v0.43 reading, or the notes' item | v0.44 result |
|---|---|
| R1, notes' item 1, review item 7: `dog_reading` 0.533, lying "on an open newspaper", one misread | **1.00 in five pictures** (15 items). Sitting up in glasses with its paper hung from its paws, "holding an open newspaper with its front paws, as if reading" in all five; the glasses named twice, "round glasses" (21, 23). Its paper "floats slightly in front of the puppy's paws rather than resting in them" twice (1, 5), an oddity |
| R2, notes' item 2: `dog_wants_walk` 0.833, its red lead "attached" to the red collar | **1.00 in five pictures** (10 items). The yellow lead hanging from its mouth: "holds a yellow lead in its mouth, as if it wants a walk" (20) |
| R3, notes' item 4: `photo` 0.90 | **0.90 again** (5 pictures), once more "a camera (or binoculars)" (23) |
| O1, notes' item 3: the goat unusual in gardens, a sheep from behind | **In the park only, never at 135:** tethered in all four pictures, "a little unusual" or "unusual but not impossible" in all four, never a sheep. Its beard, a short tuft now, was never mentioned |
| Review item 1: props the colour of the clothes behind them | The bag, can and balloon take another colour. The scoop left the rule after the screen (above) |
| Review items 2, 6, 13: the run, the sand spade, the call from the seesaw | `run` 1.00 (3 pictures); `sandbox` 1.00 (3); `seesaw_heavy` 1.00 (3), the girl "calling to him" |
| Review items 3, 4: the cat's ears, the cat by the tree | `cat_stalks_bird` 1.00 (3 pictures). Three profile cats drew an oddity each: "a small white shape at the cat's chest/front paws", its legs "folded underneath it in a slightly tangled way", a kite string at its front legs |
| Review item 5: the lost balloon's string | 0.944 (3 pictures), one picture read two ways (44) |
| Review item 8: the upward water | `water_upward` 1.00 (3 pictures), never in the street now |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.40 | v0.41 | v0.42 | v0.43 | v0.44 |
|---|---|---|---|---|---|
| Pass | 64 | 64 | 63 | 62 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 0 | 1 | 2 | 1 |

Every template was screened in at least three pictures. By count: 41 in three, 11 in four, 5 in five, 3 in six, 2 in seven, 1 in nine and 1 in thirteen, with 457 scored items behind the verdicts.

**The one failure.** `ice_cream` is at 0.846 (13 items, 13 pictures), with the misread, all three marks the girl in pink walking with her ice cream in profile, the pose all three of her probes drew. It read 1.00 in v0.43, in 19 items.

The lowest that pass:
- `photo` (0.90, 5 items, 5 pictures);
- `lost_balloon` (0.944, 9 items, 3 pictures);
- `bird_steals` (0.967, 15 items, 5 pictures).
Every other template reads 1.00.

**Per angle** (`v044/gate_yaw.json`), all 24 (template, angle) pairs pass.

## After the screen

The gate first failed `ice_cream` at 0.885, on three half marks, all the girl in pink's cream scoop. The colour rule (`TPDB_PROP44`) had made it cream against her pink dress; pink, as in v0.43, read in full there. So the scoop left the rule and is pink for everyone. Only her ice-cream variants changed: her figure was rebuilt, its four ice-cream renders and the gallery's one rendered again, and the three probes that draw her ice cream (pictures 6, 32 and 49) regenerated over their files. Every record still rebuilds identical, and the library passes the validator. A fresh reader and scorer read each picture again (`scores_e.json` to `scores_g.json`), and the re-reads replace the first scores: two half marks and a misread, where the first reads gave three half marks. The size of the ice cream, not its colour, is what failed.

## What reads least well (the v0.45 list)

| # | Template | v0.44 | What the readers saw | Fix for v0.45 |
|---|---|---|---|---|
| R1 | `ice_cream` | 0.846 (13 items, 13 pictures), one misread | The girl in pink walking with an ice cream in profile: "a small pink thing", "a tiny pink dot", a sweet, a flower, a blown kiss (6, 32, 49) | The review's item 23: on small figures the cone and scoop about 1.5 times larger, the cone a darker waffle brown, the scoop at the mouth rather than the nose. Read the walk at 90 on the small children in whole pictures |
| R2 | `photo` | 0.90 (5 pictures) | "a camera (or binoculars)" (23) | The notes' item 4 and the review's item 21: a flash on top and a wrist strap, one eye to the viewfinder; the camera facing a subject |
| R3 | `lost_balloon` | 0.944 (3 pictures) | "holding the string by its very tip, or has just let go" (44) | The string's free end a little further above the reaching hand |
| R4 | `bird_steals` | 0.967 (5 pictures) | "about to steal it or just perching" (23); the bird "overlapping" the sandwich (32) | The review's item 28: the bird clear of the hose reel and pecking at a sandwich drawn larger |

## Unintended oddities

Named kinds, from the scorers' lists (`v044/scores_summary_a.md` to `_g.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.45 |
|---|---|---|---|---|
| O1 | B | The reading dog's paper "floats slightly in front of the puppy's paws rather than resting in them", "seems to float beside the puppy" | 1, 5 | The paws drawn over the paper's corner, the toes curled over its top edge |
| O2 | B | "Black ice skates": the walking man's dark shoes, the back foot lifted on its toe, its grey sole plate read as a blade | 59 | As the run's raised foot, no sole plate under a raised walking shoe |
| O3 | C | The goat in a park "a little unusual", four of four | 10, 46, 72, 82 | Notes for the pilot |
| O4 | C | Profile cats: "a small white shape at the cat's chest/front paws", legs "folded underneath it in a slightly tangled way" | 24, 62 | Watch |
| O5 | C | The begging dog "a bit squashed and compact", "a little lumpy" | 13, 36 | Watch |
| O6 | C | The lamp post "very tall and thin" next to the trees (all three re-reads); the seesaw's low end and its rider's feet hovering; figures over the pond's outline | 6, 32, 49; 56; 43, 44 | Notes for the pilot, with the review's item 11 (scale) |

## Placement

**The set.**
- **Tiers 1 to 3.** Every cell placed under revision 42 on its base seed but one: the tier-3 playground, which failed 13 base seeds, as under revision 41. v0.43's two fresh seed lists (`tpdb_work/more44.sh`) each placed on their first seed again, and the second's, v0.43's s32043, is kept.
- **Tier 4.** The park and the playground placed on v0.43's seeds, with the same templates. The street's forced set, v0.29 to v0.43's, has the upward water, which revision 42 keeps out of the street; with the square wheel in its place it placed on v0.43's seed. The garden failed v0.43's seed and the next 44 of its search (most failures naming the stalking cat, the begging dog or the paint tracks), and placed on the first seed of a new list.
- **The isomorphs** are new. The second of tier 2 came from the tier-2 street: the park's drifted in inference or could not place the wave, and the garden's dog by the door has no isomorph outside gardens (`tpdb_work/iso44b.py`).

**The probes.**
- **The first pass** (`probes.py 3`, with five for `dog_reading`, `dog_wants_walk` and `photo`) ended `SHORT {'dog_begs': 2}`, a count of pictures, not a shortfall.
- **The pass stratified by angle** added 12 probes, and every template then had three pictures or more.

All 82 records rebuild identical to the pixel, and the library passes the validator in full.
