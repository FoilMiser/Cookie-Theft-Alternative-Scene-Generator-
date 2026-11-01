# v0.7 screen: scorer summaries

Two scorers with the same prompt scored the 41 pictures in two halves (pic_01 to pic_21, pic_22 to pic_41);
`scores.json` merges `scores_a.json` and `scores_b.json`.

## Pictures 1 to 21


Scored 255 items across pic_01-pic_21 against `keys_a.json`, using each `desc_pic_NN.md` in full (free description, inventory, unsure section). For the means, "misread" counts as 0. Where the free description commits to a reading and only the unsure section lists alternatives, the item gets 1. Where the free description itself hedges between readings, it gets 0.5.

## Mean score by item type

| Type | n | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 123 | 1.000 | 123 | 0 | 0 | 0 |
| action | 85 | 0.929 | 75 | 8 | 0 | 2 |
| inference | 25 | 0.900 | 21 | 3 | 1 | 0 |
| contradiction_notice | 11 | 0.818 | 9 | 0 | 2 | 0 |
| contradiction_explain | 11 | 0.818 | 9 | 0 | 0 | 2 |
| **all** | 255 | 0.951 | 237 | 11 | 3 | 4 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_05 | i04 | action | A cat is crouching low | 0.5 | cat described as running toward the pigeon, not crouching (but 'about to pounce') |
| pic_05 | i09 | inference | It is about to rain | 0.5 | storm clouds / 'gloomy, stormy sky' noted, but no statement that rain is coming |
| pic_08 | i09 | action | A grandmother is sweeping | 0.5 | old woman 'rakes a small pile of leaves' - ground-clearing seen, but raking not sweeping |
| pic_08 | i10 | contradiction_notice | Something is wrong with what the person is sweeping with | 0 | tool taken as an ordinary rake; nothing flagged as wrong with it |
| pic_08 | i11 | contradiction_explain | The person is sweeping with a giant fork instead of a broom | misread | giant fork read as a long-handled rake |
| pic_09 | i02 | action | A cat is crouching low | misread | black cat 'runs away under the dog' - running from the dog, not crouching |
| pic_09 | i04 | inference | The cat is about to catch the bird | 0 | no cat-bird link; cat interpreted as fleeing the dog |
| pic_10 | i01 | action | A girl is building a sandcastle in the sandbox | 0.5 | girl sits in sandbox next to a sandcastle but 'seems to be resting' - not building |
| pic_12 | i01 | action | A child is building a sandcastle in the sandbox | 0.5 | boy sits smiling in sandbox beside a sandcastle - building not stated |
| pic_13 | i09 | action | A worker is pointing up at the sky | 0.5 | worker pointing up, but said to point at the ball in the tree (clouds only an alternative in unsure) |
| pic_13 | i15 | action | A man is waving | 0.5 | man with one arm raised; waving only one of three readings (leaning, waving, scratching head) |
| pic_15 | i12 | inference | The girl let go of the balloon | 0.5 | 'maybe because her balloon got away'; unsure offers 'just excited' as alternative |
| pic_15 | i13 | action | A grandmother is sweeping | 0.5 | elderly woman 'raking leaves' with a fan rake - not sweeping |
| pic_15 | i14 | contradiction_notice | Something is wrong with what the person is sweeping with | 0 | tool taken as a normal fan rake (or litter picker); nothing flagged as wrong |
| pic_15 | i15 | contradiction_explain | The person is sweeping with a giant fork instead of a broom | misread | giant fork read as a fan rake / litter picker |
| pic_15 | i16 | action | A man is waving | 0.5 | bearded man's raised hand 'trying to grab the cap or waving at it' - two readings |
| pic_16 | i01 | action | A dog is sitting by the door with its leash in its mouth | misread | animal read as a white cat on the doorstep with a red leash from its mouth |
| pic_16 | i02 | inference | The dog wants to go for a walk | 0.5 | 'as if asking to go for a walk' offered as reading 1 of 2, and for a cat |

## Unintended oddities reported (not scored items)

### Overlap / depth / placement ambiguity (13)

- pic_01: hose reel drawn overlapping the flowerbed edge - unclear if on soil or grass
- pic_03: door handle beside the brown dog's ear could be mistaken for an ear/collar tag
- pic_04: man's legs overlap the flowerbed edge - may be standing on the soil
- pic_06: man's body overlaps the striped garment on the line - looks crowded
- pic_07: birdhouse post rises from behind the fence - may be in the neighbour's garden
- pic_11: jogger's head overlaps the shop awning behind him
- pic_13: man in red's raised hand seems to disappear at the corner of the house
- pic_14: boy stands between the clothesline posts right against the fence
- pic_15: red cap overlaps the top of the lamppost - in front of it or caught on it
- pic_16: woman looks perched on the front edge of the bench
- pic_17: fisherman's feet very close to the water line
- pic_18: white dog's head drawn on top of the ice cream scoop, mouth hard to locate
- pic_20: hose seems to pass through the bearded man's legs

### Staging gap in a keyed vignette (8)

- pic_03: ball's dotted path rises toward the fence top, may sail over the catcher
- pic_13: no paint tin near the woman painting the fence
- pic_13: balloon is far from the reaching boy
- pic_15: wind drawn only around the pink building; nothing else looks wind-blown
- pic_15: balloon is far from the little girl
- pic_17: child is quite far from the balloon
- pic_20: paint tray several steps behind the painter
- pic_20: dog's paws do not look blue although it left blue prints

### Unusual but possible scene content (8)

- pic_04: two watering cans, one in use and one on the grass
- pic_05: people eating ice cream and jumping for joy under dark storm clouds
- pic_11: fruit stall with no stallholder
- pic_11: brown dog with a collar but no leash or owner
- pic_14: two matching teal watering cans, one in use and one on the grass
- pic_15: nobody minding the fruit stall
- pic_18: man digging right beside the lamppost base - might undermine the post
- pic_19: fruit stall unattended

### Physically implausible (not keyed) (4)

- pic_07: frying pan too shallow to hold the long steady stream of water
- pic_08: seesaw tilted wrong for weights: bigger girl up, smaller girl down
- pic_10: empty seesaw resting perfectly level instead of one end down
- pic_16: pan could not pour a long continuous hose-like stream

### Shape or shadow rendering quirk (4)

- pic_11: brown dog's head drawn unusually round - could read as an upside-down cone on the scoop
- pic_19: bicycle very short; unclear if it is in front of or behind the rack
- pic_19: red bird's wing shape unusual (one large raised wing)
- pic_21: running man's shadow large and offset, making him look airborne

### Artifact of a misreading (1)

- pic_16: cat holding a leash in its mouth, 'unusual for a cat' (dog misread as cat)


## Pictures 22 to 41


237 key items across 20 pictures. Scoring: 1 = clearly conveyed; 0.5 = partly, or given as one of two readings without preferring the right one; 0 = not mentioned; misread = mentioned but read as something else. Misread counts as 0 in the means. Where a describer stated the target as the preferred reading and only listed an alternative in the unsure section, it got 1.

## Mean score by item type

| Type | n | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 121 | 1.000 | 121 | 0 | 0 | 0 |
| action | 78 | 0.955 | 72 | 5 | 0 | 1 |
| inference | 16 | 0.812 | 11 | 4 | 1 | 0 |
| contradiction_notice | 11 | 1.000 | 11 | 0 | 0 | 0 |
| contradiction_explain | 11 | 1.000 | 11 | 0 | 0 | 0 |
| **all** | 237 | 0.973 | 226 | 9 | 1 | 1 |

## Mean score by picture

| Picture | n | Mean |
|---|---:|---:|
| pic_22 | 4 | 1.000 |
| pic_23 | 11 | 1.000 |
| pic_24 | 10 | 1.000 |
| pic_25 | 25 | 0.860 |
| pic_26 | 11 | 1.000 |
| pic_27 | 11 | 1.000 |
| pic_28 | 11 | 1.000 |
| pic_29 | 9 | 1.000 |
| pic_30 | 15 | 1.000 |
| pic_31 | 15 | 0.967 |
| pic_32 | 9 | 1.000 |
| pic_33 | 15 | 0.967 |
| pic_34 | 5 | 1.000 |
| pic_35 | 13 | 1.000 |
| pic_36 | 15 | 1.000 |
| pic_37 | 4 | 0.875 |
| pic_38 | 8 | 1.000 |
| pic_39 | 8 | 1.000 |
| pic_40 | 13 | 1.000 |
| pic_41 | 25 | 0.940 |

## Items scored 0, 0.5 or misread

| Picture | Item | Type | Score | Target | What the describer said |
|---|---|---|---|---|---|
| pic_25 | i02 | action | misread | A bird is pecking at a sandwich on the bench | no bird reported: the sandwich was seen, but the bird beside it was read as 'a blue cap-shaped object' (a cap on the bench, a falling cap, or part of the girl's arm) |
| pic_25 | i03 | inference | 0 | The bird is stealing the sandwich while the woman is busy reading | no theft inference; the bird was not recognised |
| pic_25 | i09 | inference | 0.5 | The duck is coming to eat the bread | duck 'swims among small pieces of bread' and child is 'apparently feeding the duck', but never says the duck is coming for the bread |
| pic_25 | i10 | action | 0.5 | A dog is sitting up holding a newspaper | 'brown animal ... looks like a monkey or a dog wearing a red bandana' sitting holding an open book/newspaper; dog given only as one of two readings |
| pic_25 | i19 | action | 0.5 | A goat is eating grass | goat 'head down toward the grass, as if grazing or about to butt'; grazing given only as one of two readings (the literal key would accept bare 'goat') |
| pic_31 | i09 | action | 0.5 | A woman is pointing up at the sky | pointing up seen, but read as 'pointing up at the cat' on the fence; storm clouds offered only as the second reading |
| pic_33 | i03 | inference | 0.5 | The dog wants some of the food | dog's gaze is tied to the ice cream ('looking up at the man's ice cream') but no begging/wanting is stated |
| pic_37 | i02 | action | 0.5 | A goat is eating grass | goat head down 'eating grass or sniffing the ground'; eating given only as one of two readings (the literal key would accept bare 'goat') |
| pic_41 | i03 | inference | 0.5 | The man is much heavier, so the girl is stuck up in the air | man on the low end is 'pushing it down': the girl's position is put down to him pushing, not to his weight |
| pic_41 | i07 | action | 0.5 | A child is reaching up, upset | child with both arms raised 'as if reaching for the balloon or cheering'; upset not mentioned |
| pic_41 | i09 | inference | 0.5 | The child let go of the balloon | 'could be reaching for a balloon they just let go of, or simply cheering'; 'The balloon's owner is not shown' |

## Unintended oddities, grouped by kind

Oddities the describer reported that are not scored items. Interpretive hedges about scored items are in the item notes instead.

### Unintended physical or logical inconsistency (4)

- pic_22: fallen leaves being raked although the only tree is green, full and far from the pile
- pic_24: dog's paws are white even though it is leaving blue paw prints
- pic_31: watering the garden, running a sprinkler and leaving washing out while a storm is coming
- pic_40: fence section is painted blue top to bottom but the brush only touches the top

### Incongruous or out-of-place element (6)

- pic_25: goat loose in a public park, flagged as wrong
- pic_30: road worker in hi-vis outfit pushing a pram
- pic_35: goat in an ordinary back garden
- pic_36: man wearing a work hi-vis vest while having a picnic
- pic_37: goat loose in a public park
- pic_41: man sweeping grass with a broom

### Anatomy, pose or clipping glitch (5)

- pic_22: child perched far forward on the edge of the bench, slightly awkward
- pic_25: dog's tail very long and pointing straight up, looks unnatural
- pic_31: dog's body looks twisted, one front leg raised
- pic_37: woman's kneeling pose stiff; back leg stretched long and straight behind her
- pic_41: seesaw man's lower legs cross the plank with feet below it (legs pass through the plank)

### Perspective, scale or depth (5)

- pic_25: background walking woman drawn as large as foreground figures
- pic_30: bicycle wheels large for the frame; bike sits oddly in front of and across the rack
- pic_33: kite drawn right against the cloud
- pic_35: girl drawn very small and overlapping the house wall edge; looks both in front of and behind the house
- pic_35: kite drawn right against the cloud

### Placement or overlap ambiguity (10)

- pic_23: picnic basket overlaps the man's legs/feet; unclear whether it is on the blanket or the grass
- pic_27: birdhouse pole stands directly behind the fence; unclear which garden it is in
- pic_28: bucket and spade lie on the grass outside the sandbox, as if left behind
- pic_32: girl's legs stretch past the end of the chute; may have slid off onto the grass with a bump
- pic_32: bucket and spade lie on the grass outside the sandbox
- pic_36: picnic basket drawn over the man's lower legs; unclear whether on his shins or the blanket
- pic_38: bucket and spade lie outside the sandbox, as if left behind
- pic_38: rubbish bin sits on the fence line; in front of or overlapping the fence
- pic_41: bicycle overlaps the corner of the sandbox; leaning on it or behind it is unclear
- pic_41: ice-cream woman stands on the fence line by the slide ladder; inside or behind the fence is unclear

### Missing part or drawing-continuity glitch (4)

- pic_28: only one swing seat on a frame wide enough for two
- pic_29: top of the path stops at a small bush sticking out of the tree canopy instead of continuing
- pic_39: wheelbarrow has no visible back legs and looks tilted
- pic_39: man's hand not clearly connected to the hose

### Hard-to-read rendering (11)

- pic_25: item on the bench looks like a giant sandwich but could be a stack of books or folded cloth
- pic_29: girl's arm holding the balloon string is unclear; one arm seems to cross her body
- pic_30: red bird so small it is barely recognisable as a bird
- pic_31: sprinkler spray drawn as dashed lines; unclear whether it reaches the box
- pic_32: dog's head drawn as a round shape tucked against the ice cream, hard to read at first
- pic_33: ball's dotted trail starts near the girl's head; could read as the ball coming off her head
- pic_33: girl's head drawn mostly as a dark circle of hair; facing direction unclear
- pic_34: photographer's head mostly dark (hair/cap/beard); face can't be made out
- pic_35: woman's face not visible (mostly dark hair), so her gaze is hard to read
- pic_41: ponytailed girl holds a small dark unidentified object (maybe a phone)
- pic_41: red shape at the dog's neck/ear: collar, bandana or small hat

### Unintended narrative or safety cue (4)

- pic_28: boy standing at the top of the slide with both arms up and no hands on the rail looks risky
- pic_33: ball passes very close to the kite string and could hit it
- pic_33: cat walking along the fence towards the birdhouse could read as stalking birds
- pic_35: nozzle points toward the girl; water could spray her if the goat steps off

Total unintended oddities: 49. Pictures with none: pic_26.
