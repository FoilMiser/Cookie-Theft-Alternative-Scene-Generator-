# Scores summary, set A (v0.46)

Coverage check: 286 key items across 25 pictures; 286 scored, every item scored exactly once, none missing, none invented (ids matched picture by picture against keys_a.json).

## Mean score by item type

| Type | Items | Mean |
|---|---|---|
| entity | 158 | 0.975 |
| action | 87 | 1.000 |
| inference | 21 | 0.976 |
| contradiction_notice | 10 | 1.000 |
| contradiction_explain | 10 | 1.000 |
| all | 286 | 0.984 |

## Items scored 0, 0.5 or misread

| Pic | Id | Target | Score | What the describer said |
|---|---|---|---|---|
| pic_05 | i11 | There is a tree | 0 | no tree mentioned anywhere (fence, house, flower bed, pots only) |
| pic_07 | i11 | There are a few white clouds | 0 | clouds not mentioned (sunny street, bird in sky only) |
| pic_08 | i20 | There are a few white clouds | 0 | clouds not mentioned; scenery list has no sky items |
| pic_12 | i12 | There are a few white clouds | 0 | clouds not mentioned |
| pic_17 | i09 | The girl let go of one of the balloons | 0.5 | balloon "floating away"; unsure: "may have slipped from the girl ... or may belong to no one" (two readings) |

No item was scored "misread".

## Unintended oddities

Grouped by kind:

- Scene logic / timing (1): pic_19, watering the garden just before a storm could be read as the odd thing.

About animals, by angle: none. No describer reported an animal as looking wrong; all animal remarks were hedges on behaviour (e.g. cat crouching vs stalking, white bird duck vs goose), not oddities.

All other pictures: describers reported nothing as looking wrong beyond the scored contradictions (most said "nothing looks impossible or floating").
