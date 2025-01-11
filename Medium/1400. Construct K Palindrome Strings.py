"""
Given a string s and an integer k, return true if you can use all the
characters in s to construct k palindrome strings or false otherwise.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= 10^5
"""

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        if k > len(s):
            return False
        return sum(count & 1 for count in Counter(s).values()) <= k
