from threading import Semaphore
from typing import Callable


class Foo:
    def __init__(self):
        # initliaze both semaphores for printing first and second to 0
        self.semSecond = Semaphore(0)
        self.semThird = Semaphore(0)

    # print first and then release semaphore to print second
    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.semSecond.release()

    # acquire semaphore to print second, and then release third
    def second(self, printSecond: Callable[[], None]) -> None:
        self.semSecond.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.semThird.release()

    # acquire sem thrid and print third
    def third(self, printThird: Callable[[], None]) -> None:
        self.semThird.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
