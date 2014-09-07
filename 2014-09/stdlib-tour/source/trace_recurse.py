def recurse(level):
    print 'recurse(%s)' % level
    if level:
        recurse(level-1)
    return
