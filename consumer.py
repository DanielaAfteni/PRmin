from calendar import c
import json
import threading
import time
from producer import *
from flask import Flask, request
import logging
log = logging.getLogger('dana')
log.setLevel(logging.ERROR)

server3 = Flask(__name__)

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

embassy = ThreadSafeList()

# my url
# get data
@server3.route('/consumer', methods=['POST'])
def consumer():
    embassy.append(json.loads(request.data))
    return ""
        

class EmbassyStaff(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        while True:
            try:
                received_citizenship = embassy.pop()["data"]
                received_citizenship[0] = rcitiz
                received_citizenship[1] = srequest
                received_citizenship[2] = toath
                requests.post(url='http://localhost:5002/aggregator2', json={"data" : received_citizenship})
                print(f'At thread: {self.thread_name} sent wanted {received_citizenship[0]}, {received_citizenship[1]}, {received_citizenship[2]} NUMBER {received_citizenship[3]}')
            except IndexError:
                print("embassy is still empty.")
            time.sleep(2)
        
if __name__ == '__main__':
    threading.Thread(target=lambda: server3.run(port=5003, host="0.0.0.0", debug=False)).start()
    for index in range(1, 6):
        x = EmbassyStaff(thread_name=f'EmbassyStaff_Nr_{index}')
        x.start() 

