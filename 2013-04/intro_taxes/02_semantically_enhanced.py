import csv
from collections import namedtuple

# create a namedtuple to represent the rows of our csv file
Bracket = namedtuple(
    'Bracket', 
    'tax_rate single married_joint'
)

with open('simple_brackets.csv', 'rb') as f:
    reader = csv.reader(f)

    # map calls a function (Bracket._make) on each element of a list (or list-
    # like object).  Roughly translated to English, this line reads "make a
    # Bracket object out of each row of the csv file, storing the list of 
    # Brackets in the variable 'brackets'"
    brackets = map(Bracket._make, reader)

print brackets
