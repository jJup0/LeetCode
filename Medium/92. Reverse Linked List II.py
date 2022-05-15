from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # create a dummy node, in case left == 1
        dummy = curr = ListNode(next=head)
        # go to parent node of first node affected by reverse
        for _ in range(left-1):
            curr = curr.next

        # mark end of the unreversed part (append reversed part here later)
        tail_of_in_unreversed = curr
        # go one node forward, and cut off unreversed part from soon to be reversed part
        curr = curr.next
        tail_of_in_unreversed.next = None
        # the first node in the chain of nodes which is to be reversed will be the end of the reversed part
        reversed_tail = curr
        # head of the listnode of reversed part
        reversed_head = None

        # go through all nodes which are to be reversed
        for _ in range(right-left+1):
            # temporarily store next node
            temp = curr.next
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

        # return head if left > 1, else new head of list
        return dummy.next
