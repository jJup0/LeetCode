import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # make a heap containing the k biggest items from nums,
        # self.heap[0] will contain the kth biggest item
        self.heap = nums[:k]
        heapq.heapify(self.heap)

        for val in nums[k:]:
            if val > self.heap[0]:
                heapq.heappushpop(self.heap, val)

        # len(nums) could be k - 1, so append -10001 in that case add -10001
        # (constraint -10000 <= nums[i], val <= 10000)
        # -10001 will be replaced by first add() call
        if len(nums) < k:
            heapq.heappush(self.heap, -10001)


    def add(self, val: int) -> int:
        # if val is bigger than the kth smallest, discard smallest and add val to heap
        if val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        # return smallest item from heap
        return self.heap[0]
