"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in
row i and column j are 0 (rows and columns are 0-indexed).

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- mat[i][j] is either 0 or 1.
"""


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        """
        O(n * m) / O(n + m)     time / space complexity
        """
        NOT_FOUND = -1
        NOT_UNIQUE = -2
        col_idx_of_unique_one_in_row: list[int] = [NOT_FOUND] * len(mat)
        row_idx_of_unique_one_in_col: list[int] = [NOT_FOUND] * len(mat[0])
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 1:
                    col_idx_of_unique_one_in_row[i] = (
                        j
                        if col_idx_of_unique_one_in_row[i] == NOT_FOUND
                        else NOT_UNIQUE
                    )
                    row_idx_of_unique_one_in_col[j] = (
                        i
                        if row_idx_of_unique_one_in_col[j] == NOT_FOUND
                        else NOT_UNIQUE
                    )

        # return the sum of all cells which are the only one in their row and column
        return sum(
            j >= 0 and col_idx_of_unique_one_in_row[j] >= 0
            for j in row_idx_of_unique_one_in_col
        )
