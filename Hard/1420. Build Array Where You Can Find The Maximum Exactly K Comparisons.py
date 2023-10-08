from functools import cache, reduce

MOD = 10**9 + 7


def sum_and_mod(x: int, y: int, /) -> int:
    return (x + y) % MOD


class Solution:
    """
    You are given three integers n, m and k. Consider the following algorithm to
    find the maximum element of an array of positive integers:

    https://assets.leetcode.com/uploads/2020/04/02/e.png

    You should build the array arr which has the following properties:
    - arr has exactly n integers.
    - 1 <= arr[i] <= m where (0 <= i < n).
    - After applying the mentioned algorithm to arr, the value search_cost is
      equal to k.

    Return the number of ways to build the array arr under the mentioned
    conditions. As the answer may grow large, the answer must be computed
    modulo 10^9 + 7.

    Constraints:
    - 1 <= n <= 50
    - 1 <= m <= 100
    - 0 <= k <= n
    """

    def numOfArrays_simple(self, n: int, m: int, k: int) -> int:
        """
        2500ms
        O(n * m^2 * k) / O(n * m * k)     time / space complexity
        """

        @cache
        def helper(_n: int, curr_max: int, cost: int) -> int:
            nonlocal m

            if _n == 1:
                # base case, array of length 1: 1 way to have cost of 1, else no ways
                return 1 if cost == 1 else 0

            # add smaller number to all variations of arrays of length-1
            smaller = reduce(
                sum_and_mod,
                (helper(_n - 1, curr_max, cost) for _ in range(1, curr_max + 1)),
                0,
            )
            # add largest number to all variations of arrays of length-1
            larger = reduce(
                sum_and_mod,
                (helper(_n - 1, j, cost - 1) for j in range(curr_max + 1, m + 1)),
                0,
            )
            # return sum of both ways
            return sum_and_mod(smaller, larger)

        if k == 0:
            # cost of 0 is impossible
            return 0
        # sum up results for all possible maximum values of arrays
        return reduce(
            sum_and_mod,
            (helper(n, j, k) for j in range(1, m + 1)),
        )

    def numOfArrays_fast(self, n: int, m: int, k: int) -> int:
        """I have not understood how this works, but it is a lot faster.
        79ms
        O(n * m * k) / O(m * k)     time / space complexity
        """
        if m < k:
            return 0

        dp = [[int(ki == 0)] * m for ki in range(k)]
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                acc = 0
                for j in range(m - 1, -1, -1):
                    dp[i][j] = (dp[i][j] * (j + 1) + acc) % MOD
                    if i > 0:
                        acc += dp[i - 1][j]
        return sum(dp[-1]) % MOD
