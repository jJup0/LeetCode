class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))

    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        px = self.find(x)
        py = self.find(y)
        self.parents[px] = py
