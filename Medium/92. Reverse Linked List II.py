from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode" | None = None):
            self.val = val
            self.next = next


class Solution:
    """
    Given the head of a singly linked list and two integers left and right where
    left <= right, reverse the nodes of the list from position left to position
    right, and return the reversed list.

    Constraints:
    - The number of nodes in the list is n.
    - 1 <= n <= 500
    - -500 <= Node.val <= 500
    - 1 <= left <= right <= n
    """

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # create a dummy node, in case left == 1
        dummy = curr = ListNode(next=head)
        # go to parent node of first node affected by reverse
        for _ in range(left - 1):
            curr = cast(ListNode, curr.next)

        # store point to end of the first unreversed part (append reversed part here later)
        tail_of_in_unreversed = curr
        
        curr = cast(ListNode, curr.next)
        # the first node in the chain of nodes which is to be reversed will be the end of the reversed part
        reversed_tail = curr
        # head of the listnode of reversed part
        reversed_head = None

        # go through all nodes which are to be reversed
        for _ in range(right - left + 1):
            # temporarily store next node
            temp = cast(ListNode, curr.next)
            # build reverse chain
            curr.next = reversed_head
            # set new head of reversed chain
            reversed_head = curr
            # progress to next node in list
            curr = temp

        # append reversed chain back to list
        tail_of_in_unreversed.next = reversed_head
        # append rest of list to reversed list
        reversed_tail.next = curr

        # return head
        return cast(ListNode, dummy.next)
