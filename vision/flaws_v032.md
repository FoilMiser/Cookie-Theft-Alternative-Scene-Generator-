# v0.32 blind screen: what it found (the work list for v0.33)

The v0.32 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 47 probes. Keys, descriptions and scores are in `v032/`.

## Headline (the 21 pictures of the set)

| | v0.29 (21) | v0.30 (21) | v0.31 (21) | v0.32 (21) |
|---|---|---|---|---|
| Things | 0.981 | 0.990 | 1.00 | 0.991 |
| Actions | 1.00 | 0.992 | 0.996 | 0.988 |
| Inferences | 0.985 | 0.986 | 1.00 | 0.956 |
| Contradictions | 1.00 | 0.977 | 1.00 | 1.00 |
| All items | 0.991 | 0.989 | 0.998 | 0.986 |
| Misread items | 0 of 284 | 0 of 285 | 0 of 284 | 1 of 286 |
| Readers' remarks per picture (all screened pictures) | 5.15 | 5.19 | 3.51 | 3.28 |
| Oddities per picture, as logged by the scorers | 2.3 (at most 3) | 2.3 (at most 3) | 0.6 (at most 3) | 0.8 (at most 3) |

Across all 68 pictures 769 of 776 scored items had full marks, and one was misread. Things were 0.998, actions 0.992, inferences 0.973 and contradictions 1.00.

**Read the fall as two pictures, and one of them as the readers.** Of the set's six items under full marks, four are on pictures identical to the pixel in v0.31, where all four had full marks (below). Three are one gag, the dog on the hose in the tier-4 garden: the reader saw "a drop of water at the tip" and that "the dog's back foot looks as if it may be standing on the hose", and took the dog for one that "might get sprayed" (28). The fourth is a dog that "could be begging for the ice cream or simply greeting the man" (1). The other two are on a picture new in this release, the tier-3 garden, and one has a reason: a woman points up at the storm clouds from right under a cat on the fence, and was read as "pointing upward at the cat" (51). The same reader named no tree there.

**Read the remarks as the readers again.** Nine new readers made 223 remarks on 68 pictures, 3.28 a picture, from 2.71 to 4.43 each, as low as v0.31's nine. On the 19 pictures identical in both screens remarks fell from 79 to 67 with nothing changed. Of the three scorers, one gave one item under full marks in 244, and the others three each in 288 and 244. Each listed what it credited in full with a caveat, such as a bird described standing for one pecking (37, 40) and "peg up (or unpeg)" (53).

## A retest, again

19 pictures, 17 of the set's and two probes, were identical to the pixel in v0.31 and v0.32, so they were read twice by fresh readers and scorers with nothing changed (`tpdb_work/retest32.py`).

| On the same 19 pictures | v0.31 | v0.32 |
|---|---|---|
| Items | 246 | 246 |
| Items with the same score in both | 242 | 242 |
| Remarks | 79 | 67 |

Four items moved, all down: three on the dog on the hose, which is the gate's one failure, and the begging dog's inference. Last time the retest's one move was also down, and it was also the gate's one failure (`jump`). Two releases running, the one template that failed did so on a picture that had not changed.

## The v0.31 list

| v0.31 reading | v0.32 result |
|---|---|
| R1 `jump` 0.833: "could be trying to reach the ball or just cheering" | **1.00** (3 items, 3 pictures). Revision 30 keeps the jumper 200 units from a ball or kite stuck in a tree. The street's jumper is weighed and set aside: "The jumping boy could be jumping for joy or trying to reach the ball, but he is not under the tree, so I read it as jumping for joy" (16). One other still offers "jumping for joy or jumping/reaching toward something", and was credited (51) |
| R2 `hang_laundry` 1.00, "hanging the T-shirt up or taking it down" | **1.00** (3 items, 3 pictures). Not changed. Once in three, as before: "could be hanging the washing up or taking it down" (53) |
| O1 The man on the seesaw's low end | Taken off the list after the bench (turned away, or both legs behind the plank, read no better, and legs out was set aside on looking; `isolation_v032.md`). In his three pictures he drew one remark: "The seesaw plank seems to pass behind or among the old man's legs" (18) |
| O2 Watering under storm clouds | Revision 30: watering by hose or can under a clear sky only. In the 12 pictures with watering, no reader remarks on the sky |
| O3 The girl stuck up high "may look like she is hovering" | The handle raised with her (`HANDLE32`), as the bench found the readers' words were about her fists above it. "Holding the handle" in all three pictures, and nothing of the fists. One reader still saw her hover, and named the cause: "The motion arcs under the girl's feet make her look as though she is hovering slightly above the plank" (18) |
| O4 A box held at the side "as if it is half floating" | Carried on the whole forearm (`TPDB_BOX` V). "Carrying a cardboard box in both arms" (3, 52), "carried by the delivery man" (59), and no box carried floats |
| O5 A bicycle standing on its own, a toddler on a swing, a hose standing up | Notes, as before |
| O6 Autumn leaves beside summer trees | Once more (41, 42). A note for the pilot |
| O7 Goats out of place, figures over the pond, wide shadows | Throughout, as since v0.11 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.28 | v0.29 | v0.30 | v0.31 | v0.32 |
|---|---|---|---|---|---|
| Pass | 61 | 64 | 63 | 63 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 3 | 0 | 1 | 1 | 1 |

Every template was screened in at least three pictures (53 in three, 2 in four, 6 in five, 2 in six and one in nine; 401 scored items behind the verdicts). The one failure, `blocked_hose` (0.833), is three items of one picture, identical to v0.31's, where they had full marks; its two other pictures, a goat and a dog on the hose, read in full. `jump`, last release's failure, passes at 1.00.

## What reads least well (the v0.33 list)

| # | Template | v0.32 | What the readers saw | Fix for v0.33 |
|---|---|---|---|---|
| R1 | `blocked_hose` | 0.833 (12 items, 3 pictures); fails | "Only a single drop is shown, so it is unclear whether water is flowing. The dog's back foot looks as if it may be standing on the hose" (28), on a picture unchanged since v0.31 | Bench the paw: the foot squarely on the hose, the hose pinched under it, as it read in the goat's and the other dog's pictures. Watch first if the bench finds nothing |
| R2 | `dog_begs` | 0.944 (9 items, 3 pictures) | "Could be begging for the ice cream or simply greeting the man" (1), on a picture unchanged since v0.31 | Watch |
| R3 | `rain_coming` | 0.944 (9 items, 3 pictures) | "Pointing upward at the cat with a surprised face" (51): a cat on the fence right where she points | A rule: nothing else of interest on the pointer's line to the sky (a cat on the fence, a bird on a post) |

## Unintended oddities

Named kinds, from the scorers' lists (`v032/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.33 |
|---|---|---|---|---|
| O1 | C | The motion arcs under a stuck rider's feet "make her look as though she is hovering slightly above the plank" | Picture 18 | Move the kick arcs below the feet, clear of the plank, or drop them for the stuck rider |
| O2 | C | Of two children on a seesaw, one "drawn noticeably smaller than the other child, almost toddler-sized" | Pictures 5, 7 (one reader) | Cast the two riders of an age, or note it |
| O3 | C | "The wind is strong enough to blow a cap off, but the hose water is not bent by it" | Picture 44 | Bend the spray with the wind, or keep the hose out of windy pictures |
| O4 | C | A figure behind the house "looks taller than its front door" | Picture 68 | A note on depth |
| O5 | C | A child on a seesaw's low end "could be sitting just above the seesaw beam rather than firmly on it" | Picture 50 | Watch |
| O6 | C | Older ones: goats out of place, figures over the pond, autumn leaves under summer trees, a bicycle standing alone, figures with no purpose shown | Throughout | Notes for the pilot, as since v0.11 |

## Placement

The garden, park and playground tier-4 cells placed on v0.31's seeds, and their pictures are unchanged. The street's did not, with watering under a clear sky only and the jumper kept clear of the ball in the tree, and 38 more seeds failed. v0.29 to v0.31's template set, forced on the same seed, placed in 12 s, as the RUNBOOK says after a dozen seeds. The tier-3 garden came from a seed search past its showcase seed, as in v0.31, on a new seed. The tier-4 isomorph took 12 failed attempts across its three seed lists. The first probe pass left `walk_dog` and `dog_begs` short, and one more probe filled both. All 68 records rebuild identical to the pixel.
