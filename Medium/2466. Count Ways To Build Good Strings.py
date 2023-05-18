class Solution:
    """
    Given the integers zero, one, low, and high, we can construct a string by starting
    with an empty string, and then at each step perform either of the following:
        Append the character '0' zero times.
        Append the character '1' one times.
        This can be performed any number of times.

    A good string is a string constructed by the above process having a length
    between low and high (inclusive).

    Return the number of different good strings that can be constructed satisfying
    these properties. Since the answer can be large, return it modulo 10^9 + 7.

    Constraints:
        1 <= low <= high <= 10^5
        1 <= zero, one <= low
    """

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """Simple dynamic programming solution.
        O(high) / O(high)     time / space complexity
        """

        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= MOD

        return sum(dp[low:]) % MOD
