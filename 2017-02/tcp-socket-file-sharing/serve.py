#! /usr/bin/env python3
import socket

image = open('helpme.jpg', 'rb')

sock = socket.socket()
# When you set a socket option, you set its name and level
# The level argument (SOL_SOCKET) specifies the protocol level at which the
# option (SO_REUSEADDR) resides
#
# SO_REUSEADDR tells the kernel that even if this port is busy (in
# the TIME_WAIT state), go ahead and reuse it anyway
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 8080))
print('Listening on 0.0.0.0:8080')

sock.listen(1)  # number of queued connections

client, addr = sock.accept()
print('Got connection from', addr)
client.sendfile(image)
for x in [client, sock, image]:
    x.close()
