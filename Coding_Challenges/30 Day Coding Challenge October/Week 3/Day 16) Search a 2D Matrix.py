import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (matrix and matrix[0]):
            return False
        i = max(bisect.bisect_right(matrix, [target, float('inf')]) - 1, 0)
        j = max(bisect.bisect_right(matrix[i], target) - 1, 0)
        return matrix[i][j] == target
