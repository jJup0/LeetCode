# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # use two pointers, slow which progresses by one step each time, fast by two
        # this way if there is a cycle in a list of length n, it will take a maximum of n 
        # n steps for the fast node to complete the cycle and catch back up to slow
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # this can only ever be true in a graph with a cycle
            if fast == slow:
                return True
        # if fast ever reaches a point where there is no next node, there can be no cycle
        return False