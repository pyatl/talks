import os
import fnmatch

# ====================================================================
# file locator

### FIXME: need to move to a local site package
def locate(pattern, root=os.curdir, absolute=True,
		   excludeDirs=["CVS", ".svn", ".hg"]):
	"""Locate all filenames matching supplied pattern in and below root.

	Given a UNIX-style filename pattern, locate all filenames in and below
	the supplied root directory that match the pattern.  If ``root`` is
	omitted, ``os.curdir`` is used.

	Returns the absolute path of each matching filename.  Change
	``absolute`` to ``False`` to produce pathnames relative to ``root``

	Directories contained in ``excludeDirs`` are not searched; by default
	``locate()`` excludes CVS and Subversion metadata directories from its
	search.
	
	Since this is a	generator function, the results are lazy evaluated.
	
	From: http://code.activestate.com/recipes/499305/

	----------

	
	To iterate over every matching file and do something to it, you would
	normally use a for loop, like so:

	>>> for filename in locate("query*", absolute=False):
	... 	print filename
	...
	.\query_tags.py
	...
	

	Sometimes, however, it is helpful to work with the entire list of
	matches at once:

	>>> filenames = [name for name in locate("*.txt", absolute=False)]
	>>> len(filenames) == 30
	True
	>>> r".\\data\\photos\\2009_01_06\\tags.txt" in filenames
	True
	>>> r".\\query_tags.py" in filenames
	False


	Let's make sure ``locate()`` still works when fed bogus data:
	
	>>> [name for name in locate("nonexistent.*")]
	[]
	>>> [name for name in locate("*.txt", root=".\\nonexistent")]
	[]
	"""
	if absolute:
		root = os.path.abspath(root)
		
	for path, dirs, files in os.walk(root):

		# remove excluded directories, helpful for skipping CVS/subversion
		# metadata files
		for directory in excludeDirs:
			if directory in dirs:
				dirs.remove(directory)
				
		for filename in fnmatch.filter(files, pattern):
			yield os.path.join(path, filename)

