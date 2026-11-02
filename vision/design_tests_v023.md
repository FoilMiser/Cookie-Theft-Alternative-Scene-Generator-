# The v0.23 changes, read blind in whole test scenes

After the isolation bench (`isolation_v023.md`) the redrawn pan, the begging dog, the older man's profile and the barrow's
leg (builder 0.23.0), and the placement rules of revision 21, went into whole scenes with the other events around them and
were read blind there before the set was regenerated, as in v0.8 to v0.22. Each reader was a fresh model that saw only its
one picture, with the screen's reader prompt (`screen_prompts.md`). The pictures and descriptions are in
`design_tests_v023/`; `map.txt` names the scene behind each picture. Two rounds, eight pictures.

## Round 1 (six pictures)

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (garden) | The v0.23 frying pan among a dig, a dog walker and a rake | "she is pouring the water out of what looks like a frying pan or saucepan rather than a watering can, which seems odd" |
| `test_2.png` (park, tier 4) | The older man walking with his bag; the reading walker and her box a full step ahead; the begging dog; a sleeping cat; the duck feeding | "a wooden box sits on the grass just ahead of her, so she looks about to trip over it"; "a brown dog with a red collar or bandana sits up on its hind legs beside the bench, begging for the ice cream"; the older man "walks along carrying a yellow shopping bag", his "head and cap brim face right" (the way he was walking), "his stride could be read as walking either left or right" |
| `test_3.png` (street, tier 4) | The begging dog; the reading walker; a runner and a pram pusher; the square-wheeled bicycle | "A cardboard box sits on the ground just ahead of her, so she looks about to trip over it"; "a brown dog in a red bandana sits up on its hind legs and begs at a boy"; the bicycle's wheels "square or boxy, not round"; the runner "might be jogging ... Nothing visible is chasing him" |
| `test_4.png` (playground) | A runner and a pram (not heading at each other); the cat stalking a bird | The runner "seems to be running toward the cat and bird, perhaps to stop the cat"; the cat "about to pounce" |
| `test_5.png` (park) | An angler with a duck in the pond, clear of the float | "The duck is facing toward the float, so it may be about to swim over to it" |
| `test_6.png` (garden) | The barrow on its strut; the blocked hose; the washing | "an empty grey wheelbarrow at the front"; the dog "with a back paw on the hose ... the dog seems to be blocking the water" |

The pan, the begging dog, the reading walkers' boxes and the barrow read as meant, and the older man was seen facing the
way he walked. Two pictures told stories they were not meant to: a runner whose lane ended 25 px short of the cat and bird
behind her line seemed to run at them, and a duck about 130 px from the angler's float, facing it, "may be about to swim over to
it". Revision 21 therefore also deepens a runner's lane behind her line (220 px, was 150) and turns every duck away from a
float, and test_4 and test_5 were rebuilt.

## Round 2 (the two rebuilt scenes)

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_7.png` (playground) | test_4's scene, the runner's lane deeper | The cat "looks about to pounce", the runner not linked to it ("nothing in front of her explains it"); but she runs past the man with the pram, "side by side and almost touching but moving in opposite directions, so she seems to be running past him" |
| `test_8.png` (park) | test_5's scene, the duck turned away | "a white duck is swimming on the left side of it ... the only thing that seems about to happen is a possible bite on the fishing line" |

Both rules read as meant. The runner brushing past the pram pusher added one more rule, not read again before the set was
built: a runner keeps 50 px clear of any other mover beside her on her line (within 60 px in depth).
