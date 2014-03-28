# Task worker
# Connects PULL socket to tcp://localhost:5557
# Collects workloads from ventilator via that socket
# Connects PUSH socket to tcp://localhost:5558
# Sends results to sink via that socket
#
# Based on an example by Lev Givon <lev(at)columbia(dot)edu>

import sys
import time

import zmq

from resize_image import format_output_filename, resize_image

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

# Process tasks forever
while True:
    image_name, image_data = receiver.recv_pyobj()

    # Simple progress indicator for the viewer
    sys.stdout.write('.')
    sys.stdout.flush()

    # Do the work
    for size in (64, 128, 256):
        output_filename = format_output_filename(image_name, size)
        resize_image(image_data, size, output_filename)

        # Send results to sink
        sender.send(output_filename)
