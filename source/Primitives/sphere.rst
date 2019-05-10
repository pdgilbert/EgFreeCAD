
.. index:: Sphere

Sphere
------

FreeCAD :py:func:`Part.Sphere()` produces a two dimensional surface (face) embedded
in three dimensional space. (The topology of the object is S<sup>2</sup> ).
The fact that this sphere is hollow can be seen by displaying with a piece cut out.

.. testcode::

   s2 = Part.Sphere().toShape()  
   #Part.show(s2)
   print(s2.ShapeType)
   
   # Part.show(s2.cut(Part.makeBox(10,10,10)))

.. testoutput::

   Face

Below concentrates on solid objects, notice the difference between 
:py:func:`Part.Sphere()` which is hollow and :py:func:`Part.makeSphere()`
which is solid.
Solid objects will be more interesting for things like 3D printing.

The default :py:func:`Part.makeSphere(r)` produces a solid sphere centered
at the origin with radius r. This is a three dimensional object. 
A sphere can be rotated in any direction about its
center and produce an equal object, but translation gives an object that is 
not equal.

.. testcode::

   s = Part.makeSphere(10)
   #Part.show(s.cut(Part.makeBox(10,10,10)))
   print(s.ShapeType)

   sr = Part.makeSphere(10)
   sr.rotate(o, z, 180)   
   testEqual(s, sr)

   sr.translate(Vector(0,0,10))
   testNotEqual(s, sr)

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
anomolies according to the help for .revolve().  Revolve 180 degrees is better. 

(There is an anomaly here. makeSphere gives ShapeType Solid' whereas Circle
gives ShapeType 'Face', but cutting leaves an empty object. See Puzzles.)

REVOLVE A FULL CIRCLE SEEMS BROKEN. THIS DOES NOT WORK.

.. testcode::

   c10 = Part.Circle(o, z, 10)

   # Part.show(c10.toShape())   
   # Part.show(Part.makeCircle(10))   

   c10.toShape().revolve(o, x, 180).isValid()  # False
   c10.toShape().revolve(o, y, 180).isValid()  # False
   c10.toShape().revolve(o, z, 180).isValid()  # True but flat (z is norm)
   # Part.show(c10.toShape().revolve(o, z, 180))


A solid sphere can also be constructed by revolving a half circle line and
filling it in to make a solid. According to the help for revolve() this is 
better than revolving a full circle. (This is an algorithmic
improvement, not a theoretical difference.). :py:func:`LastParameter` 
for a circle is 2 * pi radians, so :py:func:`h10` in 
the next is a half circle on the X-Y plane.
Revolving around the Z-axis results in a flat full circle, filled in to make an
object of ShapeType 'Face'.
Revolving around the X-axis produces an object that is not valid. I think this is
because of the problem mentioned in the help for revolve, the meshing algorithm
does not like to rotate around a point where there is no vertex.
The Y-axis goes through both vertexes and revolving around it works well.

.. testcode::

   c10 = Part.Circle(o, z, 10)
   h10 = c10.toShape(c10.LastParameter/4, 3*c10.LastParameter/4)
   print( h10.ShapeType )
   # Part.show(h10)   # unfilled half circle on X-Y plane

   print( h10.revolve(o, z, 360).isValid() )     # True
   print( h10.revolve(o, x, 360).isValid() )     # False
   print( h10.revolve(o, y, 360).isValid() )     # True

   sf10 = h10.revolve(o, y, 360)
   print( sf10.ShapeType )
   # Part.show(sf10) 

   s10 = Part.makeSolid(Part.makeShell([sf10]))
   # Part.show(s10) 
   print( s10.ShapeType )
   print( len(s10.Solids) )
   
   print( s10.cut(s).isValid() ) # True
   print( s.cut(s10).isValid() ) # True
   
   #testEqual(s, s10) # this test seems a bit fragile

   # Part.show(s.cut(Part.makeBox(10,10,10))) 
   # Part.show(s10.cut(Part.makeBox(10,10,10))) 
   # Part.show(s10.cut(s)) 
   # Part.show(s.cut(s10)) 
   # Part.show((s10.cut(s)).cut(Part.makeBox(10,10,10))) 
   # Part.show((s.cut(s10)).cut(Part.makeBox(10,10,10))) 

.. testoutput::

   Edge
   True
   False
   True
   Face
   Solid
   1
   True
   True

To support speculation about difficulty for the meshing algorithm, this example
selects a different section of the circle and rotates successfully around
the X-axis.

.. testcode::

   c10 = Part.Circle(o, z, 10)
   print( c10.toShape(0, c10.LastParameter/2).revolve(o, x, 360).isValid() )# True
   s10x = Part.makeSolid(Part.makeShell([c10.toShape(0, 
                    c10.LastParameter/2).revolve(o, x, 360)]))
   print( s10x.ShapeType )
   # Part.show(s10x) 
   testEqual(s, s10x)

.. testoutput::

   True
   Solid

And this example creates the circle on the Y-Z plane and
selects a circle section that rotates successfully around the Z-axis.

.. testcode::

   c10z = Part.Circle(o, x, 10)
   print( c10z.toShape(0, c10z.LastParameter/2).revolve(o, x, 360).isValid() )# True
   
   s10z = Part.makeSolid(Part.makeShell([
             c10z.toShape(0, c10z.LastParameter/2).revolve(o, z, 360)  ]))
   print( s10z.ShapeType )
   # Part.show(s10z) 
   testEqual(s, s10z)

.. testoutput::

   True
   Solid

