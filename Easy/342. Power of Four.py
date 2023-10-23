"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.

Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """
        O(log(n)) / O(log(n))     time / space complexity
        """
        # numbers that are a power of 4 only have the highest bit set, and an
        # even number of zeros
        # for negative numbers num_bin[2] == 'b', so rfind('1') does not return 2
        num_bin = bin(num)
        return num_bin.rfind("1") == 2 and len(num_bin) % 2 == 1
