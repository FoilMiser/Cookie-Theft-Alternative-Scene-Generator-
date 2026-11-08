# v0.41 blind screen: what it found (the work list for v0.42)

The v0.41 screen read the set's 21 pictures and 72 probes with the prompts of v0.39 (`screen_prompts.md`): twelve readers of seven or eight pictures and four scorers of 22 to 24, the oddity tally by angle as in v0.39. Keys, descriptions and scores are in `v041/`.

v0.41 changed one drawing: the begging dog's forelegs, folded at the elbows with the paws tipped down at the chest (`isolation_v041.md`). The bench read four other changes and kept none of them: the stalking cat's legs, the woman in yellow's figure, the floating box hung level, and trees turning over a heap of dry leaves. Placement revision 39 therefore draws nothing new. Twenty of the set's 21 pictures and 23 of the probes are identical to the pixel to v0.40's, so this screen is mostly a retest.

## Headline (the 21 pictures of the set)

| | v0.37 (21) | v0.38 (21) | v0.39 (21) | v0.40 (21) | v0.41 (21) |
|---|---|---|---|---|---|
| Things | 1.00 | 1.00 | 1.00 | 0.991 | 1.00 |
| Actions | 0.996 | 1.00 | 1.00 | 0.996 | 1.00 |
| Inferences | 0.971 | 0.985 | 1.00 | 0.986 | 0.958 |
| Contradictions | 0.977 | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.993 | 0.998 | 1.00 | 0.993 | 0.995 |
| Misread items | 0 of 285 | 0 of 286 | 0 of 287 | 0 of 287 | 0 of 287 |
| Readers' remarks per picture (all screened pictures) | 2.82 | 3.38 | 3.10 | 3.04 | 3.17 |
| Oddities per picture, as logged by the scorers | 0.4 (at most 3) | 0.8 (at most 3) | 0.8 (at most 3) | 0.5 (at most 3) | 0.4 (at most 3) |

Across all 93 pictures, 999 of the 1008 scored items had full marks and none was misread. The nine under full marks:
- **Three inferences in the set, half right, each on a picture identical to v0.40's**, where all three had full marks:
  - the dropped ice cream of the tier-3 street's isomorph (06): "the dog knocked the ice cream down, or the child dropped it";
  - the coming rain of the tier-3 street (38): the clouds are "dark rain clouds", but rain is never said to be coming;
  - the kite in the tier-4 garden's isomorph (90): "It could be stuck or tangled in the tree, or flying in front of the tree".
- **The broom of a probe, half right (28):** "sweeps or rakes a pile of brown leaves with a yellow broom or fan rake".
- **The clouds of five garden probes (67 to 71), scored 0.** All five were the ninth reader's, who never mentioned the sky. Clouds are a setting item, which the gate leaves out.

The four scorers gave 1, 2, 5 and 1 items under full marks, out of 255, 263, 253 and 237.

**What the full marks rest on.** The scorers' notes mark 16 credits they gave in full where the free description commits and the unsure section adds another reading (21 in v0.40, 11 in v0.39). If those 16 are halved, 62 of 64 templates pass (`tpdb_work/strict41.py`). Two fall:
- `blocked_hose` (0.896, 24 items), with five of its credits hedged: "it could also simply be turned off" (84), and the dog on the hose or "just in front of it" (70);
- `rain_coming` (0.889, 9 items), on one hedged credit and the half mark above.

`floating_box` (0.967) and `play_catch` (1.00), v0.40's two at 0.833, both pass the strict count now.

## A retest, a twelfth time

43 pictures, 20 of the set's and 23 probes, are identical to the pixel in v0.40 and v0.41 (`tpdb_work/retest41.py`). The set came back on every seed and layout, and only the tier-3 playground's begging dog was drawn again.

| On the same 43 pictures | v0.40 | v0.41 |
|---|---|---|
| Items | 532 | 532 |
| Items with the same score in both | 523 | 523 |
| Remarks | 151 | 156 |

Nine items moved. Three are clouds, a setting item: one up and two down. Of the other six, two moved up by half a mark:
- the catcher of the tier-2 garden, v0.40's R1 (`play_catch`);
- the hose's cause in the tier-4 garden (`blocked_hose`).

Four moved down by half a mark: the dropped ice cream, the coming rain, the kite in the tree and the probe's broom. Nothing in those pictures changed.

## The v0.40 list

| v0.40 reading | v0.41 result |
|---|---|
| R1 `play_catch` 0.917, 0.833 read strictly | **1.00, and 1.00 read strictly** (10 items, 5 pictures), not changed. The half mark of v0.40 came back in full on the identical picture, and two more probes read in full |
| R2 `floating_box` 1.00, 0.833 read strictly | **1.00, and 0.967 read strictly** (15 items, 5 pictures). The bench's level box was not taken: it was still falling or thrown, and in the park it read as standing on the ground far off (`isolation_v041.md`). Once "floating, or as falling (possibly thrown over the fence from next door)" (02) |
| R3 `ladder_nothing`, `sweep_fork`, `water_upward` 0.889 read strictly | 1.00 each; read strictly 1.00, 0.944 and 1.00 |
| O1 The heaps' brown leaves under green trees | **No remark in 93 pictures** (five pictures from three readers in v0.40), the heap unchanged. The bench's turning trees read as fruit and were not taken; the remark went with the readers |
| O2 The begging dog in profile | **Redrawn** (`TPDB_BEG41` F): the forelegs folded. Begging in all four pictures, at 90 and at 45, and no reader saw rods or arms. Once at 90 "The dog's body looks slightly stretched or bent in an unusual sitting-up pose, but it does not look broken" (78). Once two ice creams: "I can't tell who the dog is begging from" (55) |
| O3 The stalking cat at 45 | **No remark** in four pictures, not changed (two in v0.40). Every leg spread on the bench drew "bunched" or "tangled", v0.40's too |
| O4 The woman in yellow called "girl" | **Not changed**: in 8 of her 24 pictures, six of them hedged ("girl or young woman", "Woman/girl"); 6 of 27 in v0.40. On the bench she was "a woman" in four cut-outs of four |
| O5 The goat | **The hunch is not remarked**, in six pictures. Out of place in seven ("a goat in a public park is unusual"), and once "it could at a glance be read as a sheep, though the horns suggest a goat" (72). Not changed |
| O6 The walking back foot | Not seen, not changed |
| O7 Older ones | As before: figures over the thing beside them (the seesaw man's legs 07, 44; a man in the pond 05, 23) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.37 | v0.38 | v0.39 | v0.40 | v0.41 |
|---|---|---|---|---|---|
| Pass | 63 | 64 | 64 | 64 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 0 | 0 | 0 | 0 |

Every template was screened in at least three pictures, and all 64 pass. By count: 43 in three, 9 in four, 5 in five, 4 in six, 1 in seven, 1 in twelve and 1 in sixteen, with 460 scored items behind the verdicts.

The lowest are each on one half mark, and each half mark is on a picture identical to v0.40's or on a probe:
- `rain_coming` (0.944, 9 items, 3 pictures);
- `sweep` (0.958, 12 items, 12 pictures);
- `kite_in_tree` (0.967, 15 items, 5 pictures);
- `ice_cream_drop` (0.969, 16 items, 4 pictures).

Per angle (`v041/gate_yaw.json`), all 17 (template, angle) pairs pass. The lowest is `ice_cream_drop` at 90 (0.938), on the same half mark. The begging dog is 1.00 at 90 and at 45.

## What reads least well (the v0.42 list)

| # | Template | v0.41 | What the readers saw | Fix for v0.42 |
|---|---|---|---|---|
| R1 | `blocked_hose` | 1.00; 0.896 read strictly (24 items, 6 pictures) | The cause given, with the tap offered as well: "I cannot see a clear kink, so it could also simply be turned off" (84); the dog on the hose or "just in front of it" (70) | A kink at the paw, the hose pinched flat where the dog stands; bench, beside v0.32's bulge |
| R2 | `rain_coming` | 0.944; 0.889 read strictly (9 items, 3 pictures) | "dark rain clouds", with the coming rain unsaid (38), on a picture identical to v0.40's, where it had full marks | Variance; watch |
| R3 | `sweep` | 0.958 (12 items, 12 pictures) | "a yellow broom or fan rake" (28) beside the heap of leaves, the reading v0.24's fan of bristles once drew | Watch; if again, the broom's head on the bench beside the rake |
| R4 | `kite_in_tree`, `ice_cream_drop` | 0.967, 0.969 | Each one half mark on a picture identical to v0.40's | Variance; watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v041/scores_summary_a.md` to `_d.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.42 |
|---|---|---|---|---|
| O1 | C | Two ice creams near the begging dog. The dog sits beside the eater on the bench, and an eater walking by is near it too: "I can't tell who the dog is begging from ... Both have ice cream" (55), and the first design test's dog begs "perhaps for the girl's ice cream". Three probes from the pass by angle place the two together | 55; probes; `design_tests_v041.md` | A placement rule: no other eater near a begging dog (revision 26 keeps others 120 units off it, which a walker in front passes) |
| O2 | C | The begging dog's body at 90: "slightly stretched or bent" (78); in both design tests at 90 "upright", "kneeling", "human-like". Its upturned nose and eye were once "a fly or bee" | 78; design tests | The body at 90; the bench's lean took nothing away (`isolation_v041.md`) |
| O3 | C | The woman in yellow called "girl", in 8 of her 24 pictures, six of them hedged | Throughout | Read her in whole pictures beside the other adults, not cut out: on the bench she is a woman |
| O4 | C | The goat out of place (seven pictures); once read as a sheep at a glance (72) | 04, 25, 36, 39, 40, 41, 72 | Notes for the pilot. The body round (the hunch at 45 and 135) is priced in `isolation_v041.md` |
| O5 | C | The stalking cat's legs at 45 | Bench only | Watch: none in the screen |
| O6 | C | Older ones: figures over the prop beside them (05, 07, 23, 44); the heaps' season, gone this time | Throughout | Notes for the pilot, as before |

## Placement

**The set.**
- **Tiers 1 to 3.** Every cell placed again on its v0.40 seed and layout under revision 39.
- **Tier 4.** The garden, park and playground placed on v0.40's seeds, the street on v0.29 to v0.40's forced set, each on the same layout as in v0.40.
- **What changed.** 20 of the 21 pictures are identical to v0.40's, all five isomorphs among them. The tier-3 playground differs only where its begging dog is drawn.

**The probes.**
- **The first pass** (`probes.py 3`, five for `play_catch` and `floating_box`) left `dog_begs` one short, as in v0.40.
- **The pass stratified by angle** added 13 probes and filled it.
- **What changed.** The probes' needs moved, so 48 of the 72 probes differ from v0.40's. 24 are identical to the pixel to a v0.40 probe: 23 of them by the same name (the retest's) and one under another seed's name.

All 93 records rebuild identical to the pixel, and the library passes the validator in full, 388 of 388.
