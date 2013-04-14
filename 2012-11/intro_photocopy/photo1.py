# tell python we need OS and system services
import os
import sys


# get the location of the JPEGs to copy from the command line
source = sys.argv[1]

print 'looking for jpgs in', source


# http://docs.python.org/2/library/os.html#os.walk

# starting in source, looking each subdirectory for JPEGs
#
# path: what directory we are in on the filesystem
# files: the list of all the files in that directory
for path, subdirs, files in os.walk(source):

    # look at each file individually
    for filename in files:

    	# if it is a JPEG
        if filename.endswith('jpg'):

	    # combine the path (directory) with the file name to produce the
	    # "absolute" location of the file
            fullname = os.path.join(path, filename)
            print fullname

