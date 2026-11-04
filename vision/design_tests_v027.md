# v0.27 design tests

The new drawings and revision 25 were read blind in whole test scenes among other events: six pictures, three fresh readers, two pictures each in different settings (`design_tests_v027/test_N.png`, `desc_test_N.md`; `map.json` names the records). `tools/cycle/design_tests.py` lists what each forces. Two small fixes came out of them, below; they were not read again, and go to the screen.

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-4 street | Faces in profile, the reading walker, the older man's ice cream, the broom | "A person in a yellow dress and red shoes walks to the right while reading an open book, not looking where they are going"; "standing and licking a pink ice cream cone"; "sweeps a small pile of autumn leaves with a yellow broom". The ball in the walker's way: "there is no shadow under it ... it looks slightly as if it is floating" |
| 2 | Tier-3 garden | The broom beside the rake, the hose to the fist | "Sweeping a small pile of orange, yellow and red leaves with a straw broom"; "raking a small pile of green and brown leaves"; "holding a hose and spraying". But the hose "rises from the ground up to the man's hand as a fairly stiff vertical line ... at first it can look like a pole or stand" |
| 3 | Tier-3 park | The pecking bird, the soil heap, the older man fishing | "A little blue bird is standing among more seeds, pecking at them"; "a hole at his feet and a heap of dirt beside it"; "a brown bag or box" |
| 4 | Tier-3 playground | The shorter figures on the seesaw, the photographer, the walking ice cream | "So the heavy old man is holding the little girl stuck up in the air"; "holding a camera up to their face and taking a picture"; "walks along licking a pink ice cream" |
| 5 | Tier-4 garden | The soaked box, sitting on air off the path, the stalking cat | "The box is already wet, with water running down its sides and a puddle around its base, so whatever is inside looks likely to get ruined"; "there is no chair or bench under them, which looks impossible"; the bird "perched and facing left towards the cat" |
| 6 | Tier-3 street | The bicycle's wheels, the bag, a seated reader | "A red bicycle is parked in a metal rack"; "carrying a yellow shopping bag". The seated reader's "feet are placed well to the right of the bench with the legs angled sideways, so he looks as if he is sliding" |

## What this says

- **The broom.** A straw broom beside a rake in the same picture, each named for what it is. Two of the six pictures have a broom, and both readers said broom.
- **The faces.** The remarks are about small things now: "dark or reddish marks around the eyes and mouth", "small dots on his face". One photographer's "head is turned away so the face is mostly hidden", at a pose that keeps its profile. No beard read as a mask or a strap, and no mouth as a moustache.
- **The trip.** Stated as "not looking where they are going", though the walker's obstacle was a ball, and a ball with no shadow.
- **The soaked box.** Read in full, inference and all, and as cardboard. Its drips are not slats.
- **The sitter on air.** Off the path, read at once as impossible.
- **The bicycle.** Nobody mentioned its wheels, which is what a wheel should do.

## Fixed from them

- A ball in a walker's way has a shadow (revision 25).
- A seated adult's feet come in from 0.40 to 0.32, as the thigh is shorter now, so the shin stands nearly upright under the knee (builder 0.27.0).

Left: the hose as "a pole or stand". Every curve tried since v0.11 has had a name from some reader: "a pole", "a stiff loop", "tightly behind/around the old man's legs". It goes on the list.
