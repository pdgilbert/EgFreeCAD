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

Returns :py:const:`False` because the translation of :py:obj:`b` 
does not affect :py:obj:`a`.

Examples in this document can be run in a FreeCAD GUI session by cut-and-paste
into the console, or they can be run in a python session after importing freecad.
To importing :py:mod:`freecad` into a python session be sure to put it on 
the python module search path, for example before starting python by using 
*export PYTHONPATH=$PYTHONPATH:/usr/lib/freecad/lib*.

To run the tests in this document the path of the :py:mod:`testEqual` module 
library is needed. This can be done before starting python with
*export PYTHONPATH=$PYTHONPATH:/path/to/testEqual*.
It can also be done inside a python session using :py:func:`sys.path.append`.
The :py:mod:`testEqual` module is not needed except to run tests, which are
mainly for the purpose of confirming that the examples in this document 
continue to work in new FreeCAD versions. 

The source files for sections of this document, available in the EgFreeCAD
github repository,  use Sphinx :py:obj:`doctest` 
and :py:obj:`testcode` with :py:obj:`testoutput` directives. 
If there is any test output then it is displayed in a block below 
the :py:obj:`testcode`. All tests use the setup code specified in Spinx
:py:obj:`conf.py` :py:obj:`doctest_global_setup` variable, which does

.. testcode::

   import FreeCAD
   from FreeCAD import Base, Vector
   import Part, Mesh, MeshPart
   from testEqual import * 

and also sets vectors for the origin :py:obj:`o` and points one unit in the
directions :py:obj:`x, y`, and :py:obj:`z`, which are used in several examples.

.. testcode::

   o = Vector(0,0,0)
   x = Vector(1,0,0)
   y = Vector(0,1,0)
   z = Vector(0,0,1)

Be sure to set these in your session.
Some examples indicate :py:obj:`Part.show(something)`. This cammand is
commented out and not run in the script tests but you may want to use it in 
a FreeCAD GUI session.
