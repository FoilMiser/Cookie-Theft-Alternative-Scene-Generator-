# v0.29 isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (the method of `isolation_v023.md`). Round 1 was thirteen readers and 36 cut-outs, up to three to a reader, no reader seeing two versions of one thing (`isolation_v029/round1`; `map.json` says which cut-out is which case). Round 2 was five readers on 14 cut-outs, and round 3 three readers on six. The variants are behind `SLEEP29`, `TRIP29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29` and `FISH29` in `scenegen/templates.py`, `SHADOW29` in `scenegen/library.py` and `TPDB_FOOT` in the cast; `vision/isolation_bench.py` has the cases. Two or three cut-outs a side is a small sample, and this file says where a choice rests on little.

## The sleeping dog (`SLEEP29`, `library.SHADOW29`)

v0.28's one reading under the gate that was on a drawing it had touched: not the dog but its shadow, which had gone from a wide oval to a narrow one. So the wider shadow was tried on the old pose, against two new poses with the chin on both paws, the elbows drawn in.

| Case | Drawing | What the readers said |
|---|---|---|
| `slpO_1`, `_2` | As it was | "So it seems to be sniffing the grass or dozing"; "it could be lying down asleep, or it could be crouching or sniffing the ground with its head down" |
| `slpW_1`, `_2` | **W**: the old pose, a wider shadow further under it | "As if it is asleep or sniffing the grass"; "lying curled up on green grass, with its eyes closed as if asleep" |
| `slpB_1`, `_2` | **B**: chin on both paws, facing out | "It could be lying down asleep, sitting and looking down, sniffing the ground, or begging with its paws together"; "or perhaps bowing its head low" |
| `slpC_1`, `_2` | **C**: the same, turned three-quarters, the head toward the viewer | "With its eyes closed; it appears to be asleep"; "its head resting low on its front paws, so it appears to be asleep". Once "unwell or collapsed", once "sad or sulking", each with sleep the likelier |

**Chosen: C.** The first drawing in which both readers said asleep before anything else. B hid the body behind the head, which is what had let v0.28's readers wonder. The wider shadow did a little, and is not needed. The cast keeps `sleep_ball`; v0.13 turned from a stretched-out sleeper because it read as collapsed, so the whole scenes had to say whether C brings that back.

## The duck (`DUCK29`)

Three half marks in v0.28 were all on one inference: "swimming towards those crumbs". The list's fix was to draw the eating.

| Case | Drawing | What the readers said |
|---|---|---|
| `fedO_1` | As it was: upright, crumbs ahead | "Floats on the pond, facing left towards her". Feeding is the woman's, not the duck's |
| `fedK_1` to `_3` | **K**: neck down along the breast, tail up, the bill at a crumb | "Pecking at a line of small pale oval pieces". Three of three also: "lying on its side or collapsed", "tipped over", "as lying on its side" |
| `fedE_1`, `_2` | **E**: round 2, neck straight out, body as it was | "Pecking at them", but still "as if it is tipping over" and "a duck that has toppled over" |
| `fedL_1`, `_2` | **L**: round 2, the neck arched and the head bent down over a crumb | "With its head lowered towards a small round pale piece, surrounded by more of these pieces, which look like bread or crumbs he is feeding it"; "so it could be eating or dipping its beak" |

**Chosen: L.** It keeps the head above the body, and nobody has the duck falling over. It is drawn as about to eat more than eating, which is what the key's inference asks.

## The trip's obstacle (`TRIP29`)

The weakest meaning that passes, and falling for two releases. The obstacle has been on the line of the stride since v0.15, and readers still put it to one side. Three ideas: nearer the viewer, in case the three-quarter body seems to head that way; and two things too wide to walk past, a box lying across the line and a plank.

| Case | Drawing | What the readers said |
|---|---|---|
| `trpO_3`, `_4` | As it was, a bucket | "He could be about to walk into it because he is reading, or it could just be sitting nearby and clear of him"; "or the bucket may just be sitting nearby" |
| `trpL_3`, `_4` | **L**: a bucket a little nearer the viewer | "May be about to walk into or trip over the bucket", then "will pass it"; the other reader did not mention tripping |
| `trpP_3`, `_4` | **P**: a plank across the line | "A flat wooden plank or board stands at a lean, on its narrow end". **Out** |
| `trpW_3`, `_4` | **W**: a long low box across the line | "Just ahead of them, in their path"; but "a little skewed" and "well away from his path" |
| `trpX_1` to `_3` | **X**: round 2, wider and straighter on, nearer | All three say it: "may be about to bump into or trip over it", "directly in their walking direction", "roughly on his path". All three on its perspective: "seems skewed" |
| `trpY_1` to `_3` | **Y**: round 3, its top less steep | "Directly ahead of him ... so he seems about to walk into it"; "as though he might trip over it"; "may be about to walk into it". All three still allow the other reading: "could be read two ways" |

**Chosen: Y.** Six of six on the last two drawings name the walk into it, against three of four on the bucket. Every reader of the bucket who named it also gave the bucket a way out, and so do all three on Y, so what the box buys is the first reading, not the only one. The box is 72 by 38 units, its top 40 deep, and it stands 30 to 52 units from the leading toe. With a floating, carried or soaked box in the picture it falls back to the bucket. So every picture without one of those has the same obstacle, where v0.28 had a bucket, a ball or a box. A ball was not read here.

## The dog at the door (`DOOR29`)

Listed as "watch", and it fails the gate, on one reader who wrote only "sits with a red lead in its mouth". Tried because it is cheap: beside the door and turned toward it, not in front of it and facing out.

| Case | Drawing | What the readers said |
|---|---|---|
| `wanO_1` | As it was | "It holds a red leash in its mouth", and "as if asking for a walk" only in passing, as one of two readings of the lead |
| `wanB_1`, `_2` | **B**: beside the door, turned to it | "The dog seems to be waiting by the door with its own leash, as if asking to go for a walk"; "waiting at the door with its leash". But "a tangle of thin shapes" behind, and the lead "more like a rigid pole" |
| `wanC_1`, `_2` | **C**: round 2, the tail curled in, the lead hanging and then along the ground | "It seems to be waiting to go for a walk, or asking to"; "as if asking to go for a walk". Still "overlapping shapes" at the rear |
| `wanD_1` | **D**: round 3, the hind paws drawn in too | "The dog seems to be waiting at the door, as if asking to go for a walk". The tail "in several folded or overlapping lobes" |

**Chosen: D.** Every reader of a dog beside the door gave the wish in the first paragraph. One cut-out is a small test of the last change, which is to the rear only.

## The hose in hand (`HOSE29`)

"Like a rigid pipe", "with no slack" in v0.28, and every earlier curve has had a name of its own.

| Case | Drawing | What the readers said |
|---|---|---|
| `hosO_1` | As it was | "The hose appears to stand stiffly upright in the air rather than hanging" |
| `hosK_1`, `_2` | Waves on the ground, a slight rise | "A stiff, near-vertical section"; "a stiff, nearly straight segment" |
| `hosS_1` to `_3` | Bowed toward the body, thinner | "Looks broken up"; "hidden by or merged with his shirt"; still once "a rigid pipe" |
| `hosT_1`, `_2` | Bowed out in front | No "stiff" or "rigid". But "a short thick teal section stands upright just below his hand ... and appears to stop or have a gap before the longer hose continues", and "looks slightly cut off" |

Those last two are a fault looked for and found: the hose in the fist is part of the figure, and met the hose on the ground end to end. **Chosen: T, with a short piece over the joint**, in front of the figure, and the old thickness to match. The joint was not read on the bench, only in the whole scenes.

## The stopped hose's swelling (`BULGE29`)

"A separate slug-shaped object", "a dark flattened blob". **Chosen: slimmer (14.5 to 10.5 units), with no highlight.** As it was: "a fat swollen bulge", "or as a separate object lying on the hose". Slimmer (`blkB_1`, `_2`): "a bulge of water backed up because the goat is standing on the hose and pinching it", "the dog appears to be standing on the hose, which could be the reason only one drop is coming out". Once "a puddle-like blob". The reason for the dry nozzle survives, which was the risk.

## The fish (`FISH29`)

"Pasted onto the leaves" in v0.28. As it was (`fshO_1`): "It does not sit on a branch, so it appears to float against the crown". On a limb from the trunk's fork (`fshB_1`): "at the end of a brown branch". Close to the trunk the limb hid (`fshB_2`): "it overlaps the tree trunk and the branch with no visible connection". So the fish now takes the slot furthest from the trunk (`fshC_1`, `_2`): "lying at the end of a branch", "stuck in or balanced on the end of the branch". **Chosen: on a limb, well out.** All five readers still call the fish the strange thing, and all five offer something else it might be: a fruit, an ornament, a decoration. The one reader of the old drawing did too, so the limb neither caused that nor cured it.

## The lifted heel (`TPDB_FOOT`)

"Looks turned up", on v0.27's heel. Lifted less (C) against as it is (`heeO`, `heeC`, two cut-outs each): "the right foot points up and to the right" against "his back foot is raised with the sole showing". **Kept as it is.** Nothing to choose between them, and the change would have re-rendered every walker.
