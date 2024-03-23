"""
You are given the head of a singly linked-list. The list can be represented as:

Reorder the list to be on the following form:

You may not modify the values in the list's nodes. Only nodes themselves may be
changed.

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode | None" = None):
            self.val = val
            self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        One pass, constant space.
        O(n) / O(1)     time / space complexity
        """
        if not head.next or not head.next.next:
            return

        # reverse first half of linked list, middle of list found using fast-slow method
        prev = None
        slow = fast = head
        while fast and fast.next:
            assert slow is not None  # for type checker
            fast = fast.next.next
            next_slow = slow.next
            slow.next = prev  # point to previous node
            prev = slow  # update prev
            slow = next_slow  # update slow

        # if list length is uneven, make the middel node the tail
        if fast:
            assert slow is not None  # for type checker
            tail = slow
            slow = slow.next  # move slow pointer to next node
            tail.next = None  # remove next pointer to avoid cycle
        else:
            tail = None

        # zip the two halves together, "building" the zipped list from the tail
        while slow and prev:
            # add on node from second half
            next_slow = slow.next
            slow.next = tail
            tail = slow
            # move to next node
            slow = next_slow

            # add on node from (reversed) first half
            next_prev = prev.next
            prev.next = tail
            tail = prev
            # move to next node
            prev = next_prev
