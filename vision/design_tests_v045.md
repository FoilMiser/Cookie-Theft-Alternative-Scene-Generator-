# v0.45 design tests

The cast of builder 0.45.0 and revision 43 were read blind in whole test scenes among other events (`tools/cycle/design_tests.py`, the v0.45 jobs), each
picture by a fresh reader with the reader template, one picture to a reader, on Opus. `design_tests_v045/map.txt` names each picture's record.

| Test | Forced | Placed |
|---|---|---|
| 1 | A park: a kite flown from its reel, a picnic with its food, a duck on the pond | first seed |
| 2 | A garden: the fence painted, flowers planted, a child on the swing | first seed |
| 3 | A garden: the hose stopped and inspected, a box carried, the washing hung out | second seed |
| 4 | A playground: a balloon lost, an ice cream in a child's hand, a reader on a bench, beside the slide | 25th seed (the rule asks for the ice cream in a child's hand, and the cast has two children) |
| 5 | A street: an ice cream dropped, a photographer, a box carried | first seed |
| 6 | A park: the goat behind a bench, a pram pushed, birds fed | the v0.44 probe's own seed, `T3_park_s23030` |

Test 4 was first written with a child on the slide as well. The lost balloon and the slide each take one of the cast's two children, so the ice
cream could only ever be a grown-up's and the rule could not be met; the slide's rider became a reader on a bench, and the slide stands in the
picture unused.

Three flaws came out of the readings, and all three were fixed in revision 43 before the set was built: the lost balloon's string end under the
railing's rail (`templates.RAIL45`), the curl at the string's end (`templates.CURL45`) and the patch at the bird table's foot (`settings.FOOT45`).
Tests 3 and 4 were built again on their seeds and read again by fresh readers, test 4 twice; the other four came out pixel for pixel as they were
read. The first readings of 3 and 4 are quoted below where they name the flaw.

**The kite's reel** (test 1): "holds a kite handle up in the air", "a red-and-white kite handle". The string "goes up to an orange diamond kite";
"the kite looks quite far to the right of the boy".

**The picnic's food** (test 1): "A wicker picnic basket on the blanket holds a baguette and a green bottle", the bottle "possibly wine". The blanket
had no room for the plate on this seed.

**The swimming duck** (test 1): "a white duck swimming on it", "swimming toward the left". "Nothing looks clearly impossible."

**The fence painter** (test 2), a boy with the roller on bare wood at the paint's edge: "holding a paint roller and painting the fence blue. A few
fence boards next to him are already blue, and a paint tin stands on the grass by his feet". One remark for the watch list: "The painter's roller is
at the height of his own head, and the painted boards are to its right, slightly away from where the roller touches. It reads either as him having
already painted those boards and moving along, or as the roller being a little detached from the painted area".

**The planting** (test 2): "kneels by a round flower bed full of colourful flowers and digs with a small trowel. A pink flower in a terracotta pot
sits beside him, so he seems to be about to plant it"; "Trowel: in the gardener's hand, digging a small hole in the soil".

**The hose** (test 3), stopped under the spotted dog and inspected by the teenager, her face toward the viewer.
- The cause read in both readings: "the hose looks flattened or bulging under its paws, as if the dog is standing on it and squeezing off the water";
  "the dog seems to be squashing or kinking the hose and stopping the water". Both hedge the bulge once: "a hose joint or a puddle", "a drawing glitch
  or a lump in the hose".
- The inspecting is one reading of two in both: "she may simply be looking at a nozzle that has stopped working (she looks at the nozzle, not at the
  woman)" beside "pointing it up and to the left toward the laundry"; "she is about to spray (and soak) the drying clothes or the woman, or she may
  simply be puzzled that no water is coming out". With the washing line behind her the raised nozzle has a target; on the bench (`gd8N_3`), with none,
  it was "looking into it".
- **The bird table's foot.** First reading: "The green patch at the base of the birdhouse pole is unexplained (could be a small bush or a drawing
  artefact)". The flat dark oval became a tuft of grass blades (`settings.FOOT45`). Second reading: "red roof, with a tuft of grass at the base".

**The carried box** (tests 3 and 5): "carrying a cardboard box" in all three readings, once "closed and taped".

**The lost balloon** (test 4), on the playground, in front of its railing.
- It read as lost in all three readings: "It looks as though she has just let go of the yellow balloon and is trying to grab it back"; "It looks as
  if she has just let go of the red balloon, or it slipped away, and she is reaching for it".
- **The string's end.** First reading, the end lying under the railing's lower rail: "Its string ends in a small curl/hook just above the fence rail,
  which is a little odd-looking". The rule that kept the end off the railing's top line now keeps it off the whole railing (`templates.RAIL45`), and
  on the same seed the end lies above the top bar. Second reading: the railing is not named, but "The small curl at the bottom of the red balloon's
  string looks like a hook rather than a loose end". The string was a straight line with a curl; it now hangs in a slow wave that grows toward its
  free end, with no curl (`templates.CURL45`). Third reading: "a red balloon that is floating away above her, its
  string dangling loose, so it looks as though she has just let it go"; "Its string ends in mid-air well above her hand, so she is clearly no longer
  holding it". No hook, and the railing is not named.

**A child's ice cream** (test 4): "a boy in a yellow shirt and orange shorts walks toward the right, holding a pink ice-cream cone"; "holding up a
pink ice-cream cone in one hand". A cone in all three readings, in a child's hand, at the size v0.44's was "a lollipop".

**The slide's ladder** (test 4): "a playground slide with a red ladder and frame and a yellow/orange chute"; "red metal frame and ladder". No remark
on the ladder.

**The camera** (test 5): "holding a camera up to his eye and taking a photo", "camera on a yellow strap".

**The dropped ice cream** (test 5): "standing holding an empty ice-cream cone"; "a brown dog with a red collar is licking it up".

**The goat's stake** (test 6), behind the bench that it stood on in v0.44's probe: "a white goat with a red collar is eating grass. It is tied with a
rope to a small stake in the ground"; the bench is "empty" and is not named with the stake.

For the watch list: the roller "slightly away" from the paint (test 2), the wheelbarrow that "looks a bit flat or tilted" (2), the hose nozzle read
as aimed at the washing (3), the bench sitter whose "feet seem to rest in front of the bench legs" and "the bench back appears partly behind/through
his torso" (4), a moustache in profile that "could also look like he has food in his mouth" (6), the pram with "no clear shadow" (6) and a bush that
"looks slightly as if it is floating at the horizon line" (6).
