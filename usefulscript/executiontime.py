"""
ExecutionTime
This class is used for timing execution of code.
For example:
    timer = ExecutionTime()
    print 'Hello world!'
    print 'Finished in {} seconds.'.format(timer.duration())
"""


import time
import random


class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time


# ---- run code ---- #


timer = ExecutionTime()
sample_list = list()
my_list = [random.randint(1, 10) for num in
           range(1, 100) if num % 2 == 0]
print my_list
print('Finished in {} seconds.'.format(timer.duration()))
