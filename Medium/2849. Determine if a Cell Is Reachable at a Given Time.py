"""
You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you
must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or
false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one
corner with it. You can visit the same cell several times.

Constraints:
- 1 <= sx, sy, fx, fy <= 10^9
- 0 <= t <= 10^9
"""


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        """
        Except for (sx,sy) == (fx, fy) and t == 1, as long as the chebyshev
        distance is smaller equal t, we can reach the goal.
        O(1) / O(1)     time / space complexity
        """
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        moves = max(dx, dy)
        if moves == 0 and t == 1:
            return False
        return moves <= t
