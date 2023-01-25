class Solution:
    """
    You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at
    most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n, indicating that there is
    a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then
    edges[i] == -1.

    You are also given two integers node1 and node2.

    Return the index of the node that can be reached from both node1 and node2, such that the
    maximum between the distance from node1 to that node, and from node2 to that node is minimized.
    If there are multiple answers, return the node with the smallest index, and if no possible
    answer exists, return -1.

    Note that edges may contain cycles.

    Constraints:
        n == edges.length
        2 <= n <= 10^5
        -1 <= edges[i] < n
        edges[i] != i
        0 <= node1, node2 < n
    """

    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        O(solution_steps) / O(solution_steps)   time / space complexity
        """
        # extra check for equality needed at start (for this implementation)
        if node1 == node2:
            return node1

        # track nodes visited by each starting node
        visited1 = {node1}
        visited2 = {node2}

        inf = len(edges) + 1
        # result variable, if == inf, then no solution found yet
        res = inf

        #
        while node1 != -1 or node2 != -1:
            # step to next node for both nodes
            next1, next2 = edges[node1], edges[node2]
            # if both are at a node they have visited before, then they are both in a loop
            if next1 in visited1 and next2 in visited2:
                break

            visited1.add(next1)
            visited2.add(next2)

            # if node1 at a node that node 2 has visited, update answer
            if next1 in visited2:
                res = min(res, next1)

            # same for node2
            if next2 in visited1:
                res = min(res, next2)

            # if either node at node which was previously visited by other node, return result node
            if res < inf:
                return res

            # update current node if not equal to -1
            if next1 != -1:
                node1 = next1
            if next2 != -1:
                node2 = next2

        # both stuck in separate loops, or both at dead end
        return -1

    def closestMeetingNode_O_n(self, edges: list[int], node1: int, node2: int) -> int:
        """
        First attempt solution.
        O(n) / O(n)     time / space solution
        """
        inf = len(edges) * 2

        visited1 = [inf] * len(edges)
        visited2 = [inf] * len(edges)

        def dfs(visited, node):
            steps = 0
            while node != -1 and visited[node] == inf:
                visited[node] = steps
                node = edges[node]
                steps += 1

        dfs(visited1, node1)
        dfs(visited2, node2)

        steps, res_node = min((max(s1, s2), i) for i, (s1, s2) in enumerate(zip(visited1, visited2)))
        if steps == inf:
            return -1
        return res_node
