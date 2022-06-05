from typing import List


class Solution:
    """
    Given a triangle array, return the minimum path sum from top to bottom.
    For each step, you may move to an adjacent number of the row below. More formally, if you
    are on index i on the current row, you may move to either index i or index i + 1 on the next row.
    Constraints:
        1 <= triangle.length <= 200
        triangle[0].length == 1
        triangle[i].length == triangle[i - 1].length + 1
        -10^4 <= triangle[i][j] <= 10^4
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        O(1) extra space (triangle is modified in place)
        """
        # previous row filled with lowest path sum to that point
        prev_row = triangle[0]
        # iterate through rest of the rows
        for row_len in range(1, len(triangle)):
            row = triangle[row_len]
            # the right most item can only be reached by the right most of the previous row
            row[-1] += prev_row[-1]

            # iterate through all values in previous row, and get minimum for each i in current row
            prev_count = prev_row[0]
            for i, curr in enumerate(prev_row):
                row[i] += min(prev_count, curr)
                prev_count = curr

            # current row is previous row for next iteration
            prev_row = row

        return min(triangle[-1])
