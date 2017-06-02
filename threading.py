#coding=utf-8
import threading
from time import ctime,sleep
def A():
    for i in range(3):
        print i
        print 'A',ctime()
        sleep(2)

def B():
    for i in range(3):
        print 11
        print 'B', ctime()
        sleep(3)

threads = []
t1 = threading.Thread(target=A)
threads.append(t1)
t2 = threading.Thread(target=B)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
