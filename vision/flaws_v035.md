# v0.35 blind screen: what it found (the work list for v0.36)

The v0.35 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 61 probes. Keys, descriptions and scores are in `v035/`.

## Headline (the 21 pictures of the set)

| | v0.32 (21) | v0.33 (21) | v0.34 (21) | v0.35 (21) |
|---|---|---|---|---|
| Things | 0.991 | 0.990 | 0.990 | 0.971 |
| Actions | 0.988 | 0.992 | 1.00 | 0.996 |
| Inferences | 0.956 | 0.957 | 0.986 | 0.957 |
| Contradictions | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.986 | 0.988 | 0.995 | 0.982 |
| Misread items | 1 of 286 | 0 of 285 | 0 of 285 | 0 of 285 |
| Readers' remarks per picture (all screened pictures) | 3.28 | 3.19 | 3.13 | 2.88 |
| Oddities per picture, as logged by the scorers | 0.8 (at most 3) | 0.9 (at most 3) | 0.5 (at most 3) | 0.2 (at most 3) |

Across all 82 pictures 855 of 877 scored items had full marks, and one was misread.

**This screen is a retest.** 20 of the set's 21 pictures came back identical to the pixel, and 58 of the 61 probes; the pictures that changed are the three with a child on the swing and one new windy park. The set's seven items under full marks are all on identical pictures: three are the clouds, the dog on the hose in the tier-4 garden is "standing on or right beside the hose" (1, twice), the ice cream in the tier-4 park "has fallen" with the dog offered as a cause (45), and a balloon in the tier-3 park is "escaping", from her hand or someone else's (72).

**Two readers named nothing in the sky.** 17 of the screen's 22 items under full marks are "a few white clouds": nine of the first reader's ten pictures, one of the second's, and seven of the ninth reader's nine. The scorers gave 12, 1 and 9 items under full marks, in 304, 283 and 290; scorer a's zeros are ten of those clouds.

## A retest, a sixth time

78 pictures, 20 of the set's and 58 probes, were identical to the pixel in v0.34 and v0.35 (`tpdb_work/retest35.py`).

| On the same 78 pictures | v0.34 | v0.35 |
|---|---|---|
| Items | 830 | 830 |
| Items with the same score in both | 806 | 806 |
| Remarks | 243 | 222 |

24 items moved, 7 up and 17 down, and 12 of the 17 down are the clouds. Up: the goat on the hose and its inference, the bird's theft in the tier-4 garden, and four entities. Down, besides the clouds: the dog on the hose and its inference in the tier-4 garden, the dropped ice cream, a balloon let go of, and the grandfather in the bucket hat, the screen's one misread.

## The v0.34 list

| v0.34 reading | v0.35 result |
|---|---|
| R1 `blocked_hose` 0.917 | **0.917** (12 items, 3 pictures), not changed. The half marks moved back from the goat to the dog in the unchanged tier-4 garden, "standing on or right beside the hose" (1); the goat by the man now reads in full. Watch |
| R2 `bird_steals` 0.958 | **1.00** (12 items, 4 pictures). Not changed |
| O1 A pile of leaves lying still in the wind | Revision 33 keeps a pile swept or raked out of a windy picture. No reader of the three windy pictures said anything lay still but the hair and the clothes ("The tree, flowers, potted plants and the woman's hair stay still", scorer a, 8) |
| O2 The storm pointer and the washing | Left as it was, and offered again on the same unchanged seed: "The pointing woman could be pointing at the dark clouds (rain coming) or at the laundry on the line" (63). The item reads in full |
| O3 A seesaw rider "slightly above the plank" | Not said |
| O4 A flower over the boy's face at the pan | Not said |
| O5 A gate's knob behind a head | Again, on the same picture: "It could be a hair bun, or it could be the gate's knob showing behind his head" (73) |
| O6 Goats, figures over the pond, autumn leaves under summer trees, swing ropes hanging straight | Goats and the pond as since v0.11. The swing ropes: see below |

**The swing.** Swung out in all three of its pictures, and read as swinging in all three: "The girl on the swing looks like she is swinging normally and enjoying it" (4); "motion lines behind him show he is swinging" (29); "happily swinging on a swing set ... with motion lines showing she is moving" (39). No reader said it hung still. One reader added "The girl's swing ropes do not quite look like they come from directly above the seat, but it reads as swinging" (39).

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.31 | v0.32 | v0.33 | v0.34 | v0.35 |
|---|---|---|---|---|---|
| Pass | 63 | 63 | 63 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 1 | 1 | 0 | 1 |

Every template was screened in at least three pictures (52 in three, 4 in four, 4 in five, 2 in six and 2 in eleven; 409 scored items behind the verdicts). The one failure is `bucket_hat` (0.889), on the screen's one misread: a grandfather with a bucket on his head, standing with his hands on his hips, was "a boy in a white shirt, brown waistcoat and dark trousers" (74). The picture is identical to v0.34's, where the item had full marks, but the readers' words point at the drawing: v0.34's reader of it wrote "I can't see the bucket-wearing man's hair, so I can't tell his age". The bucket covers the grey hair and the cap that say his age.

## What reads least well (the v0.36 list)

| # | Template | v0.35 | What the readers saw | Fix for v0.36 |
|---|---|---|---|---|
| R1 | `bucket_hat` | 0.889 (9 items, 3 pictures); fails | The grandfather under the bucket: "a boy in a white shirt, brown waistcoat" (74), and in v0.34 "I can't see the bucket-wearing man's hair, so I can't tell his age" | Bench the grandfather's age under the bucket: grey hair showing below its rim, or his moustache. Or give the bucket to someone whose age shows without the head |
| R2 | `blocked_hose` | 0.917 (12 items, 3 pictures) | "Standing on or right beside the hose" (1), on the unchanged tier-4 garden | Watch |
| R3 | `ice_cream_drop` | 0.958 (12 items, 3 pictures) | The ice cream "has fallen", the dog offered as a cause (45), on an unchanged picture | Watch |
| R4 | `lost_balloon` | 0.967 (15 items, 5 pictures) | "Escaping", from her hand or someone else's (72), unchanged | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v035/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.36 |
|---|---|---|---|---|
| O1 | C | The storm pointer and the washing, on the same seed twice | Picture 63 | Keep the washing out of a storm pointer's picture |
| O2 | C | The swing's ropes "do not quite look like they come from directly above the seat" | Picture 39 | Watch: one remark in three pictures, and it reads as swinging |
| O3 | C | The gate's knob behind a head read as a bun | Picture 73, twice now | Keep a head clear of the gate's knob |
| O4 | C | Older ones: goats out of place, figures over the pond, the man's legs over the seesaw's plank, hair and clothes the wind does not move | Throughout | Notes for the pilot |

## Placement

All four tier-4 cells placed on v0.34's seeds under revision 33, the street's on v0.29 to v0.34's forced set, and all four pictures are unchanged. The tier-3 garden placed again on its seed. 20 of the set's 21 pictures came back identical to v0.34's; the tier-2 garden isomorph differs by its swing, now swung, and its raker. The tier-4 isomorph took 12 failed attempts, as in v0.33 and v0.34. The first probe pass left `walk_dog`, `dog_begs` and `windy_hat` short, the wind with fewer pictures to share since revision 33 keeps piles out of it, and two more probes filled them. All 82 records rebuild identical to the pixel, and the library passes the validator in full, 343 of 343.
