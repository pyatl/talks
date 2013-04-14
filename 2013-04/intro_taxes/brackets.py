import csv
from collections import namedtuple
from decimal import Decimal


Bracket = namedtuple(
    'Bracket', 
    'tax_rate single married_joint'
)


def process_row(row):
    """Given a row of data, make a Bracket out of the row while converting each 
    element to a Decimal

        >>> process_row(('0.1', '2', '3.4'))
	Bracket(tax_rate=Decimal('0.1'), single=Decimal('2'), married_joint=Decimal('3.4'))	

    """

    return Bracket._make(map(Decimal, row))


with open('simple_brackets.csv', 'rb') as f:
    reader = csv.reader(f)

    # skip the header
    next(reader)

    brackets = map(process_row, reader)


# we will need the brackets list later; this next bit will print out the 
# brackets if you say
#
#       python brackets
#
# from the command line but not if some other part of the program imports them

if __name__ == '__main__':
    print brackets
