# Scores summary, key set C (pic_49 to pic_71)

Scored from desc_pic_49.md to desc_pic_71.md against keys_c.json only.

## Mean score by item type

| Type | Items | Mean | Below 1 |
|---|---|---|---|
| entity | 142 | 0.951 | 7 |
| action | 83 | 0.994 | 1 |
| inference | 17 | 0.971 | 1 |
| contradiction_notice | 10 | 0.950 | 1 |
| contradiction_explain | 10 | 0.900 | 2 |
| **all** | 262 | 0.964 | 12 |

A misread counts as 0 in the means. There were no misreads in this set.

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_55 | i01 | action | A dog is sitting by the door with its leash in its mouth | 0.5 | dog sits upright by the house door, but the red lead is 'attached to its collar and lies loose in a loop on the grass', not in its mouth |
| pic_55 | i02 | inference | The dog wants to go for a walk | 0.5 | one of two readings: 'could be waiting to go for a walk, or it may simply have been left with its lead on' |
| pic_57 | i16 | contradiction_explain | The wheelbarrow has square wheels, so it could not roll | 0.5 | 'a square, grid-like thing where its round wheel should be'; offered as one of two readings: square wheel, or the barrow sitting on a square drain grate with no wheel |
| pic_57 | i21 | entity | There are a few white clouds | 0 | no clouds or sky details mentioned |
| pic_58 | i11 | entity | There are a few white clouds | 0 | no clouds mentioned |
| pic_59 | i14 | contradiction_notice | Something is wrong with the dog | 0.5 | only 'as if reading it'; not called odd, and the unsure section offers 'simply lying on it' as an equal reading |
| pic_59 | i15 | contradiction_explain | The dog is reading a newspaper, but dogs can't read | 0.5 | dog reading described only as 'as if reading it' / 'reading it as a joke', alternative 'simply lying on it'; never says dogs can't read |
| pic_59 | i21 | entity | There are a few white clouds | 0 | no clouds mentioned |
| pic_60 | i05 | entity | There are a few white clouds | 0 | no clouds mentioned |
| pic_62 | i07 | entity | There are a few white clouds | 0 | no clouds mentioned |
| pic_64 | i03 | entity | There are a few white clouds | 0 | no clouds mentioned |
| pic_71 | i14 | entity | There is a tree | 0 | no tree mentioned |

Patterns:
- Six of the seven zeros are 'a few white clouds' (pic_57, 58, 59, 60, 62, 64): the describers say 'sunny' and stop. The other zero is the tree in pic_71, a busy scene.
- In every 0.5 the describer saw the element but got only half the meaning. In pic_55 the lead was read as clipped to the collar, not held in the mouth, so 'wants a walk' became one of two readings. The others were left as two equal readings: a square wheel or a drain grate (pic_57), and the dog 'as if reading' the newspaper or just lying on it (pic_59).

## Unintended oddities, grouped by kind

### Figure overlaps the pond (resolved as standing in front of it) (3)
- pic_52: the walking man's upper body overlaps the pond (read as standing on the grass in front of it)
- pic_56: the woman's upper body overlaps the pond (read as walking on the grass in front of it)
- pic_62: the photographer's body overlaps the pond (feet read as on the grass in front of it)

### Figure placement or overlap with other scenery (2)
- pic_51: the man in green overlaps the clothesline; unclear whether he is in front of or behind it
- pic_63: the woman in yellow seems to stand against the shop front rather than on the open pavement

### Object not grounded or not in contact (2)
- pic_61: the two potted plants look as if they are hovering above the lawn because they have no shadows
- pic_57: the woman in yellow's spade blade rests on a small brown lump instead of going into the ground

### Gaze does not match the action (1)
- pic_50: the man's face is turned to the right, so he does not seem to look at the flowers he is watering

### Prop drawing hard to read or slightly off (3)
- pic_53: the hose loops a long way from the reel to the man and is hard to follow in places
- pic_67: the slide's ladder leans off to the left of the red frame and looks a bit loose (minor)
- pic_60: the kneeling man's reflective vest band looks slightly twisted across his chest (minor; 'probably just the vest design')

### Animal body or pose hard to read (2)
- pic_58: the spotted dog's body shape is slightly hard to read (play bow or about to pick up the ball) [dog, three-quarter front or profile]
- pic_61: the cat is small and drawn compactly, so it could be read as crouching or hiding rather than sleeping [cat, three-quarter front]

Total: 13 oddities in 12 of 23 pictures; 11 pictures had none.

### Animal oddities by angle

| Animal, angle | Count |
|---|---|
| cat, three-quarter front | 1 |
| dog, three-quarter front or profile | 1 |

pic_58 has two dogs and the key lists one three-quarter front and one profile without saying which dog is which, so the spotted dog's angle is left as 'three-quarter front or profile'.

Left out as hedges rather than oddities: who a camera is pointing at (pic_54, 60, 62), crying versus rubbing an eye (pic_58), sleeping versus resting (pic_49), child's gender (pic_67), the girl's size (pic_70), and doubts that are about scored items themselves (for example the sprinkler 'pointlessly' watering the box in pic_71, the bucket possibly being a white hat).

## Coverage check

keys_c.json has 23 pictures and 262 items; scores_c.json has 23 pictures and 262 scored items.
Missing items: none. Invented items: none. Every item has exactly one score.
