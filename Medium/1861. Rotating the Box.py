"""
You are given an m x n matrix of characters box representing a side-view of a
box. Each cell of the box is one of the following:
- A stone'#'
- A stationary obstacle'*'
- Empty'.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due
to gravity. Each stone falls down until it lands on an obstacle, another stone,
or the bottom of the box. Gravity does not affect the obstacles' positions, and
the inertia from the box's rotation does not affect the stones' horizontal
positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or
the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Constraints:
- m == box.length
- n == box[i].length
- 1 <= m, n <= 500
- box[i][j] is either'#','*', or'.'.
"""


class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        n = len(box)
        m = len(box[0])

        # make all stones fall to the right
        for row in box:
            # next free spot for a rock to fall into
            next_free = m - 1
            for j in range(m - 1, -1, -1):
                val = row[j]
                if val == "#":
                    # make the rock fall: replace previous position
                    # with air, next free position with rock. Works
                    # also if the rock does not fall at all
                    row[j] = "."
                    row[next_free] = "#"
                    next_free -= 1
                elif val == "*":
                    # obstacle, so next free position for a rock is
                    # one index before the current
                    next_free = j - 1

        # rotate box
        res = [[""] * n for _ in range(m)]
        for i, row in enumerate(box):
            curr_column = n - 1 - i
            for j, val in enumerate(row):
                res[j][curr_column] = val
        return res
