__author__ = 'ariel'

#!/usr/bin/python3

import threading
import time


class Sum():

    def __init__(self):
        self.value=0

    def set_value(self,value):
        self.value=value


class Summation (threading.Thread):

    def __init__(self, arg, sum_numbers):
        threading.Thread.__init__(self)
        self.arg = arg
        self.sum_numbers = sum_numbers

    def run(self):
        # Get lock to synchronize threads
        threadLock.acquire()
        s = 0
        for k in range(1, self.arg):
            print("k: %d %d" % (k, self.arg))
            s += 1
            print_sum(s)

        # Free lock to release next thread
        self.sum_numbers.set_value(s)
        threadLock.release()

        return


def print_sum(s):
    print("Sum: %d " % s)


def main():
    sum_numbers = Sum()
    argv = 5

    # Create new threads
    t = Summation(argv,sum_numbers)

    # Start new Threads
    t.start()

    # Add threads to thread list
    t.join()

    print ("Exiting Main Thread")
    print_sum(sum_numbers.value)

if __name__ == "__main__":
    threadLock = threading.Lock()

    main()
