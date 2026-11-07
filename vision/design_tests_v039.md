# v0.39 design tests

Revision 37 and the redrawn cast (builder 0.39.0) were read blind in whole test scenes among other events: four pictures, four fresh readers, one picture each (`design_tests_v039/test_N.png`, `desc_test_N.md`; the prompts are `tpdb_work/dtp39p/test_N.txt`, the reader template cut to one picture). `tools/cycle/design_tests.py` has the jobs; three ask for an animal turned from profile (rule `angled`).

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-3 park | The goat grazing at 135, a dog walked, a kicker | The kick and the walk read: "a boy in a red cap and blue hoodie is kicking an orange ball"; "an older man ... is walking a white dog with brown spots on a red lead". But "The strangest thing is the goat: its head and legs are white, but its body is a lumpy brown shape that looks more like a sack or blanket on its back than a goat's body", as on the bench (below) |
| 2 | Tier-3 street | A dog begging at a bench at 45, the broom's summer heap, a shopper | "A brown dog with a red collar sits up on its back legs beside the bench, front paws raised, looking up at the child as if begging for the ice cream"; the heap "a small pile of green and brown leaves", and still: "The only odd detail is that the man is sweeping up leaves while the only tree in view is fully green". The shopper's "feet seem to point in slightly different directions" |
| 3 | Tier-3 garden | The washing hung out, a raker's summer pile, a cat stalking a bird | "most likely he is hanging the wet shirt up, since it is dripping and there is a full basket at his feet"; "an orange cat is crouched as if stalking a red bird ... about to pounce"; and the pile: "the raked leaves are mostly green, while every tree and bush is fully green ... A pile of fallen leaves feels slightly out of place, and they could also be read as grass clippings or weeds" |
| 4 | Tier-3 park | A game of catch (the ball short of the hands), a dog's play bow at 45, a reader on a bench | "a boy ... has just thrown a red ball. A dashed line shows its path as it arcs through the air toward a girl in a pink dress ... ready to catch it"; "the ball sits just after the top of the arc, so it reads as heading down toward the girl", no doubt about who threw; "a tan dog ... crouched in a playful bow ... next to a yellow-green tennis ball" |

**Round 1.** The catch reads one way now (v0.38's R2: "the ball sits right at the woman's hands", and the trail could run from either end). The turned dogs read as before. The summer heaps took the season out of the remark but not the remark: two readers of two asked where leaves came from under green trees, more softly ("slightly out of place", "the only odd detail") than v0.38's "autumn leaves under green trees"; the heaps stay as benched (Sam: "use it rather than the grit style"), and the remark is watched in the screen. The goat was the picture's strangest thing, so its coat went back to the bench (`isolation_v039.md`, round 3).

## Round 2

The goat white (`TPDB_GOAT39` D, chosen in the bench's round 3), test 1's seed rebuilt (`design_tests_v039/round2/test_5.png`, prompt `tpdb_work/dtp39p2/test_5.txt`): the same picture with only the goat changed.

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 5 | Tier-3 park, test 1's seed | The white goat grazing at 135 | "a white goat with grey curved horns has its head down and is eating a tuft of grass"; "Its thin legs make the body look a little stiff or awkward, but it reads clearly as a grazing goat". The one thing left is the old one: "The odd part is a goat grazing loose in an ordinary town park, with no fence or owner" (v0.38's O3, for the pilot) |
