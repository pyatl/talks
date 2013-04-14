def read_file_data(filename):
    with open(filename) as f:
        return f.read()

def print_email_addrs(filename):
    # get the file
    data = read_file_data(filename)

    # get the words out of the file
    words = data.split()

    # print out the email addresses
    for word in words:
        if '@' in word and '=' not in word:
            print word


print_email_addrs('addresses.ldif')

