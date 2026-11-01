# The v0.17 changes, read blind in whole test scenes

After the isolation bench (`isolation_v017.md`) the refined visuals and the new placement rules went back into whole
scenes, with the other events around them, and were read blind there before the set was regenerated, as in v0.8 to
v0.16. Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v017/`; `map.txt` names the scene behind each
picture. The photographer, the one template the v0.16 gate failed, was put in three of them, each time with someone to
photograph.

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (park) | The photographer; the soaked box on the lawn; a pram passing the woman feeding birds | "A bearded man ... holds a camera up to his eye"; the box "is dripping and sits in a puddle, so it is getting soaked"; "a baby is asleep in the pram under a pink polka-dot blanket". But "the lamppost stands right next to him, almost in front of the lens"; the box "could be a wooden crate, a cardboard box or a picnic basket", its blotches "wood grain, wet stains" |
| `test_2.png` (playground) | The photographer; a bird on the railing away from the slide | "A woman in a yellow dress ... holds a camera up to her face ... taking a photo toward the right side"; the bird "sits on top of the bushes or fence at the far left" |
| `test_3.png` (garden, tier 4) | The soaked box, the goat, the square-wheeled wheelbarrow, beside the blocked hose | The water "is landing on a cardboard box ... in a puddle and looks soaked and stained"; "a white goat with horns has its head down, nibbling at a tuft of grass"; "an empty wheelbarrow whose wheel looks square rather than round"; the blocked hose in full ("if the dog steps off, the water might suddenly spray out") |
| `test_4.png` (street) | The photographer beside a reader on the bench and the rising water | "An older woman with grey hair holds a camera to her eye and points it left, as if photographing the scene"; the water from the can "shoots up in a curved stream" |
| `test_5.png` (park) | The goat; the white dog on a lead; the reading dog | "A white goat with small curved horns is bent over eating a tuft of grass"; "a white dog with brown spots on a red leash"; "a brown dog sits on the grass holding an open newspaper ... which is impossible" |
| `test_6.png` (garden) | The soaked box beside a goat; the dog by the door | "The water is falling onto a brown cardboard box ... the box looks soaked and stained, and it is sitting in a puddle"; "a white goat with small dark curved horns"; the dog "holding a red lead in its mouth, as if it wants to go for a walk" |

The camera read as a camera in all three scenes; no reader said binoculars. The goat read as a goat in all three
(by its horns), the white dog as a dog, the wheelbarrow as standing at rest, and no reader saw water coming out of the
box. No reader saw a figure's feet on a bench, a pram heading into anyone, a bird on the slide or a thing cut off by the
picture's edge.

Two remarks led to changes before the set was built, both read in the screen that followed: the photographer now needs
a clear line from the lens to whoever he photographs, with no lamp post, tree, slide, swing frame or stall in the way;
and the box's darker wet patches, taken for wood grain or straw, were dropped, leaving the drips down its front, the
water running off its lid and the puddle at its foot.
