import zmq

# Awkward factory for setting up listener processes. sentinel is the "divisible
# by" value we're looking for and message is the message we print out. Usually
# called with 3, 'FIZZ' and 5, 'BUZZ'.

def fizzerbuzzer(sentinel, message):
    #  Socket to talk to message publisher
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")

    socket.setsockopt(zmq.SUBSCRIBE, '')

    # Synchronization: we'll most likely connect in the middle of the
    # publisher's message cycle, so wait till we see '100' before starting.
    while True:
        if socket.recv() == '100':
            break

    # Process 100 updates
    for index in range(100):
        value = socket.recv()
        value = int(value)

        if not value % sentinel:
            print message
        else:
            print value
