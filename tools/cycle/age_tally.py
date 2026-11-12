"""age_tally.py FOLDER MAP.json : the age bench counted (age_bench.py wrote the strips and the map; the readers wrote FOLDER/who_N.md).
Per cast, of the grown figures (the teenager, person.leo, is left out): called by a young name first, a teenager, a boy or a girl offered as
what else the figure could be, and the reader "sure"; and the (a) and (c) lines of every figure."""
import io, json, re, sys
folder, mp = sys.argv[1], json.load(open(sys.argv[2]))
YOUNG = re.compile(r"\b(boy|girl|teenager|teen|child|kid)\b", re.I)
tot = {}
for n in sorted(mp, key=int):
    m = mp[n]
    t = io.open("%s/who_%s.md" % (folder, n), encoding="utf-8").read()
    parts = re.split(r"^#+ *Person \d|^\*\*Person \d", t, flags=re.M)[1:]
    if len(parts) != 4:
        parts = re.split(r"^(?:#+ *|\*\*)?\d[.)]", t, flags=re.M)[1:]
    assert len(parts) == 4, (n, len(parts))
    for fig, part in zip(m["figures"], parts):
        ls = [l.strip() for l in part.splitlines() if l.strip()]
        a = next(l for l in ls if l.lstrip("-* ").startswith("(a)"))
        d = next(l for l in ls if l.lstrip("-* ").startswith("(d)")).lower()
        c = next(l for l in ls if l.lstrip("-* ").startswith("(c)"))
        a1 = re.sub(r"^[-* ]*\(a\)\s*\**", "", a)
        first = re.split(r"[(/,;]| or ", a1)[0]
        young = bool(YOUNG.search(first))
        teen = "teen" in d or bool(re.search(r"\b(boy|girl)\b", d))
        sure = bool(re.match(r"^[-* ]*\(d\)\s*\**sure", d))
        if "leo" not in fig:
            k = tot.setdefault(m["cast"], [0, 0, 0, 0])
            k[0] += 1; k[1] += young; k[2] += teen; k[3] += sure
        print(m["cast"], fig.replace("person.", "").ljust(20), "| young" if young else "|      ", "| teen" if teen else "|     ", "| sure" if sure else "|     ", "|", a1[:44].ljust(44), "|",
              re.sub(r"^[-* ]*\(c\)\s*", "", c)[:70])
print({k: dict(zip(("n", "young_first", "teen_offered", "sure"), v)) for k, v in tot.items()})
