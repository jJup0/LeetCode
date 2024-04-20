"""
You are given a 0-indexed m x n binary matrix land where a 0 represents a
hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares
that consist entirely of farmland. These rectangular areas are called groups.
No two groups are adjacent, meaning farmland in one group is not
four-directionally adjacent to another farmland in a different group.

 land can be represented by a coordinate system where the top left corner of
land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the
coordinates of the top left and bottom right corner of each group of farmland.
A group of farmland with a top left corner at (r_1, c_1) and a bottom right
corner at (r_2, c_2) is represented by the 4-length array [r_1, c_1, r_2, c_2].

Return a 2D array containing the 4-length arrays described above for each group
of farmland in land. If there are no groups of farmland, return an empty array.
You may return the answer in any order.

Constraints:
- m == land.length
- n == land[i].length
- 1 <= m, n <= 300
- land consists of only 0's and 1's.
- Groups of farmland are rectangular in shape.
"""


class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        """
        O(n * m) / O(n * m)     time / space complexity
        """
        self.land = land
        groups: list[list[int]] = []

        for i, row in enumerate(land):
            for j, row in enumerate(row):
                if row == 1:
                    groups.append(self._dfs_find_farmland(i, j))

        return groups

    def _dfs_find_farmland(self, starting_i: int, starting_j: int) -> list[int]:
        """Given a field, representing the top left cell of some farmland, find the dimensions of the farmland."""
        i = starting_i
        j = starting_j
        while i < len(self.land) and self.land[i][j] == 1:
            i += 1
        i -= 1
        while j < len(self.land[0]) and self.land[i][j] == 1:
            j += 1
        j -= 1
        res = [starting_i, starting_j, i, j]

        for i in range(starting_i, i + 1):
            for j in range(starting_j, j + 1):
                # could also mark as 0, but good for debugging purposes
                self.land[i][j] = 2

        return res
