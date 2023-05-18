from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode" | None = None):
            self.val = val
            self.next = next


class Solution:
    """
    Given a linked list, swap every two adjacent nodes and return its head. You must
    solve the problem without modifying the values in the list's nodes (i.e., only
    nodes themselves may be changed.)

    Constraints:
        The number of nodes in the list is in the range [0, 100].
        0 <= Node.val <= 100
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        def swap_pair(node_before: ListNode):
            first = node_before.next
            if not first:
                return False
            second = first.next
            if not second:
                return False
            after = second.next

            node_before.next = second
            second.next = first
            first.next = after
            return True

        # Step 1: traverse to node before every unswapped pair.
        # Step 2: swap.
        # Step 3: go to step 1, if there are nodes left.
        curr = dummy = ListNode(-1, head)
        while True:
            swap_res = swap_pair(curr)
            if not swap_res:
                break
            curr = curr.next.next

        return dummy.next
