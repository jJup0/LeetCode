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

        # reverse first half of linked list, middle of list found using fast-slow method
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            # rev = slow;       prepares current node to be added to reversed list
            # rev.next = rev;   actually does this
            # slow = slow.next  simple iteration through list
            rev, rev.next, slow = slow, rev, slow.next

        # if list length is uneven, skip to next node
        if fast:
            slow = slow.next

        # check if reversed first half of list is equal to second half of list
        while rev:
            if rev.val != slow.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
