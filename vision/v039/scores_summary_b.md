# v0.39 picture-description scoring, set B (pic_25 to pic_48)

Scored from `desc_pic_25.md` ... `desc_pic_48.md` against `keys_b.json`, using each whole file (free description, inventory and unsure section). Per-item scores and evidence are in `scores_b.json`.

## Completeness check

- 24 pictures, 246 scored items in `keys_b.json`; 246 scores written.
- Checked by script against the key: every item of every picture has exactly one score; no item is missing, none is invented, no id is duplicated, and no picture has more than three unintended oddities.

## Mean score by item type

| Item type | Items | Scored 1 | Mean score |
|---|---:|---:|---:|
| entity | 145 | 145 | 1.000 |
| action | 72 | 71 | 0.993 |
| inference | 17 | 16 | 0.971 |
| contradiction_notice | 6 | 6 | 1.000 |
| contradiction_explain | 6 | 6 | 1.000 |
| **all** | **246** | **244** | **0.996** |

## Items scored 0, 0.5 or misread

Scored 0: 0. Scored 0.5: 2. Misread: 0.

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_26 | i02 | inference | The dog wants to go for a walk | 0.5 | 'as if it wants to go for a walk or wants to go inside' - the walk is only one of two readings |
| pic_47 | i03 | action | A man is sweeping | 0.5 | man with the fork is 'scraping or digging at a small pile of dirt'; sweeping it toward the dustpan is offered only as an alternative reading |

## Unintended oddities, grouped by kind

13 oddities in 11 of 24 pictures; 13 pictures had none.

### human pose / limbs (4)

- pic_32: grandfather's arms are drawn as one long flat white shape stretched out to the nozzle, looking stiff or odd; his face is hard to read under the cap
- pic_33: grandfather's legs look crossed or tucked on the seesaw plank and it is hard to see how he is balanced
- pic_46: grandfather's feet are placed so it is hard to tell which leg is stepping forward; could look like he is being tugged along
- pic_48: grandmother's legs make her walking direction unclear; she seems to push the pram off the path toward the picture edge

### scene plausibility / content (3)

- pic_32: a goat loose in a family garden is unusual [goat, profile]
- pic_37: no people or other activity, so the park looks like a backdrop or an 'empty' version of the scene
- pic_38: dark storm clouds overhead while people calmly eat ice cream and read outdoors looks a bit mismatched

### leaf colour (3)

- pic_36: swept leaves are a mix of green and brown, so it is unclear whether they are fallen leaves or garden clippings
- pic_43: some raked leaves are green rather than brown or autumn-coloured, which looks odd for fallen leaves
- pic_45: some swept leaves are green, which is slightly odd for fallen leaves

### prop / physics rendering (2)

- pic_34: water pours from a shallow pan in a long, steady stream, which looks slightly strange
- pic_45: the hose under the dog's paws looks like a dark flattened blob that could be a puddle or a bulge [dog, profile]

### overlap / placement (1)

- pic_31: girl slightly overlaps the sandpit's wooden frame; unclear whether she kneels in the sand or on the edge

### Oddities about animals, by angle

| Angle | Animals in key | Oddities | Where |
|---|---:|---:|---|
| profile | 9 | 2 | pic_32 (goat), pic_45 (dog) |
| three-quarter front | 9 | 0 | - |

### Hedges left out of the oddity lists

These were reported only as small ambiguities, not as looking wrong, so they are not counted above:
- pic_25, pic_30: the dog's face has one eye that looks shut, read as happy or winking [dog, three-quarter front].
- pic_42: the bird faces the cat, so it may be staring back rather than pecking [bird, profile].
- pic_39: the walking boy and woman overlap the pond in the picture, but the describer reads them as standing on the grass in front of it.
- pic_38: the grandmother points up and to the right while the bird is up and to the left; the describer takes the clouds as her likely target.
- pic_47: the red object by the dirt pile could be a dustpan, trowel or spade blade.
