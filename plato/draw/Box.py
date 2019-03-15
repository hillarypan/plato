import itertools
import numpy as np
from .Lines import Lines
from .. import math
from .internal import attribute_setter, ShapeDecorator, ShapeAttribute

@ShapeDecorator
class Box(Lines):
    """Create a box primitive to draw the frame

    Example: prim = draw.Box((Lx,Ly,Lz,xy,xz,yz), width, color)
    
    """

    def __init__(self, *args, **kwargs):
        # argument order: box, width, color
        # Box tuple: (Lx, Ly, Lz, xy, xz, yz)
        box, width, color = None, None, None
        
        if len(args) == 0:
            box = kwargs['box']  
            width = kwargs['width']
            color = kwargs['color']

        elif len(args) == 1:
            box = args[0]
            width = kwargs['width']
            color = kwargs['color']
        
        elif len(args) == 2:
            box = args[0]
            width = args[1]
            color = kwargs['color']

        else:
            box = args[0]
            width = args[1]
            color = args[2]            

        fractions = np.array([[0,0,0], [1,0,0], [0,1,0], [0,0,1], [1,1,0], [1,0,1], [0,1,1], [1,1,1]])
        coordinates = math.fractions_to_coordinates(box, fractions)
        
        start_points = [coordinates[0], coordinates[0], coordinates[0], coordinates[1], coordinates[1], coordinates[2], 
            coordinates[2], coordinates[3], coordinates[3], coordinates[4], coordinates[5], coordinates[6]]
        end_points = [coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5], coordinates[4],
            coordinates[6], coordinates[5], coordinates[6], coordinates[7], coordinates[7], coordinates[7]]

        kwargs_ = {}
        kwargs_['colors'] = [color]*len(start_points)
        kwargs_['widths'] = [width]*len(start_points)
        kwargs_['start_points'] = start_points
        kwargs_['end_points'] = end_points
        super(Lines, self).__init__(**kwargs_)


    
