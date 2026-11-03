# v0.26 isolation bench

Each visual was forced alone into a picture, cut out with little else around it and read blind by fresh readers (the method of `isolation_v023.md`). Round 1 was nine readers and 26 cut-outs, up to three to a reader, no reader seeing two versions of one thing (`isolation_v026/round1`); round 2 was six readers and ten cut-outs (`isolation_v026/round2`). Each `map.json` says which cut-out is which case. The variants are behind `TPDB_OLD`, `TPDB_TEEN`, `TPDB_READDOG`, `TPDB_RDTAIL`, `TPDB_FEED`, `TPDB_BROOM`, `TPDB_BODY` and `draw.SWEEP26`; `vision/isolation_bench.py` has the cases.

The list came from the v0.25 list and from sorting all 428 of the v0.25 readers' remarks by what they were about, which is what added the cap, the feed bag and the sandcastle. Looking at the first crops before giving them to readers also found the newspaper's "dark square": the photo block on the page kept its outline at any fill.

## The older man's head (`TPDB_OLD`)

The v0.25 screen's most repeated remark, in ten of his 21 pictures: "the older man's face is hard to read", a cap peak on one side, grey hair on the other, "something like an ear in the middle", "no clear eyes".

| Case | Drawing | What the readers said |
|---|---|---|
| `oldA_1`, `oldA_2` | **A**: no cap, bald with the white fringe | "A patch of grey hair at the back of his head", which "could also be taken as a patch or a cap piece stuck onto the head", "a strap or bandage". "There is no visible face." The ear still "sits in the middle" |
| `oldB_1`, `oldB_2` | **B**: no cap, short white hair | "An older man with grey hair and a moustache". But "the face is hard to read", and the hair "a smooth grey cap or hat" |
| `oldC_1`, `oldC_2` | **C**: the cap kept, a shorter peak tipped up, short white hair under it | "An older man with grey hair and a moustache, wearing a blue-grey cap"; "an older man with grey hair and a blue-grey flat cap". Nothing about his head beyond a small mouth at the edge of the profile |

**Chosen: C.** Looking at the crops, B seemed best, and the reading went the other way. C has no patch for the eye to puzzle over, as the hair runs round under the cap, and it needs no change where a template depends on his cap.

## The newspaper dog's head and tail (`TPDB_READDOG`, `TPDB_RDTAIL`)

In v0.25 the head bent over the paper showed its round back and an ear: "a monkey, an otter, or a person in a costume", "a person in a spacesuit or a small robot".

| Case | Drawing | What the readers said |
|---|---|---|
| `rdgA_1`, `rdgA_2` | **A**: the head up, in profile | "A tan-and-orange dog ... appears to be reading", but "could also be taken for another animal such as a weasel or an otter"; a white "cartoon dog" |
| `rdgB_1`, `rdgB_2` | **B**: the head up and turned a little to the viewer | "A brown-and-tan cartoon dog"; "a white cartoon dog"; both "as if reading". No animal but a dog. But "the rear end spreads out into a flat, pointed shape on the ground that could be the tail or a haunch" |
| `rdgC_1`, `rdgC_2` (round 2) | **B and the tail up behind** | "A tan-brown cartoon dog ... sitting upright", "as if reading it like a person would". No flat shape. Still "very long and thin", and on the white dog the limbs "run together" |

**Chosen: B with the tail up.**

## The teenager's cap (`TPDB_TEEN`)

The cap worn backwards (v0.24) made him a boy, but seven v0.25 pictures remarked that its peak points away from his face, twice "the head on the wrong way round".

| Case | Drawing | What the readers said |
|---|---|---|
| `teeC_1`, `teeC_2` | **C**: a red beanie | "Probably a boy or young man", "a red woolly hat"; "a person"; the face "partly hidden by hair and the hat" |
| `teeD_1`, `teeD_2` | **D**: the cap worn forwards | "A cartoon boy or young man", "a red baseball cap (brim pointing left)"; "a young person ... and a red baseball cap". One peak that "appears to stick out oddly, flat and to the side" |

**Chosen: D.** No reader had his head on the wrong way round in either; D named him more firmly.

## What the sweeper has swept (`draw.SWEEP26`) and the broom (`TPDB_BROOM`)

All four v0.25 pictures of `sweep` remarked that there was nothing to sweep, and one reader said he "could be sweeping, or pausing to watch" (0.875, a gate failure).

| Case | Drawing | What the readers said |
|---|---|---|
| `swpA_1`, `swpA_2` | **A**: a heap of leaves at the broom's head | "She appears to be sweeping up leaves"; "he is sweeping a pile of autumn leaves" |
| `swpB_1`, `swpB_2` | **B**: a heap of dust and grit | "Sweeping or pushing the pile into a dustpan-like shape"; "sweeping ... a small grey speckled pile of dirt or gravel", also "a small rock or mound" |

**Chosen: A.** But all four cut-outs had the broom's head, a plain yellow wedge, as "a dustpan or scraper", with "no visible bristles". So round 2 tried a fan of seven outlined bristles, its flat face to the viewer:

| Case | Drawing | What the readers said |
|---|---|---|
| `swpC_1`, `swpC_2` (round 2) | The fan, with the leaves | "A yellow bristle head"; "a long wooden broom", "the yellow bristles rest on the ground". One "broom or rake", which "look more like a broom" |

**Chosen: the fan.** No reader said dustpan or scraper.

## The dog at the door (`dog_wants_walk`)

The gate's lowest in v0.25 (0.833): "with its eyes shut", its wish never stated. The template chose the happy or the neutral face, and the happy one closes its eyes.

| Case | Drawing | What the readers said |
|---|---|---|
| `wanN_1`, `wanN_2` | The neutral face only | "As if waiting to go for a walk"; "as if the dog is asking to go for a walk". Both also wondered about "a long tongue", and both said the loop on the grass favours a lead |

**Chosen: the neutral face.** Both readers stated the inference unprompted.

## What the bird feeder holds (`TPDB_FEED`)

In six v0.25 pictures, "a paper bag, a cup or a carton".

| Case | Drawing | What the readers said |
|---|---|---|
| `fedA_1`, `fedA_2` | **A**: a slice of bread | "A pale paper bag or packet", "a book/papers"; "a couple of sheets of paper" |
| `fedB_1`, `fedB_2` | **B**: a brown paper bag | "A brown paper bag ... apparently feeding a white duck"; "a tan cardboard box or paper bag" |

**Chosen: B.** The crumbs at the pond are now bread-coloured, and were read as "bread or feed". In these crops the bearded man's head, bowed low to the birds, was "a dark, rounded shape ... rather like a mask or helmet". Bowing it less cannot be done on its own: a rule from revision 5 needs the head within 40 degrees of the bird, as a level head seemed to face whatever was behind the birds. It stays, on the list for v0.27.

## The sandcastle

"Very straight, boxy edges ... a cardboard or wooden model" (three v0.25 pictures).

| Case | Drawing | What the readers said |
|---|---|---|
| `casA_1`, `casA_2` | Heaped sand with bucket-shaped towers | "A sandcastle with three towers and a small red flag"; "a sandcastle made of three rounded towers on a mound". Both said its base "seems to overlap" the sandbox's front frame |

**Chosen: the heaped castle.** The overlap went to placement: the child and the castle now stay back from the front rim.

## Fuller bodies (`TPDB_BODY`): tried and left

Nearly every cut-out of round 1 remarked on narrow figures, "the torso is extremely thin from the side", "very long, thin legs". Round 2 tried every person 22% deeper with limbs 12% thicker, against the same scenes as they are.

| Cases | Drawing | What the readers said |
|---|---|---|
| `bodO_1`, `bodO_2`, `bodO_3` | As they are | "The torso looks very thin from the side"; "very long, thin and pressed close together ... stiff and narrow from the side"; "very long, thin legs and a small torso" |
| `bodA_1`, `bodA_2`, `bodA_3` | Fuller | "The torso reads a little flat"; "long and narrow ... a little stiff"; "very tall and thin" |

**Left as they are.** At this size of change the readers' words did not move, and it would have meant rendering the whole library again. A real change to these figures' proportions is a larger job than one bench round.
