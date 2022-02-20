import timeit
import random


def t1():
    def loop(n):
        if a[-1] > 500 and a[-1] > 1:
            pass

    for i in range(10000):
        loop(i)


def t2():
    def loop(n):
        if (last := a[-1]) > 500 and last > 1:
            pass

    for i in range(10000):
        loop(i)


a = [random.randint(1, 1000) for i in range(1000)]
TESTNR = 500
x = timeit.timeit(t1, number=TESTNR)
print(x)
x = timeit.timeit(t2, number=TESTNR)
print(x)
