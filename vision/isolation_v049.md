# v0.49 isolation bench

The brief for v0.49 was Sam's: "go for v0.49 now! This is an improvement, but I am not sure if I love this head shape either, they look a little like bowling pins since they do not have chins. want to focus on a better head shape first using blender and carefully choosing a good style to go with?" The list beside it is `flaws_v048.md`: R1 `rain_coming`, which failed v0.48's gate, R5 the ice cream that stops short of the mouth, and O1, grown figures read young and facial hair unseen.

This file has three parts: the study of the head and the two blind benches that judged it, what changed with the head, and the single events cut out of scenes.

## The study of the head

**What v0.48's head was.** An egg (`castlib/core.py`, `TPDB_HEAD48`): 0.92 of its radius wide and 1.06 tall, narrowing below the cheeks to a rounded point. At nine tenths of the way down it is 0.31 of its half width across, and the neck under it is 0.43, so the jaw's line ran straight on into the neck's and no chin showed. The neck's skin also swelled between the collar and the jaw. The reviewers of the first bench below, who did not know which drawing was which, had v0.48's row as "a circle sitting on a stalk", "a light-bulb or inverted-pear shape" and "a balloon on a stick".

**The new head** (`TPDB_HEAD49` B; O builds v0.48's). Below its middle the head's outline is a superellipse, fuller toward the bottom than a ball's, times a taper: the cheeks come down to a corner and the chin is a rounded shelf wider than the neck. The face's side of the head has the same corner, so a side view has a chin and a jaw under it. A shape is a short list of numbers (`core.HEAD49_SHAPES`: the fullness `m`, the taper `jaw`, where it starts `z0`, the width, depth and height, the neck's width at the jaw), and a person's spec names one, so men, women, the teenager and the children differ. One map (`head_pt`) still places the head, its hair, its hats and every feature of the face.

Each trial was built on two figures and then six in Blender and rendered at 800 px per metre, twice the release's size, as a sheet of heads with a row at scene size under it (`tpdb_work/v049/trys.sh`; a build and its renders take about a minute). About thirty shapes were looked at on my own sheets; four went to reviewers:

| Shape | What it is | Fullness `m`, taper `jaw` (a man's) |
|---|---|---|
| T, tapered jaw | the cheeks narrow in a nearly straight line to a flat chin | 4.5, 0.40 |
| U, round jaw | full cheeks down to a broad, rounded chin | 3.2, 0.28 |
| V, small chin | a strong taper to a small chin, nearest v0.48's egg | 3.0, 0.46 |
| S, soft square | the sides nearly straight, a wide flat jaw | 4.0, 0.14 |

**Two faults of line, found on the sheets and mended before any reviewer.** With the neck a piece of the skin's one mesh, which draws no intersection lines (v0.39), the chin's line across the neck came out as two stubs or as dashes: the head's underside is buried in the neck there, and Line Art hid or showed whole segments of it. The neck is now a part of its own (`TPDB_NECK49` B) that keeps its intersections, so the line where the neck passes into the head is drawn whole and the head's outline is cut exactly where it meets the neck; the head is also carried a tenth of its radius forward of the neck and the neck's top set back, so from the side the jaw stands ahead of the neck. Second, a short dash on the front of a slim dress, under the collar: the rim of the neck's rounded foot, which came to the cloth from behind. The foot is narrower, and the neck keeps v0.48's width up to the collar and narrows from there to the jaw.

**Bench 1, a ranking** (`isolation_v049/heads1`). Nine heads, the same in every row (a woman from the front and turned, a man from the front, turned and from the side, the older woman, the bearded man, two children), drawn five ways: v0.48's and the four shapes, as rows A to E in an order shuffled for each of four fresh reviewers. Each described every row, said whether the grown figures look grown and whether the head has a chin, and ranked the five.

| Reviewer | Best to worst |
|---|---|
| 1 | U, V, S, T, v0.48 |
| 2 | T, U, S, v0.48, V |
| 3 | V, U, T, v0.48, S |
| 4 | V, T, S, v0.48, U |

v0.48's head is last or fourth for all four, and is the only row no reviewer placed above fourth. Beyond that the bench does not order the shapes: every reviewer put the row at the top of the sheet last and the second row fourth, whatever was in them, and three different shapes were somebody's first. A sheet of five rows at this size is read by position as much as by drawing. One reviewer said as much of the three rows it liked best: "Rows C, D and E differ only a little at this size, so the fine points between them are less certain than the points about A and B."

**Bench 2, pairs** (`isolation_v049/heads2`). The three shapes that had been somebody's first, two at a time, eight heads to a row at a larger size, each pairing in both orders so that the place on the sheet cancels: six fresh reviewers. Each said, figure by figure, which row draws it better, and chose a row.

| Pairing | Row a above | Chose | Figures to T, U, V and neither |
|---|---|---|---|
| T and U | T | U, "fairly sure" | T 0, U 4, neither 4 |
| T and U | U | U, "toss-up" | T 1, U 4, neither 3 |
| T and V | T | T, "toss-up" | T 3, V 2, neither 3 |
| T and V | V | T, "fairly sure" | T 4, V 0, neither 4 |
| U and V | U | U, "fairly sure" | U 5, V 1, neither 2 |
| U and V | V | U, "fairly sure" | U 4, V 1, neither 3 |

The round jaw was chosen over the tapered jaw and over the small chin, and the tapered jaw over the small chin, each in both orders. Of the tapered jaw beside the round one: "Row a tapers to a small chin under a wide cranium, which looks boyish, while row b's broader, flatter jaw reads as an adult man." Of the small chin: "a narrow, tapering V-shaped lower face that ends in a small pointed chin". The differences are small on the women and the children, and the reviewers said so: "The difference is strongest on the men (front, turned, side and bearded) and slight on the women and the child." One of the six described its two rows the wrong way round and chose the round jaw all the same; its choice is counted and its words are not used.

**The choice: U, the round jaw.** It won both of its pairings in both orders, it is the furthest of the three from the narrow chin on a neck that Sam named, and a broad jaw is what the reviewers read as a grown man. As built (`core.HEAD49_SHAPES`): a man's `m` 3.2 and taper 0.28 on a neck 0.90 of v0.48's width at the jaw; a woman's a little narrower in the chin (`m` 3.0, 0.34) on a neck of 0.82; the teenager's between them; a child's as wide as it is tall with a small taper (0.20). The soft square was third for three of bench 1's four reviewers and last for the fourth, and was not paired.

A sheet of the five shapes went to Sam before the cast was built (`isolation_v049/head_candidates.png`), with the round jaw named as the one the release goes ahead with.

## What changed with the head

- **The moustache** (`TPDB_MOUSTACHE49` B; `flaws_v048.md` O1). v0.48's short, thin moustache was named by the screen's readers in none of its wearers' seventeen pictures. It is a fifth wider and a quarter thicker, its ends a little lower, still clear of the mouth; v0.47's larger one stays as it was left.
- **The ice cream** (`TPDB_ICE49` B; R5). On v0.48's face the cone stopped a hand's width short of the mouth. The scoop's near side is now a finger from the lips with its middle just under the mouth, nearer still on a child, whose head is large against its reach, and the head tips twelve degrees to it for six.
- **A hand held out for the rain** (the pose `feel_rain`; R1): a figure looks up with the far hand held out in front, palm up. It is the storm watcher's pose from revision 46 (`templates.RAIN49`).

Looked at on my own sheets: all ten people from the front, at three-quarter and from the side; all nineteen expressions on the woman from the front and ten on the man from the side; a dozen poses that move the head or bring a hand to it (looking up, looking back, reading, drinking, the camera, the bucket, hands to the face); the back and far-side views of six figures.

## The age bench

`flaws_v048.md` O1 had four grown figures called a girl or a boy in 11 of their 81 screened pictures, and the runbook asks for an age question on the bench whenever a release changes heads. Eight people (the three women, the four men and the teenager), each standing at three-quarter and walking in side view: 16 figures of a cast at 0.45 of the release's size, in four strips of four different people, each strip read by one fresh reader who said what they would call each person, how old the person looks, what is on the face or the head and how sure they were (`tpdb_work/v049/who.py`, counted by `who_tally.py`; `isolation_v049/who` and `who2`, the maps in `map.json`). Four casts were read: v0.48's, v0.49's, and v0.49's with every grown figure's head at 0.90 and at 0.83 of its size against the body (`TPDB_HS49`, a bench switch in `castlib/specs.py`), tried after the first two casts came out alike.

| Of the 14 grown figures | v0.48's cast | v0.49's cast | head 0.90 | head 0.83 |
|---|---|---|---|---|
| Called by a young name first | 1 | 1 | 1 | 0 |
| A teenager, a boy or a girl offered as what else the figure could be | 10 | 9 | 9 | 8 |
| The reader "sure" of the name | 6 | 6 | 4 | 7 |

The young names: the worker walking in v0.48's cast, "a boy / young man"; the woman in purple standing in v0.49's, "A girl (or a teenage girl)"; the worker walking with the head at 0.90, "A boy, or a young worker". The teenager was "A boy" or "a boy" in all eight of his figures.

The bench shows no difference between the two heads, and none worth the name between the head's sizes. Neither a jaw and a chin nor a smaller head makes a figure of this size read older. What the readers go by is elsewhere: "slim build, no clear age cues on the face", "the face looks fairly young and smooth", and of the one woman called a girl, "she is a little shorter than the others, which is what suggests a girl". Grey hair, glasses, a cap and a moustache are named as the reason every time a reader is sure of an older figure. The head's size stays as it was.

The moustache: of the six figures with a moustache or a beard, v0.48's cast had it named on four and "may be" on one; v0.49's had it named on five and "not clear" on one. The wider moustache was named on all four of its figures, "A moustache" and "a grey moustache", where v0.48's had "small grey/dark mark under the nose" and "There may be a small dark moustache, but it is hard to tell at this size."

So O1 is carried. The cure, if there is one, is a mark of age that a reader can see on the smallest figure a scene draws, and the two smooth-faced women and the worker have none. The screen's own count over its eighty-odd pictures is the measure.

## Single events, cut out of scenes

A case is one event forced alone into a picture on one seed (`vision/isolation_bench.py`, the cases named `*xN_*` for the release's drawing and `*xO_*` for the one beside it); a reader writes what it sees and what it is unsure of, and reads at most one take of a thing. Both rounds were built while the revision's edge rule still applied to every figure and not to animals only (`scene.EDGE49`); the rule moves where a figure may stand and draws nothing, so the cut-outs are kept as they were read.

**Round 1, eleven pictures, six readers** (`isolation_v049/round1`).

*The storm watcher.* Four pictures of a watcher who looks up with a hand held out, palm up (`templates.RAIN49` B), and two of v0.48's pointer on two of the same seeds; the whole picture each time, since the clouds are the setting's. Both readers of the pointer went on to the rain: "pointing up at the clouds with a worried or frowning face, as if she has noticed that rain is coming"; "He seems to be pointing at the dark clouds, as if warning that rain is coming." Of the hand held out, one reader had the rain first, "palm out, as if checking for rain", with "pointing toward the wheelbarrow or watering can" offered beside it. Two had it as one of two readings: "as if checking for raindrops or gesturing toward something"; "It could be something she is holding, such as a pencil or a stick, or she could just be pointing or holding her palm out to feel for rain." And one did not have it: "looking and pointing toward the right, roughly at a small café table with two chairs", and of the sky, "The dark clouds could mean rain is coming, or they could just be background." At a picture's size an open hand held level is a finger pointed at whatever stands in front of it. The pointer stays (`RAIN49` O is the release's), and the probes give `rain_coming` five pictures where it had three.

*The ice cream.* Four cut-outs with the scoop at the mouth (`TPDB_ICE49` B). All four readers have it eaten: "He holds a pink ice-cream cone up to his mouth with one hand and appears to be eating or licking it."; "is eating or licking it". v0.48's screen had "she may be about to eat it or just carrying it". Three of the four add that it is too near: "The ice cream is pressed right against his face so it partly covers the mouth/nose"; "The ice cream almost looks pressed into his cheek or nose instead of just held at his mouth." The scoop was moved a finger further off and lower, its top level with the mouth; round 2 reads that.

*The goat's rope.* One cut-out with the heavier rope (`templates.ROPE49` B): "A tan rope runs from the collar down to a short brown stake in the ground, so the goat is tethered." The same reader of its path: "It seems to start near the collar or face and loop down in front of the goat's chest and front legs". v0.48's screen had the rope "thin and hard to see". The weight is kept.

**Round 2, two cut-outs, two readers** (`isolation_v049/round2`). The ice cream a finger further off and lower, on two of round 1's seeds: "He holds an ice-cream cone with a pink scoop up to his mouth with his right hand, as if eating or licking it."; "as if about to lick or eat it". Both still note how near it is, "it reads as eating, but the hand and cone are close enough that the cone could also look like it is touching or pressed into his face", and both have the eating first. It goes to the design tests as it is.
