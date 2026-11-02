"""site_patch.py OLD_SITE NEW_SITE : list the files to publish and to remove when patching the published showcase page.

Prints JSON {"files": [{"as", "path"}...], "remove": [...]} for the artifact publish tool (patch mode)."""
import os, sys, json, hashlib


def tree(d):
    out = {}
    for root, _, fs in os.walk(d):
        for f in fs:
            p = os.path.join(root, f)
            out[os.path.relpath(p, d)] = hashlib.md5(open(p, "rb").read()).hexdigest()
    return out


a, b = tree(sys.argv[1]), tree(sys.argv[2])
files = [{"as": k, "path": os.path.abspath(os.path.join(sys.argv[2], k))} for k in sorted(k for k in b if a.get(k) != b[k])]
print(json.dumps({"files": files, "remove": sorted(k for k in a if k not in b)}))
