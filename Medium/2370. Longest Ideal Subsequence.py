"""
You are given a string s consisting of lowercase letters and an integer k. We
call a string t ideal if the following conditions are satisfied:
- t is a subsequence of the string s.
- The absolute difference in the alphabet order of every two adjacent letters
  in t is less than or equal to k.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting
some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute
difference in the alphabet order of'a' and'z' is 25, not 1.

Constraints:
- 1 <= s.length <= 10^5
- 0 <= k <= 25
- s consists of lowercase English letters.
"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ress = [0] * 26
        for c in s:
            idx = ord(c) - ord("a")
            score = max(ress[max(idx - k, 0) : idx + k + 1]) + 1
            ress[idx] = score
        return max(ress)
