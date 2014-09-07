==========================================
 A Whirlwind Tour of the Standard Library
==========================================

| Doug Hellmann
| doug@doughellmann.com
| @doughellmann
| PyATL
| 2014-09

``string``: Simple Templates
============================

.. literalinclude:: string_template.py

::

  TEMPLATE:
  foo
  $
  fooiable

.. note::

   Also includes ASCII constants.

``textwrap``: Formatting
========================

* fill / wrap / justify
* indent
* dedent
* hanging indent



``re``: Pattern Matching
========================

* regular expressions
* search
* replace

Numeric and Mathematical
========================

* decimal – fixed decimal arithmetic
* fractions – rational numbers
* math – specialized mathematical functions
* random – pseudo-random number generators

``time`` and ``datetime``
=========================

.. literalinclude:: time_info.py

::

  TIME: 1410107908.56
  TODAY: 2014-09-07 12:38:28.574200

``collections``: Data Structures
================================

* namedtuple
* deque
* Counter
* OrderedDict
* defaultdict

Data Formats
============

* json – JavaScript Object Notation
* base64 – ASCII encoding of binary data
* csv – Comma Separated Value
* pickle – Python-specific serialization format

Archive formats
===============

* tarfile
* zipfile

Compression
===========

* zlib
* gzip
* bz2

.. note::

   These can be combined with the tarfile module, but they can also be
   applied to other files and even sockets or other data streams that
   are not files.

Databases
=========

* Key/Value stores

  * anydbm
  * shelve

* Relational Database

  * sqlite3

Operating System Tools
======================

* os – interface to the operating system
* os.path – work with filenames
* sys – interface to the running system

Application Building Tools
==========================

* argparse – command line arguments
* logging – files, remote services, etc.
* getpass – ask for data securely
* readline – interactive prompting
* cmd – interactive command shell framework
* gettext – internationalization and translation
* fileinput – UNIX pipeline tool framework

Concurrency
===========

* threading – single-process concurrent execution
* Queue – FIFO data structure
* multiprocessing – manage multiple processes as threads

Internet Tools
==============

* urllib/urllib2 – retrieve data
* urlparse – work with URLs
* SimpleHTTPServer – static content server
* xmlrpclib – remote function execution over HTTP
* SimpleXMLRPCServer – serve functions over HTTP

Testing Tools
=============

* unittest – test framework
* doctest – tests in documentation
* pdb – debugger
* profile – performance analysis
* trace – watch statements being executed

``trace``
=========

.. literalinclude:: trace_main.py

.. literalinclude:: trace_recurse.py

``trace``
=========

::

  $ python trace_main.py
  This is the main program.
  recurse(2)
  recurse(1)
  recurse(0)

``trace``
=========

.. rst-class:: small

    ::

      $ python -m trace --trace trace_main.py
       --- modulename: trace_main, funcname: <module>
      trace_main.py(2): from trace_recurse import recurse
       --- modulename: trace_recurse, funcname: <module>
      trace_recurse.py(4): def recurse(level):
      trace_recurse.py(11): def not_called():
      trace_main.py(5): def main():
      trace_main.py(10): if __name__ == '__main__':
      trace_main.py(11):     main()
       --- modulename: trace_main, funcname: main
      trace_main.py(6):     print 'This is the main program.'
      This is the main program.
      trace_main.py(7):     recurse(2)
       --- modulename: trace_recurse, funcname: recurse
      trace_recurse.py(5):     print 'recurse(%s)' % level
      recurse(2)
      trace_recurse.py(6):     if level:
      trace_recurse.py(7):         recurse(level-1)
       --- modulename: trace_recurse, funcname: recurse
      trace_recurse.py(5):     print 'recurse(%s)' % level
      recurse(1)
      trace_recurse.py(6):     if level:
      trace_recurse.py(7):         recurse(level-1)

      ...


Language Tools
==============

* gc – garbage collector
* inspect – ask questions about code objects at runtime
* imp – module import system
* dis - show the byte-code for source

``dis``
=======

.. literalinclude:: dis_simple.py
   :linenos:

(line num, instruction, opcode, arguments)

::

    $ python -m dis dis_simple.py
      4           0 BUILD_MAP                1
                  3 LOAD_CONST               0 (1)
                  6 LOAD_CONST               1 ('a')
                  9 STORE_MAP
                 10 STORE_NAME               0 (my_dict)
                 13 LOAD_CONST               2 (None)
                 16 RETURN_VALUE

References
==========

Internet

* https://docs.python.org/2.7/library/index.html
* http://pymotw.com

Books

* *Python Essential Reference* – Beasley
* *The Python Standard Library by Example* – Hellmann
