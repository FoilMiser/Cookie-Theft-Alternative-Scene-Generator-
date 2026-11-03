# v0.25 isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (the method of `isolation_v023.md`). Round 1 was six readers and eighteen cut-outs, three to a reader, no reader seeing two versions of one thing (`isolation_v025/round1`); round 2 one reader and two cut-outs (`isolation_v025/round2`). Each `map.json` says which cut-out is which case; the cases are `bag*`, `rol*`, `bar*`, `paw*` and `bir*` in `isolation_bench.py`. With one or two readings per candidate these are choices between drawings, not measurements; the whole scenes (`design_tests_v025.md`) read the winners again. There were no controls this time: the v0.24 screen had just read the old drawings.

The bench casts were built with `TPDB_BAG` and `TPDB_ROLLER`; the rest are `draw.BARROW_SHADOW25`, `draw.BIRD25` and `draw.PAW25`.

## The shopping bag (the v0.24 gate failure)

`carry_bag` scored 0.75 in v0.24: "carrying something yellow", "very long and thin for a shopping bag, could be a tag, folded paper". The cause was in the drawing: the bag was wide across the body and thin front to back, so a walker in profile showed only its narrow edge.

| Case | Drawing | What the readers said |
|---|---|---|
| `bagA_1`, `bagA_2` | **A**: the broad face along the walker's line, as tall as it is wide, dark handles rising to the hand | "A plain yellow shopping bag with dark handles", twice; "could be a shopping bag or a gift bag" |
| `bagB_1`, `bagB_2` | B: the same, wider and shorter | "A plain yellow rectangular bag", "could be a shopping bag or a briefcase/tote"; "a plain yellow shopping bag", "more like a box than soft bag material" |

**Chosen: A.**

## The paint roller

In v0.24 the roller "hardly seems to touch the fence", a "small pale oval". Its axis ran along the line of sight, so a profile showed only its round end.

| Case | Drawing | What the readers said |
|---|---|---|
| `rolA_1`, `rolA_2` | **A**: upright, its side to the viewer, a T on the end of the pole | "A long-handled paint roller up against the fence", twice; "very tall and narrow", and it "partly blends in" with the paint |
| `rolB_1`, `rolB_2` | B: longer and fatter | "Press it against the fence"; "a long-handled paint roller or wide brush" |

**Chosen: A.** No reader said it missed the fence.

## The wheelbarrow's shadow

"A large dark oval extending well beyond it", four v0.24 probes; it was 210 px wide.

| Case | Width | What the readers said |
|---|---|---|
| `barA_1` | **130 px** | "A soft dark shadow beneath it" |
| `barB_1` | 160 px | "A wide oval ... the barrow looks slightly lifted or hovering over the shadow" |

**Chosen: 130 px.** Both readers found the barrow's frame confusing ("loosely stacked, disconnected parts", "parts join oddly"), which is not what was tested: on the list for v0.26.

## The bird at the sandwich

"About as big as the sandwich", "a blue kettle or jug".

| Case | Size | What the readers said |
|---|---|---|
| `birA_1`, `birA_2` | **0.8** | "A blue bird ... at or pecking the sandwich"; "a blue bird ... as if pecking at or stealing it", once also "a blue cloth, a bag or a hat" |
| `birB_1`, `birB_2` | 0.68 | "A blue bird ... perhaps pecking at or stealing"; "a small blue bird ... hard to read ... a glove or a bag" |

**Chosen: 0.8.** Smaller loses the bird. One reader also found the sandwich "very large compared with the man and the bird", overlapping his thigh, so it went down with the bird, from 0.8 to 0.72 of its drawn size; this was not read on the bench.

## The newspaper dog's paws

"White gloved hands", three v0.24 pictures. They were ovals drawn over the paper, white since v0.12 (dark ones "read as hands").

| Case | Drawing | What the readers said |
|---|---|---|
| `pawA_1`, `pawA_2` | A: ovals in the dog's own colour, no toes | "Separate brown ovals stuck onto the edge of the newspaper"; "separate white ovals ... somewhat detached from the arms" |
| `pawB_1`, `pawB_2` | B: in its own colour, with toes | "Stuck to the surface of the paper rather than gripping its edges"; "rounded white blobs with dark lines stuck onto the edge" |
| `pawC_1`, `pawC_2` (round 2) | **C**: no ovals, the paper drawn behind the dog, its own paws resting on it | "Holds an open newspaper in front of itself with a white paw, as if reading it", twice |

**Chosen: C**, as neither A nor B stopped the paws looking stuck on, and the cause was the separate ovals. The C reader saw "only one paw clearly touches it", as the far paw hid behind the near one in profile, so the paws now sit at different heights. That last adjustment was not read on the bench; the whole scenes read it first.
