# v0.51 isolation bench

The brief for v0.51 was Sam's "go for v0.51!", with nothing in the pictures named, so the work is the list of `flaws_v050.md`: the two templates that failed v0.50's gate, the game of catch (R1) and the square wheel on the wheelbarrow (R2); the thief bird (R3), the stopped hose (R4), the bread for the ducks (R5) and the hedged full marks (R6); and the oddities O1 to O9. This file is the bench: what was tried on its own, what blind readers wrote of it, and what was taken. The whole scenes are in `design_tests_v051.md`.

Every reader was a fresh one that saw only its pictures. Each change is behind a switch whose "O" is v0.50's drawing (`TPDB_<NAME>51` in the cast, `templates.<NAME>51` in the scene), and every old and new drawing was read on the same seeds.

| | Tried | Taken |
|---|---|---|
| R1 the game of catch | the ball early on its path, with three solid lines behind it or on its dashed arc (`templates.CATCH51`); the catcher's two open hands and the thrower's planted feet (`TPDB_CATCH51`) | **the early ball on its dashed arc, and the poses** |
| R2 the square wheel on the barrow | no hose by the barrow (`BARROW51`) | **taken**; the wheel's own drawing left |
| R4 the stopped hose | the swelling ending short of the paw (`PAW51`) | none: v0.50's |
| R5 the bread for the ducks | a slice of bread in the feeder's hand (`BREAD51`) | **taken** |
| O1 the lost balloon's string | its end off the fence's rails, the backdrop's lines and the pond (`LOST51`) | **taken** |
| O2 the man in the red shirt | the moustache as wide as on v0.49's head (`TPDB_MOUST51`) | none: v0.50's |
| O3 the fence painter | the tin at the heel (`TIN51`); the roller's caps in a dark blue (`TPDB_ROLLER51`) | **both** |

## The game of catch (R1)

`play_catch` had 0.80 in v0.50's screen and failed its gate on two pictures of five. In both a small girl throws to the woman in the yellow dress, and one reader of each had the woman throwing, or either of them.

### Round 1, cut out

Nine cut-outs on three seeds, each with a child throwing to a grown catcher (the bench's rule `catchpair`): v0.50's drawing (O); the ball a third of the way along its path with three solid lines behind it, as behind a runner, and v0.50's poses (A); and that with a first drawing of new poses (B), the catcher's hands apart with the upper one raised palm out, and the thrower on two planted feet.

| Case | Drawn | What the readers said |
|---|---|---|
| `pcrO_1` to `_3` | **O**: v0.50 | The child the thrower in three of three, and no doubt of the direction: "A dashed line traces the ball's arc from her hand up to the ball, which is at the top of the arc near the wall." (iso_14). The catcher's hands in all three: "The woman's hands are clasped together rather than cupped open, which could read as clapping or praying instead of catching." (iso_05) |
| `pcrA_1` to `_3` | **A**: the ball early, three solid lines | The child the thrower in three of three, and the other way offered in all three: "however, the woman's outstretched arms could also read as her having just thrown it to the boy." (iso_09). The hands again: "so she could be read as about to catch or as clapping/praying." (iso_27) |
| `pcrB_1` to `_3` | **B**: A, with the first new poses | The child the thrower in three of three, the other way offered in two: "but it could also be read as the man having thrown it to her (the lines are short and ambiguous in direction)." (iso_19). The raised palm in all three: "This could read as getting ready to catch, or as waving or fending the ball off." (iso_15) |

The cut-outs do not show the fault. All three readers of v0.50's own drawing had the child throwing, where the screen's readers of two whole pictures had not: a pair cut out of its picture is easy. What the round did say is that the solid lines are no clearer than the dashed arc, of which no reader doubted where it began, and that both catchers were wrong: the old one's hands closed together, the new one's palm a wave. The catcher was drawn a third time, both arms reaching toward the ball and the two open hands one above the other with room for it between them, and the question went to whole scenes.

### In whole scenes

The two pictures that failed (v0.50's pictures 79 and 90) were built again from their own records, with the same seeds and the same people in the same places, in three arms: **O**, as screened; **D**, the trial cast's poses with v0.50's ball, late on its arc by the catcher's hands; **C**, those poses with the ball early, a third of the way along its path, at the end of a short dashed line from the thrower's hand. Twelve fresh readers each read one picture 79 and one picture 90, from two different arms, with the screen's own prompt, so every picture of every arm has four readings (`vision/isolation_v051/ws`; the pictures' names and arms are in its `map.json`).

| Arm | Picture 79 | Picture 90 | The girl throws | The woman throws | Either |
|---|---|---|---|---|---|
| O, v0.50 | 1 of 4 | 2 of 4 | **3 of 8** | 3 | 2 |
| D, the poses | 2 of 4 | 2 of 4 | **4 of 8** | 3 | 1 |
| C, the poses and the early ball | 4 of 4 | 3 of 4 | **7 of 8** | 0 | 1 |

The bench shows the fault where the screen had it. Of v0.50's own picture: "In the middle, a woman in a yellow dress has just thrown a red ball, and a dashed line shows it arcing toward a small girl in a pink dress, who runs forward with her arm out to catch it." (pic_024). The new poses with the old ball were read the same way: "In the centre back, a woman in a yellow dress throws a red ball, and a dashed line shows it arcing down toward a small girl in a pink dress who reaches out to catch it." (pic_053). With the ball early: "In the middle of the lawn a girl in a pink dress has just thrown a red ball (a dashed line shows its path from her hand) toward a woman in a yellow dress, who stands with her hands raised ready to catch it." (pic_012). The one reading of C that did not choose: "Ball direction: the dashed line could mean the woman threw it to the girl, or the girl threw it up to the woman, who is about to catch it." (pic_043). Three more of C's eight add the other way and set it aside: "could also be read as the woman having just thrown it, but the line starts at the girl." (pic_040).

**A reader carried one picture's reading to the other.** The two pictures show the same girl and the same woman, and each reader had both. The four readers whose two pictures were O and D read neither the right way: six readings the wrong way round and two either. The eight readers who had one picture of C read it the right way in seven readings, and read their other picture, an O or a D, the right way in seven as well. So the counts of O and D above mix two kinds of reader, and D cannot be told from O on this bench: read without a C beside it, each failed every time. What the bench can say is that the early ball was read right by seven readers of eight on its own evidence, since nothing in their other picture pointed that way, and that v0.50's ball, with either cast, was not read right by any reader who had only it.

**Taken:** the ball early on its dashed arc (`templates.CATCH51`, value C) and the poses (`TPDB_CATCH51`, value B). The poses are taken for what the cut-outs said of the old catcher's hands, six cut-outs of six, and not for the direction, which they do not change.

## The square wheel on the wheelbarrow (R2)

`square_wheel` had 0.875 in v0.50's screen with its one misread, on its one wheelbarrow: the sprinkler's hose lay on the ground behind the wheel. The rule (`BARROW51`) places the template after every template that lays a hose and keeps its box off each hose's run on the ground, off the ground no one may stand on, and off the garden's reel.

| Case | Drawn | What the readers said |
|---|---|---|
| `bwrO_1` | **O**: a sprinkler's hose behind the barrow, as the seed drew it | "The wheel is drawn as a square frame with a cross-hatched spoked pattern, not a round wheel; it looks odd and could read as a crate or grate rather than a wheel." and "so it could look like it is standing on the hose." (iso_04) |
| `bwrB_1` to `_3` | **B**: the rule; a sprinkler in the garden and in the park, a watering hose in the garden | A wheel that is square in three of three, and no reel in any: "The wheel is drawn as a square (a dark square frame with spokes inside) rather than a round wheel, which looks odd; it could be read as a square wheel or as a wheel seen in some strange perspective." (iso_23). A grate or a crate beside it in two: "It could be a square-drawn wheel, or a separate object (a drain grate or crate) that the wheelbarrow's axle passes into." (iso_29) |

**Taken.** The wheel's own drawing is left. The list proposed to draw it as the bicycle's is drawn; that is the wheel with a round hub that v0.22's bench had replaced on the barrow, where it read as a spoked wheel inside a square frame, and all four readers here name a wheel that is square. The grate that two of them offer beside it stays on the list.

## The bread for the ducks (R5)

`ducks_bread` had 0.944 on nine items: "her hand item is small and hard to make out". With `BREAD51` a slice of bread stands in the feeder's forward hand, and pieces are in the air on an arc from the hand when the duck is far enough away for one.

| Case | Drawn | What the readers said |
|---|---|---|
| `dbrO_1` to `_3` | **O**: v0.50 | Feeding in three of three, and the hand empty in two: "The boy's outstretched hand is well away from the crumbs and holds nothing, so it is unclear whether he has just thrown them or is only gesturing; nothing shows them in the air." (iso_08) |
| `dbrB_1` to `_3` | **B**: a slice in the hand | A piece of bread in the hand in three of three: "She holds a brown paper bag in one hand and a piece of bread in the other, and appears to be feeding a white duck." (iso_01). A doubt of what it is in two: "The pale item in his raised hand is small and boxy; it reads as a piece of bread, but it could also be a cup or small container." (iso_02) |

**Taken**, and after the round the slice was given a crust and set a little lower in the hand. That last drawing has no cut-out reading; it is read in the design tests.

## The lost balloon's string (O1)

In three v0.50 pictures the string's free end lay by something else: on a rail of the garden's fence twice, and over the pond once. With `LOST51` the end stays a head's height above the hand, where v0.50 put it, and the child stands where that is on the fence's plain boards between its two rails, or clear of the fence; never by the gate, and never over the pond.

| Case | The string's end | What the readers said |
|---|---|---|
| `lbrO_1` to `_3` | **O**: v0.50; by the gate's top, on the upper rail, over the pond's far edge | Two of three not sure that it had left the hand: "so it could be read as a balloon that has just been let go (drifting away) or as one the child is still meant to be holding but the string does not reach the hand." (iso_28). And the pond: "but the string is very long and its end hangs oddly low, almost touching the pond area." (iso_18) |
| `lbrB_1` to `_3` | **B**: on plain boards twice; in the park, where the rule sent it, at the hedge's line | Escaped in three of three: "The blue balloon's string ends in mid-air near the fence rail, not attached to anything; reads as a lost balloon floating away, which seems consistent with his reaching arm and expression." (iso_32). In the park: "so for a moment it can look as if it is tied to or growing out of the bushes rather than floating free." (iso_06) |

**Taken**, and after the round the rule took the backdrop's dark lines in as well (`Scene.outline_clear`, the check a waving hand has had since revision 16): the end lies on no hedge, hill or roof line. On that seed the string then ends in the open sky. Read in the design tests.

## The stopped hose (R4)

One reader of v0.50's five pictures was not sure that the paw was on the hose and not behind the swelling. With `PAW51` the swelling ends 13 units short of the paw, which stands on a longer flat stretch.

| Case | Drawn | What the readers said |
|---|---|---|
| `hprO_1` to `_3` | **O**: v0.50, the swelling's end under the paw | The stopped water in three of three, in two as one reading of two: "so the dog appears to be standing on the hose and blocking the water." (iso_13) |
| `hprB_1` to `_3` | **B**: the swelling short of the paw | The stopped water in one of three. "It looks like two hose pieces, or a hose that breaks and passes under or through the dog's paws, rather than one continuous hose being stepped on." (iso_16); "the dog appears to be standing on or right beside the hose, and that blob could read as a joint, a puddle, or the dog's own shadow merging with the hose." (iso_37) |

**Not taken.** It is v0.50's finding again from the other side: the swelling against the paw is what joins the paw to the water.

## The fence painter (O3)

| Case | Drawn | What the readers said |
|---|---|---|
| `ptrO_1` to `_3` | **O**: v0.50 | Painting in three of three. "The paint bucket is fairly far from him, behind his legs." and "though at first glance it could look like a small lantern or a can stuck to the fence." (iso_07) |
| `ptrB_1` to `_3` | **B**: the tin at the heel (`TIN51`), the roller's caps navy (`TPDB_ROLLER51`) | Painting in three of three, the tin "by his feet" twice and "at her feet" once: "An open grey paint can with blue paint sits on the grass by his feet." (iso_34). No lantern and no pale cylinder. One reader: "The paint can stands slightly apart from his feet and seems to float a little above the grass with only a faint shadow." (iso_21) |

**Both taken.**

## The man in the red shirt (O2): the moustache, in whole scenes

He was a boy first in two of his 23 pictures in v0.50's screen, both times sweeping, and his moustache was named in seven of them, for thirteen of 22 in v0.49: on the smaller head it is a smaller mark. `TPDB_MOUST51` "B" draws it as wide and as thick as it was on v0.49's head. Sixteen of v0.50's pictures of him were built again from their records with that cast and read beside v0.50's own, by the eight readers of the catch bench who had six pictures, two of each arm to a reader and no picture twice (`tools/cycle/age_scenes.py`'s deal, counted by its rule on the first inventory line that names the red shirt).

| Arm | A boy first | The moustache in his line |
|---|---|---|
| O, v0.50 | 2 of 16 | 7 of 16 |
| B, the wider moustache | 2 of 16 | 9 of 16 |

Seven pictures have the moustache named in both arms and seven in neither; two have it with B only. **Not taken**: the width is not what makes him a boy. What the bench does show is where he is one. Three of the four are the sweeper, bent over the broom with his face down, in three of the eight readings of a sweeping picture; the fourth pours water from the pan, and the other 23 readings have a man. "- Boy, left, front: brown hair, red T-shirt, blue trousers. Sweeping a pile of brown leaves on the path with a yellow broom." (pic_011, O). That is a matter of the pose and goes on the next list as one.

## Looked at and left

- **R3, the thief bird** (0.90 on fifteen items). Its two items under full marks are a reader who offers sharing beside stealing and a reader of a tier-4 picture who names the bird at the sandwich and goes no further. v0.47 drew the bird with its beak in the bite and turned the reader away, and dropped the piece in the beak, which was a dark blob at this size. Nothing new was drawn; the template keeps its five pictures.
- **R6, the hedged full marks** (`jump`, `dog_sleeping`, `dog_wants_walk`, `dog_begs`, `plant_flowers`). Left, as the list has it: each hedge is a reading that the thing drawn would earn in life.
- **O4, the slider; O5, the heavy seesaw's rider; O6, figures at the pond's rim; O8, the swing's one seat.** Not worked in this release. Each is one picture's remark, and they stay on the list.
- **O7, a hose in use under storm clouds.** No bench: a rule of the planner. Both v0.50 pictures that had the stopped hose under the storm clouds drew the remark, and from revision 48 the template is kept to a clear sky, as the watering templates have been since revision 30.

## What the rules cost in placement

Each on twelve seeds with the switch off and on (`tools/cycle/yield_set.py`, no band): the square wheel alone 12 and 12 in each of the four settings; with a sprinkler in the garden 12 and 11 and in the park 12 and 12; with the stopped hose and two events 11 and 11. The lost balloon 12 and 12 in the garden and in the park, and 10 and 10 in the playground. The game of catch 10 and 10 in the garden, 5 and 5 in the park, 11 and 11 in the street and in the playground. The bread and the painter's tin 12 of 12 with the rule on.
