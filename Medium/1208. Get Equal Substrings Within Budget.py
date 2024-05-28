"""
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of
t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values
of the characters).

Return the maximum length of a substring of s that can be changed to be the
same as the corresponding substring of t with a cost less than or equal to
maxCost. If there is no substring from s that can be changed to its
corresponding substring from t, return 0.

Constraints:
- 1 <= s.length <= 10^5
- t.length == s.length
- 0 <= maxCost <= 10^6
- s and t consist of only lowercase English letters.
"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        Sliding window approach.
        O(n) / O(n)   time / space complexity
        """
        remaining_budget = maxCost
        j = 0
        res = 0
        for i, (c_s, c_t) in enumerate(zip(s, t)):
            cost = abs(ord(c_s) - ord(c_t))
            remaining_budget -= cost
            while remaining_budget < 0:
                remaining_budget += abs(ord(s[j]) - ord(t[j]))
                j += 1
            res = max(res, i - j + 1)
        return res
