# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # more practical to use dummy than head
        curr = dummy = ListNode(-1)

        digit_sum = 0
        while l1 or l2:
            # either might be None
            if l1:
                digit_sum += l1.val
                l1 = l1.next
            if l2:
                digit_sum += l2.val
                l2 = l2.next

            # add digit sum to result list
            curr.next = ListNode(digit_sum % 10)

            # set digit sum to 0 or 1 depending on the need to "carry the one"
            digit_sum = (digit_sum >= 10)

            curr = curr.next

        # if last addition has overflow, account for this
        if digit_sum:
            curr.next = ListNode(1)

        return dummy.next
