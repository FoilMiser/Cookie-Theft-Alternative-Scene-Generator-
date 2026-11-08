# v0.42 picture-description scores, set A

Sources: `desc_pic_01.md` to `desc_pic_23.md`, scored against `keys_a.json`. Per-item scores and evidence are in `scores_a.json`.

Coverage check: all 23 pictures and all 250 key items have exactly one score each. No item is missing, no item was invented, and every score is 1, 0.5, 0 or "misread" (checked by script against `keys_a.json`, with a duplicate-key check).

## Mean score by item type

| Item type | Items | Mean | Below 1 |
|---|---|---|---|
| entity | 149 | 1.00 | 0 |
| action | 67 | 1.00 | 0 |
| inference | 14 | 1.00 | 0 |
| contradiction_notice | 10 | 0.90 | 1 |
| contradiction_explain | 10 | 0.90 | 1 |
| **all** | **250** | **0.99** | **2** |

No item was scored 0.5 or "misread".

## Items scored 0, 0.5 or misread

| Pic | Id | Score | Target | What the describer said |
|---|---|---|---|---|
| pic_10 | i11 | 0 | Something is wrong with the bicycle | Only "a teal bicycle parked against" the fruit stall. Nothing about it is called wrong. |
| pic_10 | i12 | 0 | The bicycle has square wheels, so it could not roll | Wheels not mentioned. In pic_04 and pic_06 the same square-wheel bicycle was caught, but there it stood alone in the foreground on a kickstand. In pic_10 it is parked against the busy stall. |

### Hedged items scored 1 (main reading correct, alternative offered)

For an item to get 0.5 as "one of two readings", the describer had to leave the readings open. These describers chose the target reading and gave an alternative only as a side note, so the items scored 1:
- pic_01 i02 and pic_23 i02, eating ice cream: the small pink cone might be "a flower he/she is smelling".
- pic_02 i01 and pic_16 i01, planting: kneeling at the flower bed and gardening, but "planting or picking" is left open.
- pic_04 i09, balloon let go: "I read it as escaping", though the child could still be about to catch it.
- pic_04 i19, taking a photo: camera, "or ... binoculars".
- pic_10 i03, bird stealing the sandwich: or the bird is "just standing on the bench next to it".
- pic_10 i15, dog reading: "Read the other way, the dog is jumping up at or grabbing a paper someone dropped".
- pic_15 i03, bird pecking: "pecking at the ground, unaware, or looking at the cat".
- pic_16 i04, kite stuck: "most likely" stuck, but it could be flying just in front of the tree.

## Unintended oddities (16 in 12 pictures), by kind

**Overlap or depth unclear (4)**
- pic_03: near the boy's legs the hose runs over or very close to his right leg. It is unclear whether it passes in front of or behind him.
- pic_04: the kite string seems to run across or very close to the tree trunk before reaching the kite.
- pic_13: a swing rope runs so close to or behind the girl's head and shoulder that it can look as if it passes through her.
- pic_19: it is unclear whether the man is sitting on the seesaw seat or perched just behind it.

**Object identity unclear (4)**
- pic_01: the small pink ice cream could be a flower he is smelling.
- pic_23: the small pink ice cream could be a flower she is smelling.
- pic_04: the old man's camera might be binoculars.
- pic_16: the worker's orange striped hi-vis vest could be mistaken for a life jacket next to the pond.

**Hose bulge reads as something else (2)**
- pic_03: the bulge behind the goat is so large and flat it could look like a puddle or a second hose.
- pic_11: the bulge behind the dog is a wide flat swelling that could be a puddle or a flattened, kinked section.

**Support or placement (2)**
- pic_10: the newspaper stands upright on the ground by itself with the dog's paws on it, so the dog could be jumping at a dropped paper [dog, profile].
- pic_16: the pram's wheels are on the grass beside the path while the old man walks on the path.

**Animal drawing hard to read (2)**
- pic_08: the dog's head, turned down into the splat, is partly hidden and its shape is hard to read [dog, profile].
- pic_09: the cat's legs are thin, stiff and angular, a little stick-like [cat, profile].

**Lighting or shadow inconsistent (2)**
- pic_09: only the wheelbarrow casts a shadow. The watering can, pots and other objects have none.
- pic_17: the lawn and colours stay bright under a dark storm sky, which looks mismatched.

### Oddities about animals, by angle

| Angle | Count | Where |
|---|---|---|
| profile | 3 | dog pic_08 (head hard to read), dog pic_10 (newspaper standing by itself), cat pic_09 (stick-like legs) |
| three-quarter front | 0 | none |
| three-quarter back | 0 | none |

The two hose-bulge oddities sit just behind the goat (pic_03, three-quarter front) and the dog (pic_11, three-quarter front). They are about the hose, not the animal, so they are not counted here.

Pictures with no unintended oddities: pic_02, 05, 06, 07, 12, 14, 15, 18, 20, 21, 22.
