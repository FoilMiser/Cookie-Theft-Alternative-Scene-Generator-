# The v0.15 isolation bench: the body, the leftover assets and each weak visual, refined on its own

v0.15 began with two things seen in the v0.14 site's gallery: gaps in some characters' anatomy in certain poses (a girl in
a dress kicking, her leg floating free below the hem), and drawings that refined poses had replaced still sitting in the
cast and the gallery (the thin "giant fork" of v0.6 and v0.7 beside the dinner fork that replaced it). Then come the one
template the v0.14 screen failed (`wave`) and the oddities its readers reported (`flaws_v014.md`).

## The body: a check for parts that come apart

`assets/cast/gapcheck.py` loads each family's `.blend`, puts it in every pose, splits the visible body
meshes into mesh islands and joins two islands when their surfaces touch or cross or one lies inside the other. A pose
whose body falls into more than one group is reported with the part that floats free and how far it is from the rest.
Over the v0.14 cast (18 families, every pose):

| Part that came apart | Poses (gap of 4 mm or more) | Worst | Cause | v0.15 |
|---|---|---|---|---|
| A bare leg under a skirt or dress | 70 (of three characters) | 170 mm (sitting on the ground) | The leg began a hand above the knee; the skirt hangs from the hips and cannot follow a thigh that comes forward | A lobe of the skirt's cloth over each thigh, from the hip joint past the top of the bare leg, turning with the thigh and tapering onto it; standing, both lie inside the skirt, which looks as before; no line drawn where a lobe passes into the skirt |
| A foot below a bare leg | most poses (a few mm) | 7 mm | The leg ended above the ankle | Every bare leg runs down to the ankle joint, inside the shoe |
| A cardigan's placket and buttons, a hoodie's strings and pocket, a hi-vis vest's bands | 22 | 290 mm (a placket in front of a woman hanging washing) | Parented rigidly to one bone while the cloth under them bent with the chest and arms | Bound to the surface they sit on: each vertex takes the bone weights of the nearest point of the shirt or vest (torso bones only, so nothing is dragged up with a raised arm) |
| A spot on the white dog | 4 | 32 mm (sitting up) | As above | Bound to the coat in the same way |

After the change no pose leaves a leg, foot or decoration apart (the remaining reports are a cap's dome above the head, the
inside of a skirt, and a neck seam of 4 to 5 mm under the outline when both arms are raised). Rendered, the sitting and
kicking poses of the three characters in skirts and dresses show the cloth over the thigh and the leg joined to it.

## Leftover assets

Every template's casting was sampled (`scenegen/reach.py`: each template's bind run many times in every setting and sky it
allows, half the time with part of the cast already taken by other events), and every cast pose checked against earlier
releases' pictures. Twelve person actions and seven animal poses that a refined drawing had replaced, and that no template
asks for any more, leave the cast and the gallery:

| Retired | Replaced by |
|---|---|
| `sweep_fork` (v0.6), `sweep_dinner_fork` (v0.7) | `sweep_giant_fork` |
| `kick` | `kick_low` |
| `jump` | `jump_tuck` |
| `dig` | `dig_lift` |
| `walk_read` | `walk_read_open` |
| `hold_cone` | `cone_dropped` |
| `sit_apple` | `sit_ice_cream` (the apple read as a cherry) |
| `cheer`, `crouch` | the slide child sliding down; the poses of the events that once used them |
| cat `stalk`, `crouch` | `stalk_paw` |
| cat `sleep`, `sleep_curl`, dog `sleep`, `lie` | `sleep_tuck`, `sleep_ball` |
| dog `look_up`, `sit_look_down` | `beg` |

Two seesaw poses first marked as replaced stay: a teenager and a child riding the seesaw together (`seesaw_low`,
`seesaw_stuck`) still use them when both children are busy elsewhere, which the first sampling (a fresh cast every time)
missed and a bench picture caught. Twenty-seven actions that no template has ever used stay in the cast for later
templates, and out of the gallery.

## Round 1 (27 images)

| Image | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_25`, `iso_01` (a girl in a dress on the garden swing) | The legs joined to the dress | "A pink top and pink shorts ... sits on a swing"; no remark on her legs. But "her hands stick out wider than where the chains appear to be ... arms could also be read as stretched straight out" | The hands hold the ropes at chest height, elbows down by the sides |
| `iso_02`, `iso_14`, `iso_23`, `iso_21`, `iso_27` (dress: on a bench, on a picnic blanket, in the sandbox, stuck on the seesaw, on the slide) | The legs joined to the dress | No leg read as detached; "the leg pose looks a little stiff or oddly joined at the knees under the puffy skirt" (bench) | None needed |
| `iso_08` (a woman in a skirt walking with an ice cream) | The skirt over a stride | "Her legs appear to cross each other in an X shape below the skirt"; "a darker blue blob near its lower part, which could be a pocket, a fold, or a stain" | The lobes flatter at the back and with no line where they pass into the skirt |
| `iso_20` (cardigan, hanging washing) | The placket bound to the cardigan | "A teal long-sleeved top, a grey-blue knee-length skirt"; no remark on the placket | None needed |
| `iso_26`, `iso_09`, `iso_22` (sweeping, raking, the giant fork) | The open-eyed face on chores | "She looks down at what she is sweeping"; no reader saw closed eyes | None needed |
| `iso_05`, `iso_11`, `iso_12` (reading while walking toward a bucket) | The bucket on the line of the leading foot | "A red bucket ... on the grass in front of her"; "a blue bucket ... in front of her"; "ahead of her and slightly to the right, roughly in her path" | None needed |
| `iso_17`, `iso_06` (a bird on a branch) | A short branch under the bird | "Perches on a short brown branch"; but "the branch floats inside the canopy ... it looks pasted onto the green leaf mass", "a small upward stub ... runs up into the bird's feet" | The branch comes out from under a cluster of leaves, like the ball caught in a tree; no stub |
| `iso_19` (garden bird table) | Standing on the lawn in front of the fence | "A thin wooden pole stands in the grass with a small box on top"; "could be a birdhouse or bird feeder, or ... a garden lamp or lantern" | A round entrance hole and a perch peg |
| `iso_18` (bush by the garden fence) | In front of the fence | "A rounded green bush in front of it on a strip of grass" | None needed |
| `iso_04`, `iso_10` (sprinkler, garden and park) | The hose clear of the path | "A dark green garden hose runs up from the bottom edge"; "connected to a dark blue hose (running off the right edge)" | None needed |
| `iso_03` (a cat asleep in the street) | At the foot of the shopfronts | "A small orange cat in the middle of the tiled pavement" | No sleeping cat or dog in the street (kept near the front so it reads, it lies on the open pavement) |
| `iso_07` (a kite in a garden with washing) | The washing lifted by the breeze | No remark on the washing | None needed |
| `iso_13`, `iso_16`, `iso_24` (a child waving) | Facing us, arcs either side | "Small curved motion lines on both sides of the hand suggest it is waving" (all three; second readings "to get attention", "cheering") | None needed |
| `iso_15` (a wave beside a stopped hose) | Waving at the man carrying a box, not at the man with the dry nozzle | "A small child ... waves one raised hand; small motion lines next to the hand show the waving" | None needed |

## Round 2 (9 images)

| Image | What was being tested | What the reader said |
|---|---|---|
| `iso_06`, `iso_08` (the swing) | The grip at chest height | "Holding the two thin swing ropes ... with both hands"; "she holds the two swing ropes at chest height". One: "I could not clearly see them continue from her hands down to the seat, so the seat can look unattached" (the ropes now run from the hands to the ends of the seat, outside the hips) |
| `iso_03`, `iso_04` (a bird on a branch) | The branch from under the leaves | "Perched on a short brown branch that sticks out of the canopy"; "stands on a short brown branch sticking out of the right side of the canopy ... its base hidden by a small cluster of leaves" |
| `iso_07` (the bird table) | The entrance hole | "A small birdhouse with a red pointed roof and a dark round entrance hole" |
| `iso_01` (walking with an ice cream, three-quarter view) | The skirt over a stride | No blob on the skirt. The legs still "crossed in a scissor shape": the walking events (an ice cream, a balloon) now walk side on |
| `iso_05`, `iso_02`, `iso_09` (dress: bench, picnic, slide) | The legs and the dress | No detached leg; "the legs look slightly stiff and stick-like". The slide child's raised arm against her head is unclear (as noted in v0.14; the slide passes the gate) |

## What went into the library and the generator

| Visual | v0.14 | v0.15 |
|---|---|---|
| Skirts and dresses | A bell from the hips; the bare leg began a hand above the knee | The bell plus a lobe of cloth over each thigh, tapering onto the bare leg |
| Bare legs | Ended above the ankle | Run to the ankle joint, inside the shoe |
| Placket, buttons, hood strings, pocket, vest bands, coat spots | Parented to one bone | Bound to the surface under them |
| Swing grip | Hands by the shoulders, arms out | Hands at chest height, elbows down; the ropes on to the seat's ends |
| Chore faces | "Focused", half-lidded | The plain face, eyes open, for every pose that bows the head over a task |
| Bird on a branch | On the leaves | On a short branch out from under a cluster of leaves |
| Garden bird table | Its post behind the fence | On the lawn, with an entrance hole |
| Garden bushes | Just behind the fence's foot | In front of the fence |
| Garden swing frame | Its right legs on the path | 55 px further from the path |
| Sprinkler hose | Off the nearer side, across a path if one lay there | Never across a path: off the bottom instead, or the sprinkler goes elsewhere |
| Sleeping cats and dogs | Anywhere | Not in the street |
| Walking with an ice cream or a balloon | Three-quarter view | Side on |
