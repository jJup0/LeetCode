from typing import List


class Solution:
    """
    Given a 2D integer array matrix, return the transpose of matrix.
    The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
    Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 1000
        1 <= m * n <= 10^5
        -10^9 <= matrix[i][j] <= 10^9
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # construct a single row by iterating over rows in inner loop, and columns in outer loop
        return [[matrix[i][j] for i in range(len(matrix))]
                for j in range(len(matrix[0]))]
