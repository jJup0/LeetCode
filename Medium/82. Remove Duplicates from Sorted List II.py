from typing import Optional,


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in case starting nodes get deleted, need dummy
        # prev contains last node in the list check so far, that has no duplicates
        prev = dummy = ListNode(next=head)
        curr = head
        # need at least two remaining nodes to have duplicate
        while curr and curr.next:
            # duplicate sublist found starting at node curr
            if curr.val == curr.next.val:
                # go through list until at last node in list, or list values differ
                while curr and curr.next:
                    if curr.val != curr.next.val:
                        break
                    curr = curr.next
                # curr is the last node with the same value as the original curr
                # "delete" all nodes upto curr by setting prev.next as curr.next
                prev.next = curr.next
            else:
                # only assign new next if no duplicate, as in the other branch curr.next
                # could also be a duplicate entry
                prev = curr
            # make progress down the list
            curr = curr.next

        return dummy.next
