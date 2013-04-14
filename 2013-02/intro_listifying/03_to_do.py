to_do = [
    'go to PyATL', 
    'laugh at dan\'s lame jokes',
    'buy him a beer',
    'how many email addresses',
    'sort email addresses',
    'longest/shortest'
]

header = 'To Do List'

print
print header
print '-' * len(header)
print

for n, item in enumerate(to_do):
    print n, item

print
print

# oh, so you want it 1-indexed, do you?
for n, item in enumerate(to_do, 1):
    print n, item
