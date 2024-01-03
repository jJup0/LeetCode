"""
Anti-theft security devices are activated inside a bank. You are given a
0-indexed binary string array bank representing the floor plan of the bank,
which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's
and '1's. '0' means the cell is empty, while'1' means the cell has a security
device.

There is one laser beam between any two security devices if both conditions are met:
- The two devices are located on two different rows: r_1 and r_2, where r_1 < r_2.
- For each row i where r_1 < i < r_2, there are no security devices in the ith row.

Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

Constraints:
- m == bank.length
- n == bank[i].length
- 1 <= m, n <= 500
- bank[i][j] is either '0' or '1'.
"""


class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        prev_ones = 0
        res = 0
        for row in bank:
            ones = row.count("1")
            if ones == 0:
                continue
            res += prev_ones * ones
            prev_ones = ones
        return res
