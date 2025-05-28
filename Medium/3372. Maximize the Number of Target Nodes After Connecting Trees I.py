"""
There exist two undirected trees with n and m nodes, with distinct labels in
ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and
m - 1, respectively, where edges1[i] = [a_i, b_i] indicates that there is an
edge between nodes a_i and b_i in the first tree and edges2[i] = [u_i, v_i]
indicates that there is an edge between nodes u_i and v_i in the second tree.
You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is
less than or equal to k. Note that a node is alwaystarget to itself.

Return an array of n integers answer, where answer[i] is the maximum possible
number of nodes target to node i of the first tree if you have to connect one
node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you
will remove the added edge before proceeding to the next query.

Constraints:
- 2 <= n, m <= 1000
- edges1.length == n - 1
- edges2.length == m - 1
- edges1[i].length == edges2[i].length == 2
- edges1[i] = [a_i, b_i]
- 0 <= a_i, b_i < n
- edges2[i] = [u_i, v_i]
- 0 <= u_i, v_i < m
- The input is generated such that edges1 and edges2 represent valid trees.
- 0 <= k <= 1000
"""


class Solution:
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]:
        """
        Find node with largest target for k-1 in second tree, always add that node to
        each node in the first tree when calculating max target.

        Note that _get_target_nodes() can be optimized to len(edges) * k with memoization,
        by defining a tree root and storing target node count for 0 <= j <= k for each node
        for its children only. Then find total target node count but going up x edges in
        the graph and summing the children `k-x`-target-count of its cousins.

        Complexity:
            Time: O(n^2 + m^2)
            Space: O(n + m)
        """
        if k == 0:
            return [1] * (len(edges1) + 1)
        adj_list1 = self._gen_adj_list(edges1)
        adj_list2 = self._gen_adj_list(edges2)
        reachable_in_tree2 = max(
            self._get_target_nodes(node, adj_list2, k - 1)
            for node in range(len(adj_list2))
        )
        return [
            self._get_target_nodes(node, adj_list1, k) + reachable_in_tree2
            for node in range(len(adj_list1))
        ]

    def _gen_adj_list(self, edges: list[list[int]]) -> list[list[int]]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        adj_list: list[list[int]] = [[] for _ in range(len(edges) + 1)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        return adj_list

    def _get_target_nodes(self, node: int, adj_list: list[list[int]], k: int) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        n = len(adj_list)
        visited = [False] * n
        visited[node] = True
        visited_count = 1
        rounds_remaining = k
        front = [node]
        while front and rounds_remaining:
            new_front: list[int] = []
            for _node in front:
                for neighbor in adj_list[_node]:
                    if visited[neighbor]:
                        continue
                    new_front.append(neighbor)
                    visited_count += 1
                    visited[neighbor] = True
            front = new_front
            rounds_remaining -= 1
        return visited_count


def test():
    sol = Solution()
    res = sol.maxTargetNodes(
        [[0, 1], [0, 2], [2, 3], [2, 4]],
        [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
        2,
    )
    assert res == [9, 7, 9, 8, 8]


test()
