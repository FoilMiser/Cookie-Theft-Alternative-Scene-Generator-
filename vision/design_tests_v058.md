# v0.58 design tests

There were no design tests of new pictures in v0.58, and this file says why.

A design test is a new picture, built under the new placement revision with a forced set, that is read blind before the screen: it is for a rule or a drawing that the last release's pictures cannot show. Every rule and drawing of revision 52 could be read where v0.57 already had a picture: the wheelbarrow in its five pictures, the kite in its six, the two seesaws in their ten and the game of catch at the garden's fence in two. Each was built again on its own record's plan with only the new drawing changed (`TPDB_REV58=51 TPDB_ONLY58=<names>`, `tools/cycle/bench_build.py`) and read in two rounds, 248 readings, a reader's pictures of a thing all of one arm. That bench is `isolation_v058.md`.

Three pictures of the release were read for the first time by the screen itself:
- the tier-4 garden, whose forced set has the man who sits on nothing in the wheelbarrow's place (`tools/cycle/forced_cell.py`, `v058garden`), on its old seed;
- two probes forced for the wheeled barrow, a park with a bird feeder and a reader on a bench and a garden with the washing and a sleeping dog (`tools/cycle/extra_probes.py`).

I looked at all three before any reader had them. In the screen each reads in full but for the clouds, which the readers of the garden and of the park left out.

What a design test would have shown and the bench did not: the wheeled barrow in a picture built under revision 52, where its figure is cast with everybody else and not by a draw of its own. In the four barrow pictures that the release keeps from v0.57 the pusher is another figure than the bench's, since the bench built v0.57's records at their own revision. The screen read those four and the two new probes, and all six are in full (`flaws_v058.md`).
