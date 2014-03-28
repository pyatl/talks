# coding=utf-8
#
#   Hello World server in Python
#   Connects REP socket to tcp://localhost:5555
#   Receives "Hello" from client, sends "World" back

from time import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print "[{}] Received {}".format(time(), message)
    socket.send("World")
