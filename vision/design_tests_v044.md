# v0.44 design tests

The cast of builder 0.44.0 and revision 42 were read blind in whole test scenes among other events (`tools/cycle/design_tests.py`, the v0.44 jobs), each
picture by a fresh reader with the reader template, one picture to a reader. `design_tests_v044/map.txt` names each picture's record.

| Test | Forced | Placed |
|---|---|---|
| 1 | A park: the reading dog, a balloon lost, a runner | first seed |
| 2 | A garden: the dog by the door, a cat stalking a bird, the water going up | first seed |
| 3 | A playground: the seesaw stuck, a sandcastle, an ice cream | first seed |
| 4 | A park: the goat at 45, an ice cream eaten with a content face, a photographer | twelfth seed (the rule asks for a content face) |
| 5 | A street: the reading dog, a shopper with a bag, a dog begging | first seed |
| 6 | A garden: the hose stopped and inspected, a raker, a child on the swing | first seed (with a planter instead of the raker, the planting placed on none of 80 seeds) |

**The reading dog** (tests 1 and 5), sitting up in glasses with its paper hung from its paws and tilted.
- It read as reading in both, the contradiction named: "sits up on its back legs, holding an open newspaper in its front paws and looking at it as if reading. That is the odd or impossible part, because dogs can't read newspapers" (1); "appears to be reading it, possibly wearing glasses. That newspaper-reading dog is the clearly odd or impossible thing in the picture" (5).
- The glasses: "dark round shapes. These could be glasses (fitting with 'reading the paper'), or just dark eye patches in its fur" (5); not mentioned in 1.
- Other readings: "just have picked up or fetched the paper and be holding it open" (1). One paper "gripped only on its right edge by the dog's paws, so the left half seems to stay up stiffly with little support" (1).
- In test 1 a runner passed close in front of it: "she seems to be running away from both", the dog and the girl, one reading among "jogging for exercise ... or hurrying somewhere".
- In test 5 the reading dog is the tan dog, so the begging dog is the white one, which begged "looking up at the man, as if begging for the ice cream".

**The dog by the door** (test 2), its lead yellow and hanging from its mouth to a loop: "holding a yellow lead in its mouth, as if it is asking to go for a walk"; "It is not clear whether it is waiting at the door to be let in or asking the boy for a walk".

**The upward water** (test 2), a tapering ribbon: "instead of pouring down onto the flowers, it shoots up into the air in a curved stream with drops at the top"; once read as "water rising out of the flower bed".

**The stalking cat** (test 2), on the fence: "a grey cat crouches low and creeps towards a small blue bird ... the cat seems about to pounce on the bird".

**The seesaw and the sandcastle** (test 3).
- The child stuck up high, one hand at her open mouth: "Her mouth is open in an 'O' and one hand is raised near her face. She looks like she is calling to him or is surprised ... the joke seems to be that she can't get down while he reads". Still "the plank looks like it crosses behind or through his lower legs", as in every screen since v0.31.
- The spade: "a child ... kneels with a red spade next to a sandcastle", once "a spade or a small trowel".

**The goat, the ice cream and the photographer** (test 4).
- The goat at 45: "a white goat with curved horns and a red collar has its head down and is eating a small tuft of grass. A rope runs from its collar to a short wooden stake"; "a tethered goat grazing in a public park" the only thing "a little unusual". Its beard went unremarked.
- The ice-cream eater with his eyes closed: "This could mean he is enjoying the taste, or he may have brain freeze".
- **The scoop.** The man in red eating an ice cream, in tests 4 and 5, had a cream scoop by the colour rule (`TPDB_PROP44`): at a threshold of 40 degrees, pink was too near his red shirt. Pale on pale skin, the scoop sank, and the cone's tip at his lip read as "a moustache or chocolate ice cream smeared on his face" (4) and "a moustache or a smudge" (5). The rule's threshold is now 20 degrees: the clashes named in the review are 0 degrees apart (a yellow bag on a yellow dress, a teal can on a teal cardigan, a pink scoop on a pink dress), and the man in red's scoop is pink again, as in v0.43. The props were rendered again; the pictures were not read again, the scoop being v0.43's.

**The hose** (test 6), stopped under the tan dog and inspected by the woman in yellow, her head level: "holds a green garden hose up near her face and looks into the nozzle. Only a single drop of water is coming out ... It looks as if the dog is standing on the hose and stopping the water". Her face "is shown only in profile and her facial expression is hard to read".
