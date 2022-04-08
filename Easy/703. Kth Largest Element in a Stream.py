import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # take the largest k values from nums
        self.nums = sorted(nums)[-k:]

        # len(nums) could be k - 1, so append -10001 in that case
        # (constraint -10000 <= nums[i], val <= 10000)
        # -10000 will be replaced with first add() call
        if len(self.nums) < k:
            self.nums.append(-10001)

        # self.nums will have exactly k items
        # turn self.nums into a heap, this way the smallest (first) item in self.nums
        # will actually be the kth biggest item from nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        # if val is bigger than the kth smallest, pop smallest and add val to heap
        if val > self.nums[0]:
            heapq.heappushpop(self.nums, val)

        # return smallest item from heap
        return self.nums[0]
