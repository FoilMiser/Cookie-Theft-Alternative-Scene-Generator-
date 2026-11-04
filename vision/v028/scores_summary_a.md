# Picture description scores, key set A

Scored from desc_pic_01.md to desc_pic_23.md against keys_a.json. Full item scores are in scores_a.json.

## Mean score by item type

| Item type | Items | Mean | Scored 1 | Scored 0.5 | Scored 0 | Misread |
|---|---|---|---|---|---|---|
| entity | 146 | 1.000 | 146 | 0 | 0 | 0 |
| action | 82 | 0.994 | 81 | 1 | 0 | 0 |
| inference | 21 | 0.905 | 17 | 4 | 0 | 0 |
| contradiction_notice | 16 | 1.000 | 16 | 0 | 0 | 0 |
| contradiction_explain | 16 | 1.000 | 16 | 0 | 0 | 0 |
| **All items** | **281** | **0.991** | **276** | **5** | **0** | **0** |

A misread would count as 0 in the means. None occurred.

## Items scored 0, 0.5 or misread

5 of 281 items. No item scored 0 and none was a misread.

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_02 | i09 | inference | The woman is going to trip over a bucket | 0.5 | 'she may be about to walk into it', but also 'might pass beside it'; no commitment |
| pic_04 | i06 | action | A dog is sleeping | 0.5 | 'small white animal' curled up asleep; 'could be a puppy or a kitten', leans puppy |
| pic_13 | i09 | inference | The grandfather is going to trip over a bucket | 0.5 | 'might bump into or trip over it, though it isn't directly in front of his feet'; 'may or may not be a danger' |
| pic_16 | i13 | inference | The woman is going to trip over a box | 0.5 | 'not looking where she is going'; box 'could be an obstacle she is about to trip on ... I could read it either way' |
| pic_18 | i03 | inference | The duck is coming to eat the bread | 0.5 | 'swimming towards those crumbs' and 'could be feeding the duck'; direction given, wanting or eating the bread not stated |

## Unintended oddities by kind

39 oddities across 20 of 23 pictures. pic_01, pic_06 and pic_23 have none.

### Figure pose and anatomy (16)

- pic_04: dog's front-on pose is tall, narrow and stiff; its long body could be mistaken for a person or a post, and the lead makes its chest hard to read
- pic_08: man's seat on the seesaw looks awkward: one leg crosses in front of the plank, hips sit above it, plank runs behind his lower legs
- pic_09: small dark mark or shading around her mouth and cheek that cannot be made out
- pic_10: boy's hands look tangled around the fork handle
- pic_10: cat's legs are long and thin, so it could look like another animal at first glance
- pic_12: goat's head and legs are bent so tightly the shape is hard to read; head seems tucked between the front legs
- pic_12: only one goat horn is clearly visible, at the back of the head at an odd angle; could be a white dog or lamb
- pic_13: cat stands on jagged fence tops that look too narrow to balance on, and its legs meet them awkwardly
- pic_15: boy's facial expression and large head make him look a little odd
- pic_16: older man's bag and legs overlap so his lower half is hard to read, and he seems to stand on the raised kerb line
- pic_17: old woman's skirt has an odd rounded barrel shape, and an unexplained white stripe runs down the front of her top
- pic_18: walking woman looks stiff, her bag hides her front leg, and she walks on the grass beside the path
- pic_19: hands and pegs overlap at the T-shirt's shoulder, so the action is hard to see and could be taking the washing in
- pic_19: feet look stacked on top of each other and legs are very narrow, though not seriously wrong
- pic_21: girl's face is tilted and rather squashed, so it is hard to read
- pic_21: very thin arms and small body could read as falling rather than jumping at first glance

### Objects merging or overlapping (6)

- pic_02: teal hose reel overlaps the flower bed edge and could read as a fan or coiled hose, with almost no hose visible
- pic_05: bench's dark back posts blend into the railing, so the bench back is hard to separate from the fence
- pic_07: man's body overlaps the pond edge, so for a moment he could seem to be standing in the water
- pic_10: swing's ropes and frame overlap the fence lines, so the upper part of the swing is hard to separate from the fence
- pic_14: paint roller's top reaches above the fence line and its head sits offset from the blue area
- pic_15: girl appears partly outside the sandpit, at or beyond its back-left corner, and the castle base overlaps the wooden frame

### Parts that look detached, floating or pasted on (9)

- pic_02: tree canopy looks as if the leaves were cut away to display the ball, trunk and branch showing through
- pic_03: water arc starts near the flowers, not clearly at the can's spout, and could read as a pale hoop or bent pipe rising from the flower bed
- pic_04: goldfish looks pasted onto the leaves, not attached to any branch
- pic_09: hose rises straight up beside her before reaching her hand; the upright section could read as a post or a separate piece
- pic_13: light-green leaf clumps look as if they float on top of the main tree shape
- pic_15: slide ladder is at a different angle to the frame and looks slightly detached from the platform
- pic_18: white wake lines are detached from the duck's tail and could read as scratches on the water
- pic_18: one crumb lies at or just past the pond's edge, possibly in mid-air
- pic_22: ball looks stuck to his foot, at shin height

### Props or marks of unclear identity (2)

- pic_07: pram looks low, small and toy-like: flat box shape with only two visible wheels
- pic_08: curved lines under the girl's feet are unclear: swinging feet, seesaw motion, or scribbles of grass or shadow

### Readings that weaken a planted contradiction (4)

- pic_11: ladder could be meant to lean on the lamp post but drawn too far away from it
- pic_14: the two boxes look so alike that it is unclear whether they are connected, for example one dropped next to the other
- pic_16: white dog's newspaper stands up by itself, not tilted to its eyes, and the dog looks away; it could be merely sitting beside the paper
- pic_20: bucket could be a makeshift rain hat because of the clouds, and it looks too big, down to her glasses

### Scene logic (2)

- pic_12: a goat loose in a park is a little unusual
- pic_20: house window stays a bright pale blue though the sky is grey

## Scoring conventions

- If the describer commits to a reading in the free description and only lists an alternative in the unsure section, the item scores 1. If they leave it undecided ("I could read it either way", "may or may not"), it scores 0.5.

- pic_18 i03 is the closest call. "Swimming towards those crumbs" links the duck to the food but does not state that it wants the bread, so the inference rule gave 0.5.

- The age of a character was not scored. The man in the red T-shirt is called a boy, or "man or boy", wherever he appears (pic_02, 03, 10, 11, 12, 19). These items scored 1 because the action was right.

## Coverage check

scores_a.json was read back and compared with keys_a.json: 23 pictures and 281 items in the key, 281 items scored. No item is missing, none is invented, and each has exactly one score.
