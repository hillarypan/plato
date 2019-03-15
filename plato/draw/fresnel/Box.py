import fresnel
from ... import draw
from .Lines import Lines
from .FresnelPrimitive import FresnelPrimitive

class Box(draw.Box, Lines):
    __doc__ = draw.Box.__doc__

    def __init__(self, *args, material=None, **kwargs):
        FresnelPrimitive.__init__(self, *args, material, **kwargs)
        if material is None:
            self._material.solid = 1
        draw.Box.__init__(self, *args, **kwargs)
