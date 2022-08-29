from typing import List


class Solution:
    """
    A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost
    row or leftmost column and going in the bottom-right direction until reaching the matrix's
    end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix,
    includes cells mat[2][0], mat[3][1], and mat[4][2].
    Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and
    return the resulting matrix.
    """

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        O(log(m + n) * m * n) / O(m + n)    time / space complexity
        """
        m = len(mat)
        n = len(mat[0])

        # sort diagonals starting from left side
        for i in range(len(mat)):
            # calulate length of diagonal
            min_len = min(m - i, n)

            # get all items and sort them
            l = sorted(mat[i + delta][delta] for delta in range(min_len))

            # replace old diagonal with sorted
            for delta in range(min_len):
                mat[i + delta][delta] = l[delta]

        # sort diagonals starting from top side
        for j in range(1 + len(mat[0])):
            # calulate length of diagonal
            min_len = min(m, n - j)

            # get all items and sort them
            l = sorted(mat[delta][j + delta] for delta in range(min_len))

            # replace old diagonal with sorted
            for delta in range(min_len):
                mat[delta][j+delta] = l[delta]

        return mat
