# Review p3: 26 tier-3 probes (garden 15, park 8, playground 2, street 1)

Scope: I viewed each of the 26 PNGs whole at 1600 x 1000 before reading its record, then cropped every scored element (and suspect props) from the record's bounding boxes and viewed them enlarged 2 to 5 times; crops are in tpdb_work/review56/crops_p3/.
I also viewed pictures reduced to 800 x 500 (saved as *_small.png) and compared the same figure or prop across pictures (feeders, waiting dog, paint scene, sweepers, catch ball, goat, watering can).

## Findings, most severe first

1. **Medium: the paper bag held by bird and duck feeders floats with no hand on it.**
   Pictures and regions: T3_park_s23031 [900,650,970,705], T3_park_s23035 [632,648,672,700], T3_park_s23040 [632,648,672,700], T3_street_s40510 [330,750,370,808].
   The bag hangs behind the forearm at waist height, and no hand, strap or arm grips it, so it looks pasted onto the figure.
   Events: ducks_bread and feed_birds.
   Seen in: 4 of 4 pictures with a feed_birds figure.
   Fix: put the bag in the second hand with a visible grip, tuck it clearly under the far arm, or stand it on the ground at the feeder's feet.

2. **Medium: the "ladder leaning on nothing" stands with its upper half against the distant tree line, so it can look as if it leans on the hedge.**
   Picture and region: T3_park_s25029 [1116,442,1224,710].
   At 800 x 500 the ladder's top meets the dark green tree band on the horizon, and that band is the only thing behind it, so depth is unclear and the contradiction weakens.
   Event: ladder_nothing.
   Seen in: 1 of 1.
   Fix: make the ladder taller, or move it forward, so its top stands well clear in open sky with a visible gap. Keep its foot off the path edge, and perhaps add a figure on it or looking at it.

3. **Medium: the leash in the waiting dog's mouth is a short yellow strap ending in a ring, which reads as a ring toy and not as a leash.**
   Pictures and regions: T3_garden_s23025 [1416,706,1436,778], T3_garden_s23064 [164,706,184,778], T3_garden_s25018 [164,706,184,778].
   The strap is about 70 px long, ends in a loop in mid-air, has no clip and no length trailing to the ground, and at 800 x 500 it is a small yellow ring by the dog's chin.
   Event: dog_wants_walk (the scored entity is the leash).
   Seen in: 3 of 3.
   Fix: draw a longer leash in a colour that matches the collar, with a clip end and a length coiled or trailing on the ground in front of the dog.

4. **Medium: the grandmother's reaching hand lands exactly on the top corner of the garden gate, so she seems to be holding the gate, not reaching for her hat.**
   Picture and region: T3_garden_s26002 [148,428,172,448].
   Her raised hand rests on the gate's top corner, while the hat is about 60 px further up and to the left, above the tree line.
   Event: windy_hat.
   Seen in: 1 of 2 windy_hat pictures (in s23025 the hand is in clear space).
   Fix: keep the reaching hand clear of fence and gate outlines, for example by moving the figure right onto open lawn, or bring the hat closer to the hand.

5. **Low: the paint tray reads as a dog's water bowl.**
   Pictures and regions: T3_garden_s23046 [504,712,584,732], T3_garden_s25018 [1200,712,1280,732], T3_garden_s26002 [1032,674,1110,696], T3_garden_s41504 [780,712,860,732].
   The tray is a flat grey dish holding a pool of mid-blue, near a dog, so a viewer may say the dog stepped in its water. The tin with a blue drip helps.
   Event: paint_tracks.
   Seen in: 4 of 4.
   Fix: draw a roller tray, which is sloped and ribbed, with the roller resting in it and a thicker paint colour.

6. **Low: the freshly painted boards are a solid block in exactly the blue of the house door, so at small size they can read as a blue gate in the fence.**
   Pictures and regions: T3_garden_s23046 [690,426,834,618], T3_garden_s25018 [950,426,1094,618], T3_garden_s26002 [1196,426,1294,618], T3_garden_s41504 [966,426,1110,618].
   The block covers whole boards and both rails evenly, and is not half-done or streaky. In s26002 it also abuts the house.
   Event: paint_tracks.
   Seen in: 4 of 4.
   Fix: use a colour that does not match any door, and leave an uneven edge or a half-painted board where the roller is.

7. **Low: the paint roller's cylinder is vertical, so it would roll sideways against the upright boards.**
   Pictures and regions: T3_garden_s23046 [698,456,728,512], T3_garden_s25018 [1056,456,1086,512], T3_garden_s26002 [1206,462,1234,510], T3_garden_s41504 [974,456,1004,512].
   Event: paint_tracks.
   Seen in: 4 of 4.
   Fix: turn the roller head so its cylinder is horizontal.

8. **Low: the catch ball's dashed flight trail runs from the thrower's fingertip to the ball like a string, and the ball's white curved band looks like a smile.**
   Picture and region: T3_garden_s23057 [270,524,340,612].
   The dashes start at the fingertip and end at the ball, so the pair can read as a yo-yo.
   Event: play_catch.
   Seen in: 1 of 2 (in s23061 the trail starts a little away from the hand); the smile-like band is seen in 2 of 2.
   Fix: start the trail a gap away from the hand, use an arc of short motion marks behind the ball, and give the ball a seam that is not a single smile curve.

9. **Low: the sweeper's hands do not clearly grip the broom.**
   Picture and region: T3_garden_s25018 [1340,470,1420,560].
   The handle is drawn over the knuckles of the upper fist, and the lower hand sits beside the handle instead of round it.
   Event: sweep.
   Seen in: 1 of 3 sweep pictures (s23061 and s41504 grip correctly).
   Fix: redraw or re-pose that facing direction so both fists close round the handle.

10. **Low: the goat's chin beard is drawn as a grey pointed wedge under the muzzle, which looks like a beak.**
    Pictures and regions: T3_park_s23031 [474,810,520,880], T3_park_s23035 [1020,575,1050,625].
    Event: goat_grazing.
    Seen in: 2 of 2.
    Fix: draw the beard as a white or tufted shape that hangs from the chin, not as a grey point.

11. **Low: the seesaw in the plain seesaw event is almost level, and neither end nor any foot touches the ground, so the children look as if they are sitting still, not playing.**
    Picture and region: T3_playground_s23069 [196,648,634,862].
    Event: seesaw.
    Seen in: 1 of 1.
    Fix: tilt the plank about 15 degrees with the low end on the ground and the low child's feet pushing off.

12. **Low: the man walking with an ice cream has his rear foot on the edge of the flower bed, as if he is stepping into it.**
    Picture and region: T3_park_s40502 [1074,840,1200,905].
    Event: ice_cream.
    Seen in: 1 of 4 ice_cream pictures.
    Fix: keep walkers' feet a clear gap from flower beds and other ground props.

13. **Low: the fish-in-tree limb is drawn over the foliage outline and ends exactly under the fish, so the fish looks set on a stick in front of the canopy.**
    Picture and region: T3_garden_s23008 [1080,300,1200,440].
    Event: fish_in_tree.
    Seen in: 1 of 1.
    Fix: draw the branch inside the canopy with leaves overlapping it, and lay the fish across the branch.

14. **Low: the filler watering can has a plain stick for a spout and a bucket-style handle, and reads as half bucket, half can.**
    Pictures and regions: for example T3_garden_s23008 [362,884,458,962] and T3_garden_s23014 [1142,884,1238,962].
    No event (filler).
    Seen in: 13 of 15 garden pictures.
    Fix: add a rose to the spout and a closed handle arching over the top.

15. **Low: the figure the records call a teenager (leo) reads as a young boy of about ten.**
    Pictures: T3_garden_s23008, T3_garden_s23019, T3_garden_s23057, T3_garden_s26002, T3_park_s40502.
    This touches items i04 (s23008), i02 (s23019), i01 (s23057), i02 (s26002) and i01 (s40502).
    Seen in: 5 of 5 pictures with leo.
    Fix: make sure the accepted answers include "boy", or make the figure older (taller, longer face).

## Contradictions

- fish_in_tree (T3_garden_s23008): this reads clearly; a bright orange goldfish against dark green foliage is obvious and plainly wrong, and the only risk is that it is taken as a toy or a decoration hung in the tree.
- sitting_on_air (T3_garden_s23033): this reads clearly; the grandfather is in a full sitting pose with only a shadow under his feet and open grass behind him, and an empty bench at far left reinforces that a seat is missing.
- ladder_nothing (T3_park_s25029): this reads only moderately well; the ladder is small and its top sits against the distant tree line, so it can be taken as a ladder propped against the hedge (finding 2).

## Picture by picture

- T3_garden_s23008: the fish's branch is drawn over the canopy like a stick (finding 13); otherwise the jump and the cat on the fence read well.
- T3_garden_s23014: nothing found that would cost an item; the reader, the box in his path, the planter and the digger all read at once.
- T3_garden_s23019: nothing found; the hose, water arc, sandwich-stealing bird and jumping girl read at once.
- T3_garden_s23025: the dog's leash reads as a yellow ring (finding 3).
- T3_garden_s23033: nothing found; the dog on the hose, the dry nozzle, the sitter on air and the jump all read.
- T3_garden_s23046: the paint tray looks like a water bowl, and the painted block is in the door's blue (findings 5 and 6).
- T3_garden_s23049: nothing found.
- T3_garden_s23052: nothing found.
- T3_garden_s23057: the ball's dashed trail touches the hand like a yo-yo string (finding 8).
- T3_garden_s23061: nothing found beyond the smile-like band on the ball (finding 8).
- T3_garden_s23064: the dog's leash reads as a yellow ring (finding 3).
- T3_garden_s24054: nothing found.
- T3_garden_s25018: the leash reads as a ring (finding 3); there are also the paint tray, paint colour and roller faults (findings 5 to 7) and a loose broom grip (finding 9).
- T3_garden_s26002: the grandmother's reaching hand rests on the gate corner (finding 4).
- T3_garden_s41504: the paint tray, paint colour and roller faults (findings 5 to 7).
- T3_park_s23031: the feeder's bread bag floats unheld (finding 1), and the goat's beard looks like a beak (finding 10).
- T3_park_s23035: the feeder's bread bag floats unheld (finding 1).
- T3_park_s23040: the feeder's bread bag floats unheld (finding 1); the begging dog reads well.
- T3_park_s23067: nothing found.
- T3_park_s25029: the ladder can look propped against the distant trees (finding 2).
- T3_park_s40502: the walking man's foot is at the flower bed edge (finding 12); the begging dog reads well.
- T3_park_s40508: nothing found.
- T3_park_s40512: nothing found.
- T3_playground_s23069: the seesaw is almost level, with no foot on the ground (finding 11).
- T3_playground_s23072: nothing found; the heavy grandfather on the low end, the girl stuck up and calling, and the slider all read.
- T3_street_s40510: the feeder's seed bag floats unheld (finding 1).

## Looked for and found fine

- The jumpers (s23008, s23019, s23033) have both feet clearly off the ground, with a detached shadow below.
- Every seated figure (the bench readers, the ice-cream eaters on benches, the seesaw riders and the swing rider) sits on the seat with no gap.
- The hose events read: the water arc lands on the flowers in s23019, and in s23033 the hose runs from the reel, under the dog's paw, up to the nozzle the grandmother is inspecting.
- The paw prints lead from the tray to a dog with blue paws that is walking away, in all four paint_tracks pictures.
- The duck feeders' crumbs lie on the water between the hand and a duck that is pecking or approaching, with a wake behind it.
- The cats walk on the picket tops, and both the grey and the orange cat stand out against the tree line.
- The fishing rod is gripped in both hands, and the line drops to a float with a ripple.
- The balloon string, the bird on the lamp, the stroller grip and the slide rider are all fine.
- The figures are consistent across pictures: the same person or prop is drawn the same way wherever it appears, apart from the broom grip in s25018.
- No faces are hidden, and no expression contradicts its event.
