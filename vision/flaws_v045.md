# v0.45 blind screen: what it found (the work list for v0.46)

The v0.45 screen read the set's 21 pictures and 72 probes with the prompts of v0.39 (`screen_prompts.md`). There were twelve readers of seven or eight pictures and four scorers of 23 or 24. After the screen, three pictures of the set were rebuilt and read again by a fresh reader and scorer each (below). The oddity tally is by angle, as in v0.39. Keys, descriptions and scores are in `v045/`; the three pictures' first descriptions and scores are in `v045/first/`.

v0.45 worked two lists: `flaws_v044.md` and a fresh look at v0.44's pictures and cut-outs by four reviewers, each with a share of its own (`tpdb_work/review45/`). The bench, in whole pictures (`isolation_v045.md`), took these into the cast (builder 0.45.0):
- **the ice cream**, cone and scoop, half as big again in a child's hand, a third in a teenager's and a fifth in an adult's, the cone the wood's brown and longer above the fist; the empty cone 1.3 times the size in a child's hand and 1.15 in a teenager's;
- **the camera** a fifth larger, with a prism hump, a longer lens in a wide silver ring and a bright strap hanging in a loop under it;
- **the shoes' sole plates** no longer than the shoe's flat underside and no wider than the shoe, dark under every shoe (under a walker's tipped foot v0.44's stood clear of the toe and the heel like a blade);
- **the hose inspector's head** toward the viewer and a little down (v0.44's turned it away, a sign error);
- **the trowel** a broad pointed blade seen from the side, on a bright handle;
- **the paint roller** on a cranked wire frame, a cream cap at each end;
- **the carried box** khaki with a brown tape; **the swimming duck's** legs out of sight; **the kite flier's reel**, two bright flanges with the cream of the wound string between them.

Placement revision 43 adds twelve rules:
- the lost balloon's string ends 62 to 80 px above the reaching hand, hangs in a slow wave with no curl, ends nowhere on a playground railing and, in the garden, above the wooden fence's pickets;
- the wet paint begins below the roller, which lies on bare wood at the paint's edge; the painter stands close enough for the roller to be on the boards, the tin with them;
- the planter kneels at the bed's end and digs in the bed, a hole under the trowel's point, the pot in front;
- the picnic's loaf and bottle stand out of the basket, and a plate with a slice of watermelon is on the blanket;
- the goat's stake is clear of every standing structure;
- a swimming animal is cut at a waterline with a ripple, and has no ground shadow;
- the slide's ladder is the frame's own end, in the frame's red;
- the bird table's foot is a tuft of grass on a low mound;
- after the screen, the reading dog's paper lies on its paws (below).

Every person and the duck is drawn anew, so no picture is identical to v0.44's, and there is no retest this time. The songbirds, the cats, the dogs and the goat are v0.44's.

## Headline (the 21 pictures of the set)

| | v0.41 (21) | v0.42 (21) | v0.43 (21) | v0.44 (21) | v0.45 (21) |
|---|---|---|---|---|---|
| Things | 1.00 | 0.991 | 0.952 | 0.991 | 0.962 |
| Actions | 1.00 | 1.00 | 0.996 | 0.996 | 0.992 |
| Inferences | 0.958 | 0.939 | 1.00 | 0.971 | 0.984 |
| Contradictions | 1.00 | 0.942 | 0.712 | 1.00 | 0.955 |
| All items | 0.995 | 0.984 | 0.955 | 0.991 | 0.977 |
| Misread items | 0 of 287 | 0 of 290 | 1 of 290 | 0 of 286 | 0 of 281 |
| Readers' remarks per picture (all screened pictures) | 3.17 | 3.05 | 3.12 | 3.27 | 2.58 |
| Oddities per picture, as logged by the scorers | 0.4 (at most 3) | 0.7 (at most 3) | 1.1 (at most 3) | 0.7 (at most 3) | 0.5 (at most 2) |

The set's figures are a little under v0.44's, and none of the fall is on a thing v0.45 redrew. The things lost four items to two readers who did not mention the clouds or a tree; the contradictions lost two half marks on the square wheels; the actions and inferences lost three half marks on the two birds.

Across all 93 pictures, 992 of the 1,009 scored items had full marks, and none was misread. The 17 under full marks:
- **Ten on the clouds and two on a tree, from two readers.** One reader left the clouds out of seven of its eight pictures (9, 11 to 16; "only 'sunny'"), another out of three of its eight (34, 36, 38). The tree was not mentioned in 16 ("only a hedge behind the fence") and 36 ("only a bush"). All twelve are zeros on setting items. v0.44 had one.
- **The thief bird, two half marks in one picture (42):** "standing next to the sandwich, looking like it is about to take it"; "it might be about to steal the sandwich, or just be perched next to it". Both are from the re-read of that picture (below).
- **The square wheels, two half marks:** the bicycle's "a bit squared/boxy" (10), and "a wheelbarrow parked in front of a square box, or a wheelbarrow with an odd square wheel" (51).
- **The bird the cat stalks (10):** "standing on the grass", where the key has it pecking.

The scorers gave ten, four, one and two items under full marks, of 260, 262, 238 and 249; the three re-reads none, two and none, of 25 each.

**What the full marks rest on.** The scorers' notes mark 9 items they credited in full where the free description commits and the unsure section adds another reading (7 in v0.44): two on the stopped hose, and one each on the pan's water, the kite in the tree, the dog that wants its walk, the thief bird, the ball in the tree, the walker about to trip and the reading dog. Halved, they take no template under the gate (`tpdb_work/strict45.py`).

## The v0.44 list and the fresh look

| v0.44 reading, or the reviewers' item | v0.45 result |
|---|---|
| R1: `ice_cream` 0.846, one misread; the girl in pink's "a small pink thing", "a tiny pink dot" | **1.00 in 14 pictures** (14 items). "a pink ice-cream cone" in a child's hand; a sweet or a lollipop in no description |
| R2: `photo` 0.90, "a camera (or binoculars)" | **1.00 in five pictures.** "holding a camera up to his eye, taking a photo, with a red strap hanging from it" (53); binoculars in no description |
| R3: `lost_balloon` 0.944, "holding the string by its very tip, or has just let go" | **1.00 in five pictures** (15 items). "has escaped and is floating up into the sky, its string dangling" (48); no hook, and no fence or railing named with the string |
| R4: `bird_steals` 0.967 | **Not worked, and 0.933** (15 items, 5 pictures): 1.00 at the first count, two half marks in the re-read of picture 42. R1 of the next list |
| O1: the reading dog's paper "floats slightly in front of the puppy's paws" | Left on the watch list, and **it failed the gate's first count** (0.833, one misread: a paper "up in the air", 90). Drawn onto the paws after the screen and read again: **1.00 in three pictures** (below) |
| O2: "black ice skates", a grey sole plate | No skates in 93 descriptions |
| O3: the goat "a little unusual", four of four | `goat_grazing` 1.00 (4 pictures); "unusual" in two of four (4, 19). Its stake "a peg in the ground", "a short wooden stake", never on a bench |
| O4, O5: profile cats, the begging dog | Not worked. The fence cat's legs "reach down past the fence top" (32), and it "walks on the pointed tops of the fence pickets" (90). No remark on the begging dog |
| O6: the lamp post, the seesaw's riders, figures over the pond | Not worked. No remark on the lamp post; the seesaw in five pictures and the pond in three (the oddities below) |
| Reviewers: the hose inspector's head turned away | `blocked_hose` 1.00 (28 items, 7 pictures) |
| Reviewers: the roller blue on blue, "a paddle"; the trowel a grey line | `paint_fence` 1.00 (9 pictures), "painting the fence blue with a paint roller on a long handle" (16, 20); `plant_flowers` 1.00 (5 pictures), "digging with a small trowel next to a pink flower in a terracotta pot, about to plant it" (56) |
| Reviewers: the duck standing on the water; the box the fence's colour | `ducks_swimming` 1.00 (4 pictures); `carry_box` 1.00 (3 pictures) |
| Reviewers: a picnic with no food in sight | `picnic` 1.00 (3 pictures): "a plate with a slice of watermelon, and beside him a wicker picnic basket with a bottle and a baguette" (54) |
| The bench: the kite flier with no spool; the slide's ladder apart from its frame | "a kite reel" or "a kite spool" in the hand in six of the seven pictures with a kite on its string (4, 10, 19, 21, 60, 83); `slide` 1.00 (3 pictures), no remark on the ladder |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.41 | v0.42 | v0.43 | v0.44 | v0.45 |
|---|---|---|---|---|---|
| Pass | 64 | 63 | 62 | 63 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 1 | 2 | 1 | 0 |

The first count was 63 and 1: `dog_reading` at 0.833 with a misread. The table has the count after the fix and the three re-reads (below).

Every template was screened in at least three pictures. By count: 38 in three, 11 in four, 10 in five, 1 in six, 1 in seven, 1 in nine, 1 in thirteen and 1 in fourteen, with 468 scored items behind the verdicts.

The lowest that pass:
- `bird_steals` (0.933, 15 items, 5 pictures);
- `square_wheel` (0.933, 15 items, 5 pictures);
- `cat_stalks_bird` (0.958, 12 items, 4 pictures).
Every other template reads 1.00.

**Per angle** (`v045/gate_yaw.json`), 21 of the 22 (template, angle) pairs pass. The one that does not is the thief bird in profile, 0.889 over 9 items in 3 pictures, on picture 42's two half marks; at the three-quarter angle it reads 1.00. The oddities by angle: the fence cat in profile twice (32, 90), the goat twice (4, 19) and a red bird "noticeably bigger than the blue one" (28).

## After the screen

**The failure.** The gate first failed `dog_reading` at 0.833 (9 items in 3 pictures) on one picture, the tier-4 garden isomorph (90): "standing on its hind legs with its front paws on an open newspaper that seems to be up in the air"; "either the puppy is holding it up with its paws, or it is floating". A half mark for the oddity and a misread for the reading. It is v0.44's O1, which this release had left on the watch list because the paper looked fine to the builder in four pictures.

**The fix** (`templates.READ45`). The paper is drawn 12 px toward the dog and 6 px higher, at the dog's scale, so the forelegs cross the near page and the paws lie on it. At 20 and 10 the paws hid 25% of the paper, over the 20% a scored thing may lose, and the garden isomorph could not be built; at 12 and 6 they hide 17 to 18% (7 to 8% before). The box the planner places the paper by is unchanged, and `dog_reading` calibrated alone with the rule off and on gives the shipped calibration's numbers, so the calibration and the priors stand. The three pictures with the reading dog (4, 42 and 90, all of the set) were regenerated over their files, the street before its isomorph. No other picture changed; all 93 records rebuild identical, and the library passes the validator.

**The re-reads.** A fresh reader and scorer read each of the three pictures (`scores_e.json` to `scores_g.json`), and the re-reads replace the first scores. The reading dog had full marks in all three: "sitting up on its hind legs holding an open newspaper as if reading it" (90), "holding an open newspaper with its front paws as if reading" (4), "sits on its haunches holding an open newspaper as if reading it" (42). No reader names a floating paper; one says "Nothing seems to float unsupported apart from the bird and kite" (4). Two of the three add another reading in the unsure section: "the dog could simply be holding/carrying the paper" (90), "holding or playing with a dropped paper" (42).

**What a re-read costs.** A re-read rolls every item of its picture again, not only the one that was fixed. Of the 66 items in the three pictures that the fix did not touch, 64 scored the same and two went down. Picture 42's thief bird, which the fix did not touch, had full marks at the first read (the inference hedged: "could be about to steal the sandwich, or just perched next to it") and two half marks at the second, from nearly the same words. `bird_steals` went from 1.00 to 0.933, and its profile row under 0.9. The second scores stand.

## What reads least well (the v0.46 list)

| # | Template | v0.45 | What the readers saw | Fix for v0.46 |
|---|---|---|---|---|
| R1 | `bird_steals` | 0.933 (15 items, 5 pictures); 0.889 in profile | "about to take it", "about to steal the sandwich, or just be perched next to it" (42, both readings); "about to peck/steal it" (10). The bird stands beside the sandwich, its beak at the edge | v0.44's R4, still open: the bird's head down and its beak in the sandwich, a bite out of the bread and crumbs under it, the sandwich drawn larger, the bird clear of the hose reel |
| R2 | `square_wheel` | 0.933 (15 items, 5 pictures) | The bicycle's wheels "a bit squared/boxy" (10); "a wheelbarrow parked in front of a square box, or a wheelbarrow with an odd square wheel" (51); "a square/boxy shape at the front rather than a round wheel" (90, credited) | The wheelbarrow's square wheel clear of the tray, with a hub and a fork, so it is a wheel before it is a box; the bicycle's squares with sharp corners and spokes |
| R3 | `cat_stalks_bird` | 0.958 (12 items, 4 pictures) | The stalked bird "standing on the grass", not pecking (10) | The bird's head down at a few seeds on the ground |

## Unintended oddities

Named kinds, from the scorers' lists (`v045/scores_summary_a.md` to `_g.md`) and the readers' unsure sections, most worth doing first. The scorers logged 27 in 93 pictures.

| # | Sev | Oddity | Where | Fix for v0.46 |
|---|---|---|---|---|
| O1 | B | The seesaw's riders: "the man's lower body overlaps the seesaw plank, as if the plank passes through his legs", "sits slightly above the seesaw plank, as if hovering", "sits slightly past the end of the seesaw plank" | 14, 26, 66, 73, 93 | Seat each rider on the plank: the plank drawn over the far leg and under the near thigh, the sitter inside the plank's end. v0.44's O6, five pictures now |
| O2 | B | The wet paint: "the lower block of the blue-painted fence section sticks out to the left of the boards above (possible drawing artefact)"; in design test 2 the painted boards "slightly away from where the roller touches" | 58 | The paint's edge on a board's joint, the board under the roller painted from the roller down with an uneven wet edge |
| O3 | B | Figures drawn over the pond: the feeding woman's "upper body is drawn over the pond, so she could seem to stand in the water" | 28, 29, 44 | Keep a standing figure's head and shoulders off the water, or give the pond a near bank. v0.44's O6 |
| O4 | B | The reading dog "could simply be holding/carrying the paper", beside reading, in two of three re-reads | 42, 90 | Pose it in Blender with bent forelegs and the paper as a held prop, and read it on the bench before the set |
| O5 | C | The swing: "only one swing hangs on a frame wide enough for two", the seat "high off the ground on short ropes", still "despite the strong wind" | 22, 26; 78; 75 | A second seat or a narrower frame; longer ropes; the seat swung by the wind's lines |
| O6 | C | The fence cat: legs "past the fence top, as if partly in front of the boards"; "walks on the pointed tops of the fence pickets" | 32, 90 | Its paws on the fence's top line; a cap rail under it |
| O7 | C | The jumping girl's shadow "far below her feet"; the kicker's ball "at his trailing foot"; the bicycle upright "with no rider or kickstand"; the jeans that "hang slanted and overlap the washing-line post"; the pan's water "spout-like"; the hose's bulge "possibly a drawing glitch" | 33; 72; 10; 21; 86; 91 | One picture each: watch |
| O8 | C | The goat in a park "a little unusual"; the crying child who "covers their eyes instead of looking at the dropped ice cream"; "a second cardboard box on the far right has no obvious purpose" | 4, 19; 4; 42 | Notes for the pilot |

For the watch list as well: the park's lost balloon whose string ends on the far tree line (56, 86; both read as lost); the garden's lost balloon high above the reaching hand since the string must clear the fence; no street among the probes, and no lost balloon on the playground among the screened pictures (design test 4 has one). The keys' `animals` list does not say which of two animals of a kind is at which angle, so one scorer's angle tag was a guess.

## Placement

**The set.**
- **Tiers 1 to 3.** Every cell placed under revision 43 on its base seed but one: the tier-3 playground, which failed the base seeds as in v0.44 and placed on the first seed of a fresh list, v0.43's s32043 again.
- **Tier 4.** The garden, the park and the street placed on v0.44's seeds with the same templates, and so did the playground at first.
- **A prior moved after the set was built.** The garden's lost balloon was lifted above the fence late (`templates.WOOD45`), its inference prior moved by 0.02 with the calibration, and two cells no longer rebuilt: the tier-3 garden's base seed now gives s5013 with other templates, and the tier-4 playground failed v0.43's seed and the next 14 before the 16th placed, s502878. Both replace the earlier pictures.
- **The isomorphs** pair the same five cells as v0.44's: the tier-2 garden (of the playground) and park (of the street), the tier-3 garden (of the street) and street (of the park), and the tier-4 garden (of the street). The tier-2 park and the tier-4 garden came out on v0.44's seeds with v0.44's templates; the other three are on new seeds.

**The probes.**
- **The first pass** (`probes.py 3`, with five for `ice_cream`, `photo`, `lost_balloon`, `plant_flowers` and `paint_fence`) built 54 and ended `SHORT {'hang_laundry': 0, 'fishing': 1, 'dog_begs': 2}`, counts of pictures: the wash line had none at all, having failed in three crowded garden groups.
- **The pass stratified by angle** added 13.
- **Five more** were forced in small groups (`tpdb_work/more_probes45.py`), three with the wash line and two with the fishing, and every template then had three pictures or more. The 72 probes are 41 gardens, 23 parks and 8 playgrounds.

**One slip in the blind rule.** A reader whose first write failed listed the screen's folder once and reported it: the listing "showed only the names of the existing desc_pic_*.md files", and it opened no file but its own seven pictures.

All 93 records rebuild identical to the pixel, and the library passes the validator in full.
