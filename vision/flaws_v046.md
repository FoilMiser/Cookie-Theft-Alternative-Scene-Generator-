# v0.46 blind screen: what it found (the work list for v0.47)

The v0.46 screen read the set's 21 pictures and 77 probes with the prompts of v0.39 (`screen_prompts.md`). There were thirteen readers of seven or eight pictures and four scorers of 24 or 25. Four templates failed the legibility gate, and nothing was redrawn, swapped or read again after the screen (below). The oddity tally is by angle, as in v0.39. Keys, descriptions and scores are in `v046/`.

v0.46 worked one brief, Sam's: "make moves to improve the art style for v.046 and clean up issues like the woman in the yellow dress having a neck that is too long". Behind its first half was an item of the v0.45 set review, "Two outline systems in one picture". All of the work is in the cast (builder 0.46.0). The bench, in whole pictures and in enlarged figure cut-outs (`isolation_v046.md`), took these:
- **the line**: a figure's outer edge at 9.5 px at render size, which in a picture is the settings' own line, and the lines inside it at 5.5 px (v0.45 had one 5 px line); the line takes no light, so it is the palette's outline colour;
- **the shading**: two flat tones, the colour and a shadow at 0.86 of it, with no pool of light (v0.45 had three soft tones);
- **the necks** of the three figures with a scaled-down head (the woman in the yellow dress, the woman in purple, the man in the red shirt): the chin where a full-size head's is, no added neck, the neck at its full width, and every grown figure's neckline 1.4 cm higher. On the model the neck that shows on the woman in the yellow dress went from 8.2 cm to 3.9 cm;
- **her waist** wider (0.94 of the standard figure's for 0.86); **the arms**: a tee's sleeve nearer the arm's width, the shoulder lower and smaller, the resting arm nearer the body;
- **clean-ups**: no seam line at the wrist; the safety vest's bands on the vest all the way round; the glasses a plain dark wire; the moustache a smooth curve rounded at its ends;
- **the mouth** drawn as a line: the lip-coloured line at v0.45's width on a wider dark line of its own.

The placement rules are revision 43's. No scene rule was changed, and the scene items of `flaws_v045.md` (R1 to R3, O1 to O8) were not worked; they are carried below.

Every person and every animal is drawn anew, so no picture is identical to v0.45's, and there is no retest this time.

## Headline (the 21 pictures of the set)

| | v0.42 (21) | v0.43 (21) | v0.44 (21) | v0.45 (21) | v0.46 (21) |
|---|---|---|---|---|---|
| Things | 0.991 | 0.952 | 0.991 | 0.962 | 0.943 |
| Actions | 1.00 | 0.996 | 0.996 | 0.992 | 0.988 |
| Inferences | 0.939 | 1.00 | 0.971 | 0.984 | 0.914 |
| Contradictions | 0.942 | 0.712 | 1.00 | 0.955 | 0.923 |
| All items | 0.984 | 0.955 | 0.991 | 0.977 | 0.957 |
| Misread items | 0 of 290 | 1 of 290 | 0 of 286 | 0 of 281 | 2 of 282 |
| Readers' remarks per picture (all screened pictures) | 3.05 | 3.12 | 3.27 | 2.58 | 2.38 |
| Oddities per picture, as logged by the scorers | 0.7 (at most 3) | 1.1 (at most 3) | 0.7 (at most 3) | 0.5 (at most 2) | 0.2 (at most 1) |

The set reads below v0.45's on every row, and it has two misread items, where v0.44's and v0.45's had none. Of its 282 items 14 are under full marks:
- six setting items that a reader did not mention (the clouds in five pictures, a tree in one);
- three on the stopped hose in one picture (96);
- two on the reading dog and one on the thief bird in one picture (53);
- one on the walker about to trip (82);
- one on the lost balloon (17).

The fewer oddities are no gain to set beside that: the scorers logged 4 in the set's 21 pictures and 33 in the 77 probes, 0.4 a picture over all 98, where v0.45 had 0.3 over its 93.

Across all 98 pictures, 1,035 of the 1,063 scored items had full marks (v0.45: 992 of 1,009), and three were misread (v0.45: none). The 28 under full marks:
- **Thirteen on the clouds and three on a tree.** One reader left the clouds out of five of its eight pictures (34, 36, 37, 39, 40), a second out of five of its seven (92, 95 to 98), a third out of two (7, 8) and a fourth out of one (12). The tree was not mentioned in 5, 28 and 49 ("only bushes"). All sixteen are zeros on setting items. v0.45 had twelve.
- **The stopped hose, five items in three pictures of one reader (95, 96, 97).** Four half marks and a zero. The dog "may be standing on the hose or just in front of it" (96); "It is unclear whether the dog is actually stepping on and blocking the hose or its paw just overlaps it." (97); the nozzle's one drop was "a drop of water coming out" (96).
- **The reading dog, two items in one picture (53):** "A brown dog sits up holding a newspaper in its mouth." A zero for the oddity that was not noticed, and a misread for the reading.
- **The walker about to trip (82), a misread:** "The box is behind him, so he is not about to trip on it."
- **The fork sweeper (85), a misread:** the man is "leaning on a big silver fork and digging into the ground", and the dustpan is a "Red trowel".
- **Three half marks:** the thief bird "perched right beside it, looking ready to steal it" (53); the balloon that "may have slipped from the girl (she reaches for it), or it may belong to no one" (17); the upward water that "looks more like a spray than a pour" (52).

The scorers gave five, seven, four and twelve items under full marks, of 286, 253, 266 and 258. Ten of the fourth scorer's twelve are in one reader's seven pictures (92 to 98), the hose's five among them.

**What the full marks rest on.** The scorers' notes mark 11 items they credited in full where the free description commits and the unsure section adds another reading, or where the reader's word is near the key's and not the same (9 in v0.45): three on the ice cream (held, not eaten; the eater called a girl), three on the ball in the tree, two on the lost balloon, and one each on the stalked bird, the upward water and the walker about to trip. Halved, they take two more templates under the gate, `lost_balloon` (0.833) and `water_upward` (0.889): 58 of 64 on the strict reading, for the gate's 60 (`tpdb_work/strict46.py`).

## What the screen says of the cast

The screen's prompt asks what is in a picture and what is happening, not how a figure is drawn. So it can show that the new drawing harmed a reading; it can show little about whether it is the better drawing. That was the bench's question (`isolation_v046.md`: beside v0.45's, the better drawn in six figure pairs of eight, and the nearer to the background's drawing in seven).

- **The woman in the yellow dress** is in 30 of the 98 pictures. She is a woman in 29 descriptions and a girl in one: "A girl with dark hair, wearing a yellow dress and red shoes" (42), as in one of v0.45's. No reader named her neck.
- **The mouths.** No reader wrote of blood, a cut or a wound at a mouth.
- **The line and the flat tones.** No reader remarked on a figure's outline or line weight. One read the shadow tone as a fault: "There is a slightly lighter, semi-transparent patch on the front of her dress where her arms cross. It could be shading, or her arm drawn faintly through her body." (89, the woman in the yellow dress digging). In the picture it is the shadow tone's hard edge across the chest beside the arm; nothing is transparent. The bench's reviewers had called the same tone "a fold or stain" on a lap. O2 below.
- **The moustache, which this release redrew, reads worse than v0.45's did.** The man in the red shirt is in 11 pictures. A moustache is named in four descriptions, a beard in three (one has both), and neither in five. Two readers, unprompted: "The brown mark under the man's nose reads as a moustache, but it could also be a smear of something (for example chocolate) on his face." (9); "The red-shirted man's face mark reads as a moustache or beard but looks a little like a smudge." (92). No description of v0.45's screen has either word. Two readers naming one oddity make it a work item by the runbook: O1 below.
- **Whether the heavier line cost a reading cannot be told from one screen.** Two of the three misreads are of figures whose pose is v0.45's and whose outline is new (the reading dog, the walking reader). Both templates lost readings in earlier screens too (`about_to_trip` 0.889 in v0.42; `dog_reading` 0.533 in v0.43 and 0.833 at v0.45's first count), and with no retest there is no picture to set the two drawings side by side. It is recorded as open, not as cleared.

## The v0.45 list

None of it was worked. What the readers said of each this time:

| v0.45 reading | v0.46 result |
|---|---|
| R1: `bird_steals` 0.933; 0.889 in profile | **0.972** (18 items, 6 pictures), one half mark: "perched right beside it, looking ready to steal it" (53). In profile 0.958 (12 items, 4 pictures); at the three-quarter angle 1.00. R5 of the next list |
| R2: `square_wheel` 0.933, "a bit squared/boxy" | **1.00 in six pictures** (18 items): "a red bicycle with square wheels, which is impossible to ride" (53). Its fix is kept on the watch list |
| R3: `cat_stalks_bird` 0.958, the bird "standing on the grass" | **1.00 in five pictures** (15 items), one of them a judgement call: the bird standing, not pecking (48). R6 |
| O1: the seesaw's riders over or above the plank | Still seen: "hard to tell whether the children are seated on the seesaw plank or perched slightly above it" (70); "the boy sits slightly above the seesaw plank rather than on it" (93); and on the slide, "the child sits slightly above the slide surface" (94). O3 |
| O2: the wet paint away from the roller | Still seen, and more strongly, in design test 3: the roller "well away from the blue part of the fence". In the screen, "the woman's reach with the long-handled roller close to the fence is slightly awkward" (49). O5 |
| O3: figures drawn over the pond | Still seen: "the boy overlaps the edge of the pond and could be read as standing in the water" (38); "the man's body overlaps the front edge of the pond" (41); "the grandmother at a glance seems to stand in the pond" (60). O4 |
| O4: the reading dog that "could simply be holding/carrying the paper" | **Failed the gate**: 0.867 (15 items, 5 pictures), one misread (53). R1 |
| O5, O6: the swing; the fence cat | No remark logged in three pictures each |
| O7: one picture each | A shadow apart from a jumper again, the cheering boy's (57). The rest not seen |
| O8: the goat "a little unusual" | Again in two of five pictures (42, 63), and "It could possibly be read as a white sheep or a young goat (kid)" (42) |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.42 | v0.43 | v0.44 | v0.45 | v0.46 |
|---|---|---|---|---|---|
| Pass | 63 | 62 | 63 | 64 | 60 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 2 | 1 | 0 | 4 |

This is the first count. There was no fix and no re-read after it (below).

The four that fail:
- `dog_reading` (0.867, 15 items, 5 pictures, one misread);
- `about_to_trip` (0.889, 9 items, 3 pictures, one misread);
- `sweep_fork` (0.889, 9 items, 3 pictures, one misread);
- `blocked_hose` (0.893, 28 items, 7 pictures, no misread).

The lowest that pass:
- `lost_balloon` (0.944, 9 items, 3 pictures);
- `water_upward` (0.944, 9 items, 3 pictures);
- `bird_steals` (0.972, 18 items, 6 pictures).
Every other template reads 1.00.

Every template was screened in at least three pictures. By count: 38 in three, 12 in four, 6 in five, 3 in six, 3 in seven, 1 in sixteen and 1 in twenty-one, with 482 scored items behind the verdicts.

**Per angle** (`v046/gate_yaw.json`), 20 of the 22 (template, angle) pairs pass. The two that do not are the hose's dog in profile (0.875, 8 items, 2 pictures: 95, 97) and at three-quarter from the front (0.833, 12 items, 3 pictures: 96); seen at three-quarter from behind it reads 1.00 (8 items, 2 pictures). All five items are one reader's, so the split by angle may be the reader's and not the angle's. The thief bird in profile is 0.958. The oddities by angle: a songbird in profile twice (30, 48), the stalking cat in profile once (48), a dog at three-quarter from the front twice (40, 78), the goat three times (42 twice, 63).

## After the screen

The four failures stand. Three earlier releases shipped with their gate failures listed (v0.42 one, v0.43 two, v0.44 one); v0.45 fixed its one and read three pictures again. This release does neither, for these reasons.

**`dog_reading` (53).** Four readers of five read it: "sitting up on hind legs holding an open newspaper as if reading" (17); "sits up on its hind legs holding an open newspaper in its front paws, as if reading it, which is impossible for a real dog" (24). The fifth saw the paper "in its mouth". In that picture the forepaws and the paper's top corner lie over the muzzle. The pose and the paper's place are v0.45's; only the line is new. Two of the four who read it add the other reading as before: "The dog could alternatively have grabbed the newspaper to chew or play with, but the pose looks like reading." (24); "Either the dog is just holding or carrying the paper, or it is reading it like a person." (82). The mend is v0.45's O4, which was carried and not done: a pose of its own, with bent forelegs and the paper held clear of the head. That is a new pose in the cast, a bench and a calibration, not a change to make after a screen.

**`about_to_trip` (82).** The boy reading as he walks faces left, toward the box at his feet. The reader had him "heading right, near the birdhouse pole", the box "behind him", and wrote that he "may be about to bump into it" of the pole. The bird table's post stands directly behind his back, and the walk pose's trailing foot points backward like a leading one. The other two pictures read: "A blue bucket stands on the pavement just ahead of her, so she might trip over it." (12); "he seems likely to trip on it, though he may also just walk past it" (53). The mend is in the walk pose, which every walker of the cast shares, and in a rule that keeps a post away from the back of a walker who heads for an obstacle. Both need a bench.

**`sweep_fork` (85).** Two of three read it: "using it to sweep a little pile of dirt and dust into a red dustpan lying on the path" (10); "reads as a deliberate absurdity" (50). In the third the heap lies at the path's edge and the dustpan wholly on the grass; the reader saw a man "digging into the ground" with a fork that "looks like a giant dinner fork", and took the pan for a trowel "lying beside the digging spot, not being used". The placement rule checks that the fork's tip and the heap are on the paving, and does not check the pan. A rule that asked for the whole pan on the paving was measured and not made: on the garden's path, 111 px wide at its far end and 295 at its near, the sweeper, the fork, the heap and the pan take about 250 px in a row at this scale, so the rule would all but end the template in the garden. The heap and the pan have to be drawn to fit the path first, then benched, then calibrated.

**`blocked_hose` (95, 96, 97).** Four pictures of seven read in full: "the bulge in the hose behind the dog suggests the dog is blocking it" (19); "only a single drop is coming out, so the water is not flowing" (32); "Either way, the dog seems to be stopping the flow." (45). The three that did not are one reader's, who hedged each ("or the paw just overlaps it in the drawing", 95) and in one made no link between the dog and the water (96). The drawing is v0.45's, where the template read 1.00 over the same 28 items. What the hedges point at is real all the same: the paw's contact with the hose is small, and a drop at the nozzle can be water coming out as well as water stopped.

**Why no picture was swapped or read again.** A probe swapped for one that looks better to the builder is selection, and a second reading of an unchanged picture is a second roll of the dice; either would raise the count without a change in what a patient sees. v0.45's note on what a re-read costs holds here too. The numbers above are the first and only count.

**What it means for the release.** v0.46 is a change of drawing style with a weaker screen than v0.45's: 0.957 for 0.977 on the set, three misreads for none, 60 of 64 for 64 of 64. The cast's changes were judged on the bench and are kept; the four templates are the first items of v0.47.

## What reads least well (the v0.47 list)

| # | Template | v0.46 | What the readers saw | Fix for v0.47 |
|---|---|---|---|---|
| R1 | `dog_reading` | 0.867 (15 items, 5 pictures), one misread | "A brown dog sits up holding a newspaper in its mouth." (53); holding or carrying beside reading in two more (24, 82) | v0.45's O4, now first: a pose of its own in Blender, forelegs bent, the paper held open in both paws below the muzzle and clear of the head, the head tipped down to it. Bench it alone and in a picture before the set |
| R2 | `about_to_trip` | 0.889 (9 items, 3 pictures), one misread | The walker read as heading the other way: "The box is behind him, so he is not about to trip on it." (82) | The walk pose's trailing foot on its toe, heel up, so the way a walker goes shows in the feet; no post or pole within a body's width behind a walker who heads for an obstacle; the obstacle a step ahead of the leading foot |
| R3 | `sweep_fork` | 0.889 (9 items, 3 pictures), one misread | Digging at the path's edge, the dustpan a "Red trowel" on the grass (85) | The heap and the pan drawn shorter so that fork, heap and pan fit the garden's path; the whole pan on the paving by rule; dust and a few leaves in the heap so it is sweepings and not soil. Bench, then calibrate |
| R4 | `blocked_hose` | 0.893 (28 items, 7 pictures); 0.875 and 0.833 at two angles | "The dog may be standing on the hose or just in front of it." (96); "a drop of water coming out" (96); a bulge, a blob or a puddle in the pictures that read | The hose pinched flat under one plainly planted forepaw, swollen behind it; no drop at the nozzle, or the nozzle held up and looked into with nothing coming |
| R5 | `bird_steals` | 0.972 (18 items, 6 pictures) | "perched right beside it, looking ready to steal it" (53) | Carried a second time: the bird's head down and its beak in the sandwich, a bite out of the bread, crumbs under it |
| R6 | `cat_stalks_bird`, `water_upward`, `lost_balloon` | 1.00, 0.944, 0.944 | The stalked bird standing, not pecking (48); the water "more like a spray than a pour" (52); the balloon that "may belong to no one" (17) | The bird's head down at seeds; the upward water as one stream that leaves the spout and bends up; the balloon's string nearer the reaching hand where the fence allows |

## Unintended oddities

Named kinds, from the scorers' lists (`v046/scores_summary_a.md` to `_d.md`) and the readers' unsure sections, most worth doing first. The scorers logged 37 in 98 pictures. The first two are this release's own.

| # | Sev | Oddity | Where | Fix for v0.47 |
|---|---|---|---|---|
| O1 | B | The moustache of the man in the red shirt: "it could also be a smear of something (for example chocolate) on his face"; "looks a little like a smudge"; "the red-shirted man's face mark looks like a smudge rather than a moustache or beard" | 9, 92; design test 2 | Draw it again: wider than the mouth, in two halves parted under the nose, clear of the mouth's line, a shade darker than the hair. Bench it in whole pictures at picture size, where this one was read, and not only in cut-outs |
| O2 | B | The shadow tone read as a patch: "a semi-transparent patch on the woman's dress, as if her arm is drawn faintly through her body" | 89 | Keep the shadow's edge off the middle of a chest or a lap: on a broad cloth it should follow the figure's side or a fold. Look at every pose of the dress |
| O3 | B | Riders above their seat: "the boy sits slightly above the seesaw plank rather than on it"; "the child sits slightly above the slide surface" | 70, 93; 94 | v0.45's O1, carried: the plank over the far leg and under the near thigh; the slider's seat on the chute |
| O4 | B | Figures over the pond: "the grandmother at a glance seems to stand in the pond" | 38, 41, 60 | v0.45's O3, carried: a near bank, or the standing figure's feet a clear step off the water's edge |
| O5 | B | The wet paint and the roller: "well away from the blue part of the fence" in design test 3; the reach "slightly awkward" | 49 | v0.45's O2, carried: the painted boards next to the roller on both sides, the roller's head flat on a board |
| O6 | B | Stiff legs: "the woman's running pose is stiff, with the back foot kicked up high"; "the boy's legs look short or tucked, hard to tell if straight or bent"; "the dog's front legs and body are drawn in a tight, slightly tangled pose" | 31; 90; 78 | With R2: the runner's and the walker's rear leg; the sitting boy's legs. The dog: watch |
| O7 | C | Things that overlap or float: "the sandwich overlaps the man's legs, so it could be on his lap or on the bench"; "the bird sits partly beyond the end of the bench and can look as if it is hovering"; "the dog is drawn quite small and overlaps the door step"; "the bikes sit inside the rack outlines rather than leaning on them"; "the cheering boy's shadow is drawn apart from his feet: jumping or a misplaced shadow" | 28; 30; 40; 88; 57 | One picture each: watch. The bench's sandwich and bird go with R5 |
| O8 | C | Where a thing stands: "the pram is partly off the path on the grass"; "the woman walks on the grass beside the path rather than on it"; "the lamppost stands alone on open grass away from the path"; "the man seems to dig into the paved path or its edge" | 39; 48; 90; 85 | The last is R3. The rest: watch |
| O9 | C | Hard to make out: "the flying blue cap could be read as a bird"; "the spade blade is hard to make out against the soil"; "the girl's ice cream is held almost touching her cheek"; "the two women look identical (same face and hair), only their clothes differ" | 34; 47; 42; 47 | Watch. The two women are a cast note: the woman in the yellow dress and the woman in purple have hair of one colour, and the second's ponytail hardly shows from the front |
| O10 | C | The goat in a park "a little unusual", and "could possibly be read as a white sheep or a young goat (kid)"; "a bottle that looks like wine sits beside a child at the picnic"; "eating ice cream on such a gloomy day is a little unusual"; "watering the garden just before a storm could be read as the odd thing"; "two people eat the same pink ice cream but no ice-cream seller is visible"; "the girl does not look upset although her kite is stuck in the tree" | 42, 63; 37; 65; 19; 69; 36 | Notes for the pilot. The bottle could be a juice bottle; the dark sky is not placed with an event that fair weather explains |

For the watch list as well:
- the square wheels' fix of v0.45's list, not needed by this screen;
- the woman in the yellow dress read as a girl once in 30 descriptions, and once in five design tests;
- her neck with the ice cream, which bench reviewers called a little long in v0.45's drawing and v0.46's alike, and which no reader of whole pictures named;
- the mouth on a face in profile, and the darker mouth under a moustache (`isolation_v046.md`);
- the validator's palette warning on 154 of the library's 400 records, for the blended band where the heavier line meets a fill; the target was not loosened;
- the garden's sets that could not be placed for the design tests (watering with planting and raking) and the park's (the picnic with the angler and the pram);
- the balloon under the fishing float in one probe, kept after a rebuild;
- only one street among the probes.

## Placement

**The set.**
- **Tiers 1 to 3.** Every cell placed on its base seed, the tier-3 playground among them, which v0.43 to v0.45 had to search for.
- **Tier 4.** The park and the street placed on earlier releases' seeds at the first try. The garden failed v0.45's seed and the next two and placed on the fourth, s552986; the playground failed v0.45's and six more before s487950 placed.
- **Templates.** The cast's drawing alone moved 44 numbers of the calibration by 0.002 or more (the largest 0.05) and 18 lines of the prior, and with them the planner's choices: five cells have v0.45's templates and eleven do not.
- **The isomorphs** are five, as before: two of tier 2 (a street of the park, a playground of the garden), two of tier 3 (a street of the park, a garden of the playground) and one of tier 4 (a garden of the playground).

**The probes.**
- **The first pass** (`probes.py 3`, with five for `bird_steals`, `square_wheel`, `cat_stalks_bird`, `dog_reading` and `ice_cream`) built 56 and ended `SHORT {'rain_coming': 0, 'dog_begs': 2, 'windy_hat': 0}`, counts of pictures: the coming rain and the blown hat each failed three times beside a garden partner.
- **The pass stratified by angle** added 15.
- **Six more** were forced in small groups (`tpdb_work/more_probes46.py`), three with the coming rain and three with the blown hat, and every template then had three pictures or more. Two were rebuilt after the builder's look, before any reader saw them: a kite's string that ran past a painter's shoulder, and a balloon that sat under a fishing float. The 77 probes are 42 gardens, 27 parks, 7 playgrounds and 1 street.

**Slips in the blind rule.** Three of the thirteen readers listed the screen's folder and so saw the names of the other description files; none opened a file but its own pictures, and the files' times show that no reader wrote over another's. One of the three did so after its first write had failed. Three of the four scorers wrote a small script to add up their scores; none saw a picture.

All 98 records rebuild identical to the pixel, and the library passes the validator in full.
