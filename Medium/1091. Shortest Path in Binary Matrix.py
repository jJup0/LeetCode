import heapq
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

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
            if i == n-1 and j == n-1:
                return dist
            # fill current coordinates to avoid searching again
            grid[i][j] = 1
            # go through all valid neighbors with empty squares and add them to the queue with incremented distance value
            for newi, newj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j-1), (i-1, j+1)):
                if (0 <= newi < n) and (0 <= newj < n) and (not grid[newi][newj]):
                    heapq.heappush(q, (max(-newi, -newj)+dist, dist+1, newi, newj))
        return -1
