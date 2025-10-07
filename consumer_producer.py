#consumer_producer

from threading import Lock
from threading import Thread
import random
import time
import sys
from collections import deque
work = deque()                       # shared data structure ===
lock = Lock()                   # create lock =============
count=[0]
class ProducerThread(Thread):
    def run(self):
        while True:
            num = random.randint(1,10)
            lock.acquire()      # acquire it ==============
            work.append(num)
            count[0] = count[0] + 1
            print('Produced ',num,
                  'work is ',work, 'count',count)
            lock.release()      # release it ==============
            time.sleep(random.random()%2)

class ConsumerThread(Thread):
    def run(self):
        while True:
            lock.acquire()      # acquire it ==============
            if count[0] > 0:
                num = work.popleft()
                count[0] -= 1
                print('Consumed ',num,
                      'work is ',work,'count',count)
                lock.release()      # release it =============
            time.sleep(random.random())

producer = Thread(None,target=ProducerThread.run, args=("Producer",))
consuer = Thread(None,target=ConsumerThread.run, args=("Producer",))
producer.start()
consuer.start()
time.sleep(30)
sys.exit()
