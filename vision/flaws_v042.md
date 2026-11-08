# v0.42 blind screen: what it found (the work list for v0.43)

The v0.42 screen read the set's 21 pictures and 72 probes with the prompts of v0.39 (`screen_prompts.md`). There were twelve readers of seven or eight pictures and four scorers of 23. Two pictures had a fresh reader and a fresh scorer of their own:
- picture 10, redrawn after the screen;
- picture 93, a probe added after it.

The oddity tally is by angle, as in v0.39. Keys, descriptions and scores are in `v042/`.

v0.42 worked two lists, `flaws_v041.md` and Sam's notes on the figures (`tpdb_work/figure-fixes-v041.md`). The bench (`isolation_v042.md`) took these into the cast (builder 0.42.0):
- **the goat redrawn:** a wedge head on a neck, a level back a fifth longer on shorter legs, split hooves, a beard and a collar;
- **the dogs:** a narrow blaze for the tan dog's bib, darker far legs, a patch on the spotted dog's foreleg, a longer muzzle;
- **the begging dog on its haunches**, and the reading dog's hind legs folded, both with a shorter trunk;
- **the trousers:** no hip node, so no V across the front, and no belt under an untucked tee;
- **shoes** with a longer toe and a sole, and bare legs with a calf;
- **the woman in yellow** with her hair in a low bun.

Placement revision 40 tethers the grazing goat and draws the songbirds and the duck at 45 as well as 90. It keeps anyone else with an ice cream away from the begging dog, and, after the screen, the square-wheeled bicycle off the stall and the bench. Every person, dog and goat is drawn anew, so no picture is identical to v0.41's, and there is no retest this time.

## Headline (the 21 pictures of the set)

| | v0.38 (21) | v0.39 (21) | v0.40 (21) | v0.41 (21) | v0.42 (21) |
|---|---|---|---|---|---|
| Things | 1.00 | 1.00 | 0.991 | 1.00 | 0.991 |
| Actions | 1.00 | 1.00 | 0.996 | 1.00 | 1.00 |
| Inferences | 0.985 | 1.00 | 0.986 | 0.958 | 0.939 |
| Contradictions | 1.00 | 1.00 | 1.00 | 1.00 | 0.942 |
| All items | 0.998 | 1.00 | 0.993 | 0.995 | 0.984 |
| Misread items | 0 of 286 | 0 of 287 | 0 of 287 | 0 of 287 | 0 of 290 |
| Readers' remarks per picture (all screened pictures) | 3.38 | 3.10 | 3.04 | 3.17 | 3.05 |
| Oddities per picture, as logged by the scorers | 0.8 (at most 3) | 0.8 (at most 3) | 0.5 (at most 3) | 0.4 (at most 3) | 0.7 (at most 3) |

Across all 93 pictures, 1010 of the 1020 scored items had full marks and none was misread. The ten under full marks:
- **Three on the reading dog, half right, in two pictures of the set.** "Either the puppy is 'reading' it like a person, or it has grabbed or knocked over someone's paper" (42, twice); the dog "just holding a fetched paper" as the second reading (78).
- **The trip, not inferred (51).** The boy reads as he walks and the box is "on the grass in front", but "has no obvious owner or purpose". The reading dog sits just beside him with its paper.
- **Three more inferences, half right:**
  - the balloon "has just got away", or the girl "could still be holding its string" (10);
  - the dropped ice cream: "not clear whether the dog took the ice cream or the child dropped it" (59);
  - the dog by the door "waiting to be taken for a walk or to be let in" (64, a probe).
- **A probe's ice cream, half right (49):** "as if eating a small ice cream or smelling something".
- **Two setting items, not mentioned:** the clouds (42) and a tree (52).

The scorers gave none, three, five and one items under full marks, of 225, 270, 237 and 250. Picture 10's scorer gave one of 25, and picture 93's none of 13.

**What the full marks rest on.** The scorers' notes mark 10 credits they gave in full where the free description commits and the unsure section adds another reading (16 in v0.41). If those are halved, 61 of 64 templates pass (`tpdb_work/strict42.py`). Three fall:
- `about_to_trip`, already under the gate;
- `photo` (0.833, 3 items), the camera "or ... binoculars" (04);
- `plant_flowers` (0.667, 3 items): "planting the potted flower, picking flowers, or weeding" (02), and "about to plant it ... or putting it down" (16).

`blocked_hose` and `rain_coming`, v0.41's two, both read 1.00, and 1.00 strictly.

## After the screen: one rule, one picture read again, one probe added

The first count had 63 of 64 templates passing. `square_wheel` was at 0.867, on picture 10, the tier-4 street's isomorph: there the bicycle stood in front of the fruit stall's legs, its square wheels among them. The reader saw a "teal bicycle parked against the stall", with nothing wrong.

**The rule.** Revision 40 now keeps the square-wheeled bicycle or barrow clear of the stall and the bench (`templates.py`, `patch42aa.py`). Every record was rebuilt, and all but that isomorph came back identical; it no longer placed. A new tier-4 isomorph was searched (`T4_street_s37111_iso`, the park's tier 4 drawn as a street), read by a fresh reader and scored by a fresh scorer. The old picture's description, scores and key are kept in `tpdb_work/set42/old_iso/`.

**What the swap moved.** `square_wheel` passes now, at 1.00 in four pictures. But the old picture had also been `about_to_trip`'s fourth picture, read in full, and that template now falls (below).

**The probe.** The swap took `balloon` and `wave` from three pictures to two. `windy_hat` had been in two all along: `probes.py` ended `SHORT {'windy_hat': 1}`, a count, which was read as a shortfall, and one probe was added where two were needed. One more probe puts all three at three (picture 93: a hat blown off, a boy waving, a child with a balloon; `tpdb_work/probe_extra42.py`). Its reader and scorer also had it alone.

## The v0.41 list and Sam's notes

| v0.41 reading, or the notes' item | v0.42 result |
|---|---|
| R1 `blocked_hose` 0.896 read strictly | **1.00, and 1.00 read strictly** (24 items, 6 pictures). The crimp at the paw was not taken: v0.41's hose already read as blocked under the paw, and the fold read as "a separate stray bit" (`isolation_v042.md`) |
| R2 `rain_coming` 0.889 read strictly | 1.00 (15 items, 5 pictures; probes.py asked for five) |
| R3 `sweep`, "a yellow broom or fan rake" | 1.00 in 12 pictures, and no "fan rake" |
| R4 `kite_in_tree`, `ice_cream_drop` | 1.00 and 0.975 |
| O1, notes' item 5: the begging dog's body at 90, "upright", "kneeling", "human-like" | **Redrawn** (`TPDB_BEG42` B). Begging in all five pictures, at 90 and 45, and no reader saw kneeling or a person. Once "it could also be read as the dog jumping up" (88) |
| O1: a second ice cream near the begging dog | **Revision 40's zone.** In both pictures with another eater (35, 88), the reader gave the eater on the bench |
| O3, item 8: the woman in yellow called "girl" | **Redrawn, no gain** (`TPDB_MEI42` B, a low bun): "girl" in 6 of her 14 pictures, five hedged ("woman or girl", "young woman or teenage girl"). It was 8 of 24 in v0.41, six hedged. Her bun reads as "a dark ponytail" |
| O4, item 1: the goat | **Redrawn and tethered** (`TPDB_GOAT42` C, `GOAT42` T). Tied to a stake in six descriptions, and out of place only twice, both softened: "A goat in a back garden is unusual but not impossible" (30, on the hose, with no tether), "a little unusual, but it is tethered and calm" (54). No sheep, and nothing said of its head or neck. The tether once "thin and partly hard to follow" (75) |
| Item 2: the belt as a ring | **Gone** under a tee (`TPDB_BELT42` B). No description mentions a belt, briefs or a waistband; v0.41's mentioned a belt in six |
| Item 3: the V across the trousers | **Gone** (`TPDB_MID42` C); not remarked |
| Item 4: the dog's chest "like a bib or nappy", the white legs | **Redrawn** (`TPDB_DOG42` B). No bib, nappy or stilts in 30 pictures with a dog |
| Item 5: the reading dog's legs stretched out "like a person sitting" | **Redrawn**, the hind legs folded and the trunk shorter. No reader called it a person in six pictures. But its paper "stands upright on its own" in three descriptions (one in v0.41), and twice it was a paper "grabbed" or "fetched": `dog_reading` 0.917 (18 items, 6 pictures) |
| Item 6: shoes, calves; knees | **Redrawn** (`TPDB_FOOT42` B); not remarked. The knees were not changed: they already bend about 20 degrees, toward the camera in front views |
| Item 7, O5: the cat | **Not changed** (`TPDB_CAT42` O: tangled either way on the bench). Once at 45 "bunched together in a tangle of lines" (76), once "a little stick-like" in profile (09) |
| Item 9: birds and duck only in profile | **At 45 too** (`BIRD42` B). Every (template, angle) pair of the four bird templates passes, 1.00 each |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.38 | v0.39 | v0.40 | v0.41 | v0.42 |
|---|---|---|---|---|---|
| Pass | 64 | 64 | 64 | 64 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 0 | 0 | 0 | 1 |

Every template was screened in at least three pictures. By count: 42 in three, 7 in four, 7 in five, 4 in six, 2 in seven, 1 in twelve and 1 in nineteen, with 474 scored items behind the verdicts.

**The one failure.** `about_to_trip` is at 0.889 (9 items, 3 pictures), on the one zero in picture 51. It was 1.00 in five pictures in v0.41, and its drawing has not changed.

The lowest that pass:
- `dog_reading` (0.917, 18 items, 6 pictures);
- `dog_wants_walk` (0.917, 6 items, 3 pictures);
- `lost_balloon` (0.967);
- `ice_cream` (0.974);
- `ice_cream_drop` (0.975).

**Per angle** (`v042/gate_yaw.json`), all 25 (template, angle) pairs pass: v0.41's 17, and the four bird templates at 90 and 45. The lowest is `ice_cream_drop` at 90 (0.938), on the half mark above. The begging dog and the goat are at 1.00 at every angle they are drawn at.

## What reads least well (the v0.43 list)

| # | Template | v0.42 | What the readers saw | Fix for v0.43 |
|---|---|---|---|---|
| R1 | `about_to_trip` | 0.889 (9 items, 3 pictures) | The box "has no obvious owner or purpose", beside a boy reading as he walks, with the reading dog and its paper just behind him (51) | Keep the reading dog away from the trip (two readers side by side), and read the trip again; the drawing is v0.41's, which read 1.00 in five pictures |
| R2 | `dog_reading` | 0.917 (18 items, 6 pictures) | The paper "stands upright on its own" (three descriptions, one in v0.41), so the dog "has grabbed or knocked over someone's paper" (42), "just holding a fetched paper" (78) | With the shorter trunk the forepaws reach less of the paper: let them grip it again (the paws higher, or the paper drawn from them), bench beside v0.41's |
| R3 | `plant_flowers`, `photo` | 1.00; read strictly 0.667 and 0.833 (3 items each) | "planting the potted flower, picking flowers, or weeding" (02); the camera "or ... binoculars" (04) | Watch: three items each, untouched; five probes each next time |

## Unintended oddities

Named kinds, from the scorers' lists (`v042/scores_summary_a.md` to `_f.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.43 |
|---|---|---|---|---|
| O1 | C | The woman in yellow "girl" in 6 of her 14 pictures, five hedged; the low bun reads as a ponytail | Throughout | Back to v0.41's bob, or another adult cue read in whole pictures (the bench reads her as a woman either way) |
| O2 | C | The woman in purple "girl" or "girl or young woman" in about ten of her 23 pictures | Throughout | As O1: an adult cue for her, read in whole pictures |
| O3 | C | The stopped hose's swelling as "a puddle" or "a drawing glitch" (nine descriptions; eight in v0.41) | Hose pictures | Watch: unchanged since v0.33, and the hose reads as blocked |
| O4 | C | The cat's legs at 45 once, and "stick-like" once in profile | 76, 09 | Watch, as v0.41 |
| O5 | C | The goat "unusual" twice, softened by the tether in the park; its tether rope hard to follow once | 30, 54, 75 | Notes for the pilot. Tether the goat on the hose too, or leave it as a garden goat |
| O6 | C | Older ones: the seesaw plank "passes under/through his thighs region" (26); figures over the prop beside them | Throughout | Notes for the pilot, as before |

## Placement

**The set.**
- **Tiers 1 to 3.** Every cell placed under revision 40 on the same base seeds as v0.41, two of the twelve on the same layout (the garden's tiers 1 and 2), all drawn anew with the v0.42 cast.
- **Tier 4.** The park placed on v0.41's seed and layout. The street placed on v0.29 to v0.41's forced set, on its fourth layout. The garden placed on the third seed of the search, and the playground on the 40th.
- **The isomorphs.** Four were found in the first pass. The tier-4 one was searched again after the screen's rule and placed on its first seed.

**The probes.**
- **The first pass** (`probes.py 3`, five for `blocked_hose` and `rain_coming`) left `windy_hat` short.
- **The pass stratified by angle** added 15 probes. The begging dog at 45 had no picture before it.
- **Two more were forced for `windy_hat`,** the second with `wave` and `balloon` after the screen.

All 93 records rebuild identical to the pixel, and the library passes the validator in full.
