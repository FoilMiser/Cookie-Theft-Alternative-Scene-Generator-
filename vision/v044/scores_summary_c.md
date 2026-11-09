# TPDB v0.44 picture-description scoring, key set C (pic_43 to pic_62)

Scored from vision/v044/desc_pic_43.md to desc_pic_62.md against vision/v044/keys_c.json; scores are in vision/v044/scores_c.json.

Coverage check: 20 pictures, 232 items in keys_c.json; every item has exactly one score, none is missing and none is invented (checked by script against the key ids).

## Mean score by item type

| Type | Items | Mean | Below 1 |
|---|---:|---:|---:|
| entity | 127 | 0.992 | 1 |
| action | 70 | 0.993 | 1 |
| inference | 21 | 0.976 | 1 |
| contradiction_notice | 7 | 1.000 | 0 |
| contradiction_explain | 7 | 1.000 | 0 |
| all | 232 | 0.991 | 3 |

Misread counts as 0 in the means. No item was scored misread.

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_44 | i05 | inference | The child let go of one of the balloons | 0.5 | offered as one of two readings: holding the string by its very tip, or has just let go and is reaching for it |
| pic_48 | i13 | entity | There are a few white clouds | 0 | no clouds or sky details mentioned anywhere in the description |
| pic_49 | i02 | action | A girl is eating an ice cream | 0.5 | girl holds 'a small white round thing up to her mouth ... as if eating something small or blowing on it'; unsure: a sweet or small ice cream, a dandelion clock, or a whistle |

## Unintended oddities (not scored items), grouped by kind

17 oddities in 12 of the 20 pictures; 8 pictures had none.

### Ground contact and support (things not touching the ground) (2)

- pic_56: the low end of the seesaw does not quite reach the ground; it hangs above the ground line (mid-motion or a drawing error)
- pic_56: the boy's feet appear possibly slightly above the ground, as if hovering

### Parts not attached (1)

- pic_56: the slide's ladder looks set behind the frame rather than attached to the platform

### Figure overlapping the pond edge (depth/layering) (2)

- pic_43: the man's upper body at a glance appears drawn over the pond water (his feet are on the grass, so he reads as standing at the edge)
- pic_44: the woman's body overlaps the front of the pond (her feet are on the grass, so she reads as standing at the edge)

### Near contact between objects (1)

- pic_57: the kite string passes very close to the cat on the fence, nearly touching its front legs [cat, profile]

### Scale (1)

- pic_55: the lamp post is very tall compared with everything else (taken as a style choice rather than an error)

### Out-of-place element or story logic (3)

- pic_59: the man eating ice cream is wearing ice skates on a dry sandy path in summer, which looks out of place
- pic_46: a goat is an unusual animal for a park, though it does not look physically wrong [goat, profile]
- pic_58: the man watering the garden just before a storm seems a bit pointless

### Unclear pose, gesture or expression (4)

- pic_60: the man's expression is unclear: eyes squeezed shut and mouth open (sneezing, yawning or laughing)
- pic_49: the girl's direction of movement is unclear: her face and the object point left but her stride could be read either way
- pic_62: the girl stands well away from and below the ball, so it is unclear whether she is reaching for it, pointing at it or waving
- pic_62: the cat's legs are folded underneath it in a slightly tangled way, so its pose looks a bit awkward [cat, profile]

### Unintended hazard or prediction cue (2)

- pic_49: a grey rock lies just in front of the girl's feet; if she is moving right she might trip on it
- pic_51: the man pushes the pram across the grass instead of the path, heading toward the flower bed; unclear whether he will go around it or into it

### Placement on a prop (1)

- pic_60: his legs stretch off the blanket onto the grass, so he looks off-centre on it

### Oddities about animals, by angle

| Angle | Animals in key | Oddities | Where |
|---|---:|---:|---|
| profile | 13 | 3 | pic_46 (goat), pic_57 (cat), pic_62 (cat) |
| three-quarter back | 1 | 0 | - |
| three-quarter front | 6 | 0 | - |

Note: pic_59's ice skates on a sandy summer path read as a deliberate impossibility but are not a scored item in keys_c.json; it is listed above as unintended.
