"""
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode | None" = None):
            self.val = val
            self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode | None:
        return self.removeNthFromEnd_get_length(head, n)

    def removeNthFromEnd_get_length(self, head: ListNode, n: int) -> ListNode | None:
        """
        O(len(head)) / O(1)     time / space complexity
        """
        # find length of linked list
        list_len = 0
        curr = head
        while curr:
            curr = curr.next
            list_len += 1

        # special case
        if list_len == 1:
            return None

        dummy_head = ListNode(0, head)
        # navigate to parent of node to delete
        steps_to_take = list_len - n
        curr = dummy_head
        for _ in range(steps_to_take):
            curr = curr.next
            assert curr is not None

        # delete node
        assert curr.next is not None
        curr.next = curr.next.next
        return dummy_head.next

    def removeNthFromEnd_one_pass(self, head: ListNode, n: int) -> ListNode | None:
        """
        One pass using two pointers, one with n steps delay.
        O(len(head)) / O(1)     time / space complexity
        """
        # skip the first n nodes
        curr = head
        for _ in range(n):
            assert curr is not None
            curr = curr.next

        # if n == len(head) then curr == None, and we remove the first element
        if not curr:
            return head.next

        # create a pointer to the predecessor of the node to be removed, this pointer will always
        # point to n nodes to the left of curr, so when curr is pointing to the last node,
        # to_remove_pred will point to the (n+1)th last node
        to_remove_pred = head

        # keep walking down the list until curr is last node in the list
        while curr.next:
            curr = curr.next
            to_remove_pred = to_remove_pred.next
            assert to_remove_pred is not None

        assert to_remove_pred.next is not None
        # remove the nth node
        to_remove_pred.next = to_remove_pred.next.next
        return head
