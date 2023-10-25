"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
Now in every subsequent row, we look at the previous row and replace each
occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is
0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of
a table of n rows.

Constraints:
- 1 <= n <= 30
- 1 <= k <= 2^n - 1
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """Every row is same as previous row, extended by ones complement.
        So n does not make any difference.
        O(log(k)) / O(1)    time / space complexity
        """
        # change to 0 indexed
        k -= 1

        curr_power_of_two = 1
        while curr_power_of_two <= k:
            curr_power_of_two <<= 1
        curr_power_of_two >>= 1

        res = 0
        while k > 0:
            # the digit at position k is the opposite to the digit at position k - x
            # where x is the largest power of two <= k
            res = 1 - res
            k -= curr_power_of_two
            while curr_power_of_two > k:
                curr_power_of_two >>= 1

        return res
