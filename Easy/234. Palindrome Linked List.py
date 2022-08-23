from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """
    Given the head of a singly linked list, return true if it is a palindrome.
    Constraints:
        The number of nodes in the list is in the range [1, 10^5].
        0 <= Node.val <= 9
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        O(n) / O(1)     time / space complexity
        """
        
        # find middle using fast-slow method
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse linked list starting from middle node, stored in slow
        prev = None
        while slow.next:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        slow.next = prev

        # iterate through nodes from both ends of the linked list (head and slow)
        dummy = head
        while slow:
            if dummy.val != slow.val:
                return False
            dummy = dummy.next
            slow = slow.next

        return True
