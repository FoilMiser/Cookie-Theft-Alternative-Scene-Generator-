# v0.49 blind screen: what it found (the work list for v0.50)

The v0.49 screen read the set's 21 pictures and 85 probes with the prompts of v0.48 (`screen_prompts.md`). There were fourteen readers, eight of eight pictures and six of seven, and five scorers of 21 or 22. Every template passed the legibility gate, where one had failed in v0.48 and in v0.47 and four in v0.46, and nothing was redrawn, swapped or read again after the screen (below). No item of the 1,144 was misread. Keys, descriptions and scores are in `v049/`.

v0.49 worked Sam's brief: "go for v0.49 now! This is an improvement, but I am not sure if I love this head shape either, they look a little like bowling pins since they do not have chins. want to focus on a better head shape first using blender and carefully choosing a good style to go with?" The work is in the cast (builder 0.49.0) and in two placement rules (revision 46):
- **the head**, on every person: a jaw and a chin (the round jaw, chosen on two blind benches of four shapes), a neck that is a part of its own and narrower than the chin, the head carried a little forward of it (`isolation_v049.md`);
- **with it**: a wider moustache, and the ice cream at the mouth (v0.48's R5);
- **v0.48's list**: the coming rain (R1), tried with a new gesture on the bench, which read worse, and left as it was with five probe pictures for three; the goat's rope (O5), thicker; an animal at the picture's foot (O6), by a rule that was written three times. R2 to R4, R6, O2 to O4 and O7 to O9 were not worked.

Every person is drawn anew and every picture was built again. Thirteen of the sixteen cells have v0.48's seeds and templates, so most of the set is v0.48's set with the new heads; the tier-2 and tier-4 gardens and the tier-4 street have other templates.

## Headline (the 21 pictures of the set)

| | v0.45 (21) | v0.46 (21) | v0.47 (21) | v0.48 (21) | v0.49 (21) |
|---|---|---|---|---|---|
| Things | 0.962 | 0.943 | 0.985 | 0.990 | 0.917 |
| Actions | 0.992 | 0.988 | 1.00 | 0.996 | 1.00 |
| Inferences | 0.984 | 0.914 | 0.968 | 0.985 | 0.985 |
| Contradictions | 0.955 | 0.923 | 1.00 | 1.00 | 1.00 |
| All items | 0.977 | 0.957 | 0.991 | 0.993 | 0.967 |
| Misread items | 0 of 281 | 2 of 282 | 1 of 283 | 0 of 276 | 0 of 284 |
| Readers' remarks per picture (all screened pictures) | 2.58 | 2.38 | 2.66 | 2.38 | 2.32 |
| Oddities per picture, as logged by the scorers | 0.5 (at most 2) | 0.2 (at most 1) | 0.3 (at most 1) | 0.1 (at most 1) | 0.2 (at most 2) |

The set's 0.967 is under v0.48's 0.993, and all of the fall is in the things: nine of the set's ten items under full marks are a part of the setting that a reader did not mention, the clouds in eight pictures (22, 25, 27, 40, 44, 47, 75, 102) and the sun in one (102). Every action and every contradiction of the set has full marks. The tenth is a half mark on the lost balloon (102): "The red balloon may belong to the girl (she let go) or to someone else; she seems to be reaching for it."

The scorers logged 4 oddities in the set's 21 pictures and 16 in the 85 probes, 0.2 a picture over all 106 (v0.48: 2 and 31 in 87, 0.4 a picture). No picture has more than two.

Across all 106 pictures, 1,102 of the 1,144 scored items had full marks (v0.48: 939 of 971), and none was misread. The 42 under full marks:
- **Twenty-nine on the clouds, eleven on a tree and one on the sun,** all zeros on setting items that a reader left out. Two readers left the clouds out of every one of their eight pictures (18 to 25, and 34 to 41), and a tree out of two and of five; a third left the clouds out of five of eight (44, 45, 47, 48, 49), a fourth out of four (101, 102, 103, 105) with the sun once, a fifth out of three with a tree twice, and two more account for three. v0.48 had twenty-three such zeros, from two readers; v0.47 sixteen, from three. It is a reader's habit and not a drawing's fault: the same clouds are named by the other readers of the same settings.
- **The lost balloon (102), a half mark,** above.

No other item of any action, inference or contradiction is under full marks. The scorers gave five, nineteen, five, five and eight items under full marks, of 210, 231, 239, 212 and 252.

**What the full marks rest on.** The scorers listed 86 judgement calls they scored 1 (19, 14, 26, 11 and 16), for v0.48's 69 in 87 pictures. The 86 are of two kinds:
- **42 where the target stands beside another reading**, in the description or in its unsure section (v0.48: 33). By template: the stopped hose five; the dropped ice cream four; the heavy seesaw, the game of catch and the begging dog three each; six templates two each; and one each for the rest. Halved, as the scoring rule's "only offered as one of two readings" read strictly, they take ten templates under 0.9: `dog_playing` (0.75, 4 items), `play_catch` (0.812, 8), `dog_sleeping`, `jump`, `rake` and `seesaw_heavy` (0.833), `balloon`, `blocked_hose`, `dog_begs` and `dog_wants_walk` (0.875). 54 of 64 pass (v0.48: 55).
- **44 on a near word or a target partly said** (v0.48: 36). Twenty-three of them are a word for a person's age: "boy" for the teenager or for a man, "girl" for a woman. The rest: "has fallen" for dropped, a frying pan "or saucepan", the sun named only in the inventory. With these halved as well, 43 of 64 pass (v0.48: 43).

The gate's 64 is therefore the count under the rule as the scorers applied it. The strict counts show how many of the full marks carry a hedge (`tools/cycle/strict_count.py`).

## What the screen says of the cast

The screen's prompt asks what is in a picture and what is happening, not how a figure is drawn. The question of the drawing was the bench's (`isolation_v049.md`).

- **The new head drew no remark.** No description of the 106 has the word jaw or chin, or writes of a head's shape. That is weak evidence, as it was in v0.48: the readers do not name such things.
- **The moustache is seen again.** The man in the red shirt is "a man with a moustache" in 13 of his 22 pictures (v0.48: none of 17; v0.47: 10 of 15): "A man with a moustache, in a red shirt and blue trousers". The older man's is named in 2 of his 23. The beard of the man in green is named in none of his 25 pictures, as in v0.48.
- **Grown people were read young more often, not less.** By the first inventory line that names each figure's clothes, the four grown figures of v0.48's count are called by a young name first in 20 of their 89 pictures (v0.48, by the same rule: 11 of 81): the woman in purple in 9 of 24 (7 of 22), "Girl, centre-front: dark ponytail, purple top, teal trousers; running to the right." (15); the woman in the yellow dress in 5 of 18 (1 of 18), "Girl/young woman, left on path, dark ponytail, yellow dress, red shoes: walking and eating a pink ice cream." (56); the man in the red shirt in 2 of 22 (2 of 17), "Boy, front left, red shirt, blue jeans, brown hair: walking and eating an ice-cream cone." (75); the man in green in 4 of 25 (1 of 24), "Boy/young man, right, green shirt, beige trousers: sweeping leaves with a yellow broom." (53). Fourteen readers are fourteen habits, and the two counts are one screen each; but a jaw was to make a grown figure read as grown, and it has not. The bench had said as much beforehand: figures of the two casts alone at a picture's size were called young equally often. O1.
- **Every animal was named for what it is.** A dog is a dog in all 38 descriptions of a picture with one, a cat a cat in all 10, the goat a goat in all 5, the duck a duck in all 7. One reader of the goat adds that its horns "could be read as ears", and that it could be a sheep or a kid (56).
- **The older woman's glasses are named in all 21 of her descriptions**, and her bun in 18 (v0.48: 16 of 16, and 8).

## The v0.48 list

| v0.48 | In v0.49 |
|---|---|
| R1: `rain_coming` 0.889 in three pictures, failing the gate on one inference left unsaid | A watcher with a hand held out for the first drop read worse on the bench than the pointer and was not used. The pointer, in five pictures: **1.00** (15 items), and the rain is said in all five: "It looks as if it is about to rain." (42); "pointing up at the dark clouds as though rain is coming" (72); "as if noticing the dark clouds or the first raindrops" (87) |
| R2: `lost_balloon` 0.933, "or the girl is just looking at it" | Not worked. **0.972** (18 items, 6 pictures), one half mark (102) and five calls, and the template nearest the gate. R1 |
| R3: `blocked_hose` 0.95, "or simply because the tap is not on" | Not worked. **1.00** (20 items, 5 pictures), with six of its marks a call: the dog "on the hose, or on its connector", and the block said as a maybe (72, 78, 89). R2 |
| R4: `about_to_trip` 1.00, hedged in four pictures of five | Not worked. **1.00** (18 items, 6 pictures), two calls, one of them on the trip (17) |
| R5: `ice_cream` 0.95, "just holding the cone up" | The scoop at the mouth and the head tipped to it. **1.00** in 14 pictures, eaten or licked in 13: "walks along the path eating a pink ice-cream cone" (106). Two of the fourteen marks are a call about the eating (21, 86) and four about the eater's age (v0.48: two half marks and eight calls in twenty): "running to the right while holding a pink ice-cream cone up near his face" (86) |
| R6: `water_upward`, `bird_steals`, `play_catch`, `dog_begs`, `bucket_hat`, `ducks_bread`, full marks on a hedge | Not worked. Each **1.00** by the gate. `play_catch` and `dog_begs` are under 0.9 on the strict count again. R3, R4 |
| O1: grown figures read young, facial hair unseen | The moustache is seen (13 of 22). The young names rose, 20 of 89 for 11 of 81. O1 |
| O2: figures in front of the pond | Three remarks (63, 83, 84), each settled by the reader: "The girl overlaps the front edge of the pond; she is clearly on the grass in front of it, not in the water." |
| O3: the seesaw's riders | Not worked. Three pictures of the seesaw (3, 7, 48) and two of the slide (10, 20): "The girl looks small and perches a little above the plank; she might be slightly floating above the seat, but it mostly reads as sitting." (3). O2 |
| O4: the painter's roller | Not worked. Three pictures (31, 70, 85): "The roller looks a little small and oddly held, high above the woman's hand, but it reads as painting." (31). O3 |
| O5: the goat's rope thin | Thicker. A rope or a tether in all five of its pictures, and no reader calls it thin. The stake is now the remark: "The goat's tether stake looks very short; the goat could be tethered or just standing by a stake." (11). O4 |
| O6: a dog cut off at the picture's foot; a post close to an arm | An animal's box ends 8 px above the foot (`scene.EDGE49`). No description has a figure cut off |
| O7: walking beside the path | One picture: "The girl appears to be walking just left of the path on the grass rather than on it." (106) |
| O8, O9: one picture each | The bicycle with no stand again (94): "The bicycle stands upright with nobody holding it; there may be a kickstand but it is hard to tell." |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

Every template was screened in at least three pictures (29 in three, 12 in four, 14 in five, 5 in six, 1 in seven, 1 in eight, 1 in fourteen and 1 in seventeen), and all 64 pass. One is under 1.00: `lost_balloon`, 0.972 on 18 items in six pictures. Per angle (`v049/gate_yaw.json`), 19 of the 19 (template, angle) pairs pass, all at 1.00.

| Template | Mean | Items | Pictures | Verdict |
|---|---|---|---|---|
| `lost_balloon` | 0.972 | 18 | 6 | pass |
| the other 63 | 1.00 | | 3 to 17 | pass |

It is one screen, and the gate is a filter for illegible drawing: the strict count above is the fairer picture of how firmly these marks stand.

## After the screen

Nothing was mended, swapped or read again. The count is the first and only one.

## What reads least well (the v0.50 list)

| | Template | v0.49 | What the readers wrote | For v0.50 |
|---|---|---|---|---|
| R1 | `lost_balloon` | 0.972 (18 items, 6 pictures) | "The red balloon may belong to the girl (she let go) or to someone else; she seems to be reaching for it." (102) | v0.47's R3, carried again: the freed balloon nearer the hand, its string loose and curling below it, the hand open; the held bunch's strings gathered to the fist |
| R2 | `blocked_hose` | 1.00 (20 items, 5 pictures); 0.875 on the strict count | the dog "on the hose, or on its connector" (72, 78, 89) | The paw plainly on the hose's run and clear of the joint; the hose swollen from the reel to the paw and slack after it |
| R3 | `play_catch` | 1.00 (8 items); 0.812 on the strict count | of the catcher, "she could also be the one who threw it" (19) | v0.48's R6, carried: the thrower's arm down and through, the catcher's hands cupped, open and out in front |
| R4 | `dog_begs`, `dog_playing`, `dog_sleeping`, `dog_wants_walk` | 1.00 each; 0.875, 0.75, 0.833 and 0.875 on the strict count | "begging for the ice cream, or just looking up at the boy" (49); the play bow beside a stretch (9); asleep beside lying with its head down (8, 12) | The sleeper's eyes shut as a line and its body curled; the player's ball under a lifted paw; the beggar's forepaws up at the plate or the cone |
| R5 | `seesaw_heavy` | 1.00 (9 items, 3 pictures); 0.833 on the strict count | the hand at the mouth of the child up in the air: "The girl's gesture could be worry, surprise, or calling out; hard to say which." (7, 48, 101) | A call that is one thing: both hands round the mouth, or an arm held down to the grown rider. With O2, a seat for each rider. `jump` and `rake` are at 0.833 too, on one call in three items each, and are left |

## Unintended oddities

Grade A is a remark in five or more pictures, or one that touches what a figure is; B in three or four; C in one or two.

| | Grade | What the readers wrote | Pictures | For v0.50 |
|---|---|---|---|---|
| O1 | A | Grown figures read young: "Girl, centre-front: dark ponytail, purple top, teal trousers; running to the right."; "Boy, front left, red shirt, blue jeans, brown hair: walking and eating an ice-cream cone."; the beard named in none of 25 pictures | 20 of the four figures' 89 | The outline of the head does not carry age, and neither does its size (the age bench, `isolation_v049.md`). A mark of age that is seen on the smallest figure: for the two women one each (hair worn up, a bag on the shoulder, a longer skirt), a fuller and darker beard, the moustache as it is. Bench the marks on figures in whole scenes, counted with `who_cmp.py`, before they go into a cast |
| O2 | A | The seesaw's and the slide's riders: "The girl looks small and perches a little above the plank; she might be slightly floating above the seat, but it mostly reads as sitting."; "The girl seems to sit slightly above the chute surface, but this is minor." | 3, 7, 48; 10, 20 | Carried a fifth time, and in five pictures for v0.48's four. A seat drawn on the plank at each end and the rider's hips on it; the slider's seat on the chute |
| O3 | B | The painter's roller: "The roller looks a little small and oddly held, high above the woman's hand, but it reads as painting." | 31, 70, 85 | Both hands closed round a longer handle; the roller's head on the board |
| O4 | C | The goat's stake: "The goat's tether stake looks very short; the goat could be tethered or just standing by a stake." | 11, 65 | A taller stake with the rope knotted round its top |
| O5 | C | A held balloon's string: "The balloon's string is perfectly straight and stiff, so it could be a balloon on a stick, or a lollipop/ice lolly on a stick; most likely a balloon." | 39 | With R1: a string that hangs in a curve |
| O6 | C | The reading dog's glasses, which are drawn and are named plainly in three of its six pictures: "The dog's dark eye area could be read either as glasses or as dark eye markings; it looks like glasses." | 57, 58 | A lighter rim with the eye seen inside it, and the bridge clear of the muzzle's patch |
| O7 | C | One picture each: "The girl in pink has a small mark near her eye that could be a tear, so she might look worried or upset rather than eager to catch; hard to tell."; the bicycle upright with no stand; the walker "just left of the path on the grass"; "The swing's ropes are very thin; otherwise nothing looks floating or impossible." | 97; 94; 106; 79 | The cheek mark of the eager face left off a figure this small. The bicycle and the path are v0.48's, kept |
| O8 | C | Notes for the pilot: the setting's clouds, tree and sun are left out by some readers and named by others of the same pictures (41 zeros, 23 in v0.48) | 41 items | None for the drawing. A person tested will leave them out too; the pilot's scoring should say whether setting items count |

## Placement

Revision 46 is the people's new boxes and anchors and two rules: the goat's rope half as thick again, and an animal's box 8 px clear of the picture's foot. The second was written three times, and the first two cost a set each (`scenegen/scene.py`, the revision's header): for every figure at 14 px, which took the front strip of the ground from the people and all but stopped tier 4 from placing; for animals at 14 px, under which the set came back to v0.48's seeds and the tier-4 isomorph still would not build in 126 calls; and for animals at 8 px, under which v0.48's own tier-4 isomorph builds on its seed, third call. The rule that stands changed two of the 106 records built under the one before it, and those two were built again before the screen.

The tier-4 garden failed on 88 seeds of four searches before one placed, and the tier-4 street on 14; the other fourteen cells placed on their showcase seeds or on v0.48's. `probes.py` left nine templates short, each having lost its three groups to a partner (the storm beside a watering template, a second dog, the playground's events with each other), and `more_probes.py` filled them with small groups. The washing was short in the first build for a reason of its own: only the three tallest grown figures reach the line.
