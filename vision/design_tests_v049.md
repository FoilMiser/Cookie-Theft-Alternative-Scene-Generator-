# v0.49 design tests

The cast of builder 0.49.0 (every person's head with a jaw and a chin on a neck of its own, the wider moustache, the ice cream at the mouth) and the placement rules of revision 46 were read blind in whole test scenes (`tools/cycle/design_tests.py`, the v0.49 jobs), each picture by a fresh reader with the reader template, one picture to a reader, on Opus. The bench (`isolation_v049.md`) had read the heads in rows and in pairs and the figures alone; this is the first time a reader had them at a picture's size, among other things. Between them the eight forced sets hold nine of the ten people, the storm watcher twice, the ice cream four times and the goat on its rope.

| Test | Forced | Placed |
|---|---|---|
| 1 | A garden under storm clouds: the watcher (`rain_coming`), the fence painted, digging | first seed |
| 2 | A park under storm clouds: the watcher (`rain_coming`), an ice cream, a reader on the bench | first seed |
| 3 | A street: the reading walker and the box (`about_to_trip`), an ice cream, a dog walked | first seed |
| 4 | A park: the goat grazing, a game of catch, a picnic | twelfth seed |
| 5 | A playground: an ice cream, a ball kicked, a balloon held | first seed |
| 6 | A street: the dog begging (`dog_begs`), the path swept, a bag carried | first seed |
| 7 | A garden: washing hung, the cat on the fence, a raker | first seed |
| 8 | A park: birds fed, a kite flown, a reader on the bench | first seed |

Two forced sets were changed before any picture of theirs existed, because the first could not be cast or placed: test 5 had a child on the swing, which is the garden's event and not the playground's, and test 7 had the flowers watered beside the washing, which placed on none of 80 seeds (the washing with the cat places on two seeds of eight: it needs a garden with room by the line). No picture was built again, before a reading or after one. I looked at all eight before a reader had them and found nothing to mend.

The eight were built while revision 46's edge rule (`scene.EDGE49`) still kept every figure 14 px off the picture's foot. It was narrowed to animals afterwards, when the set showed what it cost (the revision's header in `scenegen/scene.py`). The rule decides where a figure may stand and not how anything is drawn, so the readings stand as readings of the cast and the templates; the pictures here are kept as they were read, and these seeds would not all give them back under the narrowed rule.

## What was read

**Every forced event was read**: twenty-four of twenty-four in the eight pictures. That is a count of what a reader of mine wrote about a picture built to show it; it is not the screen, where a scorer who has not seen the picture marks each item against the description.

**The storm watcher** (R1, tests 1 and 2; the pointer, after the bench had read the open hand worse). Both readers went on to the rain. Test 1: "with three dark storm clouds overhead, so it looks as if it might rain soon", and of the woman, "points up at the sky, as if pointing out the dark clouds or warning that rain is coming." Test 2: "which suggests rain may be coming". Both also hedge what the finger is on: "She is most likely pointing at the storm clouds, to warn about rain, but she could also be pointing at the fence or gate." The hedge is the template's old one; the rain is said in both.

**The ice cream** (R5, tests 2, 3, 5 and 6). Eaten in two with no hedge: "walks along eating a pink ice-cream cone" (3), "sits on a wooden bench eating a pink ice-cream cone" (6). Hedged in two: "is licking or holding a pink ice-cream cone" (2), "It is unclear whether the girl is licking the ice cream or just holding it near her face." (5). v0.48's screen had the eating doubted in eight of twenty pictures; half of four is no better a share, and each of the four has the eating first. The screen will count it.

**The walker and the box** (test 3). "A cardboard box sits on the pavement right in front of her, so she looks about to trip over it." The hedge of v0.48's list is still there: "it looks to be right in her path but it might sit slightly to her right."

**The goat's rope** (O5, test 4). Read as what it is: "its lead hangs down to a small stake or peg in the ground". And still slight at a picture's size: "it is a thin line and the peg is small, so it could be missed or read as a stick".

**The dog begging** (test 6): "looking up at the boy as if begging for the ice cream".

## Who the figures were called

The four grown figures that v0.48's screen had called young appear nine times in the eight pictures.

| Figure | Called |
|---|---|
| The woman in purple | "a woman in a purple top and teal trousers" (1); "a girl with a dark ponytail, purple top and teal trousers" (5) |
| The woman in yellow | "a girl or young woman in a yellow dress" (8) |
| The man in red | a man (6); "a boy in a red shirt and blue trousers" (7) |
| The bearded man in green | "a man with dark skin and a beard" (2); a man (4, 6); "a darker-skinned boy in a green shirt and beige trousers" (7) |

Four of the nine are called by a young name first; v0.48's design tests had two of six. The new head has not changed it, as the age bench had said it would not. In test 7 both men are small and far and both are boys; in test 2 the same bearded man stands in front and his beard is the first thing said of him, which no reader of v0.48's eighty-seven pictures said. The older woman and the older man are an older woman and an older man each time (1, 3, 4, 8), and the teenager is a boy in all six of his pictures.

## What goes on from here

Nothing was mended after the readings. The ice cream's hedge, the box "slightly to her right", the rope "a thin line" and the grown figures called young go to the screen as they are, and to `flaws_v049.md` if the screen has them too.
