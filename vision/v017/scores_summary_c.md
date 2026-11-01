# Scoring summary: set C (pic_43 to pic_65), vision v017

**Note added after scoring.** The rotation described below was a numbering slip by reader 8: the three descriptions
have since been renamed to the pictures they describe (desc_pic_58.md is now desc_pic_56.md, desc_pic_56.md is now
desc_pic_57.md, desc_pic_57.md is now desc_pic_58.md), so the `[from desc_pic_NN]` tags below give the names the files
had when they were scored. The files as saved are in `reader8_as_saved/`.

**Alignment note.** desc_pic_56, desc_pic_57 and desc_pic_58 do not describe the pictures their keys define. They are rotated: key pic_56 (grandmother planting, goat, man feeding birds) is described in **desc_pic_58**; key pic_57 (teen sweeping with a giant fork) is in **desc_pic_56**; key pic_58 (fisherman, dropped ice cream, square-wheeled wheelbarrow) is in **desc_pic_57**. Each key was scored against the description that matches its content, and those notes are tagged `[from desc_pic_NN]`. The literal pairing (desc_pic_N with key pic_N) is shown below for comparison. key_map.json was not opened, as instructed; check whether the rotation started in the image files or in the description file names.

## Mean score by item type

| Type | n | Mean (content-aligned, used in scores_c.json) | Items < 1 | Mean if paired literally by file name |
|---|---|---|---|---|
| entity | 135 | 1.000 | 0 | 0.956 |
| action | 81 | 1.000 | 0 | 0.895 |
| inference | 19 | 1.000 | 0 | 0.947 |
| contradiction_notice | 10 | 1.000 | 0 | 0.800 |
| contradiction_explain | 10 | 1.000 | 0 | 0.800 |
| **all** | 255 | 1.000 | 0 | 0.924 |

Coverage check: every item in keys_c.json for all 23 pictures has exactly one score. No item is missing and none is invented.

## Items scored 0, 0.5 or misread

**None.** With content-aligned pairing, all 255 items scored 1.

### With literal file-name pairing, the rotated pictures would fail these items

| Pic | Item | Target | Score | Describer said |
|---|---|---|---|---|
| pic_56 | i01 | A grandmother is planting flowers | 0 | desc_pic_56: no grandmother/planting (young man sweeping with a fork) |
| pic_56 | i02 | A goat is eating grass | 0 | no goat |
| pic_56 | i03 | A man is feeding the birds | 0 | no one feeding birds |
| pic_57 | i01 | A teenager is sweeping | 0 | desc_pic_57: park/fishing scene, no sweeping |
| pic_57 | i02 | Something is wrong with what the person is sweeping with | 0 | oddity noticed is the square-wheeled wheelbarrow |
| pic_57 | i03 | The person is sweeping with a giant fork instead of a broom | 0 | no fork |
| pic_57 | i07 | There is a fence | 0 | no fence |
| pic_57 | i08 | It is the back yard of a house | 0 | park, not a back yard |
| pic_57 | i09 | Clothes are hanging on the line | 0 | no washing line |
| pic_57 | i10 | There is a swing set | 0 | no swing set |
| pic_58 | i01 | A man is fishing | 0 | desc_pic_58: no fishing |
| pic_58 | i02 | A duck is swimming in the pond | 0 | pond has 'nobody in or on it' |
| pic_58 | i03 | A child is holding an empty cone, looking down at the ice cream on the ground, upset | 0 | no child with cone |
| pic_58 | i04 | Ice cream is lying on the ground | 0 | no ice cream |
| pic_58 | i05 | A dog is licking the ice cream | 0 | no dog |
| pic_58 | i06 | The child dropped the ice cream | 0 | no ice cream |
| pic_58 | i07 | There is a wheelbarrow | 0 | no wheelbarrow |
| pic_58 | i08 | Something is wrong with the wheelbarrow | 0 | no wheelbarrow oddity |
| pic_58 | i09 | The wheelbarrow has square wheels, so it could not roll | 0 | no wheelbarrow oddity |
| pic_58 | i10 | A bird is sitting on the lamp post | 0.5 | birds pecking on the path, not on the lamp post |

## Near-misses: credited 1, but with a caveat

These items earned full credit, but the note shows a hedge, a looser verb, or a mislabelled agent or attribute.

**Teenager given an adult or shifting label (the key says 'teenager')** (8)

- pic_47 i04, "A teenager is painting the fence": painting the fence blue; actor called 'young woman' (teen labelled adult)
- pic_48 i06, "A teenager is throwing a ball": 'has just thrown a red ball'; thrower called 'woman in the blue hoodie' (teen labelled adult)
- pic_52 i04, "A teenager is reaching up for a hat": arms raised, 'trying to grab' the cap; actor called 'young man' (teen labelled adult)
- pic_53 i02, "A teenager is having a picnic": sitting on a checked picnic blanket with a basket; actor called 'young woman' (teen labelled adult)
- pic_57 i01, "A teenager is sweeping": [from desc_pic_56] sweeping dirt on the path into a dustpan; actor called 'young man' (teen labelled adult)
- pic_49 i02, "A teenager is pointing up at the tree": 'young person in a blue hoodie' pointing up at the ball in the tree
- pic_51 i10, "A teenager is jumping for joy": 'person in a blue hoodie' jumping, arms up, big happy grin (unsure: could read as floating)
- pic_55 i05, "A teenager is sitting and having a drink": 'person in a blue hoodie' drinking from a cup in a sitting position

**Second reading offered in the unsure section (primary reading correct)** (13)

- pic_43 i03, "The cat is about to catch the bird": 'stalking it and about to pounce'; 'cat catching or chasing the bird' (unsure section also allows 'simply walking past', stalking favoured)
- pic_44 i01, "A woman is painting the fence": woman in yellow painting the fence blue with a long-handled brush (unsure: brush or small roller)
- pic_47 i03, "The person is watering the flowers with a frying pan instead of a watering can": 'pouring the water from a frying pan rather than a watering can' (unsure: maybe saucepan/skillet)
- pic_48 i04, "The child let go of one of the balloons": 'slipped away'; 'The boy has lost it' (unsure: let go or came loose)
- pic_49 i07, "The cat is about to catch the bird": 'the cat may pounce on the bird' (unsure: could just be walking)
- pic_51 i09, "A dog is sleeping": small white puppy curled up asleep (unsure: could be white cat or lamb)
- pic_51 i10, "A teenager is jumping for joy": 'person in a blue hoodie' jumping, arms up, big happy grin (unsure: could read as floating)
- pic_56 i02, "A goat is eating grass": [from desc_pic_58] white goat with head down eating grass (unsure: possibly lamb/sheep, goat favoured)
- pic_57 i03, "The person is sweeping with a giant fork instead of a broom": [from desc_pic_56] 'instead of a broom he is using a giant silver dinner fork' (unsure: not a garden fork/rake)
- pic_62 i06, "The box is floating in the air with nothing holding it up": box in mid-air with nobody near it, flagged strange; hedged 'as if it is floating or falling'
- pic_63 i13, "A cat is sleeping": small orange cat 'seems to be lying asleep' (unsure: kitten, fox cub or toy)
- pic_53 i03, "A man is running": young man in red 'jogging or running'
- pic_55 i08, "A man is running": young man in red 'hurries or runs off to the right'

**Looser verb than the target, accepted by the key's phrasing list** (6)

- pic_51 i03, "A dog is licking the ice cream": dog 'bending down to sniff or eat the fallen ice cream'
- pic_55 i03, "A dog is licking the ice cream": brown dog 'sniffing or licking it up'
- pic_58 i05, "A dog is licking the ice cream": [from desc_pic_57] brown dog 'sniffing or eating it'
- pic_49 i06, "A bird is pecking on the fence": red bird 'perched' on the fence near the gate; pecking not stated (bare 'bird' is accepted)
- pic_55 i10, "A child is eating an ice cream": child in yellow 'walks away holding an ice-cream cone with a pink scoop' (holding; eating not stated)
- pic_49 i05, "A cat is crouching low on the fence": cat 'creeping along' the top of the fence towards the bird

**Attribute or identity detail off on a correctly named element** (3)

- pic_62 i04, "There is a wooden box": called a 'brown cardboard box' (key: wooden); 'box' accepted
- pic_61 i12, "A man is reading while walking": 'person in a green shirt walks along reading a book' (gender left open)
- pic_49 i04, "The teenager's ball is stuck in the tree": 'A blue ball is stuck up in the tree' (whose ball not stated)

## Unintended oddities reported (not scored items), grouped by kind

### Ambiguous rendering (10)
- pic_44: painting tool unclear: brush or small roller on a stick (tiny blue tip)
- pic_46: loose end of the red lead lies by the hose reel and could be read as a red hose coming off the reel
- pic_47: painting tool unclear: long-handled brush or small roller on a pole
- pic_49: bucket shows blue at the top: water or blue interior
- pic_54: water stream drawn as separate light-blue segments; could read as a second hose/tube
- pic_56: [desc_pic_58] only one horn visible on the goat
- pic_56: [desc_pic_58] cannot make out what the kneeling woman holds (trowel, seedling, something small and white)
- pic_57: [desc_pic_56] grey puff could be dust or smoke
- pic_60: shadow under the boy but none under the raised girl
- pic_62: object the woman holds could be a paper bag or a white cup

### Unattended / ownerless / unconnected (7)
- pic_50: fruit and vegetable stall with produce out but no stallholder
- pic_52: hose reel not connected to a tap or anything
- pic_52: leaves blown along with the cap have no tree near the man as a source
- pic_55: brown dog eating the ice cream has no lead and no visible owner
- pic_55: fruit and vegetable stall with nobody serving
- pic_56: [desc_pic_58] goat grazing loose in a town park with no owner or lead ('a bit unexpected')
- pic_58: [desc_pic_57] dog eating the ice cream has no lead or visible owner

### Scale / placement (6)
- pic_43: bird fairly large compared with the cat
- pic_53: fisherman stands far back from the pond, so his line is very long
- pic_53: runner is on the grass beside the path rather than on it
- pic_53: picnicker sits at the blanket edge with legs and shoes off it
- pic_57: [desc_pic_56] dustpan lies on the ground by itself; he sweeps into it from a distance
- pic_61: red dog-food bowl sits on its own mid-lawn, away from both dogs ('a bit odd')

### Overlap / occlusion (3)
- pic_43: bird's head drawn pressed into the ground, partly hidden (could look buried)
- pic_49: old man and man in green drawn overlapping, 'squashed together', one partly inside the other
- pic_54: hose passes very close to the man's legs; unclear whether it goes behind or loops around him

### Ambiguous pose / expression / trajectory (3)
- pic_46: dog's eyes drawn closed: happy or dozing
- pic_48: ball is level with but beside the catcher's hands; may go past her
- pic_48: girl on slide has one arm raised: holding on, waving or cheering

### Unscored situation / hazard (3)
- pic_47: watering flowers and painting the fence right before a storm looks odd (describer thinks deliberate)
- pic_48: sleeping cat lies right at the two women's feet; they might step on it
- pic_49: thrown ball could hit the reading old man instead of reaching the catcher

### Unsupported / floating (2)
- pic_51: riderless bicycle stands upright with no support (reported as fact, not flagged)
- pic_51: jumping person off the ground could be read as floating

Total unintended oddities: 34. Pictures with none: pic_45, pic_59, pic_63, pic_64, pic_65.
