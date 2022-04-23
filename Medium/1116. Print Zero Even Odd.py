from multiprocessing import Semaphore
from typing import Callable


# printNumber(x) outputs "x", where x is an integer.
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        # semaphores for printing 1, even and odd, initialize zeroSem with 1 as 0 needs to print first
        self.zeroSem = Semaphore(1)
        self.evenSem = Semaphore(0)
        self.oddSem = Semaphore(0)

    def zero(self, printNumber: Callable[[int], None]) -> None:
        # 0 needs to be printed n times
        # i is next value to print, determines which semaphore to release
        for i in range(1, self.n + 1, + 1):
            # acquire zeroSem, print, release depending on i
            self.zeroSem.acquire()
            printNumber(0)
            if i % 2:
                self.oddSem.release()
            else:
                self.evenSem.release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        # even numbers need print from 2 to (including) self.n
        for i in range(2, self.n + 1, 2):
            self.evenSem.acquire()
            printNumber(i)
            self.zeroSem.release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        # odd numbers need print from 1 to (including) self.n
        for i in range(1, self.n + 1, 2):
            self.oddSem.acquire()
            printNumber(i)
            self.zeroSem.release()
