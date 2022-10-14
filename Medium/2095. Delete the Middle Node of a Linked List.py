from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    """
    You are given the head of a linked list. Delete the middle node, and return the head of the
    modified linked list.

    The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based
    indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

    For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

    Constraints:
        The number of nodes in the list is in the range [1, 10^5].
        1 <= Node.val <= 10^5
    """

    def deleteMiddle(self, head: ListNode) -> Optional[ListNode]:
        """
        O(n) / O(1)     time / space complexity
        """
        
        # if only one node, delete that node
        if not head.next:
            return None

        # use slow/fast method to find middle node
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # delete middle node
        slow.next = slow.next.next
        return head
