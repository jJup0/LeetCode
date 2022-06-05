# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import random
from typing import Optional

from ListNode import ListNode
from TreeNode import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
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
