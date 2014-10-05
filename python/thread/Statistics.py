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

        s = 0
        threadLock.acquire()
        for k in self.numbers:
            s += k
            print("Thread sum ", s)

            time.sleep(2)

        threadLock.release()
        # Free lock to release next thread
        self.parameters.set_sum(s)
        self.parameters.set_ave(s/self.numbers.__len__())


class Minimum(threading.Thread):

    def __init__(self, numbers, parameters):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.parameters = parameters

    def run(self):
        # Get lock to synchronize threads

        m = self.numbers[0]
        k=1
        l = self.numbers.__len__()
        threadLock.acquire()
        while k < l:
            if m > self.numbers[k]:
                m = self.numbers[k]
            k += 1
            print("Thread Min ", m)
            time.sleep(1)

        threadLock.release()
        # Free lock to release next thread
        self.parameters.set_min(m)


class Maximum(threading.Thread):

    def __init__(self, numbers, parameters):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.parameters = parameters

    def run(self):
        # Get lock to synchronize threads
        m = self.numbers[0]
        k=1
        l = self.numbers.__len__()
        threadLock.acquire()
        while k < l:

            if m < self.numbers[k]:
                m = self.numbers[k]
            k += 1

            print("Thread Max ", m)

            time.sleep(3)

        threadLock.release()
        # Free lock to release next thread
        self.parameters.set_max(m)


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
    #tb = Average(numbers2,parameters2)
    tm = Minimum(numbers,parameters)
    tx = Maximum(numbers,parameters)

    # Start new Threads
    ta.start()
    tx.start()
    #tb.start()
    tm.start()

    # Add threads to thread list
    tx.join()
    ta.join()
    #tb.join()
    tm.join()

    print ("Exiting Main Thread")
    print_stat(parameters)
    print_stat(parameters2)

if __name__ == "__main__":

    threadLock = threading.Lock()

    main()
