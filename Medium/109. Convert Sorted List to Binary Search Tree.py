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
from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Only determines length of list, then calls helper method
        O(n * log(n)) / O(log(n))    time / auxiliary space complexity
        """
        # find out length of list
        length = 0
        len_node = head
        while len_node:
            len_node = len_node.next
            length += 1

        return self._sorted_list_length_to_BST(head, length)

    def _sorted_list_length_to_BST(self, list_root: Optional[ListNode], length: int):
        """Recursively splits list in half to generate tree child nodes.
        O(n * log(n)) / O(log(n))   time / auxiliary space complexity
        """
        # Base cases: if list is empty return None,
        # is list has one element return TreeNode with its value
        if length == 0:
            return None
        if length == 1:
            return TreeNode(list_root.val)

        # traverse to middle node
        half_len = length // 2
        middle_node = list_root
        for _ in range(half_len):
            middle_node = middle_node.next

        # generate left and right child trees
        # left child is created from list[:mid], right child from list[mid+1:]
        left_child = self._sorted_list_length_to_BST(list_root, half_len)
        right_child = self._sorted_list_length_to_BST(middle_node.next, length - half_len - 1)
        return TreeNode(middle_node.val, left_child, right_child)
