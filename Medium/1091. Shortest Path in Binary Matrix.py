import heapq


class Solution:
    """
    Given an n x n binary matrix grid, return the length of the shortest clear
    path in the matrix. If there is no clear path, return -1.

    A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
    to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    - All the visited cells of the path are 0.
    - All the adjacent cells of the path are 8-directionally connected (i.e., they
        are different and they share an edge or a corner).
    - The length of a clear path is the number of visited cells of this path.

    Constraints:

    - n == grid.length
    - n == grid[i].length
    - 1 <= n <= 100
    - grid[i][j] is 0 or 1
    """

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # priority queue for search front with (priority_value, distance, i, j)
        # priority_value is pseudo_manhattan_distance + covered_distance
        # manhattan distance is max(abs(n-1-x), abs(n-1-y)) but goal is never "behind" x and y so drop abs(),
        # and ignore constants of n-1
        q = [(0, 1, 0, 0)]
        while q:
            # get coordinate "closest" to goal
            _, dist, i, j = heapq.heappop(q)

            # if coordinates on not free space continue
            if grid[i][j]:
                continue

            # if coordinates are goal, return distance
            if i == n - 1 and j == n - 1:
                return dist

            # fill current coordinates to avoid searching again
            grid[i][j] = 1

            # go through all valid neighbors with empty squares and
            # add them to the queue with incremented distance value
            for newi, newj in (
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
                (i + 1, j + 1),
                (i + 1, j - 1),
                (i - 1, j - 1),
                (i - 1, j + 1),
            ):
                if (0 <= newi < n) and (0 <= newj < n) and (not grid[newi][newj]):
                    heapq.heappush(q, (max(-newi, -newj) + dist, dist + 1, newi, newj))

        # goal not reachable
        return -1
