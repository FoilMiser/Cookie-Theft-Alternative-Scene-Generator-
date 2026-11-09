# v0.43 picture-description scoring, set B (pic_25 to pic_48)

Scored from desc_pic_25.md to desc_pic_48.md against keys_b.json; no other file was opened.
Coverage check: 24 pictures, 284 key items, every item has exactly one score; none missing, none invented.
Rules: 1 = clear with the right meaning; 0.5 = partial or one of several readings; 0 = not mentioned; misread = mentioned but read as something else (counts 0 in means).

## Mean score by item type

| Type | Items | Mean | 1 | 0.5 | 0 | misread |
|---|---|---|---|---|---|---|
| entity | 163 | 1.000 | 163 | 0 | 0 | 0 |
| action | 78 | 0.994 | 77 | 1 | 0 | 0 |
| inference | 25 | 1.000 | 25 | 0 | 0 | 0 |
| contradiction_notice | 9 | 0.778 | 7 | 0 | 2 | 0 |
| contradiction_explain | 9 | 0.889 | 7 | 2 | 0 | 0 |
| **all** | 284 | 0.988 | 279 | 3 | 2 | 0 |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Score | Target | What the describer said |
|---|---|---|---|---|---|
| pic_25 | i15 | contradiction_notice | 0 | Something is wrong with the dog | not flagged; says no oddity besides the frying pan |
| pic_25 | i16 | contradiction_explain | 0.5 | The dog is reading a newspaper, but dogs can't read | reading only as an alternative ('lying/resting on it or tearing/reading it'); concluded it just lies on it |
| pic_31 | i14 | contradiction_notice | 0 | Something is wrong with the dog | not flagged as odd; dog only described as lying on and pawing at the newspaper |
| pic_31 | i15 | contradiction_explain | 0.5 | The dog is reading a newspaper, but dogs can't read | only as one of three readings: 'lying on it, tearing it, or "reading" it' |
| pic_31 | i19 | action | 0.5 | A grandfather is taking a photo | old man 'looks through binoculars (or a camera)'; camera only as the second reading |

Both dog-reading-the-newspaper contradictions (pic_25, pic_31) were missed the same way: the dog is seen on the open newspaper, "reading" is raised only as an alternative, and the picture is not called odd. No item was misread.

Full-credit items where a detail was read differently (not counted as errors):
- pic_42 i01: the dog's lead is read as clipped to its collar and lying on the ground, not held in its mouth.
- pic_45 i04: the sweeper (a man in the key) is read as a boy.

## Unintended oddities by kind

**Unclear motive or direction of a figure** (4)
- pic_27: unclear why the woman is running: away from the dog behind her, off after a thrown ball, or toward the child in the sandbox
- pic_31: unclear why the man on the left is running (jogging, or rushing away from or after something off the left edge)
- pic_36: the woman's walking direction is ambiguous: left toward the house, or at a glance right toward the waving man
- pic_40: the woman's walking direction is slightly unclear (faces right; stride could go down the path or across it)

**Pose, expression or shadow that reads oddly** (3)
- pic_35: the kite girl does not look upset although her kite is caught in the tree
- pic_35: the gap between the jumping boy and his shadow could make him look as if he is floating
- pic_43: the woman is turned partly toward the viewer while rolling the fence at her side, slightly awkward

**Animal drawing hard to read** (3)
- pic_29: the cat's body overlaps the tree trunk behind it, so its outline is hard to separate from the trunk [cat, profile]
- pic_40: at a quick glance the goat might be taken for a sheep [goat, three-quarter back]
- pic_47: the dog's head is drawn a little oddly, a large dark ear covering much of it [dog, profile]

**Figure overlapping the pond edge (settled by the describer)** (2)
- pic_32: the woman's body overlaps the far edge of the pond (describer settles it: her feet are on the bank)
- pic_37: the man stands right at the rim of the pond (describer settles it: on the grass, not in the water)

**Animal out of place (tethered goat in a park)** (2)
- pic_25: a goat tethered to a stake in a public park is a little unusual [goat, three-quarter front]
- pic_40: a goat tethered to a stake in a public park is a bit unusual [goat, three-quarter back]

**Prop drawing (stiff hose)** (1)
- pic_33: the hose rises from the ground to the woman's hands in a tight curve that looks a little stiff

**Composition (sky too large)** (1)
- pic_47: the sky takes up a large part of the picture, with everything in the lower half

Total: 16 oddities in 12 of 24 pictures; 12 pictures had none.

### Oddities about animals, by angle

| Angle | Count | Where |
|---|---|---|
| profile | 2 | pic_29 cat, pic_47 dog |
| three-quarter front | 1 | pic_25 goat |
| three-quarter back | 2 | pic_40 goat, pic_40 goat |
