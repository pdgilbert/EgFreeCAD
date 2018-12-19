
.. testsetup::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 
   
   O = Vector(0,0,0)
   X = Vector(1,0,0)
   Y = Vector(0,1,0)
   Z = Vector(0,0,1)


.. index:: Primitive Examples
Primitive Examples
==================

.. testcode::

   import sys
   print(sys.version)   # or sys.version_info

.. testoutput::

    2.7.12...

.. testcode::

   print(sys.path) # this will give output

.. testoutput::

   [...

.. testcode::

   print(FreeCAD.Version())

.. testoutput::

   ['0', '17', ...

.. include:: box.rst
.. include:: sphere.rst
.. include:: cone.rst
.. include:: polygon.rst
.. include:: torus.rst
