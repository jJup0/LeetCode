"""
There is an undirected tree with n nodes labeled from 1 to n, rooted at node 1.
The tree is represented by a 2D integer array edges of length n - 1, where
edges[i] = [u_i, v_i] indicates that there is an edge between nodes u_i and v_i.

Initially, all edges have a weight of 0. You must assign each edge a weight of
either 1 or 2.

The cost of a path between any two nodes u and v is the total weight of all
edges in the path connecting them.

Select any one node x at the maximum depth. Return the number of ways to assign
edge weights in the path from node 1 to x such that its total cost is odd.

Since the answer may be large, return it modulo 10^9 + 7.

Note: Ignore all edges not in the path from node 1 to x.

Constraints:
- 2 <= n <= 10^5
- edges.length == n - 1
- edges[i] == [u_i, v_i]
- 1 <= u_i, v_i <= n
- edges represents a valid tree.
"""


class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        """Result is simply 2 ** (longest_path-1)

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        adj_list = self._gen_adj_list(edges)
        longest_path = self._get_longest_path(adj_list)
        # way to assign weights to make odd is all ways to assign, divided by 2
        return pow(2, longest_path - 1, 10**9 + 7)

    def _gen_adj_list(self, edges: list[list[int]]):
        n = len(edges) + 1
        adj_list: list[list[int]] = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        return adj_list

    def _get_longest_path(self, adj_list: list[list[int]]):
        n = len(adj_list)
        visited = [False] * (n + 1)
        front = [1]
        depth = 0
        while front:
            new_front: list[int] = []
            for node in front:
                visited[node] = True
                for neighbor in adj_list[node]:
                    if visited[neighbor]:
                        continue
                    new_front.append(neighbor)
            front = new_front
            depth += 1
        return depth - 1


def test():
    s = Solution()
    res = s.assignEdgeWeights([[1, 2]])
    real = 1
    assert res == real, res
    res = s.assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]])
    real = 2
    assert res == real, res


test()
