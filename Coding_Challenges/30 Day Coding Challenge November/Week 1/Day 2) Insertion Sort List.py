#!!! NOT ACTUALLY SOLUTION, BUILT IN sort() USED

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def build(i):
            if i == len(stack):
                return
            return ListNode(stack[i], build(i+1))

        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        stack.sort()
        return build(0)
