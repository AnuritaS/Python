#!/usr/bin/python
'''Write a TCP/IP server and client program. It is a echo client program. The message typed by the client should be echoed back to the client by the server. Each client connection should be handled by a thread.
'''
from socket import *
import time
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.connect(("localhost",9030))
msg=client_socket.recv(1024)
print(msg)
time.sleep(20)
reply="Hello Network World I am client 1"
client_socket.send(reply.encode())
msg=client_socket.recv(1024)
print(msg)
client_socket.close()
from socket import *
client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(("localhost",9030))
msg=client_socket.recv(1024)
print(msg)
reply="Hello Network World I am client 2"
client_socket.send(reply.encode())
msg=client_socket.recv(1024)
print(msg)
client_socket.close()