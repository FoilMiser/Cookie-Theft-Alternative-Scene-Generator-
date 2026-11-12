"""qcheck.py DOC.md [FOLDER ...] : every double-quoted phrase of one document, looked up in the readers', reviewers' and scorers' own files
under this release's isolation and design-test folders and the folders named (for a flaws file: vision/v<TAG> vision/v<PREV>). check_quotes.py
does this for the README, the flaws file, the limits and the site at the end; this one is for a document while it is being written. A miss is
a question: a quote shorter than four letters pairs the marks wrongly, and Sam's brief is in nobody's file."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT, TAG  # noqa: E402
import glob, io, re
os.chdir(ROOT)
doc = io.open(sys.argv[1], encoding="utf-8").read()
dirs = [f"vision/isolation_v{TAG}", f"vision/design_tests_v{TAG}"] + sys.argv[2:]
allt = "\n".join(io.open(f, encoding="utf-8").read() for d in dirs for f in glob.glob(d + "/**/*.md", recursive=True))
bad = n = 0
for q in re.findall(r'"([^"\n]{4,})"', doc):
    n += 1
    if q in allt or q.rstrip(".,;:") in allt:
        continue
    bad += 1
    print("NOT FOUND:", q[:160])
print(n, "quotes,", bad, "not found")
