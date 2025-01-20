"""
You are given a 0-indexed integer array arr, and an m x n integer matrix mat.
arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat
containing the integer arr[i].

Return the smallest index i at which either a row or a column will be
completely painted in mat.

Constraints:
- m == mat.length
- n = mat[i].length
- arr.length == m * n
- 1 <= m, n <= 10^5
- 1 <= m * n <= 10^5
- 1 <= arr[i], mat[r][c] <= m * n
- All the integers of arr are unique.
- All the integers of mat are unique.
"""


class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        """
        Complexity:
            Time: O(n * m)
            Space: O(n * m)
        """
        # mapping from value to coordinates in matrix
        num_to_coords = [(-1, -1)] * (len(arr) + 1)
        for row_nr, row in enumerate(mat):
            for col_nr, val in enumerate(row):
                num_to_coords[val] = (row_nr, col_nr)

        height = len(mat)
        width = len(mat[0])
        # unfilled squares in each row and column
        row_remaining = [height] * width
        col_remaining = [width] * height

        # iterate through array filling up rows and cols in matrix
        for i, val in enumerate(arr):
            row_nr, col_nr = num_to_coords[val]
            row_remaining[col_nr] -= 1
            col_remaining[row_nr] -= 1
            if col_remaining[row_nr] == 0 or row_remaining[col_nr] == 0:
                return i

        raise Exception("Input invalid")
