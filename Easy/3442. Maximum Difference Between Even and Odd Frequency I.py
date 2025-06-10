"""
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a_1) - freq(a_2)
between the frequency of characters a_1 and a_2 in the string such that:
- a_1 has an odd frequency in the string.
- a_2 has an even frequency in the string.

Return this maximum difference.

Constraints:
- 3 <= s.length <= 100
- s consists only of lowercase English letters.
- s contains at least one character with an odd frequency and one with an even
  frequency.
"""

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        max_odd = max((count for count in counter.values() if count & 1))
        min_even = min((count for count in counter.values() if not count & 1))
        return max_odd - min_even
