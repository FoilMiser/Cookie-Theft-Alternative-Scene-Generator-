# v0.56 design tests

Placement revision 50 holds the list's placement rows (P1 to P10 of `flaws_v055.md`) and five rows that a rule answers better than a drawing (I5, I6, I9, I10, and part of R3 and I1). Each rule is behind a switch of its own (`scene.sw56(NAME)`; the names are in the header comment of `scenegen/scene.py`). The rules were read in whole pictures built for them: nineteen new pictures with forced sets under revision 50, two fresh readers each, dealt among the 268 readings of the drawings' bench as its arm F (`isolation_v056.md`; the pictures are `isolation_v056/bench/blind/pic_NNN.png`, the descriptions `desc_pic_NNN.md`, and `isolation_v056/digest/F_list.md` says which is which and what each was built to test). A sixth analyst read the 38 descriptions whole and wrote, for each thing a picture was built to test, what both readers said of it (`digest/digest_F.md`). Round 2 read the one rule that failed, mended, in three more pictures (`isolation_v056/bench2`).

## Round 1: nineteen pictures, 38 readings

| Rule (switch) | The fault it is for | Pictures | The fault named | Read as intended, with no doubt |
|---|---|---|---|---|
| The ladder's top third against open sky, no lamp post in its park (`LADDER`) | a support behind it: the hedge's line, a tree, the lamp | 1 | 0 of 2 | 2 of 2 |
| The picnic's blanket half as large again, sitter and basket in its middle (`PICNIC`) | the sitter half off the blanket | 2 | 0 of 4 | 4 of 4 |
| The pond's shore, and figures of other events clear of the pond (`BANK`, `PONDFIG`) | a figure standing in the water, or over it | 3 | 0 of 6 | 6 of 6 |
| A duck 120 units from an angler's float (`FLOAT`) | a duck going for the float | 1 | 1 of 2 | 1 of 2 |
| A walker's lane 70 units deep behind and 30 in front (`LANE`) | a walker heading at another event's bird or thing | 1 | 1 of 2 | 1 of 2 |
| The arm that reaches for the blown hat clear of the gate (`HATHAND`) | the hand on the gate | 1 | 0 of 2 | 0 of 2 |
| The jumper 150 units clear of the swing and the washing, never with a balloon (`REACH`) | the jumper reaching for the swing, the washing or a balloon | 2 | 0 of 4 | 1 of 4 |
| The lost balloon's string above the playground's railing (`BALLOONUP`) | the string caught in the rails | 1 | 0 of 2 | 2 of 2 |
| The photographer's subject near, at the same depth, alone on that side (`PHOTO`) | not knowing what the camera is aimed at | 2 | 4 of 4 | 0 of 4 |
| The street's sun 32 units lower (`SUN`) | the sun cut by the picture's top edge | 1 | 0 of 2 | no reader mentions the sun |
| The dropped ice cream at least 120 units in front of the horizon (`DROPFRONT`) | far back and small | 2 | 0 of 4 | 4 of 4 |
| A pram's wheels on the path (`PRAM`) | the pram on the grass | 1 | 0 of 2 | 2 of 2 |
| The garden's bird table out of the storm pointer's line (`RAINLINE`) | the bird table as what is pointed at | 1 | 0 of 2 | 2 of 2 |
| No raised hand within 250 units of the floating box (`BOXHAND`) | the box thrown by a figure | 1 | 2 of 2 | 0 of 2 |

What the readers wrote:

- **The ladder (I9).** v0.55's short ladder ended at the hedge's line, and four readers of nine in the drawings' bench offered a support behind it: "The ladder's top reaches into the background hedge line, so it might be read as leaning on the distant hedges, but they are far behind it." The long ladder, its top third on open sky: "In the middle of the grass, a tall wooden ladder stands upright on its own, leaning against nothing, which is impossible." Neither reader offered a support. The one gap between the park's lamp post and its big tree was 111 units wide, too narrow for the rule, so the planner leaves the lamp post out of the ladder's park.
- **The pond (P1).** In v0.55's pictures a doubt whether a figure stood in the water, at its edge or over it was in 5 readings of 13: "The woman is standing on the grass but the pond edge seems to reach right up to/behind her legs, so she could be read as standing at the very edge or partly overlapping the water." With the sandy shore drawn and nothing else changed it was in 4 of 28, and in the new pictures, where figures of other events also keep clear of the pond, in none of 10 (the six above and four more in pictures of the drawings).
- **The picnic (P8).** On the small blanket of v0.55's pictures built again: "The boy sits mostly off the blanket, with his body at its edge and his legs on the grass. He could be sitting on the blanket's corner or on the grass beside it." On the larger one nobody wrote of it in four readings.
- **The storm pointer (I5).** In v0.55's gardens the bird table was a second target in 7 readings of 12: "The older woman's pointing could be at the storm clouds (warning of rain) or at the birdhouse, which is close to her raised arm; I read it as pointing at the clouds." With the bird table out of the arm's line both readers had the clouds and nothing else.
- **The hat and the jumper.** No reader put the hand on the gate. Both doubted the hat itself ("could be reaching to grab the cap or waving/pointing at it"), and both tied the jumper to it: "In the front centre a boy in a yellow shirt and orange shorts jumps with both arms raised, as if leaping to catch the hat or cheering." The jumper was clear of the swing as the rule asked and found the next thing in the air. A rule was added for it (below).
- **The floating box.** No hand was within 250 units of it, and the jumper's raised arms had it all the same: "The floating box: it might have been thrown up by the jumping boy (he has his arms up as if he has just tossed it or is about to catch it), or it may simply be floating impossibly. It is far above him and to the right." In v0.55's pictures, where nobody jumps, seven readers of eight wrote that no one is near enough to have thrown it.
- **The photographer (P9).** With the subject near and alone on its side all four readers still asked: "The photographer's camera points out of the picture rather than at any particular person, so it is unclear what she is photographing." The figure is drawn at three-quarters, and its lens faces the viewer. Mended in round 2.
- **The duck and the float, the walker and the fed birds.** One reader of two each: "The duck is fairly close to the fishing line; could be read as the duck being near the hook." and "The old woman is walking close behind the boy and the birds; she could be about to walk into the birds, or simply passing by." Both are single lines among the things a reader was unsure of. At 150 units from the float a duck and an angler shared a pond on 1 seed of 12, at 110 on 7; the gap is 120, and the rules stand as they are.

## Rules added after round 1

- **A child jumping for joy is never in a picture with a hat the wind took or with a floating box** (`REACH`, the tags `jump_hat` and `jump_box` of `templates._Ex56`), as it already was never with a held balloon or a lost one. These are exclusions in the plan, so no picture needs reading for them.
- **The photographer is drawn from the side** (`PHOTO`, `templates.Photo.bind`), the camera along the picture and straight at its subject. Revision 8 had turned the figure to three-quarters, when its head read as a plain dark round shape; the cast has been drawn again since, and from the side the face shows in profile behind the camera.
- **A bicycle with nobody free to hold it is not placed** (`BIKEFALL`), since leaning on a post it read worse than on its stand (`isolation_v056.md`).

## Round 2: the photographer from the side, three pictures, 6 readings

The two pictures of round 1 built again on their seeds, and a third in the park, two fresh readers each (`isolation_v056/bench2`, arm P of `bench2_map.json`).

| Picture | Reader | What the camera is aimed at |
|---|---|---|
| Playground | 1 | "The woman with the camera: could be photographing the girl, the escaping balloon, or something else to the left." |
| Playground | 8 | "The woman's photo subject: she faces left, so she may be photographing the girl (perhaps the moment the balloon escapes), or just the playground generally." |
| Street | 2 | "Who the photographer is photographing is unclear — he faces left, possibly toward the girl with the balloon or just the street." |
| Street | 9 | "What the photographer is photographing is unclear: it could be the girl with the balloon, the stall, or the old man; his camera points left, roughly toward the girl/lamppost." |
| Park | 3 | "What the photographer is photographing: probably the running boy with the balloon, or possibly just the view to the right." |
| Park | 10 | "What the photographer is photographing is unclear: he points right, possibly at the boy with the balloon or at the trees/scenery." |

All six readers say which way the camera points and name the intended subject first; no reader has it pointing out of the picture. All six still offer something else beside it. P9 is mended as far as a rule mends it: a reader will not say what a camera sees.

## What the rules cost

Seeds placed of twelve with the band off, the rule on and off (`tools/cycle/yield_set.py`, before the photographer was turned): a pram alone in the park 7 and 12, in the playground and the street 12 and 12; a photographer with a dog walker and a balloon 7 and 10 in the park, 8 and 11 in the playground, 9 and 10 in the street; the jumper with the washing 8 and 9; the lost balloon in the playground 11 and 11; the dropped ice cream, the windy hat and the jumper with a swing 12 and 12. The ladder with an angler placed on 13 seeds of 24 for 10. On v0.55's four tier-4 sets, six seeds each, all rules on and all off: park 4 and 4, street 5 and 5, playground 3 and 3, garden 5 and 4.

**No figure's ground line lower than 970** (P2, `EDGE`) was first written for the figure's box, whose foot lies 3 to 10 units under the ground line and up to 39 for a sweeper. By the box the rule took the ground's front strip: a grown figure's raised hand clears the garden's fence only from there, and a wave placed on 2 seeds of 8 for 5, the street's tier-4 set on 2 of 6 for 5. By the ground line it costs nothing.

## Left as they were

- **Lamp posts and bins at the path's edge** (P6): two hedged remarks in 297 readings of three screens.
- **More of the wind** (I6): the wind is drawn four ways since revisions 9 to 12, and the doubts that are left are of the hat and the hand, not of the wind.
- **The painter's long step** (P10): it went with the pose that the pairs did not take.
