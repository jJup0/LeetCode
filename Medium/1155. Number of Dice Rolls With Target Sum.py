import numpy as np


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.numRollsToTarget_optimized(n, k, target)

    def numRollsToTarget_optimized(self, n: int, k: int, target: int) -> int:
        """
        O(n * target) / O(t)    time / space complexity
        """
        if n * k < target or target < n:
            return 0

        MOD = 10**9 + 7

        # dp[j] = numRollsToTarget(i, k, target)
        dp = np.zeros((target + 1,), dtype=int)

        # initialize dp with for a single dice throw
        to_fill = min(k, target)
        dp[1:to_fill + 1] = np.ones((to_fill,), dtype=int)

        # iterate through dice throw counts
        for i in range(2, n + 1):
            # create temporary array to fill next dp
            dp_next = np.zeros((target + 1,), dtype=int)

            # current sum of possible ways to to still reach target t: sum(dp[i-1][max(0, t-k):t])
            curr_sum = 0

            # iterate through targets updating dp_next, can also be in range(1, target+1)
            for t in range(i, min(i * k, target) + 1):
                # update current sum adding value from dp[t-1], since a 1 can be rolled
                curr_sum = (curr_sum + dp[t-1]) % MOD
                dp_next[t] = curr_sum
                # remove no longer reachable target from curr_sum (can not roll higher than k)
                curr_sum -= dp[max(0, t-k)]

            dp = dp_next

        return dp[target]

    def numRollsToTarget_original(self, n: int, k: int, target: int) -> int:
        """
        Lazy version with trivial dp, and recalculating sums
        O(n * target * k) / O(n * t)    time / space complexity
        """
        if n * k < target or target < n:
            return 0

        MOD = 10**9 + 7

        # dp[i][j] = numRollsToTarget(i, k, target)
        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # initialize dp with single dice throws
        dp[1][1:k + 1] = [1] * k

        for i in range(2, n + 1):
            for t in range(1, target + 1):
                # ways to get a total of t with i throws is all ways to get total of
                # t-k, t-k+1 ... t-1 with i-1 throws
                dp[i][t] = sum(dp[i-1][max(0, t-k):t]) % MOD

        return dp[-1][-1]
