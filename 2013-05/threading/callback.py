# Threading Patterns in Python
#
# The "Callback" pattern.
# This pattern is not strictly a parallel / threading pattern, but often
# comes up in asychronous development or multi-threading scenarios.
# This is also common in scenarios when using a third party library that
# you may have little to no control over.
# Some thread typically runs as an "engine" or main thread, doing various
# types of processing.  Other threads under your control are able to register
# callback functions which are called when certain events occur during the main
# threading processing.
#
#  
#  Start --> Engine (loops) --> Complete
#                   |
#                   ---> Callback function
#

import time
from threading import Thread


def engine(fizz_callback, buzz_callback):
    for i in xrange(100):
        # Engine does some work
        time.sleep(1)
        if i % 3 == 0:
            fizz_callback(i)
        if i % 5 == 0:
            callback_thread = Thread(target=buzz_callback, args=(i,))
            callback_thread.start()

def fizz_handler(num):
    print 'Value {0} is FIZZ'.format(num)

def buzz_handler(num):
    print 'Value {0} is BUZZ'.format(num)

def main():
    engine_thread = Thread(target=engine, args=(fizz_handler, buzz_handler))

    engine_thread.start()
    engine_thread.join()


if __name__ == '__main__':
    main()
