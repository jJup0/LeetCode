"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The
northwest corner is at the first row and column in the grid, and the southeast
corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid.
Whenever you move outside the grid's boundary, we continue our walk outside the
grid (but may return to the grid boundary later.). Eventually, we reach all
rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the
order you visited them.

Constraints:
- 1 <= rows, cols <= 100
- 0 <= rStart < rows
- 0 <= cStart < cols
"""


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, row_start: int, x_start: int
    ) -> list[list[int]]:
        """
        Naive implementation, just follow spiral, add coordinates if they are within the matrix.
        O(rows * cols) / O(rows * cols)     time / space complexity
        """
        # current stride length of spiral
        curr_stride_length = 1
        # directions to move and current movement
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        dir_idx = 0
        # current coordinates
        row = row_start
        col = x_start
        res: list[list[int]] = [[row, col]]

        while len(res) < rows * cols:
            dy, dx = dirs[dir_idx]
            for _ in range(curr_stride_length):
                # move to next cell
                row += dy
                col += dx
                if 0 <= col < cols and 0 <= row < rows:
                    # append coordinates if within matrix
                    res.append([row, col])

            # increase stride length after vertical movement
            if dir_idx == 1 or dir_idx == 3:
                curr_stride_length += 1
            # change direction
            dir_idx = (dir_idx + 1) % 4

        return res
