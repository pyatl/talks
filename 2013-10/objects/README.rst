Musing about Objects
====================

Support code for my `Musing about Objects`_ October PyAtl talk.

``15-puzzle_old_version.py`` is the version I wrote as an assignment in 2009.
It uses ``doctest`` as the testing framework; running the file will invoke the
tests.

The ``fifteen_puzzle`` package contains the newer implementation; its test
suite is in ``tests``.  You'll need ``pytest`` to run them::

    py.test tests

``NetworkX_sandbox.ipynb`` is an IPython notebook of my explorations of
`NetworkX`_, which provided the graph data structure for the newer version.

.. _Musing about Objects: http://pyatl.github.io/talks/2013-10_objects/
.. _NetworkX: http://networkx.github.io/
