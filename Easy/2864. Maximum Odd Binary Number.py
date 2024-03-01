"""
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number
is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created
from the given combination.

Note that the resulting string can have leading zeros.

Constraints:
- 1 <= s.length <= 100
- s consists only of '0' and '1'.
- s contains at least one '1'.
"""

from collections import Counter


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        """
        O(n) / O(n)     time / space complexity
        """
        bit_counts = Counter(s)
        return f"{'1' * (bit_counts['1'] - 1)}{'0' * bit_counts['0']}1"
