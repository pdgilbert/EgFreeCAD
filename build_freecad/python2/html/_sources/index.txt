
.. sphinxplay documentation master file, Modified from file created by
   sphinx-quickstart on Fri Dec 14 14:51:37 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   This and other rst files use imports and variables set in conf.py.

FreeCAD Scripting Examples
==========================

.. |date| date::
.. |time| date:: %H:%M

.. Generated |date| |time| on |un|

.. N.B. changes to next line will require changes to script freecadPythonCheck

Built |date| with |FC| and Python |PYv| (See Environment Details)

Recent versions of this document are at
https://pdgilbert.github.io/EgFreeCAD/ 

Table of Contents
-----------------

.. toctree::

   self
   intro
   Primitives/index
   SimpleConstructs/index
   Projects/index
   Misc
   Puzzles
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

.. testcode::

   import os
   print(os.environ['FREECAD'])

.. testoutput::
   :options: +SKIP

|FC|


.. testcode::

   import FreeCAD
   print(FreeCAD.Version())

.. testoutput::
   :options: +SKIP

|FCversion|


.. testcode::

   import sys
   print(sys.version)   # or sys.version_info

.. testoutput::
   :options: +SKIP

|PYversion|


.. testcode::

   import os
   print(os.environ['PYTHONPATH'])

.. testoutput::
   :options: +SKIP

|PYpath|

.. testcode::

   import os
   print(os.uname())

.. testoutput::
   :options: +SKIP

|un|


.. testcode::

   import sys
   print(sys.path) 

.. testoutput::

   [...

|sysPath|
