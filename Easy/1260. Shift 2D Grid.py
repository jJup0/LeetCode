import itertools
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        # flatten list in O(m*n) to make shifting easier
        flattened = list(itertools.chain.from_iterable(grid))

        # shift the one dimensional list in O(m*n)
        k = k % len(flattened)
        shifted = flattened[-k:] + flattened[:-k]

        # reconstruct the grid from the shifted list in O(n*m)
        m = len(grid)
        n = len(grid[0])
        res = [shifted[i * n:(i+1) * n] for i in range(m)]
        return res
