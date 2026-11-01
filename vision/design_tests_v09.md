# The v0.9 redesigns, read blind in test scenes before going into the set

The v0.8 screen failed four templates: the heavy seesaw, the dog begging, the person about to trip and
the lost balloon (`flaws_v08.md`). v0.9 redesigned all four, then read them blind in four test scenes
before regenerating the set, as v0.8 did for the giant fork. Each reader was a fresh model that saw only
its one picture, with the screen's reader prompt (`screen_prompts.md`). The pictures and descriptions are
in `design_tests_v09/`.

## The redesigns

- **Lost balloon.** The child holds a bunch of two balloons on strings in a hand held out to the side,
  and reaches up with the other hand for a third balloon rising just out of reach, its string trailing
  down toward the fingers (a new pose, `balloon_reach`). One balloon above a reaching child was always
  "let go, or just floating past".
- **Heavy seesaw.** A plainly grown, heavy man (never the youngest man, once read as "a boy") sits on the
  low end reading a book (`seesaw_low_read`); the child up on the high end calls out. Since v0.8 an
  ordinary seesaw also tips toward its heavier rider, so the tilt alone no longer says anyone is stuck.
- **Dog begging.** An ice cream instead of an apple (read as "a cherry ... or a red clown nose"); the dog
  sits square with its head tipped right up at the food (`beg`).
- **About to trip.** A bigger book held open, turned so its pages show in side view (`walk_read_open`;
  edge-on, the small book read as a phone), and the obstacle alone in the walker's path, clear of other
  people and of benches and stalls.

## The reads

| Picture | Lost balloon | Heavy seesaw | Dog begging | About to trip |
|---|---|---|---|---|
| `test_1.png` (playground) | | "the girl is left up in the air while he isn't paying attention to her"; "with a light child up in the air and a heavy adult down, the seesaw looks physically plausible". His small book "or a phone" | | "heading towards a red bucket ... looks likely to trip over it because she is not watching where she is going" |
| `test_2.png` (park) | "stretches his other arm up toward a red balloon that has got away from him ... as if he has just let go of it" | | "rearing up beside the bench ... the dog is about to grab or lick it"; "apparently begging for or about to snatch it" | |
| `test_3.png` (street, busy) | "it looks as if it may have got away"; hedged: "or it is tied to the stall", the reaching hand perhaps "reaching back to take a piece of red fruit" | | "stretches up on its hind legs toward her ice cream, as if begging" | "heading straight for a red bucket ... looks about to trip over it or kick it" |
| `test_4.png` (playground, busy) | "It looks like he just let go of the yellow balloon and is trying to grab it back" | "a little girl in pink sits on the high end, stuck up in the air waiting"; "he is reading and ignoring the girl stuck on the high end" | | "she looks likely to bump into it or trip over it" |

Three changes followed the reads before the set was built:

- The seesaw reader got the same big open book as the walker (his small book read as "a phone").
- The balloon child and both the bunch and the loose balloon keep clear of the fruit stall (over the
  stall the balloon seemed tied to it).
- The dog's action item names the begging, not a posture (the sitting beg read twice as "stretching up
  on its hind legs" to beg).
