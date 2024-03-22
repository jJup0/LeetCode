"""
Given the head of a singly linked list, return true if it is a palindrome or
false otherwise.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x: int, next: "ListNode | None" = None):
            self.val = x
            self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        """
        O(n) / O(1)     time / space complexity
        """

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

        # if list length is uneven, skip to next node
        if fast:
            assert slow is not None  # for type checker
            slow = slow.next

        # check if reversed first half of list is equal to second half of list
        # prev currently points to the head of the reversed first half of the list
        while prev:
            assert slow is not None  # for type checker
            if prev.val != slow.val:
                return False
            slow = slow.next
            prev = prev.next
        return True
