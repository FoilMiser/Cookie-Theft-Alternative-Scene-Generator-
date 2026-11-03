# Picture description scores, set A (pic_01 to pic_22)

Scores are in `scores_a.json`.

**Coverage check:** I checked `scores_a.json` against `keys_a.json` with a script. All 22 pictures and all 241 items have exactly one score. None is missing and none is invented.

## Mean score by item type

| Type | Items | Sum | Mean | Scored 1 | Scored 0.5 | Scored 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|---:|
| entity | 127 | 126.5 | 0.996 | 126 | 1 | 0 | 0 |
| action | 73 | 73.0 | 1.000 | 73 | 0 | 0 | 0 |
| inference | 17 | 16.5 | 0.971 | 16 | 1 | 0 | 0 |
| contradiction_notice | 12 | 12.0 | 1.000 | 12 | 0 | 0 | 0 |
| contradiction_explain | 12 | 11.5 | 0.958 | 11 | 1 | 0 | 0 |
| **All** | **241** | **239.5** | **0.994** | **238** | **3** | **0** | **0** |

## Items scored 0, 0.5 or misread

No item was scored 0 or misread. Three were scored 0.5.

| Pic | Id | Score | Target | What the describer said |
|---|---|---:|---|---|
| pic_03 | i08 | 0.5 | The person is sitting on nothing: there is no chair or bench under them | "sitting in mid-air or on the edge of the path", could be a kerb or floating with no seat. The free description and inventory both have him sitting on the path edge. |
| pic_21 | i11 | 0.5 | A package is sitting on the grass | A slatted "wooden crate" standing in a puddle, not a package. "Box" appears only in the unsure section. |
| pic_21 | i12 | 0.5 | The package is going to get soaked | Water lands on the crate and runs down it. Soaking is offered only as one of two readings ("in the way" or "deliberately soaked"), with no harm or prediction stated. |

## Scoring decisions

**Hedges in the unsure section.** If the free description or inventory commits to the target meaning, the item scores 1 even when the unsure section lists an alternative. It scores 0.5 only when the describer never commits. This rule kept these at 1: pic_02 i02 and i08, pic_10 i02, pic_14 i03, pic_15 i05, pic_21 i17.

**Lenient credits at 1.** Stricter rules could lower these:

- **pic_03 i07:** the notice appears only in the unsure section ("there is nothing visible to sit on").
- **pic_12 i03:** she is "stuck" and "he does not seem to notice", which matches an accepted phrasing. The man's weight is never named as the cause.
- **pic_01 i02 and pic_12 i02:** the girl is stuck up in the air, but calling out is not mentioned.
- **pic_10 i01:** "planting or tending", credited under the accepted "gardening".
- **pic_17 i03 and pic_21 i09:** the duck is "swimming towards the crumbs", with no explicit statement that it wants them.
- **pic_18 i02:** the action is right, but the walker is called a boy, not a man.
- **pic_20 i06:** "box" is accepted, but the describer called it cardboard, not wooden.

## Unintended oddities by kind

There are 50 across 22 pictures. pic_19 has none. Each picture is capped at three, so these counts are a floor. Assigning oddities to kinds was my judgement.

### Prop and tool drawing (14)

- **Paint roller:**
  - pic_03: head stands straight up against the fence, partly above the top of the boards.
  - pic_07: head is offset from the handle, and it is unclear whether it touches the wood.
- **Paint and prints:**
  - pic_07: blue fence block is so neat and square-edged it could be a separate fitted panel.
  - pic_07: first paw print sits immediately under the tray, as if coming out from under it.
- **Fishing rod and line:**
  - pic_04: line has a sharp bend near the rod tip.
  - pic_04: rod starts at her waist and runs straight through her hand, an awkward grip.
- **Duck pond:**
  - pic_17: wake lines run past the pond edge onto the grass.
  - pic_17: crumbs lie on or at the edge of the grass rather than on the water.
- **Other props:**
  - pic_02: lighter leaf clumps only around the kite look like an added patch on the tree.
  - pic_05: soil mound looks like a neat flat-bottomed dome on the grass, separate from the hole.
  - pic_05: dustpan lies alone on the far side of the pile, handle pointing away from the sweeper.
  - pic_09: swing ropes meet near the child's body in a small V.
  - pic_15: grey shape at the top of the fork handle is hard to read and merges with the hands and shirt.
  - pic_15: dark shadow under the man runs off the edge of the picture.

### Hose and water drawing (11)

- **Hose looks stiff:**
  - pic_08: curves up unnaturally in front of her.
  - pic_09: rises almost straight up from the grass, some way in front of the man's body.
- **Hose and nozzle not clearly joined:**
  - pic_08: hose seems to end at a rounded tip near her hip.
  - pic_18: thick hose ends near her waist behind her arm, with the nozzle out at her hand.
- **Hose bulge:**
  - pic_20: could read as a flat puddle or a thicker piece of hose.
- **Water looks solid or wrong:**
  - pic_03: thick band of drops, like a beaded curtain.
  - pic_08: pale stream follows the hose's curve and looks like a second hose or stiff band.
  - pic_14: white-edged and thick, almost a solid tube.
  - pic_21: crate with blue streaks down its sides could be a box full of water.
- **Water and pan:**
  - pic_11: pan looks close to level yet water runs from under its near edge (tilted, leaking or holed).
  - pic_11: drops land at or past the bed edge, partly missing the flowers.

### Figure and animal drawing or proportion (10)

- **Limbs and pose:**
  - pic_09: man's legs and feet are narrow and overlap, so the stance looks odd.
  - pic_10: woman's kneeling legs look awkward, with a long pale shin and skirt bunched at the hip.
  - pic_11: feet point oddly, and the shoes overlap and look small for the long thin legs.
  - pic_12: grey patch at the hi-vis man's shoulder looks like a separate odd shape.
  - pic_16: elbows are sharply bent, and forearms look lumpy where the hands meet the hips.
- **Goat:**
  - pic_10: front legs and head are folded under the body in a tangled way.
  - pic_21: drawn a little strangely, at first glance a white dog or lamb.
- **Size or age:**
  - pic_02: girl looks very thin and small compared with the woman.
  - pic_03: seated person has a childlike face on an adult-sized body.
  - pic_21: elderly woman is drawn large for how far back she seems.

### Body overlapping a prop, or depth hard to read (9)

- **Seesaw plank passing through the sitter:**
  - pic_01: runs behind or through the man's legs.
  - pic_06: almost passes through the girl in pink's lap, and her legs extend past the plank end.
  - pic_12: older man looks as if sitting right into the plank, with arms and book overlapping it.
- **Other overlaps:**
  - pic_01: girl on the slide overlaps the side rail, so she could be on the chute or beside it.
  - pic_13: girl and sandcastle sit on the rim of the sandpit, half outside the box.
  - pic_22: woman's head overlaps the striped towel, so towel and hair run together.
  - pic_22: kite string crossing the fence could be mistaken for a crack in it.
- **Depth:**
  - pic_12: hi-vis man's depth is hard to judge, with ladder and fence overlapping around him.
  - pic_22: woman's feet stand further back than the clothes posts, yet her body overlaps the washing.

### Scene logic (6)

- pic_01: grown man reading on a child's seesaw, called a funny, odd thing to do.
- pic_04: fishing in such a small park pond, called slightly unusual.
- pic_05: cat walks on the tips of the fence points, called unlikely.
- pic_06: picture feels a little empty, with most of the lawn blank and nothing about to happen.
- pic_10: goat loose in a park, called the one slightly unusual thing.
- pic_18: watering the garden just as it is about to rain, called slightly odd or funny.
