# v0.9 screen: scorer summaries

Two scorers with the same prompt scored the 41 pictures in two parts (pic_01 to pic_20, 256 items; pic_21 to pic_41, 249 items);
`scores.json` merges `scores_a.json` and `scores_b.json`.

## Pictures 1 to 20

## TPDB v09 scoring, set A (pic_01 to pic_20)

Scored from `desc_pic_01.md` to `desc_pic_20.md` (free description, inventory and unsure section together) against `keys_a.json`. Scale: 1 = clearly conveyed; 0.5 = partly conveyed, or offered only as one of two readings; 0 = not mentioned; misread = element mentioned but read as something else (counted as 0 in means). Inference items needed the stated cause, prediction or intention. Contradiction items needed an explicit 'wrong/impossible/odd' or a statement of the impossible fact. When the free description committed to a reading and the unsure section only hedged it, the committed reading was scored.

### Mean score by item type

| Type | Items | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 123 | 1.000 | 123 | 0 | 0 | 0 |
| action | 89 | 0.955 | 82 | 6 | 0 | 1 |
| inference | 22 | 0.818 | 15 | 6 | 1 | 0 |
| contradiction_notice | 11 | 1.000 | 11 | 0 | 0 | 0 |
| contradiction_explain | 11 | 0.955 | 10 | 1 | 0 | 0 |
| contradiction (notice + explain) | 22 | 0.977 | 21 | 1 | 0 | 0 |
| **all items** | 256 | 0.967 | 241 | 13 | 1 | 1 |

### Items scored 0 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_09 | i17 | action | A cat is sleeping | misread | said the orange cat is 'crouched low in the grass' (inventory: 'crouching/lying low'), an alert pose, not sleeping |
| pic_13 | i10 | inference | The woman is going to trip over a bucket | 0 | bucket noted beside her, but no prediction that she will trip or bump into it |

### Items scored 0.5 (for reference)

| Pic | Item | Type | Target | What the describer said |
|---|---|---|---|---|
| pic_01 | i03 | inference | The duck is coming to eat the bread | only 'swimming toward the crumbs'; the duck's intent to eat is not stated |
| pic_09 | i08 | action | A girl is holding an empty cone, looking upset | girl holds something to her mouth, 'perhaps an empty cone'; upset not mentioned |
| pic_09 | i11 | inference | The girl dropped the ice cream | calls it a 'dropped scoop' but 'not obvious whether it belongs to the girl' |
| pic_11 | i01 | action | A child is holding an empty cone, looking upset | boy 'holds out an ice cream cone'; could not tell if it is empty; upset not mentioned |
| pic_13 | i08 | action | A woman is reading while walking | woman walking with 'something white and open, like a book or papers'; reading-while-walking is one of two readings (vs laundry to hang) |
| pic_15 | i02 | action | A grandfather is watering the flowers | older man holds a watering can, but the water goes to the awning 'rather than onto the flower box'; pouring vs drips falling into the can left open |
| pic_15 | i04 | contradiction_explain | The water is going up into the air instead of falling down onto the flowers | 'seems to go upward onto the awning, or drip down from it into the can': upward flow only one of two readings |
| pic_15 | i11 | action | A girl is holding an empty cone, looking upset | girl holds a cone to her mouth, 'looking at or licking it'; cannot tell if empty; upset not mentioned |
| pic_15 | i14 | inference | The girl dropped the ice cream | 'fell off her cone' offered as one of two readings (vs someone else's ice cream) |
| pic_17 | i03 | inference | The duck is coming to eat the bread | duck 'swimming toward the food', 'clearly food for the duck'; duck's intent to eat not stated |
| pic_18 | i04 | inference | The kite got stuck in the tree | 'may be caught in the tree'; caught vs flying just in front offered as two readings |
| pic_18 | i07 | action | A man is catching the ball | man 'about to catch something or clapping' (two readings) |
| pic_20 | i10 | inference | The package is going to get soaked | water landing on the box with drops on top; 'the box is getting soaked' offered only as an alternative to a placement mistake |

### Unintended oddities reported (not scored items), grouped by kind

44 oddities across 18 of 20 pictures. Hedges that only restate uncertainty about a scored target (e.g. 'the cat could be stalking or just running') are left out here and kept in the item notes instead.

#### Pose or anatomy looks wrong or unreadable (9)

- pic_01: duck's body looks flattened or tilted, so swimming vs just floating is unclear
- pic_02: white dog's legs look tangled or awkwardly bent; pose could be resting, rolling or crawling
- pic_05: flying red bird has an odd shape with one wing raised awkwardly
- pic_06: painter's stance looks twisted: lower body faces the viewer while head and arms turn left to the fence
- pic_09: man digging holds the spade with one hand while the other is near his chest, an odd way to dig
- pic_11: brown dog's head looks detached or oddly shaped where it bends down to the ice cream
- pic_12: runner's direction is ambiguous: head and arm face right but legs read as running toward the viewer
- pic_14: girl's kicking leg looks stiff and comes out low from under her dress, slightly disconnected
- pic_16: man sits partly off the picnic blanket with his legs on the grass, a little awkward

#### Contact and support (floating, perched or not quite resting on something) (6)

- pic_02: blue bird sits in the leaves with no visible branch, so it could look like it is floating in front of the tree
- pic_03: jumping child is much higher than a normal jump and could look like floating; nothing (e.g. a trampoline) explains the height
- pic_08: girl seems to sit slightly in front of the seesaw board rather than on top of it
- pic_10: boy perches high with his head above the slide frame; unclear if he is on the platform or up on the frame
- pic_12: woman seems to sit slightly in front of the bench backrest
- pic_18: girl on the swing has her hands slightly outside the ropes rather than gripping them

#### Overlap, merging and depth order (6)

- pic_04: birdhouse pole stands behind the fence, so it may be in the neighbour's garden
- pic_05: bike racks overlap the wheels and frames and look like they pass through the bikes
- pic_11: bicycle sits behind or partly overlapping the bike rack
- pic_15: water stream crosses the lamp post; cannot tell if it passes in front of or behind it
- pic_15: spotted dog's white head merges with the pink ice cream
- pic_18: kite girl stands against or partly overlaps the fence

#### Scale and proportion (4)

- pic_09: flying red bird is very large compared with everything else and overlaps the cloud
- pic_09: blue bird on the bench is big relative to the sandwich and the woman
- pic_09: sandwich on the bench is 'very large' (sub/burger-like)
- pic_19: bicycle looks short and squashed, with the two wheels almost touching

#### Faces and gaze hidden or unreadable (7)

- pic_01: girl's gaze direction is unclear (basket, flower bed or ladder)
- pic_02: kicking girl's face not visible (mostly dark hair), may be facing away
- pic_03: woman in yellow is turned away; her face is hard to see
- pic_08: boy's face not clearly visible; he may be seen partly from behind
- pic_09: bearded man's face is drawn very dark, so his face and beard blend into one shape
- pic_14: unclear whether the man's beard is grey or it is the side of his grey hair
- pic_15: boy under the stuck ball faces right rather than up at the ball

#### Object identity unclear (5)

- pic_01: white object in the woman's hand is unidentifiable (bread bag, carton or cup)
- pic_04: goat's pink mouth could be chewing or just its colouring
- pic_06: painting tool is ambiguous (roller on a pole or long-handled brush)
- pic_16: object beside the man could be a picnic basket or a bucket
- pic_17: small white cartons with orange tops are unidentifiable (seed bags, bread bags or boxes)

#### Trajectory or aim does not line up (2)

- pic_01: thrown crumbs look like they will fall short of the water and land on the grass
- pic_18: ball is above and to the right of the man's hands, heading up-left, so it may sail over his head instead of into his hands

#### Scene logic inconsistencies (3)

- pic_03: hose reel is not connected to anything
- pic_04: a goat in a back garden is itself unusual
- pic_13: windy enough to blow the cap off and fly a kite, yet the laundry on the line hangs straight down

#### Drawing or rendering artefacts (2)

- pic_06: third blue fence board has a flat, shorter top compared with the pointed boards
- pic_15: water stream looks like a string of beads rather than flowing water

No unintended oddities reported: pic_07, pic_20.

## Pictures 21 to 41

## Picture description scores, key set B (pic_21 to pic_41)

Source: `desc_pic_21.md` to `desc_pic_41.md` scored against `keys_b.json`. Full per-item scores and evidence are in `scores_b.json`. In the means, "misread" counts as 0. Inference items got credit only when the cause, prediction or intention was stated. Contradiction items got credit only when the describer called the thing wrong or odd, or described the impossible fact itself.

### Mean score by item type

| Item type | Items | Mean | 1 | 0.5 | 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 114 | 0.996 | 113 | 1 | 0 | 0 |
| action | 91 | 0.962 | 85 | 5 | 0 | 1 |
| inference | 22 | 0.977 | 21 | 1 | 0 | 0 |
| contradiction_notice | 11 | 0.955 | 10 | 1 | 0 | 0 |
| contradiction_explain | 11 | 0.864 | 9 | 1 | 0 | 1 |
| contradiction (both) | 22 | 0.909 | 19 | 2 | 0 | 1 |
| **All items** | 249 | 0.974 | 238 | 9 | 0 | 2 |

### Items scored 0 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_24 | i02 | action | A man is sweeping | misread | Read as digging, not sweeping: 'jabbing it into the path ... kicks up dust', 'used as a digging tool', 'may be digging up the path, breaking a stepping stone' |
| pic_39 | i05 | contradiction_explain | The box is floating in the air with nothing holding it up | misread | Box not seen as floating: read as 'sticking out of the house wall or leaning behind the house' / 'pass through the house wall' |

No item scored a plain 0. Every scored element was mentioned in some form.

### Items given partial credit (0.5)

| Pic | Item | Type | Target | Why only partial |
|---|---|---|---|---|
| pic_21 | i01 | action | A child is holding an empty cone, looking upset | Boy holding cone up near his face; free text implies his scoop fell, but unsure section says he can't tell if the cone is empty, and gives 'sad/disappointed or just looking' as two readings |
| pic_24 | i04 | contradiction_explain | The person is sweeping with a giant fork instead of a broom | Giant dinner fork identified and called impossible, but as a digging tool / garden fork, not in place of a broom |
| pic_27 | i12 | action | A cat is walking along the fence | Cat seen walking along a high line, but placed on the washing line 'like a tightrope', not the fence |
| pic_30 | i08 | contradiction_notice | Something is wrong with what the person has on their head | Says 'has a blue bucket on their head' without calling it odd; unsure section gives 'bucket worn as a hat or a tall blue hat' |
| pic_30 | i10 | action | A bird is flying | Red bird 'on the roof edge ... with its wings raised'; flying only given as one reading ('perched ... or flying just above it') |
| pic_36 | i04 | action | A child is sliding down the slide | Boy 'sits at the bottom of the slide, leaning back'; 'has just come down the slide or is simply resting' given as two readings |
| pic_41 | i04 | action | A girl is holding an empty cone, looking upset | Small girl 'holding what looks like an ice-cream cone to her mouth'; unsure whether it's empty, and no upset noted |
| pic_41 | i05 | entity | Ice cream is lying on the ground | 'a pink dessert with sprinkles ... lying on the ground'; 'dropped scoop of ice cream ... or a small pink cake or jelly' given as two readings |
| pic_41 | i07 | inference | The girl dropped the ice cream | Only in unsure section, as one of two readings: 'as if she dropped it' vs a cake or jelly on a plate |

### Unintended oddities reported (not scored items), grouped by kind

#### Overlap, layering or merging of drawn objects (7)

- pic_21: kite drawn overlapping a cloud, could look attached to the cloud
- pic_21: dog's white head merges into the pink ice cream (white blob reads as dog or cream)
- pic_23: kite string passes very close to the girl on the seesaw
- pic_23: hoodie person stands right behind the end of the bench, crowding the seated woman
- pic_27: a beige stepping stone is drawn on top of the dog's back (layering error, or a blanket)
- pic_29: man's upper body overlaps the pond (perspective)
- pic_36: man's lower legs cross the seesaw board, so the board could look like it passes through his legs

#### Scale or proportion (9)

- pic_25: sandwich is 'unusually large for one person'
- pic_29: man's legs are drawn very long and thin compared with his upper body
- pic_30: dog's body looks unusually long and stretched
- pic_31: painter stands a little way out from the fence but her brush still touches it (arm/brush reach too long)
- pic_34: stroller handle is very long and angled
- pic_34: baby looks large for the stroller
- pic_37: birds look large compared with the woman
- pic_37: man stands a few steps from the water but his line reaches the middle of the pond
- pic_41: sandwich looks oversized compared with the bench and the man

#### Pose, anatomy or rendering (8)

- pic_24: goat's body bends at a slightly awkward angle
- pic_24: large dark shadow under the fork man, spreading off to the left
- pic_26: cap is drawn upside-down and tilted
- pic_29: dark edge like a cap peak sticks out under the bucket
- pic_32: sandcastle is very blocky and plain, like stacked boxes
- pic_33: goat's pose is awkward (body bent sharply, front legs folded) and could read as a dog
- pic_34: camera woman's head is a plain dark round shape with no face, though her body faces sideways/forward
- pic_39: faint grey shadow patch on the grass with nothing visible to cast it

#### Physics, balance or trajectory (5)

- pic_25: ball's arc heads up over the pond edge, not to the catcher's hands
- pic_33: ball is high and to the catcher's left, so it might go over him
- pic_38: seesaw is only slightly tilted even though an adult and a small child are on it
- pic_38: woman's end of the board doesn't touch the ground
- pic_38: no handle on the woman's side of the seesaw

#### Scene logic or plausibility, not a drawing fault (8)

- pic_21: man is sweeping but nothing is visible on the path
- pic_22: pet food bowl sits near the man, away from the cat, maybe for a dog that isn't there
- pic_23: eating ice cream and reading outdoors while a storm gathers is 'a bit odd'
- pic_24: a goat in a back garden is 'unusual'
- pic_24: fence is being painted blue rather than a wood colour
- pic_26: scene looks sunny and calm apart from the drawn wind lines (wind shown only by symbols)
- pic_29: duck is swimming straight at the fishing float and might peck it or get caught on the line
- pic_33: watering the flowers and running a sprinkler just before a storm 'seems pointless'

#### Ambiguous character or object identity (2)

- pic_25: small white item under the bird that couldn't be identified
- pic_30: bucket-wearer has mixed gender cues: skirt and grey hair, but suspenders and maybe a moustache

Pictures with no unintended oddities reported: pic_28, pic_35, pic_40.

### Note on person labels (not penalised)

All 11 items whose target agent is a "teenager" (the brown-ponytail, blue-hoodie figure) were described as a woman, young woman, girl or person: pic_21 i07, pic_22 i01, pic_23 i10, pic_25 i04, pic_30 i12, pic_31 i03, pic_32 i06, pic_37 i01, pic_38 i02, pic_40 i01, pic_41 i14. The action was right every time, so these got full credit. Grandparent figures were recognised as older people. The bucket-wearer in pic_30 was left open between an older woman and an older man.
