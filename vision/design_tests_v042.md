# v0.42 design tests

The cast of builder 0.42.0 and placement revision 40 (`vision/isolation_v042.md`) were read blind in whole test scenes among other events: six pictures, six fresh readers, one picture each. The files are `design_tests_v042/test_N.png` and `desc_test_N.md`; the prompts are `tpdb_work/dtp42p/test_N.txt`, the reader template cut to one picture. The jobs are in `tools/cycle/design_tests.py`, each with the redrawn animal at a forced angle. All six placed on their first seed.

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-3 garden | The goat grazing tethered (90), the hose stopped by the spotted dog, the washing hung out by the woman in yellow | The goat "is tied by a rope to a small stake near the gate and is eating a tuft of grass". The hose: "the dog seems to be blocking the water". The woman in yellow is "a woman in a yellow dress"; the woman with the hose is "a girl in a purple top" |
| 2 | Tier-3 park | The dog begging in profile (90), a second ice cream by the pond, birds fed at an angle | Begging, "as if begging, looking up toward the man and his ice cream"; the boy eating his own by the pond is not offered as the one it begs from. Once its head: "its head is tilted so far up that it could also be read as just sitting up or looking at the sky/lamp post". The bird at 45: "A small blue bird stands on the grass below him, pecking at the scattered seeds" |
| 3 | Tier-3 street | The dog begging at 45, a second ice cream at the stall, a sweeper | Begging, "apparently towards the boy and his ice cream", and "it could also be read as begging towards the sweeper or just sitting up generally"; the eater at the stall is not offered. The heap's season once: "the pile of brown leaves is a little odd since the only tree in the scene is fully green" |
| 4 | Tier-3 park | The goat at 45 tethered, the duck at 45, a reader on a bench | The goat: "so the goat looks tethered", and "The one unusual thing is a goat tied up in a public park"; once "it could just possibly be read as a young ram or a kid". The duck "swimming near its back edge". The reader, the woman in purple: "could be read as a girl (child or teenager) or as a young woman" |
| 5 | Tier-3 garden | The cat stalking a bird at 45, the flowers watered, a raker | Stalking: the cat "crouches low right behind it, with its face almost touching the bird's tail", and nothing said of its legs |
| 6 | Tier-3 park | The dog reading the paper, a bird perched at 45, a kicker | The dog "sits upright on its haunches", and of the paper "reads most like reading"; no reader called it a person. The bird at 45, "perched on top of the lamp" |

**What the tests show.**
- **The goat is somebody's goat.** Tethered in both pictures, and named a goat in both. In the park the tether makes it "tied up", still "unusual".
- **The begging dog begs from the bench.** In both pictures with a second ice cream, the reader gave the bench's eater, and revision 40's zone kept the other well away: by the pond in the park, at the stall in the street. Kneeling or a person was said in neither. The head tipped up drew "looking at the sky" once.
- **The reading dog sits on its haunches,** and reads as reading.
- **The birds and the duck at 45** read as they do at 90.
- **The woman in yellow** is a woman in the one picture she is in. The woman in purple is "a girl in a purple top" once and "a girl (child or teenager) or ... a young woman" once. In v0.41's screen "girl" stood beside her purple top 16 times and "woman" 28 times, overlapping where a reader wrote "girl or young woman" (`grep` over `v041/desc_pic_*.md`, 40 characters either way). It is not new, and it goes on the list.
- **The heap's season** was remarked in one picture of six, as in v0.41's tests, and stays a note.

No new rule was needed.
