class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n + 1)]
        self.min_dist = [float("inf") for _ in range(n + 1)]

    def find(self, city) -> int:
        if self.parents[city] != city:
            self.parents[city] = self.find(self.parents[city])
        return self.parents[city]

    def union(self, a, b) -> None:
        a_parent = self.find(a)
        b_parent = self.find(b)
        if self.min_dist[a_parent] < self.min_dist[b_parent]:
            self.parents[b_parent] = a_parent
        else:
            self.parents[a_parent] = b_parent

    def update_min_val(self, city, dist) -> None:
        self.min_dist[city] = min(self.min_dist[city], dist)

    def get_min_val(self, city) -> int:
        return self.min_dist[city]


class Solution:
    """
    You are given a positive integer n representing n cities numbered from 1 to n.
    You are also given a 2D array roads where roads[i] = [ai, bi, distancei]
    indicates that there is a bidirectional road between cities ai and bi with a
    distance equal to distancei. The cities graph is not necessarily connected.

    The score of a path between two cities is defined as the minimum distance
    of a road in this path.

    Return the minimum possible score of a path between cities 1 and n.

    Note:
        A path is a sequence of roads between two cities.
        It is allowed for a path to contain the same road multiple times, and you can
            visit cities 1 and n multiple times along the path.
        The test cases are generated such that there is at least one path between
            1 and n.

    Constraints:
        2 <= n <= 105^
        1 <= roads.length <= 10^5
        roads[i].length == 3
        1 <= a_i, b_i <= n
        a_i != b_i
        1 <= distancei <= 10^4
        There are no repeated edges.
        There is at least one path between 1 and n.
    """

    def minScore(self, n: int, roads: list[list[int]]) -> int:
        """
        Union find, with parent nodes (cities) having lower/equal distance than their child nodes.
        O(n*log(n)) / O(n)      time / space complexity
        """

        # first update minimum distance that each city has to any other city
        union_find = UnionFind(n)
        for a, b, dist in roads:
            union_find.update_min_val(a, dist)
            union_find.update_min_val(b, dist)

        # then find disjoint sets, parent "city" of a disjoint set is the
        # one with the smallest distance to any other city
        for a, b, dist in roads:
            union_find.union(a, b)

        # find city which city 1 is connected to which has
        # smallest distance to any other city
        parent = union_find.find(1)
        # return that city's minimum distance to any other city
        return union_find.get_min_val(parent)
