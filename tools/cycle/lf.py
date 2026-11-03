"""lf.py : rewrite CRLF as LF in the working tree's text files. Python's text mode writes CRLF on Windows; git stores LF
either way (.gitattributes), and this keeps the release zip the same. Run before packaging."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cfg import ROOT  # noqa: E402
TEXT = (".json", ".md", ".svg", ".txt", ".html", ".py", ".sh", ".tsv")
n = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", ".venv", "tpdb_work", "__pycache__")]
    for f in filenames:
        if f.endswith(TEXT):
            p = os.path.join(dirpath, f)
            b = open(p, "rb").read()
            if b"\r\n" in b:
                open(p, "wb").write(b.replace(b"\r\n", b"\n"))
                n += 1
print(n, "files rewritten")
