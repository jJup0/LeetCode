import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search on each row in the matrix.
        O(m * log(n)) / O(1) Time/Space
        """
        # perform binary search on each row
        for row in matrix:
            # check if target could even be in row, also avoids bisect_left returning out of bounds
            if target >= row[0] and target <= row[-1]:
                idx = bisect.bisect_left(row, target)
                # if insertion point == target, return True
                if row[idx] == target:
                    return True

        return False
