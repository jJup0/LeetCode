"""
A critical point in a linked list is defined as either a local maxima or a
local minima.

A node is a local maxima if the current node has a value strictly greater than
the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than
the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a
previous node and a next node.

Given a linked list head, return an array of length 2 containing
[minDistance, maxDistance] where minDistance is the minimum distance between
any two distinct critical points and maxDistance is the maximum distance
between any two distinct critical points. If there are fewer than two critical
points, return [-1, -1].

Constraints:
- The number of nodes in the list is in the range [2, 10^5].
- 1 <= Node.val <= 10^5
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode |None" = None):
            self.val = val
            self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        """
        O(n) / O(1)     time / space complexity
        """
        # minimum distance between critical nodes encountered so far
        min_dist = 1_000_000
        # index of first and last encountered critical node, initialize with
        # 0 as this index is impossible and means no critical node encountered yet
        first_critical = last_critical = 0
        # index of current node
        curr_node_idx = 0
        # value of previous node
        prev_node_val = head.val
        while head.next:
            curr_val = head.val
            next_val = head.next.val
            if (curr_val > prev_node_val and curr_val > next_val) or (
                curr_val < prev_node_val and curr_val < next_val
            ):
                # node is critical
                if last_critical:
                    # at least second critical node encountered, update min_dist
                    min_dist = min(min_dist, curr_node_idx - last_critical)
                else:
                    # first crictical node encountered
                    first_critical = curr_node_idx
                last_critical = curr_node_idx

            # update prev_val and move to next node
            prev_node_val = curr_val
            head = head.next
            curr_node_idx += 1

        if first_critical != last_critical:
            # at least two critical nodes encountered
            return [min_dist, last_critical - first_critical]
        return [-1, -1]
