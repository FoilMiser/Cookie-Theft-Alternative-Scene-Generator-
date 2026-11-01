# The v0.12 isolation bench: each weak visual refined on its own

v0.11 left five templates under the gate and seven oddities (`flaws_v011.md`). For v0.12 each weak visual
was first built on its own, refined, and read blind on its own before it went back into the library and
the scenes. The bench (`isolation_bench.py`, run from the package root) forces one template alone into a picture (no other events)
and crops around that template's own drawing, or around a setting element such as the slide or a parked
bike. Fresh readers who never saw the code or the intent described each crop with the isolation prompt
(below), each crop on its own. The crops and descriptions are in `isolation_v012/round1` to `round9`; `map.json` in each round names the
bench case behind each crop.

The prompt: *"You will see N small cut-outs, each taken from a different cartoon picture ... For each
cut-out, write: What I see (2–5 sentences: who or what is in it, what any person or animal is doing, and
what any object is or seems to be for); Unsure or ambiguous (anything you could not make out or that could
be read two ways, and anything that looks unintentionally strange). Be literal about what you actually
see; don't guess what a test designer intended."*

## Round 1: the first v0.12 drawings (13 crops)

| Crop | What was being tested | What the reader said | What changed |
|---|---|---|---|
| `iso_01`, `iso_04` (kick, park and garden) | The low kick: the foot at a ball on the ground | "She has just kicked the ball, or she is walking or running and the ball is rolling past her foot"; in the garden "just kicked or back-heeled it ... She faces away from the ball" | The ball moved to the toe of the kicking foot, ahead of it; two swing arcs behind the foot |
| `iso_02`, `iso_07` (dig, garden and park) | Lifting a spadeful of earth over the hole | "Digging a hole, either lifting a scoop of dirt out" (both); but the blade "reads more like a flat plate or spatula than a scooped shovel blade", "held above the ground ... could be read as hovering" | The blade lowered (and in round 3 redrawn) |
| `iso_03`, `iso_11` (square wheel, park and garden) | The square wheel on the barrow | "More like a square frame, a crate end or a window than a round wheel"; "a small crate or box stuck to the front of the barrow", "bolted onto the side" | The wheel tucked under the tub's front, the tub drawn over its top, a fork from the tub to the hub with an axle bolt |
| `iso_05`, `iso_08` (play bow, park and playground) | The play bow with a tennis ball at the paws and wag arcs | "A 'play bow' ... curved motion lines beside the tail show it is wagging. Right at its front paws is a yellow-green tennis ball"; "playing with the ball or inviting" | None needed (the stick-like hind leg noted, see below) |
| `iso_06`, `iso_10` (floating box, garden) | The box just above the fence's pickets | "(a) flying through the air ... (b) resting or balanced at an angle on top of the fence" (both) | The box hung well above the fence top, against the trees |
| `iso_09` (feed birds) | Pecking birds at the flying birds' size | "Two small birds ... pecking at the scattered seeds, so she is feeding the birds" | None needed |
| `iso_12` (slide) | The ladder's rails meeting the platform | The ladder's handrail "hooks over the platform ... It looks attached, but loosely" | None needed (no longer "detached" or "doubled") |
| `iso_13` (bike in its rack) | The longer wheelbase | No longer squashed, but a long grey bar from the pedal area "could be a kickstand or a pedal, but it looks too long and in an odd position for either" | Redrawn in round 4 |

## Round 2: the follow-ups (6 crops)

| Crop | What was being tested | What the reader said |
|---|---|---|
| `iso_01`, `iso_04` (kick) | The ball at the toe, the swing arcs | "Curved motion lines just behind that front foot suggest she has just swung her foot, so she seems to be kicking the ball"; "She seems to be kicking a small orange ball". Both still offered "a mid-stride walk" or "a long stride/step past the ball": "the kicking foot looks flat on the ground rather than lifted" |
| `iso_02`, `iso_05` (play bow) | The same drawing again | "In a 'play bow' ... as if the dog is pawing at" the ball; "playing with the ball or inviting someone to throw it" |
| `iso_03`, `iso_06` (floating box) | The box 75 px above the fence top | "Tilted at an angle in the air above the top of the fence ... The box seems to be floating or flying. Nothing holds it up"; "hangs in mid-air with nothing holding it" |

The kick went into the in-context design tests (`design_tests_v012.md`) as it was, with the remark about the
flat foot kept for later. The play bow and the floating box were done.

## Round 3: a spade that reads as a spade (2 crops)

The design tests kept finding the same blade: "the shovel blade appears to hover slightly above the hole",
"the grey blade looks flat on the ground under the dirt clump and is not clearly joined to the handle ...
a separate flat piece (like a plank or tray)". So the blade was redrawn in the cast (`dig_lift`): a dark
blade cut to a spade's outline, square heel and rounded point, starting at the end of the shaft and joined
to it by a socket, its nose dipping toward the hole and its face turned toward the viewer so the earth on
it shows; the earth a low heap of two lumps, so it cannot pass for a ball.

| Crop | What the reader said |
|---|---|
| `iso_01` (garden) | "Bent forward and digging with a long-handled shovel. The shovel blade is at a small dark hole in the ground and is carrying a lump of brown dirt. Next to the hole is a brown mound of dug-up dirt" |
| `iso_02` (park) | "Bent forward and digging with a long-handled shovel. The shovel blade is at a small dark hole and holds a lump of brown dirt" |

Neither reader saw a plate, a spatula or a hovering blade. Both said the dirt mound was "set slightly apart
from the hole, so it looks a bit pasted on", so the pile now overlaps the hole's far rim.

## Round 4: the square wheel without an X (4 crops)

In the design tests the square wheel was read as a square wheel first, but three of six readers still
offered "a separate dark crate or box standing behind the front of the wheelbarrow". The four spokes ran
along the diagonals, and a square with an X across it is how a crate is drawn. Six spokes were tried first:

| Crop | What the reader said |
|---|---|
| `iso_01` (barrow, garden) | "The wheel looks like a square with rounded corners ... Its grey face has spokes or an X shape inside ... literally it reads as a square wheel, which looks wrong for a wheelbarrow" |
| `iso_02` (bike, street) | "Both bicycle wheels look like squares ... with an X of spokes ... literally they read as square wheels, which looks strange". The stand: "the crank or pedal arm reaches below the bottoms of the wheels"; the bike "stands upright with no kickstand ... and it has no shadow" |
| `iso_03` (barrow, park) | "A rounded square with X-shaped spokes ... It could be a stylized wheel or a square box/crate sitting behind the wheelbarrow" |
| `iso_04` (bike, playground) | "Rounded squares with X-shaped spokes ... They could be stylized wheels or square boxes behind the bike"; "There's no chain" |

At picture size six spokes still read as an X. So the square wheels got eight spokes set off the
diagonals around a big round hub, and the barrow's tyre got tread blocks standing out of it, three on each
side (a crate has no tread). The bicycle (both the square-wheeled one and the parked one) got a chain ring
with its chain to the back hub, a short crank with a pedal, and a thin stand off the back of the frame
ending in a foot. The wheelbarrow and the bicycle got ground shadows like the people's (design-test readers:
"the wheelbarrow casts no visible shadow, while the people and the dog do"), and so did the kicked ball
("the ball has no shadow of its own").

## Round 5: the kick in proportion to the leg, the tread wheel (6 crops)

The kick's foot height was a fixed distance, so a child's kicking foot was well up off the ground but a
long-legged kicker's was almost on it: in the design tests the teenager "walking or stepping to the left
... kicking it or about to stumble on it". The kicking foot is now raised and set forward in proportion to
the leg (0.40 and 0.85 leg lengths), tried at three heights on three children before choosing.

| Crop | What was being tested | What the reader said |
|---|---|---|
| `iso_01` (kick, park) | The teenager's kick, foot raised | "Kicking one leg out to the left. A small orange ball ... sits on the grass just ahead of and below the raised foot. She seems to be kicking, or about to kick, the ball" |
| `iso_04` (kick, garden) | The same | "She is mid-kick: she balances on one leg while the other leg swings out to the left toward a small orange ball ... Curved motion lines behind the kicking leg show it is moving" |
| `iso_03` (dig, garden) | The pile over the hole's rim | "Digging a hole ... The shovel blade is in a dark hole and holds a clump of brown dirt, and a mound of dug dirt lies on the grass to the right of the hole" |
| `iso_05` (barrow, garden) | Tread blocks and eight spokes | "A single black wheel with spokes ... It is drawn as a rounded square or octagon with blocky bumps around the edge, so it reads as a square wheel or a chunky tread tire". No crate |
| `iso_06` (parked bike) | The new stand, chain and crank | "Parked on a paved sidewalk ... in front of a grey inverted-U bike rack, using its kickstand"; but "which way the bike faces is unclear. The dark curved piece on the left could be the handlebars or the seat" |
| `iso_02` (square bike, street) | Eight spokes on the bike | "The wheels are drawn as rounded squares ... A quick glance could also read them as two dark boxes or crates with the bike frame in front of them"; "I can't tell the seat from the handlebars" |

The kick read as a kick in both, with no walk and no stumble; only before or after the strike was left
open. The barrow's wheel lost its crate reading. The bicycle kept two: its filled square wheels as boxes
behind the frame, and a seat and handlebars too alike to tell apart. So a bicycle's square wheel is now
open, thin spokes with the ground showing between them inside a thin tyre (a box cannot be seen through),
and the bicycle has a saddle on a seat post and handlebars on a stem sweeping back to a grip.

## Round 6: the bicycle (3 crops, one per reader)

| Crop | What the reader said |
|---|---|
| `iso_01` (square bike, street) | "A teal bicycle with black tyres, a dark saddle and dark handlebars ... it looks parked"; "the wheels look like rounded squares rather than true circles ... it makes the bike look a bit odd" |
| `iso_02` (parked bike, street) | "Parked on a light grey paved sidewalk. It stands in front of a grey metal bike rack"; the stand "could be a kickstand or a pedal arm" |
| `iso_03` (square bike, playground) | "A black saddle on the left, curved handlebars on the right, a grey crank/chainring in the middle with pedals, and two dark wheels with thin grey spokes"; "Both wheels are drawn as rounded squares, not circles ... a bike with square wheels could not roll" |

No box, no crate, and the saddle and handlebars named the right way round by all three.

## Round 7: one square wheel for both (4 crops, one per reader)

Back in whole scenes (design-test round 3) the rounded square wheels drew a new second reading: "a round
wheel drawn badly", "a clumsy drawing of a wheel", "or it could just be the drawing style". The tread
blocks and rounded corners had made the barrow's wheel "a rounded square or octagon". So both square
wheels became the same open wheel with sharp corners: eight dark spokes set off the diagonals, the ground
showing between them, a thin tyre over their ends and a round hub. The barrow lost its tread blocks.

| Crop | What the reader said |
|---|---|
| `iso_01` (barrow, garden) | "Its outer rim is drawn as a square ... It reads either as a square wheel (which looks wrong) or as a wheel sitting inside a square frame or bracket. A real wheelbarrow wheel would be round" |
| `iso_02` (bike, street) | "Both wheels are drawn as squares, not circles. They are dark square outlines with spokes inside ... a bicycle could not roll on them" |
| `iso_03` (barrow, park) | "The wheel looks square: a dark square frame with spokes coming out of the round hub, instead of a round tire ... as drawn it reads as a square" |
| `iso_04` (bike, playground) | "Its wheels are square: dark square rims with spokes ... A bicycle with square wheels could not roll. It may be a deliberate joke or a drawing error. Either way it reads as 'wrong'" |

Square, and wrong, in all four; no crate, box, octagon or badly drawn round wheel. That drawing went into
the set, with one more placement rule from the design tests (`design_tests_v012.md`, round 4): the
square-wheeled object stands wholly on the path or wholly off it, since the path's curved edge seen through
the open wheel drew a round wheel inside the square.

## Round 8: the swing arcs (2 crops, one per reader)

In a busy park (design-test round 5) the arcs behind a child's raised kicking foot, drawn up the back of
the leg, hung from his shin: "something string-like trails from his foot, possibly an untied shoelace".
The arcs now follow the foot's swing about the hip, behind and below the raised foot.

| Crop | What the reader said |
|---|---|
| `iso_01` (the teenager, garden bench) | "Kicks with one leg stretched far out to the left ... Curved motion lines between the ball and the person suggest the leg's swing or the ball moving" |
| `iso_02` (the child, cut from the garden test scene) | "Standing on green grass and kicking. One leg swings out to the left toward an orange ball ... Curved motion lines under the kicking leg show the swing" |

## Round 9: the barrow's wheel set forward (2 crops, one per reader)

With its top half behind the tub, only an L of the barrow's square wheel showed. The wheel now stands
mostly out in front of the tub, so three of its corners show.

| Crop | What the reader said |
|---|---|
| `iso_01` (garden) | "The wheel is drawn as a square (a dark square frame with spokes radiating from a central hub) rather than a circle ... a square wheel looks wrong for a wheelbarrow" |
| `iso_02` (park) | "The wheel is square ... You can tell it is a wheel from the spokes and hub, but the outline is a rounded square or rectangle, not a circle" |

Read as before (square, and wrong); the forward wheel was kept because it shows the square whole.

## What the bench left as it is

- **The play bow's legs.** Four readers called the hind leg or the front legs "stick-like" or "long and
  thin", and all four still read the play bow, the wag and the ball. A cast change for proportion alone
  was left for a later release.
- **The kicked ball's moment.** "Just before the kick or just after it" stays open; either reading is a kick.
- **The floating box's shadow.** Read either as the box's shadow ("the box is high in the air over the
  yard") or as a shadow with nothing on it. Both make the box float.
