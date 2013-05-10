for i in xrange(101):
    out = []
    if not i % 3:
        out.append('Fizz')
    if not i % 5:
        out.append('Buzz')
    if not out:
        out.append(str(i))
    print ''.join(out)
