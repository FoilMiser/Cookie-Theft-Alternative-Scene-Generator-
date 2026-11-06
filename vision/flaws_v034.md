# v0.34 blind screen: what it found (the work list for v0.35)

The v0.34 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 62 probes. Keys, descriptions and scores are in `v034/`.

## Headline (the 21 pictures of the set)

| | v0.31 (21) | v0.32 (21) | v0.33 (21) | v0.34 (21) |
|---|---|---|---|---|
| Things | 1.00 | 0.991 | 0.990 | 0.990 |
| Actions | 0.996 | 0.988 | 0.992 | 1.00 |
| Inferences | 1.00 | 0.956 | 0.957 | 0.986 |
| Contradictions | 1.00 | 1.00 | 1.00 | 1.00 |
| All items | 0.998 | 0.986 | 0.988 | 0.995 |
| Misread items | 0 of 284 | 1 of 286 | 0 of 285 | 0 of 285 |
| Readers' remarks per picture (all screened pictures) | 3.51 | 3.28 | 3.19 | 3.13 |
| Oddities per picture, as logged by the scorers | 0.6 (at most 3) | 0.8 (at most 3) | 0.9 (at most 3) | 0.5 (at most 3) |

Across all 83 pictures 874 of 885 scored items had full marks, and none was misread.

**Two items in the set are under full marks.** The bird on the tier-4 garden's bench "pecks at the sandwich" (4), and that it is stealing while he reads is not said; that picture differs from v0.33's only in the woman in yellow's hair. The tier-4 park's clouds went unnamed, as in v0.33, on a picture identical to the pixel. 14 of the set's 21 pictures came back identical to v0.33's, and the other seven differ only in her hair.

The scorers gave one, none and ten items under full marks, in 314, 282 and 289. Seven of the ten are "a few white clouds", in seven of the nine pictures of one reader (75 to 83), who named nothing in the sky; one more is a tree that reader left out. The other two are the goat on the hose (below).

## A retest, a fifth time

26 pictures, 14 of the set's and 12 probes, were identical to the pixel in v0.33 and v0.34 (`tpdb_work/retest34.py`).

| On the same 26 pictures | v0.33 | v0.34 |
|---|---|---|
| Items | 299 | 299 |
| Items with the same score in both | 296 | 296 |
| Remarks | 96 | 96 |

Three items moved, two up and one down. Up: a balloon let go of, in the street isomorph, and the girl throwing bread to the ducks in the tier-4 park, both v0.33's half marks. Down: the clouds of one playground probe, unnamed by the reader who named no clouds.

## The v0.33 list

| v0.33 reading | v0.34 result |
|---|---|
| R1 `read_bench` 0.875: "a child with short dark hair, in a yellow top, yellow shorts and red shoes" | **1.00** (4 items, 4 pictures); passes. Long hair, tied back, chosen on the bench (`isolation_v034.md`). The picture she failed in reads "a young woman with dark shoulder-length or long hair, a yellow dress and red shoes sits on a wooden bench reading a red book" (42), and the new park probe "a woman (or older girl) with long dark hair tied back, wearing a yellow dress and red shoes, reading a red book" (37). Its other two pictures have a child as the reader, read as a child |
| R2 `lost_balloon` 0.933 | **1.00** (15 items, 5 pictures). Not changed |
| R3 `blocked_hose` 0.917 | **0.917** (12 items, 3 pictures). Not changed. The half marks moved to a new probe, the goat on the hose by a man: "its hooves seem to be standing on the hose, which would explain why the water has stopped" in the free description, and "on or right next to the hose" in the inventory (81). The same goat by the grandmother reads in full: "A white goat with small horns is standing on the hose, with its back hooves right on top of it" (59) |
| R4 `ducks_bread` 0.944 | **1.00** (9 items, 3 pictures). Not changed |
| O1 The storm pointer and the washing | Revision 32 keeps the washing out of the pointing cone. The seed of v0.33's picture 60 placed again with the pointer moved, and the washing is still a second reading: "could be pointing at the storm clouds (warning of rain) or at the washing on the line (to bring it in)" (16). The reason given is the storm's own: the washing is what the rain will soak, not what the arm points at. The other two storm pointers read at the clouds, one with the cat on the fence as a second reading (58) |
| O2 Water in the wind | No can, pan or sprinkler in a windy picture now, and no reader saw water in the wind. The windy garden drew a remark of the same kind: "the wind is strong enough to blow the cap and washing sideways, yet the woman's pile of leaves stays neatly in place and her hair/dress are not blown" (38) |
| O3 The roller at the top of the patch | Three remarks on the roller (26, 58, 63), four in v0.33. A note |
| O4 The dustpan under the pointer's feet | Not said: the pointer stands elsewhere on that seed now |
| O5 Goats, figures over the pond, autumn leaves, the man's legs over the plank | Throughout, as since v0.11 |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.30 | v0.31 | v0.32 | v0.33 | v0.34 |
|---|---|---|---|---|---|
| Pass | 63 | 63 | 63 | 63 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 1 | 1 | 1 | 0 |

Every template was screened in at least three pictures (51 in three, 5 in four, 4 in five, 2 in six, one in eleven and one in twelve; 411 scored items behind the verdicts), and all 64 pass, for the first time since v0.29. `read_bench`, v0.33's one failure, is at 1.00.

## What reads least well (the v0.35 list)

| # | Template | v0.34 | What the readers saw | Fix for v0.35 |
|---|---|---|---|---|
| R1 | `blocked_hose` | 0.917 (12 items, 3 pictures) | The goat's hooves "on or right next to the hose" (81), where the grandmother's goat stands "with its back hooves right on top of it" (59) | Watch. If it falls again, look at where the hoof meets the hose in the man's picture |
| R2 | `bird_steals` | 0.958 (12 items, 4 pictures) | "A blue bird pecks at the sandwich lying beside him" (4), the theft not said | Watch |

## Unintended oddities

Named kinds, from the scorers' lists (`v034/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.35 |
|---|---|---|---|---|
| O1 | C | Wind and what it leaves still: "yet the woman's pile of leaves stays neatly in place and her hair/dress are not blown" | Picture 38; the hair and skirt in v0.33's picture 18 as well | Keep a swept or raked pile of leaves out of a windy picture, as revision 32 keeps water out. Hair and clothes would need the cast to blow, a larger job |
| O2 | C | The storm pointer and the washing, "to bring it in" | Picture 16 | A wider cone will not do it, as the washing is given as what is at risk. Keep the washing out of a storm pointer's picture, or let it stand as a reading of the storm |
| O3 | C | A seesaw rider who "seems to sit slightly above the plank rather than firmly on it" | Picture 57, two children | Watch: one picture, and the stuck girl's three read in full |
| O4 | C | A flower that "seems to touch or slightly overlap his face or cap brim" though the boy's feet are in front of the bed | Picture 22 | Watch |
| O5 | C | A gate's knob behind a head: "It could be the knob of the gate behind them, or it could be read as a hair bun" | Picture 74 | Watch |
| O6 | C | Older ones: goats out of place (four pictures), figures over the pond, autumn leaves under summer trees, the man's legs over the seesaw's plank, swing ropes hanging straight under motion lines | Throughout | Notes for the pilot |

## Placement

The garden, park and playground tier-4 cells placed on v0.33's seeds under revision 32, and v0.29 to v0.33's template set, forced on v0.32's seed, placed the street's again: the park's and the street's pictures are unchanged, and the garden's and the playground's differ only in the woman in yellow's hair. The tier-3 garden placed again on v0.33's seed 11954. The five isomorphs came back, three identical to v0.33's and two differing only in her hair, and the tier-4 one took 12 failed attempts, as in v0.33. The first probe pass left `walk_dog` and `dog_begs` short, and two more probes filled them. All 83 records rebuild identical to the pixel, and the library passes the validator in full, 342 of 342.
