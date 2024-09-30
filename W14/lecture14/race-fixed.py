## Version 2

from threading import *

A = 0
B = 1000

import time
from random import random
def transfer(amt):
    global A, B
    newA = A + amt
    time.sleep(random())
    newB = B - amt
    A = newA
    B = newB
    toprint = "total = " + str(newA + newB) + " A = " + str(newA) + " B = " +str(newB)
    print(toprint)

lock = Lock()
def lockedtransfer(amt):
    lock.acquire()
    global A, B
    newA = A + amt
    time.sleep(random())
    newB = B - amt
    A = newA
    B = newB
    
    lock.release()

    toprint = "total = " + str(newA + newB) + " A = " + str(newA) + " B = " + str(newB)
    print(toprint)



start = time.time()    
def fun1():
    while time.time() - start < 30:
        lockedtransfer(int(100 * random() - 50))

x = Thread(target=fun1)
y = Thread(target=fun1)

x.start()
y.start()
