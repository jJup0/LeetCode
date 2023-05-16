import heapq


class Solution:
    """
    You are given an array of integers stones where stones[i] is the weight of the
    ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two
    stones and smash them together. Suppose the heaviest two stones have weights
    x and y with x <= y. The result of this smash is:
        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y
          has new weight y - x.

    At the end of the game, there is at most one stone left.

    Return the weight of the last remaining stone. If there are no stones left, return 0.

    Constraints:
        1 <= stones.length <= 30
        1 <= stones[i] <= 1000
    """

    def lastStoneWeight(self, stones: list[int]) -> int:
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
