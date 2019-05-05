
.. index:: Ellipse

Ellipse
-------

Make an ellipse using origin o and  two radii, 6.0 and 2.0

.. testcode::

   e = Part.Ellipse(o, 6, 2).toShape() # normal to  z-axis, longer in X direction
   e.rotate(o,  x,  90)  # normal to y-axis,  longer in X direction
   e.rotate(o,  z, -90)  # normal to x-axis,  longer in Y direction
   #Part.show(e)
   
   e2 = Part.Ellipse(o, 6, 2).toShape()
   testNotEqual(e, e2)
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
