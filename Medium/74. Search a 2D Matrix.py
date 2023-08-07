import bisect


class Solution:
    """
    You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.
    - Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 100
    - -10^4 <= matrix[i][j], target <= 10^4
    """

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        First binary search the first column for target, then the resulting row.
        O(1) space solution exists: `i = bisect.bisect_right(matrix, [target, float("inf")]) - 1`.

        O(log(n*m)) / O(m)  time / space complexity
        """

        # binary search first column
        i = bisect.bisect_right([row[0] for row in matrix], target) - 1

        # regular binary search for found row index
        j = bisect.bisect_right(matrix[i], target) - 1

        # using bisect_right() - 1 instead of bisect_left() to ensure no index
        # out of bounds. i and j may be equal to -1 if target is not in the
        # matrix, but no matter, because negative indexes are allowed
        return matrix[i][j] == target
