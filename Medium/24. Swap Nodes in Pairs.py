# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(self, head: ListNode) -> ListNode:
    i = head
    j = head = head.next
    preivousSecond = ListNode(None)
    while j:
        i.next = j.next
        j.next = i
        if preivousSecond:
            preivousSecond.next = i
        preivousSecond = i
        i = i.next
        j = j.next.next
    return head


