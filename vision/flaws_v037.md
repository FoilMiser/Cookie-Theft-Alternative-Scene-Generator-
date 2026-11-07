# v0.37 blind screen: what it found (the work list for v0.38)

The v0.37 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 61 probes. Keys, descriptions and scores are in `v037/`.

## Headline (the 21 pictures of the set)

| | v0.34 (21) | v0.35 (21) | v0.36 (21) | v0.37 (21) |
|---|---|---|---|---|
| Things | 0.990 | 0.971 | 1.00 | 1.00 |
| Actions | 1.00 | 0.996 | 1.00 | 0.996 |
| Inferences | 0.986 | 0.957 | 0.971 | 0.971 |
| Contradictions | 1.00 | 1.00 | 1.00 | 0.977 |
| All items | 0.995 | 0.982 | 0.996 | 0.993 |
| Misread items | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 |
| Readers' remarks per picture (all screened pictures) | 3.13 | 2.88 | 3.10 | 2.82 |
| Oddities per picture, as logged by the scorers | 0.5 (at most 3) | 0.2 (at most 3) | 0.6 (at most 3) | 0.4 (at most 3) |

Across all 82 pictures 870 of 876 scored items had full marks, and none was misread.

The set's four items under full marks are each half right, three on pictures identical to v0.36's and the fourth on the street isomorph, changed by the crate alone: the scoop in the tier-3 playground "has fallen", the reader unsure whether the dog knocked it off (10); the water from the tier-4 street's can, which "could be read as water pouring onto the planter, or as water shooting upward/sideways", offered only in the unsure section (21); the bird by the sandwich in the tier-4 street's isomorph, "just standing there, or about to steal" (23); and the girl feeding the ducks in the tier-4 park, holding "a small brown item" that is only possibly the bread, "fairly far from the pond for throwing food" (45). The probes' two are the washing (12, below) and an ice cream, "a small pink thing up near her mouth, probably an ice cream", or "a sweet" (69). The scorers gave four, one and one items under full marks, in 304, 283 and 289. Every reader named the clouds.

## A retest, an eighth time

75 pictures, 16 of the set's and 59 probes, were identical to the pixel in v0.36 and v0.37 (`tpdb_work/retest37.py`); the others changed with revision 35: the five street pictures with the spare crate, and the two probes the rules were written for.

| On the same 75 pictures | v0.36 | v0.37 |
|---|---|---|
| Items | 783 | 783 |
| Items with the same score in both | 775 | 775 |
| Remarks | 226 | 209 |

8 items moved, 3 up and 5 down. Up: a balloon let go of, the duck coming for the bread, a probe's tree. Down: the scoop, the girl throwing the bread, the upward water, the washing and the ice cream, each by half a mark. Every template in the v0.38 list below lost its half mark on a picture that had full marks for it in v0.36.

## The v0.36 list

| v0.36 reading | v0.37 result |
|---|---|
| R1 `ducks_bread` 0.944 | **0.944** (9 items, 3 pictures). The half mark moved: the duck coming for the bread reads in full, and the girl throwing it is half said (45, identical) |
| R2 `lost_balloon` 0.967 | **1.00** (15 items, 5 pictures). Not changed |
| O1 The gate's knob behind a head in profile, read as a bun three times | **Fixed.** Revision 35 measures the knob against the figure's drawing: no pixel of a person's mask within 16 px of its edge. Picture 73's seed, rebuilt first, put the sweeper lower down the path, and he is "a boy with short dark hair, a green shirt and khaki trousers" (73), with no word of a bun. Every reader of the five garden design tests who names the knob gives it to the gate ("a diagonal brace and a round dark knob") |
| O2 The storm pointer on the fork sweeper's dustpan | **Fixed.** The sweepers' heaps, and the fork sweeper's dustpan, are things on the ground no one else's feet stand on, whichever is placed first (revision 35). Picture 63's seed, rebuilt, stands her on open lawn; no reader of it or of the design tests puts anyone on a heap or a pan |
| O3 The empty line offered as what the storm pointer points at | **Gone.** Rebuilt with the first two rules alone, she pointed up through the empty line's post, and revision 35 takes the clothesline out of a storm pointer's garden, posts and all, as revision 19 does for the painter and the hose. "The pointing girl is most likely pointing at the storm clouds, but she could be pointing at something on the roof or in the tree" (63) |
| O4 A second storm pointer offered "the cat on the fence" | **Again**, on the same picture: "The man in green could be pointing at the storm clouds, or up at the cat or something on the fence" (57, identical since v0.35). The item reads in full. Below |
| O5 The market stall's leg standing on the crate | **Fixed.** Revision 35 sets the spare crate 50 px nearer the viewer; it is "Second cardboard box, right: on the ground beside the fruit stall" (48), and no reader of the five street pictures it is in mentions the leg |
| O6 Older ones | As before: goats out of place (38, 45, 58, 66), the seesaw man's legs over the plank (11, 14), wind that moves no plant or cap (08, 39) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.33 | v0.34 | v0.35 | v0.36 | v0.37 |
|---|---|---|---|---|---|
| Pass | 63 | 64 | 63 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 0 | 1 | 0 | 1 |

Every template was screened in at least three pictures (52 in three, 4 in four, 4 in five, 2 in six and 2 in eleven; 409 scored items behind the verdicts). The one failure is `hang_laundry` (0.833), which has one scored item a picture, three in all, so that one half mark takes it under the gate. All three of its pictures are identical to v0.36's, where it had full marks; it failed the same way once before, in v0.30. The lowest of those that pass are `ducks_bread` and `water_upward` (0.944), each on one half mark.

## What reads least well (the v0.38 list)

| # | Template | v0.37 | What the readers saw | Fix for v0.38 |
|---|---|---|---|---|
| R1 | `hang_laundry` | 0.833 (3 items, 3 pictures); fails | "I can't tell whether the boy is hanging the T-shirt up or taking it down" (12, identical; the man read as a boy). v0.31's list held the fix for this: a basket at the feet, "if the next screen halves it again" | A laundry basket at the hanger's feet, the washing coming from it, on the bench beside the line without one, then in whole scenes |
| R2 | `ducks_bread` | 0.944 (9 items, 3 pictures) | The girl holds "a small brown item", "fairly far from the pond for throwing food" (45) | Watch: the half mark moved within the template, in the busiest picture of the set |
| R3 | `water_upward` | 0.944 (9 items, 3 pictures) | "could be read as water pouring onto the planter, or as water shooting upward/sideways", in the unsure section only (21) | Watch: full marks in v0.36 on the same picture |

## Unintended oddities

Named kinds, from the scorers' lists (`v037/scores_summary_a.md` to `_c.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.38 |
|---|---|---|---|---|
| O1 | C | A storm pointer offered the cat on the fence, three screens running on one picture (the fence in v0.35, the cat in v0.36, both in v0.37) | Picture 57, unchanged since v0.35 | Keep a cat on the fence out of a storm pointer's picture, or her whole raised arm's side clear of it. Rebuild picture 57's seed and look at it before the design tests |
| O2 | C | The broom's autumn leaves under green trees ("a small seasonal inconsistency"), new in this screen, three of the four from one reader, the one who wrote most | Pictures 42, 44, 45 and 81, all identical to v0.36's, and design test 5 | Watch; or the broom's heap drawn as grit and dust, as the fork's is |
| O3 | C | The pan waterer's face against the flowers behind him, "a small layering mistake" | Picture 80, one reader, identical | Watch, or keep the head clear of the flower bed's blooms |
| O4 | C | The runner perhaps "rushing towards the boy (to catch him, grab the balloon or greet him)" | Picture 69 | Watch |
| O5 | C | Older ones: goats out of place, the seesaw man's legs over the plank, wind that moves no plant or cap, the square-wheeled bicycle standing with nothing to hold it up (23, 82), and once the slide's ladder apart from its frame (67) | Throughout | Notes for the pilot |

## Placement

All four tier-4 cells placed on v0.36's seeds under revision 35, the street's on v0.29 to v0.36's forced set, and all four came back identical to the pixel (a side test of the garden's seed under the new knob rule, before the set, came back identical too). 16 of the set's 21 pictures came back identical to v0.36's, and the other five, the street pictures with the spare crate, differ by the crate alone, in a box some 86 by 123 px. The tier-4 isomorph took 12 failed attempts, as in v0.33 to v0.36. 59 of the 61 probes came back identical; the two that did not are the two the rules were for, v0.36's pictures 73 and 63. The first probe pass left `walk_dog`, `dog_begs` and `windy_hat` short, as in v0.36, and two more probes filled them, the street's on v0.36's seed. All 82 records rebuild identical to the pixel, and the library passes the validator in full, 344 of 344.
