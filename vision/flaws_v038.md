# v0.38 blind screen: what it found (the work list for v0.39)

The v0.38 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 55 probes. Keys, descriptions and scores are in `v038/`.

## Headline (the 21 pictures of the set)

| | v0.35 (21) | v0.36 (21) | v0.37 (21) | v0.38 (21) |
|---|---|---|---|---|
| Things | 0.971 | 1.00 | 1.00 | 1.00 |
| Actions | 0.996 | 1.00 | 0.996 | 1.00 |
| Inferences | 0.957 | 0.971 | 0.971 | 0.985 |
| Contradictions | 1.00 | 1.00 | 0.977 | 1.00 |
| All items | 0.982 | 0.996 | 0.993 | 0.998 |
| Misread items | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 286 |
| Readers' remarks per picture (all screened pictures) | 2.88 | 3.10 | 2.82 | 3.38 |
| Oddities per picture, as logged by the scorers | 0.2 (at most 3) | 0.6 (at most 3) | 0.4 (at most 3) | 0.8 (at most 3) |

Across all 76 pictures 841 of 842 scored items had full marks, and none was misread. The one item under full marks is in the set: the ice cream in the tier-3 playground, on a picture identical to v0.37's, where the same item was half right (72): "It is not certain whether the boy dropped the ice cream himself or the dog knocked it out of his hand". The scorers gave none, none and one items under full marks, in 298, 268 and 276. Every reader named the clouds.

**What the full marks rest on.** Scorers a and b listed, unasked, 23 items they credited in full where the reader also gave a second reading (`scores_summary_a.md`, `_b.md`). Halved, as a strict reading of the rule's "only offered as one of two readings" would have them, 58 of 64 templates pass, and six fall under the gate: `play_catch` (0.75), `windy_hat` (0.778), `cat_sleeping` and `plant_flowers` (0.833), `bird_steals` (0.875) and `seesaw_heavy` (0.889) (`tpdb_work/strict38.py`). This is not a change in the scorers: 11 of the 23 are on pictures identical to v0.37's, and v0.37's scorers gave all 11 full marks too. Their rule credits the reading a describer states, with a second one offered in the unsure section, as v0.37's did. The strict count says where the next half marks would come from.

## A retest, a ninth time

22 pictures, 20 of the set's and 2 probes, were identical to the pixel in v0.37 and v0.38 (`tpdb_work/retest38.py`); the others changed with revision 36 or with the probe groups it changed (below).

| On the same 22 pictures | v0.37 | v0.38 |
|---|---|---|
| Items | 294 | 294 |
| Items with the same score in both | 291 | 291 |
| Remarks | 73 | 94 |

3 items moved, all up, each by half a mark, and they are three of the four half marks of v0.37's set: the girl throwing the bread (the tier-4 park), the bird stealing the sandwich (the tier-4 street's isomorph) and the upward water (the tier-4 street). The fourth, the ice cream (72), was half right in both. The remarks rose by more than a quarter on pictures that did not change, so this screen's readers wrote more, from 2.22 to 4.25 a reader.

## The v0.37 list

| v0.37 reading | v0.38 result |
|---|---|
| R1 `hang_laundry` 0.833, fails | **1.00** (3 items, 3 pictures). Revision 36 sets a basket of washing at the hanger's feet and drips the washing (`isolation_v038.md`, `design_tests_v038.md`). Two of the three pictures are v0.37's own seeds (23009 and 23053, its pictures 12 and 25), and the third v0.37's picture 74's set on a new seed. Every reader has the shirt pegged up, none offers taking it down: "He is reaching up and pegging a white T-shirt onto the line" (68); "reaching up with both hands to peg a white T-shirt on the line" (02); "reaching up to peg a wet white T-shirt on the line" (26) |
| R2 `ducks_bread` 0.944 | **1.00** (9 items, 3 pictures). Not changed; the girl throwing the bread reads in full on the identical picture |
| R3 `water_upward` 0.944 | **1.00** (9 items, 3 pictures). Not changed; full marks again on the identical picture |
| O1 A storm pointer offered the cat on the fence, three screens running on one picture | **Fixed.** Revision 36 keeps the cat walking the fence out of a storm pointer's picture and puts the stalking cat on the ground; in the garden a perched bird is dropped from the plan too, since the cat's picture, searched again, put one on the fence top where the cat had sat. The three storm pointers read at the clouds: "The clouds are the only thing up there" (69); "or, less likely, at the ball up to her right" (51, the set's tier-3 garden, where picture 57 was) |
| O2 The broom's autumn leaves under green trees | **Grew**: seven pictures, from five readers of nine (07, 08, 33, 37, 39, 65, 71), the rake's heap with the broom's: "a little odd where the leaves came from" (65), "they seem to come from nowhere" (71). Below |
| O3 The pan waterer's face against the flowers | Not seen, in three pictures with the pan (07, 37, 52) |
| O4 The runner perhaps rushing at the boy | Not seen: "I can't tell why the man is running" (67) |
| O5 Older ones | As before: goats out of place (07, 09, 14, 15), the seesaw man over the plank (19, 29), wind that moves no swing or washing (30, 47), the square-wheeled bicycle standing (39) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.34 | v0.35 | v0.36 | v0.37 | v0.38 |
|---|---|---|---|---|---|
| Pass | 64 | 63 | 64 | 63 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 1 | 0 | 1 | 0 |

Every template was screened in at least three pictures (50 in three, 6 in four, 4 in five, 2 in six and 2 in eight; 408 scored items behind the verdicts), and all 64 pass. The lowest is `ice_cream_drop` (0.958, 12 items, 3 pictures), on its one half mark; every other template has full marks.

## What reads least well (the v0.39 list)

| # | Template | v0.38 | What the readers saw | Fix for v0.39 |
|---|---|---|---|---|
| R1 | `ice_cream_drop` | 0.958 (12 items, 3 pictures) | "It is not certain whether the boy dropped the ice cream himself or the dog knocked it out of his hand" (72), half right on the same picture in v0.37 | Look at where the dog stands: a dog at the child's hand says it knocked the cone. Rebuild picture 72's seed first |
| R2 | `play_catch` | 1.00; 0.75 read strictly | Who threw: the dashed trail "could also be read as the man having thrown it and the boy about to catch it" (02); "the ball sits right at the woman's hands" (49) | The ball a little short of the catcher's hands, so the trail cannot run from either end |
| R3 | `windy_hat` | 1.00; 0.778 read strictly | "He may be reaching for it or simply throwing his hands up in dismay" (30), and alike in 34 and 47 | Watch |
| R4 | `bird_steals` | 1.00; 0.875 read strictly | "could just be sitting next to the sandwich, or actively stealing it" (05), and alike in 08 and 24, all identical to v0.37's and credited in full in both | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v038/scores_summary_a.md` to `_c.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.39 |
|---|---|---|---|---|
| O1 | C | Autumn leaves swept or raked under green trees, seven pictures from five readers (four mentions in v0.37, three from one reader) | 07, 08, 33, 37, 39, 65, 71 | The heaps drawn for summer: cut grass and twigs, a few brown leaves. Bench it, and read it beside the rake, whose cue the heap is |
| O2 | C | The fish's branch bent toward it: "almost like an arm holding the fish up" (57), "bends sharply out of the trunk toward it, which looks a bit drawn-on" (13), the trunk "bends sideways at an odd angle to end at the fish" (09) | 09, 13, 57 | Look at the limb revision 26 draws (`_limb_to`) on these three pictures. v0.31's bench tried a narrower one with less bend, and its readers named the join instead, so look at the drawing before benching again |
| O3 | C | Goats out of place, in a park or a back garden | 07, 09, 14, 15 | Notes for the pilot |
| O4 | C | A figure over the thing beside it: the hanger "very close to or tangled with the line" (26), the seesaw man over the plank (19, 29), a waterer in the flower bed (33), legs over the pond's edge (40), a head over the fruit stall (62) | Throughout | Watch the hanger; the rest as before |
| O5 | C | Older ones: wind that moves no swing or washing (30, 47), the square-wheeled bicycle standing with nothing to hold it up (39), a child drawn much smaller than the grown-up beside her (69, 72) | Throughout | Notes for the pilot |

## Placement

All four tier-4 cells placed on v0.37's seeds under revision 36, the street's on v0.29 to v0.37's forced set, and all four came back identical to the pixel, as did all five isomorphs; the tier-4 isomorph took 12 failed attempts, as in v0.33 to v0.37. 20 of the set's 21 pictures came back identical to v0.37's. The 21st is the tier-3 garden: v0.37's picture 57 drew the cat on the fence with the storm pointer, its seed placed nothing under revision 36, and neither did the twelve seeds `build_set.sh` searches after the showcase seed; three seed lists side by side then found 498 and 666 together, and 498's, with a storm pointer, was kept. The perched bird is dropped from the plan in the garden only, and not re-picked: re-picked, two other cells of the set (the tier-3 playground and street) no longer rebuilt, because an earlier try of theirs drew the pair; dropped in every setting, the playground still did not, because a plan changed in one try changes the template usage the next try plans with. With the new garden the probe groups changed, and 2 of the 55 probes came back identical. The first probe pass left `walk_dog`, `dog_begs` and `hang_laundry` short, the washing because the probe groups put it twice with the fence's paint (the painter, or the dog's paint tracks), which revision 19 keeps from the washing, and once beside a floating box and a dog walker, where it did not place; v0.37's washing and street probes were rebuilt on their own seeds, and v0.37's picture 74's set placed on a new seed. All 76 records rebuild identical to the pixel, and the library passes the validator in full, 353 of 353.
