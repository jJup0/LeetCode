# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not(head):
            return head
        end = head
        llen=1
        while end.next:
            end = end.next
            llen += 1
        evenN = False
        cur = head
        prev = head
        loops = 0
        while cur.next and loops <llen:
            loops += 1
            if evenN:
                prev.next = cur.next
                end.next = cur
                cur = prev
                end = end.next
                end.next = None
            evenN = not(evenN)
            prev = cur
            cur = cur.next
        end.next = None
        return head
    
class O_n_SpaceSolution:
    def oddEvenList(self, head):
        oddhead = odd = ListNode(0)
        evenhead = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = evenhead.next
        return oddhead.next