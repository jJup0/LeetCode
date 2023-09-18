from collections import deque


class Solution:
    """
    You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
    You are given an array graph where graph[i] is a list of all the nodes
    connected with node i by an edge.

    Return the length of the shortest path that visits every node. You may start
    and stop at any node, you may revisit nodes multiple times, and you may reuse
    edges.

    Constraints:
    - n == graph.length
    - 1 <= n <= 12
    - 0 <= graph[i].length < n
    - graph[i] does not contain i.
    - If graph[a] contains b, then graph[b] contains a.
    - The input graph is always connected.
    """

    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            # special case: graph is a single node
            return 0

        # shortest path will start at a source, if there are some,
        # no need to check all nodes for starting node
        sources: list[int] = []
        for node, neighbors in enumerate(graph):
            if len(neighbors) == 1:
                sources.append(node)
        if len(sources) == 0:
            sources = list(range(n))

        # bitmap of all visited nodes
        all_visited_bitmap = (1 << n) - 1
        # mapping of visited node bitmap and current node to best crossings so far
        # should never need more than 2n-1 steps to visit all nodes
        visited: set[tuple[int, int]] = set()

        # queue[i] = [edge_count, bitmap_visited, curr_node]
        queue: deque[tuple[int, int, int]] = deque(
            (0, 1 << node, node) for node in sources
        )
        # find shortest path via BFS
        while queue:
            edge_count, bitmap_visited, curr_node = queue.popleft()

            # check if shorter path has been reached found with same nodes visited at current node
            bitmap_currnode_tuple = (bitmap_visited, curr_node)
            if bitmap_currnode_tuple in visited:
                continue
            visited.add(bitmap_currnode_tuple)

            # add path to neighbors to BFS queue
            next_edge_count = edge_count + 1
            for neighbor in graph[curr_node]:
                # update bitmap
                new_bitmap_visited = bitmap_visited | (1 << neighbor)
                if new_bitmap_visited == all_visited_bitmap:
                    # return if path found with all nodes visited
                    return next_edge_count

                queue.append((next_edge_count, new_bitmap_visited, neighbor))

        # input guarantees that graph is connected, so should always find a path
        assert False
