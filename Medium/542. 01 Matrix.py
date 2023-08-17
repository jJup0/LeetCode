from collections import deque


class Solution:
    """
    Given an m x n binary matrix mat, return the distance of the nearest 0 for
    each cell.

    The distance between two adjacent cells is 1.

    Constraints:
    - m == mat.length
    - n == mat[i].length
    - 1 <= m, n <= 10^4
    - 1 <= m * n <= 10^4
    - mat[i][j] is either 0 or 1.
    - There is at least one 0 in mat.
    """

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        return self._update_matrix_two_pass(mat)

    def _update_matrix_bfs(self, mat: list[list[int]]) -> list[list[int]]:
        """
        BFS visit cells starting from cells with 0
        O(n * m) / O(n * m)     time / space complexity
        """
        height = len(mat)
        width = len(mat[0])

        INF = width * height + 1
        res = [[INF] * width for _ in range(height)]

        queue: deque[tuple[int, int, int]] = deque()
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if val == 0:
                    res[i][j] = 0
                    queue.append((0, i, j))

        neighbor_deltas = ((-1, 0), (0, -1), (0, 1), (1, 0))
        while queue:
            dist, i, j = queue.popleft()
            new_dist = dist + 1
            for di, dj in neighbor_deltas:
                newi = i + di
                newj = j + dj
                if newi < 0 or newj < 0 or newi >= height or newj >= width:
                    # out of bounds
                    continue
                if res[newi][newj] <= new_dist:
                    # has closer neighbor
                    continue
                res[newi][newj] = new_dist
                queue.append((new_dist, newi, newj))
        return res

    def _update_matrix_two_pass(self, mat: list[list[int]]) -> list[list[int]]:
        """
        First find closest 0 from upper & left neighbors, then find closest 0 from lower & right neighbors.
        O(n * m) / O(n * m)     time / space complexity
        """
        height = len(mat)
        width = len(mat[0])
        INF = width * height + 1

        for i in range(height):
            for j in range(width):
                if mat[i][j] > 0:
                    # matrix[i][j] is not 0
                    top = mat[i - 1][j] if i > 0 else INF
                    left = mat[i][j - 1] if j > 0 else INF
                    mat[i][j] = min(top, left) + 1

        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                if mat[i][j] > 0:
                    # matrix[i][j] is not 0
                    right = mat[i][j + 1] if j < width - 1 else INF
                    bottom = mat[i + 1][j] if i < height - 1 else INF
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)

        return mat
