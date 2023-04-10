class Solution:
    """
    You are given an m x n binary matrix grid, where 0 represents a
    sea cell and 1 represents a land cell.

    A move consists of walking from one land cell to another adjacent
    (4-directionally) land cell or walking off the boundary of the grid.

    Return the number of land cells in grid for which we cannot walk
    off the boundary of the grid in any number of moves.

    Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 500
        grid[i][j] is either 0 or 1.
    """

    def numEnclaves(self, grid: list[list[int]]) -> int:
        NOT_ENLCAVE = 2

        N_DEC = len(grid) - 1
        M_DEC = len(grid[0]) - 1

        # get all land squares bordering the edge and add to non_enclaves set
        non_enclaves = set()
        for i in range(len(grid)):
            if grid[i][0] == 1:
                non_enclaves.add((i, 0))
            if grid[i][M_DEC] == 1:
                non_enclaves.add((i, M_DEC))
        for j in range(1, M_DEC):
            if grid[0][j] == 1:
                non_enclaves.add((0, j))
            if grid[N_DEC][j] == 1:
                non_enclaves.add((N_DEC, j))

        DELTAS = ((0, -1), (-1, 0), (0, 1), (1, 0))

        def land_neighbors_of(i, j):
            """Generates all direct land neighbors bordering grid[i][j]."""
            for di, dj in DELTAS:
                newi = i + di
                newj = j + dj
                if newi < 0 or newi > N_DEC or newj < 0 or newj > M_DEC:
                    continue
                if grid[newi][newj] == 1:
                    yield (newi, newj)

        # recursively mark all landmass squares
        # neighboring non-enclaves as non-enclaves
        visited = set()
        while non_enclaves:
            edgeland = non_enclaves.pop()
            i, j = edgeland
            # mark square as non-enclave
            grid[i][j] = NOT_ENLCAVE
            for edgeland_neighbor in land_neighbors_of(i, j):
                if edgeland_neighbor in visited:
                    continue
                # add landmass neighbor to non-enclave bfs set
                visited.add(edgeland_neighbor)
                non_enclaves.add(edgeland_neighbor)

        # sum up all squares of landmass that have not been marked as non enclaves
        return sum(grid[i][j] == 1 for i in range(1, N_DEC) for j in range(1, M_DEC))
