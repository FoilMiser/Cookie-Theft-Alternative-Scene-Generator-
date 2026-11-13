# Scores summary, set d (pic_69 to pic_90)

Coverage check: every item of all 22 pictures in keys_d.json has exactly one score in scores_d.json (220 items). None is missing and none is invented. Item ids per picture match the key exactly.

## Mean score by item type

"misread" counts as 0 in the means.

| Type | Items | Total | Mean |
|---|---|---|---|
| entity | 126 | 119 | 0.944 |
| action | 69 | 67 | 0.971 |
| inference | 13 | 13 | 1.000 |
| contradiction_notice | 6 | 5.5 | 0.917 |
| contradiction_explain | 6 | 5 | 0.833 |
| **All** | **220** | **209.5** | **0.952** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_79 | i06 | Something is wrong with the wheelbarrow | 0.5 | Noted an unclear "square dark-framed object behind/under the wheelbarrow" but did not say the wheelbarrow was wrong |
| pic_79 | i07 | The wheelbarrow has square wheels, so it could not roll | misread | Read the square wheel as "a hose reel or a fan-like grate" |
| pic_79 | i09 | A girl is throwing a ball | 0.5 | Roles reversed: the girl runs to catch a ball the woman threw |
| pic_79 | i10 | A woman is catching the ball | 0.5 | Roles reversed: the woman "has just thrown" the ball |
| pic_90 | i10 | A girl is throwing a ball | 0.5 | Gave two readings (girl throws to woman, or woman throws to girl), slightly favouring the right one |
| pic_90 | i11 | A woman is catching the ball | 0.5 | Same two readings |
| pic_84 | i07 | There are a few white clouds | 0 | Not mentioned |
| pic_85 | i03 | There are a few white clouds | 0 | Not mentioned |
| pic_86 | i06 | There are a few white clouds | 0 | Not mentioned |
| pic_87 | i04 | There are a few white clouds | 0 | Not mentioned |
| pic_88 | i07 | There are a few white clouds | 0 | Not mentioned |
| pic_89 | i04 | There are a few white clouds | 0 | Not mentioned |
| pic_90 | i13 | There are a few white clouds | 0 | Not mentioned |

All 7 zeros are clouds, in pic_84 to pic_90. In earlier pictures the clouds were picked up only from the inventory line ("sun, two clouds"), and that line stops appearing from pic_84 on.

## Judgement calls scored 1

Near words (the action or object is right, the person label differs):
- pic_69 i03, pic_89 i02: "man is sweeping", but the describer said a boy.
- pic_80 i01, pic_81 i01, pic_82 i05, pic_83 i03, pic_88 i01, pic_90 i04: "teenager", but the describer said "boy in a red cap and blue hoodie".
- pic_75 i01, pic_77 i04, pic_81 i02, pic_84 i05: "grandfather", but the describer said "older/old man".
- pic_77 i05, pic_84 i04: "grandmother", but the describer said "elderly/older woman".
- pic_90 i09: "dog is sleeping", but the describer said "white puppy".
- pic_72 i05: "big tree", but the describer said "a tree" that the woman stands under.

Target given beside another reading (the main description states the target and the unsure section offers an alternative):
- pic_71 i02: dog wants a walk, or "picked up the lead to play".
- pic_83 i02: waiting to be walked, or "simply holding it while waiting by the door".
- pic_77 i03: begging for the ice cream, or "simply sitting up looking at her".
- pic_90 i03: "probably what the brown dog wants", or just sitting up near the bench.
- pic_70 i02: trying to catch the cap, or "waving/throwing it" (the describer favours the wind reading).
- pic_72 i02: cat sleeping, or "just resting with eyes closed" ("cat" is accepted anyway).

## Unintended oddities (not scored items)

Scene logic or staging (5):
- pic_70: the wind is blowing hard but the fishing line hangs straight and nobody else seems affected.
- pic_82: a sprinkler and hose in a public park looks a little unusual.
- pic_84: the boy stands too far back for his crumbs to reach the pond.
- pic_85: the watering can is held at an odd stretch, its spout well to the right of the flowers.
- pic_77: a wooden crate sits alone on the pavement with no obvious purpose.

Overlap or placement (1):
- pic_84: the photographer overlaps the pond's end and could look as if he is standing in the water.

About animals: none. No oddity was reported about any animal, so the count by angle is zero for every angle (three-quarter front 0, profile 0).

Left out as hedges about small details: the man overlapping the bench backrest (pic_72), the man partly off the blanket (pic_76), the ball overlapping the shoe and the arc offset (pic_79), the stiff roller angle (pic_80), the roller beside the painted section (pic_88), the head tilt (pic_89), and the hand overlapping the crates (pic_87). Also left out: oddities that are themselves scored items, such as the adult on the seesaw (pic_75) and the soaked box (pic_79, pic_82).
