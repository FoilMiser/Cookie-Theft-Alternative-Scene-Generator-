# v0.26 blind screen: what it found (the work list for v0.27)

The v0.26 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 46 probes. Keys, descriptions and scores are in `v026/`.

## Headline (the 21 pictures of the set)

| | v0.23 (21) | v0.24 (21) | v0.25 (21) | v0.26 (21) |
|---|---|---|---|---|
| Things | 1.00 | 1.00 | 0.991 | 0.995 |
| Actions | 1.00 | 0.988 | 1.00 | 0.992 |
| Inferences | 1.00 | 0.986 | 0.985 | 0.953 |
| Contradictions | 1.00 | 1.00 | 1.00 | 0.981 |
| All items | 1.00 | 0.993 | 0.995 | 0.988 |
| Misread items | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 |
| Readers' remarks per picture (all screened pictures, recounted) | 3.86 | 5.64 | 5.93 | 5.27 |
| Oddities per picture, as logged by the scorers | 1.0 | 5.2 | 2.6 (at most 3) | 2.6 (at most 3) |

Across all 67 pictures 743 of 752 scored items had full marks. Eight had half marks, one, in a probe, was misread, and none was missed. The set's seven half marks are three inferences (pictures 21, 27, 57), two actions (33, 62), one thing (21) and one contradiction (3, a person "sitting in mid-air or on the edge of the path"), the first contradiction below 1.00 since v0.21.

## A correction to the remarks row

Sorting the v0.25 remarks for this release's list showed that `summarize_screen.py` had counted bullets that say nothing is wrong ("Nothing is floating or passing through anything else"): 25 of v0.25's 428 and 2 of v0.24's 408. So the rise published with v0.25, 5.67 to 6.29 or 11%, was really 5.64 to 5.93, or 5%. The counter is fixed and the row recounted for every screen that has one: v0.21 3.92 (published 4.35), v0.22 4.17 (4.49), v0.23 3.86 (4.32), v0.24 5.64 (5.67), v0.25 5.93 (6.29). The v0.24 control moves with it: on the same eight pictures the current reader wrote 6.5 remarks to the v0.23 readers' 5.5, 18% more, not the 15% published.

## Reading the two bottom rows

Remarks fell by 11%, 5.93 to 5.27, the first fall since v0.23, on the same model and prompts as v0.25. Named complaints fell with them (the table below), but the remarks were not sorted by kind this time, so how much of the fall is the drawings and how much is the readers is not separated. The logged oddities are capped at three per picture, so 2.6 compares only with v0.25's.

## The v0.25 list

| v0.25 reading | v0.26 result |
|---|---|
| R1 `dog_wants_walk` 0.833: "with its eyes shut", the wish never stated | **1.00** (6 items, 3 pictures). The neutral face: "as if it is waiting to be taken for a walk", "as though it is asking to be taken for a walk", "as if it is asking to go for a walk" |
| R2 `sweep` 0.875: "could be sweeping, or pausing to watch"; "no visible rubbish or leaf pile for the old man to sweep" | **Worse: 0.667** (3 items, 3 pictures, one misread). The heap did its job: no reader asked what there was to sweep, and two were plain, "sweeping up a pile of autumn leaves", "sweeping a pile of red, orange and brown leaves with a long broom". But the third took the fan of bristles for "a long yellow-headed rake" (picture 37). See R1 below |
| R3 `ducks_bread` 0.889: "swimming towards the food" | **1.00** (9 items, 3 pictures). It was not redrawn for this; the feed bag and the crumbs' colour changed. "Probably scoring variance" stands |
| O1 The older man's head: "the older man's face is hard to read", in ten of his 21 pictures | One remark in his 12 pictures, "his cap and head tilt in a way that makes it hard to see his eyes" (picture 62). Named an old or older man, grey hair, in a cap, in all 12. No grey patch, sideburn or ear |
| O2 The newspaper dog: "a monkey, an otter, or a person in a costume", "a person in a spacesuit or a small robot" | No other animal or figure in its five pictures, and `dog_reading` 1.00 over 15 items. The white dog is "white with brown patches" (picture 59). Its pose still draws remarks: "long body and legs splayed", "very twisted" |
| O3 The cap worn backwards: seven remarks, twice a head "the wrong way round" | No head on the wrong way round in his 20 pictures. Two still said "red cap worn sideways or backwards" or "red cap worn backwards or sideways" (pictures 7, 27). The inventories name him a boy in 14, a boy or young man in 3, a person in 3, and a woman or a girl in none |
| O4 Figures overlapping the pond, poles through crates, water as a solid band | Left, a note for the pilot. Five pictures remarked on the pond (4, 30, 36, 50, 63), most adding that the feet are on the grass |
| O5 A lamp post merging with a figure; swing ropes around a head | Placement revision 24 keeps a person's box off the post. No reader had a figure growing out of it or about to walk into it; the nearest is a goat "overlapping the post slightly in depth" (picture 59), a goat not being covered by the rule. The ropes stay, as they are a drawing and no rule places them: "meet behind the girl's head" (picture 49), and much the same in 9 |
| O6 Older ones: goats, wind with nothing else blowing, shadows | Left, as since v0.11 |
| O7 Two probes nearly the same picture, both `seesaw` alone | `probes.py` now gives a second solo probe of a template a companion event. The seesaw probes now differ from one another, though two share the pair `seesaw` and `ice_cream`, in different layouts |

Added from sorting the remarks, and read here:

| v0.25 reading | v0.26 result |
|---|---|
| What the bird feeder holds: "a paper bag, a cup or a carton" | "A brown paper bag" or "a paper bag" for all six feeders in five pictures (10, 17, 21, 48, 50). No cup, carton or box |
| The sandcastle: "very straight, boxy edges ... a cardboard or wooden model" | "Building a sandcastle with three towers and a small red flag on top". No box or model in its three pictures. One reader still has the girl and the castle "half outside the box" (picture 13) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 |
|---|---|---|---|---|---|
| Pass | 63 | 64 | 63 | 61 | 59 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 0 | 1 | 3 | 5 |

Every template was screened in at least three pictures (56 in three, 3 in four, 2 in five, 3 in six; 386 scored items behind the verdicts). One of the five failures is this release's own doing. The other four are on drawings it did not change, each on one or two half marks and each in full in v0.25. The v0.9 retest put the gate's reader variance at about five templates between screens, so those four do not by themselves show that anything got worse. `sweep` does: it is a misread, on the thing this release redrew.

## What reads poorly (the v0.27 list)

| # | Template | v0.26 | What the readers saw | Fix for v0.27 |
|---|---|---|---|---|
| R1 | `sweep` | 0.667 (3 items, 3 pictures, 1 misread) | "A long yellow-headed rake" (picture 37), with the leaves at its head. This is the fan of bristles chosen on the bench, where one reader had already said "broom or rake". The heap of leaves pushes the same way, as `rake` has leaves at its head too | First on the list. The bench, a broom head that cannot be a rake: a straight-edged yard broom or a denser, narrower head, read beside `rake`. Keep the heap |
| R2 | `ice_cream` | 0.833 (6 items, 6 pictures) | The same bearded man twice, the cone held up before his face: "looking at or eating it" (picture 58), "could be eating the ice cream or just holding it up" (picture 62). 1.00 in v0.25 | The bench: the cone at the mouth, or a bite out of it. His hair and beard also "merge into one dark shape" |
| R3 | `photo` | 0.833 (3 items, 3 pictures) | "Binoculars or a camera" (picture 33), never committing to a photo. 1.00 in v0.25 | Watch; one half mark on one item. A larger camera body if it comes back |
| R4 | `about_to_trip` | 0.889 (9 items, 3 pictures) | The obstacle is off the walker's line, said by all three readers: it "lies slightly off his line" (picture 57), "the box is slightly to his side" (picture 62), and he is heading away from a bucket that "might just be a bucket on the ground" (picture 27). Half marks in 27 and 57. 1.00 in v0.25 | A placement rule: the obstacle on the line of the walk. And look at the walker's feet: "his head and arms face left", while "his legs and feet look like they stride towards the right" |
| R5 | `sprinkler_package` | 0.889 (9 items, 3 pictures) | Both half marks in one picture (21): "a wooden crate standing in a puddle", the soaking one of two readings. 1.00 in v0.25 | Watch; probably reader variance |

## Unintended oddities

Named kinds, from the scorers' lists (`v026/scores_summary_a.md` to `_c.md`).

| # | Sev | Oddity | Where | Fix for v0.27 |
|---|---|---|---|---|
| O1 | B | The seesaw plank through the sitter: "sitting right into the plank", "almost passes through the girl in pink's lap", legs past the plank's end | Pictures 1, 6, 12, 58, 64 | The riders' offsets on the bench |
| O2 | B | The hose: stiff, "like a stiff loop standing in the air"; not joined to its nozzle; the bulge "a flat puddle or a thicker piece of hose", "a dark blue pad or fat fitting" | Pictures 8, 9, 18, 20, 44, 54 | The bench: a limp hose, a clear join, a smaller bulge |
| O3 | C | Faces hidden by a tilted head, an arm or hair; "a dark curved shape" on a woman's face; "hair and beard merge into one dark shape" | Pictures 23, 36, 39, 46, 48, 62, 67 | Find what the dark shape is, then the bench |
| O4 | C | Water drawn solid: "like a beaded curtain", "almost a solid tube", "very straight and rigid" | Pictures 3, 8, 14, 32 | With the hose |
| O5 | C | The leaf clumps over a kite or a ball: "separate stickers", "pasted on"; the ball "a planet-like striped object" | Pictures 2, 23, 30, 33, 62 | Clumps in the tree's own outline |
| O6 | C | The bird at the ground: "could be tumbling or injured", a head like "a red ball"; a raised wing "confusingly drawn" | Pictures 56, 57, 65 | The bench, the red bird's head |
| O7 | C | The paint roller's head again: "offset from the handle", "floating just above the top of the fence"; "a brush or a roller" | Pictures 3, 7, 29, 43 | Watch; `paint_fence` and `paint_tracks` passed in full |
| O8 | C | The bicycle: "solid black disc wheels", overlapping its rack, "tangled" | Pictures 39, 53 | Spokes in the rack variant |
| O9 | C | The leaves have no source: "the pile of autumn leaves does not match the tree", and twice in the design tests | Picture 40 | Note for the pilot, or leaves in the tree above |
| O10 | C | Narrow figures: "long thin legs", feet that overlap. On the bench, a body 22% deeper with limbs 12% thicker did not move the readers' words | Pictures 9, 11 and most bench crops | A larger job than one bench round, a proportion change |
| O11 | C | Older ones: figures over the pond, a grown man on a child's seesaw, goats as "a white dog or lamb", a wind that reaches only the cap, shadows, the begging dog "human-like" | Throughout | Note for the pilot, as since v0.11 |

## Placement

Not a reading, but it got harder. The tier-4 playground took 89 failed seeds across two searches (3 in v0.25), found on the last seed of the second list, and the tier-4 isomorph 676 failed attempts (13 tries in v0.25). The tier-4 park took 16 failed seeds, where v0.25's seed had placed at once. The commonest failures name `about_to_trip`, `lost_balloon`, `sitting_on_air` and, for the isomorph, `sweep_fork`, but the cause was not traced. Revision 24's lamp-post rule does not apply to the playground, which has no lamp post, and its other placement change only keeps the sandbox's child and castle back from the front rim, so neither is the plain answer. Worth a look before the next rule goes in.
