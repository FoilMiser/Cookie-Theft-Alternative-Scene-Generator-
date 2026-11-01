# The v0.14 changes, read blind in whole test scenes

After the isolation bench (`isolation_v014.md`) each refined visual went back into whole scenes, with the
other events around it, and was read blind there before the set was regenerated, as v0.8 to v0.13 did.
Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v014/`; `map.txt` names the
scene behind each picture.

## Round 1: the refined visuals among the other events

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (street) | Stalking cat among passers-by, waving, walking a dog | The cat "crouches low, facing the bird, as if it is about to sneak up on it or pounce", with room round it. But the dog walked toward it from across the street: "the dog is facing left toward the cat and bird, so it might be about to lunge or chase"; and round the waving woman's hand "a faint thin circle or ring ... a motion line ... or a small transparent object such as a bubble" |
| `test_2.png` (playground) | The heavy man on the seesaw, a waving teenager, the slide | "Because the heavy reader keeps his end down and isn't paying attention, she looks stuck up in the air". The waving hand again: "waving, or holding up a small green round object such as a ball" |
| `test_3.png` (playground) | An empty seesaw among passers-by, dropped ice cream | Nobody at the seesaw; the scoop "has fallen onto the grass in front of her and made a pink splat"; a jogger right behind a dog walker "might be about to pass him, bump into him" |
| `test_4.png` (garden) | The windy hat with washing on the line, a stalking cat on the fence, a sleeping cat | "The wind has just blown it away ... a pair of blue trousers and a yellow towel ... both are blowing sideways in the wind"; the cat "creeping along the top of the fence ... about to pounce". But the flying cap "is the same blue as the man's cap, which is still on his head"; the cat on the fence "seems to sit in the wind lines next to the cap"; "the clothes and the cap are blowing hard, but the swing seat hangs perfectly still" |
| `test_5.png` (street) | Square-wheeled bicycle with its stand, dropped ice cream, a photographer | "Its wheels are drawn as squares ... a bike like that could not roll"; the stand "could be a kickstand or a pedal"; the scoop "lies splattered on the pavement" |
| `test_6.png` (park, tier 4) | Ball in a tree, a kite flying, stalking cat, walking a dog, picnic | The ball "reads as caught in the tree rather than floating"; the cat "crouched low facing the bird ... stalking it and may be about to pounce"; the kite with its "bow-tied tail" flying high, no remark on its string |

Five changes followed:

- **Short wave arcs.** The arcs either side of a waving hand are shorter and further apart, so they cannot close into
  a ring round it.
- **No dog near the stalking cat.** The ground kept free of dogs round a stalking cat is twice as wide.
- **The blown cap is nobody else's colour.** The cap blowing away is never the colour of a cap someone else in the
  picture is wearing.
- **The gust's path is clear.** The wind lines and the hat keep clear of every other person and animal.
- **The empty swing swings.** In a windy picture the empty swing seat hangs swung out downwind.

## Round 2: the scenes rebuilt

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_7.png` (`test_1` rebuilt) | Short wave arcs, the dog further from the cat | The woman waves "(small motion lines by her hand)", no ring; the cat "crouches low and creeps or runs toward a blue bird". But the dog, now further off and walking toward it, "is heading left toward the cat and bird and could lunge at them" |
| `test_8.png` (`test_2` rebuilt) | The waving teenager's arcs | "Small motion marks around his hand show he is waving"; the girl on the seesaw "looks stuck up there because the reader is not pushing off" |
| `test_9.png` (`test_4` rebuilt) | The cap's colour, the gust's path | A red cap now, "the girl reaching for it suggests it is hers, but it could be the man's cap blown toward him. It is flying toward the man's side of the picture" |

Three more changes followed:

- **No dog at the stalking cat's depth.** No dog anywhere in the band of ground the cat stands in, across the whole
  picture (twice as far off, a dog walking toward the cat still "could lunge").
- **Nobody downwind of the cap,** now or later, and nobody placed later in the gust's path.
- **The stalking cat on the fence keeps clear of the clothesline,** as the cat walking the fence already did (one
  rebuild put it between the line's posts, where it seemed to walk the line).

## Round 3: the two scenes rebuilt again

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_10.png` (`test_7` rebuilt) | Stalking cat with the dog at another depth | "An orange cat is crouched low and creeping toward a blue bird that is pecking at the ground. The cat looks about to pounce"; the dog "walks ahead of him", no remark on it; the wave "little motion lines around the hand show it is moving" |
| `test_11.png` (`test_9` rebuilt) | The cap with nobody downwind | "White wind lines in the sky and across the garden show a strong breeze blowing from right to left ... laundry ... flapping sideways in the wind"; "the cap probably blew off the woman's head" |

The stalking cat read as stalking, creeping or about to pounce in all seven scenes it was in (once "creeps or
runs"), the girl on the seesaw as stuck in both of hers, the wave as a wave in all five, with no ring once the
arcs were shortened; the wind reached the washing and the sky in both gardens. Two
remarks were left: the wind still leaves hair and clothes unmoved (the cast is posed and rendered in 3D; a
blowing skirt or hair would be a new rig), and the sleeping cat curled up is small ("a sleeping kitten or cat,
but at that size it could be read as a toy").
