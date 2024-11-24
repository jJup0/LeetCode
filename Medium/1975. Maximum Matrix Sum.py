"""
You are given an n x n integer matrix. You can do the following operation any
number of times:
- Choose any two adjacent elements of matrix and multiply each of them by -1.

Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the
maximum sum of the matrix's elements using the operation mentioned above.

Constraints:
- n == matrix.length == matrix[i].length
- 2 <= n <= 250
- -10^5 <= matrix[i][j] <= 10^5
"""


class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        """
        If there is an even count of negative numbers, all numbers can
        be made positive. Otherwise a single number will have to remain
        negative, make the smallest absolute value in the matrix be
        negative to get the maximum sum.

        Complexity:
            Time: O(n^2)
            Space: O(1)
        """
        # current parity of negative numbers in the matrix
        parity = 0
        # smallest absolute value in the matrix
        smallest_abs = 1_000_000
        # total sum of all absolute values in the matrix
        total_sum = 0
        for row in matrix:
            for val in row:
                if val < 0:
                    parity = 1 - parity
                    val = -val
                total_sum += val
                if val < smallest_abs:
                    smallest_abs = val

        if not parity:
            return total_sum
        # subtract smallest number twice, as it was included in the
        # sum as a positive number, but now is made into a negative
        return total_sum - 2 * smallest_abs
