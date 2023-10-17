class Solution:
    """
    You have n binary tree nodes numbered from 0 to n - 1 where node i has two
    children leftChild[i] and rightChild[i], return true if and only if all the
    given nodes form exactly one valid binary tree.

    If node i has no left child then leftChild[i] will equal -1, similarly for
    the right child.

    Note that the nodes have no values and that we only use the node numbers
    in this problem.

    Constraints:
    - n == leftChild.length == rightChild.length
    - 1 <= n <= 10^4
    - -1 <= leftChild[i], rightChild[i] <= n - 1
    """

    def validateBinaryTreeNodes(
        self, n: int, left_children: list[int], right_children: list[int]
    ) -> bool:
        return self.validateBinaryTreeNodes2(n, left_children, right_children)

    def validateBinaryTreeNodes1(
        self, n: int, left_children: list[int], right_children: list[int]
    ) -> bool:
        """There are 4 ways by which the inputs could result in an invalid binary tree:
        - One node has multiple parents
        - The two children of a node are the same
        - There is more than one root node
        - There is a cycle in the graph

        Check for these properties, if any are true, return false.
        O(n) / O(n)     time / space complexity
        """
        # mapping from nodes to their parent
        nodes_to_parent: list[int] = [-1] * n
        # mapping from nodes to their child count
        child_counts: list[int] = [0] * n
        for node, (left_child, right_child) in enumerate(
            zip(left_children, right_children)
        ):
            for child in (left_child, right_child):
                if child != -1:
                    child_counts[node] += 1
                    if nodes_to_parent[child] != -1:
                        # one node has multiple parents, or parent node
                        # has same node for left and right child
                        return False
                    nodes_to_parent[child] = node

        if nodes_to_parent.count(-1) != 1:
            # more than one root node, i.e. nodes form more than one tree
            return False

        leaf_nodes: list[int] = [
            node for node, child_count in enumerate(child_counts) if child_count == 0
        ]

        # check if acyclic
        visited_count = 0
        while leaf_nodes:
            node = leaf_nodes.pop()
            visited_count += 1
            parent = nodes_to_parent[node]
            if parent != -1:
                child_counts[parent] -= 1
                if child_counts[parent] == 0:
                    leaf_nodes.append(parent)
        return visited_count == n

    def validateBinaryTreeNodes2(
        self, n: int, left_children: list[int], right_children: list[int]
    ) -> bool:
        """
        O(n) / O(n)     time / space complexity
        """
        # find root, should be exactly one
        roots = set(range(n)).difference(left_children).difference(right_children)
        if len(roots) != 1:
            return False

        # visit nodes
        visited = [False] * n
        queue = [roots.pop()]
        while queue:
            curr = queue.pop()

            if visited[curr]:
                # node already visited, i.e. node has two parents
                return False
            visited[curr] = True

            l, r = left_children[curr], right_children[curr]
            if l != -1:
                queue.append(l)
            if r != -1:
                queue.append(r)

        # return true iff all nodes visited
        return all(visited)
