from multiprocessing import Process
import os, time, random


def task():
    while True:
        time.sleep(1)
        print('%s is running' %os.getpid())
        time.sleep(2)
        print('%s is done' %os.getpid())
        # 守护进程内无法再开启子进程,否则抛出异常
        # p = Process(target=time.sleep, args=(3,))
        # p.start()


if __name__ == '__main__':
    p = Process(target=task)
    p.daemon = True
    p.start()
    # p.join()
    print('主')
    time.sleep(100)
