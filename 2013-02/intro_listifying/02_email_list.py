# define some functions

def read_file_data(filename):
    with open(filename) as f:
        return f.read()


def email_addrs(words):
    # um... we need a list...
    lst = []

    for word in words:
        if '@' in word and '=' not in word:
            lst.append(word)

    return lst


# now actually do stuff

data = read_file_data('addresses.ldif')
words = data.split()

# Pop quiz: what is a variable?
emails = email_addrs(words)
print '\n'.join(emails)
