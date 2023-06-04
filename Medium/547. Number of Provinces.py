class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        px = self.find(x)
        py = self.find(y)
        self.parents[px] = py


class Solution:
    """
    There are n cities. Some of them are connected, while some are not. If city a
    is connected directly with city b, and city b is connected directly with city c,
    then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other
    cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith
    city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    Constraints:
        1 <= n <= 200
        n == isConnected.length
        n == isConnected[i].length
        isConnected[i][j] is 1 or 0.
        isConnected[i][i] == 1
        isConnected[i][j] == isConnected[j][i]
    """

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        UF = UnionFind(len(isConnected))
        for i, row in enumerate(isConnected):
            for j, is_connected in enumerate(row):
                if is_connected:
                    UF.union(i, j)

        return len(set(UF.find(i) for i in range(len(isConnected))))
