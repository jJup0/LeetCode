import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        c = Counter(nums)
        # O(n)
        heap = list((-count, val) for val, count in c.items())
        # O(n)
        heapq.heapify(heap)
        # O(k * log(n))
        res = heapq.nsmallest(k, heap)
        # O(k)
        return list(val for _, val in res)
