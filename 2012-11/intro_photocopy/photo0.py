# tell python we need system services
import sys

# sys.argv[1] is the first argument to our script, e.g. 'e:\':
#
#  % python photo0.py e:\
#
# what do you think this program will do if you forget it?
#
#   % python photo0.py
#
source = sys.argv[1]

print 'pretending to look for jpgs in', source

