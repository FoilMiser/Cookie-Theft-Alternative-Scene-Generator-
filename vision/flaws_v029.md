# v0.29 blind screen: what it found (the work list for v0.30)

The v0.29 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 54 probes. Keys, descriptions and scores are in `v029/`.

## Headline (the 21 pictures of the set)

| | v0.26 (21) | v0.27 (21) | v0.28 (21) | v0.29 (21) |
|---|---|---|---|---|
| Things | 0.995 | 1.00 | 1.00 | 0.981 |
| Actions | 0.992 | 0.996 | 0.996 | 1.00 |
| Inferences | 0.953 | 0.950 | 0.879 | 0.985 |
| Contradictions | 0.981 | 1.00 | 1.00 | 1.00 |
| All items | 0.988 | 0.993 | 0.984 | 0.991 |
| Misread items | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 |
| Readers' remarks per picture (all screened pictures) | 5.27 | 5.81 | 5.14 | 5.15 |
| Oddities per picture, as logged by the scorers | 2.6 (at most 3) | 2.2 (at most 3) | 2.0 (at most 3) | 2.3 (at most 3) |

Across all 75 pictures 829 of 834 scored items had full marks. Three had half marks, two were missed, and none was misread. Three of those five are in the set: the two missed are "a few white clouds" in two street pictures (45 and 47), a setting item and not a template's, which is all that took Things under 1.00, and the third is a half mark on the bird stealing a sandwich (34). The two in the probes are half marks on the dog at the door (9) and the water going upward (61).

## How far to believe the gate

All 64 templates pass, against 61. The gate has read 64 twice before, in v0.20 and v0.23, and the next screen fell each time, to 61 and to 63. Three things temper this one.

**The readers still offer second readings.** Four of the five trips have it both ways: "so he looks about to trip over it or bump into it" in the free description and "or the box may simply be near him and he might pass it" under unsure. Scorer c wrote down the rule it used, an item gets 1 when the free description commits to the meaning, and listed the 18 items that rest on it, among 259. Counted at half marks, its inferences fall from 1.00 to 0.75. The trip would fall to 0.87 (13 of 15), under the gate.

**That rule is not new, so this is not the scorers going soft.** v0.28's scorers gave 1 to "she may walk into it because she isn't looking" with "might ... just pass close by" below it. What moved is the free description. v0.28's said "may be about to walk into it", "might bump into or trip over it, though it isn't directly in front of his feet". v0.29's say "heading straight for a cardboard box", "directly in his path ... so he appears about to trip over it". Second readings by a rough word count are not down, 3.2 a picture against 2.9.

**It is one screen.** The v0.9 retest moved the gate by about five templates with nothing changed. Three is inside that. What goes beyond the count is that each of the three that failed is a drawing this release changed, and the words moved the way the bench said they would: "sniffing the grass" is gone from the sleeping dog, and the duck's head is down at the crumbs in the free description of two of its three pictures.

And the trip has only been read in one setting here: its five pictures are all street (v0.28's were three garden, three street). The two design tests elsewhere said it too (a garden, a playground), the garden's reader adding "or just walking past it down the path, since the box is mostly on the grass beside the path".

## Reading the two bottom rows

Remarks did not move, 5.15 against 5.14 (386 on 75 pictures, 360 on 70), on a little less in each picture, 2.92 templates against 3.06. The readers range from 4.50 to 5.75 a picture on the same split, against 4.25 to 6.38. `remark_topics.py` sorts the remarks of two screens by keyword, roughly, and the hits were read:

| Pictures that remark on | v0.28 | v0.29 | |
|---|---|---|---|
| Stiff or awkward poses | 12 | 20 | Not changed, and mostly slight: "a little stiff, but not impossible" (6), "slightly stiff but not impossible" (46). One is a real fault: "the running man's shoulders and arms look stiff and sausage-like" (72) |
| A figure over the pond | 6 | 10 | Not changed. Every one of the ten clears it itself, as "his feet are clearly on the grass" (74) |
| A branch to hold it | 3 | 6 | Half of it new: the fish's limb, "drawn on top of the leafy crown" (12), "a little pasted in" (23), "as though cut out of the green leaf mass" (67) |
| Shadows | 11 | 14 | Not changed. None calls one wide or off the feet. Five say there is none, as "no shadow on the ground beneath it" (55), two say a jumper's is far below him, as a jumper's should be (60, 72) |
| Feet overlapping | 2 | 5 | Only two are about a figure's feet: "feet are drawn close together and turned" (46), and a broom at a sweeper's (48). Two are a bird on a lamp, and one shoes at a pond's edge |
| Thin or long body or legs | 13 | 13 | Not changed |
| A face hidden or hard to read | 12 | 11 | Not changed |
| Scale | 10 | 6 | Not changed |
| The hose stiff or jointed | 1 | 2 | Redrawn. No "rigid pipe". See below |
| The hose's bulge | 3 | 4 | Slimmer. One of the four is a skirt that bulges (13). The other three read it as trapped water first |

A keyword count is a rough sort, which says where to read. It is not a measure.

## The v0.28 list

| v0.28 reading | v0.29 result |
|---|---|
| R1 `dog_sleeping` 0.667: "sniffing the grass, lying down, or curled up asleep", "could be a puppy or a kitten" | **1.00** (3 items, 3 pictures). Three-quarters, chin on its paws. "Curled up asleep", all three, and all three a puppy. Nobody has it sniffing or collapsed, the risk in a body lying stretched out. The wider shadow did little on the bench and was not used |
| R2 `ducks_bread` 0.833: "swimming towards those crumbs" | **1.00** (9 items, 3 pictures). The neck arched, the bill at a crumb. "Bending its head down to peck at the crumbs" (26), "bending down towards the crumbs" (49). "Goes after a trail of pale pieces" (7) is the weakest, and scored in full. Scored in full on the same words v0.28 might not have, so some of this may be the scorers again. New: crumbs that run past the pond's edge (26, 49) |
| R3 `dog_wants_walk` 0.833: "sits with a red lead in its mouth" | **0.917** (6 items, 3 pictures). Beside the door, turned to it. "As though asking to be taken for a walk" (48, the same seed that failed). One half mark, a reader who gives it only under unsure: "looks as if it wants a walk, but this is a guess" (9) |
| R4 `about_to_trip` 0.917, meaning 0.75: "he is moving past it, not squarely into it" | **1.00** (15 items, 5 pictures), meaning 1.00. A wide low box. See "How far to believe the gate", and placement below |
| O1 The hose in `hose_water`: "like a rigid pipe", "a post" | No rigid pipe or post. "Rises quite stiffly" (19), and one fault that is new: "seems to stop at about waist height, then the part at her hands starts again" (63) |
| O2 A ladder "too far away" from a lamp, a floating and a soaked box together, a bucket as "a makeshift rain hat" | Gone, as the rules remove the case. All three ladders "leaning against nothing at all", or close to it. No picture has both boxes, and no bucket under a dark sky |
| O3 "Wooden" in the floating box's key | The key says a box. No marks turned on it |
| O4 The lifted heel | Read on the bench, nothing to choose. Kept. "Legs walking another way": 1, as before |
| O5 The hose's bulge as "a separate slug-shaped object" | Slimmer. "As if the water is blocked there" (9), "as water backing up behind the dog's foot" (50). Second readings remain: "a thicker joint in the hose" (9), "a loop of hose lying flat" (50) |
| O6 The heavy rider's leg over the plank | Not changed. "The beam seems to pass through or behind his legs near the end" (65) |
| O7 The goldfish "pasted onto the leaves" | On a limb. Pasting moved from the fish to the limb, as above. The fish reads as impossible in all three. Two of the three also call it an ornament or toy, the third "floating or flying past the tree" |
| O8 The narrow figure | Not changed. 13 and 13 by keyword |
| O9 Older ones | Left, as since v0.11 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 |
|---|---|---|---|---|---|
| Pass | 61 | 59 | 63 | 61 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 3 | 5 | 1 | 3 | 0 |

Every template was screened in at least three pictures (48 in three, 8 in four, 4 in five, 2 in six, 2 in seven; 409 scored items behind the verdicts).

## What reads least well (the v0.30 list)

Nothing fails, so this is the bottom of a list that passes, and the things a pass hides.

| # | Template | v0.29 | What the readers saw | Fix for v0.30 |
|---|---|---|---|---|
| R1 | `about_to_trip` | 1.00 (15 items, 5 pictures) | Four of five offer "he might pass it" under unsure, and all five are street pictures. On a stricter scorer this would be the first to fall. The box is also what the tier-4 searches fail on (below) | Probes that force it into a garden and a playground, and read those. A box a little narrower, on the bench, if it costs nothing in the reading |
| R2 | `dog_wants_walk` | 0.917 (6 items, 3 pictures) | "But this is a guess" (9). Under 1 for a third release | Watch. Its picture 9 has a hose story and a bucket on a head beside it |
| R3 | `water_upward` | 0.944 (9 items, 3 pictures) | "Could be a normal pour drawn awkwardly", though the same reader has it arc upwards (61). Picture 54 read it clean. 1.00 for the three releases before | Watch. Look at the can's angle in picture 61 |
| R4 | `bird_steals` | 0.958 (12 items, 4 pictures) | "May be about to steal it", or "simply perched near the sandwich" (34). 1.00 for the three releases before | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v029/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.30 |
|---|---|---|---|---|
| O1 | B | The hose from the ground to the fist: "seems to stop at about waist height, then the part at her hands starts again" | Pictures 63; less so 19, 53 | New with the redraw, and in the drawing, as a crop of 63 shows: the short piece over the joint has a square end, wider than the fist's stub, and reads as a sleeve. The bench never read the joint, and test 1's reader called it "unclear". `hose_water` is only in probes this release. Taper the piece to the stub, and read it on the bench |
| O2 | B | The fish's limb on the crown: "drawn on top of the leafy crown", "a little pasted in", and the tuft at its end "looks detached" | Pictures 12, 23, 67 | Take the tuft off, or put the limb behind a piece of the crown. The ball's and the bird's limbs are the same drawing (42, 45, 71) |
| O3 | C | Crumbs past the pond's edge: "several crumbs lie on the grass", "unclear whether floating or on the bank" | Pictures 26, 49 | Keep the trail on the water from the duck's mouth outward. Cheap |
| O4 | C | The reading dog "a bit like a kangaroo": long body, hind legs out | Pictures 28, 34 | The bench, if it comes again |
| O5 | C | A running man's shoulders "stiff and sausage-like" | Picture 72 | Look at the crop |
| O6 | C | The hose reel as scenery, "only a short stub of hose joined to nothing" | Pictures 4, 59 | A reel with its hose wound on, when no one holds it |
| O7 | C | A square-wheeled bicycle "stands up on its own" | Pictures 34, 45 | A kickstand drawn plainly, if it does not weaken the contradiction |
| O8 | C | The lamp post "much taller than the trees" | Pictures 52, 57 | Notes for the pilot |
| O9 | C | The narrow figure, the heavy rider's leg | Throughout; 65 | Leave, or a real change of build |
| O10 | C | Older ones: figures over the pond, goats as sheep or dogs, a wind that reaches only the cap, autumn leaves under green trees, the roller's head | Throughout | Notes for the pilot, as since v0.11 |

## Placement: what the wide box cost

The tier-4 cells took 166 failed seeds, against 80 in v0.28's logs: 11 in the garden, 29 in the street, 39 in the playground and 87 in the park, the last across five searches, the last four side by side. Last release's seed failed in all four. The tier-4 isomorph took 17 failed attempts, against 226.

`about_to_trip` is what those failures name most: 169 times, against 44 in v0.28, ahead of `ice_cream_drop` (105), `lost_balloon` (82) and `sprinkler_package` (64). A box that cannot be walked past needs ground that a bucket did not, and that is a cost of Y, seen only here. It also falls back to the bucket when another box is in the picture, so every picture with a floating, carried or soaked box still has the old obstacle; none of the five screened pictures did.

**A rule can have a cliff.** The ladder's margin from a lamp was first 240 units, and that placed 0 of 8 seeds in every combination tried. 60, 110 and 160 placed 8 of 8 or 7 of 8, 200 placed none. It is 160. Old gaps were 36 to 90 units. A rule that looks like a small tightening can take a template out of the battery, so try each new rule on a few seeds at several values before the set.

The ladder's calibration now rests on one sampled placement against three (`calibration.json`, `n`), and its cue salience moved by -0.074. That may want a closer look if the ladder's difficulty matters to the pilot.
