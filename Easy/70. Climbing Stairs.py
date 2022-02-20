class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 1
        for _ in range(2, n+1):
            prev, curr = curr, prev + curr
        return curr
