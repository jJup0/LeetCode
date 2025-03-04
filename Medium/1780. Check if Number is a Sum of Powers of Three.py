"""
Given an integer n, return true if it is possible to represent n as the sum of
distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

Constraints:
- 1 <= n <= 10^7
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """Check if n in base 3 contains any 2's.

        Complexity:
            Time: O(log(n))
            Space: O(1)
        """
        while n:
            n, digit = divmod(n, 3)
            if digit == 2:
                return False
            n //= 3
        return True
