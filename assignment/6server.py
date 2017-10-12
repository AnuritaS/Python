#!/usr/bin/python
import threading
from socket import *
server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind(("localhost",9030))
server_socket.listen(5)
print ("Server Started")
print ("Waiting for clients")
def ClientServer(*tup):
    welcome_msg="Welcome client"
    conn=tup[0]
    conn.send(welcome_msg.encode())
    receive_msg=conn.recv(1024)
    print(receive_msg)
    conn.close()
while True:
    tup_client=server_socket.accept()
    thread=threading.Thread(target=ClientServer,args=tup_client)
    thread.start()
