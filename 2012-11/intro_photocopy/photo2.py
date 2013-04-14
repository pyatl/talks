import os
import sys

from shutil import copy


source = sys.argv[1]
target = '/tmp/photos/'

print 'copying jpgs from', source, 'to', target


# http://docs.python.org/2/library/os.html#os.walk

# path: what directory we are in on the filesystem
# files: the list of all the files in that directory
for path, subdirs, files in os.walk(source):
    for filename in files:
        if filename.endswith('jpg'):
            fullname = os.path.join(path, filename)
            copy(fullname, target)
            print '.',

