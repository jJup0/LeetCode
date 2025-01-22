"""
You are given an integer matrix isWater of size m x n that represents a map of
land and water cells.
- If isWater[i][j] == 0, cell (i, j) is a land cell.
- If isWater[i][j] == 1, cell (i, j) is a water cell.

You must assign each cell a height in a way that follows these rules:
- The height of each cell must be non-negative.
- If the cell is a water cell, its height must be 0.
- Any two adjacent cells must have an absolute height difference of at most 1.
  A cell is adjacent to another cell if the former is directly north, east, south,
  or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is
maximized.

Return an integer matrix height of size m x n where height[i][j] is cell
(i, j)'s height. If there are multiple solutions, return any of them.

Constraints:
- m == isWater.length
- n == isWater[i].length
- 1 <= m, n <= 1000
- isWater[i][j] is 0 or 1.
- There is at least one water cell.
"""


class Solution:
    def highestPeak(self, is_water: list[list[int]]) -> list[list[int]]:
        """
        Start at water and BFS make adjacent land one higher.
        Complexity:
            Time: O(n * m)
            Space: O(n * m)
        """
        height = len(is_water)
        width = len(is_water[0])

        # maximal heights of cells
        heights = [[-1] * width for _ in range(height)]
        # bfs front for visiting cells
        front: list[tuple[int, int]] = []
        for i, row in enumerate(is_water):
            for j, val in enumerate(row):
                if val:
                    heights[i][j] = 0
                    front.append((i, j))

        # deltas for visiting neighbors
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # next height for land
        next_height = 1
        while front:
            # list of coordinates for next BFS loop
            new_front: list[tuple[int, int]] = []
            for i, j in front:
                for di, dj in deltas:
                    new_i = i + di
                    new_j = j + dj
                    if not (0 <= new_i < height and 0 <= new_j < width):
                        # off grid
                        continue
                    if heights[new_i][new_j] != -1:
                        # already visited
                        continue
                    heights[new_i][new_j] = next_height
                    new_front.append((new_i, new_j))

            next_height += 1
            front = new_front
        return heights
