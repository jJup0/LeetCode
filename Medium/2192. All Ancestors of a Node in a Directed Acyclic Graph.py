"""
You are given a positive integer n representing the number of nodes of a
Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [from_i, to_i]
denotes that there is a unidirectional edge from from_i to to_i in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node,
sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.

Constraints:
- 1 <= n <= 1000
- 0 <= edges.length <= min(2000, n * (n - 1) / 2)
- edges[i].length == 2
- 0 <= from_i, to_i <= n - 1
- from_i!= to_i
- There are no duplicate edges.
- The graph is directed and acyclic.
"""


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        O(n^2 * log(n)) / O(n)      time / space complexity
        """
        # use `edges` to construct lists mapping node number
        # to its ancestors, children and ancestor count
        ancestors: list[list[int]] = [[] for _ in range(n)]
        children: list[list[int]] = [[] for _ in range(n)]
        ancestor_count = [0] * n
        for a, b in edges:
            ancestors[b].append(a)
            children[a].append(b)
            ancestor_count[b] += 1

        # stack for processing nodes in DAG order
        sources = [i for i, ans_count in enumerate(ancestor_count) if not ans_count]
        while sources:
            node = sources.pop()
            # get all ancestors of current node by getting ancestors of its parents
            node_ancestors = set(ancestors[node])
            for ancestor in ancestors[node]:
                node_ancestors.update(ancestors[ancestor])
            ancestors[node] = sorted(node_ancestors)

            # push children to stack if they have no more unprocessed parents
            for child in children[node]:
                ancestor_count[child] -= 1
                if ancestor_count[child] == 0:
                    sources.append(child)

        return ancestors
