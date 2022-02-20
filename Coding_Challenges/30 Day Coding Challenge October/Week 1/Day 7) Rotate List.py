# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (not head) or (k == 0):
            return head
        end, start = head, head
        i = 0
        while i < k:
            if end == None:
                if not (mod := k % i):
                    return head
                i = k - mod
                end = head.next
            else:
                end = end.next
            i += 1

        if end == None:
            return head

        while end.next:  # move pointers to part that should be moved to front
            start = start.next
            end = end.next

        ret = start.next  # actual rotating part
        start.next = None
        end.next = head
        return ret
