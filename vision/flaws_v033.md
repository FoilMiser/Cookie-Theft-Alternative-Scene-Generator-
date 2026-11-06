# v0.33 blind screen: what it found (the work list for v0.34)

The v0.33 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 59 probes. Keys, descriptions and scores are in `v033/`.

## Headline (the 21 pictures of the set)

| | v0.30 (21) | v0.31 (21) | v0.32 (21) | v0.33 (21) |
|---|---|---|---|---|
| Things | 0.990 | 1.00 | 0.991 | 0.990 |
| Actions | 0.992 | 0.996 | 0.988 | 0.992 |
| Inferences | 0.986 | 1.00 | 0.956 | 0.957 |
| Contradictions | 0.977 | 1.00 | 1.00 | 1.00 |
| All items | 0.989 | 0.998 | 0.986 | 0.988 |
| Misread items | 0 of 285 | 0 of 284 | 1 of 286 | 0 of 285 |
| Readers' remarks per picture (all screened pictures) | 5.19 | 3.51 | 3.28 | 3.19 |
| Oddities per picture, as logged by the scorers | 2.3 (at most 3) | 0.6 (at most 3) | 0.8 (at most 3) | 0.9 (at most 3) |

Across all 80 pictures 854 of 862 scored items had full marks, and none was misread.

**Every item under full marks in the set is on a picture identical to v0.32's.** 20 of the set's 21 pictures came back identical to the pixel; the new one, the tier-3 garden, has every item in full. The six under full marks are the dog on the hose ("may be standing on it", 1), the purple balloon twice ("as if it has just slipped away or is being grabbed", 7; "could be escaping from the child, or the child could be trying to catch a balloon that was never theirs", 25), the girl feeding the ducks ("she is not clearly throwing anything", 65), and the clouds of that same park, not named. The scorers gave four items under full marks in 301, one in 255 and three in 306.

## A retest, again

21 pictures, 20 of the set's and one probe, were identical to the pixel in v0.32 and v0.33 (`tpdb_work/retest33.py`).

| On the same 21 pictures | v0.32 | v0.33 |
|---|---|---|
| Items | 281 | 281 |
| Items with the same score in both | 274 | 274 |
| Remarks | 77 | 88 |

Seven items moved, three up and four down. Up: the begging dog's inference, and two of the dog on the hose's items, its misread now a half mark. Down: the two balloons, the girl and the ducks, and the clouds. Last time the moves were all down, and the gate's failure was among them; this time the gate's failure is on a picture that is new.

## The v0.32 list

| v0.32 reading | v0.33 result |
|---|---|
| R1 `blocked_hose` 0.833: "Only a single drop is shown, so it is unclear whether water is flowing" | **0.917** (12 items, 3 pictures); passes. Not changed: led in front of the front feet, or flattened wider, it read no better on the bench (`isolation_v033.md`). The goat and the other dog read in full: "The hose under and beyond the goat's feet looks squashed flat, so the goat seems to be blocking the water" (20); "A white dog with brown spots and a blue collar is standing on the hose, which squashes it and stops the water" (56). On the unchanged picture it moved up a step, the dog "right next to the hose, and may be standing on it" (1) |
| R2 `dog_begs` 0.944 | **1.00** (9 items, 3 pictures). Not changed |
| R3 `rain_coming` 0.944: "pointing upward at the cat" | **1.00** (9 items, 3 pictures). Revision 31 keeps anything up high 100 units from the fingertip. The new tier-3 garden's pointer reads "probably at the storm clouds", with "something on the fence, such as the painting or the cat" as a second reading, the cat at the fence's other end (55). Twice the washing on the line is offered instead (below) |
| O1 The kick arcs: "as though she is hovering slightly above the plank" | Gone with the arcs. The girl is stuck in all three of her pictures ("The man's end rests on the ground and his feet are planted, so the girl is stuck up high", 6), and "Nothing is floating or passing through anything else" (6, and alike in 9) |
| O2 A child on the seesaw "almost toddler-sized" | Not said in the three pictures of two children |
| O3 The hose in the wind | No hose sprays in a windy picture now. A frying pan does: "Despite the strong wind, the water from the pan falls fairly straight" (18) |
| O4 A figure behind the house "taller than its front door" | Not said. A note |
| O5 A child "just above the seesaw beam" | "The girl's feet sit at about the height of the plank and seem to dangle in front of it. That's plausible" (46). Watch |
| O6 Goats, figures over the pond, autumn leaves, a bicycle standing alone | Throughout, as since v0.11 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.29 | v0.30 | v0.31 | v0.32 | v0.33 |
|---|---|---|---|---|---|
| Pass | 64 | 63 | 63 | 63 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 1 | 1 | 1 | 1 |

Every template was screened in at least three pictures (51 in three, 5 in four, 4 in five, 2 in six, one in nine and one in ten; 407 scored items behind the verdicts). The one failure, `read_bench` (0.875), is one half mark among four items, one to a picture: a probe's woman in a yellow dress, seated reading, was read as "a child with short dark hair, in a yellow top, yellow shorts and red shoes" (39). The reading was seen; the reader was taken for a child. `blocked_hose`, last release's failure, passes.

## What reads least well (the v0.34 list)

| # | Template | v0.33 | What the readers saw | Fix for v0.34 |
|---|---|---|---|---|
| R1 | `read_bench` | 0.875 (4 items, 4 pictures); fails | The woman in yellow seated with a book: "a child with short dark hair ... in a yellow top, yellow shorts", who "could be a boy or a girl" (39). Readers have taken her for a girl standing, too (v0.32's scorers listed "a child" and "a girl") | Bench her seated: the dress over the knees as shorts is the likeliest cause. Or keep the bench reader to the cast's older adults |
| R2 | `lost_balloon` | 0.933 (15 items, 5 pictures) | "As if it has just slipped away or is being grabbed" (7); "a balloon that was never theirs" (25). Both pictures unchanged since v0.32, where they read in full | Watch |
| R3 | `blocked_hose` | 0.917 (12 items, 3 pictures) | The unchanged tier-4 garden, "may be standing on it" (1) | Watch |
| R4 | `ducks_bread` | 0.944 (9 items, 3 pictures) | "She is not clearly throwing anything" (65), unchanged since v0.32 | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v033/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.34 |
|---|---|---|---|---|
| O1 | C | The storm pointer and the washing: "She could be pointing at the storm clouds, or at the washing on the line (or both); her finger points up and to the right, roughly between the two" | Pictures 36, 60 | The pointing cone clear of washing on the line as well as of scored things (the washing is part of the setting, so revision 6's line check passes it) |
| O2 | C | Water in the wind: "Despite the strong wind, the water from the pan falls fairly straight" | Picture 18 | Revision 31's rule for every pour and spray, the can and the pan as well as the hose |
| O3 | C | The painted patch "very neat and rectangular, with sharp edges, even though the painter's roller is only at its top-left corner" | Picture 71; the roller in four pictures | Look at the roller's place against the patch |
| O4 | C | "The dustpan seems to be under the pointing girl's feet" | Picture 60 | Watch |
| O5 | C | Older ones: goats out of place, figures over the pond, autumn leaves under summer trees, the man's legs over the seesaw's plank | Throughout | Notes for the pilot |

## Placement

The garden, park and playground tier-4 cells placed on v0.32's seeds, and v0.29 to v0.32's template set, forced on v0.32's seed, placed the street's again in 12 s: all four pictures unchanged. The tier-3 garden's seed no longer placed under revision 31, its storm pointer kept from the cat on the fence, and it came from a seed search past its showcase seed, on a new seed after 11 failed. The five isomorphs came back identical to v0.32's, and the tier-4 one took 12 failed attempts. The first probe pass left `walk_dog`, `fishing` and `dog_begs` short, and three more probes filled them. All 80 records rebuild identical to the pixel.
