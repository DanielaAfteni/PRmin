import json
import threading
import time
from producer import *
from consumer import *
from flask import Flask, request
import logging
log = logging.getLogger('dana')
log.setLevel(logging.ERROR)


server2 = Flask(__name__)

class ThreadSafeList():
    def __init__(self):
        self._list = list()
        self._lock = threading.Lock()

    def append(self, value):
        with self._lock:
            self._list.append(value)

    def pop(self):
        with self._lock:
            return self._list.pop()

gov_website = ThreadSafeList()

# my url
# get data
@server2.route('/aggregator', methods=['POST'])
def aggregator():
    gov_website.append(json.loads(request.data))
    return ""
    
@server2.route('/aggregator2', methods=['POST'])
def answer():
    gov_website.append(json.loads(request.data))
    received_citizenship = gov_website.pop()["data"]
    print(f'Citizenship certificate received from CONSUMER {received_citizenship[0]}, {received_citizenship[1]}, {received_citizenship[2]} NUMBER {received_citizenship[3]}')
    if received_citizenship[2] == toath:
        requests.post(url='http://localhost:5001/producer', json={"data" : received_citizenship})
        print(f'Citizenship certificate sent to PRODUCER {received_citizenship[0]}, {received_citizenship[1]}, {received_citizenship[2]} NUMBER {received_citizenship[3]}')
    return "Citizenship is sent to PRODUCER"
            



class Admin(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        while True:
            try:
                received_citizenship = gov_website.pop()["data"]
                received_citizenship[0] = rcitiz
                received_citizenship[1] = srequest
                received_citizenship[2] = untoath
                requests.post(url='http://localhost:5003/consumer', json={"data" : received_citizenship})
                print(f'At thread: {self.thread_name} sent wanted {received_citizenship[0]}, {received_citizenship[1]}, {received_citizenship[2]} NUMBER {received_citizenship[3]}')
            except IndexError:
                print("Gov website is still empty.")
            time.sleep(2)

if __name__ == '__main__':
    threading.Thread(target=lambda: server2.run(port=5002, host="0.0.0.0", debug=False)).start()
    for index in range(1, 6):
        x = Admin(thread_name=f'Admin_Nr_{index}')
        x.start() 
