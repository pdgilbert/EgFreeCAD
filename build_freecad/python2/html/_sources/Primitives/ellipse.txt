
.. index:: Ellipse

Ellipse
-------

:py:func:`Part.Sphere` produces a face and :py:func:`Part.makeSphere` produces 
a solid, but there is 
not yet a :py:func:`Part.makeEllipsoid` to make a solid.

An ellipsoid can be produced by revolving an ellipse. If the ellipse is not
filled in (has no faces) then the revolution will be hollow. 

The following shows different ways to use an ellipse to make a solid ellipsoid
with the general shape of a rugby ball. (It could be made to look like a flying saucer but that will be left to the reader.)

:py:func:`Part.Ellipse().toShape` makes a shape that is an edge with no faces.
The ellipsoid  made by revolving this has faces but is not solid (a hollow
ellipsoid).

To start, make an ellipse, on the XY-plane through the origin, 
with radii, 6.0 and 2.0.

.. testcode::

   e = Part.Ellipse(o, 6.0, 2.0)
   print(len(e.toShape().Faces))
   #Part.show(e.toShape())

.. testoutput::

   0

Create a half ellipse on the XY-plane with ends on the X-axis and revolve it 
a full turn around the X-axis using  method :py:func:`revolve` 

.. testcode::

   eh = e.toShape(0, e.LastParameter/2)
   #Part.show(eh)
   print( eh.ShapeType )  #Edge
   print( len(eh.Solids)) # 0
   #TEST ON Z AXIS
   ecS = eh.revolve(o, x, 360)
   #Part.show(ecS )
   print( ecS.ShapeType )  #Face
   print( len(ecS.Solids)) # 0
   print( ecS.isClosed() )  #False #Looks like a BUG. 
   print( ecS.isValid()  ) #True

   e1 = Part.makeSolid(Part.makeShell([ecS]))
   #Part.show(e1 )
   print( e1.ShapeType )  #Solid
   print( len(e1.Solids)) # 1
   print( e1.isClosed() ) #True 
   print( e1.isValid()  ) #True

   #( still trying Part.makeRevolution arg need to be GeomCurve)
   #ecS = Part.makeRevolution(e, 0, e.LastParameter/2, 360, o, x)
   #ecS = Part.makeRevolution(eh, eh.LastParameter, 0, 360, o, x)
   #Part.OCCDomainError: creation of revolved shape failed    BUG ???

.. testoutput::

   Edge
   0
   Face
   0
   False
   True
   Solid
   1
   True
   True

1/ revolve full ellipse a half turn around the x axis

.. testcode::

   #ed = Part.makeRevolution(e.toShape(), 0, e.LastParameter, 180, o, x)

   ed = e.toShape().revolve(o, y, 180) #saucer THIS SHOULD USE x BUT THAT FAILS
   #Part.show(ed)
   print(ed.ShapeType)   # Face  (hollow ellipsoid)
   print(len(ed.Solids)) # 0
   print(len(ed.Faces))  # 1
   print( ed.isClosed() )  #False #Looks like a BUG. 
   print( ed.isValid()  ) #True

   #TRY THIS IN GUI
   #ed1 = e.toShape().revolve(o, x, 180) # should be rugby ball but
   #Part.show(ed1)            # does not show
   #print( ed1.ShapeType )  #Face
   #print( len(ed1.Solids)) # 0
   #print( ed1.isClosed() )  #False #Looks like a BUG. 
   #print( ed1.isValid()  ) #True
   #ed1.PrincipalProperties

.. testoutput::

   Face
   0
   1
   False
   True


I THINK THIS IS THE SAME AS FIRST NOW
An algorithmically better way to make an ellipsoid, according to the revolve documentation, is to cut the ellipse so there are vertices. LastParameter is 2 pi radians so this cuts the sweep to the half circle from 0 to  pi:

.. testcode::

   e = Part.Ellipse(o, 6.0, 2.0)
   h = e.toShape(0, e.LastParameter/2) 
   #Part.show(h)
   hd = h.revolve(o, x, 360) #rugby ball, hollow
   ed2 = Part.makeSolid(Part.makeShell([hd]))
   #Part.show(ed2)

   print(h.ShapeType)     #Edge
   print(hd.ShapeType)    #Face
   print(ed2.ShapeType)   #Solid
   print(len(ed2.Solids)) #1
   print(hd.isClosed())   #False   ???
   print(hd.isValid())    #True

   print(len(ed2.Faces))  #1
   #DO TESTEQUAL 

.. testoutput::

   Edge
   Face
   Solid
   1
   False
   True
   1


3/ a different 1/2 ellipse revolved around long axis, mirror and join

 NOT YET WORKING

.. testcode::

   e3 = e.toShape(e.LastParameter/4, 3*e.LastParameter/4)
   #Part.show(e3)

   #THESE ROTATION WORKS FINE DESPITE NOT THROUGH VERTEXES
   #hd = e3.revolve(o, x, 360) #half rugby hollow, double cover Also works
   hd = e3.revolve(o, x, 180) #half rugby hollow, singe cover
   #Part.show(hd)
   print(hd.ShapeType)   #Face
   print(len(hd.Solids)) #0
   print(hd.isClosed())  #False   ???
   print(hd.isValid())   #True

   hdm = hd.mirror(o, x)
   #Part.show(hdm)
   print(hdm.ShapeType)   #Face
   print(len(hdm.Solids)) #0
   print(hdm.isClosed())  #False   ???
   print(hdm.isValid())   #True)

   #check = Part.makeShell([hdm])
   #Part.show(check)
   #sh3 = Part.makeShell([hd, hdm]) #SUPPOSED TO MAKE SHELL FROM LIST OF FACES BUT LOSES hdm
TRY THIS IN GUI
   #sh3 = Part.makeShell([hd.Faces + hdm.Faces])
   #Part.show(sh3) # no show
   print(sh3.ShapeType)   #Face
   print(len(sh3.Solids)) #0
   print(sh3.isClosed())  #False   ???
   print(sh3.isValid())   #True

   #ed3 = Part.makeSolid(sh3)
   #Part.show(ed3)  # ONLY HALF

   #filled= Part.makeFilledFace(hd.toShape().Edges)

   #rugby = hd.fuse(hdm)  # No. Fuse wants solids (warning only in gui)
   #Part.show(rugby)

.. testoutput::

    Face
    0
    False
    True
    Face
    0
    False
    True

4/ 1/4 ellipse revolved to give 1/2 ellipsoid, mirror and join

NOT YET 

.. testcode::

   e = Part.Ellipse(o, 6.0, 2.0).toShape()
   #Part.show(e)
   ed = e.revolve(o, y, 180) #saucer
   #Part.show(ed)
   #ed1 = Part.makeShell(ed) #Error creating objec
   #ed2 = Part.makeSolid(ed) # Creation of solid failed: No shells 
   #Part.show(ed2)
   print( len(ed.Solids) )

.. testoutput::

   0


construct 2nd half rather than mirror

NOT YET  

.. testcode::

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
   #testEqual(e, e2)
   
   wi = Part.Wire(e)
   print(wi.isClosed())  #True
   
   d = Part.Face(wi)
   dd = d.extrude(Vector(20,0,0)) 
   #Part.show(dd) 
   
   #b = Part.makeCylinder(8, 20, o, x, 90)
   #b = b.cut(dd)

.. testoutput::

   True

This would not need to be rotated, but s2 does not work the way I think
# e2 = Part.Ellipse(Vector(0.0, 0.0, 6),Vector(0.0, 2, 8), Vector(0.0, 0.0, 8)).toShape()
#Part.show(e2)

An ellipsoid with equal radii is a circle a sphere made this way can be compared
with a sphere  made with :py:func:`makeSphere`.

.. testcode::

   eC = Part.Ellipse(o, 5.0, 5.0)
   edC = Part.makeSolid(Part.makeShell([
             eC.toShape(0, eC.LastParameter/2).revolve(o, x, 360)  ]))
   
   # Part.show(edC)
   testEqual( edC,Part. makeSphere(5) )

Try above using makeRevolution.

.. testcode::

   eC = Part.Ellipse(o, 5.0, 5.0)
   ech = eC.toShape(0, eC.LastParameter/2)
   #ecS = Part.makeRevolution(ech.Curve)
   #ecS = Part.makeRevolution(ech)
   #ecS = Part.makeRevolution(ech, ech.FirstParameter, ech.LastParameter, 360, o, x, Part.Solid)
