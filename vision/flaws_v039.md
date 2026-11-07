# v0.39 blind screen: what it found (the work list for v0.40)

The v0.39 screen read the set's 21 pictures and 75 probes. It used the prompts of the screens before it (`screen_prompts.md`) with one addition. Each picture's key now lists the animals drawn in it with their angle, and the scorers end an oddity about an animal with that angle, so the oddities can be counted by angle (figure-fixes-v038.md 4b.5).

96 pictures took twelve readers of eight pictures and four scorers of 24. That is the load v0.38 gave its nine readers and three scorers. Keys, descriptions and scores are in `v039/`.

## Headline (the 21 pictures of the set)

| | v0.35 (21) | v0.36 (21) | v0.37 (21) | v0.38 (21) | v0.39 (21) |
|---|---|---|---|---|---|
| Things | 0.971 | 1.00 | 1.00 | 1.00 | 1.00 |
| Actions | 0.996 | 1.00 | 0.996 | 1.00 | 1.00 |
| Inferences | 0.957 | 0.971 | 0.971 | 0.985 | 1.00 |
| Contradictions | 1.00 | 1.00 | 0.977 | 1.00 | 1.00 |
| All items | 0.982 | 0.996 | 0.993 | 0.998 | 1.00 |
| Misread items | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 286 | 0 of 287 |
| Readers' remarks per picture (all screened pictures) | 2.88 | 3.10 | 2.82 | 3.38 | 3.10 |
| Oddities per picture, as logged by the scorers | 0.2 (at most 3) | 0.6 (at most 3) | 0.4 (at most 3) | 0.8 (at most 3) | 0.8 (at most 3) |

Across all 96 pictures, 1025 of the 1030 scored items had full marks and none was misread. All five items under full marks are on probes:
- **The girl's ice cream, half right twice (04, 77).** In both, she is the company of a goat probe, placed small at the back: "She is holding something small and pink up to her mouth with both hands, probably eating a small ice cream or sweet".
- **The dog wanting a walk, half right (26):** it wants "to go for a walk or wants to go inside".
- **The man sweeping with the giant fork, half right (47):** read as "scraping or digging at a small pile of dirt".
- **The clouds of the windy park, scored 0 (21).** This is a setting item, which the gate leaves out.

The four scorers gave 2, 2, 0 and 1 items under full marks, out of 282, 246, 269 and 233.

**What the full marks rest on.** Scorers a and c listed 11 credits they gave in full where the free description commits and the unsure section adds another reading. v0.38's scorers listed 23 such credits. If those 11 are halved, 63 of 64 templates still pass (`tpdb_work/strict39.py`). The one that falls is `windy_hat`, to 0.889 (9 items, 3 pictures), on two of those credits. One reader offers the alternative "as her throwing her hands up in alarm" (71), as v0.38's readers did.

## A retest, a tenth time, with the cast redrawn

No picture can be identical to the pixel in two screens when the cast is drawn again. Instead, 7 pictures carry the same name, seed, cell and events in v0.38 and v0.39, each drawn first with v0.38's cast and then with v0.39's (`tpdb_work/retest39.py`):
- the tier-1 garden, park and playground;
- the tier-2 garden;
- the tier-4 garden and park;
- one garden probe.

| On the same 7 pictures, each in its own cast | v0.38 | v0.39 |
|---|---|---|
| Items | 75 | 75 |
| Items with the same score in both | 75 | 75 |
| Remarks | 28 | 25 |

Every item scored the same, and the remarks fell by three. The redrawn cast reads as well as the old one on the same events.

## The v0.38 list

| v0.38 reading | v0.39 result |
|---|---|
| R1 `ice_cream_drop` 0.958 | **1.00** (16 items, 4 pictures, two at 45). v0.38's picture 72 has left the set: its cell's seed placed other events under revision 37. The dog is at the splat in all four, "So the child seems to have dropped their ice cream and the dog is eating it" (03). One reader still offers the knock in the unsure section, credited in full (60). Watch |
| R2 `play_catch` 1.00, 0.75 read strictly | **1.00** (6 items, 3 pictures), with no hedge left. The ball now stops short of the catcher's hands (revision 37). "she has just thrown a red-and-white ball" ... "ready to catch the ball, which is just about to reach him" (29); "so he appears to have just thrown the ball" (36) |
| R3 `windy_hat` 1.00, 0.778 read strictly | 1.00 again, and 0.889 read strictly. The same second reading, "throwing her hands up in alarm" (71). Below, as R1 |
| R4 `bird_steals` 1.00, 0.875 read strictly | 1.00 (18 items, 6 pictures), with one hedged credit (09). Holds |
| O1 The broom's and the rake's autumn leaves under green trees | **Changed, not gone.** The heaps are now drawn for summer (`draw.HEAP39` set to S), and no reader sets the season against the trees. Five pictures from four readers find the green in the heap odd for fallen leaves: "Some of the raked leaves are green rather than brown or autumn-coloured, which looks a little odd for raked fallen leaves" (43), and "so it is not clear whether they are fallen autumn leaves or just garden clippings" (36); and alike in 45, 49 and 70. v0.38: seven pictures from five readers. Below, as O1 |
| O2 The fish's branch bent toward it | **Not seen**, in three pictures, with the limb unchanged: "a goldfish is perched on a branch like a bird" (24) |
| O3 Goats out of place | As before, in four pictures (32, 75, 77, 83): "The goat is the strangest thing" (83, in a garden). Notes for the pilot |
| O4 A figure over the thing beside it | As before: the photographer and the fisherman over the pond (03, 20), the seesaw man over the plank (33, 96), a girl over the sandpit's frame (31), a bicycle wheel through the rack's hoop (90) |
| O5 Older ones | As before: wind that moves only the hat (57, 71), the riderless bicycle standing (59), market stalls with no seller (68, 90) |

## The cast round and the angles (figure-fixes-v038.md, hang-laundry-gate-v038.md)

| What v0.39 changed | What the screen read |
|---|---|
| Intersection lines where limbs cross (`TPDB_ISECT39` B) | No remark about a line where a limb crosses the body; the overlaps logged are figures over props (O4) |
| Feet and ankles (`TPDB_SHOE39` D) | Mei's red flats were read as "pads" three times on the bench (`isolation_v039.md`) and drew no remark here. A foot's direction drew two: "The boy's feet point in different directions" (93), as for the shopper in design test 2, and the grandfather walking the dog, whose stepping leg is hard to tell (46) |
| Ben's adult cues (`TPDB_BEN39` C) | Ben is read as a man in all 17 of his pictures, mostly as "a man with brown hair and a moustache". In v0.38 he was a boy to 3 readers of his 19 pictures and a young man to 2 |
| Mid-sections and belts (`TPDB_MID39` C, `TPDB_BELT39` O) | No remark |
| Quadrupeds' legs and paws, the animal art (`TPDB_QUAD39` B, `TPDB_ART39` B, the goat white, `TPDB_GOAT39` D) | No remark about a dog's or cat's legs, at any angle. The goat is no longer "a sack or blanket" (design test 1). Its grazing head now merges with the tuft of grass under it, three times (01, 04, 08): "The goat's head is small and low against the grass tuft, and at first glance it is hard to tell head from tuft" (01). And once "Its body shape is a bit thin and angular, and its legs look stick-like, but it is clearly a goat" (83) |
| Animals at more angles (revision 37, `templates.ANIMAL_YAWS`) | Every (template, angle) placed was screened in at least two pictures, and all 17 pass at 1.00 (`v039/gate_yaw.json`, `tpdb_work/gate_yaw39.py`). The dog walked at 45 never placed (Placement, below) and is drawn at 90 |
| hang_laundry, cat_sleeping and plant_flowers in five pictures each (hang-laundry-gate-v038.md) | All three at 1.00 in five pictures. Every reader has the washing hung out; the one who raises taking it down settles it: "but the drips and the full basket suggest he is hanging it up" (28) |

The scorers tagged 13 oddities about animals with their angle. The keys list 73 animals across the 96 pictures, each kind and angle once a picture:

| Angle | Animals drawn | Oddities | Of which |
|---|---|---|---|
| Profile | 44 | 6 | Goat 3 (a loose goat twice, its head in the tuft once); dog 3 (the reading dog's paper standing up, the hose under its paws "a dark flattened blob", paws near a bench leg) |
| Three-quarter front | 25 | 4 | Goat 2 (head in the tuft); dog 1 (the hose under its paws as a puddle); cat 1 ("a small orange cushion/heap at first glance", asleep) |
| Three-quarter back | 4 | 3 | Goat 3 (loose in a park, in a garden, thin and angular) |

The goat has 10 of the 13 oddities and is drawn in 7 of the 73 cut-outs. None concerns how a three-quarter view reads, such as legs hard to count or a body seen end-on. By the gate and by these tags, no angle needs dropping.

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.35 | v0.36 | v0.37 | v0.38 | v0.39 |
|---|---|---|---|---|---|
| Pass | 63 | 64 | 63 | 64 | 64 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 0 | 1 | 0 | 0 |

Every template was screened in at least three pictures, and all 64 pass. By count: 41 in three, 10 in four, 6 in five, 4 in six, 1 in seven, 1 in eleven and 1 in twenty, with 460 scored items behind the verdicts.

The three lowest each rest on half marks:
- `dog_wants_walk` (0.917, 6 items, 3 pictures), one half mark;
- `sweep_fork` (0.944, 9 items, 3 pictures), one half mark;
- `ice_cream` (0.95, 20 items in 20 pictures), two half marks.

## What reads least well (the v0.40 list)

| # | Template | v0.39 | What the readers saw | Fix for v0.40 |
|---|---|---|---|---|
| R1 | `windy_hat` | 1.00; 0.889 read strictly (9 items, 3 pictures) | "or as her throwing her hands up in alarm rather than reaching" (71), the same second reading as v0.38's 30, 34 and 47 | The one template the strict count takes under the gate. Bench a reach: one hand open toward the hat, the other arm lower, against both arms up |
| R2 | `dog_wants_walk` | 0.917 (6 items, 3 pictures) | The dog with the lead at the door wants "to go for a walk or wants to go inside" (26) | The house door behind it offers "inside". Look at the dog turned to its owner, or by the garden gate; watch first |
| R3 | `sweep_fork` | 0.944 (9 items, 3 pictures) | "scraping or digging at a small pile of dirt" (47), the giant fork's sweep | Watch |
| R4 | `ice_cream` | 0.95 (20 items, 20 pictures) | The eater small at the back, as the goat probes' company: "something small and pink" (04, 77) | Keep an ice-cream eater out of the far back, or draw the cone larger at small scale |

## Unintended oddities

Named kinds, from the scorers' lists (`v039/scores_summary_a.md` to `_d.md`) and the readers' unsure sections, most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.40 |
|---|---|---|---|---|
| O1 | C | The summer heaps' green leaves, odd for fallen ones, in five pictures from four readers | 36, 43, 45, 49, 70 | Fallen leaves in summer are dry: the heap brown and yellow with twigs and little green, or cut grass. Bench it beside the rake |
| O2 | C | The grazing goat: its head lost in the tuft (01, 04, 08), its body "thin and angular" (83); and our own look at the pose, the rump high and the back arched at 45 and 135 | 01, 04, 08, 83 | Draw the muzzle beside the tuft, not over it, and lower the rump in `graze`. Bench at all three angles |
| O3 | C | The grandfather inspecting the hose: "The man's arms are drawn as one long flat white shape stretched out to the nozzle" (32), the white sleeve "stretched straight across his body" (05) | 05, 32 | The `hose_inspect` pose's two white sleeves merge: part the arms, or bend one |
| O4 | C | The pinched hose under the dog's paws read as a puddle: "it could also be read as a puddle or a bulge in the hose" (45), and alike in 51 | 45, 51 | Credited in full both times. Watch |
| O5 | C | A walker's feet: pointing two ways (93), as in design test 2, or the stepping leg hard to tell (46) | 46, 93 | Look at the walking feet at 90 for the boy and the grandfather |
| O6 | C | Older ones: goats out of place (32, 75, 77, 83); figures over the prop beside them (03, 20, 31, 33, 90, 96); wind moving only the hat (57, 71); the standing bicycle (59); stalls with no seller (68, 90) | Throughout | Notes for the pilot, as before |

## Placement

**The set.**
- **Tiers 1 to 3.** All twelve cells placed in the showcase pass under revision 37 and the 0.39.0 cast. Each came from its showcase seed, some after several layouts.
- **Tier 4, garden and park.** Both placed again on v0.38's seeds, the garden on its fourth layout and the park on its 21st, with the same events.
- **Tier 4, street.** v0.29 to v0.38's forced set placed on the v0.32 seed again, on its fifth layout (v0.38's on its fourth).
- **Tier 4, playground.** v0.38's seed and the next 39 of the search placed nothing. The 41st, 439653, placed on its 38th layout, with a ball in the tree and a perched bird where v0.38 had a kite in the tree and a bird flying.
- **The isomorphs.** Five, two at tier 2, two at tier 3 and one at tier 4. An animal whose template its partner shares is drawn at the partner's angle.

**The probes.**
- **The first pass** (`probes.py 3`, five for the three templates of hang-laundry-gate-v038.md) left `windy_hat` and `dog_begs` short.
- **The pass stratified by angle** (`tpdb_work/probe_angle39.py`) added 13 probes and filled `dog_begs`.
- **The dog walked at 45 never placed.** There were 12 tries in four settings and 1893 lead curves. In every one, the lead from the walker's hand crossed the dog's back on its way to the collar, which revision 12 forbids. The angle is dropped, as the gate drops one: the yaw is still drawn, and a 45 is drawn at 90 (`templates.UNPLACED`), so the records that drew 90 rebuild as they were.
- **Two garden probes changed.** They had drawn the 45 in failed tries, so they placed on earlier seeds, with the same events.
- **windy_hat** had its third picture in the park.

All 96 records rebuild identical to the pixel, and the library passes the validator in full, 391 of 391.
