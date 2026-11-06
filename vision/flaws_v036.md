# v0.36 blind screen: what it found (the work list for v0.37)

The v0.36 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 61 probes. Keys, descriptions and scores are in `v036/`.

## Headline (the 21 pictures of the set)

| | v0.33 (21) | v0.34 (21) | v0.35 (21) | v0.36 (21) |
|---|---|---|---|---|
| Things | 0.990 | 0.990 | 0.971 | 1.00 |
| Actions | 0.992 | 1.00 | 0.996 | 1.00 |
| Inferences | 0.957 | 0.986 | 0.957 | 0.971 |
| Contradictions | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.988 | 0.995 | 0.982 | 0.996 |
| Misread items | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 |
| Readers' remarks per picture (all screened pictures) | 3.19 | 3.13 | 2.88 | 3.10 |
| Oddities per picture, as logged by the scorers | 0.9 (at most 3) | 0.5 (at most 3) | 0.2 (at most 3) | 0.6 (at most 3) |

Across all 82 pictures 873 of 876 scored items had full marks, and none was misread.

The set's two items under full marks are inferences, each half right: the duck in the tier-4 park is "among small pieces of bread", the girl "apparently feeding the duck", but the duck coming for it is not said (45); and the red balloon in the tier-3 park "has escaped", the reader unsure whether the girl lost it or it was someone else's (72), as in v0.35 on the same seed. The third item under full marks in the screen is a probe's tree, not named (42). The scorers gave none, two and one items under full marks, in 304, 283 and 289. Every reader named the clouds.

## A retest, a seventh time

60 pictures, 13 of the set's and 47 probes, were identical to the pixel in v0.35 and v0.36 (`tpdb_work/retest36.py`); the others changed with the grandfather's moustache, which is in every picture he is in, or with revision 34.

| On the same 60 pictures | v0.35 | v0.36 |
|---|---|---|
| Items | 576 | 576 |
| Items with the same score in both | 563 | 563 |
| Remarks | 163 | 175 |

13 items moved, 12 up and 1 down. The 12 up are all clouds, which v0.35's two readers who named nothing in the sky had missed; the one down is the probe's tree.

## The v0.35 list

| v0.35 reading | v0.36 result |
|---|---|
| R1 `bucket_hat` 0.889, failing | **1.00** (9 items, 3 pictures), the grandfather with his moustache and the bucket sat higher. On the seed of v0.35's misread: "Old man, front centre: white hair, grey moustache, white shirt, brown waistcoat, dark trousers, metal bucket upside down on his head" (74). The other two wearers are a bearded man (12) and the grandmother, read under the bucket as an "Older man with grey hair, glasses" (01): her age right, her sex not, as v0.34's reader of the same layout had her, with the item credited |
| R2 `blocked_hose` 0.917 | **1.00** (12 items, 3 pictures). The tier-4 garden placed on another layout under revision 34 (below) |
| R3 `ice_cream_drop` 0.958 | **1.00** (12 items, 3 pictures). Not changed |
| R4 `lost_balloon` 0.967 | **0.967** (15 items, 5 pictures). "Has escaped", the reader unsure whose it was (72), as in v0.35 on the same seed. Watch |
| O1 The storm pointer and the washing | Revision 34 takes the washing off the line in her picture. The item reads in full in all three storm pictures, but the empty line is offered in the washing's place: "could be pointing at the storm clouds or at the empty washing line; nothing specific is visible where her finger points", and "The empty washing line could mean the washing has already been taken in because of the coming rain" (63). With the washing gone, that picture placed again and she stands on the fork sweeper's dustpan ("Pointing woman's feet seem to stand on the red dustpan", scorer c) |
| O2 The swing's ropes | Read as swinging in all three of its pictures; one scorer noted a reader's word on "the angle of the swing ropes against the motion lines" that ended "reads as swinging" (04) |
| O3 The gate's knob behind a head | **Not fixed.** Revision 34 keeps the box round every face 16 px clear of the knob, and the box is drawn round the eyes and mouth. The sweeper on the path stands in profile, his face turned from the gate, and the back of his hair covers the knob, 8 px past the box: the picture came back identical to v0.35's, and he was "a woman with dark hair in a bun, wearing a green top and beige trousers" (73), the knob read as a bun a third time. The item, sweeping, reads in full |
| O4 Goats, figures over the pond, the man's legs over the seesaw's plank, hair and clothes the wind does not move | As before: goats out of place (58, 66), a boy over the pond's outline (64), "a strong wind is shown but the flowers, potted plants and tree are not bending" (08) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.32 | v0.33 | v0.34 | v0.35 | v0.36 |
|---|---|---|---|---|---|
| Pass | 63 | 63 | 64 | 63 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 1 | 0 | 1 | 0 |

Every template was screened in at least three pictures (52 in three, 4 in four, 4 in five, 2 in six and 2 in eleven; 409 scored items behind the verdicts), and all 64 pass. The lowest are `ducks_bread` (0.944) and `lost_balloon` (0.967), each on one half-marked inference.

## What reads least well (the v0.37 list)

| # | Template | v0.36 | What the readers saw | Fix for v0.37 |
|---|---|---|---|---|
| R1 | `ducks_bread` | 0.944 (9 items, 3 pictures) | The duck "among small pieces of bread", the girl "apparently feeding the duck", without the duck coming for it (45) | Watch: one half mark, in the busiest picture of the set |
| R2 | `lost_balloon` | 0.967 (15 items, 5 pictures) | "Has escaped", whose unsure (72), the second screen running on that seed | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v036/scores_summary_a.md` to `_c.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.37 |
|---|---|---|---|---|
| O1 | C | The gate's knob behind a head in profile, read as a bun a third time, and now as a woman's | Picture 73, unchanged since v0.35 | Keep the whole head clear, hair included: the face's box widened by half its width each side, or the head's own mask. Rebuild picture 73's seed and look at it before the design tests |
| O2 | C | The storm pointer standing on the fork sweeper's dustpan | Picture 63, placed again in v0.36 when the washing came off | Make the fork sweeper's dustpan, and the broom's, a ground thing no one else's feet stand on (revision 20's rule for an event's things) |
| O3 | C | The empty washing line offered as what the storm pointer points at, and as "completely empty, with no clear reason" | Picture 63 | Watch. If it comes back, take the line out of a storm pointer's picture, posts and all |
| O4 | C | A second storm pointer read as perhaps pointing "at the cat on the fence" | Picture 57, unchanged | Watch: the item reads in full, and v0.35's reader offered the fence |
| O5 | C | The market stall's right leg seems to stand on the small crate under it | Pictures 48 and 53, one reader | Watch, or move the crate a little clear of the leg |
| O6 | C | Older ones: goats out of place, figures over the pond, hair and clothes the wind does not move, the grandmother read as an older man where her bun does not show (01, 10, as in v0.34) | Throughout | Notes for the pilot |

## Placement

All four tier-4 cells placed on v0.35's seeds under revision 34, the street's on v0.29 to v0.35's forced set. The tier-4 garden placed on its tenth layout, its sixth having had a face beside the gate's knob; the park and the street changed only with the grandfather's moustache, and the playground not at all. 13 of the set's 21 pictures came back identical to v0.35's, and 47 of the 61 probes; the probe for `walk_dog` and `dog_begs` is new. The tier-4 isomorph took 12 failed attempts, as in v0.33 to v0.35. All 82 records rebuild identical to the pixel, and the library passes the validator in full, 345 of 345.
