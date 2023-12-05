"""
You are given a string num representing a large integer. An integer is
good if it meets the following conditions:
- It is a substring of num with length 3.
- It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:
- A substring is a contiguous sequence of characters within a string.
- There may be leading zeroes in num or a good integer.

Constraints:
- 3 <= num.length <= 1000
- num only consists of digits.
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        O(n) / O(1)     time / space complexity
        """
        prev = num
        streak = 0
        NOT_FOUND = "\u0000"
        res = NOT_FOUND
        for digit in num:
            if digit == prev:
                streak += 1
                if streak == 3:
                    res = max(res, digit)
            else:
                prev = digit
                streak = 1

        if res == NOT_FOUND:
            return ""
        return res * 3
