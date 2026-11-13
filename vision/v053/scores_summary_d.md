# Scores summary, set d (pic_76 to pic_99)

Coverage check: all 24 pictures in keys_d.json are scored. All 256 items have exactly one score each. No item is missing and no item was invented (checked by script against keys_d.json).

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 145 | 0.979 |
| action | 74 | 1.000 |
| inference | 11 | 1.000 |
| contradiction_notice | 13 | 1.000 |
| contradiction_explain | 13 | 1.000 |
| **All** | **256** | **0.988** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_76 | i03 | There are a few white clouds | 0 | Only "sunny"; clouds not mentioned anywhere |
| pic_78 | i13 | There are a few white clouds | 0 | Only "sunny playground"; clouds not mentioned |
| pic_89 | i11 | There are a few white clouds | 0 | Only "sunny town street"; clouds not mentioned |

There were no 0.5 scores and no misreads.

## Judgement calls scored 1

| Pic | Id | Target | Why it was a call |
|---|---|---|---|
| pic_78 | i04 | Kite got stuck in the tree (inference) | Says "stuck in the branches", but the unsure section also offers "flying just behind/through it" (it calls stuck the more likely reading) |
| pic_78 | i08 | Girl dropped the ice cream (inference) | Says "dropped pink ice cream" that "has fallen", with her empty cone; does not say outright that she dropped it |
| pic_82 | i04 | Box floating with nothing holding it up | Says "floating or flying"; also offers "thrown and about to fall"; but says "nothing holds it up" |
| pic_87 | i04 | Box floating with nothing holding it up | Says "nothing holding it up"; also "or as if it is falling" |
| pic_83 | i01 | Woman eating ice cream on the bench | Calls her a "girl/young woman" (near word) |
| pic_83 | i03 | Dog wants the food (inference) | Only "begging", which is an accepted phrasing but is also the evidence for i02 |
| pic_85 | i04 | Water going up | The unsure section offers a second reading, a hose spraying up out of the flowers; the main reading is a stream rising from the can |
| pic_86 | i02 | Dog wants a walk (inference) | Says "as if it wants to go for a walk"; the unsure section adds "or just carrying the leash" |
| pic_88 | i03 | Package will get soaked (inference) | Says "getting wet" and "being soaked", but is unsure whether this is meant as a problem |
| pic_88 | i07 | Girl catching the ball | Says "ready to catch" and "waiting to catch", not that she is catching it |
| pic_89 | i05 | Man is sweeping | Says "pushing dust towards a dustpan", and "sweeping dust" in the inventory |
| pic_94 | i03 | Grandfather heavier, so girl stuck (inference) | Gives the cause as "because he is holding the low end down" (accepted "stuck because he is sitting on the other end"); does not mention weight |
| pic_97 | i02 | Dog standing on the hose | The unsure section says the dog may only be standing next to the hose, but its paw seems to press on it |
| pic_98 | i01 | Grandmother sweeping | Says "scrape or sweep"; the unsure section says "looks like sweeping" |
| pic_77 i03, pic_79 i01, pic_82 i01, pic_87 i01, pic_88 i05, pic_89 i02, pic_91 i02, pic_97 i14 | | "Teenager" items | Each figure is called a "boy" (near word for the age) |
| pic_83 i11, pic_94 i01, pic_96 i01 | | "Grandfather" items | Each is called an "older man" (near word) |
| pic_78 i09, pic_86 i06, pic_89 i09, pic_97 i01, pic_98 i01 | | "Grandmother" items | Each is called an "older woman" (near word) |

## Unintended oddities (not scored items), grouped by kind

**Figure overlapping scenery (depth/placement).** The describer resolved both of these as standing on the grass.
- pic_79: the man's upper body overlaps the pond, so he could look as if he is walking on the water.
- pic_84: the woman's dress overlaps the pond outline, so she could look as if she is standing in the water.

**Pose or contact with a prop**
- pic_94: the seesaw bar seems to run past or through the man's legs, so he looks half sitting and half standing.

**Unsupported object**
- pic_78: the bicycle stands upright on the grass with no one holding it and no visible stand. This is separate from the scored square wheels.

**About animals: none.** No oddity was reported about any animal, so the count by angle is zero for every angle (profile 0, three-quarter front 0).

Pictures with no unintended oddities: 76, 77, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99.
