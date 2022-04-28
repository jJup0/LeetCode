import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights[0])
        m = len(heights)
        n_dec = n - 1
        m_dec = m - 1

        # constraint: 1 <= heights[i][j] <= 10^6
        effort_to_coords = [[1_000_001] * n for _ in range(m)]

        # min heap with values (effort_to_square, x, y)
        min_heap = [(0, 0, 0)]

        # left, right, down, up deltas for x and y
        deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # function to get in bound neighbors of coordinates
        def get_valid_neighbors(x, y):
            neighbors = []
            if x > 0:
                neighbors.append((x - 1, y))
            if x < n_dec:
                neighbors.append((x + 1, y))
            if y > 0:
                neighbors.append((x, y - 1))
            if y < m_dec:
                neighbors.append((x, y + 1))
            return neighbors

        while min_heap:
            # get the squre with the lowest effort from the heap
            effort, x, y = heapq.heappop(min_heap)

            # effort_to_coords changed in the mean time, effort could be larger, if so, skip
            if effort >= effort_to_coords[y][x]:
                continue

            # if arrived at bottom coordinates, return effort, guaranteed to be lowest possible due to min heap
            if x == n_dec and y == m_dec:
                return effort

            # update lowest possible effort to coordinates
            effort_to_coords[y][x] = effort

            # store current height in local variable for performance
            curr_height = heights[y][x]

            # go through all possible neighbors of current coordinate
            for new_x, new_y in get_valid_neighbors(x, y):
                # if the neighbor's coordinates are in bounds, calculate the effort to get there
                effort_to_next = max(effort, abs(curr_height - heights[new_y][new_x]))

                # if its lower than the current effort to get there, add it to the min heap
                if (effort_to_next < effort_to_coords[new_y][new_x]):
                    heapq.heappush(min_heap,  (effort_to_next, new_x, new_y))
