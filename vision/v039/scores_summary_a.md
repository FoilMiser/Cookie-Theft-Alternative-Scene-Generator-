# v0.39 picture-description scoring, key A

Sources: `desc_pic_01.md` to `desc_pic_24.md` and `keys_a.json` only. Per-item scores and evidence are in `scores_a.json`.

**Completeness check:** keys_a.json has 24 pictures and 282 items. scores_a.json has the same 24 pictures and 282 scores, one per key item. No item is missing, no item was invented, and every score is 1, 0.5 or 0. There are no misreads.

## Mean score by item type

| Type | Items | Total | Mean |
|---|---:|---:|---:|
| entity | 160 | 159.0 | 0.994 |
| action | 82 | 81.5 | 0.994 |
| inference | 20 | 20.0 | 1.000 |
| contradiction_notice | 10 | 10.0 | 1.000 |
| contradiction_explain | 10 | 10.0 | 1.000 |
| **all** | **282** | **280.5** | **0.995** |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---:|---|
| pic_04 | i02 | A girl is eating an ice cream | 0.5 | She holds "something small and pink" to her mouth, "probably eating a small ice cream or sweet". The unsure section also offers a lolly, a flower she is smelling, or a whistle. |
| pic_21 | i06 | There are a few white clouds | 0 | Clouds are never mentioned. The sky is described only as having "white swirly wind lines". |

Misreads: none.

Borderline credits (scored 1 because the free description commits to the target, though the unsure section adds an alternative): pic_05 i04 (dog blocking the hose), pic_09 i03 (bird stealing the sandwich), pic_17 i09 (balloon got away), pic_21 i01 (woman reaching for the hat). pic_06 i04 got 1 for "small blue bird standing on the grass": pecking is not mentioned, but a bare "bird" is an accepted phrasing. pic_08 i09 got 1 because the girl is "feeding" the duck, with bread pieces around it.

## Unintended oddities (13 in 10 pictures)

No oddities were reported for pic_02, 06, 11 to 19 and 22 to 24.

**Animal head merges with the grass tuft (3)**
- pic_01: the goat's head is small and low against the grass tuft, and at first glance it is hard to tell head from tuft [goat, three-quarter front]
- pic_04: the goat's head is small for its body and blends into the tuft, so it could be taken for a separate white object [goat, profile]
- pic_08: the goat partly blends with the grass tuft under its head [goat, three-quarter front]

**Object or figure that looks unsupported (2)**
- pic_09: the dog's newspaper seems to stand up on its own on the ground [dog, profile]
- pic_09: the jumping girl's shadow is separated from her feet, so she could look like she is floating

**Figure drawn over the pond (2)**
- pic_03: the photographer's body overlaps the pond, though his feet are on the grass
- pic_20: the fisherman's upper body overlaps the pond, though his feet are on the bank

**Drawing gaps or placement (2)**
- pic_10: the upward water stream does not clearly start at the spout; there is a small gap
- pic_09: the flowers sit against a dark door with no pot, and the door reaches below the pavement line, so it could be a tall planter

**Prop too small to identify (1)**
- pic_04: the pink item at the girl's mouth is too small to make out (ice cream, sweet, flower or whistle). This is also why pic_04 i02 got 0.5.

**Odd body pose (1)**
- pic_05: the grandfather's white sleeve seems stretched straight across his body to the hose nozzle

**Scene logic (2)**
- pic_07: a second cardboard box lies near the stall, and the describer finds no purpose for either box
- pic_21: it is mildly odd that the grandmother calmly eats ice cream in strong wind

### Animal oddities by angle

| Angle | Count | Cases |
|---|---:|---|
| three-quarter front | 2 | goat pic_01, goat pic_08 |
| profile | 2 | goat pic_04, dog pic_09 (newspaper) |
| three-quarter back | 0 | none |

By animal: goat 3 (every picture with a goat), dog 1, and none for cat, bird or duck.

Left out as hedges about small details: seesaws with no visible handles (pic_14, 15), the tool in the girl's hand (pic_11), which way people are walking (pic_01, 18), why the woman is running (pic_17, 23), and the ball's markings (pic_19).
