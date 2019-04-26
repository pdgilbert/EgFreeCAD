
Appendix: Functions in Module testEqual
=======================================

These are the functions in module :py:mod:`testEqual`, which is used to help verify examples
in this document.

.. py:function:: isEmptyShape(a)

   Test if shape :py:obj:`a` is empty. Return :py:const:`True` if shape is empty,
   :py:const:`False` otherwise. :py:const:`True` is returned if :py:obj:`a` 
   is :py:const:`None` (not a shape) but :py:const:`False` for other non-shapes.

.. py:function:: areEqual(a, b)

   Test if shapes :py:obj:`a` and :py:obj:`b` are equal. Return :py:const:`True` 
   or :py:const:`False`. The main part of this test is based on the observation that
   :py:obj:`a.cut(b)` and :py:func:`b.cut(a)` should both be empty if the objects are equal.
   The first checks are just for the case where :py:obj:`a` or :py:obj:`b` is empty, 
   causing cut to fail.

.. py:function:: testEqual(a, b)

   Check if shapes :py:obj:`a` and :py:obj:`b` are equal and raise an exception if they are not.

.. py:function:: testNotEqual(a, b)

   Check if shapes :py:obj:`a` and :py:obj:`b` are equal and raise an exception if they are.

.. py:function:: isSubset(a, b)

   Test if shape :py:obj:`a` is a subset of :py:obj:`b`. Return :py:const:`True` 
   or :py:const:`False`. Equality is considered to be a subset (:py:const:`True` 
   is returned). A strict subset (non-equal) is based on the observation that
   :py:obj:`a.cut(b)` is not empty but :py:obj:`b.cut(a)` is empty.
   The first checks are just for case where :py:obj:`a` or :py:obj:`b` is empty, 
   causing cut to fail.

.. py:function:: testSubset(a, b)

   Check if shape :py:obj:`a` is a (non-strict) subset of :py:obj:`b` and raise an 
   exception if it is not.

.. py:function:: testNotSubset(a, b)

   Check if shape :py:obj:`a` is not a (non-strict) subset of :py:obj:`b` and 
   raise an exception if it is.

