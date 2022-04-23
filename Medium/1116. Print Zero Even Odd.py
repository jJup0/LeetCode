
from multiprocessing import Semaphore
from typing import Callable


# printNumber(x) outputs "x", where x is an integer.
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.curr = 1
        self.zeroSem = Semaphore(1)
        self.evenSem = Semaphore(0)
        self.oddSem = Semaphore(0)

    def zero(self, printNumber: Callable[[int], None]) -> None:
        while self.curr < self.n:
            self.zeroSem.acquire()
            printNumber(0)
            if self.curr % 2:
                self.oddSem.release()
            else:
                self.evenSem.release()

        if self.n == 1:
            self.zeroSem.acquire()
            printNumber(0)
            self.oddSem.release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        while self.curr < self.n:
            self.evenSem.acquire()
            printNumber(self.curr)
            self.curr += 1
            self.zeroSem.release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        while self.curr < self.n:
            self.oddSem.acquire()
            printNumber(self.curr)
            self.curr += 1
            self.zeroSem.release()

        if self.n == 1:
            self.oddSem.acquire()
            printNumber(1)
