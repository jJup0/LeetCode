import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return n == 1 << int(math.log(n, 2))
