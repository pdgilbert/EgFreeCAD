.. index:: Introduction

Introduction
------------

To date, this document is focused mainly on the Part workbench and oriented toward
exercises I have gone through to design objects for 3D printing.

Several FreeCAD scripting examples are illustrated. Functions from a
module :py:mod:`testEqual` are used to help verify that the examples work.
The verification is based on the observation that :py:obj:`a.cut(b)` 
and :py:obj:`b.cut(a)` will both be empty if the objects are equal. Empty means 
shapes with no Vertexes, Edges, Faces, ... , so equal is in the sense of defining 
the same object in space, not in the sense of being similar python objects.
Based on this, scripts can be used to build an
object in different ways, and the results compared to ensure the different approaches
actually give the same object in space. 

The test functions are documented in an appendix. The main test 
function :py:obj:`areEqual(a,b)` returns a boolean result. 
Wrapper functions :py:func:`testEqual`  and  :py:func:`testNotEqual` provide a simpler 
mechanism for running automatic checks.
They do not return a result, but raise an exception if the test fails.

One caveat in testing is that assignment in FreeCAD makes a new pointer to the same 
object, so manipulation of a second object made this way will also alter the original. 
That is

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
into the console. 
They can also be run in a python session after importing freecad.
To importing :py:mod:`freecad` into a python session be sure to put it on 
the python module search path, for example before starting python by using 
*export PYTHONPATH=/usr/lib/freecad/lib:$PYTHONPATH*.

To run the tests in this document you will need to download (git clone) 
EgFreeCAD and set the path of the :py:mod:`testEqual` module 
library. This can be done before starting python with
*export PYTHONPATH=/path/to/EgFreeCAD/lib:$PYTHONPATH*.
It can also be done inside a python session 
using :py:func:`sys.path.append("/path/to/EgFreeCAD/lib")`.
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
Some examples indicate :py:obj:`Part.show(something)`. This command is
commented out and not run in the script tests but you may want to use it in 
a FreeCAD GUI session. Beware that you may need to click the icon that
fits the contents to the screen.

Additional illustration of the testing functions is provided in the examples.
See especially *Primitives Examples / Box*.

Note that I have been constructing this document as a learning exercise 
myself, so please do not hesitate to point out mistakes or interesting 
additions. (Things do work because of the testing, but that does not mean
that I describe them properly.)

My learning draws heavily on explanations found elsewhere. See, for example,
https://www.freecadweb.org/wiki/FreeCAD_Scripting_Basics, 
https://www.freecadweb.org/wiki/Topological_data_scripting,
and
https://www.freecadweb.org/wiki/Scripting_examples. There are also a large
number of GUI based example. As a beginner I am finding two difficulties 
that I am trying to overcome with this document. 
The first is that the FreeCAD API is changing. This is necessary for evolving 
software, but a result is that many examples on the Internet do not work as
illustrated or no longer work at all. 
The generated confusion is often aggravated by the lack of version and system
detail in the examples and online documentation.  The main index page of this 
document provides system detail and the module :py:mod:`testEqual` along with 
Sphinx doctest help ensure the examples continue to work with new 
FreeCAD releases. 
The second is that I like reproducibility so, rather the GUI interface, I 
have focused on scripting which I know how to test and maintain.
