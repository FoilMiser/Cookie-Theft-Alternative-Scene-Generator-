# v0.54 isolation bench

v0.54 works the list of `flaws_v053.md`. Sam's brief was "go for v0.54, go ahead and publish and push and put the computer to sleep when you are done" and named no part of the drawing, so the list set the work: the square wheel of a bicycle that one reader did not name and the wheelbarrow's second reading (R1), the two templates with the most full marks beside another reading (R2), and the man in the red shirt, a boy to the readers of three pictures (O1). Before anything was drawn the last two screens were counted again by pose and by where a thing is named, and every flagged picture of v0.53 was looked at at full size.

One bench in whole pictures decided all three drawings. One was taken and two were not.

## What the screens said, counted before drawing

**The man in the red shirt is a boy when he reads, and only then.** By the first inventory line that names his red top, he was a boy first in every picture in which he reads: three of three in v0.53's screen (two on a bench, one walking with an open book), from three readers, and one of one in v0.52's. In his 27 other pictures of the two screens he was never a boy. The women and the grandparents who read in the same poses, in 20 pictures of the two screens, were never called young. v0.51 had found the same of him in another pose, the sweeper bent over his broom: his face down.

Reading, his head is bent 26 degrees over the book on a bench and 30 when he walks. What makes him a man, the moustache and the sideburns of v0.39, is then a few pixels at the lower edge of a face seen from above, under a full head of brown hair (`isolation_v054/trials/read_O_B.png`, top row).

**A bicycle's square wheels are named late in a third of their readings.** Over the screens of v0.51 to v0.53 a bicycle with square wheels was read twelve times: the wheels are called square in the description or the inventory in eight, only among the unsure things in three, and not at all in one, v0.53's picture 51. That is what the wheelbarrow's wheel was before v0.53 made it larger.

## The three drawings

- **The reader's head up** (`castlib/actions.py`, `READ54` B; O builds v0.53's). A grown man with facial hair, which is the man in the red shirt and the man in green, reads with his head bent 10 degrees, seated or walking, his eyes on the book. Tried large at 12 and 14 degrees and at 4 and 6 before the bench: at each the moustache is on the face and the eyes are on the page (`isolation_v054/trials/read_O_B.png`).
- **The bicycle's square wheels larger** (`draw.WHEEL54` B; O draws v0.53's). 38 units from hub to side for 30, the tyre and the spokes a little heavier, the frame raised and the wheelbase longer by as much: what `WHEEL53` did for the barrow.
- **Tread on the barrow's square tyre** (`draw.TREAD54` T; O draws v0.53's). Short marks across the tyre on all four sides, the corners kept sharp, for the second reading v0.53's larger wheel had drawn: "It could alternatively be a separate square object (a grate or frame) standing in front of the wheelbarrow." The bicycle and the barrow side by side in both drawings are `isolation_v054/trials/wheels_O_B_T.png`.

## The bench in whole scenes (`isolation_v054/bench`)

Twelve fresh readers had six pictures each and the screen's own prompt, 72 pictures in all. Each had two bicycles, two wheelbarrows and two pictures of the man reading, each pair of one arm, so that what a reader carries from the first picture of a thing to the second stays inside its arm; six readers had each arm of each question, and the arms of the three questions were crossed. The pictures are v0.53's own records built again from their own seeds with one change each, and four pictures built for the bench with v0.53's code. The map of which picture is which lay outside the folder until the readings were in (`isolation_v054/bench_map.json`).

**The man reading.** Six pictures: v0.53's three (29, 60 and 67) and three built for the bench, in the park, the playground and the street. Arm O is each as v0.53 draws it, arm B the same record built again with the two men built again. All six came back with the same templates and the same people; picture 60 came back in another layout.

| Arm | Readings | A boy first | Not called a man | A man first |
|---|---|---|---|---|
| O, v0.53's pose | 12 | 6 (four readers of six) | 2 | 4 |
| B, the head up | 12 | 1 (one reader of six) | 0 | 11 |

As screened: "- Boy (right-centre, on bench beside path): brown hair, red shirt, blue trousers; sitting reading a red book." Two more readings of that arm do not call him a man: "- Left-centre: young person in red shirt and blue trousers sitting on a bench reading a red book." and a reader who wrote "Person" for him and then "The person on the bench could be a teenager or an adult." With his head up: "- Man (right of centre, front-middle): brown hair, red shirt, blue jeans, dark shoes; sitting on a bench reading a red book." One reader of that arm names the moustache, in both its pictures: "- Man, left-centre back: brown hair, moustache, red shirt, blue trousers; sitting on a bench reading a red book." The one boy of arm B is the walker of picture 67: "- Boy (centre, front): brown hair, red shirt, blue trousers; walking/hurrying left while reading an open book."

The first arm shows the fault as the screens had it. And the head up costs the reading nothing: all 24 descriptions have him reading, and in the three pictures where a walker with a book is about to meet a box, all six readings of each arm say so.

**Taken: B.** The cast is built again as builder 0.54.0.

**The bicycle.** Four bicycles: v0.53's pictures 51, 58 and 63 and one built for the bench (v0.53's fourth is an isomorph, and with the larger wheels it did not come back as the same picture). Arm B came back with the same templates and people; picture 58 came back in another layout.

| Arm | Readings | The wheels square in the description or the inventory | Only in the unsure section | A rack offered |
|---|---|---|---|---|
| O, v0.53's wheels | 12 | 10 | 2 (one reader, both its bicycles) | 0 |
| B, the larger wheels | 12 | 8 | 4 (two readers, both theirs) | 5 (three readers) |

The larger wheels were named no sooner, and they brought a reading v0.53's wheels did not get from any of these readers: a bicycle parked in a rack. "The bicycle's wheels sit inside black square frames: it could be a bike parked in a bike rack, or a bike drawn with square wheels." Two readers put both their bicycles in a rack in the inventory and gave square wheels only as the other reading, among the unsure things, and a third wrote of a bicycle "standing in a rack" whose "wheels are square black frames". v0.14 had found the same of a real rack hoop behind the bicycle, whose legs made the wheels "square wheel-holder frames that belong to the rack": two large dark squares under a bicycle are a stand before they are wheels.

**Not taken: O.** The bicycle keeps v0.53's wheels. Its fault is as mild here as it was in the screens (two readings of twelve, one reader's, late and none missing), and the one change tried made it worse.

**The wheelbarrow's tread.** v0.53's four wheelbarrows (41, 42, 68 and 97), arm T built again from the same records: the same pictures but for the tyre.

| Arm | Readings | The wheel square in the description or the inventory | Only in the unsure section | A crate or a grate offered | The tread named |
|---|---|---|---|---|---|
| O, v0.53's tyre | 12 | 8 | 4 (two readers, both their barrows) | 0 | |
| T, the tread | 12 | 12 | 0 | 0 | 0 |

The reading the tread was drawn for did not come: no reader of either tyre offered a crate, a grate or a separate thing in front of the barrow, where two of five had on v0.53's bench. No reader named the tread. With it the wheel is in every description, and without it in eight of twelve; but the four are two readers' who also named their bicycles' wheels only in the unsure section, so the difference is as likely theirs as the tyre's. "To the right of the box is a grey wheelbarrow whose wheel is a square, which could not roll." is a reading of the tread, and "Next to the box is a grey wheelbarrow whose wheel is square, which would not roll." of the plain tyre, in the same picture.

**Not taken: O.** Nothing to choose on the reading it was drawn for. The tread stays behind its switch.

**One more count from the same readings.** The woman in purple is in three of the bench's pictures (29, 58 and 63), sixteen readings. She is a woman in all twelve of pictures 58 and 63, and a girl in three of the four of picture 29, where she holds a hose's nozzle up and looks down into it: "- Boy (front right, on bench): brown hair, red shirt, blue trousers; sitting reading a red book." is that picture's line for the man, and the same reader has her "a girl with dark hair, a purple top and teal trousers". v0.53's screen had her a girl in that picture too. Over three screens her young names are spread over five poses, and in four of them she is a woman at least as often as a girl, so it is not the one cause it is for the man; the hose inspector goes on the list.

## Looked at and left

| From the list | What was found |
|---|---|
| R2, the begging dog's eyes on the food and not on the face | The six begging dogs of v0.53 at full size: the dog sits up with its forelegs folded and its head tipped up at the eater, and the eater's food is at the eater's mouth, so the two aims are one. Two earlier changes of its head (v0.41, v0.43) lost the gaze check at three-quarters. The readers who hedge give begging first. Left |
| R2, the stopped hose's swelling read as a joint | The swelling was drawn in v0.29, v0.42, v0.47 and v0.50, and v0.50's bench found that it carries the reading under the wrong name. Every reader of v0.53 has the dog on the hose and no water. Left |
| R3, six templates on the strict count | Each reader gives the target as the likelier reading. Left, as the list said |

## The list

| From `flaws_v053.md` | In v0.54 |
|---|---|
| R1 `square_wheel`: a bicycle's wheels not named | Larger wheels benched in whole pictures and not taken: named no sooner, and a rack to three readers of six |
| R1 `square_wheel`: the barrow's crate or grate | Tread benched and not taken: no reader of either tyre offered the second reading |
| R2 `dog_begs`, `blocked_hose` | Looked at and left |
| R3 | Left |
| O1 the man in the red shirt a boy when he reads | His head up when he reads (`READ54` B): a boy in 1 reading of 12 for 6 of 12. Taken |
| O2 to O6 | Left or carried |
