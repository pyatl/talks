def read_file_data(filename):
    with open(filename) as f:
	    return f.read()

def words_in(data):
    return data.split()

data = read_file_data('addresses.ldif')
words = words_in(data)


