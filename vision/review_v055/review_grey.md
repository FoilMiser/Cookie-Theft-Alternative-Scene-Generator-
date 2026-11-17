# Grey review, review56 (21 grey pictures from list_grey.txt)

Scope: I viewed all 21 grey pictures whole at full size (1600 x 1000) before reading their records, then at 800 x 500, then every scored element as a crop enlarged 2 to 4 times (contact sheets and context crops are in tpdb_work/review56/crops_grey/), and opened the colour picture only after judging the grey one.
Grey levels are 0 to 255, read from the pixels of the grey PNGs with Pillow and numpy (fill levels are the dominant value inside the object, surrounds are the dominant value just outside it); the colour-to-grey mapping was checked pixel by pixel in the colour PNGs.

## Findings, most severe first

1. **High: the dropped ice cream turns into the grass, or into a plain grey puddle.**
   Pictures: T3_playground_s10102_iso [702,944,846,990], T4_park_s728923 [846,934,990,982], T4_playground_s512950 [728,948,872,994] (on grass); T3_street_s133 [914,924,1056,972], T4_street_s171111_iso [982,644,1094,682], T4_street_s464887 [188,742,312,784] (on paving).
   The splat's pink fill (238,145,183) becomes grey 167 and the grass (114,192,90) is grey 168, so on grass the ice cream is only a black outline with a darker 134 rim around a patch the same grey as the lawn, and it reads as a hole or a wet patch, not as ice cream.
   On paving (212) the splat is a darker 134 to 167 blob, which is visible but reads as a puddle or a spill rather than ice cream, because nothing but its colour said "strawberry ice cream".
   The empty cone in the child's hand also fades on grass: its body (210,154,92) becomes 161 against grass 168, and its dark mouth (73) could be taken for a chocolate scoop still in the cone.
   Event: ice_cream_drop, the entity "Ice cream is lying on the ground" and the inference "The child dropped the ice cream"; the dog licking and the crying child still carry part of the story.
   Colour: the fault is grey's alone; in colour the splat is bright pink with coloured sprinkles and reads at once.
   Seen in: 6 of 6 (severe, fill equal to the ground, in 3 of 6 on grass; weaker in 3 of 6 on paving).
   Fix: give the ice cream a grey value far from both grounds, for example a near-white scoop (about 235) with a mid-grey shadow rim, or keep the pink but darken it so it lands near 90 to 110 in grey; add a curved melt highlight and keep the sprinkles at high contrast so the texture says "ice cream" without colour.

2. **Medium: the kite caught in the tree has the same grey as the leaves.**
   Pictures: T2_park_s1022 [1284,410,1404,566], T2_playground_s042 [36,360,160,518], T3_playground_s10102_iso [1384,320,1508,476], T4_park_s728923 [1284,410,1404,566].
   The kite fill is 104 and the tree crown around it is 115, so only the black outline, the cross spars and the bow-tail mark the kite, and two foliage clumps (about 125) sit on top of it and break its shape.
   At full size I found the kite only by following the string; at 800 x 500 in T2_park_s1022 it is no more than a few lines inside the crown.
   Event: kite_in_tree, the entity "A kite is caught in the tree" and the inference that it got stuck.
   Colour: the fault is grey's alone; in colour the kite is purple against green and stands out.
   Seen in: 4 of 4.
   Fix: make the kite light in grey (a yellow or white kite, about 200 to 230 in grey) or give it a two-tone pattern of light and dark panels, and keep the foliage clumps from covering more than one corner of it.

3. **Medium: the sprinkler's water jets are hollow wire loops, and the wet package does not look wet.**
   Picture: T2_park_s14118_iso, sprinkler arcs [660,820,944,960] and package [882,896,996,976].
   The blue jets become grey 171 on grass 168, so each jet is just two thin dark outlines with nothing between them, and they read as bent wires or hoops rather than water; the droplets are hollow circles of the same grey as the grass.
   The water streaks on the box are 171 to 172 on a box face of 178, which is invisible, and the blue puddle under the box is close to the grass grey as well.
   Event: sprinkler_package, "A sprinkler is spraying water" and the inference "The package is going to get soaked".
   Colour: the fault is grey's alone; in colour the jets and the puddle are plainly blue water.
   Seen in: 1 of 1.
   Fix: draw the jets near white (about 235) with a darker core line, give the droplets solid light fills, and make the streaks on the box and the puddle under it a darker grey so the box looks wet.

4. **Medium: in T4_playground_s512950 the bird stealing the sandwich is a small dark blob against the dark bench back.**
   Picture: T4_playground_s512950, bird [1210,592,1252,630] beside the sandwich [1172,600,1230,630].
   The bird's body is 78, set against the black (38) outlines of the bench back and the dark railing behind it, and it is only about 42 x 38 pixels; at 800 x 500 it is a smudge at the end of the bench and I could not tell it was a bird without a crop.
   Event: bird_steals, "A bird is pecking at a sandwich on the bench" and the inference that the bird is stealing it.
   Colour: the fault is grey's alone; in colour the bird is bright blue against a tan bench.
   Seen in: 1 of 2 (in T4_street_s464887 the same bird sits on a lighter bench in front of light paving and reads, though it is just as small).
   Fix: lighten the bird's belly and head (or the whole bird to about 150) so it separates from the dark bench back, or move it onto the seat in front of the light slats; a slightly larger bird would help both pictures.

5. **Medium: in T3_playground_s3043 the ice cream the woman eats is lost against her face and shirt, so the begging dog has nothing to beg for.**
   Picture: T3_playground_s3043, ice cream at about [405,535,435,575] inside eater_1 [372,500,478,708].
   The pink scoop becomes 134, her skin is 148 and her shirt is 142, so the scoop is a small round outline at her mouth that reads as her hand or a bun; at 800 x 500 she simply looks as if she is touching her face.
   Event: dog_begs, "A woman is sitting on the bench eating an ice cream" and the inference "The dog wants some of the food".
   Colour: the fault is grey's alone; in colour the pink scoop on a tan cone is clear against her purple shirt.
   Seen in: 1 of 2 (in T3_park_s8023 the boy's scoop, 134, stands clear of his darker skin, 94).
   Fix: as in finding 1, give the scoop a grey far from skin tones (near white, about 235) and hold the cone a little away from the face.

6. **Low: the pond is only 13 grey levels darker than the grass.**
   Pictures: T1_park_s1021, T2_park_s1022, T2_park_s14118_iso, T3_park_s8023, T4_park_s728923, pond at about [140,570,800,730].
   The pond's blue (90,169,216) becomes 155 against grass 168, and its highlight streaks (171) are lighter than the grass, so the pond is held up by its outline and the reeds and can look like a flat oval of lawn; in T4_park_s728923 the duck that must be "swimming toward the shore" depends on its white wake lines to look afloat.
   Event: the setting item "There is a pond" (scored in T3_park_s8023 and T4_park_s728923) and ducks_bread in T4_park_s728923.
   Colour: the fault is grey's alone; in colour the pond is clearly blue water.
   Seen in: 5 of 5.
   Fix: darken the water to about 120 in grey or add a few horizontal ripple lines across it.

7. **Low: several small animals and balls on the grass differ from it by only 15 to 17 grey levels and are held up by their outlines.**
   Pictures and regions: sleeping cat in T1_park_s1021 [630,900,712,956] and T2_park_s14118_iso [1066,898,1146,954] (fill 151 on grass 168); sleeping dog in T2_playground_s9109_iso [604,764,716,824] (153 on 168); kicked ball in T1_park_s1021 [1292,792,1416,870], T2_park_s14118_iso [382,830,514,912] and T2_playground_s9109_iso [1268,836,1398,918] (152 on 168).
   Each is still recognisable in a crop because of its black outline and inner lines, but at 800 x 500 the sleeping cats and the sleeping dog are small grey lumps that a viewer may pass over.
   Events: cat_sleeping, dog_sleeping, kick_ball.
   Colour: the fault is grey's alone; in colour the cats are orange, the dog brown and the balls coloured on green.
   Seen in: 2 of 3 sleeping cats (the cat in T3_playground_s3043 is lighter and stands clear), 1 of 2 sleeping dogs (the white dog in T1_playground_s041 is fine), 3 of 3 kicked balls.
   Fix: shift these fills to at least 40 levels from the grass (a lighter cat around 210, a darker ball around 100), or add a soft darker shadow under the sleepers.

8. **Low: the balloon floating away is a pale grey close to the sky.**
   Pictures: T2_playground_s9109_iso [980,386,1044,646], T3_park_s8023 [1106,238,1154,440], T4_playground_s512950 [666,252,722,458].
   The yellow loose balloon becomes 193 against a sky of 210, so only its outline and highlight make it, while the two held balloons are both dark (95 and 104); it still reads as a balloon on its string, but it looks faint and is the first thing to go at small size.
   Event: lost_balloon, "A balloon is floating up into the sky".
   Colour: the faintness is grey's alone; in colour the loose balloon is a strong yellow on light blue.
   Seen in: 3 of 3.
   Fix: give the loose balloon a darker grey value (a red or purple balloon, about 100) like the ones still held, which also makes it plainly one of the same set.

## Picture by picture

- T1_garden_s011: nothing found; the freshly painted boards (97) stand well apart from the unpainted ones (161) and the raked leaves read.
- T1_park_s1021: the sleeping cat (151 on 168) is faint and easy to pass over (Low, finding 7).
- T1_playground_s041: nothing found; the white sleeping dog and the sandcastle (189 on sand 216, outlined) read well.
- T1_street_s031: nothing found; the camera, the ball (95 on 212) and its dashed path are clear.
- T2_garden_s012: nothing found; the stalking cat, the pecking bird and the seeds read.
- T2_park_s1022: the kite in the tree has the leaves' grey and almost vanishes at reduced size (Medium, finding 2).
- T2_park_s14118_iso: the sprinkler jets are hollow loops and the package shows no wetness (Medium, finding 3).
- T2_playground_s042: the kite in the tree has the leaves' grey (Medium, finding 2).
- T2_playground_s9109_iso: the sleeping dog (153 on 168) and the pale loose balloon (193 on 210) are faint (Low, findings 7 and 8).
- T2_street_s032: nothing found; the perched bird (95) is outlined against the crown (115) and the stalking cat stands clear of the paving.
- T3_garden_s16013: nothing found; the beach ball in the tree, the leash (95), the pinched hose and the box in the reader's path all read.
- T3_park_s8023: the loose balloon is pale against the sky and the pond is close to the grass (Low, findings 6 and 8).
- T3_playground_s10102_iso: the dropped ice cream has the grass's grey (High, finding 1).
- T3_playground_s3043: the woman's ice cream merges with her face and shirt, weakening dog_begs (Medium, finding 5).
- T3_street_s133: the dropped ice cream reads as a dark puddle rather than ice cream (High family, finding 1).
- T3_street_s8104_iso: nothing found; the giant fork, the beach ball in the tree and the leash all read.
- T4_garden_s552986: nothing found; the bucket hat (226), the square wheel, the cat on the fence (99 on 142) and the painted boards read.
- T4_park_s728923: the dropped ice cream has the grass's grey (High, finding 1), and the kite merges with the tree (finding 2).
- T4_playground_s512950: the dropped ice cream has the grass's grey (High, finding 1), and the sandwich-stealing bird is lost against the bench back (Medium, finding 4).
- T4_street_s171111_iso: the dropped ice cream reads as a puddle (finding 1); everything else, including the dog with its newspaper and the bucket hat, reads.
- T4_street_s464887: the dropped ice cream reads as a puddle (finding 1); the man sitting on nothing and the square-wheeled bicycle read clearly.

## Looked for and found fine

- All contradictions still read in grey: the square wheels (bicycles and wheelbarrow, dark frames on light ground), the white bucket hats (about 226), the frying pan pouring water, the giant fork, the dog holding a newspaper (187 on a 153 dog) and the man sitting on nothing.
- The dark rain clouds in T3_street_s133 (76 on a 194 sky) and the woman pointing up read as rain coming.
- Freshly painted fence boards (97 against 161) in both paint_fence pictures.
- Leashes (95 on 161 to 168) and kite strings (dark lines) are not lost.
- The hose and the dog's paw pinching it, and the dry nozzle, in both blocked_hose pictures.
- The beach balls stuck in trees, whose white and dark segments stand out in all six ball_in_tree pictures.
- The balls in the air in the play_catch pictures (about 95 on light paving or sky), with their dashed paths.
- The duck (239), the bread pieces (223) and the bread in the girl's hand in T4_park_s728923.
- Watering-can water as light dashes over the flowers, and the frying-pan stream (light, outlined) in both pan_watering pictures.
- No two people or two animals in these pictures are told apart only by colour; figures differ in hair, build, age and clothes shape as well.
