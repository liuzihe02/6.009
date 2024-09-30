# Version 1: No locks

from threading import *

import time

from random import random

import sys
def safePrint(content):
    sys.stdout.write("{0}\n".format(content))
    sys.stdout.flush()
print = safePrint # override the default print

N = 5

# we have one fork on each of the position
forks = [1] * N

def pickupFork(philosopher, forkPosition):
    if(forks[forkPosition] == 1): # there is a fork
        time.sleep(random() * 0.5) # it takes some time to reach the fork and pick it up
        forks[forkPosition] -= 1
        return True
    print("Philosopher %u cannot acquire fork %u" % (philosopher, forkPosition))
    return False

def tryEat(philosopher):
    firstFork = philosopher
    secondFork = (philosopher + 1) % N
    if(pickupFork(philosopher, firstFork)):
        if(pickupFork(philosopher, secondFork)):
            print('Philosopher %u enjoys the food with forks %u and %u' % (
                philosopher, firstFork, secondFork))
            time.sleep(5) # a long time
            forks[secondFork] += 1
            forks[firstFork] += 1
        else:
            forks[firstFork] += 1 # return the left fork back

start = time.time()    
day = 1
def func(philosopher):
    local = 0
    while(time.time() - start < (N * 0.5 + 9) * 10): # demonstrate for 10 rounds
        if(day > local):
            local = day
            tryEat(philosopher)
        else:
            time.sleep(0.1) # not dinner time

threadPool = []

for ind in range(N):
    threadPool.append(Thread(target=func, args=(ind,)))

for ind in range(N):
    threadPool[ind].start()

# Original thread: Clean the forks from time to time
while(time.time() - start < (N * 0.5 + 9) * 10): # demonstrate for 10 rounds
    time.sleep(N * 0.5 + 2) # people are eating
    for forkPosition in range(N):
        if forks[forkPosition] < 0:
            print("Two philosophers are trying to eat with the same fork %u (yuck)!" % forkPosition)
    time.sleep(5) # philosophers will put back forks
    print("\n====== Now a new day\n")
    time.sleep(2)
    day += 1
