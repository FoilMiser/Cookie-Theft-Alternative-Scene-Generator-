# v06 picture-description scoring summary

Scored 25 blind descriptions (free description + inventory + unsure section) against `keys.json`; 353 items. Scores: 1 / 0.5 / 0 / misread. **Misread counts as 0 in the means.**

## Mean score by item type

| Type | n | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 131 | 1.000 | 131 | 0 | 0 | 0 |
| action | 147 | 0.956 | 137 | 7 | 0 | 3 |
| inference | 37 | 0.851 | 29 | 5 | 3 | 0 |
| contradiction_notice | 19 | 0.974 | 18 | 1 | 0 | 0 |
| contradiction_explain | 19 | 0.895 | 17 | 0 | 0 | 2 |
| contradiction (both) | 38 | 0.934 | 35 | 1 | 0 | 2 |
| **all** | 353 | 0.959 | 332 | 13 | 3 | 5 |

## Items scored 0 or misread (8)

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_07 | i14 | action | A man is sweeping | misread | man 'stands holding a garden fork' with prongs on the paving, 'might be leaning on it rather than using it'; no sweeping |
| pic_07 | i16 | contradiction_explain | The person is sweeping with a giant fork instead of a broom | misread | fork read as a garden fork/pitchfork that is odd on paving, not as a fork used in place of a broom |
| pic_10 | i02 | action | A bird is pecking at a sandwich on the bench | misread | no bird at the sandwich; sandwich seen with a red object beside it on the bench, read as 'a tipped-over cup or flask' (probably the bird) |
| pic_10 | i03 | inference | The bird is stealing the sandwich while the grandfather is busy reading | 0 | no bird and no theft; the sandwich is just 'beside him on the bench' |
| pic_14 | i03 | inference | The man is much heavier, so the girl is stuck up in the air | 0 | positions described but no weight explanation and no 'stuck' reading |
| pic_21 | i03 | inference | The man is much heavier, so the girl is stuck up in the air | 0 | positions described but no weight explanation and no 'stuck' reading |
| pic_22 | i16 | action | A grandfather is sweeping | misread | older man 'holding a garden fork' with prongs on the paving, 'might be about to dig, resting on it'; no sweeping |
| pic_22 | i18 | contradiction_explain | The person is sweeping with a giant fork instead of a broom | misread | read as an ordinary garden fork held on the path, not a fork used in place of a broom |

## Partial credit (0.5) items, for reference (13)

| Pic | Item | Type | Target | What the describer said |
|---|---|---|---|---|
| pic_04 | i10 | action | A girl is jumping for joy | read as KNEELING with both arms up, smiling; 'cheering' is only one of three readings (also playing in sprinkler, stretching) |
| pic_07 | i06 | inference | The cat is about to catch the bird | 'creeping up behind' the bird but no pounce/catch stated; unsure section: 'stalking the red bird or just walking' |
| pic_08 | i02 | action | A child is reaching up toward the tree | boy with both arms up, 'maybe reaching for the ball'; also read as cheering/waving; stands right of the tree, not under the ball |
| pic_09 | i07 | action | A grandfather is feeding the birds | crumbs fall from the old man's hand to pecking birds, but deliberate feeding is offered alongside 'leaking out of his bag without him noticing'; he faces the fruit, not the birds |
| pic_11 | i04 | inference | The kite got stuck in the tree | 'looks like it might be caught in the branches', but also 'still flying just in front of the tree'; free description has the child flying it |
| pic_14 | i04 | action | A cat is crouching low | cat seen going for the bird but in a 'running pose', not crouching |
| pic_15 | i07 | action | A girl is holding an empty cone, looking upset | girl holding a cone, but 'I can't tell whether it is empty'; no upset noted |
| pic_15 | i10 | inference | The girl dropped the ice cream | 'so the scoop may be hers', hedged (cone may still have ice cream) |
| pic_22 | i07 | action | A child is reaching up, upset | child with arms raised looking 'surprised'; reaching for the balloon is one of three readings (goat, cheering); no upset |
| pic_22 | i09 | inference | The child let go of the balloon | balloon only 'perhaps' the child's; offered alongside reacting to the goat or cheering |
| pic_22 | i12 | inference | The teenager is going to trip over a box | 'She is not looking where she is going', but the box is described as being walked past; no trip predicted |
| pic_22 | i17 | contradiction_notice | Something is wrong with what the person is sweeping with | only notes the fork is 'on hard paving rather than soil' in the unsure list; not called wrong |
| pic_25 | i08 | action | A grandfather is feeding the birds | seeds fall from the man's bag to a pecking bird, but 'deliberately scattering' is offered alongside 'bag could be leaking'; his back is to the bird |

## Unintended oddities (not scored items), grouped by kind

### Unsupported or physically odd objects (5)

- pic_01: empty seesaw rests perfectly level (flagged as physically unlikely, possibly 'something wrong')
- pic_07: bicycle stands upright by itself with no visible stand or rider
- pic_12: red bicycle stands upright on its own with no kickstand visible
- pic_13: red bicycle stands upright on its own with no visible kickstand
- pic_18: bicycle stands upright with nothing obvious holding it up

### Drawing and anatomy glitches (22)

- pic_01: slide ladder leans far out to the left of the frame (awkward, probably drawing style)
- pic_02: two potted plants by the fence have no shadows (unclear what they stand on)
- pic_06: blue bird perched on the edge of the leaves with no branch drawn
- pic_08: sleeping cat is partly hidden by the seesaw base; could read as injured
- pic_14: man's legs cross over the seesaw board awkwardly (straddling or legs off to one side?)
- pic_14: green blob sticks out of the tree crown like an attached bush
- pic_14: only one swing seat on a frame wide enough for two
- pic_15: green blob sticks out from the big tree like an attached bush
- pic_16: green blob sticks out from the left tree's crown
- pic_16: small round mark on the older man's head (ear or hearing aid?)
- pic_17: green blob sticks out from the left tree's crown
- pic_18: green blob floating beside the tree, with no bush it could belong to ('looks odd')
- pic_19: two short white lines on the pond look like stray marks
- pic_19: picnic basket overlaps the worker's legs (on the blanket or on his legs?)
- pic_21: man's legs stretched along/over the seesaw plank awkwardly
- pic_21: swing set has only one swing
- pic_22: goat drawn oddly: only two legs clearly shown, front leg bent at a strange angle, blank white eye
- pic_22: birdhouse has no entrance hole
- pic_23: sandwich far too large and its position unclear (on lap, on bench or floating)
- pic_25: older man's face not drawn (no eyes or mouth)
- pic_25: tan dog's pose anatomically strange (half upright, back legs bent like kneeling)
- pic_25: dark mark/smear at the ice-cream woman's mouth

### Gaze, aim and placement mismatches (15)

- pic_03: thrown ball is above the catcher's hands and head; may sail over him
- pic_07: jumping young man's feet are back by the shop fronts, so it is unclear whether he is in the air
- pic_07: unclear what the photographer is photographing
- pic_08: boy reaching up stands to the right of the tree, not under the stuck ball
- pic_09: bird-feeding old man faces the fruit stall, not the birds (crumbs could be a leaking bag)
- pic_10: watering-can stream lands at the front edge of the flower box and may miss the flowers
- pic_11: thrown ball's dotted path may carry it over the catcher's head
- pic_12: watering-can stream lands near the front edge of the box, partly spilling
- pic_14: unclear what the photographer is photographing
- pic_19: kite string passes very close to the bread-thrower's hand
- pic_20: raker looks off to the right, not at the leaves
- pic_22: sprinkler set on the paved path, watering the path
- pic_23: kicked ball looks about to hit the man with the hose
- pic_24: photographer has her back to the child and balloon; subject unclear
- pic_25: bird-feeding man faces the stall with his back to the bird (could be a leaking bag)

### Stray or unexplained props (16)

- pic_01: small yellow ball lying alone on the grass, unused
- pic_02: red disc on the grass (frisbee or pet bowl), unused
- pic_03: red disc on the grass (frisbee or dog bowl), unused
- pic_06: empty picnic blanket with no owner
- pic_15: two identical blue balls (one being kicked, one in the tree)
- pic_17: empty picnic blanket with no owner
- pic_18: box on the ground looks identical to the one being carried (dropped? unrelated?)
- pic_18: cafe table with a cup but nobody there
- pic_20: red dish on the grass (empty pet bowl or frisbee)
- pic_21: yellow ball lying alone, unused
- pic_22: goat in a suburban back garden is unexpected
- pic_22: two separate cardboard boxes with no reason to be there
- pic_23: watering can sits unused while the man waters with a hose
- pic_24: cafe table with a cup but nobody there
- pic_24: fruit stall has no seller
- pic_25: red bicycle standing alone in the middle of the walkway (trip hazard)

### Unexplained actions or scene logic (9)

- pic_01: runner has no visible goal ('not clear what she is running for')
- pic_05: woman digging a hole with nothing shown waiting to be planted
- pic_10: watering flowers under heavy storm clouds seems odd/unnecessary
- pic_17: boy's excitement has no visible cause
- pic_18: runner has no visible reason to run
- pic_19: worker laughing at nothing identifiable
- pic_20: raking leaves on a summery day with no tree overhead
- pic_21: child standing on top of the slide with no hands on the rail looks risky
- pic_24: runner's reason unclear (runs away from the balloon)

### Framing and visibility (3)

- pic_04: bird and wheelbarrow partly cut off at the bottom edge
- pic_06: rubbish bin cut off at the bottom-left corner
- pic_16: yellow kite string very long and thin, easy to lose against the sky
