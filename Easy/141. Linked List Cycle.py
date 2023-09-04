from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, x: int):
            self.val = x
            self.next = None


class Solution:
    """
    Given head, the head of a linked list, determine if the linked list has a
    cycle in it.

    There is a cycle in a linked list if there is some node in the list that can
    be reached again by continuously following the next pointer. Internally, pos
    is used to denote the index of the node that tail's next pointer is connected
    to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    Constraints:
    - The number of the nodes in the list is in the range [0, 10^4].
    - -10^5 <= Node.val <= 10^5
    - pos is -1 or a valid index in the linked-list.


    Follow up: Can you solve it using O(1) (i.e. constant) memory?
    """

    def hasCycle(self, head: ListNode) -> bool:
        """
        Slow/fast method.
        O(n) / O(1)     time / space complexity
        """
        # use two pointers, slow which progresses by one step each time, fast by two
        # this way if there is a cycle in a list of length n, it will take a maximum of n
        # n steps for the fast node to complete the cycle and catch back up to slow
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # type: ignore # slow is not None
            fast = fast.next.next
            # this can only ever be true in a graph with a cycle
            if fast == slow:
                return True
        # if fast ever reaches a point where there is no next node, there can be no cycle
        return False
