from queue import Queue
from threading import Thread


def producer(que):
    data = 0
    while True:
        data += 1
        que.put(data)


def consumer(que):
    while True:
        data = que.get()
        print(data)


que = Queue()
t1 = Thread(target=consumer, args=(que,))
t2 = Thread(target=producer, args=(que,))
# t1.setDaemon(True)
# t2.setDaemon(True)
t1.start()
t2.start()
