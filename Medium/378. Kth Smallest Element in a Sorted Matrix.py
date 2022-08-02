import heapq
from typing import List


class Solution:
    """
    Given an n x n matrix where each of the rows and columns is sorted in ascending order,
    return the kth smallest element in the matrix.
    Note that it is the kth smallest element in the sorted order, not the kth distinct element.
    You must find a solution with a memory complexity better than O(n2).
    Constraints:
        n == matrix.length == matrix[i].length
        1 <= n <= 300
        -10^9 <= matrix[i][j] <= 10^9
        All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
        1 <= k <= n^2
    """

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Min-heap solution
        O(n * log(n)) / O(n)    time/space complexity
        """
        n = len(matrix)

        # min heap frontier for smallest value and position in matrix
        q = [(matrix[y][0], 0, y) for y in range(n)]
        heapq.heapify(q)

        # result variable
        val = -1

        # push/pop to frontier k times
        for _ in range(k):
            # pop smallest val from frontier
            val, x, y = heapq.heappop(q)
            # add neighbor to frontier
            next_x = x + 1
            if next_x < n:
                heapq.heappush(q, (matrix[y][next_x], next_x, y))

        # retunr last popped value
        return val
