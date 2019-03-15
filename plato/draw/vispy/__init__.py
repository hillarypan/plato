"""
The vispy backend uses `vispy <http://vispy.org/>`_ to render shapes
interactively using openGL. It supports both desktop use with a
variety of GUI backends and use inline in jupyter notebooks.

Select the backend to use with the standard vispy mechanism::

  import vispy, vispy.app
  # use in ipython notebook
  vispy.app.use_app('ipynb_webgl')
  # use pyside2
  vispy.app.use_app('pyside2')
  scene = plato.draw.vispy.Scene(...)
  scene.show()
  vispy.app.run()

"""

from .Scene import Scene

from .Box import Box
from .Arrows2D import Arrows2D
from .Disks import Disks
from .DiskUnions import DiskUnions
from .Polygons import Polygons
from .Spheropolygons import Spheropolygons
from .Voronoi import Voronoi
from .Lines import Lines
from .Spheres import Spheres
from .SpherePoints import SpherePoints
from .SphereUnions import SphereUnions
from .Mesh import Mesh
from .ConvexPolyhedra import ConvexPolyhedra
from .ConvexSpheropolyhedra import ConvexSpheropolyhedra
