
.. index:: Circle

Circle
------

The default :py:func:`Part.makeCircle(r)` produces a circular line on the
XY plane with radius r. (A one dimensional object embedded in a two dimensional space).
 
.. testcode::

   c = Part.makeCircle(5)
   #Part.show(c)
   c2 = c.copy()
   testEqual(c, c2)
   testNotEqual(c, Part.makeCircle(5.5))

A circle has attributes that can be checked as follows. 
 
.. testcode::
  
   if c.Curve.Radius != 5.0 : raise Exception("Circle radius should be 5.0.")

   if c.Curve.Center != o : raise Exception("Circle Center should be origin.")
   
   if c.Curve.Axis   != z   : raise Exception("Circle axis should be Z axis.")
      
Within its plane, a circle is symmetic around its center, so this circle can be
rotated any number of degrees around the Z-axis and produces an equal object

.. testcode::

   c2.rotate(o, z, 180)
   testEqual(c, c2)
   c2.rotate(o, z, 90)
   testEqual(c, c2)

but translation produces an object that is not equal.

.. testcode::

   c2.translate(Vector(0,0,10))
   testNotEqual(c, c2)


This circle is at origin, 
normal to z axis. A circle has one edge and no faces, properties that can
be checked. 

.. testcode::

   C = Part.makeCircle(10)
   
   if 1 != len(C.Edges): raise Exception("Circle should have 1 edge.")
   
   if 0 != len(C.Faces): raise Exception("Circle should have no faces.")
   
   if 0 != len(C.Solids): raise Exception("Circle should have no solids.")

When constructing a face (two dimensional object) from a circle (one 
dimensional object) it is uually important that the circle is not a partial 
circle, that is, it forms a complete closed loop. This is also a property 
that can be checked. 

.. testcode::

   if not C.isClosed(): raise Exception("Object C is not a closed loop")

A face can be constructed by filling in the circle. For some reason this 
needs to be converted to a wire first. 

.. testcode::

   C2 = Part.Face(Part.Wire(C))

   if 1 != len(C2.Faces): raise Exception("Circle with interior should have 1 face.")

   if 0 != len(C.Solids): raise Exception("Circle with interior should have no solids.")
  
   #Part.show(C2) 

STILL DON'T UNDERSTAND WHAT makeShell DOES
.. testcode::

   C2x = Part.makeShell(C2.Faces)
