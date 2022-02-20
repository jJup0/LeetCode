# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next
        return res


print("MEHRERE INSTRUKTIONEN IN EINER ZEILE BEDEUTET NICHT, DASS ES ATOMAR PASSIERT, ES DIENT NUR ZUR ÜBERSICHT".lower())