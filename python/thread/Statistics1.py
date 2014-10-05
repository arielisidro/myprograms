__author__ = 'ariel'

#!/usr/bin/python3

import threading
import time


class Parameters():

    def __init__(self):
        self.sum=0
        self.ave=0
        self.min=0
        self.max=0

    def set_sum(self, sum):
        self.sum = sum

    def set_ave(self, ave):
        self.ave = ave

    def set_min(self, min):
        self.min = min

    def set_max(self, max):
        self.max = max

    def get_sum(self):
        return self.sum

    def get_ave(self):
        return self.ave

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max


class Average(threading.Thread):

    def __init__(self, numbers, parameters):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.parameters = parameters

    def run(self):
        # Get lock to synchronize threads
        #threadLock.acquire()

        s = compute_sum(self.numbers)

        # Free lock to release next thread
        self.parameters.set_sum(s)
        self.parameters.set_ave(s/self.numbers.__len__())

        #threadLock.release()


def compute_sum(numbers):

    s = 0
    for k in numbers:
        s += k
        print("Thread sum ", s)
        time.sleep(5)
    return s

class Minimum(threading.Thread):

    def __init__(self, numbers, parameters):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.parameters = parameters

    def run(self):
        # Get lock to synchronize threads
        #threadLock.acquire()
        m = compute_min(self.numbers)
        # Free lock to release next thread
        self.parameters.set_min(m)

        #threadLock.release()

def compute_min(numbers):

    m = numbers[0]
    k=1
    l = numbers.__len__()
    while k < l:
        if m > numbers[k]:
            m = numbers[k]
        k += 1
        print("Thread Min ", m)
        time.sleep(5)

    return m


class Maximum(threading.Thread):

    def __init__(self, numbers, parameters):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.parameters = parameters

    def run(self):
        # Get lock to synchronize threads
        #threadLock.acquire()
        m = compute_max(self.numbers)

        # Free lock to release next thread
        self.parameters.set_max(m)

        #threadLock.release()


def compute_max(numbers):

    m = numbers[0]
    k=1
    l = numbers.__len__()
    while k < l:
        if m < numbers[k]:
            m = numbers[k]
        k += 1

        print("Thread Max ", m)

        time.sleep(2)

    return m


def print_stat(parameters):
    print("Sum:  ", parameters.get_sum())
    print("Ave:  ", parameters.get_ave())
    print("Min:  ", parameters.get_min())
    print("Max:  ", parameters.get_max())


def main():
    parameters = Parameters()
    parameters2 = Parameters()
    numbers=[32, 12, 23, 34, 99, 14, 90, 1, 23, 56, 65, 45, 23, 77, 89, 23, 11, 61]
    numbers2=[32, 12, 23, 34, 99, 14, 90, 1, 23, 56, 65, 45, 23, 77, 89, 23, 11, 61, 100]
    #for k in range(0,100):
    #    numbers.append(k)

    # Create new threads
    ta = Average(numbers,parameters)
    tb = Average(numbers2,parameters2)
    tm = Minimum(numbers,parameters)
    tx = Maximum(numbers,parameters)

    # Start new Threads
    tx.start()
    ta.start()
    tb.start()
    tm.start()

    # Add threads to thread list
    tx.join()
    ta.join()
    tb.join()
    tm.join()

    print ("Exiting Main Thread")
    print_stat(parameters)
    print_stat(parameters2)

if __name__ == "__main__":

    threadLock = threading.Lock()

    main()
