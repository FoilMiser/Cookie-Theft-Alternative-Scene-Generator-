# v0.46 design tests

The cast of builder 0.46.0 was read blind in whole test scenes (`tools/cycle/design_tests.py`, the v0.46 jobs; the placement rules are revision 43's,
as they were), each picture by a fresh reader with the reader template, one picture to a reader, on Opus. `design_tests_v046/map.txt` names each
picture's record; it lay outside the folder until the six readings were in. By the harness's count each reader made three tool calls, which opening
the picture, writing the description and handing it back account for.

| Test | Forced | Placed |
|---|---|---|
| 1 | A street: an ice cream, a photographer, a sweeper; the rule asks for the ice cream in the hand of the woman in the yellow dress | 6th seed (five built and turned down by the rule) |
| 2 | A park: a reader on a bench, a dog walked, birds fed; the rule asks for the woman in the yellow dress as the reader | 5th seed (two built and turned down by the rule, two not built) |
| 3 | A garden: flowers watered, leaves raked, the fence painted; the rule asks for the older woman in glasses in the picture | third seed |
| 4 | A street: a box carried, a wave, a shopping bag carried; the rule asks for the worker in the safety vest | 7th seed |
| 5 | A playground: a ball kicked, a child on the slide, a reader on a bench; the rule asks for the teenager | first seed |
| 6 | A park: an angler, a pram pushed, birds fed; the rule asks for the older man with the moustache | second seed |

Two forced sets were changed before a picture came of them. Test 3 was first written with flowers watered, flowers planted and leaves raked, and
test 6 with an angler, a picnic and a pram: on all 80 seeds the garden could not place the waterer or the planter, and the park could not place the
picnic. The planter became the fence's painter and the picnic the feeding of birds. Both sets are on the list as things the generator cannot draw
together.

All six forced sets are plain events. The release changes how the cast is drawn and leaves the rules alone, so no contradiction and no inference
module was forced here; those are the screen's to read.

Nothing that had to be fixed came out of the readings, and no picture was built again.

**Every forced event was read**, eighteen of eighteen, counted twice against the records' items. Of the pictures as wholes: "Nothing looks clearly
impossible" (tests 1 and 4), "Nothing in the scene looks clearly impossible" (2), "Nothing looks dangerous or about to go wrong" (3), "Nothing seems
obviously impossible" (5), "Nothing looks clearly wrong or impossible" (6).

**The woman in the yellow dress** (tests 1, 2, 3, 5 and 6), whose neck the release shortened. No reader named her neck. With the ice cream: "a woman
in a yellow dress walks towards the right, holding a pink ice-cream cone up near her face", "as if about to lick it". On the bench: "a dark-haired
woman in a yellow dress sits on a wooden bench reading a red book" (2), "sits on a wooden bench reading a red book" (5). Fishing: "stands at the edge
of a blue pond holding a long fishing rod. Her line runs to a red-and-white float bobbing on the water". Raking, bent over the rake at the picture's
front edge, she was "a girl in a yellow dress" (3). One reading of five; v0.45's screen had one "a girl (or young woman) in a yellow dress" as well,
of her sweeping in a garden. She stands a little shorter in the neck now, so the screen's readings of her are to be counted for it.

**The mouths.** No reader wrote of blood, a cut or a wound, or of a mark on a cheek. Two remarks name a mouth. Of the dog's walker, who has a
moustache: "The man's face has a small dark mark around the mouth or chin, which could be a moustache or beard" (2). Of the waving man: "his mouth
looks open as if he is calling out", and under what was unsure, "could mean calling out or just a neutral expression" (4).

**The fence's painter** (test 3), the older woman in glasses: "an older woman with grey hair, glasses, a teal top and a grey skirt is using a paint
roller on a long handle to paint the wooden fence blue. A paint tin stands on the grass by her feet". The glasses were glasses. The roller drew the
reading's one strong remark: "The odd thing is that the woman is holding her roller up in the air to her left, well away from the blue part of the
fence", and "The roller head seems to hover slightly in front of the fence rather than pressing on it". In the picture (`tpdb_work/v046/z21_paint.png`)
the roller lies on the board at the paint's edge, and that board is blue from the roller down, as revision 43 draws it; the two boards that are blue
to the top are to its left. This is O2 of v0.45's list, where a design test's reader had the painted boards "slightly away from where the roller
touches". The cast's drawing did not change it and v0.46 does not mend it: it stays on the list, with a second and stronger reading.

**The worker** (test 4): "a younger man in an orange cap and an orange high-visibility vest walks to the right carrying a cardboard box, like a
delivery worker"; the vest's bands are "reflective stripes".

**The older man** (tests 1, 3, 4 and 6): "an older man in a flat cap, brown waistcoat and white shirt sweeps a small pile of brown leaves with a
yellow broom" (1); "watering a round flower bed of colourful flowers with a teal watering can" (3); "walks to the right carrying a yellow shopping
bag" (4); "holding a paper bag and scattering seeds or crumbs, and a small red bird is pecking at them by his feet" (6). The moustache was a
"grey moustache" (3) and "grey hair and moustache" (4), and was not named in tests 1 and 6. v0.45's design test of him in profile had "could also
look like he has food in his mouth"; no reader wrote that of this drawing.

**The teenager** (tests 2 and 5): "a boy in a red cap and blue hoodie" (2), "a boy in a red cap, blue hoodie and black trousers" (5). Feeding birds: "holds a small brown paper bag and sprinkles crumbs or
seeds onto the ground, where a blue bird and a red bird are pecking at them". Kicking: "the ball is just leaving his foot, motion lines are drawn
under his leg".

**The others.** The photographer "holds a camera to her eye", with "a red camera strap" (1). The dog's walker "walks a white dog with brown spots.
The dog is on a red lead" (2). The child "in a yellow top and orange shorts is sliding down it with one arm raised" (5). The waving man: "Small
motion marks next to his hand suggest he is waving" (4). The pram: "pushing a teal-and-navy baby stroller. A baby with its eyes closed, covered by a
pink polka-dot blanket, is sleeping in the stroller" (6).

For the watch list: the roller "well away from the blue part of the fence" (test 3); the woman read as "a girl" (3); the dog walker's arms that
"stretch back and down to hold the lead, a little stiffly" (2); the bird feeder's bag "near or overlapping his body/hip, so it is a little unclear
which hand holds it" (2); the pram's pusher who "could be walking quickly or jogging/running" (6); the fishing line that "does not look connected to
the rod tip exactly at the top" (6); the blanket that "could also be read as a pink pillow or bag" (6); the bench sitter whose "legs and the bench
slats overlap slightly in a way that makes the bench look a little thin in front of her" (5); the street's bench, whose "backrest looks drawn above
and slightly separate from the seat" (1); the leaf pile that "could also be read as twigs or dirt" (1); the camera strap "a little hard to make
out" (1).
