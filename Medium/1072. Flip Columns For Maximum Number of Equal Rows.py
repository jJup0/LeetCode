"""
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that
column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number
of flips.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is either 0 or 1.
"""

from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]):
        """
        Complexity:
            Time: (n * m)
            Space: O(n * m)
        """
        # every row as the bitmask needed to make row into all the same characters
        as_flips = [
            "".join("0" if bit == row[0] else "1" for bit in row) for row in matrix
        ]
        # find most common occurance of such bitmaps
        return max(Counter(as_flips).values())

    def _maxEqualRowsAfterFlips_misunderstood(self, matrix: list[list[int]]) -> int:
        # I read the question wrong, this finds the maximum number of rows with equal to EACH OTHER after some number of flips
        as_bits = [int("".join(str(bit) for bit in row), 2) for row in matrix]
        bit_count = len(matrix[0])
        mask = (1 << bit_count) - 1

        res = max(Counter(as_bits).values()) - 1
        for num in as_bits:
            opposite = mask ^ num
            score = 0
            for num in as_bits:
                score += num == opposite
            res = max(res, score)
        return res + 1
