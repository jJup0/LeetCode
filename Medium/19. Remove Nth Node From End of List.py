# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return
        count = 0
        curNode = head
        savedNode = head
        while curNode.next:
            if count > n-1:
                savedNode = savedNode.next
            curNode = curNode.next
            count += 1
        if count <= n-1:
            return savedNode.next
        else:
            savedNode.next = savedNode.next.next
        return head
