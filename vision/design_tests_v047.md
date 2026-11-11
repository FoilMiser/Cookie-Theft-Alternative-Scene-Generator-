# v0.47 design tests

The cast of builder 0.47.0 and the placement rules of revision 44 were read blind in whole test scenes (`tools/cycle/design_tests.py`, the v0.47 jobs), each picture by a fresh reader with the reader template, one picture to a reader, on Opus. Between them the seven forced sets hold every template of the v0.47 list: the four that failed v0.46's gate (R1 `dog_reading`, R2 `about_to_trip`, R3 `sweep_fork`, R4 `blocked_hose`), `bird_steals` (R5) and the three of R6 (`cat_stalks_bird`, `water_upward`, `lost_balloon`). The pictures were laid out in a shuffled order, so a test's number says nothing of its record. `design_tests_v047/map.txt` names each picture's record; it lay outside the folder until the readings were in.

| Test | Forced | Placed |
|---|---|---|
| 1 | A garden: water going up from the watering can (`water_upward`), the fence painted, leaves raked | first seed |
| 2 | A playground: a balloon lost (`lost_balloon`), a child on the slide, a ball kicked | first seed |
| 3 | A garden: the dog on the hose (`blocked_hose`), a box carried, a child on the swing | first seed |
| 4 | A park: the dog reading a newspaper (`dog_reading`), the bird at the sandwich (`bird_steals`), a kite flown | first seed |
| 5 | A street: the reading walker and the box (`about_to_trip`), an ice cream, a dog walked | first seed as first built; fourth seed as built again |
| 6 | A garden: sweeping with a fork (`sweep_fork`), flowers watered, a box carried | first seed |
| 7 | A park: the cat stalking the bird (`cat_stalks_bird`), a picnic, a reader on a bench | first seed, built twice |

## Two pictures were built again

**Test 7, before any reader had it.** The park picture as first built had the lamp's post between the stalking cat and its bird, in front of both, so the cat looked at a post. I saw it on my own look at the seven pictures. The rule that came of it is `POST47` B: nothing upright of the setting (a lamp, a tree, a feeder, the clothesline, the swing, the slide, a stall, the hose reel) stands in the span of the cat and the bird. The picture was built again on the same seed, and that second build is the only one a reader had. With the rule the template still places on 24 of 24 seeds in each of the four settings.

**Test 5, after its first reading.** The first build had the bearded man in green as the walker, a box at his feet and the street's tree in its planter just beyond his open book. The reader had the trip, and then a second hazard: "he could alternatively be about to bump into the tree". `TRIP47` B kept upright things away from the walker's back, where v0.46's reader had him heading for a post behind him; it said nothing of what stands ahead. `TRIP47` C adds that: nothing upright of the setting ahead of the walker either, from his middle to a body's width past the obstacle, over his whole height. With C the template places on 24 of 24 seeds in each of the four settings, as it did with B. The test's first seed and the next could no longer place the walker, the third could not place the dog's walker, and the fourth gave the picture that is test 5 now, with a different cast: the walker is the woman in the purple top. The first picture and its reading are kept beside it as `test_5_first.png` and `desc_test_5_first.md`. A fresh reader had the new picture and named one hazard only: "Just ahead of her on the ground, in the bottom centre, is a closed cardboard box, and she looks as if she is about to bump into it or trip over it." The tree is now behind her, and in the reading it is only "Tree in a round planter, left."

## What was read

**Every forced event was read**: twenty-one of twenty-one in the seven pictures as they stand, and three of three in test 5's first build, counted twice against the records' items. That is a count of what a reader of mine wrote about a picture built to show it; it is not the screen, where a scorer who has not seen the picture marks each item against the description.

**The reading dog** (R1, test 4). "a brown dog sits upright on the grass reading a newspaper it holds in its front paws, and it seems to be wearing glasses. That is impossible, because dogs can't read." It was a dog with "a red collar". The glasses were less sure than the dog: "The woman's glasses and the dog's glasses are tiny, so I'm not certain either of them is wearing glasses."

**The walker and the box** (R2, test 5). First build: "He is not looking where he is going, and a cardboard box sits on the ground just ahead of and below him, so he seems about to trip over it (the tree in a round planter is also right beside him)." Second build: "Cardboard box, bottom centre on the pavement, directly in the girl's path - an obstacle she is about to reach." The stride's direction, which the bench's readers could not always tell, was told here with a hedge: "her rear foot points back-left; most likely she is walking toward the right/front, towards the box". The filler crates by the fruit stand were not taken for a second obstacle: "Second cardboard box, right, beside the fruit stall - looks like stall stock or a crate."

**The fork** (R3, test 6). "is sweeping a little pile of dirt or gravel toward a red dustpan, but instead of a broom he is using a giant silver fork." And of what kind of fork: "Another reading is a garden fork or rake, but the shape (smooth rounded head with four thin tines) is clearly a kitchen fork, oversized."

**The dog on the hose** (R4, test 3). "a brown dog with a red collar is standing right on the hose (one front paw on or by a bulky connector piece), which looks like it is squashing the hose and blocking the water." The woman "is holding a garden hose up and pointing the nozzle forward, but no water is coming out". The reader's hedge is the swelling under the paw, which `HOSE47` D draws short and round so that it is not a puddle. The dog's "front paw is right at the bulky connector piece", and the reader gave the two readings as "dog stepping on the hose and blocking the water" and "dog just standing next to the hose fitting".

**The bird at the sandwich** (R5, test 4). "Next to her on the bench is a sandwich, and a small blue bird is beside it, pecking at it or about to take it while she doesn't notice." Under what was unsure: "The bird could be eating the sandwich, about to grab it, or just sitting next to it."

**The cat and the bird** (R6, test 7). "a grey cat is creeping or stalking toward the bird, low to the ground. It looks like the cat may be about to pounce on the bird." The bird "pecks at seeds or crumbs on the grass". The hedge: "could be stalking the bird to catch it (most likely reading), or simply walking or running along. Its pose is low and stretched, which suggests hunting."

**The water going up** (R6, test 1). "The odd thing is the water: instead of pouring down onto the flowers, it shoots up in a tall arc from the can's spout, with drops flying up above it, as if it were going upwards like a fountain." The second reading the reader offered: "it is meant as a spray/arc that will fall onto the flowers, but drawn too high and pointing the wrong way".

**The lost balloon** (R6, test 2). "a red balloon has floated away up and to the left of her. She is reaching up toward it with her other arm and looks upset, so she seems to have just let go of it by accident." The string: "The bottom of its string ends in mid-air a little above and to the left of her raised hand, not in it."

**The fence's painter** (O5, test 1). The teenager "is painting the fence blue with a paint roller on a long handle", and "A few fence boards next to him are already blue". v0.46's test had the roller read as held away from the paint. This one's remark is smaller: "it is slightly unclear whether he is painting the board he is touching (which still looks wooden near the roller) or has just finished."

**The moustache of the man in the red shirt** (O1, tests 5 as first built and 6). Eating an ice cream: "there are brown marks around his mouth that could be a moustache or ice cream/chocolate smeared on his face". That is O1 again, in nearly the screen's words. Sweeping with the fork he was "a boy in a red shirt and blue trousers", and that reader wrote nothing of his mouth. The moustache is the cue v0.39 gave him because he was read as a boy, so taking it off would trade one reading for the other; it stays, and O1 goes to the next list with both readings beside it. The older man's moustache was a moustache: "grey hair and moustache" (test 1), and in test 5 "grey hair, flat grey cap, moustache, white shirt with brown vest".

**The cast.** The woman in the yellow dress, the study's character: "a woman with a dark ponytail in a yellow dress" (test 3). The older woman's glasses were named in all three of her pictures, in test 4 with the doubt above: "An older grey-haired woman with glasses" (3), "an older woman with grey hair in a bun, glasses, a teal cardigan and a grey skirt" (1), "grey hair in a bun, glasses, teal cardigan, grey skirt, brown shoes" (4). The older man: "an older man in a grey flat cap and a brown waistcoat" (1), "An older man in a flat cap and brown waistcoat" (6). The teenager was "a boy" in all four of his pictures, in "a red cap and blue jacket" (1), "a blue hoodie, dark trousers and a red cap" (2), "a red cap and blue top" (4), "a red cap and blue hoodie" (7). The children: "a dark-skinned child in a yellow top and orange shorts" (2), "a girl in a pink dress" (2), "a small child in pink" (3). The woman in the purple top was "a woman with dark hair in a purple top and teal trousers" walking the dog (5 as first built) and "a girl with a dark ponytail, purple top and teal trousers" reading as she walks (5).

No reader named a neck, a shoulder, a stiff leg or a shadow. One remark is on a body's drawing: "The man's waistcoat/arm area is a bit cluttered; he may be holding the can with one hand while the other arm is bent, hard to tell exactly." (test 1).

## For the watch list

Nothing here was mended after the readings but the walker's rule; each of these goes to the screen and to the next list as it stands.

- The man in the red shirt: the moustache as "ice cream/chocolate smeared on his face" (5 as first built), and "a boy" (6).
- The woman in the purple top as "a girl" (5).
- The hose's swelling as "a bulky connector piece", and the hose at the holder's feet: "could read as wrapped round her legs (a tripping risk) or just lying behind her" (3).
- The stalking cat that could be "simply walking or running along" (7).
- The bird at the sandwich that could be "just sitting next to it", and "The sandwich could also be read as a hot dog or burger." (4).
- The bench's reader, whom `STEAL47` B turns away from the bird: "The bench looks short and the woman is sitting at its right end, partly over the edge. Her legs reach towards the path." (4).
- The dog's walker, in both builds of test 5: "the dog faces left while the woman's stride looks to be going right/forward", and "his body seems to face left toward the dog, but his stride could also be read as walking right".
- The glasses, "tiny" on the dog and on the older woman at a whole picture's size (4).
- The painter's board that "still looks wooden near the roller" (1).
- The water as "a spray/arc that will fall onto the flowers" (1).
- The balloon's string that "ends in mid-air a little above and to the left of her raised hand" (2).
- The swing's rider "close to the right-hand upright of the frame", where "it could look like the swing is near to hitting the post" (3).
- Small things: the leaves that "could read as leaves or as twigs/debris" (1); the ball that "looks small for a football" (2); the rock that "could also be read as a grey dome or helmet" (4); the bin that "looks slightly as if it floats or sits behind it" beside the lamp (7); the picnic blanket "drawn at a tilted angle" (7); the street lamp "very tall and thin relative to the people" (7).
