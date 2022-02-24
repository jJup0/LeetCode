from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # node's tail may be longer than l-1
        def merge_sort(node: ListNode, l: int) -> ListNode:

            # to sort a list of length 1 just return it
            # disconnect it from its tail, to truly make it only have one element
            if l == 1:
                node.next = None
                return node

            # get middle node of list
            mid = l >> 1
            right_side = node
            for _ in range(mid):
                right_side = right_side.next

            # sort first and second half of list independently
            left_side = merge_sort(node, mid)
            right_side = merge_sort(right_side, l - mid)
            return merge(left_side, right_side)

        def merge(sorted_left: ListNode, sorted_right: ListNode) -> ListNode:
            # left_side and right_side contain sorted lists with lengths mid and l - mid
            # construct result by merging list, head of res is dummy node, res.next will be returned
            # tail of list pointed to by res_builder
            res_tail = res = ListNode()
            while sorted_left and sorted_right:
                # go element by element of left and right list, appending lower element to res
                if sorted_left.val < sorted_right.val:
                    res_tail.next = sorted_left
                    sorted_left = sorted_left.next
                else:
                    res_tail.next = sorted_right
                    sorted_right = sorted_right.next
                res_tail = res_tail.next

            # once either left or right side is empty (== None), add remaining other list at end
            # in python 'or' returns the first argument which is not falsey
            remaining = sorted_left or sorted_right
            res_tail.next = remaining
            return res.next

        # if there is nothing to sort return None
        if not head:
            return None

        # determine length of list
        dummy = head
        length = 0
        while dummy:
            length += 1
            dummy = dummy.next

        return merge_sort(head, length)
