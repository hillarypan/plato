from ... import draw
from .internal import GLPrimitive, GLShapeDecorator
from .Lines import Lines

@GLShapeDecorator
class Box(draw.Box, Lines):
    __doc__ = draw.Box.__doc__

    def __init__(self, *args, **kwargs):
        GLPrimitive.__init__(self)
        draw.Box.__init__(self, *args, **kwargs)
