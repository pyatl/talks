===================================================
 Operator Overloading and Python's Special Methods
===================================================

| PyATL
| September, 2013
| Doug.Hellmann@gmail.com
| @doughellmann
| http://doughellmann.com

.. note::

  Going to talk about:

  1. What special methods are.
  2. Some example special methods.
  3. Look at how the comparison operators use special methods.

What are "Special Methods"?
===========================

*Special Methods* are a naming convention to bind methods of your
class to operators or built-ins in the language.

Also known as "Dunder" methods ("double underscore").

.. note::

  Special methods tie your class in to Python by using well-defined
  names that the interpreter looks for.

__init__
========

::

  my_inst = MyClass()

When a Class type needs to initialize a new instance, it calls the
__init__ method.

__del__
=======

::

  del my_inst

Clean up resources owned by an object in __del__.

__str__ and __unicode__
=======================

::

  str(my_inst)
  unicode(my_inst)

Replacing the string representation via __str__ or __unicode__ makes
it easier to debug with custom classes.

__repr__
========

::

  repr(my_inst)
  print my_inst

The print statement uses the repr() of an object by default.

__iter__
========

::

  for i in my_inst:
    ...

The __iter__ method returns an iterator for an iterable object.

__call__
========

::

  my_inst(arg1, arg2)

Adding a __call__ method means you can use the "invoke function"
operator of two parens.


__getattr__, __setattr__, __delattr__
=====================================

::

  print my_inst.foo
  my_inst.foo = 'value'
  del my_inst.foo

Attribute access using the dot operator can be overridden, too.

__enter__ and __exit__
======================

::

  with my_inst as context:
    do_something(context)

Adding __enter__ and __exit__ makes your class work as a context
manager, so you can use it with the "with" statement.

__len__
=======

::

  len(my_inst)

The len() built-in invokes the __len__ method

__hash__
========

::

  hash(my_inst)

  d = {my_inst: 'value'}

  s = {my_inst}

To control the way dictionary keys and set membership is computed,
override the __hash__ method.

__nonzero__
===========

::

  if my_inst:
    do_something()

__nonzero__ is called to convert an object to a boolean
representation

__contains__
============

::

  if 'foo' in my_inst:
    do_something()

  if 'bar' not in my_inst:
    do_something_else()

Python will fall back to scanning data structures, but using ``in`` to
test membership can make it more efficient.

Old-Style Comparison
====================

``__cmp__()`` returns a number representing the relationship.

:-1: The object is less than the argument.
:0: The object is equal to the argument.
:1: The object is greater than the argument.

**Warning**: This comparison style is deprecated.

Rich Comparison Methods
=======================

========  ==========
 Method    Operator
========  ==========
 __lt__     ``<``
 __le__     ``<=``
 __eq__     ``==``
 __ne__     ``!=``
 __gt__     ``>``
 __ge__     ``>=``
========  ==========

``functools.total_ordering``

Default Sorting
===============

.. literalinclude:: unsorted.py
   :lines: 4-11

Default Sorting
===============

.. literalinclude:: unsorted.py
   :lines: 14-22

*What will the output be?*

Default Sorting
===============

::

   $ python unsorted.py

   Jetson, George
   Jetson, Jane
   Jetson, Elroy
   Jetson, Judy

*Why?*

Custom Sorting
==============

.. literalinclude:: sortable.py
   :lines: 6-24
   :emphasize-lines: 1,10-24

.. note::

  ``total_ordering`` adds the missing comparison operations based on
  the 2 given.

Custom Sorting
==============

::

   $ python sortable.py

   Jetson, Elroy
   Jetson, George
   Jetson, Jane
   Jetson, Judy

Caveats
=======

- ``total_ordering`` requires two rich comparison methods.
- Easy to get carried away and abuse operator overloading.
- Python does not do any type checking for you.
- Special method names are reserved for internal use, so don't name
  arbitrary methods using the dunder scheme.

References
==========

- "Special Method Names"
  http://docs.python.org/2/reference/datamodel.html#special-method-names
