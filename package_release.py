#!/usr/bin/env python3
"""Package a TPDB release so it is usable from Google Drive.

    python3 package_release.py 0.18 --single                      # one zip, tpdb_v0.18.zip (the default release)
    python3 package_release.py 0.18                               # zip parts for browsing in Google Drive
    python3 package_release.py 0.17 --from-zip tpdb_v0.17.zip     # re-split an existing single-zip release
    python3 package_release.py 0.17 --verify-only --from-zip tpdb_v0.17.zip

The release holds the same files package_v0XX.sh used to put into tpdb_v<version>.zip, all
under the one folder tpdb_v<version>/. Instead of one large zip, it is written to
release_v<version>_drive/ (or --out) as:

    README_DRIVE.md           what the parts are and how to put the tree back together
    README_v<version>.md      the release README, a copy that Drive opens directly
    showcase/*.png            the set's pictures (colour and grayscale), copies that Drive opens directly
    SHA256SUMS.txt            a checksum for every file in the tree
    tpdb_v<version>_partNofM_<name>.zip   the whole tree, split into parts that do not overlap

Why the split (sources in README_DRIVE.md):
  * Drive does not virus-scan files over 100 MB (support.google.com/drive/answer/141702) and
    shows a "can't scan this file" warning for them; v0.17 as one zip was 141 MB. Each part
    is kept under PART_MAX_BYTES (half of that, to leave room for growth).
  * Drive can preview a zip and open single files inside it, but cannot unzip it, and Google
    publishes no limit on entries or nesting. PART_MAX_ENTRIES is our own cap, to keep each
    listing short.
  * The README and the pictures are copied next to the zips so that they open in Drive
    without going through the archive viewer.

With --single the same tree goes into one zip, tpdb_v<version>.zip (or --out), checked file by
file against the source the same way; over 100 MB, Drive asks to confirm its download because it
cannot scan it, and the file downloads as normal after that.

The script only adds files to a new output folder: it does not delete or overwrite anything.
Only the Python standard library is used. After building, it checks every part against the
source (see verify()) and exits non-zero if anything differs.
"""
import argparse
import datetime
import fnmatch
import hashlib
import os
import re
import shutil
import subprocess
import sys
import time
import zipfile
from dataclasses import dataclass
from typing import Callable, Optional

# ---------------------------------------------------------------- limits
DRIVE_SCAN_LIMIT = 100_000_000   # Drive: "There's a 100MB scanning limit" (support.google.com/drive/answer/141702)
PART_MAX_BYTES = 50_000_000      # ours: each zip at most half the scan limit
PART_MAX_ENTRIES = 1000          # ours: Drive publishes no entry limit; keeps each archive listing short
# Already compressed formats are stored as they are (deflating them saves about 1% and costs CPU).
STORE_EXT = {'.png', '.webp', '.jpg', '.jpeg', '.gif', '.blend', '.zip', '.gz', '.mp4', '.webm'}

HERE = os.path.dirname(os.path.abspath(__file__))


def groups_for(tag):
    """The parts, in order: (name, what it holds, path prefixes under tpdb_vX/). An empty prefix
    list is the catch-all part."""
    return [
        ('code-docs', 'README, generator (`scenegen/`), cast and asset code, combos and calibration, '
                      'packaging script, the Garden prototype', []),
        ('scenes-probes', 'The generated set (`scenes/`: SVG, colour and grayscale PNG, thumbnail, JSON record '
                          'per picture) and the probe pictures (`probes/`)', ['scenes/', 'probes/']),
        ('site', 'The showcase page (`site/index.html` and its WebP images); download it and open '
                 '`index.html` in a browser', ['site/']),
        ('cast-models-gallery', f'The Blender `.blend` families and render configs (`assets/cast/out{tag}/`) '
                                f'and the gallery renders (`assets/cast/gallery{tag}/`)',
         [f'assets/cast/out{tag}/', f'assets/cast/gallery{tag}/']),
        ('cast-lib', f'Every cast variant the scenes and probes use (`assets/cast/lib{tag}/`)',
         [f'assets/cast/lib{tag}/']),
        ('vision', 'The blind screens, isolation bench, design tests, flaw lists and screen tools (`vision/`)',
         ['vision/']),
    ]


# ---------------------------------------------------------------- items
@dataclass
class Item:
    rel: str                    # path under tpdb_vX/, '/'-separated; directories end in '/'
    size: int
    date_time: tuple
    attr: int                   # zip external_attr
    read: Optional[Callable[[], bytes]] = None

    @property
    def is_dir(self):
        return self.rel.endswith('/')


def excluded(rel):
    """The removals package_v0XX.sh made after copying."""
    parts = rel.rstrip('/').split('/')
    if '__pycache__' in parts:
        return True
    if not rel.endswith('/') and fnmatch.fnmatch(parts[-1], '.*.cfg.json'):
        return True
    if len(parts) >= 3 and parts[0] == 'vision' and fnmatch.fnmatch(parts[1], 'v0*') and parts[2] == 'blind':
        return True
    return False


def file_item(src, rel):
    st = os.stat(src)
    zi = zipfile.ZipInfo.from_file(src, rel, strict_timestamps=False)
    return Item(rel, st.st_size, zi.date_time, zi.external_attr, lambda p=src: open(p, 'rb').read())


def collect_tree(root, version, tag, scenes, probes):
    """What package_v0XX.sh copied into its staging folder, read in place (nothing is copied)."""
    items = {}

    def need(path):
        if not os.path.exists(os.path.join(root, path)):
            sys.exit(f'missing in the working tree: {path}')
        return os.path.join(root, path)

    def add_file(src, rel):
        items[rel] = file_item(need(src), rel)

    def add_tree(src_dir, rel_dir):
        base = need(src_dir)
        for dirpath, dirnames, filenames in os.walk(base, followlinks=True):
            dirnames.sort()
            sub = os.path.relpath(dirpath, base).replace(os.sep, '/')
            rel_here = rel_dir + '/' + ('' if sub == '.' else sub + '/')
            # Every folder is recorded; drop_implied_dirs() later keeps only the empty ones,
            # as cp -r followed by zip -r would.
            zi = zipfile.ZipInfo.from_file(dirpath, rel_here, strict_timestamps=False)
            items[rel_here] = Item(rel_here, 0, zi.date_time, zi.external_attr)
            for f in sorted(filenames):
                add_file(os.path.join(src_dir, sub, f) if sub != '.' else os.path.join(src_dir, f), rel_here + f)

    add_file(f'README_v{version}.md', 'README.md')
    if os.path.exists(os.path.join(root, 'RUNBOOK.md')):
        add_file('RUNBOOK.md', 'RUNBOOK.md')          # v0.23: how a release is made
    for f in ('combos.json', 'calibration.json'):
        add_file(f, f)
    for f in ('requirements.txt', '.gitignore', '.gitattributes'):
        if os.path.exists(os.path.join(root, f)):
            add_file(f, f)                            # v0.24: how the repository is set up
    if os.path.exists(os.path.join(root, f'package_v{tag}.sh')):
        add_file(f'package_v{tag}.sh', f'package_v{tag}.sh')
    items['package_release.py'] = file_item(os.path.abspath(__file__), 'package_release.py')
    for f in ('render_assets.py', 'validate_assets.py', 'asset_manifest.schema.json', 'palette.json'):
        add_file(f'assets/{f}', f'assets/{f}')
    if os.path.exists(os.path.join(root, 'assets/blender_run.py')):
        add_file('assets/blender_run.py', 'assets/blender_run.py')   # v0.24: bpy scripts inside an installed Blender
    for f in ('build_cast.py', 'render_set.py', 'sheet.py', 'gapcheck.py'):
        add_file(f'assets/cast/{f}', f'assets/cast/{f}')
    add_tree('assets/cast/castlib', 'assets/cast/castlib')
    out = f'assets/cast/out{tag}'
    for f in sorted(os.listdir(need(out))):            # cp out/*.blend out/*.json (no dotfiles, no folders)
        if not f.startswith('.') and f.endswith(('.blend', '.json')) and os.path.isfile(os.path.join(root, out, f)):
            add_file(f'{out}/{f}', f'{out}/{f}')
    add_tree(f'assets/cast/lib{tag}', f'assets/cast/lib{tag}')
    add_tree(f'assets/cast/gallery{tag}', f'assets/cast/gallery{tag}')
    add_tree('scenegen', 'scenegen')
    add_tree(scenes, 'scenes')
    add_tree(probes, 'probes')
    add_tree(f'site{tag}', 'site')
    add_tree('garden', 'garden')
    add_tree('vision', 'vision')
    if os.path.isdir(os.path.join(root, 'tools')):
        add_tree('tools', 'tools')                    # v0.23: the release-cycle scripts (RUNBOOK.md)
    return [it for rel, it in sorted(items.items()) if not excluded(rel)]


def collect_zip(zpath, prefix):
    """The files of an existing single-zip release tpdb_vX.zip."""
    z = zipfile.ZipFile(zpath)
    items, dir_meta = [], {}
    for zi in z.infolist():
        if not zi.filename.startswith(prefix + '/'):
            sys.exit(f'{zpath}: {zi.filename} is not under {prefix}/')
        rel = zi.filename[len(prefix) + 1:]
        if zi.is_dir():
            dir_meta[rel] = (zi.date_time, zi.external_attr)
            if rel:
                items.append(Item(rel, 0, zi.date_time, zi.external_attr))
        else:
            items.append(Item(rel, zi.file_size, zi.date_time, zi.external_attr, lambda zi=zi: z.read(zi)))
    return items, dir_meta


def drop_implied_dirs(items):
    """Keep a directory item only if it is empty; the others come back as parents of their files."""
    parents = {p for it in items for p in ancestors(it.rel)}
    return [it for it in items if not it.is_dir or it.rel not in parents]


def ancestors(rel):
    parts = rel.rstrip('/').split('/')[:-1]
    return ['/'.join(parts[:i]) + '/' for i in range(1, len(parts) + 1)]


# ---------------------------------------------------------------- splitting
def group_of(rel, groups):
    for gi, (_, _, prefixes) in enumerate(groups):
        if any(rel.startswith(p) for p in prefixes):
            return gi
    return next(gi for gi, g in enumerate(groups) if not g[2])


def entry_cost(name, size):
    return size + 2 * len(name) + 100              # local + central headers: an upper bound for stored data


def chunk_stats(items, prefix):
    dirs = {prefix + '/'} | {prefix + '/' + d for it in items for d in ancestors(it.rel)}
    dirs |= {prefix + '/' + it.rel for it in items if it.is_dir}
    files = [it for it in items if not it.is_dir]
    cost = 22 + sum(entry_cost(prefix + '/' + it.rel, it.size) for it in files) + sum(entry_cost(d, 0) for d in dirs)
    return cost, len(files) + len(dirs)


def fits(items, prefix):
    cost, n = chunk_stats(items, prefix)
    return cost <= PART_MAX_BYTES * 0.98 and n <= PART_MAX_ENTRIES


def atoms(items, prefix, depth):
    """Units to pack: whole folders where they fit, otherwise their sub-folders, down to single files."""
    out, i = [], 0
    while i < len(items):
        key = '/'.join(items[i].rel.split('/')[:depth + 1])
        j = i
        while j < len(items) and '/'.join(items[j].rel.split('/')[:depth + 1]) == key:
            j += 1
        unit = items[i:j]
        if len(unit) == 1 or fits(unit, prefix):
            out.append(unit)
        else:
            out.extend(atoms(unit, prefix, depth + 1))
        i = j
    return out


def split_group(items, prefix):
    """Split one group into as few chunks as fit the limits, of even size where possible."""
    if fits(items, prefix):
        return [items]
    units = atoms(items, prefix, 0)
    for u in units:
        if not fits(u, prefix):
            sys.exit(f'{u[0].rel} alone is over the part limits')
    greedy, cur = [], []                            # fewest chunks
    for u in units:
        if cur and not fits(cur + u, prefix):
            greedy.append(cur)
            cur = []
        cur = cur + u
    greedy.append(cur)
    n = len(greedy)
    # Even out: place each unit by the midpoint of its share of the binding measure.
    cost_total, n_total = chunk_stats(items, prefix)
    by_entries = n_total / PART_MAX_ENTRIES >= cost_total / PART_MAX_BYTES
    weights = [len(u) if by_entries else sum(it.size for it in u) + 1 for u in units]
    total, acc, even = sum(weights), 0, [[] for _ in range(n)]
    for u, w in zip(units, weights):
        even[min(n - 1, int((acc + w / 2) * n / total))].extend(u)
        acc += w
    if all(c and fits(c, prefix) for c in even):
        return even
    return greedy


def plan_parts(items, prefix, tag):
    groups = groups_for(tag)
    by_group = [[] for _ in groups]
    for it in sorted(items, key=lambda it: it.rel):
        by_group[group_of(it.rel, groups)].append(it)
    plan = []
    for (name, desc, _), its in zip(groups, by_group):
        if not its:
            continue
        chunks = split_group(its, prefix)
        common = os.path.commonpath([it.rel for it in its]) if len(chunks) > 1 else ''
        base = common + '/' if common else ''
        for ci, c in enumerate(chunks):
            span = (f' ({ci + 1} of {len(chunks)}: `{c[0].rel[len(base):]}` to `{c[-1].rel[len(base):]}`)'
                    if len(chunks) > 1 else '')
            plan.append((name + (f'-{ci + 1}' if len(chunks) > 1 else ''), desc + span, c))
    width = len(str(len(plan)))
    return [(f'{prefix}_part{str(k + 1).zfill(width)}of{len(plan)}_{name}.zip', desc, c)
            for k, (name, desc, c) in enumerate(plan)]


# ---------------------------------------------------------------- writing
def is_showcase(rel):
    return re.fullmatch(r'scenes/[^/]+\.png', rel) is not None and not rel.endswith('_thumb.png')


def write_part(path, prefix, items, dir_meta, sums, loose, outdir):
    dirs = {''} | {d for it in items for d in ancestors(it.rel)} | {it.rel for it in items if it.is_dir}
    entries = sorted([(prefix + '/' + d, None) for d in dirs] +
                     [(prefix + '/' + it.rel, it) for it in items if not it.is_dir])
    tmp = path + '.partial'
    with zipfile.ZipFile(tmp, 'x', allowZip64=False) as z:
        for name, it in entries:
            if it is None:
                dt, attr = dir_meta.get(name[len(prefix) + 1:], (BUILD_TIME, (0o40755 << 16) | 0x10))
                zi = zipfile.ZipInfo(name, dt)
                zi.external_attr = attr
                z.writestr(zi, b'', compress_type=zipfile.ZIP_STORED)
                continue
            data = it.read()
            if len(data) != it.size:
                sys.exit(f'{it.rel} changed while packaging')
            sums[name] = hashlib.sha256(data).hexdigest()
            zi = zipfile.ZipInfo(name, it.date_time)
            zi.external_attr = it.attr
            if os.path.splitext(name)[1].lower() in STORE_EXT:
                z.writestr(zi, data, compress_type=zipfile.ZIP_STORED)
            else:
                z.writestr(zi, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            if it.rel in loose:
                dest = os.path.join(outdir, loose[it.rel])
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, 'xb') as f:
                    f.write(data)
                stamp = time.mktime(it.date_time + (0, 0, -1))
                os.utime(dest, (stamp, stamp))
    os.rename(tmp, path)


def human(n):
    return f'{n / 1e6:.1f} MB' if n >= 1e5 else f'{n / 1e3:.0f} KB'


def write_readme_drive(outdir, version, prefix, parts, n_files, n_showcase, src_note, made_by):
    rows = '\n'.join(f'| `{fn}` | {desc} | {human(os.path.getsize(os.path.join(outdir, fn)))} | {n:,} |'
                     for fn, desc, n in parts)
    text = f"""# TPDB v{version} on Google Drive

This folder is the TPDB v{version} release, packaged for Google Drive. Nothing is left out: the zip
parts below together hold every file of the `{prefix}/` tree ({n_files:,} files){src_note}, and
`SHA256SUMS.txt` gives a checksum for each.

## Open directly in Drive

- `README_v{version}.md`: the release README (Drive shows Markdown formatted).
- `showcase/`: the pictures of the generated set ({n_showcase} PNG files, colour and grayscale).

These are copies; the same files are also inside the parts.

## The parts

| File | Holds | Size | Entries |
|---|---|---|---|
{rows}

Each part is under {PART_MAX_BYTES // 1_000_000} MB, so Drive can virus-scan it (it does not scan files over 100 MB),
and has at most {PART_MAX_ENTRIES:,} entries. Click a part in Drive to browse it. Drive's viewer opens the PNG and SVG
pictures and the code and text files inside; `.webp`, `.json` and `.blend` files are not on Drive's preview
list and may need downloading.

## Put the full tree back together

Drive cannot unzip. Download all the parts (or the whole folder: Drive puts a folder download in a zip of
its own, so extract that first), then extract every part into the same folder. The parts do not overlap, so
the order does not matter.

macOS or Linux:

    mkdir tpdb && for f in {prefix}_part*.zip; do unzip -q "$f" -d tpdb; done
    cd tpdb && shasum -a 256 -c ../SHA256SUMS.txt      # optional check; on Linux: sha256sum -c

Windows (PowerShell):

    Get-ChildItem {prefix}_part*.zip | ForEach-Object {{ Expand-Archive $_ -DestinationPath tpdb -Force }}

Any system with Python 3:

    python3 -c "import glob, zipfile; [zipfile.ZipFile(f).extractall('tpdb') for f in sorted(glob.glob('{prefix}_part*.zip'))]"

The result is `tpdb/{prefix}/`, the tree a single `{prefix}.zip` would have held.

{made_by}
"""
    with open(os.path.join(outdir, 'README_DRIVE.md'), 'x') as f:
        f.write(text)


# ---------------------------------------------------------------- verification
def reference_from_items(items, prefix):
    files = {prefix + '/' + it.rel: hashlib.sha256(it.read()).hexdigest() for it in items if not it.is_dir}
    dirs = {prefix + '/'} | {prefix + '/' + d for it in items for d in ancestors(it.rel)}
    dirs |= {prefix + '/' + it.rel for it in items if it.is_dir}
    return files, dirs


def reference_from_sums(outdir, prefix):
    files = {}
    with open(os.path.join(outdir, 'SHA256SUMS.txt')) as f:
        for line in f:
            h, name = line.rstrip('\n').split('  ', 1)
            files[name] = h
    dirs = {prefix + '/'} | {prefix + '/' + d for n in files for d in ancestors(n[len(prefix) + 1:])}
    return files, dirs


def extra_ids(extra):
    ids, i = [], 0
    while i + 4 <= len(extra):
        ids.append(int.from_bytes(extra[i:i + 2], 'little'))
        i += 4 + int.from_bytes(extra[i + 2:i + 4], 'little')
    return ids


def verify(outdir, prefix, version, ref_files, ref_dirs, extra_dirs_ok=False):
    """Check every part: it opens, tests clean, meets the limits, and the parts together hold exactly
    the reference files (paths and bytes), with no file in two parts. Returns the list of problems."""
    problems = []
    parts = sorted(f for f in os.listdir(outdir) if re.fullmatch(re.escape(prefix) + r'_part\d+of\d+_.+\.zip', f))
    if not parts:
        return ['no parts found']
    seen, seen_dirs = {}, set()
    print(f'\n{"part":48s} {"bytes":>11s} {"entries":>7s} {"files":>6s} {"depth":>5s}  tests')
    for fn in parts:
        p = os.path.join(outdir, fn)
        size = os.path.getsize(p)
        try:
            z = zipfile.ZipFile(p)
            bad = z.testzip()
        except Exception as e:                       # noqa: BLE001
            problems.append(f'{fn}: does not open: {e}')
            continue
        infos = z.infolist()
        if bad:
            problems.append(f'{fn}: CRC error in {bad}')
        if shutil.which('unzip'):
            r = subprocess.run(['unzip', '-tqq', p], capture_output=True, text=True)
            if r.returncode != 0:
                problems.append(f'{fn}: unzip -t failed: {r.stdout}{r.stderr}')
        with open(p, 'rb') as f:
            f.seek(max(0, size - 70_000))
            if b'PK\x06\x06' in f.read():
                problems.append(f'{fn}: uses zip64')
        if size > PART_MAX_BYTES or size >= DRIVE_SCAN_LIMIT:
            problems.append(f'{fn}: {size} bytes is over the {PART_MAX_BYTES} limit')
        if len(infos) > PART_MAX_ENTRIES:
            problems.append(f'{fn}: {len(infos)} entries is over the {PART_MAX_ENTRIES} limit')
        depth = 0
        for zi in infos:
            n = zi.filename
            if not n.startswith(prefix + '/') or '..' in n.split('/') or not n.isascii() or '\\' in n:
                problems.append(f'{fn}: bad path {n}')
            if zi.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED) or zi.flag_bits & 0x1:
                problems.append(f'{fn}: {n} is not plain stored/deflate')
            if 0x0001 in extra_ids(zi.extra):
                problems.append(f'{fn}: {n} has a zip64 field')
            depth = max(depth, n.rstrip('/').count('/'))
            if zi.is_dir():
                seen_dirs.add(n)
                continue
            if n in seen:
                problems.append(f'{n} is in both {seen[n][0]} and {fn}')
            seen[n] = (fn, hashlib.sha256(z.read(zi)).hexdigest())
        nfiles = sum(1 for zi in infos if not zi.is_dir())
        print(f'{fn:48s} {size:11,d} {len(infos):7d} {nfiles:6d} {depth:5d}  '
              f'{"ok" if not bad else "FAIL"}')
    missing = sorted(set(ref_files) - set(seen))
    extra = sorted(set(seen) - set(ref_files))
    differ = sorted(n for n in set(seen) & set(ref_files) if seen[n][1] != ref_files[n])
    for label, names in (('missing from the parts', missing), ('not in the release', extra),
                         ('bytes differ', differ)):
        if names:
            problems.append(f'{len(names)} files {label}: {names[:5]}')
    if ref_dirs is not None and seen_dirs != ref_dirs and not extra_dirs_ok:
        problems.append(f'folders differ: missing {sorted(ref_dirs - seen_dirs)[:5]}, '
                        f'extra {sorted(seen_dirs - ref_dirs)[:5]}')
    # loose copies and the checksum list
    loose = {f'README_v{version}.md': prefix + '/README.md'}
    sdir = os.path.join(outdir, 'showcase')
    if os.path.isdir(sdir):
        for f in os.listdir(sdir):
            loose[f'showcase/{f}'] = f'{prefix}/scenes/{f}'
    for lf, ref in loose.items():
        p = os.path.join(outdir, lf)
        if not os.path.exists(p):
            problems.append(f'{lf} is missing')
        elif ref not in ref_files or hashlib.sha256(open(p, 'rb').read()).hexdigest() != ref_files[ref]:
            problems.append(f'{lf} does not match {ref}')
    sums, _ = reference_from_sums(outdir, prefix)
    if sums != ref_files:
        problems.append('SHA256SUMS.txt does not match the release')
    print(f'\n{len(parts)} parts, {len(seen):,} files ({len(ref_files):,} in the release), '
          f'{len(seen_dirs):,} folders ({len(ref_dirs):,} in the release), '
          f'{sum(os.path.getsize(os.path.join(outdir, f)) for f in parts):,} bytes in all; '
          f'{len(loose)} loose copies checked')
    return problems


# ---------------------------------------------------------------- main
BUILD_TIME = time.localtime()[:6]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('version', help='release version, e.g. 0.18')
    ap.add_argument('--tag', help='folder suffix (default: the version without dots, e.g. 018 for '
                                  'out018/, lib018/, gallery018/, site018/)')
    ap.add_argument('--from-zip', metavar='ZIP', help='take the files from an existing single-zip release '
                                                      'instead of the working tree')
    ap.add_argument('--scenes', default='scenes', help='folder packaged as scenes/ (default: scenes)')
    ap.add_argument('--probes', default='probes', help='folder packaged as probes/ (default: probes)')
    ap.add_argument('--out', help='output folder (default: release_v<version>_drive next to this script); '
                                  'must not exist or be empty')
    ap.add_argument('--single', action='store_true', help='write the whole release as one zip, '
                    'tpdb_v<version>.zip next to this script (or --out, a file path), and verify it')
    ap.add_argument('--verify-only', action='store_true', help='only check an existing output folder, against '
                    '--from-zip if given, otherwise against its SHA256SUMS.txt')
    a = ap.parse_args()
    if not re.fullmatch(r'\d+(\.\d+)+[a-z0-9]*', a.version):
        sys.exit(f'bad version {a.version!r}')
    tag = a.tag or a.version.replace('.', '')
    prefix = f'tpdb_v{a.version}'
    outdir = os.path.abspath(a.out or os.path.join(HERE, f'release_v{a.version}_drive'))
    try:
        if hasattr(os, "nice"):
            os.nice(10)                                   # the machine is shared; stay out of the way
    except OSError:
        pass

    if a.single:
        build_single(a, tag, prefix)
        return

    if a.verify_only:
        if a.from_zip:
            items, _ = collect_zip(a.from_zip, prefix)
            ref_files, ref_dirs = reference_from_items(items, prefix)
        else:
            ref_files, ref_dirs = reference_from_sums(outdir, prefix)
        problems = verify(outdir, prefix, a.version, ref_files, ref_dirs, extra_dirs_ok=not a.from_zip)
        report(problems)
        return

    if os.path.exists(outdir) and os.listdir(outdir):
        sys.exit(f'{outdir} exists and is not empty; choose another --out (nothing is overwritten)')
    t0 = time.time()
    if a.from_zip:
        items, dir_meta = collect_zip(a.from_zip, prefix)
        src_note = f', as in `{os.path.basename(a.from_zip)}`'
    else:
        items, dir_meta = collect_tree(HERE, a.version, tag, a.scenes, a.probes), {}
        src_note = ''
    items = drop_implied_dirs(items)
    parts = plan_parts(items, prefix, tag)
    loose = {'README.md': f'README_v{a.version}.md'}
    loose.update({it.rel: 'showcase/' + it.rel.split('/')[-1] for it in items if is_showcase(it.rel)})
    os.makedirs(outdir, exist_ok=True)
    sums, written = {}, []
    for fn, desc, chunk in parts:
        write_part(os.path.join(outdir, fn), prefix, chunk, dir_meta, sums, loose, outdir)
        written.append((fn, desc, len(zipfile.ZipFile(os.path.join(outdir, fn)).infolist())))
        print(f'wrote {fn}', flush=True)
    with open(os.path.join(outdir, 'SHA256SUMS.txt'), 'x') as f:
        f.writelines(f'{h}  {n}\n' for n, h in sorted(sums.items()))
    n_files = sum(1 for it in items if not it.is_dir)
    made_by = (f'Made by `package_release.py {a.version} --from-zip {os.path.basename(a.from_zip)}`; '
               'see that script for the limits used.' if a.from_zip else
               f'Made by `package_release.py {a.version}` (the script is in part 1); see it for the limits used.')
    write_readme_drive(outdir, a.version, prefix, written, n_files, len(loose) - 1, src_note, made_by)
    print(f'built {outdir} in {time.time() - t0:.0f} s; verifying against the source')

    # Verify against the source read a second time, independently of what was written.
    if a.from_zip:
        ref_items, _ = collect_zip(a.from_zip, prefix)
        ref_files, ref_dirs = reference_from_items(ref_items, prefix)
    else:
        ref_files, ref_dirs = reference_from_items(items, prefix)
    report(verify(outdir, prefix, a.version, ref_files, ref_dirs))


def build_single(a, tag, prefix):
    """The whole release as one zip, then every entry read back and checked against the source."""
    zpath = os.path.abspath(a.out or os.path.join(HERE, f'{prefix}.zip'))
    if a.verify_only:
        items = drop_implied_dirs(collect_tree(HERE, a.version, tag, a.scenes, a.probes))
        report_single(verify_single(zpath, prefix, items))
        return
    if os.path.exists(zpath):
        sys.exit(f'{zpath} exists; choose another --out (nothing is overwritten)')
    t0 = time.time()
    if a.from_zip:
        sys.exit('--single builds from the working tree; --from-zip is for the Drive parts')
    items = drop_implied_dirs(collect_tree(HERE, a.version, tag, a.scenes, a.probes))
    sums = {}
    write_part(zpath, prefix, items, {}, sums, {}, os.path.dirname(zpath))
    print(f'wrote {zpath} ({human(os.path.getsize(zpath))}, {len(sums):,} files) in {time.time() - t0:.0f} s; '
          'verifying against the source', flush=True)
    report_single(verify_single(zpath, prefix, items))


def verify_single(zpath, prefix, items):
    problems = []
    ref = {prefix + '/' + it.rel: hashlib.sha256(it.read()).hexdigest() for it in items if not it.is_dir}
    ref_dirs = {prefix + '/' + it.rel for it in items if it.is_dir}
    z = zipfile.ZipFile(zpath)
    bad = z.testzip()
    if bad:
        problems.append(f'CRC error in {bad}')
    got = {}
    for zi in z.infolist():
        if zi.is_dir():
            continue
        got[zi.filename] = hashlib.sha256(z.read(zi)).hexdigest()
    for n in sorted(set(ref) - set(got)):
        problems.append(f'missing from the zip: {n}')
    for n in sorted(set(got) - set(ref)):
        problems.append(f'not in the release: {n}')
    for n in sorted(set(ref) & set(got)):
        if ref[n] != got[n]:
            problems.append(f'differs from the source: {n}')
    names = {zi.filename for zi in z.infolist()}
    for d in sorted(ref_dirs - names):
        problems.append(f'empty folder missing: {d}')
    if shutil.which('unzip'):
        r = subprocess.run(['unzip', '-tq', zpath], capture_output=True, text=True)
        if r.returncode != 0:
            problems.append('unzip -t: ' + (r.stdout + r.stderr).strip()[:300])
    if not problems:
        print(f'{len(got):,} files in the zip, {len(ref):,} in the release')
    return problems


def report_single(problems):
    if problems:
        print('\nVERIFY FAILED:')
        for p in problems[:50]:
            print('  ' + p)
        sys.exit(1)
    print('\nVERIFY OK: the zip opens and tests clean (zipfile and unzip -t) and holds exactly the release '
          'files, byte for byte.')


def report(problems):
    if problems:
        print('\nVERIFY FAILED:')
        for p in problems:
            print('  ' + p)
        sys.exit(1)
    print('\nVERIFY OK: every part opens and tests clean (zipfile and unzip -t), meets the size and entry '
          'limits, and the parts together hold exactly the release files, byte for byte.')


if __name__ == '__main__':
    main()
