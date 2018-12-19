.. sphinxplay documentation master file, created by
   sphinx-quickstart on Fri Dec 14 14:51:37 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FreeCAD Scripting Examples
==========================

Contents:

.. toctree::

   self
   Primitives/index
   SimpleConstructs/index
   Misc
   Appendix

.. index:: Indices and tables

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. index:: Introduction

Introduction
------------

This document illustrates several FreeCAD scripting examples. It also uses functions
from a module :py:mod:`testEqual` to help automatically verify that the examples work.
The verification is based on the observation that :py:obj:`a.cut(b)` and :py:obj:`b.cut(a)` will both be empty if the objects are equal. Based on this, scripts can be used to build an
object in different ways, and the results compared to ensure the different approaches
actually give the same object. 

The test functions are documented in an appendix. The main test function :py:obj:`areEqual(a,b)` returns a boolean result. 
Wrapper functions :py:func:`testEqual`  and  :py:func:`testNotEqual` provide a simpler mechanism for running automatic checks.
They do not return a result, but raise an exception if the test fails.


.. testsetup::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 

One caveat in testing is that assignment in FreeCAD makes a new pointer to the same object, so manipulation of a second object made this way will also alter the original. That is

.. testcode::

   a = Part.makeBox(1,100,10)
   b = a
   a.translate(Vector(0,0,10))
   print(areEqual(a, b))

.. testoutput::

   True

Returns :py:const:`True` because the object pointed to by both :py:obj:`a` and :py:obj:`b`
is translated, whereas

.. testcode::

   a = Part.makeBox(1,100,10)
   b = a.copy()
   a.translate(Vector(0,0,10))
   print(areEqual(a, b))

.. testoutput::

   False

Returns :py:const:`False` because the translation of :py:obj:`b` does not affect :py:obj:`a`.

To run  examples in this document the path of the freecad and testEqual libraries is needed. 
This should be done before starting python with
export PYTHONPATH=$PYTHONPATH:/usr/lib/freecad/lib:/path/to/testEqual.
It can also be done inside a python session using :py:func:`sys.path.append`.

Sections of this document use doctest testcode and testoutput directives. 
The testoutput is displayed in a block below the testcode. The block will be empty
if the code has no output (since I have not figured out how to omit it).
All sections use the setup code

.. testcode::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 

and also set vectors for the origin and directions X, Y, and Z, which are used in several examples.

.. testcode::

   O = Vector(0,0,0)
   X = Vector(1,0,0)
   Y = Vector(0,1,0)
   Z = Vector(0,0,1)

