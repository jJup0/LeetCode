"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main
diagonal, switching the matrix's row and column indices.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 1000
- 1 <= m * n <= 105
- -10^9 <= matrix[i][j] <= 10^9
"""


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return self.transpose_list_comprehension(matrix)

    def transpose_regular(self, matrix: list[list[int]]) -> list[list[int]]:
        height = len(matrix)
        width = len(matrix[0])
        new_matrix = [[0] * height for _ in range(width)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                new_matrix[j][i] = val
        return new_matrix

    def transpose_list_comprehension(self, matrix: list[list[int]]) -> list[list[int]]:
        height = len(matrix)
        width = len(matrix[0])
        return [[matrix[i][j] for i in range(height)] for j in range(width)]
