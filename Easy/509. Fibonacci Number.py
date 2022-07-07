from array import array


class Solution:
    """
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
    such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).
    Constraints:
        0 <= n <= 30
    """

    def fib(self, n: int) -> int:

        # bind i and set to n to handle special cases of n==0 and n==1
        i = n

        # use array of length two to use indexing, rather than slow if statements
        prev = array('l', [0, 1])

        for i in range(n-1):
            # idx in prev to add to is i % 2, add other item to it
            idx = i & 1
            prev[idx] += prev[1 - idx]

        # final fibonacci number will be in prev[i & 1]
        return prev[i & 1]
