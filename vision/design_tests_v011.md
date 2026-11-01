# The v0.11 changes, read blind in test scenes before going into the set

The v0.10 screen left five templates under the gate, each failing for a cause visible in the picture, and
reported eight unintended oddities (`flaws_v010.md`). v0.11 changed the placements and drawings behind
all of them (placement revision 9), then read the changes blind in test scenes before regenerating the
set, as v0.8 to v0.10 did. Each reader was a fresh model that saw only its one picture, with the screen's
reader prompt (`screen_prompts.md`). The pictures and descriptions are in `design_tests_v011/`
(`round2_map.txt` and `round3_map.txt` name the scenes behind the later rounds).

## Round 1: the first fixes

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (garden) | Kite tucked into the canopy with a leaf clump over its top corner and a slack string; waver clear of the house; swing motion arcs; play bow | The swing: "motion lines show she is moving". The kite "may be stuck in the tree, or about to get caught in it", or "just flying in front of the tree"; its string "passes very close to (possibly through) the right clothesline post". The dog "in a play-bow pose" (or "stretching") |
| `test_2.png` (park) | Kite in the tree; the hat flying with the gust; picnic basket beside the sitter; play bow; waver | The gust "blowing from left to right and has carried away a red baseball cap and a few green and brown leaves". The kite "seems to be stuck in the tree" (also "it may be flying just in front of the tree"). The basket "on the blanket next to the child". The waver "raises one hand and waves" |
| `test_3.png` (street) | Pointing at the storm, always worried, clear of trees; the reading dog, brown with its tail curled forward | "Pointing up and to the right, maybe at the clouds ... maybe warning about rain", but "her pointing hand also ends right at the front corner of the produce stall, so it could instead read as her reaching toward or pointing at the produce" |
| `test_4.png` (garden) | Pointing at the storm beside a ball in the tree; dustpan touching the heap | The pointer "probably at the storm clouds", though "he could be pointing at something else in the sky or at the ball". The ball's reacher stood off to the side: the ball "up and to the left of her, not directly above" |
| `test_5.png` (park) | Pointing at the storm in a park with a flying kite; reading dog | "Points up at the sky, maybe at the dark clouds as if warning that rain is coming, or maybe at the kite". The dog's white paws "look like gloved hands or mittens" |
| `test_6.png` (playground) | Seesaw with the bigger child down; play bow facing a person | "The left end is slightly lower and that girl's feet reach the ground ... the seesaw looks like it is moving"; the dog "in a 'play bow' ... faces right, towards the adult and the seesaw" |

Five changes followed:

- **Pointing at the storm.** Never in the same picture as a flying kite (two things up in the sky to point
  at), a wider clear cone around the pointing line, the fingertip and the first stretch of the line clear
  of standing structures (stall, lamp post, tree, clothesline, swing, slide, bird feeder, house, bench),
  and the whole line clear of kite strings.
- **The kite string.** Kept clear of standing structures as well as people, short of the canopy.
- **The kite.** Clear of the house: on the canopy's edge by the house it was half hidden behind the roof,
  its leaves drawn over the wall.
- **Reaching for the ball.** A child reaching up stands under the ball, which sits out on a side of the
  canopy; the ball, like the kite, keeps clear of the house.
- **The play bow.** With nobody near, it faces the middle of the picture, and the ground ahead must lie
  inside the picture (one bow faced the frame edge).

## Round 2: the follow-ups

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_7.png` (garden) | Kite with the string clear of the clothesline; play bow toward a person | The kite "is up among the leaves at the top of that tree and looks stuck there. Its string runs down in a slack curve". The dog "in a 'play bow' ... facing the kite child as if it wants to play". Still offered "flying in the sky just in front of the tree" as a second reading ("the slack string and the overlap make (a) more likely"), and the string "seems to cross close to the base of the left post" |
| `test_8.png` (street) | Pointing at the storm clear of the stall | "Looks up with her mouth open and points her finger at the sky or the dark clouds, as if warning that rain is coming" |
| `test_9.png` (garden) | Pointing at the storm beside a teenager pointing at the ball | The pointer "looks up with a worried face and points up and to the left at the dark clouds"; the other "apparently at the ball in the tree"; the woman watering "even though rain looks about to start". The ball "near the edge of the leaves close to the house wall" could look "floating in front of the foliage" |
| `test_10.png` (park) | Pointing at the storm, no kite; a child reaching up under the ball; reading dog | "Pointing one finger at the sky or the dark clouds, as if he is noticing or warning that rain is coming". The child "stands with both arms raised, looking up toward a large tree ... seems to be reaching for it". The dog "sits upright like a person and holds an open newspaper" (no complaint about the paws) |
| `test_11.png` (playground) | A child reaching up under the ball | "Both arms raised ... her ball is stuck up there and she is reaching or calling for it" |
| `test_12.png` (garden) | Kite | "Right in front of the leaves of the big tree beside the house, so it may be caught in the tree rather than flying freely" |

The kite was still the one change read two ways. So it was drawn further into the tree: a twig runs
across it from the canopy to its top corner, a second leaf clump covers its lower corner, and the string
sags deeper.

## Round 3: the kite again

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_13.png` (garden, the scene of `test_7` rebuilt) | Kite with a twig across it, leaves over two corners, a deeper sag | "A leafy tree has a purple diamond-shaped kite stuck in its branches"; "tangled in the leaves, with leaf clumps drawn over part of it"; the string "sagging in a curve". The second reading was still offered, but "the overlap makes 'stuck' more likely"; the string "passes close to the bottom of the left washing-line post but doesn't seem to go through anything" |
| `test_14.png` (garden, the scene of `test_12` rebuilt) | The same | "The purple diamond kite is caught in the leaves of the big tree behind the house, so the child seems to be trying to tug it free"; "it is clearly in the tree ... The string is slack and curved rather than tight" |

Both readers put the kite in the tree in their own first account, one of them without a second reading,
so the drawing went into the set as it is.
