# The v0.12 changes, read blind in whole test scenes

After the isolation bench (`isolation_v012.md`) each refined visual went back into whole scenes, with the
other events around it, and was read blind there before the set was regenerated, as v0.8 to v0.11 did.
Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v012/`; `map.txt` names the
scene behind each picture.

## Round 1: the refined visuals among the other events

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (park) | Kick, play bow with its ball, dig, square wheel | The kicker "striding toward the left ... Curved motion lines by her left foot suggest she just kicked", but also "about to step on it and trip". The dog "in a play-bow pose ... nose at a tennis ball ... tail is wagging". The digger "grips a long-handled shovel ... a lump of brown soil on it", her "eyes look closed or squinting". The wheel "a square box with an X through it ... (a) a square wheel ... or (b) a box or crate pushed up against the front of the wheelbarrow" |
| `test_2.png` (garden) | Dig, a child kicking, floating box | The box "clearly floating above the fence with a shadow on the grass". The child "could be mid-kick and leaning back for balance, or ... slipping/falling backward, or sitting on the grass while kicking. Her body is tipped back at a sharp angle". The man "digging right next to the base of a clothesline post ... the post is about to be undermined"; "the shovel blade appears to hover slightly above the hole" |
| `test_3.png` (playground) | Kick, slide ladder, play bow | "Arms out for balance, kicking an orange ball to the right with one foot. Motion lines behind the kicking foot"; the dog "in a play-bow crouch with its head low toward a tennis ball"; the slide "red frame, blue top platform, grey ladder" (no complaint about the ladder) |
| `test_4.png` (street) | Square-wheeled bicycle | "Clearly impossible and look deliberate. It is also odd that the bicycle stands upright with no rider, stand or support. I could not tell for sure which end is the handlebars and which is the seat" |
| `test_5.png` (busy park, five events) | Kick, dig, play bow, square wheel among ducks, a reader about to trip and a dropped ice cream | The child "leaning back with arms out and one leg stretched toward an orange ball, as if kicking it or losing balance"; the digger "with a dirt pile and a dark hole just to his left"; the dog "in a play bow ... facing a tennis ball"; the wheel "a square box with an X, not a circle" |
| `test_6.png` (garden) | Play bow, square wheel | The dog "(play bow) beside a tennis ball, tail raised with wag lines". The wheel "an impossible square wheel ... The other is that it is a crate or box standing in front of the wheelbarrow, hiding the real wheel" |

Five changes followed:

- **The child's kick.** The kick leaned back less (a lean of 12 degrees read as falling or sitting); 6.
- **The square wheel.** Tucked under the front of the tub, with the tub drawn over its top and a fork from
  the tub to the hub (drawn in front of the tub it read as a crate standing there).
- **The blade.** Lowered toward the hole.
- **The hole.** Clear of every standing structure (a clothesline post, a bench, the hose reel, the fence).
- **The ball's path.** The ground ahead of the kicked ball, where it is going, must be clear of every
  person, animal and drawn object, and there is room round the kicker (a ball heading for the square-wheeled
  barrow; a play-bowing dog with its own ball right by the kicker).

## Round 2: the same scenes rebuilt

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_7.png` (`test_2` rebuilt) | The upright kick, the lowered blade, the box | The child "mid-kick, standing on one leg, with the other leg swung out to the left toward the ball and motion lines behind it". The box "floating or falling". The blade still "looks flat on the ground under the dirt clump and is not clearly joined to the handle ... a separate flat piece (like a plank or tray)" |
| `test_8.png` (`test_6` rebuilt) | The wheel under the tub | "The wheel is clearly drawn as a square ... Another reading is that it is a square box or crate behind the wheelbarrow that hides the wheel, but the axle hub in its centre makes it look like a square wheel" |
| `test_9.png` (`test_5` rebuilt) | All five events | "He kicks an orange ball, and there are motion lines by his leg"; "digs a hole in the grass, looking down at it"; the dog "in a play bow ... facing a tennis ball"; "Its wheel looks square" |
| `test_10.png` (`test_1` rebuilt) | Kick, play bow, dig, square wheel | The kicker "walking or stepping to the left with arms spread, one foot right next to an orange ball. They seem to be kicking it or about to stumble on it". The dog "in a play bow with its tail up and wag lines". The digger "digging a hole and looking down at it", "a brown clump of dirt on the blade". The wheel "reads as a square wheel, which is impossible or wrong. It could also be read as a separate dark crate" |

Everything now read as intended in first place, but three visuals still drew a second reading: the
spade's blade (a plank or tray), the long-legged kicker (her kicking foot nearly on the ground: "walking
or stepping"), and the square wheel (a crate). Each went back to the isolation bench (rounds 3 to 6 in
`isolation_v012.md`).

## Round 3: the bench's drawings back in the scenes

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_11.png` (`test_1` rebuilt) | The redrawn spade, the kick in proportion to the leg, the tread wheel | The teenager "stands on their right leg with the left leg swung out ... (motion lines by the foot) ... kicking at or toward the orange ball". The digger "is digging. The blade is at the hole with a lump of dirt on it". The dog "in a play bow ... with a tennis ball by its front paws". The wheel "square or box-shaped with spokes ... Read one way it's a deliberately impossible square wheel. Read the other way it's a round wheel drawn badly, or a wheel with a crate or block stuck in front of it" |
| `test_12.png` (`test_2` rebuilt) | The spade, a child's kick, the box | The man's "blade in a small hole in the lawn ... Clearly digging ... He seems to be lifting soil out". The child "kicking or about to kick". The box "floating or falling in mid-air above the gate" |
| `test_13.png` (`test_4` rebuilt) | The redrawn bicycle | "They look like rounded squares, not circles. This could be a deliberate 'something is wrong' detail (square wheels can't roll), or it could just be the drawing style" |
| `test_14.png` (`test_5` rebuilt) | All five events | "Digging with a long-handled shovel. The blade is in the dirt"; "kicking with one leg (motion lines behind it)"; "in a play-bow"; the wheel "square or boxy ... may be meant as an impossible 'square wheel,' or it may just be a clumsy drawing of a wheel" |

The spade and the kick were settled: every reader named digging and kicking first, with no plank, tray,
walk or stumble. The square wheels had traded the crate for "a clumsy drawing", and went back to the bench
(round 7).

## Round 4: the open square wheel

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_15.png` (`test_1` rebuilt) | The open square wheel on the barrow | "Its wheel is drawn as a square"; "it looks square (a square frame with spokes) instead of round. This looks wrong or impossible for a working wheel". The kick "kicking, or to have just kicked"; the digger "the blade is at a hole in the ground and carries a lump of brown dirt"; the play bow |
| `test_16.png` (`test_4` rebuilt) | The open square wheels on the bicycle | "Its wheels are square with spokes"; "this looks deliberately wrong/impossible (you could not ride it), but it could also be read as a drawing error" |
| `test_17.png` (`test_5` rebuilt) | The barrow among five events | "It looks a little strange. The wheel sits inside a black square frame ... It could read as a normal wheelbarrow or as one that is tipped or broken" |

In `test_17` the barrow stood across the edge of the path, and the path's curved edge, seen through the
open wheel, drew a round wheel inside the square. So the square-wheeled object now stands wholly on the
path or wholly off it.

## Round 5: the busy park again

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_18.png` (`test_5` rebuilt) | The barrow kept off the path's edge | The wheel "looks square or squarish (a square outline with spokes) rather than round. That could be an intentional 'impossible' detail (a square wheel), or just a stylised or angled drawing". The child kicking: "something string-like trails from his foot, possibly an untied shoelace ... It isn't clear whether he is about to step on the orange ball, kick it, or trip on his lace" |
| `test_19.png` (`test_5` rebuilt) | The swing arcs about the hip | The child "running and kicking an orange ball, with motion lines by his foot", the ball "just kicked" (or "running and about to trip over it"). The barrow's wheel "drawn as a square frame with spokes rather than a round wheel, and the whole thing looks slightly tilted, as if it is tipped". The dog "in a play bow ... (or a stretch)" |

The shoelace in `test_18` sent the arcs back to the bench (round 8): drawn up the back of the raised leg
they hung from the shin. In `test_19` they read as the swing. In this, the busiest test picture, the square wheel was named but hedged; elsewhere it read as square and
wrong. The set's screen will show whether the barrow holds up there.
