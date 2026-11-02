# The v0.19 changes, read blind in whole test scenes

After the isolation bench (`isolation_v019.md`) the refined visuals and the new placement rules went back into whole
scenes, with the other events around them, and were read blind there before the set was regenerated, as in v0.8 to
v0.18. Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v019/`; `map.txt` names the scene behind each
picture. The four templates the v0.18 gate failed were put in them: the reading walker in two busy tier-4 scenes with
no wind, the stalking cat on a garden fence, the frying pan in a garden with no hose reel, and a runner in three.

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (park, tier 4) | A man reading as he walks toward a ball in a busy park with no wind; a runner; the duck feeding; sitting on nothing | "An older man in a cap and vest walks to the left while reading an open newspaper. A red ball lies on the grass right in front of him, so he looks about to trip over it"; "a woman in a yellow dress is running fast to the left in front of the pond, with motion lines behind her"; but "her dark speed lines are drawn on the water's surface ... she could also look like she is running in or out of the water" |
| `test_2.png` (garden, tier 4) | The stalking cat on the fence by a perched bird; the ball in the tree; the sprinkler and the box; someone hosing the flowers; a catch | "On top of the fence a black-and-white cat crouches as if it is stalking a red bird perched a little way along the fence, and it looks about to pounce"; a person "looking up and pointing at a blue ball that is stuck in the branches of a tree"; a woman who "holds a garden hose and sprays water onto a bed of colourful flowers"; the sprinkler "spraying arcs of water to the left onto a cardboard box ... The box is dripping and sits in a puddle" |
| `test_3.png` (garden) | The frying pan with no hose reel in the picture | The man "holds a grey can out over a flowerbed ... and water pours out of it", then "a round grey disc with a dark handle and no clear spout, so it could be read as a frying pan or saucepan rather than a watering can ... its shape looks more like a pan" |
| `test_4.png` (park) | A runner; the kicked ball against the toe | "A woman ... is running to the right across the middle of the scene; speed lines behind her show she is moving fast"; "a girl ... is kicking an orange ball" |
| `test_5.png` (street, tier 4) | A man reading as he walks; a runner; the begging dog clear of the eater's legs; people passing the lamp post and the stall | "A man in a red shirt and blue jeans walks along reading an open book. He isn't looking where he's going, and a blue bucket sits on the pavement just ahead of him, so he seems about to trip over it"; the dog "stretches up towards him, looking at the ice cream as if it is about to jump for it or beg"; a woman "walks past a black lamp post"; a runner "with speed lines trailing behind her" |
| `test_6.png` (playground, tier 4) | The child pointing from under the ball in the tree; the swing frame and the slide to keep clear of | "A little girl in a pink dress stands by a tree and points up at a blue ball that is stuck on a branch in the tree"; but a woman pushing a pram along the railing seemed to walk the other way, "so she seems to be pulling it rather than pushing it" |

The reading walker read as reading and about to trip in both scenes, and as reading a book or a newspaper, with no
reader saying papers in the wind. The stalking cat on the fence read as stalking, "about to pounce". The runner read as
running in all three scenes, each time by the speed lines. The hose's jet and the sprinkler's arcs read as water, and the
begging dog, the child pointing at the ball and the kick read as meant. No reader saw anyone against a lamp post, inside
the swing frame or among the stall's legs.

Two remarks led to changes before the set was built: the runner's speed lines drawn over the pond (they now stay off
the water), and the frying pan read at first as "a grey can" before the reader added that its shape "looks more like a
pan" (left as it is: on the bench both readers named a frying pan or a saucepan, and none a spout or a rose; a note for
the screen). The pram that seemed pulled is the pram pusher's pose, unchanged since v0.6; it is noted for the screen.
