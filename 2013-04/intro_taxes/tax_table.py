import csv

from brackets import Bracket
from tax import tax


filename = 'simple_tax_table.csv'


with open(filename, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['earnings'] + list(Bracket._fields[1:]))

    for amount in xrange(5000, 100001, 5000):

        # first column: earnings amount
        data = [amount]

        data += [tax(amount, filing_status) 
	         for filing_status in Bracket._fields[1:]]

        writer.writerow(data)


print 'tax table written to', filename
