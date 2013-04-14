
====================
How to Eat a Problem
====================

:Author: Daniel J. Rocco, Ph.D.


A demonstration of software development through iterative refinement: breaking
a problem into logical chunks, coding a bit, testing, and repeating until the 
problem is solved.

The example involved a Python script to copy files.

Topics covered:

*   iterative software development
*   Python's ``if`` conditional and ``for`` looping control structures
*   reading arguments from the command line
*   OS file services, including copying files walking directory trees


Organization
============

``photo0.py``
    getting an argument from the command line
    
``photo1.py``
    walking a directory tree
    
``photo2.py``
    put it all together, copying files from one location to another
    
``photocopy.py``
    the (somewhat rough) program that I actually use to do this task, which 
    utilizes two external programs (``jhead`` and ``exiftool``), performs 
    lossless, automatic image rotation based on the camera's rotation sensor, 
    names photos by time stamp, and organizes photos by date.
    
``locator.py``
    Helper module used by ``photocopy.py`` based on a recipe on ActiveState.  
    It demonstrates some more sophisticated directory traversal techniques.

Resources
=========

*   `The Python Tutorial <http://docs.python.org/2/tutorial/>`_
*   |The os module|_ 
*   `jhead <http://www.sentex.net/~mwandel/jhead/>`_
*   `ExifTool <http://www.sno.phy.queensu.ca/~phil/exiftool/>`_

.. |The os module| replace:: The ``os`` module
.. _The os module: http://docs.python.org/2/library/os.html