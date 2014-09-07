========================================
 Creating Presentations with Hieroglyph
========================================

Hieroglyph (https://pypi.python.org/pypi/hieroglyph) is a Sphinx
(https://pypi.python.org/pypi/Sphinx) builder for converting
reStructuredText files to HTML slide presentations. It lets you write
simple text files with headings, lists, and embedded code samples and
then turns them into slide presentations for you.

Example
=======

First, you need a copy of cookiecutter
(https://pypi.python.org/pypi/cookiecutter) installed. Cookiecutter
uses templates to populate a directory with the files needed for a
project. You can use the template for hieroglyph at
https://github.com/dhellmann/cookiecutter-hieroglyph to create a basic
presentation, which you can then modify with your own content.

::

  $ pip install cookiecutter

Next, create a directory to contain the inputs for the
presentation::

  $ mkdir mypres
  $ cd mypres

Now run cookiecutter to create the basic presentation files::

  $ cookiecutter https://github.com/dhellmann/cookiecutter-hieroglyph
  config_path is /Users/dhellmann/.cookiecutterrc
  Cloning into 'cookiecutter-hieroglyph'...
  remote: Counting objects: 19, done.
  remote: Compressing objects: 100% (5/5), done.
  remote: Total 19 (delta 0), reused 0 (delta 0)
  Unpacking objects: 100% (19/19), done.
  Checking connectivity... done.
  full_name (default is "Doug Hellmann")?
  email (default is "doug@doughellmann.com")?
  twitter (default is "doughellmann")?
  repo_name (default is "talk")?
  meeting_date (default is "Date of meeting")? 2014-09
  title (default is "Title of your presentation")? A Whirlwind Tour of the Standard Library

This creates a few files::

  $ tree .
  .
  ├── Makefile
  ├── requirements.txt
  └── source
      ├── _static
      │   └── custom.css
      ├── conf.py
      └── index.rst

  2 directories, 5 files

Put your content in ``source/index.rst``, using some of the other
hieroglyph-based presentations in this repository as examples.

To build your slides, just run ``make``. It will use virtualenv
(https://pypi.python.org/pypi/virtualenv) to install the tools it
needs and then use those tools to convert your input file to HTML.

::

  $ make
  virtualenv .venv
  New python executable in .venv/bin/python
  Installing setuptools, pip...done.
  .venv/bin/pip install -r requirements.txt
  Downloading/unpacking Sphinx (from -r requirements.txt (line 1))

  ... lots more download and installation output elided ...

  Successfully installed Sphinx hieroglyph flake8 Jinja2 Pygments docutils 
    six pyflakes mccabe pep8 markupsafe
  Cleaning up...
  ./.venv/bin/sphinx-build -b slides -d build/doctrees   source build/slides
  Making output directory...
  Running Sphinx v1.2.3
  loading pickled environment... not yet created
  building [slides]: targets for 1 source files that are out of date
  updating environment: 1 added, 0 changed, 0 removed
  reading sources... [100%] index
  looking for now-outdated files... none found
  pickling environment... done
  checking consistency... done
  preparing documents... done
  writing output... [100%] index
  writing additional files... genindex search
  copying static files... done
  copying extra files... done
  dumping search index... done
  dumping object inventory... done
  build succeeded, 1 warning.

  Build finished. The slides are in build/slides.

The output presentation is in ``./build/slides/index.html``. All of
the required files should be present under ``build/slides``, allowing
you to give your presentation even without internet access.
