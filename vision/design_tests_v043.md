# v0.43 design tests

The cast of builder 0.43.0 and revision 41 were read blind in whole test scenes among other events (`tools/cycle/design_tests.py`, the v0.43 jobs), each
picture by a fresh reader with the reader template, one picture to a reader. `design_tests_v043/map.txt` names each picture's record.

| Test | Forced | Placed |
|---|---|---|
| 1 | A park: the trip, the reading dog, a kicker | first seed |
| 2 | A street: the trip, the reading dog, an ice cream | first seed |
| 3 | A garden: the hose stopped by a dog at 45, the goat grazing at 135, a raker | first seed (with the flowers watered instead of the raker, the set could not be drawn: the garden's one hose reel was the waterer's) |
| 4 | A playground: the dog begging at 45, the woman in yellow, a child on the slide | fifth seed |
| 5 | A park: the woman in purple taking a photo, a child with a balloon, the goat at 45 | fourth seed |
| 6 | A garden: a cat stalking a bird, a planter, a child on the swing | second seed |

**The trip and the reading dog** (tests 1 and 2). In both pictures revision 41 put the dog well away from the walker reading toward the box.
- The trip read in both: the grandmother is "about to bump into it or trip over it", and the woman in purple "about to trip over it because she isn't looking where she's going".
- The dog lying over its paper read as reading in both, and both readers named the contradiction. In test 1 it is "looking down at it as if it is reading the paper. That is odd, because dogs can't read". In test 2 it is "as if it were reading it, which is the oddest thing in the scene".
- Each reader also offered a second reading: "Or it may just be lying on or pawing at a newspaper someone dropped", or "pawing at or about to chew it". The screen will say what that costs under the strict count.
- No reader said the paper stood by itself or that the dog looked like a person.

**The hose and the goat** (test 3).
- The dog stopping the hose read in full.
- The goat, at 135 at the back of the garden, was "apparently tied by a thin cord to a small stake in the ground". It was still "A goat in a small suburban back garden is a little unusual, but not impossible", which is as softened as v0.42's garden goat.

**The begging dog and the woman in yellow** (test 4).
- The dog at 45, its mouth closed, begged "as if begging for her ice cream".
- The other eater, a boy walking off with his own ice cream, was kept outside revision 40's zone, and the reader did not link him to the dog.
- The woman in yellow was "a woman with dark hair in a yellow dress sits on a wooden bench".

**The woman in purple and the goat at 45** (test 5).
- The goat was tethered, though the rope "could also be read as a loose rope just lying on the grass next to a peg".
- The woman in purple, taking a photo with her back half turned, was "a person with long dark hair": "Photographer's gender: long hair suggests a woman, but it is not certain". In test 2 she was "a young woman with dark hair in a ponytail". No reader in the six called either woman a girl.

**The stalking cat** (test 6), now in profile only, read as stalking. But on the ground its face was "right up against a small red bird", so "either (a) the cat is about to pounce and catch the bird, or (b) it already has the bird at its mouth".
- In profile the cat's whole length reaches toward the bird, where at 45 it was foreshortened.
- Revision 41 now keeps a gap of 45 units between the cat's front and the bird. The rule placed 12 of 12 seeds in the garden and in the park (`tpdb_work/place43.py`).
- The picture was rebuilt (test 6b). This time the cat placed on the fence, and a fresh reader had it "creeping along the top of the fence towards a small blue bird", "about to pounce on the bird".
- The woman in yellow, kneeling at the flowers with a pot, was "as if planting, weeding or picking flowers". This is the strict count's hedge on `plant_flowers` (`flaws_v042.md` R3), not drawn this time: it has five probes in the screen.
