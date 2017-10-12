#!/usr/bin/env python
'''
Implement a UDP server and client program. It is a echo client program. The message typed by the client should be echoed back to the client by the server. Each client connection should be handled by a thread.
'''
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.  It will be repeated.'

try:

    # Send data
    print(sys.stderr, 'sending "%s"' % message)
    sent = sock.sendto(message, server_address)

    # Receive response
    print(sys.stderr, 'waiting to receive')
    data, server = sock.recvfrom(4096)
    print(sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()