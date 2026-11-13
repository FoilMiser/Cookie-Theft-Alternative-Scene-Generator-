# v0.50 design tests

The cast of builder 0.50.0 (marks of age and smaller heads on the grown figures, the balloon's string, the painter's pole) and the placement rules of revision 47 (the seesaw's seat and grab bar, the lost balloon's string, the goat's stake) were read blind in whole test scenes (`tools/cycle/design_tests.py`, the v0.50 jobs), each picture by a fresh reader with the reader template, one picture to a reader, on Opus. The bench (`isolation_v050.md`) had read each change on its own; here a reader has them at a picture's size, among other things. Between them the eight forced sets hold nine of the ten people.

| Test | Forced | Placed |
|---|---|---|
| 1 | A playground: two children on the seesaw, a photographer, a pram pushed | second seed |
| 2 | A playground: the heavy seesaw (`seesaw_heavy`), a runner, an ice cream | first seed |
| 3 | A garden: a balloon lost (`lost_balloon`), the fence painted, the path swept | first seed |
| 4 | A park: the goat grazing, a balloon held, a reader on the bench | first seed |
| 5 | A street: an ice cream, a dog walked, a shopper | first seed |
| 6 | A garden: the hose stopped by a dog (`blocked_hose`), a box carried, a child on the swing | first seed |
| 7 | A park: a runner, a photographer, a picnic | first seed |
| 8 | A playground: a child on the slide, a wave, a pram pushed | first seed |

One forced set was changed before any picture of it existed: test 1 had a shopper, who cannot be forced in the playground, and has a pram in the shopper's place. Test 8 was built twice before any reader had it. On my look at the eight, its empty seesaw had the old T handles where a ridden seesaw now has grab bars (`isolation_v050.md`, the seesaw); the empty one was given the same bars (`settings.SEESAW50`) and the picture built again on its seed. I found nothing else to mend, and no picture was built again after a reading.

## What was read

**Every forced event was read**: twenty-four of twenty-four in the eight pictures. That is a count of what a reader of mine wrote about a picture built to show it; it is not the screen, where a scorer who has not seen the picture marks each item against the description.

**The seesaw** (O2; tests 1 and 2). Each rider sits and holds: "She is sitting on the raised left end of the seesaw, holding the handle." (1); "They are sitting on the low right end of the seesaw, holding the handle." (1); "where a small girl in pink sits holding the handle" (2). Neither reader has a rider above the plank: "Nothing appears to be floating or passing through anything else." (1, 2). The heavy seesaw is read through to its point, "almost as if she is stuck up high while the man ignores her", with the call's old hedge: "her hand at her mouth could mean fear or distress at being stuck up high, surprise, or simply that she is eating or calling out". The grown rider's seat is v0.31's note still: "he might be sitting on the low end of the plank, or on the ground right next to it".

**The slide** (test 8), left as v0.49 had it after three benched placements read no better: "is sliding down a red-framed slide with a yellow chute". This reader has nothing on how the child sits.

**The lost balloon** (R1; test 3; the string's end a head's height above the hand, over the garden's fence). "The red balloon looks like it has escaped, and its string is trailing down out of his reach." And the second reading is still offered: "it could have just slipped out of the boy's hand and be floating away (he is reaching for it). Or it could be loose and unrelated to him." The nearer end has not ended that; it is one picture.

**The stopped hose** (R2; test 6; v0.49's drawing, kept by the bench). "If the dog is on the hose, it may be stepping on it and blocking the water, which could explain why the boy seems to be looking at the nozzle."

**The goat's stake** (O4; test 4). "The goat is tied by a rope to a short wooden stake in the ground." Tethered, and the stake still short to this reader; "It looks tied to the stake, but it is hard to tell how tight or secure the knot is."

**A held balloon's string** (O5; test 4). "is walking or running to the left while holding the string of a red balloon". No stick.

**The painter's pole** (O3; test 3). "She holds a long-handled blue paint roller up against the fence." The reader's doubt is where the roller is, not what it is: "the woman is holding the roller over plain, unpainted wood, although the blue section is to her left, a little away from her".

## Who the figures were called

The four grown figures that v0.49's screen had called young in 20 of 89 pictures appear ten times in the eight pictures, by the screen's own rule (`who_cmp.py`: the first inventory line that names the figure's clothes).

| Figure | Called |
|---|---|
| The woman in purple | "woman with dark hair, purple top, teal trousers, black shoes" (1); "Woman, centre-right, front of the pond: dark hair, purple top, teal trousers, dark shoes." (7) |
| The woman in the yellow dress | "Woman, centre-left, mid-ground: dark hair, yellow dress, red shoes." (2); "Woman (right, front, on the path): dark hair, yellow dress." (3); "woman with dark hair in a ponytail, wearing a yellow dress and red shoes" (5); "Woman, left-centre front, on the path: long dark hair, yellow dress, red shoes, red camera strap." (7) |
| The man in the red shirt | "boy or young man with brown hair, in a red T-shirt and blue trousers" (5); "Man, centre-left, mid-ground: brown hair, red T-shirt, blue trousers, black shoes." (7) |
| The man in green | "man with a beard and short dark hair, green t-shirt, beige trousers, brown shoes" (1); "Black man with a beard in a green T-shirt and beige trousers." (8) |

One of ten is young first, the man in the red shirt striding with an ice cream at his mouth, where the cone hides his moustache: "The person with the ice cream could be a teenage boy or a young man." v0.49's design tests had four of nine. The woman in yellow is a woman when she runs (2); the one figure the bench left young was the woman in purple running. The beard is named in both of its wearer's pictures. The teenager is "a boy" in all three of his pictures (2, 4, 6), which is what he is.

## What the tests did not show

- Ten appearances are few. The count that stands is the bench's (1 of 45, for 13 of 45 with v0.49's cast, `isolation_v050.md`), and the screen will make its own.
- The lost balloon keeps its second reading in the one picture that has it.
- No reader wrote of a head's size or of a figure's shape, here or on the bench: what the smaller heads and the marks changed is what the figures were called.
