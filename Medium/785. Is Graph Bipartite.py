from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Enums for deciding whether a node is in a left/right side of a bipartite graph, or not yet decided
        # LEFT = -1, RIGHT = 1 here, but any non-zero integer and its negative counterpart works
        UNDECIDED = 0

        # constant length list to track which side of a bipartite graph a node is on
        side_of_node = [UNDECIDED] * len(graph)

        # track how many nodes are undecided, needed in case graph is not connected
        nodes_left = set(range(len(graph)))

        # stack of nodes and which side they have to be on
        node_stack: List[int] = []

        while nodes_left:
            # if there are nodes left, but the node stack is empty, it is either the first iteration,
            # or the graph is not connected, so add an unvisited node to the stack
            new_node = nodes_left.pop()
            node_stack.append(new_node)
            side_of_node[new_node] = -1

            # iterate through nodes of connected graph
            while node_stack:
                # get any node from the stack, it has determined side
                node = node_stack.pop()

                # precalculate "opposite" side of current node, all its neighbors will get assigned this side
                # or have to already have it assigned for the graph to be bipartite
                assert side_of_node[node] != UNDECIDED
                opposite = -side_of_node[node]

                # loop through the node's neighbors, assigning them each the side "opposite"
                for adjacent in graph[node]:
                    neighbor_side = side_of_node[adjacent]
                    if neighbor_side == UNDECIDED:
                        # if undecided, assign neighbor opposite side, and append it to node stack
                        side_of_node[adjacent] = opposite
                        node_stack.append(adjacent)
                        nodes_left.remove(adjacent)
                    elif neighbor_side != opposite:
                        return False
        return True
