# v0.40 design tests

Revision 38 and the cast of builder 0.40.0 were read blind in whole test scenes among other events: four pictures, four fresh readers, one picture each. The files are `design_tests_v040/test_N.png` and `desc_test_N.md`; the prompts are `tpdb_work/dtp40p/test_N.txt`, the reader template cut to one picture. The jobs are in `tools/cycle/design_tests.py`, and two of them ask for the goat turned from profile (rule `angled`).

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-3 park | A hat blown off, an ice cream, the goat at an angle | The reach reads one way: "an elderly woman ... reaches up with her right arm. Her mouth is open in surprise as an orange baseball cap flies away above her", "right arm stretched up toward the flying cap, left arm at her side", and nothing of hands thrown up. The ice cream reads at the middle distance: "holds a pink ice-cream cone to her mouth with one hand". The goat is "eating a small tuft of dark green grass", but "there is no fence, lead or owner, so it could be a loose or escaped goat" (O3) |
| 2 | Tier-3 garden | The hose inspected, a raker's dry leaves, the washing hung out | "She holds the hose nozzle in both hands, raised toward her face, and seems to be looking into it", the dog on the hose read: "I read it as the dog standing on the hose and pinching it". The raker is "raking a small pile of brown leaves on the path", with no remark on the leaves under the green tree |
| 3 | Tier-3 street | A sweeper's dry leaves under the one tree, an ice cream, a reader | The leaves read as leaves, and the old remark comes back once: "The brown leaves are the main oddity. They look like dry autumn leaves, but the tree is fully green and it is a bright sunny day, so it is unclear where they came from" |
| 4 | Tier-3 park | The goat at an angle, an ice cream, a kicker | "a white goat with curved grey horns has its head down and is eating a small tuft of grass"; and of its body: "The goat's body is short and hunched, with a small head and long legs. It is still recognisable as a goat" |

**What the tests show.**
- **The reach and the hose read as benched.** The reach is one arm up toward the cap with the other at her side; the hose is held in two hands at the face.
- **The tuft is no longer named over the goat's head.** Its hunch stays, as on the bench.
- **The heap's season remark comes back in one picture of two.** The dry leaves are read as leaves, not as the bench's nuts, and no reader finds them green. The street sweeper's are "dry autumn leaves" under a green tree, as v0.38's autumn heap was. The heaps stay as benched, and the remark is counted in the screen. The heap has now been drawn three ways (autumn, summer green, dry), and each drew a remark about the season or about green leaves.
