# v0.48 scoring summary (key set a)

Coverage check: all 22 pictures (pic_01 to pic_22) and all 257 items in keys_a.json have exactly one score in scores_a.json. No item is missing and none is invented. The ids match the key in each picture, in the key's order.

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| action | 86 | 86 | 1.000 |
| entity | 130 | 121 | 0.931 |
| inference | 23 | 22 | 0.957 |
| contradiction_notice | 9 | 9 | 1.000 |
| contradiction_explain | 9 | 9 | 1.000 |
| **all** | **257** | **247** | **0.961** |

## Items scored 0, 0.5 or misread

No item got 0.5 or misread. All 10 of these are 0 (not mentioned).

| Pic | Id | Target | What the describer said |
|---|---|---|---|
| pic_13 | i10 (inference) | It is about to rain | Describes "grey sky with dark storm clouds" and the child "pointing up at the sky, perhaps at the storm clouds", but never says rain is coming |
| pic_17 | i10 | There are a few white clouds | No clouds mentioned |
| pic_17 | i11 | There is a tree | No tree mentioned |
| pic_18 | i03 | There are a few white clouds | No clouds mentioned |
| pic_19 | i19 | There is a tree | No tree mentioned (only a birdhouse on a pole) |
| pic_20 | i05 | There are a few white clouds | No clouds mentioned |
| pic_20 | i06 | There is a tree | No tree mentioned (only a bush and potted plants) |
| pic_21 | i04 | There are a few white clouds | No clouds mentioned |
| pic_22 | i11 | There are a few white clouds | No clouds mentioned |
| pic_22 | i12 | There is a tree | No tree mentioned |

Pattern: 9 of the 10 misses are background clouds and trees in v0.48 pictures with more going on. The only missed inference is the rain prediction in pic_13.

## Judgement calls scored 1

Near words (the age group was read differently; the action is right):
- pic_02 i02: woman eating ice cream. Called a "girl in a yellow dress". The unsure section also hedges between licking it and holding it near her face.
- pic_11 i01: man on the low end of the seesaw, reading. Called a "bigger boy in a green shirt".
- Teenager called "boy" (red cap, blue hoodie) in: pic_01 i05, pic_04 i12, pic_07 i04, pic_12 i06, pic_13 i01, pic_17 i08, pic_19 i05, pic_20 i01, pic_22 i09.
- pic_19 i20: the fence is named only as "by the gate" ("gate" is an accepted phrasing).

Target given with another reading beside it:
- pic_04 i04: grandfather will trip over the box. Unsure section: "he might step around it".
- pic_05 i03: man will trip over the box. Free text says "may be about to trip"; unsure section says he could have already passed it.
- pic_09 i07: grandmother will trip. Unsure section: the box may be slightly to the side, so she might miss it.
- pic_10 i04: grandmother will trip. Unsure section: she might pass just beside it.
- pic_06 i02: dog wants a walk. Unsure section: "could be waiting for a walk or just carrying it".
- pic_07 i03 and pic_20 i03: water going up. A spray that rises before falling, or the boy flicking the can, is offered as the less likely reading.
- pic_13 i04 and pic_19 i04: dog blocking the hose. Unsure section: the dog could just be standing near it, or "not certain".
- pic_15 i04/i05 and pic_22 i08/i09: thrower and catcher. Reversed roles are offered as a second reading.
- pic_17 i01: woman eating ice cream. She may instead be holding it out of the dog's reach.

## Unintended oddities (not scored items)

None of these is about an animal, so the count by animal angle is zero for every angle (profile 0, three-quarter front 0).

Pose or anatomy (3):
- pic_11: the seated man's legs look slightly overlapped with the seesaw board.
- pic_18: the man's body looks twisted toward the pond with his legs off the blanket; unclear if he is sitting or half-lying.
- pic_18: the man's face is hard to read: a relaxed eyes-closed smile or a pained grimace.

Hand and prop contact (3):
- pic_01: the paint roller looks slightly detached from the man's hands at the top of the handle.
- pic_20: the watering can is small for the boy and held level, not tilted, so the pour looks odd.
- pic_20: the water stream does not clearly start at the spout.

Placement off the path (2):
- pic_02: the girl walks on the very edge of the path with one foot on the grass.
- pic_21: the older man walks on the grass beside the path rather than on it.

Direction or role unclear (2):
- pic_05: unclear which way the reading man is walking; he may already have passed the box.
- pic_22: unclear who threw the ball, because both children have their arms forward.
