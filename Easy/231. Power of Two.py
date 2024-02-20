"""
Given an integer n, return true if it is a power of two. Otherwise, return
false.

An integer n is a power of two, if there exists an integer x such that n == 2^x.

Constraints:
- -2^31 <= n <= 2^31 - 1
"""

import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return n == 1 << round(math.log(n, 2))
