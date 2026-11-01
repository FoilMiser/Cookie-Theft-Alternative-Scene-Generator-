# The v0.13 changes, read blind in whole test scenes

After the isolation bench (`isolation_v013.md`) each refined visual went back into whole scenes, with the
other events around it, and was read blind there before the set was regenerated, as v0.8 to v0.12 did.
Each reader was a fresh model that saw only its one picture, with the screen's reader prompt
(`screen_prompts.md`). The pictures and descriptions are in `design_tests_v013/`; `map.txt` names the
scene behind each picture.

## Round 1: the refined visuals among the other events

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_1.png` (garden) | Blocked hose, floating box, sleeping cat, laundry | "The bulge ends right where the dog's back paw is, so the dog seems to be standing on the hose and blocking the water ... the man's drip-only nozzle supports the 'dog is blocking it' reading". The box "floating in mid-air with no support or string". But the cat "right next to the hose (possibly on it)": it lay across the slack hose at the holder's feet |
| `test_2.png` (park) | Kite in a tree, stalking cat, sleeping dog, pram, kick | The kite "tangled in the leaves of that big tree; leaf clumps are drawn over it, so it looks stuck"; the cat "sneaking up to pounce on the bird". The puppy, curled up small far back by the pond, "looks asleep or sniffing" |
| `test_3.png` (garden) | Windy hat, catch, sleeping cat | The cap "seems to be blowing away in the wind"; the man "ready to catch" the thrown ball; the cat "lying curled on its side with its eyes closed ... asleep or dozing". Still: "the trees, hedge, bush and flowers show no sign of wind, so the gust looks like it is confined to the area around the cap" |
| `test_4.png` (playground) | The heavy man on the seesaw, sandbox | "Being heavy, he keeps her stuck up in the air"; the boy "kneels inside the sandbox ... building" |
| `test_5.png` (street) | Windy hat, square-wheeled bicycle, pram, sleeping cat | The cap blown off, the square wheels "a deliberate 'impossible' detail", the cat "curled up with eyes closed, sleeping". But "the pram overlaps the front of the fruit stall's table and its leg", and the wind again "only seems to affect the cap and the few leaves. The tree ... show[s] no sign of wind" |
| `test_6.png` (busy park) | Kite, ducks, catch, stalking cat, sleeping dog | The kite "clearly tangled in the tree"; the duck "swimming left toward the floating crumbs"; the cat "stalking it, ready to pounce"; the puppy "curled up with its eyes closed and appears to be sleeping" |

Five changes followed:

- **The hose's run along the ground.** No one placed later stands or lies on it (its strip is added to the
  ground boxes no one's feet may enter).
- **Sleepers lie on their own.** A curled-up cat or dog keeps open ground around itself, clear of people,
  animals, drawn objects and standing structures, and nothing placed later comes into that ground.
- **The sleeping dog nearer the front,** like the sleeping cat, so it is drawn larger; both keep up from the
  bottom edge.
- **The pram clear of the market stall.**
- **The gust strips the tree.** Where the picture has a tree, a few leaves stream off the downwind side of its
  crown with a short wind line past it, in open air clear of everything else.

## Round 2: the same scenes rebuilt

| Picture | What was being tested | What the reader said |
|---|---|---|
| `test_7.png` (`test_1` rebuilt) | The hose with the cat moved off it | "The dog's position: it reads as standing on the hose, which is what makes the 'blocked hose' story ... The bulge in the hose: I read it as trapped water building up behind the dog. Another reading is that it is a fitting or connector on the hose, but its shape (a smooth swelling with a highlight) suggests pressure"; the cat away from the hose |
| `test_8.png` (`test_5` rebuilt) | The gust in the tree, the pram clear of the stall | "The leaves and lines suggest the wind blows from the tree (right) towards the cap (left)"; no complaint about the pram. But the sleeping cat lay "very close to the base of the free-standing square-wheeled bike ... 'the bike might topple onto the cat'" (the open ground round sleepers came after this round) |
| `test_9.png` (`test_6` rebuilt) | The sleeping dog nearer the front | No complaint about the dog; the catch "most likely he threw it toward the woman, who is waiting to catch it" |
| `test_10.png` (`test_2` rebuilt) | The sleeping dog nearer the front | "Puppy: it's clearly asleep (closed eyes, curled up)"; the kite "stuck in the tree because the string sags and the kite sits inside the foliage, partly behind a leaf clump" |

The hose read as intended first in both of its pictures, the kite as stuck in all four, the stalking cat as
stalking in all four, and the sleeping cats and dogs as asleep in every picture once the dog was drawn
larger. Two remarks recur and were left: the pecking songbird "could look as if it is tipping forward",
and the wind still leaves hair and awnings unmoved.

## Inspecting the built set

Inspecting every picture of the first builds added three placement rules and one change of angle, each for
a slip seen in a picture: the flying kite keeps clear of the clouds and the sun (in three pictures it sat
against a cloud's underside, as if hanging from it); nobody stands beside the ladder that leans on nothing,
now or later (a man waving right beside its top could have been holding it up); a perched bird keeps off
the tree's branch when something is caught in that tree or someone points up (a red bird sat on the branch
beside a ball stuck in the crown, which a child pointed at); and the curled-up cat is drawn at 45 degrees,
an angle the asset schema allows, rather than 60 (read again on the bench, round 5).
