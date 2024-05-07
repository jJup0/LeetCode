"""
You are given the head of a non-empty linked list representing a non-negative
integer without leading zeroes.

Return the head of the linked list after doubling it.

Constraints:
- The number of nodes in the list is in the range [1, 10^4]
- 0 <= Node.val <= 9
- The input is generated such that the list represents a number that does not
  have leading zeros, except the number 0 itself.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode | None" = None):
            self.val = val
            self.next = next


class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        """
        Big int solution would also work, but does not scale well.
        O(n) / O(n)     time / space complexity
        """
        as_list: list[int] = []

        # as_int = 0
        curr = head
        while curr:
            as_list.append(curr.val)
            curr = curr.next

        carry = 0
        for i in range(len(as_list) - 1, -1, -1):
            num = as_list[i]
            res_digit = num * 2 + carry
            if res_digit >= 10:
                carry = 1
                res_digit -= 10
            else:
                carry = 0
            as_list[i] = res_digit

        curr = head
        if carry:
            # prepend 1 if carry is set
            head = ListNode(1, head)

        for d in as_list:
            assert curr
            curr.val = d
            curr = curr.next
        return head
