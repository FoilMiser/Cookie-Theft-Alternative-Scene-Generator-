# v0.25 blind screen: what it found (the work list for v0.26)

The v0.25 screen used the prompts of the twenty-one before it (`screen_prompts.md`), with one addition: scorers now list under "unintended" only what the describer presents as looking wrong, impossible or confusing, at most three for a picture. Nine readers who never saw the key described 68 pictures (`v025/desc_pic_NN.md`): the 21 pictures of the set (16 showcase pictures and 5 isomorphs) and 47 probe pictures. Three scorers scored pictures 1 to 22, 23 to 45 and 46 to 68 against `keys.json` (`scores_a.json` to `scores_c.json`, merged in `scores.json`). Per-template means are in `screen_summary.json`; the gate is in `v025/gate.json`. Readers and scorers ran on Claude Opus 5.5.

## Headline (the 21 pictures of the set)

| | v0.22 (21) | v0.23 (21) | v0.24 (21) | v0.25 (21) |
|---|---|---|---|---|
| Things | 1.00 | 1.00 | 1.00 | 0.991 |
| Actions | 1.00 | 1.00 | 0.988 | 1.00 |
| Inferences | 0.971 | 1.00 | 0.986 | 0.985 |
| Contradictions | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.997 | 1.00 | 0.993 | 0.995 |
| Misread items | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 |
| Readers' remarks per picture (all screened pictures) | 4.49 | 4.32 | 5.67 | 6.29 |
| Oddities per picture, as logged by the scorers | 1.2 | 1.0 | 5.2 | 2.6 (at most 3) |

Across all 68 pictures 779 of 785 scored items had full marks. Four had half marks, two were missed, and none was misread.

## Reading the two bottom rows

Remarks are counted directly from the "unsure" sections of the descriptions (`summarize_screen.py`), so they do not depend on a scorer. They rose again, by 11%, and the changes of this release did not bring the total down: what they removed were the named complaints below. Current readers write about 15% more than the v0.23 readers on the same pictures (`v024/control/`), and how much of the rest is readers, pictures or the mix of pictures is not separated. The logged oddities are capped at three per picture by the new prompt line, so 2.6 compares with neither v0.24's 5.2 nor v0.23's 1.0.

## The v0.24 list

| v0.24 reading | v0.25 result |
|---|---|
| The shopping bag, the gate's one failure: "carrying something yellow", "very long and thin ... could be a tag, folded paper" (0.75) | **1.00** over three pictures: "a yellow shopping bag" twice, "a yellow bag" once. No tag, paper or plank |
| The wheelbarrow's shadow: "a large dark oval extending well beyond it" (four probes) | No remark on it in any of the 68 pictures |
| The bird at the sandwich: "about as big as the sandwich", "a blue kettle or jug" | No kettle or jug. `bird_steals` 1.00 over 12 items. Its cue salience fell by 0.32 in the calibration, as a smaller cue should |
| The newspaper dog's paws: "white gloved hands" | No gloves or mitts. `dog_reading` 1.00 over 21 items, seven pictures. See O2 for its head |
| The paint roller: "hardly seems to touch the fence", "a small pale oval" | One remark, that it "reaches up above the fence top". `paint_fence` and `paint_tracks` 1.00 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 |
|---|---|---|---|---|---|
| Pass | 61 | 63 | 64 | 63 | 61 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 3 | 1 | 0 | 1 | 3 |

Every template was screened in at least three pictures (51 in three, 7 in four, 1 in five, 3 in six, 2 in seven; 409 scored items behind the verdicts). None of the three that fail was changed by this release, and all three read in full in v0.24. The v0.9 retest put the gate's reader variance at about five templates between screens, so this drop does not by itself show that anything got worse. Each still has something to look at.

## What reads poorly (the v0.26 list)

| # | Template | v0.25 | What the readers saw | Fix for v0.26 |
|---|---|---|---|---|
| R1 | `dog_wants_walk` | 0.833 (6 items, 3 pictures) | A dog by the door with the lead in its mouth "with its eyes shut", the wish never stated (one inference missed, picture 45). Closed eyes read as resting | The bench: drop the happy face from this template, as its eyes close (the template picks happy or neutral), and read it with eyes open |
| R2 | `sweep` | 0.875 (4 items, 4 pictures) | An older man "as if sweeping", but "could be sweeping, or pausing to watch" (picture 19); "no visible rubbish or leaf pile for the old man to sweep" (picture 9), and much the same in 16, an old remark | A small heap of dust or leaves at the broom's head |
| R3 | `ducks_bread` | 0.889 (9 items, 3 pictures) | "Swimming towards the food": direction read, the purpose only implied (pictures 18 and 42, half marks). One scorer called this its closest call | Probably scoring variance, no drawing change. Look again if it recurs |

The other two items below full marks are the clouds, not mentioned in one description (picture 2), and a floating wooden box called cardboard and half marked (picture 47) though the key accepts "box".

## Unintended oddities

Named kinds, from the scorers' lists (`scores_summary_a.md` to `_c.md`).

| # | Sev | Oddity | Where | Fix for v0.26 |
|---|---|---|---|---|
| O1 | B | The older man's head: "the older man's face is hard to read", cap peak, a grey patch "or a sideburn", a "grey beard ... like a patch"; he has a moustache and a ring of white hair under a cap. The most repeated specific | Ten of his 21 pictures: 2, 5, 7, 8, 17, 52, 55, 58, 62 and 67 | The bench, one more round on his profile |
| O2 | B | The newspaper dog's head and body: "could be taken for a monkey, an otter, or a person in a costume" (tan), "a person in a spacesuit or a small robot" (white). In the design tests the white dog was "an odd white figure ... ghostly". The item still scored in full | Pictures 11, 16 and others | Prefer the tan dog to read; a clearer muzzle and eye in this pose |
| O3 | C | The cap worn backwards: seven remarks that the peak points away from his face, mostly read as a backwards cap, twice as a head "the wrong way round" | Pictures 15, 30, 37, 38, 39, 50, 55 | Watch; he is named a boy or man in all 15 of his pictures |
| O4 | C | Figures overlapping the pond, a stall's poles through its crates, water drawn as a solid band | Pictures 29, 32, 34, 36, 38, 39, 42 | Note for the pilot |
| O5 | C | A lamp post merging with a figure; swing ropes around a head; a grown man on a child's seesaw | Pictures 4, 5, 6, 8, 18, 20 | A placement rule for the post and the ropes |
| O6 | C | Older ones: goats, wind with nothing else blowing, shadows, sweeping with nothing to sweep | Throughout | Note for the pilot, as since v0.11 |
| O7 | C | Two probes, 56 and 61, are nearly the same picture, both `seesaw` alone, as `probes.py` makes the same template more than once when one needs three pictures | 2 probes | Vary them, or accept it for the screen |

The wheelbarrow's frame was "loosely stacked, disconnected parts" on the bench, a remark for the same drawing session as R2.
