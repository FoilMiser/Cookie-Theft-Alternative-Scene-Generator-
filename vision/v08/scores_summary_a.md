# v08 key A: picture description scores

Scored against `keys_a.json` (pic_01 to pic_16, 240 items) using the full description file (free description, inventory and unsure section). A score of "misread" counts as 0 in the means.

## Mean score by item type

| Type | Items | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 99 | 0.995 | 98 | 1 | 0 | 0 |
| action | 91 | 0.973 | 87 | 3 | 0 | 1 |
| inference | 26 | 0.827 | 20 | 3 | 3 | 0 |
| contradiction_notice | 12 | 1.000 | 12 | 0 | 0 | 0 |
| contradiction_explain | 12 | 0.958 | 11 | 1 | 0 | 0 |
| contradiction (both) | 24 | 0.979 | | | | |
| **all items** | 240 | **0.967** | | | | |

Per-picture mean: 01 1.00, 02 1.00, 03 1.00, 04 1.00, 05 1.00, 06 0.97, 07 0.94, 08 1.00, 09 1.00, 10 1.00, 11 1.00, 12 0.96, 13 0.83, 14 0.93, 15 1.00, 16 1.00

## Items scored 0 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_07 | i05 | action | A woman is reading while walking | misread | reading material read as a phone: woman 'walks while looking at a phone' ('red-and-white phone'); distracted walking kept, reading lost |
| pic_13 | i03 | inference | The dog wants some of the food | 0 | no begging/wanting stated; dog only 'looking up at her' (and the food itself was uncertain) |
| pic_13 | i09 | inference | The worker is going to trip over a box | 0 | no trip/bump prediction; worker and box described separately |
| pic_14 | i03 | inference | The man is much heavier, so the girl is stuck up in the air | 0 | no weight explanation; positions on the seesaw described but not why |

### Partial credit (0.5), for reference

| Pic | Item | Type | Target | Note |
|---|---|---|---|---|
| pic_06 | i10 | contradiction_explain | The box is floating in the air with nothing holding it up | floating offered as one reading ('could look as if it is floating or stuck on the fence') but rejected: 'probably resting there', leaning against the fence |
| pic_07 | i13 | inference | The child let go of the balloon | two readings offered: child holding the balloon, or 'just let go and reaching up to grab it back' |
| pic_12 | i02 | action | A dog is sitting by the bench, looking up | dog by the bench looking at the woman, but posture read as 'rearing up', 'standing up on its back legs (or jumping up)', not sitting |
| pic_12 | i15 | inference | The child let go of the balloon | two readings offered: 'could belong to the boy, who has just let go of it, or it could simply be floating past' |
| pic_13 | i01 | action | A grandmother is sitting on the bench eating an apple | sits on bench 'holding something small and red to her mouth'; unsure: cherry/small apple/sweet she is eating, OR a red clown nose she is putting on |
| pic_13 | i04 | action | A cat is crouching low | free description says the cat 'is running toward' the bird; inventory 'running or stalking'; crouch not described |
| pic_13 | i08 | entity | There is a box on the ground in front of a worker | 'a cardboard box on the grass' mentioned, but placed 'behind the girl' and not linked to the worker's path |
| pic_13 | i12 | inference | The child let go of the balloon | two readings offered: balloon 'may have just slipped out of the boy's hand or may simply be passing over him' |

## Unintended oddities, grouped by kind

Things the describer flagged as odd, impossible, unexplained or hard to read that are not scored items.

**contact/placement** (6)

- pic_03: broom seems to sweep the grass at the edge of the path rather than the path itself
- pic_08: older girl's body sits slightly in front of the seesaw beam with shadow offset, so she can look as if perching in front of the seat
- pic_09: girl's legs come close to the right leg of the swing frame
- pic_14: jumper's shadow is separate from the feet; at a glance they could seem to be floating
- pic_15: ball sits a little in front of the toe rather than touching it
- pic_15: rubbish bin overlaps the fence line and could look attached to it

**gaze/target unclear** (5)

- pic_05: photographer aims up and to the right at nothing identifiable (buildings, lamp post or sky)
- pic_05: whom the old man is waving at is unclear
- pic_09: painter's head tipped back looking up rather than at the fence he is painting
- pic_13: waving woman: not clear at whom she is waving
- pic_16: waterer's head turned toward the can/stream rather than the flowers

**object rendering** (4)

- pic_01: white/grey patch beside the bucket-wearer's ear: sideburn, beard or hair, hard to tell
- pic_05: the dog's 'newspaper' has ring-binder holes: newspaper, notebook or ring binder?
- pic_07: the dog's reading matter is drawn as an open book with ring-binder holes, not a newspaper
- pic_12: digging tool has a small pronged shape at the top of the handle: pitchfork head or D-grip?

**character age** (4)

- pic_06: hose holder could be a teenage boy or a young man
- pic_14: jumper could be a teenage boy or girl
- pic_15: kicker could be a teenage girl or a young woman
- pic_16: fisher could be a teenage girl or a young woman

**posture** (3)

- pic_02: picnic man sits at the very end of the blanket with legs stretched off it: slightly awkward
- pic_15: kicker's arms stiff and not swinging; one hand tucked behind her back with a small grey shape at it
- pic_15: kicker's head in profile looks slightly twisted against the body

**scene incongruity** (2)

- pic_01: everyone calmly carrying on under a dark stormy sky, no rain falling
- pic_14: eating ice cream and playing cheerfully under dark storm clouds: 'a bit odd but not impossible'

**missing connection** (2)

- pic_06: sprinkler sprays water with no visible hose or pipe connected
- pic_09: sprinkler sprays water with no hose connected; the nearby hose reel is not linked to it

**stray artifact** (2)

- pic_06: small grey shadow-shape behind the flower bed near the hose reel that belongs to nothing
- pic_16: water drops near the duck: end of the odd stream or splashes from the duck?

**out-of-place object** (1)

- pic_02: why a ladder is in the park at all is unclear: no one using it, nothing to climb

**missing expected prop** (1)

- pic_04: no paint tin visible anywhere although the fence is being painted

**idle props** (1)

- pic_04: empty swing and unused wheelbarrow just sitting there

**duplicate prop** (1)

- pic_07: two identical red balls, one in the air and one on the ground: possibly confusing

**behaviour/safety** (1)

- pic_08: boy standing upright on the very top of the slide 'looks a bit unsafe' (named as one of the things that 'seem wrong')

**proportion/reach** (1)

- pic_16: fisher stands well back from the water's edge, so the rod has to stretch far over the pond
