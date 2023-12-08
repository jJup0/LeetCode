"""
You are given a string num, representing a large integer. Return the
largest-valued odd integer (as a string) that is a non-empty substring
of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Constraints:
- 1 <= num.length <= 10^5
- num only consists of digits and does not contain any leading zeros.
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        O(n) / O(1)     time / space complexity
        """
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) & 1:
                return num[: i + 1]
        return ""
