"""
Given an n x n array of integers matrix, return the minimum sum of any falling
path throughmatrix.

A falling path starts at any element in the first row and chooses the element
in the next row that is either directly below or diagonally left/right.
Specifically, the next element from position (row, col) will be (row + 1, col -
1), (row + 1, col), or (row + 1, col + 1).

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 100
- -100 <= matrix[i][j] <= 100
"""

import heapq
from typing import NamedTuple


class DPState(NamedTuple):
    score: int
    row: int
    col: int


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        return self.minFallingPathSum_simple(matrix)

    def minFallingPathSum_simple(self, matrix: list[list[int]]) -> int:
        """
        O(n * n) / O(n * n)     time / space complexity
        """
        n = len(matrix)
        prev_dp = matrix[0]

        for i in range(1, n):
            # reset dp
            dp = [0] * n
            curr_row = matrix[i]

            # edge cases, first and last column
            dp[0] = min(prev_dp[0], prev_dp[1]) + curr_row[0]
            dp[n - 1] = min(prev_dp[n - 2], prev_dp[n - 1]) + curr_row[n - 1]

            # regular cases
            for j in range(1, n - 1):
                dp[j] = min(prev_dp[j], prev_dp[j - 1], prev_dp[j + 1]) + curr_row[j]
            prev_dp = dp
        return min(prev_dp)

    def minFallingPathSum_bfs(self, matrix: list[list[int]]) -> int:
        """
        O(n * n * log(n)) / O(n * n)    time / space complexity
        """
        INT_INF = 1_000_000
        # make all values positive
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                matrix[i][j] = val + 100

        n = len(matrix)
        dp: list[list[int]] = [[INT_INF] * n for _ in range(n)]
        queue: list[DPState] = [
            DPState(num, 0, col) for col, num in enumerate(matrix[0])
        ]
        heapq.heapify(queue)
        while True:
            score, row, col = heapq.heappop(queue)
            if score >= dp[row][col]:
                continue
            dp[row][col] = score

            if row == n - 1:
                return score - 100 * n
            new_row = row + 1
            for new_col in range(max(0, col - 1), min(n, col + 2)):
                new_score = score + matrix[new_row][new_col]
                heapq.heappush(queue, DPState(new_score, new_row, new_col))
