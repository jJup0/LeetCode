import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n_dec = len(heights[0]) - 1
        m_dec = len(heights) - 1

        # create visited structure
        visited = [[False] * (n_dec + 1) for _ in range(m_dec + 1)]

        # min heap with values (effort_to_square, x, y)
        min_heap = [(0, 0, 0)]

        while min_heap:
            # get the square with the lowest effort from the heap
            effort, x, y = heapq.heappop(min_heap)

            # if already visited, effort is larger/equal than any previous effort at these coordinates
            if visited[y][x]:
                continue

            # if arrived at bottom coordinates, return effort, guaranteed to be lowest possible due to min heap
            if x == n_dec and y == m_dec:
                return effort

            # update visited
            visited[y][x] = True

            # get all valid neighbors of current coordinate
            neighbors = []
            if x > 0:
                neighbors.append((x - 1, y))
            if x < n_dec:
                neighbors.append((x + 1, y))
            if y > 0:
                neighbors.append((x, y - 1))
            if y < m_dec:
                neighbors.append((x, y + 1))

            # store current height in local variable for performance
            curr_height = heights[y][x]

            # try traversing to each neighbor
            for new_x, new_y in neighbors:
                if not visited[new_y][new_x]:
                    # calculate the effort to get to neighbor, and add to min heap
                    effort_to_next = max(effort, abs(curr_height - heights[new_y][new_x]))
                    heapq.heappush(min_heap,  (effort_to_next, new_x, new_y))
