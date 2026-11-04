# v0.30 blind screen: what it found (the work list for v0.31)

The v0.30 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 57 probes. Keys, descriptions and scores are in `v030/`.

## Headline (the 21 pictures of the set)

| | v0.27 (21) | v0.28 (21) | v0.29 (21) | v0.30 (21) |
|---|---|---|---|---|
| Things | 1.00 | 1.00 | 0.981 | 0.990 |
| Actions | 0.996 | 0.996 | 1.00 | 0.992 |
| Inferences | 0.950 | 0.879 | 0.985 | 0.986 |
| Contradictions | 1.00 | 1.00 | 1.00 | 0.977 |
| All items | 0.993 | 0.984 | 0.991 | 0.989 |
| Misread items | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 |
| Readers' remarks per picture (all screened pictures) | 5.81 | 5.14 | 5.15 | 5.19 |
| Oddities per picture, as logged by the scorers | 2.2 (at most 3) | 2.0 (at most 3) | 2.3 (at most 3) | 2.3 (at most 3) |

Across all 78 pictures 872 of 877 scored items had full marks. Four had half marks, one was missed, and none was misread. All five are in the set: a missed "a few white clouds" (2), and half marks on the dog reading a newspaper (26), the man at the washing line (54), and the girl eating an ice cream and the lost balloon, both in one picture (67). One scorer gave no item under full marks in 302, and listed 22 it thought a stricter scorer might halve.

## A retest nobody planned

This release changed so little in the set that 18 of its 21 pictures came back identical to the pixel, with one probe. So 19 pictures were read twice, in v0.29 and in v0.30, by fresh readers and fresh scorers, with nothing changed between. It is the first such measure since the v0.9 retest.

| On the same 19 pictures | v0.29 | v0.30 |
|---|---|---|
| Items | 230 | 230 |
| Items with the same score in both | 223 | 223 |
| Remarks | 106 | 108 |
| Readers offering that the trip's walker may pass the box (the same five pictures) | 4 of 5 | 1 of 5 |

Seven items moved. Three are clouds: two missed in v0.29 and read now, one the other way. Three lost half marks they had not lost before, and one gained. So these means moved with no picture changed: `dog_begs` 1.00 to 0.944, `dog_reading` 1.00 to 0.967, `lost_balloon` 1.00 to 0.967, `bird_steals` 0.958 to 1.00.

Three things follow, and two of them correct v0.29's notes.

- **Scored items are stable.** 97% of them agree between two whole sets of readers and scorers. Remarks per picture are stable too, at 5.58 and 5.68. Both are worth more than this release's headline.
- **A single half mark is noise.** Each of those four moves is one half mark on a picture that did not change. A template with few items crosses the gate on that alone. The gate read 64 then 63, and that move is of this kind.
- **Four of five allowing the walker may pass was noise as well.** v0.29 made much of that, and said a stricter scorer would fail the trip on it. On the same five pictures it is now one of five. Second readings come and go with the reader. Nothing was done to the drawing, so nothing earned the change, and the 0.87 that v0.29 reported was not a property of the picture.

The keyword rows are worse than either. See below.

## Reading the two bottom rows

Remarks did not move, 5.19 against 5.15 (405 on 78 pictures, 386 on 75), on a few more templates in each picture, 2.99 against 2.92. The readers range from 4.50 to 6.12 a picture on the same split, against 4.50 to 5.75. `remark_topics.py` sorts the remarks of two screens by keyword, roughly, and the hits were read:

| Pictures that remark on | v0.29 | v0.30 | |
|---|---|---|---|
| Thin or long body or legs | 13 | 6 | **Not changed.** Half, with the figures and 18 set pictures the same. v0.28's and v0.29's notes read a rise in this row, and it now reads as noise |
| A figure over the pond | 10 | 6 | Not changed |
| Scale | 6 | 3 | Not changed |
| Feet overlapping | 5 | 2 | Not changed |
| A branch to hold it | 6 | 2 | Partly this release's. The tuft's complaints are gone, as "looks detached" and "a little pasted in" do not come back |
| Stiff or awkward poses | 20 | 20 | Not changed |
| Shadows | 14 | 12 | Not changed. None calls one wide |
| The seesaw's plank | 3 | 5 | Not changed. See O1 below |
| Goat as something else | 7 | 8 | Not changed |
| The hose stiff or jointed | 2 | 1 | Redrawn. "Slightly rigid for a hose" (73), and "a stiff curve" under another keyword (71) |
| The hose's bulge | 4 | 2 | Not changed since v0.29 |

A keyword count is a rough sort, which says where to read. It is not a measure, and the first row is why. From here on, a row should not be given as a result unless it moves by more than these did with nothing changed.

## The v0.29 list

| v0.29 reading | v0.30 result |
|---|---|
| R1 `about_to_trip` 1.00, on five street pictures | **1.00** (33 items, 11 pictures), now in every setting: two gardens, two parks, two playgrounds and five streets. Forced in as probes, and the box was not redrawn. All eleven name it in the free description: "Directly ahead of her, right in her path ... seems about to trip over it" (11), "so it looks like he is about to trip over it" (37). Five offer that the walker may step round it, four of them off the street |
| R2 `dog_wants_walk` 0.917 | **1.00** (6 items, 3 pictures). Not changed |
| R3 `water_upward` 0.944 | **1.00** (9 items, 3 pictures). Not changed |
| R4 `bird_steals` 0.958 | **1.00** (12 items, 4 pictures). Not changed, and the half mark was on a picture that came back the same |
| O1 The hose at the fist: "seems to stop at about waist height" | Gone. It runs on to the fist and hangs from it. In its three pictures nobody has it stop or break. "Stiff" stays, twice: "rises to her hand in a stiff curve" (71) |
| O2 The fish's limb: "drawn on top of the leafy crown", the tuft "looks detached" | Gone, with the fork's other arm. What it cost: "it sits on what looks like the tree's bent trunk" (65), "the trunk seems to bend into it" (55). All three read the fish as impossible |
| O3 Crumbs past the pond's edge | Gone. No remark on crumbs off the water in three pictures. And the duck is at them: "the duck is eating" (52), "eating them" (69) |
| O4 The reading dog "a bit like a kangaroo" | No kangaroo in 78 pictures, with the dog not changed |
| O5 A running man's shoulders "stiff and sausage-like" | Not changed. Not named again |
| O6 The reel, "only a short stub of hose joined to nothing" | Gone. In all four of its pictures a nozzle on the grass, not in use: "a yellow nozzle lying on the grass" (9). Two now say the reel "overlaps" the flower bed's edge, which it always has |
| O7 A square-wheeled bicycle "stands up on its own" | Not changed. Once: "seems to stand with no one holding it" (42) |
| O8 to O10 | Left |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 |
|---|---|---|---|---|---|
| Pass | 59 | 63 | 61 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 5 | 1 | 3 | 0 | 1 |

Every template was screened in at least three pictures (44 in three, 11 in four, 4 in five, 2 in six, and one each in seven, ten and eleven; 433 scored items behind the verdicts). The one failure is on one half mark among three items, on a picture new this release. v0.29 said 64 had fallen each time before, and it has, by one.

## What reads least well (the v0.31 list)

| # | Template | v0.30 | What the readers saw | Fix for v0.31 |
|---|---|---|---|---|
| R1 | `hang_laundry` | 0.833 (3 items, 3 pictures); fails | "(a) hanging the washing out, or (b) taking it down because of the coming storm" (54). A fair reading of a picture that put washing under storm clouds, not a fault of the drawing. Full marks in its other two | A rule: no washing under a dark sky, as for the bucket |
| R2 | `dog_begs` | 0.944 (9 items, 3 pictures) | "An ice cream or a pink lolly, or she could just be holding her hand to her mouth" (67), on a picture that read in full last time. Two others find the cone hard to see (27, 48) | The cone, if a bench shows that the hand hides it. Otherwise watch |
| R3 | `dog_reading` | 0.967 (15 items, 5 pictures) | "Genuinely reading, or as just holding or playing with the newspaper" (26). On a picture that read in full last time | Watch |
| R4 | `lost_balloon` | 0.967 (15 items, 5 pictures) | "Holding all three on separate strings" (67). On a picture that read in full last time | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v030/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.31 |
|---|---|---|---|---|
| O1 | B | The seesaw: "the man's legs appear to go through or around the plank", and riders "a little above and slightly in front of the plank" | Pictures 29, 44, 53, 61, 64 | On this list since v0.27, and the largest thing left that is plainly a drawing fault. Take it to the bench, as the larger job it is |
| O2 | C | The bearded man's vest: "a jagged edge against the white shirt", "the white sleeve wraps over the vest in a jagged shape" | Pictures 37, 55, 57, and two cut-outs on the bench | In the cast, and the same figure every time. Look at the crop; likely cheap |
| O3 | C | The fish's limb as a bent trunk: "the trunk seems to bend into it" | Pictures 55, 65, and "one bent pipe" on the bench | A little less bend where it leaves the trunk, if it does not lose the limb |
| O4 | C | The hand and the sandcastle: "the hand and castle merge a little" | Pictures 21, 39, 44 | Move the castle a little from the child |
| O5 | C | A book that floats: "seems to float a little ahead of her hands" | Pictures 2, 11 | Look at the walker's grip |
| O6 | C | The feed bag as "a small box", against the body with no clear hold | Five of five cut-outs on the bench; less in whole pictures | Look at it |
| O7 | C | The reel over the bed's edge: "partly overlapping the edge of the flower bed" | Pictures 9, 32 | Move the reel 20 units |
| O8 | C | Older ones: goats as sheep or dogs, figures over the pond, a wind that reaches only the cap, the roller's head, a sky that goes dark and leaves the colours bright | Throughout | Notes for the pilot, as since v0.11 |

"Stiff" of a hose held at the waist is not on this list. It has been said of every way of drawing one since v0.25 and costs no marks.

## Placement

All four tier-4 cells placed on last release's seeds, with no failed seed, against 166 in v0.29. That is not the wide box getting cheaper: nothing about it changed, so the seeds that had been found came back. What it costs a fresh search is still as v0.29 found it.

The box was tried narrower (60 units for 72), and the lane beyond it shorter (300 for 380). Forced into a picture with the band off, every combination placed every time, 40 of 40 at tier 3 and 24 of 24 at tier 4, which only says the test could not tell them apart: the search's cost is in the band. With the band on, a test of the two extremes placed the same in its first two settings (none of 8 in the garden, one of 8 in the park), and was stopped as the question had gone away. It stays 72 and 380, as 60 reads a little less firmly (`isolation_v030.md`). The question is open for the next release that has to search.

The tier-4 isomorph took 13 failed attempts. The first probe pass left two templates short, and two more probes filled them. Six more were forced for the trip.
