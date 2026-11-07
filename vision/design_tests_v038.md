# v0.38 design tests

Revision 36 was read blind in whole test scenes among other events: six pictures, six fresh readers, one picture each (`design_tests_v038/test_N.png`, `desc_test_N.md`; the prompts are `tpdb_work/dtp38p/test_N.txt`, the reader template cut to one picture), then a second round of four (`design_tests_v038/round2/`, `tpdb_work/dtp38p2/`). Tests 1 and 2 are the seeds of v0.37's pictures 12 and 74, the probes where `hang_laundry` lost its half mark and its third picture, rebuilt under revision 36 from their own records (`tpdb_work/rb38.py`), as `vision/flaws_v037.md` asked: each came back with only the basket and the drops new. v0.37's picture 57, the storm pointer with the cat on the fence, does not place on its seed under revision 36: its twelfth try, the one that placed in v0.37, drew the cat on the fence with the storm pointer, and the rule draws that plan again. Tests 5 and 6 stand for it. `tools/cycle/design_tests.py` has the jobs for tests 3 to 6.

## Round 1

| Test | Picture | What it tests | What the reader said |
|---|---|---|---|
| 1 | Tier-3 garden, v0.37's picture 12 rebuilt | The washing hung out, the basket of washing under the dripping shirt (revision 36) | "a boy or young man in a red shirt and blue jeans reaches up to peg a white T-shirt onto the line"; but "The white T-shirt is dripping water, and the drops are falling toward a wooden laundry basket on the grass below, which holds pink, white and blue clothes, so the dry laundry may be about to get wet" |
| 2 | Tier-3 garden, v0.37's picture 74 rebuilt | The same, beside a game of catch and the grandfather under the bucket | "reaching up to a clothesline and pegging out a white T-shirt that is dripping water", the basket "holding pink, white and blue clothes waiting to be hung"; "Only the white T-shirt drips. The jeans are dry, which is a little odd if they were washed together, but not impossible" |
| 3 | Tier-3 garden | The washing beside a planter and a broom sweeper | "reaching up to peg a white T-shirt onto a washing line", "These are clothes waiting to be hung"; "the dripping shirt and full basket suggest he is hanging washing up, but the pose alone could also be read as unpegging it" |
| 4 | Tier-3 garden | The washing among a digger and a dog at play | "The white T-shirt is dripping water, so it looks freshly washed, and a basket of more laundry (blue, white and pink items) sits on the grass at his feet"; "The jeans and the clothes in the basket do not show drips, so it is unclear whether everything is wet or just that shirt" |
| 5 | Tier-3 garden | The storm pointer with a cat stalking a bird, the cat on the ground (revision 36), and a fence painter | "She points up toward the dark clouds, as if warning that rain is coming and will spoil the wet paint"; the cat "crouched low and creeping toward a small red bird"; "she could be pointing at or calling to the man, or at something on the fence" |
| 6 | Tier-3 garden | The storm pointer among the templates of v0.37's picture 57, no cat on the fence | "looking up and pointing at the dark clouds, as if warning that rain is coming"; "he might be pointing at something else in the sky, such as a bird or plane, but I cannot see anything else up there. Clouds seem the most likely reading" |

All four readers of the washing had it hung out, three of them with the pose alone as a second reading that the drops or the basket settle. But two readings were new and the drawing's. The basket stood under the dripping shirt, and its clothes, with no drop on them, read dry: "the dry laundry may be about to get wet", an event of the picture's own making (test 1). And with the shirt alone dripping, "Only the white T-shirt drips" (tests 2 and 4).

The first fix tried kept the basket from under the shirt. There is room for it only behind the hanger's heels, a step further along the line, and there it stands where the planter kneels by the flower bed: the washing and a planter placed 3 of 12 together, where they had placed 12 of 12, and picture 12's seed no longer placed (`tpdb_work/bcost38.py`). So the basket stays where the bench read it, and the rest of the washing is wet too: the jeans beside the shirt drip, and a drop forms at the cuff of the sleeve over the basket's rim. Placed so, the washing and a planter place 12 of 12 again, and the two tests were rebuilt and read again in round 2 with tests 1 and 2.

The storm pointers read at the clouds. Test 5's "something on the fence" is the fence being painted, which her arm points across; test 6's reader sees nothing else in the sky. Test 6's two fence painters come from forcing `paint_fence` with `paint_tracks`, which each bring one.

## Round 2

| Test | Picture | What the reader said |
|---|---|---|
| 1 | Test 1 rebuilt, all the washing dripping | "reaches up to peg a white T-shirt onto it. A pair of blue jeans already hangs on the line, and both pieces of clothing are dripping water"; the basket "holds the washing that is still to be hung"; "The boy could be hanging the T-shirt up or taking it down. Because it drips, hanging it up seems more likely" |
| 2 | Test 2 rebuilt | "reaching up to peg a white T-shirt onto a washing line ... both items are dripping water, and a basket of more washing sits on the grass under the line"; "These look like the rest of the washing waiting to be hung"; "They read as wet laundry, not as anything spilling" |
| 3 | Test 3 rebuilt | "Both garments are dripping water, so the washing seems freshly washed"; the basket "holds the washing still to be hung"; "Either way he looks like he is hanging the shirt" |
| 4 | Test 4 rebuilt | "water is dripping from both, so they look freshly washed", the basket "waiting to be hung up"; "The dripping water and the full basket make hanging it up the more likely reading" |

All four have the washing hung out and the basket as what is still to be hung, and none has dry washing about to get wet or one garment dry. Two still offer taking it down from the pose alone, and settle it by the drops and the basket, as the bench's readers did; the other two raise no doubt. Two readers say the drops could also be "small floating blue marks" (test 3) or "small floating marks" (test 4), and both read them as drips. No reading called for a further rule, and the set was built with these drawings.

Remarks on other things: the broom's autumn leaves under a green tree, as in v0.37's test 5 ("Season mismatch, perhaps unintentional", test 3), and the hanger's long legs and twisted stance, as on the bench.
