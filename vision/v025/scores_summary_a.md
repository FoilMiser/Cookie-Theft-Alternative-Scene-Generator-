# Picture description scores, set A

22 pictures, 248 scored items. Item-level scores and evidence are in `scores_a.json`.

**Completeness check:** a script compared `scores_a.json` with `keys_a.json`. All 248 key items have exactly one score, none is missing and none is invented, and every score is 0, 0.5, 1 or "misread".

## Mean score by item type

| Item type | Items | Points | Mean |
|---|---:|---:|---:|
| entity | 135 | 134.0 | 0.993 |
| action | 75 | 74.5 | 0.993 |
| inference | 14 | 13.5 | 0.964 |
| contradiction_notice | 12 | 12.0 | 1.000 |
| contradiction_explain | 12 | 12.0 | 1.000 |
| **All items** | **248** | **246.0** | **0.992** |

No item was scored "misread". The means would have counted a misread as 0.

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_02 | i13 | entity | There are a few white clouds | 0 | Nothing. Clouds appear nowhere in the description, though "sunny" does. |
| pic_18 | i03 | inference | The duck is coming to eat the bread | 0.5 | "swimming towards the food". This gives the direction only and never says the duck wants the food or is coming to eat it. |
| pic_19 | i01 | action | A grandfather is sweeping | 0.5 | Stands holding a broom "as if sweeping" and looks at the women. "The broom seems still" and he "could be sweeping, or pausing to watch". |

## Judgement calls scored 1

These are worth a second look, because another scorer could mark some of them lower. A reading stated in the free description stayed at 1 when the unsure section only added an alternative. pic_19 i01 is the exception, because the describer also gave evidence against sweeping.

- **Different person label, right action.** The accepted phrasings name only the action, so these were credited:
  - pic_02 i11: teenager read as a man
  - pic_09 i01: teenager read as a boy
  - pic_15 i02: teenager read as a boy
  - pic_10 i01: man read as a boy
  - pic_12 i03: man read as a boy or young man
  - pic_13 i08: woman read as a child, "could also be a small adult"
- **Reading stated, then hedged in the unsure section:**
  - pic_02 i03: "as if begging for it", then "or just looking at the man"
  - pic_05 i03: "seems unable to come down while he stays on it", then "or she could just be enjoying it"
  - pic_08 i03: "seems stuck up there while he stays down", then "or just sitting calmly"
- **Part of the target not reported, accepted phrasing met:**
  - pic_05 i02 and pic_08 i02: stuck up in the air, but no calling out, and her face is read as neutral
  - pic_05 i03 and pic_08 i03: the man's weight is not named as the cause
  - pic_02 i10: the bearded man only holds his ice cream near his face
  - pic_18 i01: food is seen as brown pieces, and bread is not named
- **Different material:** pic_22 i01, where the key says a wooden box and the describer says cardboard with a tape line.

## Unintended oddities by kind

52 oddities in total, with at most three per picture.

### Accidental stories or situations that need explaining (10)
- pic_02: man jumping beside the boy and the stuck ball, unclear if he is reaching for it or jumping for joy
- pic_05: a grown man on a child's seesaw reading a book looks odd
- pic_08: a grown man on a child's seesaw reading a book looks odd
- pic_09: old man sweeps a clean path with nothing to sweep
- pic_11: woman walks straight at the lamp post and looks about to walk into it
- pic_14: woman waters flowers just as it looks about to rain, possibly an intended joke
- pic_16: so many unrelated events that it reads as a collection of little stories and items are easy to miss
- pic_19: no dirt or leaves on the path for the man to sweep
- pic_21: a goat in a small back garden is itself somewhat out of place
- pic_22: garden otherwise empty, could read as something missing, such as a person carrying or catching the box

### Props and effects hard to identify or looking wrong (9)
- pic_02: ball very large for the branch, looks balanced rather than wedged
- pic_03: water arcs look like solid thin blue tubes, could be bent wires or hoops
- pic_04: soil on the spade is a smooth round blob, could be a stone or a dug-up object
- pic_07: baby's body very short and flat, blanket could be a separate cushion
- pic_09: yellow broom head small and pointed, could be a large paintbrush or a dustpan
- pic_10: hose bulge extreme and dark, could be a slug or flat stone on the hose
- pic_12: falling seed dots evenly spaced, hang in the air like a string of beads
- pic_13: painted fence section a very straight even block, neater than a small roller would manage
- pic_20: pan seems small for that much water

### Poses, bodies and shadows (9)
- pic_01: boy has a shadow but the girl has none, so her height off the ground is hard to judge
- pic_01: girl's body thin and small next to the boy
- pic_03: man faces the flowers while his hand reaches to the pot, not looking at what his hand does
- pic_08: boy upright and perched on the chute rather than lying back into it
- pic_10: boy's face close behind his hands, could be read as drinking from the hose
- pic_12: woman's kneeling pose hard to read, skirt forms a round ball and legs look awkward
- pic_13: raking figure could be a child or small adult, girl or boy, with a mouth mark like a little moustache
- pic_14: man's finger points up and left of the clouds, not at them
- pic_17: man's legs stiff with feet close together

### Overlaps, touching and merging (8)
- pic_05: sandcastle overlaps the boy's lower legs, he may be kneeling partly into it
- pic_06: lamp post looks as if it grows out of the man's shoulder or runs behind his back
- pic_13: rake head overlaps the shoes, and the long handle could be taken for a broom
- pic_15: girl overlaps the sandpit frame, unclear if she is in the sand, on the edge or outside
- pic_16: bucket overlaps the fruit stall, could be taken for part of the display
- pic_18: lamp post so close behind the woman that she almost looks attached to it
- pic_18: pram on the grass while the man's feet are on the path
- pic_19: broom handle crosses his body and the head sits near his feet, slightly tangled

### Heads, faces and headwear hard to read (7)
- pic_02: older man has cap peak on one side, grey hair on the other, no clear eye
- pic_05: older man has cap peak, grey hair, something like an ear, no clear eyes
- pic_07: older man has cap peak, grey hair, an ear in the middle, no clear eyes or mouth
- pic_08: older man has cap peak, grey hair, something like an ear, no clear eyes
- pic_15: boy's cap peak points left while his face looks right
- pic_17: older man's head a little hard to read, a round mark on the side of the face taken for an ear
- pic_18: woman's head mostly hair with a small face at the left

### Animals that read as something else or are drawn oddly (5)
- pic_10: goat's head small and horn tiny, could be a lamb or a dog
- pic_11: dog has no clear muzzle or eyes, could be a monkey, an otter or a person in a costume
- pic_12: goat's head small with one horn showing, could be a lamb or a dog
- pic_16: white dog's head a smooth white ball, could be a person in a spacesuit or a small robot
- pic_21: goat's rear legs merged, fewer than four distinct legs

### Swing ropes (2)
- pic_04: ropes narrow towards the boy's head and spread again to the seat, unclear if in front of or behind him
- pic_20: ropes run behind the child's head and come out lower at the seat

### Pasted-on look (2)
- pic_21: fish could look pasted on top of the leaves, or like a decoration with nothing holding it
- pic_22: box very clean and sharp, as if pasted onto the sky
