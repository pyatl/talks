# Task ventilator
# Binds PUSH socket to tcp://localhost:5557
# Sends batch of tasks to workers via that socket

import sys
from time import sleep

import zmq

context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

for filename in sys.argv[1:]:
    with open(filename, 'rb') as f:
        payload = filename, f.read()

        # Why, yes: Python *is* awesome!
        sender.send_pyobj(payload)

        sleep(0.25)
