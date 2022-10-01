from functools import cache


class Solution:
    """
    A message containing letters from A-Z can be encoded into numbers using the following mapping:
        'A' -> "1"
        'B' -> "2"
        ...
        'Z' -> "26"
    To decode an encoded message, all the digits must be grouped then mapped back into letters
    using the reverse of the mapping above (there may be multiple ways). For example, "11106" can
    be mapped into:
        "AAJF" with the grouping (1 1 10 6)
        "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is
    different from "06".
    Given a string s containing only digits, return the number of ways to decode it.
    The test cases are generated so that the answer fits in a 32-bit integer.
    Constraints:
        1 <= s.length <= 100
        s contains only digits and may contain leading zero(s).
    """

    def numDecodings(self, s: str) -> int:
        return self.numDecodings_cache_translated(s)

    # max length of s is 100, cache is just dictionary version of dp
    @cache
    def numDecodings_cache(self, s: str) -> int:
        # "" can be decoded in 1 way
        if not s:
            return 1
        
        # if s starts with zero, cannot be decoded
        if s[0] == '0':
            return 0
        
        # if only one digit left, can be decoded in 1 way
        if len(s) == 1:
            return 1

        # find decodings, dropping first digit
        ret = self.numDecodings(s[1:])

        # if first two digits are less than 26, add nr. of decodings dropping first two digits
        if (s[0] == '1') or (s[0] == '2' and s[1] <= '6'):
            ret += self.numDecodings(s[2:])

        return ret

    def numDecodings_cache_translated(self, s: str) -> int:
        n = len(s)

        # memoization; dp[i] = numDecodings(s[i:])
        dp = [-1] * (n + 1)

        # helper function, calculated numDecodings(s[i:]) with memoization
        def helper(i):
            # if numDecodings(s[i:]) not previously calculated
            if dp[i] == -1:
                if i == n:
                    dp[i] = 1
                elif s[i] == "0":
                    dp[i] = 0
                elif i == n-1:
                    dp[i] = 1
                else:
                    dp[i] = helper(i+1)
                    if s[i] == '1' or s[i:i+2] <= '26':
                        dp[i] += helper(i+2)
            return dp[i]

        return helper(0)
