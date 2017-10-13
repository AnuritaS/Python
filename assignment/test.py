import threading,os
import time

def child(ip):
    p = " ping " + ip
    print(p)
    ping_out = os.popen(p)
    line = ping_out.read()
    print(line)

for i in range(0,3):
    n=input("Enter the ip address:")
    thread = threading.Thread(target=child, args=(n,))
    thread.start()
    print("pinging")

print("Main thread exiting")
