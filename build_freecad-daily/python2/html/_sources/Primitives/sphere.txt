
.. index:: Sphere

Sphere
------

FreeCAD :py:func:`Part.Sphere()` produces a two dimensional surface (face) embedded
in three dimensional space. (The mathematical topology of the object is S<sup>2</sup>).
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


While py:func:`Part.makeSphere` will generally be easier to use to make a sphere, 
or portions of it, an arc can be used to make different rotation profiles. 
The next example shows making a sphere using :py:func:`Part.arc` 
and :py:func:`Part.makeRevolution` so easy test comparisons are 
possible, but that will generally not be the most interesting rotation profile.

:py:func:`Part.makeRevolution` takes 7 arguments. 
(Prior to FreeCAD 0.19,  if the first argument was Part.Shape object then it was 
used to determine the ShapeType and only the 6 first arguments were supported.)

Notice also that the angle, center, 
and axis arguments are in a different order from the :py:func:`.revolve` method.

.. testcode::

   arc = Part.Arc(-10*z, 10*x, 10*z)
   #Part.show(arc.toShape()) 

   aS = Part.makeRevolution(arc, arc.FirstParameter, arc.LastParameter, 
                 360, o, z, Part.Solid)
   print(aS.isClosed() )  #True
   print(aS.isValid() )   #True
   print( aS.ShapeType )  #Solid
   #Part.show(aS) 

   Part.makeRevolution(arc, arc.FirstParameter, arc.LastParameter, 
                 360, o, z, Part.Face).ShapeType  # Face

   #Part.show(aS) 

   testEqual(s, aS)

   testEqual(s, Part.makeRevolution(arc.toShape(), 
              arc.FirstParameter, arc.LastParameter, 360, o, z) )

   # This should work in 0.19
   #if (100* float(FreeCAD.Version()[0]) + float(FreeCAD.Version()[1]) >= 19.0 ):
   #testEqual(s, Part.makeRevolution(arc.toShape(), 
   #           arc.FirstParameter, arc.LastParameter, 360, o, z, Part.Solid) )
   #testEqual(s, Part.makeRevolution(arc.toShape(), 
   #           arc.FirstParameter, arc.LastParameter, 360, o, z, Part.Solid) )
   #if (100* float(FreeCAD.Version()[0]) + float(FreeCAD.Version()[1]) >= 19.0 ):
   #  aSe = Part.makeRevolution(arc.toShape(), arc.FirstParameter, arc.LastParameter, 
   #              360, o, z, Part.Face).ShapeType  #Face

.. testoutput::

   True
   True
   Solid

It is important that the shape created by :py:func:`Part.makeRevolution` is closed
or the result is not likely to be valid, and the problem is not immediately indicated
unless you check. Subsequent use of the returned object is likely to be problematic 
but the source of the problem may not be obvious.

Also beware that it not alway obvious how to convert a Face object created with 
the :py:obj:`.revolve` method into a solid. (At least, I have not yet figured 
out something that always works).

.. testcode::

   arcS = arc.toShape().revolve(o, z, 360)
   print( arcS.ShapeType )
   #Part.makeSolid(Part.makeShell([arcS]))
   #Part.makeSolid(arcS)
   #Part.makeFilledFace(arcS.Edges)

   testNotEqual(s, arcS )

.. testoutput::

   Face


CLEAN THIS UP
py:func:`Part.makeRevolution` also works for making solid 
hemispheres. It is used next to illustrate mirror and fuse.


py:func:`Part.makeSphere(radius, center, axis, fromLatitude, toLatitude, rotationAngle)
where fromLatitude is angle to start of sweep, measured fom a normal to the axis,
toLatitude is angle to end of sweep, measured from a normal to the axis,
and rotationAngle is the circular sweep around the axis. Angles in degrees.

.. testcode::

   #Part.show(Part.makeSphere(10, o, y, 45, 90, 360)) 
   #Part.show(Part.makeSphere(10, o, y, 45, 60, 360)) 
   #Part.show(Part.makeSphere(10, o, y, 45, 60, 270)) 
  
   hS  = Part.makeSphere(10, o, y, 0, 90, 360) 
   hSm = Part.makeSphere(10, o, -y, 0, 90, 360) 

   testEqual(s, hS.fuse(hSm)  )
   testEqual(hSm, hS.mirror(o, y) )
   testEqual(s, hS.fuse(hS.mirror(o, y))  )
   testEqual(s, hS.mirror(o, y).fuse(hS)  )

   #Part.show(hS) 
   #Part.show(hSm) 
   #Part.show(hS.fuse(hSm) )

   arc = Part.Arc(-10*z, 10*x, 10*z)
   hSr = Part.makeRevolution(arc, 
              arc.FirstParameter, arc.LastParameter, 180, o, z, Part.Solid)

   print( hSr.isClosed() )  # True
   print( hSr.isValid() )   # True
   print( hSr.ShapeType )   # Solid
   #Part.show(hSr) 

   testEqual(hS, hSr )
   testEqual(hS.mirror(o, y), hSr.mirror(o, y) )
   testEqual(s, hS.mirror(o, y).fuse(hSr) )
   testEqual(s, hSr.mirror(o, y).fuse(hS) )

   #Part.show(hS.mirror(o, y).fuse(hSr))
   #Part.show(hSr.mirror(o, y).fuse(hS))
   
   hSrm = Part.makeRevolution(Part.Arc(-10*z, -10*x, 10*z), 
              arc.FirstParameter, arc.LastParameter, 180, o, z, Part.Solid)
   print( hSrm.isClosed() )   # True
   print( hSrm.isValid() )    # True
   print( hSrm.ShapeType )    # Solid
   #Part.show(hSrm)      
   #Part.show(hSrm.fuse(hS)) 
   hS2 = hSm.fuse(hS)
   #Part.show(hS2) 

   hSm1 = hS.mirror(o, x)
   print( hSm1.isClosed() )  # True
   print( hSm1.isValid() )   # True
   print( hSm1.ShapeType )   # Solid
   #Part.show(hSm1) 
   #Part.show(hS.fuse(hSm1) )

   # STILL TO FIX BELOW
   # this produces a flat disk, which 
   # LOOKS TO ME LIKE A BUG OR LIMIT ON ANGLE, OR UNDOCUMENTED AND UNCHECKED FEATURE
   hSm = Part.makeRevolution(arc, 
              arc.FirstParameter, arc.LastParameter, -180, o, z, Part.Solid)
   #Part.show(hSm) 

   # NEXT SHOULD BE SAME AS ABOVE (reversing signs on 180 and z)
   # this works but has some anomolies across the flat face
   hSm = Part.makeRevolution(arc, 
              arc.FirstParameter, arc.LastParameter, 180, o, -z, Part.Solid)

   #Part.show(hSm) 
   print( hSm.isClosed() )  #True
   print( hSm.isValid() )   #False  but  ???


   Part.makeShell(hSm.Faces).isValid()  #False but ???
   shellm = Part.makeShell(hSm.Faces)
   shellm.isValid()
   #Part.makeShell([hSm.Faces]).isValid()RuntimeError: check failed, shape may be empty
   #Part.show(shellm) 
   #hSm = hS.mirror(o, x)
   HS = hS.fuse([hSm])   # FAILS USING GUI UNION TOO
   #testEqual(s, HS.cleaned(), debug = True)
   #Part.show(HS) 
   # this misses a quarter HS = hS.fuse(hS.mirror(o, x))

.. testoutput::

   True
   True
   Solid
   True
   True
   Solid
   True
   True
   Solid
   True
   False

