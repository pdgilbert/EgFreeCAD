
.. testsetup::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 
   
   O = Vector(0,0,0)
   X = Vector(1,0,0)
   Y = Vector(0,1,0)
   Z = Vector(0,0,1)

.. index:: Polygon

Polygon
-------

Make a line betweeen two points

.. testcode::

   line  = Part.makeLine((0.5, 0.5, 0.5),(1, 2, 3))
   line2 = line.copy()
   testEqual(line, line2)

Make a plane (rectangle) from origin 2 units in x direction and 4 in Y direction.

.. testcode::

   plane = Part.makePlane(2, 4)

   # there seems to be a bug here?
   #plane2 = plane.rotate(O, Z, 20)
   #Part.show(plane2)
   
   plane2 = plane.copy()
   testEqual(plane, plane2)
   
   plane2.rotate(O, Z, 20)
   testNotEqual(plane, plane2)

Make a polygon of a list of points

.. testcode::

   poly  = Part.makePolygon([O, X, Y, Z])
   poly2 = poly.copy()
   testEqual(poly, poly2)
   
   poly2.rotate(O, Z, 20)
   testNotEqual(poly, poly2)
