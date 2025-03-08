"""
There exists an infinitely large two-dimensional grid of uncolored unit cells.
You are given a positive integer n, indicating that you must do the following
routine for n minutes:
- At the first minute, color any arbitrary unit cell blue.
- Every minute thereafter, color blue every uncolored cell that touches a blue cell.

Below is a pictorial representation of the state of the grid after minutes 1,
2, and 3.

Return the number of colored cells at the end of n minutes.

Constraints:
- 1 <= n <= 10^5
"""


class Solution:
    def coloredCells(self, n: int) -> int:
        # rearrage terms:
        # 1 + sum(i * 2 + (i - 2) * 2 for i in range(2, n + 1))
        # ->  1 + sum((i-1) * 4 for i in range(2, n + 1))
        # ->  1 + sum(i * 4 for i in range(1, n))
        # ->  1 + 4 * sum(i for i in range(1, n))
        # ->  1 + 4 * (n * (n-1) // 2)
        # ->
        return 1 + 2 * n * (n - 1)

    def coloredCells_linear(self, n: int) -> int:
        return 1 + sum(i * 2 + (i - 2) * 2 for i in range(2, n + 1))
