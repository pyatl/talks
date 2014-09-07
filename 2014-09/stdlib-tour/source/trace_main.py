#!/usr/bin/env python
from trace_recurse import recurse


def main():
    print 'This is the main program.'
    recurse(2)
    return

if __name__ == '__main__':
    main()
