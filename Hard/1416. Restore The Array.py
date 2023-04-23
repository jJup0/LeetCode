class Solution:
    """
    A program was supposed to print an array of integers. The program forgot to print
    whitespaces and the array is printed as a string of digits s and all we know is
    that all integers in the array were in the range [1, k] and there are no leading
    zeros in the array.

    Given the string s and the integer k, return the number of the possible arrays that
    can be printed as s using the mentioned program. Since the answer may be very large,
    return it modulo 10^9 + 7.

    Constraints:
        1 <= s.length <= 10^5
        s consists of only digits and does not contain leading zeros.
        1 <= k <= 10^9
    """

    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        # memoize ways to restructure array
        # dp[0] := 1, dp[i] = numberOfArrays(s[-i:], k)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        # convert string to digit array
        s_int = [int(c) for c in reversed(s)]
        for i, digit in enumerate(s_int):
            # no leading zeroes, so dp[i+1] stays 0
            if digit == 0:
                continue
            # accumulation of ways
            ways = 0
            # current value of "first" number in current array restructure
            curr_val = 0
            for j in range(i, -1, -1):
                # keep adding a digit to the first number in the current
                # virtual array restructure until it is bigger than k
                curr_val = curr_val * 10 + s_int[j]
                if curr_val > k:
                    break
                # add possible ways to restructure what is left of the
                # string to the sum of restructures for s[-i:]
                ways = (ways + dp[j]) % MOD
            # memoize ways to restructure
            dp[i + 1] = ways
        return dp[-1]
