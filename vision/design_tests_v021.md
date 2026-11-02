# The v0.21 changes, read blind in whole test scenes

v0.21 changed no drawing, so there was no isolation bench: every change is a placement rule (revision 19). The rules went
into whole scenes, with the other events around them, and were read blind there before the set was regenerated, as in
v0.8 to v0.20. Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v021/`; `map.txt` names the scene behind each
picture.

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (garden, rain coming) | Painting the fence with no worker's vest in the garden and no washing on the line; watering by can with no hose reel near, the stream well inside the bed; a dog bowl by a playing dog | The painter "a girl with a brown ponytail in a blue hoodie"; no line, no reel; the water "falling from the can onto the middle of the flower bed"; "a red bowl of dog food sits on the grass to its right", "the food bowl nearby doesn't seem to be part of the action" |
| `test_2.png` (garden, rain coming) | Someone hanging the washing: heads clear of the hung clothes, only the jeans already on the line; a kick clear of others | "A man in a red shirt and blue jeans is stretching up to peg a white T-shirt onto a washing line, where a pair of blue jeans already hangs"; the ball "just leaving his foot". No overlap remarked: "the man in front of the washing line" |
| `test_3.png` (park, tier 4) | The pond: the duck feeder, the bird feeder and the photographer off the cattails and the rim | The duck feeder "stands to the right of the pond by a tall black lamp post ... reaching his other arm out towards the water"; the two women "overlap the pond's outline. Their feet are on the grass in front of it, so they read as standing at the bank"; no cattail remark |
| `test_4.png` (park) | The angler at the pond; a runner; a reader on the bench | "A woman ... stands at the right edge of the pond, facing left, and is fishing"; "her legs and feet are drawn over the lower edge of the pond, with her feet and shadow on the grass below it. The usual reading is that she stands on the grass in front of the pond"; no cattail remark |
| `test_5.png` (playground) | A kick with its line clear of the sandpit and of the people | The ball "heading off to the right, away from the other children"; "the ball is kicked towards the right, where there is nobody" |
| `test_6.png` (street, tier 4) | Walkers of different events kept off each other's heads and shoulders up to 80 px apart in depth | Box carrier, reading walker, dog walker, the girl with the dropped ice cream and the pram pusher each described on their own; no overlap of figures remarked ("no obvious impossible elements"). The girl "holds an empty ice-cream cone and rubs her eye as if crying. Her ice cream ... has fallen onto the ground"; the only crowding was the pram pusher's head over the fruit crates of the stall behind him |
| `test_7.png` (garden, tier 4) | The blocked hose with no spare watering can, no worker's vest; paint tracks, sweeping, catch, raking | "Only a single drop of water is coming out. A white dog with brown spots is standing on the hose"; "a trail of blue paw prints from the paint tray"; the painter "a woman in a purple top"; no can in the picture, no remark on the reel |

Every rule read as meant. No reader saw a worker's vest in a garden, a hose reel or a spare can beside someone
watering, a bowl away from a dog, a head among the hung washing, a figure in the cattails or out on the water, walkers
on each other's shoulders, or a kick aimed at the sandpit. The washing line read as "a white T-shirt" being pegged
"where a pair of blue jeans already hangs"; the can's water fell "onto the middle of the flower bed". Two readers said
people at the pond's front edge "overlap the pond's outline", each adding that their feet and shadows are on the grass,
"so they read as standing at the bank". Nothing in the test scenes called for another change.

One test scene had to be split before it could be built: duck feeding and fishing together in a tier-4 park placed in
none of four seeds under revision 19 (one of four under revision 18, the two of them crowding the pond's rim). Each
placed on its own with the other park events, as in `test_3.png` and `test_4.png`.
