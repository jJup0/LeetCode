# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-6000)
        prev = dummy
        node = head
        while node:
            cur = node
            node = node.next
            # only reset prev to dummy, if val is smaller
            if cur.val < prev.val:
                prev = dummy
            # otherwise keep searching where prev left off last time
            while prev.next and cur.val > prev.next.val:
                prev = prev.next
            # prev stores largest node in sorted part, that is smaller than cur.val
            # insert cur into sorted part
            cur.next = prev.next
            prev.next = cur
        return dummy.next