from typing import List
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        #find middle node
        slow,fast=head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse 2nd half of list
        prev=None
        curr = slow
        
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        
        #merge 2nd half with 1st half
        first,second = head,prev
        while second.next:          #insort node from second half between two first 
            first.next, first = second, first.next
            second.next, second = first, second.next 
            