"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Constraints:
- 1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        # ways to climb stairs for current and previous stair count
        prev = 1  # 1 way to climb 0 stairs
        curr = 1  # 1 way to climb 1 stair
        for _ in range(2, n + 1):
            # you can either take one or two stairs, so sum up the
            # ways of getting to the past two stairs
            new_ways = prev + curr
            # update prev and curr
            prev = curr
            curr = new_ways
        return curr
