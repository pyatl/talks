import csv

with open('simple_brackets.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print ', '.join(row)
