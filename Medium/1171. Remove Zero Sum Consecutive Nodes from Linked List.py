"""
Given the head of a linked list, we repeatedly delete consecutive sequences of
nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list. You may return any
such answer.

Constraints:
- The given linked list will contain between 1 and 1000 nodes.
- Each node in the linked list has -1000 <= node.val <= 1000.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode | None" = None):
            self.val = val
            self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode | None:
        """
        O(n) / O(n)     time / space complexity
        """
        # create dummy node so that head can also be removed from list
        curr = dummy = ListNode(0, head)
        # keep a mapping of cumulative sum to list node
        cumulative_sums: dict[int, ListNode] = {}
        curr_cumulative_sum = 0
        while curr:
            # update current cumulative sum
            curr_cumulative_sum += curr.val
            if curr_cumulative_sum in cumulative_sums:
                # if current cumulative sum previously seen,
                # then all nodes between that node and curr sum up to 0

                prev_node_with_cumulative_sum = cumulative_sums[curr_cumulative_sum]

                # remove all cumulative sums mappings of nodes which are about to be deleted
                temp = prev_node_with_cumulative_sum.next
                temp_sum = curr_cumulative_sum
                while temp is not curr:
                    assert temp is not None
                    temp_sum += temp.val
                    del cumulative_sums[temp_sum]
                    temp = temp.next

                # "delete" nodes between including curr
                prev_node_with_cumulative_sum.next = curr.next
            else:
                cumulative_sums[curr_cumulative_sum] = curr

            # traverse to next node
            curr = curr.next

        # return "head" of linked list, may be None
        return dummy.next
