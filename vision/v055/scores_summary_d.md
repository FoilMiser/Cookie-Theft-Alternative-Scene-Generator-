# Scores summary, set d (pic_76 to pic_99)

24 pictures, 256 scored items. I checked every item in keys_d.json against scores_d.json, picture by picture. Each item has exactly one score. None is missing and none was added that is not in the key.

## Mean score by item type

| Type | Items | Sum | Mean |
|---|---|---|---|
| entity | 145 | 137 | 0.945 |
| action | 74 | 74 | 1.000 |
| inference | 11 | 10.5 | 0.955 |
| contradiction_notice | 13 | 13 | 1.000 |
| contradiction_explain | 13 | 13 | 1.000 |
| **all** | **256** | **247.5** | **0.967** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_76 | i03 | There are a few white clouds | 0 | no clouds mentioned |
| pic_78 | i13 | There are a few white clouds | 0 | no clouds mentioned |
| pic_86 | i08 | There are a few white clouds | 0 | no clouds mentioned |
| pic_87 | i07 | There are a few white clouds | 0 | no clouds mentioned |
| pic_89 | i11 | There are a few white clouds | 0 | no clouds mentioned (town street) |
| pic_90 | i03 | There are a few white clouds | 0 | no clouds mentioned |
| pic_91 | i05 | There are a few white clouds | 0 | no clouds mentioned |
| pic_92 | i04 | There are a few white clouds | 0 | no clouds mentioned (town square) |
| pic_97 | i04 | The dog is blocking the water by standing on the hose | 0.5 | no water "could be because the dog is standing on it, or she may simply not have turned it on" (one of two readings) |

No item was misread. All eight zeros are the clouds item. In each of those descriptions the sky gets only "sunny", or nothing at all.

## Judgement calls scored 1

**Near words**
- Teenager described as "boy" (the red-cap, blue-hoodie figure): pic_77 i03, pic_79 i01, pic_82 i01, pic_87 i01, pic_88 i05, pic_89 i02, pic_97 i14. Scored on the action.
- Grandparent described as "older/elderly woman/man": pic_78 i09, pic_83 i11, pic_86 i06, pic_89 i09, pic_94 i01, pic_96 i01, pic_97 i01, pic_98 i01.
- pic_87 i05: woman described as "girl or young woman".
- pic_78 i08: the inference "girl dropped the ice cream" was only stated through the phrase "her dropped pink ice cream".
- pic_83 i03: the inference that the dog wants food rests on "begging toward the woman", which is an accepted phrasing.
- pic_89 i05: "pushing dust or dirt towards a dustpan" with the fork, which is counted as sweeping.
- pic_96 i03: "frying pan or saucepan". Either way it is a cooking pan, not a watering can.

**Target given beside another reading (target was the main reading)**
- pic_78 i04: kite stuck in the tree. They also suggested "just flying behind it", but leaned towards tangled.
- pic_80 i03: fish in the tree. They mentioned "possibly a toy/decoration", but said it looks like a real fish.
- pic_81 i03: ladder leaning on nothing. They mentioned "leaning on something far away", then rejected it.
- pic_82 i04 and pic_87 i04: box floating with nothing holding it up. "Thrown/falling" was given as the alternative.
- pic_86 i02: dog wants a walk. "Simply carrying the leash" was the alternative.
- pic_86 i05: water rising upward. They also suggested "a hose attached to the can".
- pic_89 i07 and pic_98 i03: giant dinner fork. "Pitchfork/garden fork drawn oddly" was the alternative.
- pic_90 i01: planting. "Digging it up/weeding" was the alternative, but the pot beside him pointed to planting.
- pic_97 i18: square wheel, would not roll. "Possibly a drawing glitch" was the alternative.

## Unintended oddities (not scored items)

**Figure pose or drawing**
- pic_79: the man's stride looks odd, legs in a big step but upper body upright.
- pic_84: the running man's back leg/foot looks odd, pointing down off the path edge.

**Overlap or depth**
- pic_79: the man overlaps the pond visually.
- pic_83: the man with the bucket overlaps the fence.

**Object support**
- pic_78: the bicycle stands upright with nobody holding it.

**Unclear motive or action**
- pic_81: the man runs with a worried face, but nothing explains what he is running to or from.
- pic_84: the man runs with an anxious face for no clear reason.
- pic_88: the kicked ball heads away from the other children, so it is unclear whom the boy is playing with.

**Animals:** no unintended oddities about animals were reported. By angle: three-quarter front 0, profile 0.
