class Solution:
    """
        Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and all the
    elements on the secondary diagonal that are not part of the primary diagonal.

    Constraints:
        n == mat.length == mat[i].length
        1 <= n <= 100
        1 <= mat[i][j] <= 100
    """

    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        primary = sum(mat[i][i] for i in range(n))
        secondary = sum(mat[i][n - 1 - i] for i in range(n))

        middle_double = -mat[n // 2][n // 2] if n & 1 else 0

        return primary + secondary + middle_double
