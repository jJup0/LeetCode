"""
The Tribonacci sequence T_n is defined as follows:

T_0 = 0, T_1 = 1, T_2 = 1, and T_n+3 = T_n + T_n+1 + T_n+2 for n >= 0.

Given n, return the value of T_n.

Constraints:
- 0 <= n <= 37
- The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        trib = [0, 1, 1]
        for _ in range(n - 2):
            trib.append(sum(trib[-3:]))
        return trib[n]
