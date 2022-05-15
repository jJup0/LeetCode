from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    """
    Given the head of a linked list and a value x, partition it such that all nodes
    ess than x come before nodes greater than or equal to x.
    You should preserve the original relative order of the nodes in each of the two partitions.
    Constraints:
        The number of nodes in the list is in the range [0, 200].
        -100 <= Node.val <= 100
        -200 <= x <= 200
    """

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # create a less than/greater than pointer and dummy node
        less_than = less_than_dummy = ListNode()
        greater_than = greater_than_dummy = ListNode()
        # iterate through list adding node with smaller values to the less than list,
        # and nodes with greater equal values to the greater than list
        while head:
            if head.val < x:
                less_than.next = head
                less_than = less_than.next
            else:
                greater_than.next = head
                greater_than = greater_than.next

            head = head.next

        # append the start of the greater than list to the end of the less than list
        less_than.next = greater_than_dummy.next
        # set the end of the greater than list to None to avoid loops, incase last node in original list
        # does not have a value greater than x
        greater_than.next = None

        # return the start of the less than list (has greater than list appended)
        return less_than_dummy.next
