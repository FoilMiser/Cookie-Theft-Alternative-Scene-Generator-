"""calib_cmp.py OLD.json NEW.json : two calibrations compared by the rule of v0.49. Of n, b0_mean, b0_sd, s_mean, d_mean, r and a over the calibration's items, those that moved by 0.002 or more (the rule of v0.49)."""
import json, sys
a = json.load(open(sys.argv[1])); b = json.load(open(sys.argv[2]))
keys = ("n", "b0_mean", "b0_sd", "s_mean", "d_mean", "r", "a")
tot = moved = 0
for t in sorted(set(a) | set(b)):
    for it in sorted(set(a.get(t, {})) | set(b.get(t, {}))):
        x, y = a.get(t, {}).get(it), b.get(t, {}).get(it)
        if x is None or y is None:
            print("ONLY IN ONE:", t, it); continue
        for k in keys:
            tot += 1
            if abs(x[k] - y[k]) >= 0.002 - 1e-9:
                moved += 1
                print(t, it, k, x[k], "->", y[k])
print(moved, "of", tot, "moved by 0.002 or more")
