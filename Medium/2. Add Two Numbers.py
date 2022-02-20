# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = head = ListNode(-1)
        carry = 0
        while l1 or l2:

            thisSum = carry
            if l1:
                thisSum += l1.val
                l1 = l1.next
            if l2:
                thisSum += l2.val
                l2 = l2.next

            carry = thisSum >= 10
            curr.next = curr = ListNode(thisSum % 10)

        if carry:
            curr.next = ListNode(1)
        return head.next


# class Solution(object):
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         dummyHead = ListNode(0)
#         cur = dummyHead
#         carry = 0
#         while l1 or l2:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             carry, res = divmod(val1 + val2 + carry, 10)
#             cur.next = ListNode(res)
#             cur = cur.next  # cur redefined to point to the next item
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         if carry:
#             cur.next = ListNode(carry)
#         # has 'start' of cur stored, cur was redifined earlier, no longer contains start
#         return dummyHead.next


# class altSolution(object):
#     def addTwoNumbers(self, l1, l2):
#         cur = dummyHead = ListNode(0)
#         carry = 0
#         while l1 or l2:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             thissum = val1 + val2 + carry
#             if thissum >= 10:
#                 carry, res = 1, thissum - 10
#             else:
#                 carry, res = 0, thissum
#             cur.next = ListNode(res)
#             cur = cur.next  # cur redefined to point to the next item
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         if carry:
#             cur.next = ListNode(carry)
#         # has 'start' of cur stored, cur was redifined earlier, no longer contains start
#         return dummyHead.next
