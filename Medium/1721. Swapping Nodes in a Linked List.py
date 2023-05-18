from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode" | None = None):
            self.val = val
            self.next = next


class Solution:
    """
    You are given the head of a linked list, and an integer k.

    Return the head of the linked list after swapping the values of the kth node
    from the beginning and the kth node from the end (the list is 1-indexed).

    Constraints:
        The number of nodes in the list is n.
        1 <= k <= n <= 10^5
        0 <= Node.val <= 100
    """

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """O(n) / O(1)  time / space complexity"""
        # find kth node
        kth = head
        for _ in range(k - 1):
            kth = kth.next

        # find kth from end node
        tail = kth
        minus_kth = head
        while tail.next:
            tail = tail.next
            minus_kth = minus_kth.next

        # switch values
        kth.val, minus_kth.val = minus_kth.val, kth.val
        return head
