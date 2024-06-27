"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A
star graph is a graph where there is one center node and exactly n - 1 edges
that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [u_i, v_i]
indicates that there is an edge between the nodes u_i and v_i. Return the
center of the given star graph.

Constraints:
- 3 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 1 <= u_i, v_i <= n
- u_i!= v_i
- The given edges represent a valid star graph.
"""


class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        a, b = edges[0]
        if a in edges[1]:
            return a
        return b
