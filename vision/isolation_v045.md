# v0.45 isolation bench

The brief for v0.45 was the drawings: improve the visuals, find the flaws and fix them. The work list came from two places: `flaws_v044.md` (R1 the ice cream at the gate's line, R2 the camera "or binoculars", R3 the lost balloon, R4 the thief bird, O2 "black ice skates") and a fresh look at v0.44's pictures and cut-outs by four reviewers, each with a share of the set or the library (their notes are kept in `tpdb_work/review45/`). What two or more of the reviewers named, or a reviewer and the flaws list, was drawn.

As in v0.44 the bench read whole pictures: a tier-3 picture with the changed templates forced among the planner's own, built once in v0.44's drawing and once in v0.45's on the same seed. The readers got the screen's own whole-picture prompt (`tpdb_work/iso_round45.py`) and ran on Opus, as every reader and scorer of this release does. There were two rounds:
- round 1: fifteen readers of 30 pictures, two to a reader. The ten new pictures were read twice, by different readers (`isolation_v045/round1a`, `round1b`); the ten old ones once (`round1o`);
- round 2: two readers of the three pictures that changed after round 1 (`round2a`, `round2b`).

`map.json` in each says which picture is which case. The first three letters of a case name the scene (`st8` a street, `pk8` and `kt8_1` the park, `pg8` and `kt8_2` the playground, `gd8` the garden); the fourth the drawing: O v0.44's cast (`BENCH_CAST=assets/cast/out044`) and revision 42's rules, N the cast with every v0.45 switch on (`tpdb_work/bench45/out_N`) and every revision-43 rule on. `gd8_1` builds in neither drawing (the planner cannot seat the blocked hose beside the planting on that seed) and was not read.

Nine changes are in the cast, behind switches read when it is built:
- `TPDB_ICE45` (R1; three reviewers): the cone darker, the wood's brown, and longer above the fist, cone and scoop half as big again in a child's hand, a third in a teen's and a fifth in an adult's, the scoop below and in front of the mouth; the empty cone 1.3 times the size in a child's hand and 1.15 in a teen's (in v0.44 a child's ice cream was "a lollipop": the cone, the colour of skin, hid in the fist and the scoop sat on the cheek).
- `TPDB_CAM45` (R2; two reviewers): the camera a fifth larger, a prism hump in the middle of its top, a longer lens with a wide silver ring, and a strap in a bright colour hanging in a loop under it (v0.44's at the eyes was once more "a camera (or binoculars)").
- `TPDB_SOLE45` (O2; two reviewers): the sole plate no longer than the shoe's flat underside and no wider than the shoe, dark under every shoe (it was longer than the shoe and pointed, grey under a dark shoe, and under a walker's tipped foot stood clear of the toe and the heel like a blade: "black ice skates").
- `TPDB_HOSE45` (two reviewers): the hose inspector's head turned toward the viewer and a little down. v0.44's INSPECT44 turned it the other way, a sign error: the face was hidden.
- `TPDB_TROWEL45` (three reviewers): the trowel a broad pointed blade seen from its side on a bright handle (edge on it was a grey line).
- `TPDB_PAINT45` (two reviewers): the roller a blue sleeve with a cream cap at each end on a cranked wire frame ("a paddle").
- `TPDB_BOX45` (two reviewers): the carried box khaki with a brown tape (it was the garden fence's colour).
- `TPDB_DUCK45` (three reviewers): a swimming duck's legs are not drawn.
- `TPDB_KITE45` (one reviewer, and my own look): a reel on a handle above the kite flier's fist, two bright flanges with the cream of the wound string between them (the spool, a wood-coloured cylinder seen end on, was "a small tan ball with a brown dot", the fist's size and on two of the three children its colour).

Seven changes are in placement revision 43:
- `templates.BAL45` (R3; two reviewers): the lost balloon's string end 62 to 80 px above the reaching hand at full size (closer, the child was "holding the string by its very tip, or has just let go"). After round 1 the end also keeps clear of the top line of the setting's fence.
- `templates.PAINT45`: the wet paint on the board under the roller begins below the roller, so the blue roller lies on bare wood at the paint's edge (on a blue board it was lost). After round 1 the painter also stands a step further forward until the roller lies well below the boards' tops.
- `templates.PLANT45`: the planter kneels at the bed's end and digs in the bed: a hole under the trowel's point, a few clods beyond it, the pot in front of the bed. My first drawing, a dug patch on the lawn, lay under the planter's shoe; it was redrawn twice before any reader saw it.
- `templates.PICNIC45` (two reviewers): a loaf and a bottle stand out of the basket, and where the blanket has room a plate with a slice of watermelon lies on it (v0.44's picnic showed no food).
- `templates.TETHER45` (two reviewers): the goat's stake is never drawn in front of a standing structure (it stood on a bench's rail).
- `library.SWIM45` (three reviewers): a swimming animal is cut along a waterline with a ripple round it and has no ground shadow ("the duck stands on the water").
- `settings.SLIDE45` (from round 1): the slide's ladder is the frame's own end, in the frame's red: two rails to the ground with slate rungs between them, the near rail running on up into the hand rail over the deck. v0.44's slate ladder leaned across a red upright.

Looked at and left before the readers: a grey remix (`compose.to_gray` stays standard luma: every picture's grey twin would move for a cosmetic gain), the reading dog's paper (fine in four pictures of my own look), the leash, the goat's profile, the throw and the tucked jump.

## Round 1

| Thing | v0.45's drawing (N, two readers a picture) | v0.44's (O, one reader) |
|---|---|---|
| A child's ice cream | "holding a pink ice-cream cone" in both readings (pk8N_3) | "very small and could be read as a lollipop or a pink sweet rather than an ice-cream cone" (pk8O_3) |
| The empty cone | "holds an empty ice-cream cone" in both (pg8N_1); once it "looks slightly separated from the child's hand, as if floating at the hand" | "empty cone" (pg8O_1) |
| The camera | A camera in all eight readings, the strap named in every one ("holding a camera with a red strap to her eye", pk8N_1) | A camera in all four |
| Shoes | No skates or boots named | None named |
| The hose inspector | "holds the nozzle of a green garden hose up near his face and is looking into it" (gd8N_3); "The nozzle is pointed up near his face ... as if he might spray himself" | "holding the hose nozzle up and peering at it" (gd8O_3) |
| Planting | "digging with a trowel" in all four readings (gd8N_2, pk8N_2), the pot "apparently waiting to be planted" | No trowel in either: "tending the colourful flowers" (gd8O_2); "could be putting the tulip pot into the bed or taking it out" (pk8O_2) |
| Painting the fence | "painting the wooden fence blue with a paint roller on a long handle" in both (gd8N_2). But "the roller hovers slightly above the fence top line on its left edge" and "is held up against the fence top rather than on the part she seems to be painting" | "painting it blue with a paint roller on a stick" (gd8O_2) |
| The carried box | "a cardboard box" in all six, once "taped" | In all three |
| The swimming duck | "swimming" in all six, "leaving a wake behind it" (pk8N_2) | "swimming" in all three |
| The picnic | The baguette and the bottle named in all six ("a wicker basket holding a baguette and a green bottle", pk8N_2); the plate with the watermelon slice in both readings of the picture that has it (pk8N_3) | "a wicker basket beside it" in all three, no food named |
| The kite's reel | Named in all four: "holding a kite spool up in one hand" (kt8N_1), "her red-and-white spool" (kt8N_2) | "holds the string in one raised hand; I cannot see whether he has a spool" (kt8O_1); "holds a string" (kt8O_2) |
| The lost balloon | "its string dangling free" (pk8N_1), "dangles well above his hand, so it seems he has just let go of it and can't reach it" (pk8N_3). On the playground the end lay at the railing's top line: "it could look like it is tied to the fence, but no knot is visible", "caught on/attached to the fence rather than floating free" (pg8N_1) | "or that she is still holding it by a very fine string; the string appears to end in a loop just above her fingers" (pg8O_1); "the string end is not clearly in her hand" (pk8O_1) |
| The slide's ladder (not a v0.45 change) | "The slide's ladder and frame look slightly mismatched (ladder drawn in front of/ beside the red frame)" (pg8N_1); "seems to stand slightly separate from/behind the red frame, which looks a bit odd" (kt8N_2) | "drawn slightly slanted and separate from the frame; minor drawing oddity" (kt8O_2) |

The goat's stake stood clear of every bench on these seeds in both drawings, so the bench did not see `TETHER45` at work. It was seen afterwards on the seed of the v0.44 probe that had shown the flaw (`T3_park_s23030`, built again with the rule off and on by `tpdb_work/tether45.py`): off, the stake's box reaches down to y 720 and stands on the top rail of the bench in front of the goat; on, it ends at y 708, clear of the bench. That picture is design test 6 (`design_tests_v045.md`).

So after round 1: the ice cream, the planting with its trowel, the picnic's food, the kite's reel and the lost balloon read better; the camera, the shoes, the hose inspector, the box and the duck read as well as they did (the camera's and the shoes' misreadings were the screen's, one in ten and one in eighty, and a bench of four pictures does not show them either way). Three things were left to fix: the roller at the fence's top line, the balloon's string end on the railing's top line, and the slide's ladder, which three of the six readings of the playground called separate from its frame in the old drawing and the new alike.

## Round 2

Three changes went in after round 1 (`tpdb_work/patch45k.py`): the painter stands a step further forward until the roller lies below y 480, the tin with them; the balloon's string end is never laid within 26 px above to 30 px below the top of the setting's fence; and `settings.SLIDE45`. The park's pictures came out pixel for pixel as round 1's, so only the three changed pictures were read again, by two readers:
- **The slide:** "a red climbing frame with a yellow/orange slide", "Slide and climbing frame: left, red frame with ladder and yellow/orange chute", "Slide with red ladder (left): unused". No remark on the ladder in four readings.
- **The lost balloon:** "its string ends just out of her reach" (pg8N_1); "The yellow balloon's string ends in mid-air well above the girl's hand; she seems to have just let go. Reads as escaping, not as an unintended floating object." The fence is not named.
- **The painter:** "painting the fence blue with a roller on a handle; a few boards next to her are already blue" (gd8N_2). "The woman stands a little in front of the fence with the roller near the top of the boards ... Not obviously wrong"; "reads fine as work in progress". Nothing hovers. One reader has the tin "a step or two behind the woman rather than at her feet" (v0.44's was "several steps behind/beside").

## Taken

- The cast (builder 0.45.0): `TPDB_ICE45`, `TPDB_CAM45`, `TPDB_SOLE45`, `TPDB_HOSE45`, `TPDB_TROWEL45`, `TPDB_PAINT45`, `TPDB_BOX45`, `TPDB_DUCK45` and `TPDB_KITE45`, all A. Every person and the duck are rebuilt; the other animals are carried from v0.44.
- Revision 43: `templates.BAL45`, `PAINT45`, `PLANT45`, `PICNIC45` and `TETHER45`, `library.SWIM45` and `settings.SLIDE45`, all B.
- After the design tests (`design_tests_v045.md`), three more in revision 43: `templates.RAIL45` (on a railing the lost balloon's string end lies nowhere on it), `templates.CURL45` (its string hangs in a slow wave, with no curl at its end) and `settings.FOOT45` (the bird table's post stands in a tuft of grass), all B.
- After the set's first isomorphs, one more in revision 43, from my own look and no reader's: `templates.WOOD45`, B. In the garden the lost balloon's string end lay on the wooden fence in every picture (twelve of twelve test seeds, `tpdb_work/wood45.py`): the fence is 190 px tall and a child's raised hand reaches half way up it. A thin dark string over boards with dark gaps and two rails is hard to follow: in `T4_garden_s27111_iso` it ran down a board gap and ended at the upper rail, as if it ran into the fence. The end is now lifted clear above the pickets' tops, 34 to 48 px at full size, so the whole string hangs before the hedge and the sky, and a child whose hand would be more than 200 px below it at full size is not stood there. The gap above the hand is larger than elsewhere, about the child's own height at most. The same twelve seeds all place with the rule on. Calibration was run again with it (the garden's child stands further back).
- For the watch list: the paint tin's place, the empty cone "slightly separated from the child's hand" (one reader), the catcher who "overlaps the fence rails" (two readers, kt8N_2), a raised hand "a bit small/clawlike" (one), held balloon strings that "curve oddly to the left of her body" (one), and far crumbs that "could look like floating stones/bubbles" (one).
