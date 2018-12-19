
.. testsetup::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 
   
   O = Vector(0,0,0)
   X = Vector(1,0,0)
   Y = Vector(0,1,0)
   Z = Vector(0,0,1)

.. index:: Torus
Torus
-----

Make a torus SxS with first radius 20 in the X-Y plane and second radius 5

.. testcode::

   torus =  Part.makeTorus(20, 5)
   #Part.show(torus)
   
   
   torus2 = torus.copy()
   #Part.show(torus2)
   testEqual(torus, torus2 )
   
   torus2.rotate(O, Z, 90)
   testEqual(torus, torus2 )

.. testoutput::
  
Flipping will be equal

.. testcode::

   torus2.rotate(O, X, 180)
   testEqual(torus, torus2 )
 
.. testoutput::
  
but half flip is not

.. testcode::

   torus2.rotate(O, X, 90)
   testNotEqual(torus, torus2 )
   
.. testoutput::

pnt is the center of torus and dir is the normal direction.
The default is O, Z. Starting with default and rotating 90 around x-axis
is the same as indicating y-axis as the initial normal direction.

.. testcode::

   torus2 = torus.copy()
   torus2.rotate(O, X, 90)
   testEqual(torus2,  Part.makeTorus(20, 5, O, Y))
   
.. testoutput::

Make an ellipse using origin O and  two radii, 6.0 and 2.0

.. testcode::

   e = Part.Ellipse(O, 6, 2).toShape() # normal to  z-axis, longer in X direction
   e.rotate(O,  X,  90)  # normal to y-axis,  longer in X direction
   e.rotate(O,  Z, -90)  # normal to x-axis,  longer in Y direction
   #Part.show(e)
   
   e2 = Part.Ellipse(O, 6, 2).toShape()
   testNotEqual(e, e2)
   e2.translate(X)
   e2.rotate(X,  X,  90)
   e2.rotate(X,  Z, -90)
   e2.translate(-X)
   testEqual(e, e2)
   
   wi = Part.Wire(e)
   if not wi.isClosed(): raise Exception("Objects wi is not a closed loop")
   
   d = Part.Face(wi)
   dd = d.extrude(Vector(20,0,0)) 
   #Part.show(dd) 
   
   b = Part.makeCylinder(8, 20, O, X, 90)
   b = b.cut(dd)
      
.. testoutput::

This would not need to be rotated, but s2 does not work the way I think
# e2 = Part.Ellipse(Vector(0.0, 0.0, 6),Vector(0.0, 2, 8), Vector(0.0, 0.0, 8)).toShape()
#Part.show(e2)
