=====================================
 Getting Started With ``virtualenv``
=====================================

| PyLadiesATL
| July, 2013
| doug.hellmann@gmail.com
| @doughellmann
| http://doughellmann.com

The Problem
===========

None of us gets to work on a single version of a system, or on only
one project at a time.

Different projects mean *different dependencies*.

Changing dependencies == **Conflict**

Options
=======

1. Delete and reinstall packages
2. Separate physical or virtual computers
3. virtualenv

.. note::

  1. Deleting packages is error prone, dangerous, and annoying.
  2. Using a separate VM or physical machine for every task is
     expensive to set up and maintain.
  3. virtualenv brings similar isolation, but is easier to use.

What is virtualenv?
===================

- "micro python environment"
- separate directory for installing and using packages

Where ``import`` Looks for Modules
==================================

1. Location of the "main" program
2. ``PYTHONPATH`` environment variable
3. **sys.prefix** + ``lib/python$VERSION/site-packages``
4. **sys.exec_prefix** + ``lib/python$VERSION/site-packages``

How virtualenv Works
====================

*Tricks!*

Changes **sys.prefix** and **sys.exec_prefix**

Results in a new import path.

.. note::

   * virtualenv "cheats" by creating a separate copy of the Python
     interpreter.
   * Because the default import path includes directories based on the
     location of the interpreter, moving the interpreter changes the
     path.

Hands-on Section
================

1. Install virtualenv under your "user" packages directory

   ::

      $ pip install --user virtualenv

2. Make sure virtualenv is in your path

   ::

      $ export PATH=~/.local/bin:~/Library/Python/2.7/bin:$PATH

.. note::

   From this point on, I will go at a pace to let you run the commands
   on your own system.

   To start, we need to install virtualenv. I install it into my user
   package directory using the ``--user`` option, but it is also safe
   to install the system package with apt-get or yum if you prefer.

   The second step is only needed if you've never installed something
   into your user package directory.

Create a virtualenv
===================

::

  $ virtualenv env
  New python executable in env/bin/python
  Installing setuptools............done.
  Installing pip...............done.

.. note::

   Adding the -v option between the virtualenv command and the
   environment name will provide more output about what virtualenv is
   doing.

   virtualenv also accepts ``--help``.

Exploring
=========

::

  $ find env -type d
  env
  env/bin
  env/include
  env/lib
  env/lib/python2.7
  env/lib/python2.7/site-packages

.. note::

   If you look at the directories in the virtualenv, you will see
   something that looks like a normal Python installation with a
   ``bin``, ``lib/python2.7`` and ``site-packages`` directories.

Exploring: ``env/bin``
======================

Contains several useful executables

::

  $ ls env/bin
  activate
  activate.csh
  activate.fish
  activate_this.py
  easy_install
  easy_install-2.7
  pip
  pip-2.7
  python
  python2
  python2.7

.. note::

   The ``bin`` directory includes a few programs you'll recognize,
   like the interpreter and ``pip``.

   It also includes a script called ``activate``, which is...

Exploring: ``env/bin/activate``
===============================

A Bourne shell script for enabling the virtualenv.

.. code-block:: bash

    # ...
    VIRTUAL_ENV="/Users/dhellmann/tmp/virtualenv/env"
    export VIRTUAL_ENV
    
    _OLD_VIRTUAL_PATH="$PATH"
    PATH="$VIRTUAL_ENV/bin:$PATH"
    export PATH
    
    # unset PYTHONHOME if set
    # this will fail if PYTHONHOME is set to the empty string (which is bad anyway)
    # could use `if (set -u; : $PYTHONHOME) ;` in bash
    if [ -n "$PYTHONHOME" ] ; then
        _OLD_VIRTUAL_PYTHONHOME="$PYTHONHOME"
        unset PYTHONHOME
    fi
    # ...

.. note::

   The script sets up two variables.

   VIRTUAL_ENV refers to the full path of the environment, and is only
   used for convenience. For example, you can ``cd $VIRTUAL_ENV``.

   The ``PATH`` variable is the more important variable. The bin
   directory in the environment is added to the front of the shell's
   search path, so it is found before the one installed in the normal
   system location.

Exploring: ``env/lib/python2.7``
================================

Copy of standard library modules needed to bootstrap Python.

.. rst-class:: small
  
  .. code-block:: text
    
    $ ls env/lib/python2.7/
    UserDict.py      fnmatch.pyc              site-packages
    UserDict.pyc     genericpath.py           site.py
    _abcoll.py       genericpath.pyc          site.pyc
    _abcoll.pyc      lib-dynload              sre.py
    _weakrefset.py   linecache.py             sre_compile.py
    _weakrefset.pyc  linecache.pyc            sre_compile.pyc
    abc.py           locale.py                sre_constants.py
    abc.pyc          no-global-site-packages.txt  sre_constants.pyc
    codecs.py        ntpath.py                sre_parse.py
    codecs.pyc       orig-prefix.txt          sre_parse.pyc
    config           os.py                    stat.py
    copy_reg.py      os.pyc                   stat.pyc
    copy_reg.pyc     posixpath.py             types.py
    distutils        posixpath.pyc            types.pyc
    encodings        re.py                    warnings.py
    fnmatch.py       re.pyc                   warnings.pyc

.. note::

   The lib directory contains the subset of the standard library
   required to get the interpreter to start properly.

Exploring: ``env/lib/python2.7/site-packages``
==============================================

Private directory for installing modules and packages

::

  $ ls env/lib/python2.7/site-packages
  easy-install.pth
  pip-1.3.1-py2.7.egg
  setuptools-0.6c11-py2.7.egg
  setuptools.pth

.. note::

   And the site-packages directory is the analog for the system
   location where packages are installed globally.

Activating the virtualenv
=========================

::

  $ which python
  /Library/Frameworks/Python.framework/Versions/2.7/bin/python

::

  $ source env/bin/activate
  (env)$ 

  (env)$ which python
  /Users/dhellmann/tmp/virtualenv/env/bin/python

::

  (env)$ deactivate
  $

.. note::

   That activate script is used to "turn on" the environment, so that
   the programs you run can see it.

   Because you are sourcing it in the shell, only the current shell
   and its children see the environment.

Default Import Path
===================

.. rst-class:: small
  
  .. code-block:: text
  
    $ python -c 'import site; site._script()'
    sys.path = [
        '',
        '/Users/dhellmann/Library/Python/2.7/lib/python/site-packages/pip-1.3.1-py2.7.egg',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
        '/Users/dhellmann/Library/Python/2.7/lib/python/site-packages',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg-info',
        '/Library/Python/2.7/site-packages',
    ]
    USER_BASE: '/Users/dhellmann/Library/Python/2.7' (exists)
    USER_SITE: '/Users/dhellmann/Library/Python/2.7/lib/python/site-packages' (exists)
    ENABLE_USER_SITE: True

.. note::

   The import path without the virtualenv active includes my user
   site-packages directory and the directory where Python is installed
   for everyone.

virtualenv Import Path
======================

.. rst-class:: small

  .. code-block:: text
  
    (env)$ python -c 'import site; site._script()'
    sys.path = [
        '',
        '/Users/dhellmann/tmp/env/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg',
        '/Users/dhellmann/tmp/env/lib/python2.7/site-packages/pip-1.3.1-py2.7.egg',
        '/Users/dhellmann/tmp/env/lib/python27.zip',
        '/Users/dhellmann/tmp/env/lib/python2.7',
        '/Users/dhellmann/tmp/env/lib/python2.7/plat-darwin',
        '/Users/dhellmann/tmp/env/lib/python2.7/plat-mac',
        '/Users/dhellmann/tmp/env/lib/python2.7/plat-mac/lib-scriptpackages',
        '/Users/dhellmann/tmp/env/lib/python2.7/lib-tk',
        '/Users/dhellmann/tmp/env/lib/python2.7/lib-old',
        '/Users/dhellmann/tmp/env/lib/python2.7/lib-dynload',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
        '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
        '/Users/dhellmann/tmp/env/lib/python2.7/site-packages',
    ]
    USER_BASE: '/Users/dhellmann/.local' (doesn't exist)
    USER_SITE: '/Users/dhellmann/.local/lib/python2.7/site-packages' (doesn't exist)
    ENABLE_USER_SITE: False

.. note::

   With the virtualenv active, most of the global directories are
   added to the path before the virtualenv.

Installing Packages
===================

::

  (env)$ which tox
  (env)$ 

::

  (env)$ pip install tox

  Downloading/unpacking tox
    Downloading tox-1.5.0.tar.gz (73kB): 73kB downloaded
    Running setup.py egg_info for package tox

  ...

  Successfully installed tox virtualenv py
  Cleaning up...

::

  (env)$ which tox
  /Users/dhellmann/tmp/env/bin/tox


Other Uses for virtualenv
=========================

- Testing combinations of libraries
- Testing versions of Python

Testing cliff
=============

::

  (env)$ cd $VIRTUAL_ENV

::

  (env)$ git clone https://github.com/dreamhost/cliff.git
  Cloning into 'cliff'...
  remote: Counting objects: 1025, done.
  remote: Compressing objects: 100% (427/427), done.
  remote: Total 1025 (delta 620), reused 995 (delta 595)
  Receiving objects: 100% (1025/1025), 182.64 KiB, done.
  Resolving deltas: 100% (620/620), done.

::
  
  (env)$ cd cliff

Testing cliff
=============

::

  (env)$ tox -e py27
  GLOB sdist-make: /Users/dhellmann/tmp/env/cliff/setup.py
  py27 create: /Users/dhellmann/tmp/env/cliff/.tox/py27
  py27 installdeps: nose, mock, coverage
  py27 inst: /Users/dhellmann/tmp/env/cliff/.tox/dist/cliff-1.4.zip
  py27 runtests: commands[0] | nosetests -d --with-coverage --cover-inclusive --cover-package cliff
  .................................
  Ran 33 tests in 0.228s
  
  OK
  _________________________________________________ summary _________________________________________________
    py27: commands succeeded
    congratulations :)

Testing cliff
=============

::

  (env)$ tox -e py33
  py33 create: /Users/dhellmann/tmp/env/cliff/.tox/py33
  py33 installdeps: nose, mock, coverage
  py33 inst: /Users/dhellmann/tmp/env/cliff/.tox/dist/cliff-1.4.zip
  .................................
  Ran 33 tests in 0.248s
  
  OK
  _________________________________________________ summary _________________________________________________
    py33: commands succeeded
    congratulations :)

What did tox do?
================

Two virtualenvs were created, with different versions of Python

::

  (env)$ ls .tox
  dist
  log
  py27
  py33

  (env)$ ls .tox/py27/bin/python*
  python
  python2
  python2.7

  (env)$ ls .tox/py33/bin/python*
  python
  python3
  python3.3

Using virtualenv Without ``activate``
=====================================

Because Python builds its import path based on the location of the
interpreter, it is not necessary to "activate" a virtualenv to use it.

Exploring ``.tox/py27``
=======================

::

  (env)$ .tox/py27/bin/pip freeze
  cliff==1.4
  cmd2==0.6.5.1
  coverage==3.6
  mock==1.0.1
  nose==1.3.0
  prettytable==0.7.2
  pyparsing==1.5.7     <===
  wsgiref==0.1.2


Exploring ``.tox/py33``
=======================

::

  (env)$ .tox/py33/bin/pip freeze
  cliff==1.4
  cmd2==0.6.5.1
  coverage==3.6
  distribute==0.6.34
  mock==1.0.1
  nose==1.3.0
  prettytable==0.7.2
  pyparsing==2.0.0    <===


Caveats
=======

- Not all packages can be installed under virtualenv (pygame)
- Python 3.3 includes ``venv``, which works slightly differently
- Proliferation of virtualenvs can get confusing (see
  virtualenvwrapper)

References
==========

- virtualenv

  - http://www.virtualenv.org/en/latest/
  - https://github.com/pypa/virtualenv

- This presentation

  - https://github.com/pyatl/talks

- ``import``

  - http://pymotw.com/2/sys/imports.html
  - http://pymotw.com/2/site/
  - http://effbot.org/zone/import-confusion.htm
