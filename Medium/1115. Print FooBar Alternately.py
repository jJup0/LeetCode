from threading import Semaphore
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        # use two semaphores, one to allow foo to print, one to allow bar to print
        self.fooSem = Semaphore(1)
        self.barSem = Semaphore(0)

    # foo waits for fooSem, and releases barSem after printing
    def foo(self, printFoo: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.fooSem.acquire()
            printFoo()  # printFoo() outputs "foo". Do not change or remove this line.
            self.barSem.release()

    # bar waits for barSem, and releases fooSem after printing
    def bar(self, printBar: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.barSem.acquire()
            printBar()  # printBar() outputs "bar". Do not change or remove this line.
            self.fooSem.release()
