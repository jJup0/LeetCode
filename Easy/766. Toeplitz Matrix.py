from typing import List


class Solution:
    """
    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

    Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 20
        0 <= matrix[i][j] <= 99
    """

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        min_len = min(m, n)

        # check diagonals starting from first row
        for i in range(m):
            # set the value which every entry should have
            val = matrix[i][0]

            # calculate the length of this diagonal
            diag_len = min(m - i, min_len)

            # check if every value is the same
            if any(matrix[i + j][j] != val for j in range(1, diag_len)):
                return False

        # check diagonals starting from second column (first has already been checked)
        for j in range(1, n):
            val = matrix[0][j]
            diag_len = min(n - j, min_len)
            if any(matrix[i][j + i] != val for i in range(1, diag_len)):
                return False

        # if values within a diagonal do not differ, for all diagonals, return true
        return True
