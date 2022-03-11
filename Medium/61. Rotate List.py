from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next

    def __repr__(self) -> str:
        curr = self
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        return str(l)

    def __str__(self) -> str:
        return self.__repr__()


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case
        if not head:
            return None

        # determine length of list
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        # if rotation by k does nothing then return head
        if (k % length) == 0:
            return head

        # steps to take to reach predecessor of new head node
        steps = length - (k % length) - 1

        # traverse to new head node
        curr = head
        while steps:
            curr = curr.next
            steps -= 1

        # store new head in variable
        new_head = curr.next

        # cut off old previous list from new head
        curr.next = None

        # old tail traverses to old end of list, to append old head to it
        old_tail = new_head
        steps = (k % length) - 1
        while steps:
            old_tail = old_tail.next
            steps -= 1

        # append old head
        old_tail.next = head
        return new_head
