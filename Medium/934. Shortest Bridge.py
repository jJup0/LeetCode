from collections import deque


class Solution:
    """
    You are given an n x n binary matrix grid where 1 represents land and 0
    represents water.

    An island is a 4-directionally connected group of 1's not connected to any
    other 1's. There are exactly two islands in grid.

    You may change 0's to 1's to connect the two islands to form one island.

    Return the smallest number of 0's you must flip to connect the two islands.

    Constraints:
        n == grid.length == grid[i].length
        2 <= n <= 100
        grid[i][j] is either 0 or 1.
        There are exactly two islands in grid.
    """

    def shortestBridge(self, grid: list[list[int]]) -> int:
        def dfs_find_islands(i: int, j: int, val: int):
            nonlocal deltas, grid, island_val_to_nodes
            # if already visited, return
            if grid[i][j] == val:
                return

            # add to list of islands
            island_val_to_nodes[val].append((i, j))

            # set land to island code value
            grid[i][j] = val

            # visit neighbors and recurse
            for di, dj in deltas:
                newi = i + di
                newj = j + dj
                if 0 <= newi < height and 0 <= newj < width and grid[newi][newj] == 1:
                    dfs_find_islands(newi, newj, val)

        def bfs_find_shortest_bridge(i: int, j: int, length: int) -> None:
            nonlocal deltas, grid, island_val_to_nodes, TARGET_ISLAND, res, bfs_queue
            # check if target reached and update result
            if grid[i][j] == TARGET_ISLAND:
                res = min(res, length)
                return

            # if cell has been visited in fewer steps, break
            if grid[i][j] <= length:
                return

            # update fewest steps needed to reach
            grid[i][j] = length

            # add neighbors to bfs queue
            for di, dj in deltas:
                newi = i + di
                newj = j + dj
                if 0 <= newi < height and 0 <= newj < width and length < res:
                    bfs_queue.append((length + 1, newi, newj))

        height = len(grid)
        width = len(grid[0])
        # movement deltas
        deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # constants to mark cells in the grid
        UNDISCOVERED_OCEAN = 1000
        STARTING_ISLAND = -2
        TARGET_ISLAND = -3

        # list of coordinates in
        island_val_to_nodes: dict[int, list[tuple[int, int]]] = {
            STARTING_ISLAND: [],
            TARGET_ISLAND: [],
        }

        # find cells of two islands and mark them
        curr_island = STARTING_ISLAND
        for i in range(height):
            for j in range(width):
                grid_val = grid[i][j]
                if grid_val == 1:
                    dfs_find_islands(i, j, curr_island)
                    curr_island = TARGET_ISLAND
                elif grid_val == 0:
                    grid[i][j] = UNDISCOVERED_OCEAN

        # bfs with priority queue to find shortest bridge
        # add ocean neighbors of starting island to priority queue
        bfs_queue: deque[tuple[int, int, int]] = deque()
        res = UNDISCOVERED_OCEAN
        for i, j in island_val_to_nodes[STARTING_ISLAND]:
            for di, dj in deltas:
                newi = i + di
                newj = j + dj
                if (
                    0 <= newi < height
                    and 0 <= newj < width
                    and grid[newi][newj] != STARTING_ISLAND
                ):
                    bfs_queue.append((0, newi, newj))

        # find shortest bridge with bfs
        while bfs_queue:
            # pop from queue
            length, i, j = bfs_queue.popleft()
            # break if minimal result found
            if length >= res:
                break
            bfs_find_shortest_bridge(i, j, length)

        return res
