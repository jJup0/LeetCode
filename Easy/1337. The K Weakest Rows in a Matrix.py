class Solution:
    """
    You are given an m x n binary matrix mat of 1's (representing soldiers) and
    0's (representing civilians). The soldiers are positioned in front of the
    civilians. That is, all the 1's will appear to the left of all the 0's in
    each row.

    A row i is weaker than a row j if one of the following is true:
    - The number of soldiers in row i is less than the number of soldiers in
      row j.
    - Both rows have the same number of soldiers and i < j.

    Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

    Constraints:
    - m == mat.length
    - n == mat[i].length
    - 2 <= n, m <= 100
    - 1 <= k <= m
    - matrix[i][j] is either 0 or 1.
    """

    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        def powerOfRow(row: list[int]) -> int:
            # binary search to get position of first 0
            lo = 0
            hi = len(row)
            while lo < hi:
                mid = (lo + hi) >> 1
                if row[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        powers = sorted((powerOfRow(row), i) for i, row in enumerate(mat))
        return [i for _, i in powers[:k]]
