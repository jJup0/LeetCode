class Solution:
    """
    Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
    4-directionally connected group of 0s and a closed island is an island totally
    (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.

    Constraints:
        1 <= grid.length, grid[0].length <= 100
        0 <= grid[i][j] <=1
    """

    def closedIsland(self, grid: list[list[int]]) -> int:
        NOT_ISLAND = 3
        IS_ISLAND = 4

        N_DEC = len(grid) - 1
        M_DEC = len(grid[0]) - 1

        # get all land squares bordering the edge and add to non_islands set
        non_islands = set()
        for i in range(len(grid)):
            if grid[i][0] == 0:
                non_islands.add((i, 0))
            if grid[i][M_DEC] == 0:
                non_islands.add((i, M_DEC))
        for j in range(1, M_DEC):
            if grid[0][j] == 0:
                non_islands.add((0, j))
            if grid[N_DEC][j] == 0:
                non_islands.add((N_DEC, j))

        DELTAS = ((0, -1), (-1, 0), (0, 1), (1, 0))

        def land_neighbors_of(i, j):
            """Generates all direct land neighbors bordering grid[i][j]."""
            for di, dj in DELTAS:
                newi = i + di
                newj = j + dj
                if newi < 0 or newi > N_DEC or newj < 0 or newj > M_DEC:
                    continue
                if grid[newi][newj] != 0:
                    continue
                yield (newi, newj)

        # recursively add all landmass touching previous
        # main land to set of mainland squares
        visited = set()
        while non_islands:
            mainland = non_islands.pop()
            i, j = mainland
            grid[i][j] = NOT_ISLAND
            for mainland_neighbor in land_neighbors_of(i, j):
                if mainland_neighbor in visited:
                    continue
                visited.add(mainland_neighbor)
                non_islands.add(mainland_neighbor)

        def island_dfs(i, j):
            """Marks a square and all of its land neighbors as islands."""
            grid[i][j] = IS_ISLAND
            for island_neighbor in land_neighbors_of(i, j):
                newi, newj = island_neighbor
                island_dfs(newi, newj)

        # find all patches of land not marked as main land.
        # mark them as islands with dfs
        island_count = 0
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] == 0:
                    island_dfs(i, j)
                    island_count += 1
        return island_count
