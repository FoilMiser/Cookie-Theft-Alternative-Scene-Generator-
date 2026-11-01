# Scoring summary, v018, answer key A (pic_01 to pic_18)

Scored from desc_pic_01.md to desc_pic_18.md against keys_a.json. Scale: 1 = clearly mentioned with the right meaning; 0.5 = partly or only as one of several readings; 0 = not mentioned; misread = mentioned but read as something else (misread counts as 0 in means).

## Completeness check

- keys_a.json has 18 pictures and 239 scored items. scores_a.json has the same 18 pictures and 239 item scores.
- Every key item received exactly one score. No item is missing, none is invented, and every score is one of 1 / 0.5 / 0 / misread (checked by script against keys_a.json).

## Mean score by item type

| Item type | n | Mean | Items below 1 |
|---|---:|---:|---:|
| entity | 118 | 1.000 | 0 |
| action | 80 | 0.988 | 2 |
| inference | 21 | 0.976 | 1 |
| contradiction_notice | 10 | 1.000 | 0 |
| contradiction_explain | 10 | 1.000 | 0 |
| **all** | 239 | 0.994 | 3 |

## Items scored 0, 0.5 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_08 | i04 | action | A child is reaching up toward the tree | 0.5 | boy 'stands with both arms raised over his head'; reaching for the ball offered only as one of four readings (cheering, stretching, waving); 'not directly under the tree' |
| pic_08 | i07 | action | A cat is crouching low on the fence | 0.5 | cat seen, but posture read as 'walking along the top of the fence' toward the bird, not crouching; 'possibly stalking it' only in unsure section |
| pic_08 | i09 | inference | The cat is about to catch the bird | 0.5 | 'a black-and-white cat is walking toward a small blue bird'; intent only hedged: 'appears to be heading toward it, possibly stalking it' |

There were no items scored 0 and no misreads.

## Judgement calls credited as 1 (for audit)

- pic_04 i07 (inference, duck coming for the bread): no explicit 'the duck wants the food'. Credited because the girl is 'feeding the duck' and the duck swims toward the floating crumbs, which the describer reads as food *because* the duck heads for them.
- pic_08 i03 (inference, dog wants the food): credited from 'reaching for the ice cream', which states a goal and not only a posture.
- pic_08 i06 (inference, child's ball stuck): 'stuck in the branches' matches the accepted phrasing, but the describer does not link the ball to the boy (see i04 = 0.5).
- pic_08 i08 (bird pecking on fence): credited via the accepted bare 'little bird'. Pecking was only one of three readings.
- pic_08 i16/i17 (girl throws, man catches): 'the ball is being thrown between them' = playing catch (accepted). Direction hedged, leaning correct.
- pic_04 i09 (package): called a 'wooden crate'. Credited as a box.
- Agent labels differ from the key, but the action is right: pic_01 i02 teenager called 'a woman'; pic_13 i05 man called 'a boy'; pic_08 i01 teenager called 'a man'.

## Unintended oddities reported (not scored items), grouped by kind

### Unclear rendering / object identity (10)
- pic_01: small pink mark at the man's mouth/cheek (could be whistling or humming)
- pic_04: dark dome-shaped dirt mound 'could be mistaken for some other brown object'
- pic_04: duck food on the ground could be read as small pebbles
- pic_05: grey object in the corner could be a rock or a half-buried ball
- pic_06: small white shape at the older woman's chest (chain, tissue or hand)
- pic_06: puppy small enough to be mistaken for a lamb or rabbit
- pic_06: grey object by the sandpit could be a rock or a half-buried ball
- pic_09: not certain the goat's hooves are actually on the hose (if not, the bulge has no visible cause)
- pic_14: can't tell where the leash attaches to the dog
- pic_18: hose water drawn as a dashed line with gaps (could read as a dotted line)

### Unexplained or unusual situation (8)
- pic_03: fruit stall with no stallholder
- pic_04: woman fishing in a small park pond with her float close to the swimming duck
- pic_05: no adult supervising the two children
- pic_07: dog with no leash and no owner nearby
- pic_07: fruit stall with no stallholder
- pic_09: goat in a back garden; unclear whether it belongs there or wandered in
- pic_14: goat in a back garden ('unusual but not impossible')
- pic_18: hose in use while a separate watering can lies unused

### Placement / spatial logic (6)
- pic_03: young man stands beside the trunk, not under the stuck ball
- pic_06: pram heading left toward the sleeping puppy (could be read as about to roll into it)
- pic_08: boy with raised arms is not under the tree and the ball is well out of reach
- pic_08: woman with the parcel faces right while the path runs toward the viewer
- pic_12: the woman fishing stands back on the grass rather than at the water's edge
- pic_15: elderly woman's feet on the path while the pram is on the grass beside it

### Overlap / clipping (5)
- pic_01: man sits at the very edge of the picnic blanket; his legs stick out onto the grass and the picnic basket overlaps his lap/hip
- pic_02: spotted dog's paws/body overlap the woman's legs and the bench (cramped)
- pic_15: a reed sits directly behind the ice-cream eater's head
- pic_16: photographer overlaps the swing-set leg / stands inside the swing frame
- pic_18: hose passes very tightly behind/around the old man's legs

### Physics / pose / support (5)
- pic_02: toddler shown swinging with no one pushing her
- pic_05: seesaw nearly level even though one child's feet are on the ground and the other's are in the air
- pic_08: blue bird on the fence in an awkward pose with one wing raised
- pic_14: goat's head turned at an awkward, twisted angle while eating
- pic_17: picnicking woman leans back with legs out and no visible arm support

### Scale / perspective (3)
- pic_01: boy very small next to the lamp post (describer put it down to perspective, not a size error)
- pic_07: red bird 'quite large for the top of the lamp'
- pic_15: elderly woman at the back drawn almost the same size as the people in front

Pictures with no unintended oddities reported: pic_10, pic_11, pic_13.
