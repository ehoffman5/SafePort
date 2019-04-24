import socket
import time
import threading
from multiprocessing import JoinableQueue
import sys

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

# This sets the IP that we are scanning to the IP of the device running this code
target = '127.0.0.1'
# This saves the start time to calculate the speed of tests later on
start = time.time()
# This creates a queue for the Smart Scan feature I want to implement
userQ = JoinableQueue()
# This makes a list for which we are going to use to keep track of the open ports
openPorts = []

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # This sends the connection request to each port in the queue
    try:
        connection = s.connect((target, port))
        with lock:
            # print1 = 'Port', port, 'is open!'
            # print(print1)
            openPorts.append(port)
        connection.close()
    except:
        pass
    # Notifies the user that the scan is over
    if port == 54870:
        time.sleep(0.5)
        # print('Done!')
        message = '<h4>Open ports on your device:</h4><br/>'
        results = ', '.join(str(x) for x in openPorts)
        print (message + results + '<br/><br/><br/><i class="fas fa-search fa-md"></i>&nbsp; Scan Type: <i>Smart Scan</i>')
        return results


def thread():
    while True:
        worker = userQ.get()
        portscan(worker)
        userQ.task_done()

# This sets how many threads you want to run and starts them
for x in range(100):
    t = threading.Thread(target = thread)
    t.daemon = True
    t.start()

smartList = [0, 21, 22, 23, 25, 53, 79, 80, 110, 113, 119, 135, 137, 138, 139, 143, 389, 443, 445, 555, 631, 666, 902, 912, 1001, 1002, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1243, 1433, 1434, 1720, 1900, 2000, 4380, 4381, 5000, 5040, 5088, 5354, 5432, 6463, 6667, 6670, 6711, 6776, 6969, 7000, 7680, 8080, 8733, 12345, 12346, 13148, 15292, 15393, 21554, 22222, 27015, 27017, 27275 , 27374, 29559, 31337, 31338, 49664, 49665, 49666, 49668, 49684, 49731, 49765, 49774, 50698, 50760, 51229, 54860, 54870, 57621]

for worker in smartList:
    userQ.put(worker)

userQ.join()
