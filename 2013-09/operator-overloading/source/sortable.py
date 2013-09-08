#!/bin/env python

import functools


@functools.total_ordering
class Person(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return ', '.join([self.last, self.first])

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (self.last, self.first) == (other.last, other.first)

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (self.last, self.first) < (other.last, other.first)


data = [
    Person('George', 'Jetson'),
    Person('Jane', 'Jetson'),
    Person('Elroy', 'Jetson'),
    Person('Judy', 'Jetson'),
]

for p in sorted(data):
    print p
