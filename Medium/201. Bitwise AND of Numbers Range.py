"""
Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.

Constraints:
- 0 <= left <= right <= 2^31 - 1
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        O(log(n)) / O(1)    time / space complexity
        """
        shift = 0
        # find highest set bit where left and right differ
        # all bits up to and including this bit will be set to 0 by bitwise AND
        # of the number in the range(left, right) all higher bits are identical
        # for all numbers in the range
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # assert left == right
        # return original left with the first `shift` bits set to 0
        return left << shift
