from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        self.grid = grid
        one_to_n = list(range(len(grid)))
        return self._equal_pairs(one_to_n, one_to_n, 0)

    def _equal_pairs(self, row_idxs: list[int], col_idxs: list[int], depth: int) -> int:
        """equalPairs helper function.
        Given a list of row and column indexes which have the same first *depth* numbers,
        calculates how many row and column pairs are fully equal.

        e.g. row_idxs = [0], col_idxs = [0], depth = 2 means that the first two numbers in
        the first row and the first column are equal. So continue by checking 3rd number.
        """

        grid = self.grid
        # if end of square matrix reached, trivially calculate pairs
        if depth == len(grid):
            return len(row_idxs) * len(col_idxs)

        # for rows and columns, map values to indexes
        rows: dict[int, list[int]] = defaultdict(list)
        for i in row_idxs:
            num = grid[i][depth]
            rows[num].append(i)

        cols: dict[int, list[int]] = defaultdict(list)
        for j in col_idxs:
            num = grid[depth][j]
            cols[num].append(j)

        # iterate through all new/next numbers in current rows,
        # and recurse with columns that have the same next value
        res = 0
        for num in rows:
            if num in cols:
                res += self._equal_pairs(rows[num], cols[num], depth + 1)
        return res
