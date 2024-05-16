import threading
import time


class Singleton(object):
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._lock:
                cls._instance = object.__new__(cls)
        return cls._instance


class Cat(Singleton):

    def name(self):
        time.sleep(1)
        print(self)


if __name__ == "__main__":
    for i in range(6):
        cat = Cat()
        t = threading.Thread(target=cat.name, args=())
        t.setDaemon(True)
        t.start()
        print("stop")
    time.sleep(2)

