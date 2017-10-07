'''5.	Write a Python program to determine in a local network which addresses/computers are active.Get a list of ip addresses from the user(each ip address entered as a string). Every time we would have to wait a few seconds for the return values. A solution without threads is highly inefficient, because the script will have to wait for every ping.'''
from threading import Thread
import subprocess
from queue import Queue

ips = list(x for x in input("Enter ip addresses: ").split())

num_threads = 4
queue = Queue()

#wraps system ping command
def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print("Thread %s: Pinging %s" % (i, ip))
        ret = subprocess.call("ping -c 1 %s" % ip,
            shell=True,
            stdout=open('/dev/null', 'w'),
            stderr=subprocess.STDOUT)
        if ret == 0:
            print("%s: is active" % ip)
        else:
            print("%s: is not active" % ip)
        q.task_done()
#Spawn thread pool
for i in range(num_threads):

    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
#Place work in queue
for ip in ips:
    queue.put(ip)
#Wait until worker threads are done to exit
queue.join()
