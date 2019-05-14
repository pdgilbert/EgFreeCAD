.. index:: Puzzles

Puzzles
-------

- How does Part.Circle(o, z, 10) different from Part.makeCircle(10) 

- Why does a circle need to be converted to a wire before converting to a face

C = Part.makeCircle(10)
C2 = Part.Face(Part.Wire(C))

- ( following s.revolve help )

Why does this work

e = Part.Ellipse()
s = e.toShape()
r = s.revolve(o, y, 360) # this has artifacts because of doubling
#Part.show(r)

and this

r = s.revolve(o, y, 180) # this still has artifacts because of no vertex
#Part.show(r)

But not this

c10 = Part.Circle(o, z, 10) 
s10 = c10.toShape()
r = s10.revolve(o, y, 360)
#Part.show(r)  # THERE SEEMS TO BE A BUG HERE

or this

r = s10.revolve(o, y, 180)
#Part.show(r)  # THERE SEEMS TO BE A BUG HERE

-LastParameter is 2 pi radians for the sweep of a circle
Next works well, but I'm just guessing that toShape arguments
mean take the sweep from pi / 2 to 3 pi / 2

s = c10.toShape(c10.LastParameter/4, 3*c10.LastParameter/4)
r = s.revolve(o, y, 360)
#Part.show(r)

-There is an anomaly here. s.ShapeType is Solid' whereas r10.ShapeType is
'Face', but cutting leaves an empty object.  The difference can be seen by
cutting open the sphere. Perhaps the problem is caused by the fact that
cutting the surface from a solid sphere leaves an unbounded interior of the
sphere, but I'm not sure the answer should be to remove the interior with
no warning.

.. testcode::

   s  = Part.makeSphere(10)
   print(s.ShapeType)
   # Part.show(s.cut(Part.makeBox(10,10,10)))

   c10 = Part.Circle(o, z, 10) 
   s10 = c10.toShape(c10.LastParameter/4, 3*c10.LastParameter/4)
   r10 = s10.revolve(o, y, 360)
   print(r10.ShapeType)
   # Part.show(s.cut(Part.makeBox(10,10,10)))

   testNotEqual(s, r10)
   print(areEqual(s, r10))

.. testoutput::

   Solid
   Face
   False
