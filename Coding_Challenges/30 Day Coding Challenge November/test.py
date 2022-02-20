from typing import List
import timeit
import random


def t1():
    num = 0
    for c in testStr:
        num = num*10 + int(c)


def t2():
    num = ""
    for c in testStr:
        num += c
    num = int(num)


def t3():
    for c in testStr:
        pass


testStr = ""
for i in range(5):
    testStr += str(random.randint(1, 9))

x = timeit.timeit(t1, number=100000)
print(x)
x = timeit.timeit(t2, number=100000)
print(x)
x = timeit.timeit(t3, number=100000)
print(x)
