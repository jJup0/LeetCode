import collections


class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]

    def find(self, city) -> int:
        if self.parents[city] != city:
            self.parents[city] = self.find(self.parents[city])
        return self.parents[city]

    def union(self, child, parent) -> None:
        parent_of_child = self.find(child)
        parent_of_parent = self.find(parent)
        self.parents[parent_of_child] = parent_of_parent


class Solution:
    """
    You are given an integer n. There is an undirected graph with n nodes, numbered
    from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [a_i, b_i]
    denotes that there exists an undirected edge connecting nodes a_i and b_i.

    Return the number of pairs of different nodes that are unreachable from each other.

    Constraints:
        1 <= n <= 10^5
        0 <= edges.length <= 2 * 10^5
        edges[i].length == 2
        0 <= a_i, b_i < n
        a_i != b_i
        There are no repeated edges.
    """

    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        """
        Find disjoint sets with union find data structure, then simple combinatorics
        with the size of the disjoint sets to find out total pairwise unreachable nodes.
        O(n*log(n)) / O(n)      time / space complexity
        """
        union_find = UnionFind(n)
        for a, b in edges:
            union_find.union(a, b)

        # get different disjoint set sizes
        parents = collections.Counter(union_find.find(i) for i in range(n))
        # amount of nodes in previously iterated disjoint sets
        prev_nodes_count = 0
        # result variable
        res = 0
        # simple combinatorics, all nodes in current disjoint set are
        # pairwise unreachable with all previously "seen" nodes
        for _, curr_count in parents.items():
            res += prev_nodes_count * curr_count
            # update previously seen nodes count
            prev_nodes_count += curr_count
        return res
