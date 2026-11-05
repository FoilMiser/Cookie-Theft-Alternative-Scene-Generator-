# v0.31 isolation bench

Each visual was forced into a picture with little else and cut out, then read blind by fresh readers (the method of `isolation_v023.md`). Round 1 was eleven readers and 32 cut-outs, up to three to a reader, no reader seeing two versions of one thing (`isolation_v031/round1`; `map.json` says which cut-out is which case). Round 2 was eight readers and ten cut-outs (`isolation_v031/round2`).

## The seesaw (`templates.SEESAW31`, `RIDE31`)

On the list since v0.27 as "the larger job". The whole rider was one picture, drawn in front of the plank, with the hips over it: "the man's legs appear to go through or around the plank", and riders "a little above and slightly in front of the plank". v0.24 raised the riders and read that as worse, on one cut-out each, and v0.27 looked at it and left it because a rider cut in two was a larger job.

It turned out not to be large. The renderer now takes a pose name with `~near` or `~far`: the same pose, same frame and same anchors, drawn without the leg further from the camera, or with that leg alone (`render_assets.split_leg`, by the bones' weights in the mesh, since the legs are one mesh). The far leg goes behind the plank and the rest in front. Nothing in the cast changes, and only these two pieces are new renders.

| Case | Drawn | What the readers said |
|---|---|---|
| `ridO_1` to `_4` | **O**: v0.30, the whole figure in front | "Seems to sit slightly beside or in front of the beam rather than squarely on it" (`_1`); "whether his leg passes in front of or through it" (`_3`); "her body looks a bit sunk into the seesaw" (`_4`) |
| `ridS_1` to `_4` | **S**: far leg behind, no rise | "As if he is sitting in the air beside or in front of the low end" (`_1`); "his body overlaps the board" (`_3`); "the thigh seems to come out from below or through the plank's edge" (`_4`). **No better.** The leg was only half of it: the hips still lay over the plank |
| `ridT_2`, `_4` | **T**: children raised 14 units, far leg behind | "Sits on the plank holding on with both hands" (`_2`); "the hips sit on the plank" (`_4`). Still "hard to tell whether the child straddles the plank or sits on its near side" (`_4`). No floating, which v0.24 feared of a raised rider |
| `ridT_1` | **T**: the man raised 14 | "A small dark piece under him may be a handle or seat post". The raise bared the handle's post under his thigh |
| `ridU_1`, `_3` | **U**: the man raised 5 | "He looks like he sits on the beam" (`_3`), and still "hard to tell whether he is astride the seesaw or sitting side-on" (`_1`). The best of the four for him, not cured |
| `ridP_1`, `_2`, `_4` | **P**: riders on a seat on the plank | "Sits on a tan seat" (`_2`), "a small brown seat on each end" (`_4`), and "the children seem to sit a little in front of the beam, not squarely on top of it" (`_2`), "a short brown bar under him" (`_1`). A new thing to explain, and no better |

**Chosen: U.** The children sit on the plank, with the near leg over it and the far leg behind. The man on the low end is better than he was and is not fixed. Every reader had him sitting on the low end, so nothing scored depends on it, and it stays a note.

## The bearded man's vest (`TPDB_VEST`, in the cast)

The crop showed it at once: the shirt came through the vest, so where the two meshes crossed the line was jagged. The vest is now wider than the shirt by enough that it cannot (1.12 and 1.20 of the shirt, for 1.075 and 1.10). A third, wider still, looked bulky and was not read.

| Case | Drawn | What the readers said |
|---|---|---|
| `vstO_1` to `_3` | **O**: v0.30 | "The white shirt looks as if it runs over parts of it, so the layering is a bit hard to read" (`_2`). Nothing on the vest in `_1` and `_3` |
| `vstB_1` to `_3` | **B** | All three read a brown vest or waistcoat over a white shirt, with nothing on how they join |

**Chosen: B.** A family re-rendered, and nothing else.

## The castle and the hand (`templates.CASTLE31`)

| Case | Castle beyond the spade | What the readers said |
|---|---|---|
| `sanO_1`, `_2` | **26** units (v0.30) | "Her hands are mostly hidden behind the sandcastle" (`_1`); "the hands and arms overlap the castle's left tower" (`_2`) |
| `sanM_1` to `_3` | **52** units | All three now see what is in the hand: "a toy spade or trowel" (`_1`), "a small spade or trowel" (`_2`), "a small toy spade or trowel" (`_3`), each with some doubt as it is small. "Her hands blend into the edge of the castle" once (`_3`) |

**Chosen: 52.** The spade had been drawn all along, behind the castle.

## The reel and the bed (`settings.REEL31`)

| Case | Moved | What the readers said |
|---|---|---|
| `relB_3` | not (v0.30) | "The reel overlaps the edge of the flower bed" |
| `relM_1`, `_2` | 24 left | Off the bed, onto the door: "the reel overlaps the step slightly" (`_1`) |
| `relN_1`, `_2` | 16 left, 16 down | Neither says anything about the bed or the step. "The reel sits on open grass" (`_2`) |

**Chosen: 16 and 16.**

## Tried and not taken

**The fish's limb (`LIMB31`).** Narrower where it leaves the trunk, with less bend, so that it would not read as the trunk bending. All three readers of the new one named the join instead: "a sharp step at the top of the trunk, with a small notch at the join" (`fshL_1`), "a sharp junction" (`fshL_2`), "a blunt, notched corner" (`fshL_3`). The old one was "a bit like a bent pipe or a hook" (`fshE_6`). Stays as v0.30. The limb was drawn in v0.29, redrawn in v0.30 and tried again here, with a remark each time and no mark lost, so it comes off the list, as the hose's "stiff" did.

**The cone (`TPDB_CONE`).** The fist lower on a longer cone, to show more of it. Seated, both versions read as a cone (`conO_1`, `conB_1`, `conB_3`). On the walking girl neither did: "There is no visible stick or cone that settles it" (`conO_2`), "I cannot see a clear cone or stick" (`conB_2`). A bench that found nothing to choose between them, so the old one stays and nothing is re-rendered.

## Looked at and left

**The walker's book.** "Seems to float a little ahead of her hands", twice in v0.30. Up close the near hand does hold the book's lower corner, as v0.27's bench chose, and the far hand is behind it. Left.

**The feed bag.** "A small box" on the bench, less in whole pictures, and no mark has depended on it. Left.

## No drawing

**Washing under storm clouds.** `hang_laundry` now asks for a clear sky, as the picnic, the sprinkler and the bucket on the head do. It needed no bench: the one half mark was a fair reading of what the picture showed.
