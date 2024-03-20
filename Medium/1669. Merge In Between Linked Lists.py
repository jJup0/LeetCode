"""
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their
place.

The blue edges and nodes in the following figure indicate the result:

Build the result list and return its head.

Constraints:
- 3 <= list1.length <= 10^4
- 1 <= a <= b < list1.length - 1
- 1 <= list2.length <= 10^4
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x: int, next: "ListNode | None" = None):
            self.val = x
            self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        # navigate to node a-1 in list1
        curr = list1
        for _ in range(a - 1):
            curr = curr.next
            assert curr is not None

        # keep a pointer to the first node to delete
        deleted_node = curr.next
        # update the next node to disconnect the ath node from list1
        curr.next = list2
        # navigate to node b-1 in list1
        for _ in range(b - a):
            assert deleted_node is not None
            deleted_node = deleted_node.next
        assert deleted_node is not None

        # navigate to the last node in list2, note that curr is currently
        # pointing to the parent of the head node of list2
        while curr.next:
            curr = curr.next
        # make the tail of list2 point to node b in list1
        curr.next = deleted_node.next

        # return the head of list1
        return list1
