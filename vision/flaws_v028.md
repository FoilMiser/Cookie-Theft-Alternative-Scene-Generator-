# v0.28 blind screen: what it found (the work list for v0.29)

The v0.28 screen used the prompts of the screens before it (`screen_prompts.md`), with nine readers and three scorers, and read the set's 21 pictures and 49 probes. Keys, descriptions and scores are in `v028/`.

## Headline (the 21 pictures of the set)

| | v0.25 (21) | v0.26 (21) | v0.27 (21) | v0.28 (21) |
|---|---|---|---|---|
| Things | 0.991 | 0.995 | 1.00 | 1.00 |
| Actions | 1.00 | 0.992 | 0.996 | 0.996 |
| Inferences | 0.985 | 0.953 | 0.950 | 0.879 |
| Contradictions | 1.00 | 0.981 | 1.00 | 1.00 |
| All items | 0.995 | 0.988 | 0.993 | 0.984 |
| Misread items | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 |
| Readers' remarks per picture (all screened pictures) | 5.93 | 5.27 | 5.81 | 5.14 |
| Oddities per picture, as logged by the scorers | 2.6 (at most 3) | 2.6 (at most 3) | 2.2 (at most 3) | 2.0 (at most 3) |

Across all 70 pictures 766 of 775 scored items had full marks. Eight had half marks, one was missed, and none was misread. Eight of those nine are in the set, seven of them inferences: three on the trip, three on the duck and the bread, and the one missed, the dog that wants a walk. No cloud or tree was missed, where v0.27 lost eight such items to one reader's habit.

## Reading the two bottom rows

Remarks fell by 12%, 5.81 to 5.14 (360 on 70 pictures against 389 on 67), on the same model and prompts as v0.27. The pictures were a little less busy, 3.06 templates a picture against 3.18, which is not enough to account for it. It is not spread evenly: on the same split of the pictures the readers range from 4.25 to 6.38 a picture, against 5.29 to 6.29, with five of the nine under 5. So readers differ a good deal, and this is one screen. `remark_topics.py` sorts the remarks of two screens by keyword, roughly:

| Pictures that remark on | v0.27 | v0.28 | |
|---|---|---|---|
| Shadows | 20 | 11 | This release's main change. Of the eleven, none says a shadow is too wide or off the feet, the closest being "the small ball shadow and his shadow are a bit apart but make sense" |
| Marks on a face | 9 | 5 | No brows over closed eyes, a smaller blush |
| A beard as a strap or mask | 2 | 0 | The goatee: "a small beard", "short dark hair and moustache" |
| Stiff or awkward poses | 18 | 12 | Not changed |
| A branch to hold it | 5 | 3 | "Stuck in a fork of a branch" (28) |
| Thin or long body or legs | 8 | 13 | Not changed |
| A face hidden or hard to read | 10 | 12 | Not changed |
| A figure over the pond | 6 | 6 | Not changed |
| The seesaw's plank | 5 | 5 | The heavy rider's leg, not changed |

A keyword count is a rough sort, which says where to read. It is not a measure.

## The v0.27 list

| v0.27 reading | v0.28 result |
|---|---|
| R1 `dog_begs` 0.889: "could be hers, begging from her bag", "or be watching the kite" | **1.00** (9 items, 3 pictures), the one failure of v0.27. The dog at the end of the bench the eater sits nearest, its gaze on the food, nobody else near. "Begging for the ice cream"; "hoping for a lick or a dropped bit of ice cream"; "apparently begging for it". Whose food is no longer asked |
| R2 `dog_wants_walk` 0.917: "or could just be an odd pose" | **0.833** (6 items, 3 pictures), and it fails. Not changed. One reader in the T2 garden gives only "sits with a red lead in its mouth", a picture v0.27 read in full |
| R3 `sweep_fork` 0.944 | **1.00** (9 items, 3 pictures). Not changed |
| R4 `about_to_trip` 0.958: "headed roughly past it" | **0.917** (18 items, 6 pictures), meaning items 0.75. Not changed, as a look at the crops showed the obstacle already on the line of the stride. Three half marks of six: "might pass beside it", "he is moving past it, not squarely into it", "I could read it either way" |
| O1 Shadows: "a very wide oval, much wider than the puppy" | Gone. From the figure's own footprint, and flatter for drawn objects. See above |
| O2 Eyes shut while walking; blush or ice cream | Gone. No walker has closed eyes in 70 pictures, and no remark on a blush as ice cream |
| O3 The fallen ice cream: "a pink hat or a pink frisbee", a flying saucer | Gone. A flat splat in all three pictures: "a pink splat with coloured sprinkles", "a pink splat of dropped ice cream", "his pink ice cream is splattered on the ground". The item reads in full |
| O4 The seesaw: "almost past it", the plank and the leg | The rider near the end is gone, with riders further in. No remark on one shadow under the whole seesaw but "a soft shadow on the grass" (63). The heavy rider's leg stays: "one leg crosses in front of the plank, hips sit above it" (8) |
| O5 The hose in `hose_water` | Not changed, and up: "like a rigid pipe" (25), "with no slack" (46), "the upright section could read as a post" (9) |
| O6 A branch or clump on the crown | Much less. The ball is now a beach ball, called one in all four of its pictures, with a limb from a fork at the top of the trunk. New: "as if the leaves had been cut away to display the ball" (2), once. The goldfish, not changed: "looks pasted onto the leaves" (4) |
| O7 The beard: "a thin dark strap along the jaw" | Gone, with the goatee |
| O8 Marks on a small face | Down, as above: "small dark mark or shading around her mouth and cheek" (9) is the kind that is left |
| O9 The narrow figure | Not changed, and up by keyword |
| O10 A crowd in a tier-4 picture | No remark on one this time |
| O11 Older ones | Left, as since v0.11: figures over the pond, goats as sheep or dogs, a wind that reaches only the cap ("Wind seems to touch only the cap and leaves"), autumn leaves under green trees |
| Two bins side by side (five pictures in v0.27) | Gone, with one bin to a picture |

## The legibility gate (mean at least 0.9 over at least two pictures, no misread)

| | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 |
|---|---|---|---|---|---|
| Pass | 63 | 61 | 59 | 63 | 61 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 |
| Fail | 1 | 3 | 5 | 1 | 3 |

Every template was screened in at least three pictures (47 in three, 12 in four, 2 in five, 3 in six; 393 scored items behind the verdicts). The one failure of v0.27 passes in full. Of the three that now fail, one is on a drawing this release touched, and two are not, and the v0.9 retest put reader variance at about five templates between screens. So 63 to 61 is not a measure of the drawings getting worse, and neither was 59 to 63 a measure of their getting better.

## What reads poorly (the v0.29 list)

| # | Template | v0.28 | What the readers saw | Fix for v0.29 |
|---|---|---|---|---|
| R1 | `dog_sleeping` | 0.667 (3 items, 3 pictures); fails | Two half marks: "could be a puppy or a kitten", and "sniffing the grass, lying down, or curled up asleep". 1.00 in v0.27 ("apparently asleep"), and the drawing has not changed, but its shadow has: a wide oval under it may have said lying down. On the bench the old shadow's reader said asleep, and the new one's "either sniffing the grass or lying curled up asleep". One cut-out each | The bench: a wider shadow for a body lying on the ground, against a sleeper seen more from the side, head on its paws |
| R2 | `ducks_bread` | 0.833 (9 items, 3 pictures); fails | All three half marks on the same inference: "swimming towards those crumbs", "swimming toward the man and the bread". v0.27's readers wrote much the same, "swimming towards the food", and scored in full, so this is mostly the scorers. One scorer called it "the closest call" | The duck's bill at a crumb, so that eating is drawn and not left to be said. Looks cheap |
| R3 | `dog_wants_walk` | 0.833 (6 items, 3 pictures); fails | One reader: "sits with a red lead in its mouth", no more. Two of three say it in full: "looking as if it wants to go for a walk". Second release under 1 | Watch. If it falls again, the dog's gaze on the door |
| R4 | `about_to_trip` | 0.917 (18 items, 6 pictures); passes | The weakest meaning that passes (0.75), and it has fallen for two releases. The obstacle is on the line of the stride, by eye and by rule, and readers still have the walker going past it | The bench: an obstacle wider across the line (a box lengthwise), or the walker's body turned square to it |

## Unintended oddities

Named kinds, from the scorers' lists (`v028/scores_summary_a.md` to `_c.md`), most worth doing first.

| # | Sev | Oddity | Where | Fix for v0.29 |
|---|---|---|---|---|
| O1 | B | The hose in `hose_water`: "like a rigid pipe", "with no slack", "a post" | Pictures 9, 25, 46 | Every curve so far has had a name. A hose that leaves the fist downward and only then bends |
| O2 | B | Readings that weaken a contradiction: a ladder "too far away" from a lamp post, the floating box and the soaked box alike, a bucket as "a makeshift rain hat" under storm clouds | Pictures 11, 14, 20 | Rules: no lamp post near the ladder, no soaked box with a floating one, no bucket hat under a dark sky |
| O3 | C | A key's word: the floating box is "wooden" in its key, and readers say cardboard, with tape | Pictures 14, 62, 65 | "A box" in the key. Two scorers raised it. It costs no marks |
| O4 | C | The lifted heel: a walker's rear shoe "looks turned up", and one reader had a man and his dog going opposite ways | Pictures 28, 40 | Look at it. The heel was chosen on the bench in v0.27 |
| O5 | C | The hose's bulge as "a separate slug-shaped object" or "a dark flattened blob" | Pictures 25, 49 | Thinner, and the same colour as the hose all along |
| O6 | C | The heavy rider's leg over the plank | Pictures 8, 52 | The larger job it has been since v0.27 |
| O7 | C | The goldfish "pasted onto the leaves", with no branch | Picture 4 | The limb the ball has now, if it does not spoil the contradiction |
| O8 | C | The narrow figure: "very thin arms and small body could read as falling" | Pictures 21, 35, 38 | Leave, or a real change of build |
| O9 | C | Older ones: figures over the pond, goats as sheep or dogs, wind that reaches only the cap, leaves with no tree near, autumn leaves under green trees, the roller's head, a window that stays bright under a dark sky | Throughout | Notes for the pilot, as since v0.11 |

## Placement: why the tier-4 playground would not place

v0.27 could not place a tier-4 playground from 219 free seeds and forced an old picture's set. v0.28 tested the question directly: the same 12 seeds, 40 cast sets to a seed, one change at a time.

| Change, on the same 12 seeds | Seeds that placed |
|---|---|
| None | 0 |
| The trip never drawn | 0 |
| The templates the failures name placed first | 0 |
| A search that leans away from whatever it last failed on, by 1 or by 3 | 0, 0 |
| At most five or six people in a plan | 0, 0 |
| None of the ground-hungry templates (the trip, the stalking cat, the balloon, sitting on air, catch, running, the pram, the walked dog, the kick) | 0 |
| The bird stealing a sandwich and the square wheel required | 0 |
| The railing counted up to 30% hidden | 0 |
| The railing, and the required pair | 0 |
| The railing, and no swing set as scenery | 0 |
| **All three together** | **2** |

The change that found this was to take away the difficulty band and try 226 random sets of the planner's shape for 14 layouts each. Five placed. All five held the bird stealing a sandwich (a reader on a bench, no ground taken) and the square-wheeled bicycle (no person): 5 of 72 sets with both, none of 154 without. None of the five had a swing set. And all five were one or two things short of the tier's 18, because the railing, a long thing a fifth hidden, had just failed the rule that a scored thing be at least 80% in view (four of the five sets: 20.5% to 23%). Being short, plans went back for the swing and the sandbox, which took the ground that would have let them place. That is the loop, and why each piece alone did nothing.

So revision 26 has three rules for a tier-4 playground: the pair required, no swing set as scenery, and the railing counted up to 30% hidden. The real search then took two lists. Last release's seed failed, and one of the two seeds the test had placed came out again, in 49 seconds, with a set of its own: `bird_steals`, `ball_in_tree`, `lost_balloon`, `square_wheel`, `bucket_hat`, `run`, `dog_playing`, `ice_cream`, `bird_perched`. It is the first tier-4 playground not forced since v0.26.

Two things this does not show. Requiring two templates costs some of what forcing cost: every tier-4 playground now has those two, and no tier-4 playground can have the begging dog, which also needs the bench. And 2 of 12 seeds is a small sample, though enough to find a picture.

The tier-4 street had got hard the same way (57 failed seeds across three searches). Both its last pictures held the bird stealing a sandwich, so requiring it was tried, and placed after 13 failed seeds across two searches. One picture does not show that the rule is what did it. The garden came on its v0.27 seed, and the park took 9 failed seeds. The tier-4 isomorph took 226 failed attempts.
