
.. sphinxplay documentation master file, Modified from file created by
   sphinx-quickstart on Fri Dec 14 14:51:37 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   This and other rst files use imports and variables set in conf.py.

FreeCAD Scripting Examples
==========================

.. |date| date::
.. |time| date:: %H:%M

Generated |date| |time| on |un|

using FreeCAD |FCversion|

and Python version |PYversion|

Contents:

.. toctree::

   self
   intro
   Primitives/index
   SimpleConstructs/index
   Projects/index
   Misc
   Appendix

.. index:: Indices and tables

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. index:: Environment Details

Environment Details
-------------------

Environment variable FREECAD setting |FC|

.. testcode::

   import os
   print(os.environ['FREECAD'])

.. testoutput::
   :options: +SKIP


Freecad version |FCversion|

.. testcode::

   import FreeCAD
   print(FreeCAD.Version())

.. testoutput::
   :options: +SKIP


Python version |PYversion|

.. testcode::

   import sys
   print(sys.version)   # or sys.version_info

.. testoutput::
   :options: +SKIP

Python path |PYpath|

.. testcode::

   import os
   print(os.environ['PYTHONPATH'])

.. testoutput::
   :options: +SKIP

OS version |un|

.. testcode::

   import os
   print(os.uname())

.. testoutput::
   :options: +SKIP

OS Path |OSpath|

.. testcode::

   import sys
   print(sys.path) 

.. testoutput::

   [...
