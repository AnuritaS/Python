#!/usr/bin/python
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