def read_file_data(filename):
    with open(filename) as f:
	    return f.read()

data = read_file_data('addresses.ldif')

