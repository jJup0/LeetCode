from collections import defaultdict


class Solution:
    """
    Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples
    in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum
    time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and
    coming back to this vertex.

    The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means
    that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array
    hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not
    have any apple.

    Constraints:
        1 <= n <= 10^5
        edges.length == n - 1
        edges[i].length == 2
        0 <= a_i < b_i <= n - 1
        from_i < to_i
        hasApple.length == n
    """

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        # make edge-lookup more efficient
        e = [[] for _ in range(n)]
        for a, b in edges:
            e[a].append(b)
            e[b].append(a)

        # returns the amount of nodes needed to visit to collect all apples
        def dfs(node: int, visited: set[int]):
            # mark current node as visited
            visited.add(node)
            # dfs to all neighbors, summing up nodes needed
            nodes_needed = sum(dfs(neighbor, visited)
                               for neighbor in e[node]
                               if neighbor not in visited)

            # if the current node needs to be visited because one of its children
            # has an apple, or it has an apple itself, add 1
            if (nodes_needed or hasApple[node]):
                nodes_needed += 1

            return nodes_needed

        # steps required is nodes needed to (visit-1)*2, and 0 if no apples are on the tree
        return max(0, (dfs(0, set()) - 1) * 2)
