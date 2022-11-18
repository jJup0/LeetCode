class Solution:
    """
    An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.

    Constraints:
        -2^31 <= n <= 2^31 - 1
    """

    def isUgly(self, num: int) -> bool:
        # zero and negative numbers have other factors
        if num < 1:
            return False

        # divide by ugly factors as long as possible
        for div in (2, 3, 5):
            while num % div == 0:
                num //= div

        # remainder should be 1
        return num == 1
