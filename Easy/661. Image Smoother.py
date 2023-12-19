"""
An image smoother is a filter of the size 3 x 3 that can be applied to each
cell of an image by rounding down the average of the cell and the eight
surrounding cells (i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present, we do not
consider it in the average (i.e., the average of the four cells in the red smoother).

Constraints:
- m == img.length
- n == img[i].length
- 1 <= m, n <= 200
- 0 <= img[i][j] <= 255
"""


class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        """
        Naive implementation.
        O(n * m) / O(n * m)     time / space complexity
        """
        self.img = img
        res = [[0] * len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                res[i][j] = self._avg(i, j)
        return res

    def _avg(self, i: int, j: int):
        _sum = 0
        cell_count = 0
        for newi in range(i - 1, i + 2):
            for newj in range(j - 1, j + 2):
                if self._in_img(newi, newj):
                    cell_count += 1
                    _sum += self.img[newi][newj]
        return _sum // cell_count

    def _in_img(self, i: int, j: int) -> bool:
        return i >= 0 and j >= 0 and i < len(self.img) and j < len(self.img[0])
