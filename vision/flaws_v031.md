# v0.31 blind screen: what it found (the work list for v0.32)

The v0.31 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 50 probes. Keys, descriptions and scores are in `v031/`.

## Headline (the 21 pictures of the set)

| | v0.28 (21) | v0.29 (21) | v0.30 (21) | v0.31 (21) |
|---|---|---|---|---|
| Things | 1.00 | 0.981 | 0.990 | 1.00 |
| Actions | 0.996 | 1.00 | 0.992 | 0.996 |
| Inferences | 0.879 | 0.985 | 0.986 | 1.00 |
| Contradictions | 1.00 | 1.00 | 0.977 | 1.00 |
| All items | 0.984 | 0.991 | 0.989 | 0.998 |
| Misread items | 0 of 283 | 0 of 284 | 0 of 285 | 0 of 284 |
| Readers' remarks per picture (all screened pictures) | 5.14 | 5.15 | 5.19 | 3.51 |
| Oddities per picture, as logged by the scorers | 2.0 (at most 3) | 2.3 (at most 3) | 2.3 (at most 3) | 0.6 (at most 3) |

Across all 71 pictures 783 of 784 scored items had full marks. One had a half mark and none was misread: a child jumping for joy, which "could be trying to reach the ball or just cheering" (31).

**Read the last two rows as the readers, not the pictures.** Nine new readers made 249 remarks on 71 pictures, 3.51 a picture. Every one of them made fewer than the fewest of v0.30's nine (2.62 to 4.43 a picture, against 4.50 to 6.12). On the 12 pictures that came back identical to the pixel (below), remarks fell from 65 to 45 with nothing changed. The scorers' oddity row follows the remarks it is drawn from. So neither row says anything about this release's drawings, and the comparisons below are made only where a picture's own words can be read.

**Read the top rows with the scorers in mind.** Two of the three scorers gave no item under full marks, in 236 and 253 items, as one of v0.30's did. Each listed what it credited in full with a caveat: a bird "standing on the ground" for one pecking (7, 44), a bird "about to take it" for one pecking at the sandwich (2), a grandmother read as "an old man" (17), and second readings offered beside the right one. A stricter scorer would halve some of these. The 0.998 is a ceiling as much as a result.

## A retest, again

12 pictures, 11 of the set's and one probe, were identical to the pixel in v0.30 and v0.31, so they were read twice by fresh readers and scorers with nothing changed (`tpdb_work/retest31.py`).

| On the same 12 pictures | v0.30 | v0.31 |
|---|---|---|
| Items | 141 | 141 |
| Items with the same score in both | 137 | 137 |
| Remarks | 65 | 45 |

Four items moved, three up and one down, each a half mark. The one down is the screen's only half mark, and it is the gate's one failure: `jump` was 1.00 last time, on two of the same pictures and one other.

## The v0.30 list

| v0.30 reading | v0.31 result |
|---|---|
| R1 `hang_laundry` 0.833: washing under storm clouds | **1.00** (3 items, 3 pictures). No washing is hung under a dark sky now. One reader still offers both: "Whether the man is hanging the T-shirt up or taking it down: his hands are at the pegs, so it reads either way", and then, the jeans being up already, "hanging washing out" "seems the more natural reading" (33). The design tests found the same under a clear sky, so the sky was not the whole of it |
| R2 `dog_begs` 0.944 | **1.00** (9 items, 3 pictures). The cone not changed: the bench found nothing to choose (`isolation_v031.md`) |
| R3 `dog_reading` 0.967 | **1.00** (15 items, 5 pictures). Not changed |
| R4 `lost_balloon` 0.967 | **1.00** (15 items, 5 pictures). Not changed |
| O1 The seesaw: "the man's legs appear to go through or around the plank" | Riders astride, the far leg behind the plank, raised so the hips rest on it. Plank remarks in **2 of 6** seesaw pictures, against 5 of 6 in v0.30, and none in the three pictures of two children. Both are the man on the low end, and both readers settle it: "He mostly reads as sitting on it" (20), "he could be read as sitting on the plank end or sitting just beside it with the plank behind his legs" (47). The girl stuck up high once "may look like she is hovering slightly, but she mostly reads as seated" (20), a cost of the raise |
| O2 The bearded man's vest, "a jagged edge against the white shirt" | Gone. The man is in 13 pictures, and no reader remarks on his vest |
| O3 The fish's limb as a bent trunk | Not changed, as the bench's redraw was worse. No remark on the limb in its three pictures, and "lying on a branch" once (50). Off the list |
| O4 The hand and the sandcastle | Gone. No remark in the three sandbox pictures, and the spade is named in two: "probably a toy spade, next to the castle" (54), "a little spade/scoop" (5) |
| O5 A book that floats ahead of the hands | Not changed. No remark in five pictures of a walker reading |
| O6 The feed bag as "a small box" | Not changed. No remark |
| O7 The reel over the bed's edge | Gone. The reel is in 10 pictures, and no reader remarks on it |

The O rows that read as gone include three that were not changed (O3, O5, O6). With readers who remark a third less, a row that went to none is weak evidence for any one of them. The seesaw is the exception worth the name, as it fell from five pictures to two where most rows fell by a third, and the two that are left are both one figure.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 |
|---|---|---|---|---|---|
| Pass | 63 | 61 | 64 | 63 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 3 | 0 | 1 | 1 |

Every template was screened in at least three pictures (52 in three, 4 in four, 5 in five, 2 in six and one in nine; 401 scored items behind the verdicts). The one failure, `jump` (0.833), is one half mark among three items, on a picture identical to v0.30's, where that item had full marks. It is the retest's one move downward.

## What reads least well (the v0.32 list)

| # | Template | v0.31 | What the readers saw | Fix for v0.32 |
|---|---|---|---|---|
| R1 | `jump` | 0.833 (3 items, 3 pictures); fails | "Could be trying to reach the ball or just cheering" (31), on a picture unchanged since v0.30. Elsewhere "It isn't clear why the boy is cheering. Nothing obvious is happening near him" (28) | Watch. If it falls again, give the jump something to be glad about, or keep it away from a ball in a tree |
| R2 | `hang_laundry` | 1.00 | Still "hanging the T-shirt up or taking it down", under a clear sky (33, and design test 3) | A basket at the feet, if the next screen halves it again |

## Unintended oddities

Named kinds, from the scorers' lists (`v031/scores_summary_a.md` to `_c.md`), most worth doing first. With this screen's readers the list is short, which is a reason to keep the older notes in mind and not to strike them.

| # | Sev | Oddity | Where | Fix for v0.32 |
|---|---|---|---|---|
| O1 | B | The man on the seesaw's low end: "sitting on the plank end or sitting just beside it" | Pictures 20, 47, and both men in the design tests | The pose: a knee up and a shin across a rising plank. A pose with both feet on the ground ahead of the plank's end, so the shin does not cross it |
| O2 | C | Watering under storm clouds: it "could be read as ironic or pointless, but she does not seem to have noticed the clouds" | Picture 59 | The rule the washing got: watering with a hose or can under a clear sky only |
| O3 | C | The girl stuck up high "may look like she is hovering slightly" | Picture 20 | Less of the raise for the stuck rider, whose legs hang and do not cross the plank |
| O4 | C | A box held at the side "as if it is half floating" | Picture 63 | Look at the carrier's grip |
| O5 | C | A bicycle standing on its own, a toddler on a swing with no one to push, a hose "standing up by itself" | Pictures 34, 37, 59 | Notes, as before |
| O6 | C | Autumn leaves beside summer flowers and green trees | Pictures 45, 69 | A note for the pilot |
| O7 | C | Older ones: goats out of place, figures over the pond, wide shadows | Throughout | Notes for the pilot, as since v0.11 |

## Placement

The park, street and playground tier-4 cells placed on v0.30's seeds. The garden's did not, with the reel moved and no washing under a dark sky: 13 seeds failed before one placed. The tier-3 garden came from a seed search past its showcase seed. The tier-4 isomorph took 12 failed attempts across its three seed lists. The first probe pass left `walk_dog` and `dog_begs` short, and two more probes filled them. All 71 records rebuild identical to the pixel.
