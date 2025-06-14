"""
You are given an integer num. You know that Bob will sneakily remap one of the
10 possible digits ( 0 to 9 ) to another digit.

Return the difference between the maximum and minimum values Bob can make by
remapping exactlyone digit in num.

Notes:
- When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences
  of d1 in num with d2.
- Bob can remap a digit to itself, in which case num does not change.
- Bob can remap different digits for obtaining minimum and maximum values
  respectively.
- The resulting number after remapping can contain leading zeroes.

Constraints:
- 1 <= num <= 10^8
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = str_num = str(num)
        for digit in str_num:
            if digit != "9":
                max_num = str_num.replace(digit, "9")
                break
        min_num = str_num.replace(str_num[0], "0")
        return int(max_num) - int(min_num)
