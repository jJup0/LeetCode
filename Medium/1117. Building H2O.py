from multiprocessing import Semaphore
from typing import Callable


class H2O:
    def __init__(self):
        # set hydrogen semaphore to 0
        self.hSem = Semaphore(0)
        # set oxygen semaphore to 2, required to call oxygen once
        self.oSem = Semaphore(2)
        # using a mutual exclusion semaphore so that oxygen can acquire two counts of oSem
        self.mutex = Semaphore(1)

    # releaseHydrogen() outputs "H"

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        # calling hyrogen aquires one hydrogen semaphore, and releases one oxygen semaphore
        self.hSem.acquire()
        releaseHydrogen()
        self.oSem.release()

    # releaseOxygen() outputs "O"

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        # calling oxygen requires two hydrogen semaphores, as the oxygen to hydrogen ratio is 1:2
        # acquire and release mutual exclusion semaphore
        with self.mutex:
            self.oSem.acquire()
            self.oSem.acquire()
        releaseOxygen()
        # release two hydrogen semaphores, (release(n) in python 3.9)
        self.hSem.release()
        self.hSem.release()
