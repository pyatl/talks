
=========================
Intro to Python Scripting
=========================

:Author: Daniel J. Rocco, Ph.D.


A short introduction to Python scripting basics using the example of
extracting email addresses from a weird data file.

Topics covered:

*   how to read in a file
*   objects: *know stuff* and *do stuff*
*   packaging code into *functions*—named, reusable blobs of code
*   working with *variables*, which are named handles to objects


Organization
============

``read1.py``
    opening the file, reading its data, calculating the number of characters/words

``read2.py``
    package reading the file as a function, storing the result in a variable

``words.py``
    splitting the file's data into words

``extract_addr.py``
    put it all together, loop over the words in the file and print only the email addresses


Resources
=========

*   `The Python Tutorial <http://docs.python.org/2/tutorial/>`_
*   `Dive Into Python <http://www.diveintopython.net/toc/index.html>`_
