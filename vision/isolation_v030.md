# v0.30 isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (the method of `isolation_v023.md`). Round 1 was nine readers and 25 cut-outs, up to three to a reader, no reader seeing two versions of one thing (`isolation_v030/round1`; `map.json` says which cut-out is which case). Round 2 was three readers on eight. The variants are behind `HOSE30`, `FISH30`, `TRIP_W30` and `CRUMB30` in `scenegen/templates.py` and `REEL30` in `scenegen/settings.py`; `vision/isolation_bench.py` has the cases. The cast did not change. Two or three cut-outs a side is a small sample, and this file says where a choice rests on little.

Looking at the first crops stopped three things before any reader saw them: the bench's flags had left the old obstacle and the old duck on the new cases, the nozzle was too small to be anything but outline, and the hose ran up to its `hose_in` anchor, which is the low end of the stub the figure holds, not the fist.

## The hose at the fist (`HOSE30`)

v0.29's one new fault: "seems to stop at about waist height, then the part at her hands starts again". A crop showed why: a square piece over the joint, wider than the fist's stub.

| Case | Drawing | What the readers said |
|---|---|---|
| `hosO_5`, `_6` | As it was | "Ending in a squared-off shape by her hip", "a separate handle or post"; "more like a rigid pipe or stand" |
| `hosU_1` to `_3` | **U**: the hose itself runs on in front of the figure, up to the fist | No square end and no gap. "Stands stiffly upright by itself"; "a stiff vertical section"; "it is hard to see how it joins the nozzle" |
| `hosV_1` to `_3` | **V**: round 2, that, and hanging from the fist as a rope hangs, steep there and flattening as it reaches the ground | No square end and no gap. "A little stiff, as though it is standing up on its own"; "a stiff loop near the hand"; "a stiff curve from the ground to her hands" |

**Chosen: V.** The fault is gone from both. "Stiff", or standing up on its own, is not, in six of six, and has now been said of every way of drawing it since v0.25. A hose held at the waist has to rise, so this release stops there. V is chosen over U on little: U's S-bend had the hose "over the rim of the soil bed" twice, and V's once, "in front of the flower bed edge". The fist's stub is in the cast, and the hose now covers it.

## The fish's limb (`FISH30`)

"Drawn on top of the leafy crown", "a little pasted in", and the tuft at the fork's other arm "looks detached from the rest of the crown". Drawing the arm short, and leaves over the limb's middle, were stopped by eye: each looked like a sapling inside the crown.

| Case | Drawing | What the readers said |
|---|---|---|
| `fshO_3`, `_4` | As it was | "A small, separate darker-green leaf clump, which looks slightly stuck on"; "it looks pasted on top of the crown" |
| `fshG_3`, `_4` | **G**: and the leaves the ball's crown has | "Look like bushes floating in the foliage"; "more like a perch or a bent pipe"; "ends in a blunt, cut-off shape" |
| `fshE_3`, `_4` | **E**: no other arm | "Almost looks like it is growing out of the end of the branch"; "drawn on top of the crown ... which looks slightly pasted-on" |
| `fshF_3` to `_5` | **F**: round 2, that, and running on past the fish, so the fish lies on it | "Lies on a bare brown tree branch", but "may be hovering just above", "floating just above", "floating in the air just above", and three of three on its end: "a blunt stub", "bare wood at its end", "a blunt, bare stub" |

**Chosen: E.** The fewest things named, and nothing new added. F took away "growing out of" and gave a floating fish and a stub. All nine cut-outs have the fish as the strange thing, so the contradiction was never at risk. All nine also offer something else it might be, a fruit, a toy, an ornament or a bird, as in v0.29. The ball's limb and the bird's were not changed: readers remarked little on them.

## The trip's box (`TRIP_W30`)

v0.29 read its long box only in street pictures, and its tier-4 searches fail on it most. So the box as it is (`trpA`, 72 units across) against a narrower one (`trpN`, 60), in the three settings it had not been read in: a garden path, a playground and a park.

| | **72 units** | **60 units** |
|---|---|---|
| Garden path | "So he seems about to walk into it or trip over it because he is looking at the book" | "So he looks about to walk into it without noticing" |
| Playground | "So she seems to be walking towards it". Below: "a parcel that was left there or just a trip hazard" | Only below: "an obstacle she is about to walk into", or "simply sitting there as background" |
| Park | "His path appears to lead toward the box". Below: "something he is about to trip over", or "an object sitting nearby" | Only below: "directly in his walking path", "something he is about to trip over", or "a box left on the ground beside him" |

**Kept at 72.** It reads outside the street, which is what this was for. 60 reads a little less firmly in two of three, on one cut-out each. Tier-3 and forced tier-4 pictures place in full at either width, so the width does nothing there (see below).

## The crumbs (`CRUMB30`)

"Several crumbs lie on the grass past the pond edge". As it was (`fedO_3`, `_4`): "some lie on the grass, well away from the water", "several of the ovals lie on the grass below the pond edge". Only those on the water, clear of its edge (`fedW_1` to `_3`): "floating on the water", "float on the water", "appear to sit on the water". **Chosen.** One crumb sits apart from the rest, and each of the three says so without minding it. Three of five, on both drawings, find the duck's body "a little" tipped, or "lying awkwardly", each reading it as a duck at food. Not changed, and to watch.

## The reel (`REEL30`)

"Only a short stub of hose joined to nothing". As it was (`relO_1`): "stops abruptly in a rounded end with no nozzle and does not lead anywhere, so it looks cut off". A nozzle on the stub (`relB_1`, `_2`): "ends in a yellow, pointed nozzle lying on the grass", but "more like a stub or a hook". A longer end, lying on the grass (`relC_1`, `_2`): "ends in a yellow pointed nozzle lying on the ground", "looks left lying on the grass". **Chosen: the longer end.** Both also offer "a pencil tip". It goes when somebody has the hose, as a second stub by the reel was remarked on in v0.29, and that is read only in the whole scenes.

## Not tried

The reading dog as "a bit like a kangaroo" was one reader in two pictures, and it has been to the bench twice (v0.11, v0.26). Left, as the list said, unless it comes again.
