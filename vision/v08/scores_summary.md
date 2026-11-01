# v0.8 screen: scorer summaries

Two scorers with the same prompt scored the 39 pictures in two parts (pic_01 to pic_16, 240 items; pic_17 to pic_39, 242 items);
`scores.json` merges `scores_a.json` and `scores_b.json`.

## Pictures 1 to 16

## v08 key A: picture description scores

Scored against `keys_a.json` (pic_01 to pic_16, 240 items) using the full description file (free description, inventory and unsure section). A score of "misread" counts as 0 in the means.

### Mean score by item type

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

### Items scored 0 or misread

| Pic | Item | Type | Target | Score | What the describer said |
|---|---|---|---|---|---|
| pic_07 | i05 | action | A woman is reading while walking | misread | reading material read as a phone: woman 'walks while looking at a phone' ('red-and-white phone'); distracted walking kept, reading lost |
| pic_13 | i03 | inference | The dog wants some of the food | 0 | no begging/wanting stated; dog only 'looking up at her' (and the food itself was uncertain) |
| pic_13 | i09 | inference | The worker is going to trip over a box | 0 | no trip/bump prediction; worker and box described separately |
| pic_14 | i03 | inference | The man is much heavier, so the girl is stuck up in the air | 0 | no weight explanation; positions on the seesaw described but not why |

#### Partial credit (0.5), for reference

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

### Unintended oddities, grouped by kind

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

## Pictures 17 to 39

## Picture description scoring, set B (pic_17 to pic_39)

Source: `desc_pic_17.md` to `desc_pic_39.md` scored against `keys_b.json`. Item scores are in `scores_b.json`. Means count `misread` as 0. Scoring rules: 1 = clearly conveyed; 0.5 = partly, or given as only one of two readings; inference items need the inferred meaning stated; contradiction items need the oddity flagged or the impossible fact described.

### Mean score by item type

| Type | Items | Mean | 1 | 0.5 | 0 | misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 129 | 1.000 | 129 | 0 | 0 | 0 |
| action | 81 | 0.994 | 80 | 1 | 0 | 0 |
| inference | 16 | 0.938 | 14 | 2 | 0 | 0 |
| contradiction_notice | 8 | 1.000 | 8 | 0 | 0 | 0 |
| contradiction_explain | 8 | 1.000 | 8 | 0 | 0 | 0 |
| **contradiction (both)** | 16 | 1.000 | 16 | 0 | 0 | 0 |
| **ALL** | 242 | 0.994 | 239 | 3 | 0 | 0 |

### Items scored 0 or misread

None. Every scored item was mentioned in some form.

#### Partial credit (0.5), listed because these are the only lost points

| Pic | Item | Type | Target | What the describer said |
|---|---|---|---|---|
| pic_24 | i03 | inference | The man is much heavier, so the girl is stuck up in the air | 'the bigger boy is down and the smaller girl is up, so this doesn't look wrong': weight-tilt link stated, but the adult is read as a boy, the girl is not seen as stuck, and the size gap is put down to drawing scale |
| pic_27 | i02 | action | A girl is holding an empty cone, looking upset | 'holds an ice-cream cone up to her face, but the cone seems to be empty': empty cone seen, but she is read as not having noticed ('looking at it or eating from it'), not upset |
| pic_29 | i04 | inference | The kite got stuck in the tree | 'so it may be stuck in the tree'; unsure section gives (a) caught vs (b) flying low in front of the tree |

#### Slips that kept full credit (accepted phrasing met, but a detail differs from the key)

- pic_24 i01: The man on the low end of the seesaw is called 'a boy'. This is what cost the pic_24 inference.
- pic_19 i05: The worker is called 'a boy or young man'.
- pic_29 i02, pic_31 i11, pic_32 i01, pic_36 i01, pic_37 i02, pic_39 i01: The teenager (brown ponytail, blue hoodie) is called a woman (4), a man (1) or a girl (1); elsewhere 'young person' or 'older girl or young woman'.
- pic_27 i07: Bird placed on the slide, not the fence.
- pic_28 i04: Box called cardboard, not wooden.
- pic_32 i02: Dog described as standing, not sitting.
- pic_21 i02: Cat 'lying down' stated firmly, but 'sleeping' given only as one of two readings (the other: creeping to the food bowl).
- pic_27 i03 / i05: Fallen scoop: 'pink ball' reading raised, then rejected.
- pic_31 i04: Tripping predicted, but unsure whether over the bucket or the lying dog.
- pic_34 i06: Wind blew the cap away, but unsure whether off her head or off the washing line.

### Unintended oddities reported by the describer (not scored items), by kind

34 reports across 20 of 23 pictures. Pictures with none: pic_28, pic_31, pic_33.

#### Drawing distortion or rendering glitch (5)

- pic_18: bicycle looks compact/squashed: frame small for the wheels, rack hoop sits behind and around it
- pic_19: older man's grey lower face could be a beard or a face mask
- pic_19: digger's hands/forearms greyish and striped: gloves, or an awkward drawing of the arms crossing the spade handle
- pic_35: slide ladder drawn in a different colour and leaning, looks slightly separate from the frame
- pic_39: rightmost painted board has a flat, squared-off top instead of a pointed one

#### Layering / overlap / contact (9)

- pic_17: dog's tail close to or touching the man's leg (ownership unclear)
- pic_18: bird overlaps the roof edge of the peach building (flying past vs landing; judged benign)
- pic_20: woman's body overlaps the lamp post (reads as in front of it; judged benign)
- pic_24: low-end rider seems to sit just above/behind the end of the plank rather than on it
- pic_25: small bush at the foot of the fence has its top hidden by the fence boards (layering glitch)
- pic_26: left swing chain seems to pass through the girl's head/body
- pic_30: hose water passes near the bottom of the clothesline post (reads as in front of it; judged benign)
- pic_37: bike rack hoop overlaps the bicycle so it looks inside the rack (judged normal)
- pic_38: yellow door knob just beside the dog's head could look like an ear tag

#### Placement / scale (5)

- pic_21: cat drawn very small in the picture
- pic_23: water stream lands at the very edge of the flower bed and may fall short
- pic_26: girl's feet stick out to the left of the seat, as if perched on its end
- pic_26: swing set's left legs stand on the stepping-stone path
- pic_32: kite-flying boy stands right at the base of the fence and looks small, almost as if against or on the fence

#### Physics / shadow (2)

- pic_35: seesaw only slightly tilted despite the large size difference between the riders
- pic_35: shadow under the seesaw's left end is offset from the rider's feet

#### Missing prop or continuity gap (2)

- pic_25: no paint tin, tray or bucket anywhere: unclear where the paint comes from
- pic_25: painted section is finished down to the ground although he is only reaching the top

#### Simplified or stylised drawing (5)

- pic_23: wheelbarrow drawn with only one handle visible
- pic_23: unclear where the hose attaches past the man's hand (judged not wrong)
- pic_29: wheelbarrow shows only one handle
- pic_36: seed trail drawn as a neat curved dotted line, 'a little stylised'
- pic_38: wheelbarrow seen with only one handle (judged normal)

#### Context / plausibility (4)

- pic_21: small leaf pile with no tree directly above it ('slightly unexplained')
- pic_27: old man carrying a cardboard box through a playground is 'a little unusual'
- pic_34: a goat loose in a home garden is 'unusual'
- pic_35: standing with arms raised at the top of the slide is 'a little unsafe'

#### Framing (cut off by the edge) (2)

- pic_20: fallen ice cream and the white dog's head cut off by the bottom edge
- pic_22: rubbish bin in the bottom-left corner cut off by the edge
