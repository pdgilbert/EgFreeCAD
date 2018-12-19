
.. testsetup::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 
   
   O = Vector(0,0,0)
   X = Vector(1,0,0)
   Y = Vector(0,1,0)
   Z = Vector(0,0,1)


.. index:: Box
Box
---


The function :py:func:`areEqual` compares two shapes and returns :py:const:`True` if
they are equal and :py:const:`False` otherwise. Here it is used to compare boxes one with x, y, z
dimensions 1x100x10 and the other 1x100x9. These boxes are created in the default position, with one corner at the origin and dimensions extending in the positive direction. 

.. testcode::

   print(areEqual(Part.makeBox(1,100,10), Part.makeBox(1,100,10)))
   print(areEqual(Part.makeBox(1,100,10), Part.makeBox(1,100,9)))

.. testoutput::

   True
   False

The function :py:func:`isSubset` compares two shapes and returns :py:const:`True` if
the first is a subset of the second, and :py:const:`False` otherwise. Equal is 
considered to be a subset, that is, the subset need not be a strict subset, so the
result is :py:const:`True` if the objects are equal.

.. testcode::

   print(isSubset(Part.makeBox(1,100,10), Part.makeBox(1,100,10)))
   print(isSubset(Part.makeBox(1,100,9),  Part.makeBox(1,100,10)))
   print(isSubset(Part.makeBox(1,100,10), Part.makeBox(1,100,9)))

.. testoutput::

   True
   True
   False

These  have no output

.. testcode::

   testEqual(Part.makeBox(1,100,10), Part.makeBox(1,100,10)) 
   testNotEqual(Part.makeBox(1,100,10), Part.makeBox(1,100,9))

.. testoutput::

and these  raise exceptions

.. testcode::

   testNotEqual(Part.makeBox(1,100,10), Part.makeBox(1,100,10)) 
   testEqual(Part.makeBox(1,100,10), Part.makeBox(1,100,9))

.. testoutput::

    Traceback (most recent call last):
    ...
    Exception: Objects are equal
    Traceback (most recent call last):
    ...
    Exception: Objects are not equal


.. testcode::

   C1 = Part.Arc( Vector(0,10,0), Vector(-10,0,0), Vector(0,-10,0))
   C2 = Part.Arc(Vector(30,10,0), Vector(40,0,0),  Vector(30,-10,0))
   L1 = Part.LineSegment(Vector(0,10,0), Vector(30,10,0))
   L2 = Part.LineSegment(Vector(30,-10,0), Vector(0,-10,0)) 
   S1 = Part.Shape([C1,L1,C2,L2]) 
   
   W = Part.Wire(S1.Edges)
   P = W.extrude(Vector(0,0,10)) 
   # Part.show(P) 
   
   testEqual(P, W.extrude(Vector(0,0,10)))
   testNotEqual(P, W.extrude(Vector(0,0,20))) 

.. testoutput::
