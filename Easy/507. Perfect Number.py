"""
A perfect number is a positive integer that is equal to the sum of its positive
divisors, excluding the number itself. A divisor of an integer x is an integer
that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Constraints:
- 1 <= num <= 10^8
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        divisors_sum = 1
        for i in range(2, int(num**0.5) + 1):
            if not num % i:
                divisors_sum += i + num // i
        return num == divisors_sum
