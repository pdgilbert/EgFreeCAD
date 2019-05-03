
.. index:: Box

Box
---

The function :py:func:`areEqual` compares two shapes and returns :py:const:`True` if
they are equal and :py:const:`False` otherwise. Here it is used to compare solid boxes, one with x, y, z
dimensions 1x100x10 and the other 1x100x9. These boxes are created in the default position, with one corner at the origin and dimensions extending in the positive direction. 

.. testcode::

   box1 = Part.makeBox(1, 100, 10)
   print(areEqual(box1, Part.makeBox(1, 100, 10)))
   print(areEqual(box1, Part.makeBox(1, 100, 9)))

.. testoutput::

   True
   False

The function :py:func:`isSubset` compares two shapes and returns :py:const:`True` if
the first is a subset of the second, and :py:const:`False` otherwise. Equal is 
considered to be a subset, that is, the subset need not be a strict subset, so the
result is :py:const:`True` if the objects are equal.

.. testcode::

   print(isSubset(Part.makeBox(1, 100, 10), box1))
   print(isSubset(Part.makeBox(1, 100, 9),  box1))
   print(isSubset(box1, Part.makeBox(1, 100, 9)))

.. testoutput::

   True
   True
   False

These  have no output

.. testcode::

   testEqual(box1, Part.makeBox(1, 100, 10)) 
   testNotEqual(box1, Part.makeBox(1, 100, 9))

and these  raise exceptions

.. testcode::

   testNotEqual(box1, Part.makeBox(1, 100, 10)) 
   testEqual(box1, Part.makeBox(1, 100, 9))

.. testoutput::

    Traceback (most recent call last):
    ...
    Exception: Objects are equal
    Traceback (most recent call last):
    ...
    Exception: Objects are not equal

A solid box can also be constructed by extruding a square made from line
segments starting at the origin:

.. testcode::

   L1 = Part.LineSegment(o, x)
   L2 = Part.LineSegment(x, Vector(1, 100, 0)) 
   L3 = Part.LineSegment(Vector(1, 100,0), Vector(0, 100, 0))
   L4 = Part.LineSegment(Vector(0, 100, 0), o) 
   sq = Part.Shape([L1, L2, L3, L4]) 
   
   w = Part.Wire(sq.Edges)
   box2 = w.extrude(Vector(0,0,10)) 
   # Part.show(box2) 
   
   print(areEqual(box1, box2))
   testEqual(box1, box2,)

.. testoutput::

   True
