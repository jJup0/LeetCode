from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode" | None = None):
            self.val = val
            self.next = next


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Constraints:
    - The number of nodes in each linked list is in the range [1, 100].
    - 0 <= Node.val <= 9
    - It is guaranteed that the list represents a number that does not have leading zeros.
    """

    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode:
        """
        Applied follow up: did not reverse input lists
        O(n + m) / O(n + m)     time / space complexity
        """
        # convert linked list numbers into integers
        num1 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        # sum them up
        num_sum = num1 + num2

        # construct the sum as a linked list
        result: ListNode | None = None
        while num_sum:
            result = ListNode(num_sum % 10, result)
            num_sum //= 10

        # result is None if both addends are 0, so return 0
        if result is None:
            return ListNode(0)
        return result
