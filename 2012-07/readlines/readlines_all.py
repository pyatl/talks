#!/usr/bin/env python

input_filename = '/Users/dhellmann/Dropbox/Org/dreamhost.org'

body = open(input_filename, 'rt').read()
total_bytes = len(body)
total_lines = len(body.splitlines())
print 'total bytes:', total_bytes

with open(input_filename, 'rt') as f:
    lines = f.readlines()
    print 'total lines:', len(lines)
