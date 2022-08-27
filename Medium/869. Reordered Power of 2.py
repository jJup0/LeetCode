import math


class Solution:
    """
    You are given an integer n. We reorder the digits in any order (including the original order)
    such that the leading digit is not zero.
    Return true if and only if we can do this so that the resulting number is a power of two.
    """

    def reorderedPowerOf2(self, n: int) -> bool:
        """
        O(1) / O(1)     time / space complexity
        """
        # lowest power of 2 with same magnitude as n
        power = 1 << math.ceil(math.log(10 ** (len(str(n)) - 1), 2))

        # digits of n sorted
        n_sorted = sorted(str(n))

        # check if the next 4 powers of two (max amount of powers with same amount of digits)
        # contain the same digits as n
        for _ in range(4):
            if sorted(str(power)) == n_sorted:
                return True
            power *= 2

        return False
