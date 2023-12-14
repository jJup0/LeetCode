"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:
- Let the number of ones in the ith row be onesRow_i.
- Let the number of ones in the jth column be onesCol_j.
- Let the number of zeros in the ith row be zerosRow_i.
- Let the number of zeros in the jth column be zerosCol_j.
- diff[i][j] = onesRow_i + onesCol_j - zerosRow_i - zerosCol_j

Return the difference matrix diff.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10^5
- 1 <= m * n <= 10^5
- grid[i][j] is either 0 or 1.
"""


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        """
        O(n*m) / O(n*m)     time / space complexity
        """
        grid_width = len(grid[0])

        # row_sums = onesRow_i - zerosRow_i
        row_sums: list[int] = []
        # col_sums = onesCol_i - zerosCol_i
        col_sums = [0] * grid_width
        for row in grid:
            for j, val in enumerate(row):
                # branchless arithmetic: if the value is a 1, then add 1, if the value is a 0 subtract zero
                col_sums[j] += val * 2 - 1

            # same approach as branchless above, but applied to the whole row
            row_val = 2 * sum(row) - grid_width
            row_sums.append(row_val)

        # construct diff matrix
        diff = [[row_sum + col_sum for col_sum in col_sums] for row_sum in row_sums]
        return diff
