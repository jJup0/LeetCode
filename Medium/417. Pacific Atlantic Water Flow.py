from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> Set[Tuple[int, int]]:
        """
        Simulate water flowing uphill from oceans, dfs spread to all cells
        O(n * m) / O(m * n)     time / space complexity
        """

        m, n = len(heights), len(heights[0])

        # set of coordinates that flow to ocean
        pacific: Set[Tuple[int, int]] = set()
        atlantic: Set[Tuple[int, int]] = set()

        # adds neighbors to ocean of which this cell flows into
        def dfs(row, col, ocean, prev_height):
            if ((row, col) in ocean or prev_height > heights[row][col]):
                return

            # add item to the ocean set
            ocean.add((row, col))

            # call DFS for the other directions
            curr_height = heights[row][col]
            if row < m - 1:
                dfs(row+1, col, ocean, curr_height)
            if row > 0:
                dfs(row-1, col, ocean, curr_height)
            if col < n - 1:
                dfs(row, col+1, ocean, curr_height)
            if col > 0:
                dfs(row, col-1, ocean, curr_height)

        # start dfs for first row -> pacific, last row -> atlantic
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n-1, atlantic, heights[r][n-1])

        # start dfs for first column -> pacific, last column -> atlantic
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m-1, c, atlantic, heights[m-1][c])

        return pacific.intersection(atlantic)

    def pacificAtlantic_firstAttemptSlow(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights),  len(heights[0])

        can_flow = [[0] * n for _ in range(m)]
        for j in range(n):
            can_flow[0][j] |= 1
            can_flow[-1][j] |= 2
        for i in range(m):
            can_flow[i][0] |= 1
            can_flow[i][-1] |= 2

        def dfs(row, col, visited) -> int:
            nonlocal m, n
            if ((row * m + col) in visited) or (can_flow[row][col] >= 4):
                return can_flow[row][col] & 3

            visited.add(row * m + col)

            height = heights[row][col]
            for new_row, new_col in ((row+1, col), (row, col+1), (row-1, col), (row, col-1)):
                if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and heights[new_row][new_col] <= height:
                    can_flow[row][col] |= dfs(new_row, new_col, visited)

            return can_flow[row][col] & 3

        res = []
        for i in range(m):
            for j in range(n):
                dfs(i, j, set())
                can_flow[i][j] |= 4
                if can_flow[i][j] == 7:
                    res.append([i, j])

        return res
