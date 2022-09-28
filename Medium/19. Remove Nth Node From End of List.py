# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its
    head.

    Constraints:
        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        One pass using two pointers, one with n steps delay.
        O(len(head)) / O(1)     time / space complexity
        """
        # skip the first n nodes
        curr = head
        for _ in range(n):
            curr = curr.next

        # if n == len(head) then curr == None, and we remove the first element
        if not curr:
            return head.next

        # create a pointer to the predecessor of the node to be removed, this pointer will always
        # point to n nodes to the left of curr, so when curr is pointing to the last node,
        # to_remove_pred will point to the (n+1)th last node
        to_remove_pred = head

        # keep walking down the list until curr is last node in the list
        while curr.next:
            curr = curr.next
            to_remove_pred = to_remove_pred.next

        # remove the nth node
        to_remove_pred.next = to_remove_pred.next.next
        return head
