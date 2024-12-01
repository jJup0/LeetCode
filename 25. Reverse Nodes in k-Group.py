"""
Given the head of a linked list, reverse the nodes of the list k at a time, and
return the modified list.

 k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes, in the
end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be
changed.

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val: int = 0, next: "ListNode | None" = None):
            self.val = val
            self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverseKGroup_constant_space(head, k)

    def reverseKGroup_constant_space(self, head: ListNode, k: int) -> ListNode:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        dummy = ListNode(-1, head)
        # tail of already k-group reversed list
        result_tail = dummy

        while True:
            # check if there are k nodes remaining
            assert result_tail
            check_length_node = result_tail.next
            has_k_nodes = True
            for _ in range(k):
                if check_length_node is None:
                    has_k_nodes = False
                    break
                check_length_node = check_length_node.next
            if not has_k_nodes:
                break

            # reverse k group
            tail_of_k = check_length_node
            next_end_of_prev_k = curr_k = result_tail.next
            for _ in range(k):
                assert curr_k
                next_node = curr_k.next
                curr_k.next = tail_of_k
                tail_of_k = curr_k
                curr_k = next_node

            result_tail.next = tail_of_k
            result_tail = next_end_of_prev_k
        assert dummy.next
        return dummy.next

    def reverseKGroup_simple(self, head: ListNode, k: int) -> ListNode:
        """
        Complexity:
            Time: O(n)
            Space: O(k)
        """
        dummy = end_of_current_section = ListNode(-1, head)
        curr = head

        while True:
            # collect k nodes in list
            k_nodes: list[ListNode] = []
            has_k_nodes = True
            for _ in range(k):
                if curr:
                    k_nodes.append(curr)
                    curr = curr.next
                else:
                    has_k_nodes = False
                    break
            if not has_k_nodes:
                # fewer than k nodes remaining in list, nothing to reverse
                break

            # reverse k nodes
            for node in reversed(k_nodes):
                end_of_current_section.next = node
                end_of_current_section = end_of_current_section.next
            # attach next nodes to end of reverse
            end_of_current_section.next = curr

        assert dummy.next  # for type checker
        return dummy.next
