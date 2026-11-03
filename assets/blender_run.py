"""Let a bpy script run with plain `python`, with the bpy module or with an installed Blender.

    import blender_run; blender_run.ensure(__file__)    # before `import bpy`

Where the bpy module is there, nothing happens. Where it is not (bpy has wheels for one Python version only,
3.13 for Blender 5.2), the script runs again inside Blender: TPDB_BLENDER, else `blender` on the PATH, else the
newest Blender under Program Files. Inside Blender sys.argv is put back to what the script would see under
python, so `python build_cast.py out024` means the same either way.
"""
import glob
import os
import shutil
import subprocess
import sys


def find_blender():
    exe = os.environ.get("TPDB_BLENDER") or shutil.which("blender")
    if exe:
        return exe
    for base in (os.environ.get("ProgramFiles"), os.environ.get("ProgramW6432")):
        found = sorted(glob.glob(os.path.join(base or "", "Blender Foundation", "Blender *", "blender.exe")))
        if base and found:
            return found[-1]
    return None


def ensure(script):
    script = os.path.abspath(script)
    try:
        import bpy  # noqa: F401
    except ModuleNotFoundError:
        exe = find_blender()
        if not exe:
            raise
        sys.exit(subprocess.run([exe, "-b", "--factory-startup", "--python-exit-code", "1", "-P", script, "--", *sys.argv[1:]]).returncode)
    if "--" in sys.argv:
        sys.argv = [script] + sys.argv[sys.argv.index("--") + 1:]
