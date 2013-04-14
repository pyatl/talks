with open('addresses.ldif') as f:
    words = f.read().split()

emails = [word for word in words if '@' in word and '=' not in word]

print 'length:', len(emails)
print 'sorted:', sorted(emails)
print 'reversed:', list(reversed(emails))
print 'sorted reverse:', sorted(emails, reverse=True)

shortest = sorted(emails, key=len)[0]
print 'shortest:', shortest, '(', len(shortest), ')'

longest = sorted(emails, key=len, reverse=True)[0]
longest = sorted(emails, key=len)[-1]

# MINUS 1 ???!?!?!?!!!1
print 'longest:', longest, '(', len(longest), ')'
