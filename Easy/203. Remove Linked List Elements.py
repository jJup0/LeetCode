# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        curNode, prevNode = head, None
        while curNode:
            if curNode.val == val:
                prevNode.next = curNode.next
            else:
                prevNode = curNode
            curNode = curNode.next
        return head
