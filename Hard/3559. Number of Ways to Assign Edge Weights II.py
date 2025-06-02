"""
There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1.
The tree is represented by a 2D integer array edges of length n - 1, where
edges[i] = [u_i, v_i] indicates that there is an edge between nodes u_i and v_i.

Initially, all edges have a weight of 0. You must assign each edge a weight of
either 1 or 2.

The cost of a path between any two nodes u and v is the total weight of all
edges in the path connecting them.

You are given a 2D integer array queries. For each queries[i] = [u_i, v_i],
determine the number of ways to assign weights to edges in the path such that
the cost of the path between u_i and v_i is odd.

Return an array answer, where answer[i] is the number of valid assignments for
queries[i].

Since the answer may be large, apply modulo 10^9 + 7 to each answer[i].

Note: For each query, disregard all edges not in the path between node u_i and v_i.

Constraints:
- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i] == [u_i, v_i]
- 1 <= queries.length <= 10^5
- queries[i] == [u_i, v_i]
- 1 <= u_i, v_i <= n
- edges represents a valid tree.
"""

from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        """
        Find lowest common ancestor of each node in query, which is the
        shortest path. For this shortest path there are 2**(length - 1) ways to
        make that path have odd weight. Complexity is due to the fact that we
        have runtime of O(n) for each query if we find LCA the normal way. We
        can use "binary lifting" ancestor table for each node to find lowest
        common ancestor quickly.

        Complexity:
            Time: O(n + m * log(n))
            Space: O(n * log(n) + m)
        """
        self.n = len(edges) + 2
        adj_list = self._construct_adjacency_list(edges)

        self.node_to_parent = [0] * (self.n)
        self.node_to_depth = [0] * (self.n)
        depth = self._fill_node_parents_and_depth(adj_list)

        self.node_to_ancestor_lvl = [
            defaultdict(int, {1: self.node_to_parent[i]}) for i in range(self.n)
        ]
        self._construct_nodes_to_ancestors(depth)

        #
        MOD = 10**9 + 7
        return [
            0 if a == b else pow(2, self.get_dist_between_nodes(a, b) - 1, MOD)
            for a, b in queries
        ]

    def _fill_node_parents_and_depth(self, adj_list: list[list[int]]):
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        visited = [False] * (len(adj_list) + 1)
        front = [1]
        depth = 0
        while front:
            new_front: list[int] = []
            for node in front:
                self.node_to_depth[node] = depth
                visited[node] = True
                for neighbor in adj_list[node]:
                    if visited[neighbor]:
                        continue
                    new_front.append(neighbor)
                    self.node_to_parent[neighbor] = node
            front = new_front
            depth += 1
        return depth

    def _construct_adjacency_list(self, edges: list[list[int]]):
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        adj_list: list[list[int]] = [[] for _ in range(self.n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        return adj_list

    def _construct_nodes_to_ancestors(self, depth: int):
        """Fills ancestor lookup with powers of 2. i.e node 1 above, 2 above, 4 above...

        Complexity:
            Time: O(n * log(n))
            Space: O(n * log(n))
        """
        nodes = list(range(1, self.n))
        nodes.sort(key=lambda node: self.node_to_depth[node], reverse=True)

        for jump_base_2 in range(1, depth.bit_length() + 1):
            prev_jump = 1 << (jump_base_2 - 1)
            jump = 1 << jump_base_2
            for node in nodes:
                prev_ancestor = self.node_to_ancestor_lvl[node][prev_jump]
                if prev_ancestor == 0:
                    self.node_to_ancestor_lvl[node][jump] = 0
                    break
                super_ancestor = self.node_to_ancestor_lvl[prev_ancestor][prev_jump]
                self.node_to_ancestor_lvl[node][jump] = super_ancestor

    def get_dist_between_nodes(self, node1: int, node2: int) -> int:
        """Get distance between two nodes by going up the ancestors with as many steps at a time as possible.

        Takes log(depth) steps to get to same depth ancestors, and another
        log(depth) steps to get to lowest common ancestor.

        Complexity:
            Time: O(log(n))
            Space: O(log(n))
        """
        if node1 == node2:
            return 0

        d1 = self.node_to_depth[node1]
        d2 = self.node_to_depth[node2]

        if d1 < d2:
            d1, d2 = d2, d1
            node1, node2 = node2, node1
        if d2 < d1:
            jump_dist = d1 - d2
            power_2 = 1
            while power_2 <= jump_dist:
                power_2 *= 2
            power_2 //= 2
            return power_2 + self.get_dist_between_nodes(
                self.node_to_ancestor_lvl[node1][power_2], node2
            )

        # nodes are at the same depth
        power_2 = 1
        while True:
            power_2 *= 2
            a1 = self.node_to_ancestor_lvl[node1][power_2]
            a2 = self.node_to_ancestor_lvl[node2][power_2]
            if a1 == 0 or a2 == 0:
                # either node does not have an ancestor `power_2` levels up
                power_2 //= 2
                break
            if a1 == a2:
                # found a common ancestor but need to reduce by one power to ensure it is the lowest
                power_2 //= 2
                break

        # keep searching `power_2` levels up, and add 2 * `power_2` to result as
        # both nodes need to go up `power_2` edges to get to their respective ancestors
        return 2 * power_2 + self.get_dist_between_nodes(
            self.node_to_ancestor_lvl[node1][power_2],
            self.node_to_ancestor_lvl[node2][power_2],
        )

    @cache
    def _get_dist_between_nodes_real(self, node1: int, node2: int) -> int:
        """Used to debug/verify _get_dist_between_nodes()"""
        if node1 == node2:
            return 0
        d1 = self.node_to_depth[node1]
        d2 = self.node_to_depth[node2]
        if d1 < d2:
            return 1 + self._get_dist_between_nodes_real(
                node1, self.node_to_parent[node2]
            )
        return 1 + self._get_dist_between_nodes_real(self.node_to_parent[node1], node2)


def test():

    s = Solution()
    res = s.assignEdgeWeights([[1, 2]], [[1, 1], [1, 2]])
    real = [0, 1]
    assert res == real, res
    res = s.assignEdgeWeights(
        [[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]]
    )
    real = [2, 1, 4]
    assert res == real, res

    res = s.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]], [[2, 5]])
    real = [4]
    assert res == real, res

    res = s.assignEdgeWeights([[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 5]])
    real = [8]
    assert res == real, res


def big_test():
    import random
    import timeit

    seed = random.randint(1, 1000000)
    seed = 877628
    print(f"{seed=}")
    random.seed(seed)

    sol = Solution()
    n = 10000
    m = 10000
    nodes = list(range(2, n))

    random.shuffle(nodes)
    front = [1, 1]
    edges: list[list[int]] = []
    while nodes:
        if len(front) < 50:  # or random.randint(1, 10) == 1:
            random.shuffle(front)
        parent = front.pop()
        child = nodes.pop()
        edges.append([child, parent])
        front.append(child)
        front.append(child)

    queries = [[random.randint(1, n - 1), random.randint(1, n - 1)] for _ in range(m)]
    time_taken = timeit.timeit(lambda: sol.assignEdgeWeights(edges, queries), number=1)
    print(f"{time_taken=}")


def large_input_test():
    import json
    import time

    with open("big_input.txt") as f:
        edges = json.loads(f.readline())
        queries = json.loads(f.readline())

    start = time.perf_counter()
    sol = Solution()
    sol.assignEdgeWeights(edges, queries)
    print("took", time.perf_counter() - start, "seconds")
    # print(sol.get_dist_between_nodes.cache_info())


big_test()
test()
