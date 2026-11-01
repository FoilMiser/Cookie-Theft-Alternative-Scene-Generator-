# TPDB v011 set C (pic_39 to pic_61): scoring summary

Scored from desc_pic_39.md to desc_pic_61.md against keys_c.json. 'misread' counts as 0 in the means.

## Mean score by item type

| Type | n | Mean | 1 | 0.5 | 0 | misread |
|---|---|---|---|---|---|---|
| entity | 136 | 1.000 | 136 | 0 | 0 | 0 |
| action | 70 | 0.979 | 68 | 1 | 0 | 1 |
| inference | 12 | 0.833 | 9 | 2 | 1 | 0 |
| contradiction_notice | 9 | 1.000 | 9 | 0 | 0 | 0 |
| contradiction_explain | 9 | 1.000 | 9 | 0 | 0 | 0 |
| contradiction (notice + explain) | 18 | 1.000 | 18 | 0 | 0 | 0 |
| **all items** | 236 | 0.985 | 231 | 3 | 1 | 1 |

## Items scored 0 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_54 | i06 | inference | The woman is going to trip over a box | 0 | box noted near the reading woman, but no trip/fall/bump prediction anywhere |
| pic_54 | i15 | action | A girl is kicking a ball | misread | girl described as standing by a tree with hands near her chest; an orange ball plus a 'wooden bat with a yellow end' at her hip height, maybe airborne; no kicking (the 'bat' may be her raised leg and yellow shoe) |

## Items scored 0.5 (for reference)

| Pic | Item | Type | Target | What the describer said |
|---|---|---|---|---|
| pic_42 | i03 | inference | The grandfather is much heavier, so the girl is stuck up in the air | links his sitting to her being up ('deliberately keeping the girl up in the air or ... not paying attention'), but hedged between two readings; no weight imbalance and no 'stuck/can't get down' |
| pic_54 | i09 | inference | The package is going to get soaked | sprinkler sprays 'onto a cardboard box rather than the grass or flowers', but framed as a mis-aimed sprinkler; no consequence (soaked/ruined/move it), and 'water spurting out of it' offered as an alternative |
| pic_54 | i13 | action | A man is digging | man with spade by a freshly dug hole, but described as leaning on the spade, eyes closed, hand on chest 'as if tired or unwell', not digging |

## Unintended oddities reported (not scored items), by kind

### Malformed or oddly drawn objects and anatomy (8)
- pic_44: bush at the base of the fence looks cut off along the fence line, 'almost upside down'
- pic_45: older man's arms look odd: one crosses his chest to hold the cone while the other hangs on the same side
- pic_47: bicycle looks squashed: oversized wheels almost touching, short frame, extra bar; the rack seems to pass behind or through it
- pic_50: wheelbarrow looks squat, possibly slightly tipped
- pic_51: birds are unusually large (about knee height); could be chickens or pigeons
- pic_55: slide's ladder looks doubled and leans away from the frame
- pic_55: sandcastle is tall and blocky, like stacked boxes or toy blocks
- pic_61: fishing line rises from the rod tip before dropping to the float (odd line shape)

### Overlap / depth artifacts (figure or object drawn across another) (5)
- pic_39: older man overlaps the pond in the drawing (read as walking past it, not in it)
- pic_41: man stands in front of a clothesline post and the spray passes in front of it (read as normal depth)
- pic_43: clothesline post appears to go behind the man's body
- pic_56: man overlaps the edge of the pond (read as standing in front of it)
- pic_57: seesaw plank overlaps the man's legs (could read as passing through them)

### Missing expected props or people (5)
- pic_42: no buckets or spades in the sandbox although a sandcastle is being built
- pic_47: fruit stall has no seller
- pic_48: no adults visible supervising the children
- pic_59: swing set has only one seat; a second seat may be missing
- pic_60: elderly woman is digging but nothing to plant is visible

### Ambiguous pose, motion or state (5)
- pic_44: dog's pose could be sleeping or crawling/stalking/sniffing
- pic_46: swing and chains drawn hanging straight down despite the motion lines
- pic_48: girl's legs hang at an angle that makes it unclear if she sits on the seat or is perched at the very end
- pic_54: man leaning on the spade with eyes closed and hand on chest, 'tired, pain or just resting' (linked to i13)
- pic_57: child on the slide has both arms raised to the head: cheering, or covering the face

### Plausible but unusual situations (4)
- pic_43: hi-vis work vest and cap seem unusual for watering a home garden
- pic_51: goat loose in a public park
- pic_53: woman fishing stands back on the grass rather than at the water's edge
- pic_54: sleeping cat lies right on the path where people walk

### Odd tool choice: an unused proper tool sits nearby (2)
- pic_40: hose reel unused right beside the man who is using a watering can ('not impossible, just noticeable')
- pic_49: a watering can lies unused on the grass and a hose reel is unused by the bed while she waters with a pan

### Water aim or reach slightly off (2)
- pic_41: hose spray lands at the front edge of the flower bed rather than squarely on the flowers
- pic_52: water arc from the small can reaches unusually far ('cartoon-normal, but slightly exaggerated')

### Unsupported / floating objects (not scored) (1)
- pic_54: bat and orange ball hovering at the girl's hip height with no shadows, not connected to anyone (likely produced by the i15 misreading)
