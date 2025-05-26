"""
Given an integer num, return a string of its base 7 representation.

Constraints:
- -10^7 <= num <= 10^7
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = num < 0
        if negative:
            num = -num

        res: list[str] = []
        while num:
            remainder, digit = divmod(num, 7)
            res.append(str(digit))
            num = remainder

        if negative:
            res.append("-")
        return "".join(reversed(res))
