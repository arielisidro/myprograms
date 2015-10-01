__author__ = 'ariel'

#!/usr/bin/python3

import threading
import time
import numpy


class Parameters():

    def __init__(self, size):

        self.row_col = {}

        #direction 1- row ,1- column
        for i in range(1, 2):
            for j in range(size+1):
                self.row_col[(i, j)] = False


class Validate(threading.Thread):

    def __init__(self,  parameters, direction, numbers):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.direction = direction
        self.parameters = parameters

    def run(self):
        # Get lock to synchronize threads

        s = 0
        for k in self.numbers:
            threadLock.acquire()
            s += k
            threadLock.release()
            print("Thread sum ", s)

            time.sleep(2)

        # Free lock to release next thread
        self.parameters.set_sum(s)
        self.parameters.set_ave(s/self.numbers.__len__())


def print_stat(parameters):
    pass


def main():
    parameters = Parameters()
    parameters2 = Parameters()

    sudoku = numpy.array([
                [6, 2, 4, 5, 3, 9, 1, 8, 7],
                [5, 1, 9, 7, 2, 8, 6, 3, 4],
                [8, 3, 7, 6, 1, 4, 2, 9, 5],
                [1, 4, 3, 8, 6, 5, 7, 2, 9],
                [9, 5, 8, 2, 4, 7, 3, 6, 1],
                [7, 6, 2, 3, 9, 1, 4, 5, 8],
                [3, 7, 1, 9, 5, 6, 8, 4, 2],
                [4, 9, 6, 1, 8, 2, 5, 7, 3],
                [2, 8, 5, 4, 7, 3, 9, 1, 6]])


    # Create new threads
    ta = Average(numbers,parameters)
    tb = Average(numbers2,parameters2)
    tm = Minimum(numbers,parameters)
    tx = Maximum(numbers,parameters)

    # Start new Threads
    ta.start()
    tx.start()
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
