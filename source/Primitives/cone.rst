
.. testsetup::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 
   
   O = Vector(0,0,0)
   X = Vector(1,0,0)
   Y = Vector(0,1,0)
   Z = Vector(0,0,1)


.. index:: Cone
Cone
----

Make a cone with base radius 5, top radius 10, and height 15

.. testcode::

   cone  = Part.makeCone(5, 10.0, 15)
   #Part.show(cone)
   cone2  = cone.copy()
   
   testEqual(cone, cone2)

.. testoutput::
   
The cone is symmetic under Z axis rotation

.. testcode::

   cone2.rotate(O, Z, 20)
   testEqual(cone, cone2)

.. testoutput::
 
but not symmetic under X axis rotation

.. testcode::

   cone2.rotate(O, X, 20)
   testNotEqual(cone, cone2)
   
   cone2.translate(Vector(0,0,10))
   testNotEqual(cone, cone2)

.. testoutput::
   
Translation and rotation can be undone, but if not undone in the reverse order
then the axis for the rotation needs to be modified to the center of the cone.

.. testcode::

   cone2.rotate(Vector(0,0,10), X, -20)
   cone2.translate(Vector(0,0,-10))
   testEqual(cone, cone2)
   
   c  = Part.makeCylinder(5, 10.0, O, Z, 360)
   c2 = c.copy()
   testEqual(c, c2) 
   
   c2.rotate(O, Z, 180)
   testEqual(c, c2)
   
   c2.rotate(O, Vector(1,0,0), 180)
   c2.translate(Vector(0,0,10))
   testEqual(c, c2)
   
   c2 = c.copy()
   testEqual(c, c2)
   
   c2.rotate(O, Z, 90)
   testEqual(c, c2) 
   
   c2.rotate(O, Vector(1,0,0), 90)
   testNotEqual(c, c2)

.. testoutput::
   
