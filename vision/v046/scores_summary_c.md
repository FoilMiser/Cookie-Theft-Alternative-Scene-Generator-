# Scores, set C (pic_51 to pic_74), v0.46

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 157 | 1.000 |
| action | 77 | 0.994 |
| inference | 16 | 1.000 |
| contradiction_notice | 8 | 0.812 |
| contradiction_explain | 8 | 0.875 |
| all | 266 | 0.989 |

Misread counts as 0 in the means.

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Score | Target | What the describer said |
|---|---|---|---|---|---|
| pic_52 | i03 | contradiction_notice | 0.5 | Something is wrong with the water from the watering can | only in unsure section: arcs upward, 'looks more like a spray than a pour'; never called wrong |
| pic_53 | i02 | action | 0.5 | A bird is pecking at a sandwich on the bench | bird 'perched right beside' the sandwich, not pecking it |
| pic_53 | i11 | contradiction_notice | 0 | Something is wrong with the dog | dog with newspaper reported as ordinary; no oddity noted |
| pic_53 | i12 | contradiction_explain | misread | The dog is reading a newspaper, but dogs can't read | dog 'holding a newspaper in its mouth' (carrying, not reading) |

## Unintended oddities, by kind

### Placement or drawing ambiguity (3)
- pic_57: the cheering boy's shadow is drawn apart from his feet: jumping or a misplaced shadow
- pic_60: the grandmother at a glance seems to stand in the pond
- pic_70: hard to tell whether the children are seated on the seesaw plank or perched slightly above it

### Unusual but possible situation (3)
- pic_63: a goat tied up in a public park is a little unusual [goat, three-quarter front]
- pic_65: eating ice cream on such a gloomy day is a little unusual
- pic_69: two people eat the same pink ice cream but no ice-cream seller is visible

### Oddities about animals, by angle

| Angle | Count | Cases |
|---|---|---|
| three-quarter front | 1 | pic_63 goat tied up in a park |
| profile | 0 | none |

No describer reported an animal's body as malformed or hard to read; the only animal oddity is situational (a tethered goat). 18 of 24 pictures have no unintended oddity.

## Completeness check

All 266 items of all 24 pictures in keys_c.json have exactly one score in scores_c.json; none is missing and none is invented (item ids checked against the key for every picture).
