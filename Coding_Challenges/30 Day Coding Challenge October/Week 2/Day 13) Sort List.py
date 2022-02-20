# Definition for singly-linked list.
class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        vals = []
        dummy = head
        while dummy:
            vals.append(dummy.val)
            dummy = dummy.next

        dummy = head
        i = 0
        vals.sort()
        while dummy:
            dummy.val = vals[i]
            dummy = dummy.next
            i += 1
        return head
