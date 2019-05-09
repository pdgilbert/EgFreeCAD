
.. index:: Sphere

Sphere
------

FreeCAD :py:func:`Part.Sphere()` produces a two dimensional surface (face) embedded
in three dimensional space. (The topology of the object is S<sup>2</sup> ).

.. testcode::

   s  = Part.Sphere().toShape()  
   #Part.show(s)
   print(s.ShapeType)

.. testoutput::

   Face

Below concentrates on solid objects, notice the difference between 
:py:func:`Part.Sphere()` and :py:func:`Part.makeSphere()`.
Solid objects will be more interesting for things like 3D printing.

The default :py:func:`Part.makeSphere(r)` produces a solid sphere centered
at the origin with radius r. This is a three dimensional object. 
A sphere can be rotated in any direction about its
center and produce an equal object, but translation gives an object that is 
not equal.

.. testcode::

   s  = Part.makeSphere(10)
   #Part.show(s)
   print(s.ShapeType)

   s2 = Part.makeSphere(10)
   s2.rotate(o, z, 180)   
   testEqual(s, s2)

   s2.translate(Vector(0,0,10))
   testNotEqual(s, s2)

   testNotEqual(s, Part.makeSphere(9))

.. testoutput::

   Solid


A sphere object has edges, faces and solids.

.. testcode::

   print(len(s.Edges))
   print(len(s.Faces))
   print( len(s.Solids))

.. testoutput::

   3
   1
   1


A sphere can also be constructed by revolving a circle.
A full circle revolved 360 degrees covers the sphere twice over, which causes
anomolies according to the help for .revolve().  Revolve 180 degrees is better,
and even better is revolving a half circle 360 degrees. (This is an algorithmic
improvement, not a theoretical difference.)

The next works well (but I'm just guessing that toShape arguments
mean take the sweep from pi/2 to 3pi/2.)  LastParameter for a circle 
is 2*pi radians.

(There is an anomaly here. makeSphere gives ShapeType Solid' whereas Circle
gives ShapeType 'Face', but cutting leaves an empty object. See Puzzles.)

.. testcode::

   s  = Part.makeSphere(10)

   c10 = Part.Circle(o, z, 10)
   testEqual(c10.toShape(), Part.makeCircle(10))

   # Part.show(c10.toShape())   
   # Part.show(Part.makeCircle(10))   

   zc = c10.toShape()
   zz = Part.makeCircle(10).revolve(o, x, 180)  
   # Part.show(zz)   # does not show

   zz = c10.toShape().revolve(o, x, 180)  
   # Part.show(zz)   # does not show
   # Part.show(zz.cut(Part.makeBox(10,10,10)))   # does not show

and more

.. testcode::

   h10 = c10.toShape(c10.LastParameter/4, 3*c10.LastParameter/4)
   # Part.show(h10)   # unfilled half circle
   
   f10 = Part.makeFilledFace(c10.toShape().Edges)
   # Part.show(f10)  # filled disk
   s10 = f10.revolve(o, x, 180)  
   s10 = f10.revolve(o, y, 180)  
   s10 = f10.revolve(o, z, 180)  
   # Part.show(s10)     # still filled disk

#f = Part.makeFilledFace(s10.Edges)
#r10 = s10.revolve(o, y, 360)
# Part.show(r10)
#if  r10.ShapeType == 'Face': raise Exception("Sphere is hollow.")

and more

.. testcode::

   s  = Part.makeSphere(10)
   # Part.show(s.cut(Part.makeBox(10,10,10)))
   # Part.show(r10.cut(Part.makeBox(10,10,10)))
   print(s.ShapeType)
   #   print(r10.ShapeType)
   
   testEqual(s, s10)
   print(areEqual(s, s10))

.. testoutput::

   Solid
   True


ABOVE NEEDS TO BE FIXED SINCE so not hollow
