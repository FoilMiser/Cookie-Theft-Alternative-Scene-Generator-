# v09 retest: scoring against keys_a.json

Scored from `desc_pic_01.md` to `desc_pic_20.md` (free description, inventory and unsure section together) against `keys_a.json`. Scores: 1 = conveyed, 0.5 = partial, 0 = absent, misread = seen as something else (counted as 0 in means). Full per-item evidence is in `scores_a.json`.

## Mean score by item type

| Type | Items | Mean | 1 | 0.5 | 0 |
|---|---|---|---|---|---|
| entity | 123 | 1.000 | 123 | 0 | 0 |
| action | 89 | 0.972 | 84 | 5 | 0 |
| inference | 22 | 0.932 | 20 | 1 | 1 |
| contradiction_notice | 11 | 1.000 | 11 | 0 | 0 |
| contradiction_explain | 11 | 1.000 | 11 | 0 | 0 |
| contradiction (both) | 22 | 1.000 | 22 | 0 | 0 |
| **all items** | 256 | 0.984 | 249 | 6 | 1 |

No item was scored misread.

## Items scored 0 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_13 | i10 | inference | The woman is going to trip over a bucket | 0 | no trip/fall prediction; bucket read as 'possibly a laundry or peg bucket' |

### Items scored 0.5 (for reference)

| Pic | Id | Type | Target | What the describer said |
|---|---|---|---|---|
| pic_09 | i08 | action | A girl is holding an empty cone, looking upset | girl 'looking at her hand, maybe at an empty ice-cream cone'; cone only tentative ('hard to make out'); upset not mentioned |
| pic_11 | i01 | action | A child is holding an empty cone, looking upset | boy 'holding an ice-cream cone' that 'appears empty or nearly empty' but 'can't tell whether any ice cream is left'; upset not mentioned |
| pic_13 | i08 | action | A woman is reading while walking | woman walking while 'looking at an open book or a white sheet'; reading-while-walking only one of two readings (other: laundry to hang) |
| pic_15 | i02 | action | A grandfather is watering the flowers | older man 'pouring from a teal watering can', but describer says 'nothing is actually being watered; the flower planter is ... not under the stream' |
| pic_15 | i11 | action | A girl is holding an empty cone, looking upset | girl 'holds a cone that looks empty' but describer says 'she does not look especially upset' |
| pic_18 | i04 | inference | The kite got stuck in the tree | 'the main question is whether the kite is flying or caught in the tree'; stuck only one of two readings |

### Scoring conventions applied

- 1 when the describer's committed or favoured reading (including hedges like 'probably', 'looks like') conveys the target or an accepted phrasing; an alternative reading in the unsure section does not lower it.
- 0.5 when the element is seen but a meaning-bearing part is explicitly contradicted, the key state is only tentative ('maybe', 'can't tell'), or the target is one of two readings offered without preference.
- Surface attributes (age label, material) and omitted sub-parts already covered by an accepted phrasing were noted but not penalised.

### Discrepancies that did not cost points

- Age label: key 'teenager' described as a girl (pic_04 i01, pic_18 i02, pic_20 i01), a young woman (pic_17 i04) or a man (pic_13 i02).
- Material: pic_16 i03 'wooden box' described as a cardboard box.
- Emotion omitted on otherwise correct actions: pic_03 i03 (balloon girl, upset not mentioned). Of the five targets whose text says 'upset', only pic_19 i01 had the emotion stated; pic_09 i08 and pic_11 i01 omitted it, pic_15 i11 denied it.

## Unintended oddities, grouped by kind

Things the describer flagged as odd, awkward or ambiguous that are not scored items.

### Overlap, occlusion and placement (10)

- pic_05: brown dog overlaps the front of the bench and the woman's legs; front paws hard to place
- pic_09: blue ball sits on the surface of the tree's leaves, looks pasted on
- pic_10: boy's head and upper body stick up above and overlap the slide frame; could be perched on the rail
- pic_12: woman sits right at the edge of the bench seat; seated position slightly ambiguous
- pic_14: kneeling man's reaching arm overlaps the flowers; unclear where his hand ends
- pic_16: man's legs run behind/under the picnic basket; basket may be partly on his legs
- pic_17: baby in the pram mostly hidden; could be a doll or a bundle
- pic_18: kite girl's head is above the fence top, so she looks at first glance as if standing on the fence
- pic_18: ball is high and slightly past the man's hands, might go over his head
- pic_20: two separate hoses (girl's and sprinkler's); unclear whether they are connected

### Figure/animal rendering (8)

- pic_01: duck's shape slightly unusual (body tilted, tail raised)
- pic_02: girl's face not visible: head drawn as solid dark hair with a small circle, may be seen from behind
- pic_02: red object on the brown dog's head could be a collar, a bow or part of the ear
- pic_09: newspaper dog's body is in an awkward crouched, half-kneeling pose
- pic_11: brown dog's head attaches awkwardly to its neck; small white shape between head and scoop
- pic_11: runner's head could be read as facing either way
- pic_15: spotted dog's head drawn as a white round shape on the ice cream; could read as a white scoop on a pink scoop
- pic_15: tan dog at far left small and partly squashed in shape

### Plausibility (odd but not impossible) (4)

- pic_03: jumping child appears fairly high above her shadow, could read as floating
- pic_04: a goat in a back garden (unusual but not impossible)
- pic_17: young man stands far back from the pond, so his food flies a long way
- pic_20: a goat in a back garden (a little odd, not impossible)

### Object shape and drawing style (3)

- pic_03: water from the watering can drawn as a chain of blue segments
- pic_16: picnic basket shaped like a bucket with a single handle
- pic_19: bicycle looks short and squashed with large wheels; rack loop overlaps the wheels

No unintended oddities reported: pic_06, pic_07, pic_08, pic_13.
