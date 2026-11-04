# v0.27 blind screen: what it found (the work list for v0.28)

The v0.27 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 46 probes. Keys, descriptions and scores are in `v027/`.

## Headline (the 21 pictures of the set)

| | v0.24 (21) | v0.25 (21) | v0.26 (21) | v0.27 (21) |
|---|---|---|---|---|
| Things | 1.00 | 0.991 | 0.995 | 1.00 |
| Actions | 0.988 | 1.00 | 0.992 | 0.996 |
| Inferences | 0.986 | 0.985 | 0.953 | 0.950 |
| Contradictions | 1.00 | 1.00 | 0.981 | 1.00 |
| All items | 0.993 | 0.995 | 0.988 | 0.993 |
| Misread items | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 |
| Readers' remarks per picture (all screened pictures) | 5.64 | 5.93 | 5.27 | 5.81 |
| Oddities per picture, as logged by the scorers | 5.2 | 2.6 (at most 3) | 2.6 (at most 3) | 2.2 (at most 3) |

Across all 67 pictures 743 of 756 scored items had full marks. Five had half marks, eight were missed, and none was misread. The set's four half marks are three inferences (pictures 21, 21, 34) and one action (32).

The eight missed items are all in probes and none is on an event: six "a few white clouds" and two "there is a tree". One reader, of pictures 9 to 16, names no cloud and no sun in any of its eight pictures, which accounts for all six clouds and one tree, so this is that reader's habit and not the drawing. No item had been missed in v0.26.

## Reading the two bottom rows

Remarks rose by 10%, 5.27 to 5.81 (389 against 353), on the same model and prompts as v0.26, and the rise is spread across the readers (5.3 to 6.3 a picture, against 4.3 to 6.0 on the same split of the pictures). This release did not make the pictures read as cleaner in general, even as the gate and the named complaints improved. The new `remark_topics.py` sorts the remarks of two screens by keyword, roughly:

| Pictures that remark on | v0.26 | v0.27 | |
|---|---|---|---|
| A face hidden or hard to read | 22 | 10 | The head turn, this release's main change |
| Marks on a face | 4 | 9 | Faces are more on view: "dark marks around her nose and mouth", "a pink cheek mark" |
| Shadows | 13 | 20 | Nothing changed. "A very wide oval, much wider than the puppy", and a little girl with "no clear shadow of her own" |
| Stiff or awkward poses | 22 | 18 | |
| Thin or long body or legs | 6 | 8 | The shorter legs did not move this, against eight remarks to three on the bench |
| The hose stiff or jointed | 3 | 1 | |
| Water drawn solid | 2 | 0 | Not changed by this release |
| A figure over the pond | 5 | 6 | |
| The bicycle's wheels | 2 | 1 | |
| The roller | 6 | 7 | |

A keyword count is a rough sort, which says where to read. It is not a measure.

## The v0.26 list

| v0.26 reading | v0.27 result |
|---|---|
| R1 `sweep` 0.667: "a long yellow-headed rake", the one misread | **1.00** (3 items, 3 pictures). Nearly parallel bristles with two bindings. No reader in its three pictures said rake. "Sweeping leaves with a yellow-headed broom" |
| R2 `ice_cream` 0.833: "looking at or eating it" | **1.00** (13 items, 13 pictures), the scoop at the lips. New remarks only on detail: "could be mistaken for a nose or something else at first glance" |
| R3 `photo` 0.833: "binoculars or a camera" | **1.00** (3 items, 3 pictures). Not changed, so the half mark was probably reader variance, as the list guessed |
| R4 `about_to_trip` 0.889, meaning items 0.667: the obstacle off the walker's line | **0.958** (12 items, 4 pictures), meaning items 0.875. Offered unprompted in all four: "she might walk into it or trip over it", "he may be about to walk into or trip over it", "he might bump into or trip over something". The obstacle's line still draws remarks, one a half mark: "He is headed roughly past it, slightly to its right, so it may not be in his way at all". No placement rule was added; the lifted heel and the turned head are what changed |
| R5 `sprinkler_package` 0.889: "a wooden crate standing in a puddle" | **1.00** (9 items, 3 pictures). "So the box looks like it is getting soaked". No crate |
| O1 The seesaw's plank through the sitter | Looked at on the bench and left, and still there: "his leg overlaps the plank", "almost past it". Five pictures, against six |
| O2 The hose: stiff; not joined to its nozzle; the bulge | Down, not gone. "The hose goes up stiffly from the ground to the hand, almost like a pipe, and there is a small visible joint or gap near the top before the nozzle" (44), and "a bit stiff where it meets the hand" (18), both in `hose_water`. The bulge read as the blockage in pictures 16, 29 and 46 ("a big bulge", "as if water is building up behind the blockage"), though one scorer logged it as a possible extra object |
| O3 Faces hidden; "hair and beard merge" | Ten pictures against 22, by keyword. Of the ten, three are animals and two small faces, and the rest are poses that keep their profile (a hand-held thing at the face would be left behind), a bowed head, or a bucket over the eyes: "The front of her face is hidden by her own arm and hair" (16). The bearded man's beard still draws it twice: "a thin dark strap along the jaw" (47), "it could look like a chin strap" (50) |
| O4 Water drawn solid | No remark. Not changed, so reader variance, or the pictures this time |
| O5 Leaf clumps; the ball "planet-like" | Looked at and left, and still there: "a blue planet-like sphere" (21), "a bit like a pasted-on sticker" (53). New words for the same thing: "a small bare branch drawn on top of the crown" (33) |
| O6 The bird at the ground: "tumbling or injured" | Gone in this screen: `feed_birds` 1.00, "pecking at seeds". Redrawn on the bench |
| O7 The paint roller's head | Not changed, and still there: "more like a big blue block or roller" (5), "a paint roller or a wide flat brush" (9). `paint_fence` and `paint_tracks` pass in full |
| O8 The bicycle: "solid black disc wheels" | Gone: spokes, and no remark on its wheels |
| O9 The leaves have no source | Once: "Autumn leaves are being swept while the tree is fully green" (40). A note for the pilot |
| O10 Narrow figures | Legs an eighth shorter and limbs 14% thicker. Fewer remarks on the bench, though four cut-outs a side is a small sample, and no fewer on the screen: "long and stiff" (19), "a bit thin and stretched" (38). Whole pictures don't confirm the bench here |
| O11 Older ones | Left, as since v0.11: figures over the pond, goats as "a sheep or a dog", a wind that reaches only the cap ("It is odd that the washing and cap are blowing hard, yet the tree, the bushes and the flowers look perfectly still") |

Added from looking closely, and read here:

| v0.26 reading | v0.27 result |
|---|---|
| A black line near the edge of the face taken for a beard | No moustache or facial hair on anyone without a beard, in 67 pictures. Marks on a face are up, as above |
| The waist of the dress: "two separate yellow shapes" | A yellow dress in 16 of its 18 pictures. Both others are the pose sitting on air: "a boy in a yellow shirt and shorts" (29), "could be a dress or a top with shorts" (49). The belt may do that when she sits; a sample of two |
| The hand past the edge of the book | No remark in the four trip pictures, though "his book and arm overlap the stall" (32) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 |
|---|---|---|---|---|---|
| Pass | 64 | 63 | 61 | 59 | 63 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 0 | 1 | 3 | 5 | 1 |

Every template was screened in at least three pictures (54 in three, 6 in four, 1 in five, 2 in six, 1 in thirteen; 393 scored items behind the verdicts). All five of v0.26's failures pass. Three of the five were redrawn or reposed, and the others (`photo`, and `sprinkler_package`, whose drips only changed) may have been reader variance, which the v0.9 retest put at about five templates between screens. So the recovery from 59 to 63 is good news without being a measure of how much the drawings gained.

## What reads poorly (the v0.28 list)

| # | Template | v0.27 | What the readers saw | Fix for v0.28 |
|---|---|---|---|---|
| R1 | `dog_begs` | 0.889 (9 items, 3 pictures); fails | Both half marks say whose food: "could be hers, begging from her bag, or could be doing its own trick" (21), "it might be begging for the ice cream from the seated person, or be watching the kite, or doing a trick for the boy" (34). Where the dog is right beside the eater it reads in full: "looking up at the ice cream" (50). 1.00 in v0.26, and the dog was not redrawn | A placement rule: the dog close to the eater with its face toward the cone, and no other person nearer it than the eater. Looks cheap |
| R2 | `dog_wants_walk` | 0.917 (6 items, 3 pictures); passes | One half mark: "looks like it is asking for a walk, or could just be an odd pose" (15) | Watch |
| R3 | `sweep_fork` | 0.944 (9 items, 3 pictures); passes | The teenager: "I am not sure what the boy is doing with it" (32), where the older man read in full. The fork's top "rounded and pale" against his chest | Watch; the fork's grip on the teenager's pose |
| R4 | `about_to_trip` | 0.958 (12 items, 4 pictures); passes | "Headed roughly past it", "a little to one side of him". The revision-13 rule puts the obstacle on the line of the leading foot, which may not look like the line of the walk | A low cost try: the obstacle on the walker's centre line |

## Unintended oddities

Named kinds, from the scorers' lists (`v027/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.28 |
|---|---|---|---|---|
| O1 | B | Shadows: wide ovals "much wider than the puppy", "larger than expected", offset from the feet, and none under a child riding a seesaw | Pictures 1, 6, 7, 18, 19, 20, 22, 23, 38 | The shadow from the figure's own footprint, not its box. The commonest named thing that is plain to fix |
| O2 | B | Eyes shut while walking with an ice cream: "Walking with eyes shut is slightly odd", and pink marks that "could be blush or could be ice cream" | Pictures 24, 58, 60, 62 | `walk_ice_cream` out of `EYES_MAY_CLOSE`; the blush smaller, or none |
| O3 | B | The fallen ice cream: "a pink hat or a pink frisbee", a flying saucer | Pictures 33, 53 | The bench: a splat with no dome |
| O4 | C | The seesaw's plank and its riders: "his leg overlaps the plank", "almost past it" | Pictures 1, 6, 48, 64 | The rider further in from the end; a larger job for the leg |
| O5 | C | The hose in `hose_water`: "almost like a pipe", with a "joint or gap" | Pictures 18, 44 | Every curve so far has had a name. A hose that leaves the fist downward and only then bends |
| O6 | C | A branch or clump on top of the crown: "pasted-on", "drawn on top" | Pictures 21, 32, 33, 42, 53 | The branch from the trunk, or leaves over its near end |
| O7 | C | The bearded man's beard: "a thin dark strap along the jaw" | Pictures 47, 50 | Fuller on the cheek |
| O8 | C | Marks on a seated or small face: "dark marks around her nose and mouth" | Pictures 17, 26, 58 | The bench: fewer face lines under a set height |
| O9 | C | The narrow figure. Shorter legs did not move the screen | Pictures 17, 19, 38 | Leave, or a real change of build, not another small one |
| O10 | C | A crowd: "the group on the right a bit crowded", a walker close before a sweeper and a stall | Picture 32 | Watch; a tier-4 picture at its limit of room |
| O11 | C | Older ones: figures over the pond, goats as sheep, a wind that reaches only the cap, autumn leaves under a green tree, the roller's head | Throughout | Notes for the pilot, as since v0.11 |

## Placement

The v0.26 list asked why the tier-4 playground had got so hard (89 failed seeds, 3 in v0.25). This time it got harder and the search did not finish: **219 free seeds across six searches side by side, 40 cast sets to a seed, placed nothing.** Two experiments say where the difficulty is, and where it is not.

- **Not the placement rules.** The same 24 seeds under revisions 23, 24 and 25 (`about_to_trip` named 378, 379 and 379 times, `lost_balloon` 225 each, `sitting_on_air` 212 each) placed nothing under any of them. The rules added since v0.25 add almost no failures. This ran on the current cast, so it says nothing about the cast.
- **Not the room, for the right events.** The template sets that placed in v0.24, v0.25 and v0.26 were then forced, each from two seed lists. Each placed on the first seed of one list, in 7 to 17 seconds, after one, two and five rejected cast sets. Each failed the first seed of the other list, at eight cast sets to a seed. This release's tier-4 playground is the v0.26 picture's template set, forced (`regen.forced`, so it rebuilds exactly).

So the planner keeps drawing sets of nine events that cannot fit this setting. `cat_stalks_bird` is in 63% of its tier-4 playground plans, `about_to_trip` in 59% and `dog_begs` in 48%, and the first failures name `about_to_trip`, `lost_balloon` and `sitting_on_air`. Those three sets are of course sets known to fit, so this does not say how rare a fitting set is. Why it got harder after v0.25 is still not shown: a moved prior moves which sets are drawn, which would fit the timing, but it was not tested. For v0.28, the cheap test is a free search with the trip left out; the fix may be for the planner to try a set's footprint before it spends layouts on it. The rest of the set took 24 failed seeds (park), 14 (street) and the garden none, and the tier-4 isomorph 123 failed attempts.

This costs variety. The tier-4 playground repeats v0.26's events, as the tier-4 garden has repeated v0.24's since v0.24.
