# Threading Patterns in Python
#
# The Producer-Consumer Pattern
# This is a very common pattern in multi-threading scenarios. In this pattern, one or
# more threads are doing some pre-processing and "producing" units of work, while another
# set of "consumer" or "worker" threads are actually doing the processing on these units
# of work. Often, a queue system is used to communicate between threads and provide
# synchronization.  These queue-linked producers and consumers can be chained together
# to form a type of pipeline.  The queue can also set a maximum size to limit how much 
# work is done at once.

import time
from threading import Thread, Event
from Queue import Queue, Empty

producers_complete = Event()
consumers_complete = Event()

source_queue = Queue()
work_queue = Queue()


def consumer(consumers_complete):
    print 'Consumer started.'
    while not consumers_complete.is_set():
        try:
            item = work_queue.get(True, 1)
            print 'Consumer is working on {0}'.format(item)
            time.sleep(1)
            work_queue.task_done()
        except Empty:
            print 'Consumer Work Queue was empty, no work to do.'

    print 'Consumer exited.'

def producer(producers_complete):
    print 'Producer started.'
    while not producers_complete.is_set():
        try:
            number = source_queue.get(True, 1)
            print 'Producer is generating work for item #{0}'.format(number)
            work_queue.put('Work Item #{0}'.format(number))
            source_queue.task_done()
        except Empty:
            print 'Producer Source Queue was empty, no work to do.'
    print 'Producer exited.'


def main():
    # Set up initial signal conditions

    # Create 5 consumers
    consumers = [Thread(target=consumer, args=(consumers_complete,)) for i in range(5)]
    # Create 3 producers
    producers = [Thread(target=producer, args=(producers_complete,)) for i in range(3)]

    # Provide some original source of work
    for i in xrange(100):
        source_queue.put(i + 1)

    # Start consumers and producers
    for c in consumers:
        c.start()
    for p in producers:
        p.start()

    # Wait until all the work has been picked up
    source_queue.join()
    # Signal all our producers threads to exit
    producers_complete.set()

    # Wait on all the work to be completed
    work_queue.join()
    consumers_complete.set()

    # Now wait on all the threads to exit
    for p in producers:
        p.join()
    for c in consumers:
        c.join()


if __name__ == '__main__':
    main()
