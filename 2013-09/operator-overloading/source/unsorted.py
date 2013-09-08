#!/bin/env python


class Person(object):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return ', '.join([self.last, self.first])


data = [
    Person('George', 'Jetson'),
    Person('Jane', 'Jetson'),
    Person('Elroy', 'Jetson'),
    Person('Judy', 'Jetson'),
]

for p in sorted(data):
    print p
