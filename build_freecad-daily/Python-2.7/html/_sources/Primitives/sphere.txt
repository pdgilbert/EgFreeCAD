
.. index:: Sphere

Sphere
------

.. testcode::

   S = Part.makeCircle(5)
   S2 = S.copy()
   testEqual(S, S2)
   testNotEqual(S, Part.makeCircle(5.5))
   
   if S.Curve.Radius != 5.0 : raise Exception("Circle radius should be 5.0.")

   if S.Curve.Center != Vector(0,0,0) : raise Exception("Circle Center should be origin.")
   
   if S.Curve.Axis   != Z   : raise Exception("Circle axis should be Z axis.")
      
   # circle is symmetic

.. testcode::

   S2.rotate(O, Z, 180)
   testEqual(S, S2)
   S2.rotate(O, Z, 90)
   testEqual(S, S2)

.. testcode::

   S2.translate(Vector(0,0,10))
   testNotEqual(S, S2)

.. testcode::

   s  = Part.makeSphere(10)
   s2 = Part.makeSphere(10)
   s2.rotate(O, Z, 180)
   
   testEqual(s, Part.makeSphere(10))
   testNotEqual(s, Part.makeSphere(9))
   testEqual(s, s2)

A sphere can be constructed by revolving a circle

.. testcode::

   C = Part.makeCircle(10) # at origin, normal to z axis, one edge, no faces
   
   if not C.isClosed(): raise Exception("Object C is not a closed loop")
   
   if 1 != len(C.Edges): raise Exception("Circle should have 1 edge.")
   
   if 0 != len(C.Faces): raise Exception("Circle should have no faces.")
   
   C2 = Part.Face(Part.Wire(C))
   if 1 != len(C2.Faces): raise Exception("Circle with interior should have 1 face.")
   
   C2x = Part.makeShell(C2.Faces)

  
See https://www.freecadweb.org/wiki/Part_Revolve
revolve a face should give a solid
   
.. testcode::

   S2 = C2.revolve(Vector(0,0,0), Vector(1,1,1), 360)  
   #Part.show(S2) 
   S2 = C2x.revolve(O, X, 360)  
   #Part.show(S2) 
   #  THIS IS NOT SHOWING PROPERLY
   S2 = C2.revolve(O, Y, 360)  
   S2 = C2.revolve(O, Z, 360)  


