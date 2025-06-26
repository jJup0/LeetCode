"""
You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number
less than or equal to k.

Note:
- The subsequence can contain leading zeroes.
- The empty string is considered to be equal to 0.
- A subsequence is a string that can be derived from another string by deleting
  some or no characters without changing the order of the remaining characters.

Constraints:
- 1 <= s.length <= 1000
- s[i] is either'0' or'1'.
- 1 <= k <= 10^9
"""


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """Use all zeros and greedily use lowest set bits while less than k.

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        zeros = s.count("0")
        ones = 0
        current_value = 0
        for i, c in enumerate(reversed(s)):
            if c == "0":
                continue
            bit = 1 << i
            if current_value + bit > k:
                break
            current_value += bit
            ones += 1
        return zeros + ones


def test():
    sol = Solution()
    res = sol.longestSubsequence("0111101", 518459120)
    assert res == 7


test()
