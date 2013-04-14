import csv

with open('simple_brackets.csv', 'rb') as f:
    reader = csv.reader(f)
    brackets = list(reader)

print brackets
