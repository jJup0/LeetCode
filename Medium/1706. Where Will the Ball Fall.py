from typing import List


class Solution:
    """
    You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on
    the top and bottom sides.

    Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a
    ball to the right or to the left.

        A board that redirects the ball to the right spans the top-left corner to the bottom-right 
        corner and is represented in the grid as 1.
        A board that redirects the ball to the left spans the top-right corner to the bottom-left
        corner and is represented in the grid as -1.

    We drop one ball at the top of each column of the box. Each ball can get stuck in the box or
    fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or
    if a board redirects the ball into either wall of the box.

    Return an array answer of size n where answer[i] is the column that the ball falls out of at
    the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets
    stuck in the box.

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 100
        grid[i][j] is 1 or -1.
    """

    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        O(n) / O(1)     time / extra space complexity
        """

        height = len(grid)
        width = len(grid[0])

        # result variable
        final_cols = [-1] * width

        # drop a ball from each column
        for starting_col in range(width):
            col = starting_col
            # let the ball fall through the rows
            for row in range(height):
                board = grid[row][col]
                # if the ball encounters a board slating to the right, and the ball is at the
                # rightmost column, or the left neighboring board slants to the left, the the ball
                # is stuck, so set final col to -1 and break
                # same goes for when the ball encounters a board slanting left and the ball is at
                # the leftmost column, or the right neighboring board slants to the right
                if (board == 1 and (col == width - 1 or grid[row][col + 1] == -1)) or \
                   (board == -1 and (col == 0 or grid[row][col - 1] == 1)):
                    col = -1
                    break

                # let the ball drop either to the right or left
                col += board

            # set the resulting column for the starting column
            final_cols[starting_col] = col

        return final_cols
