from itertools import cycle
import time

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

for index in cycle(range(1, 101)):
    socket.send(str(index))
    time.sleep(0.05)
