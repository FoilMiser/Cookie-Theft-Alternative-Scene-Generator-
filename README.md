# TPDB v0.46: the cast drawn again in the settings' own line and two flat tones, with shorter necks, read a forty-third time

v0.45 ended with all 64 templates through the gate. Sam's brief for v0.46 was the drawing itself: "make moves to improve the art style for v.046 and clean up issues like the woman in the yellow dress having a neck that is too long". The work list came from three places:
- Sam's remark on the neck;
- an item of v0.45's set review (`tpdb_work/review45/review_set.md`, item 26), "Two outline systems in one picture": "people and animals have soft shading and thin outlines in a darker shade of their own colour; props and set have bold black outlines and flat fills". It asked for "a dark outline of constant width on the cast";
- a look at v0.45's cast at full size, figure by figure, which found a seam line at every wrist, the safety vest's bands standing off the chest, sleeves that stood off the arm like shoulder pads and a moustache with a notched edge.

All of the work is in the cast (builder 0.46.0). The bench read it in whole pictures and then in enlarged figure cut-outs, v0.45's drawing beside v0.46's, in five rounds, and took these:
- **The line:** a figure's outer edge is 9.5 px wide at render size, about 4.5 px in a picture, which is the settings' own line, and the lines inside it are 5.5 px (v0.45 had one 5 px line, about half the weight of the settings'). The line takes no light, so it is the palette's outline colour; lit, it had come out darker than its ink in every earlier release.
- **The shading:** two flat tones, the colour and a shadow at 0.86 of it, with no pool of light (v0.45 had three soft tones against the settings' flat fills).
- **The necks** of the three figures with a scaled-down head (the woman in the yellow dress, the woman in purple and the man in the red shirt): the chin sits where a full-size head's does, no neck is added and the neck keeps its full width. Every grown figure's neckline is 1.4 cm higher and its neck a little fuller. On the model the neck that shows on the woman in the yellow dress went from 8.2 cm to 3.9 cm.
- **The figure:** her waist is wider (0.94 of the standard figure's for 0.86); a tee's sleeve ends nearer the arm's width, the shoulder is lower and smaller, and the resting arm hangs nearer the body.
- **Clean-ups:** no seam line at the wrist; the safety vest's two bands lie on the vest all the way round; the glasses are a plain dark wire, a fifth thicker; the moustache is a smooth curve rounded at its ends.
- **The mouth** drawn as a line: the lip-coloured line at v0.45's width, riding on a wider dark line of its own. It took three drawings: the first closed to a dark mark under the heavier line, and the second, a plain red line, was read by one bench reviewer as "a cut or blood".
- **Placement revision 43 is unchanged.** No scene rule was changed.
- **Looked at and left before the readers:** one line weight for the edge and the inner lines alike; the new line over v0.45's soft tones; flat colour with no shadow tone at all; a higher neckline still; glasses half as thick again.
- **Not worked:** the scene items of v0.45's list (the thief bird, the square wheels, the stalked bird and the oddities), carried to `vision/flaws_v046.md`.

The set was regenerated and screened a forty-third time. Every person and every animal is drawn anew, so no picture is identical to v0.45's.

The forty-third screen read 98 pictures, the set's 21 and 77 probes, with thirteen readers and four scorers: 1,035 of 1,063 scored items had full marks, and three were misread. **It is a weaker screen than v0.45's.** The set's overall score is 0.957, from 0.977, and four templates fall under the gate, where v0.45 had none: `dog_reading` (0.867), `about_to_trip` (0.889), `sweep_fork` (0.889) and `blocked_hose` (0.893). In one picture each the reading dog was "holding a newspaper in its mouth", the teenager who reads as he walks had the box "behind him", and the man sweeping with a garden fork was "digging into the ground"; the stopped hose fell on one reader's hedges in three pictures. Nothing was mended, swapped or read again after the screen, so the count is the first and only one, and the four head the list for v0.47. Of what the release set out to do: no reader of the 98 named a neck, an outline or a mouth, and the woman in the yellow dress is a woman in 29 descriptions of 30. The smoothed moustache was to two readers a possible "smear" or "smudge". Sixteen of the 28 items under full marks are clouds or a tree that six readers left out.

Everything is built by code and reproducible: the cast is modeled and posed in Blender (Blender 5.2.3 LTS), and the scenes are composed in SVG by the generator in `scenegen/`. From v0.24 the whole cycle also runs on Windows with an installed Blender (`RUNBOOK.md`, Setup).

Source and release history: https://github.com/FoilMiser/Cookie-Theft-Alternative-Scene-Generator- (each release is one commit; `RUNBOOK.md` there says how a release is made).

## What changed, and what the readers made of it

| What Sam, v0.45's reviewers or the bench saw | v0.46 |
|---|---|
| "Two outline systems in one picture": the figures in thin lines and soft shading, the settings in bold lines and flat fills | An outer edge as heavy as the settings' line, and two flat tones. In enlarged cut-outs beside v0.45's it was the better drawn in six pairs of eight and the nearer to the background's drawing in seven: "match the scene and read more clearly". In whole pictures the pair reviewers did not see it: "No difference" in sixteen pairs of sixteen |
| The neck of the woman in the yellow dress, too long (Sam) | 8.2 cm to 3.9 cm on the model. Seated on the bench: "neck about right; head size suits the body". With the ice cream, her head tipped back, a reviewer still wrote "neck too long and too thin, same as a", where a is v0.45's. No reader of the 98 screened pictures named a neck, and she is a woman in 29 descriptions of 30 |
| A seam line at the wrist, v0.45's "stray ring at the raised wrist" | Gone |
| The vest's bands, which in v0.45's drawing "look torn and spill past the outline" | They "are clean and stay inside the vest"; an "orange hi-vis vest with reflective stripes" in whole pictures |
| The glasses, in profile the far lens a black disc past the face | A plain dark wire. No gain shown: in both drawings they "look as if they are floating off the face" |
| The moustache's notched edge, "a dark brown blob around his mouth that reads more like a smudge than a moustache or mouth" | **Worse in the screen.** Smoothed and rounded at its ends, it "could also be a smear of something (for example chocolate) on his face" and "looks a little like a smudge"; four of its wearer's eleven descriptions name a moustache. First of the oddities for v0.47 |
| A line mouth under the heavier line | Drawn three times; the release's is v0.45's mouth made as geometry. No reader wrote of blood, a cut or a wound at a mouth. On a face in profile it is still "a red blob stuck on the cheek rather than a mouth", as v0.45's was |
| v0.45's soft tones, "shiny" and "plastic" in the cut-outs | Two flat tones. The shadow's hard edge was read once as a fault, "her arm drawn faintly through her body", and on the bench as "a fold or stain" on a lap. On the v0.47 list |
| The legibility gate, 64 of 64 in v0.45 | **60 of 64.** `dog_reading`, `about_to_trip` and `sweep_fork` each fell on one misread, and `blocked_hose` on one reader's hedges. No placement rule had changed, and nothing was mended, swapped or read again after the screen |
| v0.45's list: `bird_steals` 0.933, `square_wheel` 0.933, `cat_stalks_bird` 0.958 | Not worked: 0.972, 1.00 and 1.00 |

Left as notes for the pilot: the goat in a park "a little unusual", "a bottle that looks like wine sits beside a child at the picnic", and "the two women look identical (same face and hair), only their clothes differ".

## The isolation bench

The bench is eight tier-3 pictures, two each of the street, the park, the playground and the garden, with events forced among the planner's own so that all ten people of the cast and both dogs stand in at least one. Each was built on revision 43's rules in v0.45's cast and in v0.46's on the same seed, so only the cast differs (`vision/isolation_v046.md`). Three forced sets were swapped before any reading for ones the planner could place. There were five rounds and 41 fresh readers and reviewers:
- **Rounds 1 and 2, whole pictures.** Sixteen readers read every scene and every forced event as built, in both casts. Eight pair reviewers had the two pictures of a scene side by side, which is which drawn at random, and were asked how the people and animals are drawn and whether they belong to the drawing round them. On belonging they said "No difference" in sixteen pairs of sixteen: "I could not tell the two drawing styles apart at this size, so the choice should rest on other grounds". What they named, they named in both casts: thin necks, and the kneeling man's moustache, "a dark brown smudge at his mouth or chin that reads as a moustache or as dirt". One thing went against the new cast, the glasses ("her glasses are thin, light lines on a small face"), and the wire was thickened. A bench of whole pictures could not judge this release's changes, so round 3 enlarged the figures.
- **Round 3, twelve figures cut out of the bench pictures and enlarged to 640 px**, v0.45's beside the new, the order drawn at random. The new drawing was the better in eight pairs, v0.45's in two, with no difference in two; its outline and colours were the nearer to the background's in eight, with no difference in four. "Its bold outlines and flat colours match the scene, so the figure sits in it more naturally." "The vest stripes are clean and sit within the body, while in a they look scratchy and stick out like loose straps." The two pairs that went to v0.45 named two faults of the new drawing. Under the heavier line the mouth's own outline closed over its colour, "only a small dark mark"; and the shadow tone, one hard-edged band at 0.72 of the colour, was "a darker, dull yellow band that looks like a stain or a shadow pasted on". The mouth became a plain line with no outline, and the shadow was lightened to 0.86.
- **The line's colour.** The validator, run on the release's renders before round 4, put 374 of the library's 386 records under its palette share. Line Art's strokes were lit like any surface and came out at (28, 28, 34), where the palette's outline colour, which the settings are drawn in, is (38, 38, 46). It had been so in every release since Line Art came in, and a thin line hid it. The line now takes no light.
- **Round 4, the release's cast, sixteen pairs.** Beside round 3's drawing it was the better in three pairs of twelve, on the mouth alone, with no difference in nine: no reviewer saw the lighter shadow or the line's colour. Beside v0.45's, in four pairs, it was the nearer to the background's drawing in all four and the better drawn in two, v0.45's in two. And one reviewer wrote of the plain mouth: "a red smudge on the cheek beside the nose, too large and off to the side, which can read as a cut or blood rather than a mouth." A mouth that one reader in a handful can take for blood cannot go into a picture for patients, so it was drawn again: v0.45's coloured line, riding on a wider dark line sunk into the face.
- **Round 5, fourteen pairs.** Between the two mouths, in six pairs, one went to each and four were no difference; on the figure where the plain mouth had been a cut it was again "a red smear or wound on the cheek", and the new one "a smaller red mark that reads as a mouth". Beside v0.45's, in eight pairs, the release's drawing was the better in six, v0.45's in one, with no difference in one; it was the nearer to the background's drawing in seven, with no difference in one. Its "flat fills and firmer outlines match the scene and read more clearly", where v0.45's shading "looks like it belongs to a different picture". The one pair to v0.45 was given for the form its shading shows: "the shading gives the top, legs and shoes some shape".
- **The neck Sam named.** Seated on the bench, the release's is "neck about right; head size suits the body", where v0.45's is "neck about right, perhaps slightly long". Standing with the ice cream, her head tipped back, the reviewer with v0.45's beside it wrote "neck too long and too thin, same as a" of the release's, a being v0.45's, and another wrote "a little too thick (about as wide as the lower face) and slightly long". It was not shortened again: reviewers asked about the neck in that pose called it a little long in both drawings, and round 3's reviewer had called the seated one "a little short". The pose is on the watch list.
- **What the bench left open.** The mouth of a face in profile lies at the edge of the outline and is "a red blob stuck on the cheek rather than a mouth" in both mouths. Under the moustache the release's mouth is darker than the plain one was: "You cannot make out a mouth." Hands have no fingers and legs no knees, in both casts. And a crop changed a thing: both reviewers of the woman walking her dog read the lead, which the crop cut off from the dog, as "a thin red stick (a cane)".

The release's cast as it stands was read on the bench in cut-outs only; whole pictures in it were the design tests' and the screen's to read. Some readers and reviewers listed their round's folder when their files were written and so saw the names of the other files in it; none opened one, and from round 4 the maps lay outside the folders (`vision/isolation_v046.md`, The blind rule).

## Design tests

The cast of builder 0.46.0 was read blind in whole test scenes among other events, on revision 43's rules as they were (`vision/design_tests_v046.md`, six pictures, one fresh reader each). The six placed on their 6th, 5th, third, 7th, first and second seeds. Two forced sets were changed before a picture came of them: on 80 seeds the garden could not place a waterer, a planter and a raker together, nor the park an angler, a picnic and a pram, so the planter became the fence's painter and the picnic the feeding of birds. All six sets are plain events: the release changes how the cast is drawn and leaves the rules alone, so the contradictions and the inferences were left to the screen. Every forced event was read, eighteen of eighteen; nothing had to be fixed and no picture was built again:
- **The woman in the yellow dress**, in five of the six. No reader named her neck. With the ice cream: "a woman in a yellow dress walks towards the right, holding a pink ice-cream cone up near her face". On the bench: "a dark-haired woman in a yellow dress sits on a wooden bench reading a red book". Raking, bent over the rake at the picture's front edge, she was "a girl in a yellow dress": one reading of five, as v0.45's screen had one.
- **The mouths.** No reader wrote of blood, a cut or a wound, or of a mark on a cheek. Of the dog's walker, who has a moustache: "The man's face has a small dark mark around the mouth or chin, which could be a moustache or beard".
- **The older woman in glasses:** "an older woman with grey hair, glasses, a teal top and a grey skirt is using a paint roller on a long handle to paint the wooden fence blue. A paint tin stands on the grass by her feet". The roller drew the tests' one strong remark, held "well away from the blue part of the fence". It is an item of v0.45's list that the cast's drawing did not change, and it stays on the list with a second reading.
- **The worker:** "a younger man in an orange cap and an orange high-visibility vest walks to the right carrying a cardboard box, like a delivery worker", the vest's bands "reflective stripes".
- **The older man:** "an older man in a flat cap, brown waistcoat and white shirt sweeps a small pile of brown leaves with a yellow broom". His moustache was named in two readings of four, a "grey moustache" in one.
- **The others:** the photographer "holds a camera to her eye"; the dog's walker "walks a white dog with brown spots. The dog is on a red lead"; the kicker, "the ball is just leaving his foot, motion lines are drawn under his leg"; the child on the slide "is sliding down it with one arm raised".
- **Of the pictures as wholes:** "Nothing looks clearly impossible" in two readings, and the like in each reader's own words in the other four.

## Placement revision 43

Every record stores the placement revision it was made with. v0.46 pictures use revision 43, as v0.45's did: no placement rule changed in this release. The revision's rules, new in v0.45:
- **The lost balloon:** its string's end 62 to 80 px above the reaching hand at full size (`templates.BAL45`), the string a slow wave that grows toward its free end, with no curl (`CURL45`). On a playground the end lies nowhere on the railing (`RAIL45`). In the garden it lies above the wooden fence's pickets, 34 to 48 px at full size, and a child whose hand would be more than 200 px below it is not stood there (`WOOD45`).
- **The fence painter:** the wet paint on the board under the roller begins below the roller, so the roller lies on bare wood at the paint's edge; the painter stands a step further forward until the roller lies well below the boards' tops, the tin with them (`templates.PAINT45`).
- **The planter:** kneels at the bed's end and digs in the bed, a hole under the trowel's point, a few clods beyond it, the pot in front of the bed (`templates.PLANT45`).
- **The picnic:** a loaf and a bottle stand out of the basket, and where the blanket has room a plate with a slice of watermelon lies on it (`templates.PICNIC45`).
- **The goat:** its stake never drawn in front of a standing structure (`templates.TETHER45`).
- **A swimming animal:** cut along a waterline with a ripple round it, with no ground shadow (`library.SWIM45`).
- **The slide's ladder:** the frame's own end, in the frame's red: two rails to the ground with slate rungs between them, the near rail running on up into the hand rail over the deck (`settings.SLIDE45`).
- **The bird table:** its post stands in a tuft of grass (`settings.FOOT45`).
- **The reading dog:** its paper drawn 12 px toward the dog and 6 px higher, at the dog's scale, so the forelegs cross the near page and the paws lie on it (`templates.READ45`).

Each switch is "B"; any other value gives the rule's v0.44 form. The rules are v0.45's and the renders are not: a v0.45 record rebuilds with the v0.45 package, and a v0.46 record with v0.46's.

The cast draws every person and every animal again (builder 0.46.0), behind eleven switches read when it is built: `TPDB_STYLE46`, `TPDB_NECK46`, `TPDB_ARM46`, `TPDB_MEI46`, `TPDB_CLEAN46`, `TPDB_COLLAR46`, `TPDB_GLASSW46`, `TPDB_SHADE46` and `TPDB_INK46` at B, `TPDB_MOUSTACHE46` at C and `TPDB_MOUTH46` at D, which are the code's defaults. The letter O gives the drawing before the switch.

Every cell of the set placed under revision 43, with the priors of the cast's new drawing: tiers 1 to 3 on their base seeds, the tier-3 playground in the showcase pass on its base seed's eighth try; the tier-4 park on its seed and the tier-4 street on its forced set, both with v0.45's templates; the tier-4 garden on the fourth seed of its list and the tier-4 playground on the eighth. Five cells have v0.45's templates (tier 1's garden, park and street and tier 4's park and street) and eleven have others. The isomorphs are five again and not v0.45's five: only the tier-3 street drawn from the park pairs the same cells the same way round. The probe pass built 56, the pass stratified by angle added 15, and six more were forced for the coming rain and the windblown hat, which the passes had not placed: 77 probes. Every picture was looked at before the screen, and two probes were built again on other seeds after that look, for a kite's string that ran close past the fence painter's cap and a child's balloon 30 px under the angler's float. All 98 records rebuild identical to the pixel, and the library passes the validator in full, 400 of 400. Its soft palette warning is raised by 154 records (83 of 382 in v0.45): what is off the palette is the blended band where the heavier line meets a fill, and the target was not loosened.

The planner's difficulty priors are the calibration measured on the v0.46 templates (`calibration.json`), with f = 0 and a = 4.47 for every inference and contradiction, as in v0.20 to v0.45. With every figure drawn anew, 44 fields of the calibration moved by 0.002 or more, most of all `cat_stalks_bird`'s inference (s from -0.569 to -0.519), and 18 lines of the planner's priors moved with them.

## The forty-third blind screen

Thirteen fresh readers, who had never seen the key, described every picture of the new set and 77 probe pictures; four separate scorers, each given part of the pictures and the same prompt, marked each scored item against the key, exactly as in the earlier screens. The headline figures cover the set; the probe pictures count only toward the templates they carry. Every template appeared in at least three screened pictures, as in v0.10 to v0.45.

| | v0.4 (15 pictures) | v0.5 (21 pictures) | v0.6 (20 pictures) | v0.7 (21 pictures) | v0.8 (20 pictures) | v0.9 (21 pictures) | v0.10 (21 pictures) | v0.11 (21 pictures) | v0.12 (21 pictures) | v0.13 (21 pictures) | v0.14 (21 pictures) | v0.15 (21 pictures) | v0.16 (21 pictures) | v0.17 (21 pictures) | v0.18 (21 pictures) | v0.19 (21 pictures) | v0.20 (21 pictures) | v0.21 (21 pictures) | v0.22 (21 pictures) | v0.23 (21 pictures) | v0.24 (21 pictures) | v0.25 (21 pictures) | v0.26 (21 pictures) | v0.27 (21 pictures) | v0.28 (21 pictures) | v0.29 (21 pictures) | v0.30 (21 pictures) | v0.31 (21 pictures) | v0.32 (21 pictures) | v0.33 (21 pictures) | v0.34 (21 pictures) | v0.35 (21 pictures) | v0.36 (21 pictures) | v0.37 (21 pictures) | v0.38 (21 pictures) | v0.39 (21 pictures) | v0.40 (21 pictures) | v0.41 (21 pictures) | v0.42 (21 pictures) | v0.43 (21 pictures) | v0.44 (21 pictures) | v0.45 (21 pictures) | v0.46 (21 pictures) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Things, mean score | 0.98 | 0.98 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.97 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.95 | 0.99 | 0.96 | 0.94 |
| Actions, mean score | 0.87 | 0.92 | 0.95 | 0.93 | 0.97 | 0.95 | 0.98 | 0.98 | 0.99 | 0.99 | 1.00 | 0.98 | 1.00 | 1.00 | 0.98 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 1.00 | 0.99 | 1.00 | 0.99 | 0.99 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.99 |
| Inferences, mean score | 0.86 | 0.72 | 0.86 | 0.85 | 0.83 | 0.91 | 0.92 | 0.95 | 0.96 | 0.94 | 0.96 | 0.95 | 0.99 | 1.00 | 0.95 | 0.96 | 0.98 | 1.00 | 0.97 | 1.00 | 0.99 | 0.98 | 0.95 | 0.95 | 0.88 | 0.98 | 0.99 | 1.00 | 0.96 | 0.96 | 0.99 | 0.96 | 0.97 | 0.97 | 0.98 | 1.00 | 0.99 | 0.96 | 0.94 | 1.00 | 0.97 | 0.98 | 0.91 |
| Contradictions, mean score | 1.00 | 0.75 | 0.91 | 0.82 | 1.00 | 0.95 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 | 1.00 | 1.00 | 1.00 | 1.00 | 0.94 | 0.71 | 1.00 | 0.95 | 0.92 |
| All items, mean score | 0.93 | 0.91 | 0.95 | 0.94 | 0.97 | 0.96 | 0.98 | 0.99 | 0.99 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.99 | 0.99 | 0.98 | 0.99 | 0.99 | 1.00 | 0.99 | 0.99 | 0.99 | 0.98 | 1.00 | 0.99 | 1.00 | 1.00 | 0.99 | 0.99 | 0.98 | 0.95 | 0.99 | 0.98 | 0.96 |
| Items misread | 5 of 206 | 8 of 284 | 5 of 279 | 4 of 283 | 1 of 266 | 1 of 284 | 0 of 285 | 1 of 285 | 0 of 284 | 0 of 287 | 0 of 283 | 0 of 283 | 0 of 282 | 0 of 285 | 0 of 280 | 0 of 283 | 0 of 286 | 1 of 285 | 0 of 287 | 0 of 283 | 0 of 285 | 0 of 286 | 0 of 286 | 0 of 289 | 0 of 283 | 0 of 284 | 0 of 285 | 0 of 284 | 1 of 286 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 285 | 0 of 286 | 0 of 287 | 0 of 287 | 0 of 287 | 0 of 290 | 1 of 290 | 0 of 286 | 0 of 281 | 2 of 282 |
| Oddities per picture, as logged by the scorers | 6.6 | 1.8 | 2.8 | 2.5 | 1.5 | 2.3 | 1.5 | 1.0 | 1.5 | 2.1 | 1.3 | 1.4 | 1.1 | 1.3 | 1.9 | 1.3 | 1.2 | 1.1 | 1.2 | 1.0 | 5.2 | 2.6 | 2.6 | 2.2 | 2.0 | 2.3 | 2.3 | 0.6 | 0.8 | 0.9 | 0.5 | 0.2 | 0.6 | 0.4 | 0.8 | 0.8 | 0.5 | 0.4 | 0.7 | 1.1 | 0.7 | 0.5 | 0.2 |
| Readers' remarks per picture (recounted in v0.26) | 8.8 | 5.4 | 6.4 | 4.8 | 4.7 | 4.8 | 4.9 | 4.4 | 4.3 | 4.4 | 4.4 | 4.4 | 3.9 | 3.9 | 4.4 | 4.0 | 4.0 | 3.9 | 4.2 | 3.9 | 5.6 | 5.9 | 5.3 | 5.8 | 5.1 | 5.2 | 5.2 | 3.5 | 3.3 | 3.2 | 3.1 | 2.9 | 3.1 | 2.8 | 3.4 | 3.1 | 3.0 | 3.2 | 3.0 | 3.1 | 3.3 | 2.6 | 2.4 |

Across all 98 pictures 1,035 of 1,063 scored items had full marks, and three were misread. Of the 28 under full marks:
- sixteen are setting items that six readers left out, thirteen the clouds and three a tree, all zeros (v0.45 had twelve, from two readers);
- five are the stopped hose's, in three pictures that one reader read, who hedged in each: "may be standing on the hose or just in front of it", "It is unclear whether the dog is actually stepping on and blocking the hose or its paw just overlaps it.", and of the nozzle "a drop of water coming out";
- two are the reading dog's in one picture, the tier-4 street, a zero and a misread: "A brown dog sits up holding a newspaper in its mouth.";
- one is the reading walker's, a misread in the tier-4 garden isomorph: "The box is behind him, so he is not about to trip on it.";
- one is the fork sweeper's, a misread in a probe: "leaning on a big silver fork and digging into the ground";
- three are half marks: the thief bird "perched right beside it, looking ready to steal it", the balloon that "may have slipped from the girl (she reaches for it), or it may belong to no one", and the water that "looks more like a spray than a pour".

The set's headline is all items 0.957 (0.977 in v0.45). Its things lost six items, five to the clouds and one to a tree. Its contradictions lost the reading dog's two in the tier-4 street (0.923, from 0.955). Its inferences lost the walker's misread, the hose's cause and half of the balloon's (0.914, from 0.984). Its actions lost three half marks, the thief bird's and two of the hose's (0.988). Two of the set's 282 items were misread, where v0.45's set had none.

**After the screen.** Nothing was changed: the four failures stand, no probe was swapped and no picture was read again. A probe swapped for one that looks better to its builder is selection, and a second reading of an unchanged picture is a second roll of the dice. What the four pictures show (`vision/flaws_v046.md`, After the screen):
- **The reading dog.** Its forepaws and the paper's top corner lie over its muzzle. The pose and the paper's place are v0.45's, and only the line is new. It read as reading in four pictures of five: "sitting up on hind legs holding an open newspaper as if reading".
- **The walker.** A bird table's post stands right behind his back, and the walk pose's trailing foot points backward like a leading one; the reader had him heading the other way. The other two pictures read: "A blue bucket stands on the pavement just ahead of her, so she might trip over it."
- **The fork sweeper.** His heap lies at the path's edge and his dustpan wholly on the grass, which the placement rule does not check. A rule that kept the pan on the paving was measured and not made: on the garden's narrowing path it would all but end the template there, so the heap and the pan have to be drawn to fit the path first.
- **The stopped hose.** The drawing is v0.45's, where the same template read 1.00 over the same number of items. The three pictures are one reader's, and the other four read in full: "the bulge in the hose behind the dog suggests the dog is blocking it".

Whether the heavier line cost the dog and the walker their readings one screen cannot tell: each lost a reading in an earlier screen too, and with every figure drawn anew there is no picture to set the two drawings side by side. It is recorded as open.

**The cast in the descriptions.** The woman in the yellow dress is in 30 screened pictures, a woman in 29 and in one "A girl with dark hair, wearing a yellow dress and red shoes". No reader of the 98 named a neck or an outline, or wrote of blood, a cut or a wound at a mouth. The man in the red shirt is in eleven: a moustache in four descriptions, a beard in three (one has both) and neither in five. Two readers doubted the mark: "The brown mark under the man's nose reads as a moustache, but it could also be a smear of something (for example chocolate) on his face." and "The red-shirted man's face mark reads as a moustache or beard but looks a little like a smudge." One reader took the shadow tone's edge for a possible fault: "It could be shading, or her arm drawn faintly through her body." Both are on the list for v0.47.

**What the full marks rest on.** The scorers' notes mark 11 items they credited in full where the free description commits and the unsure section adds another reading (9 in v0.45). Halved, they take two more templates under the gate, `lost_balloon` (0.833) and `water_upward` (0.889): 58 of 64. One scorer gave twelve of the 28 marks under full, ten of them in one reader's seven pictures.

**Remarks were 2.38 a picture, 233 on 98 pictures**, from 1.71 to 3.12 a reader, the fewest of the forty-three screens.

The four templates under the gate, the two lowest that pass, the three of v0.45's list and seven plain events that redrawn figures carry; no scene of them was changed in this release (mean of each template's scored items; inference and contradiction items alone in the last column):

| Template | v0.45 | v0.46 | v0.46 meaning items |
|---|---|---|---|
| `dog_reading` | 1.00 (9 items) | 0.87 (15 items) | 0.80 (10) |
| `about_to_trip` | 1.00 (9 items) | 0.89 (9 items) | 0.67 (3) |
| `sweep_fork` | 1.00 (9 items) | 0.89 (9 items) | 1.00 (6) |
| `blocked_hose` | 1.00 (28 items) | 0.89 (28 items) | 0.71 (7) |
| `lost_balloon` | 1.00 (15 items) | 0.94 (9 items) | 0.83 (3) |
| `water_upward` | 1.00 (9 items) | 0.94 (9 items) | 0.92 (6) |
| `bird_steals` | 0.93 (15 items) | 0.97 (18 items) | 1.00 (6) |
| `square_wheel` | 0.93 (15 items) | 1.00 (18 items) | 1.00 (12) |
| `cat_stalks_bird` | 0.96 (12 items) | 1.00 (15 items) | 1.00 (5) |
| `ice_cream` | 1.00 (14 items) | 1.00 (21 items) | — |
| `sweep` | 1.00 (13 items) | 1.00 (16 items) | — |
| `paint_fence` | 1.00 (9 items) | 1.00 (7 items) | — |
| `walk_dog` | 1.00 (4 items) | 1.00 (5 items) | — |
| `photo` | 1.00 (5 items) | 1.00 (4 items) | — |
| `carry_box` | 1.00 (3 items) | 1.00 (4 items) | — |
| `read_bench` | 1.00 (3 items) | 1.00 (3 items) | — |

`dog_reading` reads 0.867 in five pictures, as reading in four of them. `about_to_trip` and `sweep_fork` read 0.889 in three pictures each, in full in two and misread in the third, and `blocked_hose` 0.893 in seven, in full in four. `lost_balloon` and `water_upward` read 0.944 in three each, on a half mark. Of v0.45's list, `bird_steals` reads 0.972 in six pictures and `square_wheel` and `cat_stalks_bird` 1.00 in six and five; none was worked, so the rise is one screen's roll and not a mend. Where a redrawn figure carries a plain event the reading held: `ice_cream` 1.00 in 21 pictures, `sweep` in sixteen, `paint_fence` in seven, `walk_dog` in five, `photo` and `carry_box` in four each and `read_bench` in three.

### The legibility gate

| Gate outcome | v0.9 | v0.9 retest | v0.10 | v0.11 | v0.12 | v0.13 | v0.14 | v0.15 | v0.16 | v0.17 | v0.18 | v0.19 | v0.20 | v0.21 | v0.22 | v0.23 | v0.24 | v0.25 | v0.26 | v0.27 | v0.28 | v0.29 | v0.30 | v0.31 | v0.32 | v0.33 | v0.34 | v0.35 | v0.36 | v0.37 | v0.38 | v0.39 | v0.40 | v0.41 | v0.42 | v0.43 | v0.44 | v0.45 | v0.46 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Pass (mean at least 0.9, at least two pictures, no misread) | 54 | 59 | 59 | 59 | 63 | 61 | 63 | 61 | 63 | 63 | 60 | 60 | 64 | 61 | 63 | 64 | 63 | 61 | 59 | 63 | 61 | 64 | 63 | 63 | 63 | 63 | 64 | 63 | 64 | 63 | 64 | 64 | 64 | 64 | 63 | 62 | 63 | 64 | 60 |
| Read well, but in fewer than two pictures | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Fail | 10 | 5 | 5 | 5 | 1 | 3 | 1 | 3 | 1 | 1 | 4 | 4 | 0 | 3 | 1 | 0 | 1 | 3 | 5 | 1 | 3 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 4 |

Every template was screened in at least three pictures (38 in three, 12 in four, 6 in five, 3 in six, 3 in seven, 1 in sixteen and 1 in twenty-one), and 60 of the 64 pass, where all 64 did in v0.45. The four that fail are in the table below; three carry a misread, and the gate fails any template with one. The count is the first and only one, with no fix and no re-read behind it. The lowest that pass are `lost_balloon` and `water_upward` (0.944) and `bird_steals` (0.972), and every other template reads 1.00. Per angle (`vision/v046/gate_yaw.json`), 20 of the 22 (template, angle) pairs pass: the stopped hose's dog reads 0.875 in profile over 8 items in 2 pictures and 0.833 at the three-quarter angle over 12 items in 3. The gate is a filter, and the pilot with people is the test of difficulty.

Templates that did not pass (`vision/flaws_v046.md` gives what the readers saw and the next fix):

| Template | v0.46 mean | Pictures | Misreads |
|---|---|---|---|
| `dog_reading` | 0.87 (15 items) | 5 | 1 |
| `about_to_trip` | 0.89 (9 items) | 3 | 1 |
| `sweep_fork` | 0.89 (9 items) | 3 | 1 |
| `blocked_hose` | 0.89 (28 items) | 7 | 0 |

## The generated set

16 showcase pictures (one per setting and tier) and 5 isomorphs. 21 of 21 meet every row of their tier's band and every placement and legibility rule.

| Scene | Content items | Inference units (contradictions) | Scene load | Content completeness | Inference completeness | Drawn objects | Edge density | Templates |
|---|---|---|---|---|---|---|---|---|
| T1_garden_s011 | 4 | 0 (0) | 3 | 0.783 | — | 15 | 0.036 | rake, paint fence, birds flying |
| T1_park_s1021 | 4 | 0 (0) | 3 | 0.775 | — | 16 | 0.022 | cat sleeping, kick ball, ice cream |
| T1_street_s031 | 4 | 0 (0) | 2 | 0.781 | — | 14 | 0.047 | photo, read bench |
| T1_playground_s5041 | 5 | 0 (0) | 3 | 0.779 | — | 16 | 0.033 | dog playing, run, drink bench |
| T2_garden_s3012 | 8 | 1 (0) | 4 | 0.709 | 0.387 | 19 | 0.045 | kite in tree, drink bench, sweep, water flowers |
| T2_park_s3022 | 8 | 1 (0) | 4 | 0.710 | 0.368 | 19 | 0.029 | cat stalks bird, plant flowers, run, push stroller |
| T2_street_s1032 | 8 | 1 (0) | 4 | 0.711 | 0.371 | 17 | 0.047 | cat stalks bird, balloon, wave, feed birds |
| T2_street_s6109_iso (isomorph of T2_park_s3022) | 8 | 1 (0) | 4 | 0.709 | 0.351 | 17 | 0.051 | dog begs, ice cream, birds flying, carry bag |
| T2_playground_s042 | 8 | 1 (0) | 4 | 0.700 | 0.384 | 19 | 0.036 | kite in tree, sandbox, dog playing, play catch |
| T2_playground_s6118_iso (isomorph of T2_garden_s3012) | 8 | 1 (0) | 4 | 0.692 | 0.369 | 16 | 0.035 | lost balloon, cat sleeping, carry box, sandbox |
| T3_garden_s12013 | 12 | 2 (1) | 6 | 0.651 | 0.333 | 20 | 0.041 | dog wants walk, sitting on air, dog sleeping, jump, bird perched, play catch |
| T3_garden_s7104_iso (isomorph of T3_playground_s6043) | 12 | 2 (0) | 6 | 0.628 | 0.307 | 20 | 0.041 | cat stalks bird, sprinkler package, cat sleeping, rake, bird perched, dog sleeping |
| T3_park_s7023 | 12 | 2 (1) | 5 | 0.645 | 0.324 | 22 | 0.030 | lost balloon, square wheel, fly kite, goat grazing, carry bag |
| T3_street_s15133 | 12 | 2 (0) | 5 | 0.642 | 0.372 | 20 | 0.051 | ice cream drop, about to trip, walk dog, carry box, bird perched |
| T3_street_s10104_iso (isomorph of T3_park_s7023) | 12 | 2 (1) | 5 | 0.647 | 0.321 | 20 | 0.053 | ball in tree, square wheel, ice cream, birds flying, run |
| T3_playground_s6043 | 12 | 2 (0) | 6 | 0.647 | 0.295 | 20 | 0.037 | dog begs, ball in tree, birds flying, dog sleeping, push stroller, photo |
| T4_garden_s552986 | 18 | 4 (2) | 9 | 0.565 | 0.212 | 29 | 0.052 | blocked hose, ball in tree, bucket hat, square wheel, birds flying, drink bench, paint fence, sweep, cat on fence |
| T4_garden_s18111_iso (isomorph of T4_playground_s487950) | 18 | 5 (2) | 9 | 0.567 | 0.230 | 27 | 0.047 | bird steals, about to trip, ball in tree, square wheel, dog reading, plant flowers, rake, cat on fence, jump |
| T4_park_s728923 | 18 | 5 (2) | 8 | 0.569 | 0.260 | 33 | 0.039 | ice cream drop, ducks bread, kite in tree, dog reading, pan watering, birds flying, goat grazing, sweep |
| T4_street_s430752 | 18 | 5 (2) | 9 | 0.571 | 0.233 | 26 | 0.060 | bird steals, about to trip, ball in tree, dog reading, square wheel, birds flying, sweep, jump, carry bag |
| T4_playground_s487950 | 18 | 5 (2) | 9 | 0.568 | 0.222 | 28 | 0.044 | bird steals, ball in tree, lost balloon, square wheel, dog reading, photo, walk dog, cat sleeping, run |

Isomorph pairs differ by at most 0.019 in content and 0.018 in inference completeness, with identical item signatures.

## How many pictures the generator can make

| Setting | Tier | Structures | Signatures | Largest isomorph pool | Scenes (order of magnitude) |
|---|---|---|---|---|---|
| garden | 1 | 2,167 | 9 | 1,671 | 10^10.0 |
| garden | 2 | 22,678 | 27 | 9,831 | 10^12.6 |
| garden | 3 | 1,980,031 | 296 | 255,371 | 10^18.5 |
| garden | 4 | 55,032,378 | 565 | 4,320,056 | 10^23.2 |
| park | 1 | 4,402 | 9 | 3,594 | 10^9.3 |
| park | 2 | 45,955 | 24 | 19,978 | 10^11.5 |
| park | 3 | 5,569,417 | 236 | 972,951 | 10^17.2 |
| park | 4 | 307,551,136 | 376 | 41,212,001 | 10^23.0 |
| street | 1 | 952 | 9 | 682 | 10^9.5 |
| street | 2 | 7,298 | 24 | 2,847 | 10^11.8 |
| street | 3 | 386,503 | 220 | 58,895 | 10^17.4 |
| street | 4 | 5,450,566 | 330 | 701,036 | 10^21.6 |
| playground | 1 | 1,700 | 11 | 1,150 | 10^9.6 |
| playground | 2 | 13,970 | 24 | 5,733 | 10^12.4 |
| playground | 3 | 738,151 | 183 | 110,468 | 10^17.6 |
| playground | 4 | 10,363,379 | 232 | 1,312,634 | 10^20.9 |

In all 387,170,683 structures over four settings. Structures are template sets that fit a tier's plan and can reach its content band, counted before placement.

## Key words, frequency and age of acquisition


Unchanged from v0.20: every item record carries its key word's Zipf frequency (f, for things and actions only) and its
age of acquisition (a, from the bundled excerpt of Kuperman, Stadthagen-Gonzalez and Brysbaert, 2012) at weight 0;
`scenegen/norms/aoa_kuperman2012.tsv` keeps the citation and source in its header and every record stores its sha256.
The licence note and what the pilot should test are in the v0.20 README section of the same name (the CC BY-NC-ND 3.0
question about shipping an excerpt; the model with AoA against the model without, pre-registered; AoA kept varying apart
from frequency when choosing the pilot's pictures). Before the pilot, check the bundled rows against the original file
(`python -m scenegen.difficulty --check-aoa <the original .xlsx or .csv>`).

## Folders

| Folder | What it holds |
|---|---|
| `assets/render_assets.py` | Renderer 0.4.0 (per-pose `hide` lists for swapped body parts; from v0.31 a pose name with `~near` or `~far` draws a figure in two pieces at its far leg, and from v0.32 `~body` and `~legs` at both legs, for the bench; from v0.46 a family's config can ask for a wider line round the figure's outer edge (`silhouette_px`), a line that takes no light (`unlit`) and cel tones of its own (`cel`)) |
| `assets/blender_run.py` | Lets the `bpy` scripts run with plain `python`, inside an installed Blender where the `bpy` module is missing |
| `assets/validate_assets.py` | Checks for every rendered variant; from v0.32 a piece of a split figure is checked by its base pose, and the manifest schema takes the `~` suffix; from v0.46 a record that carries its own cel tones is measured against those tones, and the schema takes the line's and the tones' new fields |
| `assets/cast/castlib/` | Cast library: `core.py`, `face.py`, `people.py`, `actions.py` (77 actions), `animals.py`, `specs.py`; v0.29 added the dogs' `sleep_paws`, `sleep_paws_turn` and `sit_wait` and the duck's `swim_eat` and `swim_look`, v0.30 draws nothing new, v0.31 widens the vest, v0.32 carries a box on the whole forearm, v0.33 draws nothing new, v0.34 gives the woman in yellow long hair (and, off, a dress across the lap seated), v0.35 draws nothing new, v0.36 draws the grandfather's moustache and sits the bucket higher, v0.37 and v0.38 draw nothing new in the cast, v0.39 redraws the cast: the seams where parts overlap, feet and ankles, the mid-section, the man in red's age, the quadrupeds' legs, paws and builds, and every animal at four angles, v0.40 redraws the reach for a blown hat, the hose held in two hands and the goat's graze, v0.41 folds the begging dog's forelegs, v0.42 redraws the goat, the dogs, the trousers' waist, the shoes and the woman in yellow's hair, v0.43 lays the reading dog down and redraws the dogs' legs, the goat's horns and beard and the two women's heads, v0.44 sits the reading dog up in reading glasses, redraws the cats' ears, the goat's beard and the dogs' noses, gives props colours of their own and redraws the run, the sand spade, the nozzle's inspection, the call from the seesaw and the content face, v0.45 enlarges the ice cream, redraws the camera, the shoes' soles, the trowel, the paint roller, the carried box and the kite's reel, turns the hose inspector's head to the viewer and hides the swimming duck's legs, and v0.46 draws the whole cast again: a heavier outer line and two flat tones, no added neck under the three smaller heads, higher necklines, fuller sleeves, no wrist seam, the vest's bands on the vest, a plain wire for the glasses, a smoother moustache and a line mouth on a dark line of its own |
| `assets/cast/gapcheck.py` | Finds body parts that come apart in any pose |
| `assets/cast/render_set.py` | Renders a list of variants |
| `assets/cast/out046/` | The 18 `.blend` families (builder 0.46.0), their render configs and `cast_catalog.json` |
| `assets/cast/lib046/` | Every variant the generated scenes and probes use, all rendered from `out046`: every person and every animal, nothing carried over |
| `assets/cast/gallery046/` | Gallery renders: every action the templates use, every animal pose, lineups, expressions (180, all pass the validator) |
| `scenegen/` | The generator (0.46.0, placement revision 43); `draw.py` holds the square wheel's three bench drawings (`SQUARE_STYLE20`), the barrow's two bench legs (`LEG23`), the riders' bench offsets (`RIDE24`), the bench values of `BARROW_SHADOW25`, `BIRD25` and `PAW25`, the swept heap's two drawings (`SWEEP26`) the bicycle's two wheels (`WHEEL27`), the fallen ice cream's three drawings (`SPLAT28`), the seesaw's inset (`SEESAW_IN28`) and its handle raised with a rider (`up`), the swing's three bench drawings (`SWING35`), the long box (`long_box`), the hose through its points (`hose_through`) and its end over a figure (`hose_tail`), the laundry basket's bundles drawn as cloth (`laundry_basket`, `cloth`) and a water drop (`drop`); `library.py` the shadow's two (`SHADOW28`), the sleeper's wider one (`SHADOW29`) and a figure turned about a point (`Placed.rot`, the child on a swung seat); `difficulty.py` (the item model, `zipf`, `aoa`); `norms/aoa_kuperman2012.tsv` (the AoA excerpt); `cairo_compat.py` (cairosvg on the pycairo wheel's cairo where the system has none); `reach.py` lists the poses the templates can ask for |
| `scenes/` | The v0.46 set: SVG, colour PNG, grayscale PNG, thumbnail and JSON record per picture |
| `probes/` | Probe pictures that put every template in front of the readers at least three times; screened, not part of the set |
| `site/` | The showcase page |
| `vision/` | The isolation bench (`isolation_bench.py`, `isolation_v012.md` to `isolation_v046.md` and their rounds; none in v0.21 or v0.37), flaw lists (`flaws_v04.md` to `flaws_v046.md`), the test-retest (`retest_v09.md`, `v09_retest/`), the design tests (`fork_tests_v08.md`, `design_tests_v09.md` to `design_tests_v046.md`), screen tools and prompts (`screen_prompts.md`, `remark_topics.py`), the keys, descriptions and scores of all forty-three screens, `screen_summary.json`, `gate.json` |
| `combos.json`, `calibration.json` | Combination counts; measured inference difficulty per template (also the planner's priors) |
| `garden/` | The v0.3 Garden prototype, kept for comparison |
| `RUNBOOK.md`, `tools/` | How each release is made, step by step, and the scripts that set up, build, search, verify, prune and screen a release |
| `requirements.txt`, `.gitignore`, `.gitattributes` | The Python packages (Pillow pinned, as it changes every embedded asset) and the repository's settings |

## How to run

```bash
python -m venv .venv && source tools/env.sh      # from Git Bash on Windows too
pip install -r requirements.txt                  # the cast needs Blender 5.2.3 LTS: installed, or pip install bpy==5.2.3 on Python 3.13

python assets/cast/build_cast.py assets/cast/out046                 # build the cast (under a minute)
cd assets/cast && python gapcheck.py out046 person.kai && cd ../..  # check one character's poses for parts that come apart
python -m scenegen.generate --tier 3 --setting playground --seed 7 --out scenes
python -m scenegen.generate --from-record scenes/T3_park_s7023.json --out tpdb_work/check   # exact rebuild
python -m scenegen.reach --out reach.json                          # the poses the templates can ask for

python -m scenegen.batch showcase --out scenes
python -m scenegen.calibrate --out calibration.json
python -m scenegen.difficulty --check-aoa <the original Kuperman et al. file>   # compare the bundled AoA rows
python -m scenegen.combos --out combos.json
BENCH_CAST=<a cast built with TPDB_PROFILE=0> python vision/isolation_bench.py tpdb_work/bench proO_1 proO_2   # one template alone, cropped
python vision/prepare_screen.py scenes,probes vision/v046   # then describe and score: vision/screen_prompts.md
bash tools/cycle/summarize.sh                               # add the screen to vision/screen_summary.json
python vision/gate.py vision/v046 scenes,probes
python -m scenegen.site --scenes scenes --gallery assets/cast/gallery046 --old-gallery <v0.45 renders of the same variants> \
    --combos combos.json --screen vision/screen_summary.json --out site
python3 package_release.py 0.46 --single   # the release as one zip, tpdb_v0.46.zip
```

The release is one zip, `tpdb_v0.46.zip`, about 265 MB. Google Drive does not virus-scan a file over 100 MB, so it asks to confirm the download ("can't scan this file for viruses"); the file downloads as normal after that. `package_release.py` checks, file by file, that the zip holds every file of the release. Without `--single` it writes the same release as zip parts under 50 MB each, with the README and the set's pictures beside them, for browsing in Drive.

Exact rebuilds hold within a release: a v0.45 record rebuilds with the v0.45 package. They also depend on Pillow, pinned in `requirements.txt`: Pillow 13 resamples RGBA differently from 12, and every embedded asset changes. A different cairo moves a few pixels by one level and leaves the SVG identical. Renders from an installed Blender differ from the Linux module's only in sub-pixel anti-aliasing on the outlines, with identical anchors and geometry, so the library mixes the two.

## Known limits

- The weights are still the spec's starting values: every predicted completeness is a placeholder
  until the pilot fit.
- The blind screen used AI readers. It is a filter for illegible drawing; the pilot with people
  remains the test of difficulty.
- Four templates fall under the legibility gate after the v0.46 screen, where v0.45 had none: `dog_reading` (0.87, 5 pictures), `about_to_trip` (0.89, 3 pictures) and
  `sweep_fork` (0.89, 3 pictures), each on one misread, and `blocked_hose` (0.89, 7 pictures), on one reader's hedges in three pictures. In one picture each the dog was
  "holding a newspaper in its mouth", the walker was read as heading away from his obstacle ("The box is behind him, so he is not about to trip on it."), and the fork
  sweeper, his heap at the path's edge and the dustpan on the grass, was "digging into the ground". v0.46 changed the cast's drawing (a heavier outer line, two flat
  tones, shorter necks) and no placement rule. None of the four was mended after the screen and no picture was swapped or read again, so the count is the first and only
  one. Whether the heavier line cost the dog and the walker their readings cannot be told from one screen: each lost a reading in an earlier screen too (the walker
  in v0.42, the dog in v0.45's first count), and with every figure drawn anew there is no retest. The other 60 pass, the lowest `lost_balloon` and `water_upward` (0.94, 3 pictures each) and `bird_steals`
  (0.97, 6 pictures). Of the 22 (template, angle) pairs placed, 20 pass on their own in two or more pictures: the stopped hose's dog is at 0.88 in profile and 0.83 at 45.
  Read strictly, the full marks the scorers themselves called hedged take two more under the gate, `lost_balloon` and `water_upward` (`vision/flaws_v046.md`, which lists
  the oddities for v0.47, first among them the reading dog).
- A single half mark is noise. 19 pictures were identical to the pixel in v0.29 and v0.30, and 223 of their 230 items scored the same across fresh readers and scorers, with four templates moving by a half mark and no picture changed (`vision/flaws_v030.md`, A retest nobody planned). In v0.31, 12 pictures came back identical once more, and 137 of their 141 items scored the same; the one that went down is the gate's one failure. In v0.32, 19 came back identical, and 242 of their 246 items scored the same; the four that went down are again the gate's one failure, and a begging dog's half mark. In v0.33, 21 came back identical, and 274 of their 281 items scored the same, three moving up and four down. In v0.34, 26 came back identical, and 296 of their 299 items scored the same, two moving up and one down. In v0.35, 78 came back identical, and 806 of their 830 items scored the same, 7 moving up and 17 down, 12 of the 17 the clouds of two readers who named nothing in the sky. In v0.36, 60 came back identical, and 563 of their 576 items scored the same, 12 moving up, every one those clouds, and one down. In v0.37, 75 came back identical, and 775 of their 783 items scored the same, three moving up and five down, one of the five the gate's one failure. In v0.38, 22 came back identical, and 291 of their 294 items scored the same, three moving up and none down. With v0.39's cast redrawn none could; on the 7 pictures with the same seed and events in both screens, each in its own cast, all 75 items scored the same. In v0.40, 28 came back identical, and 326 of their 328 items scored the same, two moving up and none down, both on templates of v0.39's list. In v0.41, 43 came back identical, and 523 of their 532 items scored the same, three moving up and six down, three of the nine the clouds. In v0.42 none could: every person, dog and goat was drawn anew. Nor in v0.43, with both dogs, the goat and the two women redrawn, nor in v0.44, with every dog, cat, goat and person redrawn, nor in v0.45, with every person and the duck redrawn, nor in v0.46, with every person and animal drawn again in a heavier line and flat tones. In v0.45 three pictures were read twice, before and after the reading dog's paper moved: of the 66 items the change did not touch, 64 scored the same and two went down by a half mark, the thief bird's (above). A template with few items can cross the gate on that alone: `read_bench` and `hang_laundry` have one item to a picture.
- What the trip's long box costs a fresh tier-4 search is as v0.29 found it, 166 failed seeds against 80. In v0.32 the garden, park and playground cells came back on their seeds; the street's did not under revision 30, in 39 seeds, and placed at once with v0.31's template set forced. In v0.33 all four came back unchanged, the street's on the same forced set, and in v0.34 to v0.38 all four came back on their seeds again, identical to the pixel in v0.37 and v0.38. With v0.39's redrawn cast the garden and park came back on their seeds and the street on its forced set; the playground's seed and the next 39 placed nothing, and the 41st did. In v0.40 all four placed again on v0.39's seeds and layouts, and in v0.41 all four came back identical to the pixel. With v0.42's redrawn cast the park placed on its seed and layout and the street on its forced set; the garden took three seeds and the playground forty. In v0.43 the park, the playground and the street placed on v0.42's seeds and layouts, and the garden on the fourth seed of its search. In v0.44 the park and the playground placed on v0.43's seeds with the same templates, the street on its forced set with the square wheel for the upward water (which revision 42 keeps out of the street), and the garden on a new seed list after v0.43's seed and 44 more placed nothing. In v0.45 the garden, the park and the street placed on v0.44's seeds with the same templates; so did the playground, until the lost balloon's prior moved after the set was built, and then its seed and the next 14 placed nothing, and the 16th did. With v0.46's redrawn cast the park placed on its seed and the street on its forced set, both with v0.45's templates; the garden's seed and the next two placed nothing, and the fourth did; the playground's seed and six more placed nothing before one did.
- The oddities come in two rows. Readers' remarks per picture are counted directly from their descriptions and compare across
  screens, with the caveat that current readers write about 18% more than the v0.23 readers on the same pictures (`vision/v024/control/`,
  one reader and eight pictures). The row was recounted in v0.26, as the counter had taken bullets saying nothing is wrong for remarks, so its
  figures differ from those published up to v0.25. The scorers' logged oddities do not compare: v0.23's logged 25% of the remarks, v0.24's 83%, and
  from v0.25 the prompt caps them at three per picture. Earlier screens did not record which model read them; v0.24's to v0.46's ran on Claude Opus 5.5. Readers differ widely: on v0.28's nine, from 4.25 to 6.38 remarks a picture, on v0.29's from 4.50 to 5.75, and on v0.30's from 4.50 to 6.12. v0.31's nine wrote from 2.62 to 4.43, every one fewer than the fewest of v0.30's, and on 12 pictures identical in both screens remarks fell from 65 to 45. So a screen's readers can move the row by a third, and its fall to 3.51 in v0.31 says nothing about the drawings. v0.32's nine wrote from 2.71 to 4.43, 3.28 a picture, and on 19 pictures identical in both screens remarks fell from 79 to 67. v0.33's nine wrote from 2.44 to 4.11, 3.19 a picture, and on 21 identical pictures remarks rose from 77 to 88. v0.34's nine wrote from 2.40 to 4.50, 3.13 a picture, and on 26 identical pictures remarks were 96 in both. v0.35's nine wrote from 2.44 to 3.50, 2.88 a picture, and on 78 identical pictures remarks fell from 243 to 222. v0.36's nine wrote from 2.33 to 3.89, 3.10 a picture, and on 60 identical pictures remarks rose from 163 to 175. v0.37's nine wrote from 1.89 to 4.44, 2.82 a picture, and on 75 identical pictures remarks fell from 226 to 209. v0.38's nine wrote from 2.22 to 4.25, 3.38 a picture, and on 22 identical pictures remarks rose from 73 to 94. v0.39's twelve, eight pictures each, wrote from 2.62 to 4.00, 3.10 a picture, and on 7 pictures of the same events in both screens remarks fell from 28 to 25. v0.40's twelve wrote from 2.62 to 3.62, 3.04 a picture, and on 28 identical pictures remarks fell from 106 to 93. v0.41's twelve wrote from 2.25 to 3.88, 3.17 a picture, and on 43 identical pictures remarks rose from 151 to 156. v0.42's twelve wrote from 2.25 to 4.00, 3.05 a picture over all 93 screened, v0.43's twelve from 2.50 to 4.12, 3.12 a picture over 94, v0.44's eleven from 2.29 to 3.86, 3.27 a picture over 82, v0.45's twelve from 1.88 to 3.50, 2.58 a picture over 93, and v0.46's thirteen from 1.71 to 3.12, 2.38 a picture over 98, the fewest of any screen.
- No reader says "teenager": he is read as a boy, a boy or young man, or a person, which the key mostly accepts. The v0.24 redraw moved him
  from a woman to a boy, and v0.26's cap worn forwards moved him no further toward the key's own word. It read once as "worn backward or sideways" in v0.27.
- The retest of the v0.9 pictures (`vision/retest_v09.md`) put the gate's reader variance at about five
  templates between screens. A template with one to three items per picture fails on a single picture
  where something next to it pulls the reading away: the gate is a filter, not a measurement.
- Scores are near the ceiling: across 98 pictures 1035 of 1063 scored items had full marks, sixteen of the 28 others the clouds or a tree that six readers left out
  (992 of 1009 in v0.45, twelve of the 17 others the clouds or a tree that two readers left out; 920 of 927 in v0.44, four of the seven others the girl in pink's ice cream; 977 of 1003 in
  v0.43, ten of the 26 others the clouds of two readers who wrote "sunny" and ten the reading dog's; 1010 of 1020 in v0.42; 999 of 1008 in v0.41, five of the nine others the clouds of one reader; 1011 of 1014 in v0.40, 1025 of 1030 in v0.39, 841 of 842 in v0.38, 870 of 876 in v0.37, 873 of 876 in v0.36, and 855 of 877 in v0.35, 17 of
  whose 22 others were the clouds of two readers who named nothing in the sky). AI readers describe
  exhaustively, so the screen cannot rank templates by difficulty; that is the pilot's job.
- Scorers differ on hedges: some give full marks when the description commits to the key's reading and
  only the "unsure" section offers another, some give a half point. The prompt allows both; two v0.17 scorers
  counted 6 and 13 such items they credited in full, a v0.18 scorer listed seven judgment calls, a v0.19 scorer six,
  a v0.20 scorer seven, a v0.21 scorer nine, v0.22 scorers two, eight and nine, v0.23 scorers six to twelve, a v0.24 scorer eleven, and all three scorers of v0.25 to v0.38 listed such calls, enough to move a template across the gate. A v0.29 scorer listed 18 items that hold full marks because the free description committed and only the unsure section hedged, and a v0.30 scorer gave nothing under full marks in 302 and listed 22 it thought a stricter scorer might halve. Two v0.31 scorers gave nothing under full marks, in 236 and 253 items, among them a bird "about to take it" credited as pecking. v0.32's three gave one, three and three items under full marks, in 244, 288 and 244, v0.33's four, one and three, in 301, 255 and 306, v0.34's one, none and ten, in 314, 282 and 289, where the second listed four inferences a stricter scorer might halve, v0.35's twelve, one and nine, in 304, 283 and 290, v0.36's none, two and one, in 304, 283 and 289, where the first listed eight hedged inferences it credited in full, v0.37's four, one and one, in 304, 283 and 289, where the second listed seven items it credited in full on a committed free description, and two birds seen standing, not pecking, and v0.38's none, none and one, in 298, 268 and 276, where the first listed eleven items it credited in full though the reader gave a second reading, and the second twelve more. Halved, those 23 would take six templates under the gate; 11 of them are on pictures identical to v0.37's, whose scorers had credited all 11 in full (`vision/flaws_v038.md`). v0.39's four (for 96 pictures) gave two, two, none and one, in 282, 246, 269 and 233, where two listed 11 items they credited in full on a committed free description; halved, those would take one template under the gate (`vision/flaws_v039.md`). v0.40's four, and a fifth for one picture read again, gave one, one, one, none and none, in 228, 270, 260, 241 and 15, and listed 21 items they credited in full on a committed free description; halved, those would take five templates under the gate (`vision/flaws_v040.md`). v0.41's four gave one, two, five and one, in 255, 263, 253 and 237, the five the clouds of one reader, and their notes mark 16 items they credited in full on a committed free description; halved, those would take two templates under the gate (`vision/flaws_v041.md`). v0.42's four gave none, three, five and one, in 225, 270, 237 and 250 (scorer a's old picture 10 left out, read again with one of 25 under), and their notes mark 10 items they credited in full on a committed free description; halved, those would take two more templates under the gate (`vision/flaws_v042.md`). v0.43's four gave two, five, twelve and seven, in 231, 284, 262 and 226, and their notes mark seven; halved, those take none under the gate (`vision/flaws_v043.md`). v0.44's four gave one, three, three and none, in 250, 225, 232 and 220, three more one each on three pictures read again after the screen, and their notes mark seven; halved, those take none under the gate (`vision/flaws_v044.md`). v0.45's four gave ten, four, one and two, in 260, 262, 238 and 249, three more none, two and none on three pictures read again after the screen, and their notes mark nine; halved, those take none under the gate (`vision/flaws_v045.md`). v0.46's four gave five, seven, four and twelve, in 286, 253, 266 and 258, ten of the twelve in one reader's seven pictures, and their notes mark eleven; halved, those take two more templates under the gate (`vision/flaws_v046.md`). A misread is a call too: the
  rake in v0.26's picture 37 could have been marked as sweeping half right.
- Tier-4 pictures are the hardest to place, and revisions 14 to 26 make them harder (walkers' and runners' lanes, pointing
  lines, feet off benches and off other events' things, the photographer's line of sight, the waver's clear hand, body gaps, the gap
  from thin parts, heads clear of figures up to 80 px apart in depth, the ground clear past a reading walker's obstacle, jumpers in the
  front half, an obstacle a full step ahead, runners clear of other movers, ducks off a float, sleepers clear of walkers' feet, nobody in
  the strip before the horizon, a person's box off the lamp post, the ground kept clear round a begging dog). A tier-4 playground plan now holds the bird stealing a sandwich and the
  square wheel, has no swing set as scenery and counts the railing up to 30% hidden, each of which alone placed nothing from 12 seeds, where all three placed 2 (`vision/flaws_v028.md`). So every tier-4 playground has those two, and none
  has the begging dog. A tier-4 street plan holds the bird too, on the evidence of one picture. A picture that also holds a floating, carried or soaked box falls back to the bucket from the long box, and none of the eleven screened pictures of the trip did.
- The square-wheeled bicycle still stands on its own: four stands have been tried on the bench, and each
  read as something else (pedals, legs) or not at all.
- The low kick's direction is ambiguous when the kicker's hair hides the face; the teenager kicks first,
  and the kick read in full in all its screened pictures. His cap now points the way he faces, but two readers still took it for sideways or backwards.
- The stuck girl on the seesaw always calls out, and from v0.33 no kick arcs are drawn at her feet: the tilt, the man's weight, her open mouth and
  the raised handle carry the reading, and in the v0.33 and v0.34 screens she was stuck in all three of her pictures.
- The body check (`assets/cast/gapcheck.py`) finds parts that come apart, not parts that pass through one
  another: a hand inside a hip or a lobe of skirt inside the bell is allowed, and only the outline drawn
  in the render shows whether the join looks right.
- The wind reaches the hat, the washing, an empty swing, the tree and the sky, but not hair or clothes, nor the
  bushes and flowers (three v0.19 probe readers noticed): the cast is posed and rendered in 3D, and a blowing
  fringe or skirt would be a new rig. From revision 32 no can, pan, hose or sprinkler pours in a windy picture, and from revision 33 no pile is
  swept or raked in one (in v0.34 one lay still: "yet the woman's pile of leaves stays neatly in place").
- The isolation bench reads one template cut out of its picture. A visual that reads alone can still be
  misread among other events, so the bench comes before the test scenes and the screen, never instead of them.
- The planner's priors come from the v0.46 calibration, with f = 0 and a at its centre for every inference and contradiction, as in
  v0.20 to v0.45. 44 fields moved by 0.002 or more, on the cast's new drawing alone, most of all `cat_stalks_bird`'s inference (s from -0.57 to -0.52) (26 in v0.45, most of all `lost_balloon`'s inference, the string's end lifted above the reaching hand; 24 in v0.44, most of all `lost_balloon`'s inference, the balloon high on its long string; 42 in v0.43, most of all `dog_reading`'s contradiction, the dog lying down; 34 in v0.42, with the cast redrawn). The ladder's still rests on one sampled placement, since v0.29's lamp rule.
- Exact rebuilds hold within a release, on the pinned Pillow: v0.46 keeps the v0.45 placement rules (revision 43), which end the lost balloon's string 62 to 80 px above the reaching hand,
  in a slow wave with no curl, off a playground's railing and above a garden fence's pickets; begin the wet paint below the roller, the painter close enough for the roller
  to lie on the boards; kneel the planter at the bed's end with a hole under the trowel's point; stand the picnic's loaf and bottle out of the basket beside a plate; keep the
  goat's stake clear of every standing structure; cut a swimming animal at a waterline; draw the slide's ladder as the frame's own end and a tuft of grass at the bird table's
  foot; and lay the reading dog's paper on its paws. Each rule's v0.44 form is kept behind its switch (`BAL45`, `PAINT45`, `PLANT45`, `PICNIC45`, `TETHER45`, `RAIL45`,
  `CURL45`, `WOOD45` and `READ45` in `templates.py`, `library.SWIM45`, `settings.SLIDE45`, `settings.FOOT45`). A v0.45 record rebuilds with the v0.45 package: v0.46's rules are the same, and no render of its cast is. Revisions 31 to 43 keep their rules in the templates'
  placement and binding, the planner's features and plans, the setting or `fits`, each behind its revision; revision 30's sky rule is still read at import (`RUNBOOK.md`).
- Every variant comes from the v0.46 cast (builder 0.46.0, `out046`), which draws every person and every animal again: an outer line as heavy as the settings' own with thinner lines inside it, and two flat tones for v0.45's three soft ones; on the people, no added neck under the three smaller heads, higher necklines, fuller sleeves, a plain wire for the glasses, a smoother moustache and a mouth drawn as a line. No render carried over from `lib045`, and the seesaw's riders are in two pieces each, as before. The library keeps only the 400 variants the v0.46 set and probes use. The bench
  variants (`TPDB_PROFILE`, `TPDB_FOOT`, `TPDB_BROOM`, `TPDB_ICE`, `TPDB_BOOK`, `TPDB_MOUTH`, `TPDB_BODY`, `TPDB_PECK`, `TPDB_DRESS`, `TPDB_NOZ`, `TPDB_BEARD`, `TPDB_BROW`, `TPDB_BLUSH`, `draw.WHEEL27`, `draw.SPLAT28`, `draw.SEESAW_IN28`, `draw.SWING35`, `library.SHADOW28`, `library.SHADOW29`, and `SLEEP29`, `TRIP29`, `TRIP_OBJ29`, `DUCK29`, `DOOR29`, `HOSE29`, `BULGE29`, `FISH29`, `LADDER_LAMP29`, `HOSE30`, `FISH30`, `TRIP_W30`, `TRIP_LANE30`, `CRUMB30`, `SEESAW31`, `RIDE31`, `CASTLE31`, `LIMB31`, `LOW32`, `LOW_IN32`, `LOW_RISE32`, `LOW_RISE_B32`, `STUCK32`, `HANDLE32`, `HOSE33`, `KICK33` and `BASKET38` in `templates.py`, `REEL30` and `REEL31` in `settings.py`, and `TPDB_VEST`, `TPDB_CONE`, `TPDB_BOX`, `TPDB_LOW`, `TPDB_SEAT34`, `TPDB_HAIR34`, `TPDB_MOUSTACHE36`, `TPDB_MOUSTACHE36_FLAT`, `TPDB_BUCKET36`, `TPDB_ISECT39`, `TPDB_SHOE39`, `TPDB_KNEE39`, `TPDB_MID39`, `TPDB_BELT39`, `TPDB_BEN39`, `TPDB_QUAD39`, `TPDB_ART39`, `TPDB_GOAT39`, `TPDB_REACH40`, `TPDB_HOSE40`, `TPDB_GRAZE40`, `TPDB_WALK40`, `TPDB_BEG41`, `TPDB_STALK41`, `TPDB_MEI41`, `TPDB_GOAT42`, `TPDB_DOG42`, `TPDB_BEG42`, `TPDB_CAT42`, `TPDB_MID42`, `TPDB_BELT42`, `TPDB_FOOT42`, `TPDB_MEI42`, `TPDB_DOG43`, `TPDB_GOAT43`, `TPDB_READ43`, `TPDB_ADULT43`, `TPDB_READ44`, `TPDB_CAT44`, `TPDB_GOAT44`, `TPDB_NOSE44`, `TPDB_PROP44`, `TPDB_RUN44`, `TPDB_THROW44`, `TPDB_SPADE44`, `TPDB_INSPECT44`, `TPDB_CALL44`, `TPDB_CONTENT44`, `TPDB_ICE45`, `TPDB_CAM45`, `TPDB_SOLE45`, `TPDB_HOSE45`, `TPDB_TROWEL45`, `TPDB_PAINT45`, `TPDB_BOX45`, `TPDB_KITE45`, `TPDB_DUCK45`, `TPDB_STYLE46`, `TPDB_NECK46`, `TPDB_ARM46`, `TPDB_MEI46`, `TPDB_CLEAN46`, `TPDB_COLLAR46`, `TPDB_GLASSW46`, `TPDB_MOUSTACHE46`, `TPDB_SHADE46`, `TPDB_INK46` and `TPDB_MOUTH46` in the cast, and `YAW39`, `TUFT40`, `ICE40`, `BOX41`, `SEASON41`, `GOAT42`, `BIRD42`, `KINK42`, `BEG40`, `TRIP43`, `READ43`, `HOSE43`, `CAT43`, `BEGX43`, `TETHER43`, `READ44`, `READ44T`, `LEAD44`, `GOAT44`, `CAT44`, `BAL44`, `BAL45`, `PAINT45`, `PLANT45`, `PICNIC45`, `TETHER45`, `RAIL45`, `CURL45`, `WOOD45` and `READ45` in `templates.py`, `SWIM45` in `library.py`, `SLIDE45` and `FOOT45` in `settings.py` and `HEAP39`, `HEAP40`, `WATER44` and `WHEEL44` in `draw.py`) stay in the code.
- The new line and shading were chosen on the bench, in whole pictures and in figure pairs (`vision/isolation_v046.md`: beside v0.45's, the better drawn in six pairs of eight and the nearer to the background's drawing in seven). The screen asks what is in a picture and not how it is drawn, so it can show that a drawing harmed a reading and little about whether it is the better drawing. No reader of the 98 pictures remarked on an outline, a neck or a mouth, which is weak evidence that they are right. The woman in the yellow dress, whose neck v0.46 shortened, is a woman in 29 descriptions of 30 and a girl in one.
- Two things the new drawing made worse are on the v0.47 list. The moustache, smoothed and rounded at its ends, was to two readers a mark that "could also be a smear of something (for example chocolate) on his face" and "looks a little like a smudge", and four of the eleven descriptions of its wearer name a moustache. The shadow tone's hard edge across a dress was once "her arm drawn faintly through her body", and on the bench "a fold or stain" on a lap.
- The validator's soft palette warning is raised by 154 of the library's 400 records (83 of 382 in v0.45). What is off the palette is the blended band where the heavier line meets a fill, which grows with the line and is largest on small figures; the target was not loosened.
- The figures are still narrow. Legs an eighth shorter and limbs 14% thicker took the bench from eight remarks to three, on four cut-outs a side, but the screen's remarks on
  thin or long bodies did not fall (six pictures to eight in v0.27, to thirteen in v0.28 and v0.29, and back to six in v0.30, with nothing changed, and one each in v0.31 and v0.32, with readers who remark less; by keyword, so that row says little). A real change of build is a larger job than these.
- A person in full profile has the head turned 35 degrees to the viewer, baked as a twin action of the pose (`__p`), except where a hand-held thing at the face would be left behind
  (`PROFILE_SKIP`). Those poses keep the hidden face readers remark on.
- Age of acquisition is recorded at weight 0, so it moves nothing until the pilot's pre-registered test says it
  should. The bundled ratings are a verbatim excerpt of Kuperman et al. (2012) under CC BY-NC-ND 3.0, taken from a
  copy in the lftk package; they have not yet been checked against the original file at crr.ugent.be.
- Key words follow one rule (the word the first accepted answer names: an action's verb, or the thing that names
  it), applied by hand in v0.20 and unchanged since; a key that is itself an accepted answer was left alone.
- The sleeping cat, 1.4 times its v0.17 size, read as "small" in one v0.18 probe and drew no remark in its four
  v0.19 pictures; drawn larger, the standing and stalking cats would come out as big as the small white dog.
- Twenty-seven actions in the cast are used by no template; they are kept for later templates and left
  out of the gallery and the screen, so they have never been read blind.
- Edge density is not part of the isomorph rule. Street pictures stay the busiest, so a street
  isomorph of a park or playground picture carries more visual detail at the same object count.
- The top third of park and playground pictures is still mostly sky.
- A filler closer than 24 px to the picture's side edge is now moved 30 px inside it, and no reader said one
  was cut off; the sun can still sit partly off the top edge, where the backdrop draws it.
- The strip before the horizon leaves the playground less room: the tier-3 playground placed only without template-variety steering in
  v0.24 and v0.25, and with it from v0.26. The v0.44 isomorphs were new, the second of tier 2 a park drawn from the tier-2 street, as the park's own drifted in inference and the garden's dog by the door has no isomorph outside gardens. v0.45's pair the same five cells, the tier-2 park and the tier-4 garden on v0.44's seeds with v0.44's templates and the other three on new seeds. v0.46's are five again and not the same five: tier 2's two pairs are v0.45's the other way round (a playground drawn from the garden, a street from the park), tier 3 keeps a street drawn from the park and has a garden drawn from the playground, as the tier-3 street's dropped ice cream placed in neither the park nor the playground, and tier 4's is a garden drawn from the playground. The tier-3 playground itself placed in v0.43 to v0.45 only on a fresh seed list without template-variety steering, after the showcase pass and its search failed 13 base seeds, and in v0.46 in the showcase pass, on its base seed's eighth try; an animal whose template its partner shares is drawn at the
  partner's angle (revision 37), a constraint `calibrate.py` has not yet tested for difficulty.
- The strip applies to the park and the playground, not the street, where the back row stands at the shop fronts: one design-test
  reader still found a woman there "large compared with the door".
- A shadow from the figure's own footprint is smaller, and a body lying down has little of it showing. The sleeping dog now reads in full on its new pose and that shadow; a wider one did little on the bench, so whether the shadow cost it marks in v0.28 is still not shown.
- The trip reads in full on the long box, in eleven pictures in v0.30 and five each in v0.31 to v0.41. In v0.42 it read in two of three: the third reader, a reading dog beside the walker, saw the box and no trip. From v0.43 the reading dog is kept away from it (revision 41), and it read in all five of its pictures, in v0.44 as well, and in all three in v0.45. In v0.46 it read in two of three and failed the gate on the third, a misread: the walker, a bird table's post right behind his back, was read as heading away from the box ("The box is behind him, so he is not about to trip on it."). In v0.30, five of its readers also said the walker may step round it, which on the same five pictures went from four of five to one of five with nothing changed.
- The man on the seesaw's low end is drawn astride, his far leg behind the plank. The v0.32 bench turned him away, or put both legs behind the plank, and readers of each still doubted his seat (legs out was set aside on looking);
  in the v0.32 screen he drew one remark in three pictures, that "the seesaw plank seems to pass behind or among the old man's legs". He is off the list; in v0.33 his legs over the plank drew a remark once more. The stuck girl holds a handle raised with her,
  and once a reader saw her hover, from the kick arcs under her feet, which v0.33 does not draw.
- A rider on the seesaw is two pictures, the far leg drawn behind the plank as background and the rest of the figure in front. The far leg is in no count, mask or check of the scene's own.
  Until v0.32 the validator failed the 12 pieces on their names; it now checks each by its base pose and leaves the ground rule to the piece with the body.
- The child on the swing is swung out 12 degrees (revision 33), turned in the picture with its seat and ropes, not posed so in the cast. The frame is widened on the
  side away from the path when a child swings, so its legs stay off the path, and an empty seat keeps the frame it had. One v0.35 reader found the ropes not quite
  "directly above the seat", and read the child as swinging.
- The gate's knob is kept 16 px clear of every figure's drawing, hair, hands and props included (revision 35; revision 34's box round the face missed the back of a
  head in profile). The sweeper it was for now stands lower on the path, and was "a boy with short dark hair". A storm pointer's garden has no clothesline
  (revision 35): with the washing off it (revision 34) the empty line was offered as what she pointed at, and the planner had long noted that an empty line reads
  as a bare wire. Her readers still offer the tree or the roof as a second reading. From revision 36 no cat walks the fence in her picture (one storm pointer was offered
  the cat on the fence in three screens running) and the stalking cat stays on the ground, and in the garden no bird perches up high either; the three v0.38 storm pointers
  read at the clouds. The bird is dropped from the plan in the garden only: dropped in every setting, it changed a playground cell whose picture has neither, as an earlier try of its seed drew the pair.
- The broom's and the rake's heaps have been drawn three ways, and each drew a remark on the season: v0.38's autumn leaves "under green trees" (seven pictures),
  v0.39's summer heap, whose green leaves were "a little odd for raked fallen leaves" (five), and v0.40's dry leaves, leaf-shaped (`draw.HEAP40` "D"), "The brown leaves
  are slightly odd when the trees are green" (five pictures, from three readers). Cut grass read as a dome or dustpan on the bench, and grit as dust or a rock.
  In v0.41, the heap unchanged, no reader remarked on the season in 93 pictures; trees turning over the heap read as fruit on the bench (`vision/isolation_v041.md`).
- Animals are drawn at 45 or 135 as well as 90 for eight templates (revision 37), and the songbirds and the duck at 45 for four more (revision 40); the stalking cat is drawn in profile only from revision 41, its legs tangled at 45 and at 135, and the grazing goat not at 135 from revision 42; people are not. The dog walked on a lead is drawn at 90 only: at 45 its lead
  crossed its back at every spot tried, which revision 12 forbids. Every (template, angle) placed read at 1.00 in two or more pictures in v0.39, and at 0.94 or more in v0.40 to v0.42 and 1.00 in v0.43, the four bird templates at 45 too; in v0.44 all 24 passed, in v0.45 21 of 22, the thief bird in profile at 0.89 after one of its pictures was read again, and in v0.46 20 of 22, the stopped hose's dog at 0.88 in profile and 0.83 at 45 on one reader's hedges,
  and the scorers' oddities by angle were about the goat out of place, the begging dog's upright pose in profile and the stalking cat's legs at 45, not about an
  angle as such.
- The begging dog's forelegs are folded from v0.41, the elbows forward and the paws tipped down at the chest: held out level, they were "stiff rods" to the bench's readers
  (`vision/isolation_v041.md`). From v0.42 it sits on its haunches with a shorter trunk, and no screen reader saw it kneel; once it was "jumping up". Nobody else with an
  ice cream comes near it (revision 40), and in both v0.42 pictures with another eater in view the reader gave the one on the bench. From v0.43 its mouth is closed;
  a head lowered to look at the eater rather than the sky did not place at 45, where the gaze check found it facing the viewer (`vision/isolation_v043.md`).
- The goat is tethered when it grazes, a rope from its collar to a peg (revision 40): out of place twice in v0.42, both softened ("a little unusual, but it is tethered
  and calm"), where it was seven times in v0.41. From v0.43 its rope is slack and it is never drawn untethered or on the stopped hose; unusual in four of six
  pictures, and twice, from behind, possibly a sheep. From v0.44 it grazes in the park only: tethered in all four pictures, "a little unusual" in all four, never a sheep. In v0.45, its stake clear of every standing structure (revision 43), it is tethered in all four pictures again and "unusual" in two. In v0.46 it is tethered in all five of its pictures and "a little unusual" in two, and in one of those the reader added "It could possibly be read as a white sheep or a young goat (kid)." The reading dog sat with its hind legs folded
  in v0.42, and its paper "stands upright on its own" in three descriptions; v0.43 laid it down over the paper, which read as lying on it; v0.44 sits it up again in
  reading glasses, its paper hung from its raised paws and tilted, and it read as reading in all five of its pictures, its paper twice "floating" beside it. In v0.45, the paper as it was, it failed the gate's first count on a paper "up in the air" in one picture of three; with the paper drawn onto the paws after the screen it read as reading in all three, and two of the three readers offered beside it that the dog might only be holding the paper ("could simply be holding/carrying the paper"). In v0.46, the pose and the paper as they were and the line heavier, it failed the gate: it read as reading in four pictures of five, and in the fifth it was "holding a newspaper in its mouth", its forepaws and the paper's corner over the muzzle.
- A reader can describe the wrong picture. v0.40's reader 7 described picture 56 under picture 55's name, and wrote of picture 56 that it "couldn't find any difference between this
  picture and pic_55"; the files were distinct and right. Picture 55 was read again by a fresh reader and scored by a fresh scorer, and reader 7's description is kept aside
  (`vision/flaws_v040.md`). A scorer who finds a description that does not fit its key, as this one did, is the check.
- The washing's hanger is read hanging it out from the basket at her feet and the drops, not from the pose: on the bench, with neither, three readers of three could
  not tell up from down, and some design-test readers still said the pose alone could go either way (none of v0.38's three did, and of v0.39's five, one raised taking it down and settled it on the drips and the basket). All the washing drips, the jeans and the sleeve over the basket's rim too: with
  the shirt alone wet, a design test read the basket's clothes as dry and "about to get wet". The washing and a watering can placed 0 of 12 together, with the
  basket or without it.
- The cast is a stand-in. Final character art would replace the models; rigs, poses, faces,
  anchors and manifests carry over.
