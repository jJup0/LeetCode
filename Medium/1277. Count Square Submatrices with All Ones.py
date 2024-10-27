"""
Given a m * n matrix of ones and zeros, return how many square submatrices have
all ones.

Constraints:
- 1 <= arr.length <= 300
- 1 <= arr[0].length <= 300
- 0 <= arr[i][j] <= 1
"""


class OwnSolution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        Use known positions of squares of side length x - 1 to determine
        in O(1) if a cell is the bottom left corrner of a 1s square of size x.
        Complexity:
            Time: O(n * m * min(n, m))
            Space: O(n * m)
        """
        self.matrix = matrix
        bottom_left_corners: set[tuple[int, int]] = set(
            (i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if val
        )

        height = len(matrix)
        width = len(matrix[0])
        res = len(bottom_left_corners)
        for square_size in range(2, min(height, width) + 1):
            if not bottom_left_corners:
                break
            new_bottom_left_corners = self.get_new_bottom_left_corners_faster(
                bottom_left_corners, square_size
            )
            res += len(new_bottom_left_corners)
            bottom_left_corners = new_bottom_left_corners
        return res

    def get_new_bottom_left_corners_intuitive(
        self, bottom_left_corners: set[tuple[int, int]], square_size: int
    ):
        matrix = self.matrix
        height = len(matrix)
        width = len(matrix[0])

        new_bottom_left_corners: set[tuple[int, int]] = set()
        # note that iterating over all i, j here is a huge waste of time
        for i in range(square_size - 1, height):
            for j in range(width - square_size + 1):
                if (
                    matrix[i][j]
                    and (i - 1, j) in bottom_left_corners
                    and (i, j + 1) in bottom_left_corners
                    # top right corner, not covered by previous squares
                    and matrix[i - square_size + 1][j + square_size - 1]
                ):
                    new_bottom_left_corners.add((i, j))
        return new_bottom_left_corners

    def get_new_bottom_left_corners_faster(
        self, bottom_left_corners: set[tuple[int, int]], square_size: int
    ):
        # faster for matrices with few 1's
        prev_square_size = square_size - 1
        new_bottom_left: set[tuple[int, int]] = set()
        for i_dec, j in bottom_left_corners:
            i = i_dec + 1
            if i == len(self.matrix):
                continue
            if (
                self.matrix[i][j]
                and (i, j + 1) in bottom_left_corners
                and self.matrix[i - prev_square_size][j + prev_square_size]
            ):
                new_bottom_left.add((i, j))
        return new_bottom_left


class Solution2:
    def countSquares(self, matrix: list[list[int]]) -> int:
        """
        Use known positions of squares of side length x - 1 to determine
        in O(1) if a cell is the bottom left corrner of a 1s square of size x.
        Complexity:
            Time: O(n * m)
            Space: O(m)
        """

        width = len(matrix[0])

        # size of squares of the previous row in the matrix
        # prev_squares_row[j] = largest square size for having (i,j) as the bottom right corner
        prev_squares_row = list(matrix[0])
        res = sum(prev_squares_row)

        for i in range(1, len(matrix)):
            curr_squares_row = [0] * width
            curr_squares_row[0] = matrix[i][0]
            for j in range(1, width):
                if matrix[i][j]:
                    curr_squares_row[j] = 1 + min(
                        curr_squares_row[j - 1],
                        prev_squares_row[j],
                        prev_squares_row[j - 1],
                    )
            res += sum(curr_squares_row)
            prev_squares_row = curr_squares_row
        return res


class Solution(Solution2):
    pass
