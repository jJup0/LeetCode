from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode" | None = None):
            self.val = val
            self.next = next


class Solution:
    """
    In a linked list of size n, where n is even, the ith node (0-indexed) of the linked
    list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of
    node 2. These are the only nodes with twins for n = 4.
    The twin sum is defined as the sum of a node and its twin.

    Given the head of a linked list with even length, return the maximum twin sum
    of the linked list.
    """

    def pairSum(self, head: ListNode) -> int:
        """O(n) / O(1)  time / space complexity"""
        # find middle
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # iterate through first half zipped with reversed second half
        # and find max pair sum
        head1 = head
        head2 = prev
        res = 0
        while head2:
            res = max(res, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next
        return res
