# v0.42 picture-description scoring, set B (pic_24 to pic_46)

Scored from `desc_pic_24.md` ... `desc_pic_46.md` against `keys_b.json`. 23 pictures, 270 items.

## Mean score by item type

| Type | Items | Mean | Scored 1 | Scored 0.5 | Scored 0 / misread |
|---|---:|---:|---:|---:|---:|
| entity | 150 | 0.993 | 149 | 0 | 1 |
| action | 79 | 1.000 | 79 | 0 | 0 |
| inference | 21 | 1.000 | 21 | 0 | 0 |
| contradiction_notice | 10 | 0.950 | 9 | 1 | 0 |
| contradiction_explain | 10 | 0.950 | 9 | 1 | 0 |
| **all** | 270 | 0.993 | 267 | 2 | 1 |

No item was scored "misread".

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_42 | i14 | contradiction_notice | Something is wrong with the dog | 0.5 | not called wrong or odd; only listed as unsure ('reading' it like a person, or grabbed someone's paper; pose awkward to read) |
| pic_42 | i15 | contradiction_explain | The dog is reading a newspaper, but dogs can't read | 0.5 | 'as if it is reading it or has grabbed it': reading offered as one of two readings, never said to be impossible |
| pic_42 | i21 | entity | There are a few white clouds | 0 | no clouds mentioned anywhere (only sun and a bird near the sun) |

Every other item (all of pic_24 to pic_41 and pic_43 to pic_46) scored 1. Minor wording slips that still earned 1: the man with the hose in pic_34 and pic_36 is called a boy; the teenager in pic_27, pic_35, pic_39, pic_40 and pic_42 is called a boy; pic_28's child is not described as upset.

## Unintended oddities, grouped by kind

16 oddities in 12 of 23 pictures; 11 pictures had none (pic_24, 25, 27, 29, 31, 33, 38, 39, 41, 45, 46).

### Possible drawing glitches or bad geometry (7)

- pic_30: the hose swells into a bulge just before the goat; could be an oddly drawn wide piece of hose
- pic_34: the hose bulges fat under the dog; could be a puddle or a drawing glitch where the hose suddenly widens
- pic_36: the hose bulges right under the dog's paws; could be a puddle or an odd wide section of hose
- pic_26: the seesaw plank seems to pass under/through the man's thighs while his feet are planted
- pic_40: the tree branch bends out specially to hold the fish, slightly unnatural
- pic_42: the newspaper stands upright on the ground by itself; the puppy only has a paw on it [dog, profile]
- pic_32: a small dark mark on the woman's cheek, possibly a drawing artefact

### Pose or face hard to read (2)

- pic_30: the man's face is turned away/down, so his expression is hard to read
- pic_42: the puppy's pose (sitting back with legs out) is awkward to read [dog, profile]

### Proportion (1)

- pic_28: the fishing rod looks very long relative to the woman

### Placement that suggests an unintended event (2)

- pic_35: the walking man's front foot is at the flower bed's rim, so he looks about to step into it
- pic_43: the cat walks on the freshly painted fence boards but shows no paint on its paws [cat, profile]

### Unclear who or what something belongs to or is aimed at (3)

- pic_44: the flying hat is an orange baseball cap that doesn't match the old woman's outfit, so it may not be hers
- pic_37: unclear who the grandfather is waving at; nobody is looking at him
- pic_42: two cardboard boxes lying on the pavement for no obvious reason

### Unusual scene content (1)

- pic_30: a goat in a back garden is called unusual (though not impossible) [goat, profile]

### Oddities about animals, by angle

| Angle | Count | Where |
|---|---:|---|
| profile | 4 | pic_30 goat, pic_42 dog, pic_42 dog, pic_43 cat |
| three-quarter front | 0 | - |
| three-quarter back | 0 | - |

The three hose bulges sit under an animal's feet (goat, profile in pic_30; dog, three-quarter back in pic_34 and pic_36) but are about the hose, so they are not counted against an angle.

## Completeness check

Checked by script against `keys_b.json`: all 23 pictures present, all 270 items scored exactly once, no item missing, no item or picture invented, item order matches the key, no picture has more than three unintended oddities.
