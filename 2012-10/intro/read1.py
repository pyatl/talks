with open('addresses.ldif') as f:
    print f.name
    data = f.read()

print len(data)

print len(data.split('\n'))


