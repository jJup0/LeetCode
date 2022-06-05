from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Given the head of a singly linked list where elements are sorted in ascending order, convert it
    to a height balanced BST.
    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth
    of the two subtrees of every node never differ by more than 1.
    Constraints:
        The number of nodes in head is in the range [0, 2 * 10^4].
        -10^5 <= Node.val <= 10^5
    """

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Construct balanced tree by always splitting list in half.
        """
        if not head:  # if no nodes, return null
            return None
        if not head.next:  # if only one node, return as TreeNode
            return TreeNode(head.val)

        # find node before middle node with slow/fast method and initializing fast to head.next.next
        slow = head
        fast = head.next.next
        while fast and fast.next:
            assert slow  # type hint
            slow = slow.next
            fast = fast.next.next

        assert slow  # type hint

        # keep reference to middle node
        middle = slow.next

        assert middle  # type hint

        # cut of start of list from middle
        slow.next = None

        # initialize tree with middle value
        root = TreeNode(middle.val)

        # construct left children with all values less than middle
        root.left = self.sortedListToBST(head)

        # construct right children with all values greater than middle
        root.right = self.sortedListToBST(middle.next)

        # return constructed tree
        return root
