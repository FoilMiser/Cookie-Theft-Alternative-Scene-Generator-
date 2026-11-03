# Picture-description scores, batch c (pic_45 to pic_67)

Sources: `desc_pic_45.md` to `desc_pic_67.md`, `keys_c.json`. Item scores are in `scores_c.json`.

## Coverage check

Checked by script against `keys_c.json`: 23 pictures, 253 items, each with exactly one score. None missing, none invented.

## Mean score by item type

Misread would count as 0; there were none in this batch.

| Type | Items | Mean | Scored 1 | Scored 0.5 | Scored 0 | Misread |
|---|---:|---:|---:|---:|---:|---:|
| entity | 141 | 1.000 | 141 | 0 | 0 | 0 |
| action | 78 | 0.987 | 76 | 2 | 0 | 0 |
| inference | 18 | 0.972 | 17 | 1 | 0 | 0 |
| contradiction_notice | 8 | 1.000 | 8 | 0 | 0 | 0 |
| contradiction_explain | 8 | 1.000 | 8 | 0 | 0 | 0 |
| **all** | **253** | **0.994** | **250** | **3** | **0** | **0** |

## Items scored 0, 0.5 or misread

| Pic | Id | Type | Target | Score | What the describer said |
|---|---|---|---|---:|---|
| pic_57 | i09 | inference | The man is going to trip over a bucket | 0.5 | only in the unsure section, against 'may simply be strolling': may be about to walk into something, could trip on the bucket, but it lies slightly off his line |
| pic_58 | i03 | action | A man is eating an ice cream | 0.5 | cone held up near his face and looked at; 'looking at or eating it', might be admiring it rather than eating |
| pic_62 | i10 | action | A man is eating an ice cream | 0.5 | bearded man walking, holds up a cone and looks at it; 'could be eating the ice cream or just holding it up' |

No item scored 0 and none was misread.

## Credited 1, but a judgement call

These are not below 1. They are listed so the calls can be checked.

| Pic | Id | Target | Why it is close |
|---|---|---|---|
| pic_50 | i01 | A man is sitting on the bench eating an ice cream | Holding up the cone and looking at it; eating never stated. Credited on sitting on the bench with the cone. The describers of pic_58 i03 and pic_62 i10 used similar words (holding up the cone, looking at it) but also doubted eating outright, so those got 0.5. |
| pic_60 | i01 | A girl is sitting on the bench eating an ice cream | Inventory says "eating or holding", ice cream at her mouth. Credited on sitting on the bench. |
| pic_62 | i09 | The grandfather is going to trip over a box | Free description states he is not looking where he is going and might trip, then doubts it: the box is slightly to his side and he may be past it. pic_57 i09 got 0.5 because the trip appears only in the unsure section, as an alternative to strolling. Both describers say the obstacle is off the walker's line. |
| pic_57 | i08 | There is a bucket on the ground in front of a man | Bucket named and ahead of him, but "slightly off his line". |
| pic_61 | i01 | There is a wooden box | Called cardboard, not wooden. Credited because the key accepts "box". |
| pic_66 | i04 | The wind blew the grandmother's hat off | Wind and cap blowing away are clear; ownership hedged as "probably hers". |

Not scored: the teenager is read as a boy in pic_46 to pic_51, and as "boy or young man" or of unclear age in pic_64 and pic_65. The items score the action, so this did not lower any score.

## Unintended oddities by kind

54 oddities across 22 pictures. pic_52 had none. At most three were kept per picture, so these counts are a floor.

### Human figure awkward, stiff or face hidden (13)

- pic_46: older woman's arm hides her face, head tilted back looks awkward
- pic_48: woman's face tilted so far down that her hair hides it
- pic_49: woman's hands clasped, not open, could read as clapping or praying
- pic_51: painter stands side-on to the fence and reaches sideways, looks awkward
- pic_55: woman in yellow looks quite tall compared with the fence
- pic_58: girl sits on the plank's very end with legs hanging over it, no clear shadow
- pic_62: older man's arms across the book look stiff or tangled, head tilt hides his eyes
- pic_62: bearded man's hair and beard merge into one dark shape, features hidden
- pic_63: woman's lower arm hangs with a small awkward hand
- pic_64: boy's legs bend back awkwardly under the seat
- pic_64: ice cream eater looks small next to the children, could read as a small person
- pic_65: running man's back arm and hand look stiff and odd
- pic_67: woman's head tilted back with her face hidden by arm and hair

### Overlap or layering confusion (10)

- pic_46: flower stems overlap the old man's arm, so his hand is hard to read
- pic_50: boy's body overlaps the pond, could seem to stand at the water's edge
- pic_53: bike overlaps its rack and wheels are solid black with no spokes, unclear if locked or leaning
- pic_53: bird on the lamp post overlaps a window, could look as if on the window
- pic_55: carried box looks flat and semi-transparent with fence lines meeting it, could read as stuck to the fence
- pic_56: child on the slide sits to the side of the chute, could look as if hovering above it or leaning off
- pic_58: man overlaps the slide's ladder
- pic_60: dog overlaps the bench legs, appears partly in front of the bench
- pic_61: rake handle merges visually with the man's body and leg
- pic_63: woman overlaps the pond, could look as if standing in the water

### Action, purpose or link between figures not clear (10)

- pic_45: sprinkler points away from the flower bed and only wets the grass and the box
- pic_47: raking man looks off to the right, away from the leaves
- pic_47: watering can and pots placed on the lawn with no clear purpose
- pic_50: man faces away from the dog with the cone on the far side, so the link is only suggested
- pic_51: sprinkler soaks the box while the flower bed beside it gets no water
- pic_53: waving woman's gaze connects to no one in the picture
- pic_57: man in red's head faces the gate but his stride seems to go down or across the path
- pic_65: unclear what the running man is running to or from, seems headed toward the tree
- pic_66: pram sits largely on the grass while the man walks on the path
- pic_66: red baseball cap looks unusual on the older woman

### Animal pose odd or hard to read (9)

- pic_47: cat's head at an awkward angle, body reads as a blob of orange with a face
- pic_50: dog's upright begging pose looks rather human-like
- pic_54: faint pale shape under the goat's belly could not be identified; goat looks stiff and blocky
- pic_56: bird's pose is odd: head a red ball at the ground, tail up, could be tumbling or injured
- pic_57: bird head-down with tail up could read as tumbling over
- pic_59: white dog's body very twisted, legs thin and awkward
- pic_59: sleeping cat could be read as hurt or fallen at the path's edge
- pic_60: dog's pose hard to read: human-like, thin stretched body, could be falling backwards
- pic_65: bird's raised wing is large and confusingly drawn

### Object drawn oddly or not identifiable (9)

- pic_48: duck's wake lines look stiff and straight for water
- pic_49: swing ropes meet behind the girl's head, then spread to the seat corners
- pic_54: bulge in the hose could read as a separate object (pad or fat fitting)
- pic_59: green and brown bits by the hat: unclear what they are or why they are there
- pic_60: unexplained green or dark mark near the girl's mouth, ice cream not clearly on a cone
- pic_61: leaf pile sits past the rake head, cannot tell if gathering or pushing
- pic_62: ball could read as a planet-like striped object at first glance
- pic_67: T-shirt looks stiff and flat, far sleeve sticks out sideways instead of hanging
- pic_67: wheelbarrow's handles and legs are confusing, might be tipped

### Physical logic doubted (3)

- pic_58: seesaw nearly level even though the girl looks smaller and lighter
- pic_64: seesaw said to look wrong in its balance, later judged reasonable
- pic_66: strong wind drawn near the cap but trees, dress and hair are unaffected
