"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that
row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the
matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including
zero moves).

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- grid[i][j] is either 0 or 1.
"""


class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        """
        O(n * m) / O(n * m)     time / space complexity
        """
        NUM_INVERSE_MASK = (1 << len(grid[0])) - 1
        # result variable, total maximum sum of numbers after flips
        res = 0
        # convert all rows to regular integers
        grid_as_ints = [int("".join(str(cell) for cell in row), 2) for row in grid]
        for i, num in enumerate(grid_as_ints):
            if grid[i][0]:
                res += num
            else:
                # flip each row that starts with a 0
                flipped_num = NUM_INVERSE_MASK ^ num
                res += flipped_num
                grid_as_ints[i] = flipped_num

        # iterate through each column, if there are more 0s than 1s in that column, flip that column
        numbers_count = len(grid)
        for col in range(len(grid[0])):
            # amount of ones in the current column
            ones = sum(((row >> col) & 1) for row in grid_as_ints)
            if ones <= numbers_count // 2:
                # do not actually flip in `grid_as_ints`, just adjust res
                res += (1 << col) * (numbers_count - 2 * ones)

        return res
