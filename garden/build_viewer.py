"""Bundle the master SVG + tags into a single-file viewer page."""
import json, sys, os

out = sys.argv[1] if len(sys.argv) > 1 else "out"
svg = open(os.path.join(out, "garden_master.svg")).read()
svg = svg.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000">',
                  '<svg id="ui-scene" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" role="img" aria-label="Garden scene">')
svg = svg.replace("</svg>", '<g id="ui-overlay" pointer-events="none"></g></svg>')
tags = json.load(open(os.path.join(out, "garden_tags.json")))
slim = {
    "concepts": {k: {kk: v[kk] for kk in ("text", "kind", "tier_min", "tier_max", "inference_type", "elements", "cells")}
                 for k, v in tags["concepts"].items()},
    "elements": [{k: e.get(k) for k in ("id", "label", "role", "tier_min", "tier_max", "concepts", "bbox")}
                 for e in tags["elements"]],
    "tiers": tags["tiers"],
}
tpl = open(os.path.join(os.path.dirname(__file__) or ".", "viewer_template.html")).read()
html = tpl.replace("%%SVG%%", svg).replace("%%DATA%%", json.dumps(slim, separators=(",", ":")))
open(os.path.join(out, "garden_viewer.html"), "w").write(html)
print(len(html) // 1024, "KB")
