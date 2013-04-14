from __future__ import print_function
from os import remove, rmdir

from shutil import copy
from subprocess import call
import sys
from tempfile import mkdtemp

from locator import locate


source = sys.argv[1]
tempdir = mkdtemp()

print('creating temporary directory ' + tempdir)

print('copying files', end='')
count = 0

match_pattern = '*.[jn][pe][gf]'

for photo in locate(match_pattern, root=source):
    print('.', end='')
    count += 1

    copy(photo, tempdir)

print(' done.  Copied {0} files.'.format(count))

print('auto rotate and date stamp photos...')

call('jhead -ft -autorot {0}/*.jpg'.format(tempdir))

print('copying photo files...')

call('exiftool "-Filename<CreateDate" -d /photos/%Y_%m_%d/%Y%m%d-%H%M%S%%-c.%%e {0}/'.format(tempdir))

print('removing originals and temporary directory...')

rmdir(tempdir)

for photo in locate(match_pattern, root=source):
    remove(photo)

print('\nphotocopy complete.')
