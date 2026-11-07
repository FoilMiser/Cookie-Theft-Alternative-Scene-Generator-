# v0.40 blind screen: what it found (the work list for v0.41)

The v0.40 screen read the set's 21 pictures and 73 probes with the prompts of v0.39 (`screen_prompts.md`): twelve readers of seven or eight pictures, four scorers of 23 or 24, the oddity tally by angle as in v0.39. Keys, descriptions and scores are in `v040/`.

One reader described the wrong picture. Reader 7's description of picture 55, the windy garden, was of picture 56, the park, whose own description says "I couldn't find any difference between this picture and pic_55". Picture 55 was read again by a fresh reader and scored by a fresh scorer (`desc_pic_55.md`, `scores_e.json`, `scores_summary_e.md`; the prompts `tpdb_work/v040prompts/reader_13_pic55.txt` and `scorer_e.txt`). Reader 7's description is kept as `tpdb_work/set40/desc_pic_55_reader7_wrong.md`, and the oddity it put on picture 56 was dropped from the merged scores.

## Headline (the 21 pictures of the set)

| | v0.36 (21) | v0.37 (21) | v0.38 (21) | v0.39 (21) | v0.40 (21) |
|---|---|---|---|---|---|
| Things | 1.00 | 1.00 | 1.00 | 1.00 | 0.991 |
| Actions | 1.00 | 0.996 | 1.00 | 1.00 | 0.996 |
| Inferences | 0.971 | 0.971 | 0.985 | 1.00 | 0.986 |
| Contradictions | 1.00 | 0.977 | 1.00 | 1.00 | 1.00 |
| All items | 0.996 | 0.993 | 0.998 | 1.00 | 0.993 |
| Misread items | 0 of 285 | 0 of 285 | 0 of 286 | 0 of 287 | 0 of 287 |
| Readers' remarks per picture (all screened pictures) | 3.10 | 2.82 | 3.38 | 3.10 | 3.04 |
| Oddities per picture, as logged by the scorers | 0.6 (at most 3) | 0.4 (at most 3) | 0.8 (at most 3) | 0.8 (at most 3) | 0.5 (at most 3) |

Across all 94 pictures, 1011 of the 1014 scored items had full marks and none was misread. All three items under full marks are in the set:
- **The catcher, half right (35, the tier-2 garden):** "ready to catch the ball or just having thrown it". The catch is the same as in v0.39, where it had full marks; only the broom's heap in that picture was redrawn.
- **The dog on the hose, half right (57, the tier-4 garden):** the cause was given only in the unsure section, beside "she may just be starting to water".
- **The clouds of the tier-3 street's isomorph, scored 0 (07):** a setting item, which the gate leaves out.

The five scorers gave 1, 1, 1, 0 and 0 items under full marks, out of 228, 270, 260 (picture 55 apart), 241 and 15.

**What the full marks rest on.** The scorers listed 21 credits they gave in full where the free description commits and the unsure section adds another reading. v0.39's listed 11, v0.38's 23. If those 21 are halved, 59 of 64 templates pass (`tpdb_work/strict40.py`). Five fall, each on one or two such credits:
- `floating_box` (0.833, 9 items): the box in mid-air, but the unsure section "also allows 'falling or thrown in'";
- `play_catch` (0.833, 6 items);
- `ladder_nothing`, `sweep_fork` and `water_upward` (0.889, 9 items each).

`windy_hat`, the one template under the strict count in v0.39, passes it now, at 0.933 in five pictures.

## A retest, an eleventh time

28 pictures, 13 of the set's and 15 probes, are identical to the pixel in v0.39 and v0.40 (`tpdb_work/retest40.py`). Only the windy hat, the hose, the goat, the heaps and the ice-cream eater changed, so every picture without them came back unchanged.

| On the same 28 pictures | v0.39 | v0.40 |
|---|---|---|
| Items | 328 | 328 |
| Items with the same score in both | 326 | 326 |
| Remarks | 106 | 93 |

Two items moved, both up by half a mark, and both were on v0.39's list: the man sweeping with the giant fork and the dog that wants a walk (v0.39's R3 and R2). They moved with nothing changed in their pictures.

## The v0.39 list

| v0.39 reading | v0.40 result |
|---|---|
| R1 `windy_hat` 1.00, 0.889 read strictly | **1.00, and 0.933 read strictly** (15 items, 5 pictures). Revision 38's cast reaches for the hat with one hand, the other at the side. "He reaches up with one arm toward an orange cap" (55), and the hands-up reading is gone. Once "it could also be read as waving or pointing at something" (47) |
| R2 `dog_wants_walk` 0.917 | **1.00** (10 items, 5 pictures), not changed. The half mark of v0.39 came back in full on the identical picture |
| R3 `sweep_fork` 0.944 | **1.00** (9 items, 3 pictures), not changed. Up on the identical picture; 0.889 read strictly |
| R4 `ice_cream` 0.95 | **1.00** (17 items, 17 pictures). Revision 38 keeps the eater at least 170 px tall, and no eater is "small and pink" |
| O1 The summer heap's green leaves | **Changed, not gone.** The heap is now dry leaves, leaf-shaped (`draw.HEAP40` D). No reader finds the leaves green, but five pictures from three readers find brown leaves odd under green trees, as v0.38's autumn heap was found: "One odd thing is that the leaves being swept are brown autumn leaves, while all the trees and hedges are fully green and it looks like a bright summer day" (71); "The brown leaves are slightly odd when the trees are green and flowers are blooming" (38); and alike in 04, 33 and 35. In v0.39, five pictures from four readers |
| O2 The goat's graze: head in the tuft, thin body, rump high | **The head and body remarks are gone.** None of the head in the tuft (three in v0.39), none of "thin and angular". Once at 135 "The goat's body is drawn somewhat from behind with its head turned, which makes its pose a little awkward to read" (38). Loose in a park or garden in seven pictures, as before (O6) |
| O3 The grandfather's arms to the nozzle | One remark against two: "The older man's arm holding the nozzle is held stiffly straight out sideways, which looks slightly awkward" (68, the tier-3 garden). The two hands now hold the nozzle and the hose apart |
| O4 The pinched hose read as a puddle | **Not seen**, in six pictures |
| O5 A walker's feet | **Not seen**, with the walk unchanged (`TPDB_WALK40` O). The bench's back foot "seems to point backward" remains (`isolation_v040.md`), below |
| O6 Older ones | As before: goats out of place (10, 22, 25, 38, 41, 73, 78); figures over the thing beside them (the seesaw man's legs over the plank 01, 11, 94; a girl on the slide's chute 17; figures over the pond 13, 32); wind that moves only the hat (47) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.36 | v0.37 | v0.38 | v0.39 | v0.40 |
|---|---|---|---|---|---|
| Pass | 64 | 63 | 64 | 64 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 1 | 0 | 0 | 0 |

Every template was screened in at least three pictures, and all 64 pass. By count: 41 in three, 11 in four, 5 in five, 4 in six, 1 in seven, 1 in twelve and 1 in seventeen, with 463 scored items behind the verdicts.

The lowest are each on one half mark:
- `play_catch` (0.917, 6 items, 3 pictures), on a picture whose catch v0.39 read in full;
- `blocked_hose` (0.979, 24 items, 6 pictures).

Per angle (`v040/gate_yaw.json`), all 17 (template, angle) pairs pass. The lowest is `blocked_hose` at 45 (0.938), on the same half mark.

## What reads least well (the v0.41 list)

| # | Template | v0.40 | What the readers saw | Fix for v0.41 |
|---|---|---|---|---|
| R1 | `play_catch` | 0.917; 0.833 read strictly (6 items, 3 pictures) | The catcher "ready to catch the ball or just having thrown it" (35), on a picture whose catch v0.39 read in full; a reverse throw offered as option (b) (35) | Reader variance on an unchanged picture. Watch; a fourth and fifth probe |
| R2 | `floating_box` | 1.00; 0.833 read strictly (9 items, 3 pictures) | The box in mid-air, the unsure section allowing "falling or thrown in" (36, 42) | A box too high and too still to be falling: drawn higher, with no motion cue, or with a shadow under it on the grass; bench |
| R3 | `ladder_nothing`, `sweep_fork`, `water_upward` | 1.00; 0.889 read strictly each | The ladder's top "could touch the distant hills" (13, 16); the fork "scrape[s] dirt and gravel" (46); the water "falling from above" as a second reading (72) | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v040/scores_summary_a.md` to `_e.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.41 |
|---|---|---|---|---|
| O1 | C | The heap's brown leaves under green trees, five pictures from three readers. It is the third drawing to draw a remark: v0.38's autumn leaves, v0.39's green ones, v0.40's dry ones | 04, 33, 35, 38, 71 | The season, not the leaves: a heap of something else a broom sweeps in summer (on the bench cut grass on a path read as a green dustpan or dome, and grit as dust or a rock, `isolation_v039.md`, `isolation_v040.md`), or leave it as a note for the pilot |
| O2 | C | The begging dog in profile: "stretched-upright body and far-back head tilt make its shape look odd/awkward; could read as jumping up" (79), "upright sitting pose looks a little stiff and human-like" (89) | 79, 89 | Look at `beg` at 90 beside 45, where it drew nothing |
| O3 | C | The stalking cat at 45: "legs are bunched up and a bit tangled under its body" (03, 75) | 03, 75 | Look at `stalk_paw` at 45: part the legs |
| O4 | C | The woman in the yellow dress (Mei) called "girl" in 6 of her 27 pictures (5 of 24 in v0.39), credited on the action | Throughout | As Ben's in v0.39: an adult's cues, bench |
| O5 | C | The goat: loose in a park or garden (seven pictures); its pose "a little awkward to read" from behind (38); the body's hunch at 45 and 135 on the bench (`isolation_v040.md`) | 10, 22, 25, 38, 41, 73, 78 | The hunch is the redrawn goat's body; a body round for v0.41. Out of place: notes for the pilot |
| O6 | C | The walking back foot on its toe, "seems to point backward" on the bench, though not in the screen | Bench | A shoe with a toe cap, or the back foot flatter; bench |
| O7 | C | Older ones: figures over the prop beside them (01, 11, 13, 17, 32, 94); goats out of place; wind that moves only the hat | Throughout | Notes for the pilot, as before |

## Placement

**The set.**
- **Tiers 1 to 3.** Every cell placed again on its v0.39 seed and layout under revision 38.
- **Tier 4.** The garden, park and playground placed on v0.39's seeds, the street on v0.29 to v0.39's forced set, each on the same layout as in v0.39.
- **What changed.** 13 of the 21 pictures are identical to v0.39's. The other 8 differ only where the heap, the goat or the hose is drawn: seven cells (two at tier 1, one at tier 2, one at tier 3, three at tier 4) and one isomorph.
- **The isomorphs.** All five came back as in v0.39, four identical to the pixel and the fifth changed only by its sweeper's heap.

**The probes.**
- **The first pass** (`probes.py 3`, five for `windy_hat` and `dog_wants_walk`) left `windy_hat` at three and `dog_begs` short.
- **The pass stratified by angle** added 13 probes and filled `dog_begs`.
- **Two more windy-hat probes** were placed in the park and the street (`tpdb_work/probe_windy40.py`), as the garden's company, the broom, cannot share a gust.
- **Identical probes.** 15 of the 73 probes are identical to the pixel to v0.39's.

All 94 records rebuild identical to the pixel, and the library passes the validator in full, 392 of 392.
