# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    """
    Populate each next pointer to point to its next right node.
    If there is no next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.
    Constraints:
        The number of nodes in the tree is in the range [0, 6000].
        -100 <= Node.val <= 100
    """

    def connect(self, root: 'Node') -> 'Node':
        # O(1) space, O(n) time

        # leftmost node at current depth,
        leftmost = root
        while leftmost:
            # assert: leftmost will already have a fully constructed next chain

            # dummy node to construct next chain on
            next_depth_leftmost_dummy = next_depth_curr = Node()

            # go through the fully constructed next-chain of leftmost
            while leftmost:
                # go through children in order
                for child in (leftmost.left, leftmost.right):
                    if child:
                        # this sets left child's next to right child (trivial), and sets next_depth_curr to
                        # its right most child, so that in the next iteration, that child can receive left most
                        # child of the current node's next node
                        next_depth_curr.next = child
                        next_depth_curr = next_depth_curr.next

                # go to next node in next-chain
                leftmost = leftmost.next

            # go to next depth, if there were no children nodes at this depth, next_depth_leftmost_dummy.next
            # will be None and the out loop will break
            leftmost = next_depth_leftmost_dummy.next
        return root

    def connect_O_depth(self, root: 'Node') -> 'Node':
        # O(depth) space, O(n) time

        # vistits node in reverse preorder and assigns "next" nodes
        def helper(node, depth):
            # if node is null, nothing to do
            if not node:
                return
            # if at deepest depth so far, append to leftmost_at_depth list
            if len(leftmost_at_depth) == depth:
                leftmost_at_depth.append(None)

            # set next to most left node visted so far, in reverse pre-order
            node.next = leftmost_at_depth[depth]
            # update leftmost to current node
            leftmost_at_depth[depth] = node

            # visit nodes in right child first, so they get receive an accurate leftmost node first
            helper(node.right, depth + 1)
            # then visit all nodes in left subtree
            helper(node.left, depth + 1)

        # used non locally in helper
        leftmost_at_depth = []

        # traverse through tree by helper function
        helper(root, 0)

        # return edited with updated next nodes
        return root
