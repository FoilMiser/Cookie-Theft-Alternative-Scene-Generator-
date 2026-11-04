# Picture description scores, key A

Completeness check: all 26 pictures and all 296 items in keys_a.json have exactly one score. No item is missing and none is invented (checked by script against keys_a.json).

## Mean score by item type

A misread would count as 0 in the mean; there were none.

| Type | Items | Mean | 1 | 0.5 | 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 161 | 0.994 | 160 | 0 | 1 | 0 |
| action | 88 | 1.000 | 88 | 0 | 0 | 0 |
| inference | 21 | 1.000 | 21 | 0 | 0 | 0 |
| contradiction_notice | 13 | 1.000 | 13 | 0 | 0 | 0 |
| contradiction_explain | 13 | 0.962 | 12 | 1 | 0 | 0 |
| **all** | 296 | 0.995 | 294 | 1 | 1 | 0 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_02 | i11 | entity | There are a few white clouds | 0 | clouds not mentioned anywhere in the description |
| pic_26 | i15 | contradiction_explain | The dog is reading a newspaper, but dogs can't read | 0.5 | calls it impossible, 'something a dog cannot do', but reading is only one of two readings: 'genuinely reading, or just holding or playing with the newspaper' |

## Scored 1, with a qualification worth knowing

These met the scoring rule, but the describer qualified them.

- pic_04 i02, i03: the upward water is described and called odd, but explained away: "it fits the wind". This picture also has the blown-hat event.
- pic_10 i02, i03: water flowing upward is named as possibly impossible, with wind as the other reading. This picture also has the blown-hat event.
- pic_10 i07: the wind blowing the hat is stated, but the describer doubts the hat is the older woman's.
- pic_26 i02, i03: the bird is read as about to take the sandwich, not yet pecking at it.
- pic_26 i18: the jumping is seen, but the describer cannot choose between jumping for joy and reaching for the ball in the tree.
- pic_02 i03, pic_18 i14, pic_24 i04: stated in the free description, then hedged in the unsure section.

## Unintended oddities by kind (64 in total)

### Objects overlapping, touching or placed unclearly (14)

- pic_02: watering can and water stream overlap the flowers in a tangled way
- pic_04: older woman overlaps the flowers with the can hard to see, and seems to stand against or in the flower bed
- pic_06: pot of pink flowers overlaps the soil mound, unclear whether it is in the bed or next to it
- pic_07: birdhouse post could be read as passing through the fence rails
- pic_07: bench overlaps the edge of the house and may be touching the wall
- pic_08: man on the path overlaps the gate, which seems to pass behind his head
- pic_09: hose reel sits so close that it overlaps the edge of the flower bed
- pic_13: walking boy's rear foot looks as if it is at or on the edge of the sandpit
- pic_16: birdhouse post sits a little oddly between the path and the fence
- pic_20: hard to tell whether he is in front of the washing line or under it
- pic_21: girl seems to sit half on the sandpit's wooden rim, legs at or behind the back edge, rather than inside it
- pic_21: sandcastle overlaps the rim as if it stands on the frame rather than on the sand
- pic_22: man's feet are on the grass but his body overlaps the pond's outline
- pic_23: balloon almost touches the lamp post

### Held object not clearly held, or hands merging with the object (12)

- pic_01: newspaper nearly as big as the white dog and seems to stand on its own in front of it rather than being held
- pic_01: older woman's broom and arm overlap oddly with her skirt
- pic_02: older woman's book overlaps her arm and seems to float a little ahead of her hands
- pic_03: woman's hands and the fork handle overlap in a confusing white shape near her chest
- pic_05: man's arms look bunched together at his waist, so it is hard to tell how he holds the lead
- pic_08: man's arms and the fork overlap confusingly near his chest, with a white shape at his hand
- pic_11: walker's hand sits below the book, so the book looks as if it floats just above her hand
- pic_12: workman's hand is at the side of the box rather than gripping it, so the box looks stuck to him
- pic_12: balloon strings simply meet at the boy's fingertips, looking too tidy
- pic_14: man's hands have an odd bunched look where they meet on the lead, and his shoulder and arm look stiff
- pic_18: kneeling man's hands are hidden behind the flowers or pot, with the pot in front and his arm behind
- pic_26: older woman's hands and the can run together, and her position relative to the flower box is unclear

### Body part or pose stiff, odd or hard to read (9)

- pic_05: man's facing direction is hard to read (looking back to the right or ahead to the left)
- pic_12: workman's other arm is a grey-ish shape against the vest, hard to read
- pic_14: boy's shoes look large and rounded relative to his legs
- pic_15: pointing man's lower arm hangs stiffly and his trousers bulge at the hips
- pic_17: man's upper body seems narrow and his arm holding the can looks short
- pic_20: man's feet look odd: shoes tilted and stacked close together, as if on tiptoe or balancing
- pic_21: girl's lower body is partly hidden behind the castle, so her pose is hard to read
- pic_25: man's raised arm joins the sleeve at a narrow pinched point and looks a little disconnected
- pic_25: dark patch on his lower face could be a beard or a shadowed open mouth

### Story logic missing or unexplained (7)

- pic_10: flying red cap looks like a boy's baseball cap, not something the older woman or the painter would wear, so its owner is uncertain
- pic_10: older woman is some way below and to the right of the hat, not actually close to catching it
- pic_11: unclear why the box is sitting on the grass or whose it is
- pic_13: not obvious why the box is sitting where it is
- pic_15: looks odd that people are watering flowers and painting a fence outdoors just as it is about to rain
- pic_17: fish's branch is the only visible branch on the tree and curves out specially to hold it
- pic_26: newspaper's printed side faces the viewer, so it is unclear the dog could read it from where it sits

### String, motion or trail behaving oddly (6)

- pic_09: kite string seems unusually long and thin for the small girl
- pic_18: pawprint trail does not quite reach the paint tray; it starts just to the right of it
- pic_23: if the child is running the balloon should trail behind, but it stands upright in front on a nearly straight string
- pic_23: child's direction of travel is not clear (left toward the lamp post or right toward the pond)
- pic_24: kite string runs in a big sagging loop across the fence and past the post, strange for a line under tension
- pic_24: swing has motion lines yet the seat hangs nearly straight below the bar

### Animal hard to identify or read (5)

- pic_01: goat's horn or ear is hard to make out; at a glance the goat looks like a dog-shaped animal
- pic_06: goat's plain body could be read as a white dog or a lamb at a glance
- pic_17: cat's curled pose is hard to read; it could conceivably be hurt
- pic_18: goat's white body is hard to read and its back legs look stiff; it could be a lamb or a dog
- pic_19: cat is small with its body and head bunched together, and took a moment to read

### Object hard to identify (4)

- pic_03: red dustpan is so flat and thin-handled it could be a small trowel or scoop
- pic_04: flying cap could be a strange orange bird or leaf at a glance
- pic_06: thin tool in the woman's hand cannot be made out (trowel, dibber or stick)
- pic_09: paint roller looks like a brush or mallet on a stick, its top sticking up above the fence against the sky

### Size or proportion (3)

- pic_11: the two figures look very different in size (distance, or a young child)
- pic_13: sandpit looks oversized compared with the boy
- pic_26: red bird looks large relative to the buildings and people

### Storm sky not matched by the rest of the picture (2)

- pic_15: sky is grey but the grass and colours stay sunlit and the house window stays bright blue, so it does not look fully stormy
- pic_25: house windows stay bright blue, which does not match the grey weather

### Cat balanced on the fence points (2)

- pic_07: cat's feet on the fence tips look balanced in an unlikely way
- pic_14: cat stands right on the pointed fence tops, which would be uncomfortable in real life
