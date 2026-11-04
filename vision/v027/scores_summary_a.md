# Scores summary, set A

22 pictures, 231 scored items, 60 unintended oddities.

**Completeness check:** run by script against `keys_a.json`. Every item of every picture has exactly one score: none missing, none invented.

## Mean score by item type

A misread counts as 0 in the means. There were no misreads.

| Type | Items | Mean | Scored 1 | Scored 0.5 | Scored 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 132 | 0.947 | 125 | 0 | 7 | 0 |
| action | 68 | 1.000 | 68 | 0 | 0 | 0 |
| inference | 13 | 0.885 | 10 | 3 | 0 | 0 |
| contradiction_notice | 9 | 1.000 | 9 | 0 | 0 | 0 |
| contradiction_explain | 9 | 1.000 | 9 | 0 | 0 | 0 |
| **all** | **231** | **0.963** | **221** | **3** | **7** | **0** |

## Items scored 0, 0.5 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_09 | i08 | entity | There are a few white clouds | 0 | clouds not mentioned anywhere in the description |
| pic_11 | i05 | entity | There are a few white clouds | 0 | clouds not mentioned anywhere in the description |
| pic_12 | i03 | entity | There are a few white clouds | 0 | clouds not mentioned anywhere in the description |
| pic_14 | i09 | entity | There are a few white clouds | 0 | clouds not mentioned; the sky is called 'empty' |
| pic_15 | i02 | inference | The dog wants to go for a walk | 0.5 | absent from the free description; unsure section only: 'looks like it is asking for a walk, or could just be an odd pose' |
| pic_15 | i11 | entity | There are a few white clouds | 0 | clouds not mentioned anywhere in the description |
| pic_16 | i09 | entity | There are a few white clouds | 0 | clouds not mentioned anywhere in the description |
| pic_16 | i10 | entity | There is a tree | 0 | no tree mentioned; only a small bush by the house |
| pic_21 | i03 | inference | The dog wants some of the food | 0.5 | begging stated, but 'begging from her bag, or could be doing its own trick'; never linked to the man's ice cream |
| pic_21 | i13 | inference | The teenager is going to trip over a bucket | 0.5 | 'may be about to walk into or trip over it', but also 'headed roughly past it... may not be in his way at all' |

**Pattern in the misses:** all six cloud misses fall in pic_09 to pic_16, and they are every cloud item in that range. Every cloud item outside it scored 1. The descriptions in that range also never list the sun or sky as an inventory item, so this may be a habit of those descriptions rather than a problem with the pictures. The pictures themselves were not checked.

## Unintended oddities by kind

Most common kind first. Each oddity appears under one kind only.

### Parts that merge, overlap or pass through each other (11)

- pic_22: Fork handle overlaps the man's chest and looks as if it passes through his body or sticks to his shirt
- pic_02: Cat's legs and the tree trunk overlap confusingly, giving a brown patch at the cat's chest
- pic_07: Ball sits so close to the kicking boy's shoe that it looks stuck on
- pic_09: Watering can is small and seems to merge with the woman's hand
- pic_11: Duck's wake lines spill off the pond edge onto the bank
- pic_12: Top of the chute passes into the red frame, with the frame drawn over it; looks slightly unnatural
- pic_12: Girl sits slightly above the chute surface or merges with it at the hips
- pic_13: Girl sits partly on the sandpit frame rather than inside it, overlapping the frame
- pic_13: Castle base sits over the sandpit frame, so it is unclear if it is inside the pit
- pic_14: Boy's lower legs and foot merge with the broom head and shadow
- pic_16: Hose looks close to passing through or behind the goat's back foot

### Stiff, twisted or oddly built bodies (11)

- pic_16: Woman's face is hidden by her arm and hair, so her head looks on backwards or turned away
- pic_03: Boy's arms look awkwardly crossed or folded over his chest, possibly drawn at an odd angle
- pic_04: Dog's tail and body look stiff
- pic_13: Boy's hood is a blue lump behind the neck that looks slightly odd
- pic_17: Woman's arm and torso look narrow and twisted, with very straight, thin legs
- pic_18: Hose rises at a sharp, stiff angle where it meets the hand
- pic_18: Skirt of the yellow dress looks narrow and lumpy
- pic_19: Bearded man's legs look long and stiff, and his body sits slightly in front of the bench back
- pic_20: Sitting man's legs bend and fold oddly behind the basket
- pic_20: Bearded man's arms stretch long and straight to a sharply angled handle; stroller looks small next to him
- pic_21: White begging dog is thin and upright, 'rather like a tall stretched shape'

### Objects or animals hard to recognise (9)

- pic_19: Flying cap is hard to recognise at first; could be taken for a red bird or a shoe
- pic_10: Goat hard to read: face pressed down, could be a sheep or kid, stiff legs, body angled sharply
- pic_10: Pink plant in the pot looks a bit like a tulip head or a hand
- pic_11: Duck's pale oval wing could look like a plate on its back
- pic_15: Fish looks flat on the foliage with no support; could be a toy or a stray piece of the drawing
- pic_16: Hose bulge could be read as an extra object lying on it, such as a dark blue fish or bag
- pic_21: Goat's head looks twisted or low; could be read as a sheep or a dog at first glance
- pic_21: Ball looks like a blue planet in a nest of leaves, and paler leaf clumps look like bushes stuck in the foliage
- pic_22: Dustpan looks flat and small, more like a red wedge; could be a toy or a trowel

### Shadows missing, oversized or offset (8)

- pic_18: Puppy's shadow is a very wide oval, much wider than the puppy; looks like a patch or hole on the grass
- pic_01: Boy has a shadow but the girl has none; looks inconsistent
- pic_06: Boy has a shadow but the girl has none; looks inconsistent
- pic_07: Jumping boy's shadow sits a little far to the side
- pic_08: Floating box has no shadow, and its size and distance are hard to judge
- pic_19: Dog's shadow is a wide dark oval, larger than the dog
- pic_20: Runner's shadow is a large oval, wide and offset from her feet
- pic_22: Man's shadow is a wide dark oval, larger than expected

### Scale and depth look wrong (5)

- pic_06: Woman looks too large for how far back she stands: nearly as tall as the swing frame, feet level with the fence base
- pic_03: Boy looks rather small next to the bench, and his feet barely have a shadow
- pic_05: Little girl drawn very small compared with the adults
- pic_15: Paint tray seems small for the roller, and the tin overlaps it
- pic_17: Lamppost looks very tall compared with the people

### Held objects and tools not clearly in use or in contact (5)

- pic_05: Painter's tool unclear: blue head looks like a big block sticking up above the fence, and the painted panel looks like a flat block
- pic_09: Roller head seems to stand clear of the fence, at the top of an unpainted plank
- pic_10: Paper bag lies flat against the man's body, as though not quite held
- pic_15: Painter works rightward into the blue section with the unpainted part on his left; 'not clear why he is on that side'
- pic_17: Cone sits right at the front of the woman's face, so she could be smelling it rather than eating

### Seesaw seating and balance (3)

- pic_01: Seesaw nearly level, yet the boy's feet touch the ground while the girl's dangle (called 'the oddest thing')
- pic_01: Little girl sits almost past the end of the plank and looks close to falling off
- pic_06: Little girl sits very near the end of the plank, close to the edge

### Motion and trajectory cues (3)

- pic_05: Ball looks too high and could be heading over the fence, past the catcher
- pic_03: Balloon hangs at head height rather than pulling upward
- pic_07: Motion lines under the kicking foot are curved and detached; could be marks on the grass

### Scene logic (3)

- pic_14: The two boxes look alike, so the wet box could be read as having fallen from the sky
- pic_02: Seems 'a bit silly' to water the flowers when it is about to rain
- pic_08: No people at all, unusual compared with a busy garden scene

### Figure in front of the pond reads as standing in the water (2)

- pic_04: Man in red overlaps the pond and can look as if he is standing in or walking on the water
- pic_11: Man's upper body covers part of the pond, and he looks close to standing in the water

## Judgement calls behind the scores

These items scored 1, but a stricter reader could differ.

- **Hedged inferences.** The free description commits to the inference and the unsure section only names an alternative, so these scored 1: pic_05 i05, pic_09 i02, pic_21 i10. Scored 0.5 instead were pic_15 i02 (only in the unsure section) and pic_21 i13 (the describer argues the boy is walking past the bucket). If all three went to 0.5, the inference mean would be 0.769 rather than 0.885.
- **Wooden box read as cardboard.** pic_08 i01 and pic_14 i04 scored 1 because 'box' is accepted, but the describer calls it a cardboard box both times. In pic_14 they say the floating box and the package look like the same kind of box, while the key treats them as a wooden box and a package.
- **Begging dog.** pic_21 i02 scored 1 because 'dog begging' is accepted, but the describer places the dog with the older woman, not the man on the bench.
- **Bird action.** pic_21 i09 scored 1 because bare 'bird' is accepted, but the describer says the bird stands, not that it pecks.
- **Age labels.** Figures keyed as teenager are consistently called a boy (pic_07, 13, 15, 16, 21, 22). The red-shirt figure keyed as man is often 'boy', 'boy or young man' or 'man or older boy' (pic_02, 04, 09, 10, 14, 19, 20, 21). No item was marked down for this, since the targets are the actions.
