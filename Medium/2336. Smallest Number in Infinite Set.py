import heapq


class SmallestInfiniteSet:
    """
    You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

    Implement the SmallestInfiniteSet class:
        SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain
          all positive integers.
        int popSmallest() Removes and returns the smallest integer contained in
          the infinite set.
        void addBack(int num) Adds a positive integer num back into the infinite
          set, if it is not already in the infinite set.

    Constraints:
        1 <= num <= 1000
        At most 1000 calls will be made in total to popSmallest and addBack.
    """

    def __init__(self):
        """
        Separately store smallest added back numbers and smallest unadded number
        denote n as the amount of added back numbers than have previously been popped.
        Space complexity of data structure: O(n)
        Time complexity of init: O(1)
        """
        self.inf_smallest = 1
        self.queue = []
        self.queue_set = set()

    def popSmallest(self) -> int:
        """O(log(n)) time complexity"""
        # check first if number in queue
        if self.queue:
            res = heapq.heappop(self.queue)
            self.queue_set.remove(res)
            return res

        # else return smallest not popped so far
        res = self.inf_smallest
        self.inf_smallest += 1
        return res

    def addBack(self, num: int) -> None:
        """O(log(n)) time complexity"""
        # only add if not in set, that means not in queue
        # and not smaller than smallest popped so far
        if num not in self.queue_set and num < self.inf_smallest:
            heapq.heappush(self.queue, num)
            self.queue_set.add(num)
