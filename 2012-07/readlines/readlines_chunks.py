#!/usr/bin/env python

input_filename = '/Users/dhellmann/Dropbox/Org/dreamhost.org'

CHUNK = 5000

with open(input_filename, 'rt') as f:
    num_lines = 0
    while True:
        lines = f.readlines(CHUNK)
        print '  ', len(lines)
        if not lines:
            break
        num_lines += len(lines)

print 'total lines:', num_lines
