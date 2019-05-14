
.. index:: Circle

Circle
------

The default :py:func:`Part.makeCircle(r)` produces a circular line on the
XY plane with radius r. (A one dimensional object embedded in a two 
dimensional plane in three dimensional space). 
The function :py:func:`Part.Circle(r)` does essentially the same thing but takes
arguments for the center, normal and radius, and has to be converted to a 
shape object.
 
.. testcode::

   c = Part.makeCircle(5)
   #Part.show(c)
   c2 = c.copy()
   testEqual(c, c2)
   testNotEqual(c, Part.makeCircle(6))

   testEqual(c, Part.Circle(o, z, 5).toShape() )

A circle has attributes that can be checked as follows. 
 
.. testcode::
  
   print(c.Curve.Radius == 5.0)
   print(c.Curve.Center == o )
   print(c.Curve.Axis   == z )

.. testoutput::

   True
   True
   True

Within its plane, a circle is symmetic around its center, so this circle can be
rotated any number of degrees around the Z-axis and produces an equal object

.. testcode::

   c2.rotate(o, z, 180)
   testEqual(c, c2)
   c2.rotate(o, z, 90)
   testEqual(c, c2)
   c2.rotate(o, z, 33)
   testEqual(c, c2)

but translation produces an object that is not equal.

.. testcode::

   c2.translate(Vector(0,0,10))
   testNotEqual(c, c2)


This circle is centered at the origin and is on the plane
normal to z axis. A circle has one edge and no faces, properties that can
be checked. 

.. testcode::

   C = Part.makeCircle(10)
   print( len(C.Edges) )
   print( len(C.Faces) )
   print( len(C.Solids) )

.. testoutput::

   1
   0
   0

When constructing a face (two dimensional object) from a circle (one 
dimensional object) it is usually important that the circle is not a partial 
circle, that is, it forms a complete closed loop. This is also a property 
that can be checked. 

.. testcode::

   print( C.isClosed() )

.. testoutput::

   True

A face can be constructed by filling in the circle. For some reason this 
needs to be converted to a wire first. 

.. testcode::

   C2 = Part.Face(Part.Wire(C))
   print( C2.ShapeType )
   print( len(C2.Faces) )
   print( len(C2.Solids) )
   #Part.show(C2) 

.. testoutput::

   Face
   1
   0

