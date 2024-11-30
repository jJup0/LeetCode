"""
You are given a 0-indexed 2D integer array pairs where
pairs[i] = [start_i, end_i]. An arrangement of pairs is valid if for every
index i where 1 <= i < pairs.length, we have end_i-1 == start_i.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid arrangement
of pairs.

Constraints:
- 1 <= pairs.length <= 10^5
- pairs[i].length == 2
- 0 <= start_i, end_i <= 10^9
- start_i != end_i
- No two pairs are exactly the same.
- There exists a valid arrangement of pairs.
"""

import itertools
from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: list[list[int]]) -> list[tuple[int, int]]:
        """
        Find Eularian path using Hierholzer's algorithm.
        Complexity:
            Time: O(m)
            Space: O(m)
        """
        # construct graph
        graph: defaultdict[int, list[int]] = defaultdict(list)
        net_out_degree: dict[int, int] = defaultdict(int)
        for a, b in pairs:
            net_out_degree[a] += 1
            net_out_degree[b] -= 1
            graph[a].append(b)

        start_node = self._get_start_node(graph, net_out_degree)

        # eularian = self.get_eularian_iterative(graph, start_node)
        eularian = self._get_eularian_recursive(graph, [], start_node)

        return list(itertools.pairwise(reversed(eularian)))

    def _get_eularian_recursive(
        self, graph: dict[int, list[int]], eularian: list[int], node: int
    ) -> list[int]:
        """Get nodes in reverse eularian path order.
        Recursive implementation.
        """
        while graph[node]:
            self._get_eularian_recursive(graph, eularian, graph[node].pop())
        eularian.append(node)
        return eularian

    def _get_eularian_iterative(
        self, graph: dict[int, list[int]], start_node: int
    ) -> list[int]:
        """Get nodes in reverse eularian path order.
        Iterative implementation.
        """
        # current stack of visited nodes with outgoing edges remaining
        curr_path: list[int] = [start_node]
        # nodes in reverse order of eularian path
        eularian: list[int] = []
        curr_node = start_node
        while curr_path:
            if graph[curr_node]:
                curr_path.append(curr_node)
                next_v = graph[curr_node].pop()
                curr_node = next_v
            else:
                eularian.append(curr_node)
                curr_node = curr_path.pop()
        return eularian

    def _get_start_node(
        self, graph: dict[int, list[int]], net_degree: dict[int, int]
    ) -> int:
        """
        Find a source node if it exists, else return a random node.
        Complexity:
            Time: O(m)
            Space: O(m)
        """
        source = sink = -1
        for val, diff in net_degree.items():
            if diff % 2:
                if diff > 0:
                    source = val
                else:
                    sink = val

        if source == -1:
            # graph is strongly connected, choose any node to start
            start_node = next(iter(graph))
        else:
            # make sink is in adjacency graph
            if sink not in graph:
                graph[sink] = []
            start_node = source
        return start_node
