# Scores summary, set d (pic_75 to pic_98)

Scored blind descriptions against keys_d.json. Misread counts as 0 in the means.

## Mean score by item type

| Type | Items | Mean | Below 1 |
|---|---|---|---|
| entity | 152 | 0.967 | 5 |
| action | 71 | 0.972 | 3 |
| inference | 13 | 0.769 | 4 |
| contradiction_notice | 11 | 1.000 | 0 |
| contradiction_explain | 11 | 1.000 | 0 |
| all | 258 | 0.961 | 12 |

## Items scored 0, 0.5 or misread

| Pic | Id | Score | Target | What the describer said |
|---|---|---|---|---|
| pic_82 | i10 | misread | The teenager is going to trip over a box | box seen but placed 'behind him, so he is not about to trip on it'; predicts he may bump into the birdhouse pole instead |
| pic_85 | i01 | misread | A man is sweeping | read as digging at the edge of the path with a giant fork, not sweeping |
| pic_92 | i07 | 0 | There are a few white clouds | no clouds mentioned (sun and wind lines only) |
| pic_95 | i05 | 0.5 | The dog is blocking the water by standing on the hose | two readings: paw squashing the hose and stopping the water, or just overlapping it in the drawing |
| pic_95 | i10 | 0 | There are a few white clouds | no clouds mentioned |
| pic_96 | i02 | 0.5 | The dog is standing on the hose | 'dog stands by the hose'; unsure: 'may be standing on the hose or just in front of it' |
| pic_96 | i03 | 0.5 | No water is coming out | 'a drop of water coming out', dripping nozzle; not said that the hose is not working |
| pic_96 | i04 | 0 | The dog is blocking the water by standing on the hose | no link made between the dog and the water |
| pic_96 | i20 | 0 | There are a few white clouds | no clouds mentioned |
| pic_97 | i04 | 0.5 | The dog is blocking the water by standing on the hose | 'which may be why the water is not flowing', but unsure section says the paw may just overlap the hose |
| pic_97 | i06 | 0 | There are a few white clouds | no clouds mentioned |
| pic_98 | i04 | 0 | There are a few white clouds | no clouds mentioned |

## Unintended oddities by kind

### Figure hovering above the surface it sits on (2)
- pic_93: the boy sits slightly above the seesaw plank rather than on it
- pic_94: the child sits slightly above the slide surface

### Drawing or body-rendering oddity (4)
- pic_78: the dog's front legs and body are drawn in a tight, slightly tangled pose [dog, three-quarter front]
- pic_89: a semi-transparent patch on the woman's dress, as if her arm is drawn faintly through her body
- pic_90: the boy's legs look short or tucked, hard to tell if straight or bent
- pic_92: the red-shirted man's face mark looks like a smudge rather than a moustache or beard

### Odd placement (2)
- pic_85: the man seems to dig into the paved path or its edge
- pic_90: the lamppost stands alone on open grass away from the path

### Object not visibly supported (1)
- pic_88: the bikes sit inside the rack outlines rather than leaning on them

### Oddities about key animals, by angle

- dog, three-quarter front: 1
- profile: 0

Pictures with no unintended oddity: 16 of 24.

## Completeness check

Every item in keys_d.json has exactly one score: 258 items across 24 pictures; none missing, none invented (checked by script).
