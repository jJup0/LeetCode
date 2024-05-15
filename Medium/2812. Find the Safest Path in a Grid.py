"""
You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:
- A cell containing a thief if grid[r][c] = 1
- An empty cell if grid[r][c] = 0

You are initially positioned at cell (0, 0). In one move, you can move to any
adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan
distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1),
(r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to
|a - x| + |b - y|, where |val| denotes the absolute value of val.

Constraints:
- 1 <= grid.length == n <= 400
- grid[i].length == n
- grid[i][j] is either 0 or 1.
- There is at least one thief in the grid.
"""

import heapq
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        """
        O(n^2 * log(n)) / O(n^2)    time / space complexity
        """

        def iter_neighbors(i: int, j: int):
            for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                newi = i + di
                newj = j + dj
                if newi < 0 or newi >= height or newj < 0 or newj >= width:
                    continue
                yield newi, newj

        height = len(grid)
        width = len(grid[0])
        distances = [[0] * width for _ in range(height)]
        visited = [[False] * width for _ in range(height)]

        thief_dist_front: deque[tuple[int, int, int]] = deque(
            (i, j, 0) for i in range(height) for j in range(width) if grid[i][j]
        )
        while thief_dist_front:
            i, j, dist = thief_dist_front.popleft()
            if visited[i][j]:
                continue
            distances[i][j] = dist
            visited[i][j] = True
            for newi, newj in iter_neighbors(i, j):
                thief_dist_front.append((newi, newj, dist + 1))

        # simply djikstra
        bfs_queue: list[tuple[int, int, int]] = [(-distances[0][0], 0, 0)]
        safest = [[0] * width for _ in range(height)]
        while bfs_queue:
            neg_safety, i, j = heapq.heappop(bfs_queue)
            safety = -neg_safety
            if safest[i][j] >= safety:
                continue
            safest[i][j] = safety

            for newi, newj in iter_neighbors(i, j):
                next_safety_og = distances[newi][newj]
                next_safety = min(safety, next_safety_og)
                if next_safety <= safest[newi][newj]:
                    continue

                heapq.heappush(
                    bfs_queue,
                    (-next_safety, newi, newj),
                )

        return safest[-1][-1]
