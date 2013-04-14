
==================
The Tax Man Cometh
==================

---------------------------
Or: The Other Inevitability
---------------------------


:Author: Daniel J. Rocco, Ph.D.


Tax season gave me an excuse to look at the ``csv`` module to show how one 
could read in CSV data, manipulate it, and write out a CSV file using Python.

Topics covered:

*   reading in a CSV file
*   creating a lightweight model of a tax bracket using ``namedtuple``
*   using ``map`` to call a function on each element of a list
*   massaging the string data from a CSV into a more useful numeric format with
    Python's ``Decimal`` class
*   problem analysis: breaking down the "compute tax" problem into a set of 
    prerequisites and a list of smaller steps
*   review of some of Python's list mechanisms including comprehensions and the 
    ``sum`` function
*   writing out a CSV file


Organization
============

``01_csv2.py``
    read in a CSV file and print out its rows
    
``01b_csv2.py``
    read in a CSV file and convert its rows to a list

``02_semantically_enhanced.py``
    create a lightweight model of a tax bracket using ``namedtuple``; use the 
    ``Bracket._make`` function to convert the rows of the CSV file to Bracket 
    objects
    
``brackets.py``
    further process the input data by converting strings to ``Decimal`` objects 
    more suited for mathematical calculations

``03_split_by_bracket.txt``
    sketches out the design of our tax calculator, which includes the 
    prerequisite information needed to perform the calculation and the steps 
    involved in the calculation itself
        
``split_by_bracket.py``
    implementation of 03 step 1, including some sample calculations
        
``tax.py``
    implementation of the tax calculator, including some sample calculations
        
``tax_table.py``
    uses ``tax.py`` to write out a tax table
        
``simple_brackets.csv``
    the example brackets, which present a simplified progressive tax model.  
    Changing the values here (e.g. using tax schedule data available on the 
    web) will update the brackets used by the examples above


Running the Examples
--------------------

I've added support code to the example Python programs above to allow them to 
be run standalone.  All you will need is a working Python installation; for 
example::

    $ python tax.py
    single $5000: 500.0
    single $11000: 1200.0
    single $24000: 4200.0
    
    married $7000: 700.0
    married $15000: 1500.0
    married $19000: 2300.0
    married $31000: 4800.0


Recursive implementation of ``split_by_bracket``
------------------------------------------------

Due to popular demand I have added a recursive implementation of 
``split_by_bracket`` in ``split_by_bracket_recursive.py`` along with some 
example runs.


Resources
=========

*   `The Python Tutorial <http://docs.python.org/2/tutorial/>`_
*   `The csv module <http://docs.python.org/2/library/csv.html>`_ 
*   `The collections module, home of namedtuple <http://docs.python.org/2/library/collections.html>`_ 
*   `Python's Decimal <http://docs.python.org/2/library/decimal.html>`_ 
*   `Tax Bracket Article <http://en.wikipedia.org/wiki/Tax_bracket>`_; source of the simple brackets used in the demo
