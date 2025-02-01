"""
You are given a string s consisting only of digits. A valid pair is defined as
two adjacent digits in s such that:
- The first digit is not equal to the second.
- Each digit in the pair appears in s exactly as many times as its numeric value.

Return the first valid pair found in the string s when traversing from left to
right. If no valid pair exists, return an empty string.

Constraints:
- 2 <= s.length <= 100
- s only consists of digits from'1' to'9'.
"""

from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        digits = [int(c) for c in s]
        counter = Counter(digits)
        prev_digit = -100
        for digit in digits:
            if (
                digit != prev_digit
                and counter[prev_digit] == prev_digit
                and counter[digit] == digit
            ):
                return f"{prev_digit}{digit}"
            prev_digit = digit
        return ""
