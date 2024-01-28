"""
Given a matrix and a target, return the number of non-empty submatrices that
sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <=
x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they
have some coordinate that is different: for example, if x1 != x1'.

Constraints:
- 1 <= matrix.length <= 100
- 1 <= matrix[0].length <= 100
- -1000 <= matrix[i] <= 1000
- -10^8 <= target <= 10^8
"""


from collections import Counter


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        return self.numSubmatrixSumTarget_fast(matrix, target)

    def numSubmatrixSumTarget_n_power_4(
        self, matrix: list[list[int]], target: int
    ) -> int:
        """
        Original solution, too slow
        O(n^4) / O(n^2)     time / space complexity
        """
        height = len(matrix)
        width = len(matrix[0])
        # msums[i][j] contains the sum all values in the submatrix `matrix[:i :j]`
        msums = [[0] * (width + 1) for _ in range(height + 1)]
        for i, row in enumerate(matrix, start=1):
            row_sum_so_far = 0
            for j, val in enumerate(row, start=1):
                row_sum_so_far += val
                msums[i][j] = row_sum_so_far + msums[i - 1][j]

        # print(*msums, sep="\n")

        res = 0
        for start_i in range(height):
            for end_i in range(start_i, height):
                for start_j in range(width):
                    for end_j in range(start_j, width):
                        sub_matrix_val = (
                            msums[end_i + 1][end_j + 1]
                            - msums[start_i][end_j + 1]
                            - msums[end_i + 1][start_j]
                            + msums[start_i][start_j]
                        )
                        res += sub_matrix_val == target
                        # print(f"YES [{start_i}:{end_i}][{start_j}:{end_j}]")
                        # for i in range(start_i, end_i + 1):
                        #     print(msums[i][start_j : end_j + 1])

        return res

    def numSubmatrixSumTarget_fast(self, matrix: list[list[int]], target: int) -> int:
        """
        Calculate prefix sums for rows and iterate through column chunks of the matrix.
        Reduce time complexity by performing looksups for previous submatrix sums.
        This is a similar approach to finding all pairs of numbers which sum to target.

        O(n * m^2) / O(n * m)   time / space complexity
        """
        height = len(matrix)
        width = len(matrix[0])

        # calculate prefix sums for all rows in the matrix
        row_sums = [[0] * (width + 1) for _ in range(height)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row, start=1):
                row_sums[i][j] += row_sums[i][j - 1] + val

        res = 0
        for col_start in range(width):
            for col_end in range(col_start, width):
                # a counter for the amount of submatrix sums previously encountered,
                # for submatrices that span the `col_start` to `col_end`
                prev_submatrix_sums: dict[int, int] = Counter([0])
                # current submatrix sum
                submatrix_sum = 0
                for i in range(height):
                    # add current row to submatrix sum
                    submatrix_sum += row_sums[i][col_end + 1] - row_sums[i][col_start]
                    # check how much is missing (or extra) to reach target
                    diff_to_target = submatrix_sum - target
                    # increase res by the amount of previous submatrices that
                    # can be removed from the current submatrix to reach target
                    res += prev_submatrix_sums[diff_to_target]
                    # increase the counter of the current submatrix sum
                    prev_submatrix_sums[submatrix_sum] += 1
        return res
