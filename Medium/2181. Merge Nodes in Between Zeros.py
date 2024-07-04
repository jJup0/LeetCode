"""
You are given the head of a linked list, which contains a series of integers
separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a
single node whose value is the sum of all the merged nodes. The modified list
should not contain any 0's.

Return the head of the modified linked list.

Constraints:
- The number of nodes in the list is in the range [3, 2 * 10^5].
- 0 <= Node.val <= 1000
- There are no two consecutive nodes with Node.val == 0.
- The beginning and end of the linked list have Node.val == 0.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x: int, next: "ListNode | None" = None):
            self.val = x
            self.next = next


class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode | None:
        """
        Use existing zero-nodes to store sums, and link them together, excluding the first zero-node.
        O(n) / O(1)     time / space complexity
        """
        prev_0 = head
        curr_node = head.next
        curr_sum = 0
        while curr_node:
            if curr_node.val != 0:
                curr_sum += curr_node.val
            else:
                # set the zero-node's value to the current sum
                curr_node.val = curr_sum
                # link to the previous zero-node
                prev_0.next = curr_node
                # update tail of zero-node list
                prev_0 = curr_node
                # reset running sum
                curr_sum = 0
            curr_node = curr_node.next
        # exclude starting zero node
        return head.next
