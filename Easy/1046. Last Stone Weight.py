import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap for the stones, possible by negating values
        # and creating a min heap from these values
        stones = list(-x for x in stones)
        heapq.heapify(stones)

        # play the game until only one or no stones are left
        while len(stones) > 1:
            # get the two biggest rocks, no need to negate them, as only their difference is relevant
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            # result of smashing the rocks, result is non-positive as x, y < 0 and x < y
            result = x - y

            # if not 0, push the result onto the heap
            if result:
                heapq.heappush(stones, result)

        # if there is a stone left return its weight (negated from heap), otherwise return 0
        return -stones[0] if stones else 0
