# Threading Patterns in Python
#
# The "Barrier" pattern.
# This pattern is used when you need to have multiple threads doing work,
# and additional work needs to be completed, but only AFTER the other threads
# have first completed their work.  You can think of it like a dependency tree,
# like so:
#
#  
#            --> Task A -->
#  Start --> --> Task B --> --> Task D --> Complete
#            --> Task C -->

import time
from threading import Thread, Event

A = Event()
B = Event()
C = Event()
D = Event()

def taskA():
    print 'Task A is doing some work'
    time.sleep(4)
    A.set()
    D.wait()
    print 'Task A is exiting'

def taskB():
    print 'Task B is doing some work'
    time.sleep(1)
    B.set()
    D.wait()
    print 'Task B is exiting'

def taskC():
    print 'Task C is doing some work'
    time.sleep(3)
    C.set()
    D.wait()
    print 'Task C is exiting'

def taskD():
    print 'Task D is waiting on other tasks'
    A.wait()
    B.wait()
    C.wait()
    print 'Task D is doing some work'
    time.sleep(1)
    D.set()
    print 'Task D is exiting'


def main():

    # Create our threads
    tasks = [
            Thread(target=taskA),
            Thread(target=taskB),
            Thread(target=taskC),
            Thread(target=taskD),
    ]

    print '"Main" is starting threads'
    # Start all the threads running
    for task in tasks:
        task.start()

    print '"Main" is waiting for threads to finish'
    for task in tasks:
        task.join()


if __name__ == '__main__':
    main()

