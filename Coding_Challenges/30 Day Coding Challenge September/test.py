# import numpy as np
# import heapq
# from bisect import insort
# from collections import Counter, defaultdict
# from typing import List
import timeit
import random
# import string


def t1():
    def innert1(_nums):
        for i, presence in enumerate(_nums[1:], start=1):
            pass


def t2():
    def innert1(_nums):
        _nums[0] = -1
        for i, presence in enumerate(_nums):
            pass


def genLists(rseed):
    return [1 for i in range(10000)]


functionArgs = [0]*500
for i in range(500):
    functionArgs[i] = genLists(i)

RUNS = 10000

x = timeit.timeit(t1, number=RUNS)
print(x)
x = timeit.timeit(t2, number=RUNS)
print(x)

#
#
#
# def genLists(rseed):
#     random.seed(rseed*55)
#     trips = []
#     for start in range(1000):
#         passengers = random.randint(1, 100)
#         stop = max(start + random.randint(1, 100), 1000)
#         trips.append((passengers, start, start))
#     random.shuffle(trips)
#     return random.randint(1, 10000), trips

#
#
# def genLists(rseed):
#     random.seed(rseed)
#     llength = 1000
#     rrange = (1, 10)
#     return [random.randint(*rrange) for i in range(llength)], [random.randint(*rrange) for i in range(llength)]
