import heapq
from typing import List


class Solution:
    """
    You are a hiker preparing for an upcoming hike. You are given heights, a 2D
    array of size rows x columns, where heights[row][col] represents the height
    of cell (row, col). You are situated in the top-left cell, (0, 0), and you
    hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
    You can move up, down, left, or right, and you wish to find a route that
    requires the minimum effort.

    A route's effort is the maximum absolute difference in heights between two
    consecutive cells of the route.

    Return the minimum effort required to travel from the top-left cell to the
    bottom-right cell.

    Constraints:
    - rows == heights.length
    - columns == heights[i].length
    - 1 <= rows, columns <= 100
    - 1 <= heights[i][j] <= 10^6
    """

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n_dec = len(heights[0]) - 1
        m_dec = len(heights) - 1

        # create visited structure
        visited = [[False] * (n_dec + 1) for _ in range(m_dec + 1)]

        # min heap with values (effort_to_square, x, y)
        min_heap: list[tuple[int, int, int]] = [(0, 0, 0)]

        while min_heap:
            # get the square with the lowest effort from the heap
            effort, x, y = heapq.heappop(min_heap)

            if visited[y][x]:
                # if already visited, effort is larger/equal than
                # any previous effort at these coordinates
                continue
            # else update visited
            visited[y][x] = True

            # if arrived at bottom coordinates, return effort, guaranteed to be lowest possible due to min heap
            if x == n_dec and y == m_dec:
                return effort

            # get all valid neighbors of current coordinate
            neighbors: list[tuple[int, int]] = []
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
                    effort_to_next = max(
                        effort, abs(curr_height - heights[new_y][new_x])
                    )
                    heapq.heappush(min_heap, (effort_to_next, new_x, new_y))

        assert False
