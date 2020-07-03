import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(0.1)
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                cls._instance = object.__new__(cls)
                return cls._instance
        else:
            return cls._instance


class A(Singleton):
    pass


def task(arg):
    obj = A()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
