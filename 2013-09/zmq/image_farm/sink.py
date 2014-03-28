import sys
from time import time

import zmq

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

while True:
    image_name = receiver.recv()
    print '[{}] {} generated'.format(time(), image_name)
