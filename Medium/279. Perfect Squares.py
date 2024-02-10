from functools import cache
from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        return self.numSquares_lagrange(n)

    @cache
    def numSquares_dp(self, n: int) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        sqrt_n = isqrt(n)
        if n == sqrt_n * sqrt_n:
            return 1

        return min(self.numSquares_dp(n - i * i) for i in range(1, isqrt(n) + 1)) + 1

    def numSquares_lagrange(self, n: int) -> int:
        """
        Lagranges four square theorem.
        O(sqrt(n)) / O(1)     time / space complexity
        """

        def isSquare(n: int) -> bool:
            sqrt_n = isqrt(n)
            return n == sqrt_n * sqrt_n

        # if perfect square then return 1
        if isSquare(n):
            return 1

        while n % 4 == 0:
            n >>= 2

        if n % 8 == 7:
            return 4

        # try all combinations for 2
        for i in range(1, isqrt(n) + 1):
            if isSquare(n - (i * i)):
                return 2

        # if no rules apply, result is 3
        return 3
