from typing import Optional


class ListNode:

    @staticmethod
    def fromList(l):
        dummy = curr = ListNode()
        for x in l:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next

    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional["ListNode"] = next

    def __repr__(self):
        l = []
        head = self
        while head:
            l.append(head.val)
            head = head.next

        return str(l)
