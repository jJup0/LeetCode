"""
You are given a binary matrix matrix of size m x n, and you are allowed to
rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element
of the submatrix is 1 after reordering the columns optimally.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m * n <= 10^5
- matrix[i][j] is either 0 or 1.
"""


class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        """
        O(n * m * log(n))
        """
        m = len(matrix)
        n = len(matrix[0])

        # set matrix[i][j] to be the amount one consecutive 1's in the ith column up to row j
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        # for each row, find the largest submatrix of 1's, where the last
        # row of the submatrix is the "current" row
        res = 0
        for row in matrix:
            row.sort(reverse=True)
            for submatrix_width, submatrix_height in enumerate(row, start=1):
                res = max(res, submatrix_height * submatrix_width)

        return res
