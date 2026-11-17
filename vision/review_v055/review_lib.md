# Review of the cast library (lib055, 355 sprites)

I viewed all 30 sheets at full size, six sheets reduced to half size, and enlarged crops, faces and true-scale line-ups made from the single sprites in assets/cast/lib055 (saved in tpdb_work/review56/crops_lib/).
I also compared sprite sizes from the anchors in each NAME.json and counted the differing pixels between every pair of sprites that share family, pose and angle but differ in expression.

Note on the sheets: the fishing sprites (ben, leo, mei, tomas) look child-sized on the sheets only because the long rod makes the tile shrink to fit; measured from head_top to ground point they are the same height as the other poses, so this is not a sprite fault.

## Findings, most severe first

1. **High: the hang_washing pose reads as diving, stretching or "hands up", not as pegging washing.**
   Sprites: person.ben__hang_washing__neutral__y090, person.mei__hang_washing__neutral__y090, person.mei__hang_washing__smile__y090, person.rosa__hang_washing__smile__y090, person.tomas__hang_washing__neutral__y090, person.tomas__hang_washing__smile__y090 (6 of 6 hang_washing sprites).
   Both arms go straight up and forward with the palms pressed flat together like a diver, so the hands hold no peg or cloth and give no sign of reaching to a line.
   The near arm starts in front of the chin and chest instead of at the shoulder (clearest on Tomas, whose white sleeve rises out of the middle of his waistcoat), and it covers the mouth, so the smile and neutral variants cannot be told apart.
   Fix: keep the upper arms at the shoulders, raise the hands to about head height and a little apart, with fingers pinched as if holding a peg or the top corners of a cloth, and keep the face clear of the arm.

2. **High: in feed_birds and feed_birds_low the person looks as if pointing at the ground or holding a parcel, not scattering food.**
   Sprites: person.ana__feed_birds__smile__y090, person.ben__feed_birds__smile__y090, person.dev__feed_birds__smile__y090, person.nia__feed_birds__smile__y090, person.tomas__feed_birds__smile__y090, person.ben__feed_birds_low__smile__y090, person.dev__feed_birds_low__smile__y090, person.leo__feed_birds_low__smile__y090, person.mei__feed_birds_low__smile__y090, person.tomas__feed_birds_low__smile__y090 (10 of 10).
   The bag is a square brown box that floats beside the hip with no visible hand on it, so it reads as a parcel.
   The feeding hand is a closed fist in feed_birds (reads as a punch or a held-out fist) and a flat paddle with the index finger extended in feed_birds_low (reads as pointing down at something).
   Fix: show the far hand gripping the rolled top of a paper bag, open the feeding hand palm-down with spread fingers, and add a few crumbs or seeds leaving the hand.

3. **Medium: in profile (y090) the expression is invisible, so smile, neutral, determined and focused variants are practically the same picture.**
   Sprites: 37 same-pose expression pairs differ in fewer than 200 pixels of an image about 650 pixels tall; for example person.ana__hose_spray__neutral/smile, ana__kneel_plant, ana__paint, ana__push, ana__water_plants, ben__water_plants, ben__kneel_plant, ben__run__determined/focused, dev__walk_bag, dev__water_plants, jo__walk_box, leo__kneel_plant, leo__paint, leo__walk_bag, leo__water_plants, mei__fish, mei__water_pan, mei__water_plants, nia__throw_ball, rosa__paint, rosa__push, rosa__walk_box, tomas__kneel_plant, tomas__paint, tomas__water_pan (all y090).
   The mouth in profile is a short tick on the edge of the jaw, about 10 pixels across at sheet size, and on Ben, Dev and Tomas it is covered by the moustache or beard, so no smile can be seen at all.
   Fix: in profile draw a longer, curved mouth set in from the jaw edge with a raised cheek and a crinkled eye for smiles, and lift the moustache or beard clear of the mouth corner on the three men.

4. **Medium: in fly_kite the raised arm covers the face, so puzzled, sad, smile and worried cannot be read.**
   Sprites: person.kai__fly_kite__puzzled/sad/smile__y090, person.leo__fly_kite__puzzled/sad/worried__y090, person.nia__fly_kite__smile__y090 (7 of 7).
   The head is tipped back and the near forearm passes in front of the mouth and chin; Kai's three variants differ by about 100 pixels and look identical, and Leo's differ only in the eye.
   Fix: hold the spool with the far arm, or bring the near arm lower and further forward so that the mouth and eyebrows stay visible.

5. **Medium: jump_tuck shows straight, spread legs with flat feet, which reads as cheering on the spot rather than a jump.**
   Sprites: person.kai__jump_tuck__happy/laughing__y045, person.leo__jump_tuck__happy/laughing__y045, person.nia__jump_tuck__happy/laughing__y045 (6 of 6).
   The legs hang straight in an A-shape with the soles flat as if standing, so even when the scene lifts the sprite off the ground it reads as a figure floating in a cheering stance, and the name's tuck is not drawn.
   Fix: bend the knees up under the body (tuck) or bend them back with pointed toes, so the pose cannot be read as standing.

6. **Medium: sweep and rake hold the broom or rake upright beside the feet, so the figure looks as if it is leaning on the tool, not working with it.**
   Sprites: sweep for ana (2), ben (2), dev (2), jo (1), leo (2), mei (1), rosa (1), tomas (2), and rake for ana, rosa and tomas (16 of 16).
   The handle is nearly vertical, the brush or rake head sits under the near foot with no lean and no forward reach, and the body is upright, which is the stance of someone standing and holding a broom.
   Fix: tilt the handle to about 45 degrees with the head out in front of the feet, bend the trunk slightly forward, and push the lower hand down the handle.

7. **Medium: the animals are at the wrong sizes against each other.**
   Sprites: animal.cat_01 and animal.cat_02 (all 6), animal.bird_01 and animal.bird_02 (all 16), compared with animal.dog_02 and the people.
   On a true-scale line-up the walking cats are as tall at the back as dog_01 and taller than dog_02, and a perching bird is about as big as the duck and comes up to Nia's knee, so the small birds read as hens or crows.
   Fix: if the scene generator does not rescale animals per species, shrink the cats to about two-thirds of dog_02 and the songbirds to about half their present size.

8. **Medium: the grazing goat seen from the side has its head folded under its chest, so it has no face.**
   Sprites: animal.goat_01__graze__happy__y090 and animal.goat_01__graze__neutral__y090 (2 of 3 goat sprites).
   The head is turned down and back into the neck so that only a white lump, one horn and a grey patch show, which reads as a headless or sheep-like animal, and the happy variant cannot show any expression.
   Fix: put the head down and forward with the muzzle to the grass and the eye, ear, horns and beard in profile, as the y045 sprite already does.

9. **Medium: skirts and dresses turn into shorts in the seated and kneeling poses.**
   Sprites: person.mei__sit_drink__smile__y045, mei__sit_read__neutral__y045, mei__sit_ground__happy__y045; person.nia__sit_drink__content__y045, nia__sit~near__smile__y090, nia__sit__smile__y090, nia__sit_ice_cream (2), nia__sit_read__neutral__y045, nia__seesaw_stuck_call__calling__y090, nia__sand_build__smile__y045; person.rosa__sit_ice_cream__content/smile__y045, rosa__sit_read__neutral__y045, rosa__kneel_plant__smile__y090 (about 17 of the 24 seated or kneeling sprites of the three women and girls).
   The skirt wraps each thigh separately with a crease between the legs, so from the front it looks like a pair of shorts and the figure's clothes change from pose to pose.
   Fix: drape the skirt as one sheet across both thighs with the hem hanging over the knees.

10. **Medium: Jo and Leo have the same face, and Jo does not read as a grown man.**
    Sprites: all 6 person.jo sprites, compared with the 39 person.leo sprites.
    Both have the same round beardless face, brown hair, skin tone and peaked cap, and differ only in cap colour and clothes, so Jo looks as young as Leo, and a viewer could take Jo for a teenager in a hi-vis vest.
    Fix: give Jo an adult cue such as stubble or a moustache, a longer jaw and a different hair colour, and give him a heavier build.

11. **Medium: the pecking bird seen at three-quarter angle is a tilted blob.**
    Sprites: animal.bird_01__peck__neutral__y045 and animal.bird_02__peck__neutral__y045 (2 of 4 peck sprites).
    The body is tipped forward and the dark wing oval covers most of it, so the head is a small stub at the bottom and at scene size the bird reads as a red or blue ball.
    Fix: show more of the head and beak against the ground and make the wing smaller than the body.

12. **Low: skin-coloured patches show through Mei's dress.**
    Sprites: person.mei__run__focused__y090 and person.mei__kneel_plant__neutral__y090 (2 of 29 Mei sprites).
    In the run a pale skin patch shows on the dress behind the knee, and in kneel_plant a skin wedge shows at the hem and the dress bulges into a lump at the hip.
    Fix: correct the cloth so that the rear leg passes under the hem.

13. **Low: in cone_dropped the cone is still held and still looks full.**
    Sprites: person.kai__cone_dropped__sad__y045 and person.nia__cone_dropped__sad__y045 (2 of 2).
    The cone floats at the shoulder with no visible hand, its open end shows a dark brown filling and a pink fingertip, so it reads as holding a chocolate cone, and "dropped" depends wholly on the scoop that the scene adds.
    Fix: show the hand holding an empty, light-coloured cone, or draw the hand open and empty.

14. **Low: the catch pose without a ball reads as sleepwalking.**
    Sprites: catch for ana (2), ben (2), dev (2), kai (2), leo (1), mei (2), nia (2) (13 of 13).
    Both arms go straight out at chest height with palms up, so the figure reads as reaching or sleepwalking until the ball is placed in front of the hands.
    Fix: spread the hands a little apart with cupped fingers and lean the trunk back a little.

15. **Low: in photo the camera hides the face, so the smile and neutral variants are identical.**
    Sprites: person.mei__photo__neutral/smile__y045 and person.tomas__photo__neutral/smile__y045 (4 of 12 photo sprites).
    The camera covers the eyes and mouth, and each pair differs in about 100 pixels.
    Fix: drop the extra expression variant, or show the mouth below the camera.

16. **Low: Ana and Mei have the same face and hair.**
    Sprites: all 34 person.ana and 29 person.mei sprites.
    Both women have the same face, the same long black hair with a ponytail and nearly the same skin tone, so they can be told apart only by their clothes.
    Fix: change one woman's hairstyle, for example a bob or a bun for Mei.

17. **Low: some animal expression variants are the same picture.**
    Sprites: animal.cat_01__walk__happy__y090 against walk__neutral__y090 (39 differing pixels), and the bird sing variants, whose open beak is only a slight gap.
    Fix: give the happy cat narrowed eyes and an upturned tail tip, and open the singing beak wider.

## Figure by figure

- **Ana** (woman): clearly a grown woman in a purple top and teal trousers, consistent in every pose. Her weakest poses are feed_birds and the profile smiles.
- **Ben** (man): clearly a grown man with a moustache, red T-shirt and blue jeans, consistent in every pose. His weakest pose is hang_washing, and his moustache hides every profile smile.
- **Dev** (man): clearly a grown man with a beard and a green T-shirt. His beard and dark skin hide the mouth, so his smiles do not show, and his weakest pose is feed_birds_low.
- **Jo** (man, 6 sprites): the hi-vis vest and cap read as a worker, but his face is Leo's and he looks young. His weakest pose is sweep, with the broom upright.
- **Kai** (boy): reads at once as a young boy, with consistent yellow and orange clothes. His weakest poses are fly_kite, where the face is hidden, and jump_tuck.
- **Leo** (teenage boy): the cap and hoodie are consistent and he is sized between Kai and the adults, but his face reads as an older child as much as a teenager. His weakest pose is fly_kite.
- **Mei** (woman): reads as a grown woman in a yellow dress. Her dress turns into shorts or shows skin in the sitting, kneeling and running poses (her weakest is kneel_plant), and her face matches Ana's.
- **Nia** (little girl): reads at once as a small girl in a pink dress. Her dress splits into shorts in every seated pose, and her weakest pose is seesaw_stuck_call.
- **Rosa** (grandmother): grey bun, glasses and cardigan read at once as a grandmother in every pose. Her weakest poses are sit_ice_cream, where the skirt splits, and hang_washing.
- **Tomas** (grandfather): grey hair, flat cap, waistcoat and white moustache read at once as a grandfather. His weakest pose is hang_washing, where the arm comes out of his chest.
- **bird_01** (red): reads as a small bird when perching and singing, but it is far too large. Its weakest pose is peck at y045.
- **bird_02** (blue): the same as bird_01. Its weakest pose is peck at y045.
- **cat_01** (grey): reads as a cat, with pointed ears, whiskers and an upright tail, but it is dog-sized. Its weakest sprite is walk__happy, which is identical to neutral.
- **cat_02** (orange): reads as a cat, and the sleeping curl is good. Its weakest pose is walk, because of the size.
- **dog_01** (brown, red collar): reads as a dog in every pose, and the begging, play bow, sniffing and reading poses are clear. Its weakest pose is sleep_paws_turn, which is a little small and flat, but still readable.
- **dog_02** (spotted, blue collar): reads as a dog in every pose. It is smaller than the cats, which is its main fault.
- **duck_01**: reads as a white duck by its beak and shape. Its weakest pose is swim_look, where the head turns down and away.
- **goat_01**: reads as a goat at y045, with horns and an eye. At y090 the head is folded out of sight.

## The fifteen weakest sprites

1. person.tomas__hang_washing__neutral__y090: the arm rises out of the middle of his chest and covers his face, and the pose reads as diving.
2. person.ben__hang_washing__neutral__y090: the arms are pressed straight up together, and the pose reads as a dive or a stretch.
3. person.mei__hang_washing__neutral__y090: the arms are raised with flat palms in front of the face, and nothing suggests washing.
4. person.tomas__feed_birds_low__smile__y090: the flat pointing hand and floating box read as pointing at the ground.
5. person.dev__feed_birds__smile__y090: a closed fist held out beside a floating box reads as holding a parcel.
6. person.kai__fly_kite__smile__y090: the arm covers the mouth, so the smile cannot be seen, and it is identical to puzzled and sad.
7. person.kai__fly_kite__puzzled__y090: the face is hidden by the arm, so puzzlement cannot be read.
8. animal.goat_01__graze__happy__y090: the head is folded under the chest, so the goat has no face.
9. animal.bird_01__peck__neutral__y045: a tilted red ball with a large wing oval, with the head barely visible.
10. person.kai__jump_tuck__happy__y045: the straight, splayed legs with flat feet read as cheering on the ground.
11. person.leo__jump_tuck__happy__y045: the same as Kai's, with the legs straight and wide, so it reads as cheering.
12. person.mei__kneel_plant__neutral__y090: the dress bulges at the hip and a skin wedge shows at the hem.
13. person.rosa__sit_ice_cream__content__y045: the skirt is split into two shorts legs.
14. person.dev__water_plants__smile__y090: the beard hides the mouth, so the smile is identical to neutral.
15. person.ben__sweep__neutral__y045: the broom is upright beside his feet, so he looks as if he is standing with it, not sweeping.

## Looked for and found fine

- The people are drawn at one consistent size per person across poses (head-to-ground spread under 5 percent in standing poses), and the order of sizes, from Nia and Kai through Leo to the adults, matches their ages.
- Clothes, colours, hair and accessories stay the same for each person in every pose, apart from the skirt problem in finding 9.
- The seated poses (sit_ice_cream, sit_drink, sit_read) have thighs level, knees bent at the seat edge and shins down, with the lower body correctly drawn.
- The walk, walk_box, walk_bag, walk_read_open, walk_ice_cream, run, push, wave, point_up, reach_up, photo, eat_ice_cream, water_plants, water_pan, dig_lift, kneel_plant and throw_ball poses read at once for every figure that has them.
- The deliberate contradictions (the bucket worn as a hat, sweeping with a giant fork, watering from a frying pan, a dog reading in glasses) are drawn clearly and unmistakably.
- The front-facing faces (sit_swing, wave at y000) and the three-quarter faces carry their expressions clearly, including Kai's and Leo's puzzled, sad and worried point_up faces and Rosa's scared and surprised reach_up faces.
- The layer sprites (~far and ~near for sit and seesaw) are clean partial figures that line up with their full sprites.
- The fishing sprites are the same height as the other poses; they look small on the sheets only because the rod enlarges the tile.
- The dogs' begging, play bow, sniffing, sitting and sleeping poses and the cats' stalking and sleeping poses read as their species and action at both angles.
