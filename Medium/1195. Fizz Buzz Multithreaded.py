from threading import Semaphore
from typing import Callable

# fizz(), buzz() and fizzbuzz() calculate total calls before hand,
# acquire their semaphore at each iteration and release the number semaphore after printing


class FizzBuzz:

    def __init__(self, n: int):
        self.n = n
        # semaphores for printing numbers, fizz and fizzbuzz
        self.numberSem = Semaphore(0)
        self.fizzSem = Semaphore(0)
        self.buzzSem = Semaphore(0)
        self.fizbuzzSem = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: Callable[[], None]) -> None:
        for _ in range((self.n // 3) - (self.n // 15)):
            self.fizzSem.acquire()
            printFizz()
            self.numberSem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: Callable[[], None]) -> None:
        for _ in range((self.n // 5) - (self.n // 15)):
            self.buzzSem.acquire()
            printBuzz()
            self.numberSem.release()

    # printFizzBuzz() outputs "fizzbuzz"

    def fizzbuzz(self, printFizzBuzz: Callable[[], None]) -> None:
        for _ in range(self.n // 15):
            self.fizbuzzSem.acquire()
            printFizzBuzz()
            self.numberSem.release()

    # printNumber(x) outputs "x", where x is an integer.

    def number(self, printNumber: Callable[[int], None]) -> None:
        # iterate through numbers from 1 to (including) self.n
        for i in range(1, self.n + 1):
            # perform action depending on divisibility of i
            # do NOT: aquire semaphore at each iteration and release in else, rundundant semaphore access
            if i % 15 == 0:
                self.fizbuzzSem.release()
                self.numberSem.acquire()
            elif i % 5 == 0:
                self.buzzSem.release()
                self.numberSem.acquire()
            elif i % 3 == 0:
                self.fizzSem.release()
                self.numberSem.acquire()
            else:
                printNumber(i)
