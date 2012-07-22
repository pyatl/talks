#!/usr/bin/env python

import itertools

input_filename = '/Users/dhellmann/Dropbox/Org/dreamhost.org'

total_bytes = len(open(input_filename, 'rt').read())

print '%10s  %5s  %5s  %s' % ('bufsize', 'mult', 'lines', 'bytes')

for i in itertools.chain(
    xrange(1, 1000, 200),
    xrange(1000, 6000, 1000),
    [8192],
    xrange(10000, total_bytes + 5000, 5000),
    ):

    with open(input_filename, 'rt') as f:
        lines = f.readlines(i)
        print '%10d  %5d  %5d  %5d' % \
            (i, i / 8192, len(lines), len(''.join(lines)))
