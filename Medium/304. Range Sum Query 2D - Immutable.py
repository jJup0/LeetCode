from typing import List


class NumMatrix:
    """
    Given a 2D matrix matrix, handle multiple queries of the following type:
        Calculate the sum of the elements of matrix inside the rectangle defined by its upper left
        corner (row1, col1) and lower right corner (row2, col2).
    Implement the NumMatrix class:
        NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
        int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix
        inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
    Constraints:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 200
        -10^5 <= matrix[i][j] <= 10^5
        0 <= row1 <= row2 < m
        0 <= col1 <= col2 < n
        At most 10^4 calls will be made to sumRegion.
    """

    def __init__(self, matrix: List[List[int]]):

        row_sum = 0
        first_row = matrix[0]
        for j, val in enumerate(first_row):
            row_sum += val
            first_row[j] = row_sum

        prev_row = first_row
        for i in range(1, len(matrix)):
            row = matrix[i]
            row_sum = 0
            for j, val in enumerate(row):
                row_sum += val
                row[j] = row_sum + prev_row[j]
            prev_row = row

        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # some inner rectangle sum can be calculated by getting the sumRegion(0, 0, row2, col2)
        # then subtracting the rectangles/areas to the top and right of the queried coordinates
        res = self.matrix[row2][col2]
        if col1:
            # subtract right rectable if applicable
            res -= self.matrix[row2][col1-1]
        if row1:
            # subtract top rectangle if applicable
            res -= self.matrix[row1-1][col2]
        if col1 and row1:
            # if both time was subtracted, add top left rectangle again, as it was subtracted twice
            res += self.matrix[row1-1][col1-1]
        return res
