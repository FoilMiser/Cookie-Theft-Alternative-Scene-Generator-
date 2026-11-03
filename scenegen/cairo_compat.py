"""cairosvg draws through cairocffi, and cairocffi needs a native libcairo, which Windows does not ship.

Where that library is missing, install() hands cairosvg the cairo built into the pycairo wheel under
the name cairocffi; the two share an API, apart from the attribute cairosvg sets on an image surface.
Where libcairo is there (Linux), nothing changes. Import this before cairosvg.
"""
import sys
import types


def install():
    try:
        import cairocffi  # noqa: F401
        return
    except OSError:
        pass
    import cairo

    class PngSurface:
        """A surface read from a PNG. cairosvg hangs its pattern on it, and pycairo's surfaces take no new attributes."""

        def __init__(self, surface):
            self.surface = surface

        def __getattr__(self, name):
            return getattr(self.surface, name)

    class ImageSurface:
        def __new__(cls, *args):
            return cairo.ImageSurface(*args)

        @staticmethod
        def create_from_png(f):
            return PngSurface(cairo.ImageSurface.create_from_png(f))

    def SurfacePattern(surface):
        return cairo.SurfacePattern(getattr(surface, "surface", surface))

    shim = types.ModuleType("cairocffi")
    shim.__dict__.update({k: getattr(cairo, k) for k in dir(cairo) if not k.startswith("__")})
    shim.ImageSurface = ImageSurface
    shim.SurfacePattern = SurfacePattern
    sys.modules["cairocffi"] = shim


install()
