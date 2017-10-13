'''
Get a list of URLs from user. , Connect to the URL of a website, and print out the first 1024 bytes of the page. Use threads for each url connection.
'''
import threading
import urllib.request
import ssl
context = ssl._create_unverified_context()

urls = [x for x in input("Enter urls:").split()]

def fetch_url(url):
    web_file = urllib.request.urlopen(url,context=context)
    data = web_file.read()

    print(data[0:1024])

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
