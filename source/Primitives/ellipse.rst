
.. index:: Ellipse

Ellipse
-------

Part.Sphere produces a face and Part.makeSphere() produces a solid, but there is 
not yet a Part.makeEllipsoid() to make a solid.


An ellipsoid can be produced by revolving an ellipse. When the ellipse is not
filled in (has no faces) then the revolution will be hollow. 

The following shows different ways to use an ellipse to make a solid ellipsoid
with the general shape of a rugby ball. (It could be made to look like a flying saucer but that will be left to the reader.)

Part.Ellipse().toShape() makes a shape that is an edge with no faces.
The ellipsoid  made by revolving this has faces but is not solid (a hollow
ellipsoid).

1/ revolve full ellipse on x axis
2/ 1/2 ellipse revolved around vertices on long axis
3/ a different 1/2 ellipse revolved around long axis , mirror and join
4/ 1/4 ellipse revolved to give 1/2 ellipsoid, mirror and join

Make an ellipse, on the plane of the origin and normal to  z-axis, 
with radii, 6.0 and 2.0.

..testcode::

   e = Part.Ellipse(o, 6.0, 2.0)
   print(len(e.toShape().Faces))
   #Part.show(e.toShape())

..testoutput::

   0

1/ revolve full ellipse on x axis
ASKING ON FORUM    NOT YET WORKING
..testcode::
   ed = e.toShape().revolve(o, y, 180) #saucer THIS SHOULD USE x
   #Part.show(ed)
   print(ed.ShapeType) #  hollow
   print(len(ed.Solids))
   print(len(ed.Faces))

   ed1 = e.toShape().revolve(o, x, 180) # should be rugby ball but
   #Part.show(ed1)            # does not show

   #ed1.PrincipalProperties

..testoutput::

   Face
   0
   1


2/ An algorithmically better way to make an ellipsoid, according to the revolve documentation, is to cut the ellipse so there are vertices. LastParameter is 2 pi radians so this cuts the sweep to the half circle from 0 to  pi:

there is something weird in sphinx happening with testoutput here.


..testcode::

   e = Part.Ellipse(o, 6.0, 2.0)
   h = e.toShape(0, e.LastParameter/2) 
   hd = h.revolve(o, x, 360) #rugby ball, hollow
   ed2 = Part.makeSolid(Part.makeShell([hd]))
   #Part.show(ed2)

   #print(h.ShapeType)
   #print(hd.ShapeType)
   #print(ed2.ShapeType)
   #print(len(ed2.Solids))
   #print(len(ed2.Faces))


Do TESTEQUAL WITH first

3/ a different 1/2 ellipse revolved around long axis, mirror and join

ASKING ON FORUM    NOT YET WORKING

..testcode::

   h2 = e.toShape(e.LastParameter/4, 3*e.LastParameter/4)
   #Part.show(h2)

   hd = h2.revolve(o, x, 360) #half rugby hollow, double cover
   #Part.show(hd)

   hd = h2.revolve(o, x, 180) #half rugby hollow
   #Part.show(hd)
   hdm = hd.mirror(o, x)
   #Part.show(hdm)

   #check = Part.makeShell([hdm])
   #Part.show(check)
   sh3 = Part.makeShell([hd, hdm]) #SUPPOSED TO MAKE SHELL FROM LIST OF FACES BUT LOSES hdm

   #Part.show(sh3)

   ed3 = Part.makeSolid(sh3)
   #Part.show(ed3)  # ONLY HALF

   #filled= Part.makeFilledFace(hd.toShape().Edges)

   #rugby = hd.fuse(hdm)  # No. Fuse wants solids (warning only in gui)
   #Part.show(rugby)


4/ 1/4 ellipse revolved to give 1/2 ellipsoid, mirror and join

ASKING ON FORUM  NOT YET 

..testcode::

   e = Part.Ellipse(o, 6.0, 2.0).toShape()
   #Part.show(e)
   ed = e.revolve(o, y, 180) #saucer
   #Part.show(ed)
   #ed1 = Part.makeShell(ed) #Error creating objec
   ed2 = Part.makeSolid(ed) # Creation of solid failed: No shells 
   #Part.show(ed2)
   if 1 != len(ed.Solids): raise Exception("This ellipsoid should be solid.")


construct 2nd half rather than mirror

NOT YET  

..testcode::

   e = Part.Ellipse(o, 6.0, 2.0).toShape()
   #Part.show(e)
   ed = e.revolve(o, y, 180) #saucer
   #ed = e.revolve(o, x, 180) # why not rugby ball
   #Part.show(ed)

   e2 = Part.Ellipse(o, 6.0, 2.0).toShape()
   e2.rotate(o,  z,  90) 
   #Part.show(e2)
   ed2 = e2.revolve(o, y, 180) # why not 
   ed2 = e2.revolve(o, x, 180) # why saucer 
   #Part.show(ed2)
   testNotEqual(e, e2)
   e.rotate(o,  x,  90) 
      e2.translate(x)
   e2.rotate(x,  x,  90)
   e2.rotate(x,  z, -90)
   e2.translate(-x)
   testEqual(e, e2)
   
   wi = Part.Wire(e)
   if not wi.isClosed(): raise Exception("Objects wi is not a closed loop")
   
   d = Part.Face(wi)
   dd = d.extrude(Vector(20,0,0)) 
   #Part.show(dd) 
   
   b = Part.makeCylinder(8, 20, o, x, 90)
   b = b.cut(dd)
      
This would not need to be rotated, but s2 does not work the way I think
# e2 = Part.Ellipse(Vector(0.0, 0.0, 6),Vector(0.0, 2, 8), Vector(0.0, 0.0, 8)).toShape()
#Part.show(e2)

COMPARE ELLIPSOID WITH EQUAL RADII AND A SPHERE
