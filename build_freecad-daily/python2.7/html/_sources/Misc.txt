.. index:: Misc for understanding Sphinx

Misc testing of how to use Sphinx
=================================

what is func vs function  :py:func: 2 * 2

The :py:func:`whatever` provides highlighting.


##   print(sys.path) # this will give output

.. doctest::

   >>> print(2 * 2)
   4

show python attached modules::
.. doctest::

   >>> print(dir())
   [...

.. testcode::

   print(dir())

.. testoutput::

   [...

.. testcode::

   print(dir())

.. testoutput::

   [...

Or inline

>>> print(dir())
[...

But I still have not been able to print the actual output rather than expected.

The value  is :py:print:dir()

Doctest example:

.. doctest::

   >>> print 2+2
   4

testcode/testoutput example:

.. testcode::

   1+1        # this will give no output!
   print 2+2  # this will give output

.. testoutput::

   4

reST doctest blocks are simply doctests put into a paragraph of their own, like

>>> print 1
1

Some more documentation text.
Note though that you cannot have blank lines in reST doctest blocks.
