import csv
from collections import namedtuple

Bracket = namedtuple(
    'Bracket', 
    'tax_rate single married_joint'
)

with open('simple_brackets.csv', 'rb') as f:
    reader = csv.reader(f)

    # skip the header
    next(reader)

    brackets = map(Bracket._make, reader)

print brackets
