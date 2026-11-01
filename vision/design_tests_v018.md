# The v0.18 changes, read blind in whole test scenes

After the isolation bench (`isolation_v018.md`) the refined visuals and the new placement rules went back into whole
scenes, with the other events around them, and were read blind there before the set was regenerated, as in v0.8 to
v0.17. Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v018/`; `map.txt` names the scene behind each
picture. The waver, the one template the v0.17 gate failed, was put in all six, so each placement could only stand
where its hand is clear of the backdrop's lines and not at the far back.

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (park) | The waver; a sleeping cat; the duck's wake beside a picnic on the shore | The woman in yellow "raises one hand high and waves (there are motion marks around her hand) ... She is facing a man ... walking along a winding sandy path ... so they seem to be greeting each other"; "a small orange cat is curled up asleep on the grass"; the duck "swimming across it, with little wake lines behind it" |
| `test_2.png` (garden) | A catch and a woman reading as she walks in the same garden (in v0.17 a reader beside a catcher was "squashed together" with him); the waver at the gate; a sleeping cat | "Two children are playing catch in front of the fence"; the reader "is looking at the book and not at the ground, and a closed cardboard box sits right in front of her leading foot"; a man at the gate "waving one raised hand (motion lines show the waving)"; "an orange cat is curled up asleep" |
| `test_3.png` (playground) | The waver at the railing; a catch; the larger cat stalking a bird | "Right hand raised and waving (motion lines)"; the man "reaching to catch the ball"; the cat "crouched low with its tail straight out behind ... Stalking, or about to pounce on the bird" |
| `test_4.png` (street) | The dark-haired woman reading as she walks; the waver by the stall | "A woman in a yellow dress is walking to the left while reading an open book ... since she seems to be looking at her book rather than where she is going, she looks about to trip over it"; "a man in a red shirt ... raising one hand and waving"; but "her facial features are minimal" |
| `test_5.png` (park, tier 4) | The waver among eight other events; a sleeping cat; the duck's wake | A small girl "waves one raised arm (with motion lines) and faces the viewer"; the duck "swims left toward the food, with wake lines behind it"; "the cat is sleeping out in the open in the middle of a busy park" |
| `test_6.png` (garden, tier 4) | A catch in front of a man reading as he walks; the waver on the path; the stalking cat on the fence; a sleeping cat | "A boy ... has just thrown a red ball (a dashed line shows its arc), and a little girl in a pink dress holds her arms out to catch it"; the reader "looks about to walk into it or trip over it"; a man "waving one hand high and calling out"; "a black-and-white cat is creeping along toward a red bird"; "an orange cat lies curled up asleep" |

The wave read as a wave in all six scenes, every time "with motion lines", and no reader saw a string, a held object or
anything else at the raised hand. No reader saw two figures in each other, a ball heading for someone other than the
catcher, a duck's wake reaching anyone, or a thing cut off by the picture's edge. The sleeping cat read as a sleeping cat
in all four scenes it was in, and no reader there called it small. The dark-haired woman was read as reading as she walks
in the street, though her "facial features are minimal".

Nothing in the test scenes led to a further change before the set was built.
