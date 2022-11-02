import threading
# requests are just for post (requests.post)
import requests
import time
import random
from flask import Flask, request
import logging
log = logging.getLogger('dana')
log.setLevel(logging.ERROR)

# (depusa cerera)
srequest = "submitted request"
# (Nu e depusa cerera)
unsrequest = "unsubmitted request"
# (Nu e depunerea juramantului)
untoath = "not taking the oath"
# (depunerea juramantului)
toath = "taking the oath"
rcitiz = "Romanian citizenship"

server1 = Flask(__name__)

# my url
@server1.route('/producer', methods = ['POST'])
def producer():
    return "Success"
    

class Citizen(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.thread_name = thread_name

    def run(self):
        while True:
            citizenship = list([rcitiz, unsrequest, untoath, str(random.randint(100, 999))])
            try:
                requests.post(url='http://localhost:5002/aggregator', json={"data" : citizenship})
                print(f'At thread: {self.thread_name} sent wanted {citizenship[0]}, {citizenship[1]}, {citizenship[2]} NUMBER {citizenship[3]}')
            except requests.exceptions.ConnectionError:
                print("Gov website server is not working.")

            time.sleep(2)

if __name__ == '__main__':
    threading.Thread(target=lambda: server1.run(port=5001, host="0.0.0.0", debug=False)).start()

    for index in range(1, 6):
        x = Citizen(thread_name=f'Citizen_Nr_{index}')
        x.run()