
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
   
   torus2.rotate(o, z, 90)
   testEqual(torus, torus2 )

Flipping will be equal

.. testcode::

   torus2.rotate(o, x, 180)
   testEqual(torus, torus2 )

but half flip is not

.. testcode::

   torus2.rotate(o, x, 90)
   testNotEqual(torus, torus2 )
   
pnt is the center of torus and dir is the normal direction.
The default is o, z. Starting with default and rotating 90 around x-axis
is the same as indicating y-axis as the initial normal direction.

.. testcode::

   torus2 = torus.copy()
   torus2.rotate(o, x, 90)
   testEqual(torus2,  Part.makeTorus(20, 5, o, y))
   
