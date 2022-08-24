import math


class Solution:
    """
    Given an integer n, return true if it is a power of three. Otherwise, return false.
    An integer n is a power of three, if there exists an integer x such that n == 3^x.
    Constraints:
        -2^31 <= n <= 2^31 - 1
    """

    def isPowerOfThree(self, n: int) -> bool:
        return self.isPowerOfThree_log(n)

    def isPowerOfThree_loop(self, n: int) -> bool:
        # keep diving by three and checking remainder until factor of 1 is left
        if n <= 0:
            return False
        while n > 1:
            if n % 3:
                return False
            else:
                n //= 3
        return True

    def isPowerOfThree_preCalcluated(self, n: int) -> bool:
        # check if largest power of three that can fit in an integer is divisible
        return n > 0 and 1162261467 % n == 0

    def isPowerOfThree_log(self, n: int) -> bool:
        # calculate log_3 of the number, round it, take it to the power of three and
        # check if it is equal to the original number
        return n > 0 and math.pow(3, round(math.log(n, 3))) == n
