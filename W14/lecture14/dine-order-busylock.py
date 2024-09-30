# Version 2: With locks but starving

from threading import *

import time

from random import random

from busylock import BusyLock

import sys
def safePrint(content):
    sys.stdout.write("{0}\n".format(content))
    sys.stdout.flush()
print = safePrint # override the default print

N = 5

# we have one fork on each of the position
forks = [1] * N
#Using our customized lock here!
forkLocks = [BusyLock() for _ in range(N)]

def tryReleaseLock(lock):
    try:
        lock.release()
    except ThreadError:
        pass # the monitor might detect a deadlock and release my lock.
             # double-release a lock will cause ThreadError

def pickupFork(philosopher, forkPosition):
    # print("Philosopher %u trying to acquire fork %u" % (philosopher, forkPosition))
    forkLocks[forkPosition].acquire()
    print("Philosopher %u acquired fork %u" % (philosopher, forkPosition))
    if(forks[forkPosition] == 1): # there is a fork
        time.sleep(random() * 0.5) # it takes some time to reach the fork and pick it up
        forks[forkPosition] -= 1
        return True
    print("Philosopher %u cannot acquire fork %u" % (philosopher, forkPosition))
    tryReleaseLock(forkLocks[forkPosition])
    return False

def putBackFork(forkPosition):
    forks[forkPosition] += 1
    #print("trying to release fork %u" % forkPosition)
    tryReleaseLock(forkLocks[forkPosition])

def tryEat(philosopher):
    starved = [False] # use a list to let sub-function visit this variable
    def starving():
        starved[0] = True
        print("Philosopher %u is starving!" % philosopher)
    starvingEvent = Timer(N * 0.5 + 1, starving) # make sure starving is after everyone attempts to eat.
    starvingEvent.start()
    firstFork = philosopher
    secondFork = (philosopher + 1) % N
    # ---------------- Difference ---------------
    if(firstFork > secondFork):
        firstFork, secondFork = secondFork, firstFork # always fetch the smallest first
    # -------------------------------------------
    if(pickupFork(philosopher, firstFork)):
        if(not starved[0] and pickupFork(philosopher, secondFork)):
            if(not starved[0]): # starvation could happen after picking up second fork.
                starvingEvent.cancel()
                print("Philosopher %u enjoys the food with forks %u and %u" % (
                    philosopher, firstFork, secondFork))
            putBackFork(secondFork)
            putBackFork(firstFork)
        else:
            putBackFork(firstFork)

start = time.time()    
day = 1
def func(philosopher):
    local = 0
    while(time.time() - start < (N * 0.5 + 8) * 10): # demonstrate for 30 rounds
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

# Clean the forks from time to time
while(time.time() - start < (N * 0.5 + 8) * 10): # demonstrate for 10 rounds
    time.sleep(N * 0.5 + 2) # people are eating
    #print("------ Break any deadlock")
    for forkPosition in range(N):
        if forks[forkPosition] < 0:
            print("Two philosophers are trying to eat with the same fork %u (yuck)!" % forkPosition)
        if forks[forkPosition] != 1: # relieve the philosophers from dead locks
            tryReleaseLock(forkLocks[forkPosition])
    time.sleep(6)
    forks = [1] * N # Put the forks back        
    print("\n====== Now a new day\n")
    day += 1
