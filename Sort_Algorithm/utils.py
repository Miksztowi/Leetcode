# -*- encoding:utf-8 -*-
# __author__=='Gan'

import random
import time

from functools import wraps


def generate_array(length=10, start=0, end=100):
    return [random.randint(start, end) for _ in range(length)]


def decorator_timer(func):
    start = time.time()

    @wraps(func)
    def timer(*args):
        print('Begin:', args[0])
        result = func(args[0])
        print('After:', result)
        print('This sort algorithm has cost {}s'.format(time.time() - start))
        return result

    return timer



