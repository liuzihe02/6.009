import time
import threading
from collections import defaultdict

SLEEP_INTERVAL = 0.001

class BusyLock:
    counter = 0
    id = 0
    # single dict instructions in python are atomic by GIL
    def __init__(self):
        self.id = BusyLock.counter
        BusyLock.counter += 1 # static counter to get N
        self.level = defaultdict(lambda _: -1)
        self.lastToEnter = defaultdict(lambda _: -1)

    # assumption 1: locks are initialized before the first lock acquisition
    # assumption 2: the number of locks equals the number of worker threads
    def acquire(self):
        thread_id = threading.get_ident()
        for t in range(BusyLock.counter):
            self.level[thread_id] = t
            self.lastToEnter[t] = thread_id
            while self.lastToEnter[t] == thread_id:
                found = False
                for k in self.level.keys():
                    if k != thread_id and self.level[k] >= t:
                        found = True
                        break
                if found:
                    #Another thread is ahead --> go to sleep and try again after waking
                    time.sleep(SLEEP_INTERVAL)
                else:
                    break

    def release(self):
        # print("Lock %d is released." % self.id)
        # reset the level state
        self.level = defaultdict(lambda _: -1)
